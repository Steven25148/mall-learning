# Hibernate 面试八股文（含综合应用）

本文用于 Java 面试复习。每道题先给出可直接口述的“面试回答”，再补充原理、代码和常见追问。

> 项目背景说明：当前 mall 项目实际采用 MyBatis，并没有引入 Hibernate 或 Spring Data JPA。因此本文的 Hibernate/JPA 代码是面试型参考实现；涉及项目时，会使用 mall 项目的 MyBatis 代码进行对照。

## 总体主线

先记住一条核心关系：

```text
JPA 是持久化规范
Hibernate 是 JPA 的常见实现，也是独立 ORM 框架
Session / EntityManager 管理持久化上下文
事务中的受管理实体可以通过脏检查自动生成 UPDATE
```

---

## 1. 什么是 ORM？Hibernate 与 JPA 是什么关系？

### 面试回答

ORM 是 Object-Relational Mapping，即对象关系映射。它在 Java 对象模型与关系数据库模型之间建立映射，例如把类映射成表、属性映射成列、对象关联映射成外键关系，让开发者可以主要以对象方式完成持久化操作。

JPA，也就是 Jakarta Persistence，是 Java 持久化规范，定义了实体注解、`EntityManager`、JPQL、实体生命周期等标准 API；Hibernate 是 ORM 框架，也是 JPA 最常用的实现之一。JPA 是规范，Hibernate 是实现，但 Hibernate 还提供 `Session`、HQL 等超出 JPA 标准的原生能力。

### 对象与关系模型的映射

```text
Java 类            ↔ 数据库表
Java 属性          ↔ 数据库列
对象标识           ↔ 主键
对象引用           ↔ 外键
对象集合           ↔ 一对多或多对多关系
继承关系           ↔ 单表、连接表等继承映射策略
```

示例：

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username;
}
```

### JPA 与 Hibernate 的 API 对应

```text
JPA                         Hibernate 原生 API
EntityManagerFactory        SessionFactory
EntityManager               Session
JPQL                        HQL
jakarta.persistence 注解    Hibernate 扩展注解与能力
```

### 易错点

- JPA 不是一个具体 ORM 产品，而是一套规范。
- Hibernate 不只等于 JPA，它也有自己的原生 API 和扩展能力。
- Spring Data JPA 也不是 JPA 实现，它是在 JPA 之上的 Repository 抽象，底层仍需要 Hibernate 等 Provider。
- ORM 不代表完全不需要理解 SQL、索引、事务和数据库执行计划。

---

## 2. Hibernate 和 MyBatis 有什么区别？

### 面试回答

Hibernate 是完整 ORM，更强调对象模型、实体关系和持久化上下文，通常由框架根据实体映射生成 SQL，并支持实体状态管理、脏检查和关联加载。MyBatis 是 SQL 映射框架，更强调开发者显式编写和控制 SQL，再把查询结果映射成 Java 对象。

Hibernate 更适合领域模型清晰、实体关系较稳定、希望减少普通 CRUD 代码的场景；MyBatis 更适合 SQL 复杂、报表较多、需要精细控制 SQL 和数据库特性的场景。二者没有绝对优劣，应根据业务和团队能力选择。

### 主要区别

Hibernate：

- 是完整 ORM。
- 关注实体、关系、生命周期和持久化上下文。
- 常规 CRUD 通常不需要手写 SQL。
- 支持脏检查，修改受管理实体后可以自动产生 UPDATE。
- 支持关联关系、级联、延迟加载和一级、二级缓存。
- 复杂查询需要理解 JPQL/HQL、Criteria 或原生 SQL。
- 容易出现意外 SQL、N+1、懒加载和关联抓取问题。

MyBatis：

- 是 SQL 映射框架，不是完整 ORM。
- 开发者通常显式编写 SQL 或使用生成器。
- SQL 执行行为更直观、更容易精细优化。
- 不提供 Hibernate 式的实体生命周期和自动脏检查。
- 关联查询通常通过 JOIN、嵌套查询或手动组装完成。
- 更依赖开发者的 SQL、索引和数据库知识。

### 结合 mall 项目

当前项目使用 MyBatis。品牌创建的调用链为：

```text
PmsBrandController
→ PmsBrandServiceImpl
→ PmsBrandMapper.insertSelective()
→ SQL
```

Service 必须显式调用 Mapper 执行新增或更新：

```java
return brandMapper.insertSelective(pmsBrand);
```

代码见 [`PmsBrandServiceImpl`](../../mall/mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java)。

如果使用 Hibernate，事务中查询得到的受管理实体发生变化后，可能不需要显式调用 `update()`，Hibernate 会通过脏检查生成 UPDATE。

### 易错点

- 不要简单说 Hibernate 一定慢、MyBatis 一定快，性能取决于 SQL、映射、抓取策略、缓存和使用方式。
- MyBatis 也有一级、二级缓存，但它与 Hibernate 的持久化上下文不是同一个概念。
- Hibernate 同样允许使用原生 SQL，MyBatis 也可以封装通用 CRUD。

---

## 3. Session 与 SessionFactory 有什么区别？

### 面试回答

`SessionFactory` 是重量级、线程安全、通常全局共享的工厂对象，负责保存实体映射和数据库配置并创建 `Session`，还可以承载二级缓存。`Session` 是轻量级、非线程安全的工作单元，代表一次持久化上下文，负责实体查询、保存、删除、脏检查和一级缓存，通常与一个事务或一次业务操作绑定。

### SessionFactory

主要特点：

- 创建成本高。
- 通常一个数据库配置对应一个实例。
- 应用启动时创建，应用关闭时销毁。
- 线程安全，可以被多个线程共享。
- 用于创建 `Session`。
- 二级缓存通常位于 `SessionFactory` 范围。

```java
Session session = sessionFactory.openSession();
```

### Session

主要特点：

- 创建成本相对较低。
- 非线程安全，不能在多个并发线程间共享。
- 代表一个持久化上下文。
- 管理实体状态和一级缓存。
- 执行查询、持久化、删除、flush 等操作。
- 使用完应关闭；在 Spring 中通常由事务管理器管理。

### JPA 对应关系

```text
Hibernate SessionFactory ≈ JPA EntityManagerFactory
Hibernate Session        ≈ JPA EntityManager
```

### 易错点

- 不要把一个 `Session` 做成全局单例。
- `Session` 不是数据库物理连接本身，但执行 SQL 时会通过连接管理机制获得数据库连接。
- Session 生命周期过长会积累大量受管理实体，导致内存占用和脏检查成本增加。

---

## 4. Hibernate 实体有哪四种状态？

### 面试回答

Hibernate 实体常分为四种状态：Transient、Persistent/Managed、Detached 和 Removed。

- Transient：新创建的普通对象，没有持久化标识或尚未被持久化上下文管理。
- Managed/Persistent：正在被当前持久化上下文管理，对它的修改可以被脏检查检测。
- Detached：曾经被管理，但当前已经脱离持久化上下文。
- Removed：已在持久化上下文中被标记为删除，通常会在 flush 时执行 DELETE。

### 状态转换示例

```java
User user = new User();          // Transient

