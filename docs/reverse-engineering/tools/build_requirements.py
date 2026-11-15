from pathlib import Path
import json,re,collections
ROOT=Path('D:/project'); OUT=ROOT/'docs/reverse-engineering'
apis=json.loads((OUT/'api-inventory.json').read_text(encoding='utf-8'))
java=list((ROOT/'mall').glob('*/src/main/java/**/*.java'))
def source(cls,module):
    found=[p for p in java if p.stem==cls and p.parts[len(ROOT.parts)+1]=='mall-'+module]
    return found[0] if len(found)==1 else None
def lk(p,n=1,label=None):return f'[{label or p.stem}]({p.as_posix()}:{n})'
# Each record is a human-authored reverse requirement, verified against the named implementation.
# controller|requirement|name|business behavior|boundary/errors|tables|middleware
DATA=r'''
admin|CmsPrefrenceAreaController|REQ-CMS-001|查询优选区域|返回全部优选区域，供商品关联选择；未找到本Controller的写入操作|没有分页或专门空结果错误；不能扩展成完整CMS管理|cms_prefrence_area|未见直接Redis/MQ/ES
admin|CmsSubjectController|REQ-CMS-002|查询商品专题|全部查询，或按专题名称模糊条件分页查询，用于商品关联等场景|此处没有专题增删改接口；空列表由通用结果返回|cms_subject|未见直接Redis/MQ/ES
admin|MinioController|REQ-FILE-001|MinIO上传与删除文件|Controller直接创建MinioClient；桶不存在则创建并配置策略；对象名为日期/原文件名，返回名称和URL；删除按objectName执行|上传为multipart file，异常捕获后failed；未发现扩展名白名单的服务端校验；没有Service层|无MySQL业务表写入|MinIO SDK；不是Redis/MQ/ES
admin|OmsCompanyAddressController|REQ-ORDERCFG-001|查询公司收货地址|读取公司地址列表，退货处理可引用地址|此Controller没有新增、编辑或删除公司地址接口|oms_company_address|未见直接Redis/MQ/ES
admin|OmsOrderController|REQ-ADMINORDER-001|后台订单处理|列表按订单号、状态、来源、类型、日期、收件人筛选；详情带明细和日志；发货SQL限状态1；关闭/编辑写操作记录；删除为逻辑删除|close与商城cancel不同，不释放锁库存和权益；费用修改未重算payAmount；操作人固定后台管理员|oms_order,oms_order_item,oms_order_operate_history|未见直接Redis/MQ/ES
admin|OmsOrderReturnApplyController|REQ-ADMINRETURN-001|处理退货申请|按条件分页/关联详情；状态1确认，2收货完成，3拒绝；删除条件含status=3|状态更新未检查旧状态；未发现支付渠道退款或自动入库；非法目标状态返回0|oms_order_return_apply,oms_company_address|未见直接Redis/MQ/ES
admin|OmsOrderReturnReasonController|REQ-ORDERCFG-002|维护退货原因|创建时设创建时间，提供分页、详情、修改、批量删除及状态变更|受影响行数由Controller判断；不能由原因配置推断完整售后审批规则|oms_order_return_reason|未见直接Redis/MQ/ES
admin|OmsOrderSettingController|REQ-ORDERCFG-003|读取和修改订单设置|按ID读取/更新设置；商城延迟取消实际读取主键1的normalOrderOvertime|表中其他时限字段不证明存在对应定时任务；更新不自动重发已有消息|oms_order_setting|本接口无；延迟取消路径读取本表后使用MQ
admin|OssController|REQ-FILE-002|OSS上传签名与回调信息|Service生成有目录前缀、大小上限、到期时间的上传policy和signature；callback从请求参数组装URL/大小等|签名生成异常记录后仍返回结果对象；实际上传由前端直接向OSS执行；未证明真实账号可用|无MySQL业务表写入|OSS SDK；不是Redis/MQ/ES
admin|PmsBrandController|REQ-PRODUCT-001|维护品牌|品牌新增/编辑/查询/删除及批量状态；首字母为空取名称第一个字符；修改品牌时同步商品表内brandName|没有将首字符转换为拼音的步骤；删除未见禁止有商品品牌删除的校验|pms_brand,pms_product|未见直接Redis/MQ/ES
admin|PmsProductAttributeCategoryController|REQ-PRODUCT-002|维护商品属性分类|创建时仅设name并insertSelective，属性/参数数量由SQL默认值0提供；提供列表、详情、修改、删除和带属性列表|分类数量为存储字段；删除未见自动清理所有关联数据的完整链路|pms_product_attribute_category,pms_product_attribute|未见直接Redis/MQ/ES
admin|PmsProductAttributeController|REQ-PRODUCT-003|维护规格和参数|按分类及type分页；新增type0增加attributeCount，type1增加paramCount；删除按首条所属分类修正计数；按商品分类查筛选属性|删除依赖非空ID列表且以第一条判断分类/类型，不能断言支持跨类别批量删除的一致计数|pms_product_attribute,pms_product_attribute_category,pms_product_category_attribute_relation|未见直接Redis/MQ/ES
admin|PmsProductCategoryController|REQ-PRODUCT-004|维护商品分类|由parentId设置level；创建和修改维护筛选属性关系；修改同步商品内分类名；提供层级查询、导航/显示状态|删除是主键删除，未见强制级联清理商品与全部子分类|pms_product_category,pms_product_category_attribute_relation,pms_product|未见直接Redis/MQ/ES
admin|PmsProductController|REQ-PRODUCT-005|创建编辑和管理商品|主表及会员价/阶梯价/满减/SKU/属性值/专题/优选关联一起保存；SKU编码缺失时按日期商品ID序号生成；查询及批量审核/上下架/新品/推荐/删除状态|审核人固定test；业务事务在接口声明；会员价可维护不代表结算使用；删除状态不等同物理删除；没有自动同步ES|pms_product,pms_member_price,pms_product_ladder,pms_product_full_reduction,pms_sku_stock,pms_product_attribute_value,cms_subject_product_relation,cms_prefrence_area_product_relation,pms_product_vertify_record|未见直接Redis/MQ/ES
admin|PmsSkuStockController|REQ-PRODUCT-006|查询和批量更新SKU|按productId和可选skuCode查SKU；更新先按productId过滤请求列表，再调用DAO的REPLACE INTO语句|语句未列lock_stock和promotion_price，不能按普通字段局部UPDATE理解；该后台维护入口不是下单并发锁|pms_sku_stock|未见直接Redis/MQ/ES
admin|SmsCouponController|REQ-MARKETING-001|维护优惠券定义|创建将剩余数量设为发行数量并清使用/领取计数；useType2写指定商品关系，1写分类关系；删除同时清两类关系；更新按当前类型替换相应关系|未自动证明历史领取记录随删除清理；修改类型时仅替换当前类型分支，其他旧关系不应假定已删除|sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation|未见直接Redis/MQ/ES
admin|SmsCouponHistoryController|REQ-MARKETING-002|查询优惠券领取记录|按券ID、使用状态、订单号查询领取记录，分页返回|该入口只查询，不是人工核销或退款退券接口|sms_coupon_history|未见直接Redis/MQ/ES
admin|SmsFlashPromotionController|REQ-FLASH-001|维护秒杀活动配置|活动新增、编辑、删除、上下线和名称分页查询|存在活动不证明有独立高并发秒杀购买链；未发现此操作通知MQ|sms_flash_promotion|未见直接Redis/MQ/ES
admin|SmsFlashPromotionProductRelationController|REQ-FLASH-002|维护活动场次商品|批量插入商品关系，编辑促销配置、删除、详情、按活动/场次查关联商品|这一步写活动关联表；不等于实际预扣SKU库存或严格执行秒杀限购|sms_flash_promotion_product_relation,pms_product|未见直接Redis/MQ/ES
admin|SmsFlashPromotionSessionController|REQ-FLASH-003|维护秒杀时间段|场次创建/修改/启停/删除；可选列表筛status1并计算对应活动商品数量|商城当前时间选择场次的查询与此可选列表筛选条件不完全相同|sms_flash_promotion_session,sms_flash_promotion_product_relation|未见直接Redis/MQ/ES
admin|SmsHomeAdvertiseController|REQ-HOMEADMIN-001|维护首页广告|创建初始化clickCount/orderCount为0；编辑、上下线、删除、详情与条件分页|没有发现点击/转化计数持续更新链，不能把两个字段当已接通统计|sms_home_advertise|未见直接Redis/MQ/ES
admin|SmsHomeBrandController|REQ-HOMEADMIN-002|维护品牌推荐|批量插入首页品牌条目，设推荐状态与排序初值；可排序、批量删、改推荐状态、按名称/状态查|维护首页配置，不是个性化推荐算法；数据库未声明该业务关联唯一性|sms_home_brand|未见直接Redis/MQ/ES
admin|SmsHomeNewProductController|REQ-HOMEADMIN-003|维护首页新品|批量添加条目、排序、删除、推荐状态及名称/状态分页查询|这里的推荐条目与pms_product.new_status是不同数据存储，不假定自动双向同步|sms_home_new_product|未见直接Redis/MQ/ES
admin|SmsHomeRecommendProductController|REQ-HOMEADMIN-004|维护首页人气推荐|批量添加条目、排序、删除、推荐状态和条件分页|这里维护手工推荐表，不能写成销量实时算法|sms_home_recommend_product|未见直接Redis/MQ/ES
admin|SmsHomeRecommendSubjectController|REQ-HOMEADMIN-005|维护首页专题推荐|添加专题推荐条目、改排序/状态、批量删与分页|仅推荐关系，不构成专题内容编辑的全部能力|sms_home_recommend_subject|未见直接Redis/MQ/ES
admin|UmsAdminController|REQ-ADMIN-001|后台账号与登录|注册检查用户名后BCrypt存储；登录核对密码和启用状态、写登录日志、返回Token；信息查角色/菜单；账号编辑、状态、改密、删除、分配角色、刷新及登出|注册/登录等列入白名单；登出只清缓存；修改/删除与缓存失效顺序见正文观察；前端无角色拒绝进入|ums_admin,ums_admin_login_log,ums_admin_role_relation,ums_role,ums_role_resource_relation,ums_resource,ums_role_menu_relation,ums_menu|Redis管理员/资源缓存；无业务MQ/ES
admin|UmsMemberLevelController|REQ-MEMBERLEVEL-001|查询会员等级|按defaultStatus查询等级列表，供商品会员价等选择|未发现此Controller提供会员等级创建/编辑或完整会员管理|ums_member_level|未见直接Redis/MQ/ES
admin|UmsMenuController|REQ-PERMISSION-001|维护后台菜单|创建/编辑时由父节点设置level；按父ID分页、详情、删除、树查询和hidden变更|菜单隐藏与后端资源授权独立；删除不代表自动回收所有关联资源|ums_menu|未见直接Redis/MQ/ES
admin|UmsResourceCategoryController|REQ-PERMISSION-002|维护资源分类|新增设创建时间，提供全部查询、修改与删除|资源分类仅用于整理资源，未见按分类自动授权整组资源的机制|ums_resource_category|未见直接Redis/MQ/ES
admin|UmsResourceController|REQ-PERMISSION-003|维护URL资源|提供资源增删改查；写操作后清当前进程动态权限Map，更新/删除清相关管理员资源缓存|规则匹配URL而非HTTP动词；进程内刷新没有找到跨实例广播|ums_resource,ums_role_resource_relation,ums_admin_role_relation|Redis资源缓存失效；本进程权限Map；无MQ/ES
admin|UmsRoleController|REQ-PERMISSION-004|维护角色及授权|角色增删改/启停/查询；菜单和资源分配先删除旧关系再插入新关系，资源分配清成员资源缓存|权限查询未过滤角色status；不能仅凭字段断言角色禁用实时失权|ums_role,ums_role_menu_relation,ums_role_resource_relation,ums_menu,ums_resource,ums_admin_role_relation|Redis资源缓存失效；无MQ/ES
portal|AlipayController|REQ-PAY-001|支付宝网页支付与查询通知|电脑和手机支付直接使用请求订单号/金额/标题生成HTML；notify验签且TRADE_SUCCESS时按订单号处理支付；query成功时也可更新订单|notify返回String未ResponseBody；未见退款；金额/归属完整核对未见；SDK错误处理可能返回null后继续访问|oms_order,oms_order_item,pms_sku_stock（经订单Service）|支付宝SDK；无直接Redis/MQ/ES
portal|HomeController|REQ-HOME-001|展示商城首页|广告、推荐品牌、当前活动/场次、秒杀商品、新品、人气、专题聚合；分类按显示状态；推荐商品接口实际分页返回未删已上架商品|首页广告只筛type1/status1；推荐商品不是个性化；当前场次查询未筛status；空活动返回空内容对象|sms_home_advertise,sms_home_brand,sms_home_new_product,sms_home_recommend_product,sms_home_recommend_subject,sms_flash_promotion,sms_flash_promotion_session,sms_flash_promotion_product_relation,pms_product,pms_brand,pms_product_category,cms_subject|未见直接Redis/MQ/ES
portal|MemberAttentionController|REQ-MEMBERDATA-001|关注品牌|当前会员+品牌先查重复；按sqlEnable读取品牌补信息；保存Mongo，按会员查询/取消/清空|品牌ID为空或SQL品牌不存在返回0；先查后写未证明并发唯一|pms_brand（可选读取）；Mongo MemberBrandAttention|MongoDB；认证可读Redis，无直接业务MQ/ES
portal|MemberProductCollectionController|REQ-MEMBERDATA-002|收藏商品|按当前会员+商品查重复；按sqlEnable读取未删除商品信息；保存Mongo；按会员查询、取消和清空|商品ID为空、商品不存在/已删返回0；无已声明的联合唯一约束|pms_product（可选读取）；Mongo MemberProductCollection|MongoDB；认证可读Redis，无直接业务MQ/ES
portal|MemberReadHistoryController|REQ-MEMBERDATA-003|记录商品浏览|写当前会员、创建时间并重置ID；开关控制SQL补商品信息；按当前会员时间倒序查/清空；可按ID列表删除|按ID列表删除未加会员条件；新增每次独立写，不按商品去重|pms_product（可选读取）；Mongo MemberReadHistory|MongoDB；认证可读Redis，无直接业务MQ/ES
portal|OmsCartItemController|REQ-CART-001|维护购物车并计算促销|按当前会员及商品/SKU合并数量；列表可带促销；按本人ID更新数量、删除或清空；改规格先删旧项再add|空cartIds在listPromotion中不会筛选，实际选择全部；改规格旧项删除缺会员过滤；未见统一正数量校验|oms_cart_item,pms_product,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,pms_product_attribute,pms_product_attribute_value|无直接业务Redis/MQ/ES；公共认证用Redis
portal|OmsPortalOrderController|REQ-PORTALORDER-001|会员订单操作|确认单、下单、支付状态写入、取消及重新发送取消消息、订单列表详情、确认收货、删除；流程见正文REQ-ORDER-001至004|接口之间归属和状态约束不同；不能由名称假定全部检查；库存/积分/支付风险见第23章|oms_order,oms_order_item,oms_cart_item,oms_order_setting,pms_sku_stock,sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,ums_member,ums_member_receive_address,ums_integration_consume_setting,pms_product,pms_product_ladder,pms_product_full_reduction|Redis会员缓存/订单计数；RabbitMQ取消；无ES
portal|OmsPortalOrderReturnApplyController|REQ-PORTALRETURN-001|提交退货申请|复制请求对象到申请表，设创建时间与status0|未查询订单归属、支付状态及可退数量；不执行退款|oms_order_return_apply|未见直接Redis/MQ/ES
portal|PmsPortalBrandController|REQ-BROWSE-001|浏览品牌与品牌商品|推荐品牌按首页品牌表；品牌详情按ID；品牌商品按未删除且上架分页|品牌不存在可返回null；不是后台品牌管理|pms_brand,sms_home_brand,pms_product|未见直接Redis/MQ/ES
portal|PmsPortalProductController|REQ-BROWSE-002|查询商品、分类树与详情|search用MySQL名称LIKE及品牌/分类筛选，排除已删未上架；排序ID/销量/价格；详情聚合品牌、属性/SKU、条件促销及可用券|详情按主键取商品后继续读取，不像search一样显式检查上架/删除；分类树读取所有分类|pms_product,pms_product_category,pms_brand,pms_product_attribute,pms_product_attribute_value,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation|本搜索走MySQL；没有直接ES调用
portal|UmsMemberController|REQ-MEMBER-001|会员账号及验证码|手机号验证码写Redis并直接返回；注册验证验证码、查用户名/电话、BCrypt密码、设默认等级；登录/Token刷新/当前信息/验证码改密|未发现短信发送服务；验证码验证不销毁；会员login不显式检查isEnabled|ums_member,ums_member_level|Redis会员缓存/验证码；无MQ/ES
portal|UmsMemberCouponController|REQ-COUPON-001|领取并查询会员优惠券|校验券存在、剩余数、enableTime、领取数量；写领取历史并减数量；按会员查历史、可用券、商品券、购物车可用/不可用券|库存不足/未到领取时间/限领抛ApiException；listCart门槛用intValue，日期与精度边界见正文；无严格并发扣减|sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,pms_product；购物车券查询另读取购物车及促销|无直接业务Redis/MQ/ES；认证用Redis
portal|UmsMemberReceiveAddressController|REQ-ADDRESS-001|维护会员地址|新地址覆盖memberId为当前会员；列表、详情、删改按memberId过滤；更新默认地址时先清同会员原默认标记|新增不执行与更新相同的默认地址清理；详情未找到返回null，不能保证下单后续友好报错|ums_member_receive_address|无直接业务Redis/MQ/ES；认证用Redis
search|EsProductController|REQ-SEARCH-001|管理和检索ES商品索引|importAll/create读取未删已上架MySQL商品和属性后save；删索引按ID；简单搜索、组合过滤排序、相似商品与筛选聚合|显式接口同步，无后台自动同步；importAll不删除旧文档；应用未见Security链，外围访问控制未知|pms_product,pms_product_attribute_value,pms_product_attribute|Elasticsearch pms索引；没有业务Redis/MQ
'''
records=[]
for row in DATA.strip().splitlines():
    mod,ctl,rid,name,flow,edge,tables,mw=row.split('|')
    group=[a for a in apis if a['module']=='mall-'+mod and a['controller']==ctl]
    if not group:raise ValueError(ctl)
    services=sorted({call.split('.')[0] for a in group for call in a['calls'] if 'Service' in call.split('.')[0]})
    files=[]; access=set()
    for svc in services:
        p=source(svc+'Impl',mod)
        if p:
            files.append(p)
            s=p.read_text(encoding='utf-8-sig')
            for typ,var in re.findall(r'private\s+(\w+)\s+(\w+)\s*;',s):
                if re.search(r'\b'+var+r'\.',s) and typ.endswith(('Mapper','Dao','Repository')):access.add(typ)
    records.append(dict(module=mod,controller=ctl,id=rid,name=name,flow=flow,edge=edge,tables=tables,middleware=mw,apis=group,services=services,files=files,access=sorted(access)))
