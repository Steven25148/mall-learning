# Mall 数据库优化实践

目标：完成一次可以展示证据的数据库优化闭环，而不修改 `pms_product` 的业务数据。

配套文件：

- `01-setup.sql`：建立 10 万行隔离练习表，只建立主键索引。
- `02-index-labs.sql`：EXPLAIN、联合索引、最左前缀、回表、排序和分页练习。
- `03-transaction-labs.sql`：事务原子性和隔离级别双会话练习。
- `04-record-template.md`：保存优化前后证据，最终形成可用于面试的案例。
- `99-cleanup.sql`：完成后删除练习表。

## 使用规则

1. 在 Navicat 中连接 `mall`，按文件编号执行。
2. `01-setup.sql` 只创建 `lab_` 开头的练习表，不修改项目业务表。
3. 每次只执行当前题目要求的语句，不要一次运行整个 `02` 或 `03` 文件。
4. 每题先写下预测，再执行并解释结果。
5. 保存 SQL、执行计划截图和结论；只记录耗时，没有执行计划不算完成。
6. 当前练习库性能只能说明本机测试结果，不能推断生产环境表现。

## 实践路径与验收标准

### 阶段 1：读懂基线

完成 `02-index-labs.sql` 的练习 1～2。

达标：能解释 `type`、`possible_keys`、`key`、`key_len`、`rows`、`filtered`、`Extra`，并区分估算值和实际值。

### 阶段 2：完成联合索引对比

完成练习 3～5。

达标：能说明 `(brand_id, delete_status, price)` 的排序结构、最左前缀、范围条件，以及为什么没有给所有字段分别建索引。

### 阶段 3：理解回表与排序

完成练习 6～8。

达标：能从执行计划判断覆盖索引、回表、额外排序和深分页，并提出有业务前提的改进方案。

### 阶段 4：完成事务实验

完成 `03-transaction-labs.sql`。

达标：能演示 `COMMIT`、`ROLLBACK`、原子性，以及 `READ COMMITTED` 与 `REPEATABLE READ` 的可见性区别；能指出项目中的 `@Transactional` 位置。

### 阶段 5：映射回真实项目

真实商品列表代码：

- `mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java`
- `mall-admin/src/main/java/com/macro/mall/dto/PmsProductQueryParam.java`

完成实验后，用真实商品查询参数组合提出一个候选索引。不要立刻修改业务表；先说明查询频率、字段选择性、排序、分页和写入成本，再在专用测试数据上验证。

## 最终成果

填写 `04-record-template.md`。能够脱离提示讲清楚以下内容，才可以说“使用 EXPLAIN 定位并完成了一次基础 SQL 优化”：

1. 哪条 SQL、多少数据、什么数据分布。
2. 优化前实际扫描、返回和耗时。
3. 为什么选择该联合索引及字段顺序。
4. 优化后实际扫描、返回和耗时。
5. 索引空间与写入维护成本。
6. 结论适用范围和没有解决的问题。