entityManager.persist(user);     // Managed

entityManager.detach(user);      // Detached

User managed = entityManager.merge(user); // managed 是 Managed

entityManager.remove(managed);   // Removed
```

关闭 `EntityManager` 或执行 `clear()` 后，原本受管理的实体通常会变成 Detached。

### 重要细节

`merge()` 不会把传入对象本身变成 Managed，而是把它的状态复制到一个受管理实例，并返回这个受管理实例：

```java
User detached = ...;
User managed = entityManager.merge(detached);

System.out.println(detached == managed); // 通常是 false
```

### 易错点

- Managed 实体才会参与自动脏检查。
- Detached 对象修改后不会自动更新数据库。
- Removed 对象仍可能处于持久化上下文中，只是已被标记为待删除。
- “是否有主键值”不能单独决定实体是否 Managed，关键是它是否由当前持久化上下文管理。

---

## 5. `persist`、`merge`、`remove` 有什么作用？

### 面试回答

- `persist()` 用于把新实体加入持久化上下文，使其从 Transient 变为 Managed，插入 SQL 可能立即执行，也可能延迟到 flush。
- `merge()` 把传入对象的状态复制到一个受管理实例，并返回这个受管理实例；传入对象本身不会因此变成 Managed。
- `remove()` 把受管理实体标记为 Removed，DELETE 通常在 flush 时执行。

### `persist()`

```java
User user = new User();
user.setUsername("tom");

entityManager.persist(user);
```

要点：

- 主要用于新增实体。
- 方法返回值是 `void`。
- 调用后实体进入 Managed 状态。
- 如果主键由数据库生成，主键获得时机取决于生成策略和 flush 行为。

### `merge()`

```java
User detached = ...;
User managed = entityManager.merge(detached);
```

要点：

- 常用于合并 Detached 实体状态，也可以处理其他状态，但语义要谨慎。
- 返回值才是受管理实体。
- 传入对象仍可能是 Detached。
- 不应把 `merge()` 简单理解成“让原对象重新托管”。

### `remove()`

```java
User user = entityManager.find(User.class, id);
entityManager.remove(user);
```

要点：

- 通常要求传入当前持久化上下文中的 Managed 实体。
- 调用后标记为 Removed。
- 真正 DELETE 一般在 flush 时执行。
- 关联实体是否一起删除由级联配置和数据库约束共同决定。

### 易错点

- `persist()`、`remove()` 不等于已经提交事务。
- `merge()` 返回的新引用非常重要。
- 不要为更新一个已处于 Managed 状态的实体重复调用 `merge()`。

---

## 6. 一级缓存与二级缓存有什么区别？

### 面试回答

一级缓存属于 `Session` 或持久化上下文范围，默认存在，用于保证同一持久化上下文内实体身份一致，并减少同一主键的重复查询。二级缓存属于 `SessionFactory` 范围，需要额外配置缓存提供者和实体缓存策略，可以让多个 Session 复用实体数据。

### 一级缓存

```java
User a = entityManager.find(User.class, 1L);
User b = entityManager.find(User.class, 1L);

