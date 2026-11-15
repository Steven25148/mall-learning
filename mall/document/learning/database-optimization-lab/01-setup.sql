-- 在 mall 数据库中建立隔离练习表，不修改 pms_product。
USE mall;

DROP TABLE IF EXISTS lab_product_query;

CREATE TABLE lab_product_query (
    id BIGINT NOT NULL AUTO_INCREMENT,
    brand_id BIGINT NOT NULL,
    product_category_id BIGINT NOT NULL,
    product_sn VARCHAR(64) NOT NULL,
    name VARCHAR(200) NOT NULL,
    delete_status TINYINT NOT NULL,
    publish_status TINYINT NOT NULL,
    verify_status TINYINT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    create_time DATETIME NOT NULL,
    description VARCHAR(500) NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- 生成 100,000 行可重复的测试数据。
-- 品牌约 100 种、分类约 20 种；约 98% 未删除，状态和价格有固定分布。
SET SESSION cte_max_recursion_depth = 100001;

INSERT INTO lab_product_query (
    brand_id,
    product_category_id,
    product_sn,
    name,
    delete_status,
    publish_status,
    verify_status,
    price,
    create_time,
    description
)
WITH RECURSIVE seq AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 100000
)
SELECT
    MOD(n, 100) + 1,
    MOD(n, 20) + 1,
    CONCAT('SN', LPAD(n, 8, '0')),
    CONCAT('商品-', LPAD(n, 8, '0')),
    IF(MOD(n, 50) = 0, 1, 0),
    MOD(n, 2),
    MOD(n, 3) = 0,
    MOD(n * 37, 100000) / 100 + 1,
    TIMESTAMP('2024-01-01 00:00:00') + INTERVAL MOD(n, 730) DAY,
    RPAD(CONCAT('商品说明-', n), 200, 'x')
FROM seq;

ANALYZE TABLE lab_product_query;

SELECT COUNT(*) AS row_count FROM lab_product_query;
SHOW INDEX FROM lab_product_query;

-- 验收：row_count = 100000，索引列表中只有 PRIMARY。

