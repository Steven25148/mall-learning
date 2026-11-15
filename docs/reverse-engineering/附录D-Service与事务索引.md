# 附录D：Service与事务证据索引

【已确认事实】按源码提取注入依赖和方法；生成Mapper按单表访问，DAO通常对应手写XML。事务索引只包含主源码，不含测试。外部资源不因这些注解自动加入数据库事务。

## 事务声明（35项）

- [mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java:22)：`@Transactional int delivery(List<OmsOrderDeliveryParam> deliveryParamList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java:28)：`@Transactional int close(List<Long> ids, String note);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java:44)：`@Transactional int updateReceiverInfo(OmsReceiverInfoParam receiverInfoParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java:50)：`@Transactional int updateMoneyInfo(OmsMoneyInfoParam moneyInfoParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java:56)：`@Transactional int updateNote(Long id, String note, Integer status);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsBrandService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsBrandService.java:27)：`@Transactional int updateBrand(Long id, PmsBrandParam pmsBrandParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductAttributeService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductAttributeService.java:25)：`@Transactional int create(PmsProductAttributeParam pmsProductAttributeParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductAttributeService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductAttributeService.java:41)：`@Transactional int delete(List<Long> ids);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductCategoryService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductCategoryService.java:18)：`@Transactional int create(PmsProductCategoryParam pmsProductCategoryParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductCategoryService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductCategoryService.java:24)：`@Transactional int update(Long id, PmsProductCategoryParam pmsProductCategoryParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java:21)：`@Transactional(isolation = Isolation.DEFAULT,propagation = Propagation.REQUIRED) int create(PmsProductParam productParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java:32)：`@Transactional int update(Long id, PmsProductParam productParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java:46)：`@Transactional int updateVerifyStatus(List<Long> ids, Integer verifyStatus, String detail);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java:17)：`@Transactional int create(SmsCouponParam couponParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java:23)：`@Transactional int delete(Long id);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsCouponService.java:29)：`@Transactional int update(Long id, SmsCouponParam couponParam);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsFlashPromotionProductRelationService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsFlashPromotionProductRelationService.java:17)：`@Transactional int create(List<SmsFlashPromotionProductRelation> relationList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeBrandService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeBrandService.java:16)：`@Transactional int create(List<SmsHomeBrand> homeBrandList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeNewProductService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeNewProductService.java:16)：`@Transactional int create(List<SmsHomeNewProduct> homeNewProductList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendProductService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendProductService.java:16)：`@Transactional int create(List<SmsHomeRecommendProduct> homeRecommendProductList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendSubjectService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendSubjectService.java:16)：`@Transactional int create(List<SmsHomeRecommendSubject> recommendSubjectList);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/UmsAdminService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/UmsAdminService.java:65)：`@Transactional int updateRole(Long adminId, List<Long> roleIds);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/UmsRoleService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/UmsRoleService.java:58)：`@Transactional int allocMenu(Long roleId, List<Long> menuIds);`
- [mall/mall-admin/src/main/java/com/macro/mall/service/UmsRoleService.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/UmsRoleService.java:64)：`@Transactional int allocResource(Long roleId, List<Long> resourceIds);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsCartItemService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsCartItemService.java:18)：`@Transactional int add(OmsCartItem cartItem);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsCartItemService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsCartItemService.java:49)：`@Transactional int updateAttr(OmsCartItem cartItem);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java:25)：`@Transactional Map<String, Object> generateOrder(OrderParam orderParam);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java:31)：`@Transactional Integer paySuccess(Long orderId, Integer payType);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java:37)：`@Transactional Integer cancelTimeOutOrder();`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java:43)：`@Transactional void cancelOrder(Long orderId);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java:74)：`@Transactional void paySuccessByOrderSn(String orderSn, Integer payType);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberCouponService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberCouponService.java:19)：`@Transactional void add(Long couponId);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberReceiveAddressService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberReceiveAddressService.java:29)：`@Transactional int update(Long id, UmsMemberReceiveAddress address);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberService.java:25)：`@Transactional void register(String username, String password, String telephone, String authCode);`
- [mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberService.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/UmsMemberService.java:36)：`@Transactional void updatePassword(String telephone, String password, String authCode);`

## CmsPrefrenceAreaServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsPrefrenceAreaServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsPrefrenceAreaServiceImpl.java:1)

注入依赖：`CmsPrefrenceAreaMapper prefrenceAreaMapper`

方法：
- `listAll()` → `List<CmsPrefrenceArea>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsPrefrenceAreaServiceImpl.java:22)。

## CmsSubjectServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsSubjectServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsSubjectServiceImpl.java:1)

注入依赖：`CmsSubjectMapper subjectMapper`

方法：
- `listAll()` → `List<CmsSubject>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsSubjectServiceImpl.java:24)。
- `list(String keyword, Integer pageNum, Integer pageSize)` → `List<CmsSubject>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/CmsSubjectServiceImpl.java:29)。

## OmsCompanyAddressServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsCompanyAddressServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsCompanyAddressServiceImpl.java:1)

注入依赖：`OmsCompanyAddressMapper companyAddressMapper`

方法：
- `list()` → `List<OmsCompanyAddress>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsCompanyAddressServiceImpl.java:21)。

## OmsOrderReturnApplyServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:1)

注入依赖：`OmsOrderReturnApplyDao returnApplyDao`；`OmsOrderReturnApplyMapper returnApplyMapper`

方法：
- `list(OmsReturnApplyQueryParam queryParam, Integer pageSize, Integer pageNum)` → `List<OmsOrderReturnApply>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:29)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:35)。
- `updateStatus(Long id, OmsUpdateStatusParam statusParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:42)。
- `getItem(Long id)` → `OmsOrderReturnApplyResult`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java:75)。

## OmsOrderReturnReasonServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:1)

注入依赖：`OmsOrderReturnReasonMapper returnReasonMapper`

方法：
- `create(OmsOrderReturnReason returnReason)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:23)。
- `update(Long id, OmsOrderReturnReason returnReason)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:29)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:35)。
- `list(Integer pageSize, Integer pageNum)` → `List<OmsOrderReturnReason>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:42)。
- `updateStatus(List<Long> ids, Integer status)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:50)。
- `getItem(Long id)` → `OmsOrderReturnReason`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnReasonServiceImpl.java:62)。

## OmsOrderServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:1)

注入依赖：`OmsOrderMapper orderMapper`；`OmsOrderDao orderDao`；`OmsOrderOperateHistoryDao orderOperateHistoryDao`；`OmsOrderOperateHistoryMapper orderOperateHistoryMapper`

方法：
- `list(OmsOrderQueryParam queryParam, Integer pageSize, Integer pageNum)` → `List<OmsOrder>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:36)。
- `delivery(List<OmsOrderDeliveryParam> deliveryParamList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:42)。
- `close(List<Long> ids, String note)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:61)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:81)。
- `detail(Long id)` → `OmsOrderDetail`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:90)。
- `updateReceiverInfo(OmsReceiverInfoParam receiverInfoParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:95)。
- `updateMoneyInfo(OmsMoneyInfoParam moneyInfoParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:119)。
- `updateNote(Long id, String note, Integer status)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java:138)。

## OmsOrderSettingServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderSettingServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderSettingServiceImpl.java:1)

注入依赖：`OmsOrderSettingMapper orderSettingMapper`

方法：
- `getItem(Long id)` → `OmsOrderSetting`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderSettingServiceImpl.java:19)。
- `update(Long id, OmsOrderSetting orderSetting)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderSettingServiceImpl.java:24)。

## OssServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java:1)

注入依赖：`int ALIYUN_OSS_EXPIRE`；`int ALIYUN_OSS_MAX_SIZE`；`String ALIYUN_OSS_CALLBACK`；`String ALIYUN_OSS_BUCKET_NAME`；`String ALIYUN_OSS_ENDPOINT`；`String ALIYUN_OSS_DIR_PREFIX`；`OSSClient ossClient`

方法：
- `policy()` → `OssPolicyResult`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java:50)。
- `callback(HttpServletRequest request)` → `OssCallbackResult`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java:90)。

## PmsBrandServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:1)

注入依赖：`PmsBrandMapper brandMapper`；`PmsProductMapper productMapper`

方法：
- `listAllBrand()` → `List<PmsBrand>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:31)。
- `createBrand(PmsBrandParam pmsBrandParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:36)。
- `updateBrand(Long id, PmsBrandParam pmsBrandParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:47)。
- `deleteBrand(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:65)。
- `deleteBrand(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:70)。
- `listBrand(String keyword, Integer showStatus, int pageNum, int pageSize)` → `List<PmsBrand>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:77)。
- `getBrand(Long id)` → `PmsBrand`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:92)。
- `updateShowStatus(List<Long> ids, Integer showStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:97)。
- `updateFactoryStatus(List<Long> ids, Integer factoryStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java:106)。

## PmsProductAttributeCategoryServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:1)

注入依赖：`PmsProductAttributeCategoryMapper productAttributeCategoryMapper`；`PmsProductAttributeCategoryDao productAttributeCategoryDao`

方法：
- `create(String name)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:27)。
- `update(Long id, String name)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:34)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:42)。
- `getItem(Long id)` → `PmsProductAttributeCategory`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:47)。
- `getList(Integer pageSize, Integer pageNum)` → `List<PmsProductAttributeCategory>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:52)。
- `getListWithAttr()` → `List<PmsProductAttributeCategoryItem>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java:58)。

## PmsProductAttributeServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:1)

注入依赖：`PmsProductAttributeMapper productAttributeMapper`；`PmsProductAttributeCategoryMapper productAttributeCategoryMapper`；`PmsProductAttributeDao productAttributeDao`

