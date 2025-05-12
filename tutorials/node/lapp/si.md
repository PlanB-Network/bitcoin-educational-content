---
name: LAPP Bitcoin
description: ඔබගේ පළමු LApp සංවර්ධනය කිරීම සඳහා උපකාරකය
---

ඔබේ පළමු මිනිත්තු යෙදුම කේතය කිරීමට ඉගෙන ගන්න


අවශ්‍යතා:



- NodeJs >= 8
- LND >= 9


NodeJs lahko prenesete z njegove uradne spletne strani


LND නියමකය බාගත කිරීම සහ පිහිටුවීම වෙනුවට, අපි polar මෙවලම භාවිතා කරමු, එය අප වෙනුවෙන් මෙම කාර්යය සිදු කරනු ඇත.


Za izdelavo naše aplikacije Lightning bomo uporabili naslednje tehnologije:



- අපගේ වෙබ් සේවාදායකය සඳහා Express
- Pug ටෙම්ප්ලේට් + bootstrap අපගේ ඉදිරිපස සඳහා


## آپریٹنگ سسٹم


Linux භාවිතා කිරීම නිර්දේශිතය, ඔබ Windows 10 මත සිටිනවා නම් මෙම කිහිපයෙහි පියවර අනුගමනය කිරීමෙන් Linux සංවාදයක් ලබා ගත හැක.

මූලිකය සකස් කිරීම


ඉක්මනින් යෙදුම් කුටියක් නිර්මාණය කිරීමට, express යෙදුම් ජනක මෙවලම භාවිතා කරන්න.


```
$ sudo npm install express-generator -g
```


මෙම උපදෙස් අනුව, අපි lnapp නම් Express යෙදුමක් නිර්මාණය කරමු. යෙදුම වර්තමාන කාර්ය නියමිතයේ lnapp නම් ඩිරෙක්ටරියක නිර්මාණය වන අතර, දසුනේ එන්ජිම Pug වෙත පවරනු ලැබේ.


```
$ express --view=pug lnapp
```


පසුව අපි නාමාවලියට පිවිස, වෙබ් සේවාදායකය ක්‍රියාත්මක වීමට අවශ්‍ය පැකේජ ස්ථාපනය කරමු.


```
$ cd myapp
$ npm install
```


අපි දැන් සරලව සේවාදායකය ක්‍රියාත්මක කරමු


```
$ npm start
```


ඊළඟට, මෙම Address http://localhost:3000 බ්‍රවුසරයේ විවෘත කර යෙදුමට ප්‍රවේශ වන්න.


උත්පාදිත යෙදුම පහත දැක්වෙන නාමාවලිය ව්‍යුහය ඇත:


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


Polar බාගන්න, ස්ථාපනය කරන්න, සහ 2 LND නියුඩ් (ඇලීස් සහ බොබ්) සහ 1 bitcoind සමඟ ජාලයක් සාදන්න. අපගේ නියුඩ් පෙන්වන ග්‍රැෆය්ය යෙදුම තුළ දැකීමෙන් පසු, ආරම්භ බොත්තම ක්ලික් කරන්න සහ සෑම නියුඩ් එකකම දර්ශකය Green වෙත වර්ණය වෙනස් වන තෙක් තත්පර කිහිපයක් රැඳී සිටින්න.


ලයිට්නින්ග් මත ගෙවීම් යැවීමට, නෝඩ් එකිනෙකට නාලිකා හරහා අන්තර් සම්බන්ධ විය යුතුය. Polar සමඟ නාලිකා නිර්මාණය කිරීම ඉතා සරලය, අපිට ඇලීස් නෝඩ් එකේ කනක් මත මවුස් එකෙන් ක්ලික් කර බොබ් නෝඩ් එකේ කනකට ඇදගෙන යාමට පමණි. වහාම, නව නාලිකාවක් විවෘත කරන්නැයි ශීර්ෂය ඇති මොඩල් කවුළුවක් පෙනිය යුතුය, අපි පෙරනිමි අගයන් තබා නාලිකාව විවෘත කරන්න බොත්තම ඔබමු. දැන් අපි ක්‍රියාව නැවත කරන අතර මේ වතාවේ බොබ් සිට ඇලීස් වෙත, මෙසේ නෝඩ් දෙකම මුදල් යැවීමට සහ ලබා ගැනීමට හැකි වේ.


