# Spring MVC 面试八股文（结合 mall 项目）

本文用于 Java 面试复习。建议先记住每题的“面试回答”，再用“展开说明”和项目代码应对追问。

项目技术背景：Spring Boot 3.5.14、Java 17、Spring MVC、Spring Security、MyBatis。项目通过 `spring-boot-starter-web` 使用 Spring MVC，主要提供前后端分离的 REST API。

## 总体主线

Spring MVC 的核心请求链可以先记成一句话：

> 请求经过 Filter 到达 DispatcherServlet；DispatcherServlet 通过 HandlerMapping 找到处理器，再由 HandlerAdapter 调用 Controller；Controller 调用 Service 完成业务处理；返回值通过 HttpMessageConverter 转成 JSON，或者经过 ViewResolver 渲染页面；异常则交给 HandlerExceptionResolver 处理。

---

## 1. MVC 三个部分分别负责什么？

### 面试回答

MVC 是一种职责分离的设计模式：

- Model（模型）负责承载业务数据、业务状态以及相关业务规则。
- View（视图）负责展示处理结果，例如 JSP、Thymeleaf 页面；在前后端分离项目中，客户端接收到的 JSON 可以看作表现层数据，但 `@ResponseBody` 返回 JSON 时并不会经过传统的视图解析流程。
- Controller（控制器）负责接收请求、解析参数、调用业务组件，并决定如何返回结果。

MVC 与常见的 Controller、Service、DAO 三层架构不是同一个概念。Service 和 DAO 是应用内部的业务与数据访问分层，不能把它们分别等同于 MVC 中的 Model 和 View。

### 结合 mall 项目

以商品品牌接口为例：

- Controller：`PmsBrandController`
- 请求模型：`PmsBrandParam`
- 数据模型：`PmsBrand`
- 统一响应模型：`CommonResult`
- 业务处理：`PmsBrandService`
- 数据访问：`PmsBrandMapper`
- 最终表现：JSON 响应

项目代码：

- [`PmsBrandController`](../../mall/mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java)
- [`CommonResult`](../../mall/mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java)

### 易错点

- 不要回答“MVC 就是 Controller、Service、DAO”。
- Model 不只指数据库实体，也可以包括 DTO、VO、校验结果和业务处理结果。
- REST 接口通常不使用 JSP 或 Thymeleaf，也不需要经过 `ViewResolver`。

---

## 2. Spring MVC 与 Spring Boot 有什么关系？

### 面试回答

Spring MVC 是基于 Servlet API 的 Web 框架，负责请求映射、参数绑定、Controller 调用、数据校验、视图解析、JSON 转换和异常处理。

Spring Boot 是用于快速创建和运行 Spring 应用的工程化框架。它通过自动配置、Starter 依赖和内嵌 Web 容器，降低 Spring MVC 的配置成本。

二者不是替代关系：

> Spring MVC 负责“如何处理 Web 请求”，Spring Boot 负责“如何快速配置、启动和管理 Spring 应用”。

### Spring Boot 为 Spring MVC 做了什么？

引入 `spring-boot-starter-web` 后，Spring Boot 通常会自动完成：

- 引入 Spring MVC、Jackson、Bean Validation 等常用依赖。
- 启动内嵌 Tomcat。
- 注册并配置 `DispatcherServlet`。
- 配置 `RequestMappingHandlerMapping` 和 `RequestMappingHandlerAdapter`。
- 配置常用 `HttpMessageConverter`。
- 根据配置文件定制 MVC 行为。

### 结合 mall 项目