covered={r['controller'] for r in records}; expected={a['controller'] for a in apis if a['module']!='mall-demo'}
assert covered==expected,(expected-covered,covered-expected)
lines=['# 附录E：功能需求与代码追踪','', '【代码推断·高可信】本附录把已经存在的接口与实现归纳为需求；编号为本次文档所编，不冒充原始PRD编号。每个功能簇列出全部入口。代码行为是事实，业务目的属于逆向解释。','',f'覆盖 {len(records)} 个业务Controller功能簇、{sum(len(r["apis"]) for r in records)} 个业务映射方法。教学接口在附录A单列。正文另展开5个跨路径核心需求。','', '输入和输出以本附录的逐接口签名为准，字段/继承/注解见附录C，HTTP方法与权限详见附录A。DTO有注解不代表调用处一定使用@Validated/@Valid。','', '## 需求—代码对应总表','', '| 需求ID | 功能 / Controller | Service | Mapper/DAO/Repository（直接使用） | 表或集合（功能簇） | Redis / MQ / ES及其他 |','| --- | --- | --- | --- | --- | --- |']
for r in records:
    lines.append('| '+' | '.join([r['id'],r['name']+' / '+r['controller'],'、'.join(r['services']) or 'Controller直接操作','、'.join(r['access']) or '无直接数据访问依赖；见说明',r['tables'],r['middleware']])+' |')
