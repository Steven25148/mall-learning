"""Read-only source inventory. Writes only report appendices, never application code."""
from pathlib import Path
import re, json, hashlib, collections

ROOT=Path('D:/project')
OUT=ROOT/'docs/reverse-engineering'
JAVA=sorted((ROOT/'mall').glob('*/src/main/java/**/*.java'))
def read(p): return p.read_text(encoding='utf-8-sig')
def rel(p): return p.relative_to(ROOT).as_posix()
def link(p,line=1,label=None): return f'[{label or rel(p)}]({p.as_posix()}:{line})'
def clean(s): return re.sub(r'\s+',' ',s).strip()
def mask(s):
    pattern=r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\''
    return re.sub(pattern,lambda m: ''.join('\n' if c=='\n' else ' ' for c in m[0]),s)
def end_pair(s,start,opening='(',closing=')'):
    depth=0
    for i in range(start,len(s)):
        if s[i]==opening: depth+=1
        elif s[i]==closing:
            depth-=1
            if depth==0:return i
    raise ValueError(start)
def methods(p):
    s=read(p); m=mask(s); result=[]
    for hit in re.finditer(r'\bpublic\s+(?!class\b|interface\b|enum\b)([\w<>?,.\s\[\]]+?)\s+(\w+)\s*\(',m):
        op=m.index('(',hit.start()); en=end_pair(m,op)
        aft=re.match(r'\s*(?:throws[\w\s,.]+)?([;{])',m[en+1:])
        if not aft:continue
        b=en+1+aft.end()-1; e=end_pair(m,b,'{','}') if m[b]=='{' else b
        result.append(dict(name=hit[2],returns=clean(s[hit.start(1):hit.end(1)]),params=clean(s[op+1:en]),start=hit.start(),end=e+1,line=s.count('\n',0,hit.start())+1,body=s[b+1:e] if m[b]=='{' else ''))
    return result
def annotation(s,pos):
    op=s.find('(',pos); en=end_pair(mask(s),op)
    return s[pos:en+1],en+1
def title_before(s,pos):
    a=list(re.finditer(r'@Operation\s*\(\s*summary\s*=\s*"([^"]+)"',s[:pos]))
    return a[-1][1] if a else ''
def db_tables_for(p):
    s=read(p)
    return sorted(set(re.findall(r'\b(?:cms|oms|pms|sms|ums)_[a-z_]+\b',s)))

OUT.mkdir(parents=True,exist_ok=True)
apis=[]
seed_resources=[]
seed_sql=read(ROOT/'mall/document/sql/mall.sql')
for sm in re.finditer(r"INSERT INTO `ums_resource` VALUES \((\d+), '[^']*', '([^']*)', '([^']*)'",seed_sql):
    seed_resources.append((sm[1],sm[2],sm[3],seed_sql.count('\n',0,sm.start())+1))
for p in JAVA:
    if p.parent.name!='controller':continue
    s=read(p); cm=re.search(r'public\s+class\s+(\w+)',s)
    if not cm:continue
    head=s[:cm.start()]; base=''
    match=re.search(r'@RequestMapping\s*\(\s*(?:value\s*=\s*)?"([^"]*)"',head)
    if match:base=match[1]
    deps=dict(re.findall(r'private\s+(\w+)\s+(\w+)\s*;',s))
    deps={v:k for k,v in deps.items()}
    prev=cm.end()
    for meth in methods(p):
        pre=s[prev:meth['start']]; prev=meth['end']
        maps=list(re.finditer(r'@(Request|Get|Post|Put|Delete|Patch)Mapping\s*\(',pre))
        if not maps:continue
        ann,_=annotation(pre,maps[-1].start())
        strings=re.findall(r'"([^"]*)"',ann)
        url=base+(strings[0] if strings else '')
        kind=maps[-1][1]
        verbs=re.findall(r'RequestMethod\.(\w+)',ann) if kind=='Request' else [kind.upper()]
        calls=sorted(set(f'{deps.get(obj,obj)}.{fn}' for obj,fn in re.findall(r'\b(\w+)\.(\w+)\(',meth['body']) if obj in deps))
        op=re.search(r'@Operation\s*\(\s*summary\s*=\s*"([^"]+)"',pre)
        module=p.relative_to(ROOT/'mall').parts[0]
        if module=='mall-admin':
            white=['/admin/login','/admin/register','/admin/info','/admin/logout','/minio/upload','/aliyun/oss/policy']
            permission='配置白名单放行；方法内可能仍依赖登录主体' if url in white else '后台动态资源权限（按URL匹配；运行时角色分配未确认）'
            if url not in white:
                matches=[]
                for rid,rname,pattern,rline in seed_resources:
                    if pattern.endswith('/**'):
                        yes=url==pattern[:-3] or url.startswith(pattern[:-2])
                    else:yes=url==pattern
                    if yes:matches.append(f'{rid}:{rname.strip()} ({pattern})')
                permission+='；SQL样例可匹配资源：'+('、'.join(matches) if matches else '未匹配；按该样例配置会被动态授权拒绝')
        elif module=='mall-portal':permission='配置白名单放行' if any(url.startswith(x) for x in ['/sso/','/home/','/product/','/brand/','/alipay/']) else '需会员认证；对象归属另看业务方法'
        elif module=='mall-demo':permission='教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置'
        else:permission='该应用未发现Security过滤链；外部访问控制无法确认'
        apis.append(dict(module=module,controller=cm[1],file=rel(p),method=meth['name'],http=','.join(verbs) or 'ANY（未限定）',url=url or '/',summary=op[1] if op else '未声明摘要',params=meth['params'],returns=meth['returns'],calls=calls,permission=permission,line=meth['line']))

