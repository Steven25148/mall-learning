# 附录C：请求与响应模型字段

【已确认事实】摘录业务 DTO / domain / BO 与生成 Model 的类声明、字段及紧邻注解。继承字段须结合父类；`Example` 查询构造器不列入接口模型。字段存在不表示每个接口都返回非空值或允许修改。

## AdminUserDetails

[mall/mall-admin/src/main/java/com/macro/mall/bo/AdminUserDetails.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/bo/AdminUserDetails.java:1)

```java
public class AdminUserDetails implements UserDetails
//后台用户
private final UmsAdmin umsAdmin;
//拥有资源列表
private final List<UmsResource> resourceList;
```

## BucketPolicyConfigDto

[mall/mall-admin/src/main/java/com/macro/mall/dto/BucketPolicyConfigDto.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/BucketPolicyConfigDto.java:1)

```java
public class BucketPolicyConfigDto
private String Version;
private List<Statement> Statement;
// 以下字段属于嵌套类型：public static class Statement
private String Effect;
private String Principal;
private String Action;
private String Resource;
```

## MinioUploadDto

[mall/mall-admin/src/main/java/com/macro/mall/dto/MinioUploadDto.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/MinioUploadDto.java:1)

```java
public class MinioUploadDto
@Schema(title = "文件访问URL")
private String url;
@Schema(title = "文件名称")
private String name;
```

## OmsMoneyInfoParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsMoneyInfoParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsMoneyInfoParam.java:1)

```java
public class OmsMoneyInfoParam
@Schema(title = "订单ID")
private Long orderId;
@Schema(title = "运费金额")
private BigDecimal freightAmount;
@Schema(title = "管理员后台调整订单所使用的折扣金额")
private BigDecimal discountAmount;
@Schema(title = "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单")
private Integer status;
```

## OmsOrderDeliveryParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderDeliveryParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderDeliveryParam.java:1)

```java
public class OmsOrderDeliveryParam
@Schema(title = "订单id")
private Long orderId;
@Schema(title = "物流公司")
private String deliveryCompany;
@Schema(title = "物流单号")
private String deliverySn;
```

## OmsOrderDetail

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderDetail.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderDetail.java:1)

```java
public class OmsOrderDetail extends OmsOrder
@Getter
@Setter
@Schema(title = "订单商品列表")
private List<OmsOrderItem> orderItemList;
@Getter
@Setter
@Schema(title = "订单操作记录列表")
private List<OmsOrderOperateHistory> historyList;
```

## OmsOrderQueryParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderQueryParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderQueryParam.java:1)

```java
public class OmsOrderQueryParam
@Schema(title =  "订单编号")
private String orderSn;
@Schema(title =  "收货人姓名/号码")
private String receiverKeyword;
@Schema(title =  "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单")
private Integer status;
@Schema(title =  "订单类型：0->正常订单；1->秒杀订单")
private Integer orderType;
@Schema(title =  "订单来源：0->PC订单；1->app订单")
private Integer sourceType;
@Schema(title =  "订单提交时间")
private String createTime;
```

## OmsOrderReturnApplyResult

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderReturnApplyResult.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsOrderReturnApplyResult.java:1)

```java
public class OmsOrderReturnApplyResult extends OmsOrderReturnApply
@Getter
@Setter
@Schema(title =  "公司收货地址")
private OmsCompanyAddress companyAddress;
```

## OmsReceiverInfoParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsReceiverInfoParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsReceiverInfoParam.java:1)

```java
public class OmsReceiverInfoParam
@Schema(title =  "订单ID")
private Long orderId;
@Schema(title =  "收货人姓名")
private String receiverName;
@Schema(title =  "收货人电话")
private String receiverPhone;
@Schema(title =  "收货人邮编")
private String receiverPostCode;
@Schema(title =  "详细地址")
private String receiverDetailAddress;
@Schema(title =  "省份/直辖市")
private String receiverProvince;
@Schema(title =  "城市")
private String receiverCity;
@Schema(title =  "区")
private String receiverRegion;
@Schema(title =  "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单")
private Integer status;
```

## OmsReturnApplyQueryParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsReturnApplyQueryParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsReturnApplyQueryParam.java:1)

```java
public class OmsReturnApplyQueryParam
@Schema(title = "服务单号")
private Long id;
@Schema(title =  "收货人姓名/号码")
private String receiverKeyword;
@Schema(title =  "申请状态：0->待处理；1->退货中；2->已完成；3->已拒绝")
private Integer status;
@Schema(title =  "申请时间")
private String createTime;
@Schema(title =  "处理人员")
private String handleMan;
@Schema(title =  "处理时间")
private String handleTime;
```

## OmsUpdateStatusParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OmsUpdateStatusParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OmsUpdateStatusParam.java:1)

```java
public class OmsUpdateStatusParam
@Schema(title = "服务单号")
private Long id;
@Schema(title = "收货地址关联id")
private Long companyAddressId;
@Schema(title = "确认退款金额")
private BigDecimal returnAmount;
@Schema(title = "处理备注")
private String handleNote;
@Schema(title = "处理人")
private String handleMan;
@Schema(title = "收货备注")
private String receiveNote;
@Schema(title = "收货人")
private String receiveMan;
@Schema(title = "申请状态：1->退货中；2->已完成；3->已拒绝")
private Integer status;
```

## OssCallbackParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/OssCallbackParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OssCallbackParam.java:1)

```java
public class OssCallbackParam
@Schema(title = "请求的回调地址")
private String callbackUrl;
@Schema(title = "回调是传入request中的参数")
private String callbackBody;
@Schema(title = "回调时传入参数的格式，比如表单提交形式")
private String callbackBodyType;
```

## OssCallbackResult

[mall/mall-admin/src/main/java/com/macro/mall/dto/OssCallbackResult.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OssCallbackResult.java:1)

```java
public class OssCallbackResult
@Schema(title = "文件名称")
private String filename;
@Schema(title = "文件大小")
private String size;
@Schema(title = "文件的mimeType")
private String mimeType;
@Schema(title = "图片文件的宽")
private String width;
@Schema(title = "图片文件的高")
private String height;
```

## OssPolicyResult

[mall/mall-admin/src/main/java/com/macro/mall/dto/OssPolicyResult.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/OssPolicyResult.java:1)

```java
public class OssPolicyResult
@Schema(title = "访问身份验证中用到用户标识")
private String accessKeyId;
@Schema(title = "用户表单上传的策略,经过base64编码过的字符串")
private String policy;
@Schema(title = "对policy签名后的字符串")
private String signature;
@Schema(title = "上传文件夹路径前缀")
private String dir;
@Schema(title = "oss对外服务的访问域名")
private String host;
@Schema(title = "上传成功后的回调设置")
private String callback;
```

## PmsBrandParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsBrandParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsBrandParam.java:1)

```java
public class PmsBrandParam
@NotEmpty
@Schema(title =  "品牌名称",requiredMode = Schema.RequiredMode.REQUIRED)
private String name;
@Schema(title =  "品牌首字母")
private String firstLetter;
@Min(value = 0)
@Schema(title =  "排序字段")
private Integer sort;
@FlagValidator(value = {"0","1"}, message = "厂家状态不正确")
@Schema(title =  "是否为厂家制造商")
private Integer factoryStatus;
@FlagValidator(value = {"0","1"}, message = "显示状态不正确")
@Schema(title =  "是否进行显示")
private Integer showStatus;
@NotEmpty
@Schema(title =  "品牌logo",requiredMode = Schema.RequiredMode.REQUIRED)
private String logo;
@Schema(title =  "品牌大图")
private String bigPic;
@Schema(title =  "品牌故事")
private String brandStory;
```

## PmsProductAttributeCategoryItem

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductAttributeCategoryItem.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductAttributeCategoryItem.java:1)

```java
public class PmsProductAttributeCategoryItem extends PmsProductAttributeCategory
@Getter
@Setter
@Schema(title =  "商品属性列表")
private List<PmsProductAttribute> productAttributeList;
```

## PmsProductAttributeParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductAttributeParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductAttributeParam.java:1)