System.out.println(a == b); // 通常为 true
```

在同一个持久化上下文中，第二次按相同实体类型和主键查询时，通常可以直接返回已管理实例。

特点：

- Session/EntityManager 级别。
- 默认存在，是持久化上下文语义的一部分。
- 生命周期通常与持久化上下文一致。
- `clear()`、`detach()`、`evict()` 等操作会影响缓存中的管理状态。

### 二级缓存

特点：

- SessionFactory/EntityManagerFactory 级别。
- 可以跨 Session 复用。
- 需要缓存提供者和缓存策略。
- 适合读多写少、变化较少的数据。
- 必须考虑缓存一致性、并发策略和集群环境。

### 查询缓存

查询缓存与二级实体缓存不是同一概念。查询缓存通常缓存查询结果中的标识或标量结果；要高效复用实体查询结果，往往还需要配合二级实体缓存。

### 易错点

- 一级缓存不是简单的通用 Map，它也是实体身份管理和脏检查的基础。
- 开启二级缓存不代表所有实体和查询都会自动缓存。
- 高频变化的数据不一定适合二级缓存。
- 缓存不能替代正确的索引和查询设计。

---

## 7. 脏检查机制如何实现自动更新？

### 面试回答

脏检查是 Hibernate 对 Managed 实体状态变化的检测机制。实体进入持久化上下文时，Hibernate 会保存用于比较的状态快照，或者使用字节码增强记录属性变化；flush 时比较实体当前状态与原状态，发现字段变化后生成并执行相应 UPDATE SQL。因此事务中的受管理实体修改属性后，通常不需要显式调用 `update()`。

### 示例

```java
@Transactional
public void changeUsername(Long id, String newName) {
    User user = entityManager.find(User.class, id);
    user.setUsername(newName);
}
```

虽然没有显式调用：

```java
entityManager.update(...);
```

但 `user` 是 Managed 实体。事务提交前 flush 时，Hibernate 检测到 `username` 变化并生成类似 SQL：

```sql
UPDATE users
SET username = ?
WHERE id = ?;
```

### 自动更新的必要条件

- 实体处于 Managed 状态。
- 修改发生在有效持久化上下文中。
- 事务正常提交，或主动执行 flush。
- 映射字段可更新。
- 事务没有被回滚。

### 可能的实现方式

- 状态快照比较：flush 时比较当前属性和原快照。
- 字节码增强：实体属性变化时记录哪些字段被修改，提高检测效率。

### 易错点

- Detached 实体修改不会自动持久化。
- Dirty Checking 表示发现变化；flush 表示把变化同步为 SQL；commit 表示提交数据库事务，三者不是同一件事。
- 生成 UPDATE 不等于事务已经提交，之后仍可能回滚。

---

## 8. `flush` 和 `commit` 有什么区别？

### 面试回答

`flush` 是把持久化上下文中待处理的新增、修改、删除同步为 SQL 并发送到数据库，但不结束也不提交事务；`commit` 是提交数据库事务，使事务修改正式生效。事务提交前通常会自动触发 flush，但 flush 后仍然可以回滚。

### 示例

```java
transaction.begin();

User user = new User();
entityManager.persist(user);

entityManager.flush(); // 执行 INSERT，但事务还没有提交

transaction.rollback(); // INSERT 仍会被回滚
```

### flush 可能在什么时候发生？

- 显式调用 `flush()`。
- 事务 `commit()` 之前。
- 某些查询执行之前，为保证查询能看到当前事务中的待同步变更。
- 由 FlushMode 决定的其他时机。

### 为什么需要手动 flush？

- 希望提前发现唯一约束、外键约束等数据库错误。
- 后续数据库查询或存储过程必须看到当前待同步变更。
- 大批量处理中分批执行 `flush()` 和 `clear()`，控制持久化上下文大小。

### 易错点

- `flush()` 不等于 `commit()`。
- flush 后 SQL 可能已发送到数据库，但事务仍可回滚。
- commit 通常会触发 flush，但如果 flush 或数据库提交失败，事务仍不能成功完成。

---

## 9. Lazy 和 Eager 有什么区别？

### 面试回答

Lazy 表示延迟加载，关联数据在真正访问时才尝试加载；Eager 表示急切加载，加载当前实体时关联数据也必须在当前加载计划中被获取。Lazy 可以避免无意义查询，但可能导致 N+1 或持久化上下文关闭后的懒加载异常；Eager 使用简单但容易产生过量查询和不可控的数据抓取。

### 示例

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id")
private User user;
```

查询订单时，`user` 可能先表现为代理对象；真正访问：

```java
order.getUser().getUsername();
```

才触发用户查询。

### JPA 默认抓取策略

常见默认值：

```text
@ManyToOne   默认 EAGER
@OneToOne    默认 EAGER
@OneToMany   默认 LAZY
@ManyToMany  默认 LAZY
```

实践中经常将 `@ManyToOne`、`@OneToOne` 也显式设置为 LAZY，再根据具体用例使用 `JOIN FETCH`、EntityGraph 或 DTO 投影控制查询。

### 易错点

- LAZY 是加载提示和映射策略，实际是否额外发送 SQL 还与查询方式、会话状态和 Hibernate 实现有关。
- EAGER 不保证一定用一条 JOIN SQL，也可能产生额外查询。
- 不要为了避免 `LazyInitializationException` 就把所有关联都改成 EAGER。
- 最好的策略通常是默认谨慎加载，再为具体接口定义明确的 Fetch Plan。

---

## 10. 什么是 N+1 查询问题？如何解决？

### 面试回答

N+1 是指先执行 1 条 SQL 查询一批主实体，随后访问每个主实体的关联属性时，又执行 N 条关联查询，最终产生 1+N 次数据库访问。它会增加网络往返、数据库压力和接口延迟。

