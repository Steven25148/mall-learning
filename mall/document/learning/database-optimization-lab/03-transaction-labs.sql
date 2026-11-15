USE mall;

DROP TABLE IF EXISTS lab_account;
CREATE TABLE lab_account (
    id BIGINT NOT NULL,
    owner_name VARCHAR(50) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT chk_lab_balance CHECK (balance >= 0)
) ENGINE=InnoDB;

INSERT INTO lab_account VALUES
(1, '甲', 1000.00),
(2, '乙', 1000.00);

-- 练习 1：ROLLBACK 验证原子性
START TRANSACTION;
UPDATE lab_account SET balance = balance - 100 WHERE id = 1;
UPDATE lab_account SET balance = balance + 100 WHERE id = 2;
SELECT * FROM lab_account;
ROLLBACK;
SELECT * FROM lab_account;

-- 验收：事务内看到 900/1100，回滚后恢复 1000/1000。

-- 练习 2：COMMIT
START TRANSACTION;
UPDATE lab_account SET balance = balance - 100 WHERE id = 1;
UPDATE lab_account SET balance = balance + 100 WHERE id = 2;
COMMIT;
SELECT * FROM lab_account;

-- 完成观察后恢复数据：
UPDATE lab_account SET balance = 1000.00;

-- 练习 3：REPEATABLE READ。打开 Navicat 的查询窗口 A 和 B。
-- 窗口 A：
-- SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- START TRANSACTION;
-- SELECT balance FROM lab_account WHERE id = 1;

-- 窗口 B：
-- UPDATE lab_account SET balance = 888.00 WHERE id = 1;
-- COMMIT;

-- 回到窗口 A：
-- SELECT balance FROM lab_account WHERE id = 1;
-- COMMIT;
-- SELECT balance FROM lab_account WHERE id = 1;

-- 问题：窗口 A 在提交前后分别看到什么？为什么？

-- 练习 4：READ COMMITTED。先恢复 balance=1000，再重复双窗口步骤。
-- 窗口 A：
-- SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- START TRANSACTION;
-- SELECT balance FROM lab_account WHERE id = 1;

-- 窗口 B：
-- UPDATE lab_account SET balance = 777.00 WHERE id = 1;
-- COMMIT;

-- 回到窗口 A：
-- SELECT balance FROM lab_account WHERE id = 1;
-- COMMIT;

-- 问题：它与 REPEATABLE READ 的第二次读取有何差别？

-- 收尾恢复：
UPDATE lab_account SET balance = 1000.00;

-- 项目映射题：阅读以下接口上的 @Transactional，并追踪实现中的多表写入：
-- mall-admin/src/main/java/com/macro/mall/service/PmsProductService.java
-- mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderService.java
-- 回答：如果其中第 N 次写入抛出运行时异常，前面写入为什么需要回滚？