项目父工程使用 Spring Boot 3.5.14：

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.5.14</version>
</parent>
```

`mall-common` 引入 Web Starter：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

`mall-admin` 使用 `@SpringBootApplication` 启动：

```java
@SpringBootApplication
public class MallAdminApplication {
    public static void main(String[] args) {
        SpringApplication.run(MallAdminApplication.class, args);
    }
}
```

### 易错点

- Spring MVC 可以不依赖 Spring Boot，只是需要更多手动配置。
- Spring Boot 不一定使用 Spring MVC，例如非 Web 应用或 WebFlux 应用。
- Spring Boot 没有替代 Spring MVC，而是简化了它的使用。

---

## 3. DispatcherServlet 的作用是什么？

### 面试回答

`DispatcherServlet` 是 Spring MVC 的前端控制器，是 MVC 请求处理的统一入口和总调度器。

它本身通常不执行具体业务，而是协调多个策略组件完成请求处理：

- 通过 `HandlerMapping` 查找处理器。
- 通过 `HandlerAdapter` 调用处理器。
- 通过 `HandlerExceptionResolver` 解析异常。
- 通过 `ViewResolver` 解析传统 MVC 的逻辑视图名。
- 配合返回值处理器和 `HttpMessageConverter` 输出 JSON 等响应体。

### 为什么叫“前端控制器”？

这里的“前端”不是浏览器前端，而是 Front Controller 设计模式：符合映射范围的请求先进入一个统一入口，再由这个入口分发给具体 Controller。

### 它不负责什么？

`DispatcherServlet` 不应该负责：

- 订单、商品等具体业务规则。
- 直接执行数据库 SQL。
- 代替 Controller 或 Service。

### 易错点

- 应称为“前端控制器”，不是“前置控制器”。
- 它负责调度，不负责具体业务。
- Filter 通常位于 `DispatcherServlet` 之前，不属于 Spring MVC 内部的 Handler 执行链。

---

## 4. 完整描述 Spring MVC 请求执行流程

### 面试回答

客户端请求首先进入 Servlet 容器并经过 Filter 链，然后到达 `DispatcherServlet`。`DispatcherServlet` 通过 `HandlerMapping` 找到匹配的处理器及拦截器执行链，再选择支持该处理器的 `HandlerAdapter`。拦截器执行 `preHandle` 后，`HandlerAdapter` 完成参数解析、数据绑定、类型转换、消息转换和参数校验，并调用 Controller。Controller 调用 Service、Mapper 等组件完成业务处理。对于传统 MVC，返回的 `ModelAndView` 会经过 `ViewResolver` 解析并渲染；对于 REST 接口，返回对象会通过 `HttpMessageConverter` 序列化为 JSON。发生异常时，`DispatcherServlet` 会交给 `HandlerExceptionResolver` 处理，最终执行拦截器的完成回调并返回 HTTP 响应。

### 完整步骤

1. 客户端发送 HTTP 请求。
2. 请求进入 Tomcat 等 Servlet 容器。
3. 请求依次经过 Servlet Filter，例如 CORS Filter、Spring Security Filter、JWT Filter。
4. Filter 放行后，请求到达 `DispatcherServlet`。
5. `DispatcherServlet` 请求 `HandlerMapping` 查找处理器。
6. `HandlerMapping` 返回 `HandlerExecutionChain`，其中包括 Handler 和匹配的 Interceptor。
7. `DispatcherServlet` 根据 Handler 类型选择合适的 `HandlerAdapter`。
8. Interceptor 执行 `preHandle()`；如果返回 `false`，请求链会被中断。
9. `HandlerAdapter` 使用参数解析器准备 Controller 方法参数。
10. Spring 完成请求参数绑定、类型转换、JSON 反序列化和 Bean Validation 校验。
11. `HandlerAdapter` 调用 Controller 方法。
12. Controller 调用 Service，Service 再调用 Mapper 或 Repository。
13. Controller 返回处理结果。
14. Interceptor 在 Handler 正常执行后调用 `postHandle()`。
15. 如果是传统页面请求，Spring 使用 `ViewResolver` 解析视图并渲染。
16. 如果带有 `@ResponseBody`，返回值处理器使用 `HttpMessageConverter` 将对象序列化为 JSON，并写入响应体。
17. 如果处理中发生异常，`HandlerExceptionResolver` 尝试匹配 `@ExceptionHandler` 等异常处理机制。
18. 请求处理完成后调用 Interceptor 的 `afterCompletion()`。
19. HTTP 响应经过 Filter 链返回客户端。

### mall 项目实例：`POST /brand/create`

```text
客户端
  ↓
Tomcat
  ↓
Spring Security / JwtAuthenticationTokenFilter
  ↓
DispatcherServlet
  ↓
HandlerMapping 找到 PmsBrandController.create()
  ↓
HandlerAdapter 解析 @RequestBody、执行 @Validated
  ↓
