# 附录E：功能需求与代码追踪

【代码推断·高可信】本附录把已经存在的接口与实现归纳为需求；编号为本次文档所编，不冒充原始PRD编号。每个功能簇列出全部入口。代码行为是事实，业务目的属于逆向解释。

覆盖 45 个业务Controller功能簇、233 个业务映射方法。教学接口在附录A单列。正文另展开5个跨路径核心需求。

输入和输出以本附录的逐接口签名为准，字段/继承/注解见附录C，HTTP方法与权限详见附录A。DTO有注解不代表调用处一定使用@Validated/@Valid。

## 需求—代码对应总表

| 需求ID | 功能 / Controller | Service | Mapper/DAO/Repository（直接使用） | 表或集合（功能簇） | Redis / MQ / ES及其他 |
| --- | --- | --- | --- | --- | --- |
| REQ-CMS-001 | 查询优选区域 / CmsPrefrenceAreaController | CmsPrefrenceAreaService | CmsPrefrenceAreaMapper | cms_prefrence_area | 未见直接Redis/MQ/ES |
| REQ-CMS-002 | 查询商品专题 / CmsSubjectController | CmsSubjectService | CmsSubjectMapper | cms_subject | 未见直接Redis/MQ/ES |
| REQ-FILE-001 | MinIO上传与删除文件 / MinioController | Controller直接操作 | 无直接数据访问依赖；见说明 | 无MySQL业务表写入 | MinIO SDK；不是Redis/MQ/ES |
| REQ-ORDERCFG-001 | 查询公司收货地址 / OmsCompanyAddressController | OmsCompanyAddressService | OmsCompanyAddressMapper | oms_company_address | 未见直接Redis/MQ/ES |
| REQ-ADMINORDER-001 | 后台订单处理 / OmsOrderController | OmsOrderService | OmsOrderDao、OmsOrderMapper、OmsOrderOperateHistoryDao、OmsOrderOperateHistoryMapper | oms_order,oms_order_item,oms_order_operate_history | 未见直接Redis/MQ/ES |
| REQ-ADMINRETURN-001 | 处理退货申请 / OmsOrderReturnApplyController | OmsOrderReturnApplyService | OmsOrderReturnApplyDao、OmsOrderReturnApplyMapper | oms_order_return_apply,oms_company_address | 未见直接Redis/MQ/ES |
| REQ-ORDERCFG-002 | 维护退货原因 / OmsOrderReturnReasonController | OmsOrderReturnReasonService | OmsOrderReturnReasonMapper | oms_order_return_reason | 未见直接Redis/MQ/ES |
| REQ-ORDERCFG-003 | 读取和修改订单设置 / OmsOrderSettingController | OmsOrderSettingService | OmsOrderSettingMapper | oms_order_setting | 本接口无；延迟取消路径读取本表后使用MQ |
| REQ-FILE-002 | OSS上传签名与回调信息 / OssController | OssService | 无直接数据访问依赖；见说明 | 无MySQL业务表写入 | OSS SDK；不是Redis/MQ/ES |
| REQ-PRODUCT-001 | 维护品牌 / PmsBrandController | PmsBrandService | PmsBrandMapper、PmsProductMapper | pms_brand,pms_product | 未见直接Redis/MQ/ES |
| REQ-PRODUCT-002 | 维护商品属性分类 / PmsProductAttributeCategoryController | PmsProductAttributeCategoryService | PmsProductAttributeCategoryDao、PmsProductAttributeCategoryMapper | pms_product_attribute_category,pms_product_attribute | 未见直接Redis/MQ/ES |
| REQ-PRODUCT-003 | 维护规格和参数 / PmsProductAttributeController | PmsProductAttributeService | PmsProductAttributeCategoryMapper、PmsProductAttributeDao、PmsProductAttributeMapper | pms_product_attribute,pms_product_attribute_category,pms_product_category_attribute_relation | 未见直接Redis/MQ/ES |
| REQ-PRODUCT-004 | 维护商品分类 / PmsProductCategoryController | PmsProductCategoryService | PmsProductCategoryAttributeRelationDao、PmsProductCategoryAttributeRelationMapper、PmsProductCategoryDao、PmsProductCategoryMapper、PmsProductMapper | pms_product_category,pms_product_category_attribute_relation,pms_product | 未见直接Redis/MQ/ES |
| REQ-PRODUCT-005 | 创建编辑和管理商品 / PmsProductController | PmsProductService | CmsPrefrenceAreaProductRelationMapper、CmsSubjectProductRelationMapper、PmsMemberPriceMapper、PmsProductAttributeValueMapper、PmsProductDao、PmsProductFullReductionMapper、PmsProductLadderMapper、PmsProductMapper、PmsProductVertifyRecordDao、PmsSkuStockMapper | pms_product,pms_member_price,pms_product_ladder,pms_product_full_reduction,pms_sku_stock,pms_product_attribute_value,cms_subject_product_relation,cms_prefrence_area_product_relation,pms_product_vertify_record | 未见直接Redis/MQ/ES |
| REQ-PRODUCT-006 | 查询和批量更新SKU / PmsSkuStockController | PmsSkuStockService | PmsSkuStockDao、PmsSkuStockMapper | pms_sku_stock | 未见直接Redis/MQ/ES |
| REQ-MARKETING-001 | 维护优惠券定义 / SmsCouponController | SmsCouponService | SmsCouponDao、SmsCouponMapper、SmsCouponProductCategoryRelationDao、SmsCouponProductCategoryRelationMapper、SmsCouponProductRelationDao、SmsCouponProductRelationMapper | sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation | 未见直接Redis/MQ/ES |
| REQ-MARKETING-002 | 查询优惠券领取记录 / SmsCouponHistoryController | SmsCouponHistoryService | SmsCouponHistoryMapper | sms_coupon_history | 未见直接Redis/MQ/ES |
| REQ-FLASH-001 | 维护秒杀活动配置 / SmsFlashPromotionController | SmsFlashPromotionService | SmsFlashPromotionMapper | sms_flash_promotion | 未见直接Redis/MQ/ES |
| REQ-FLASH-002 | 维护活动场次商品 / SmsFlashPromotionProductRelationController | SmsFlashPromotionProductRelationService | SmsFlashPromotionProductRelationDao、SmsFlashPromotionProductRelationMapper | sms_flash_promotion_product_relation,pms_product | 未见直接Redis/MQ/ES |
| REQ-FLASH-003 | 维护秒杀时间段 / SmsFlashPromotionSessionController | SmsFlashPromotionSessionService | SmsFlashPromotionSessionMapper | sms_flash_promotion_session,sms_flash_promotion_product_relation | 未见直接Redis/MQ/ES |
| REQ-HOMEADMIN-001 | 维护首页广告 / SmsHomeAdvertiseController | SmsHomeAdvertiseService | SmsHomeAdvertiseMapper | sms_home_advertise | 未见直接Redis/MQ/ES |
| REQ-HOMEADMIN-002 | 维护品牌推荐 / SmsHomeBrandController | SmsHomeBrandService | SmsHomeBrandMapper | sms_home_brand | 未见直接Redis/MQ/ES |
| REQ-HOMEADMIN-003 | 维护首页新品 / SmsHomeNewProductController | SmsHomeNewProductService | SmsHomeNewProductMapper | sms_home_new_product | 未见直接Redis/MQ/ES |
| REQ-HOMEADMIN-004 | 维护首页人气推荐 / SmsHomeRecommendProductController | SmsHomeRecommendProductService | SmsHomeRecommendProductMapper | sms_home_recommend_product | 未见直接Redis/MQ/ES |
| REQ-HOMEADMIN-005 | 维护首页专题推荐 / SmsHomeRecommendSubjectController | SmsHomeRecommendSubjectService | SmsHomeRecommendSubjectMapper | sms_home_recommend_subject | 未见直接Redis/MQ/ES |
| REQ-ADMIN-001 | 后台账号与登录 / UmsAdminController | UmsAdminService、UmsRoleService | UmsAdminLoginLogMapper、UmsAdminMapper、UmsAdminRoleRelationDao、UmsAdminRoleRelationMapper、UmsRoleDao、UmsRoleMapper、UmsRoleMenuRelationMapper、UmsRoleResourceRelationMapper | ums_admin,ums_admin_login_log,ums_admin_role_relation,ums_role,ums_role_resource_relation,ums_resource,ums_role_menu_relation,ums_menu | Redis管理员/资源缓存；无业务MQ/ES |
| REQ-MEMBERLEVEL-001 | 查询会员等级 / UmsMemberLevelController | UmsMemberLevelService | UmsMemberLevelMapper | ums_member_level | 未见直接Redis/MQ/ES |
| REQ-PERMISSION-001 | 维护后台菜单 / UmsMenuController | UmsMenuService | UmsMenuMapper | ums_menu | 未见直接Redis/MQ/ES |
| REQ-PERMISSION-002 | 维护资源分类 / UmsResourceCategoryController | UmsResourceCategoryService | UmsResourceCategoryMapper | ums_resource_category | 未见直接Redis/MQ/ES |
| REQ-PERMISSION-003 | 维护URL资源 / UmsResourceController | UmsResourceService | UmsResourceMapper | ums_resource,ums_role_resource_relation,ums_admin_role_relation | Redis资源缓存失效；本进程权限Map；无MQ/ES |
| REQ-PERMISSION-004 | 维护角色及授权 / UmsRoleController | UmsRoleService | UmsRoleDao、UmsRoleMapper、UmsRoleMenuRelationMapper、UmsRoleResourceRelationMapper | ums_role,ums_role_menu_relation,ums_role_resource_relation,ums_menu,ums_resource,ums_admin_role_relation | Redis资源缓存失效；无MQ/ES |
| REQ-PAY-001 | 支付宝网页支付与查询通知 / AlipayController | AlipayService | 无直接数据访问依赖；见说明 | oms_order,oms_order_item,pms_sku_stock（经订单Service） | 支付宝SDK；无直接Redis/MQ/ES |
| REQ-HOME-001 | 展示商城首页 / HomeController | HomeService | CmsSubjectMapper、HomeDao、PmsProductCategoryMapper、PmsProductMapper、SmsFlashPromotionMapper、SmsFlashPromotionSessionMapper、SmsHomeAdvertiseMapper | sms_home_advertise,sms_home_brand,sms_home_new_product,sms_home_recommend_product,sms_home_recommend_subject,sms_flash_promotion,sms_flash_promotion_session,sms_flash_promotion_product_relation,pms_product,pms_brand,pms_product_category,cms_subject | 未见直接Redis/MQ/ES |
| REQ-MEMBERDATA-001 | 关注品牌 / MemberAttentionController | MemberAttentionService | MemberBrandAttentionRepository、PmsBrandMapper | pms_brand（可选读取）；Mongo MemberBrandAttention | MongoDB；认证可读Redis，无直接业务MQ/ES |
| REQ-MEMBERDATA-002 | 收藏商品 / MemberProductCollectionController | MemberCollectionService | MemberProductCollectionRepository、PmsProductMapper | pms_product（可选读取）；Mongo MemberProductCollection | MongoDB；认证可读Redis，无直接业务MQ/ES |
| REQ-MEMBERDATA-003 | 记录商品浏览 / MemberReadHistoryController | MemberReadHistoryService | MemberReadHistoryRepository、PmsProductMapper | pms_product（可选读取）；Mongo MemberReadHistory | MongoDB；认证可读Redis，无直接业务MQ/ES |
| REQ-CART-001 | 维护购物车并计算促销 / OmsCartItemController | OmsCartItemService、UmsMemberService | OmsCartItemMapper、PortalProductDao、UmsMemberLevelMapper、UmsMemberMapper | oms_cart_item,pms_product,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,pms_product_attribute,pms_product_attribute_value | 无直接业务Redis/MQ/ES；公共认证用Redis |
| REQ-PORTALORDER-001 | 会员订单操作 / OmsPortalOrderController | OmsPortalOrderService | OmsOrderItemMapper、OmsOrderMapper、OmsOrderSettingMapper、PmsSkuStockMapper、PortalOrderDao、PortalOrderItemDao、SmsCouponHistoryMapper、UmsIntegrationConsumeSettingMapper | oms_order,oms_order_item,oms_cart_item,oms_order_setting,pms_sku_stock,sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,ums_member,ums_member_receive_address,ums_integration_consume_setting,pms_product,pms_product_ladder,pms_product_full_reduction | Redis会员缓存/订单计数；RabbitMQ取消；无ES |
| REQ-PORTALRETURN-001 | 提交退货申请 / OmsPortalOrderReturnApplyController | OmsPortalOrderReturnApplyService | OmsOrderReturnApplyMapper | oms_order_return_apply | 未见直接Redis/MQ/ES |
| REQ-BROWSE-001 | 浏览品牌与品牌商品 / PmsPortalBrandController | PmsPortalBrandService | HomeDao、PmsBrandMapper、PmsProductMapper | pms_brand,sms_home_brand,pms_product | 未见直接Redis/MQ/ES |
| REQ-BROWSE-002 | 查询商品、分类树与详情 / PmsPortalProductController | PmsPortalProductService | PmsBrandMapper、PmsProductAttributeMapper、PmsProductAttributeValueMapper、PmsProductCategoryMapper、PmsProductFullReductionMapper、PmsProductLadderMapper、PmsProductMapper、PmsSkuStockMapper、PortalProductDao | pms_product,pms_product_category,pms_brand,pms_product_attribute,pms_product_attribute_value,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation | 本搜索走MySQL；没有直接ES调用 |
| REQ-MEMBER-001 | 会员账号及验证码 / UmsMemberController | UmsMemberService | UmsMemberLevelMapper、UmsMemberMapper | ums_member,ums_member_level | Redis会员缓存/验证码；无MQ/ES |
| REQ-COUPON-001 | 领取并查询会员优惠券 / UmsMemberCouponController | OmsCartItemService、UmsMemberCouponService、UmsMemberService | OmsCartItemMapper、PmsProductMapper、PortalProductDao、SmsCouponHistoryDao、SmsCouponHistoryMapper、SmsCouponMapper、SmsCouponProductCategoryRelationMapper、SmsCouponProductRelationMapper、UmsMemberLevelMapper、UmsMemberMapper | sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,pms_product；购物车券查询另读取购物车及促销 | 无直接业务Redis/MQ/ES；认证用Redis |
| REQ-ADDRESS-001 | 维护会员地址 / UmsMemberReceiveAddressController | UmsMemberReceiveAddressService | UmsMemberReceiveAddressMapper | ums_member_receive_address | 无直接业务Redis/MQ/ES；认证用Redis |
| REQ-SEARCH-001 | 管理和检索ES商品索引 / EsProductController | EsProductService | EsProductDao、EsProductRepository | pms_product,pms_product_attribute_value,pms_product_attribute | Elasticsearch pms索引；没有业务Redis/MQ |