常见解决方式包括 `JOIN FETCH`、EntityGraph、批量抓取、DTO 投影以及重新设计查询；具体选择要结合分页、集合大小和返回字段，不能简单把所有关系改成 EAGER。

### 示例

```java
List<Order> orders = entityManager
        .createQuery("select o from Order o", Order.class)
        .getResultList();

for (Order order : orders) {
    System.out.println(order.getUser().getUsername());
}
```

可能产生：

```text
1 条 SQL：查询 N 个订单
N 条 SQL：分别查询每个订单对应的用户
```

如果多个订单属于同一个用户，一级缓存可能减少部分查询，但仍不能依赖这种偶然情况解决问题。

### 解决方法一：JOIN FETCH

```java
select o
from Order o
join fetch o.user
where o.status = :status
```

在一次查询中获取订单和用户。

### 解决方法二：EntityGraph

```java
@EntityGraph(attributePaths = "user")
List<Order> findByStatus(OrderStatus status);
```

把抓取计划与实体默认映射分开。

### 解决方法三：批量抓取

可以使用 Hibernate Batch Fetching，使多个延迟关联通过 `IN (...)` 分批加载，而不是逐条查询。

### 解决方法四：DTO 投影

如果接口只需要订单号和用户名，可以直接查询需要的字段：

```java
select new com.example.OrderSummary(o.id, u.username)
from Order o
join o.user u
```

这样可以减少实体和无关字段加载。

### 注意事项

- `JOIN FETCH` 一对多集合与分页组合时可能导致内存分页、重复行或统计错误，应谨慎设计。
- 同时抓取多个集合可能产生笛卡尔积，Hibernate 对某些多个 bag 抓取还会拒绝执行。
- 不要把所有关系改成 EAGER，这可能把 N+1 变成更隐蔽的过量查询。
- 排查时应查看实际 SQL数量，而不是只看 Java 代码。

---

## 11. 一对多、多对多关系应该怎么映射？

### 一对多：用户与订单

一个用户可以有多个订单，一个订单只属于一个用户。数据库外键通常放在“多”的一方，也就是 `orders.user_id`。

用户实体：

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(
        mappedBy = "user",
        cascade = CascadeType.ALL,
        orphanRemoval = true
    )
    private List<Order> orders = new ArrayList<>();

    public void addOrder(Order order) {
        orders.add(order);
        order.setUser(this);
    }

    public void removeOrder(Order order) {
        orders.remove(order);
        order.setUser(null);
    }
}
```

订单实体：

```java
@Entity
@Table(name = "orders")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}
```

其中：

- `Order.user` 是维护外键的一方，也称 owning side。
- `User.orders` 使用 `mappedBy = "user"`，表示关系由 `Order.user` 维护。
- 双向关联应该通过辅助方法同时维护两端内存状态。

是否使用 `CascadeType.ALL` 和 `orphanRemoval = true` 必须根据聚合生命周期决定，不能机械复制。

### 多对多：学生与课程

简单映射可以使用中间表：

```java
@ManyToMany
@JoinTable(
    name = "student_course",
    joinColumns = @JoinColumn(name = "student_id"),
    inverseJoinColumns = @JoinColumn(name = "course_id")
)
private Set<Course> courses = new HashSet<>();
```

另一端：

```java
@ManyToMany(mappedBy = "courses")
private Set<Student> students = new HashSet<>();
```

### 为什么业务项目常用中间实体？

如果关系自身存在属性，例如选课时间、成绩、状态，就应该把中间表建模成实体：

```text
Student
  ↓ one-to-many
Enrollment
  ↑ many-to-one
