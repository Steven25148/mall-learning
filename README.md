# mall-learning

mall 电商项目学习工作区：Spring Boot 后端、Vue 3 管理前端、学习笔记、接口文档与虚假样例数据。

## 来源与许可

- 后端：https://github.com/macrozheng/mall ，来源提交 0504e86b1f1b6f1b8aa6a734d37a90fb67346be7。
- 前端：https://github.com/macrozheng/mall-admin-web ，来源提交 81fc17e5a19f452bd854b106a9d59fa1ed5c7eac。
- 保留各项目原始 LICENSE、版权声明和 README。此仓库含本地学习修改，不是上游官方仓库。

## 目录

- `mall`：Java 17 / Spring Boot 多模块后端，IDEA 导入 pom.xml。
- `mall-admin-web`：Vue 3 / Vite 前端，安装依赖后 npm run dev。
- `docs`、`学习成果`：学习资料。
- `postman`：接口调试资料。
- `local`：本地运行参考脚本。部分脚本适用于原作者本机 WSL，跨机器需要调整路径。

## 本地运行

需要 Java 17、MySQL、Redis 兼容服务和符合前端 package.json 要求的 Node.js。导入 `mall/document/sql/mall.sql` 中的虚假样例数据。

公开副本中的部分密码及 JWT 签名配置已替换为 `CHANGE_ME`，请在未提交的本机配置中填写实际值。不要将真实数据、Token、日志、数据库运行目录或密钥提交到仓库。此仓库没有运行环境安装包，local 中的原机路径需按实际安装位置修改。

前端可使用 `.env.development.local` 设置 `VITE_BASE_SERVER_URL=http://127.0.0.1:8080`，此文件不提交。

历史运行说明中的验证记录来自原学习环境，不代表新机器已经配置成功。此副本保留当前学习源码，未包含上游 Git 历史。
