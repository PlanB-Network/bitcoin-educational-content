---
name: Lightning App
description: آموزش توسعه اولین برنامه Lightning (LAPP) شما
---

![cover](assets/cover.webp)

## یاد بگیرید اولین برنامه Lightning خود را کدنویسی کنید


الزامات:



- NodeJs >= 8
- LND >= 9


NodeJs می‌تواند از وب‌سایت رسمی آن دانلود شود.


به جای دانلود و راه‌اندازی یک نود LND، از ابزار polar استفاده خواهیم کرد که این کار را برای ما انجام می‌دهد.


برای ساخت برنامه Lightning خود، از فناوری‌های زیر استفاده خواهیم کرد:



- اکسپرس برای وب‌سرور ما
- قالب‌های Pug + بوت‌استرپ برای فرانت‌اند ما


https://planb.network/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## سیستم‌عامل


توصیه می‌شود از لینوکس استفاده کنید، اگر از ویندوز 10 استفاده می‌کنید، می‌توانید با دنبال کردن این چند مرحله یک کنسول لینوکس داشته باشید.

آماده‌سازی پایه


از ابزار تولید کننده برنامه، express، برای ایجاد سریع یک اسکلت برنامه استفاده کنید.


```
$ sudo npm install express-generator -g
```


با دستور زیر، یک برنامه Express به نام lnapp ایجاد می‌کنیم. این برنامه در یک دایرکتوری به نام lnapp در دایرکتوری کاری فعلی ایجاد خواهد شد و موتور نمایش به Pug اختصاص داده می‌شود.


```
$ express --view=pug lnapp
```


سپس وارد دایرکتوری می‌شویم و بسته‌های لازم برای اجرای وب سرور را نصب می‌کنیم.


```
$ cd myapp
$ npm install
```


اکنون به سادگی سرور را اجرا می‌کنیم


```
$ npm start
```


سپس، به این Address http://localhost:3000 در مرورگر بروید تا به برنامه دسترسی پیدا کنید.


برنامه تولید شده دارای ساختار دایرکتوری زیر است:


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


## قطبی


Polar را دانلود و نصب کنید و یک شبکه با 2 گره LND (Alice و Bob) و 1 bitcoind ایجاد کنید. هنگامی که نمودار در برنامه نشان‌دهنده گره‌های ما را مشاهده کردید، روی دکمه Start کلیک کنید و چند ثانیه صبر کنید تا نشانگر هر گره به رنگ Green تغییر کند.


برای ارسال پرداخت‌ها در شبکه لایتنینگ، لازم است که نودها از طریق کانال‌ها به یکدیگر متصل شوند. ایجاد کانال‌ها با Polar بسیار ساده است، فقط کافی است با ماوس روی یکی از گوش‌های نود Alice کلیک کرده و آن را به یکی از گوش‌های نود Bob بکشیم. بلافاصله، یک پنجره مدال با عنوان Open new channel ظاهر می‌شود، مقادیر پیش‌فرض را باقی می‌گذاریم و دکمه open channel را فشار می‌دهیم. حالا این عمل را تکرار می‌کنیم اما این بار از Bob به Alice، به این ترتیب هر دو نود می‌توانند پول ارسال و دریافت کنند.


## ندمون


برای جلوگیری از نیاز به راه‌اندازی مجدد nodejs هر بار که تغییری در کد ایجاد می‌کنیم، nodemon را نصب خواهیم کرد.


```
$ npm install nodemon -D
```


ما باید یک ورودی در بخش scripts فایل package.json ایجاد کنیم، این خط را اضافه کنید "dev": "nodemon ./bin/www"، بخش scripts باید به این صورت باشد:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


به کنسولی بروید که npm start در حال اجرا است، کلیدهای ctrl + c را فشار دهید و دوباره nodejs را این بار با استفاده از nodemon شروع کنید.


```
$ npm run dev
```


## در حال اتصال به LND


برای اتصال به یک نود لایتنینگ از nodejs، از کتابخانه LN-service استفاده خواهیم کرد، همچنین dotenv را برای مدیریت متغیرهای محیطی نصب خواهیم کرد.


```
$ npm install ln-service dotenv
```


در دایرکتوری lnapp ما، فایلی به نام .env ایجاد کنید، باید شامل این متغیرها باشد:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


به Polar برگردید، Bob را انتخاب کنید، نودی که می‌خواهیم به آن متصل شویم، به تب "Connect" بروید، محتوای GRPC Host را کپی کرده و در متغیر LND_GRPC_HOST قرار دهید، در قسمت پایین تب connect، base64 را انتخاب کنید و محتوای TLS Cert را کپی کرده و در متغیر LND_CERT_BASE64 قرار دهید، و همین کار را با admin macaroon در LND_MACAROON_BASE64 انجام دهید.


اکنون این خط را به فایل app.js که در ریشه دایرکتوری کاری قرار دارد اضافه کنید، باید آن را در اولین خط فایل کپی کنیم.


```
require('dotenv').config();
```


برای اطمینان از اینکه nodejs می‌تواند به نود ما متصل شود، فایل routes/index.js را باز کنید. این فایل مسیرها توسط express generator ایجاد شده است. ابتدا کتابخانه LN-service را نیاز داریم، بنابراین آن را در خط اول اضافه می‌کنیم.


