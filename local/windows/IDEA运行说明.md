# Windows 原生运行

已初始化 MySQL，导入 mall 数据库（76 张表）。Memurai 由 Windows 服务运行。

## IDEA

1. 打开 D:\project\mall\pom.xml，作为 Maven 项目导入。
2. Project SDK 和 Maven 导入/运行 JDK 使用 D:\project\local\windows\runtime\jdk-17.0.21+9。
3. Maven 可以选择 IDEA Bundled Maven，等待依赖下载。
4. 运行 mall-admin 模块的 com.macro.mall.MallAdminApplication，默认 dev 配置即可。
5. 如 8080 已被本次验证用 JAR 占用，在 PowerShell 执行 Stop-Process -Id 32420 后，再从 IDEA 启动。仅在确认该 PID 仍对应此次 Java 进程时执行。

## 数据库

DBeaver 新建 MySQL 连接：127.0.0.1:3306，数据库 mall，用户名 root，密码 root。首次连接按提示下载驱动。若出现 Public Key Retrieval 错误，在驱动属性设置 allowPublicKeyRetrieval=true、useSSL=false（本地开发）。

MySQL 未注册系统服务；重新开机后执行本目录 Start-MySQL.ps1。Memurai 端口 6379。

## 前端

在 D:\project\mall-admin-web 执行 npm.cmd run dev，打开 http://127.0.0.1:5173 。开发 API 已改为 http://127.0.0.1:8080。

后台样例账号：admin / macro123。API 文档：http://127.0.0.1:8080/swagger-ui.html 。

本次通过现有 JAR 验证了登录及带 Token 的商品查询，没有通过 IDEA 重新编译源码。图片上传等额外服务尚未配置。
