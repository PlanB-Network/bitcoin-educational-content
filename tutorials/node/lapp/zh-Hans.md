---
name: LAPP比特币
description: 开发你的第一个LApp的教程
---

学习编写你的第一个闪电网络应用

要求：

- NodeJs >= 8
- LND >= 9

NodeJs可以从其官方网站下载

我们将使用polar工具代替下载和设置LND节点，这个工具将为我们完成这项任务。

为了构建我们的闪电网络应用，我们将使用以下技术：

- Express作为我们的web服务器
- Pug模板 + bootstrap作为我们的前端

## 操作系统

建议使用Linux，如果你使用的是Windows 10，你可以通过以下几个步骤获得一个Linux控制台。
准备基础

使用应用程序生成器工具express，快速创建一个应用程序骨架。

```
$ sudo npm install express-generator -g
```

通过以下指令，我们创建一个名为lnapp的Express应用程序。应用程序将在当前工作目录中的一个名为lnapp的目录中创建，并且视图引擎将被指定为Pug。

```
$ express --view=pug lnapp
```

然后我们进入目录并安装运行web服务器所需的包。

```
$ cd myapp
$ npm install
```

现在我们简单地运行服务器

```
$ npm start
```

接下来，去浏览器访问这个地址 http://localhost:3000 来访问应用程序。

生成的应用程序具有以下目录结构：

```
.
├── app.js
├── bin
│ └── www
├── package.json
├── public
│ ├── images
│ ├── javascripts
│ └── stylesheets
│ └── style.css
├── routes
│ ├── index.js
│ └── users.js
└── views
├── error.pug
├── index.pug
└── layout.pug
```

## Polar

下载Polar，安装它，并创建一个包含2个LND节点（Alice和Bob）和1个bitcoind的网络。一旦我们在应用中看到显示我们节点的图表，点击开始按钮并等待几秒钟，直到每个节点的指示器变成绿色。

为了在闪电网络上发送支付，节点之间通过通道相互连接是必要的。使用Polar创建通道非常简单，我们只需要用鼠标点击Alice节点的一个耳朵并拖动到Bob节点的一个耳朵上。立即，一个标题为Open new channel的模态窗口应该出现，我们保留默认值并按下打开通道按钮。现在我们重复操作，但这次从Bob到Alice，这样两个节点都可以发送和接收金钱。

## Nodemon

为了避免每次在代码中进行更改时都必须重启nodejs，我们将安装nodemon

```
$ npm install nodemon -D
```

我们必须在package.json文件的scripts部分创建一个条目，添加这行代码 "dev": "nodemon ./bin/www"，scripts部分应该看起来像这样：

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

转到运行npm start的控制台，按ctrl + c并再次启动nodejs，但这次使用nodemon

```
$ npm run dev
```

## 连接到LND

为了从nodejs连接到一个闪电网络节点，我们将使用ln-service库，我们还将安装dotenv来管理环境变量。