PmsBrandController
  ↓
PmsBrandServiceImpl
  ↓
PmsBrandMapper
  ↓
MySQL
  ↑
CommonResult
  ↑
@ResponseBody + Jackson 序列化
  ↑
JSON 响应
```

项目中的 JWT Filter：[`JwtAuthenticationTokenFilter`](../../mall/mall-security/src/main/java/com/macro/mall/security/component/JwtAuthenticationTokenFilter.java)。

### 异常流程补充

Controller 同步调用 Service、Mapper 时，如果异常没有在中途被捕获，就会沿调用栈返回 `DispatcherServlet`，再由异常解析器寻找匹配的 `@ExceptionHandler`。

但以下异常不一定能被 MVC 全局异常处理器捕获：

- `DispatcherServlet` 之前的 Filter 中抛出的异常。
- 新线程或线程池任务中的异常。
- 定时任务、消息消费者中的异常。
- 已经在业务代码中捕获且没有重新抛出的异常。

---

## 5. HandlerMapping 与 HandlerAdapter 有什么区别？

### 面试回答

> HandlerMapping 负责找到谁来处理请求，HandlerAdapter 负责以正确的方式调用这个处理器。

### HandlerMapping

输入通常是当前 `HttpServletRequest`，输出是 `HandlerExecutionChain`。

它主要完成：

- 根据 URL、HTTP 方法、请求参数、请求头等条件匹配 Handler。
- 找到对应的 Controller 方法。
- 组合当前请求需要执行的 Interceptor。

注解式 Controller 常用的实现是 `RequestMappingHandlerMapping`。

例如：

```java
@RequestMapping("/brand")
public class PmsBrandController {

    @RequestMapping(value = "/create", method = RequestMethod.POST)
    public CommonResult create(...) {
        // ...
    }
}
```

`POST /brand/create` 会被映射到 `create()` 方法。

### HandlerAdapter

不同 Handler 的调用方式可能不同，`DispatcherServlet` 不直接依赖每一种 Handler，而是通过适配器统一调用。

注解式 Controller 常用的实现是 `RequestMappingHandlerAdapter`，它会负责：

- 解析 Controller 方法参数。
- 执行数据绑定和校验。
- 调用 Controller 方法。
- 处理方法返回值。

### 为什么需要 HandlerAdapter？

这是适配器模式的应用。`DispatcherServlet` 面向统一接口调度，不需要知道注解 Controller、传统 Controller 等不同处理器的具体调用方式，从而降低耦合并提高扩展性。

### 记忆口诀

```text
Mapping：找方法。
Adapter：调方法。
```

---

## 6. `@Controller` 和 `@RestController` 的区别是什么？

### 面试回答

`@Controller` 表示 Spring MVC 控制器，方法返回的字符串默认可能被解释为逻辑视图名。如果希望返回 JSON，需要在方法或类上增加 `@ResponseBody`。

`@RestController` 是组合注解，等价于：

```java
@Controller
@ResponseBody
```

因此 `@RestController` 中的方法返回值默认写入 HTTP 响应体，通常通过 `HttpMessageConverter` 转换为 JSON，不会被当作逻辑视图名。

### 示例

传统页面：

```java
@Controller
public class PageController {

    @GetMapping("/home")
    public String home() {
        return "home";
    }
}
```

这里的 `"home"` 通常是逻辑视图名。

REST 接口：

```java
@RestController
public class UserController {

    @GetMapping("/users/1")
    public User getUser() {
        return new User();
    }
}
```

返回的 `User` 通常被序列化为 JSON。

### 结合 mall 项目

项目大量使用：

```java
@Controller
public class PmsBrandController {

