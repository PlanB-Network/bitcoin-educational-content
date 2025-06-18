---
name: LAPP Bitcoin
description: Mafunzo ya kutengeneza LApp yako ya kwanza
---

Jifunze kuweka msimbo kwenye programu yako ya kwanza ya umeme


Mahitaji:



- NodeJs >= 8
- LND >= 9


NodeJs inaweza kupakuliwa kutoka kwa tovuti yake rasmi


Badala ya kupakua na kuanzisha node ya LND, tutatumia chombo cha polar, ambacho kitatufanyia kazi hii.


Ili kuunda programu yetu ya Umeme, tutakuwa tukitumia teknolojia zifuatazo:



- Express kwa webserver yetu
- Violezo vya Pug + bootstrap kwa upande wetu wa mbele


## Mfumo wa uendeshaji


Inashauriwa kutumia Linux, ikiwa uko kwenye Windows 10 unaweza kuwa na koni ya Linux kwa kufuata hatua hizi chache.

Kuandaa msingi


Tumia zana ya jenereta ya programu, eleza, ili kuunda kiunzi cha programu haraka.


```
$ sudo npm install express-generator -g
```


Kwa maagizo yafuatayo, tunaunda programu ya Express inayoitwa lnapp. Programu itaundwa kwenye saraka inayoitwa lnapp kwenye saraka ya sasa ya kufanya kazi, na injini ya kutazama itapewa Pug.


```
$ express --view=pug lnapp
```


Kisha tunaingia kwenye saraka na kufunga vifurushi muhimu kwa seva ya mtandao ili kukimbia.


```
$ cd myapp
$ npm install
```


Sasa tunaendesha seva tu


```
$ npm start
```


Ifuatayo, nenda kwa Address hii http://localhost:3000 kwenye kivinjari ili kufikia programu.


Programu iliyotengenezwa ina muundo wa saraka ufuatao:


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


Pakua Polar, isakinishe, na uunde mtandao wenye nodi 2 za LND (Alice na Bob) na 1 bitcoind. Mara tu tunapoona grafu kwenye programu inayoonyesha nodes zetu, bofya kwenye kifungo cha Mwanzo na kusubiri sekunde chache hadi kiashiria cha kila nodi kibadilisha rangi hadi Green.


Ili kutuma malipo kwa Umeme, ni muhimu kwa nodi kuunganishwa kupitia chaneli. Kuunda vituo na Polar ni rahisi sana, tunahitaji tu kubofya na panya kwenye moja ya masikio ya node ya Alice na kuivuta kwa moja ya masikio ya node ya Bob. Mara moja, dirisha la modal lenye kichwa Fungua kituo kipya kinapaswa kuonekana, tunaacha maadili ya msingi na bonyeza kitufe cha wazi cha kituo. Sasa tunarudia kitendo lakini wakati huu kutoka kwa Bob hadi Alice, kwa njia hii nodi zote mbili zinaweza kutuma na kupokea pesa.


## Nodemon


Ili kuzuia kulazimika kuanza tena nodejs kila wakati tunapofanya mabadiliko katika nambari, tutasakinisha nodemon


```
$ npm install nodemon -D
```


Ni lazima tuunde ingizo katika sehemu ya hati ya faili ya package.json, ongeza laini hii "dev": "nodemon ./bin/www", sehemu ya hati inapaswa kuonekana kama hii:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Nenda kwenye koni ambapo npm start inaendeshwa, bonyeza ctrl + c na uanze nodejs tena lakini wakati huu ukitumia nodemon


```
$ npm run dev
```


## Inaunganisha kwa LND


Ili kuunganisha kwenye nodi ya Umeme kutoka kwa nodejs, tutatumia maktaba ya huduma ya LN, pia tutasakinisha dotenv ili kudhibiti vigezo vya mazingira.


```
$ npm install ln-service dotenv
```


Katika saraka yetu ya lnapp, unda faili inayoitwa .env, inapaswa kuwa na anuwai hizi:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Rudi kwenye Polar, chagua Bob, nodi tunayotaka kuunganisha, nenda kwenye kichupo cha "Unganisha", nakili maudhui ya GRPC Host na uyaweke katika LND_GRPC_HOST lahaja, katika sehemu ya chini ya kichupo cha kuunganisha chagua base64 na unakili maudhui ya TLS Cert na uyaweke katika kibadilishio cha LND_CERT_BASE64, na ufanye vivyo hivyo na admin_BASE64 admin.


Sasa ongeza mstari huu kwenye faili ya app.js iliyoko kwenye mzizi wa saraka ya kazi, lazima tuinakili kwenye mstari wa kwanza wa faili.


```
require('dotenv').config();
```


Ili kuthibitisha kwamba nodi zinaweza kuunganishwa kwenye nodi yetu, fungua faili za njia/index.js, faili hii ya njia iliundwa na jenereta ya kueleza, kwanza tunahitaji maktaba ya huduma ya LN, kwa hiyo tunaiongeza kwenye mstari wa kwanza.