```
$ npm install ln-service dotenv
在我们的lnapp目录中，创建一个名为.env的文件，它应该包含以下变量：

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

返回到Polar，选择我们想要连接的节点Bob，进入“连接”标签页，复制GRPC Host的内容并将其放入LND_GRPC_HOST变量中，在连接标签页的底部选择base64并复制TLS Cert的内容，然后将其放入LND_CERT_BASE64变量中，对admin macaroon也做同样的操作，将其放入LND_MACAROON_BASE64。

现在将这行代码添加到位于工作目录根目录的app.js文件中，我们必须将其复制到文件的第一行。

```
require('dotenv').config();
```

为了验证nodejs能否连接到我们的节点，打开routes/index.js文件，这个路由文件是由express生成器创建的，首先我们需要引入ln-service库，所以我们在第一行添加它

```
const lnservice = require('ln-service');
```

我们添加一个新的路由，它将给我们提供关于我们节点的信息。

```
router.get('/info', async function(req, res, next) {
try {
// 使用lnd进行认证
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// 获取节点信息
const info = await lnservice.getWalletInfo({ lnd });

    // 以json格式显示信息
    res.send(`
      <h1>节点信息</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

现在访问这个地址 http://localhost:3000/info

如果你看到了一个包含LND节点信息的json，恭喜你！！！你的应用现在可以与闪电网络互动了。
创建一个假模型

为了模拟数据库，我们需要创建一个假模型，这将允许我们在不安装和配置数据库的情况下使用应用。

首先，安装uuid包

```
$ npm install uuid
```

创建models目录，并在其中创建Post.js文件，内容如下：

```
const { v4: uuidv4 } = require('uuid');'
class Post {
  constructor() {
    this.posts = [];
  }
  add({ time, name, content, paid, hash, preimage, request }) {
    const post = {
      id: uuidv4(),
      time: time || new Date(),
      name,
      content,
      paid: paid || false,
      hash: hash || null,
      preimage: preimage || null,
      request: request || null,
    };
    this.posts.push(post);

    return post;
  }

  find(id) {
    return this.posts.find(p => p.id === id);
  }

  findByHash(hash) {
    return this.posts.find(p => p.hash === hash);
  }

  findAll() {
    return this.posts;
  }

  findAllPaid() {
    return this.posts
      .filter(p => !!p.paid)
      .sort((a, b) => b.time - a.time);
  }

  paid(hash) {
    let updatedPost;
    this.posts = this.posts.map(p => {
      if (p.hash === hash) {

```markdown
const router = express.Router();
const posts = require('../models/posts');

router.post('/post', async (req, res) => {
  try {
    const { name, content } = req.body;
    const newPost = await posts.createPost(name, content);
    if (newPost) {
      res.json({ success: true, data: newPost });
    } else {
      res.json({ success: false });
    }
  } catch (error) {
    res.status(500).send(error.toString());
  }
});

module.exports = router;
```

## 准备视图

我们需要使用bootstrap来使我们的html看起来更好，因此我们修改位于views目录中的layout.pug文件，使其看起来像这样：

```
doctype html
html
  head
    title= title
    link(rel='stylesheet', href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css')
    link(rel='stylesheet', href='/stylesheets/style.css')
  body
    block content
    block scripts
      script(src="https://code.jquery.com/jquery-3.4.1.min.js")
      script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js")
      script(src="/javascripts/main.js")
```

## 创建文章

要创建一篇文章，我们需要一个表单。在views目录中，创建一个名为form.pug的文件，内容如下：

```
.collapse#post-form
  form
    h2 写一篇文章
    .form-group
      label(for="name") 名称
      input(id="name").form-control
    .form-group
      label(for="content") 内容
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") 发送
```

## 前端中的Javascript

我们与用户交互的最直接方式是在网页浏览器中使用javascript。为此，在javascript目录中创建一个名为main.js的文件，我们已经从layout.pug中调用了它。main.js的初始内容如下：

```
const App = {
  endpoint: 'http://localhost:3000/api',
  interval: null,
};

App.init = () => {
  $('#post-form').collapse('show');
  $('#send-btn').click(App.sendBtn);
}

App.sendBtn = () => {
  console.log('!hola');
};

$(() => App.init());
```

点击“发送”按钮，如果一切正常，它应该在控制台显示一条消息“!hola”。现在我们可以修改App.sendBtn()方法，将信息发送到我们的API。

```
App.sendBtn = async () => {
  const name = $('#name').val();
  const content = $('#content').val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error('获取数据出错！');
  if (response.success) {
    // 使用响应做一些事情
  }
};
```

```markdown
// 将来自API的数据打印到控制台
console.log(response.data);
}
};
```

我们还创建了App.makeRequest()方法并将其添加到main.js中

```markdown
App.makeRequest = ({api, post}) => {
const type = !post ? 'GET' : 'POST';
const data = !!post ? JSON.stringify(post) : null;
return $.ajax(`${App.endpoint}/${api}`, {
type,
data,
contentType: 'application/json',
dataType: 'json',
});
};
```

## 创建API

为此，我们需要在routes目录中创建一个名为api.js的新文件，并编写响应App.sendBtn()内部所做请求的方法。

```markdown
const express = require('express');
```
```markdown
const lnservice = require('ln-service');const router = express.Router();
const post = require('../models/Post');

router.post('/post', (req, res) => {
const { name, content } = req.body;
return res.json({
success: true,
data: { name, content },
});
});

module.exports = router;
```

这个文件必须包含在app.js中，因此我们添加以下几行：

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

再次点击发送按钮，它应该会返回我们在表单中输入的相同数据。

## 创建发票

当用户创建帖子时执行的方法应该生成一个发票，然后在数据库中创建一个记录将其与发票链接，并将发票返回给用户以便他们支付。

```markdown
router.post('/post', async (req, res) => {
// 使用lnd进行认证
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

const { name, content } = req.body;
try {
const invoice = await lnservice.createInvoice({
lnd,
tokens: 1000,
description: name,
});
if (!!invoice) {
const p = post.add({
name,
content,
hash: invoice.id,
request: invoice.request,
preimage: invoice.secret,
});
return res.json({
success: true,
data: p,
});
}
} catch (e) {
console.log(e);
}
});
```

如果我们在按下发送后收到一个帖子对象作为响应，就像这样，那么一切都进行得很正确。现在我们需要显示文本，以便用户可以支付它。

```markdown
{
"success":true,
"data":{
"id":"0fb1544a-d7f9-487d-961a-d0004ecc515c",
"time":"2020-09-02T21:29:53.747Z",
"name":"epale",
"content":"contenido bla bla",
"paid":false,
"hash":"0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
"preimage":null,
}
```

## 新发票视图

在views目录中，我们需要创建一个名为invoice.pug的文件，内容如下：

```
.collapse#invoice-form
form
.h2 支付这张发票
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

并将其包含在index.pug中

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## 修改App.sendBtn()

现在我们修改App.sendBtn()来显示获取的数据：

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('获取数据出错！');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## 接收支付
我们需要知道何时收到付款，为此我们将使用lnservice的subscribeToInvoices()方法，该方法允许我们在发票状态更新时执行代码，要使用它，我们在app.js中添加以下几行。

```javascript
// 引入lnservice和我们的post表
const lnservice = require('ln-service');
const post = require('./models/Post');

// 使用lnd进行认证
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// 每次发票更新时检查发票是否已支付
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // 标记发票为'已支付'
      const paid = post.paid(invoice.id);
      if (paid) console.log('发票已支付！');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// 启动发票订阅
subscribeInvoices();
```

在我们的API中创建一个HTTP GET方法，以便用户检查哈希是否已支付。

```javascript
router.get('/post/:hash', (req, res) => {
  const { hash } = req.params;
  const data = post.findByHash(hash);
  if (!!data) {
    return res.json({
      success: true,
      data,
    });
  } else {
    return res.json({
      success: false,
      data: null,
    });
  }
});
```

现在，从main.js中，我们创建一个名为App.waitPayment()的函数，该函数查询API是否已进行付款。

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("付款已完成");
  }
};
```

现在我们遇到一个问题，函数App.waitPayment()只执行一次，用户可能已经进行了付款，而我们未能指示已收到他们的付款。为此，我们使用一个名为setInterval()的JavaScript函数，它允许我们无限期地以我们指定的时间间隔执行一个函数。

让我们修改函数App.waitPayment()和App.sendBtn()，包括setInterval()和clearInterval()

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    clearInterval(App.interval);
    App.interval = null;
    $("#invoice-form").collapse("hide");
    $("#preimage").text(response.data.preimage);
    $("#success").collapse("show");
  }
};

App.sendBtn = async () => {
  const name = $("#name").val();
  const content = $("#content").val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error("获取数据出错！");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
我们创建一个视图来表示支付已成功接收，我们在views中创建名为success.pug的文件，内容如下：
```pug
.collapse#success
  h2 支付成功
  div 支付凭证：
    #preimage
```

我们将其包含在index.pug中。

```pug
extends layout

block content
  h1 闪电网络应用
  include form.pug
  include invoice.pug
  include success.pug
```

如果在支付发票后你能看到“支付成功”的消息和支付凭证，恭喜你！！！你做到了，你已经完成了你的第一个LApp。