    @ResponseBody
    public CommonResult getItem(...) {
        // ...
    }
}
```

对于全部方法都返回 JSON 的 Controller，可以使用 `@RestController` 减少重复的 `@ResponseBody`。

### 易错点

- 两个注解都能被 Spring 扫描为 Controller Bean。
- 区别主要在于是否默认带有 `@ResponseBody` 语义。
- `@RestController` 返回字符串时，字符串就是响应体内容，不会默认被解析为页面名。

---

## 7. `@RequestParam`、`@PathVariable`、`@RequestBody` 的区别是什么？

### 面试回答

- `@RequestParam` 从查询字符串、表单字段等请求参数中取值。
- `@PathVariable` 从 URL 路径模板中取值。
- `@RequestBody` 读取 HTTP 请求体，并通过 `HttpMessageConverter` 转换为 Java 对象。

### `@RequestParam`

请求：

```text
GET /brand/list?pageNum=1&pageSize=5
```

代码：

```java
@GetMapping("/brand/list")
public CommonResult list(
        @RequestParam(defaultValue = "1") Integer pageNum,
        @RequestParam(defaultValue = "5") Integer pageSize) {
    // ...
}
```

常用属性：

- `value` 或 `name`：参数名。
- `required`：是否必须提供。
- `defaultValue`：默认值；设置后通常隐含该参数非必填。

### `@PathVariable`

请求：

```text
GET /brand/10
```

代码：

```java
@GetMapping("/brand/{id}")
public CommonResult getItem(@PathVariable Long id) {
    // ...
}
```

路径变量通常用于标识具体资源。

### `@RequestBody`

请求：

```http
POST /brand/create
Content-Type: application/json

{
  "name": "Yamaha",
  "firstLetter": "Y"
}
```

代码：

```java
@PostMapping("/brand/create")
public CommonResult create(
        @Validated @RequestBody PmsBrandParam param) {
    // ...
}
```

Jackson 会将 JSON 转换为 `PmsBrandParam`，随后 `@Validated` 触发参数校验。

### 易错点

- `@RequestParam` 不是专门用于 JSON。
- `@PathVariable` 对应 URL 模板中的 `{变量}`。
- 一个 HTTP 请求只有一个请求体，通常一个方法最多声明一个主要的 `@RequestBody` 参数。
- JSON 格式错误通常会产生 `HttpMessageNotReadableException`。
- 参数绑定成功但校验失败时，可能产生 `MethodArgumentNotValidException`。

---

## 8. Filter、Interceptor、AOP 有什么区别？

### 面试回答

Filter 属于 Servlet 规范，工作在 `DispatcherServlet` 之外，面向 Servlet 请求和响应；Interceptor 属于 Spring MVC，工作在 Handler 执行链中，面向 Controller 请求；AOP 属于 Spring 的方法级横切机制，面向 Spring Bean 的方法调用。

### Filter

特点：

- 属于 Jakarta Servlet 规范。
- 通常在 `DispatcherServlet` 之前执行。
- 可以包装或修改 `HttpServletRequest`、`HttpServletResponse`。
- 不只针对 Spring MVC Controller，也可以处理其他 Servlet 资源。

常见用途：

- CORS。
- 编码处理。
- 请求包装。
- 安全认证。
- 链路追踪。

典型方法：

```java
doFilter(request, response, chain)
```

mall 项目的 `JwtAuthenticationTokenFilter` 继承 `OncePerRequestFilter`，属于 Filter。

### Interceptor

特点：

- 属于 Spring MVC。
- 围绕 Handler，也就是 Controller 方法执行。
- 可以获得匹配到的 Handler 信息。
- 一般通过 `WebMvcConfigurer#addInterceptors` 注册。

生命周期方法：

```java
preHandle()
postHandle()
afterCompletion()
```

常见用途：

- 登录检查。
- Controller 接口权限检查。
- 接口耗时统计。
- 操作日志。
- 公共模型数据处理。

### AOP

特点：

- 基于 Spring AOP，常见实现方式是代理。
- 面向 Spring Bean 方法，而不是只面向 HTTP 请求。
- 可以作用于 Controller、Service、Repository 等 Bean。
- 同一个 Service 方法即使由定时任务调用，也可能经过相应 AOP 切面。

常见用途：

- 声明式事务。
- 方法日志。
- 权限校验。
- 缓存。
- 监控与性能统计。

常见通知：

```java
@Before
@After
@AfterReturning
@AfterThrowing
@Around
```

### 执行位置

典型 Web 请求可以粗略理解为：

```text
Filter
  ↓
DispatcherServlet
  ↓
Interceptor.preHandle
  ↓
Controller（可能经过 AOP 代理）
  ↓
Service（可能经过事务等 AOP 代理）
  ↓
Interceptor.postHandle / afterCompletion
  ↓
Filter 返回阶段
```

