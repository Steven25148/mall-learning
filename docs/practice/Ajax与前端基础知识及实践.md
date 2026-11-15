# Ajax 与前端基础知识及实践（结合 mall 项目）

本文面向已有 Java、Spring MVC 和 HTTP 基础，希望理解“浏览器如何在不刷新页面的情况下调用后端接口”的学习者。

学习目标不是立刻掌握完整前端框架，而是先打通下面这条链路：

```text
HTML 页面
→ JavaScript 获取输入
→ 监听用户事件
→ Ajax 发送 HTTP 请求
→ Spring MVC 接收请求
→ 后端返回 JSON
→ JavaScript 解析响应
→ DOM 局部更新页面
```

## 学习范围与优先级

| 模块 | 需要掌握的内容 | 优先级 |
| --- | --- | --- |
| HTML 基础 | `input`、`button`、`form`、`table`、`script` | 必学 |
| JavaScript 基础 | `let`、`const`、函数、对象、数组、条件、循环 | 必学 |
| DOM 操作 | `getElementById`、`value`、`innerHTML`、`textContent` | 必学 |
| 事件处理 | `onclick`、`addEventListener`、表单提交事件 | 必学 |
| HTTP 基础 | GET、POST、Header、Body、JSON、状态码 | 已有基础，需要结合前端复习 |
| Ajax 核心 | 异步请求、响应处理、局部更新 | 必学 |
| XMLHttpRequest | `open()`、`send()`、`onreadystatechange` | 建议掌握 |
| jQuery Ajax | `$.ajax()`、`$.get()`、`$.post()` | 建议掌握 |
| Fetch API | `fetch()`、Promise、`async/await` | 必学 |
| CSS | 基本选择器、简单布局 | 了解即可 |
| Vue / React | 组件、路由、状态管理等 | 暂时不用深入 |

当前 mall 前端主要使用 Vue 3 和 Axios，但底层仍然离不开 HTML、JavaScript、DOM、事件和 HTTP。先掌握本文前半部分，再阅读项目的 Axios 封装，会更容易理解。

---

# 一、HTML 基础

HTML 负责描述页面结构。浏览器读取 HTML 后，会把它转换成 DOM 树，JavaScript 再通过 DOM API 查找和修改页面节点。

## 1. `input`：接收用户输入

```html
<label for="username">用户名</label>
<input id="username" name="username" type="text" />

<label for="password">密码</label>
<input id="password" name="password" type="password" />
```

需要掌握的属性：

- `id`：页面内节点标识，JavaScript 可以据此查找元素。
- `name`：表单字段名称，传统表单提交和 `FormData` 会使用它。
- `type`：输入类型，例如 `text`、`password`、`number`、`email`。
- `value`：输入框当前值。
- `placeholder`：输入提示。
- `required`：浏览器基础必填校验。
- `disabled`：禁用，通常不会参与传统表单提交。
- `readonly`：只读，但通常仍可参与表单提交。

JavaScript 读取输入：

```javascript
const usernameInput = document.getElementById('username')
const username = usernameInput.value
```

## 2. `button`：触发操作

```html
<button id="loadButton" type="button">加载品牌</button>
```

常见类型：

- `type="button"`：普通按钮，不会自动提交表单。
- `type="submit"`：提交所在表单。
- `type="reset"`：重置表单控件。

如果按钮在 `<form>` 中但没有显式写 `type`，默认行为可能是提交表单。普通操作按钮建议明确写：

```html
type="button"
```

## 3. `form`：组织并提交表单

```html
<form id="loginForm">
  <label>
    用户名
    <input id="username" name="username" required />
  </label>

  <label>
    密码
    <input id="password" name="password" type="password" required />
  </label>

  <button type="submit">登录</button>
</form>
```

传统表单提交会导致页面跳转或刷新。使用 Ajax 时通常拦截 `submit` 事件：

```javascript
const form = document.getElementById('loginForm')

form.addEventListener('submit', event => {
  event.preventDefault()
  // 在这里使用 fetch 或 Axios 发送请求
})
```

`event.preventDefault()` 用于阻止浏览器默认提交行为。

## 4. `table`：展示列表数据

```html
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>品牌名称</th>
      <th>显示状态</th>
    </tr>
  </thead>
  <tbody id="brandTableBody"></tbody>
</table>
```

Ajax 获得品牌数组后，可以为 `<tbody>` 动态添加 `<tr>`。

## 5. `script`：加载 JavaScript

页面底部加载脚本：

```html
<script src="./app.js"></script>
```

现代模块写法：

```html
<script type="module" src="./app.js"></script>
```

`type="module"` 支持 `import`、`export`，并且脚本默认延迟执行。

如果脚本放在 `<head>` 中，可以使用：

```html
<script defer src="./app.js"></script>
```

这样浏览器会先解析 HTML，再执行脚本，避免脚本执行时 DOM 元素尚未创建。

## HTML 实践

创建一个页面，包含：

- 用户名输入框。
- 密码输入框。
- 登录按钮。
- “加载品牌”按钮。
- 错误信息区域。
- 品牌列表表格。

此时先不请求后端，只完成页面结构。

---

# 二、JavaScript 基础

## 1. `const` 和 `let`