方法：
- `getList(Long cid, Integer type, Integer pageSize, Integer pageNum)` → `List<PmsProductAttribute>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:33)。
- `create(PmsProductAttributeParam pmsProductAttributeParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:42)。
- `update(Long id, PmsProductAttributeParam productAttributeParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:58)。
- `getItem(Long id)` → `PmsProductAttribute`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:66)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:71)。
- `getProductAttrInfo(Long productCategoryId)` → `List<ProductAttrInfo>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java:98)。

## PmsProductCategoryServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:1)

注入依赖：`PmsProductCategoryMapper productCategoryMapper`；`PmsProductMapper productMapper`；`PmsProductCategoryAttributeRelationDao productCategoryAttributeRelationDao`；`PmsProductCategoryAttributeRelationMapper productCategoryAttributeRelationMapper`；`PmsProductCategoryDao productCategoryDao`

方法：
- `create(PmsProductCategoryParam pmsProductCategoryParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:38)。
- `update(Long id, PmsProductCategoryParam pmsProductCategoryParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:70)。
- `getList(Long parentId, Integer pageSize, Integer pageNum)` → `List<PmsProductCategory>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:96)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:105)。
- `getItem(Long id)` → `PmsProductCategory`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:110)。
- `updateNavStatus(List<Long> ids, Integer navStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:115)。
- `updateShowStatus(List<Long> ids, Integer showStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:124)。
- `listWithChildren()` → `List<PmsProductCategoryWithChildrenItem>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductCategoryServiceImpl.java:133)。

## PmsProductServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:1)

注入依赖：`PmsProductMapper productMapper`；`PmsMemberPriceDao memberPriceDao`；`PmsMemberPriceMapper memberPriceMapper`；`PmsProductLadderDao productLadderDao`；`PmsProductLadderMapper productLadderMapper`；`PmsProductFullReductionDao productFullReductionDao`；`PmsProductFullReductionMapper productFullReductionMapper`；`PmsSkuStockDao skuStockDao`；`PmsSkuStockMapper skuStockMapper`；`PmsProductAttributeValueDao productAttributeValueDao`；`PmsProductAttributeValueMapper productAttributeValueMapper`；`CmsSubjectProductRelationDao subjectProductRelationDao`；`CmsSubjectProductRelationMapper subjectProductRelationMapper`；`CmsPrefrenceAreaProductRelationDao prefrenceAreaProductRelationDao`；`CmsPrefrenceAreaProductRelationMapper prefrenceAreaProductRelationMapper`；`PmsProductDao productDao`；`PmsProductVertifyRecordDao productVertifyRecordDao`

方法：
- `create(PmsProductParam productParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:69)。
- `getUpdateInfo(Long id)` → `PmsProductResult`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:116)。
- `update(Long id, PmsProductParam productParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:121)。
- `list(PmsProductQueryParam productQueryParam, Integer pageSize, Integer pageNum)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:207)。
- `updateVerifyStatus(List<Long> ids, Integer verifyStatus, String detail)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:234)。
- `updatePublishStatus(List<Long> ids, Integer publishStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:256)。
- `updateRecommendStatus(List<Long> ids, Integer recommendStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:265)。
- `updateNewStatus(List<Long> ids, Integer newStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:274)。
- `updateDeleteStatus(List<Long> ids, Integer deleteStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:283)。
- `list(String keyword)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java:292)。

## PmsSkuStockServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java:1)

注入依赖：`PmsSkuStockMapper skuStockMapper`；`PmsSkuStockDao skuStockDao`

方法：
- `getList(Long pid, String keyword)` → `List<PmsSkuStock>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java:27)。
- `update(Long pid, List<PmsSkuStock> skuStockList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java:37)。

## SmsCouponHistoryServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponHistoryServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponHistoryServiceImpl.java:1)

注入依赖：`SmsCouponHistoryMapper historyMapper`

方法：
- `list(Long couponId, Integer useStatus, String orderSn, Integer pageSize, Integer pageNum)` → `List<SmsCouponHistory>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponHistoryServiceImpl.java:23)。

## SmsCouponServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:1)

注入依赖：`SmsCouponMapper couponMapper`；`SmsCouponProductRelationMapper productRelationMapper`；`SmsCouponProductCategoryRelationMapper productCategoryRelationMapper`；`SmsCouponProductRelationDao productRelationDao`；`SmsCouponProductCategoryRelationDao productCategoryRelationDao`；`SmsCouponDao couponDao`