```
const lnservice = require('ln-service');
```


Tunaongeza njia mpya ambayo itatupa habari kuhusu nodi yetu.


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


Sasa nenda kwa Address hii http://localhost:3000/info


Ukiona json na habari ya nodi ya LND, hongera !!! programu yako sasa inaweza kuingiliana na Lightning Network.

Kuunda mfano wa uwongo


Ili kuiga hifadhidata, tunahitaji kuunda mfano wa uwongo, hii itaturuhusu kutumia programu bila kusakinisha na kusanidi hifadhidata.


Kwanza, sasisha kifurushi cha uuid


```
$ npm install uuid
```


Unda saraka ya mifano na ndani yake, unda faili ya Post.js na maudhui yafuatayo:


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


## Tayarisha mwonekano


Tunahitaji bootstrap ili kufanya html yetu ionekane bora, kwa hivyo tunarekebisha faili ya layout.pug iliyoko kwenye saraka ya maoni ili ionekane kama hii:


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


## Kuunda Chapisho


Ili kuunda chapisho, tunahitaji fomu. Ndani ya saraka ya maoni, tengeneza faili inayoitwa form.pug na yaliyomo yafuatayo:


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


## Javascript katika frontend


Njia ya moja kwa moja tunayopaswa kuingiliana na mtumiaji ni kwa kutumia javascript kwenye kivinjari cha wavuti. Kwa hili, tengeneza faili inayoitwa main.js kwenye saraka ya javascript, ambayo tayari tunaita kutoka kwa mpangilio.pug. Katika faili hii, anzisha mradi. Maudhui ya awali ya main.js ni kama ifuatavyo:


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


Bofya kitufe cha "Enviar" na ikiwa kila kitu kiko sawa, inapaswa kuonyesha ujumbe "!hola" kwenye console. Sasa tunaweza kurekebisha njia ya App.sendBtn() ili kutuma maelezo kwa API yetu.


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


Pia tunaunda mbinu ya App.makeRequest() na kuiongeza kwa main.js


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


## Unda API


Ili kufanya hivyo, tunahitaji kuunda faili mpya katika routes/api.js na kuandika mbinu inayojibu ombi lililotolewa ndani ya App.sendBtn().


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


Faili hii lazima ijumuishwe kwenye app.js, kwa hivyo tunaongeza mistari hii:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Wacha tubonyeze kitufe cha kutuma tena na inapaswa kujibu kwa data ile ile tuliyoweka kwenye fomu.


## Unda Invoice


Njia ambayo inatekelezwa wakati mtumiaji anaunda chapisho inapaswa generate Invoice, kisha kuunda rekodi katika hifadhidata inayoiunganisha na Invoice, na kurudisha Invoice kwa mtumiaji ili aweze kuilipa.


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


Ikiwa tutapokea kitu cha chapisho kama jibu baada ya kubonyeza tuma, kama hii, kila kitu kimeenda sawa. Sasa tunahitaji kuonyesha maandishi ili mtumiaji aweze kulipa.


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


## Mwonekano mpya wa Invoice


Katika saraka ya maoni, tunahitaji kuunda faili inayoitwa Invoice.pug na maudhui yafuatayo:


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


Na ni pamoja na katika index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Kurekebisha App.sendBtn()


Sasa tunarekebisha App.sendBtn() ili kuonyesha data iliyopatikana:


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


## Kupokea malipo


Tunahitaji kujua tunapopokea malipo, kwa hili tutatumia njia ya subscribeToInvoices() kutoka lnservice, njia hii huturuhusu kutekeleza msimbo wakati hali ya Invoice imesasishwa, ili kuitumia tunaongeza laini hizi kwenye app.js.


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


Unda mbinu ya HTTP GET katika API yetu ili mtumiaji aangalie ikiwa Hash imelipwa.


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

api: `post/${Hash}`,

});

ikiwa (response.success && response.data.paid) {

console.log("Malipo yamefanywa");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`,

});

ikiwa (response.success && response.data.paid) {

clearInterval(App.interval);

App.interval = null;

$("#Invoice-form").kunja("ficha");

$("#preimage").text(response.data.preimage);

$("#success").collapse("show");

}

};


App.sendBtn = async () => {

const name = $("#jina").val();

const content = $("#content").val();

const response = await App.makeRequest({

api: "chapisho",

chapisho: {jina, maudhui },

});

if (!response) console.error("Hitilafu katika kupata data!");

ikiwa (jibu.mafanikio) {

$("#post-form").collapse("ficha");

$("#Invoice-form").kunja("onyesha");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.poromoka#mafanikio

h2 Malipo yamefaulu

Div Ushahidi wa malipo:

#taswira

```

We include it in index.pug.

```

huongeza mpangilio


kuzuia maudhui

h1 Programu ya Umeme

ni pamoja na fomu.pug

ni pamoja na Invoice.pug

ni pamoja na mafanikio.pug

```