优先使用 `const`：

```javascript
const apiBaseUrl = 'http://localhost:8080'
```

变量需要重新赋值时使用 `let`：

```javascript
let token = ''
token = 'Bearer abc123'
```

不建议在现代代码中使用 `var`，因为它存在函数作用域、变量提升和重复声明等容易引发误解的行为。

注意，`const` 表示变量引用不能重新赋值，不代表对象内容完全不可修改：

```javascript
const user = { username: 'admin' }
user.username = 'test' // 可以

// user = {}           // 不可以
```

## 2. 基本数据类型

常见类型：

```javascript
const username = 'admin'       // string
const pageNum = 1              // number
const enabled = true           // boolean
const emptyValue = null        // null
let notAssigned                // undefined
const user = { id: 1 }         // object
const brands = []              // array，也是 object
```

判断类型：

```javascript
typeof username // "string"
typeof pageNum  // "number"
```

判断数组：

```javascript
Array.isArray(brands)
```

## 3. 函数

普通函数：

```javascript
function add(a, b) {
  return a + b
}
```

箭头函数：

```javascript
const add = (a, b) => a + b
```

异步函数：

```javascript
async function loadBrands() {
  const response = await fetch('/brand/list')
  return response.json()
}
```

`async` 函数总是返回 Promise。`await` 只能直接用于异步函数内部或模块顶层。

## 4. 对象

创建对象：

```javascript
const loginRequest = {
  username: 'admin',
  password: '123456',
}
```

读取属性：

```javascript
loginRequest.username
loginRequest['password']
```

对象解构：

```javascript
const { username, password } = loginRequest
```

展开对象：

```javascript
const requestWithCode = {
  ...loginRequest,
  authCode: '1234',
}
```

JSON 只能表达数据，不能直接表达函数、`undefined` 等 JavaScript 行为。

## 5. 数组

```javascript
const brands = [
  { id: 1, name: 'Yamaha' },
  { id: 2, name: 'Honda' },
]
```

常用操作：

```javascript
brands.forEach(brand => {
  console.log(brand.name)
})

const names = brands.map(brand => brand.name)

const visibleBrands = brands.filter(brand => brand.showStatus === 1)

const yamaha = brands.find(brand => brand.name === 'Yamaha')
```

前端处理接口列表时，`forEach`、`map`、`filter` 和 `find` 比传统循环更常见。

## 6. 条件

```javascript
if (result.code === 200) {
  console.log('请求成功')
} else if (result.code === 401) {
  console.log('登录失效')
} else {
  console.log(result.message)
}
```

优先使用严格比较：

```javascript
===
!==
```

避免依赖 `==` 的隐式类型转换。

## 7. 循环

```javascript
for (const brand of brands) {
  console.log(brand.name)
}
```

如果需要下标：

```javascript
for (let index = 0; index < brands.length; index += 1) {
  console.log(index, brands[index])
}
```

不要对数组使用 `for...in` 作为首选，它遍历的是可枚举属性名。

## JavaScript 实践

先使用静态数组完成以下任务：

1. 找出所有 `showStatus === 1` 的品牌。
2. 提取品牌名称数组。
3. 根据输入的关键字过滤品牌。
4. 将结果打印到控制台。
5. 下一节再把结果显示到页面。

---

# 三、DOM 操作

DOM 是浏览器对 HTML 文档的对象表示。JavaScript 可以查找、读取、创建、修改和删除 DOM 节点。

## 1. `getElementById`

HTML：

```html
<input id="keyword" />
<p id="message"></p>
```

JavaScript：

```javascript
const keywordInput = document.getElementById('keyword')
const messageElement = document.getElementById('message')
```

还应认识：

```javascript
document.querySelector('#keyword')
document.querySelector('.brand-row')
document.querySelectorAll('.brand-row')
```

`querySelector` 使用 CSS 选择器，表达能力更强。

## 2. `value`

读取输入框：

```javascript
const keyword = keywordInput.value.trim()
```

设置输入框：

```javascript
keywordInput.value = 'Yamaha'
```

`value` 主要适用于表单控件；普通 `<div>`、`<p>` 通常使用 `textContent`。

## 3. `textContent`

```javascript
messageElement.textContent = '加载成功'
```

如果字符串来自用户或后端，应优先使用 `textContent`，因为它会按纯文本显示，不会把内容解析成 HTML。

例如后端返回：

```text
<img src=x onerror=alert(1)>
```

使用 `textContent` 时只会显示文字，不会执行其中的 HTML 或脚本。

## 4. `innerHTML`

```javascript
messageElement.innerHTML = '<strong>加载成功</strong>'
```

`innerHTML` 会解析 HTML，使用方便，但如果内容中混入不可信输入，会产生 XSS 风险。

错误示例：

```javascript
messageElement.innerHTML = serverResult.message
```

如果确实需要构造列表，更安全、清晰的方式是创建 DOM 节点：

```javascript
function appendBrandRow(tableBody, brand) {
  const row = document.createElement('tr')

  const idCell = document.createElement('td')
  idCell.textContent = String(brand.id)

  const nameCell = document.createElement('td')
  nameCell.textContent = brand.name

  row.append(idCell, nameCell)
  tableBody.appendChild(row)
}
```

