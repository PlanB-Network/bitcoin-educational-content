---
name: Lightning App
description: Inyigisho zo gutegura porogaramu yawe ya mbere y'umuravyo (LAPP)
---
![cover](assets/cover.webp)

## Iga gukora code ya porogaramu yawe ya mbere y'umuravyo


Ibisabwa:



- InyugutiJs >= 8
- LND >= 9


NodeJs ishobora gukurwa ku rubuga rwayo rwemewe .


Aho gukura no gushinga node ya LND, tuzokoresha igikoresho ca polar, kizodukorera ico gikorwa.


Kugira ngo twubake app yacu ya Lightning, tuzoba turiko turakoresha ubuhinga bukurikira:



- Ivuge ku rubuga rwacu
- Ivyitegererezo vya Pug + bootstrap y'imbere yacu


https://planb.network/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## Uburyo bwo gukoresha


Ni vyiza gukoresha Linux, iyo uri kuri Windows 10 ushobora kugira console ya Linux ukurikije izi ntambwe nke.

Gutegura ishingiro


Koresha igikoresho co guhingura ibikorwa, express, kugira ngo ukore ningoga umubiri w’ibikorwa.


```
$ sudo npm install express-generator -g
```


Dukoresheje amabwirizwa akurikira, duca dukora porogarama ya Express yitwa lnapp. Iryo koraniro rizoremwa mu bubiko bwitwa lnapp mu bubiko bukora ubu, kandi moteri y’ukureba izohabwa Pug.


```
$ express --view=pug lnapp
```


Hanyuma twinjira mu bubiko maze tugashiramwo amapaki akenewe kugira ngo server y’urubuga ikore.


```
$ cd myapp
$ npm install
```


Ubu rero dukoresha server


```
$ npm start
```


Inyuma y’aho, genda kuri iyi Address http://localhost:3000 mu mucukumbuzi kugira ngo ushikire porogarama.


Porogaramu yashizweho ifise ububiko bukurikira:


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


Gukuraho Polar, uyishiremwo, hanyuma ureme urubuga rufise ama node 2 LND (Alice na Bob) na 1 bitcoind. Tumaze kubona igicapo muri app kigaragaza utugingo ngengabuzima twacu, dufyonde kuri buto ya Start maze urindire amasegonda makeyi gushika ikimenyetso c’utugingo ngengabuzima twose gihinduye ibara kikaba Green.


Kugira ngo umuntu yohereze amahera kuri Lightning, birakenewe ko izo node zihuzwa biciye ku mihora. Gukora imirongo na Polar biroroshe cane, dukeneye gusa gukanda n’imbeba kuri rimwe mu matwi y’uruzitiro rwa Alice tukayikwegera kuri rimwe mu matwi y’uruzitiro rwa Bob. Ubwo nyene, idirisha ry’uburyo ryitwa Gufungura umurongo mushasha rikwiye guseruka, tugasiga agaciro ka mbere maze tugakanda buto y’umurongo mushasha. Ubu rero turasubiramwo igikorwa ariko ubu kuva kuri Bob gushika kuri Alice, muri ubwo buryo izo node zompi zishobora kohereza no kwakira amahera.


## Nodemoni


Kugira ngo ntitube dusubira gutangura nodejs igihe cose duhinduye kode, tuzoshiramwo nodemon .


```
$ npm install nodemon -D
```


Tubwirizwa gukora inyandiko mu gice c'inyandiko ca dosiye package.json, twongereko uyu murongo "dev": "nodemon ./bin/www", igice c'inyandiko gikwiye gusa n'iki:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Genda kuri console aho npm start iriko irakora, ukande ctrl + c hanyuma wongere utangure nodejs ariko ubu ukoresheje nodemon .


```
$ npm run dev
```


## Guhuza na LND


Kugira ngo twifatanye n’uruzitiro rwa Lightning ruvuye kuri nodejs, tuzokoresha ububiko bw’ibitabu bwa LN-service, tuzoshiramwo kandi dotenv kugira ngo ducunge ibihinduka vy’ibidukikije.


```
$ npm install ln-service dotenv
```


Mu bubiko bwacu bwa lnapp, rema dosiye yitwa .env, igomba kubamwo ibi bihinduka:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Subira kuri Polar, uhitemwo Bob, node dushaka gufatanya, genda ku rubuga "Gufatanya", ukope ibirimwo GRPC Host maze ubishire mu mpinduka LND_GRPC_HOST, mu gice co hasi c'uruzitiro rwo gufatanya uhitemwo base64 maze ukope ibiri muri TLS Cert na L4. umuyobozi w'imakaroni muri LND_IKARONI_ISHIMIKIRO64.


Ubu rero wongere uyu murongo kuri dosiye app.js iri mu muzi w’ububiko bukora, dutegerezwa kuyikopa ku murongo wa mbere wa dosiye.


```
require('dotenv').config();
```


Kugira ngo umenye neza ko nodejs ishobora kwifatanya na node yacu, fungura dosiye routes/index.js, iyi dosiye routes yaremwe n’umuhinguzi w’ibintu vyihuta, mbere dusaba ububiko bw’ibitabu bwa LN-service, rero turayishira ku murongo wa mbere


```
const lnservice = require('ln-service');
```


Twongerako inzira nshasha izoduha amakuru yerekeye urudodo rwacu.


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


Ubu rero genda kuri iyi Address http://umushitsi wo mu karere:3000/amakuru


Niwabona json irimwo amakuru y'uruzitiro rwa LND, urakoze!!! porogaramu yawe ubu irashobora gukorana na Lightning Network.

Guhingura ikigereranyo c'ikinyoma