表集合按功能簇汇总，不表示每个入口都操作所有表。Mapper列是对应ServiceImpl直接使用的访问对象；下游Service的访问在正文核心链路和附录D继续定位。公共认证查用户/资源不自动变成业务接口的直接依赖。

## REQ-CMS-001 查询优选区域

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】返回全部优选区域，供商品关联选择；未找到本Controller的写入操作。
- 异常与范围边界：没有分页或专门空结果错误；不能扩展成完整CMS管理。
- 数据表/集合：cms_prefrence_area。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[CmsPrefrenceAreaController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsPrefrenceAreaController.java:1)。
- Service证据：[CmsPrefrenceAreaServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsPrefrenceAreaServiceImpl.java:1)。

### 输入、输出及操作入口

- **获取所有商品优选**：`GET /prefrenceArea/listAll` → `CmsPrefrenceAreaController.listAll`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<CmsPrefrenceArea>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsPrefrenceAreaController.java:30)。
  - 调用：CmsPrefrenceAreaService.listAll；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：23:商品优选管理 (/prefrenceArea/**)。

## REQ-CMS-002 查询商品专题

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】全部查询，或按专题名称模糊条件分页查询，用于商品关联等场景。
- 异常与范围边界：此处没有专题增删改接口；空列表由通用结果返回。
- 数据表/集合：cms_subject。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[CmsSubjectController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java:1)。
- Service证据：[CmsSubjectServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsSubjectServiceImpl.java:1)。

### 输入、输出及操作入口

- **获取全部商品专题**：`GET /subject/listAll` → `CmsSubjectController.listAll`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<CmsSubject>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java:32)。
  - 调用：CmsSubjectService.listAll；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：24:商品专题管理 (/subject/**)。
- **根据专题名称分页获取商品专题**：`GET /subject/list` → `CmsSubjectController.getList`。
  - 输入：`@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<CmsSubject>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java:40)。
  - 调用：CmsSubjectService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：24:商品专题管理 (/subject/**)。

## REQ-FILE-001 MinIO上传与删除文件

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】Controller直接创建MinioClient；桶不存在则创建并配置策略；对象名为日期/原文件名，返回名称和URL；删除按objectName执行。
- 异常与范围边界：上传为multipart file，异常捕获后failed；未发现扩展名白名单的服务端校验；没有Service层。
- 数据表/集合：无MySQL业务表写入。
- 中间件：MinIO SDK；不是Redis/MQ/ES。
- Controller证据：[MinioController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/MinioController.java:1)。
- Service证据：无独立Service实现，直接逻辑见Controller。

### 输入、输出及操作入口

- **文件上传**：`POST /minio/upload` → `MinioController.upload`。
  - 输入：`@RequestPart("file") MultipartFile file`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/MinioController.java:44)。
  - 调用：方法内处理；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **文件删除**：`POST /minio/delete` → `MinioController.delete`。
  - 输入：`@RequestParam("objectName") String objectName`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/MinioController.java:105)。
  - 调用：方法内处理；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：未匹配；按该样例配置会被动态授权拒绝。

## REQ-ORDERCFG-001 查询公司收货地址

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】读取公司地址列表，退货处理可引用地址。
- 异常与范围边界：此Controller没有新增、编辑或删除公司地址接口。
- 数据表/集合：oms_company_address。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[OmsCompanyAddressController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsCompanyAddressController.java:1)。
- Service证据：[OmsCompanyAddressServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsCompanyAddressServiceImpl.java:1)。

### 输入、输出及操作入口

- **获取所有收货地址**：`GET /companyAddress/list` → `OmsCompanyAddressController.list`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<OmsCompanyAddress>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsCompanyAddressController.java:30)。
  - 调用：OmsCompanyAddressService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：12:收货地址管理 (/companyAddress/**)。

## REQ-ADMINORDER-001 后台订单处理

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】列表按订单号、状态、来源、类型、日期、收件人筛选；详情带明细和日志；发货SQL限状态1；关闭/编辑写操作记录；删除为逻辑删除。
- 异常与范围边界：close与商城cancel不同，不释放锁库存和权益；费用修改未重算payAmount；操作人固定后台管理员。
- 数据表/集合：oms_order,oms_order_item,oms_order_operate_history。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[OmsOrderController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:1)。
- Service证据：[OmsOrderServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:1)。

### 输入、输出及操作入口

- **查询订单**：`GET /order/list` → `OmsOrderController.list`。
  - 输入：`OmsOrderQueryParam queryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<OmsOrder>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:30)。
  - 调用：OmsOrderService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **批量发货**：`POST /order/update/delivery` → `OmsOrderController.delivery`。
  - 输入：`@RequestBody List<OmsOrderDeliveryParam> deliveryParamList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:40)。
  - 调用：OmsOrderService.delivery；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **批量关闭订单**：`POST /order/update/close` → `OmsOrderController.close`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam String note`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:51)。
  - 调用：OmsOrderService.close；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **批量删除订单**：`POST /order/delete` → `OmsOrderController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:62)。
  - 调用：OmsOrderService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **获取订单详情：订单信息、商品信息、操作记录**：`GET /order/{id}` → `OmsOrderController.detail`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<OmsOrderDetail>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:73)。
  - 调用：OmsOrderService.detail；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **修改收货人信息**：`POST /order/update/receiverInfo` → `OmsOrderController.updateReceiverInfo`。
  - 输入：`@RequestBody OmsReceiverInfoParam receiverInfoParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:81)。
  - 调用：OmsOrderService.updateReceiverInfo；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **修改订单费用信息**：`POST /order/update/moneyInfo` → `OmsOrderController.updateReceiverInfo`。
  - 输入：`@RequestBody OmsMoneyInfoParam moneyInfoParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:92)。
  - 调用：OmsOrderService.updateMoneyInfo；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- **备注订单**：`POST /order/update/note` → `OmsOrderController.updateNote`。
  - 输入：`@RequestParam("id") Long id, @RequestParam("note") String note, @RequestParam("status") Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:103)。
  - 调用：OmsOrderService.updateNote；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。

## REQ-ADMINRETURN-001 处理退货申请

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按条件分页/关联详情；状态1确认，2收货完成，3拒绝；删除条件含status=3。
- 异常与范围边界：状态更新未检查旧状态；未发现支付渠道退款或自动入库；非法目标状态返回0。
- 数据表/集合：oms_order_return_apply,oms_company_address。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[OmsOrderReturnApplyController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:1)。
- Service证据：[OmsOrderReturnApplyServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:1)。

### 输入、输出及操作入口

- **分页查询退货申请**：`GET /returnApply/list` → `OmsOrderReturnApplyController.list`。
  - 输入：`OmsReturnApplyQueryParam queryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<OmsOrderReturnApply>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:32)。
  - 调用：OmsOrderReturnApplyService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- **批量删除退货申请**：`POST /returnApply/delete` → `OmsOrderReturnApplyController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:42)。
  - 调用：OmsOrderReturnApplyService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- **获取退货申请详情**：`GET /returnApply/{id}` → `OmsOrderReturnApplyController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:53)。
  - 调用：OmsOrderReturnApplyService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- **修改退货申请状态**：`POST /returnApply/update/status/{id}` → `OmsOrderReturnApplyController.updateStatus`。
  - 输入：`@PathVariable Long id, @RequestBody OmsUpdateStatusParam statusParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:61)。
  - 调用：OmsOrderReturnApplyService.updateStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。

## REQ-ORDERCFG-002 维护退货原因

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】创建时设创建时间，提供分页、详情、修改、批量删除及状态变更。
- 异常与范围边界：受影响行数由Controller判断；不能由原因配置推断完整售后审批规则。
- 数据表/集合：oms_order_return_reason。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[OmsOrderReturnReasonController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:1)。
- Service证据：[OmsOrderReturnReasonServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加退货原因**：`POST /returnReason/create` → `OmsOrderReturnReasonController.create`。
  - 输入：`@RequestBody OmsOrderReturnReason returnReason`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:29)。
  - 调用：OmsOrderReturnReasonService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- **修改退货原因**：`POST /returnReason/update/{id}` → `OmsOrderReturnReasonController.update`。
  - 输入：`@PathVariable Long id, @RequestBody OmsOrderReturnReason returnReason`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:40)。
  - 调用：OmsOrderReturnReasonService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- **批量删除退货原因**：`POST /returnReason/delete` → `OmsOrderReturnReasonController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:51)。
  - 调用：OmsOrderReturnReasonService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- **分页查询退货原因**：`GET /returnReason/list` → `OmsOrderReturnReasonController.list`。
  - 输入：`@RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<OmsOrderReturnReason>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:62)。
  - 调用：OmsOrderReturnReasonService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- **获取单个退货原因详情信息**：`GET /returnReason/{id}` → `OmsOrderReturnReasonController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<OmsOrderReturnReason>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:71)。
  - 调用：OmsOrderReturnReasonService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- **修改退货原因启用状态**：`POST /returnReason/update/status` → `OmsOrderReturnReasonController.updateStatus`。
  - 输入：`@RequestParam(value = "status") Integer status, @RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:79)。
  - 调用：OmsOrderReturnReasonService.updateStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。

## REQ-ORDERCFG-003 读取和修改订单设置

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按ID读取/更新设置；商城延迟取消实际读取主键1的normalOrderOvertime。
- 异常与范围边界：表中其他时限字段不证明存在对应定时任务；更新不自动重发已有消息。
- 数据表/集合：oms_order_setting。
- 中间件：本接口无；延迟取消路径读取本表后使用MQ。
- Controller证据：[OmsOrderSettingController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderSettingController.java:1)。
- Service证据：[OmsOrderSettingServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderSettingServiceImpl.java:1)。

### 输入、输出及操作入口

- **获取指定订单设置**：`GET /orderSetting/{id}` → `OmsOrderSettingController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<OmsOrderSetting>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderSettingController.java:26)。
  - 调用：OmsOrderSettingService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：11:订单设置管理 (/orderSetting/**)。
- **修改指定订单设置**：`POST /orderSetting/update/{id}` → `OmsOrderSettingController.update`。
  - 输入：`@PathVariable Long id, @RequestBody OmsOrderSetting orderSetting`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderSettingController.java:34)。
  - 调用：OmsOrderSettingService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：11:订单设置管理 (/orderSetting/**)。

## REQ-FILE-002 OSS上传签名与回调信息

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】Service生成有目录前缀、大小上限、到期时间的上传policy和signature；callback从请求参数组装URL/大小等。
- 异常与范围边界：签名生成异常记录后仍返回结果对象；实际上传由前端直接向OSS执行；未证明真实账号可用。
- 数据表/集合：无MySQL业务表写入。
- 中间件：OSS SDK；不是Redis/MQ/ES。
- Controller证据：[OssController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OssController.java:1)。
- Service证据：[OssServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java:1)。

### 输入、输出及操作入口

- **Oss上传签名生成**：`GET /aliyun/oss/policy` → `OssController.policy`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<OssPolicyResult>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OssController.java:32)。
  - 调用：OssService.policy；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **Oss上传成功回调**：`POST /aliyun/osscallback` → `OssController.callback`。
  - 输入：`HttpServletRequest request`。
  - 输出：`CommonResult<OssCallbackResult>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OssController.java:40)。
  - 调用：OssService.callback；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：未匹配；按该样例配置会被动态授权拒绝。

## REQ-PRODUCT-001 维护品牌

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】品牌新增/编辑/查询/删除及批量状态；首字母为空取名称第一个字符；修改品牌时同步商品表内brandName。
- 异常与范围边界：没有将首字符转换为拼音的步骤；删除未见禁止有商品品牌删除的校验。
- 数据表/集合：pms_brand,pms_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsBrandController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:1)。
- Service证据：[PmsBrandServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:1)。

### 输入、输出及操作入口

- **获取全部品牌列表**：`GET /brand/listAll` → `PmsBrandController.getList`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<PmsBrand>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:31)。
  - 调用：PmsBrandService.listAllBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **添加品牌**：`POST /brand/create` → `PmsBrandController.create`。
  - 输入：`@Validated @RequestBody PmsBrandParam pmsBrand`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:38)。
  - 调用：PmsBrandService.createBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **更新品牌**：`POST /brand/update/{id}` → `PmsBrandController.update`。
  - 输入：`@PathVariable("id") Long id, @Validated @RequestBody PmsBrandParam pmsBrandParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:52)。
  - 调用：PmsBrandService.updateBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **删除品牌**：`GET /brand/delete/{id}` → `PmsBrandController.delete`。
  - 输入：`@PathVariable("id") Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:67)。
  - 调用：PmsBrandService.deleteBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **根据品牌名称分页获取品牌列表**：`GET /brand/list` → `PmsBrandController.getList`。
  - 输入：`@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "showStatus",required = false) Integer showStatus, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<PmsBrand>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:79)。
  - 调用：PmsBrandService.listBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **根据编号查询品牌信息**：`GET /brand/{id}` → `PmsBrandController.getItem`。
  - 输入：`@PathVariable("id") Long id`。
  - 输出：`CommonResult<PmsBrand>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:90)。
  - 调用：PmsBrandService.getBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **批量删除品牌**：`POST /brand/delete/batch` → `PmsBrandController.deleteBatch`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:97)。
  - 调用：PmsBrandService.deleteBrand；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **批量更新显示状态**：`POST /brand/update/showStatus` → `PmsBrandController.updateShowStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("showStatus") Integer showStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:109)。
  - 调用：PmsBrandService.updateShowStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- **批量更新厂家制造商状态**：`POST /brand/update/factoryStatus` → `PmsBrandController.updateFactoryStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("factoryStatus") Integer factoryStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:122)。
  - 调用：PmsBrandService.updateFactoryStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。

## REQ-PRODUCT-002 维护商品属性分类

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】创建时仅设name并insertSelective，属性/参数数量由SQL默认值0提供；提供列表、详情、修改、删除和带属性列表。
- 异常与范围边界：分类数量为存储字段；删除未见自动清理所有关联数据的完整链路。
- 数据表/集合：pms_product_attribute_category,pms_product_attribute。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsProductAttributeCategoryController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:1)。
- Service证据：[PmsProductAttributeCategoryServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加商品属性分类**：`POST /productAttribute/category/create` → `PmsProductAttributeCategoryController.create`。
  - 输入：`@RequestParam String name`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:30)。
  - 调用：PmsProductAttributeCategoryService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- **修改商品属性分类**：`POST /productAttribute/category/update/{id}` → `PmsProductAttributeCategoryController.update`。
  - 输入：`@PathVariable Long id, @RequestParam String name`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:42)。
  - 调用：PmsProductAttributeCategoryService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- **删除单个商品属性分类**：`GET /productAttribute/category/delete/{id}` → `PmsProductAttributeCategoryController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:54)。
  - 调用：PmsProductAttributeCategoryService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- **获取单个商品属性分类信息**：`GET /productAttribute/category/{id}` → `PmsProductAttributeCategoryController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<PmsProductAttributeCategory>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:66)。
  - 调用：PmsProductAttributeCategoryService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- **分页获取所有商品属性分类**：`GET /productAttribute/category/list` → `PmsProductAttributeCategoryController.getList`。
  - 输入：`@RequestParam(defaultValue = "5") Integer pageSize, @RequestParam(defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<PmsProductAttributeCategory>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:74)。
  - 调用：PmsProductAttributeCategoryService.getList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- **获取所有商品属性分类及其下属性**：`GET /productAttribute/category/list/withAttr` → `PmsProductAttributeCategoryController.getListWithAttr`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<PmsProductAttributeCategoryItem>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:82)。
  - 调用：PmsProductAttributeCategoryService.getListWithAttr；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。

## REQ-PRODUCT-003 维护规格和参数

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按分类及type分页；新增type0增加attributeCount，type1增加paramCount；删除按首条所属分类修正计数；按商品分类查筛选属性。
- 异常与范围边界：删除依赖非空ID列表且以第一条判断分类/类型，不能断言支持跨类别批量删除的一致计数。
- 数据表/集合：pms_product_attribute,pms_product_attribute_category,pms_product_category_attribute_relation。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsProductAttributeController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:1)。
- Service证据：[PmsProductAttributeServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:1)。

### 输入、输出及操作入口

- **根据分类查询属性列表或参数列表**：`GET /productAttribute/list/{cid}` → `PmsProductAttributeController.getList`。
  - 输入：`@PathVariable Long cid, @RequestParam(value = "type") Integer type, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<PmsProductAttribute>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:36)。
  - 调用：PmsProductAttributeService.getList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- **添加商品属性信息**：`POST /productAttribute/create` → `PmsProductAttributeController.create`。
  - 输入：`@RequestBody PmsProductAttributeParam productAttributeParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:47)。
  - 调用：PmsProductAttributeService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- **修改商品属性信息**：`POST /productAttribute/update/{id}` → `PmsProductAttributeController.update`。
  - 输入：`@PathVariable Long id, @RequestBody PmsProductAttributeParam productAttributeParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:59)。
  - 调用：PmsProductAttributeService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- **查询单个商品属性**：`GET /productAttribute/{id}` → `PmsProductAttributeController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<PmsProductAttribute>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:71)。
  - 调用：PmsProductAttributeService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- **批量删除商品属性**：`POST /productAttribute/delete` → `PmsProductAttributeController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:79)。
  - 调用：PmsProductAttributeService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- **根据商品分类的id获取商品属性及属性分类**：`GET /productAttribute/attrInfo/{productCategoryId}` → `PmsProductAttributeController.getAttrInfo`。
  - 输入：`@PathVariable Long productCategoryId`。
  - 输出：`CommonResult<List<ProductAttrInfo>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:91)。
  - 调用：PmsProductAttributeService.getProductAttrInfo；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。

## REQ-PRODUCT-004 维护商品分类

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】由parentId设置level；创建和修改维护筛选属性关系；修改同步商品内分类名；提供层级查询、导航/显示状态。
- 异常与范围边界：删除是主键删除，未见强制级联清理商品与全部子分类。
- 数据表/集合：pms_product_category,pms_product_category_attribute_relation,pms_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsProductCategoryController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:1)。
- Service证据：[PmsProductCategoryServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加商品分类**：`POST /productCategory/create` → `PmsProductCategoryController.create`。
  - 输入：`@Validated @RequestBody PmsProductCategoryParam productCategoryParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:32)。
  - 调用：PmsProductCategoryService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **修改商品分类**：`POST /productCategory/update/{id}` → `PmsProductCategoryController.update`。
  - 输入：`@PathVariable Long id, @Validated @RequestBody PmsProductCategoryParam productCategoryParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:44)。
  - 调用：PmsProductCategoryService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **分页查询商品分类**：`GET /productCategory/list/{parentId}` → `PmsProductCategoryController.getList`。
  - 输入：`@PathVariable Long parentId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<PmsProductCategory>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:58)。
  - 调用：PmsProductCategoryService.getList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **根据id获取商品分类**：`GET /productCategory/{id}` → `PmsProductCategoryController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<PmsProductCategory>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:68)。
  - 调用：PmsProductCategoryService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **删除商品分类**：`POST /productCategory/delete/{id}` → `PmsProductCategoryController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:76)。
  - 调用：PmsProductCategoryService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **修改导航栏显示状态**：`POST /productCategory/update/navStatus` → `PmsProductCategoryController.updateNavStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("navStatus") Integer navStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:88)。
  - 调用：PmsProductCategoryService.updateNavStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **修改显示状态**：`POST /productCategory/update/showStatus` → `PmsProductCategoryController.updateShowStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("showStatus") Integer showStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:100)。
  - 调用：PmsProductCategoryService.updateShowStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- **查询所有一级分类及子分类**：`GET /productCategory/list/withChildren` → `PmsProductCategoryController.listWithChildren`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<PmsProductCategoryWithChildrenItem>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:112)。
  - 调用：PmsProductCategoryService.listWithChildren；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。

## REQ-PRODUCT-005 创建编辑和管理商品

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】主表及会员价/阶梯价/满减/SKU/属性值/专题/优选关联一起保存；SKU编码缺失时按日期商品ID序号生成；查询及批量审核/上下架/新品/推荐/删除状态。
- 异常与范围边界：审核人固定test；业务事务在接口声明；会员价可维护不代表结算使用；删除状态不等同物理删除；没有自动同步ES。
- 数据表/集合：pms_product,pms_member_price,pms_product_ladder,pms_product_full_reduction,pms_sku_stock,pms_product_attribute_value,cms_subject_product_relation,cms_prefrence_area_product_relation,pms_product_vertify_record。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsProductController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:1)。
- Service证据：[PmsProductServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:1)。

### 输入、输出及操作入口

- **创建商品**：`POST /product/create` → `PmsProductController.create`。
  - 输入：`@RequestBody PmsProductParam productParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:32)。
  - 调用：PmsProductService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **根据商品id获取商品编辑信息**：`GET /product/updateInfo/{id}` → `PmsProductController.getUpdateInfo`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<PmsProductResult>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:44)。
  - 调用：PmsProductService.getUpdateInfo；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **更新商品**：`POST /product/update/{id}` → `PmsProductController.update`。
  - 输入：`@PathVariable Long id, @RequestBody PmsProductParam productParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:52)。
  - 调用：PmsProductService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **查询商品**：`GET /product/list` → `PmsProductController.getList`。
  - 输入：`PmsProductQueryParam productQueryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:64)。
  - 调用：PmsProductService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **根据商品名称或货号模糊查询**：`GET /product/simpleList` → `PmsProductController.getList`。
  - 输入：`String keyword`。
  - 输出：`CommonResult<List<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:74)。
  - 调用：PmsProductService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **批量修改审核状态**：`POST /product/update/verifyStatus` → `PmsProductController.updateVerifyStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("verifyStatus") Integer verifyStatus, @RequestParam("detail") String detail`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:82)。
  - 调用：PmsProductService.updateVerifyStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **批量上下架商品**：`POST /product/update/publishStatus` → `PmsProductController.updatePublishStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("publishStatus") Integer publishStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:96)。
  - 调用：PmsProductService.updatePublishStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **批量推荐商品**：`POST /product/update/recommendStatus` → `PmsProductController.updateRecommendStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("recommendStatus") Integer recommendStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:109)。
  - 调用：PmsProductService.updateRecommendStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **批量设为新品**：`POST /product/update/newStatus` → `PmsProductController.updateNewStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("newStatus") Integer newStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:122)。
  - 调用：PmsProductService.updateNewStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- **批量修改删除状态**：`POST /product/update/deleteStatus` → `PmsProductController.updateDeleteStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam("deleteStatus") Integer deleteStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:135)。
  - 调用：PmsProductService.updateDeleteStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。

## REQ-PRODUCT-006 查询和批量更新SKU

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按productId和可选skuCode查SKU；更新先按productId过滤请求列表，再调用DAO的REPLACE INTO语句。
- 异常与范围边界：语句未列lock_stock和promotion_price，不能按普通字段局部UPDATE理解；该后台维护入口不是下单并发锁。
- 数据表/集合：pms_sku_stock。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsSkuStockController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsSkuStockController.java:1)。
- Service证据：[PmsSkuStockServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java:1)。

### 输入、输出及操作入口

- **根据商品ID及sku编码模糊搜索sku库存**：`GET /sku/{pid}` → `PmsSkuStockController.getList`。
  - 输入：`@PathVariable Long pid, @RequestParam(value = "keyword",required = false) String keyword`。
  - 输出：`CommonResult<List<PmsSkuStock>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsSkuStockController.java:28)。
  - 调用：PmsSkuStockService.getList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：6:商品库存管理 (/sku/**)。
- **批量更新sku库存信息**：`POST /sku/update/{pid}` → `PmsSkuStockController.update`。
  - 输入：`@PathVariable Long pid,@RequestBody List<PmsSkuStock> skuStockList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsSkuStockController.java:35)。
  - 调用：PmsSkuStockService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：6:商品库存管理 (/sku/**)。

## REQ-MARKETING-001 维护优惠券定义

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】创建将剩余数量设为发行数量并清使用/领取计数；useType2写指定商品关系，1写分类关系；删除同时清两类关系；更新按当前类型替换相应关系。
- 异常与范围边界：未自动证明历史领取记录随删除清理；修改类型时仅替换当前类型分支，其他旧关系不应假定已删除。
- 数据表/集合：sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsCouponController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:1)。
- Service证据：[SmsCouponServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加优惠券**：`POST /coupon/create` → `SmsCouponController.add`。
  - 输入：`@RequestBody SmsCouponParam couponParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:29)。
  - 调用：SmsCouponService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- **删除优惠券**：`POST /coupon/delete/{id}` → `SmsCouponController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:40)。
  - 调用：SmsCouponService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- **修改优惠券**：`POST /coupon/update/{id}` → `SmsCouponController.update`。
  - 输入：`@PathVariable Long id,@RequestBody SmsCouponParam couponParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:51)。
  - 调用：SmsCouponService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- **根据优惠券名称和类型分页获取优惠券列表**：`GET /coupon/list` → `SmsCouponController.list`。
  - 输入：`@RequestParam(value = "name",required = false) String name, @RequestParam(value = "type",required = false) Integer type, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsCoupon>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:62)。
  - 调用：SmsCouponService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- **获取单个优惠券的详细信息**：`GET /coupon/{id}` → `SmsCouponController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<SmsCouponParam>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:74)。
  - 调用：SmsCouponService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。

## REQ-MARKETING-002 查询优惠券领取记录

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按券ID、使用状态、订单号查询领取记录，分页返回。
- 异常与范围边界：该入口只查询，不是人工核销或退款退券接口。
- 数据表/集合：sms_coupon_history。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsCouponHistoryController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponHistoryController.java:1)。
- Service证据：[SmsCouponHistoryServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponHistoryServiceImpl.java:1)。

### 输入、输出及操作入口

- **根据优惠券id，使用状态，订单编号分页获取领取记录**：`GET /couponHistory/list` → `SmsCouponHistoryController.list`。
  - 输入：`@RequestParam(value = "couponId", required = false) Long couponId, @RequestParam(value = "useStatus", required = false) Integer useStatus, @RequestParam(value = "orderSn", required = false) String orderSn, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsCouponHistory>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponHistoryController.java:32)。
  - 调用：SmsCouponHistoryService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：14:优惠券领取记录管理 (/couponHistory/**)。

## REQ-FLASH-001 维护秒杀活动配置

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】活动新增、编辑、删除、上下线和名称分页查询。
- 异常与范围边界：存在活动不证明有独立高并发秒杀购买链；未发现此操作通知MQ。
- 数据表/集合：sms_flash_promotion。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsFlashPromotionController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:1)。
- Service证据：[SmsFlashPromotionServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加活动**：`POST /flash/create` → `SmsFlashPromotionController.create`。
  - 输入：`@RequestBody SmsFlashPromotion flashPromotion`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:29)。
  - 调用：SmsFlashPromotionService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- **编辑活动**：`POST /flash/update/{id}` → `SmsFlashPromotionController.update`。
  - 输入：`@PathVariable Long id, @RequestBody SmsFlashPromotion flashPromotion`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:40)。
  - 调用：SmsFlashPromotionService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- **删除活动**：`POST /flash/delete/{id}` → `SmsFlashPromotionController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:51)。
  - 调用：SmsFlashPromotionService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- **修改上下线状态**：`POST /flash/update/status/{id}` → `SmsFlashPromotionController.update`。
  - 输入：`@PathVariable Long id, Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:62)。
  - 调用：SmsFlashPromotionService.updateStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- **获取活动详情**：`GET /flash/{id}` → `SmsFlashPromotionController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<SmsFlashPromotion>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:73)。
  - 调用：SmsFlashPromotionService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- **根据活动名称分页查询**：`GET /flash/list` → `SmsFlashPromotionController.getItem`。
  - 输入：`@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsFlashPromotion>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:81)。
  - 调用：SmsFlashPromotionService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。

## REQ-FLASH-002 维护活动场次商品

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】批量插入商品关系，编辑促销配置、删除、详情、按活动/场次查关联商品。
- 异常与范围边界：这一步写活动关联表；不等于实际预扣SKU库存或严格执行秒杀限购。
- 数据表/集合：sms_flash_promotion_product_relation,pms_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsFlashPromotionProductRelationController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:1)。
- Service证据：[SmsFlashPromotionProductRelationServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:1)。

### 输入、输出及操作入口

- **批量选择商品添加关联**：`POST /flashProductRelation/create` → `SmsFlashPromotionProductRelationController.create`。
  - 输入：`@RequestBody List<SmsFlashPromotionProductRelation> relationList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:30)。
  - 调用：SmsFlashPromotionProductRelationService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- **修改关联信息**：`POST /flashProductRelation/update/{id}` → `SmsFlashPromotionProductRelationController.update`。
  - 输入：`@PathVariable Long id, @RequestBody SmsFlashPromotionProductRelation relation`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:41)。
  - 调用：SmsFlashPromotionProductRelationService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- **删除关联**：`POST /flashProductRelation/delete/{id}` → `SmsFlashPromotionProductRelationController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:52)。
  - 调用：SmsFlashPromotionProductRelationService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- **获取关联商品促销信息**：`GET /flashProductRelation/{id}` → `SmsFlashPromotionProductRelationController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<SmsFlashPromotionProductRelation>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:63)。
  - 调用：SmsFlashPromotionProductRelationService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- **分页查询不同场次关联及商品信息**：`GET /flashProductRelation/list` → `SmsFlashPromotionProductRelationController.list`。
  - 输入：`@RequestParam(value = "flashPromotionId") Long flashPromotionId, @RequestParam(value = "flashPromotionSessionId") Long flashPromotionSessionId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsFlashPromotionProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:71)。
  - 调用：SmsFlashPromotionProductRelationService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。

## REQ-FLASH-003 维护秒杀时间段

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】场次创建/修改/启停/删除；可选列表筛status1并计算对应活动商品数量。
- 异常与范围边界：商城当前时间选择场次的查询与此可选列表筛选条件不完全相同。
- 数据表/集合：sms_flash_promotion_session,sms_flash_promotion_product_relation。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsFlashPromotionSessionController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:1)。
- Service证据：[SmsFlashPromotionSessionServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加场次**：`POST /flashSession/create` → `SmsFlashPromotionSessionController.create`。
  - 输入：`@RequestBody SmsFlashPromotionSession promotionSession`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:29)。
  - 调用：SmsFlashPromotionSessionService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **修改场次**：`POST /flashSession/update/{id}` → `SmsFlashPromotionSessionController.update`。
  - 输入：`@PathVariable Long id, @RequestBody SmsFlashPromotionSession promotionSession`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:40)。
  - 调用：SmsFlashPromotionSessionService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **修改启用状态**：`POST /flashSession/update/status/{id}` → `SmsFlashPromotionSessionController.updateStatus`。
  - 输入：`@PathVariable Long id, Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:51)。
  - 调用：SmsFlashPromotionSessionService.updateStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **删除场次**：`POST /flashSession/delete/{id}` → `SmsFlashPromotionSessionController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:62)。
  - 调用：SmsFlashPromotionSessionService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **获取场次详情**：`GET /flashSession/{id}` → `SmsFlashPromotionSessionController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<SmsFlashPromotionSession>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:73)。
  - 调用：SmsFlashPromotionSessionService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **获取全部场次**：`GET /flashSession/list` → `SmsFlashPromotionSessionController.list`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<SmsFlashPromotionSession>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:81)。
  - 调用：SmsFlashPromotionSessionService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- **获取全部可选场次及其数量**：`GET /flashSession/selectList` → `SmsFlashPromotionSessionController.selectList`。
  - 输入：`Long flashPromotionId`。
  - 输出：`CommonResult<List<SmsFlashPromotionSessionDetail>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:89)。
  - 调用：SmsFlashPromotionSessionService.selectList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。

## REQ-HOMEADMIN-001 维护首页广告

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】创建初始化clickCount/orderCount为0；编辑、上下线、删除、详情与条件分页。
- 异常与范围边界：没有发现点击/转化计数持续更新链，不能把两个字段当已接通统计。
- 数据表/集合：sms_home_advertise。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsHomeAdvertiseController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:1)。
- Service证据：[SmsHomeAdvertiseServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加广告**：`POST /home/advertise/create` → `SmsHomeAdvertiseController.create`。
  - 输入：`@RequestBody SmsHomeAdvertise advertise`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:29)。
  - 调用：SmsHomeAdvertiseService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- **删除广告**：`POST /home/advertise/delete` → `SmsHomeAdvertiseController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:39)。
  - 调用：SmsHomeAdvertiseService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- **修改上下线状态**：`POST /home/advertise/update/status/{id}` → `SmsHomeAdvertiseController.updateStatus`。
  - 输入：`@PathVariable Long id, Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:49)。
  - 调用：SmsHomeAdvertiseService.updateStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- **获取广告详情**：`GET /home/advertise/{id}` → `SmsHomeAdvertiseController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<SmsHomeAdvertise>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:59)。
  - 调用：SmsHomeAdvertiseService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- **修改广告**：`POST /home/advertise/update/{id}` → `SmsHomeAdvertiseController.update`。
  - 输入：`@PathVariable Long id, @RequestBody SmsHomeAdvertise advertise`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:67)。
  - 调用：SmsHomeAdvertiseService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- **分页查询广告**：`GET /home/advertise/list` → `SmsHomeAdvertiseController.list`。
  - 输入：`@RequestParam(value = "name", required = false) String name, @RequestParam(value = "type", required = false) Integer type, @RequestParam(value = "endTime", required = false) String endTime, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsHomeAdvertise>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:77)。
  - 调用：SmsHomeAdvertiseService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。

## REQ-HOMEADMIN-002 维护品牌推荐

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】批量插入首页品牌条目，设推荐状态与排序初值；可排序、批量删、改推荐状态、按名称/状态查。
- 异常与范围边界：维护首页配置，不是个性化推荐算法；数据库未声明该业务关联唯一性。
- 数据表/集合：sms_home_brand。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsHomeBrandController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:1)。
- Service证据：[SmsHomeBrandServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加首页推荐品牌**：`POST /home/brand/create` → `SmsHomeBrandController.create`。
  - 输入：`@RequestBody List<SmsHomeBrand> homeBrandList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:29)。
  - 调用：SmsHomeBrandService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- **修改推荐品牌排序**：`POST /home/brand/update/sort/{id}` → `SmsHomeBrandController.updateSort`。
  - 输入：`@PathVariable Long id, Integer sort`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:40)。
  - 调用：SmsHomeBrandService.updateSort；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- **批量删除推荐品牌**：`POST /home/brand/delete` → `SmsHomeBrandController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:51)。
  - 调用：SmsHomeBrandService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- **批量修改推荐品牌状态**：`POST /home/brand/update/recommendStatus` → `SmsHomeBrandController.updateRecommendStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:62)。
  - 调用：SmsHomeBrandService.updateRecommendStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- **分页查询推荐品牌**：`GET /home/brand/list` → `SmsHomeBrandController.list`。
  - 输入：`@RequestParam(value = "brandName", required = false) String brandName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsHomeBrand>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:73)。
  - 调用：SmsHomeBrandService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。

## REQ-HOMEADMIN-003 维护首页新品

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】批量添加条目、排序、删除、推荐状态及名称/状态分页查询。
- 异常与范围边界：这里的推荐条目与pms_product.new_status是不同数据存储，不假定自动双向同步。
- 数据表/集合：sms_home_new_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsHomeNewProductController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:1)。
- Service证据：[SmsHomeNewProductServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加首页新品**：`POST /home/newProduct/create` → `SmsHomeNewProductController.create`。
  - 输入：`@RequestBody List<SmsHomeNewProduct> homeNewProductList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:29)。
  - 调用：SmsHomeNewProductService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- **修改首页新品排序**：`POST /home/newProduct/update/sort/{id}` → `SmsHomeNewProductController.updateSort`。
  - 输入：`@PathVariable Long id, Integer sort`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:40)。
  - 调用：SmsHomeNewProductService.updateSort；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- **批量删除首页新品**：`POST /home/newProduct/delete` → `SmsHomeNewProductController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:51)。
  - 调用：SmsHomeNewProductService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- **批量修改首页新品状态**：`POST /home/newProduct/update/recommendStatus` → `SmsHomeNewProductController.updateRecommendStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:62)。
  - 调用：SmsHomeNewProductService.updateRecommendStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- **分页查询首页新品**：`GET /home/newProduct/list` → `SmsHomeNewProductController.list`。
  - 输入：`@RequestParam(value = "productName", required = false) String productName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsHomeNewProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:73)。
  - 调用：SmsHomeNewProductService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。

## REQ-HOMEADMIN-004 维护首页人气推荐

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】批量添加条目、排序、删除、推荐状态和条件分页。
- 异常与范围边界：这里维护手工推荐表，不能写成销量实时算法。
- 数据表/集合：sms_home_recommend_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsHomeRecommendProductController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:1)。
- Service证据：[SmsHomeRecommendProductServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加首页推荐**：`POST /home/recommendProduct/create` → `SmsHomeRecommendProductController.create`。
  - 输入：`@RequestBody List<SmsHomeRecommendProduct> homeRecommendProductList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:29)。
  - 调用：SmsHomeRecommendProductService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- **修改推荐排序**：`POST /home/recommendProduct/update/sort/{id}` → `SmsHomeRecommendProductController.updateSort`。
  - 输入：`@PathVariable Long id, Integer sort`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:40)。
  - 调用：SmsHomeRecommendProductService.updateSort；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- **批量删除推荐**：`POST /home/recommendProduct/delete` → `SmsHomeRecommendProductController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:51)。
  - 调用：SmsHomeRecommendProductService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- **批量修改推荐状态**：`POST /home/recommendProduct/update/recommendStatus` → `SmsHomeRecommendProductController.updateRecommendStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:62)。
  - 调用：SmsHomeRecommendProductService.updateRecommendStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- **分页查询推荐**：`GET /home/recommendProduct/list` → `SmsHomeRecommendProductController.list`。
  - 输入：`@RequestParam(value = "productName", required = false) String productName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsHomeRecommendProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:73)。
  - 调用：SmsHomeRecommendProductService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。

## REQ-HOMEADMIN-005 维护首页专题推荐

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】添加专题推荐条目、改排序/状态、批量删与分页。
- 异常与范围边界：仅推荐关系，不构成专题内容编辑的全部能力。
- 数据表/集合：sms_home_recommend_subject。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[SmsHomeRecommendSubjectController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:1)。
- Service证据：[SmsHomeRecommendSubjectServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加首页推荐专题**：`POST /home/recommendSubject/create` → `SmsHomeRecommendSubjectController.create`。
  - 输入：`@RequestBody List<SmsHomeRecommendSubject> homeRecommendSubjectList`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:29)。
  - 调用：SmsHomeRecommendSubjectService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- **修改推荐排序**：`POST /home/recommendSubject/update/sort/{id}` → `SmsHomeRecommendSubjectController.updateSort`。
  - 输入：`@PathVariable Long id, Integer sort`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:40)。
  - 调用：SmsHomeRecommendSubjectService.updateSort；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- **批量删除推荐**：`POST /home/recommendSubject/delete` → `SmsHomeRecommendSubjectController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:51)。
  - 调用：SmsHomeRecommendSubjectService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- **批量修改推荐状态**：`POST /home/recommendSubject/update/recommendStatus` → `SmsHomeRecommendSubjectController.updateRecommendStatus`。
  - 输入：`@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:62)。
  - 调用：SmsHomeRecommendSubjectService.updateRecommendStatus；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- **分页查询推荐**：`GET /home/recommendSubject/list` → `SmsHomeRecommendSubjectController.list`。
  - 输入：`@RequestParam(value = "subjectName", required = false) String subjectName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<SmsHomeRecommendSubject>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:73)。
  - 调用：SmsHomeRecommendSubjectService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。

## REQ-ADMIN-001 后台账号与登录

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】注册检查用户名后BCrypt存储；登录核对密码和启用状态、写登录日志、返回Token；信息查角色/菜单；账号编辑、状态、改密、删除、分配角色、刷新及登出。
- 异常与范围边界：注册/登录等列入白名单；登出只清缓存；修改/删除与缓存失效顺序见正文观察；前端无角色拒绝进入。
- 数据表/集合：ums_admin,ums_admin_login_log,ums_admin_role_relation,ums_role,ums_role_resource_relation,ums_resource,ums_role_menu_relation,ums_menu。
- 中间件：Redis管理员/资源缓存；无业务MQ/ES。
- Controller证据：[UmsAdminController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:1)。
- Service证据：[UmsAdminServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:1)、[UmsRoleServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:1)。

### 输入、输出及操作入口

- **用户注册**：`POST /admin/register` → `UmsAdminController.register`。
  - 输入：`@Validated @RequestBody UmsAdminParam umsAdminParam`。
  - 输出：`CommonResult<UmsAdmin>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:49)。
  - 调用：UmsAdminService.register；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **登录以后返回token**：`POST /admin/login` → `UmsAdminController.login`。
  - 输入：`@Validated @RequestBody UmsAdminLoginParam umsAdminLoginParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:60)。
  - 调用：UmsAdminService.login；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **刷新token**：`GET /admin/refreshToken` → `UmsAdminController.refreshToken`。
  - 输入：`HttpServletRequest request`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:74)。
  - 调用：UmsAdminService.refreshToken；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **获取当前登录用户信息**：`GET /admin/info` → `UmsAdminController.getAdminInfo`。
  - 输入：`Principal principal`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:89)。
  - 调用：UmsAdminService.getAdminByUsername、UmsAdminService.getRoleList、UmsRoleService.getMenuList；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **登出功能**：`POST /admin/logout` → `UmsAdminController.logout`。
  - 输入：`Principal principal`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:110)。
  - 调用：UmsAdminService.logout；权限：配置白名单放行；方法内可能仍依赖登录主体。
- **根据用户名或姓名分页获取用户列表**：`GET /admin/list` → `UmsAdminController.list`。
  - 输入：`@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<UmsAdmin>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:118)。
  - 调用：UmsAdminService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **获取指定用户信息**：`GET /admin/{id}` → `UmsAdminController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<UmsAdmin>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:128)。
  - 调用：UmsAdminService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **修改指定用户信息**：`POST /admin/update/{id}` → `UmsAdminController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsAdmin admin`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:136)。
  - 调用：UmsAdminService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **修改指定用户密码**：`POST /admin/updatePassword` → `UmsAdminController.updatePassword`。
  - 输入：`@Validated @RequestBody UpdateAdminPasswordParam updatePasswordParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:147)。
  - 调用：UmsAdminService.updatePassword；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **删除指定用户信息**：`POST /admin/delete/{id}` → `UmsAdminController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:165)。
  - 调用：UmsAdminService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **修改帐号状态**：`POST /admin/updateStatus/{id}` → `UmsAdminController.updateStatus`。
  - 输入：`@PathVariable Long id,@RequestParam(value = "status") Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:176)。
  - 调用：UmsAdminService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **给用户分配角色**：`POST /admin/role/update` → `UmsAdminController.updateRole`。
  - 输入：`@RequestParam("adminId") Long adminId, @RequestParam("roleIds") List<Long> roleIds`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:189)。
  - 调用：UmsAdminService.updateRole；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- **获取指定用户的角色**：`GET /admin/role/{adminId}` → `UmsAdminController.getRoleList`。
  - 输入：`@PathVariable Long adminId`。
  - 输出：`CommonResult<List<UmsRole>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:201)。
  - 调用：UmsAdminService.getRoleList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。

## REQ-MEMBERLEVEL-001 查询会员等级

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】按defaultStatus查询等级列表，供商品会员价等选择。
- 异常与范围边界：未发现此Controller提供会员等级创建/编辑或完整会员管理。
- 数据表/集合：ums_member_level。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[UmsMemberLevelController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMemberLevelController.java:1)。
- Service证据：[UmsMemberLevelServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMemberLevelServiceImpl.java:1)。

### 输入、输出及操作入口

- **查询所有会员等级**：`GET /memberLevel/list` → `UmsMemberLevelController.list`。
  - 输入：`@RequestParam("defaultStatus") Integer defaultStatus`。
  - 输出：`CommonResult<List<UmsMemberLevel>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMemberLevelController.java:31)。
  - 调用：UmsMemberLevelService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：30:会员等级管理 (/memberLevel/**)。

## REQ-PERMISSION-001 维护后台菜单

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】创建/编辑时由父节点设置level；按父ID分页、详情、删除、树查询和hidden变更。
- 异常与范围边界：菜单隐藏与后端资源授权独立；删除不代表自动回收所有关联资源。
- 数据表/集合：ums_menu。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[UmsMenuController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:1)。
- Service证据：[UmsMenuServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加后台菜单**：`POST /menu/create` → `UmsMenuController.create`。
  - 输入：`@RequestBody UmsMenu umsMenu`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:31)。
  - 调用：UmsMenuService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **修改后台菜单**：`POST /menu/update/{id}` → `UmsMenuController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsMenu umsMenu`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:43)。
  - 调用：UmsMenuService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **根据ID获取菜单详情**：`GET /menu/{id}` → `UmsMenuController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<UmsMenu>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:56)。
  - 调用：UmsMenuService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **根据ID删除后台菜单**：`POST /menu/delete/{id}` → `UmsMenuController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:64)。
  - 调用：UmsMenuService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **分页查询后台菜单**：`GET /menu/list/{parentId}` → `UmsMenuController.list`。
  - 输入：`@PathVariable Long parentId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<UmsMenu>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:76)。
  - 调用：UmsMenuService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **树形结构返回所有菜单列表**：`GET /menu/treeList` → `UmsMenuController.treeList`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<UmsMenuNode>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:86)。
  - 调用：UmsMenuService.treeList；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- **修改菜单显示状态**：`POST /menu/updateHidden/{id}` → `UmsMenuController.updateHidden`。
  - 输入：`@PathVariable Long id, @RequestParam("hidden") Integer hidden`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:94)。
  - 调用：UmsMenuService.updateHidden；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。

## REQ-PERMISSION-002 维护资源分类

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】新增设创建时间，提供全部查询、修改与删除。
- 异常与范围边界：资源分类仅用于整理资源，未见按分类自动授权整组资源的机制。
- 数据表/集合：ums_resource_category。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[UmsResourceCategoryController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:1)。
- Service证据：[UmsResourceCategoryServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:1)。

### 输入、输出及操作入口

- **查询所有后台资源分类**：`GET /resourceCategory/listAll` → `UmsResourceCategoryController.listAll`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<UmsResourceCategory>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:28)。
  - 调用：UmsResourceCategoryService.listAll；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- **添加后台资源分类**：`POST /resourceCategory/create` → `UmsResourceCategoryController.create`。
  - 输入：`@RequestBody UmsResourceCategory umsResourceCategory`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:36)。
  - 调用：UmsResourceCategoryService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- **修改后台资源分类**：`POST /resourceCategory/update/{id}` → `UmsResourceCategoryController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsResourceCategory umsResourceCategory`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:48)。
  - 调用：UmsResourceCategoryService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- **根据ID删除后台资源分类**：`POST /resourceCategory/delete/{id}` → `UmsResourceCategoryController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:61)。
  - 调用：UmsResourceCategoryService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。

## REQ-PERMISSION-003 维护URL资源

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】提供资源增删改查；写操作后清当前进程动态权限Map，更新/删除清相关管理员资源缓存。
- 异常与范围边界：规则匹配URL而非HTTP动词；进程内刷新没有找到跨实例广播。
- 数据表/集合：ums_resource,ums_role_resource_relation,ums_admin_role_relation。
- 中间件：Redis资源缓存失效；本进程权限Map；无MQ/ES。
- Controller证据：[UmsResourceController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:1)。
- Service证据：[UmsResourceServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加后台资源**：`POST /resource/create` → `UmsResourceController.create`。
  - 输入：`@RequestBody UmsResource umsResource`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:33)。
  - 调用：DynamicSecurityMetadataSource.clearDataSource、UmsResourceService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- **修改后台资源**：`POST /resource/update/{id}` → `UmsResourceController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsResource umsResource`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:46)。
  - 调用：DynamicSecurityMetadataSource.clearDataSource、UmsResourceService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- **根据ID获取资源详情**：`GET /resource/{id}` → `UmsResourceController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<UmsResource>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:60)。
  - 调用：UmsResourceService.getItem；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- **根据ID删除后台资源**：`POST /resource/delete/{id}` → `UmsResourceController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:68)。
  - 调用：DynamicSecurityMetadataSource.clearDataSource、UmsResourceService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- **分页模糊查询后台资源**：`GET /resource/list` → `UmsResourceController.list`。
  - 输入：`@RequestParam(required = false) Long categoryId, @RequestParam(required = false) String nameKeyword, @RequestParam(required = false) String urlKeyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<UmsResource>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:81)。
  - 调用：UmsResourceService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- **查询所有后台资源**：`GET /resource/listAll` → `UmsResourceController.listAll`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<UmsResource>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:93)。
  - 调用：UmsResourceService.listAll；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。

## REQ-PERMISSION-004 维护角色及授权

- 使用者：后台管理员（写接口按动态资源授权；白名单入口单列）。
- 处理流程与业务规则：【已确认事实】角色增删改/启停/查询；菜单和资源分配先删除旧关系再插入新关系，资源分配清成员资源缓存。
- 异常与范围边界：权限查询未过滤角色status；不能仅凭字段断言角色禁用实时失权。
- 数据表/集合：ums_role,ums_role_menu_relation,ums_role_resource_relation,ums_menu,ums_resource,ums_admin_role_relation。
- 中间件：Redis资源缓存失效；无MQ/ES。
- Controller证据：[UmsRoleController](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:1)。
- Service证据：[UmsRoleServiceImpl](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加角色**：`POST /role/create` → `UmsRoleController.create`。
  - 输入：`@RequestBody UmsRole role`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:29)。
  - 调用：UmsRoleService.create；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **修改角色**：`POST /role/update/{id}` → `UmsRoleController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsRole role`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:40)。
  - 调用：UmsRoleService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **批量删除角色**：`POST /role/delete` → `UmsRoleController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:51)。
  - 调用：UmsRoleService.delete；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **获取所有角色**：`GET /role/listAll` → `UmsRoleController.listAll`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<UmsRole>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:62)。
  - 调用：UmsRoleService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **根据角色名称分页获取角色列表**：`GET /role/list` → `UmsRoleController.list`。
  - 输入：`@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<CommonPage<UmsRole>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:70)。
  - 调用：UmsRoleService.list；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **修改角色状态**：`POST /role/updateStatus/{id}` → `UmsRoleController.updateStatus`。
  - 输入：`@PathVariable Long id, @RequestParam(value = "status") Integer status`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:80)。
  - 调用：UmsRoleService.update；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **获取角色相关菜单**：`GET /role/listMenu/{roleId}` → `UmsRoleController.listMenu`。
  - 输入：`@PathVariable Long roleId`。
  - 输出：`CommonResult<List<UmsMenu>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:93)。
  - 调用：UmsRoleService.listMenu；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **获取角色相关资源**：`GET /role/listResource/{roleId}` → `UmsRoleController.listResource`。
  - 输入：`@PathVariable Long roleId`。
  - 输出：`CommonResult<List<UmsResource>>`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:101)。
  - 调用：UmsRoleService.listResource；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **给角色分配菜单**：`POST /role/allocMenu` → `UmsRoleController.allocMenu`。
  - 输入：`@RequestParam Long roleId, @RequestParam List<Long> menuIds`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:109)。
  - 调用：UmsRoleService.allocMenu；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- **给角色分配资源**：`POST /role/allocResource` → `UmsRoleController.allocResource`。
  - 输入：`@RequestParam Long roleId, @RequestParam List<Long> resourceIds`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:117)。
  - 调用：UmsRoleService.allocResource；权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。

## REQ-PAY-001 支付宝网页支付与查询通知

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】电脑和手机支付直接使用请求订单号/金额/标题生成HTML；notify验签且TRADE_SUCCESS时按订单号处理支付；query成功时也可更新订单。
- 异常与范围边界：notify返回String未ResponseBody；未见退款；金额/归属完整核对未见；SDK错误处理可能返回null后继续访问。
- 数据表/集合：oms_order,oms_order_item,pms_sku_stock（经订单Service）。
- 中间件：支付宝SDK；无直接Redis/MQ/ES。
- Controller证据：[AlipayController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:1)。
- Service证据：[AlipayServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:1)。

### 输入、输出及操作入口

- **支付宝电脑网站支付**：`GET /alipay/pay` → `AlipayController.pay`。
  - 输入：`AliPayParam aliPayParam, HttpServletResponse response`。
  - 输出：`void`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:39)。
  - 调用：AlipayConfig.getCharset、AlipayService.pay；权限：配置白名单放行。
- **支付宝手机网站支付**：`GET /alipay/webPay` → `AlipayController.webPay`。
  - 输入：`AliPayParam aliPayParam, HttpServletResponse response`。
  - 输出：`void`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:48)。
  - 调用：AlipayConfig.getCharset、AlipayService.webPay；权限：配置白名单放行。
- **支付宝异步回调**：`POST /alipay/notify` → `AlipayController.notify`。
  - 输入：`HttpServletRequest request`。
  - 输出：`String`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:57)。
  - 调用：AlipayService.notify；权限：配置白名单放行。
- **支付宝统一收单线下交易查询**：`GET /alipay/query` → `AlipayController.query`。
  - 输入：`String outTradeNo, String tradeNo`。
  - 输出：`CommonResult<String>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:69)。
  - 调用：AlipayService.query；权限：配置白名单放行。

## REQ-HOME-001 展示商城首页

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】广告、推荐品牌、当前活动/场次、秒杀商品、新品、人气、专题聚合；分类按显示状态；推荐商品接口实际分页返回未删已上架商品。
- 异常与范围边界：首页广告只筛type1/status1；推荐商品不是个性化；当前场次查询未筛status；空活动返回空内容对象。
- 数据表/集合：sms_home_advertise,sms_home_brand,sms_home_new_product,sms_home_recommend_product,sms_home_recommend_subject,sms_flash_promotion,sms_flash_promotion_session,sms_flash_promotion_product_relation,pms_product,pms_brand,pms_product_category,cms_subject。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[HomeController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:1)。
- Service证据：[HomeServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:1)。

### 输入、输出及操作入口

- **首页内容信息展示**：`GET /home/content` → `HomeController.content`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<HomeContentResult>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:31)。
  - 调用：HomeService.content；权限：配置白名单放行。
- **分页获取推荐商品**：`GET /home/recommendProductList` → `HomeController.recommendProductList`。
  - 输入：`@RequestParam(value = "pageSize", defaultValue = "4") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<List<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:39)。
  - 调用：HomeService.recommendProductList；权限：配置白名单放行。
- **获取首页商品分类**：`GET /home/productCateList/{parentId}` → `HomeController.getProductCateList`。
  - 输入：`@PathVariable Long parentId`。
  - 输出：`CommonResult<List<PmsProductCategory>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:48)。
  - 调用：HomeService.getProductCateList；权限：配置白名单放行。
- **根据分类获取专题**：`GET /home/subjectList` → `HomeController.getSubjectList`。
  - 输入：`@RequestParam(required = false) Long cateId, @RequestParam(value = "pageSize", defaultValue = "4") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<List<CmsSubject>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:56)。
  - 调用：HomeService.getSubjectList；权限：配置白名单放行。
- **分页获取人气推荐商品**：`GET /home/hotProductList` → `HomeController.hotProductList`。
  - 输入：`@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize`。
  - 输出：`CommonResult<List<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:66)。
  - 调用：HomeService.hotProductList；权限：配置白名单放行。
- **分页获取新品推荐商品**：`GET /home/newProductList` → `HomeController.newProductList`。
  - 输入：`@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize`。
  - 输出：`CommonResult<List<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:75)。
  - 调用：HomeService.newProductList；权限：配置白名单放行。

## REQ-MEMBERDATA-001 关注品牌

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】当前会员+品牌先查重复；按sqlEnable读取品牌补信息；保存Mongo，按会员查询/取消/清空。
- 异常与范围边界：品牌ID为空或SQL品牌不存在返回0；先查后写未证明并发唯一。
- 数据表/集合：pms_brand（可选读取）；Mongo MemberBrandAttention。
- 中间件：MongoDB；认证可读Redis，无直接业务MQ/ES。
- Controller证据：[MemberAttentionController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:1)。
- Service证据：[MemberAttentionServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加品牌关注**：`POST /member/attention/add` → `MemberAttentionController.add`。
  - 输入：`@RequestBody MemberBrandAttention memberBrandAttention`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:27)。
  - 调用：MemberAttentionService.add；权限：需会员认证；对象归属另看业务方法。
- **取消品牌关注**：`POST /member/attention/delete` → `MemberAttentionController.delete`。
  - 输入：`Long brandId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:39)。
  - 调用：MemberAttentionService.delete；权限：需会员认证；对象归属另看业务方法。
- **分页查询当前用户品牌关注列表**：`GET /member/attention/list` → `MemberAttentionController.list`。
  - 输入：`@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<MemberBrandAttention>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:51)。
  - 调用：MemberAttentionService.list；权限：需会员认证；对象归属另看业务方法。
- **根据品牌ID获取品牌关注详情**：`GET /member/attention/detail` → `MemberAttentionController.detail`。
  - 输入：`@RequestParam Long brandId`。
  - 输出：`CommonResult<MemberBrandAttention>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:60)。
  - 调用：MemberAttentionService.detail；权限：需会员认证；对象归属另看业务方法。
- **清空当前用户品牌关注列表**：`POST /member/attention/clear` → `MemberAttentionController.clear`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:68)。
  - 调用：MemberAttentionService.clear；权限：需会员认证；对象归属另看业务方法。

## REQ-MEMBERDATA-002 收藏商品

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】按当前会员+商品查重复；按sqlEnable读取未删除商品信息；保存Mongo；按会员查询、取消和清空。
- 异常与范围边界：商品ID为空、商品不存在/已删返回0；无已声明的联合唯一约束。
- 数据表/集合：pms_product（可选读取）；Mongo MemberProductCollection。
- 中间件：MongoDB；认证可读Redis，无直接业务MQ/ES。
- Controller证据：[MemberProductCollectionController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:1)。
- Service证据：[MemberCollectionServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加商品收藏**：`POST /member/productCollection/add` → `MemberProductCollectionController.add`。
  - 输入：`@RequestBody MemberProductCollection productCollection`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:28)。
  - 调用：MemberCollectionService.add；权限：需会员认证；对象归属另看业务方法。
- **删除商品收藏**：`POST /member/productCollection/delete` → `MemberProductCollectionController.delete`。
  - 输入：`Long productId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:40)。
  - 调用：MemberCollectionService.delete；权限：需会员认证；对象归属另看业务方法。
- **显示当前用户商品收藏列表**：`GET /member/productCollection/list` → `MemberProductCollectionController.list`。
  - 输入：`@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<MemberProductCollection>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:52)。
  - 调用：MemberCollectionService.list；权限：需会员认证；对象归属另看业务方法。
- **显示商品收藏详情**：`GET /member/productCollection/detail` → `MemberProductCollectionController.detail`。
  - 输入：`@RequestParam Long productId`。
  - 输出：`CommonResult<MemberProductCollection>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:61)。
  - 调用：MemberCollectionService.detail；权限：需会员认证；对象归属另看业务方法。
- **清空当前用户商品收藏列表**：`POST /member/productCollection/clear` → `MemberProductCollectionController.clear`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:69)。
  - 调用：MemberCollectionService.clear；权限：需会员认证；对象归属另看业务方法。

## REQ-MEMBERDATA-003 记录商品浏览

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】写当前会员、创建时间并重置ID；开关控制SQL补商品信息；按当前会员时间倒序查/清空；可按ID列表删除。
- 异常与范围边界：按ID列表删除未加会员条件；新增每次独立写，不按商品去重。
- 数据表/集合：pms_product（可选读取）；Mongo MemberReadHistory。
- 中间件：MongoDB；认证可读Redis，无直接业务MQ/ES。
- Controller证据：[MemberReadHistoryController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:1)。
- Service证据：[MemberReadHistoryServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:1)。

### 输入、输出及操作入口

- **创建浏览记录**：`POST /member/readHistory/create` → `MemberReadHistoryController.create`。
  - 输入：`@RequestBody MemberReadHistory memberReadHistory`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:30)。
  - 调用：MemberReadHistoryService.create；权限：需会员认证；对象归属另看业务方法。
- **删除浏览记录**：`POST /member/readHistory/delete` → `MemberReadHistoryController.delete`。
  - 输入：`@RequestParam("ids") List<String> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:42)。
  - 调用：MemberReadHistoryService.delete；权限：需会员认证；对象归属另看业务方法。
- **清空浏览记录**：`POST /member/readHistory/clear` → `MemberReadHistoryController.clear`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:54)。
  - 调用：MemberReadHistoryService.clear；权限：需会员认证；对象归属另看业务方法。
- **分页获取浏览记录**：`GET /member/readHistory/list` → `MemberReadHistoryController.list`。
  - 输入：`@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<MemberReadHistory>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:62)。
  - 调用：MemberReadHistoryService.list；权限：需会员认证；对象归属另看业务方法。

## REQ-CART-001 维护购物车并计算促销

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】按当前会员及商品/SKU合并数量；列表可带促销；按本人ID更新数量、删除或清空；改规格先删旧项再add。
- 异常与范围边界：空cartIds在listPromotion中不会筛选，实际选择全部；改规格旧项删除缺会员过滤；未见统一正数量校验。
- 数据表/集合：oms_cart_item,pms_product,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,pms_product_attribute,pms_product_attribute_value。
- 中间件：无直接业务Redis/MQ/ES；公共认证用Redis。
- Controller证据：[OmsCartItemController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:1)。
- Service证据：[OmsCartItemServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:1)、[UmsMemberServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加商品到购物车**：`POST /cart/add` → `OmsCartItemController.add`。
  - 输入：`@RequestBody OmsCartItem cartItem`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:33)。
  - 调用：OmsCartItemService.add；权限：需会员认证；对象归属另看业务方法。
- **获取当前会员的购物车列表**：`GET /cart/list` → `OmsCartItemController.list`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<OmsCartItem>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:44)。
  - 调用：OmsCartItemService.list、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。
- **获取当前会员的购物车列表,包括促销信息**：`GET /cart/list/promotion` → `OmsCartItemController.listPromotion`。
  - 输入：`@RequestParam(required = false) List<Long> cartIds`。
  - 输出：`CommonResult<List<CartPromotionItem>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:52)。
  - 调用：OmsCartItemService.listPromotion、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。
- **修改购物车中指定商品的数量**：`GET /cart/update/quantity` → `OmsCartItemController.updateQuantity`。
  - 输入：`@RequestParam Long id, @RequestParam Integer quantity`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:60)。
  - 调用：OmsCartItemService.updateQuantity、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。
- **获取购物车中指定商品的规格,用于重选规格**：`GET /cart/getProduct/{productId}` → `OmsCartItemController.getCartProduct`。
  - 输入：`@PathVariable Long productId`。
  - 输出：`CommonResult<CartProduct>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:72)。
  - 调用：OmsCartItemService.getCartProduct；权限：需会员认证；对象归属另看业务方法。
- **修改购物车中商品的规格**：`POST /cart/update/attr` → `OmsCartItemController.updateAttr`。
  - 输入：`@RequestBody OmsCartItem cartItem`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:80)。
  - 调用：OmsCartItemService.updateAttr；权限：需会员认证；对象归属另看业务方法。
- **删除购物车中的指定商品**：`POST /cart/delete` → `OmsCartItemController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:91)。
  - 调用：OmsCartItemService.delete、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。
- **清空当前会员的购物车**：`POST /cart/clear` → `OmsCartItemController.clear`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:102)。
  - 调用：OmsCartItemService.clear、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。

## REQ-PORTALORDER-001 会员订单操作

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】确认单、下单、支付状态写入、取消及重新发送取消消息、订单列表详情、确认收货、删除；流程见正文REQ-ORDER-001至004。
- 异常与范围边界：接口之间归属和状态约束不同；不能由名称假定全部检查；库存/积分/支付风险见第23章。
- 数据表/集合：oms_order,oms_order_item,oms_cart_item,oms_order_setting,pms_sku_stock,sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,ums_member,ums_member_receive_address,ums_integration_consume_setting,pms_product,pms_product_ladder,pms_product_full_reduction。
- 中间件：Redis会员缓存/订单计数；RabbitMQ取消；无ES。
- Controller证据：[OmsPortalOrderController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:1)。
- Service证据：[OmsPortalOrderServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:1)。

### 输入、输出及操作入口

- **根据购物车信息生成确认单**：`POST /order/generateConfirmOrder` → `OmsPortalOrderController.generateConfirmOrder`。
  - 输入：`@RequestBody List<Long> cartIds`。
  - 输出：`CommonResult<ConfirmOrderResult>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:35)。
  - 调用：OmsPortalOrderService.generateConfirmOrder；权限：需会员认证；对象归属另看业务方法。
- **根据购物车信息生成订单**：`POST /order/generateOrder` → `OmsPortalOrderController.generateOrder`。
  - 输入：`@RequestBody OrderParam orderParam`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:43)。
  - 调用：OmsPortalOrderService.generateOrder；权限：需会员认证；对象归属另看业务方法。
- **用户支付成功的回调**：`POST /order/paySuccess` → `OmsPortalOrderController.paySuccess`。
  - 输入：`@RequestParam Long orderId,@RequestParam Integer payType`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:51)。
  - 调用：OmsPortalOrderService.paySuccess；权限：需会员认证；对象归属另看业务方法。
- **自动取消超时订单**：`POST /order/cancelTimeOutOrder` → `OmsPortalOrderController.cancelTimeOutOrder`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:59)。
  - 调用：OmsPortalOrderService.cancelTimeOutOrder；权限：需会员认证；对象归属另看业务方法。
- **取消单个超时订单**：`POST /order/cancelOrder` → `OmsPortalOrderController.cancelOrder`。
  - 输入：`Long orderId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:67)。
  - 调用：OmsPortalOrderService.sendDelayMessageCancelOrder；权限：需会员认证；对象归属另看业务方法。
- **按状态分页获取用户订单列表**：`GET /order/list` → `OmsPortalOrderController.list`。
  - 输入：`@RequestParam Integer status, @RequestParam(required = false, defaultValue = "1") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<OmsOrderDetail>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:77)。
  - 调用：OmsPortalOrderService.list；权限：需会员认证；对象归属另看业务方法。
- **根据ID获取订单详情**：`GET /order/detail/{orderId}` → `OmsPortalOrderController.detail`。
  - 输入：`@PathVariable Long orderId`。
  - 输出：`CommonResult<OmsOrderDetail>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:87)。
  - 调用：OmsPortalOrderService.detail；权限：需会员认证；对象归属另看业务方法。
- **用户取消订单**：`POST /order/cancelUserOrder` → `OmsPortalOrderController.cancelUserOrder`。
  - 输入：`Long orderId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:95)。
  - 调用：OmsPortalOrderService.cancelOrder；权限：需会员认证；对象归属另看业务方法。
- **用户确认收货**：`POST /order/confirmReceiveOrder` → `OmsPortalOrderController.confirmReceiveOrder`。
  - 输入：`Long orderId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:103)。
  - 调用：OmsPortalOrderService.confirmReceiveOrder；权限：需会员认证；对象归属另看业务方法。
- **用户删除订单**：`POST /order/deleteOrder` → `OmsPortalOrderController.deleteOrder`。
  - 输入：`Long orderId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:111)。
  - 调用：OmsPortalOrderService.deleteOrder；权限：需会员认证；对象归属另看业务方法。

## REQ-PORTALRETURN-001 提交退货申请

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】复制请求对象到申请表，设创建时间与status0。
- 异常与范围边界：未查询订单归属、支付状态及可退数量；不执行退款。
- 数据表/集合：oms_order_return_apply。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[OmsPortalOrderReturnApplyController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderReturnApplyController.java:1)。
- Service证据：[OmsPortalOrderReturnApplyServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderReturnApplyServiceImpl.java:1)。

### 输入、输出及操作入口

- **申请退货**：`POST /returnApply/create` → `OmsPortalOrderReturnApplyController.create`。
  - 输入：`@RequestBody OmsOrderReturnApplyParam returnApply`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderReturnApplyController.java:29)。
  - 调用：OmsPortalOrderReturnApplyService.create；权限：需会员认证；对象归属另看业务方法。

## REQ-BROWSE-001 浏览品牌与品牌商品

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】推荐品牌按首页品牌表；品牌详情按ID；品牌商品按未删除且上架分页。
- 异常与范围边界：品牌不存在可返回null；不是后台品牌管理。
- 数据表/集合：pms_brand,sms_home_brand,pms_product。
- 中间件：未见直接Redis/MQ/ES。
- Controller证据：[PmsPortalBrandController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:1)。
- Service证据：[PmsPortalBrandServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java:1)。

### 输入、输出及操作入口

- **分页获取推荐品牌**：`GET /brand/recommendList` → `PmsPortalBrandController.recommendList`。
  - 输入：`@RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum`。
  - 输出：`CommonResult<List<PmsBrand>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:31)。
  - 调用：PmsPortalBrandService.recommendList；权限：配置白名单放行。
- **获取品牌详情**：`GET /brand/detail/{brandId}` → `PmsPortalBrandController.detail`。
  - 输入：`@PathVariable Long brandId`。
  - 输出：`CommonResult<PmsBrand>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:40)。
  - 调用：PmsPortalBrandService.detail；权限：配置白名单放行。
- **分页获取品牌相关商品**：`GET /brand/productList` → `PmsPortalBrandController.productList`。
  - 输入：`@RequestParam Long brandId, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:48)。
  - 调用：PmsPortalBrandService.productList；权限：配置白名单放行。

## REQ-BROWSE-002 查询商品、分类树与详情

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】search用MySQL名称LIKE及品牌/分类筛选，排除已删未上架；排序ID/销量/价格；详情聚合品牌、属性/SKU、条件促销及可用券。
- 异常与范围边界：详情按主键取商品后继续读取，不像search一样显式检查上架/删除；分类树读取所有分类。
- 数据表/集合：pms_product,pms_product_category,pms_brand,pms_product_attribute,pms_product_attribute_value,pms_sku_stock,pms_product_ladder,pms_product_full_reduction,sms_coupon,sms_coupon_product_relation,sms_coupon_product_category_relation。
- 中间件：本搜索走MySQL；没有直接ES调用。
- Controller证据：[PmsPortalProductController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:1)。
- Service证据：[PmsPortalProductServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java:1)。

### 输入、输出及操作入口

- **综合搜索、筛选、排序**：`GET /product/search` → `PmsPortalProductController.search`。
  - 输入：`@RequestParam(required = false) String keyword, @RequestParam(required = false) Long brandId, @RequestParam(required = false) Long productCategoryId, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize, @RequestParam(required = false, defaultValue = "0") Integer sort`。
  - 输出：`CommonResult<CommonPage<PmsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:37)。
  - 调用：PmsPortalProductService.search；权限：配置白名单放行。
- **以树形结构获取所有商品分类**：`GET /product/categoryTreeList` → `PmsPortalProductController.categoryTreeList`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<PmsProductCategoryNode>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:50)。
  - 调用：PmsPortalProductService.categoryTreeList；权限：配置白名单放行。
- **获取前台商品详情**：`GET /product/detail/{id}` → `PmsPortalProductController.detail`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<PmsPortalProductDetail>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:58)。
  - 调用：PmsPortalProductService.detail；权限：配置白名单放行。

## REQ-MEMBER-001 会员账号及验证码

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】手机号验证码写Redis并直接返回；注册验证验证码、查用户名/电话、BCrypt密码、设默认等级；登录/Token刷新/当前信息/验证码改密。
- 异常与范围边界：未发现短信发送服务；验证码验证不销毁；会员login不显式检查isEnabled。
- 数据表/集合：ums_member,ums_member_level。
- 中间件：Redis会员缓存/验证码；无MQ/ES。
- Controller证据：[UmsMemberController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:1)。
- Service证据：[UmsMemberServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:1)。

### 输入、输出及操作入口

- **会员注册**：`POST /sso/register` → `UmsMemberController.register`。
  - 输入：`@RequestParam String username, @RequestParam String password, @RequestParam String telephone, @RequestParam String authCode`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:39)。
  - 调用：UmsMemberService.register；权限：配置白名单放行。
- **会员登录**：`POST /sso/login` → `UmsMemberController.login`。
  - 输入：`@RequestParam String username, @RequestParam String password`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:50)。
  - 调用：UmsMemberService.login；权限：配置白名单放行。
- **获取会员信息**：`GET /sso/info` → `UmsMemberController.info`。
  - 输入：`Principal principal`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:65)。
  - 调用：UmsMemberService.getCurrentMember；权限：配置白名单放行。
- **获取验证码**：`GET /sso/getAuthCode` → `UmsMemberController.getAuthCode`。
  - 输入：`@RequestParam String telephone`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:76)。
  - 调用：UmsMemberService.generateAuthCode；权限：配置白名单放行。
- **会员修改密码**：`POST /sso/updatePassword` → `UmsMemberController.updatePassword`。
  - 输入：`@RequestParam String telephone, @RequestParam String password, @RequestParam String authCode`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:84)。
  - 调用：UmsMemberService.updatePassword；权限：配置白名单放行。
- **刷新token**：`GET /sso/refreshToken` → `UmsMemberController.refreshToken`。
  - 输入：`HttpServletRequest request`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:95)。
  - 调用：UmsMemberService.refreshToken；权限：配置白名单放行。

## REQ-COUPON-001 领取并查询会员优惠券

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】校验券存在、剩余数、enableTime、领取数量；写领取历史并减数量；按会员查历史、可用券、商品券、购物车可用/不可用券。
- 异常与范围边界：库存不足/未到领取时间/限领抛ApiException；listCart门槛用intValue，日期与精度边界见正文；无严格并发扣减。
- 数据表/集合：sms_coupon,sms_coupon_history,sms_coupon_product_relation,sms_coupon_product_category_relation,pms_product；购物车券查询另读取购物车及促销。
- 中间件：无直接业务Redis/MQ/ES；认证用Redis。
- Controller证据：[UmsMemberCouponController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:1)。
- Service证据：[OmsCartItemServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:1)、[UmsMemberCouponServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:1)、[UmsMemberServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:1)。

### 输入、输出及操作入口

- **领取指定优惠券**：`POST /member/coupon/add/{couponId}` → `UmsMemberCouponController.add`。
  - 输入：`@PathVariable Long couponId`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:40)。
  - 调用：UmsMemberCouponService.add；权限：需会员认证；对象归属另看业务方法。
- **获取会员优惠券历史列表**：`GET /member/coupon/listHistory` → `UmsMemberCouponController.listHistory`。
  - 输入：`@RequestParam(value = "useStatus", required = false) Integer useStatus`。
  - 输出：`CommonResult<List<SmsCouponHistory>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:50)。
  - 调用：UmsMemberCouponService.listHistory；权限：需会员认证；对象归属另看业务方法。
- **获取会员优惠券列表**：`GET /member/coupon/list` → `UmsMemberCouponController.list`。
  - 输入：`@RequestParam(value = "useStatus", required = false) Integer useStatus`。
  - 输出：`CommonResult<List<SmsCoupon>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:60)。
  - 调用：UmsMemberCouponService.list；权限：需会员认证；对象归属另看业务方法。
- **获取登录会员购物车的相关优惠券**：`GET /member/coupon/list/cart/{type}` → `UmsMemberCouponController.listCart`。
  - 输入：`@PathVariable Integer type`。
  - 输出：`CommonResult<List<SmsCouponHistoryDetail>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:70)。
  - 调用：OmsCartItemService.listPromotion、UmsMemberCouponService.listCart、UmsMemberService.getCurrentMember；权限：需会员认证；对象归属另看业务方法。
- **获取当前商品相关优惠券**：`GET /member/coupon/listByProduct/{productId}` → `UmsMemberCouponController.listByProduct`。
  - 输入：`@PathVariable Long productId`。
  - 输出：`CommonResult<List<SmsCoupon>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:79)。
  - 调用：UmsMemberCouponService.listByProduct；权限：需会员认证；对象归属另看业务方法。

## REQ-ADDRESS-001 维护会员地址

- 使用者：商城会员；公开内容/SSO/支付宝入口按配置白名单放行。
- 处理流程与业务规则：【已确认事实】新地址覆盖memberId为当前会员；列表、详情、删改按memberId过滤；更新默认地址时先清同会员原默认标记。
- 异常与范围边界：新增不执行与更新相同的默认地址清理；详情未找到返回null，不能保证下单后续友好报错。
- 数据表/集合：ums_member_receive_address。
- 中间件：无直接业务Redis/MQ/ES；认证用Redis。
- Controller证据：[UmsMemberReceiveAddressController](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:1)。
- Service证据：[UmsMemberReceiveAddressServiceImpl](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:1)。

### 输入、输出及操作入口

- **添加收货地址**：`POST /member/address/add` → `UmsMemberReceiveAddressController.add`。
  - 输入：`@RequestBody UmsMemberReceiveAddress address`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:28)。
  - 调用：UmsMemberReceiveAddressService.add；权限：需会员认证；对象归属另看业务方法。
- **删除收货地址**：`POST /member/address/delete/{id}` → `UmsMemberReceiveAddressController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:39)。
  - 调用：UmsMemberReceiveAddressService.delete；权限：需会员认证；对象归属另看业务方法。
- **修改收货地址**：`POST /member/address/update/{id}` → `UmsMemberReceiveAddressController.update`。
  - 输入：`@PathVariable Long id, @RequestBody UmsMemberReceiveAddress address`。
  - 输出：`CommonResult`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:50)。
  - 调用：UmsMemberReceiveAddressService.update；权限：需会员认证；对象归属另看业务方法。
- **获取所有收货地址**：`GET /member/address/list` → `UmsMemberReceiveAddressController.list`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<List<UmsMemberReceiveAddress>>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:61)。
  - 调用：UmsMemberReceiveAddressService.list；权限：需会员认证；对象归属另看业务方法。
- **获取收货地址详情**：`GET /member/address/{id}` → `UmsMemberReceiveAddressController.getItem`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<UmsMemberReceiveAddress>`；实际响应分支见[方法实现](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:69)。
  - 调用：UmsMemberReceiveAddressService.getItem；权限：需会员认证；对象归属另看业务方法。

## REQ-SEARCH-001 管理和检索ES商品索引

- 使用者：搜索HTTP调用者；项目未声明应用内认证，外部控制无法确认。
- 处理流程与业务规则：【已确认事实】importAll/create读取未删已上架MySQL商品和属性后save；删索引按ID；简单搜索、组合过滤排序、相似商品与筛选聚合。
- 异常与范围边界：显式接口同步，无后台自动同步；importAll不删除旧文档；应用未见Security链，外围访问控制未知。
- 数据表/集合：pms_product,pms_product_attribute_value,pms_product_attribute。
- 中间件：Elasticsearch pms索引；没有业务Redis/MQ。
- Controller证据：[EsProductController](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:1)。
- Service证据：[EsProductServiceImpl](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:1)。

### 输入、输出及操作入口

- **导入所有数据库中商品到ES**：`POST /esProduct/importAll` → `EsProductController.importAllList`。
  - 输入：`无方法参数`。
  - 输出：`CommonResult<Integer>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:34)。
  - 调用：EsProductService.importAll；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **根据id删除商品**：`GET /esProduct/delete/{id}` → `EsProductController.delete`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<Object>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:42)。
  - 调用：EsProductService.delete；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **根据id批量删除商品**：`POST /esProduct/delete/batch` → `EsProductController.delete`。
  - 输入：`@RequestParam("ids") List<Long> ids`。
  - 输出：`CommonResult<Object>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:50)。
  - 调用：EsProductService.delete；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **根据id创建商品**：`POST /esProduct/create/{id}` → `EsProductController.create`。
  - 输入：`@PathVariable Long id`。
  - 输出：`CommonResult<EsProduct>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:58)。
  - 调用：EsProductService.create；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **简单搜索**：`GET /esProduct/search/simple` → `EsProductController.search`。
  - 输入：`@RequestParam(required = false) String keyword, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<EsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:70)。
  - 调用：EsProductService.search；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **综合搜索、筛选、排序**：`GET /esProduct/search` → `EsProductController.search`。
  - 输入：`@RequestParam(required = false) String keyword, @RequestParam(required = false) Long brandId, @RequestParam(required = false) Long productCategoryId, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize, @RequestParam(required = false, defaultValue = "0") Integer sort`。
  - 输出：`CommonResult<CommonPage<EsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:81)。
  - 调用：EsProductService.search；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **根据商品id推荐商品**：`GET /esProduct/recommend/{id}` → `EsProductController.recommend`。
  - 输入：`@PathVariable Long id, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize`。
  - 输出：`CommonResult<CommonPage<EsProduct>>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:94)。
  - 调用：EsProductService.recommend；权限：该应用未发现Security过滤链；外部访问控制无法确认。
- **获取搜索的相关品牌、分类及筛选属性**：`GET /esProduct/search/relate` → `EsProductController.searchRelatedInfo`。
  - 输入：`@RequestParam(required = false) String keyword`。
  - 输出：`CommonResult<EsProductRelatedInfo>`；实际响应分支见[方法实现](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:104)。
  - 调用：EsProductService.searchRelatedInfo；权限：该应用未发现Security过滤链；外部访问控制无法确认。

## REQ-UI-001 管理前端导航与首页展示

- 【已确认事实】登录后从后端取得角色与菜单，Pinia保存用户状态并启用持久化，Axios请求附加Token。功能路由覆盖商品、订单、营销与权限；隐藏页用于编辑、分配和详情。
- 输入：登录表单、菜单选择、各业务表单及查询条件；输出：页面、列表、操作反馈。字段与请求以src/apis和src/types为准。
- 规则：无Token转登录，无角色时前端报错；菜单依据名称筛选，testMode=false。首页图表取本地数组并按日期截取，不查询经营统计接口。
- 异常：HTTP拦截器检查业务code，401提示重新登录；其他网络错误展示错误信息。
- Controller/Service/数据表：导航调用后台账号信息与角色菜单链，详见REQ-ADMIN-001；首页示例图表无统计Controller和数据库来源。
- 证据：[用户状态](D:/project/mall-admin-web/src/stores/user.ts:1)、[菜单](D:/project/mall-admin-web/src/stores/permission.ts:1)、[HTTP](D:/project/mall-admin-web/src/utils/http.ts:1)、[首页](D:/project/mall-admin-web/src/views/home/index.vue:35)。

## 教学示例的范围

mall-demo的13个接口提供品牌CRUD与RestTemplate示例，有独立应用入口，不计入233个商城业务接口。不能把演示远程HTTP调用推断为三个业务应用之间存在同样的调用链。详见附录A的mall-demo部分。