## 5. 清空和重新渲染

```javascript
function renderBrands(brands) {
  const tableBody = document.getElementById('brandTableBody')
  tableBody.replaceChildren()

  for (const brand of brands) {
    appendBrandRow(tableBody, brand)
  }
}
```

这就是“局部更新”：只替换表格内容，不重新加载整个网页。

## DOM 实践

使用上一节的静态品牌数组：

1. 点击按钮后读取关键字。
2. 使用 `filter()` 过滤数组。
3. 清空 `<tbody>`。
4. 使用 `createElement()` 添加表格行。
5. 没有结果时使用 `textContent` 显示提示。

---

# 四、事件处理

事件表示浏览器中发生的行为，例如点击、输入、提交、键盘操作和页面加载。

## 1. `onclick`

HTML 内联写法：

```html
<button onclick="loadBrands()">加载品牌</button>
```

这种写法容易把 HTML 与 JavaScript 逻辑混在一起，适合认识概念，不推荐用于较大的项目。

DOM 属性写法：

```javascript
button.onclick = loadBrands
```

同一个元素的 `onclick` 属性只能保留一个处理函数，新赋值会覆盖旧处理函数。

## 2. `addEventListener`

推荐写法：

```javascript
const button = document.getElementById('loadButton')

button.addEventListener('click', () => {
  loadBrands()
})
```

它允许同一元素注册多个监听器，也支持更完整的事件配置。

如果要移除监听器，需要保存同一个函数引用：

```javascript
function handleClick() {
  loadBrands()
}

button.addEventListener('click', handleClick)
button.removeEventListener('click', handleClick)
```

## 3. 表单提交事件

```javascript
const loginForm = document.getElementById('loginForm')

loginForm.addEventListener('submit', async event => {
  event.preventDefault()

  const username = document.getElementById('username').value.trim()
  const password = document.getElementById('password').value

  await login(username, password)
})
```

监听 `submit` 比只监听按钮 `click` 更完整，因为用户按 Enter 也能触发表单提交。

## 4. 事件对象

```javascript
button.addEventListener('click', event => {
  console.log(event.target)
  console.log(event.currentTarget)
})
```

- `target`：真正触发事件的元素。
- `currentTarget`：当前监听器绑定的元素。
- `preventDefault()`：阻止默认行为。
- `stopPropagation()`：阻止事件继续冒泡，应该谨慎使用。

## 事件实践

完成以下交互：

- 登录表单监听 `submit`。
- 搜索按钮监听 `click`。
- 关键字输入框监听 `input`，实时显示输入字符数。
- 请求过程中禁用按钮，完成后恢复按钮。

```javascript
async function runWithLoading(button, action) {
  button.disabled = true
  try {
    await action()
  } finally {
    button.disabled = false
  }
}
```

---

# 五、HTTP 基础

## 1. 请求的组成

一个 HTTP 请求主要包含：

```text
请求方法 Method
请求地址 URL
请求头 Headers
请求体 Body（不一定存在）
```

示例：

```http
POST /admin/login HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{
  "username": "admin",
  "password": "123456"
}
```

## 2. GET

GET 主要用于读取资源：

```http
GET /brand/list?pageNum=1&pageSize=5
```

查询参数位于 URL 中。使用 Fetch 时可以手动使用 `URLSearchParams`：

```javascript
const params = new URLSearchParams({
  pageNum: '1',
  pageSize: '5',
})

fetch(`${apiBaseUrl}/brand/list?${params}`)
```

GET 请求通常不应使用请求体发送业务数据。

## 3. POST

POST 常用于创建资源、提交命令或登录：

```javascript
fetch(`${apiBaseUrl}/admin/login`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ username, password }),
})
```

JavaScript 对象必须先通过：

```javascript
JSON.stringify(object)
```

转换为 JSON 字符串，才能作为 JSON 请求体发送。

## 4. Header

常见请求头：

```text
Content-Type：请求体的数据格式
Accept：客户端希望接收的响应格式
Authorization：身份认证信息
```

项目 JWT 请求头示例：

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
```

不要把 Token 写进 URL 查询参数，因为 URL 更容易出现在日志、历史记录和中间设备中。

## 5. Body 和 JSON

请求体 JSON：

```json
{
  "name": "Yamaha",
  "sort": 1
}
```

Spring MVC 使用：

```java
@RequestBody PmsBrandParam param
```

把请求 JSON 转换成 Java 对象。

后端响应：

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "pageNum": 1,
    "pageSize": 5,
    "list": []
  }
}
```

前端使用：

```javascript
const result = await response.json()
```

把 JSON 响应解析成 JavaScript 对象。

## 6. HTTP 状态码和业务码

HTTP 状态码属于 HTTP 响应：

- 200：请求成功。
- 201：创建成功。
- 204：成功但没有响应体。
- 400：请求参数错误。
- 401：未认证。
- 403：已认证但无权限。
- 404：资源不存在。
- 409：资源冲突。
- 500：服务器内部错误。

mall 项目还在 JSON 中定义了业务码：

```json
{
  "code": 500,
  "message": "操作失败",
  "data": null
}
```

需要分别判断：

```javascript
if (!response.ok) {
  // HTTP 协议层失败
}

if (result.code !== 200) {
  // 项目业务层失败
}
```