```java
public class PmsProductAttributeParam
@NotEmpty
@Schema(title = "属性分类ID")
private Long productAttributeCategoryId;
@NotEmpty
@Schema(title = "属性名称")
private String name;
@FlagValidator({"0","1","2"})
@Schema(title = "属性选择类型：0->唯一；1->单选；2->多选")
private Integer selectType;
@FlagValidator({"0","1"})
@Schema(title = "属性录入方式：0->手工录入；1->从列表中选取")
private Integer inputType;
@Schema(title = "可选值列表，以逗号隔开")
private String inputList;
private Integer sort;
@Schema(title = "分类筛选样式：0->普通；1->颜色")
@FlagValidator({"0","1"})
private Integer filterType;
@Schema(title = "检索类型；0->不需要进行检索；1->关键字检索；2->范围检索")
@FlagValidator({"0","1","2"})
private Integer searchType;
@Schema(title = "相同属性产品是否关联；0->不关联；1->关联")
@FlagValidator({"0","1"})
private Integer relatedStatus;
@Schema(title = "是否支持手动新增；0->不支持；1->支持")
@FlagValidator({"0","1"})
private Integer handAddStatus;
@Schema(title = "属性的类型；0->规格；1->参数")
@FlagValidator({"0","1"})
private Integer type;
```

## PmsProductCategoryParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductCategoryParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductCategoryParam.java:1)

```java
public class PmsProductCategoryParam
@Schema(title = "父分类的编号")
private Long parentId;
@NotEmpty
@Schema(title = "商品分类名称",requiredMode = Schema.RequiredMode.REQUIRED)
private String name;
@Schema(title = "分类单位")
private String productUnit;
@FlagValidator(value = {"0","1"},message = "状态只能为0或1")
@Schema(title = "是否在导航栏显示")
private Integer navStatus;
@FlagValidator(value = {"0","1"},message = "状态只能为0或1")
@Schema(title = "是否进行显示")
private Integer showStatus;
@Min(value = 0)
@Schema(title = "排序")
private Integer sort;
@Schema(title = "图标")
private String icon;
@Schema(title = "关键字")
private String keywords;
@Schema(title = "描述")
private String description;
@Schema(title = "产品相关筛选属性集合")
private List<Long> productAttributeIdList;
```

## PmsProductCategoryWithChildrenItem

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductCategoryWithChildrenItem.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductCategoryWithChildrenItem.java:1)

```java
public class PmsProductCategoryWithChildrenItem extends PmsProductCategory
@Getter
@Setter
@Schema(title = "子级分类")
private List<PmsProductCategory> children;
```

## PmsProductParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductParam.java:1)

```java
public class PmsProductParam extends PmsProduct
@Schema(title = "商品阶梯价格设置")
private List<PmsProductLadder> productLadderList;
@Schema(title = "商品满减价格设置")
private List<PmsProductFullReduction> productFullReductionList;
@Schema(title = "商品会员价格设置")
private List<PmsMemberPrice> memberPriceList;
@Schema(title = "商品的sku库存信息")
private List<PmsSkuStock> skuStockList;
@Schema(title = "商品参数及自定义规格属性")
private List<PmsProductAttributeValue> productAttributeValueList;
@Schema(title = "专题和商品关系")
private List<CmsSubjectProductRelation> subjectProductRelationList;
@Schema(title = "优选专区和商品的关系")
private List<CmsPrefrenceAreaProductRelation> prefrenceAreaProductRelationList;
```

## PmsProductQueryParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductQueryParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductQueryParam.java:1)

```java
public class PmsProductQueryParam
@Schema(title = "上架状态")
private Integer publishStatus;
@Schema(title = "审核状态")
private Integer verifyStatus;
@Schema(title = "商品名称模糊关键字")
private String keyword;
@Schema(title = "商品货号")
private String productSn;
@Schema(title = "商品分类编号")
private Long productCategoryId;
@Schema(title = "商品品牌编号")
private Long brandId;
```

## PmsProductResult

[mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductResult.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/PmsProductResult.java:1)

```java
public class PmsProductResult extends PmsProductParam
@Getter
@Setter
@Schema(title = "商品所选分类的父id")
private Long cateParentId;
```

## ProductAttrInfo

[mall/mall-admin/src/main/java/com/macro/mall/dto/ProductAttrInfo.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/ProductAttrInfo.java:1)

```java
public class ProductAttrInfo
@Schema(title = "商品属性ID")
private Long attributeId;
@Schema(title = "商品属性分类ID")
private Long attributeCategoryId;
```

## SmsCouponParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/SmsCouponParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/SmsCouponParam.java:1)

```java
public class SmsCouponParam extends SmsCoupon
@Getter
@Setter
@Schema(title = "优惠券绑定的商品")
private List<SmsCouponProductRelation> productRelationList;
@Getter
@Setter
@Schema(title = "优惠券绑定的商品分类")
private List<SmsCouponProductCategoryRelation> productCategoryRelationList;
```

## SmsFlashPromotionProduct

[mall/mall-admin/src/main/java/com/macro/mall/dto/SmsFlashPromotionProduct.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/SmsFlashPromotionProduct.java:1)

```java
public class SmsFlashPromotionProduct extends SmsFlashPromotionProductRelation
@Getter
@Setter
@Schema(title = "关联商品")
private PmsProduct product;
```

## SmsFlashPromotionSessionDetail

[mall/mall-admin/src/main/java/com/macro/mall/dto/SmsFlashPromotionSessionDetail.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/SmsFlashPromotionSessionDetail.java:1)

```java
public class SmsFlashPromotionSessionDetail extends SmsFlashPromotionSession
@Setter
@Getter
@Schema(title = "商品数量")
private Long productCount;
```

## UmsAdminLoginParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/UmsAdminLoginParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/UmsAdminLoginParam.java:1)

```java
public class UmsAdminLoginParam
@NotEmpty
@Schema(title =  "用户名",requiredMode = Schema.RequiredMode.REQUIRED)
private String username;
@NotEmpty
@Schema(title =  "密码",requiredMode = Schema.RequiredMode.REQUIRED)
private String password;
```

## UmsAdminParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/UmsAdminParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/UmsAdminParam.java:1)

```java
public class UmsAdminParam
@NotEmpty
@Schema(title = "用户名", requiredMode = Schema.RequiredMode.REQUIRED)
private String username;
@NotEmpty
@Schema(title =  "密码", requiredMode = Schema.RequiredMode.REQUIRED)
private String password;
@Schema(title =  "用户头像")
private String icon;
@Email
@Schema(title =  "邮箱")
private String email;
@Schema(title =  "用户昵称")
private String nickName;
@Schema(title =  "备注")
private String note;
```

## UmsMenuNode

[mall/mall-admin/src/main/java/com/macro/mall/dto/UmsMenuNode.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/UmsMenuNode.java:1)

```java
public class UmsMenuNode extends UmsMenu
@Schema(title =  "子级菜单")
private List<UmsMenuNode> children;
```

## UpdateAdminPasswordParam

[mall/mall-admin/src/main/java/com/macro/mall/dto/UpdateAdminPasswordParam.java](D:/project/mall/mall-admin/src/main/java/com/macro/mall/dto/UpdateAdminPasswordParam.java:1)

```java
public class UpdateAdminPasswordParam
@NotEmpty
@Schema(title =  "用户名", requiredMode = Schema.RequiredMode.REQUIRED)
private String username;
@NotEmpty
@Schema(title =  "旧密码", requiredMode = Schema.RequiredMode.REQUIRED)
private String oldPassword;
@NotEmpty
@Schema(title =  "新密码", requiredMode = Schema.RequiredMode.REQUIRED)
private String newPassword;
```

## SwaggerProperties

[mall/mall-common/src/main/java/com/macro/mall/common/domain/SwaggerProperties.java](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/domain/SwaggerProperties.java:1)

```java
public class SwaggerProperties
private String apiBasePackage;
private boolean enableSecurity;
private String title;
private String description;
private String version;
private String contactName;
private String contactUrl;
private String contactEmail;
```

## WebLog

[mall/mall-common/src/main/java/com/macro/mall/common/domain/WebLog.java](D:/project/mall/mall-common/src/main/java/com/macro/mall/common/domain/WebLog.java:1)

```java
public class WebLog
private String description;
private String username;
private Long startTime;
private Integer spendTime;
private String basePath;
private String uri;
private String url;
private String method;
private String ip;
private Object parameter;
private Object result;
```

## AdminUserDetails

[mall/mall-demo/src/main/java/com/macro/mall/demo/bo/AdminUserDetails.java](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/bo/AdminUserDetails.java:1)

```java
public class AdminUserDetails implements UserDetails
private UmsAdmin umsAdmin;
```

## PmsBrandDto

[mall/mall-demo/src/main/java/com/macro/mall/demo/dto/PmsBrandDto.java](D:/project/mall/mall-demo/src/main/java/com/macro/mall/demo/dto/PmsBrandDto.java:1)