### 易错点

- Filter 不属于 Spring MVC，它属于 Servlet 规范。
- Interceptor 主要拦截 MVC Handler。
- AOP 不局限于 HTTP 请求，可以拦截普通 Spring Bean 方法。
- Filter 中发生且未进入 `DispatcherServlet` 的异常，通常不能直接依赖 MVC 的 `@ControllerAdvice` 处理。

---

## 9. Spring MVC 如何统一处理异常？

### 面试回答

Spring MVC 可以通过 `@ExceptionHandler` 处理指定异常，通过 `@ControllerAdvice` 或 `@RestControllerAdvice` 将异常处理扩展到多个 Controller。底层由 `HandlerExceptionResolver` 体系解析异常。REST 项目通常将异常转换为统一响应结构，并配合 `ResponseEntity` 或 `@ResponseStatus` 设置正确的 HTTP 状态码。

### 局部异常处理

在某个 Controller 内定义：

```java
@ExceptionHandler(IllegalArgumentException.class)
@ResponseBody
public CommonResult handle(IllegalArgumentException e) {
    return CommonResult.failed(e.getMessage());
}
```

它主要处理当前 Controller 中传播出来的匹配异常。

### 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ApiException.class)
    public ResponseEntity<CommonResult<Void>> handleApiException(
            ApiException e) {
        return ResponseEntity.badRequest()
                .body(CommonResult.failed(e.getMessage()));
    }
}
```

其中：

- `@ExceptionHandler(ApiException.class)` 表示处理 `ApiException` 及其子类。
- `@RestControllerAdvice` 相当于 `@ControllerAdvice` 与 `@ResponseBody` 的组合。
- 如果出现多个候选方法，Spring 会优先选择异常类型更加具体的处理方法。

### 结合 mall 项目

项目使用 [`GlobalExceptionHandler`](../../mall/mall-common/src/main/java/com/macro/mall/common/exception/GlobalExceptionHandler.java) 处理：

- `ApiException`：业务异常。
- `MethodArgumentNotValidException`：常见于 `@RequestBody` 对象校验失败。
- `BindException`：常见于表单或查询参数绑定对象时校验失败。
- `SQLSyntaxErrorException`：SQL 相关异常。

`ApiException` 可以通过两种方式创建：

```java
throw new ApiException(ResultCode.FAILED);
throw new ApiException("库存不足");
```

第一种会给 `errorCode` 字段赋值；第二种只设置异常的 `message`，此时 `getErrorCode()` 返回 `null`。

### 项目中值得指出的改进点

1. 全局处理器没有统一调用 `log.error(..., e)`，被处理的异常不保证留下完整堆栈。
2. SQL 异常信息不应直接返回给客户端，否则可能泄露数据库结构和 SQL 信息。
3. MyBatis 与 Spring 常把底层 `SQLException` 转换为 `DataAccessException`，只处理 `SQLSyntaxErrorException` 可能覆盖不完整。
4. 返回体中的业务 `code=500` 不代表 HTTP 状态一定是 500；如果没有 `ResponseEntity` 或 `@ResponseStatus`，HTTP 状态可能仍是 200。
5. 还可以补充处理 `HttpMessageNotReadableException`、`HandlerMethodValidationException` 和兜底 `Exception`，但兜底时必须记录日志。

### 推荐原则

- 可预期业务异常：返回稳定、可理解的业务信息。
- 参数校验异常：返回具体字段错误，但避免泄露内部实现。
- 未知系统异常：记录完整堆栈，对外只返回通用提示。
- 区分业务错误码和 HTTP 状态码。
- 不要捕获 `Throwable` 后把所有严重错误都吞掉。

---

## 10. GET、POST、PUT、DELETE 的语义和幂等性是什么？

### 面试回答

- GET 用于获取资源，按 HTTP 语义是安全且幂等的。
- POST 常用于创建资源或提交命令，通常不保证幂等。
- PUT 用于在指定 URI 创建或整体替换资源，按语义是幂等的。
- DELETE 用于删除资源，按语义是幂等的。

幂等的含义是：

> 对服务器端资源而言，同一个请求执行一次和执行多次，预期效果相同；不要求每次响应内容和状态码完全相同。

### GET

```http
GET /products/10
```

用于读取资源。它应该是：

- 安全：客户端不期望它修改服务端业务状态。
- 幂等：执行多次不会产生额外业务副作用。

日志、统计计数或缓存变化通常不改变 GET 的语义判断，但不能使用 GET 完成删除订单等业务操作。

### POST

```http
POST /orders
```

常用于创建资源、提交表单或执行命令。如果同一个创建订单请求重复执行，可能创建多个订单，因此通常不幂等。

可以通过幂等键、唯一约束、请求去重等手段把具体 POST 接口设计成幂等，但这不是 POST 方法天然保证的。

### PUT

```http
PUT /users/10
```

通常表示用请求中的完整数据创建或整体替换指定资源。多次提交同样内容，最终资源状态相同，所以具有幂等语义。

部分更新更常用 PATCH。实际项目如果使用 PUT 做部分更新，应在接口文档中明确约定。

### DELETE

```http
DELETE /products/10
```

第一次可能成功删除并返回 204，第二次可能返回 404，但资源都处于“不存在”的状态，因此仍然符合幂等语义。

### 结合 mall 项目

项目中存在类似：

```java
@RequestMapping(value = "/delete/{id}", method = RequestMethod.GET)
```

也就是使用 GET 删除品牌。这能够工作，但不符合标准 HTTP 语义，可能带来：

- 被浏览器预取或爬虫误触发。
- 被缓存系统错误处理。
- 与 REST 接口语义不一致。

更合理的形式是：

```java
@DeleteMapping("/brand/{id}")
```

### 易错点

- 幂等不表示每次返回内容必须完全相同。
- POST 并非永远不幂等，可以由业务额外保证。
- DELETE 多次请求的状态码可以不同，但最终资源状态应一致。
- “安全方法”表示不期望修改资源，不等于网络安全或身份认证安全。

---

## 11. JSON 是如何转换为 Java 对象的？

### 面试回答

Spring MVC 通过 `HttpMessageConverter` 完成 HTTP 消息体和 Java 对象之间的转换。使用 Jackson 时，通常由 `MappingJackson2HttpMessageConverter` 调用 `ObjectMapper`，根据 `Content-Type`、目标参数类型和 JSON 内容，把请求体反序列化为 Java 对象。Controller 返回值带有 `@ResponseBody` 时，同一机制会把 Java 对象序列化为 JSON。

### 请求 JSON 转 Java 对象

```java
@PostMapping("/users")
public CommonResult create(@Valid @RequestBody UserParam param) {
    // ...
}
```

处理流程：

```text
HTTP 请求体字节
  ↓