方法：
- `create(SmsCouponParam couponParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:38)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:62)。
- `update(Long id, SmsCouponParam couponParam)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:85)。
- `list(String name, Integer type, Integer pageSize, Integer pageNum)` → `List<SmsCoupon>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:108)。
- `getItem(Long id)` → `SmsCouponParam`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java:122)。

## SmsFlashPromotionProductRelationServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:1)

注入依赖：`SmsFlashPromotionProductRelationMapper relationMapper`；`SmsFlashPromotionProductRelationDao relationDao`

方法：
- `create(List<SmsFlashPromotionProductRelation> relationList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:26)。
- `update(Long id, SmsFlashPromotionProductRelation relation)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:34)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:40)。
- `getItem(Long id)` → `SmsFlashPromotionProductRelation`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:45)。
- `list(Long flashPromotionId, Long flashPromotionSessionId, Integer pageSize, Integer pageNum)` → `List<SmsFlashPromotionProduct>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:50)。
- `getCount(Long flashPromotionId, Long flashPromotionSessionId)` → `long`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionProductRelationServiceImpl.java:56)。

## SmsFlashPromotionServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:1)

注入依赖：`SmsFlashPromotionMapper flashPromotionMapper`

方法：
- `create(SmsFlashPromotion flashPromotion)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:25)。
- `update(Long id, SmsFlashPromotion flashPromotion)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:31)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:37)。
- `updateStatus(Long id, Integer status)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:42)。
- `getItem(Long id)` → `SmsFlashPromotion`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:50)。
- `list(String keyword, Integer pageSize, Integer pageNum)` → `List<SmsFlashPromotion>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java:55)。

## SmsFlashPromotionSessionServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:1)

注入依赖：`SmsFlashPromotionSessionMapper promotionSessionMapper`；`SmsFlashPromotionProductRelationService relationService`

方法：
- `create(SmsFlashPromotionSession promotionSession)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:29)。
- `update(Long id, SmsFlashPromotionSession promotionSession)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:35)。
- `updateStatus(Long id, Integer status)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:41)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:49)。
- `getItem(Long id)` → `SmsFlashPromotionSession`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:54)。
- `list()` → `List<SmsFlashPromotionSession>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:59)。
- `selectList(Long flashPromotionId)` → `List<SmsFlashPromotionSessionDetail>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java:65)。

## SmsHomeAdvertiseServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:1)

注入依赖：`SmsHomeAdvertiseMapper advertiseMapper`

方法：
- `create(SmsHomeAdvertise advertise)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:27)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:34)。
- `updateStatus(Long id, Integer status)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:41)。
- `getItem(Long id)` → `SmsHomeAdvertise`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:49)。
- `update(Long id, SmsHomeAdvertise advertise)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:54)。
- `list(String name, Integer type, String endTime, Integer pageSize, Integer pageNum)` → `List<SmsHomeAdvertise>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java:60)。

## SmsHomeBrandServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:1)

注入依赖：`SmsHomeBrandMapper homeBrandMapper`

方法：
- `create(List<SmsHomeBrand> homeBrandList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:23)。
- `updateSort(Long id, Integer sort)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:33)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:41)。
- `updateRecommendStatus(List<Long> ids, Integer recommendStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:48)。
- `list(String brandName, Integer recommendStatus, Integer pageSize, Integer pageNum)` → `List<SmsHomeBrand>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeBrandServiceImpl.java:57)。

## SmsHomeNewProductServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:1)

注入依赖：`SmsHomeNewProductMapper homeNewProductMapper`

方法：
- `create(List<SmsHomeNewProduct> homeNewProductList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:23)。
- `updateSort(Long id, Integer sort)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:33)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:41)。
- `updateRecommendStatus(List<Long> ids, Integer recommendStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:48)。
- `list(String productName, Integer recommendStatus, Integer pageSize, Integer pageNum)` → `List<SmsHomeNewProduct>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeNewProductServiceImpl.java:57)。

## SmsHomeRecommendProductServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:1)

注入依赖：`SmsHomeRecommendProductMapper recommendProductMapper`

方法：
- `create(List<SmsHomeRecommendProduct> homeRecommendProductList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:23)。
- `updateSort(Long id, Integer sort)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:33)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:41)。
- `updateRecommendStatus(List<Long> ids, Integer recommendStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:48)。
- `list(String productName, Integer recommendStatus, Integer pageSize, Integer pageNum)` → `List<SmsHomeRecommendProduct>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendProductServiceImpl.java:57)。

## SmsHomeRecommendSubjectServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:1)

注入依赖：`SmsHomeRecommendSubjectMapper smsHomeRecommendSubjectMapper`

方法：
- `create(List<SmsHomeRecommendSubject> recommendSubjectList)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:23)。
- `updateSort(Long id, Integer sort)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:33)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:41)。
- `updateRecommendStatus(List<Long> ids, Integer recommendStatus)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:48)。
- `list(String subjectName, Integer recommendStatus, Integer pageSize, Integer pageNum)` → `List<SmsHomeRecommendSubject>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeRecommendSubjectServiceImpl.java:57)。

## UmsAdminCacheServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:1)

注入依赖：`UmsAdminService adminService`；`RedisService redisService`；`UmsAdminRoleRelationMapper adminRoleRelationMapper`；`UmsAdminRoleRelationDao adminRoleRelationDao`；`String REDIS_DATABASE`；`Long REDIS_EXPIRE`；`String REDIS_KEY_ADMIN`；`String REDIS_KEY_RESOURCE_LIST`

方法：
- `delAdmin(Long adminId)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:44)。
- `delResourceList(Long adminId)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:53)。
- `delResourceListByRole(Long roleId)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:59)。
- `delResourceListByRoleIds(List<Long> roleIds)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:71)。
- `delResourceListByResource(Long resourceId)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:83)。
- `getAdmin(String username)` → `UmsAdmin`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:93)。
- `setAdmin(UmsAdmin admin)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:99)。
- `getResourceList(Long adminId)` → `List<UmsResource>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:105)。
- `setResourceList(Long adminId, List<UmsResource> resourceList)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java:111)。

## UmsAdminServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:1)

注入依赖：`JwtTokenUtil jwtTokenUtil`；`PasswordEncoder passwordEncoder`；`UmsAdminMapper adminMapper`；`UmsAdminRoleRelationMapper adminRoleRelationMapper`；`UmsAdminRoleRelationDao adminRoleRelationDao`；`UmsAdminLoginLogMapper loginLogMapper`

方法：
- `getAdminByUsername(String username)` → `UmsAdmin`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:61)。
- `register(UmsAdminParam umsAdminParam)` → `UmsAdmin`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:79)。
- `login(String username, String password)` → `String`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:99)。
- `refreshToken(String oldToken)` → `String`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:149)。
- `getItem(Long id)` → `UmsAdmin`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:154)。
- `list(String keyword, Integer pageSize, Integer pageNum)` → `List<UmsAdmin>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:159)。
- `update(Long id, UmsAdmin admin)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:171)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:191)。
- `updateRole(Long adminId, List<Long> roleIds)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:199)。
- `getRoleList(Long adminId)` → `List<UmsRole>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:221)。
- `getResourceList(Long adminId)` → `List<UmsResource>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:226)。
- `updatePassword(UpdateAdminPasswordParam param)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:242)。
- `loadUserByUsername(String username)` → `UserDetails`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:265)。
- `getCacheService()` → `UmsAdminCacheService`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:276)。
- `logout(String username)` → `void`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java:281)。

## UmsMemberLevelServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMemberLevelServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMemberLevelServiceImpl.java:1)

注入依赖：`UmsMemberLevelMapper memberLevelMapper`

方法：
- `list(Integer defaultStatus)` → `List<UmsMemberLevel>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMemberLevelServiceImpl.java:21)。

## UmsMenuServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:1)

注入依赖：`UmsMenuMapper menuMapper`

方法：
- `create(UmsMenu umsMenu)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:26)。
- `update(Long id, UmsMenu umsMenu)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:51)。
- `getItem(Long id)` → `UmsMenu`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:58)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:63)。
- `list(Long parentId, Integer pageSize, Integer pageNum)` → `List<UmsMenu>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:68)。
- `treeList()` → `List<UmsMenuNode>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:77)。
- `updateHidden(Long id, Integer hidden)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java:87)。

## UmsResourceCategoryServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:1)

注入依赖：`UmsResourceCategoryMapper resourceCategoryMapper`

方法：
- `listAll()` → `List<UmsResourceCategory>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:23)。
- `create(UmsResourceCategory umsResourceCategory)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:30)。
- `update(Long id, UmsResourceCategory umsResourceCategory)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:36)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceCategoryServiceImpl.java:42)。

## UmsResourceServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:1)

注入依赖：`UmsResourceMapper resourceMapper`；`UmsAdminCacheService adminCacheService`

方法：
- `create(UmsResource umsResource)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:27)。
- `update(Long id, UmsResource umsResource)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:33)。
- `getItem(Long id)` → `UmsResource`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:41)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:46)。
- `list(Long categoryId, String nameKeyword, String urlKeyword, Integer pageSize, Integer pageNum)` → `List<UmsResource>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:53)。
- `listAll()` → `List<UmsResource>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsResourceServiceImpl.java:70)。

## UmsRoleServiceImpl

[mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:1)

注入依赖：`UmsRoleMapper roleMapper`；`UmsRoleMenuRelationMapper roleMenuRelationMapper`；`UmsRoleResourceRelationMapper roleResourceRelationMapper`；`UmsRoleDao roleDao`；`UmsAdminCacheService adminCacheService`

