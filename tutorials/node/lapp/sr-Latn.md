---
name: LAPP Bitcoin
description: Uputstvo za razvoj vaše prve LApp
---

Naučite da kodirate svoju prvu lightning aplikaciju


Zahtevi:



- NodeJs >= 8
- LND >= 9


NodeJs se može preuzeti sa njegove zvanične veb stranice.


Umesto preuzimanja i postavljanja LND čvora, koristićemo alat polar, koji će obaviti ovaj zadatak za nas.


Da bismo izgradili našu Lightning aplikaciju, koristićemo sledeće tehnologije:



- Express za naš web server
- Pug šabloni + bootstrap za naš frontend


## Operativni sistem


Preporučuje se korišćenje Linux-a, ako ste na Windows 10 možete imati Linux konzolu prateći ove korake.

Priprema baze


Koristite alat za generisanje aplikacija, express, da brzo kreirate skelet aplikacije.


```
$ sudo npm install express-generator -g
```


Sa sledećim uputstvom, kreiramo Express aplikaciju pod nazivom lnapp. Aplikacija će biti kreirana u direktorijumu pod nazivom lnapp u trenutnom radnom direktorijumu, a view engine će biti postavljen na Pug.


```
$ express --view=pug lnapp
```


Zatim ulazimo u direktorijum i instaliramo potrebne pakete da bi veb server radio.


```
$ cd myapp
$ npm install
```


Sada jednostavno pokrenemo server


```
$ npm start
```


Zatim, idite na ovaj Address http://localhost:3000 u pregledaču da pristupite aplikaciji.


Generisana aplikacija ima sledeću strukturu direktorijuma:


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


Preuzmite Polar, instalirajte ga i kreirajte mrežu sa 2 LND čvora (Alice i Bob) i 1 bitcoind. Kada vidimo grafikon u aplikaciji koji prikazuje naše čvorove, kliknite na dugme Start i sačekajte nekoliko sekundi dok indikator svakog čvora ne promeni boju u Green.


Da bi se slala plaćanja na Lightning mreži, neophodno je da čvorovi budu međusobno povezani kroz kanale. Kreiranje kanala sa Polar-om je veoma jednostavno, samo treba da kliknemo mišem na jedno od ušiju Alice čvora i prevučemo ga na jedno od ušiju Bob čvora. Odmah će se pojaviti modalni prozor pod nazivom Otvori novi kanal, ostavljamo podrazumevane vrednosti i pritisnemo dugme za otvaranje kanala. Sada ponavljamo akciju, ali ovaj put od Boba ka Alice, na taj način oba čvora mogu slati i primati novac.


## Nodemon


Da bismo izbegli ponovno pokretanje nodejs-a svaki put kada napravimo promenu u kodu, instaliraćemo nodemon


```
$ npm install nodemon -D
```


Moramo kreirati unos u odeljku scripts datoteke package.json, dodajte ovu liniju "dev": "nodemon ./bin/www", odeljak scripts treba da izgleda ovako:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Idite na konzolu gde je pokrenut npm start, pritisnite ctrl + c i ponovo pokrenite nodejs, ali ovog puta koristeći nodemon.


```
$ npm run dev
```


## Povezivanje sa LND


Da bismo se povezali sa Lightning čvorom iz nodejs-a, koristićemo biblioteku LN-service, takođe ćemo instalirati dotenv za upravljanje promenljivim okruženja.


```
$ npm install ln-service dotenv
```


U našem lnapp direktorijumu, kreirajte fajl pod nazivom .env, treba da sadrži ove promenljive:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Vratite se na Polar, izaberite Bob, čvor na koji želimo da se povežemo, idite na karticu "Connect", kopirajte sadržaj GRPC Host i postavite ga u promenljivu LND_GRPC_HOST, u donjem delu kartice connect izaberite base64 i kopirajte sadržaj TLS Cert i postavite ga u promenljivu LND_CERT_BASE64, i uradite isto sa admin macaroon u LND_MACAROON_BASE64.


Sada dodajte ovu liniju u app.js datoteku koja se nalazi u korenu radnog direktorijuma, moramo je kopirati na prvu liniju datoteke.


