# Vue 3 阶段学习笔记：Router × Pinia × Props × Sidebar

> **本阶段学习目标**：读懂 Vue 3 后台系统中，路由配置如何变成左侧菜单，以及点击菜单后，哪个文件负责把目标 `.vue` 页面显示出来。
>
> **依据**：本次交流中用户实际提供的 `router/index.ts`、路由守卫、`stores/permission.ts`、`Layout.vue`、`AppMain.vue`、`Sidebar/index.vue`、`SidebarItem.vue`。未看到完整代码的 `main.ts`、`Navbar.vue`、`views/home/index.vue`、`stores/user` 等，只讨论可推断的职责，不捏造实现。

## 1. 先记住最重要的结论

- **Vue Router**：记录和匹配路由；管理导航；决定应渲染哪个 Vue 组件。
- **Pinia**：保存共享的路由配置、权限处理结果和 UI 状态，但**不是**负责 URL 跳转的路由管理器。
- **Props**：Vue 内置的父组件向子组件传数据的方式，**不是** Pinia 的功能。
- **SidebarItem**：把路由数组转成可以展开、点击的菜单。
- **Layout**：公共页面框架，包括侧边栏、顶部导航和业务内容区域。
- **AppMain**：固定容器，内部通过 `<router-view>` 显示不同的业务组件。

最容易混淆的三个名字：

| 名字 | 含义 | 典型来源 |
|---|---|---|
| `router` | Vue Router 实例，提供 `addRoute()`、`push()` 等 | `createRouter()` |
| `route` | 当前匹配的路由信息，如 `route.path` | `useRoute()` |
| `routes` | Sidebar 读取的菜单路由数组 | `computed(() => permissionStore.routers)` |

## 2. 全部文件如何连接？

```text
router/index.ts
  ├─ constantRouterMap：基础路由
  ├─ asyncRouterMap：业务路由候选集合
  └─ createRouter({ routes: constantRouterMap })：创建 Router 实例
                 │
                 ├─────────────────────────────────────────┐
                 ▼                                         ▼
stores/permission.ts                               导航守卫 beforeEach
  ├─ routers：基础+用户可访问的动态路由              ├─ 读取 userStore 的 token/menus
  ├─ addRouters：待注册的动态路由                   ├─ 调用 generateRoutes(...)
  └─ generateRoutes(...)：按权限筛选、排序            ├─ router.addRoute(...)
                 │                                 └─ next(...) 放行/重定向
                 ▼
Sidebar/index.vue
  ├─ permissionStore = usePermissionStore()
  ├─ routes = computed(() => permissionStore.routers)
  └─ <SidebarItem :routes="routes" />
                 │ Props：把数组从父组件交给子组件
                 ▼
SidebarItem.vue
  ├─ defineProps({ routes: ... })
  ├─ props.routes → filter() → v-for
  ├─ <el-sub-menu>：展开一级菜单
  └─ <router-link :to="...">：点击具体菜单后导航
                 │
                 ▼
Vue Router 匹配目标 URL，例如 /pms/product
  ├─ 父路由 /pms → Layout.vue
  └─ 子路由 product → views/pms/product/index.vue
                 │
                 ▼
Layout.vue
  ├─ Sidebar.vue（左侧菜单）
  ├─ Navbar.vue（顶部导航）
  └─ AppMain.vue → <router-view> → 动态显示业务组件
```

这是一张**协作和数据流图**，不是严格的同步函数执行次序。

---

## 3. 路由表：配置是怎么写出来的？

实际项目的 `router/index.ts` 有：