根据 Content-Type 选择 HttpMessageConverter
  ↓
Jackson ObjectMapper
  ↓
读取 JSON 属性
  ↓
实例化并填充 UserParam
  ↓
执行 @Valid / @Validated 校验
  ↓
作为参数传给 Controller
```

常见请求头：

```http
Content-Type: application/json
```

如果客户端没有发送正确的 `Content-Type`，可能出现 415 Unsupported Media Type；如果 JSON 格式错误或字段类型无法转换，可能抛出 `HttpMessageNotReadableException`。

### Java 对象转 JSON

```java
@ResponseBody
public CommonResult<User> getUser() {
    return CommonResult.success(user);
}
```

处理流程：

```text
Java 返回对象
  ↓
返回值处理器识别 @ResponseBody
  ↓
根据响应类型和 Accept 选择 HttpMessageConverter
  ↓
Jackson ObjectMapper 序列化
  ↓
JSON 写入 HTTP 响应体
```

### Jackson 常见关注点

- Java 属性名与 JSON 属性名的映射。
- Getter、Setter、字段可见性和构造方式。
- 日期时间格式。
- 枚举的序列化方式。
- 未知字段处理。
- 空值处理。
- 循环引用。
- `@JsonProperty`、`@JsonIgnore`、`@JsonFormat` 等注解。

### 易错点

- JSON 转换不是 `DispatcherServlet` 自己手写完成的，而是委托给消息转换器。
- `@RequestBody` 主要读取请求体，不是读取 URL 查询参数。
- 对象创建成功后，`@Valid` 或 `@Validated` 才继续执行 Bean Validation。
- `@ResponseBody` 返回 JSON 时通常不经过 `ViewResolver`。

---

## 12. 转发与重定向有什么区别？

### 面试回答

转发发生在服务器内部，通常只有一次客户端请求，浏览器地址栏不变，可以共享同一个请求对象和请求属性；重定向由服务器返回 3xx 和 `Location` 响应头，浏览器再发送一次新请求，因此地址栏会改变，原请求属性通常不能直接保留。

### 转发 Forward

Spring MVC 示例：

```java
return "forward:/target";
```

特点：

- 服务器内部把同一个请求交给另一个资源处理。
- 浏览器通常不知道服务器内部发生了转发。
- 地址栏 URL 不变。
- 通常只有一次客户端请求。
- 可以继续读取原来的 request attribute。
- 一般只能转发到当前 Web 应用内部资源。

示例：

```java
request.setAttribute("message", "success");
return "forward:/result";
```

目标处理器仍然可以从当前 request 中读取 `message`。

### 重定向 Redirect

Spring MVC 示例：

```java
return "redirect:/login";
```

大致过程：

```text
客户端请求 /old
  ↓
