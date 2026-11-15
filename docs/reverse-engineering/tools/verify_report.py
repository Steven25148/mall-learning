from pathlib import Path
import json,re,hashlib
ROOT=Path('D:/project'); OUT=ROOT/'docs/reverse-engineering'
apis=json.loads((OUT/'api-inventory.json').read_text(encoding='utf-8'))
tables=json.loads((OUT/'database-inventory.json').read_text(encoding='utf-8'))
reqs=json.loads((OUT/'requirements-inventory.json').read_text(encoding='utf-8'))
summary=json.loads((OUT/'inventory-summary.json').read_text(encoding='utf-8'))
errors=[]; checks=[]
def check(name,value):
    checks.append({'name':name,'pass':bool(value)})
    if not value:errors.append(name)

# Independent mapping-marker count, distinct from method extraction.
count=0
for p in (ROOT/'mall').glob('*/src/main/java/**/controller/*.java'):
    s=p.read_text(encoding='utf-8-sig'); s=re.sub(r'/\*[\s\S]*?\*/|//[^\n]*','',s)
    c=re.search(r'public\s+class\s+\w+',s)
    if c:count+=len(re.findall(r'@(Request|Get|Post|Put|Delete|Patch)Mapping\b',s[c.end():]))
check('Controller方法映射标记数量与API清单一致',count==len(apis)==246)
check('全部45个业务Controller被需求覆盖',{r['controller'] for r in reqs}=={a['controller'] for a in apis if a['module']!='mall-demo'})
check('需求ID唯一',len({r['id'] for r in reqs})==len(reqs))
sql=(ROOT/'mall/document/sql/mall.sql').read_text(encoding='utf-8-sig')
check('76张DDL表全部进入数据字典',set(re.findall(r'CREATE TABLE `([^`]+)`',sql))=={t['name'] for t in tables} and len(tables)==76)
check('数据库索引记录没有遗漏',sum(len(t['indices']) for t in tables)==len(re.findall(r'^\s*(?:PRIMARY KEY|UNIQUE INDEX|INDEX|KEY|CONSTRAINT|FOREIGN KEY)\b',sql,re.M)))
check('主源码事务注解数量与事务索引一致',sum(len(re.findall(r'@Transactional\b',p.read_text(encoding='utf-8-sig'))) for p in (ROOT/'mall').glob('*/src/main/java/**/*.java'))==summary['transaction_declarations'])
body=(OUT/'项目需求与架构设计说明书.md').read_text(encoding='utf-8')
check('正文23章完整且顺序一致',[int(x) for x in re.findall(r'^## (\d+)\.',body,re.M)]==list(range(1,24)))
check('正文证据引用已经解析',not re.search(r'\[\[[a-z]+:',body))
link_count=0; broken=[]
for p in OUT.glob('*.md'):
    s=p.read_text(encoding='utf-8')
    check(p.name+'代码围栏成对',len(re.findall(r'^```',s,re.M))%2==0)
    for target in re.findall(r'\]\((D:/[^)\n]+)\)',s):
        link_count+=1
        m=re.match(r'(.+?)(?::(\d+))?$',target); file=Path(m[1]); line=int(m[2] or 1)
        if not file.is_file():broken.append(target)
        elif line>len(file.read_text(encoding='utf-8-sig').splitlines()):broken.append(target)
check('本地证据/文档链接存在且行号未越界',not broken)
manifest=json.loads((OUT/'source-manifest.json').read_text(encoding='utf-8'))
changed=[a['file'] for a in manifest if hashlib.sha256((ROOT/a['file']).read_bytes()).hexdigest()!=a['sha256']]
check('提取后源文件指纹未变化',not changed)

# Cross-reference DDL tables to the explicitly authored functional groups.
p=OUT/'附录B-数据库完整字典.md'; text=p.read_text(encoding='utf-8')
if '## 业务使用范围索引' not in text:
    rows=['## 业务使用范围索引','','【已确认事实】DDL中的表存在；下表“需求”是本次追踪到的功能簇。空缺表示未纳入已确认业务链，不能凭生成Model/Mapper认定相应产品功能已完成。','', '| 表 | 对应已追踪需求 |','| --- | --- |']
    for t in tables:
        use=[r['id'] for r in reqs if re.search(r'\b'+re.escape(t['name'])+r'\b',r['tables'])]
        rows.append('| '+t['name']+' | '+('、'.join(use) if use else '当前已追踪功能中未确认；保留DDL/生成访问代码证据')+' |')
    text=text.replace('## cms_help', '\n'.join(rows)+'\n\n## cms_help',1)
    p.write_text(text,encoding='utf-8')
result={'scope':'文档结构/覆盖/引用检查，不是业务运行验收','api_mapping_methods':len(apis),'business_api_methods':sum(a['module']!='mall-demo' for a in apis),'sql_tables':len(tables),'business_requirements':len(reqs),'evidence_links_checked':link_count,'checks':checks,'broken_links':broken,'changed_sources':changed,'errors':errors}
(OUT/'verification-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 文档核查记录','','2026-09-17。此记录只验证文档提取、覆盖与引用，不代表应用测试、接口验收、并发或支付测试。','',f'核对 {len(apis)} 个接口映射、{len(tables)} 张表、{len(reqs)} 个后台/商城/搜索需求簇与 {link_count} 个本地引用。','']
lines += [f'- {"通过" if c["pass"] else "失败"}：{c["name"]}。' for c in checks]
lines += ['','人工复核重点：白名单与业务主体检查、JWT字段和登出行为、SQL与ES两种搜索、接口级事务、MQ状态防重与未注册定时类、订单积分写入时序、后台关闭与商城取消差异、支付宝返回方式、SQL默认值与REPLACE语句。','', '局限：自动校验不能证明所有解释都没有遗漏；正文明确区分已确认事实、代码推断、未知与分析意见。']
(OUT/'文档核查记录.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'errors':errors,'checked_links':link_count,'checks':len(checks)},ensure_ascii=False))
if errors:raise SystemExit(1)
