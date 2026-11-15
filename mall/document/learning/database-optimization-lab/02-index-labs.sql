USE mall;

-- 每次只执行当前练习块，并把结果记录到 04-record-template.md。

-- 练习 1：主键查询基线
-- 执行前预测 type、key、rows，再对照结果。
EXPLAIN ANALYZE
SELECT * FROM lab_product_query WHERE id = 50000;

-- 练习 2：没有二级索引时按品牌查询
-- 问题：实际读取多少行？返回多少行？为什么主键不能帮助 brand_id 定位？
EXPLAIN ANALYZE
SELECT id, name, price
FROM lab_product_query
WHERE brand_id = 42
  AND delete_status = 0;

-- 练习 3：建立第一个联合索引并重复练习 2
CREATE INDEX idx_lab_brand_delete
ON lab_product_query (brand_id, delete_status);

ANALYZE TABLE lab_product_query;

EXPLAIN ANALYZE
SELECT id, name, price
FROM lab_product_query
WHERE brand_id = 42
  AND delete_status = 0;

-- 问题：优化前后的 actual rows、执行时间和访问路径分别有什么变化？

-- 练习 4：验证最左前缀
EXPLAIN ANALYZE
SELECT id FROM lab_product_query WHERE brand_id = 42;

EXPLAIN ANALYZE
SELECT id FROM lab_product_query WHERE delete_status = 0;

EXPLAIN ANALYZE
SELECT id FROM lab_product_query
WHERE delete_status = 0 AND brand_id = 42;

-- 问题：WHERE 中条件的书写顺序是否改变索引字段顺序？
-- 问题：为什么只查 delete_status 时，这个联合索引不能高效定位？

-- 练习 5：等值条件加价格范围
CREATE INDEX idx_lab_brand_delete_price
ON lab_product_query (brand_id, delete_status, price);

ANALYZE TABLE lab_product_query;

EXPLAIN ANALYZE
SELECT id, brand_id, delete_status, price
FROM lab_product_query
WHERE brand_id = 42
  AND delete_status = 0
  AND price BETWEEN 100 AND 500;

EXPLAIN ANALYZE
SELECT id, brand_id, delete_status, price
FROM lab_product_query
WHERE price BETWEEN 100 AND 500;

-- 问题：为什么第二条不能像第一条一样定位一个连续索引范围？

-- 练习 6：覆盖索引与回表
EXPLAIN ANALYZE
SELECT id, brand_id, delete_status, price
FROM lab_product_query
WHERE brand_id = 42
  AND delete_status = 0
  AND price BETWEEN 100 AND 500;

EXPLAIN ANALYZE
SELECT id, brand_id, delete_status, price, name, description
FROM lab_product_query
WHERE brand_id = 42
  AND delete_status = 0
  AND price BETWEEN 100 AND 500;

-- 问题：第一条所需列是否都能从二级索引获得？第二条为什么需要读取聚簇索引？
-- 注意：EXPLAIN ANALYZE 的树形输出比传统 Extra 更适合观察实际访问路径。

-- 练习 7：LIKE 与索引可定位范围
CREATE INDEX idx_lab_name ON lab_product_query (name);
ANALYZE TABLE lab_product_query;

EXPLAIN ANALYZE
SELECT id, name FROM lab_product_query WHERE name LIKE '商品-00012%';

EXPLAIN ANALYZE
SELECT id, name FROM lab_product_query WHERE name LIKE '%0012%';

-- 问题：前缀匹配和包含匹配的访问范围为什么不同？

-- 练习 8：排序、LIMIT 与深分页
EXPLAIN ANALYZE
SELECT id, price
FROM lab_product_query
WHERE brand_id = 42 AND delete_status = 0
ORDER BY price, id
LIMIT 20;

EXPLAIN ANALYZE
SELECT id, price
FROM lab_product_query
WHERE brand_id = 42 AND delete_status = 0
ORDER BY price, id
LIMIT 800, 20;

-- 取得上一页最后一行的 price 和 id 后，将值代入下面的游标分页示例：
-- SELECT id, price
-- FROM lab_product_query
-- WHERE brand_id = 42
--   AND delete_status = 0
--   AND (price > 500.00 OR (price = 500.00 AND id > 12345))
-- ORDER BY price, id
-- LIMIT 20;

-- 问题：OFFSET 为什么需要跳过前面的记录？游标分页有什么功能限制？

-- 练习 9：评估索引成本
SHOW TABLE STATUS LIKE 'lab_product_query';
SHOW INDEX FROM lab_product_query;

-- 比较 Data_length、Index_length；解释为什么不能无限增加索引。

