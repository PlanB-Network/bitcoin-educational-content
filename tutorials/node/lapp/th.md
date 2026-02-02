---
name: Lightning App
description: บทแนะนำการพัฒนา Lightning App (LAPP) แรกของคุณ
---
![cover](assets/cover.webp)

## เรียนรู้การเขียนโค้ดแอปสายฟ้าแรกของคุณ


ข้อกำหนด:



- NodeJs >= 8
- LND >= 9


NodeJs สามารถดาวน์โหลดได้จากเว็บไซต์ทางการของมัน


แทนที่จะดาวน์โหลดและตั้งค่าโหนด LND เราจะใช้เครื่องมือ polar ซึ่งจะทำงานนี้ให้เรา


ในการสร้างแอป Lightning ของเรา เราจะใช้เทคโนโลยีดังต่อไปนี้:



- Express สำหรับเว็บเซิร์ฟเวอร์ของเรา
- Pug templates + bootstrap สำหรับ frontend ของเรา


https://planb.academy/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## ระบบปฏิบัติการ


แนะนำให้ใช้ Linux หากคุณใช้ Windows 10 คุณสามารถมีคอนโซล Linux ได้โดยทำตามขั้นตอนเหล่านี้

กำลังเตรียมฐาน


ใช้เครื่องมือสร้างแอปพลิเคชัน express เพื่อสร้างโครงร่างแอปพลิเคชันอย่างรวดเร็ว


```
$ sudo npm install express-generator -g
```


ด้วยคำแนะนำต่อไปนี้ เราจะสร้างแอปพลิเคชัน Express ที่ชื่อว่า lnapp แอปพลิเคชันจะถูกสร้างในไดเรกทอรีที่ชื่อว่า lnapp ในไดเรกทอรีการทำงานปัจจุบัน และจะกำหนดให้ view engine เป็น Pug


```
$ express --view=pug lnapp
```


จากนั้นเราจะเข้าสู่ไดเรกทอรีและติดตั้งแพ็กเกจที่จำเป็นสำหรับการทำงานของเว็บเซิร์ฟเวอร์


```
$ cd myapp
$ npm install
```


ตอนนี้เราเพียงแค่รันเซิร์ฟเวอร์


```
$ npm start
```


ถัดไป ไปที่ที่อยู่นี้ http://localhost:3000 ในเบราว์เซอร์เพื่อเข้าถึงแอปพลิเคชัน


แอปพลิเคชันที่สร้างขึ้นมีโครงสร้างไดเรกทอรีดังต่อไปนี้:


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


## ขั้วโลก


ดาวน์โหลด Polar ติดตั้งและสร้างเครือข่ายด้วยโหนด LND จำนวน 2 โหนด (Alice และ Bob) และ 1 bitcoind เมื่อเราเห็นกราฟในแอปที่แสดงโหนดของเราแล้ว ให้คลิกที่ปุ่มเริ่มและรอสักครู่จนกว่าตัวบ่งชี้ของแต่ละโหนดจะเปลี่ยนเป็นสีเขียว


ในการส่งการชำระเงินบน Lightning จำเป็นที่โหนดจะต้องเชื่อมต่อกันผ่านช่องทาง การสร้างช่องทางด้วย Polar นั้นง่ายมาก เราเพียงแค่คลิกที่หูข้างหนึ่งของโหนด Alice และลากไปยังหูข้างหนึ่งของโหนด Bob ทันทีจะมีหน้าต่างโมดัลชื่อ Open new channel ปรากฏขึ้น เราปล่อยค่าเริ่มต้นไว้และกดปุ่มเปิดช่องทาง ตอนนี้เราทำซ้ำการกระทำแต่คราวนี้จาก Bob ไปยัง Alice ด้วยวิธีนี้โหนดทั้งสองสามารถส่งและรับเงินได้


## Nodemon


เพื่อหลีกเลี่ยงการต้องรีสตาร์ท nodejs ทุกครั้งที่เราทำการเปลี่ยนแปลงในโค้ด เราจะติดตั้ง nodemon


```
$ npm install nodemon -D
```


