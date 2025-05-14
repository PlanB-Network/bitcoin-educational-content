---
name: LAPP Bitcoin
description: Handledning för att utveckla din första LApp
---

Lär dig att koda din första blixtapp


Krav som ställs:



- NodeJs >= 8
- LND >= 9


NodeJs kan laddas ner från dess officiella webbplats


I stället för att ladda ner och konfigurera en LND-nod använder vi polarverktyget, som utför den här uppgiften åt oss.


För att bygga vår Lightning-app kommer vi att använda följande tekniker:



- Express för vår webbserver
- Pug-mallar + bootstrap för vår frontend


## Operativsystem


Vi rekommenderar att du använder Linux, men om du använder Windows 10 kan du få en Linux-konsol genom att följa dessa steg.

Förberedelse av basen


Använd verktyget för applikationsgenerering, express, för att snabbt skapa ett applikationsskelett.


```
$ sudo npm install express-generator -g
```


Med följande instruktion skapar vi en Express-applikation som heter lnapp. Programmet kommer att skapas i en katalog som heter lnapp i den aktuella arbetskatalogen och vymotorn kommer att tilldelas Pug.


```
$ express --view=pug lnapp
```


Sedan går vi in i katalogen och installerar de paket som behövs för att webbservern ska fungera.


```
$ cd myapp
$ npm install
```


Nu kör vi helt enkelt servern


```
$ npm start
```


Gå sedan till denna Address http://localhost:3000 i webbläsaren för att komma åt applikationen.


Den genererade applikationen har följande katalogstruktur:


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


Ladda ner Polar, installera det och skapa ett nätverk med 2 LND-noder (Alice och Bob) och 1 bitcoind. När vi ser grafen i appen som visar våra noder klickar vi på Start-knappen och väntar några sekunder tills indikatorn för varje nod ändrar färg till Green.


För att kunna skicka betalningar på Lightning är det nödvändigt att noderna är sammankopplade via kanaler. Att skapa kanaler med Polar är mycket enkelt, vi behöver bara klicka med musen på ett av öronen på Alice-noden och dra det till ett av öronen på Bob-noden. Omedelbart bör ett modalt fönster med titeln Öppna ny kanal visas, vi lämnar standardvärdena och trycker på knappen Öppna kanal. Nu upprepar vi åtgärden men den här gången från Bob till Alice, på det här sättet kan båda noderna skicka och ta emot pengar.


## Nodemon


För att undvika att behöva starta om nodejs varje gång vi gör en ändring i koden installerar vi nodemon


```
$ npm install nodemon -D
```


Vi måste skapa en post i skriptavsnittet i filen package.json, lägg till den här raden "dev": "nodemon ./bin/www", skriptavsnittet ska se ut så här:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Gå till konsolen där npm start körs, tryck ctrl + c och starta nodejs igen men den här gången med hjälp av nodemon


```
$ npm run dev
```


## Anslutning till LND


För att ansluta till en Lightning-nod från nodejs kommer vi att använda LN-service-biblioteket, vi kommer också att installera dotenv för att hantera miljövariabler.


```
$ npm install ln-service dotenv
```


I vår lnapp-katalog skapar du en fil som heter .env, den ska innehålla dessa variabler:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Gå tillbaka till Polar, välj Bob, den nod vi vill ansluta till, gå till fliken "Anslut", kopiera innehållet i GRPC Host och placera det i variabeln LND_GRPC_HOST, i den nedre delen av anslutningsfliken väljer du base64 och kopierar innehållet i TLS Cert och placerar det i variabeln LND_CERT_BASE64, och gör samma sak med admin macaroon i LND_MACAROON_BASE64.


Lägg nu till den här raden i filen app.js som ligger i roten till arbetskatalogen, vi måste kopiera den på första raden i filen.


```
require('dotenv').config();
```


För att verifiera att nodejs kan ansluta till vår nod, öppna filen routes/index.js, den här routes-filen skapades av expressgeneratorn, först behöver vi LN-service-biblioteket, så vi lägger till det på första raden