```ts
export const constantRouterMap: RouteRecordExt[] = [
  { path: '/404', component: () => import('@/views/normal/404/index.vue'), hidden: true },
  { path: '/login', component: () => import('@/views/normal/login/index.vue'), hidden: true },
  {
    path: '',
    component: Layout,
    redirect: '/home',
    meta: { title: '首页', icon: 'home' },
    children: [
      {
        path: 'home',
        name: 'home',
        component: () => import('@/views/home/index.vue'),
        meta: { title: '首页', icon: 'dashboard' }
      }
      // 另有 document、video 两条外部教程链接
    ]
  }
]

export const asyncRouterMap: RouteRecordExt[] = [
  // /pms（商品）、/oms（订单）、/sms（营销）、/ums（权限）等
]
```

| 字段 | 意义 |
|---|---|
| `path` | URL 路径，例如 `/pms`、`product` |
| `name` | 路由名称；这个项目的权限筛选会使用它 |
| `component` | URL 匹配时要显示的 Vue 组件 |
| `children` | 父子路由关系；**不是**所有子路由都在 `home` 里面 |
| `redirect` | 访问父路径时重定向 |
| `meta.title` | 提供菜单标题等元数据 |
| `meta.icon` | 提供菜单图标名等元数据 |
| `hidden` | 项目自定义的菜单隐藏标记；不是服务端权限 |
| `sort` / `alwaysShow` | 项目自定义的排序和显示控制 |

比如商品：

```ts
{
  path: '/pms',
  component: Layout,
  redirect: '/pms/product',
  name: 'pms',
  meta: { title: '商品', icon: 'product' },
  children: [
    {
      path: 'product',
      name: 'product',
      component: () => import('@/views/pms/product/index.vue'),
      meta: { title: '商品列表', icon: 'product-list' }
    }
  ]
}
```

当路由 `/pms/product` 已经注册且导航成功时，会匹配两个层级：

```text
/pms                 → Layout.vue（公共布局）
  └── product         → views/pms/product/index.vue（业务页面）
```

该文件的结尾是：

```ts
const router = createRouter({
  history: createWebHashHistory(),
  routes: constantRouterMap
})

export default router
```

所以 **`constantRouterMap` 已经作为初始路由交给 Vue Router**；但 `asyncRouterMap` 还需要以后动态注册。

**`export` 不是「自动交给 Pinia」**，它只是允许其他文件 `import` 这个变量。

---

## 4. 本阶段新发现：Pinia 中真正保存了什么？

我们现在已经拿到了真实的 `stores/permission.ts`：

```ts
import { defineStore } from 'pinia'
import { shallowRef } from 'vue'
import { asyncRouterMap, constantRouterMap } from '@/router/index'

export const usePermissionStore = defineStore('permission', () => {
  // 所有路由：基础 + 用户可访问的动态路由
  const routers = shallowRef(constantRouterMap)

  // 有权限访问的动态路由
  const addRouters = shallowRef<RouteRecordExt[]>([])

  const testMode = false

  const generateRoutes = (data: { menus: UmsMenu[]; username: string }) => {
    // 具体筛选与合并逻辑见下节
  }

  return { routers, addRouters, generateRoutes }
})

export default usePermissionStore
```

### 4.1 为什么 `usePermissionStore()` 能读取 Pinia？

因为它**确实由 Pinia 的 `defineStore()` 创建**：

```ts
export const usePermissionStore = defineStore('permission', () => { ... })
```

`defineStore()` 返回一个用于获取这个 Store 实例的函数。所以在组件中：

```ts
const permissionStore = usePermissionStore()
```

取得的是 `permission` Store 实例；然后才能访问它向外返回的成员：

```ts
permissionStore.routers
permissionStore.addRouters
permissionStore.generateRoutes(...)
```

不能因为一个普通函数名叫 `useSomethingStore()` 就断言它来自 Pinia；这一次我们有实际的 `defineStore` 源码作为依据。

### 4.2 `routers` 和 `addRouters` 的区别

| 字段 | 初始内容 | `generateRoutes()` 执行后 | 用途 |
|---|---|---|---|
| `routers` | `constantRouterMap` | `constantRouterMap.concat(accessedRouters)` | **Sidebar 生成菜单** |
| `addRouters` | `[]` | `accessedRouters` | **路由守卫调用 `router.addRoute()` 注册** |