เราต้องสร้างรายการในส่วนของสคริปต์ในไฟล์ package.json เพิ่มบรรทัดนี้ "dev": "nodemon ./bin/www", ส่วนของสคริปต์ควรมีลักษณะดังนี้:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


ไปที่คอนโซลที่กำลังรัน npm start กด ctrl + c และเริ่ม nodejs อีกครั้งแต่คราวนี้ใช้ nodemon


```
$ npm run dev
```


## กำลังเชื่อมต่อกับ LND


ในการเชื่อมต่อกับ Lightning node จาก nodejs เราจะใช้ไลบรารี ln-service และเราจะติดตั้ง dotenv เพื่อจัดการตัวแปรสภาพแวดล้อม


```
$ npm install ln-service dotenv
```


ในไดเรกทอรี lnapp ของเรา สร้างไฟล์ชื่อ .env ซึ่งควรมีตัวแปรเหล่านี้:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


กลับไปที่ Polar เลือก Bob ซึ่งเป็นโหนดที่เราต้องการเชื่อมต่อ ไปที่แท็บ "Connect" คัดลอกเนื้อหาของ GRPC Host และวางลงในตัวแปร LND_GRPC_HOST ในส่วนล่างของแท็บ connect เลือก base64 และคัดลอกเนื้อหาของ TLS Cert และวางลงในตัวแปร LND_CERT_BASE64 และทำเช่นเดียวกันกับ admin macaroon ใน LND_MACAROON_BASE64


ตอนนี้เพิ่มบรรทัดนี้ไปที่ไฟล์ app.js ซึ่งอยู่ในรูทของไดเรกทอรีการทำงาน เราต้องคัดลอกมันไปไว้ที่บรรทัดแรกของไฟล์


```
require('dotenv').config();
```


ในการตรวจสอบว่า nodejs สามารถเชื่อมต่อกับโหนดของเราได้ ให้เปิดไฟล์ routes/index.js ไฟล์ routes นี้ถูกสร้างขึ้นโดย express generator ก่อนอื่นเราต้องการใช้ไลบรารี ln-service ดังนั้นเราจึงเพิ่มมันในบรรทัดแรก


```
const lnservice = require('ln-service');
```


เราเพิ่มเส้นทางใหม่ที่จะให้ข้อมูลเกี่ยวกับโหนดของเรา


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


ตอนนี้ไปที่ที่อยู่นี้ http://localhost:3000/info


หากคุณเห็น json ที่มีข้อมูลของโหนด LND ขอแสดงความยินดี!!! แอปของคุณสามารถโต้ตอบกับ Lightning Network ได้แล้ว

สร้างโมเดลปลอม


ในการจำลองฐานข้อมูล เราจำเป็นต้องสร้างโมเดลปลอม ซึ่งจะช่วยให้เราสามารถใช้แอปได้โดยไม่ต้องติดตั้งและกำหนดค่าฐานข้อมูล


ก่อนอื่น ติดตั้งแพ็กเกจ uuid


```
$ npm install uuid
```


สร้างไดเรกทอรี models และภายในนั้น สร้างไฟล์ Post.js ด้วยเนื้อหาดังต่อไปนี้:


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


## เตรียมมุมมอง


เราต้องการ bootstrap เพื่อทำให้ html ของเราดูดีขึ้น ดังนั้นเราจึงแก้ไขไฟล์ layout.pug ที่อยู่ในไดเรกทอรี views ให้มีลักษณะดังนี้:


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


## กำลังสร้างโพสต์


ในการสร้างโพสต์ เราจำเป็นต้องมีฟอร์ม ภายในไดเรกทอรี views ให้สร้างไฟล์ชื่อ form.pug พร้อมด้วยเนื้อหาดังต่อไปนี้:


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


## JavaScript ในส่วนหน้าของเว็บไซต์


วิธีที่ตรงที่สุดที่เรามีในการโต้ตอบกับผู้ใช้คือการใช้ javascript ในเว็บเบราว์เซอร์ สำหรับสิ่งนี้ ให้สร้างไฟล์ชื่อ main.js ในไดเรกทอรี javascript ซึ่งเราได้เรียกจาก layout.pug แล้ว ในไฟล์นี้ ให้เริ่มต้นโปรเจกต์ เนื้อหาเริ่มต้นของ main.js มีดังนี้:


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


