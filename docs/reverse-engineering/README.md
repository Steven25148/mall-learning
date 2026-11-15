# 文档阅读入口

从[《项目需求与架构设计说明书》](D:/project/docs/reverse-engineering/项目需求与架构设计说明书.md)开始阅读。

本套文档分析已存在的mall工程，不重新设计系统；正文23章描述实际实现，潜在问题单列第23章。分析日期为2026-09-17，源代码版本与本次静态分析边界在正文开头说明。

## 按问题查阅

- 想了解用途、功能、角色：正文第1—4章。
- 想跟踪登录、下单、支付、取消：正文第5、15章及第4章核心需求。
- 想查接口参数与返回类型：[附录A](D:/project/docs/reverse-engineering/附录A-API完整清单.md)和[附录C](D:/project/docs/reverse-engineering/附录C-接口模型字段.md)。
- 想查76张表的字段、默认值、主键与索引：[附录B](D:/project/docs/reverse-engineering/附录B-数据库完整字典.md)。
- 想了解Redis、MQ、ES、事务和并发：正文第12—17章。
- 想按一个业务功能定位代码：[附录E](D:/project/docs/reverse-engineering/附录E-功能需求与代码追踪.md)与[附录D](D:/project/docs/reverse-engineering/附录D-Service与事务索引.md)。
- 想了解本次检查的范围：[文档核查记录](D:/project/docs/reverse-engineering/文档核查记录.md)。这不等于应用运行或全量测试结果。

正文中的图使用Mermaid语法；在支持Mermaid的Markdown阅读器中显示为架构、时序与ER图。源代码链接使用当前工作区绝对路径并尽量带行号。接口方法数量按源码映射计数，教学应用单列；表存在、接口存在、历史验收和当前运行验证是不同证据，文档没有混用。

附带JSON是可检索的原始清单与核查结果；tools中的脚本仅用于重新提取/校验文档，不参与商城运行。重新提取会更新附录，正文分析需要在代码变化后人工复核。
