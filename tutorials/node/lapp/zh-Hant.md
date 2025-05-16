---
name: LAPP Bitcoin
description: 開發第一個 LApp 的教學
---

學習編寫您的第一個 lightning 應用程式


要求：



- NodeJs >= 8
- LND >= 9


NodeJs 可從其官方網站下載


我們不需要下載和設定 LND 節點，而是使用極地工具，它會為我們執行這項任務。


為了建立我們的 Lightning 應用程式，我們將使用下列技術：



- 我們網站伺服器的 Express
- 為我們的前端提供 Pug 模板 + bootstrap


## 作業系統


建議使用 Linux，如果您使用的是 Windows 10，只要遵循以下幾個步驟即可擁有 Linux 主控台。

準備底座


使用應用程式產生器工具 express 快速建立應用程式骨架。


```
$ sudo npm install express-generator -g
```


透過以下指令，我們建立一個名為 lnapp 的 Express 應用程式。應用程式會建立在目前工作目錄中名為 lnapp 的目錄下，而視圖引擎會指定給 Pug。


```
$ express --view=pug lnapp
```


然後，我們進入目錄，安裝網頁伺服器執行所需的套件。


```
$ cd myapp
$ npm install
```


現在我們只要執行伺服器


```
$ npm start
```


接下來，在瀏覽器中進入此 Address http://localhost:3000 以存取應用程式。


生成的應用程式具有以下目錄結構：


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


## 極地


下載 Polar 並安裝，然後用 2 個 LND 節點 (Alice 和 Bob) 和 1 個 bitcoind 建立一個網路。當我們在應用程式中看到顯示節點的圖形後，按一下 Start (開始) 按鈕，等待幾秒鐘，直到每個節點的指示器變色為 Green。


為了在 Lightning 上傳送付款，節點之間必須透過通道互相連接。使用 Polar 創建通道非常簡單，我們只需用滑鼠點擊 Alice 節點的一個耳朵，然後將其拖曳到 Bob 節點的一個耳朵上。隨即會出現一個名為 Open new channel (開啟新通道) 的模式視窗，我們保留預設值，然後按下 Open channel (開啟通道) 按鈕。現在我們重複這個動作，但這次是從 Bob 到 Alice，這樣兩個節點都可以傳送和接收金錢。


## Nodemon


為了避免每次修改程式碼時都要重新啟動 nodejs，我們將安裝 nodemon


```
$ npm install nodemon -D
```


我們必須在 package.json 檔案的 scripts 區段中建立一個項目，加入這一行 "dev"："nodemon ./bin/www"，腳本部分應該是這樣的：


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


前往 npm start 正在執行的主控台，按下 ctrl + c 並再次啟動 nodejs，但這次要使用 nodemon


```
$ npm run dev
```


## 連接至 LND


要從 nodejs 連接到 Lightning 節點，我們會使用 LN-service 函式庫，我們也會安裝 dotenv 來管理環境變數。


```
$ npm install ln-service dotenv
```


在 lnapp 目錄中，建立一個名為 .env 的檔案，其中應該包含這些變數：


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


回到 Polar，選擇 Bob，也就是我們要連線的節點，進入「連線」標籤，複製 GRPC Host 的內容並將其放置在 LND_GRPC_HOST 變數中，在連線標籤的下半部分選擇 base64 並複製 TLS Cert 的內容並將其放置在 LND_CERT_BASE64 變數中，並在 LND_MACAROON_BASE64 中對 admin macaroon 做同樣的動作。


現在將此行加入位於工作目錄根目錄的 app.js 檔案，我們必須將它複製到檔案的第一行。


```
require('dotenv').config();
```


為了驗證 nodejs 是否能連線到我們的節點，請開啟 routes/index.js 檔案，這個 routes 檔案是由 express 產生器建立的，首先我們需要 LN-service 函式庫，所以我們在第一行加入它


```
const lnservice = require('ln-service');
```


我們新增一個路由，它會提供我們節點的相關資訊。


```
router.get('/info', async function(req, res, next) {
try {
// authenticate with lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// get node information
const info = await lnservice.getWalletInfo({ lnd });

// display info in json format
res.send(`
<h1>Node info</h1>
<pre>${JSON.stringify(info, null, 2)}</pre>
`);
next();

} catch (e) {
console.log(e);
}
});
```


現在前往此 Address http://localhost:3000/info


如果您看到有 LND 節點資訊的 json，恭喜您！！您的應用程式現在可以與 Lightning Network 互動了。

建立虛假模型


為了模擬資料庫，我們需要建立一個虛假模型，這將允許我們在不安裝和設定資料庫的情況下使用應用程式。


首先，安裝 uuid 套件


```
$ npm install uuid
```