```java
public class PmsBrandDto
@Schema(title = "品牌名称",requiredMode = Schema.RequiredMode.REQUIRED)
@NotNull(message = "名称不能为空")
private String name;
@Schema(title = "品牌首字母",requiredMode = Schema.RequiredMode.REQUIRED)
@NotNull(message = "首字母不能为空")
private String firstLetter;
@Schema(title = "排序字段")
@Min(value = 0, message = "排序最小为0")
private Integer sort;
@Schema(title = "是否为厂家制造商")
@FlagValidator(value = {"0","1"}, message = "厂家状态不正确")
private Integer factoryStatus;
@Schema(title = "是否进行显示")
@FlagValidator(value = {"0","1"}, message = "显示状态不正确")
private Integer showStatus;
@Schema(title = "品牌logo")
private String logo;
@Schema(title = "品牌大图")
private String bigPic;
@Schema(title = "品牌故事")
private String brandStory;
```

## CmsHelp

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsHelp.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsHelp.java:1)

```java
public class CmsHelp implements Serializable
private Long id;
private Long categoryId;
private String icon;
private String title;
private Integer showStatus;
private Date createTime;
private Integer readCount;
private String content;
```

## CmsHelpCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsHelpCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsHelpCategory.java:1)

```java
public class CmsHelpCategory implements Serializable
private Long id;
private String name;
@Schema(title = "分类图标")
private String icon;
@Schema(title = "专题数量")
private Integer helpCount;
private Integer showStatus;
private Integer sort;
```

## CmsMemberReport

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsMemberReport.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsMemberReport.java:1)

```java
public class CmsMemberReport implements Serializable
private Long id;
@Schema(title = "举报类型：0->商品评价；1->话题内容；2->用户评论")
private Integer reportType;
@Schema(title = "举报人")
private String reportMemberName;
private Date createTime;
private String reportObject;
@Schema(title = "举报状态：0->未处理；1->已处理")
private Integer reportStatus;
@Schema(title = "处理结果：0->无效；1->有效；2->恶意")
private Integer handleStatus;
private String note;
```

## CmsPrefrenceArea

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsPrefrenceArea.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsPrefrenceArea.java:1)

```java
public class CmsPrefrenceArea implements Serializable
private Long id;
private String name;
private String subTitle;
private Integer sort;
private Integer showStatus;
@Schema(title = "展示图片")
private byte[] pic;
```

## CmsPrefrenceAreaProductRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsPrefrenceAreaProductRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsPrefrenceAreaProductRelation.java:1)

```java
public class CmsPrefrenceAreaProductRelation implements Serializable
private Long id;
private Long prefrenceAreaId;
private Long productId;
```

## CmsSubject

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubject.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubject.java:1)

```java
public class CmsSubject implements Serializable
private Long id;
private Long categoryId;
private String title;
@Schema(title = "专题主图")
private String pic;
@Schema(title = "关联产品数量")
private Integer productCount;
private Integer recommendStatus;
private Date createTime;
private Integer collectCount;
private Integer readCount;
private Integer commentCount;
@Schema(title = "画册图片用逗号分割")
private String albumPics;
private String description;
@Schema(title = "显示状态：0->不显示；1->显示")
private Integer showStatus;
@Schema(title = "转发数")
private Integer forwardCount;
@Schema(title = "专题分类名称")
private String categoryName;
private String content;
```

## CmsSubjectCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectCategory.java:1)

```java
public class CmsSubjectCategory implements Serializable
private Long id;
private String name;
@Schema(title = "分类图标")
private String icon;
@Schema(title = "专题数量")
private Integer subjectCount;
private Integer showStatus;
private Integer sort;
```

## CmsSubjectComment

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectComment.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectComment.java:1)

```java
public class CmsSubjectComment implements Serializable
private Long id;
private Long subjectId;
private String memberNickName;
private String memberIcon;
private String content;
private Date createTime;
private Integer showStatus;
```

## CmsSubjectProductRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectProductRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectProductRelation.java:1)

```java
public class CmsSubjectProductRelation implements Serializable
private Long id;
private Long subjectId;
private Long productId;
```

## CmsTopic

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopic.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopic.java:1)

```java
public class CmsTopic implements Serializable
private Long id;
private Long categoryId;
private String name;
private Date createTime;
private Date startTime;
private Date endTime;
@Schema(title = "参与人数")
private Integer attendCount;
@Schema(title = "关注人数")
private Integer attentionCount;
private Integer readCount;
@Schema(title = "奖品名称")
private String awardName;
@Schema(title = "参与方式")
private String attendType;
@Schema(title = "话题内容")
private String content;
```

## CmsTopicCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopicCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopicCategory.java:1)

```java
public class CmsTopicCategory implements Serializable
private Long id;
private String name;
@Schema(title = "分类图标")
private String icon;
@Schema(title = "专题数量")
private Integer subjectCount;
private Integer showStatus;
private Integer sort;
```

## CmsTopicComment

[mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopicComment.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/CmsTopicComment.java:1)

```java
public class CmsTopicComment implements Serializable
private Long id;
private String memberNickName;
private Long topicId;
private String memberIcon;
private String content;
private Date createTime;
private Integer showStatus;
```

## OmsCartItem

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsCartItem.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsCartItem.java:1)

```java
public class OmsCartItem implements Serializable
private Long id;
private Long productId;
private Long productSkuId;
private Long memberId;
@Schema(title = "购买数量")
private Integer quantity;
@Schema(title = "添加到购物车的价格")
private BigDecimal price;
@Schema(title = "商品主图")
private String productPic;
@Schema(title = "商品名称")
private String productName;
@Schema(title = "商品副标题（卖点）")
private String productSubTitle;
@Schema(title = "商品sku条码")
private String productSkuCode;
@Schema(title = "会员昵称")
private String memberNickname;
@Schema(title = "创建时间")
private Date createDate;
@Schema(title = "修改时间")
private Date modifyDate;
@Schema(title = "是否删除")
private Integer deleteStatus;
@Schema(title = "商品分类")
private Long productCategoryId;
private String productBrand;
private String productSn;
@Schema(title = "商品销售属性:[{'key':'颜色','value':'颜色'},{'key':'容量','value':'4G'}]")
private String productAttr;
```

## OmsCompanyAddress

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsCompanyAddress.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsCompanyAddress.java:1)

```java
public class OmsCompanyAddress implements Serializable
private Long id;
@Schema(title = "地址名称")
private String addressName;
@Schema(title = "默认发货地址：0->否；1->是")
private Integer sendStatus;
@Schema(title = "是否默认收货地址：0->否；1->是")
private Integer receiveStatus;
@Schema(title = "收发货人姓名")
private String name;
@Schema(title = "收货人电话")
private String phone;
@Schema(title = "省/直辖市")
private String province;
@Schema(title = "市")
private String city;
@Schema(title = "区")
private String region;
@Schema(title = "详细地址")
private String detailAddress;
```

## OmsOrder

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrder.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrder.java:1)

```java
public class OmsOrder implements Serializable
@Schema(title = "订单id")
private Long id;
private Long memberId;
private Long couponId;
@Schema(title = "订单编号")
private String orderSn;
@Schema(title = "提交时间")
private Date createTime;
@Schema(title = "用户帐号")
private String memberUsername;
@Schema(title = "订单总金额")
private BigDecimal totalAmount;
@Schema(title = "应付金额（实际支付金额）")
private BigDecimal payAmount;
@Schema(title = "运费金额")
private BigDecimal freightAmount;
@Schema(title = "促销优化金额（促销价、满减、阶梯价）")
private BigDecimal promotionAmount;
@Schema(title = "积分抵扣金额")
private BigDecimal integrationAmount;
@Schema(title = "优惠券抵扣金额")
private BigDecimal couponAmount;
@Schema(title = "管理员后台调整订单使用的折扣金额")
private BigDecimal discountAmount;
@Schema(title = "支付方式：0->未支付；1->支付宝；2->微信")
private Integer payType;
@Schema(title = "订单来源：0->PC订单；1->app订单")
private Integer sourceType;
@Schema(title = "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单")
private Integer status;
@Schema(title = "订单类型：0->正常订单；1->秒杀订单")
private Integer orderType;
@Schema(title = "物流公司(配送方式)")
private String deliveryCompany;
@Schema(title = "物流单号")
private String deliverySn;
@Schema(title = "自动确认时间（天）")
private Integer autoConfirmDay;
@Schema(title = "可以获得的积分")
private Integer integration;
@Schema(title = "可以活动的成长值")
private Integer growth;
@Schema(title = "活动信息")
private String promotionInfo;
@Schema(title = "发票类型：0->不开发票；1->电子发票；2->纸质发票")
private Integer billType;
@Schema(title = "发票抬头")
private String billHeader;
@Schema(title = "发票内容")
private String billContent;
@Schema(title = "收票人电话")
private String billReceiverPhone;
@Schema(title = "收票人邮箱")
private String billReceiverEmail;
@Schema(title = "收货人姓名")
private String receiverName;
@Schema(title = "收货人电话")
private String receiverPhone;
@Schema(title = "收货人邮编")
private String receiverPostCode;
@Schema(title = "省份/直辖市")
private String receiverProvince;
@Schema(title = "城市")
private String receiverCity;
@Schema(title = "区")
private String receiverRegion;
@Schema(title = "详细地址")
private String receiverDetailAddress;
@Schema(title = "订单备注")
private String note;
@Schema(title = "确认收货状态：0->未确认；1->已确认")
private Integer confirmStatus;
@Schema(title = "删除状态：0->未删除；1->已删除")
private Integer deleteStatus;
@Schema(title = "下单时使用的积分")
private Integer useIntegration;
@Schema(title = "支付时间")
private Date paymentTime;
@Schema(title = "发货时间")
private Date deliveryTime;
@Schema(title = "确认收货时间")
private Date receiveTime;
@Schema(title = "评价时间")
private Date commentTime;
@Schema(title = "修改时间")
private Date modifyTime;
```