Course
```

`Enrollment` 可以包含：

- `student_id`
- `course_id`
- `enrolled_at`
- `score`
- `status`

这种设计比直接 `@ManyToMany` 更容易扩展、审计和控制级联。

### 易错点

- 一对多外键通常位于“多”的一方。
- 双向关系必须明确 owning side，`mappedBy` 一方不直接维护外键。
- 不要在多对多关系两端随意配置 `CascadeType.REMOVE`，否则可能误删共享实体。
- 实体的 `equals()`、`hashCode()` 和集合类型需要谨慎设计，避免使用可变字段导致集合行为异常。

---

## 12. CascadeType 和 FetchType 有什么区别？

### 面试回答

`CascadeType` 控制对当前实体执行持久化操作时，操作是否传播到关联实体；`FetchType` 控制查询实体时，关联数据什么时候加载。一个控制“操作传播”，一个控制“数据加载”，二者没有包含关系。

### CascadeType

常见类型：

- `PERSIST`：持久化当前实体时级联持久化关联实体。
- `MERGE`：合并当前实体时级联合并关联实体。
- `REMOVE`：删除当前实体时级联删除关联实体。
- `REFRESH`：刷新当前实体时级联刷新关联实体。
- `DETACH`：分离当前实体时级联分离关联实体。
- `ALL`：包含全部级联操作。

示例：

```java
@OneToMany(mappedBy = "user", cascade = CascadeType.PERSIST)
private List<Order> orders;
```

持久化 User 时，新建的 Order 也可以被级联持久化。

### FetchType

只有两类：

- `LAZY`：需要时再加载。
- `EAGER`：加载当前实体时关联也必须被获取。

示例：

```java
@ManyToOne(fetch = FetchType.LAZY)
private User user;
```

### 必须区分的概念

```text
Cascade：保存、合并、删除等操作要不要传递。
Fetch：查询时关联数据什么时候加载。
```

`orphanRemoval = true` 也不完全等于 `CascadeType.REMOVE`：前者通常表示子实体从父实体集合中移除后将作为孤儿删除；后者表示删除父实体时把删除操作传播给子实体。

---

## 13. HQL、JPQL、SQL 有什么区别？

### 面试回答

SQL 面向数据库表和列，由数据库直接执行；JPQL 是 JPA 标准查询语言，面向实体类和实体属性；HQL 是 Hibernate 的对象查询语言，与 JPQL 很相似，但支持一些 Hibernate 扩展。JPQL/HQL 最终会由 ORM 根据映射和数据库方言转换成 SQL。

### SQL

```sql
SELECT o.id, o.total_amount
FROM orders o
WHERE o.user_id = ?;
```

特点：

- 面向表、列、JOIN、索引和数据库函数。
- 由数据库执行。
- 可以充分使用数据库特有能力。
- 数据库可移植性可能较弱。

### JPQL

```java
select o
from Order o
where o.user.id = :userId
```

特点：

- 面向实体类 `Order` 和属性 `user.id`。
- 是 JPA 标准。
- 支持实体关联导航。
- 最终由 JPA Provider 转换为 SQL。

### HQL

```java
from Order o
where o.user.id = :userId
```

特点：

- Hibernate 提供。
- 大量语法与 JPQL 相同。
- 支持 Hibernate 特有的函数和扩展语法。

### 易错点

- JPQL/HQL 中通常写实体名和属性名，不是表名和列名。
- JPQL 不是数据库直接执行的语言。
- 原生 SQL 返回结果如果需要映射实体或 DTO，可能需要额外结果映射。
- 使用 JPQL 不代表生成的 SQL 一定高效，仍应查看实际 SQL 和执行计划。

---

## 14. 什么是乐观锁和悲观锁？

### 面试回答

乐观锁假设并发冲突较少，读取时不长期加排他锁，更新时通过版本号或条件更新判断数据是否已被其他事务修改；冲突时更新失败，应用进行提示或重试。悲观锁假设冲突较多，读取数据时就申请数据库锁，阻止其他事务同时修改，直到当前事务提交或回滚。

### 乐观锁

JPA 常使用 `@Version`：

```java
@Entity
public class ProductStock {

    @Id
    private Long productId;

    private Integer stock;

    @Version
    private Long version;
}
```

Hibernate 更新时会生成类似：

```sql
UPDATE product_stock
SET stock = ?, version = version + 1
WHERE product_id = ?
  AND version = ?;
```

如果影响行数为 0，说明版本已经变化，通常抛出乐观锁异常。

优点：

- 没有长期持有数据库排他锁。
- 吞吐量通常较高。
- 适合读多写少、冲突较低的场景。

缺点：

- 冲突发生后需要重试或提示。
- 高冲突场景下大量失败重试可能降低性能。

### 悲观锁

```java
ProductStock stock = entityManager.find(
        ProductStock.class,
        productId,
        LockModeType.PESSIMISTIC_WRITE
);
```

数据库通常产生类似：

```sql
SELECT ...
FROM product_stock
WHERE product_id = ?
FOR UPDATE;
```

优点：

- 能在事务期间阻止其他事务修改同一数据。
- 高冲突且逻辑必须串行时更容易保证一致性。

缺点：

- 增加锁等待、超时和死锁风险。
- 事务必须尽量短。
- 吞吐量可能下降。

### 选择原则

- 读多写少、冲突低：优先考虑乐观锁。
- 冲突高、临界区短、失败成本高：可以考虑悲观锁。
- 简单库存扣减：数据库原子条件更新通常比“先查后改”更直接。

---

## 15. 什么是 LazyInitializationException？

### 面试回答

`LazyInitializationException` 表示程序访问延迟加载的代理或集合时，对应的 Hibernate Session 或持久化上下文已经关闭，Hibernate 无法再执行 SQL 初始化关联数据。

### 典型示例

```java
public Order findOrder(Long id) {
    return orderRepository.findById(id).orElseThrow();
}
```

如果 `Order.user` 是 LAZY，并且离开事务后执行：

```java
order.getUser().getUsername();
```

此时持久化上下文已经关闭，就可能发生：

```text
LazyInitializationException:
could not initialize proxy - no Session
```

### 推荐解决方式

- 在 Service 事务内完成需要的数据访问和 DTO 转换。
- 使用 `JOIN FETCH` 查询该用例需要的关联。
- 使用 EntityGraph 声明抓取计划。
- 使用 DTO Projection 直接查询接口需要的字段。
- 对批量关联读取使用合理的 Batch Fetching。

示例：

```java
@Transactional(readOnly = true)
public OrderDetailResponse getOrder(Long id) {
    Order order = orderRepository.findDetailById(id)
            .orElseThrow();

    return OrderDetailResponse.from(order);
}
```

### 不推荐的简单处理

- 把所有关联都改成 EAGER。
- 在 Controller 中随意访问延迟关联并依赖 Open Session in View。
- 捕获 `LazyInitializationException` 后返回空数据。

Open Session in View 可以让持久化上下文延续到 Web 层，但可能导致 Controller 或序列化阶段产生不可控 SQL，是否开启应根据团队架构明确决定。

---

# 综合应用

## 16. 设计用户和订单的关系数据库及实体映射

### 关系设计

一个用户可以拥有多个订单，一个订单只能属于一个用户，因此是“一对多/多对一”。外键应该放在订单表。

数据库表示例：

```sql
CREATE TABLE users (
    id          BIGINT PRIMARY KEY AUTO_INCREMENT,
    username    VARCHAR(64) NOT NULL,
    email       VARCHAR(128) NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_users_username UNIQUE (username),
    CONSTRAINT uk_users_email UNIQUE (email)
);