lines+=['','表集合按功能簇汇总，不表示每个入口都操作所有表。Mapper列是对应ServiceImpl直接使用的访问对象；下游Service的访问在正文核心链路和附录D继续定位。公共认证查用户/资源不自动变成业务接口的直接依赖。','']
for r in records:
    user='后台管理员（写接口按动态资源授权；白名单入口单列）' if r['module']=='admin' else '商城会员；公开内容/SSO/支付宝入口按配置白名单放行' if r['module']=='portal' else '搜索HTTP调用者；项目未声明应用内认证，外部控制无法确认'
    lines += [f"## {r['id']} {r['name']}",'',f'- 使用者：{user}。',f"- 处理流程与业务规则：【已确认事实】{r['flow']}。",f"- 异常与范围边界：{r['edge']}。",f"- 数据表/集合：{r['tables']}。",f"- 中间件：{r['middleware']}。",f"- Controller证据：{lk(ROOT/r['apis'][0]['file'])}。",'- Service证据：'+ ('、'.join(lk(p) for p in r['files']) or '无独立Service实现，直接逻辑见Controller')+'。','', '### 输入、输出及操作入口','']
    for a in r['apis']:
        lines += [f"- **{a['summary']}**：`{a['http']} {a['url']}` → `{a['controller']}.{a['method']}`。",f"  - 输入：`{a['params'] or '无方法参数'}`。",f"  - 输出：`{a['returns']}`；实际响应分支见{lk(ROOT/a['file'],a['line'],'方法实现')}。",f"  - 调用：{'、'.join(a['calls']) or '方法内处理'}；权限：{a['permission']}。"]
    lines += ['']
