# 附录B：SQL数据库字典

【已确认事实】依据 `mall/document/sql/mall.sql` 的 CREATE TABLE 原文提取，保留字段类型、NULL、默认值、注释与索引。这里只记录仓库DDL，不代表运行数据库已逐项比对。SQL样例业务数据与账号凭据不复制。

共 76 张表。各表实体及生成Mapper位于 mall-mbg；业务使用范围见主文与附录D。

## 业务使用范围索引

【已确认事实】DDL中的表存在；下表“需求”是本次追踪到的功能簇。空缺表示未纳入已确认业务链，不能凭生成Model/Mapper认定相应产品功能已完成。

| 表 | 对应已追踪需求 |
| --- | --- |
| cms_help | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_help_category | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_member_report | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_prefrence_area | REQ-CMS-001 |
| cms_prefrence_area_product_relation | REQ-PRODUCT-005 |
| cms_subject | REQ-CMS-002、REQ-HOME-001 |
| cms_subject_category | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_subject_comment | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_subject_product_relation | REQ-PRODUCT-005 |
| cms_topic | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_topic_category | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| cms_topic_comment | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| oms_cart_item | REQ-CART-001、REQ-PORTALORDER-001 |
| oms_company_address | REQ-ORDERCFG-001、REQ-ADMINRETURN-001 |
| oms_order | REQ-ADMINORDER-001、REQ-PAY-001、REQ-PORTALORDER-001 |
| oms_order_item | REQ-ADMINORDER-001、REQ-PAY-001、REQ-PORTALORDER-001 |
| oms_order_operate_history | REQ-ADMINORDER-001 |
| oms_order_return_apply | REQ-ADMINRETURN-001、REQ-PORTALRETURN-001 |
| oms_order_return_reason | REQ-ORDERCFG-002 |
| oms_order_setting | REQ-ORDERCFG-003、REQ-PORTALORDER-001 |
| pms_album | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_album_pic | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_brand | REQ-PRODUCT-001、REQ-HOME-001、REQ-MEMBERDATA-001、REQ-BROWSE-001、REQ-BROWSE-002 |
| pms_comment | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_comment_replay | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_feight_template | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_member_price | REQ-PRODUCT-005 |
| pms_product | REQ-PRODUCT-001、REQ-PRODUCT-004、REQ-PRODUCT-005、REQ-FLASH-002、REQ-HOME-001、REQ-MEMBERDATA-002、REQ-MEMBERDATA-003、REQ-CART-001、REQ-PORTALORDER-001、REQ-BROWSE-001、REQ-BROWSE-002、REQ-COUPON-001、REQ-SEARCH-001 |
| pms_product_attribute | REQ-PRODUCT-002、REQ-PRODUCT-003、REQ-CART-001、REQ-BROWSE-002、REQ-SEARCH-001 |
| pms_product_attribute_category | REQ-PRODUCT-002、REQ-PRODUCT-003 |
| pms_product_attribute_value | REQ-PRODUCT-005、REQ-CART-001、REQ-BROWSE-002、REQ-SEARCH-001 |
| pms_product_category | REQ-PRODUCT-004、REQ-HOME-001、REQ-BROWSE-002 |
| pms_product_category_attribute_relation | REQ-PRODUCT-003、REQ-PRODUCT-004 |
| pms_product_full_reduction | REQ-PRODUCT-005、REQ-CART-001、REQ-PORTALORDER-001、REQ-BROWSE-002 |
| pms_product_ladder | REQ-PRODUCT-005、REQ-CART-001、REQ-PORTALORDER-001、REQ-BROWSE-002 |
| pms_product_operate_log | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| pms_product_vertify_record | REQ-PRODUCT-005 |
| pms_sku_stock | REQ-PRODUCT-005、REQ-PRODUCT-006、REQ-PAY-001、REQ-CART-001、REQ-PORTALORDER-001、REQ-BROWSE-002 |
| sms_coupon | REQ-MARKETING-001、REQ-PORTALORDER-001、REQ-BROWSE-002、REQ-COUPON-001 |
| sms_coupon_history | REQ-MARKETING-002、REQ-PORTALORDER-001、REQ-COUPON-001 |
| sms_coupon_product_category_relation | REQ-MARKETING-001、REQ-PORTALORDER-001、REQ-BROWSE-002、REQ-COUPON-001 |
| sms_coupon_product_relation | REQ-MARKETING-001、REQ-PORTALORDER-001、REQ-BROWSE-002、REQ-COUPON-001 |
| sms_flash_promotion | REQ-FLASH-001、REQ-HOME-001 |
| sms_flash_promotion_log | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| sms_flash_promotion_product_relation | REQ-FLASH-002、REQ-FLASH-003、REQ-HOME-001 |
| sms_flash_promotion_session | REQ-FLASH-003、REQ-HOME-001 |
| sms_home_advertise | REQ-HOMEADMIN-001、REQ-HOME-001 |
| sms_home_brand | REQ-HOMEADMIN-002、REQ-HOME-001、REQ-BROWSE-001 |
| sms_home_new_product | REQ-HOMEADMIN-003、REQ-HOME-001 |
| sms_home_recommend_product | REQ-HOMEADMIN-004、REQ-HOME-001 |
| sms_home_recommend_subject | REQ-HOMEADMIN-005、REQ-HOME-001 |
| ums_admin | REQ-ADMIN-001 |
| ums_admin_login_log | REQ-ADMIN-001 |
| ums_admin_permission_relation | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_admin_role_relation | REQ-ADMIN-001、REQ-PERMISSION-003、REQ-PERMISSION-004 |
| ums_growth_change_history | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_integration_change_history | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_integration_consume_setting | REQ-PORTALORDER-001 |
| ums_member | REQ-PORTALORDER-001、REQ-MEMBER-001 |
| ums_member_level | REQ-MEMBERLEVEL-001、REQ-MEMBER-001 |
| ums_member_login_log | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_member_tag_relation | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_product_category_relation | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_receive_address | REQ-PORTALORDER-001、REQ-ADDRESS-001 |
| ums_member_rule_setting | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_statistics_info | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_tag | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_member_task | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_menu | REQ-ADMIN-001、REQ-PERMISSION-001、REQ-PERMISSION-004 |
| ums_permission | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_resource | REQ-ADMIN-001、REQ-PERMISSION-003、REQ-PERMISSION-004 |
| ums_resource_category | REQ-PERMISSION-002 |
| ums_role | REQ-ADMIN-001、REQ-PERMISSION-004 |
| ums_role_menu_relation | REQ-ADMIN-001、REQ-PERMISSION-004 |
| ums_role_permission_relation | 当前已追踪功能中未确认；保留DDL/生成访问代码证据 |
| ums_role_resource_relation | REQ-ADMIN-001、REQ-PERMISSION-003、REQ-PERMISSION-004 |