CREATE TABLE orders (
    id            BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_no      VARCHAR(64) NOT NULL,
    user_id       BIGINT NOT NULL,
    status        VARCHAR(32) NOT NULL,
    total_amount  DECIMAL(18, 2) NOT NULL,
    version       BIGINT NOT NULL DEFAULT 0,
    created_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_orders_order_no UNIQUE (order_no),
    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE INDEX idx_orders_user_created
    ON orders(user_id, created_at);
```

设计要点：

- 不使用 `user`、`order` 等可能与数据库关键字冲突的单数表名。
- 金额使用 `DECIMAL`，Java 使用 `BigDecimal`，不要使用 `double`。
- `orders.user_id` 建立外键和索引。
- 经常按用户和时间查询时，可建立 `(user_id, created_at)` 联合索引。
- `order_no` 使用唯一约束保证业务唯一性。

### User 实体

```java
@Entity
@Table(
    name = "users",
    uniqueConstraints = {
        @UniqueConstraint(name = "uk_users_username", columnNames = "username"),
        @UniqueConstraint(name = "uk_users_email", columnNames = "email")
    }
)
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 64)
    private String username;

    @Column(nullable = false, length = 128)
    private String email;

    @Column(name = "created_at", nullable = false, updatable = false)
    private Instant createdAt;

    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<Order> orders = new ArrayList<>();
}
```

### Order 实体

```java
@Entity
@Table(
    name = "orders",
    indexes = @Index(
        name = "idx_orders_user_created",
        columnList = "user_id, created_at"
    )
)
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "order_no", nullable = false, unique = true)
    private String orderNo;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 32)
    private OrderStatus status;

    @Column(name = "total_amount", nullable = false, precision = 18, scale = 2)
    private BigDecimal totalAmount;

    @Version
    private Long version;

    @Column(name = "created_at", nullable = false, updatable = false)
    private Instant createdAt;
}
```

这里没有默认给 `User.orders` 配置 `CascadeType.ALL`，因为用户和订单的生命周期是否完全一致需要根据业务决定。真实电商系统通常不能因为删除用户就物理删除全部订单。

---

## 17. 实现一个新增用户的 REST API

### 请求 DTO

不要直接把 Entity 作为 API 请求对象：

```java
public record CreateUserRequest(
        @NotBlank
        @Size(max = 64)
        String username,

        @NotBlank
        @Email
        @Size(max = 128)
        String email
) {
}
```

### 响应 DTO

```java
public record UserResponse(
        Long id,
        String username,
        String email,
        Instant createdAt
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getId(),
                user.getUsername(),
                user.getEmail(),
                user.getCreatedAt()
        );
    }
}
```

### Repository

```java
public interface UserRepository extends JpaRepository<User, Long> {
    boolean existsByUsername(String username);
    boolean existsByEmail(String email);
}
```

### Service

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public UserResponse create(CreateUserRequest request) {
        if (userRepository.existsByUsername(request.username())) {
            throw new BusinessException("用户名已存在");
        }
        if (userRepository.existsByEmail(request.email())) {
            throw new BusinessException("邮箱已存在");
        }

        User user = new User();
        user.setUsername(request.username());
        user.setEmail(request.email());
        user.setCreatedAt(Instant.now());

        userRepository.save(user);
        return UserResponse.from(user);
    }
}
```

数据库唯一约束仍然必须保留，因为“先查询是否存在，再插入”在并发场景下仍存在竞争窗口。Service 需要把唯一约束冲突转换成明确的业务错误。

### Controller

```java
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping
    public ResponseEntity<UserResponse> create(
            @Valid @RequestBody CreateUserRequest request) {

        UserResponse response = userService.create(request);
        URI location = URI.create("/users/" + response.id());

        return ResponseEntity.created(location).body(response);
    }
}
```

REST 语义：

- 创建成功返回 `201 Created`。
- `Location` 指向新资源地址。
- 参数校验失败返回 400。
- 用户名或邮箱冲突可返回 409 Conflict。

---

## 18. 实现按用户 ID 查询所有订单的接口

数据量可能增长，因此实际接口应优先分页，而不是无条件返回“所有”订单。

### 响应 DTO

```java
public record OrderSummaryResponse(
        Long id,
        String orderNo,
        OrderStatus status,
        BigDecimal totalAmount,
        Instant createdAt
) {
}
```

### Repository DTO 投影

```java
public interface OrderRepository extends JpaRepository<Order, Long> {

    @Query("""
        select new com.example.api.OrderSummaryResponse(
            o.id,
            o.orderNo,
            o.status,
            o.totalAmount,
            o.createdAt
        )
        from Order o
        where o.user.id = :userId
        order by o.createdAt desc
        """)
    Page<OrderSummaryResponse> findSummariesByUserId(
            @Param("userId") Long userId,
            Pageable pageable
    );
}
```