这是整个项目设计中最重要的区分：

```text
Pinia 中有一份路由配置
          ≠
Vue Router 已经注册这份路由
```

只有调用 `router.addRoute(route)`，新动态路由才正式添加到 Vue Router。

### 4.3 为什么使用 `shallowRef()`？

`shallowRef()` 来自 **Vue**，不是 Pinia。它创建一个浅层响应式引用：

```ts
const routers = shallowRef(constantRouterMap)
```

在 Store 定义函数内部读写它时，要用 `.value`：

```ts
routers.value = constantRouterMap.concat(accessedRouters)
```

整体替换 `.value` 会触发响应式更新；但它不会自动深度追踪每一层嵌套对象的变化。

这个项目正好通过**替换数组**更新菜单数据。

### 4.4 为什么组件里不写 `.value`？

Pinia 对 Setup Store 返回的 Ref 做自动解包：

```ts
// Store 定义内部
routers.value = ...

// 组件中获取 Store 后
permissionStore.routers
```

但 Sidebar 另外创建的 `computed` 自身仍是 Ref：

```ts
const routes = computed(() => permissionStore.routers)

// 在 <script setup> 的脚本里
console.log(routes.value)

// 在模板里自动解包，不写 .value
// <SidebarItem :routes="routes" />
```

---

## 5. `generateRoutes()`：权限怎样筛选出路由？

用户提供的核心代码如下（保留真实逻辑）：

```ts
const generateRoutes = (data: { menus: UmsMenu[]; username: string }) => {
  const { menus, username } = data

  const accessedRouters = asyncRouterMap.filter(v => {
    if (testMode && username === 'admin') return true

    if (hasPermission(menus, v)) {
      if (v.children && v.children.length > 0) {
        v.children = v.children.filter(child => {
          if (hasPermission(menus, child)) return child
          return false
        })
        return v
      }
      return v
    }
    return false
  })

  sortRouters(accessedRouters)
  addRouters.value = accessedRouters
  routers.value = constantRouterMap.concat(accessedRouters)
}
```

这个函数依次做四件事：

1. **取得用户菜单信息**：`menus` 和 `username` 来自调用方，在你给出的守卫中来自 `userStore.userInfo`。
2. **按权限过滤**：只留下符合权限条件的动态父路由和子路由，得到 `accessedRouters`。
3. **排序**：`sortRouters(accessedRouters)`。
4. **保存结果**：动态路由放进 `addRouters`；静态 + 动态合集放进 `routers`。

### 5.1 `hasPermission()` 怎样判断？

```ts
function getMenu(name: string, menus: UmsMenu[]) {
  return menus.find(menu => name === menu.name) || null
}
```

本项目通过**路由 `name` 对应菜单 `name`** 查找授权菜单。例如 `route.name = 'product'`，就找 `menus` 中 `name === 'product'` 的条目。

真实 `hasPermission()` 的主要行为：

- 路由**有 `name`** 且找到匹配菜单：返回 `true`，并可能把菜单的 `title`、`icon`、`hidden`、`sort` 写到路由对象上。
- 路由有 `name` 但找不到菜单：一般返回 `false`；如果该路由原先是 `hidden: true`，它仍被保留，并把 `sort` 设为 `-1`。
- 路由**没有 `name`**：直接返回 `true`。
- `currMenu.hidden !== 0` 用来计算路由的隐藏标记；若值为 `0` 就不隐藏。
- `testMode` 的真实值是 `false`，所以“测试模式下 admin 直接放行”分支当前不会触发。

**注意**：前端的菜单/路由筛选，不构成后端接口的安全授权；服务端仍应验证权限。

### 5.2 `sortRouters()` 排序规则