建立 models 目錄，並在其中建立 Post.js 檔案，內容如下：


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
updatedPost = { ...p, paid: true };
return updatedPost;
}
return p;
});
if (updatedPost) {
return true;
}
return false;
}
}

const posts = new Post();

module.exports = posts;
```


## 準備檢視


我們需要 bootstrap 讓我們的 html 看起來更好看，所以我們修改位於 views 目錄下的 layout.pug 檔案，讓它看起來像這樣：


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


## 建立文章


要建立一篇文章，我們需要一個表單。在 views 目錄內，建立一個名為 form.pug 的檔案，內容如下：


```
.collapse#post-form
form
h2 Escriba un artículo
.form-group
label(for="name") Nombre
input(id="name").form-control
.form-group
label(for="content") Contenido
textarea(id="content").form-control
button.btn.btn-primary#send-btn(type="button") Enviar
```


## 前端的 Javascript


我們與使用者互動的最直接方式，就是在網頁瀏覽器中使用 javascript。為此，請在 javascript 目錄中建立一個名為 main.js 的檔案，我們已經從 layout.pug 中呼叫這個檔案。在這個檔案中，初始化專案。main.js 的初始內容如下：


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


按一下「傳送」按鈕，如果一切正常，控制台應該會顯示「！你好」的訊息。現在我們可以修改 App.sendBtn() 方法，將資訊傳送至我們的 API。


```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Error getting data!');
if (response.success) {
// Do something with the response
}
};
```


```markdown
// Print the data that comes from the API to the console
console.log(response.data);
}
};
```


我們也建立方法 App.makeRequest() 並將其加入 main.js


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


## 建立 API


要做到這一點，我們需要在 routes/api.js 中建立一個新檔案，並寫下回應 App.sendBtn() 中請求的方法。


```markdown
const express = require('express');
const lnservice = require('ln-service');
const router = express.Router();
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


此檔案必須包含在 app.js 中，因此我們加入這幾行：


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


讓我們再次按下傳送按鈕，它應該會回應我們在表單中輸入的相同資料。


## 建立 Invoice


使用者建立文章時執行的方法應該是 generate 和 Invoice，然後在資料庫中建立記錄，將其連結到 Invoice，並將 Invoice 傳回給使用者，以便他們付款。


```markdown
router.post('/post', async (req, res) => {
// Authenticate with lnd
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


如果我們在按下傳送之後收到一個 post 物件作為回應，就像這樣，一切都正常進行。現在我們需要顯示文字，讓使用者可以付款。


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


## 新的 Invoice 檢視


在 views 目錄中，我們需要建立一個名為 Invoice.pug 的檔案，內容如下：


```
.collapse#invoice-form
form
.h2 Pay this invoice
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```


並將其納入 index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## 修改 App.sendBtn()


現在我們修改 App.sendBtn()，以顯示取得的資料：


```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Error getting data!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```


## 收到付款


我們需要知道何時收到付款，為此我們將使用 lnservice 的 subscribeToInvoices() 方法，此方法允許我們在 Invoice 的狀態更新時執行程式碼，要使用此方法，我們在 app.js 中加入這幾行。


```
// require lnservice and our post table
const lnservice = require('ln-service');
const post = require('./models/Post');

// authenticate with lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// check if the invoice has been paid every time an invoice is updated
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

// mark the invoice as 'paid'
const paid = post.paid(invoice.id);
if (paid) console.log('Invoice paid!');
});

} catch (e) {
console.log(e);
return e;
}
};
// start the invoice subscription
subscribeInvoices();
```


在我們的 API 中建立 HTTP GET 方法，讓使用者檢查 Hash 是否已支付。


````

router.get('/post/:Hash', (req, res) => {

const { Hash } = req.params;'

```javascript
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
````

Now, from main.js, we create a function called App.waitPayment() that queries the API if the payment has been made.

```

App.waitPayment = async (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`、

});

if (response.success && response.data.paid) {

console.log("Payment made")；

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`、

});

if (response.success && response.data.paid) {

clearInterval(App.interval)；

App.interval = null；

$("#Invoice-form").collapse("hide")；

$("#preimage").text(response.data.preimage)；

$("#success").collapse("show")；

}

};


App.sendBtn = async () => {

const name = $("#name").val()；

const content = $("#content").val()；

const response = await App.makeRequest({

api："post"、

post：{ name, content }、

});

if (!response) console.error("Error getting data!")；

if (response.success) {

$("#post-form").collapse("hide")；

$("#Invoice-form").collapse("show")；

$("#Invoice").val(response.data.request)；

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash)；

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#success

h2 付款成功

div 付款證明：

#preimage

```

We include it in index.pug.

```

延伸佈局


块内容

h1 Lightning App

include form.pug

include Invoice.pug

include success.pug

```