服务器返回 302 + Location: /login
  ↓
浏览器重新请求 /login
```

特点：

- 通常产生两次 HTTP 请求。
- 浏览器地址栏变成新的 URL。
- 新请求拥有新的 request 和 response。
- 原来的 request attribute 不会自动保留。
- 可以重定向到外部网站。
- 可以通过查询参数、Session 或 Flash Attribute 在两次请求之间传递必要数据。

### 常见应用场景

转发适合：

- 服务器内部把请求交给另一个处理器。
- 希望保留当前请求属性。
- 不希望客户端 URL 改变。

重定向适合：

- 登录完成后跳转首页。
- 表单提交成功后跳转结果页。
- 使用 PRG（Post/Redirect/Get）避免用户刷新页面时重复提交表单。
- 跳转到外部地址。

### REST 项目中的处理

前后端分离 REST API 通常不会通过逻辑视图名控制浏览器跳转。后端更常返回：

- 正确的 3xx HTTP 状态码。
- `Location` 响应头。
- 或普通 JSON，由前端路由决定页面跳转。

例如：

```java
return ResponseEntity.status(HttpStatus.FOUND)
        .location(URI.create("/login"))
        .build();
```

### 易错点

- 转发通常一次请求；重定向通常两次请求。
- 转发地址栏不变；重定向地址栏改变。
- 转发能共享 request attribute；重定向不能直接共享。
- 重定向默认可能使用 302，但不同业务可以选择 301、303、307、308 等状态码，它们对缓存和请求方法处理的语义不同。

---

## 面试前最终速记

```text
MVC：Model 管数据，View 管展示，Controller 管协调。

Spring MVC 管 Web 请求；Spring Boot 管自动配置和快速启动。

DispatcherServlet 是统一入口和总调度器。

HandlerMapping 找方法；HandlerAdapter 调方法。

@RestController = @Controller + @ResponseBody。

@RequestParam 取请求参数；
@PathVariable 取路径变量；
@RequestBody 读取请求体。

Filter 属于 Servlet；
Interceptor 属于 Spring MVC；
AOP 面向 Spring Bean 方法。

@ControllerAdvice + @ExceptionHandler 实现全局异常处理。

GET 安全且幂等；
POST 通常不幂等；
PUT、DELETE 按语义幂等。

JSON 转换依赖 HttpMessageConverter 和 Jackson。

转发是服务器内部的一次请求；
重定向是浏览器发起的新请求。
```

## 推荐口述顺序

如果面试官要求完整描述一次请求，可以按以下顺序回答：

```text
Tomcat
→ Filter
→ DispatcherServlet
→ HandlerMapping
→ HandlerAdapter
→ Interceptor.preHandle
→ 参数解析、JSON 转换、参数校验
→ Controller
→ Service
→ Mapper
→ Controller 返回值
→ JSON 消息转换或视图渲染
→ Interceptor.afterCompletion
→ HTTP 响应
```

回答时最好结合项目中的 `POST /brand/create` 举例，这比只背框架组件名称更有说服力。