## Nodemon


කේතයේ වෙනසක් කරන සෑම විටම nodejs නැවත ආරම්භ කිරීමට අවශ්‍යතාවය වලක්වා ගැනීමට, අපි nodemon ස්ථාපනය කරමු.


```
$ npm install nodemon -D
```


package.json දෝෂාත්මකයි.


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


කන්සෝලයට යන්න, එහි npm start ක්‍රියාත්මක වේ, ctrl + c ඔබා nodejs නැවත ආරම්භ කරන්න නමුත් මේ වතාවේ nodemon භාවිතා කරමින්


```
$ npm run dev
```


## LND සම්බන්ධ කිරීම


Nodejs-დან Lightning නියමක සම්බන්ධ වීමට, අපි LN-service පුස්තකාලය භාවිතා කරමු, අපි පරිසර විචල්‍ය කළමනාකරණය කිරීමට dotenv ද ස්ථාපනය කරමු.


```
$ npm install ln-service dotenv
```


Na našem lnapp imeniku ustvarite datoteko z imenom .env, ki naj vsebuje te spremenljivke:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


පෝලර් වෙත ආපසු ගොස්, අපට සම්බන්ධ වීමට අවශ්‍ය නෝඩය වන බොබ් තෝරන්න, "Connect" ටැබය වෙත යන්න, GRPC Host හි අන්තර්ගතය පිටපත් කර LND_GRPC_HOST විචල්‍යය තුළ තබන්න, සම්බන්ධ ටැබයේ පහළ කොටසෙහි base64 තෝරන්න සහ TLS Cert හි අන්තර්ගතය පිටපත් කර LND_CERT_BASE64 විචල්‍යය තුළ තබන්න, සහ LND_MACAROON_BASE64 හි පරිපාලක මැකරුන් සමඟ එකම දේ කරන්න.


දැන් මෙම පේළිය වැඩ කරන නාමාවලියේ මූලික ස්ථානයේ ඇති app.js ගොනුවට එක් කරන්න, අපි එය ගොනුවේ පළමු පේළියට පිටපත් කළ යුතුය.


```
require('dotenv').config();
```


To verify that nodejs can connect to our node, open the routes/index.js file, this routes file was created by the express generator, first we require the LN-service library, so we add it on the first line


```
const lnservice = require('ln-service');
```


අපගේ නෝඩ් පිළිබඳ තොරතුරු ලබා දෙන නව මාර්ගයක් අපි එක් කරමු.


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


Zdaj pojdite na to Address http://localhost:3000/info


Če vidite json z informacijami o vozlišču LND, čestitke!!! vaša aplikacija lahko zdaj komunicira z Lightning Network.

Ustvarjanje lažnega modela


데이터베이스를 시뮬레이션하려면 가짜 모델을 만들어야 합니다. 이렇게 하면 데이터베이스를 설치하고 구성하지 않고도 앱을 사용할 수 있습니다.


ප්‍රථමයෙන්, uuid පැකේජය ස්ථාපනය කරන්න


```
$ npm install uuid
```


`models` නාමාවලිය සාදන්න සහ එහි ඇතුළත, පහත අන්තර්ගතය සමඟ `Post.js` ගොනුව සාදන්න:


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


## දෘශ්‍යය සකසන්න


අපට bootstrap අවශ්‍යයි අපගේ html වඩා හොඳින් පෙනෙන්න, එබැවින් අපි views නාමාවලිය තුළ පිහිටා ඇති layout.pug ගොනුව මෙවන් ආකාරයකට වෙනස් කරමු:


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


## පශ්චාත් එකක් නිර්මාණය කිරීම


Za ustvarjanje objave potrebujemo obrazec. Znotraj imenika views ustvarite datoteko z imenom form.pug z naslednjo vsebino:


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


## ඉදිරිපසෙහි ජාවාස්ක්‍රිප්ට්


