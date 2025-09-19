---
name: Lightning App
description: Handleiding om je eerste Lightning-app (LAPP) te ontwikkelen
---

![cover](assets/cover.webp)

## Leer je eerste lightning-app te coderen


Vereisten:



- NodeJs >= 8
- LND >= 9


NodeJs kan worden gedownload van de officiële website


In plaats van het downloaden en opzetten van een LND node, zullen we het polar gereedschap gebruiken, dat deze taak voor ons zal uitvoeren.


Om onze Lightning-app te bouwen, gebruiken we de volgende technologieën:



- Express voor onze webserver
- Pug templates + bootstrap voor onze frontend


https://planb.network/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## Besturingssysteem


Het is aan te raden om Linux te gebruiken, als je Windows 10 gebruikt kun je een Linux console krijgen door deze paar stappen te volgen.

De basis voorbereiden


Gebruik de applicatiegenerator, express, om snel een applicatieskelet te maken.


```
$ sudo npm install express-generator -g
```


Met de volgende instructie maken we een Express-toepassing genaamd lnapp. De applicatie wordt gemaakt in een map genaamd lnapp in de huidige werkmap en de view engine wordt toegewezen aan Pug.


```
$ express --view=pug lnapp
```


Vervolgens gaan we de directory binnen en installeren we de benodigde pakketten om de webserver te laten draaien.


```
$ cd myapp
$ npm install
```


Nu draaien we gewoon de server


```
$ npm start
```


Ga vervolgens naar deze Address http://localhost:3000 in de browser om toegang te krijgen tot de applicatie.


De gegenereerde applicatie heeft de volgende mapstructuur:


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


## Pool


Download Polar, installeer het en maak een netwerk met 2 knooppunten LND (Alice en Bob) en 1 bitcoind. Zodra we de grafiek in de app zien met onze knooppunten, klik je op de Start-knop en wacht je een paar seconden totdat de indicator van elk knooppunt van kleur verandert naar Green.


Om betalingen via Lightning te versturen, moeten de knooppunten onderling verbonden zijn via kanalen. Het maken van kanalen met Polar is heel eenvoudig, we hoeven alleen maar met de muis op een van de oren van het Alice knooppunt te klikken en het naar een van de oren van het Bob knooppunt te slepen. Onmiddellijk verschijnt een modaal venster met de titel Open new channel (Nieuw kanaal openen), we laten de standaardwaarden staan en drukken op de knop Open channel (Kanaal openen). Nu herhalen we de actie, maar nu van Bob naar Alice, zodat beide knooppunten geld kunnen verzenden en ontvangen.


## Nodemon


Om te voorkomen dat we nodejs elke keer opnieuw moeten starten als we een wijziging in de code aanbrengen, installeren we nodemon


```
$ npm install nodemon -D
```


We moeten een item aanmaken in de scripts sectie van het package.json bestand, voeg deze regel "dev" toe: "nodemon ./bin/www", de scripts sectie zou er zo uit moeten zien:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Ga naar de console waar npm start draait, druk op ctrl + c en start nodejs opnieuw maar deze keer met nodemon


```
$ npm run dev
```


## Aansluiten op LND


Om verbinding te maken met een Lightning node vanuit nodejs, zullen we de LN-service bibliotheek gebruiken, we zullen ook dotenv installeren om omgevingsvariabelen te beheren.


```
$ npm install ln-service dotenv
```


Maak in onze lnapp-directory een bestand aan met de naam .env, dat deze variabelen moet bevatten:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Ga terug naar Polar, selecteer Bob, het knooppunt waarmee we willen verbinden, ga naar het tabblad "Connect", kopieer de inhoud van GRPC Host en plaats deze in de variabele LND_GRPC_HOST, selecteer in het onderste gedeelte van het tabblad "connect" base64 en kopieer de inhoud van TLS Cert en plaats deze in de variabele LND_CERT_BASE64, en doe hetzelfde met de admin macaroon in LND_MACAROON_BASE64.


Voeg nu deze regel toe aan het app.js bestand in de root van de werkmap, we moeten het kopiëren op de eerste regel van het bestand.


```
require('dotenv').config();
```