方法：
- `create(UmsRole role)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:35)。
- `update(Long id, UmsRole role)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:43)。
- `delete(List<Long> ids)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:49)。
- `list()` → `List<UmsRole>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:58)。
- `list(String keyword, Integer pageSize, Integer pageNum)` → `List<UmsRole>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:63)。
- `getMenuList(Long adminId)` → `List<UmsMenu>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:73)。
- `listMenu(Long roleId)` → `List<UmsMenu>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:78)。
- `listResource(Long roleId)` → `List<UmsResource>`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:83)。
- `allocMenu(Long roleId, List<Long> menuIds)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:88)。
- `allocResource(Long roleId, List<Long> resourceIds)` → `int`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java:104)。

## RedisServiceImpl

[mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:1)

注入依赖：

方法：
- `set(String key, Object value, long time)` → `void`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:21)。
- `set(String key, Object value)` → `void`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:26)。
- `get(String key)` → `Object`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:31)。
- `del(String key)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:36)。
- `del(List<String> keys)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:41)。
- `expire(String key, long time)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:46)。
- `getExpire(String key)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:51)。
- `hasKey(String key)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:56)。
- `incr(String key, long delta)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:61)。
- `decr(String key, long delta)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:66)。
- `hGet(String key, String hashKey)` → `Object`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:71)。
- `hSet(String key, String hashKey, Object value, long time)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:76)。
- `hSet(String key, String hashKey, Object value)` → `void`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:82)。
- `hGetAll(String key)` → `Map<Object, Object>`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:87)。
- `hSetAll(String key, Map<String, Object> map, long time)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:92)。
- `hSetAll(String key, Map<String, ?> map)` → `void`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:98)。
- `hDel(String key, Object... hashKey)` → `void`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:103)。
- `hHasKey(String key, String hashKey)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:108)。
- `hIncr(String key, String hashKey, Long delta)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:113)。
- `hDecr(String key, String hashKey, Long delta)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:118)。
- `sMembers(String key)` → `Set<Object>`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:123)。
- `sAdd(String key, Object... values)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:128)。
- `sAdd(String key, long time, Object... values)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:133)。
- `sIsMember(String key, Object value)` → `Boolean`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:140)。
- `sSize(String key)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:145)。
- `sRemove(String key, Object... values)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:150)。
- `lRange(String key, long start, long end)` → `List<Object>`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:155)。
- `lSize(String key)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:160)。
- `lIndex(String key, long index)` → `Object`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:165)。
- `lPush(String key, Object value)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:170)。
- `lPush(String key, Object value, long time)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:175)。
- `lPushAll(String key, Object... values)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:182)。
- `lPushAll(String key, Long time, Object... values)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:187)。
- `lRemove(String key, long count, Object value)` → `Long`；[源码](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java:194)。

## DemoServiceImpl

[mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:1)

注入依赖：`PmsBrandMapper brandMapper`

方法：
- `listAllBrand()` → `List<PmsBrand>`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:25)。
- `createBrand(PmsBrandDto pmsBrandDto)` → `int`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:30)。
- `updateBrand(Long id, PmsBrandDto pmsBrandDto)` → `int`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:37)。
- `deleteBrand(Long id)` → `int`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:45)。
- `listBrand(int pageNum, int pageSize)` → `List<PmsBrand>`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:50)。
- `getBrand(Long id)` → `PmsBrand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java:56)。

## AlipayServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:1)

注入依赖：`AlipayConfig alipayConfig`；`AlipayClient alipayClient`；`OmsOrderMapper orderMapper`；`OmsPortalOrderService portalOrderService`

方法：
- `pay(AliPayParam aliPayParam)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:41)。
- `notify(Map<String, String> params)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:72)。
- `query(String outTradeNo, String tradeNo)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:99)。
- `webPay(AliPayParam aliPayParam)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java:133)。

## HomeServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:1)

注入依赖：`SmsHomeAdvertiseMapper advertiseMapper`；`HomeDao homeDao`；`SmsFlashPromotionMapper flashPromotionMapper`；`SmsFlashPromotionSessionMapper promotionSessionMapper`；`PmsProductMapper productMapper`；`PmsProductCategoryMapper productCategoryMapper`；`CmsSubjectMapper subjectMapper`

方法：
- `content()` → `HomeContentResult`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:41)。
- `recommendProductList(Integer pageSize, Integer pageNum)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:59)。
- `getProductCateList(Long parentId)` → `List<PmsProductCategory>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:70)。
- `getSubjectList(Long cateId, Integer pageSize, Integer pageNum)` → `List<CmsSubject>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:80)。
- `hotProductList(Integer pageNum, Integer pageSize)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:92)。
- `newProductList(Integer pageNum, Integer pageSize)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java:98)。

## MemberAttentionServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:1)

注入依赖：`Boolean sqlEnable`；`PmsBrandMapper brandMapper`；`MemberBrandAttentionRepository memberBrandAttentionRepository`；`UmsMemberService memberService`

方法：
- `add(MemberBrandAttention memberBrandAttention)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:35)。
- `delete(Long brandId)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:64)。
- `list(Integer pageNum, Integer pageSize)` → `Page<MemberBrandAttention>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:70)。
- `detail(Long brandId)` → `MemberBrandAttention`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:77)。
- `clear()` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java:83)。

## MemberCollectionServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:1)

注入依赖：`Boolean sqlEnable`；`PmsProductMapper productMapper`；`MemberProductCollectionRepository productCollectionRepository`；`UmsMemberService memberService`

方法：
- `add(MemberProductCollection productCollection)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:33)。
- `delete(Long productId)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:61)。
- `list(Integer pageNum, Integer pageSize)` → `Page<MemberProductCollection>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:67)。
- `detail(Long productId)` → `MemberProductCollection`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:74)。
- `clear()` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberCollectionServiceImpl.java:80)。

## MemberReadHistoryServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:1)

注入依赖：`Boolean sqlEnable`；`PmsProductMapper productMapper`；`MemberReadHistoryRepository memberReadHistoryRepository`；`UmsMemberService memberService`

方法：
- `create(MemberReadHistory memberReadHistory)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:37)。
- `delete(List<String> ids)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:62)。
- `list(Integer pageNum, Integer pageSize)` → `Page<MemberReadHistory>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:74)。
- `clear()` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java:81)。

## OmsCartItemServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:1)

注入依赖：`OmsCartItemMapper cartItemMapper`；`PortalProductDao productDao`；`OmsPromotionService promotionService`；`UmsMemberService memberService`

方法：
- `add(OmsCartItem cartItem)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:39)。
- `list(Long memberId)` → `List<OmsCartItem>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:75)。
- `listPromotion(Long memberId, List<Long> cartIds)` → `List<CartPromotionItem>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:82)。
- `updateQuantity(Long id, Long memberId, Integer quantity)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:95)。
- `delete(Long memberId, List<Long> ids)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:105)。
- `getCartProduct(Long productId)` → `CartProduct`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:114)。
- `updateAttr(OmsCartItem cartItem)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:119)。
- `clear(Long memberId)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsCartItemServiceImpl.java:132)。

## OmsPortalOrderReturnApplyServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderReturnApplyServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderReturnApplyServiceImpl.java:1)

注入依赖：`OmsOrderReturnApplyMapper returnApplyMapper`

方法：
- `create(OmsOrderReturnApplyParam returnApply)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderReturnApplyServiceImpl.java:22)。

## OmsPortalOrderServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:1)

注入依赖：`UmsMemberService memberService`；`OmsCartItemService cartItemService`；`UmsMemberReceiveAddressService memberReceiveAddressService`；`UmsMemberCouponService memberCouponService`；`UmsIntegrationConsumeSettingMapper integrationConsumeSettingMapper`；`PmsSkuStockMapper skuStockMapper`；`SmsCouponHistoryDao couponHistoryDao`；`OmsOrderMapper orderMapper`；`PortalOrderItemDao orderItemDao`；`SmsCouponHistoryMapper couponHistoryMapper`；`RedisService redisService`；`String REDIS_KEY_ORDER_ID`；`String REDIS_DATABASE`；`PortalOrderDao portalOrderDao`；`OmsOrderSettingMapper orderSettingMapper`；`OmsOrderItemMapper orderItemMapper`；`CancelOrderSender cancelOrderSender`

方法：
- `generateConfirmOrder(List<Long> cartIds)` → `ConfirmOrderResult`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:70)。
- `generateOrder(OrderParam orderParam)` → `Map<String, Object>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:94)。
- `paySuccess(Long orderId, Integer payType)` → `Integer`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:253)。
- `cancelTimeOutOrder()` → `Integer`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:268)。
- `cancelOrder(Long orderId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:297)。
- `sendDelayMessageCancelOrder(Long orderId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:328)。
- `confirmReceiveOrder(Long orderId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:337)。
- `list(Integer status, Integer pageNum, Integer pageSize)` → `CommonPage<OmsOrderDetail>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:353)。
- `detail(Long orderId)` → `OmsOrderDetail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:396)。
- `deleteOrder(Long orderId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:408)。
- `paySuccessByOrderSn(String orderSn, Integer payType)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java:423)。

## OmsPromotionServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java:1)

注入依赖：`PortalProductDao portalProductDao`