Kugira ngo twigane urutonde rw’amakuru, turakeneye gukora ikigereranyo c’ikinyoma, ivyo bizodufasha gukoresha app ata gushiramwo no gutunganya urutonde rw’amakuru.


Ubwambere, shiramwo umuzigo wa uuid


```
$ npm install uuid
```


Rema ububiko bw'ibigereranyo maze imbere muri bwo, ureme dosiye ya Post.js irimwo ibi bikurikira:


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


## Gutegura ivyerekanwa


Turakeneye bootstrap kugira html yacu isa neza, rero turahindura dosiye layout.pug iri mu bubiko bw'ivyo tubona kugira ngo isa n'iyi:


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


## Gukora ivyashizweho


Kugira ngo dukore post, turakeneye urupapuro. Imbere mu bubiko bw'ibigaragara, rema dosiye yitwa form.pug irimwo ibi bikurikira:


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


## Inyandiko ya Java iri imbere


Uburyo butaziguye cane dufise bwo gukorana n’uwukoresha ni ugukoresha javascript mu mucukumbuzi w’urubuga. Ku bw’ivyo, nushireho dosiye yitwa main.js mu bubiko bwa javascript, iyo turiko turayihamagara tuvuye kuri layout.pug. Muri iyi dosiye, tangura umugambi. Ibiri muri main.js ni ibi bikurikira:


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


Fyonda kuri buto ya "Enviar" maze nimba vyose bimeze neza, bikwiye kwerekana ubutumwa "!hola" muri console. Ubu turashobora guhindura uburyo bwa App.sendBtn() kugira ngo twohereze amakuru kuri API yacu.


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


Turarema kandi uburyo App.makeRequest () tukabwongera kuri main.js .


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


## Rema API


Kugira ivyo tubishikeko, turakeneye gukora dosiye nshasha muri routes/api.js maze tukandika uburyo bwishura ku busabe bwakozwe muri App.sendBtn().


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


Iyi dosiye itegerezwa kuba iri muri app.js, rero twongerako iyi mirongo:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Reka dusubire gukanda kuri buto yo kohereza kandi ikwiye kwishura n’amakuru nyene twinjije muri iyo form.


## Rema Invoice


Uburyo bukoreshwa iyo umukoresha akoze ikiganiro bukwiye generate an Invoice, hanyuma akora inyandiko mu rutonde rw’amakuru ihuza na Invoice, hanyuma akagarukana Invoice ku mukoresha kugira ngo bashobore kuyihemba.


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


Iyo twakiriye ikintu co gushiramwo nk’inyishu tumaze gukanda send, nk’ibi, vyose vyagenda neza. Ubu rero turakeneye kwerekana umwandiko kugira ngo uwuwukoresha ashobore kuwutanga.


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


## Imbonerahamwe nshasha ya Invoice


Mu bubiko bw'ivyo tubona, dukeneye gukora dosiye yitwa Invoice.pug irimwo ibi bikurikira:


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


Kandi ubishire muri index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Guhindura Porogaramu.koherezaBtn()


Ubu duhindura App.sendBtn() kugira ngo yerekane amakuru yaronswe:


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


## Kwakira amahera


Turakeneye kumenya igihe tuzoronka amahera, kubera ivyo tuzokoresha uburyo bwa subscribeToInvoices() buva kuri lnservice, ubu buryo buratuma dushobora gukora code igihe status ya Invoice yahinduwe, kugira ngo tuyikoreshe twongerako iyi mirongo muri app.js.


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


Rema uburyo bwa HTTP GET muri API yacu kugira ngo umukoresha asuzume nimba Hash yarishe.


""

umurongozi.kuronka('/iposita/:Hash', (bisabwa, inyishu) => {

const { Hash } = ivyangombwa;'

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

Porogaramu.kurindiraInyishu = idahuye (Hash) => {

const inyishu = kurindira App.gusaba ({

api: `itangazo/${Hash}`,

});

niba (inyishu.kuroranirwa && inyishu.amakuru.yishuwe) {

console.log("Ukwishura kwakozwe");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

Porogaramu.kurindiraInyishyura = idahuye (Hash) => {

const inyishu = kurindira App.gusaba ({

api: `itangazo/${Hash}`,

});

niba (inyishu.kuroranirwa && inyishu.amakuru.yishuwe) {

gukurahoIgihe(Igihe c'Iporogarama);

App.igihe = ubusa;

$("#Invoice-ifomu").gusenyuka("kwihisha");

$("#ishusho y'imbere").umwandiko (inyishu.amakuru.ishusho y'imbere);

$("#uguterimbere").gusenyuka("kwerekana");

}

};


Porogaramu.yoherezaBtn = idahuye () => {

const izina = $ ("# izina").val ();

const ibirimwo = $ ("# ibirimwo").val ();

const inyishu = kurindira App.gusaba ({

api: "iposita",

ivyashizweho: { izina, ibirimwo },

});

niba (!inyishu) console.ikosa("Ikosa ryo kuronka amakuru!");

niba (inyishu.ukuroranirwa) {

$("#ifomu y'ivyashizweho").gusenyuka("kwihisha");

$("#Invoice-ifomu").gusenyuka("kwerekana");

$("#Invoice").val(inyishu.amakuru.isaba);

App.igihe = setIgihe(Iporogarama.kurindiraInyishyu, 1000, inyishu.amakuru.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.gusenyuka#kuroranirwa

h2 Ukwishura kwagenze neza

div Ikimenyamenya co kwishura:

#ishusho y'imbere

```

We include it in index.pug.

```

kwagura imiterere


guhagarika ibirimwo

h1 Porogaramu y'umuravyo

harimwo ifomu.pug

harimwo Invoice.pug

harimwo ukuroranirwa.pug

```