คลิกปุ่ม "Enviar" และหากทุกอย่างถูกต้อง ควรแสดงข้อความ "!hola" ในคอนโซล ตอนนี้เราสามารถแก้ไขเมธอด App.sendBtn() เพื่อส่งข้อมูลไปยัง API ของเราได้


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


เรายังสร้างเมธอด App.makeRequest() และเพิ่มลงใน main.js


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


## สร้าง API


ในการทำเช่นนี้ เราจำเป็นต้องสร้างไฟล์ใหม่ใน routes/api.js และเขียนเมธอดที่ตอบสนองต่อคำขอที่ทำภายใน App.sendBtn().


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


ไฟล์นี้จะต้องถูกรวมใน app.js ดังนั้นเราจึงเพิ่มบรรทัดเหล่านี้:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


ลองกดปุ่มส่งอีกครั้งและมันควรตอบกลับด้วยข้อมูลเดียวกับที่เราป้อนในแบบฟอร์ม


## สร้างใบแจ้งหนี้


วิธีการที่ถูกดำเนินการเมื่อผู้ใช้สร้างโพสต์ควร generate ใบแจ้งหนี้ จากนั้นสร้างบันทึกในฐานข้อมูลที่เชื่อมโยงกับใบแจ้งหนี้ และส่งคืนใบแจ้งหนี้ให้กับผู้ใช้เพื่อให้พวกเขาสามารถชำระเงินได้


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


หากเราได้รับวัตถุโพสต์เป็นการตอบกลับหลังจากกดส่งแบบนี้ แสดงว่าทุกอย่างถูกต้องแล้ว ตอนนี้เราจำเป็นต้องแสดงข้อความเพื่อให้ผู้ใช้สามารถชำระเงินได้


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


## มุมมองใบแจ้งหนี้ใหม่


ในไดเรกทอรี views เราจำเป็นต้องสร้างไฟล์ชื่อ invoice.pug ด้วยเนื้อหาดังต่อไปนี้:


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


และรวมไว้ใน index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## กำลังแก้ไข App.sendBtn()


ตอนนี้เราแก้ไข App.sendBtn() เพื่อแสดงข้อมูลที่ได้รับ:


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


## ได้รับการชำระเงิน


เราจำเป็นต้องทราบเมื่อเราได้รับการชำระเงิน สำหรับสิ่งนี้เราจะใช้เมธอด subscribeToInvoices() จาก lnservice เมธอดนี้ช่วยให้เราสามารถเรียกใช้โค้ดเมื่อสถานะของใบแจ้งหนี้ได้รับการอัปเดต เพื่อใช้งานเราจะเพิ่มบรรทัดเหล่านี้ใน app.js


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


สร้าง HTTP GET method ใน API ของเราเพื่อให้ผู้ใช้ตรวจสอบว่า hash ได้รับการชำระเงินหรือไม่


````

router.get('/post/:hash', (req, res) => {

const { hash } = req.params;'

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

App.waitPayment = async (hash) => {

const response = await App.makeRequest({

api: `post/${hash}`,

});

ถ้า (response.success && response.data.paid) {

console.log("Payment made");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (hash) => {

const response = await App.makeRequest({

api: `post/${hash}`,

});

ถ้า (response.success && response.data.paid) {

ล้างการตั้งค่า App.interval;

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

โพสต์: { ชื่อ, เนื้อหา },

});

หาก (!response) console.error("Error getting data!");

ถ้า (response.success) {

$("#post-form").collapse("hide");

$("#invoice-form").collapse("show");

$("#invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#success

h2 การชำระเงินสำเร็จ

div หลักฐานการชำระเงิน:

#preimage

```

We include it in index.pug.

```

ขยายเค้าโครง


บล็อกเนื้อหา

h1 Lightning App

include form.pug

include invoice.pug

รวม success.pug

```