## OmsOrderItem

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderItem.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderItem.java:1)

```java
public class OmsOrderItem implements Serializable
private Long id;
@Schema(title = "订单id")
private Long orderId;
@Schema(title = "订单编号")
private String orderSn;
private Long productId;
private String productPic;
private String productName;
private String productBrand;
private String productSn;
@Schema(title = "销售价格")
private BigDecimal productPrice;
@Schema(title = "购买数量")
private Integer productQuantity;
@Schema(title = "商品sku编号")
private Long productSkuId;
@Schema(title = "商品sku条码")
private String productSkuCode;
@Schema(title = "商品分类id")
private Long productCategoryId;
@Schema(title = "商品促销名称")
private String promotionName;
@Schema(title = "商品促销分解金额")
private BigDecimal promotionAmount;
@Schema(title = "优惠券优惠分解金额")
private BigDecimal couponAmount;
@Schema(title = "积分优惠分解金额")
private BigDecimal integrationAmount;
@Schema(title = "该商品经过优惠后的分解金额")
private BigDecimal realAmount;
private Integer giftIntegration;
private Integer giftGrowth;
@Schema(title = "商品销售属性:[{'key':'颜色','value':'颜色'},{'key':'容量','value':'4G'}]")
private String productAttr;
```

## OmsOrderOperateHistory

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderOperateHistory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderOperateHistory.java:1)

```java
public class OmsOrderOperateHistory implements Serializable
private Long id;
@Schema(title = "订单id")
private Long orderId;
@Schema(title = "操作人：用户；系统；后台管理员")
private String operateMan;
@Schema(title = "操作时间")
private Date createTime;
@Schema(title = "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单")
private Integer orderStatus;
@Schema(title = "备注")
private String note;
```

## OmsOrderReturnApply

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnApply.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnApply.java:1)

```java
public class OmsOrderReturnApply implements Serializable
private Long id;
@Schema(title = "订单id")
private Long orderId;
@Schema(title = "收货地址表id")
private Long companyAddressId;
@Schema(title = "退货商品id")
private Long productId;
@Schema(title = "订单编号")
private String orderSn;
@Schema(title = "申请时间")
private Date createTime;
@Schema(title = "会员用户名")
private String memberUsername;
@Schema(title = "退款金额")
private BigDecimal returnAmount;
@Schema(title = "退货人姓名")
private String returnName;
@Schema(title = "退货人电话")
private String returnPhone;
@Schema(title = "申请状态：0->待处理；1->退货中；2->已完成；3->已拒绝")
private Integer status;
@Schema(title = "处理时间")
private Date handleTime;
@Schema(title = "商品图片")
private String productPic;
@Schema(title = "商品名称")
private String productName;
@Schema(title = "商品品牌")
private String productBrand;
@Schema(title = "商品销售属性：颜色：红色；尺码：xl;")
private String productAttr;
@Schema(title = "退货数量")
private Integer productCount;
@Schema(title = "商品单价")
private BigDecimal productPrice;
@Schema(title = "商品实际支付单价")
private BigDecimal productRealPrice;
@Schema(title = "原因")
private String reason;
@Schema(title = "描述")
private String description;
@Schema(title = "凭证图片，以逗号隔开")
private String proofPics;
@Schema(title = "处理备注")
private String handleNote;
@Schema(title = "处理人员")
private String handleMan;
@Schema(title = "收货人")
private String receiveMan;
@Schema(title = "收货时间")
private Date receiveTime;
@Schema(title = "收货备注")
private String receiveNote;
```

## OmsOrderReturnReason

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnReason.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnReason.java:1)

```java
public class OmsOrderReturnReason implements Serializable
private Long id;
@Schema(title = "退货类型")
private String name;
private Integer sort;
@Schema(title = "状态：0->不启用；1->启用")
private Integer status;
@Schema(title = "添加时间")
private Date createTime;
```

## OmsOrderSetting

[mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderSetting.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/OmsOrderSetting.java:1)

```java
public class OmsOrderSetting implements Serializable
private Long id;
@Schema(title = "秒杀订单超时关闭时间(分)")
private Integer flashOrderOvertime;
@Schema(title = "正常订单超时时间(分)")
private Integer normalOrderOvertime;
@Schema(title = "发货后自动确认收货时间（天）")
private Integer confirmOvertime;
@Schema(title = "自动完成交易时间，不能申请售后（天）")
private Integer finishOvertime;
@Schema(title = "订单完成后自动好评时间（天）")
private Integer commentOvertime;
```

## PmsAlbum

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsAlbum.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsAlbum.java:1)

```java
public class PmsAlbum implements Serializable
private Long id;
private String name;
private String coverPic;
private Integer picCount;
private Integer sort;
private String description;
```

## PmsAlbumPic

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsAlbumPic.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsAlbumPic.java:1)

```java
public class PmsAlbumPic implements Serializable
private Long id;
private Long albumId;
private String pic;
```

## PmsBrand

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsBrand.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsBrand.java:1)

```java
public class PmsBrand implements Serializable
private Long id;
private String name;
@Schema(title = "首字母")
private String firstLetter;
private Integer sort;
@Schema(title = "是否为品牌制造商：0->不是；1->是")
private Integer factoryStatus;
private Integer showStatus;
@Schema(title = "产品数量")
private Integer productCount;
@Schema(title = "产品评论数量")
private Integer productCommentCount;
@Schema(title = "品牌logo")
private String logo;
@Schema(title = "专区大图")
private String bigPic;
@Schema(title = "品牌故事")
private String brandStory;
```

## PmsComment

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsComment.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsComment.java:1)

```java
public class PmsComment implements Serializable
private Long id;
private Long productId;
private String memberNickName;
private String productName;
@Schema(title = "评价星数：0->5")
private Integer star;
@Schema(title = "评价的ip")
private String memberIp;
private Date createTime;
private Integer showStatus;
@Schema(title = "购买时的商品属性")
private String productAttribute;
private Integer collectCouont;
private Integer readCount;
@Schema(title = "上传图片地址，以逗号隔开")
private String pics;
@Schema(title = "评论用户头像")
private String memberIcon;
private Integer replayCount;
private String content;
```

## PmsCommentReplay

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsCommentReplay.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsCommentReplay.java:1)

```java
public class PmsCommentReplay implements Serializable
private Long id;
private Long commentId;
private String memberNickName;
private String memberIcon;
private String content;
private Date createTime;
@Schema(title = "评论人员类型；0->会员；1->管理员")
private Integer type;
```

## PmsFeightTemplate

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsFeightTemplate.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsFeightTemplate.java:1)

```java
public class PmsFeightTemplate implements Serializable
private Long id;
private String name;
@Schema(title = "计费类型:0->按重量；1->按件数")
private Integer chargeType;
@Schema(title = "首重kg")
private BigDecimal firstWeight;
@Schema(title = "首费（元）")
private BigDecimal firstFee;
private BigDecimal continueWeight;
private BigDecimal continmeFee;
@Schema(title = "目的地（省、市）")
private String dest;
```

## PmsMemberPrice

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsMemberPrice.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsMemberPrice.java:1)

```java
public class PmsMemberPrice implements Serializable
private Long id;
private Long productId;
private Long memberLevelId;
@Schema(title = "会员价格")
private BigDecimal memberPrice;
private String memberLevelName;
```

## PmsProduct

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java:1)

