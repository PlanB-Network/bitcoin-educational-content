---
name: Lightning App
description: Учебно ръководство за разработване на първия ви Lightning App (LAPP)
---
![cover](assets/cover.webp)

## Научете се да програмирате първото си приложение Lightning


Изисквания:



- NodeJs >= 8
- LND >= 9


NodeJs може да бъде изтеглен от официалния му уебсайт


Вместо да изтегляме и настройваме възел LND, ще използваме инструмента polar, който ще изпълни тази задача вместо нас.


За създаването на нашето приложение Lightning ще използваме следните технологии:



- Express за нашия уеб сървър
- Шаблони за мопс + bootstrap за нашия frontend


https://planb.academy/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## Операционна система


Препоръчително е да използвате Linux, но ако сте с Windows 10, можете да използвате конзола за Linux, като следвате тези няколко стъпки.

Подготовка на основата


Използвайте инструмента за генериране на приложения - Express, за да създадете бързо скелет на приложение.


```
$ sudo npm install express-generator -g
```


Със следната инструкция създаваме приложение Express, наречено lnapp. Приложението ще бъде създадено в директория, наречена lnapp, в текущата работна директория, а механизмът за изглед ще бъде назначен на Pug.


```
$ express --view=pug lnapp
```


След това влизаме в директорията и инсталираме необходимите пакети, за да работи уеб сървърът.


```
$ cd myapp
$ npm install
```


Сега просто стартираме сървъра


```
$ npm start
```


След това отидете на този адрес http://localhost:3000 в браузъра, за да получите достъп до приложението.


Генерираното приложение има следната структура на директориите:


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


Изтеглете Polar, инсталирайте го и създайте мрежа с 2 възела LND (Alice и Bob) и 1 bitcoind. След като видим графиката в приложението, показваща нашите възли, щракнете върху бутона Start (Старт) и изчакайте няколко секунди, докато индикаторът на всеки възел промени цвета си на зелен.


За да можете да изпращате плащания чрез Lightning, е необходимо възлите да са свързани помежду си чрез канали. Създаването на канали с помощта на Polar е много лесно, просто трябва да щракнем с мишката върху едно от ушите на възел Alice и да го плъзнем към едно от ушите на възел Bob. Веднага трябва да се появи модален прозорец със заглавие Open new channel (Отвори нов канал), оставяме стойностите по подразбиране и натискаме бутона Open channel (Отвори канал). Сега повтаряме действието, но този път от Bob към Alice, като по този начин и двата възела могат да изпращат и получават пари.


## Nodemon


За да не се налага да рестартираме nodejs всеки път, когато направим промяна в кода, ще инсталираме nodemon


```
$ npm install nodemon -D
```


Трябва да създадем запис в раздела за скриптове на файла package.json, да добавим този ред "dev": "nodemon ./bin/www", разделът със скриптове трябва да изглежда така:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Отидете в конзолата, където се изпълнява npm start, натиснете ctrl + c и стартирайте nodejs отново, но този път с помощта на nodemon


```
$ npm run dev
```


## Свързване с LND


За да се свържем с възел Lightning от nodejs, ще използваме библиотеката ln-service, ще инсталираме и dotenv за управление на променливите на средата.


```
$ npm install ln-service dotenv
```


В директорията lnapp създайте файл, наречен .env, който трябва да съдържа тези променливи:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Върнете се в Polar, изберете Bob, възела, към който искаме да се свържем, отидете в раздела "Свързване", копирайте съдържанието на GRPC Host и го поставете в променливата LND_GRPC_HOST, в долната част на раздела за свързване изберете base64 и копирайте съдържанието на TLS Cert и го поставете в променливата LND_CERT_BASE64, и направете същото с администраторския macaroon в LND_MACAROON_BASE64.


Сега добавете този ред към файла app.js, разположен в корена на работната директория, като трябва да го копирате на първия ред на файла.


```
require('dotenv').config();
```


За да проверите дали nodejs може да се свърже с нашия възел, отворете файла routes/index.js, този файл е създаден от генератора на експресни маршрути, първо изискваме библиотеката ln-service, така че я добавяме на първия ред


```
const lnservice = require('ln-service');
```


Добавяме нов маршрут, който ще ни даде информация за нашия възел.


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


Сега отидете на този адрес http://localhost:3000/info


Ако видите json с информацията за възела LND, поздравления!!! Приложението ви вече може да взаимодейства с Lightning Network.

Създаване на фалшив модел


За да симулираме база данни, трябва да създадем фалшив модел, който ще ни позволи да използваме приложението, без да инсталираме и конфигурираме база данни.


Първо, инсталирайте пакета uuid


```
$ npm install uuid
```


Създайте директорията models и в нея създайте файла Post.js със следното съдържание:


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


## Подготовка на изгледа


Нуждаем се от bootstrap, за да направим нашия html да изглежда по-добре, затова променяме файла layout.pug, намиращ се в директорията views, така че да изглежда по следния начин:


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


## Създаване на публикация


За да създадем публикация, ни е необходим формуляр. В директорията views създайте файл, наречен form.pug, със следното съдържание:


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


## Javascript във frontend


Най-прекият начин за взаимодействие с потребителя е използването на javascript в уеб браузъра. За тази цел създайте файл, наречен main.js, в директорията с javascript, който вече извикваме от layout.pug. В този файл инициализирайте проекта. Началното съдържание на main.js е следното:


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


Щракнете върху бутона "Enviar" и ако всичко е наред, в конзолата трябва да се появи съобщение "!hola". Сега можем да модифицираме метода App.sendBtn(), за да изпратим информацията до нашия API.


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


Създаваме и метода App.makeRequest() и го добавяме в main.js


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


## Създаване на API


За да направим това, трябва да създадем нов файл в routes/api.js и да напишем метода, който отговаря на заявката, направена в App.sendBtn().


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


Този файл трябва да бъде включен в app.js, затова добавяме тези редове:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Натиснете отново бутона за изпращане и той трябва да отговори със същите данни, които въведохме във формуляра.


## Създаване на фактурата


Методът, който се изпълнява, когато потребителят създаде публикация, трябва да generate фактура, след това да създаде запис в базата данни, който да я свързва с фактурата, и да върне фактурата на потребителя, за да може той да я плати.


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


Ако след натискане на бутона "Изпрати" получим като отговор пост обект, както е показано тук, всичко е преминало правилно. Сега трябва да покажем текста, за да може потребителят да го плати.


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


## Нов изглед на фактурата


В директорията с изгледи трябва да създадем файл, наречен invoice.pug, със следното съдържание:


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


И го включете в index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Модифициране на App.sendBtn()


Сега модифицираме App.sendBtn(), за да покажем получените данни:


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


## Получаване на плащането


Трябва да знаем кога ще получим плащането, за това ще използваме метода subscribeToInvoices() от lnservice, този метод ни позволява да изпълняваме код, когато статусът на дадена фактура е актуализиран, за да го използваме, добавяме тези редове в app.js.


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


Създайте HTTP GET метод в нашия API, за да може потребителят да провери дали е платен даден хеш.


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

if (response.success && response.data.paid) {

console.log("Плащането е извършено");

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

публикация: { name, content },

});

if (!response) console.error("Грешка при получаване на данни!");

if (response.success) {

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

h2 Успешно плащане

div Доказателство за плащане:

#preimage

```

We include it in index.pug.

```

разширява оформлението


съдържание на блока

h1 Lightning App

включване на form.pug

включване на invoice.pug

включва success.pug

```