```ts
function compare(a: RouteRecordExt, b: RouteRecordExt) {
  if (a.sort && b.sort) {
    return b.sort - a.sort
  }
  return 0
}
```

两者 `sort` 都为真值时，按**降序**排。因为 `0` 是假值，所以有一方 `sort = 0` 时返回 `0`，即比较器认为它们在这次比较中顺序相同。`sortRouters()` 会对父路由数组及各父路由的 `children` 排序。

### 5.3 源码阅读时发现的潜在问题

- `asyncRouterMap.filter()` 只生成新数组，**不深拷贝路由对象**。`v.children = v.children.filter(...)`、`hasPermission()` 内的字段赋值，都会改动导入的原始路由对象，可能影响以后重新生成不同权限路由的结果。
- 图标赋值的条件写成 `currMenu.icon != null && currMenu.title !== ''`，第二项检查的是 `title` 而非 `icon`，值得复核。
- `SidebarItem` 后面会用 `children[0]`，但判断“只有一个可显示子路由”时先过滤了 `hidden`；如果原数组第一项隐藏，可能选错跳转目标。

这些是**源码层面的风险提示**，不是已经在实际运行中验证的故障。

---

## 6. 导航守卫：如何把 Pinia 的路由注册到 Router？

你之前找到的主要代码：

```ts
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const permissionStore = usePermissionStore()

  if (userStore.userInfo.token) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else if (permissionStore.addRouters.length === 0) {
      permissionStore.generateRoutes({
        menus: userStore.userInfo.menus,
        username: userStore.userInfo.username
      })

      permissionStore.addRouters.forEach(route => {
        router.addRoute(route)
      })

      next({ ...to, replace: true })
    } else {
      next()
    }
  } else {
    // /login 在白名单中可以放行；其他路由跳转 /login
  }
})
```

| 代码 | 作用 |
|---|---|
| `beforeEach` | 在导航前执行登录和路由检查 |
| `userStore.userInfo.token` | 前端判断有无 Token；不等于服务端已验证合法性 |
| `generateRoutes()` | 用用户菜单数据筛选动态路由 |
| `permissionStore.addRouters` | Pinia 保存的当前可访问动态路由数组 |
| **`router.addRoute(route)`** | **真正注册动态路由** |
| `next({ ...to, replace: true })` | 注册后重新导航、重新匹配目标，并替换历史记录 |

**最关键的一点：** Pinia 负责保存“要注册的路由”，Vue Router 的 `addRoute` 才负责“执行注册”。

---

## 7. Sidebar：从 Pinia 取得数据，交给 SidebarItem

真实 `Sidebar/index.vue`：

```ts
const appStore = useAppStore()
const permissionStore = usePermissionStore()
const route = useRoute()

const routes = computed(() => permissionStore.routers)
const isCollapse = computed(() => !appStore.sidebar.opened)
```

模板：

```vue
<el-menu :default-active="route.path" :collapse="isCollapse">
  <sidebar-item :routes="routes"></sidebar-item>
</el-menu>
```

这里有三条**不同的信息**：

- `permissionStore.routers`：**显示哪些菜单项**。
- `route.path`：**当前位于哪个路由**，用于 `el-menu` 选中项。
- `appStore.sidebar.opened`：**侧边栏是否收缩**，与当前业务页面是哪一个无关。

### 7.1 `computed` 是在干什么？

```ts
const routes = computed(() => permissionStore.routers)
```

`computed()` 来自 **Vue**，它把 Store 的 `routers` 包装成一个响应式计算属性。Pinia 的数据变化时，它也反映更新。它**不是**连接 Pinia 的必须步骤：在模板里直接使用 `permissionStore.routers` 也可以。

### 7.2 `<sidebar-item :routes="routes" />` 到底是什么意思？

```vue
<SidebarItem :routes="routes" />
              └─┬─┘  └─┬─┘
             Prop 名  父组件变量
```