当前项目的某些异常响应可能是 HTTP 200，但响应体业务码不是 200，因此前端 Axios 响应拦截器检查的是 `res.code`。

## 7. 同源策略和 CORS

浏览器中的 JavaScript 受到同源策略约束。协议、域名、端口只要有一个不同，就属于不同源。

例如：

```text
前端：http://localhost:5173
后端：http://localhost:8080
```

端口不同，因此是跨域请求。后端必须正确配置 CORS，或者开发服务器通过反向代理把请求变成同源请求。

CORS 不是 Postman 或后端之间通信的限制，它主要是浏览器的安全机制。

---

# 六、Ajax 核心

Ajax 原意是 Asynchronous JavaScript and XML。现代项目多数使用 JSON，但“Ajax”这个名称仍然保留。

Ajax 的核心不是某个具体函数，而是一种交互方式：

```text
JavaScript 异步发送请求
→ 等待服务器响应
→ 处理 JSON
→ 只更新页面的一部分
→ 页面整体不刷新
```

## 同步与异步

错误的直觉是：代码会一直停在网络请求处，浏览器完全不能做其他事情。

实际使用 Promise 时：

```javascript
console.log('开始')

fetch('/brand/list')
  .then(response => response.json())
  .then(result => console.log(result))

console.log('请求已经发出')
```

通常输出顺序是：

```text
开始
请求已经发出
服务器响应结果
```

浏览器不会因为等待网络响应而冻结整个页面线程。

## Ajax 的基本状态处理

一个完整请求通常要处理：

- 空闲状态。
- 加载状态。
- 成功状态。
- 无数据状态。
- 业务失败状态。
- 网络或协议失败状态。

示例：

```javascript
async function handleLoad() {
  setLoading(true)
  showMessage('正在加载...')

  try {
    const brands = await loadBrands()
    renderBrands(brands)
    showMessage(brands.length === 0 ? '暂无数据' : '加载成功')
  } catch (error) {
    showMessage(error.message)
  } finally {
    setLoading(false)
  }
}
```

## Ajax 的优势

- 页面无需整体刷新。
- 用户交互更流畅。
- 前后端可以使用 JSON 解耦。
- 可以按需加载局部数据。

## Ajax 需要注意的问题

- 网络请求可能失败或超时。
- 用户可能重复点击导致重复请求。
- 响应返回顺序可能与请求发出顺序不同。
- 登录 Token 可能过期。
- 需要处理跨域、状态码和业务码。
- 不能把服务端返回内容不加处理地写入 `innerHTML`。

---

# 七、XMLHttpRequest

`XMLHttpRequest` 是经典的浏览器 Ajax API。现代业务更常使用 Fetch 或 Axios，但面试中应理解它的基本执行过程。

## 基本 GET 请求

```javascript
function loadBrandsWithXHR() {
  const xhr = new XMLHttpRequest()

  xhr.open(
    'GET',
    'http://localhost:8080/brand/list?pageNum=1&pageSize=5',
    true,
  )

  xhr.setRequestHeader('Authorization', token)

  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status >= 200 && xhr.status < 300) {
        const result = JSON.parse(xhr.responseText)
        console.log(result)
      } else {
        console.error('HTTP 请求失败：', xhr.status)
      }
    }
  }

  xhr.onerror = function () {
    console.error('网络错误')
  }

  xhr.send()
}
```

## 三个核心方法或属性

### `open()`

```javascript
xhr.open(method, url, async)
```

- 配置请求方法和地址。
- 第三个参数为 `true` 表示异步。
- `open()` 只是初始化请求，不会立即发送。

### `send()`

```javascript
xhr.send()
```

真正发送请求。

POST JSON：

```javascript
xhr.setRequestHeader('Content-Type', 'application/json')
xhr.send(JSON.stringify({ username, password }))
```

### `onreadystatechange`

请求状态变化时触发。

常见 `readyState`：

```text
0：UNSENT，尚未调用 open
1：OPENED，已经调用 open
2：HEADERS_RECEIVED，收到响应头
3：LOADING，正在接收响应体
4：DONE，请求完成
```

只有 `readyState === 4` 表示传输完成，还必须检查 HTTP `status` 是否成功。

## 更现代的 XHR 事件写法

```javascript
xhr.addEventListener('load', () => {
  if (xhr.status >= 200 && xhr.status < 300) {
    console.log(JSON.parse(xhr.responseText))
  }
})

xhr.addEventListener('error', () => {
  console.error('网络错误')
})
```

## 项目中的使用

mall 前端的 TinyMCE 上传代码直接创建了：

```javascript
const xhr = new XMLHttpRequest()
```

见 [`Tinymce/index.vue`](../../mall-admin-web/src/components/Tinymce/index.vue)。

这类上传场景可能需要上传进度、底层事件或第三方编辑器回调，因此仍可能使用 XHR。

## XHR 实践

1. 使用 XHR 调用公开或已登录的 GET 接口。
2. 输出 `readyState` 的每次变化。
3. 分别处理 HTTP 成功、HTTP 失败和网络失败。
4. 把返回列表渲染到表格。
5. 再用 Fetch 重写同一个请求并比较代码量。