lines += ['## REQ-UI-001 管理前端导航与首页展示','', '- 【已确认事实】登录后从后端取得角色与菜单，Pinia保存用户状态并启用持久化，Axios请求附加Token。功能路由覆盖商品、订单、营销与权限；隐藏页用于编辑、分配和详情。','- 输入：登录表单、菜单选择、各业务表单及查询条件；输出：页面、列表、操作反馈。字段与请求以src/apis和src/types为准。','- 规则：无Token转登录，无角色时前端报错；菜单依据名称筛选，testMode=false。首页图表取本地数组并按日期截取，不查询经营统计接口。','- 异常：HTTP拦截器检查业务code，401提示重新登录；其他网络错误展示错误信息。','- Controller/Service/数据表：导航调用后台账号信息与角色菜单链，详见REQ-ADMIN-001；首页示例图表无统计Controller和数据库来源。','- 证据：[用户状态](D:/project/mall-admin-web/src/stores/user.ts:1)、[菜单](D:/project/mall-admin-web/src/stores/permission.ts:1)、[HTTP](D:/project/mall-admin-web/src/utils/http.ts:1)、[首页](D:/project/mall-admin-web/src/views/home/index.vue:35)。','', '## 教学示例的范围','', 'mall-demo的13个接口提供品牌CRUD与RestTemplate示例，有独立应用入口，不计入233个商城业务接口。不能把演示远程HTTP调用推断为三个业务应用之间存在同样的调用链。详见附录A的mall-demo部分。','']
(OUT/'附录E-功能需求与代码追踪.md').write_text('\n'.join(lines),encoding='utf-8')
(OUT/'requirements-inventory.json').write_text(json.dumps([{k:v for k,v in r.items() if k not in ('files','apis')} for r in records],ensure_ascii=False,indent=2),encoding='utf-8')
print(f'功能簇 {len(records)}，全部业务映射已覆盖；另列前端需求。')

# Resolve short evidence references in the authored report. Never invent a path/line.
report=OUT/'项目需求与架构设计说明书.md'
text=report.read_text(encoding='utf-8')
def resolve(m):
    module,cls,method=m[1],m[2],m[3]
    p=source(cls,module)
    if p is None:raise ValueError('unresolved '+m[0])
    s=p.read_text(encoding='utf-8-sig'); line=1
    if method:
        # Handles private methods as well as public method declarations.
        h=re.search(r'\b(?:public|private|protected)\s+[^;{}=]+?\b'+re.escape(method)+r'\s*\(',s)
        if not h:raise ValueError('missing method '+m[0])
        line=s.count('\n',0,h.start())+1
    return lk(p,line,cls+('.'+method if method else ''))
text=re.sub(r'\[\[([a-z]+):(\w+)(?:#(\w+))?\]\]',resolve,text)
report.write_text(text,encoding='utf-8')
print('正文证据引用解析完成。')
