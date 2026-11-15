# mall-admin pytest 接口测试

这些测试不创建、更新或删除商品和订单。登录接口会写入登录日志；其余接口只读取数据。覆盖登录与鉴权、商品筛选与分页、订单筛选、列表与详情一致性。可选的数据库测试只执行参数化 `SELECT`。

## 运行

在 `D:\project\mall` 下运行，先确保 mall-admin、MySQL 和 Redis 已启动。测试账号请使用有读取商品与订单权限的账号。

```powershell
$env:MALL_BASE_URL = 'http://127.0.0.1:8080'
$env:MALL_TEST_USERNAME = 'admin'
$env:MALL_TEST_PASSWORD = '<本地测试账号密码>'
& .\.venv-api-tests\Scripts\python.exe -m pytest -c tests\api\pytest.ini tests\api -v
```

若未安装依赖：`python -m pip install -r tests/api/requirements.txt`。不要把真实密码写入测试代码或提交到仓库。服务运行在 WSL 时，把 `MALL_BASE_URL` 改为 Windows 可访问的 WSL 地址。

只看测试清单：`python -m pytest -c tests/api/pytest.ini tests/api --collect-only -q`。

单独运行鉴权测试：`python -m pytest -c tests/api/pytest.ini tests/api -m integration -k auth -v`。

数据库核对为可选项。设置 `MALL_DB_HOST`、`MALL_DB_PORT`（默认 3306）、`MALL_DB_USER`、`MALL_DB_PASSWORD`、`MALL_DB_NAME` 后，加 `--run-db -m db`。数据库账号只需 `pms_product` 的 `SELECT` 权限。

## pytest 知识点

- `fixture`：复用 HTTP 会话、登录 Token、样本商品与订单；会话级和模块级作用域减少重复请求。
- `parametrize`：同一断言覆盖多个页大小、筛选字段与鉴权输入；每组有独立测试结果。
- `mark`、`-m`、`-k`：按集成测试、数据库测试或名称选取用例。
- `pytest.skip`：只有样本数据不足或未启用数据库校验时才跳过；服务不可达与断言不符均报失败。
- `pytest_addoption`：通过 `--base-url` 和 `--run-db` 控制环境；凭据从环境变量读取。

这些用例校验当前源码可确认的行为。它们没有覆盖尚未实现的金额区间筛选，也不代表压力测试或移动端测试。

当前错误密码走 `ApiException`，业务码是 500，测试据此写断言。面试时可以提出缺陷候选：更合适的做法可能是统一为明确的认证失败业务码，并保持 HTTP 状态和响应体语义一致；是否改动需遵循团队 API 规范。