---

# 八、jQuery Ajax

jQuery 曾经用于统一不同浏览器的 DOM 和 Ajax 行为。现代浏览器和 Vue/React 项目通常不再为了 Ajax 单独引入 jQuery，但维护旧项目时仍应能看懂。

## 引入 jQuery

```html
<script src="https://cdn.example.com/jquery.min.js"></script>
```

实际项目中应使用可信来源、固定版本，并遵守项目的依赖和安全策略。

当前 mall 前端没有把 jQuery 作为主要网络请求库，而是使用 Axios。

## `$.ajax()`

```javascript
$.ajax({
  url: 'http://localhost:8080/brand/list',
  method: 'GET',
  data: {
    pageNum: 1,
    pageSize: 5,
  },
  headers: {
    Authorization: token,
  },
  success(result) {
    console.log(result)
  },
  error(xhr) {
    console.error(xhr.status, xhr.responseText)
  },
})
```

POST JSON：

```javascript
$.ajax({
  url: 'http://localhost:8080/brand/create',
  method: 'POST',
  contentType: 'application/json',
  data: JSON.stringify({
    name: 'Yamaha',
    logo: 'https://example.com/logo.png',
  }),
  success(result) {
    console.log(result)
  },
})
```

注意：

- `contentType` 表示发送给服务器的请求体格式。
- `dataType` 表示期望或解析的响应数据类型。
- 两者不能混为一谈。

## `$.get()`

```javascript
$.get(
  'http://localhost:8080/brand/list',
  { pageNum: 1, pageSize: 5 },
).done(result => {
  console.log(result)
})
```

## `$.post()`

```javascript
$.post(
  'http://localhost:8080/some-form-endpoint',
  { name: 'Yamaha' },
).done(result => {
  console.log(result)
})
```

`$.post()` 的简写形式常以表单编码发送数据。如果后端参数使用 `@RequestBody` 接收 JSON，应使用 `$.ajax()` 并明确设置 `contentType` 和 `JSON.stringify()`。

## jQuery Ajax 实践

目标是“能看懂、能维护”，不要求作为新项目首选：

1. 使用 `$.get()` 查询品牌列表。
2. 使用 `$.ajax()` 登录并发送 JSON。
3. 分清 `contentType` 和 `dataType`。
4. 把同一请求分别用 XHR、jQuery Ajax、Fetch 编写一次。

---

# 九、Fetch API

Fetch 是现代浏览器原生网络请求 API，基于 Promise，适合与 `async/await` 配合使用。

## 1. Promise 基础

Promise 表示一个未来才会完成的异步结果，存在三种状态：

```text
pending：进行中
fulfilled：成功完成
rejected：失败
```

链式写法：