- `SidebarItem`：要创建的子组件。
- `:routes`：传给子组件一个名叫 `routes` 的属性。
- 右侧 `"routes"`：**父组件中变量 `routes` 的当前值**。
- `:` 是 `v-bind:` 的简写，右侧按 JavaScript 表达式求值。

相当于：

```ts
const menuList = computed(() => permissionStore.routers)
```

```vue
<SidebarItem :routes="menuList" />
```

左边是参数名，右边是实参。**这里传的是路由数组的值，而不是 `usePermissionStore()` 函数或访问 Pinia 的“工具”。**

若写成没有冒号的 `routes="routes"`，传入的只是字符串 `"routes"`。

---

## 8. Props：子组件如何接收数据？

在 `SidebarItem.vue` 中：

```ts
const props = defineProps({
  routes: {
    type: Array as PropType<RouteRecordExt[]>
  },
  isNest: {
    type: Boolean,
    default: false
  }
})
```

逐项解释：

| 写法 | 含义 |
|---|---|
| `defineProps()` | Vue `<script setup>` 的组件输入声明机制 |
| `routes` | 这个子组件可以接收一个名叫 `routes` 的 Prop |
| `type: Array` | 运行时做数组类型的粗略检查 |
| `PropType<RouteRecordExt[]>` | 告诉 TypeScript 里面的元素是什么路由类型 |
| `props.routes` | 子组件读取父组件给它的数据 |
| `isNest` | 表示是不是嵌套菜单；默认 `false` |

**Props 属于 Vue，不属于 Pinia。** 即使不用 Pinia，也能正常父传子。

注意项目里的：

```ts
props.routes!.filter(...)
```

其中 `!` 是 TypeScript 非空断言，只影响类型检查；由于 `routes` 没声明为 `required: true`，如果调用方没传数组，运行时仍可能出错。

### 8.1 为什么递归菜单适合用 Props？

实际模板还写了：

```vue
<sidebar-item
  :is-nest="true"
  class="nest-menu"
  v-if="child.children && child.children.length > 0"
  :routes="[child]"
  :key="child.path"
/>
```

这意味着 `SidebarItem` 可以再创建一个 `SidebarItem`。子组件只需要处理本次收到的 `[child]`，而不必每一层重新从 Pinia 获取全部菜单。这叫**递归组件**。

---

## 9. SidebarItem 的 template 怎样把数组画成菜单？

首先过滤：

```ts
const filteredRoutes = computed(() => {
  return props.routes!.filter(item => !item.hidden && item.children)
})
```

然后循环：

```vue
<template v-for="item in filteredRoutes">
  <!-- 根据 item 的 children 情况决定采用哪种菜单结构 -->
</template>
```

比如 `item` 是 `/pms`：

```text
item.meta.title = 商品
item.children:
  product       → 商品列表
  addProduct    → 添加商品
  productCate   → 商品分类
  brand         → 品牌管理
  ...
```

同一份模板经过 `v-for` 可以生成多项菜单，不需要程序员写四遍 HTML。

| 标签 | 在这个组件中的职责 |
|---|---|
| `<el-sub-menu>` | 生成能展开/收起的一级菜单 |
| `<el-menu-item>` | 生成具体菜单选项 |
| `<template #title>` | 填充菜单项标题部分 |
| `<svg-icon>` | 根据 `meta.icon` 显示图标 |
| `<router-link :to="...">` | 点击普通菜单后触发路由导航 |
| `<a href="..." target="_blank">` | 点击外链后打开新标签页 |
| `v-if` / `v-else` | 决定单级菜单还是下拉菜单 |
| `v-for` | 根据路由数组生成重复结构 |

### 9.1 一个子路由时为什么不显示下拉菜单？

真实条件：

```vue
v-if="item.children &&
      hasOneShowingChildren(item.children) &&
      !item.children[0]!.children &&
      !item.alwaysShow"
```