```
require('dotenv').config();
```


Da bismo verifikovali da nodejs može da se poveže sa našim čvorom, otvorite datoteku routes/index.js, ova datoteka ruta je kreirana pomoću express generatora, prvo zahtevamo biblioteku LN-service, tako da je dodajemo na prvu liniju.


```
const lnservice = require('ln-service');
```


Dodajemo novu rutu koja će nam dati informacije o našem čvoru.


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


Sada idi na ovaj Address http://localhost:3000/info


Ako vidite JSON sa informacijama o čvoru LND, čestitamo!!! vaša aplikacija sada može komunicirati sa Lightning Network.

Kreiranje lažnog modela


Da bismo simulirali bazu podataka, potrebno je kreirati lažni model, što će nam omogućiti korišćenje aplikacije bez instaliranja i konfigurisanja baze podataka.


Prvo, instalirajte uuid paket


```
$ npm install uuid
```


Kreirajte direktorijum models i unutar njega kreirajte datoteku Post.js sa sledećim sadržajem:


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


## Pripremi prikaz


Trebamo bootstrap da bi naš HTML izgledao bolje, pa modifikujemo datoteku layout.pug koja se nalazi u direktorijumu views da izgleda ovako:


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


## Kreiranje objave


Da bismo kreirali objavu, potrebna nam je forma. Unutar direktorijuma views, kreirajte fajl pod nazivom form.pug sa sledećim sadržajem:


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


## Javascript na frontend-u


Najdirektniji način na koji možemo komunicirati sa korisnikom je korišćenjem javascript-a u web pregledaču. Za ovo, kreirajte fajl pod nazivom main.js u direktorijumu javascript, koji već pozivamo iz layout.pug. U ovom fajlu, inicijalizujte projekat. Početni sadržaj main.js je sledeći:


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


Kliknite na dugme "Enviar" i ako je sve u redu, trebalo bi da se prikaže poruka "!hola" u konzoli. Sada možemo modifikovati metodu App.sendBtn() da pošaljemo informacije našem API-ju.


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


Takođe kreiramo metodu App.makeRequest() i dodajemo je u main.js


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


## Kreiraj API


Da bismo to uradili, potrebno je kreirati novu datoteku u routes/api.js i napisati metodu koja odgovara na zahtev napravljen unutar App.sendBtn().


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


Ova datoteka mora biti uključena u app.js, tako da dodajemo ove linije:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Hajde da ponovo pritisnemo dugme za slanje i trebalo bi da odgovori sa istim podacima koje smo uneli u formu.


## Kreiraj Invoice


Metod koji se izvršava kada korisnik kreira objavu treba da generate i Invoice, zatim kreira zapis u bazi podataka povezujući ga sa Invoice, i vrati Invoice korisniku kako bi ga mogli platiti.


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


Ako primimo objekat posta kao odgovor nakon pritiska na dugme za slanje, kao što je ovo, sve je prošlo ispravno. Sada treba da prikažemo tekst kako bi korisnik mogao da ga plati.


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


## Novi Invoice pogled


U direktorijumu views, potrebno je kreirati datoteku pod nazivom Invoice.pug sa sledećim sadržajem:


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


I uključi ga u index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Modifikovanje App.sendBtn()


Sada modifikujemo App.sendBtn() da prikaže dobijene podatke:


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


## Primanje uplate


Moramo znati kada primimo uplatu, za to ćemo koristiti metodu subscribeToInvoices() iz lnservice, ova metoda nam omogućava da izvršimo kod kada je status Invoice ažuriran, da bismo je koristili dodajemo ove linije u app.js.


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


Kreirajte HTTP GET metodu u našem API-ju kako bi korisnik mogao proveriti da li je Hash plaćen.


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

console.log("Plaćanje izvršeno");

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

post: { ime, sadržaj },

});

if (!response) console.error("Greška pri dobijanju podataka!");

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

.sruši#uspeh

h2 Uplata uspešna

div Dokaz o uplati:

#preimage

```

We include it in index.pug.

```

proširuje raspored


blok sadržaj

h1 Lightning App

uključiti form.pug

uključiti Invoice.pug

uključiti success.pug

```