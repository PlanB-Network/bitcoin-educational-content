---
name: Lightning App
description: 첫 번째 라이트닝 앱(LAPP) 개발을 위한 튜토리얼
---
![cover](assets/cover.webp)

## 첫 번째 라이트닝 앱 코딩 배우기


요구 사항:



- NodeJs >= 8
- LND >= 9


NodeJs는 공식 웹사이트에서 다운로드할 수 있습니다


LND 노드를 다운로드하고 설정하는 대신 이 작업을 대신 수행할 폴라 도구를 사용하겠습니다.


Lightning 앱을 구축하기 위해 다음 기술을 사용할 것입니다:



- 웹서버용 Express
- 프론트엔드를 위한 Pug 템플릿 + 부트스트랩


https://planb.network/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## 운영 체제


Linux를 사용하는 것이 좋습니다. Windows 10을 사용하는 경우 다음 몇 가지 단계에 따라 Linux 콘솔을 사용할 수 있습니다.

베이스 준비하기


애플리케이션 생성기 도구인 Express를 사용하여 애플리케이션 스켈레톤을 빠르게 생성할 수 있습니다.


```
$ sudo npm install express-generator -g
```


다음 지침에 따라 lnapp이라는 Express 애플리케이션을 생성합니다. 애플리케이션은 현재 작업 디렉터리의 lnapp이라는 디렉터리에 생성되고 뷰 엔진은 Pug에 할당됩니다.


```
$ express --view=pug lnapp
```


그런 다음 디렉토리에 들어가 웹 서버를 실행하는 데 필요한 패키지를 설치합니다.


```
$ cd myapp
$ npm install
```


이제 서버를 실행하기만 하면 됩니다


```
$ npm start
```


그런 다음 브라우저에서 이 Address http://localhost:3000 로 이동하여 애플리케이션에 액세스합니다.


생성된 애플리케이션의 디렉토리 구조는 다음과 같습니다:


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


Polar를 다운로드하고 설치한 다음, 2개의 LND 노드(Alice 및 Bob)와 1개의 bitcoind으로 네트워크를 생성합니다. 앱에 노드가 표시된 그래프가 나타나면 시작 버튼을 클릭하고 각 노드의 표시기가 Green로 색이 바뀔 때까지 몇 초간 기다립니다.


라이트닝에서 결제를 전송하려면 채널을 통해 노드를 상호 연결해야 합니다. Polar로 채널을 만드는 것은 매우 간단합니다. Alice 노드의 귀 중 하나를 마우스로 클릭하고 Bob 노드의 귀 중 하나로 드래그하기만 하면 됩니다. 즉시 새 채널 열기라는 제목의 모달 창이 나타나면 기본값을 그대로 두고 채널 열기 버튼을 누릅니다. 이제 같은 작업을 반복하지만 이번에는 Bob에서 Alice로 이동하여 두 노드 모두 송금을 주고받을 수 있습니다.


## 노데몬


코드를 변경할 때마다 nodejs를 다시 시작하지 않으려면 nodemon을 설치합니다


```
$ npm install nodemon -D
```


Package.json 파일의 스크립트 섹션에 항목을 생성하고 "dev" 줄을 추가해야 합니다: "nodemon ./bin/www", 스크립트 섹션은 다음과 같이 표시되어야 합니다:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Npm 시작이 실행 중인 콘솔로 이동하여 ctrl + c를 누르고 nodejs를 다시 시작하되 이번에는 nodemon을 사용합니다


```
$ npm run dev
```


## LND에 연결


Nodejs에서 Lightning 노드에 연결하기 위해 LN 서비스 라이브러리를 사용하고 환경 변수를 관리하기 위해 dotenv도 설치합니다.


```
$ npm install ln-service dotenv
```


Lnapp 디렉토리에 .env라는 파일을 만들고 이 파일에는 이러한 변수가 포함되어야 합니다:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Polar로 돌아가서 연결하려는 노드인 Bob를 선택하고 "연결" 탭으로 이동하여 GRPC Host의 내용을 복사하여 LND_GRPC_HOST 변수에 넣고, 연결 탭의 하단에서 base64를 선택하고 TLS Cert의 내용을 복사하여 LND_CERT_BASE64 변수에 넣고, 관리자 마카롱도 LND_MACAROON_BASE64에 동일하게 넣습니다.


이제 작업 디렉터리의 루트에 있는 app.js 파일에 이 줄을 추가하고 파일의 첫 줄에 복사해야 합니다.


```
require('dotenv').config();
```


Nodejs가 우리 노드에 연결할 수 있는지 확인하려면 routes/index.js 파일을 열고, 이 경로 파일은 express 생성기에 의해 생성되었으며, 먼저 LN 서비스 라이브러리가 필요하므로 첫 번째 줄에 추가합니다