方法：
- `calcCartPromotion(List<OmsCartItem> cartItemList)` → `List<CartPromotionItem>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java:29)。
- `compare(PmsProductFullReduction o1, PmsProductFullReduction o2)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java:179)。
- `compare(PmsProductLadder o1, PmsProductLadder o2)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java:213)。

## PmsPortalBrandServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java:1)

注入依赖：`HomeDao homeDao`；`PmsBrandMapper brandMapper`；`PmsProductMapper productMapper`

方法：
- `recommendList(Integer pageNum, Integer pageSize)` → `List<PmsBrand>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java:31)。
- `detail(Long brandId)` → `PmsBrand`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java:37)。
- `productList(Long brandId, Integer pageNum, Integer pageSize)` → `CommonPage<PmsProduct>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java:42)。

## PmsPortalProductServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java:1)

注入依赖：`PmsProductMapper productMapper`；`PmsProductCategoryMapper productCategoryMapper`；`PmsBrandMapper brandMapper`；`PmsProductAttributeMapper productAttributeMapper`；`PmsProductAttributeValueMapper productAttributeValueMapper`；`PmsSkuStockMapper skuStockMapper`；`PmsProductLadderMapper productLadderMapper`；`PmsProductFullReductionMapper productFullReductionMapper`；`PortalProductDao portalProductDao`

方法：
- `search(String keyword, Long brandId, Long productCategoryId, Integer pageNum, Integer pageSize, Integer sort)` → `List<PmsProduct>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java:45)。
- `categoryTreeList()` → `List<PmsProductCategoryNode>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java:74)。
- `detail(Long id)` → `PmsPortalProductDetail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java:85)。

## UmsMemberCacheServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:1)

注入依赖：`RedisService redisService`；`UmsMemberMapper memberMapper`；`String REDIS_DATABASE`；`Long REDIS_EXPIRE`；`Long REDIS_EXPIRE_AUTH_CODE`；`String REDIS_KEY_MEMBER`；`String REDIS_KEY_AUTH_CODE`

方法：
- `delMember(Long memberId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:34)。
- `getMember(String username)` → `UmsMember`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:43)。
- `setMember(UmsMember member)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:49)。
- `setAuthCode(String telephone, String authCode)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:56)。
- `getAuthCode(String telephone)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java:63)。

## UmsMemberCouponServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:1)

注入依赖：`UmsMemberService memberService`；`SmsCouponMapper couponMapper`；`SmsCouponHistoryMapper couponHistoryMapper`；`SmsCouponHistoryDao couponHistoryDao`；`SmsCouponProductRelationMapper couponProductRelationMapper`；`SmsCouponProductCategoryRelationMapper couponProductCategoryRelationMapper`；`PmsProductMapper productMapper`

方法：
- `add(Long couponId)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:43)。
- `listHistory(Integer useStatus)` → `List<SmsCouponHistory>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:103)。
- `listCart(List<CartPromotionItem> cartItemList, Integer type)` → `List<SmsCouponHistoryDetail>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:115)。
- `listByProduct(Long productId)` → `List<SmsCoupon>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:173)。
- `list(Integer useStatus)` → `List<SmsCoupon>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java:208)。

## UmsMemberReceiveAddressServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:1)

注入依赖：`UmsMemberService memberService`；`UmsMemberReceiveAddressMapper addressMapper`

方法：
- `add(UmsMemberReceiveAddress address)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:26)。
- `delete(Long id)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:33)。
- `update(Long id, UmsMemberReceiveAddress address)` → `int`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:41)。
- `list()` → `List<UmsMemberReceiveAddress>`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:63)。
- `getItem(Long id)` → `UmsMemberReceiveAddress`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberReceiveAddressServiceImpl.java:71)。

## UmsMemberServiceImpl

[mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:1)

注入依赖：`PasswordEncoder passwordEncoder`；`JwtTokenUtil jwtTokenUtil`；`UmsMemberMapper memberMapper`；`UmsMemberLevelMapper memberLevelMapper`；`UmsMemberCacheService memberCacheService`；`String REDIS_KEY_PREFIX_AUTH_CODE`；`Long AUTH_CODE_EXPIRE_SECONDS`

方法：
- `getByUsername(String username)` → `UmsMember`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:58)。
- `getById(Long id)` → `UmsMember`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:73)。
- `register(String username, String password, String telephone, String authCode)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:78)。
- `generateAuthCode(String telephone)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:110)。
- `updatePassword(String telephone, String password, String authCode)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:121)。
- `getCurrentMember()` → `UmsMember`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:139)。
- `updateIntegration(Long id, Integer integration)` → `void`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:147)。
- `loadUserByUsername(String username)` → `UserDetails`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:156)。
- `login(String username, String password)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:165)。
- `refreshToken(String token)` → `String`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java:183)。

## EsProductServiceImpl

[mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:1)

注入依赖：`EsProductDao productDao`；`EsProductRepository productRepository`；`ElasticsearchTemplate elasticsearchTemplate`

方法：
- `importAll()` → `int`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:45)。
- `delete(Long id)` → `void`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:58)。
- `create(Long id)` → `EsProduct`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:63)。
- `delete(List<Long> ids)` → `void`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:74)。
- `search(String keyword, Integer pageNum, Integer pageSize)` → `Page<EsProduct>`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:87)。
- `search(String keyword, Long brandId, Long productCategoryId, Integer pageNum, Integer pageSize,Integer sort)` → `Page<EsProduct>`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:93)。
- `recommend(Long id, Integer pageNum, Integer pageSize)` → `Page<EsProduct>`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:161)。
- `searchRelatedInfo(String keyword)` → `EsProductRelatedInfo`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java:215)。