```javascript
fetch('/brand/list')
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

`async/await` 写法：

```javascript
async function loadBrands() {
  try {
    const response = await fetch('/brand/list')
    const result = await response.json()
    console.log(result)
  } catch (error) {
    console.error(error)
  }
}
```

`await` 让异步代码看起来像顺序代码，但不会把网络 IO 变成同步阻塞请求。

## 2. GET 请求

```javascript
async function loadBrands(pageNum, pageSize) {
  const params = new URLSearchParams({
    pageNum: String(pageNum),
    pageSize: String(pageSize),
  })

  const response = await fetch(
    `${apiBaseUrl}/brand/list?${params}`,
    {
      headers: {
        Authorization: token,
      },
    },
  )

  if (!response.ok) {
    throw new Error(`HTTP 请求失败：${response.status}`)
  }

  const result = await response.json()

  if (result.code !== 200) {
    throw new Error(result.message || '业务处理失败')
  }

  return result.data.list
}
```

## 3. POST JSON

```javascript
async function createBrand(brand) {
  const response = await fetch(`${apiBaseUrl}/brand/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: token,
    },
    body: JSON.stringify(brand),
  })

  if (!response.ok) {
    throw new Error(`HTTP 请求失败：${response.status}`)
  }

  const result = await response.json()

  if (result.code !== 200) {
    throw new Error(result.message || '创建失败')
  }

  return result.data
}
```

## 4. Fetch 的重要陷阱

Fetch 遇到 HTTP 404、500 时，Promise 通常不会自动进入 `catch`；只要浏览器成功收到了 HTTP 响应，Promise 就可能 fulfilled。因此必须主动检查：

```javascript
if (!response.ok) {
  throw new Error(...)
}
```

`catch` 更常处理：

- 断网。
- DNS 失败。
- CORS 阻止响应。
- 主动抛出的异常。
- 请求被取消。

## 5. 超时和取消

Fetch 本身没有简单的 `timeout` 参数，可以使用 `AbortController`：

```javascript
async function fetchWithTimeout(url, options = {}, timeoutMs = 5000) {
  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs)

  try {
    return await fetch(url, {
      ...options,
      signal: controller.signal,
    })
  } finally {
    clearTimeout(timeoutId)
  }
}
```

## 6. 封装通用请求函数

```javascript
const apiBaseUrl = 'http://localhost:8080'
let token = ''

async function request(path, options = {}) {
  const headers = new Headers(options.headers)
  headers.set('Accept', 'application/json')

  if (options.body && !headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json')
  }

  if (token) {
    headers.set('Authorization', token)
  }

  const response = await fetch(`${apiBaseUrl}${path}`, {
    ...options,
    headers,
  })

  const contentType = response.headers.get('content-type') || ''
  const result = contentType.includes('application/json')
    ? await response.json()
    : null

  if (!response.ok) {
    throw new Error(result?.message || `HTTP ${response.status}`)
  }

  if (result && result.code !== 200) {
    throw new Error(result.message || '业务处理失败')
  }

  return result
}
```

调用：

```javascript
const result = await request('/brand/list?pageNum=1&pageSize=5')
renderBrands(result.data.list)
```

## 项目中的 Fetch

mall 前端在文件上传场景使用了 `fetch()`：

- [`singleUpload.vue`](../../mall-admin-web/src/components/Upload/singleUpload.vue)
- [`multiUpload.vue`](../../mall-admin-web/src/components/Upload/multiUpload.vue)

普通业务接口则主要通过 Axios 统一封装。

---

# 十、Axios 与当前 mall 项目

Axios 不是浏览器标准 API，而是第三方 HTTP 客户端。它同样用于 Ajax 请求，并提供实例、超时、请求拦截器和响应拦截器等能力。

## 1. 项目的统一实例

项目在 [`src/utils/http.ts`](../../mall-admin-web/src/utils/http.ts) 中创建实例：

```typescript
const http = axios.create({
  baseURL: import.meta.env.VITE_BASE_SERVER_URL,
  timeout: 5000,
})
```

开发环境后端基础地址通常是：

```text
http://localhost:8080
```

## 2. 请求拦截器

```typescript
http.interceptors.request.use(config => {
  const userStore = useUserStore()
  const token = userStore.userInfo.token

  if (token) {
    config.headers.Authorization = token
  }

  return config
})
```

作用是在每次请求前统一添加 JWT Token，不需要每个 API 方法重复编写。

## 3. 响应拦截器

项目会检查后端返回的业务码：

```typescript
http.interceptors.response.use(response => {
  const result = response.data

  if (result.code !== 200) {
    // 统一显示错误、处理 401
    return Promise.reject('error')
  }

  return response.data
})
```

## 4. API 模块

品牌列表：

```typescript
export function getBrandListAPI(params: PageParam) {
  return http({
    url: '/brand/list',
    method: 'get',
    params,
  })
}
```

创建品牌：

```typescript
export function createBrandAPI(data: PmsBrand) {
  return http({
    url: '/brand/create',
    method: 'post',
    data,
  })
}
```

Axios 中：

```text
params → URL 查询参数 → 后端 @RequestParam
data   → HTTP 请求体 → 后端 @RequestBody
```

## 5. 页面调用

```typescript
const response = await getBrandListAPI({
  pageNum: 1,
  pageSize: 5,
})

brandList.value = response.data.list
```

Vue 的响应式状态变化后，Vue 会自动更新相关 DOM。原生 JavaScript 中需要手动调用 `renderBrands()`，这是二者最直观的区别之一。

## 项目 Ajax 完整链路

```text
Vue 页面事件
→ API 方法
→ Axios 实例
→ 请求拦截器添加 Authorization
→ HTTP 请求
→ Spring Security JWT Filter
→ DispatcherServlet
→ Controller
→ Service / Mapper
→ CommonResult JSON
→ Axios 响应拦截器
→ Vue 响应式状态
→ 页面局部更新
```

---

# 十一、CSS 基础

CSS 负责页面样式。现阶段只需掌握基本选择器、盒模型和简单布局。

## 1. 选择器

元素选择器：

```css
button {
  cursor: pointer;
}
```

类选择器：

```css
.error-message {
  color: #c62828;
}
```

ID 选择器：

```css
#brandTable {
  width: 100%;
}
```

属性选择器：

```css
input[type='password'] {
  font-family: monospace;
}
```

## 2. 盒模型

元素尺寸由以下部分组成：

```text
content
padding
border
margin
```

建议统一：

```css
* {
  box-sizing: border-box;
}
```

## 3. 简单布局

Flex 布局：

```css
.toolbar {
  display: flex;
  gap: 12px;
  align-items: center;
}
```

简单页面：

```css
body {
  max-width: 960px;
  margin: 0 auto;
  padding: 24px;
  font-family: system-ui, sans-serif;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px 12px;
  border: 1px solid #ddd;
  text-align: left;
}
```

现阶段不需要深入动画、复杂响应式布局和 CSS 工程化。

---

# 十二、Vue / React 暂时需要理解到什么程度？

目前不需要先系统学习 Vue 或 React，先理解它们解决的问题：

- 把页面拆成组件。
- 用状态描述页面数据。
- 状态变化后自动更新 DOM。
- 使用路由切换页面。
- 使用状态管理在多个组件间共享数据。

原生 JavaScript：

```javascript
brands = await loadBrands()
renderBrands(brands)
```

Vue：

```typescript
brandList.value = await loadBrands()
```

Vue 会根据模板和响应式系统自动更新 DOM。

学习当前 mall 项目时，只需先能看懂：

- `.vue` 文件包含模板、脚本和样式。
- `ref()` 创建响应式数据。
- `@click` 监听点击。
- `v-model` 绑定输入值。
- `v-for` 渲染数组。
- 页面方法调用 `src/apis` 中的 API。
- Pinia 保存登录用户和 Token。

掌握原生 Ajax 后，再学习这些框架概念会更容易。

---

# 十三、综合实践：原生 JavaScript 对接 mall 后端

实践目标：

1. 输入用户名和密码。
2. 使用 Fetch 调用 `/admin/login`。
3. 保存返回的 Token。
4. 携带 Token 调用 `/brand/list`。
5. 把品牌列表渲染到表格。
6. 不刷新整个页面。

## 1. HTML 页面

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>mall Ajax 练习</title>
    <link rel="stylesheet" href="./style.css" />
    <script type="module" src="./app.js"></script>
  </head>

  <body>
    <h1>mall Ajax 练习</h1>

    <form id="loginForm">
      <label>
        用户名
        <input id="username" required />
      </label>

      <label>
        密码
        <input id="password" type="password" required />
      </label>

      <button id="loginButton" type="submit">登录</button>
    </form>

    <section>
      <div class="toolbar">
        <input id="keyword" placeholder="品牌关键字" />
        <button id="loadButton" type="button">加载品牌</button>
      </div>

      <p id="message" aria-live="polite"></p>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>名称</th>
            <th>首字母</th>
            <th>显示状态</th>
          </tr>
        </thead>
        <tbody id="brandTableBody"></tbody>
      </table>
    </section>
  </body>
</html>
```

## 2. JavaScript

```javascript
const apiBaseUrl = 'http://localhost:8080'

const loginForm = document.getElementById('loginForm')
const loginButton = document.getElementById('loginButton')
const loadButton = document.getElementById('loadButton')
const messageElement = document.getElementById('message')
const tableBody = document.getElementById('brandTableBody')

let token = ''

function showMessage(message, isError = false) {
  messageElement.textContent = message
  messageElement.className = isError ? 'error-message' : 'success-message'
}

async function parseResult(response) {
  const contentType = response.headers.get('content-type') || ''
  const result = contentType.includes('application/json')
    ? await response.json()
    : null

  if (!response.ok) {
    throw new Error(result?.message || `HTTP ${response.status}`)
  }

  if (!result) {
    throw new Error('服务器没有返回 JSON')
  }

  if (result.code !== 200) {
    throw new Error(result.message || '业务处理失败')
  }

  return result
}

async function login(username, password) {
  const response = await fetch(`${apiBaseUrl}/admin/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json',
    },
    body: JSON.stringify({ username, password }),
  })

  const result = await parseResult(response)
  token = result.data.token
}

async function loadBrands(keyword) {
  if (!token) {
    throw new Error('请先登录')
  }

  const params = new URLSearchParams({
    keyword,
    pageNum: '1',
    pageSize: '10',
  })

  const response = await fetch(
    `${apiBaseUrl}/brand/list?${params}`,
    {
      headers: {
        Accept: 'application/json',
        Authorization: token,
      },
    },
  )

  const result = await parseResult(response)
  return result.data.list
}

function createCell(text) {
  const cell = document.createElement('td')
  cell.textContent = text
  return cell
}

function renderBrands(brands) {
  tableBody.replaceChildren()

  for (const brand of brands) {
    const row = document.createElement('tr')
    row.append(
      createCell(String(brand.id)),
      createCell(brand.name || ''),
      createCell(brand.firstLetter || ''),
      createCell(brand.showStatus === 1 ? '显示' : '隐藏'),
    )
    tableBody.appendChild(row)
  }
}

loginForm.addEventListener('submit', async event => {
  event.preventDefault()

  const username = document.getElementById('username').value.trim()
  const password = document.getElementById('password').value

  loginButton.disabled = true
  showMessage('正在登录...')

  try {
    await login(username, password)
    showMessage('登录成功')
  } catch (error) {
    showMessage(error.message, true)
  } finally {
    loginButton.disabled = false
  }
})

loadButton.addEventListener('click', async () => {
  const keyword = document.getElementById('keyword').value.trim()

  loadButton.disabled = true
  showMessage('正在加载品牌...')

  try {
    const brands = await loadBrands(keyword)
    renderBrands(brands)
    showMessage(brands.length === 0 ? '暂无品牌' : `加载了 ${brands.length} 条品牌`)
  } catch (error) {
    renderBrands([])
    showMessage(error.message, true)
  } finally {
    loadButton.disabled = false
  }
})
```

## 3. CSS

```css
* {
  box-sizing: border-box;
}

body {
  max-width: 960px;
  margin: 0 auto;
  padding: 24px;
  font-family: system-ui, sans-serif;
}

form,
.toolbar {
  display: flex;
  gap: 12px;
  align-items: end;
  margin-bottom: 20px;
}

label {
  display: grid;
  gap: 4px;
}

input,
button {
  padding: 8px 12px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px 12px;
  border: 1px solid #ddd;
  text-align: left;
}

.error-message {
  color: #c62828;
}

.success-message {
  color: #2e7d32;
}
```

## 4. 实践注意事项

- 先确保 mall-admin 后端运行在配置的地址。
- 浏览器跨域访问时，确认后端 CORS 配置允许当前前端来源。
- 不要把真实账号密码硬编码到 JavaScript 文件。
- 练习中 Token 只保存在内存变量，页面刷新后需要重新登录。
- 生产项目的 Token 保存位置需要综合考虑 XSS、CSRF 和整体认证架构，不能只凭“方便”决定。
- 后端项目的 `Authorization` 值包含配置的 Token 前缀时，应完整保存和发送登录接口返回的 Token 格式。

---

# 十四、实践任务清单

## 阶段一：静态页面

- [ ] 创建输入框、按钮、表格和提示区域。
- [ ] 使用 CSS 完成基本布局。
- [ ] 正确区分 `button` 和 `submit`。

## 阶段二：JavaScript 与 DOM

- [ ] 使用 `const`、`let`、对象和数组保存数据。
- [ ] 使用 `getElementById()` 获取元素。
- [ ] 使用 `value` 获取输入。
- [ ] 使用 `textContent` 显示提示。
- [ ] 使用 `createElement()` 渲染表格，避免把不可信内容直接写入 `innerHTML`。

## 阶段三：事件

- [ ] 使用 `addEventListener()` 监听点击。
- [ ] 监听表单 `submit` 并调用 `preventDefault()`。
- [ ] 请求期间禁用按钮，避免重复提交。

## 阶段四：Ajax

- [ ] 使用 XHR 完成一次 GET 请求。
- [ ] 理解 `open()`、`send()`、`readyState` 和 `status`。
- [ ] 使用 Fetch 和 `async/await` 重写请求。
- [ ] 分别处理 HTTP 错误和业务码错误。
- [ ] 请求完成后只更新表格，不刷新页面。

## 阶段五：连接 mall 后端

- [ ] 调用 `/admin/login` 获取 Token。
- [ ] 在 `Authorization` Header 中发送 Token。
- [ ] 调用 `/brand/list` 获取分页数据。
- [ ] 使用查询参数发送 `pageNum`、`pageSize`、`keyword`。
- [ ] 显示加载、空数据、成功和失败状态。

## 阶段六：读懂项目 Axios

- [ ] 理解 `axios.create()`。
- [ ] 理解 `baseURL` 和 `timeout`。
- [ ] 理解请求拦截器添加 Token。
- [ ] 理解响应拦截器检查 `CommonResult.code`。
- [ ] 理解 `params` 与 `data` 的区别。
- [ ] 找到 Vue 页面调用 API 后更新响应式状态的位置。

---

# 十五、面试速记

## 什么是 Ajax？

> Ajax 是浏览器使用 JavaScript 异步发送 HTTP 请求、处理服务器响应并局部更新页面的技术思想。现代 Ajax 通常传输 JSON，可以通过 XMLHttpRequest、Fetch、Axios 或 jQuery Ajax 实现。

## Ajax 的异步体现在哪里？

> 网络请求发出后，浏览器不需要刷新整个页面，也不会为了等待网络响应而停止所有用户交互。请求完成后通过回调、Promise 或 `async/await` 继续处理结果。

## XHR、Fetch、Axios 的关系是什么？

> XMLHttpRequest 和 Fetch 是浏览器提供的网络 API；Axios 是第三方 HTTP 客户端。在浏览器环境中它会使用可用的底层适配器发送请求，并额外提供实例、拦截器、超时和统一配置等能力。

## Fetch 为什么要检查 `response.ok`？

> Fetch 收到 404、500 等 HTTP 响应时通常不会自动 reject，因为网络传输本身已经成功完成，所以业务代码必须检查 `response.ok` 或 `response.status`。

## `params` 和 `data` 有什么区别？

> 在 Axios 中，`params` 通常被编码到 URL 查询字符串，对应 Spring MVC 的 `@RequestParam`；`data` 通常放入 HTTP 请求体，JSON 请求体对应后端的 `@RequestBody`。

## `innerHTML` 和 `textContent` 有什么区别？

> `innerHTML` 会把字符串解析成 HTML，使用不可信内容时可能造成 XSS；`textContent` 只按文本显示内容，因此显示用户输入和服务端普通文本时应优先使用 `textContent`。

## 当前 mall 项目如何使用 Ajax？

> 普通业务接口主要通过统一封装的 Axios 实例发送请求，请求拦截器添加 JWT Token，响应拦截器检查统一业务码；上传场景还使用 Fetch 和 XMLHttpRequest。响应数据写入 Vue 响应式状态后，Vue 自动局部更新 DOM。

---

# 推荐学习顺序

```text
HTML 表单和表格
→ JavaScript 变量、函数、对象、数组
→ DOM 查找和修改
→ 事件监听和表单提交
→ HTTP 请求与 JSON
→ Ajax 核心思想
→ XMLHttpRequest
→ Fetch + Promise + async/await
→ Axios 封装与拦截器
→ 最后再进入 Vue 组件和响应式系统
```

完成综合实践后，应能独立解释下面这条链路：

```text
点击按钮
→ JavaScript 事件处理器
→ Fetch/Axios 发送请求
→ Header 携带 Token
→ Spring MVC 接收参数
→ 返回 CommonResult JSON
→ 前端检查 HTTP 状态和业务码
→ 解析 data
→ 更新 DOM 或 Vue 响应式状态
```