```
const lnservice = require('ln-service');
```


노드에 대한 정보를 제공하는 새 경로를 추가합니다.


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


이제 이 Address로 이동하세요 http://localhost:3000/info


LND 노드 정보가 포함된 json이 표시되면 축하합니다!!! 이제 앱이 Lightning Network와 상호 작용할 수 있습니다.

가짜 모델 만들기


데이터베이스를 시뮬레이션하려면 가짜 모델을 만들어야 하는데, 이렇게 하면 데이터베이스를 설치 및 구성하지 않고도 앱을 사용할 수 있습니다.


먼저 uuid 패키지를 설치합니다


```
$ npm install uuid
```


Models 디렉터리를 만들고 그 안에 다음 내용으로 Post.js 파일을 만듭니다:


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


## 뷰 준비


HTML을 더 보기 좋게 만들려면 부트스트랩이 필요하므로 뷰 디렉터리에 있는 layout.pug 파일을 다음과 같이 수정합니다:


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


## 글 만들기


글을 만들려면 양식이 필요합니다. 보기 디렉터리 내에 다음 내용으로 form.pug라는 파일을 만듭니다:


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


## 프론트엔드의 자바스크립트


사용자와 상호작용하는 가장 직접적인 방법은 웹 브라우저에서 자바스크립트를 사용하는 것입니다. 이를 위해 layout.pug에서 이미 호출하고 있는 javascript 디렉토리에 main.js라는 파일을 만듭니다. 이 파일에서 프로젝트를 초기화합니다. Main.js의 초기 내용은 다음과 같습니다:


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


"Enviar" 버튼을 클릭하고 모든 것이 정상이면 콘솔에 "!hola"라는 메시지가 표시됩니다. 이제 App.sendBtn() 메서드를 수정하여 정보를 API로 전송할 수 있습니다.


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


또한 App.makeRequest() 메서드를 생성하여 main.js에 추가합니다


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


## API 만들기


이렇게 하려면 routes/api.js에 새 파일을 만들고 App.sendBtn() 내에서 요청에 응답하는 메서드를 작성해야 합니다.


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


이 파일은 app.js에 포함되어야 하므로 다음 줄을 추가합니다:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


다시 보내기 버튼을 누르면 양식에 입력한 것과 동일한 데이터가 응답할 것입니다.


## Invoice 생성


사용자가 글을 작성할 때 실행되는 메서드는 generate에 Invoice를 생성한 다음 데이터베이스에 Invoice에 연결되는 레코드를 생성하고 사용자에게 Invoice를 반환하여 결제할 수 있도록 해야 합니다.


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


이와 같이 보내기를 누른 후 응답으로 게시물 객체를 받으면 모든 것이 올바르게 진행되었습니다. 이제 사용자가 결제할 수 있도록 텍스트를 표시해야 합니다.


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


## 새로운 Invoice 보기


보기 디렉토리에 다음 내용으로 Invoice.pug라는 파일을 만들어야 합니다:


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


그리고 index.pug에 포함하세요


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## App.sendBtn() 수정하기


이제 획득한 데이터를 표시하도록 App.sendBtn()을 수정합니다:


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


## 결제 받기


결제를 언제 받을지 알아야 하는데, 이를 위해 lnservice의 subscribeToInvoices() 메서드를 사용할 것입니다. 이 메서드를 사용하면 Invoice의 상태가 업데이트되었을 때 코드를 실행할 수 있으며, 이를 사용하려면 app.js에 이 줄을 추가합니다.


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


사용자가 Hash이 결제되었는지 확인할 수 있도록 API에 HTTP GET 메서드를 생성합니다.


````

라우터.get('/post/:Hash', (req, res) => {

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

api: `post/${Hash}`,

});

if (response.success && response.data.paid) {

console.log("결제 완료");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = 비동기 (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`,

});

if (response.success && response.data.paid) {

clearInterval(App.interval);

App.interval = null;

$("#Invoice-form").collapse("hide");

$("#preimage").text(response.data.preimage);

$("#success").collapse("show");

}

};


App.sendBtn = async () => {

const name = $("#name").val();

const content = $("#content").val();

const response = await App.makeRequest({

api: "post",

post: { 이름, 콘텐츠 },

});

if (!response) console.error("데이터 가져오기 오류!");

if (response.success) {

$("#post-form").collapse("hide");

$("#Invoice-form").collapse("show");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#성공

h2 결제 성공

div 결제 증명:

#프리이미지

```

We include it in index.pug.

```

레이아웃 확장


콘텐츠 차단

h1 라이트닝 앱

form.pug 포함

gW-34.pug 포함

성공.pug 포함

```