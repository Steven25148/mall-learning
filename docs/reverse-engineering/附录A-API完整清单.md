# 附录A：Controller API完整清单

【已确认事实】从当前源码的类级路径与方法级映射拼接。方法签名保留参数注解、默认值与返回类型。未标注 `@RequestBody` 的复杂对象不能直接当作 JSON body；`@RequestParam` 对应请求参数，`@PathVariable` 对应路径参数。权限描述来自随仓配置，不代表线上配置。

通用响应、过滤链与对象级权限见主说明书。业务模型字段见附录C；本清单不宣称接口已运行验收。

共 246 个映射方法；包含 mall-demo 的教学接口，单独分组，不作为商城业务。

## mall-admin

### `GET /prefrenceArea/listAll`

- 功能：获取所有商品优选。
- Controller：`CmsPrefrenceAreaController.listAll`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsPrefrenceAreaController.java:30)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：23:商品优选管理 (/prefrenceArea/**)。
- 直接调用：`CmsPrefrenceAreaService.listAll`。
- 返回类型：`CommonResult<List<CmsPrefrenceArea>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /subject/listAll`

- 功能：获取全部商品专题。
- Controller：`CmsSubjectController.listAll`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java:32)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：24:商品专题管理 (/subject/**)。
- 直接调用：`CmsSubjectService.listAll`。
- 返回类型：`CommonResult<List<CmsSubject>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /subject/list`

- 功能：根据专题名称分页获取商品专题。
- Controller：`CmsSubjectController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：24:商品专题管理 (/subject/**)。
- 直接调用：`CmsSubjectService.list`。
- 返回类型：`CommonResult<CommonPage<CmsSubject>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize
```

### `POST /minio/upload`

- 功能：文件上传。
- Controller：`MinioController.upload`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/MinioController.java:44)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：无注入对象调用；见方法源码。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestPart("file") MultipartFile file
```

### `POST /minio/delete`

- 功能：文件删除。
- Controller：`MinioController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/MinioController.java:105)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：未匹配；按该样例配置会被动态授权拒绝。
- 直接调用：无注入对象调用；见方法源码。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("objectName") String objectName
```

### `GET /companyAddress/list`

- 功能：获取所有收货地址。
- Controller：`OmsCompanyAddressController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsCompanyAddressController.java:30)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：12:收货地址管理 (/companyAddress/**)。
- 直接调用：`OmsCompanyAddressService.list`。
- 返回类型：`CommonResult<List<OmsCompanyAddress>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /order/list`

- 功能：查询订单。
- Controller：`OmsOrderController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:30)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.list`。
- 返回类型：`CommonResult<CommonPage<OmsOrder>>`。
- 请求参数 / Body：
```java
OmsOrderQueryParam queryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /order/update/delivery`

- 功能：批量发货。
- Controller：`OmsOrderController.delivery`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.delivery`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<OmsOrderDeliveryParam> deliveryParamList
```

### `POST /order/update/close`

- 功能：批量关闭订单。
- Controller：`OmsOrderController.close`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.close`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam String note
```

### `POST /order/delete`

- 功能：批量删除订单。
- Controller：`OmsOrderController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `GET /order/{id}`

- 功能：获取订单详情：订单信息、商品信息、操作记录。
- Controller：`OmsOrderController.detail`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.detail`。
- 返回类型：`CommonResult<OmsOrderDetail>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /order/update/receiverInfo`

- 功能：修改收货人信息。
- Controller：`OmsOrderController.updateReceiverInfo`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:81)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.updateReceiverInfo`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsReceiverInfoParam receiverInfoParam
```

### `POST /order/update/moneyInfo`

- 功能：修改订单费用信息。
- Controller：`OmsOrderController.updateReceiverInfo`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:92)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.updateMoneyInfo`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsMoneyInfoParam moneyInfoParam
```

### `POST /order/update/note`

- 功能：备注订单。
- Controller：`OmsOrderController.updateNote`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java:103)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：8:订单管理 (/order/**)。
- 直接调用：`OmsOrderService.updateNote`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("id") Long id, @RequestParam("note") String note, @RequestParam("status") Integer status
```

### `GET /returnApply/list`

- 功能：分页查询退货申请。
- Controller：`OmsOrderReturnApplyController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:32)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- 直接调用：`OmsOrderReturnApplyService.list`。
- 返回类型：`CommonResult<CommonPage<OmsOrderReturnApply>>`。
- 请求参数 / Body：
```java
OmsReturnApplyQueryParam queryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /returnApply/delete`

- 功能：批量删除退货申请。
- Controller：`OmsOrderReturnApplyController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:42)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- 直接调用：`OmsOrderReturnApplyService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `GET /returnApply/{id}`

- 功能：获取退货申请详情。
- Controller：`OmsOrderReturnApplyController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:53)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- 直接调用：`OmsOrderReturnApplyService.getItem`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /returnApply/update/status/{id}`

- 功能：修改退货申请状态。
- Controller：`OmsOrderReturnApplyController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java:61)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：9:订单退货申请管理 (/returnApply/**)。
- 直接调用：`OmsOrderReturnApplyService.updateStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody OmsUpdateStatusParam statusParam
```

### `POST /returnReason/create`

- 功能：添加退货原因。
- Controller：`OmsOrderReturnReasonController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsOrderReturnReason returnReason
```

### `POST /returnReason/update/{id}`

- 功能：修改退货原因。
- Controller：`OmsOrderReturnReasonController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody OmsOrderReturnReason returnReason
```

### `POST /returnReason/delete`

- 功能：批量删除退货原因。
- Controller：`OmsOrderReturnReasonController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `GET /returnReason/list`

- 功能：分页查询退货原因。
- Controller：`OmsOrderReturnReasonController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.list`。
- 返回类型：`CommonResult<CommonPage<OmsOrderReturnReason>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /returnReason/{id}`

- 功能：获取单个退货原因详情信息。
- Controller：`OmsOrderReturnReasonController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:71)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.getItem`。
- 返回类型：`CommonResult<OmsOrderReturnReason>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /returnReason/update/status`

- 功能：修改退货原因启用状态。
- Controller：`OmsOrderReturnReasonController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java:79)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：10:退货原因管理 (/returnReason/**)。
- 直接调用：`OmsOrderReturnReasonService.updateStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam(value = "status") Integer status, @RequestParam("ids") List<Long> ids
```

### `GET /orderSetting/{id}`

- 功能：获取指定订单设置。
- Controller：`OmsOrderSettingController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderSettingController.java:26)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：11:订单设置管理 (/orderSetting/**)。
- 直接调用：`OmsOrderSettingService.getItem`。
- 返回类型：`CommonResult<OmsOrderSetting>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /orderSetting/update/{id}`

- 功能：修改指定订单设置。
- Controller：`OmsOrderSettingController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OmsOrderSettingController.java:34)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：11:订单设置管理 (/orderSetting/**)。
- 直接调用：`OmsOrderSettingService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody OmsOrderSetting orderSetting
```

### `GET /aliyun/oss/policy`

- 功能：Oss上传签名生成。
- Controller：`OssController.policy`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OssController.java:32)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：`OssService.policy`。
- 返回类型：`CommonResult<OssPolicyResult>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /aliyun/osscallback`

- 功能：Oss上传成功回调。
- Controller：`OssController.callback`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/OssController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：未匹配；按该样例配置会被动态授权拒绝。
- 直接调用：`OssService.callback`。
- 返回类型：`CommonResult<OssCallbackResult>`。
- 请求参数 / Body：
```java
HttpServletRequest request
```

### `GET /brand/listAll`

- 功能：获取全部品牌列表。
- Controller：`PmsBrandController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:31)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.listAllBrand`。
- 返回类型：`CommonResult<List<PmsBrand>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /brand/create`

- 功能：添加品牌。
- Controller：`PmsBrandController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:38)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.createBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@Validated @RequestBody PmsBrandParam pmsBrand
```

### `POST /brand/update/{id}`

- 功能：更新品牌。
- Controller：`PmsBrandController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:52)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.updateBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id, @Validated @RequestBody PmsBrandParam pmsBrandParam
```

### `GET /brand/delete/{id}`

- 功能：删除品牌。
- Controller：`PmsBrandController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:67)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.deleteBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id
```

### `GET /brand/list`

- 功能：根据品牌名称分页获取品牌列表。
- Controller：`PmsBrandController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:79)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.listBrand`。
- 返回类型：`CommonResult<CommonPage<PmsBrand>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "showStatus",required = false) Integer showStatus, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize
```

### `GET /brand/{id}`

- 功能：根据编号查询品牌信息。
- Controller：`PmsBrandController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:90)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.getBrand`。
- 返回类型：`CommonResult<PmsBrand>`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id
```

### `POST /brand/delete/batch`

- 功能：批量删除品牌。
- Controller：`PmsBrandController.deleteBatch`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:97)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.deleteBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /brand/update/showStatus`

- 功能：批量更新显示状态。
- Controller：`PmsBrandController.updateShowStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:109)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.updateShowStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("showStatus") Integer showStatus
```

### `POST /brand/update/factoryStatus`

- 功能：批量更新厂家制造商状态。
- Controller：`PmsBrandController.updateFactoryStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java:122)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：1:商品品牌管理 (/brand/**)。
- 直接调用：`PmsBrandService.updateFactoryStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("factoryStatus") Integer factoryStatus
```

### `POST /productAttribute/category/create`

- 功能：添加商品属性分类。
- Controller：`PmsProductAttributeCategoryController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:30)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam String name
```

### `POST /productAttribute/category/update/{id}`

- 功能：修改商品属性分类。
- Controller：`PmsProductAttributeCategoryController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:42)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestParam String name
```

### `GET /productAttribute/category/delete/{id}`

- 功能：删除单个商品属性分类。
- Controller：`PmsProductAttributeCategoryController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:54)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /productAttribute/category/{id}`

- 功能：获取单个商品属性分类信息。
- Controller：`PmsProductAttributeCategoryController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:66)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.getItem`。
- 返回类型：`CommonResult<PmsProductAttributeCategory>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /productAttribute/category/list`

- 功能：分页获取所有商品属性分类。
- Controller：`PmsProductAttributeCategoryController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:74)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.getList`。
- 返回类型：`CommonResult<CommonPage<PmsProductAttributeCategory>>`。
- 请求参数 / Body：
```java
@RequestParam(defaultValue = "5") Integer pageSize, @RequestParam(defaultValue = "1") Integer pageNum
```

### `GET /productAttribute/category/list/withAttr`

- 功能：获取所有商品属性分类及其下属性。
- Controller：`PmsProductAttributeCategoryController.getListWithAttr`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeCategoryController.java:82)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：2:商品属性分类管理 (/productAttribute/category/**)、3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeCategoryService.getListWithAttr`。
- 返回类型：`CommonResult<List<PmsProductAttributeCategoryItem>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /productAttribute/list/{cid}`

- 功能：根据分类查询属性列表或参数列表。
- Controller：`PmsProductAttributeController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:36)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.getList`。
- 返回类型：`CommonResult<CommonPage<PmsProductAttribute>>`。
- 请求参数 / Body：
```java
@PathVariable Long cid, @RequestParam(value = "type") Integer type, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /productAttribute/create`

- 功能：添加商品属性信息。
- Controller：`PmsProductAttributeController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:47)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody PmsProductAttributeParam productAttributeParam
```

### `POST /productAttribute/update/{id}`

- 功能：修改商品属性信息。
- Controller：`PmsProductAttributeController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:59)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody PmsProductAttributeParam productAttributeParam
```

### `GET /productAttribute/{id}`

- 功能：查询单个商品属性。
- Controller：`PmsProductAttributeController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:71)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.getItem`。
- 返回类型：`CommonResult<PmsProductAttribute>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /productAttribute/delete`

- 功能：批量删除商品属性。
- Controller：`PmsProductAttributeController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:79)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `GET /productAttribute/attrInfo/{productCategoryId}`

- 功能：根据商品分类的id获取商品属性及属性分类。
- Controller：`PmsProductAttributeController.getAttrInfo`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java:91)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：3:商品属性管理 (/productAttribute/**)。
- 直接调用：`PmsProductAttributeService.getProductAttrInfo`。
- 返回类型：`CommonResult<List<ProductAttrInfo>>`。
- 请求参数 / Body：
```java
@PathVariable Long productCategoryId
```

### `POST /productCategory/create`

- 功能：添加商品分类。
- Controller：`PmsProductCategoryController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:32)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@Validated @RequestBody PmsProductCategoryParam productCategoryParam
```

### `POST /productCategory/update/{id}`

- 功能：修改商品分类。
- Controller：`PmsProductCategoryController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:44)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @Validated @RequestBody PmsProductCategoryParam productCategoryParam
```

### `GET /productCategory/list/{parentId}`

- 功能：分页查询商品分类。
- Controller：`PmsProductCategoryController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:58)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.getList`。
- 返回类型：`CommonResult<CommonPage<PmsProductCategory>>`。
- 请求参数 / Body：
```java
@PathVariable Long parentId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /productCategory/{id}`

- 功能：根据id获取商品分类。
- Controller：`PmsProductCategoryController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:68)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.getItem`。
- 返回类型：`CommonResult<PmsProductCategory>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /productCategory/delete/{id}`

- 功能：删除商品分类。
- Controller：`PmsProductCategoryController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:76)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /productCategory/update/navStatus`

- 功能：修改导航栏显示状态。
- Controller：`PmsProductCategoryController.updateNavStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:88)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.updateNavStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("navStatus") Integer navStatus
```

### `POST /productCategory/update/showStatus`

- 功能：修改显示状态。
- Controller：`PmsProductCategoryController.updateShowStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:100)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.updateShowStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("showStatus") Integer showStatus
```

### `GET /productCategory/list/withChildren`

- 功能：查询所有一级分类及子分类。
- Controller：`PmsProductCategoryController.listWithChildren`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java:112)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：4:商品分类管理 (/productCategory/**)。
- 直接调用：`PmsProductCategoryService.listWithChildren`。
- 返回类型：`CommonResult<List<PmsProductCategoryWithChildrenItem>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /product/create`

- 功能：创建商品。
- Controller：`PmsProductController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:32)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody PmsProductParam productParam
```

### `GET /product/updateInfo/{id}`

- 功能：根据商品id获取商品编辑信息。
- Controller：`PmsProductController.getUpdateInfo`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:44)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.getUpdateInfo`。
- 返回类型：`CommonResult<PmsProductResult>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /product/update/{id}`

- 功能：更新商品。
- Controller：`PmsProductController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:52)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody PmsProductParam productParam
```

### `GET /product/list`

- 功能：查询商品。
- Controller：`PmsProductController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:64)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.list`。
- 返回类型：`CommonResult<CommonPage<PmsProduct>>`。
- 请求参数 / Body：
```java
PmsProductQueryParam productQueryParam, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /product/simpleList`

- 功能：根据商品名称或货号模糊查询。
- Controller：`PmsProductController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:74)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.list`。
- 返回类型：`CommonResult<List<PmsProduct>>`。
- 请求参数 / Body：
```java
String keyword
```

### `POST /product/update/verifyStatus`

- 功能：批量修改审核状态。
- Controller：`PmsProductController.updateVerifyStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:82)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.updateVerifyStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("verifyStatus") Integer verifyStatus, @RequestParam("detail") String detail
```

### `POST /product/update/publishStatus`

- 功能：批量上下架商品。
- Controller：`PmsProductController.updatePublishStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:96)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.updatePublishStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("publishStatus") Integer publishStatus
```

### `POST /product/update/recommendStatus`

- 功能：批量推荐商品。
- Controller：`PmsProductController.updateRecommendStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:109)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.updateRecommendStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("recommendStatus") Integer recommendStatus
```

### `POST /product/update/newStatus`

- 功能：批量设为新品。
- Controller：`PmsProductController.updateNewStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:122)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.updateNewStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("newStatus") Integer newStatus
```

### `POST /product/update/deleteStatus`

- 功能：批量修改删除状态。
- Controller：`PmsProductController.updateDeleteStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java:135)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：5:商品管理 (/product/**)。
- 直接调用：`PmsProductService.updateDeleteStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam("deleteStatus") Integer deleteStatus
```

### `GET /sku/{pid}`

- 功能：根据商品ID及sku编码模糊搜索sku库存。
- Controller：`PmsSkuStockController.getList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsSkuStockController.java:28)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：6:商品库存管理 (/sku/**)。
- 直接调用：`PmsSkuStockService.getList`。
- 返回类型：`CommonResult<List<PmsSkuStock>>`。
- 请求参数 / Body：
```java
@PathVariable Long pid, @RequestParam(value = "keyword",required = false) String keyword
```

### `POST /sku/update/{pid}`

- 功能：批量更新sku库存信息。
- Controller：`PmsSkuStockController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/PmsSkuStockController.java:35)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：6:商品库存管理 (/sku/**)。
- 直接调用：`PmsSkuStockService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long pid,@RequestBody List<PmsSkuStock> skuStockList
```

### `POST /coupon/create`

- 功能：添加优惠券。
- Controller：`SmsCouponController.add`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- 直接调用：`SmsCouponService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody SmsCouponParam couponParam
```

### `POST /coupon/delete/{id}`

- 功能：删除优惠券。
- Controller：`SmsCouponController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- 直接调用：`SmsCouponService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /coupon/update/{id}`

- 功能：修改优惠券。
- Controller：`SmsCouponController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- 直接调用：`SmsCouponService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id,@RequestBody SmsCouponParam couponParam
```

### `GET /coupon/list`

- 功能：根据优惠券名称和类型分页获取优惠券列表。
- Controller：`SmsCouponController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- 直接调用：`SmsCouponService.list`。
- 返回类型：`CommonResult<CommonPage<SmsCoupon>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "name",required = false) String name, @RequestParam(value = "type",required = false) Integer type, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /coupon/{id}`

- 功能：获取单个优惠券的详细信息。
- Controller：`SmsCouponController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java:74)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：13:优惠券管理 (/coupon/**)。
- 直接调用：`SmsCouponService.getItem`。
- 返回类型：`CommonResult<SmsCouponParam>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /couponHistory/list`

- 功能：根据优惠券id，使用状态，订单编号分页获取领取记录。
- Controller：`SmsCouponHistoryController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsCouponHistoryController.java:32)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：14:优惠券领取记录管理 (/couponHistory/**)。
- 直接调用：`SmsCouponHistoryService.list`。
- 返回类型：`CommonResult<CommonPage<SmsCouponHistory>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "couponId", required = false) Long couponId, @RequestParam(value = "useStatus", required = false) Integer useStatus, @RequestParam(value = "orderSn", required = false) String orderSn, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /flash/create`

- 功能：添加活动。
- Controller：`SmsFlashPromotionController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody SmsFlashPromotion flashPromotion
```

### `POST /flash/update/{id}`

- 功能：编辑活动。
- Controller：`SmsFlashPromotionController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody SmsFlashPromotion flashPromotion
```

### `POST /flash/delete/{id}`

- 功能：删除活动。
- Controller：`SmsFlashPromotionController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /flash/update/status/{id}`

- 功能：修改上下线状态。
- Controller：`SmsFlashPromotionController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.updateStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer status
```

### `GET /flash/{id}`

- 功能：获取活动详情。
- Controller：`SmsFlashPromotionController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.getItem`。
- 返回类型：`CommonResult<SmsFlashPromotion>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /flash/list`

- 功能：根据活动名称分页查询。
- Controller：`SmsFlashPromotionController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionController.java:81)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：15:限时购活动管理 (/flash/**)。
- 直接调用：`SmsFlashPromotionService.list`。
- 返回类型：`CommonResult<CommonPage<SmsFlashPromotion>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /flashProductRelation/create`

- 功能：批量选择商品添加关联。
- Controller：`SmsFlashPromotionProductRelationController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:30)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- 直接调用：`SmsFlashPromotionProductRelationService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<SmsFlashPromotionProductRelation> relationList
```

### `POST /flashProductRelation/update/{id}`

- 功能：修改关联信息。
- Controller：`SmsFlashPromotionProductRelationController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:41)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- 直接调用：`SmsFlashPromotionProductRelationService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody SmsFlashPromotionProductRelation relation
```

### `POST /flashProductRelation/delete/{id}`

- 功能：删除关联。
- Controller：`SmsFlashPromotionProductRelationController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:52)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- 直接调用：`SmsFlashPromotionProductRelationService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /flashProductRelation/{id}`

- 功能：获取关联商品促销信息。
- Controller：`SmsFlashPromotionProductRelationController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:63)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- 直接调用：`SmsFlashPromotionProductRelationService.getItem`。
- 返回类型：`CommonResult<SmsFlashPromotionProductRelation>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /flashProductRelation/list`

- 功能：分页查询不同场次关联及商品信息。
- Controller：`SmsFlashPromotionProductRelationController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionProductRelationController.java:71)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：16:限时购商品关系管理 (/flashProductRelation/**)。
- 直接调用：`SmsFlashPromotionProductRelationService.list`。
- 返回类型：`CommonResult<CommonPage<SmsFlashPromotionProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "flashPromotionId") Long flashPromotionId, @RequestParam(value = "flashPromotionSessionId") Long flashPromotionSessionId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /flashSession/create`

- 功能：添加场次。
- Controller：`SmsFlashPromotionSessionController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody SmsFlashPromotionSession promotionSession
```

### `POST /flashSession/update/{id}`

- 功能：修改场次。
- Controller：`SmsFlashPromotionSessionController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody SmsFlashPromotionSession promotionSession
```

### `POST /flashSession/update/status/{id}`

- 功能：修改启用状态。
- Controller：`SmsFlashPromotionSessionController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.updateStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer status
```

### `POST /flashSession/delete/{id}`

- 功能：删除场次。
- Controller：`SmsFlashPromotionSessionController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /flashSession/{id}`

- 功能：获取场次详情。
- Controller：`SmsFlashPromotionSessionController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.getItem`。
- 返回类型：`CommonResult<SmsFlashPromotionSession>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /flashSession/list`

- 功能：获取全部场次。
- Controller：`SmsFlashPromotionSessionController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:81)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.list`。
- 返回类型：`CommonResult<List<SmsFlashPromotionSession>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /flashSession/selectList`

- 功能：获取全部可选场次及其数量。
- Controller：`SmsFlashPromotionSessionController.selectList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsFlashPromotionSessionController.java:89)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：17:限时购场次管理 (/flashSession/**)。
- 直接调用：`SmsFlashPromotionSessionService.selectList`。
- 返回类型：`CommonResult<List<SmsFlashPromotionSessionDetail>>`。
- 请求参数 / Body：
```java
Long flashPromotionId
```

### `POST /home/advertise/create`

- 功能：添加广告。
- Controller：`SmsHomeAdvertiseController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody SmsHomeAdvertise advertise
```

### `POST /home/advertise/delete`

- 功能：删除广告。
- Controller：`SmsHomeAdvertiseController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:39)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /home/advertise/update/status/{id}`

- 功能：修改上下线状态。
- Controller：`SmsHomeAdvertiseController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:49)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.updateStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer status
```

### `GET /home/advertise/{id}`

- 功能：获取广告详情。
- Controller：`SmsHomeAdvertiseController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:59)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.getItem`。
- 返回类型：`CommonResult<SmsHomeAdvertise>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /home/advertise/update/{id}`

- 功能：修改广告。
- Controller：`SmsHomeAdvertiseController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:67)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody SmsHomeAdvertise advertise
```

### `GET /home/advertise/list`

- 功能：分页查询广告。
- Controller：`SmsHomeAdvertiseController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeAdvertiseController.java:77)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：18:首页轮播广告管理 (/home/advertise/**)。
- 直接调用：`SmsHomeAdvertiseService.list`。
- 返回类型：`CommonResult<CommonPage<SmsHomeAdvertise>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "name", required = false) String name, @RequestParam(value = "type", required = false) Integer type, @RequestParam(value = "endTime", required = false) String endTime, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /home/brand/create`

- 功能：添加首页推荐品牌。
- Controller：`SmsHomeBrandController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- 直接调用：`SmsHomeBrandService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<SmsHomeBrand> homeBrandList
```

### `POST /home/brand/update/sort/{id}`

- 功能：修改推荐品牌排序。
- Controller：`SmsHomeBrandController.updateSort`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- 直接调用：`SmsHomeBrandService.updateSort`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer sort
```

### `POST /home/brand/delete`

- 功能：批量删除推荐品牌。
- Controller：`SmsHomeBrandController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- 直接调用：`SmsHomeBrandService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /home/brand/update/recommendStatus`

- 功能：批量修改推荐品牌状态。
- Controller：`SmsHomeBrandController.updateRecommendStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- 直接调用：`SmsHomeBrandService.updateRecommendStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus
```

### `GET /home/brand/list`

- 功能：分页查询推荐品牌。
- Controller：`SmsHomeBrandController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeBrandController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：19:首页品牌管理 (/home/brand/**)。
- 直接调用：`SmsHomeBrandService.list`。
- 返回类型：`CommonResult<CommonPage<SmsHomeBrand>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "brandName", required = false) String brandName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /home/newProduct/create`

- 功能：添加首页新品。
- Controller：`SmsHomeNewProductController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- 直接调用：`SmsHomeNewProductService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<SmsHomeNewProduct> homeNewProductList
```

### `POST /home/newProduct/update/sort/{id}`

- 功能：修改首页新品排序。
- Controller：`SmsHomeNewProductController.updateSort`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- 直接调用：`SmsHomeNewProductService.updateSort`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer sort
```

### `POST /home/newProduct/delete`

- 功能：批量删除首页新品。
- Controller：`SmsHomeNewProductController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- 直接调用：`SmsHomeNewProductService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /home/newProduct/update/recommendStatus`

- 功能：批量修改首页新品状态。
- Controller：`SmsHomeNewProductController.updateRecommendStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- 直接调用：`SmsHomeNewProductService.updateRecommendStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus
```

### `GET /home/newProduct/list`

- 功能：分页查询首页新品。
- Controller：`SmsHomeNewProductController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeNewProductController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：20:首页新品管理 (/home/newProduct/**)。
- 直接调用：`SmsHomeNewProductService.list`。
- 返回类型：`CommonResult<CommonPage<SmsHomeNewProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "productName", required = false) String productName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /home/recommendProduct/create`

- 功能：添加首页推荐。
- Controller：`SmsHomeRecommendProductController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- 直接调用：`SmsHomeRecommendProductService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<SmsHomeRecommendProduct> homeRecommendProductList
```

### `POST /home/recommendProduct/update/sort/{id}`

- 功能：修改推荐排序。
- Controller：`SmsHomeRecommendProductController.updateSort`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- 直接调用：`SmsHomeRecommendProductService.updateSort`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer sort
```

### `POST /home/recommendProduct/delete`

- 功能：批量删除推荐。
- Controller：`SmsHomeRecommendProductController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- 直接调用：`SmsHomeRecommendProductService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /home/recommendProduct/update/recommendStatus`

- 功能：批量修改推荐状态。
- Controller：`SmsHomeRecommendProductController.updateRecommendStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- 直接调用：`SmsHomeRecommendProductService.updateRecommendStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus
```

### `GET /home/recommendProduct/list`

- 功能：分页查询推荐。
- Controller：`SmsHomeRecommendProductController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendProductController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：21:首页人气推荐管理 (/home/recommendProduct/**)。
- 直接调用：`SmsHomeRecommendProductService.list`。
- 返回类型：`CommonResult<CommonPage<SmsHomeRecommendProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "productName", required = false) String productName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /home/recommendSubject/create`

- 功能：添加首页推荐专题。
- Controller：`SmsHomeRecommendSubjectController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- 直接调用：`SmsHomeRecommendSubjectService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody List<SmsHomeRecommendSubject> homeRecommendSubjectList
```

### `POST /home/recommendSubject/update/sort/{id}`

- 功能：修改推荐排序。
- Controller：`SmsHomeRecommendSubjectController.updateSort`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- 直接调用：`SmsHomeRecommendSubjectService.updateSort`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, Integer sort
```

### `POST /home/recommendSubject/delete`

- 功能：批量删除推荐。
- Controller：`SmsHomeRecommendSubjectController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- 直接调用：`SmsHomeRecommendSubjectService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /home/recommendSubject/update/recommendStatus`

- 功能：批量修改推荐状态。
- Controller：`SmsHomeRecommendSubjectController.updateRecommendStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- 直接调用：`SmsHomeRecommendSubjectService.updateRecommendStatus`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids, @RequestParam Integer recommendStatus
```

### `GET /home/recommendSubject/list`

- 功能：分页查询推荐。
- Controller：`SmsHomeRecommendSubjectController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/SmsHomeRecommendSubjectController.java:73)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：22:首页专题推荐管理 (/home/recommendSubject/**)。
- 直接调用：`SmsHomeRecommendSubjectService.list`。
- 返回类型：`CommonResult<CommonPage<SmsHomeRecommendSubject>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "subjectName", required = false) String subjectName, @RequestParam(value = "recommendStatus", required = false) Integer recommendStatus, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /admin/register`

- 功能：用户注册。
- Controller：`UmsAdminController.register`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:49)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：`UmsAdminService.register`。
- 返回类型：`CommonResult<UmsAdmin>`。
- 请求参数 / Body：
```java
@Validated @RequestBody UmsAdminParam umsAdminParam
```

### `POST /admin/login`

- 功能：登录以后返回token。
- Controller：`UmsAdminController.login`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:60)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：`UmsAdminService.login`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@Validated @RequestBody UmsAdminLoginParam umsAdminLoginParam
```

### `GET /admin/refreshToken`

- 功能：刷新token。
- Controller：`UmsAdminController.refreshToken`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:74)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.refreshToken`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
HttpServletRequest request
```

### `GET /admin/info`

- 功能：获取当前登录用户信息。
- Controller：`UmsAdminController.getAdminInfo`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:89)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：`UmsAdminService.getAdminByUsername`、`UmsAdminService.getRoleList`、`UmsRoleService.getMenuList`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Principal principal
```

### `POST /admin/logout`

- 功能：登出功能。
- Controller：`UmsAdminController.logout`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:110)。
- 权限：配置白名单放行；方法内可能仍依赖登录主体。
- 直接调用：`UmsAdminService.logout`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Principal principal
```

### `GET /admin/list`

- 功能：根据用户名或姓名分页获取用户列表。
- Controller：`UmsAdminController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:118)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.list`。
- 返回类型：`CommonResult<CommonPage<UmsAdmin>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /admin/{id}`

- 功能：获取指定用户信息。
- Controller：`UmsAdminController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:128)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.getItem`。
- 返回类型：`CommonResult<UmsAdmin>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /admin/update/{id}`

- 功能：修改指定用户信息。
- Controller：`UmsAdminController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:136)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsAdmin admin
```

### `POST /admin/updatePassword`

- 功能：修改指定用户密码。
- Controller：`UmsAdminController.updatePassword`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:147)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.updatePassword`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@Validated @RequestBody UpdateAdminPasswordParam updatePasswordParam
```

### `POST /admin/delete/{id}`

- 功能：删除指定用户信息。
- Controller：`UmsAdminController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:165)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /admin/updateStatus/{id}`

- 功能：修改帐号状态。
- Controller：`UmsAdminController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:176)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id,@RequestParam(value = "status") Integer status
```

### `POST /admin/role/update`

- 功能：给用户分配角色。
- Controller：`UmsAdminController.updateRole`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:189)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.updateRole`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("adminId") Long adminId, @RequestParam("roleIds") List<Long> roleIds
```

### `GET /admin/role/{adminId}`

- 功能：获取指定用户的角色。
- Controller：`UmsAdminController.getRoleList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java:201)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：25:后台用户管理 (/admin/**)。
- 直接调用：`UmsAdminService.getRoleList`。
- 返回类型：`CommonResult<List<UmsRole>>`。
- 请求参数 / Body：
```java
@PathVariable Long adminId
```

### `GET /memberLevel/list`

- 功能：查询所有会员等级。
- Controller：`UmsMemberLevelController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMemberLevelController.java:31)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：30:会员等级管理 (/memberLevel/**)。
- 直接调用：`UmsMemberLevelService.list`。
- 返回类型：`CommonResult<List<UmsMemberLevel>>`。
- 请求参数 / Body：
```java
@RequestParam("defaultStatus") Integer defaultStatus
```

### `POST /menu/create`

- 功能：添加后台菜单。
- Controller：`UmsMenuController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:31)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody UmsMenu umsMenu
```

### `POST /menu/update/{id}`

- 功能：修改后台菜单。
- Controller：`UmsMenuController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:43)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsMenu umsMenu
```

### `GET /menu/{id}`

- 功能：根据ID获取菜单详情。
- Controller：`UmsMenuController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:56)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.getItem`。
- 返回类型：`CommonResult<UmsMenu>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /menu/delete/{id}`

- 功能：根据ID删除后台菜单。
- Controller：`UmsMenuController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:64)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /menu/list/{parentId}`

- 功能：分页查询后台菜单。
- Controller：`UmsMenuController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:76)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.list`。
- 返回类型：`CommonResult<CommonPage<UmsMenu>>`。
- 请求参数 / Body：
```java
@PathVariable Long parentId, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /menu/treeList`

- 功能：树形结构返回所有菜单列表。
- Controller：`UmsMenuController.treeList`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:86)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.treeList`。
- 返回类型：`CommonResult<List<UmsMenuNode>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /menu/updateHidden/{id}`

- 功能：修改菜单显示状态。
- Controller：`UmsMenuController.updateHidden`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java:94)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：27:后台菜单管理 (/menu/**)。
- 直接调用：`UmsMenuService.updateHidden`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestParam("hidden") Integer hidden
```

### `GET /resourceCategory/listAll`

- 功能：查询所有后台资源分类。
- Controller：`UmsResourceCategoryController.listAll`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:28)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- 直接调用：`UmsResourceCategoryService.listAll`。
- 返回类型：`CommonResult<List<UmsResourceCategory>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /resourceCategory/create`

- 功能：添加后台资源分类。
- Controller：`UmsResourceCategoryController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:36)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- 直接调用：`UmsResourceCategoryService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody UmsResourceCategory umsResourceCategory
```

### `POST /resourceCategory/update/{id}`

- 功能：修改后台资源分类。
- Controller：`UmsResourceCategoryController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:48)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- 直接调用：`UmsResourceCategoryService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsResourceCategory umsResourceCategory
```

### `POST /resourceCategory/delete/{id}`

- 功能：根据ID删除后台资源分类。
- Controller：`UmsResourceCategoryController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java:61)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：28:后台资源分类管理 (/resourceCategory/**)。
- 直接调用：`UmsResourceCategoryService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /resource/create`

- 功能：添加后台资源。
- Controller：`UmsResourceController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:33)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`DynamicSecurityMetadataSource.clearDataSource`、`UmsResourceService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody UmsResource umsResource
```

### `POST /resource/update/{id}`

- 功能：修改后台资源。
- Controller：`UmsResourceController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:46)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`DynamicSecurityMetadataSource.clearDataSource`、`UmsResourceService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsResource umsResource
```

### `GET /resource/{id}`

- 功能：根据ID获取资源详情。
- Controller：`UmsResourceController.getItem`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:60)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`UmsResourceService.getItem`。
- 返回类型：`CommonResult<UmsResource>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /resource/delete/{id}`

- 功能：根据ID删除后台资源。
- Controller：`UmsResourceController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:68)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`DynamicSecurityMetadataSource.clearDataSource`、`UmsResourceService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /resource/list`

- 功能：分页模糊查询后台资源。
- Controller：`UmsResourceController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:81)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`UmsResourceService.list`。
- 返回类型：`CommonResult<CommonPage<UmsResource>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) Long categoryId, @RequestParam(required = false) String nameKeyword, @RequestParam(required = false) String urlKeyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /resource/listAll`

- 功能：查询所有后台资源。
- Controller：`UmsResourceController.listAll`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsResourceController.java:93)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：29:后台资源管理 (/resource/**)。
- 直接调用：`UmsResourceService.listAll`。
- 返回类型：`CommonResult<List<UmsResource>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /role/create`

- 功能：添加角色。
- Controller：`UmsRoleController.create`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:29)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody UmsRole role
```

### `POST /role/update/{id}`

- 功能：修改角色。
- Controller：`UmsRoleController.update`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:40)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsRole role
```

### `POST /role/delete`

- 功能：批量删除角色。
- Controller：`UmsRoleController.delete`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:51)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `GET /role/listAll`

- 功能：获取所有角色。
- Controller：`UmsRoleController.listAll`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:62)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.list`。
- 返回类型：`CommonResult<List<UmsRole>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /role/list`

- 功能：根据角色名称分页获取角色列表。
- Controller：`UmsRoleController.list`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:70)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.list`。
- 返回类型：`CommonResult<CommonPage<UmsRole>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "keyword", required = false) String keyword, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `POST /role/updateStatus/{id}`

- 功能：修改角色状态。
- Controller：`UmsRoleController.updateStatus`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:80)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestParam(value = "status") Integer status
```

### `GET /role/listMenu/{roleId}`

- 功能：获取角色相关菜单。
- Controller：`UmsRoleController.listMenu`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:93)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.listMenu`。
- 返回类型：`CommonResult<List<UmsMenu>>`。
- 请求参数 / Body：
```java
@PathVariable Long roleId
```

### `GET /role/listResource/{roleId}`

- 功能：获取角色相关资源。
- Controller：`UmsRoleController.listResource`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:101)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.listResource`。
- 返回类型：`CommonResult<List<UmsResource>>`。
- 请求参数 / Body：
```java
@PathVariable Long roleId
```

### `POST /role/allocMenu`

- 功能：给角色分配菜单。
- Controller：`UmsRoleController.allocMenu`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:109)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.allocMenu`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam Long roleId, @RequestParam List<Long> menuIds
```

### `POST /role/allocResource`

- 功能：给角色分配资源。
- Controller：`UmsRoleController.allocResource`；[源码](D:/project/mall/mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java:117)。
- 权限：后台动态资源权限（按URL匹配；运行时角色分配未确认）；SQL样例可匹配资源：26:后台用户角色管理 (/role/**)。
- 直接调用：`UmsRoleService.allocResource`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam Long roleId, @RequestParam List<Long> resourceIds
```

## mall-demo

### `GET /brand/listAll`

- 功能：获取全部品牌列表。
- Controller：`DemoController.getBrandList`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:34)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.listAllBrand`。
- 返回类型：`CommonResult<List<PmsBrand>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /brand/create`

- 功能：添加品牌。
- Controller：`DemoController.createBrand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:41)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.createBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@Validated @RequestBody PmsBrandDto pmsBrand
```

### `POST /brand/update/{id}`

- 功能：更新品牌。
- Controller：`DemoController.updateBrand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:57)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.updateBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id, @Validated @RequestBody PmsBrandDto pmsBrandDto
```

### `GET /brand/delete/{id}`

- 功能：删除品牌。
- Controller：`DemoController.deleteBrand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:73)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.deleteBrand`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id
```

### `GET /brand/list`

- 功能：分页获取品牌列表。
- Controller：`DemoController.listBrand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:87)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.listBrand`。
- 返回类型：`CommonResult<CommonPage<PmsBrand>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "3") Integer pageSize
```

### `GET /brand/{id}`

- 功能：根据编号查询品牌信息。
- Controller：`DemoController.brand`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java:96)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`DemoService.getBrand`。
- 返回类型：`CommonResult<PmsBrand>`。
- 请求参数 / Body：
```java
@PathVariable("id") Long id
```

### `GET /template/get/{id}`

- 功能：getForEntity url。
- Controller：`RestTemplateDemoController.getForEntity`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:40)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.getForEntity`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /template/get2/{id}`

- 功能：getForEntity params。
- Controller：`RestTemplateDemoController.getForEntity2`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:49)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.getForEntity`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /template/get3/{id}`

- 功能：getForEntity Uri。
- Controller：`RestTemplateDemoController.getForEntity3`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:60)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.getForEntity`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /template/get4/{id}`

- 功能：getForObject url。
- Controller：`RestTemplateDemoController.getForObject`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:70)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.getForObject`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /template/post`

- 功能：postForEntity jsonBody。
- Controller：`RestTemplateDemoController.postForEntity`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:79)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.postForEntity`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@RequestBody PmsBrand brand
```

### `POST /template/post2`

- 功能：postForEntity jsonBody。
- Controller：`RestTemplateDemoController.postForObject`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:88)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.postForObject`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@RequestBody PmsBrand brand
```

### `POST /template/post3`

- 功能：postForEntity form。
- Controller：`RestTemplateDemoController.postForEntity3`；[源码](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java:97)。
- 权限：教学应用自定义SecurityConfig对/**配置permitAll；其他过滤行为见该配置。
- 直接调用：`RestTemplate.postForEntity`。
- 返回类型：`Object`。
- 请求参数 / Body：
```java
@RequestParam String name
```

## mall-portal

### `GET /alipay/pay`

- 功能：支付宝电脑网站支付。
- Controller：`AlipayController.pay`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:39)。
- 权限：配置白名单放行。
- 直接调用：`AlipayConfig.getCharset`、`AlipayService.pay`。
- 返回类型：`void`。
- 请求参数 / Body：
```java
AliPayParam aliPayParam, HttpServletResponse response
```

### `GET /alipay/webPay`

- 功能：支付宝手机网站支付。
- Controller：`AlipayController.webPay`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:48)。
- 权限：配置白名单放行。
- 直接调用：`AlipayConfig.getCharset`、`AlipayService.webPay`。
- 返回类型：`void`。
- 请求参数 / Body：
```java
AliPayParam aliPayParam, HttpServletResponse response
```

### `POST /alipay/notify`

- 功能：支付宝异步回调。
- Controller：`AlipayController.notify`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:57)。
- 权限：配置白名单放行。
- 直接调用：`AlipayService.notify`。
- 返回类型：`String`。
- 请求参数 / Body：
```java
HttpServletRequest request
```

### `GET /alipay/query`

- 功能：支付宝统一收单线下交易查询。
- Controller：`AlipayController.query`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java:69)。
- 权限：配置白名单放行。
- 直接调用：`AlipayService.query`。
- 返回类型：`CommonResult<String>`。
- 请求参数 / Body：
```java
String outTradeNo, String tradeNo
```

### `GET /home/content`

- 功能：首页内容信息展示。
- Controller：`HomeController.content`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:31)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.content`。
- 返回类型：`CommonResult<HomeContentResult>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /home/recommendProductList`

- 功能：分页获取推荐商品。
- Controller：`HomeController.recommendProductList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:39)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.recommendProductList`。
- 返回类型：`CommonResult<List<PmsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageSize", defaultValue = "4") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /home/productCateList/{parentId}`

- 功能：获取首页商品分类。
- Controller：`HomeController.getProductCateList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:48)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.getProductCateList`。
- 返回类型：`CommonResult<List<PmsProductCategory>>`。
- 请求参数 / Body：
```java
@PathVariable Long parentId
```

### `GET /home/subjectList`

- 功能：根据分类获取专题。
- Controller：`HomeController.getSubjectList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:56)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.getSubjectList`。
- 返回类型：`CommonResult<List<CmsSubject>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) Long cateId, @RequestParam(value = "pageSize", defaultValue = "4") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /home/hotProductList`

- 功能：分页获取人气推荐商品。
- Controller：`HomeController.hotProductList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:66)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.hotProductList`。
- 返回类型：`CommonResult<List<PmsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize
```

### `GET /home/newProductList`

- 功能：分页获取新品推荐商品。
- Controller：`HomeController.newProductList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java:75)。
- 权限：配置白名单放行。
- 直接调用：`HomeService.newProductList`。
- 返回类型：`CommonResult<List<PmsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize
```

### `POST /member/attention/add`

- 功能：添加品牌关注。
- Controller：`MemberAttentionController.add`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:27)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberAttentionService.add`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody MemberBrandAttention memberBrandAttention
```

### `POST /member/attention/delete`

- 功能：取消品牌关注。
- Controller：`MemberAttentionController.delete`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:39)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberAttentionService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long brandId
```

### `GET /member/attention/list`

- 功能：分页查询当前用户品牌关注列表。
- Controller：`MemberAttentionController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:51)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberAttentionService.list`。
- 返回类型：`CommonResult<CommonPage<MemberBrandAttention>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize
```

### `GET /member/attention/detail`

- 功能：根据品牌ID获取品牌关注详情。
- Controller：`MemberAttentionController.detail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:60)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberAttentionService.detail`。
- 返回类型：`CommonResult<MemberBrandAttention>`。
- 请求参数 / Body：
```java
@RequestParam Long brandId
```

### `POST /member/attention/clear`

- 功能：清空当前用户品牌关注列表。
- Controller：`MemberAttentionController.clear`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberAttentionController.java:68)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberAttentionService.clear`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /member/productCollection/add`

- 功能：添加商品收藏。
- Controller：`MemberProductCollectionController.add`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:28)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberCollectionService.add`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody MemberProductCollection productCollection
```

### `POST /member/productCollection/delete`

- 功能：删除商品收藏。
- Controller：`MemberProductCollectionController.delete`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:40)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberCollectionService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long productId
```

### `GET /member/productCollection/list`

- 功能：显示当前用户商品收藏列表。
- Controller：`MemberProductCollectionController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:52)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberCollectionService.list`。
- 返回类型：`CommonResult<CommonPage<MemberProductCollection>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize
```

### `GET /member/productCollection/detail`

- 功能：显示商品收藏详情。
- Controller：`MemberProductCollectionController.detail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:61)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberCollectionService.detail`。
- 返回类型：`CommonResult<MemberProductCollection>`。
- 请求参数 / Body：
```java
@RequestParam Long productId
```

### `POST /member/productCollection/clear`

- 功能：清空当前用户商品收藏列表。
- Controller：`MemberProductCollectionController.clear`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberProductCollectionController.java:69)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberCollectionService.clear`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /member/readHistory/create`

- 功能：创建浏览记录。
- Controller：`MemberReadHistoryController.create`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:30)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberReadHistoryService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody MemberReadHistory memberReadHistory
```

### `POST /member/readHistory/delete`

- 功能：删除浏览记录。
- Controller：`MemberReadHistoryController.delete`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:42)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberReadHistoryService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<String> ids
```

### `POST /member/readHistory/clear`

- 功能：清空浏览记录。
- Controller：`MemberReadHistoryController.clear`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:54)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberReadHistoryService.clear`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /member/readHistory/list`

- 功能：分页获取浏览记录。
- Controller：`MemberReadHistoryController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java:62)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`MemberReadHistoryService.list`。
- 返回类型：`CommonResult<CommonPage<MemberReadHistory>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "5") Integer pageSize
```

### `POST /cart/add`

- 功能：添加商品到购物车。
- Controller：`OmsCartItemController.add`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:33)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.add`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsCartItem cartItem
```

### `GET /cart/list`

- 功能：获取当前会员的购物车列表。
- Controller：`OmsCartItemController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:44)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.list`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult<List<OmsCartItem>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /cart/list/promotion`

- 功能：获取当前会员的购物车列表,包括促销信息。
- Controller：`OmsCartItemController.listPromotion`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:52)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.listPromotion`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult<List<CartPromotionItem>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) List<Long> cartIds
```

### `GET /cart/update/quantity`

- 功能：修改购物车中指定商品的数量。
- Controller：`OmsCartItemController.updateQuantity`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:60)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.updateQuantity`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam Long id, @RequestParam Integer quantity
```

### `GET /cart/getProduct/{productId}`

- 功能：获取购物车中指定商品的规格,用于重选规格。
- Controller：`OmsCartItemController.getCartProduct`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:72)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.getCartProduct`。
- 返回类型：`CommonResult<CartProduct>`。
- 请求参数 / Body：
```java
@PathVariable Long productId
```

### `POST /cart/update/attr`

- 功能：修改购物车中商品的规格。
- Controller：`OmsCartItemController.updateAttr`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:80)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.updateAttr`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsCartItem cartItem
```

### `POST /cart/delete`

- 功能：删除购物车中的指定商品。
- Controller：`OmsCartItemController.delete`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:91)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.delete`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /cart/clear`

- 功能：清空当前会员的购物车。
- Controller：`OmsCartItemController.clear`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsCartItemController.java:102)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.clear`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /order/generateConfirmOrder`

- 功能：根据购物车信息生成确认单。
- Controller：`OmsPortalOrderController.generateConfirmOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:35)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.generateConfirmOrder`。
- 返回类型：`CommonResult<ConfirmOrderResult>`。
- 请求参数 / Body：
```java
@RequestBody List<Long> cartIds
```

### `POST /order/generateOrder`

- 功能：根据购物车信息生成订单。
- Controller：`OmsPortalOrderController.generateOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:43)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.generateOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OrderParam orderParam
```

### `POST /order/paySuccess`

- 功能：用户支付成功的回调。
- Controller：`OmsPortalOrderController.paySuccess`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:51)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.paySuccess`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam Long orderId,@RequestParam Integer payType
```

### `POST /order/cancelTimeOutOrder`

- 功能：自动取消超时订单。
- Controller：`OmsPortalOrderController.cancelTimeOutOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:59)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.cancelTimeOutOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
无方法参数
```

### `POST /order/cancelOrder`

- 功能：取消单个超时订单。
- Controller：`OmsPortalOrderController.cancelOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:67)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.sendDelayMessageCancelOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long orderId
```

### `GET /order/list`

- 功能：按状态分页获取用户订单列表。
- Controller：`OmsPortalOrderController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:77)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.list`。
- 返回类型：`CommonResult<CommonPage<OmsOrderDetail>>`。
- 请求参数 / Body：
```java
@RequestParam Integer status, @RequestParam(required = false, defaultValue = "1") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize
```

### `GET /order/detail/{orderId}`

- 功能：根据ID获取订单详情。
- Controller：`OmsPortalOrderController.detail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:87)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.detail`。
- 返回类型：`CommonResult<OmsOrderDetail>`。
- 请求参数 / Body：
```java
@PathVariable Long orderId
```

### `POST /order/cancelUserOrder`

- 功能：用户取消订单。
- Controller：`OmsPortalOrderController.cancelUserOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:95)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.cancelOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long orderId
```

### `POST /order/confirmReceiveOrder`

- 功能：用户确认收货。
- Controller：`OmsPortalOrderController.confirmReceiveOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:103)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.confirmReceiveOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long orderId
```

### `POST /order/deleteOrder`

- 功能：用户删除订单。
- Controller：`OmsPortalOrderController.deleteOrder`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java:111)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderService.deleteOrder`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Long orderId
```

### `POST /returnApply/create`

- 功能：申请退货。
- Controller：`OmsPortalOrderReturnApplyController.create`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderReturnApplyController.java:29)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsPortalOrderReturnApplyService.create`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody OmsOrderReturnApplyParam returnApply
```

### `GET /brand/recommendList`

- 功能：分页获取推荐品牌。
- Controller：`PmsPortalBrandController.recommendList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:31)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalBrandService.recommendList`。
- 返回类型：`CommonResult<List<PmsBrand>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum
```

### `GET /brand/detail/{brandId}`

- 功能：获取品牌详情。
- Controller：`PmsPortalBrandController.detail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:40)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalBrandService.detail`。
- 返回类型：`CommonResult<PmsBrand>`。
- 请求参数 / Body：
```java
@PathVariable Long brandId
```

### `GET /brand/productList`

- 功能：分页获取品牌相关商品。
- Controller：`PmsPortalBrandController.productList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java:48)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalBrandService.productList`。
- 返回类型：`CommonResult<CommonPage<PmsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam Long brandId, @RequestParam(value = "pageNum", defaultValue = "1") Integer pageNum, @RequestParam(value = "pageSize", defaultValue = "6") Integer pageSize
```

### `GET /product/search`

- 功能：综合搜索、筛选、排序。
- Controller：`PmsPortalProductController.search`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:37)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalProductService.search`。
- 返回类型：`CommonResult<CommonPage<PmsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) String keyword, @RequestParam(required = false) Long brandId, @RequestParam(required = false) Long productCategoryId, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize, @RequestParam(required = false, defaultValue = "0") Integer sort
```

### `GET /product/categoryTreeList`

- 功能：以树形结构获取所有商品分类。
- Controller：`PmsPortalProductController.categoryTreeList`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:50)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalProductService.categoryTreeList`。
- 返回类型：`CommonResult<List<PmsProductCategoryNode>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /product/detail/{id}`

- 功能：获取前台商品详情。
- Controller：`PmsPortalProductController.detail`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java:58)。
- 权限：配置白名单放行。
- 直接调用：`PmsPortalProductService.detail`。
- 返回类型：`CommonResult<PmsPortalProductDetail>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /sso/register`

- 功能：会员注册。
- Controller：`UmsMemberController.register`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:39)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.register`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam String username, @RequestParam String password, @RequestParam String telephone, @RequestParam String authCode
```

### `POST /sso/login`

- 功能：会员登录。
- Controller：`UmsMemberController.login`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:50)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.login`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam String username, @RequestParam String password
```

### `GET /sso/info`

- 功能：获取会员信息。
- Controller：`UmsMemberController.info`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:65)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
Principal principal
```

### `GET /sso/getAuthCode`

- 功能：获取验证码。
- Controller：`UmsMemberController.getAuthCode`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:76)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.generateAuthCode`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam String telephone
```

### `POST /sso/updatePassword`

- 功能：会员修改密码。
- Controller：`UmsMemberController.updatePassword`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:84)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.updatePassword`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestParam String telephone, @RequestParam String password, @RequestParam String authCode
```

### `GET /sso/refreshToken`

- 功能：刷新token。
- Controller：`UmsMemberController.refreshToken`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberController.java:95)。
- 权限：配置白名单放行。
- 直接调用：`UmsMemberService.refreshToken`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
HttpServletRequest request
```

### `POST /member/coupon/add/{couponId}`

- 功能：领取指定优惠券。
- Controller：`UmsMemberCouponController.add`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:40)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberCouponService.add`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long couponId
```

### `GET /member/coupon/listHistory`

- 功能：获取会员优惠券历史列表。
- Controller：`UmsMemberCouponController.listHistory`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:50)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberCouponService.listHistory`。
- 返回类型：`CommonResult<List<SmsCouponHistory>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "useStatus", required = false) Integer useStatus
```

### `GET /member/coupon/list`

- 功能：获取会员优惠券列表。
- Controller：`UmsMemberCouponController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:60)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberCouponService.list`。
- 返回类型：`CommonResult<List<SmsCoupon>>`。
- 请求参数 / Body：
```java
@RequestParam(value = "useStatus", required = false) Integer useStatus
```

### `GET /member/coupon/list/cart/{type}`

- 功能：获取登录会员购物车的相关优惠券。
- Controller：`UmsMemberCouponController.listCart`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:70)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`OmsCartItemService.listPromotion`、`UmsMemberCouponService.listCart`、`UmsMemberService.getCurrentMember`。
- 返回类型：`CommonResult<List<SmsCouponHistoryDetail>>`。
- 请求参数 / Body：
```java
@PathVariable Integer type
```

### `GET /member/coupon/listByProduct/{productId}`

- 功能：获取当前商品相关优惠券。
- Controller：`UmsMemberCouponController.listByProduct`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java:79)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberCouponService.listByProduct`。
- 返回类型：`CommonResult<List<SmsCoupon>>`。
- 请求参数 / Body：
```java
@PathVariable Long productId
```

### `POST /member/address/add`

- 功能：添加收货地址。
- Controller：`UmsMemberReceiveAddressController.add`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:28)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberReceiveAddressService.add`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@RequestBody UmsMemberReceiveAddress address
```

### `POST /member/address/delete/{id}`

- 功能：删除收货地址。
- Controller：`UmsMemberReceiveAddressController.delete`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:39)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberReceiveAddressService.delete`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /member/address/update/{id}`

- 功能：修改收货地址。
- Controller：`UmsMemberReceiveAddressController.update`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:50)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberReceiveAddressService.update`。
- 返回类型：`CommonResult`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestBody UmsMemberReceiveAddress address
```

### `GET /member/address/list`

- 功能：获取所有收货地址。
- Controller：`UmsMemberReceiveAddressController.list`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:61)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberReceiveAddressService.list`。
- 返回类型：`CommonResult<List<UmsMemberReceiveAddress>>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /member/address/{id}`

- 功能：获取收货地址详情。
- Controller：`UmsMemberReceiveAddressController.getItem`；[源码](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberReceiveAddressController.java:69)。
- 权限：需会员认证；对象归属另看业务方法。
- 直接调用：`UmsMemberReceiveAddressService.getItem`。
- 返回类型：`CommonResult<UmsMemberReceiveAddress>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

## mall-search

### `POST /esProduct/importAll`

- 功能：导入所有数据库中商品到ES。
- Controller：`EsProductController.importAllList`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:34)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.importAll`。
- 返回类型：`CommonResult<Integer>`。
- 请求参数 / Body：
```java
无方法参数
```

### `GET /esProduct/delete/{id}`

- 功能：根据id删除商品。
- Controller：`EsProductController.delete`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:42)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.delete`。
- 返回类型：`CommonResult<Object>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `POST /esProduct/delete/batch`

- 功能：根据id批量删除商品。
- Controller：`EsProductController.delete`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:50)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.delete`。
- 返回类型：`CommonResult<Object>`。
- 请求参数 / Body：
```java
@RequestParam("ids") List<Long> ids
```

### `POST /esProduct/create/{id}`

- 功能：根据id创建商品。
- Controller：`EsProductController.create`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:58)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.create`。
- 返回类型：`CommonResult<EsProduct>`。
- 请求参数 / Body：
```java
@PathVariable Long id
```

### `GET /esProduct/search/simple`

- 功能：简单搜索。
- Controller：`EsProductController.search`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:70)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.search`。
- 返回类型：`CommonResult<CommonPage<EsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) String keyword, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize
```

### `GET /esProduct/search`

- 功能：综合搜索、筛选、排序。
- Controller：`EsProductController.search`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:81)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.search`。
- 返回类型：`CommonResult<CommonPage<EsProduct>>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) String keyword, @RequestParam(required = false) Long brandId, @RequestParam(required = false) Long productCategoryId, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize, @RequestParam(required = false, defaultValue = "0") Integer sort
```

### `GET /esProduct/recommend/{id}`

- 功能：根据商品id推荐商品。
- Controller：`EsProductController.recommend`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:94)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.recommend`。
- 返回类型：`CommonResult<CommonPage<EsProduct>>`。
- 请求参数 / Body：
```java
@PathVariable Long id, @RequestParam(required = false, defaultValue = "0") Integer pageNum, @RequestParam(required = false, defaultValue = "5") Integer pageSize
```

### `GET /esProduct/search/relate`

- 功能：获取搜索的相关品牌、分类及筛选属性。
- Controller：`EsProductController.searchRelatedInfo`；[源码](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/controller/EsProductController.java:104)。
- 权限：该应用未发现Security过滤链；外部访问控制无法确认。
- 直接调用：`EsProductService.searchRelatedInfo`。
- 返回类型：`CommonResult<EsProductRelatedInfo>`。
- 请求参数 / Body：
```java
@RequestParam(required = false) String keyword
```