Om te controleren of nodejs verbinding kan maken met onze node, openen we het bestand routes/index.js. Dit routebestand is gemaakt door de express generator. Eerst hebben we de LN-service bibliotheek nodig, dus voegen we die toe op de eerste regel


```
const lnservice = require('ln-service');
```


We voegen een nieuwe route toe die ons informatie geeft over ons knooppunt.


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


Ga nu naar deze Address http://localhost:3000/info


Als je een json ziet met de informatie van de LND node, gefeliciteerd!!! je app kan nu communiceren met de Lightning Network.

Een nepmodel maken


Om een database te simuleren, moeten we een nepmodel maken. Hiermee kunnen we de app gebruiken zonder een database te installeren en te configureren.


Installeer eerst het uuid-pakket


```
$ npm install uuid
```


Maak de map models en maak daarin het bestand Post.js met de volgende inhoud:


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


## De weergave voorbereiden


We hebben bootstrap nodig om onze html er beter uit te laten zien, dus we passen het bestand layout.pug in de views-directory aan zodat het er als volgt uitziet:


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


## Een bericht maken


Om een bericht te maken, hebben we een formulier nodig. Maak in de map views een bestand genaamd form.pug met de volgende inhoud:


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


## Javascript aan de voorkant


De meest directe manier om met de gebruiker te communiceren is door javascript te gebruiken in de webbrowser. Maak hiervoor een bestand genaamd main.js in de javascript directory, dat we al aanroepen vanuit layout.pug. In dit bestand initialiseer je het project. De initiële inhoud van main.js is als volgt:


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


Klik op de knop "Enviar" en als alles in orde is, wordt er een bericht "!hola" weergegeven in de console. Nu kunnen we de methode App.sendBtn() aanpassen om de informatie naar onze API te sturen.


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


We maken ook de methode App.makeRequest() en voegen deze toe aan main.js


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


## De API maken


Om dit te doen, moeten we een nieuw bestand maken in routes/api.js en de methode schrijven die reageert op het verzoek dat wordt gedaan in App.sendBtn().


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


Dit bestand moet worden opgenomen in app.js, dus voegen we deze regels toe:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Laten we nog een keer op de verzendknop drukken en deze zou moeten reageren met dezelfde gegevens die we in het formulier hebben ingevoerd.


## Maak de Invoice


De methode die wordt uitgevoerd wanneer een gebruiker een bericht maakt, moet generate een Invoice maken, dan een record aanmaken in de database die het koppelt aan de Invoice, en de Invoice terugsturen naar de gebruiker zodat die het kan betalen.


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


Als we een postobject ontvangen als antwoord nadat we op verzenden hebben gedrukt, zoals dit, is alles goed gegaan. Nu moeten we de tekst weergeven zodat de gebruiker kan betalen.


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


## Nieuwe Invoice weergave


In de views directory moeten we een bestand genaamd Invoice.pug maken met de volgende inhoud:


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


En neem het op in index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## App.sendBtn() wijzigen


Nu passen we App.sendBtn() aan om de verkregen gegevens weer te geven:


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


## De betaling ontvangen


We moeten weten wanneer we de betaling ontvangen, hiervoor gebruiken we de methode subscribeToInvoices() van lnservice, met deze methode kunnen we code uitvoeren wanneer de status van een Invoice is bijgewerkt, om het te gebruiken voegen we deze regels toe in app.js.


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


Maak een HTTP GET methode in onze API voor de gebruiker om te controleren of een Hash betaald is.


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

console.log("Betaling gedaan");

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

clearInterval(App.interval);

App.interval = null;

$("#Invoice-formulier").collapse("verbergen");

$("#preimage").text(response.data.preimage);

$("#succes").collapse("show");

}

};


App.sendBtn = async () => {

const naam = $("#naam").val();

inhoud = $("#content").val();

const response = await App.makeRequest({

api: "post",

post: {naam, inhoud },

});

als (!response) console.error("Fout bij het ophalen van gegevens!");

als (antwoord.succes) {

$("#post-formulier").collapse("verbergen");

$("#Invoice-formulier").collapse("weergeven");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#succes

h2 Betaling geslaagd

div Betalingsbewijs:

#preafbeelding

```

We include it in index.pug.

```

breidt lay-out uit


inhoud blok

h1 Bliksem App

include formulier.pug

include Invoice.pug

include succes.pug

```