```
const lnservice = require('ln-service');
```


ما یک مسیر جدید اضافه می‌کنیم که به ما اطلاعاتی درباره نودمان می‌دهد.


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


اکنون به این Address بروید http://localhost:3000/info


اگر یک json با اطلاعات نود LND مشاهده کردید، تبریک!!! اکنون برنامه شما می‌تواند با Lightning Network تعامل داشته باشد.

ایجاد یک مدل جعلی


برای شبیه‌سازی یک پایگاه داده، نیاز داریم یک مدل جعلی ایجاد کنیم، این به ما اجازه می‌دهد تا بدون نصب و پیکربندی یک پایگاه داده از برنامه استفاده کنیم.


ابتدا، بسته uuid را نصب کنید


```
$ npm install uuid
```


دایرکتوری models را ایجاد کنید و درون آن، فایل Post.js را با محتوای زیر ایجاد کنید:


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


## نمایش را آماده کنید


ما به بوت‌استرپ نیاز داریم تا HTML ما بهتر به نظر برسد، بنابراین فایل layout.pug واقع در دایرکتوری views را به این صورت تغییر می‌دهیم:


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


## ایجاد یک پست


برای ایجاد یک پست، به یک فرم نیاز داریم. داخل دایرکتوری views، فایلی به نام form.pug با محتوای زیر ایجاد کنید:


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


## جاوااسکریپت در فرانت‌اند


مستقیم‌ترین راهی که برای تعامل با کاربر داریم، استفاده از جاوااسکریپت در مرورگر وب است. برای این کار، فایلی به نام main.js در دایرکتوری جاوااسکریپت ایجاد کنید که ما قبلاً از layout.pug آن را فراخوانی کرده‌ایم. در این فایل، پروژه را مقداردهی اولیه کنید. محتوای اولیه main.js به صورت زیر است:


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


روی دکمه "Enviar" کلیک کنید و اگر همه چیز درست باشد، باید پیامی با عنوان "!hola" در کنسول نمایش داده شود. اکنون می‌توانیم متد App.sendBtn() را تغییر دهیم تا اطلاعات را به API خود ارسال کنیم.


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


ما همچنین متد App.makeRequest() را ایجاد کرده و به main.js اضافه می‌کنیم.


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


## ایجاد API


برای انجام این کار، باید یک فایل جدید در routes/api.js ایجاد کنیم و متدی بنویسیم که به درخواست ارسال شده در App.sendBtn() پاسخ دهد.


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


این فایل باید در app.js گنجانده شود، بنابراین این خطوط را اضافه می‌کنیم:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


بیایید دوباره دکمه ارسال را فشار دهیم و باید با همان داده‌هایی که در فرم وارد کردیم پاسخ دهد.


## Invoice را ایجاد کنید


روشی که هنگام ایجاد یک پست توسط کاربر اجرا می‌شود باید generate و Invoice را انجام دهد، سپس یک رکورد در پایگاه داده ایجاد کند که آن را به Invoice متصل کند و Invoice را به کاربر بازگرداند تا بتواند آن را پرداخت کند.


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


اگر پس از فشردن دکمه ارسال، یک شیء پست به عنوان پاسخ دریافت کنیم، همه چیز به درستی پیش رفته است. اکنون باید متن را نمایش دهیم تا کاربر بتواند آن را پرداخت کند.


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


## نمای جدید Invoice


در پوشه views، باید فایلی به نام Invoice.pug با محتوای زیر ایجاد کنیم:


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


و آن را در index.pug بگنجانید.


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## تغییر App.sendBtn()


اکنون ما App.sendBtn() را تغییر می‌دهیم تا داده‌های به‌دست‌آمده را نمایش دهد:


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


## دریافت پرداخت


ما نیاز داریم بدانیم چه زمانی پرداخت را دریافت می‌کنیم، برای این منظور از متد subscribeToInvoices() از lnservice استفاده خواهیم کرد، این متد به ما اجازه می‌دهد تا زمانی که وضعیت یک Invoice به‌روزرسانی شده است، کد اجرا کنیم، برای استفاده از آن این خطوط را در app.js اضافه می‌کنیم.


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


یک متد HTTP GET در API ما ایجاد کنید تا کاربر بتواند بررسی کند که آیا Hash پرداخت شده است یا خیر.


````

```fa
router.get('/post/:Hash', (req, res) => {
```

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

```plaintext
const response = await App.makeRequest({
```

api: `post/${Hash}`,

});

اگر (response.success && response.data.paid) {

console.log("پرداخت انجام شد");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

```plaintext
const response = await App.makeRequest({
```

api: `post/${Hash}`,

});

اگر (response.success && response.data.paid) {

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

```plaintext
const response = await App.makeRequest({
```

api: "پست",

پست: { نام، محتوا },

});

اگر (!response) console.error("خطا در دریافت داده!");

اگر (response.success) {

$("#post-form").collapse("hide");

$("#Invoice-form").collapse("show");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#موفقیت

h2 پرداخت موفقیت‌آمیز

div اثبات پرداخت:

#پیش‌تصویر

```

We include it in index.pug.

```

گسترش می‌دهد layout


مسدود کردن محتوا

h1 برنامه رعد و برق

فرم.pug را وارد کنید

شامل کردن Invoice.pug

شامل کردن success.pug

```