翻译：父路由有子路由，**恰好一个子路由需要显示**，第一个子路由没有更深的子路由，而且没有要求始终显示父菜单，就简化成一个可直接点击的菜单项。

`hasOneShowingChildren` 会先过滤 `hidden: true` 再计数，所以**“只有一个可显示的子路由”不等于数组里只有一个元素**。

相反，多个可显示子路由时走 `<el-sub-menu>`，会生成「商品 ▼」这种父菜单。你的首页父路由实际包含 `home`、`document`、`video`，因此按所给模板，它不是“只有一个子路由”的情况。

### 9.2 哪里才是点击后真正跳转的代码？

```vue
<router-link :to="item.path + '/' + child.path">
  <el-menu-item :index="item.path + '/' + child.path">
    <!-- 菜单标题和图标 -->
  </el-menu-item>
</router-link>
```

如果：

```ts
item.path = '/pms'
child.path = 'product'
```

拼接后 `to = '/pms/product'`。`router-link` 负责向 Vue Router 发起导航；`el-menu-item` 主要负责菜单项样式、标识、选中状态。

外部教程地址则由 `child.path.startsWith('http')` 分支生成 `<a href="..." target="_blank">`，不走普通内部路由跳转。

---

## 10. Layout 与 AppMain：页面为什么能在同一块区域切换？

实际 `Layout.vue`：

```vue
<template>
  <div class="app-wrapper" :class="classObj">
    <Sidebar class="sidebar-container" />
    <div class="main-container">
      <Navbar />
      <AppMain />
    </div>
  </div>
</template>
```

实际 `AppMain.vue`：

```vue
<template>
  <section class="app-main">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </section>
</template>
```

因此：

```text
Layout.vue 固定组织：Sidebar + Navbar + AppMain
AppMain.vue 文件固定不变
AppMain 内的 <router-view> 取得当前路由组件
<component :is="Component" /> 把组件显示出来
```

例如：

```text
/#/home          → Layout + home/index.vue
/#/pms/product   → Layout + pms/product/index.vue
/#/oms/order     → Layout + oms/order/index.vue
```

Sidebar 和 Navbar 可以因选中项、状态等而更新，但不需要像中间业务区域一样整体换成另一个业务组件。

---

## 11. 一次完整的点击：从「商品列表」到商品页面

1. `router/index.ts` 定义 `/pms`（父路由）与 `product`（子路由），以及对应的 Vue 组件。
2. `stores/permission.ts` 从用户菜单中筛选出允许访问的路由，保存到 `addRouters`，并将基础路由与动态路由合并为 `routers`。
3. 导航守卫使用 `router.addRoute()` 真正注册动态路由。
4. `Sidebar/index.vue` 通过 `usePermissionStore()` 读取 `permissionStore.routers`。
5. `<SidebarItem :routes="routes" />` 使用 Props 把菜单数组交给 `SidebarItem.vue`。
6. `SidebarItem.vue` 用 `v-for`、`el-sub-menu`、`el-menu-item` 生成菜单，用 `router-link` 绑定导航目标。
7. 用户点击「商品列表」，Vue Router 导航到 `/pms/product`，按路由表匹配 Layout 和商品列表组件。
8. `Layout.vue` 的 `AppMain.vue` 通过 `router-view` 显示 `views/pms/product/index.vue`。
9. `route.path` 变为 `/pms/product`，Sidebar 的 `default-active` 可据此高亮对应菜单项。

**核心：菜单生成、路由注册、点击导航、页面渲染是四个不同的步骤。**

---

## 12. 常见误区与准确表述