## cms_help — 帮助表

[DDL来源](D:/project/mall/document/sql/mall.sql:24)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `category_id` | bigint(20) NULL DEFAULT NULL |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `title` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `read_count` | int(1) NULL DEFAULT NULL |
| `content` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_help_category — 帮助分类表

[DDL来源](D:/project/mall/document/sql/mall.sql:44)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分类图标' |
| `help_count` | int(11) NULL DEFAULT NULL COMMENT '专题数量' |
| `show_status` | int(2) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_member_report — 用户举报表

[DDL来源](D:/project/mall/document/sql/mall.sql:62)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NULL DEFAULT NULL |
| `report_type` | int(1) NULL DEFAULT NULL COMMENT '举报类型：0->商品评价；1->话题内容；2->用户评论' |
| `report_member_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '举报人' |
| `create_time` | datetime NULL DEFAULT NULL |
| `report_object` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `report_status` | int(1) NULL DEFAULT NULL COMMENT '举报状态：0->未处理；1->已处理' |
| `handle_status` | int(1) NULL DEFAULT NULL COMMENT '处理结果：0->无效；1->有效；2->恶意' |
| `note` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
```

## cms_prefrence_area — 优选专区

[DDL来源](D:/project/mall/document/sql/mall.sql:81)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `sub_title` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `pic` | varbinary(500) NULL DEFAULT NULL COMMENT '展示图片' |
| `sort` | int(11) NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_prefrence_area_product_relation — 优选专区和产品关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:103)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `prefrence_area_id` | bigint(20) NULL DEFAULT NULL |
| `product_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_subject — 专题表

[DDL来源](D:/project/mall/document/sql/mall.sql:126)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `category_id` | bigint(20) NULL DEFAULT NULL |
| `title` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `pic` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '专题主图' |
| `product_count` | int(11) NULL DEFAULT NULL COMMENT '关联产品数量' |
| `recommend_status` | int(1) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `collect_count` | int(11) NULL DEFAULT NULL |
| `read_count` | int(11) NULL DEFAULT NULL |
| `comment_count` | int(11) NULL DEFAULT NULL |
| `album_pics` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '画册图片用逗号分割' |
| `description` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL COMMENT '显示状态：0->不显示；1->显示' |
| `content` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL |
| `forward_count` | int(11) NULL DEFAULT NULL COMMENT '转发数' |
| `category_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '专题分类名称' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_subject_category — 专题分类表

[DDL来源](D:/project/mall/document/sql/mall.sql:160)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分类图标' |
| `subject_count` | int(11) NULL DEFAULT NULL COMMENT '专题数量' |
| `show_status` | int(2) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_subject_comment — 专题评论表

[DDL来源](D:/project/mall/document/sql/mall.sql:180)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `subject_id` | bigint(20) NULL DEFAULT NULL |
| `member_nick_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `member_icon` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `content` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_subject_product_relation — 专题商品关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:199)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `subject_id` | bigint(20) NULL DEFAULT NULL |
| `product_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_topic — 话题表

[DDL来源](D:/project/mall/document/sql/mall.sql:227)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `category_id` | bigint(20) NULL DEFAULT NULL |
| `name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `start_time` | datetime NULL DEFAULT NULL |
| `end_time` | datetime NULL DEFAULT NULL |
| `attend_count` | int(11) NULL DEFAULT NULL COMMENT '参与人数' |
| `attention_count` | int(11) NULL DEFAULT NULL COMMENT '关注人数' |
| `read_count` | int(11) NULL DEFAULT NULL |
| `award_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '奖品名称' |
| `attend_type` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '参与方式' |
| `content` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '话题内容' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_topic_category — 话题分类表

[DDL来源](D:/project/mall/document/sql/mall.sql:251)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分类图标' |
| `subject_count` | int(11) NULL DEFAULT NULL COMMENT '专题数量' |
| `show_status` | int(2) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## cms_topic_comment — 专题评论表

[DDL来源](D:/project/mall/document/sql/mall.sql:269)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_nick_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `topic_id` | bigint(20) NULL DEFAULT NULL |
| `member_icon` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `content` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_cart_item — 购物车表

