# mall 本地运行说明

源码：D:\project\mall（Java 后端）；D:\project\mall-admin-web（管理网页）。

## 使用

不想记命令时，可以直接双击：

- `Debug-Mall-Admin.cmd`：重新构建并启动当前学习需要的 MySQL、Redis、mall-admin 和管理网页，同时开放 5005 调试端口。
- `Start-Mall-All.cmd`：启动当前已经安装的整套项目服务。

在 PowerShell 中运行。平时调试后台接口只启动最小环境：

```powershell
& D:\project\local\Start-Mall.ps1 -Mode Admin
```

如果要在 IDEA 中直接以 Debug 方式运行 `MallAdminApplication`，先只启动基础设施：

```powershell
& D:\project\local\Start-Mall.ps1 -Mode Infra
```

如果要由脚本启动后台并使用 IDEA Remote JVM Debug，运行后按脚本打印的 WSL IP 附加到 5005 端口：

```powershell
& D:\project\local\Start-Mall.ps1 -Mode Admin -DebugAdmin
```

修改 Java 源码后，如果仍由脚本运行 JAR，增加 `-Build` 重新打包：

```powershell
& D:\project\local\Start-Mall.ps1 -Mode Admin -Build -DebugAdmin
```

需要商城全部本地服务时才使用：

```powershell
& D:\project\local\Start-Mall.ps1 -Mode All
& D:\project\local\Test-Mall.ps1
```

打开 http://127.0.0.1:5173 ，本地样例账号 admin / macro123。
启动脚本会读取当前 Ubuntu IP，更新网页接口地址，并打印三个 Swagger 文档地址。首次启动后端需等待约 20～60 秒再运行验收脚本。

## 单独启动 Elasticsearch

在 Ubuntu 终端执行：

```bash
bash /mnt/d/project/local/start-elasticsearch.sh
```

该脚本使用 nohup 后台启动，已有服务时不会重复启动。日志保存在 `D:\project\local\elasticsearch.log`。关闭启动终端不会因终端挂断而停止 ES；关机或停止 WSL 会停止 ES，下次需重新启动。这不包含 Windows 开机自动启动设置。

整套启动入口 `Start-Mall-All.cmd` / `Start-Mall.ps1 -Mode All` 通过 `start-backends.sh` 调用同一个 ES 启动脚本。ES 的 JVM 参数包含 `-Djava.net.preferIPv4Stack=true`，避免本机曾出现的 IPv4 映射 IPv6 监听下 WSL 本机转发不可达问题；ES 仍仅绑定 `127.0.0.1`。

Elasticvue 使用 No authorization，地址为 `http://127.0.0.1:9200`。Ubuntu 中用 `curl http://127.0.0.1:9200` 检查，Windows PowerShell 中用 `curl.exe --noproxy "*" http://127.0.0.1:9200` 检查。Ubuntu 能访问不代表 Windows 转发一定正常，应分别验证。

## 已验证（2026-09-14）

- 后端全部 Maven 模块打包成功；此次使用跳过测试参数，不能视为单元测试通过。
- 管理网页 Vite 生产构建成功；网页 HTTP 返回成功。浏览器自动化不可用，尚未完成可视化点击验收。
- admin 登录成功；带 JWT 查询商品成功，共 20 条样例商品。
- 商城首页查询成功。
- 搜索导入 20 条数据；搜索“小米”返回 6 条。
- MySQL 导入 76 张表；Redis PING 返回 PONG。
- RabbitMQ 的 mall.order.cancel 队列有 1 个消费者连接，尚未做下单和延迟取消完整测试。
- 结构化接口验收结果：verification.json。

## 环境与本地调整

运行环境在现有 Ubuntu-24.04 / WSL2 中：Java 17、Maven 3.8.7、MySQL 8.0、Redis、RabbitMQ、MongoDB 8.0.4、Elasticsearch 8.18.0 + IK 8.18.0。

Docker 已安装，但 Docker Hub 网络超时，当前中间件使用 Ubuntu 软件包或官方独立程序运行。项目 README 的 MySQL 5.7、ES 7.x 环境表与当前 Spring Boot 3.5 分支存在年代差异；本次实际验证以上运行组合，尚未做所有 SQL 和业务兼容性回归。

后端仓库未修改；独立 run-backend.sh 覆盖数据库地址及账号。mall 数据库使用专用本地账号，配置见该脚本。网页补充显式依赖 @element-plus/icons-vue，并添加 pnpm 锁文件；.env.development.local 保存当前 WSL API 地址。

管理后端 8080、商城后端 8085、搜索后端 8081；ES 9200 和 MongoDB 27017 仅监听 Ubuntu 本机。后台页面监听 Windows 127.0.0.1:5173。

源码版本：
- mall: 0504e86b1f1b6f1b8aa6a734d37a90fb67346be7
- mall-admin-web: 81fc17e5a19f452bd854b106a9d59fa1ed5c7eac

## 尚未跑通的范围

- MinIO 图片上传：官方二进制下载地址返回 HTTP 410，未安装。阿里云 OSS 也未配置真实账号。
- 支付宝真实/沙箱支付：仓库保留占位配置，需要自己的沙箱应用信息。
- 移动端商城网页未拉取；商城后端可通过 Swagger 调用。
- Nginx、日志采集栈、Jenkins 尚未部署；现阶段网页由 Vite 提供。
- 未进行并发、压力、缓存一致性或故障实验，不声称已有优化结论。

## 下一次从哪里读

先亲自登录并查询商品，再从 mall-admin 的 UmsAdminController.login 开始，追踪 UmsAdminServiceImpl、UmsAdminCacheServiceImpl，以及 mall-security 中的 JWT 过滤器。先弄清请求如何认证、何时访问 Redis、何时查询 MySQL。随后再读 PmsProductServiceImpl 的商品分页查询。

运行日志位于本目录的 *.log，编译日志在 D:\project\mall-build.log。再次通过启动脚本启动的后端日志名为 mall-admin.log、mall-portal.log、mall-search.log；本次首次运行对应 admin.log、portal.log、search.log。