```java
public class PmsProduct implements Serializable
private Long id;
private Long brandId;
private Long productCategoryId;
private Long feightTemplateId;
private Long productAttributeCategoryId;
private String name;
private String pic;
@Schema(title = "货号")
private String productSn;
@Schema(title = "删除状态：0->未删除；1->已删除")
private Integer deleteStatus;
@Schema(title = "上架状态：0->下架；1->上架")
private Integer publishStatus;
@Schema(title = "新品状态:0->不是新品；1->新品")
private Integer newStatus;
@Schema(title = "推荐状态；0->不推荐；1->推荐")
private Integer recommandStatus;
@Schema(title = "审核状态：0->未审核；1->审核通过")
private Integer verifyStatus;
@Schema(title = "排序")
private Integer sort;
@Schema(title = "销量")
private Integer sale;
private BigDecimal price;
@Schema(title = "促销价格")
private BigDecimal promotionPrice;
@Schema(title = "赠送的成长值")
private Integer giftGrowth;
@Schema(title = "赠送的积分")
private Integer giftPoint;
@Schema(title = "限制使用的积分数")
private Integer usePointLimit;
@Schema(title = "副标题")
private String subTitle;
@Schema(title = "市场价")
private BigDecimal originalPrice;
@Schema(title = "库存")
private Integer stock;
@Schema(title = "库存预警值")
private Integer lowStock;
@Schema(title = "单位")
private String unit;
@Schema(title = "商品重量，默认为克")
private BigDecimal weight;
@Schema(title = "是否为预告商品：0->不是；1->是")
private Integer previewStatus;
@Schema(title = "以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮")
private String serviceIds;
private String keywords;
private String note;
@Schema(title = "画册图片，连产品图片限制为5张，以逗号分割")
private String albumPics;
private String detailTitle;
@Schema(title = "促销开始时间")
private Date promotionStartTime;
@Schema(title = "促销结束时间")
private Date promotionEndTime;
@Schema(title = "活动限购数量")
private Integer promotionPerLimit;
@Schema(title = "促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购")
private Integer promotionType;
@Schema(title = "品牌名称")
private String brandName;
@Schema(title = "商品分类名称")
private String productCategoryName;
@Schema(title = "商品描述")
private String description;
private String detailDesc;
@Schema(title = "产品详情网页内容")
private String detailHtml;
@Schema(title = "移动端网页详情")
private String detailMobileHtml;
```

## PmsProductAttribute

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttribute.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttribute.java:1)

```java
public class PmsProductAttribute implements Serializable
private Long id;
private Long productAttributeCategoryId;
private String name;
@Schema(title = "属性选择类型：0->唯一；1->单选；2->多选")
private Integer selectType;
@Schema(title = "属性录入方式：0->手工录入；1->从列表中选取")
private Integer inputType;
@Schema(title = "可选值列表，以逗号隔开")
private String inputList;
@Schema(title = "排序字段：最高的可以单独上传图片")
private Integer sort;
@Schema(title = "分类筛选样式：1->普通；1->颜色")
private Integer filterType;
@Schema(title = "检索类型；0->不需要进行检索；1->关键字检索；2->范围检索")
private Integer searchType;
@Schema(title = "相同属性产品是否关联；0->不关联；1->关联")
private Integer relatedStatus;
@Schema(title = "是否支持手动新增；0->不支持；1->支持")
private Integer handAddStatus;
@Schema(title = "属性的类型；0->规格；1->参数")
private Integer type;
```

## PmsProductAttributeCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeCategory.java:1)

```java
public class PmsProductAttributeCategory implements Serializable
private Long id;
private String name;
@Schema(title = "属性数量")
private Integer attributeCount;
@Schema(title = "参数数量")
private Integer paramCount;
```

## PmsProductAttributeValue

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeValue.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeValue.java:1)

```java
public class PmsProductAttributeValue implements Serializable
private Long id;
private Long productId;
private Long productAttributeId;
@Schema(title = "手动添加规格或参数的值，参数单值，规格有多个时以逗号隔开")
private String value;
```

## PmsProductCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategory.java:1)

```java
public class PmsProductCategory implements Serializable
private Long id;
@Schema(title = "上机分类的编号：0表示一级分类")
private Long parentId;
private String name;
@Schema(title = "分类级别：0->1级；1->2级")
private Integer level;
private Integer productCount;
private String productUnit;
@Schema(title = "是否显示在导航栏：0->不显示；1->显示")
private Integer navStatus;
@Schema(title = "显示状态：0->不显示；1->显示")
private Integer showStatus;
private Integer sort;
@Schema(title = "图标")
private String icon;
private String keywords;
@Schema(title = "描述")
private String description;
```

## PmsProductCategoryAttributeRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryAttributeRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryAttributeRelation.java:1)

```java
public class PmsProductCategoryAttributeRelation implements Serializable
private Long id;
private Long productCategoryId;
private Long productAttributeId;
```

## PmsProductFullReduction

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductFullReduction.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductFullReduction.java:1)

```java
public class PmsProductFullReduction implements Serializable
private Long id;
private Long productId;
private BigDecimal fullPrice;
private BigDecimal reducePrice;
```

## PmsProductLadder

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductLadder.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductLadder.java:1)

```java
public class PmsProductLadder implements Serializable
private Long id;
private Long productId;
@Schema(title = "满足的商品数量")
private Integer count;
@Schema(title = "折扣")
private BigDecimal discount;
@Schema(title = "折后价格")
private BigDecimal price;
```

## PmsProductOperateLog

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductOperateLog.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductOperateLog.java:1)

```java
public class PmsProductOperateLog implements Serializable
private Long id;
private Long productId;
private BigDecimal priceOld;
private BigDecimal priceNew;
private BigDecimal salePriceOld;
private BigDecimal salePriceNew;
@Schema(title = "赠送的积分")
private Integer giftPointOld;
private Integer giftPointNew;
private Integer usePointLimitOld;
private Integer usePointLimitNew;
@Schema(title = "操作人")
private String operateMan;
private Date createTime;
```

## PmsProductVertifyRecord

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductVertifyRecord.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsProductVertifyRecord.java:1)

```java
public class PmsProductVertifyRecord implements Serializable
private Long id;
private Long productId;
private Date createTime;
@Schema(title = "审核人")
private String vertifyMan;
private Integer status;
@Schema(title = "反馈详情")
private String detail;
```

## PmsSkuStock

[mall/mall-mbg/src/main/java/com/macro/mall/model/PmsSkuStock.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/PmsSkuStock.java:1)

```java
public class PmsSkuStock implements Serializable
private Long id;
private Long productId;
@Schema(title = "sku编码")
private String skuCode;
private BigDecimal price;
@Schema(title = "库存")
private Integer stock;
@Schema(title = "预警库存")
private Integer lowStock;
@Schema(title = "展示图片")
private String pic;
@Schema(title = "销量")
private Integer sale;
@Schema(title = "单品促销价格")
private BigDecimal promotionPrice;
@Schema(title = "锁定库存")
private Integer lockStock;
@Schema(title = "商品销售属性，json格式")
private String spData;
```

## SmsCoupon

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCoupon.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCoupon.java:1)

```java
public class SmsCoupon implements Serializable
private Long id;
@Schema(title = "优惠券类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券")
private Integer type;
private String name;
@Schema(title = "使用平台：0->全部；1->移动；2->PC")
private Integer platform;
@Schema(title = "数量")
private Integer count;
@Schema(title = "金额")
private BigDecimal amount;
@Schema(title = "每人限领张数")
private Integer perLimit;
@Schema(title = "使用门槛；0表示无门槛")
private BigDecimal minPoint;
private Date startTime;
private Date endTime;
@Schema(title = "使用类型：0->全场通用；1->指定分类；2->指定商品")
private Integer useType;
@Schema(title = "备注")
private String note;
@Schema(title = "发行数量")
private Integer publishCount;
@Schema(title = "已使用数量")
private Integer useCount;
@Schema(title = "领取数量")
private Integer receiveCount;
@Schema(title = "可以领取的日期")
private Date enableTime;
@Schema(title = "优惠码")
private String code;
@Schema(title = "可领取的会员类型：0->无限时")
private Integer memberLevel;
```

## SmsCouponHistory

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponHistory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponHistory.java:1)

```java
public class SmsCouponHistory implements Serializable
private Long id;
private Long couponId;
private Long memberId;
private String couponCode;
@Schema(title = "领取人昵称")
private String memberNickname;
@Schema(title = "获取类型：0->后台赠送；1->主动获取")
private Integer getType;
private Date createTime;
@Schema(title = "使用状态：0->未使用；1->已使用；2->已过期")
private Integer useStatus;
@Schema(title = "使用时间")
private Date useTime;
@Schema(title = "订单编号")
private Long orderId;
@Schema(title = "订单号码")
private String orderSn;
```

## SmsCouponProductCategoryRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponProductCategoryRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponProductCategoryRelation.java:1)

```java
public class SmsCouponProductCategoryRelation implements Serializable
private Long id;
private Long couponId;
private Long productCategoryId;
@Schema(title = "产品分类名称")
private String productCategoryName;
@Schema(title = "父分类名称")
private String parentCategoryName;
```

## SmsCouponProductRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponProductRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsCouponProductRelation.java:1)

```java
public class SmsCouponProductRelation implements Serializable
private Long id;
private Long couponId;
private Long productId;
@Schema(title = "商品名称")
private String productName;
@Schema(title = "商品编码")
private String productSn;
```

## SmsFlashPromotion

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotion.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotion.java:1)

```java
public class SmsFlashPromotion implements Serializable
private Long id;
@Schema(title = "秒杀时间段名称")
private String title;
@Schema(title = "开始日期")
private Date startDate;
@Schema(title = "结束日期")
private Date endDate;
@Schema(title = "上下线状态")
private Integer status;
@Schema(title = "创建时间")
private Date createTime;
```

## SmsFlashPromotionLog

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionLog.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionLog.java:1)

```java
public class SmsFlashPromotionLog implements Serializable
private Integer id;
private Integer memberId;
private Long productId;
private String memberPhone;
private String productName;
@Schema(title = "会员订阅时间")
private Date subscribeTime;
private Date sendTime;
```

## SmsFlashPromotionProductRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionProductRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionProductRelation.java:1)

```java
public class SmsFlashPromotionProductRelation implements Serializable
@Schema(title = "编号")
private Long id;
private Long flashPromotionId;
@Schema(title = "编号")
private Long flashPromotionSessionId;
private Long productId;
@Schema(title = "限时购价格")
private BigDecimal flashPromotionPrice;
@Schema(title = "限时购数量")
private Integer flashPromotionCount;
@Schema(title = "每人限购数量")
private Integer flashPromotionLimit;
@Schema(title = "排序")
private Integer sort;
```

## SmsFlashPromotionSession

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionSession.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionSession.java:1)

```java
public class SmsFlashPromotionSession implements Serializable
@Schema(title = "编号")
private Long id;
@Schema(title = "场次名称")
private String name;
@Schema(title = "每日开始时间")
private Date startTime;
@Schema(title = "每日结束时间")
private Date endTime;
@Schema(title = "启用状态：0->不启用；1->启用")
private Integer status;
@Schema(title = "创建时间")
private Date createTime;
```

## SmsHomeAdvertise

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeAdvertise.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeAdvertise.java:1)

```java
public class SmsHomeAdvertise implements Serializable
private Long id;
private String name;
@Schema(title = "轮播位置：0->PC首页轮播；1->app首页轮播")
private Integer type;
private String pic;
private Date startTime;
private Date endTime;
@Schema(title = "上下线状态：0->下线；1->上线")
private Integer status;
@Schema(title = "点击数")
private Integer clickCount;
@Schema(title = "下单数")
private Integer orderCount;
@Schema(title = "链接地址")
private String url;
@Schema(title = "备注")
private String note;
@Schema(title = "排序")
private Integer sort;
```

## SmsHomeBrand

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeBrand.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeBrand.java:1)

```java
public class SmsHomeBrand implements Serializable
private Long id;
private Long brandId;
private String brandName;
private Integer recommendStatus;
private Integer sort;
```

## SmsHomeNewProduct

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeNewProduct.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeNewProduct.java:1)

```java
public class SmsHomeNewProduct implements Serializable
private Long id;
private Long productId;
private String productName;
private Integer recommendStatus;
private Integer sort;
```

## SmsHomeRecommendProduct

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeRecommendProduct.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeRecommendProduct.java:1)

```java
public class SmsHomeRecommendProduct implements Serializable
private Long id;
private Long productId;
private String productName;
private Integer recommendStatus;
private Integer sort;
```

## SmsHomeRecommendSubject

[mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeRecommendSubject.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/SmsHomeRecommendSubject.java:1)

```java
public class SmsHomeRecommendSubject implements Serializable
private Long id;
private Long subjectId;
private String subjectName;
private Integer recommendStatus;
private Integer sort;
```

## UmsAdmin

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdmin.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdmin.java:1)

```java
public class UmsAdmin implements Serializable
private Long id;
private String username;
private String password;
@Schema(title = "头像")
private String icon;
@Schema(title = "邮箱")
private String email;
@Schema(title = "昵称")
private String nickName;
@Schema(title = "备注信息")
private String note;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "最后登录时间")
private Date loginTime;
@Schema(title = "帐号启用状态：0->禁用；1->启用")
private Integer status;
```

## UmsAdminLoginLog

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminLoginLog.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminLoginLog.java:1)

```java
public class UmsAdminLoginLog implements Serializable
private Long id;
private Long adminId;
private Date createTime;
private String ip;
private String address;
@Schema(title = "浏览器登录类型")
private String userAgent;
```

## UmsAdminPermissionRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminPermissionRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminPermissionRelation.java:1)

```java
public class UmsAdminPermissionRelation implements Serializable
private Long id;
private Long adminId;
private Long permissionId;
private Integer type;
```

## UmsAdminRoleRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminRoleRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsAdminRoleRelation.java:1)

```java
public class UmsAdminRoleRelation implements Serializable
private Long id;
private Long adminId;
private Long roleId;
```

## UmsGrowthChangeHistory

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsGrowthChangeHistory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsGrowthChangeHistory.java:1)

```java
public class UmsGrowthChangeHistory implements Serializable
private Long id;
private Long memberId;
private Date createTime;
@Schema(title = "改变类型：0->增加；1->减少")
private Integer changeType;
@Schema(title = "积分改变数量")
private Integer changeCount;
@Schema(title = "操作人员")
private String operateMan;
@Schema(title = "操作备注")
private String operateNote;
@Schema(title = "积分来源：0->购物；1->管理员修改")
private Integer sourceType;
```

## UmsIntegrationChangeHistory

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsIntegrationChangeHistory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsIntegrationChangeHistory.java:1)

```java
public class UmsIntegrationChangeHistory implements Serializable
private Long id;
private Long memberId;
private Date createTime;
@Schema(title = "改变类型：0->增加；1->减少")
private Integer changeType;
@Schema(title = "积分改变数量")
private Integer changeCount;
@Schema(title = "操作人员")
private String operateMan;
@Schema(title = "操作备注")
private String operateNote;
@Schema(title = "积分来源：0->购物；1->管理员修改")
private Integer sourceType;
```

## UmsIntegrationConsumeSetting

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsIntegrationConsumeSetting.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsIntegrationConsumeSetting.java:1)

```java
public class UmsIntegrationConsumeSetting implements Serializable
private Long id;
@Schema(title = "每一元需要抵扣的积分数量")
private Integer deductionPerAmount;
@Schema(title = "每笔订单最高抵用百分比")
private Integer maxPercentPerOrder;
@Schema(title = "每次使用积分最小单位100")
private Integer useUnit;
@Schema(title = "是否可以和优惠券同用；0->不可以；1->可以")
private Integer couponStatus;
```

## UmsMember

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java:1)

```java
public class UmsMember implements Serializable
private Long id;
private Long memberLevelId;
@Schema(title = "用户名")
private String username;
@Schema(title = "密码")
private String password;
@Schema(title = "昵称")
private String nickname;
@Schema(title = "手机号码")
private String phone;
@Schema(title = "帐号启用状态:0->禁用；1->启用")
private Integer status;
@Schema(title = "注册时间")
private Date createTime;
@Schema(title = "头像")
private String icon;
@Schema(title = "性别：0->未知；1->男；2->女")
private Integer gender;
@Schema(title = "生日")
private Date birthday;
@Schema(title = "所做城市")
private String city;
@Schema(title = "职业")
private String job;
@Schema(title = "个性签名")
private String personalizedSignature;
@Schema(title = "用户来源")
private Integer sourceType;
@Schema(title = "积分")
private Integer integration;
@Schema(title = "成长值")
private Integer growth;
@Schema(title = "剩余抽奖次数")
private Integer luckeyCount;
@Schema(title = "历史积分数量")
private Integer historyIntegration;
```

## UmsMemberLevel

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLevel.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLevel.java:1)

```java
public class UmsMemberLevel implements Serializable
private Long id;
private String name;
private Integer growthPoint;
@Schema(title = "是否为默认等级：0->不是；1->是")
private Integer defaultStatus;
@Schema(title = "免运费标准")
private BigDecimal freeFreightPoint;
@Schema(title = "每次评价获取的成长值")
private Integer commentGrowthPoint;
@Schema(title = "是否有免邮特权")
private Integer priviledgeFreeFreight;
@Schema(title = "是否有签到特权")
private Integer priviledgeSignIn;
@Schema(title = "是否有评论获奖励特权")
private Integer priviledgeComment;
@Schema(title = "是否有专享活动特权")
private Integer priviledgePromotion;
@Schema(title = "是否有会员价格特权")
private Integer priviledgeMemberPrice;
@Schema(title = "是否有生日特权")
private Integer priviledgeBirthday;
private String note;
```