| 容易搞错的说法 | 正确说法 |
|---|---|
| `export` 自动把路由交给 Pinia | 本项目是 `stores/permission.ts` 显式 `import`，然后用 `shallowRef` 保存 |
| Pinia 就是 Router | Pinia 保存共享数据；Router 负责路由注册、匹配和导航 |
| `routes` 是 Router 实例 | 此处 `routes` 是读取 Store 中数组的计算属性 |
| `computed()` 是 Pinia 的功能 | 它来自 Vue；`defineStore()` 才来自 Pinia |
| Props 是 Pinia 的一部分 | Props 是 Vue 内置的组件输入机制 |
| `:routes="routes"` 传的是 Pinia 访问函数 | 传的是 `routes` 的当前数组值，不是 `usePermissionStore()` |
| `children` 就是 Home 中的内容 | `children` 属于它所在的父路由，如 `/pms`，并通过嵌套路由出口渲染 |
| Layout 就是侧边栏 | Layout 是 Sidebar、Navbar、AppMain 的公共布局 |
| AppMain 会随路由切换文件 | AppMain 固定，内部渲染的业务组件改变 |
| 点击「商品」一定会跳转 | 这里的 `<el-sub-menu>` 展开菜单，子项的 `router-link` 才发起导航 |
| `hidden: true` 表示服务器拒绝访问 | 它控制项目菜单展示，不替代后端权限验证 |

---

## 13. 自测题（先答，再展开参考答案）

1. `constantRouterMap` 是在 `export` 时进入 Pinia，还是在 `stores/permission.ts` 被导入并赋给 `shallowRef` 时进入？
2. `permissionStore.routers` 与 `permissionStore.addRouters` 分别给谁使用？
3. `generateRoutes()` 更新 `addRouters` 后，是否自动完成 Vue Router 注册？
4. `computed(() => permissionStore.routers)` 中 `computed` 属于 Vue 还是 Pinia？
5. `<SidebarItem :routes="menuList" />` 中，子组件接收的 Prop 名称是哪一个？
6. 为什么 Store 定义内部写 `routers.value`，外面读取时写 `permissionStore.routers`？
7. `el-sub-menu`、`router-link`、`router-view` 分别负责哪一步？
8. `/pms/product` 匹配到的父组件与子组件分别是什么？

<details>
<summary>参考答案</summary>

1. 在 `stores/permission.ts` 中显式导入、作为 `shallowRef(constantRouterMap)` 的初始值被 Store 管理；`export` 只表示允许其他文件导入。
2. `routers` 给 Sidebar 生成菜单；`addRouters` 给导航守卫调用 `router.addRoute()`。
3. 不会，还需要 `router.addRoute(route)`。
4. Vue。
5. `routes`；右边 `menuList` 是父组件的变量名。
6. Store 内部处理 Ref 要使用 `.value`；Pinia 的 Store 实例会自动解包返回的 Ref。
7. 展开/收起菜单；发起导航；显示匹配到的路由组件。
8. `/pms` → `Layout.vue`；`product` → `views/pms/product/index.vue`。

</details>

---

## 14. 后续学习与源码验证清单

本阶段路由—菜单链路已能解释；但尚未亲自查看以下文件的完整实现：

- `main.ts` / `main.js`：Vue、Pinia、Router、守卫如何初始化和注册。
- `stores/user`：`token`、`menus` 从哪里取得，怎样处理登录和持久化。
- `Navbar.vue`、`stores/app`：侧边栏展开/收起的触发逻辑。
- `views/home/index.vue`：主页统计卡片、数据、事件和请求来源。
- API、Controller、Service：前端页面动作怎样贯通后端。

**推荐下一阶段：从 `views/home/index.vue` 入手，按「模板显示 → 状态变量 → 事件函数 → API 请求 → Network → Controller → Service」顺序完整追踪一个业务功能。**

### 一句话终极复述

> **Router Map 负责定义“有什么页面”；Pinia Permission Store 根据权限整理“有哪些可用页面和菜单”；Sidebar 借助 Props 把这份数据交给 SidebarItem；SidebarItem 负责“画出菜单并让它能点击”；Vue Router 负责“真的跳转”；Layout 和 AppMain 负责“把目标业务页面显示出来”。**