使用 DTO Projection 可以避免加载不需要的实体字段和关联，也避免 Controller 序列化实体图。

### Service

```java
@Service
public class OrderQueryService {

    private final UserRepository userRepository;
    private final OrderRepository orderRepository;

    public OrderQueryService(
            UserRepository userRepository,
            OrderRepository orderRepository) {
        this.userRepository = userRepository;
        this.orderRepository = orderRepository;
    }

    @Transactional(readOnly = true)
    public Page<OrderSummaryResponse> findByUserId(
            Long userId,
            Pageable pageable) {

        if (!userRepository.existsById(userId)) {
            throw new ResourceNotFoundException("用户不存在");
        }

        return orderRepository.findSummariesByUserId(userId, pageable);
    }
}
```

### Controller

```java
@GetMapping("/users/{userId}/orders")
public Page<OrderSummaryResponse> findOrders(
        @PathVariable Long userId,
        @PageableDefault(size = 20) Pageable pageable) {

    return orderQueryService.findByUserId(userId, pageable);
}
```

### 面试追问

如果只需要订单列表，不要为了获得用户名就把完整 `User.orders` 集合序列化出去。查询应围绕接口所需字段设计，并结合分页与索引。

---

## 19. 用户订单查询很慢，你会怎么排查？

### 面试回答

我会先定位慢在哪一层，再从 SQL 数量、单条 SQL 执行计划、索引、数据量、关联抓取、分页、锁等待、连接池和序列化等方面逐层排查，而不是一开始就盲目加缓存。

### 第一步：确认问题边界

- 只慢一个接口还是整个系统都慢？
- 平均耗时、P95、P99 分别是多少？
- 是持续慢还是高峰期慢？
- 数据库耗时、应用耗时、网络耗时分别多少？
- 同一个用户订单量是否异常大？

使用 APM、链路追踪、接口日志和数据库慢查询日志定位耗时区间。

### 第二步：查看实际 SQL

- 开启受控的 Hibernate SQL/统计信息或使用数据源代理。
- 确认一次接口到底执行了多少条 SQL。
- 检查是否存在 N+1。
- 检查是否重复查询同一数据。
- 检查是否意外加载了订单明细、商品、用户等大对象图。

### 第三步：分析执行计划

对慢 SQL 使用数据库 `EXPLAIN` 或 `EXPLAIN ANALYZE`，检查：

- 是否使用正确索引。
- 是否发生全表扫描。
- 扫描行数与返回行数是否相差过大。
- JOIN 顺序是否合理。
- 是否发生临时表或文件排序。
- 条件中是否对索引列使用函数或隐式类型转换。

对于：

```sql
SELECT ...
FROM orders
WHERE user_id = ?
ORDER BY created_at DESC
LIMIT ?, ?;
```

通常可以考虑：

```sql
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at);
```

但最终要根据真实查询条件和执行计划决定。

### 第四步：检查分页方式

- 是否一次返回几万条订单？
- 深分页 `OFFSET` 是否越来越慢？
- 是否可以使用基于 `created_at`、`id` 的游标分页？
- count 查询是否成为瓶颈？

### 第五步：检查 ORM 抓取策略

- 是否发生 N+1？
- 是否因为 EAGER 加载无关关联？
- 是否在 JSON 序列化阶段触发懒加载？
- 是否对一对多集合使用了不合适的 fetch join 和分页？
- 是否应该改用 DTO Projection？

### 第六步：检查数据库运行状态

- 锁等待和死锁。
- CPU、内存、磁盘 IO。
- 缓冲池命中率。
- 连接池是否耗尽。
- 长事务是否占锁。
- 主从延迟或网络延迟。

### 第七步：最后考虑缓存和架构优化

如果数据读多写少且允许一定一致性延迟，可以考虑：

- 缓存热点订单摘要。
- 预计算统计数据。
- 读写分离。
- 历史订单归档或分区。
- 搜索场景使用适合的检索存储。

缓存不能替代错误 SQL、缺失索引和 N+1 修复。

---

## 20. 并发修改订单库存应该怎么处理？

### 面试回答

库存扣减的核心是保证“检查库存”和“扣减库存”的原子性，避免先查询库存再无条件更新。对于单库库存，可以优先使用带库存条件的原子 UPDATE，根据影响行数判断是否扣减成功；如果业务需要读取并修改复杂实体，可以使用 `@Version` 乐观锁并进行有限重试；冲突非常高且临界区较短时可以使用悲观锁。无论选择哪种方案，都要配合事务、幂等设计和失败补偿。

### 推荐方案一：数据库原子条件更新

```sql
UPDATE product_stock
SET stock = stock - :quantity
WHERE product_id = :productId
  AND stock >= :quantity;
```

判断影响行数：

```text
影响 1 行：扣减成功
影响 0 行：库存不足或商品不存在
```

这种方式把库存检查和扣减放在一条 SQL 中，可以避免典型的“先查后改”竞争窗口。

### 方案二：乐观锁

```java
@Version
private Long version;
```

更新时带上原版本号。如果其他事务已经修改库存，当前更新影响行数为 0，并产生乐观锁冲突。应用可以：

- 返回并发冲突提示。
- 在明确安全的前提下有限次数重试。
- 重新读取最新库存再判断。

重试必须有次数限制、退避策略和幂等保障，不能无限重试。

### 方案三：悲观锁