## UmsMemberLoginLog

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLoginLog.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLoginLog.java:1)

```java
public class UmsMemberLoginLog implements Serializable
private Long id;
private Long memberId;
private Date createTime;
private String ip;
private String city;
@Schema(title = "登录类型：0->PC；1->android;2->ios;3->小程序")
private Integer loginType;
private String province;
```

## UmsMemberMemberTagRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberMemberTagRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberMemberTagRelation.java:1)

```java
public class UmsMemberMemberTagRelation implements Serializable
private Long id;
private Long memberId;
private Long tagId;
```

## UmsMemberProductCategoryRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberProductCategoryRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberProductCategoryRelation.java:1)

```java
public class UmsMemberProductCategoryRelation implements Serializable
private Long id;
private Long memberId;
private Long productCategoryId;
```

## UmsMemberReceiveAddress

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberReceiveAddress.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberReceiveAddress.java:1)

```java
public class UmsMemberReceiveAddress implements Serializable
private Long id;
private Long memberId;
@Schema(title = "收货人名称")
private String name;
private String phoneNumber;
@Schema(title = "是否为默认")
private Integer defaultStatus;
@Schema(title = "邮政编码")
private String postCode;
@Schema(title = "省份/直辖市")
private String province;
@Schema(title = "城市")
private String city;
@Schema(title = "区")
private String region;
@Schema(title = "详细地址(街道)")
private String detailAddress;
```

## UmsMemberRuleSetting

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberRuleSetting.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberRuleSetting.java:1)

```java
public class UmsMemberRuleSetting implements Serializable
private Long id;
@Schema(title = "连续签到天数")
private Integer continueSignDay;
@Schema(title = "连续签到赠送数量")
private Integer continueSignPoint;
@Schema(title = "每消费多少元获取1个点")
private BigDecimal consumePerPoint;
@Schema(title = "最低获取点数的订单金额")
private BigDecimal lowOrderAmount;
@Schema(title = "每笔订单最高获取点数")
private Integer maxPointPerOrder;
@Schema(title = "类型：0->积分规则；1->成长值规则")
private Integer type;
```

## UmsMemberStatisticsInfo

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberStatisticsInfo.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberStatisticsInfo.java:1)

```java
public class UmsMemberStatisticsInfo implements Serializable
private Long id;
private Long memberId;
@Schema(title = "累计消费金额")
private BigDecimal consumeAmount;
@Schema(title = "订单数量")
private Integer orderCount;
@Schema(title = "优惠券数量")
private Integer couponCount;
@Schema(title = "评价数")
private Integer commentCount;
@Schema(title = "退货数量")
private Integer returnOrderCount;
@Schema(title = "登录次数")
private Integer loginCount;
@Schema(title = "关注数量")
private Integer attendCount;
@Schema(title = "粉丝数量")
private Integer fansCount;
private Integer collectProductCount;
private Integer collectSubjectCount;
private Integer collectTopicCount;
private Integer collectCommentCount;
private Integer inviteFriendCount;
@Schema(title = "最后一次下订单时间")
private Date recentOrderTime;
```

## UmsMemberTag

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberTag.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberTag.java:1)

```java
public class UmsMemberTag implements Serializable
private Long id;
private String name;
@Schema(title = "自动打标签完成订单数量")
private Integer finishOrderCount;
@Schema(title = "自动打标签完成订单金额")
private BigDecimal finishOrderAmount;
```

## UmsMemberTask

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberTask.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMemberTask.java:1)

```java
public class UmsMemberTask implements Serializable
private Long id;
private String name;
@Schema(title = "赠送成长值")
private Integer growth;
@Schema(title = "赠送积分")
private Integer intergration;
@Schema(title = "任务类型：0->新手任务；1->日常任务")
private Integer type;
```

## UmsMenu

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMenu.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsMenu.java:1)

```java
public class UmsMenu implements Serializable
private Long id;
@Schema(title = "父级ID")
private Long parentId;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "菜单名称")
private String title;
@Schema(title = "菜单级数")
private Integer level;
@Schema(title = "菜单排序")
private Integer sort;
@Schema(title = "前端名称")
private String name;
@Schema(title = "前端图标")
private String icon;
@Schema(title = "前端隐藏")
private Integer hidden;
```

## UmsPermission

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsPermission.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsPermission.java:1)

```java
public class UmsPermission implements Serializable
private Long id;
@Schema(title = "父级权限id")
private Long pid;
@Schema(title = "名称")
private String name;
@Schema(title = "权限值")
private String value;
@Schema(title = "图标")
private String icon;
@Schema(title = "权限类型：0->目录；1->菜单；2->按钮（接口绑定权限）")
private Integer type;
@Schema(title = "前端资源路径")
private String uri;
@Schema(title = "启用状态；0->禁用；1->启用")
private Integer status;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "排序")
private Integer sort;
```

## UmsResource

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsResource.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsResource.java:1)

```java
public class UmsResource implements Serializable
private Long id;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "资源名称")
private String name;
@Schema(title = "资源URL")
private String url;
@Schema(title = "描述")
private String description;
@Schema(title = "资源分类ID")
private Long categoryId;
```

## UmsResourceCategory

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsResourceCategory.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsResourceCategory.java:1)

```java
public class UmsResourceCategory implements Serializable
private Long id;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "分类名称")
private String name;
@Schema(title = "排序")
private Integer sort;
```

## UmsRole

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRole.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRole.java:1)

```java
public class UmsRole implements Serializable
private Long id;
@Schema(title = "名称")
private String name;
@Schema(title = "描述")
private String description;
@Schema(title = "后台用户数量")
private Integer adminCount;
@Schema(title = "创建时间")
private Date createTime;
@Schema(title = "启用状态：0->禁用；1->启用")
private Integer status;
private Integer sort;
```

## UmsRoleMenuRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRoleMenuRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRoleMenuRelation.java:1)

```java
public class UmsRoleMenuRelation implements Serializable
private Long id;
@Schema(title = "角色ID")
private Long roleId;
@Schema(title = "菜单ID")
private Long menuId;
```

## UmsRolePermissionRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRolePermissionRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRolePermissionRelation.java:1)

```java
public class UmsRolePermissionRelation implements Serializable
private Long id;
private Long roleId;
private Long permissionId;
```

## UmsRoleResourceRelation

[mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRoleResourceRelation.java](D:/project/mall/mall-mbg/src/main/java/com/macro/mall/model/UmsRoleResourceRelation.java:1)

```java
public class UmsRoleResourceRelation implements Serializable
private Long id;
@Schema(title = "角色ID")
private Long roleId;
@Schema(title = "资源ID")
private Long resourceId;
```

## AliPayParam

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/AliPayParam.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/AliPayParam.java:1)

```java
public class AliPayParam
private String outTradeNo;
private String subject;
private BigDecimal totalAmount;
```

## CartProduct

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/CartProduct.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/CartProduct.java:1)

```java
public class CartProduct extends PmsProduct
@Schema(title = "商品属性列表")
private List<PmsProductAttribute> productAttributeList;
@Schema(title = "商品SKU库存列表")
private List<PmsSkuStock> skuStockList;
```

## CartPromotionItem

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/CartPromotionItem.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/CartPromotionItem.java:1)

```java
public class CartPromotionItem extends OmsCartItem
@Schema(title = "促销活动信息")
private String promotionMessage;
@Schema(title = "促销活动减去的金额，针对每个商品")
private BigDecimal reduceAmount;
@Schema(title = "剩余库存-锁定库存")
private Integer realStock;
@Schema(title = "购买商品赠送积分")
private Integer integration;
@Schema(title = "购买商品赠送成长值")
private Integer growth;
```

## ConfirmOrderResult

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/ConfirmOrderResult.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/ConfirmOrderResult.java:1)

```java
public class ConfirmOrderResult
@Schema(title = "包含优惠信息的购物车信息")
private List<CartPromotionItem> cartPromotionItemList;
@Schema(title = "用户收货地址列表")
private List<UmsMemberReceiveAddress> memberReceiveAddressList;
@Schema(title = "用户可用优惠券列表")
private List<SmsCouponHistoryDetail> couponHistoryDetailList;
@Schema(title = "积分使用规则")
private UmsIntegrationConsumeSetting integrationConsumeSetting;
@Schema(title = "会员持有的积分")
private Integer memberIntegration;
@Schema(title = "计算的金额")
private CalcAmount calcAmount;
// 以下字段属于嵌套类型：public static class CalcAmount
@Schema(title = "订单商品总金额")
private BigDecimal totalAmount;
@Schema(title = "运费")
private BigDecimal freightAmount;
@Schema(title = "活动优惠")
private BigDecimal promotionAmount;
@Schema(title = "应付金额")
private BigDecimal payAmount;
```