```
const lnservice = require('ln-service');
```


Vi lägger till en ny rutt som kommer att ge oss information om vår nod.


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


Gå nu till denna Address http://localhost:3000/info


Om du ser en json med information om LND-noden, grattis!!! din app kan nu interagera med Lightning Network.

Skapa en falsk modell


För att simulera en databas måste vi skapa en falsk modell, vilket gör att vi kan använda appen utan att installera och konfigurera en databas.


Installera först uuid-paketet


```
$ npm install uuid
```


Skapa katalogen models och i den skapar du filen Post.js med följande innehåll:


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


## Förbered utsikten


Vi behöver bootstrap för att få vår html att se bättre ut, så vi ändrar filen layout.pug som finns i views-katalogen så att den ser ut så här:


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


## Skapa ett inlägg


För att skapa ett inlägg behöver vi ett formulär. I views-katalogen skapar du en fil som heter form.pug med följande innehåll:


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


## Javascript i frontend


Det mest direkta sättet vi har att interagera med användaren är genom att använda javascript i webbläsaren. För detta skapar du en fil som heter main.js i javascript-katalogen, som vi redan anropar från layout.pug. I den här filen initialiserar du projektet. Det initiala innehållet i main.js är följande:


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


Klicka på knappen "Enviar" och om allt är bra ska det visas ett meddelande "!hola" i konsolen. Nu kan vi modifiera App.sendBtn()-metoden för att skicka informationen till vårt API.


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


Vi skapar också metoden App.makeRequest() och lägger till den i main.js


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


## Skapa API:et


För att göra detta måste vi skapa en ny fil i routes/api.js och skriva den metod som svarar på den begäran som görs i App.sendBtn().


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


Den här filen måste inkluderas i app.js, så vi lägger till dessa rader:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Nu trycker vi på skicka-knappen igen och den ska svara med samma data som vi angav i formuläret.


## Skapa Invoice


Den metod som körs när en användare skapar ett inlägg ska generate en Invoice, sedan skapa en post i databasen som länkar den till Invoice och returnera Invoice till användaren så att de kan betala den.


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


Om vi får ett postobjekt som svar efter att ha tryckt på send, så här, har allt gått rätt till. Nu behöver vi visa texten så att användaren kan betala den.


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


## Ny vy för Invoice


I views-katalogen måste vi skapa en fil som heter Invoice.pug med följande innehåll:


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


Och inkludera den i index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Ändra App.sendBtn()


Nu ändrar vi App.sendBtn() för att visa de erhållna uppgifterna:


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


## Mottagande av betalning


Vi behöver veta när vi får betalningen, för detta kommer vi att använda metoden subscribeToInvoices() från lnservice, den här metoden låter oss exekvera kod när statusen för en Invoice har uppdaterats, för att använda den lägger vi till dessa rader i app.js.


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


Skapa en HTTP GET-metod i vårt API för att användaren ska kunna kontrollera om en Hash har betalats.


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

if (response.success && response.data.paid) {

console.log("Betalning utförd");

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

if (response.success && response.data.paid) {

clearInterval(App.intervall);

App.interval = null;

$("#Invoice-form").collapse("hide");

$("#preimage").text(respons.data.preimage);

$("#success").collapse("show");

}

};


App.sendBtn = async () => {

const namn = $("#namn").val();

const content = $("#content").val();

const response = await App.makeRequest({

api: "post",

post: { namn, innehåll },

});

if (!response) console.error("Fel vid hämtning av data!");

if (svar.framgång) {

$("#post-form").collapse("hide");

$("#Invoice-form").collapse("show");

$("#Invoice").val(svar.data.begäran);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.kollaps#framgång

h2 Betalning framgångsrik

div Betalningsbevis:

#förbild

```

We include it in index.pug.

```

utökar layout


blockinnehåll

h1 Lightning App

inkludera form.pug

inkludera Invoice.pug

inkludera framgång.pug

```