අපට පරිශීලකයා සමඟ අන්තර්ක්‍රියා කිරීමට ඇති වඩාත්ම සෘජු ක්‍රමය වෙබ් බ්‍රවුසරයේ ජාවාස්ක්‍රිප්ට් භාවිතා කිරීමයි. මෙ සඳහා, ජාවාස්ක්‍රිප්ට් නාමාවලිය තුළ main.js නම් ගොනුවක් සාදන්න, අපි දැනටමත් layout.pug වෙතින් කැඳවමින් සිටිමු. මෙම ගොනුවේ, ව්‍යාපෘතිය ආරම්භ කරන්න. main.js හි ආරම්භක අන්තර්ගතය පහත පරිදි වේ:


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


"Enviar" බොත්තම ක්ලික් කරන්න සහ හැමදේම හරි නම්, එය console එකේ "!hola" පණිවිඩයක් පෙන්විය යුතුය. දැන් අපි App.sendBtn() ක්‍රමය වෙනස් කර අපගේ API වෙත තොරතුරු යැවිය හැක.


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


අපි App.makeRequest() ක්‍රමයද නිර්මාණය කර main.js වෙත එකතු කරමු.


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


## API සෑදීම


මෙය කිරීමට, අපි routes/api.js හි නව ගොනුවක් තනන්නට හා App.sendBtn() තුළ සිදු කරන ලද ඉල්ලීමට ප්‍රතිචාර දක්වන ක්‍රමය ලිවිය යුතුය.


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


මෙම ගොනුව app.js හි ඇතුළත් කළ යුතු බැවින්, අපි මෙම පේළි එකතු කරමු:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


අපි නැවත යැවීමේ බොත්තම ඔබා එය අපි පෝරමයේ ඇතුළත් කළ දත්ත සමඟ ප්‍රතිචාර දක්විය යුතුය.


## Ustvarite Invoice


පරිශීලකයෙකු පශ්චාත් එකක් නිර්මාණය කරන විට ක්‍රියාත්මක වන ක්‍රමය generate සහ Invoice ක්‍රියාත්මක කළ යුතු අතර, එය Invoice සමඟ සම්බන්ධ කරන ලද දත්ත ගබඩාවේ වාර්තාවක් නිර්මාණය කළ යුතු අතර, පරිශීලකයාට එය ගෙවිය හැකි වන පරිදි Invoice ආපසු ලබා දිය යුතුය.


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


ඔබ "යවන්න" බොත්තම ඔබා අවසන් වරට, අපට ප්‍රතිචාරයක් ලෙස පළ කිරීමේ වස්තුවක් ලැබුණහොත්, සියල්ල නිවැරදිව සිදු වී ඇත. දැන් අපට පෙන්නුම් කළ යුතුය, එවිට පරිශීලකයා එය ගෙවිය හැක.


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


## New Invoice pogled


දෘශ්‍යයන් ගොනුවේ, අපට Invoice.pug නම් ගොනුවක් පහත අන්තර්ගතය සමඟ නිර්මාණය කළ යුතුය:


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


ඒවා index.pug හි ඇතුළත් කරන්න


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## App.sendBtn() මාරු කිරීම


Zdaj spremenimo App.sendBtn(), da prikaže pridobljene podatke:


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


## ගෙවීම ලැබීම


Moramo vedeti, kdaj prejmemo plačilo, za to bomo uporabili metodo subscribeToInvoices() iz lnservice, ta metoda nam omogoča izvajanje kode, ko je stanje Invoice posodobljeno, za uporabo dodamo te vrstice v app.js.


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


අපගේ API හි HTTP GET ක්‍රමයක් සාදන්න, පරිශීලකයාට Hash ගෙවීම් කර ඇතිදැයි පරීක්ෂා කිරීමට.


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

če (odgovor.uspeh && odgovor.podatki.placano) {

console.log("ගෙවීම සිදු කරන ලදී");

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

če (odgovor.uspeh && odgovor.podatki.placano) {

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

පශ්චාත්: { නම, අන්තර්ගතය },

});

če (!odgovor) console.error("Napaka pri pridobivanju podatkov!");

če (odgovor.uspeh) {

$("#post-form").collapse("hide");

$("#Invoice-form").collapse("show");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#success

h2 Plačilo uspešno

div Plačilni dokaz:

#preimage

```

We include it in index.pug.

```

ලේඛනය දිගහරින්නේ layout


ब्लक सामग्री

h1 ලයිට්නින් ඇප්

form.pug අන්තර්ගත කරන්න

Invoice.pug ඇතුළත් කරන්න

include success.pug

```