```java
@Lock(LockModeType.PESSIMISTIC_WRITE)
@Query("select s from ProductStock s where s.productId = :productId")
Optional<ProductStock> findForUpdate(@Param("productId") Long productId);
```

事务中先获得行锁，再检查和扣减库存。适合高冲突、必须串行处理且事务很短的场景，但要注意锁等待、超时和死锁。

### 分布式业务还要考虑

- 请求幂等键，防止重复下单、重复扣减。
- 订单创建与库存扣减的一致性。
- 本地事务、事务消息、Outbox 或 Saga 等方案。
- 超时取消订单后的库存回补。
- 消息重复消费与去重。
- 数据库唯一约束或业务流水表。

不要只说“加 Redis 分布式锁”。分布式锁不能自动解决数据库事务、消息一致性、锁失效和重复请求问题，应在明确需要跨进程互斥时再使用。

---

## 21. 哪些逻辑应放在 Controller、Service、DAO 中？

### 面试回答

Controller 负责 HTTP 协议适配，Service 负责业务用例和事务边界，DAO/Repository 负责数据持久化。Controller 应保持轻薄，不直接编写 SQL；Service 不应依赖 HTTP 请求细节；DAO 不应承载业务流程。

### Controller 应负责

- URL 和 HTTP 方法映射。
- 接收 `@RequestParam`、`@PathVariable`、`@RequestBody`。
- 触发基础参数校验。
- 调用 Service。
- 将结果转换为 HTTP 状态、响应头和响应 DTO。

不应该负责：

- 复杂业务判断。
- 开启和控制核心业务事务。
- 直接调用多个 Mapper 拼业务流程。
- 直接编写 SQL。

### Service 应负责

- 实现一个完整业务用例。
- 业务规则和状态流转。
- 编排多个 Repository、Mapper 或外部服务。
- 定义事务边界。
- 并发控制、幂等和一致性策略。
- 将持久化模型转换成业务输出 DTO，或调用专门的 Mapper/Assembler。

示例：

```java
@Transactional
public OrderResponse createOrder(CreateOrderCommand command) {
    // 检查用户
    // 校验商品
    // 扣减库存
    // 计算金额
    // 创建订单
    // 记录操作
}
```

### DAO/Repository 应负责

- 实体或记录的查询、保存、更新、删除。
- 封装 JPQL、HQL、Criteria 或 SQL。
- 提供数据访问语义明确的方法。
- 对数据存储细节进行隔离。

不应该负责：

- HTTP 请求和响应。
- 跨多个业务模块的流程编排。
- 发送短信、组装页面跳转等业务行为。

### DTO、Entity 和领域对象

- Request DTO：承载客户端输入和接口级校验。
- Response DTO：定义稳定的 API 输出。
- Entity：映射数据库并参与持久化上下文管理。
- Domain Object：如果采用领域模型，可以承载与自身状态紧密相关的业务规则。

不建议直接把 JPA Entity 作为 API 响应，因为可能导致：

- 暴露数据库字段。
- JSON 序列化触发懒加载。
- 双向关联产生循环引用。
- API 与数据库结构强耦合。
- 客户端意外修改本不允许修改的字段。

### 结合 mall 项目

mall 项目目前的典型分层是：

```text
PmsBrandController
→ PmsBrandService / PmsBrandServiceImpl
→ PmsBrandMapper
→ MySQL
```

虽然底层是 MyBatis 而不是 Hibernate，但 Controller、Service、DAO/Mapper 的职责划分原则相同。

---

# 面试前最终速记

```text
ORM：对象和关系数据库之间的映射。
JPA 是规范，Hibernate 是实现。

SessionFactory：重量级、线程安全、创建 Session。
Session：轻量级、非线程安全、代表持久化上下文。

实体四状态：Transient、Managed、Detached、Removed。

persist：新实体进入 Managed。
merge：复制状态并返回 Managed 实例。
remove：标记删除。

一级缓存属于 Session；二级缓存属于 SessionFactory。

脏检查：Managed 实体变化，flush 时自动生成 UPDATE。

flush：同步 SQL，但不提交事务。
commit：提交事务，通常会先 flush。

LAZY：需要时加载。
EAGER：加载当前实体时关联必须被获取。

N+1：1 条主查询加 N 条关联查询。
解决：JOIN FETCH、EntityGraph、批量抓取、DTO 投影。

一对多外键放在多的一方；mappedBy 一方不维护外键。

Cascade 管操作传播；Fetch 管加载时机。

SQL 面向表；JPQL/HQL 面向实体。

乐观锁用版本号检测冲突；悲观锁提前持有数据库锁。

LazyInitializationException：访问懒加载属性时 Session 已关闭。

Controller 管 HTTP；Service 管业务和事务；DAO 管数据访问。
```

# 推荐复习顺序

1. 先掌握 ORM、JPA 与 Hibernate 的关系。
2. 掌握 Session、持久化上下文和实体四种状态。
3. 掌握 `persist`、`merge`、`remove`、脏检查、flush 和 commit。
4. 掌握实体关系、级联和加载策略。
5. 掌握 N+1、LazyInitializationException 和查询优化。
6. 掌握事务锁、库存并发和接口分层。
7. 最后结合 mall 项目的 MyBatis 代码比较两种持久化方式。

“重置进度”属于原复习页面的操作文字，不是 Hibernate 面试题，因此未单独作为问题整理。