## FlashPromotionProduct

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/FlashPromotionProduct.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/FlashPromotionProduct.java:1)

```java
public class FlashPromotionProduct extends PmsProduct
@Schema(title = "秒杀价格")
private BigDecimal flashPromotionPrice;
@Schema(title = "用于秒杀到数量")
private Integer flashPromotionCount;
@Schema(title = "秒杀限购数量")
private Integer flashPromotionLimit;
```

## HomeContentResult

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/HomeContentResult.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/HomeContentResult.java:1)

```java
public class HomeContentResult
@Schema(title = "轮播广告")
private List<SmsHomeAdvertise> advertiseList;
@Schema(title = "推荐品牌")
private List<PmsBrand> brandList;
@Schema(title = "当前秒杀场次")
private HomeFlashPromotion homeFlashPromotion;
@Schema(title = "新品推荐")
private List<PmsProduct> newProductList;
@Schema(title = "人气推荐")
private List<PmsProduct> hotProductList;
@Schema(title = "推荐专题")
private List<CmsSubject> subjectList;
```

## HomeFlashPromotion

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/HomeFlashPromotion.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/HomeFlashPromotion.java:1)

```java
public class HomeFlashPromotion
@Schema(title = "本场开始时间")
private Date startTime;
@Schema(title = "本场结束时间")
private Date endTime;
@Schema(title = "下场开始时间")
private Date nextStartTime;
@Schema(title = "下场结束时间")
private Date nextEndTime;
@Schema(title = "属于该秒杀活动的商品")
private List<FlashPromotionProduct> productList;
```

## MemberBrandAttention

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberBrandAttention.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberBrandAttention.java:1)

```java
public class MemberBrandAttention
@Id
private String id;
@Indexed
private Long memberId;
private String memberNickname;
private String memberIcon;
@Indexed
private Long brandId;
private String brandName;
private String brandLogo;
private String brandCity;
private Date createTime;
```

## MemberDetails

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberDetails.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberDetails.java:1)

```java
public class MemberDetails implements UserDetails
private final UmsMember umsMember;
```

## MemberProductCollection

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberProductCollection.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberProductCollection.java:1)

```java
public class MemberProductCollection
@Id
private String id;
@Indexed
private Long memberId;
private String memberNickname;
private String memberIcon;
@Indexed
private Long productId;
private String productName;
private String productPic;
private String productSubTitle;
private String productPrice;
private Date createTime;
```

## MemberReadHistory

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberReadHistory.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/MemberReadHistory.java:1)

```java
public class MemberReadHistory
@Id
private String id;
@Indexed
private Long memberId;
private String memberNickname;
private String memberIcon;
@Indexed
private Long productId;
private String productName;
private String productPic;
private String productSubTitle;
private String productPrice;
private Date createTime;
```

## OmsOrderDetail

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OmsOrderDetail.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OmsOrderDetail.java:1)

```java
public class OmsOrderDetail extends OmsOrder
@Schema(title = "订单商品列表")
private List<OmsOrderItem> orderItemList;
```

## OmsOrderReturnApplyParam

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OmsOrderReturnApplyParam.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OmsOrderReturnApplyParam.java:1)

```java
public class OmsOrderReturnApplyParam
@Schema(title = "订单id")
private Long orderId;
@Schema(title = "退货商品id")
private Long productId;
@Schema(title = "订单编号")
private String orderSn;
@Schema(title = "会员用户名")
private String memberUsername;
@Schema(title = "退货人姓名")
private String returnName;
@Schema(title = "退货人电话")
private String returnPhone;
@Schema(title = "商品图片")
private String productPic;
@Schema(title = "商品名称")
private String productName;
@Schema(title = "商品品牌")
private String productBrand;
@Schema(title = "商品销售属性：颜色：红色；尺码：xl;")
private String productAttr;
@Schema(title = "退货数量")
private Integer productCount;
@Schema(title = "商品单价")
private BigDecimal productPrice;
@Schema(title = "商品实际支付单价")
private BigDecimal productRealPrice;
@Schema(title = "原因")
private String reason;
@Schema(title = "描述")
private String description;
@Schema(title = "凭证图片，以逗号隔开")
private String proofPics;
```

## OrderParam

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OrderParam.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/OrderParam.java:1)

```java
public class OrderParam
@Schema(title = "收货地址ID")
private Long memberReceiveAddressId;
@Schema(title = "优惠券ID")
private Long couponId;
@Schema(title = "使用的积分数")
private Integer useIntegration;
@Schema(title = "支付方式")
private Integer payType;
@Schema(title = "被选中的购物车商品ID")
private List<Long> cartIds;
```

## PmsPortalProductDetail

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PmsPortalProductDetail.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PmsPortalProductDetail.java:1)

```java
public class PmsPortalProductDetail
@Schema(title = "商品信息")
private PmsProduct product;
@Schema(title = "商品品牌")
private PmsBrand brand;
@Schema(title = "商品属性与参数")
private List<PmsProductAttribute> productAttributeList;
@Schema(title = "手动录入的商品属性与参数值")
private List<PmsProductAttributeValue> productAttributeValueList;
@Schema(title = "商品的sku库存信息")
private List<PmsSkuStock> skuStockList;
@Schema(title = "商品阶梯价格设置")
private List<PmsProductLadder> productLadderList;
@Schema(title = "商品满减价格设置")
private List<PmsProductFullReduction> productFullReductionList;
@Schema(title = "商品可用优惠券")
private List<SmsCoupon> couponList;
```

## PmsProductCategoryNode

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PmsProductCategoryNode.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PmsProductCategoryNode.java:1)

```java
public class PmsProductCategoryNode extends PmsProductCategory
@Schema(title = "子分类集合")
private List<PmsProductCategoryNode> children;
```

## PromotionProduct

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PromotionProduct.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/PromotionProduct.java:1)

```java
public class PromotionProduct extends PmsProduct
//商品库存信息
private List<PmsSkuStock> skuStockList;
//商品打折信息
private List<PmsProductLadder> productLadderList;
//商品满减信息
private List<PmsProductFullReduction> productFullReductionList;
```

## QueueEnum

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/QueueEnum.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/QueueEnum.java:1)

```java
public enum QueueEnum
private final String exchange;
private final String name;
private final String routeKey;
```

## SmsCouponHistoryDetail

[mall/mall-portal/src/main/java/com/macro/mall/portal/domain/SmsCouponHistoryDetail.java](D:/project/mall/mall-portal/src/main/java/com/macro/mall/portal/domain/SmsCouponHistoryDetail.java:1)

```java
public class SmsCouponHistoryDetail extends SmsCouponHistory
@Schema(title = "相关优惠券信息")
private SmsCoupon coupon;
@Schema(title = "优惠券关联商品")
private List<SmsCouponProductRelation> productRelationList;
@Schema(title = "优惠券关联商品分类")
private List<SmsCouponProductCategoryRelation> categoryRelationList;
```

## EsProduct

[mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProduct.java](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProduct.java:1)

```java
public class EsProduct implements Serializable
@Id
private Long id;
@Field(type = FieldType.Keyword)
private String productSn;
private Long brandId;
@Field(type = FieldType.Keyword)
private String brandName;
private Long productCategoryId;
@Field(type = FieldType.Keyword)
private String productCategoryName;
private String pic;
@Field(analyzer = "ik_max_word",type = FieldType.Text)
private String name;
@Field(analyzer = "ik_max_word",type = FieldType.Text)
private String subTitle;
@Field(analyzer = "ik_max_word",type = FieldType.Text)
private String keywords;
private BigDecimal price;
private Integer sale;
private Integer newStatus;
private Integer recommandStatus;
private Integer stock;
private Integer promotionType;
private Integer sort;
@Field(type = FieldType.Nested, fielddata = true)
private List<EsProductAttributeValue> attrValueList;
```

## EsProductAttributeValue

[mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProductAttributeValue.java](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProductAttributeValue.java:1)

```java
public class EsProductAttributeValue implements Serializable
private Long id;
private Long productAttributeId;
//属性值
@Field(type = FieldType.Keyword)
private String value;
//属性参数：0->规格；1->参数
private Integer type;
//属性名称
@Field(type=FieldType.Keyword)
private String name;
```

## EsProductRelatedInfo

[mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProductRelatedInfo.java](D:/project/mall/mall-search/src/main/java/com/macro/mall/search/domain/EsProductRelatedInfo.java:1)

```java
public class EsProductRelatedInfo
private List<String> brandNames;
private List<String> productCategoryNames;
private List<ProductAttr> productAttrs;
// 以下字段属于嵌套类型：public static class ProductAttr
private Long attrId;
private String attrName;
private List<String> attrValues;
```