(OUT/'api-inventory.json').write_text(json.dumps(apis,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 附录A：Controller API完整清单','', '【已确认事实】从当前源码的类级路径与方法级映射拼接。方法签名保留参数注解、默认值与返回类型。未标注 `@RequestBody` 的复杂对象不能直接当作 JSON body；`@RequestParam` 对应请求参数，`@PathVariable` 对应路径参数。权限描述来自随仓配置，不代表线上配置。','', '通用响应、过滤链与对象级权限见主说明书。业务模型字段见附录C；本清单不宣称接口已运行验收。','', f'共 {len(apis)} 个映射方法；包含 mall-demo 的教学接口，单独分组，不作为商城业务。','']
for module,items in __import__('itertools').groupby(apis,key=lambda a:a['module']):
    lines += [f'## {module}','']
    for a in items:
        lines += [f"### `{a['http']} {a['url']}`",'',f"- 功能：{a['summary']}。",f"- Controller：`{a['controller']}.{a['method']}`；{link(ROOT/a['file'],a['line'],'源码')}。",f"- 权限：{a['permission']}。",f"- 直接调用：{'、'.join('`'+x+'`' for x in a['calls']) or '无注入对象调用；见方法源码'}。",f"- 返回类型：`{a['returns']}`。",'- 请求参数 / Body：','```java',a['params'] or '无方法参数','```','']
(OUT/'附录A-API完整清单.md').write_text('\n'.join(lines),encoding='utf-8')

sqlp=ROOT/'mall/document/sql/mall.sql'; sql=read(sqlp); tables=[]
for hit in re.finditer(r'CREATE TABLE `([^`]+)`\s*\(([\s\S]*?)\) ENGINE\s*=([^;]+);',sql):
    name,body,tail=hit.groups(); fields=[]; indices=[]
    for line in body.splitlines():
        f=re.match(r'\s*`([^`]+)`\s+(.+?)(?:,)?$',line)
        if f:fields.append([f[1],f[2].rstrip(',')])
        elif re.search(r'PRIMARY KEY|INDEX|CONSTRAINT|FOREIGN KEY',line):indices.append(line.strip().rstrip(','))
    comment=re.search(r"COMMENT\s*=\s*'([^']*)'",tail)
    tables.append(dict(name=name,comment=comment[1] if comment else '',fields=fields,indices=indices,line=sql.count('\n',0,hit.start())+1))
(OUT/'database-inventory.json').write_text(json.dumps(tables,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 附录B：SQL数据库字典','', '【已确认事实】依据 `mall/document/sql/mall.sql` 的 CREATE TABLE 原文提取，保留字段类型、NULL、默认值、注释与索引。这里只记录仓库DDL，不代表运行数据库已逐项比对。SQL样例业务数据与账号凭据不复制。','',f'共 {len(tables)} 张表。各表实体及生成Mapper位于 mall-mbg；业务使用范围见主文与附录D。','']
for t in tables:
    lines += [f"## {t['name']} — {t['comment']}",'',link(sqlp,t['line'],'DDL来源'),'', '| 字段 | 类型、约束与原始注释 |','| --- | --- |']
    lines += [f'| `{n}` | {d.replace(chr(124),"／")} |' for n,d in t['fields']]
    lines += ['','索引 / 约束：','```sql',*t['indices'],'```','']
(OUT/'附录B-数据库完整字典.md').write_text('\n'.join(lines),encoding='utf-8')

lines=['# 附录C：请求与响应模型字段','', '【已确认事实】摘录业务 DTO / domain / BO 与生成 Model 的类声明、字段及紧邻注解。继承字段须结合父类；`Example` 查询构造器不列入接口模型。字段存在不表示每个接口都返回非空值或允许修改。','']
model_count=0
for p in JAVA:
    if p.parent.name not in ['dto','domain','bo','model']:continue
    if p.stem.endswith('Example'):continue
    s=read(p); cl=re.search(r'public (?:class|enum) [^{]+',s)
    if not cl:continue
    fields=[]; pending=[]
    for row in s.splitlines():
        if re.search(r'\bclass\s+\w+',row) and not re.search(r'\bclass\s+'+re.escape(p.stem)+r'\b',row):
            fields.append('// 以下字段属于嵌套类型：'+row.strip().rstrip('{').strip()); pending=[]
        elif row.strip().startswith('@') or row.strip().startswith('//'):pending.append(row.strip())
        elif re.match(r'\s*private\s+(?!static)',row):
            fields.extend(pending);fields.append(row.strip());pending=[]
        elif row.strip():pending=[]
    if not fields:continue
    model_count+=1
    lines += [f'## {p.stem}','',link(p), '', '```java',clean(cl[0]),*fields,'```','']
(OUT/'附录C-接口模型字段.md').write_text('\n'.join(lines),encoding='utf-8')

transactions=[]; service_inventory=[]
for p in JAVA:
    s=read(p)
    for mat in re.finditer(r'@Transactional(?:\([^)]*\))?\s*([\s\S]*?);',s):
        transactions.append(dict(file=rel(p),line=s.count('\n',0,mat.start())+1,signature=clean(mat[0])))
    if p.parent.name=='impl' and 'Service' in p.stem:
        deps=re.findall(r'private\s+(\w+)\s+(\w+)\s*;',s)
        service_inventory.append(dict(file=rel(p),name=p.stem,deps=deps,methods=[{'name':m['name'],'line':m['line'],'params':m['params'],'returns':m['returns']} for m in methods(p)]))
lines=['# 附录D：Service与事务证据索引','', '【已确认事实】按源码提取注入依赖和方法；生成Mapper按单表访问，DAO通常对应手写XML。事务索引只包含主源码，不含测试。外部资源不因这些注解自动加入数据库事务。','',f'## 事务声明（{len(transactions)}项）','']
for t in transactions:lines += [f"- {link(ROOT/t['file'],t['line'])}：`{t['signature']}`"]
for a in service_inventory:
    lines += ['',f"## {a['name']}",'',link(ROOT/a['file']),'','注入依赖：'+ '；'.join(f'`{t} {n}`' for t,n in a['deps']),'','方法：']
    for m in a['methods']:lines += [f"- `{m['name']}({m['params']})` → `{m['returns']}`；{link(ROOT/a['file'],m['line'],'源码')}。"]
(OUT/'附录D-Service与事务索引.md').write_text('\n'.join(lines),encoding='utf-8')

manifest=[]
for p in JAVA + sorted((ROOT/'mall').glob('*/src/main/resources/**/*')) + sorted((ROOT/'mall').glob('*/pom.xml')) + sorted((ROOT/'mall-admin-web/src').rglob('*')) + sorted((ROOT/'local').glob('*.ps1')) + sorted((ROOT/'local').glob('*.sh')) + [sqlp,ROOT/'mall/pom.xml',ROOT/'mall-admin-web/package.json',ROOT/'mall-admin-web/vite.config.ts']:
    if p.is_file():manifest.append({'file':rel(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(OUT/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'java_files':len(JAVA),'api_methods':len(apis),'api_by_module':dict(collections.Counter(x['module'] for x in apis)),'controller_count':len(set(x['file'] for x in apis)),'tables':len(tables),'models':model_count,'transaction_declarations':len(transactions),'service_implementations':len(service_inventory)}
(OUT/'inventory-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