[DDL来源](D:/project/mall/document/sql/mall.sql:288)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_sku_id` | bigint(20) NULL DEFAULT NULL |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `quantity` | int(11) NULL DEFAULT NULL COMMENT '购买数量' |
| `price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '添加到购物车的价格' |
| `product_pic` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品主图' |
| `product_name` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品名称' |
| `product_sub_title` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品副标题（卖点）' |
| `product_sku_code` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品sku条码' |
| `member_nickname` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '会员昵称' |
| `create_date` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `modify_date` | datetime NULL DEFAULT NULL COMMENT '修改时间' |
| `delete_status` | int(1) NULL DEFAULT 0 COMMENT '是否删除' |
| `product_category_id` | bigint(20) NULL DEFAULT NULL COMMENT '商品分类' |
| `product_brand` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_sn` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_attr` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品销售属性:[{\"key\":\"颜色\",\"value\":\"颜色\"},{\"key\":\"容量\",\"value\":\"4G\"}]' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_company_address — 公司收发货地址表

[DDL来源](D:/project/mall/document/sql/mall.sql:419)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `address_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '地址名称' |
| `send_status` | int(1) NULL DEFAULT NULL COMMENT '默认发货地址：0->否；1->是' |
| `receive_status` | int(1) NULL DEFAULT NULL COMMENT '是否默认收货地址：0->否；1->是' |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收发货人姓名' |
| `phone` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收货人电话' |
| `province` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省/直辖市' |
| `city` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '市' |
| `region` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '区' |
| `detail_address` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详细地址' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order — 订单表

[DDL来源](D:/project/mall/document/sql/mall.sql:444)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT COMMENT '订单id' |
| `member_id` | bigint(20) NOT NULL |
| `coupon_id` | bigint(20) NULL DEFAULT NULL |
| `order_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '订单编号' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '提交时间' |
| `member_username` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户帐号' |
| `total_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '订单总金额' |
| `pay_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '应付金额（实际支付金额）' |
| `freight_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '运费金额' |
| `promotion_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '促销优化金额（促销价、满减、阶梯价）' |
| `integration_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '积分抵扣金额' |
| `coupon_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '优惠券抵扣金额' |
| `discount_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '管理员后台调整订单使用的折扣金额' |
| `pay_type` | int(1) NULL DEFAULT NULL COMMENT '支付方式：0->未支付；1->支付宝；2->微信' |
| `source_type` | int(1) NULL DEFAULT NULL COMMENT '订单来源：0->PC订单；1->app订单' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单' |
| `order_type` | int(1) NULL DEFAULT NULL COMMENT '订单类型：0->正常订单；1->秒杀订单' |
| `delivery_company` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '物流公司(配送方式)' |
| `delivery_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '物流单号' |
| `auto_confirm_day` | int(11) NULL DEFAULT NULL COMMENT '自动确认时间（天）' |
| `integration` | int(11) NULL DEFAULT NULL COMMENT '可以获得的积分' |
| `growth` | int(11) NULL DEFAULT NULL COMMENT '可以活动的成长值' |
| `promotion_info` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '活动信息' |
| `bill_type` | int(1) NULL DEFAULT NULL COMMENT '发票类型：0->不开发票；1->电子发票；2->纸质发票' |
| `bill_header` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '发票抬头' |
| `bill_content` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '发票内容' |
| `bill_receiver_phone` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收票人电话' |
| `bill_receiver_email` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收票人邮箱' |
| `receiver_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '收货人姓名' |
| `receiver_phone` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '收货人电话' |
| `receiver_post_code` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收货人邮编' |
| `receiver_province` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省份/直辖市' |
| `receiver_city` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '城市' |
| `receiver_region` | varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '区' |
| `receiver_detail_address` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详细地址' |
| `note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '订单备注' |
| `confirm_status` | int(1) NULL DEFAULT NULL COMMENT '确认收货状态：0->未确认；1->已确认' |
| `delete_status` | int(1) NOT NULL DEFAULT 0 COMMENT '删除状态：0->未删除；1->已删除' |
| `use_integration` | int(11) NULL DEFAULT NULL COMMENT '下单时使用的积分' |
| `payment_time` | datetime NULL DEFAULT NULL COMMENT '支付时间' |
| `delivery_time` | datetime NULL DEFAULT NULL COMMENT '发货时间' |
| `receive_time` | datetime NULL DEFAULT NULL COMMENT '确认收货时间' |
| `comment_time` | datetime NULL DEFAULT NULL COMMENT '评价时间' |
| `modify_time` | datetime NULL DEFAULT NULL COMMENT '修改时间' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order_item — 订单中所包含的商品

[DDL来源](D:/project/mall/document/sql/mall.sql:565)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `order_id` | bigint(20) NULL DEFAULT NULL COMMENT '订单id' |
| `order_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '订单编号' |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_pic` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_brand` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '销售价格' |
| `product_quantity` | int(11) NULL DEFAULT NULL COMMENT '购买数量' |
| `product_sku_id` | bigint(20) NULL DEFAULT NULL COMMENT '商品sku编号' |
| `product_sku_code` | varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品sku条码' |
| `product_category_id` | bigint(20) NULL DEFAULT NULL COMMENT '商品分类id' |
| `promotion_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品促销名称' |
| `promotion_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '商品促销分解金额' |
| `coupon_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '优惠券优惠分解金额' |
| `integration_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '积分优惠分解金额' |
| `real_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '该商品经过优惠后的分解金额' |
| `gift_integration` | int(11) NULL DEFAULT 0 |
| `gift_growth` | int(11) NULL DEFAULT 0 |
| `product_attr` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品销售属性:[{\"key\":\"颜色\",\"value\":\"颜色\"},{\"key\":\"容量\",\"value\":\"4G\"}]' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order_operate_history — 订单操作历史记录

[DDL来源](D:/project/mall/document/sql/mall.sql:692)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `order_id` | bigint(20) NULL DEFAULT NULL COMMENT '订单id' |
| `operate_man` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人：用户；系统；后台管理员' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '操作时间' |
| `order_status` | int(1) NULL DEFAULT NULL COMMENT '订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单' |
| `note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order_return_apply — 订单退货申请

[DDL来源](D:/project/mall/document/sql/mall.sql:749)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `order_id` | bigint(20) NULL DEFAULT NULL COMMENT '订单id' |
| `company_address_id` | bigint(20) NULL DEFAULT NULL COMMENT '收货地址表id' |
| `product_id` | bigint(20) NULL DEFAULT NULL COMMENT '退货商品id' |
| `order_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '订单编号' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '申请时间' |
| `member_username` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '会员用户名' |
| `return_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '退款金额' |
| `return_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '退货人姓名' |
| `return_phone` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '退货人电话' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '申请状态：0->待处理；1->退货中；2->已完成；3->已拒绝' |
| `handle_time` | datetime NULL DEFAULT NULL COMMENT '处理时间' |
| `product_pic` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品图片' |
| `product_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品名称' |
| `product_brand` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品品牌' |
| `product_attr` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品销售属性：颜色：红色；尺码：xl;' |
| `product_count` | int(11) NULL DEFAULT NULL COMMENT '退货数量' |
| `product_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '商品单价' |
| `product_real_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '商品实际支付单价' |
| `reason` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '原因' |
| `description` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述' |
| `proof_pics` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '凭证图片，以逗号隔开' |
| `handle_note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理备注' |
| `handle_man` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理人员' |
| `receive_man` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收货人' |
| `receive_time` | datetime NULL DEFAULT NULL COMMENT '收货时间' |
| `receive_note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收货备注' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order_return_reason — 退货原因表

[DDL来源](D:/project/mall/document/sql/mall.sql:809)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '退货类型' |
| `sort` | int(11) NULL DEFAULT NULL |
| `status` | int(1) NULL DEFAULT NULL COMMENT '状态：0->不启用；1->启用' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '添加时间' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## oms_order_setting — 订单设置表

[DDL来源](D:/project/mall/document/sql/mall.sql:835)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `flash_order_overtime` | int(11) NULL DEFAULT NULL COMMENT '秒杀订单超时关闭时间(分)' |
| `normal_order_overtime` | int(11) NULL DEFAULT NULL COMMENT '正常订单超时时间(分)' |
| `confirm_overtime` | int(11) NULL DEFAULT NULL COMMENT '发货后自动确认收货时间（天）' |
| `finish_overtime` | int(11) NULL DEFAULT NULL COMMENT '自动完成交易时间，不能申请售后（天）' |
| `comment_overtime` | int(11) NULL DEFAULT NULL COMMENT '订单完成后自动好评时间（天）' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_album — 相册表

[DDL来源](D:/project/mall/document/sql/mall.sql:854)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `cover_pic` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `pic_count` | int(11) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |
| `description` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_album_pic — 画册图片表

[DDL来源](D:/project/mall/document/sql/mall.sql:872)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `album_id` | bigint(20) NULL DEFAULT NULL |
| `pic` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_brand — 品牌表

[DDL来源](D:/project/mall/document/sql/mall.sql:887)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `first_letter` | varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '首字母' |
| `sort` | int(11) NULL DEFAULT NULL |
| `factory_status` | int(1) NULL DEFAULT NULL COMMENT '是否为品牌制造商：0->不是；1->是' |
| `show_status` | int(1) NULL DEFAULT NULL |
| `product_count` | int(11) NULL DEFAULT NULL COMMENT '产品数量' |
| `product_comment_count` | int(11) NULL DEFAULT NULL COMMENT '产品评论数量' |
| `logo` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '品牌logo' |
| `big_pic` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '专区大图' |
| `brand_story` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '品牌故事' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_comment — 商品评价表

[DDL来源](D:/project/mall/document/sql/mall.sql:922)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `member_nick_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `star` | int(3) NULL DEFAULT NULL COMMENT '评价星数：0->5' |
| `member_ip` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '评价的ip' |
| `create_time` | datetime NULL DEFAULT NULL |
| `show_status` | int(1) NULL DEFAULT NULL |
| `product_attribute` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '购买时的商品属性' |
| `collect_couont` | int(11) NULL DEFAULT NULL |
| `read_count` | int(11) NULL DEFAULT NULL |
| `content` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL |
| `pics` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '上传图片地址，以逗号隔开' |
| `member_icon` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '评论用户头像' |
| `replay_count` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_comment_replay — 产品评价回复表

[DDL来源](D:/project/mall/document/sql/mall.sql:949)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `comment_id` | bigint(20) NULL DEFAULT NULL |
| `member_nick_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `member_icon` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `content` | varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `type` | int(1) NULL DEFAULT NULL COMMENT '评论人员类型；0->会员；1->管理员' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_feight_template — 运费模版

[DDL来源](D:/project/mall/document/sql/mall.sql:968)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `charge_type` | int(1) NULL DEFAULT NULL COMMENT '计费类型:0->按重量；1->按件数' |
| `first_weight` | decimal(10, 2) NULL DEFAULT NULL COMMENT '首重kg' |
| `first_fee` | decimal(10, 2) NULL DEFAULT NULL COMMENT '首费（元）' |
| `continue_weight` | decimal(10, 2) NULL DEFAULT NULL |
| `continme_fee` | decimal(10, 2) NULL DEFAULT NULL |
| `dest` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '目的地（省、市）' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_member_price — 商品会员价格表

[DDL来源](D:/project/mall/document/sql/mall.sql:988)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `member_level_id` | bigint(20) NULL DEFAULT NULL |
| `member_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '会员价格' |
| `member_level_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product — 商品信息

[DDL来源](D:/project/mall/document/sql/mall.sql:1085)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `brand_id` | bigint(20) NULL DEFAULT NULL |
| `product_category_id` | bigint(20) NULL DEFAULT NULL |
| `feight_template_id` | bigint(20) NULL DEFAULT NULL |
| `product_attribute_category_id` | bigint(20) NULL DEFAULT NULL |
| `name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL |
| `pic` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_sn` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '货号' |
| `delete_status` | int(1) NULL DEFAULT NULL COMMENT '删除状态：0->未删除；1->已删除' |
| `publish_status` | int(1) NULL DEFAULT NULL COMMENT '上架状态：0->下架；1->上架' |
| `new_status` | int(1) NULL DEFAULT NULL COMMENT '新品状态:0->不是新品；1->新品' |
| `recommand_status` | int(1) NULL DEFAULT NULL COMMENT '推荐状态；0->不推荐；1->推荐' |
| `verify_status` | int(1) NULL DEFAULT NULL COMMENT '审核状态：0->未审核；1->审核通过' |
| `sort` | int(11) NULL DEFAULT NULL COMMENT '排序' |
| `sale` | int(11) NULL DEFAULT NULL COMMENT '销量' |
| `price` | decimal(10, 2) NULL DEFAULT NULL |
| `promotion_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '促销价格' |
| `gift_growth` | int(11) NULL DEFAULT 0 COMMENT '赠送的成长值' |
| `gift_point` | int(11) NULL DEFAULT 0 COMMENT '赠送的积分' |
| `use_point_limit` | int(11) NULL DEFAULT NULL COMMENT '限制使用的积分数' |
| `sub_title` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '副标题' |
| `description` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '商品描述' |
| `original_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '市场价' |
| `stock` | int(11) NULL DEFAULT NULL COMMENT '库存' |
| `low_stock` | int(11) NULL DEFAULT NULL COMMENT '库存预警值' |
| `unit` | varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '单位' |
| `weight` | decimal(10, 2) NULL DEFAULT NULL COMMENT '商品重量，默认为克' |
| `preview_status` | int(1) NULL DEFAULT NULL COMMENT '是否为预告商品：0->不是；1->是' |
| `service_ids` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮' |
| `keywords` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `note` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `album_pics` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '画册图片，连产品图片限制为5张，以逗号分割' |
| `detail_title` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `detail_desc` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL |
| `detail_html` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '产品详情网页内容' |
| `detail_mobile_html` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '移动端网页详情' |
| `promotion_start_time` | datetime NULL DEFAULT NULL COMMENT '促销开始时间' |
| `promotion_end_time` | datetime NULL DEFAULT NULL COMMENT '促销结束时间' |
| `promotion_per_limit` | int(11) NULL DEFAULT NULL COMMENT '活动限购数量' |
| `promotion_type` | int(1) NULL DEFAULT NULL COMMENT '促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购' |
| `brand_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '品牌名称' |
| `product_category_name` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品分类名称' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_attribute — 商品属性参数表

[DDL来源](D:/project/mall/document/sql/mall.sql:1177)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_attribute_category_id` | bigint(20) NULL DEFAULT NULL |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `select_type` | int(1) NULL DEFAULT NULL COMMENT '属性选择类型：0->唯一；1->单选；2->多选' |
| `input_type` | int(1) NULL DEFAULT NULL COMMENT '属性录入方式：0->手工录入；1->从列表中选取' |
| `input_list` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '可选值列表，以逗号隔开' |
| `sort` | int(11) NULL DEFAULT NULL COMMENT '排序字段：最高的可以单独上传图片' |
| `filter_type` | int(1) NULL DEFAULT NULL COMMENT '分类筛选样式：1->普通；1->颜色' |
| `search_type` | int(1) NULL DEFAULT NULL COMMENT '检索类型；0->不需要进行检索；1->关键字检索；2->范围检索' |
| `related_status` | int(1) NULL DEFAULT NULL COMMENT '相同属性产品是否关联；0->不关联；1->关联' |
| `hand_add_status` | int(1) NULL DEFAULT NULL COMMENT '是否支持手动新增；0->不支持；1->支持' |
| `type` | int(1) NULL DEFAULT NULL COMMENT '属性的类型；0->规格；1->参数' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_attribute_category — 产品属性分类表

[DDL来源](D:/project/mall/document/sql/mall.sql:1254)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `attribute_count` | int(11) NULL DEFAULT 0 COMMENT '属性数量' |
| `param_count` | int(11) NULL DEFAULT 0 COMMENT '参数数量' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_attribute_value — 存储产品参数信息的表

[DDL来源](D:/project/mall/document/sql/mall.sql:1282)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_attribute_id` | bigint(20) NULL DEFAULT NULL |
| `value` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手动添加规格或参数的值，参数单值，规格有多个时以逗号隔开' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_category — 产品分类

[DDL来源](D:/project/mall/document/sql/mall.sql:1428)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `parent_id` | bigint(20) NULL DEFAULT NULL COMMENT '上机分类的编号：0表示一级分类' |
| `name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `level` | int(1) NULL DEFAULT NULL COMMENT '分类级别：0->1级；1->2级' |
| `product_count` | int(11) NULL DEFAULT NULL |
| `product_unit` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `nav_status` | int(1) NULL DEFAULT NULL COMMENT '是否显示在导航栏：0->不显示；1->显示' |
| `show_status` | int(1) NULL DEFAULT NULL COMMENT '显示状态：0->不显示；1->显示' |
| `sort` | int(11) NULL DEFAULT NULL |
| `icon` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '图标' |
| `keywords` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `description` | text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '描述' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_category_attribute_relation — 产品的分类和属性的关系表，用于设置分类筛选条件（只支持一级分类）

[DDL来源](D:/project/mall/document/sql/mall.sql:1492)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_category_id` | bigint(20) NULL DEFAULT NULL |
| `product_attribute_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_full_reduction — 产品满减表(只针对同商品)

[DDL来源](D:/project/mall/document/sql/mall.sql:1512)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(11) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `full_price` | decimal(10, 2) NULL DEFAULT NULL |
| `reduce_price` | decimal(10, 2) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_ladder — 产品阶梯价格表(只针对同商品)

[DDL来源](D:/project/mall/document/sql/mall.sql:1564)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `count` | int(11) NULL DEFAULT NULL COMMENT '满足的商品数量' |
| `discount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '折扣' |
| `price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '折后价格' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_operate_log — 

[DDL来源](D:/project/mall/document/sql/mall.sql:1616)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `price_old` | decimal(10, 2) NULL DEFAULT NULL |
| `price_new` | decimal(10, 2) NULL DEFAULT NULL |
| `sale_price_old` | decimal(10, 2) NULL DEFAULT NULL |
| `sale_price_new` | decimal(10, 2) NULL DEFAULT NULL |
| `gift_point_old` | int(11) NULL DEFAULT NULL COMMENT '赠送的积分' |
| `gift_point_new` | int(11) NULL DEFAULT NULL |
| `use_point_limit_old` | int(11) NULL DEFAULT NULL |
| `use_point_limit_new` | int(11) NULL DEFAULT NULL |
| `operate_man` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人' |
| `create_time` | datetime NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_product_vertify_record — 商品审核记录

[DDL来源](D:/project/mall/document/sql/mall.sql:1640)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `vertify_man` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '审核人' |
| `status` | int(1) NULL DEFAULT NULL |
| `detail` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '反馈详情' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## pms_sku_stock — sku的库存

[DDL来源](D:/project/mall/document/sql/mall.sql:1660)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `sku_code` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'sku编码' |
| `price` | decimal(10, 2) NULL DEFAULT NULL |
| `stock` | int(11) NULL DEFAULT 0 COMMENT '库存' |
| `low_stock` | int(11) NULL DEFAULT NULL COMMENT '预警库存' |
| `pic` | varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '展示图片' |
| `sale` | int(11) NULL DEFAULT NULL COMMENT '销量' |
| `promotion_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '单品促销价格' |
| `lock_stock` | int(11) NULL DEFAULT 0 COMMENT '锁定库存' |
| `sp_data` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品销售属性，json格式' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_coupon — 优惠券表

[DDL来源](D:/project/mall/document/sql/mall.sql:1779)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `type` | int(1) NULL DEFAULT NULL COMMENT '优惠券类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券' |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `platform` | int(1) NULL DEFAULT NULL COMMENT '使用平台：0->全部；1->移动；2->PC' |
| `count` | int(11) NULL DEFAULT NULL COMMENT '数量' |
| `amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '金额' |
| `per_limit` | int(11) NULL DEFAULT NULL COMMENT '每人限领张数' |
| `min_point` | decimal(10, 2) NULL DEFAULT NULL COMMENT '使用门槛；0表示无门槛' |
| `start_time` | datetime NULL DEFAULT NULL |
| `end_time` | datetime NULL DEFAULT NULL |
| `use_type` | int(1) NULL DEFAULT NULL COMMENT '使用类型：0->全场通用；1->指定分类；2->指定商品' |
| `note` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注' |
| `publish_count` | int(11) NULL DEFAULT NULL COMMENT '发行数量' |
| `use_count` | int(11) NULL DEFAULT NULL COMMENT '已使用数量' |
| `receive_count` | int(11) NULL DEFAULT NULL COMMENT '领取数量' |
| `enable_time` | datetime NULL DEFAULT NULL COMMENT '可以领取的日期' |
| `code` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '优惠码' |
| `member_level` | int(1) NULL DEFAULT NULL COMMENT '可领取的会员类型：0->无限时' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_coupon_history — 优惠券使用、领取历史表

[DDL来源](D:/project/mall/document/sql/mall.sql:1814)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `coupon_id` | bigint(20) NULL DEFAULT NULL |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `coupon_code` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `member_nickname` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '领取人昵称' |
| `get_type` | int(1) NULL DEFAULT NULL COMMENT '获取类型：0->后台赠送；1->主动获取' |
| `create_time` | datetime NULL DEFAULT NULL |
| `use_status` | int(1) NULL DEFAULT NULL COMMENT '使用状态：0->未使用；1->已使用；2->已过期' |
| `use_time` | datetime NULL DEFAULT NULL COMMENT '使用时间' |
| `order_id` | bigint(20) NULL DEFAULT NULL COMMENT '订单编号' |
| `order_sn` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '订单号码' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
INDEX `idx_member_id`(`member_id`) USING BTREE
INDEX `idx_coupon_id`(`coupon_id`) USING BTREE
```

## sms_coupon_product_category_relation — 优惠券和产品分类关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:1855)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `coupon_id` | bigint(20) NULL DEFAULT NULL |
| `product_category_id` | bigint(20) NULL DEFAULT NULL |
| `product_category_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '产品分类名称' |
| `parent_category_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '父分类名称' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_coupon_product_relation — 优惠券和产品的关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:1873)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `coupon_id` | bigint(20) NULL DEFAULT NULL |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_name` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品名称' |
| `product_sn` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品编码' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_flash_promotion — 限时购表

[DDL来源](D:/project/mall/document/sql/mall.sql:1894)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `title` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '秒杀时间段名称' |
| `start_date` | date NULL DEFAULT NULL COMMENT '开始日期' |
| `end_date` | date NULL DEFAULT NULL COMMENT '结束日期' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '上下线状态' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_flash_promotion_log — 限时购通知记录

[DDL来源](D:/project/mall/document/sql/mall.sql:1913)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | int(11) NOT NULL AUTO_INCREMENT |
| `member_id` | int(11) NULL DEFAULT NULL |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `member_phone` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `product_name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `subscribe_time` | datetime NULL DEFAULT NULL COMMENT '会员订阅时间' |
| `send_time` | datetime NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_flash_promotion_product_relation — 商品限时购与商品关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:1932)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号' |
| `flash_promotion_id` | bigint(20) NULL DEFAULT NULL |
| `flash_promotion_session_id` | bigint(20) NULL DEFAULT NULL COMMENT '编号' |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `flash_promotion_price` | decimal(10, 2) NULL DEFAULT NULL COMMENT '限时购价格' |
| `flash_promotion_count` | int(11) NULL DEFAULT NULL COMMENT '限时购数量' |
| `flash_promotion_limit` | int(11) NULL DEFAULT NULL COMMENT '每人限购数量' |
| `sort` | int(11) NULL DEFAULT NULL COMMENT '排序' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_flash_promotion_session — 限时购场次表

[DDL来源](D:/project/mall/document/sql/mall.sql:1999)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号' |
| `name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '场次名称' |
| `start_time` | time NULL DEFAULT NULL COMMENT '每日开始时间' |
| `end_time` | time NULL DEFAULT NULL COMMENT '每日结束时间' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '启用状态：0->不启用；1->启用' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_home_advertise — 首页轮播广告表

[DDL来源](D:/project/mall/document/sql/mall.sql:2024)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `type` | int(1) NULL DEFAULT NULL COMMENT '轮播位置：0->PC首页轮播；1->app首页轮播' |
| `pic` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `start_time` | datetime NULL DEFAULT NULL |
| `end_time` | datetime NULL DEFAULT NULL |
| `status` | int(1) NULL DEFAULT NULL COMMENT '上下线状态：0->下线；1->上线' |
| `click_count` | int(11) NULL DEFAULT NULL COMMENT '点击数' |
| `order_count` | int(11) NULL DEFAULT NULL COMMENT '下单数' |
| `url` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '链接地址' |
| `note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注' |
| `sort` | int(11) NULL DEFAULT 0 COMMENT '排序' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_home_brand — 首页推荐品牌表

[DDL来源](D:/project/mall/document/sql/mall.sql:2059)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `brand_id` | bigint(20) NULL DEFAULT NULL |
| `brand_name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `recommend_status` | int(1) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_home_new_product — 新鲜好物表

[DDL来源](D:/project/mall/document/sql/mall.sql:2085)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_name` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `recommend_status` | int(1) NULL DEFAULT NULL |
| `sort` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_home_recommend_product — 人气推荐商品表

[DDL来源](D:/project/mall/document/sql/mall.sql:2111)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `product_id` | bigint(20) NULL DEFAULT NULL |
| `product_name` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `recommend_status` | int(1) NULL DEFAULT NULL |
| `sort` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## sms_home_recommend_subject — 首页推荐专题表

[DDL来源](D:/project/mall/document/sql/mall.sql:2133)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `subject_id` | bigint(20) NULL DEFAULT NULL |
| `subject_name` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `recommend_status` | int(1) NULL DEFAULT NULL |
| `sort` | int(11) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_admin — 后台用户表

[DDL来源](D:/project/mall/document/sql/mall.sql:2156)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `username` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `password` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像' |
| `email` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱' |
| `nick_name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称' |
| `note` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注信息' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `login_time` | datetime NULL DEFAULT NULL COMMENT '最后登录时间' |
| `status` | int(1) NULL DEFAULT 1 COMMENT '帐号启用状态：0->禁用；1->启用' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_admin_login_log — 后台用户登录日志表

[DDL来源](D:/project/mall/document/sql/mall.sql:2186)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `admin_id` | bigint(20) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `ip` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `address` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `user_agent` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '浏览器登录类型' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_admin_permission_relation — 后台用户和权限关系表(除角色中定义的权限以外的加减权限)

[DDL来源](D:/project/mall/document/sql/mall.sql:2616)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `admin_id` | bigint(20) NULL DEFAULT NULL |
| `permission_id` | bigint(20) NULL DEFAULT NULL |
| `type` | int(1) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_admin_role_relation — 后台用户和角色关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:2632)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `admin_id` | bigint(20) NULL DEFAULT NULL |
| `role_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_growth_change_history — 成长值变化历史记录表

[DDL来源](D:/project/mall/document/sql/mall.sql:2653)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `change_type` | int(1) NULL DEFAULT NULL COMMENT '改变类型：0->增加；1->减少' |
| `change_count` | int(11) NULL DEFAULT NULL COMMENT '积分改变数量' |
| `operate_man` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人员' |
| `operate_note` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作备注' |
| `source_type` | int(1) NULL DEFAULT NULL COMMENT '积分来源：0->购物；1->管理员修改' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_integration_change_history — 积分变化历史记录表

[DDL来源](D:/project/mall/document/sql/mall.sql:2674)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `change_type` | int(1) NULL DEFAULT NULL COMMENT '改变类型：0->增加；1->减少' |
| `change_count` | int(11) NULL DEFAULT NULL COMMENT '积分改变数量' |
| `operate_man` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人员' |
| `operate_note` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作备注' |
| `source_type` | int(1) NULL DEFAULT NULL COMMENT '积分来源：0->购物；1->管理员修改' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_integration_consume_setting — 积分消费设置

[DDL来源](D:/project/mall/document/sql/mall.sql:2694)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `deduction_per_amount` | int(11) NULL DEFAULT NULL COMMENT '每一元需要抵扣的积分数量' |
| `max_percent_per_order` | int(11) NULL DEFAULT NULL COMMENT '每笔订单最高抵用百分比' |
| `use_unit` | int(11) NULL DEFAULT NULL COMMENT '每次使用积分最小单位100' |
| `coupon_status` | int(1) NULL DEFAULT NULL COMMENT '是否可以和优惠券同用；0->不可以；1->可以' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member — 会员表

[DDL来源](D:/project/mall/document/sql/mall.sql:2712)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_level_id` | bigint(20) NULL DEFAULT NULL |
| `username` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名' |
| `password` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码' |
| `nickname` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称' |
| `phone` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机号码' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '帐号启用状态:0->禁用；1->启用' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '注册时间' |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像' |
| `gender` | int(1) NULL DEFAULT NULL COMMENT '性别：0->未知；1->男；2->女' |
| `birthday` | date NULL DEFAULT NULL COMMENT '生日' |
| `city` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所做城市' |
| `job` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '职业' |
| `personalized_signature` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '个性签名' |
| `source_type` | int(1) NULL DEFAULT NULL COMMENT '用户来源' |
| `integration` | int(11) NULL DEFAULT NULL COMMENT '积分' |
| `growth` | int(11) NULL DEFAULT NULL COMMENT '成长值' |
| `luckey_count` | int(11) NULL DEFAULT NULL COMMENT '剩余抽奖次数' |
| `history_integration` | int(11) NULL DEFAULT NULL COMMENT '历史积分数量' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
UNIQUE INDEX `idx_username`(`username`) USING BTREE
UNIQUE INDEX `idx_phone`(`phone`) USING BTREE
```

## ums_member_level — 会员等级表

[DDL来源](D:/project/mall/document/sql/mall.sql:2755)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `growth_point` | int(11) NULL DEFAULT NULL |
| `default_status` | int(1) NULL DEFAULT NULL COMMENT '是否为默认等级：0->不是；1->是' |
| `free_freight_point` | decimal(10, 2) NULL DEFAULT NULL COMMENT '免运费标准' |
| `comment_growth_point` | int(11) NULL DEFAULT NULL COMMENT '每次评价获取的成长值' |
| `priviledge_free_freight` | int(1) NULL DEFAULT NULL COMMENT '是否有免邮特权' |
| `priviledge_sign_in` | int(1) NULL DEFAULT NULL COMMENT '是否有签到特权' |
| `priviledge_comment` | int(1) NULL DEFAULT NULL COMMENT '是否有评论获奖励特权' |
| `priviledge_promotion` | int(1) NULL DEFAULT NULL COMMENT '是否有专享活动特权' |
| `priviledge_member_price` | int(1) NULL DEFAULT NULL COMMENT '是否有会员价格特权' |
| `priviledge_birthday` | int(1) NULL DEFAULT NULL COMMENT '是否有生日特权' |
| `note` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_login_log — 会员登录记录

[DDL来源](D:/project/mall/document/sql/mall.sql:2784)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `create_time` | datetime NULL DEFAULT NULL |
| `ip` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `city` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `login_type` | int(1) NULL DEFAULT NULL COMMENT '登录类型：0->PC；1->android;2->ios;3->小程序' |
| `province` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_member_tag_relation — 用户和标签关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:2803)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `tag_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_product_category_relation — 会员与产品分类关系表（用户喜欢的分类）

[DDL来源](D:/project/mall/document/sql/mall.sql:2818)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `product_category_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_receive_address — 会员收货地址表

[DDL来源](D:/project/mall/document/sql/mall.sql:2833)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '收货人名称' |
| `phone_number` | varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `default_status` | int(1) NULL DEFAULT NULL COMMENT '是否为默认' |
| `post_code` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮政编码' |
| `province` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省份/直辖市' |
| `city` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '城市' |
| `region` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '区' |
| `detail_address` | varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详细地址(街道)' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_rule_setting — 会员积分成长规则表

[DDL来源](D:/project/mall/document/sql/mall.sql:2860)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `continue_sign_day` | int(11) NULL DEFAULT NULL COMMENT '连续签到天数' |
| `continue_sign_point` | int(11) NULL DEFAULT NULL COMMENT '连续签到赠送数量' |
| `consume_per_point` | decimal(10, 2) NULL DEFAULT NULL COMMENT '每消费多少元获取1个点' |
| `low_order_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '最低获取点数的订单金额' |
| `max_point_per_order` | int(11) NULL DEFAULT NULL COMMENT '每笔订单最高获取点数' |
| `type` | int(1) NULL DEFAULT NULL COMMENT '类型：0->积分规则；1->成长值规则' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_statistics_info — 会员统计信息

[DDL来源](D:/project/mall/document/sql/mall.sql:2879)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `member_id` | bigint(20) NULL DEFAULT NULL |
| `consume_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '累计消费金额' |
| `order_count` | int(11) NULL DEFAULT NULL COMMENT '订单数量' |
| `coupon_count` | int(11) NULL DEFAULT NULL COMMENT '优惠券数量' |
| `comment_count` | int(11) NULL DEFAULT NULL COMMENT '评价数' |
| `return_order_count` | int(11) NULL DEFAULT NULL COMMENT '退货数量' |
| `login_count` | int(11) NULL DEFAULT NULL COMMENT '登录次数' |
| `attend_count` | int(11) NULL DEFAULT NULL COMMENT '关注数量' |
| `fans_count` | int(11) NULL DEFAULT NULL COMMENT '粉丝数量' |
| `collect_product_count` | int(11) NULL DEFAULT NULL |
| `collect_subject_count` | int(11) NULL DEFAULT NULL |
| `collect_topic_count` | int(11) NULL DEFAULT NULL |
| `collect_comment_count` | int(11) NULL DEFAULT NULL |
| `invite_friend_count` | int(11) NULL DEFAULT NULL |
| `recent_order_time` | datetime NULL DEFAULT NULL COMMENT '最后一次下订单时间' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_tag — 用户标签表

[DDL来源](D:/project/mall/document/sql/mall.sql:2907)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `finish_order_count` | int(11) NULL DEFAULT NULL COMMENT '自动打标签完成订单数量' |
| `finish_order_amount` | decimal(10, 2) NULL DEFAULT NULL COMMENT '自动打标签完成订单金额' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_member_task — 会员任务表

[DDL来源](D:/project/mall/document/sql/mall.sql:2923)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL |
| `growth` | int(11) NULL DEFAULT NULL COMMENT '赠送成长值' |
| `intergration` | int(11) NULL DEFAULT NULL COMMENT '赠送积分' |
| `type` | int(1) NULL DEFAULT NULL COMMENT '任务类型：0->新手任务；1->日常任务' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_menu — 后台菜单表

[DDL来源](D:/project/mall/document/sql/mall.sql:2940)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `parent_id` | bigint(20) NULL DEFAULT NULL COMMENT '父级ID' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `title` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '菜单名称' |
| `level` | int(4) NULL DEFAULT NULL COMMENT '菜单级数' |
| `sort` | int(4) NULL DEFAULT NULL COMMENT '菜单排序' |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '前端名称' |
| `icon` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '前端图标' |
| `hidden` | int(1) NULL DEFAULT NULL COMMENT '前端隐藏' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_permission — 后台用户权限表

[DDL来源](D:/project/mall/document/sql/mall.sql:2985)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `pid` | bigint(20) NULL DEFAULT NULL COMMENT '父级权限id' |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称' |
| `value` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '权限值' |
| `icon` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '图标' |
| `type` | int(1) NULL DEFAULT NULL COMMENT '权限类型：0->目录；1->菜单；2->按钮（接口绑定权限）' |
| `uri` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '前端资源路径' |
| `status` | int(1) NULL DEFAULT NULL COMMENT '启用状态；0->禁用；1->启用' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `sort` | int(11) NULL DEFAULT NULL COMMENT '排序' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_resource — 后台资源表

[DDL来源](D:/project/mall/document/sql/mall.sql:3025)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '资源名称' |
| `url` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '资源URL' |
| `description` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述' |
| `category_id` | bigint(20) NULL DEFAULT NULL COMMENT '资源分类ID' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_resource_category — 资源分类表

[DDL来源](D:/project/mall/document/sql/mall.sql:3074)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `name` | varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分类名称' |
| `sort` | int(4) NULL DEFAULT NULL COMMENT '排序' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_role — 后台用户角色表

[DDL来源](D:/project/mall/document/sql/mall.sql:3096)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `name` | varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称' |
| `description` | varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述' |
| `admin_count` | int(11) NULL DEFAULT NULL COMMENT '后台用户数量' |
| `create_time` | datetime NULL DEFAULT NULL COMMENT '创建时间' |
| `status` | int(1) NULL DEFAULT 1 COMMENT '启用状态：0->禁用；1->启用' |
| `sort` | int(11) NULL DEFAULT 0 |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_role_menu_relation — 后台角色菜单关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:3118)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `role_id` | bigint(20) NULL DEFAULT NULL COMMENT '角色ID' |
| `menu_id` | bigint(20) NULL DEFAULT NULL COMMENT '菜单ID' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_role_permission_relation — 后台用户角色和权限关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:3168)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `role_id` | bigint(20) NULL DEFAULT NULL |
| `permission_id` | bigint(20) NULL DEFAULT NULL |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```

## ums_role_resource_relation — 后台角色资源关系表

[DDL来源](D:/project/mall/document/sql/mall.sql:3200)

| 字段 | 类型、约束与原始注释 |
| --- | --- |
| `id` | bigint(20) NOT NULL AUTO_INCREMENT |
| `role_id` | bigint(20) NULL DEFAULT NULL COMMENT '角色ID' |
| `resource_id` | bigint(20) NULL DEFAULT NULL COMMENT '资源ID' |

索引 / 约束：
```sql
PRIMARY KEY (`id`) USING BTREE
```
