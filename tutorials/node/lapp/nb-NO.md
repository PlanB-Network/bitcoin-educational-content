---
name: LAPP bitcoin
description: Veiledning for å utvikle din første LApp
---

Lær å kode din første lyn-app

Krav:

- NodeJs >= 8
- LND >= 9

NodeJs kan lastes ned fra den offisielle nettsiden

I stedet for å laste ned og sette opp en LND-node, vil vi bruke verktøyet polar, som vil utføre denne oppgaven for oss.

For å bygge vår Lightning-app, vil vi bruke følgende teknologier:

- Express for vår webserver
- Pug-maler + bootstrap for vår frontend

## Operativsystem

Det anbefales å bruke Linux, hvis du er på Windows 10 kan du ha en Linux-konsoll ved å følge disse få stegene.
Forberede grunnlaget

Bruk applikasjonsgenereringsverktøyet, express, for å raskt opprette et applikasjonsskjelett.

```
$ sudo npm install express-generator -g
```

Med følgende instruksjon oppretter vi en Express-applikasjon kalt lnapp. Applikasjonen vil bli opprettet i en mappe kalt lnapp i gjeldende arbeidskatalog, og visningsmotoren vil bli tildelt til Pug.

```
$ express --view=pug lnapp
```

Deretter går vi inn i mappen og installerer de nødvendige pakkene for at webserveren skal kjøre.

```
$ cd myapp
$ npm install
```

Nå kjører vi ganske enkelt serveren

```
$ npm start
```

Neste, gå til denne adressen http://localhost:3000 i nettleseren for å få tilgang til applikasjonen.

Den genererte applikasjonen har følgende katalogstruktur:

```
.
├── app.js
├── bin
│ └── www
├── package.json
├── public
│ ├── bilder
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

Last ned Polar, installer det, og opprett et nettverk med 2 LND-noder (Alice og Bob) og 1 bitcoind. Når vi ser grafen i appen som viser nodene våre, klikker vi på Start-knappen og venter noen sekunder til indikatoren for hver node endrer farge til grønn.

For å kunne sende betalinger på Lightning, er det nødvendig at nodene er forbundet gjennom kanaler. Å opprette kanaler med Polar er veldig enkelt, vi trenger bare å klikke med musen på en av ørene til Alice-noden og dra den til en av ørene til Bob-noden. Umiddelbart bør et modalvindu med tittelen Åpne ny kanal dukke opp, vi lar standardverdiene stå og trykker på åpne kanal-knappen. Nå gjentar vi handlingen, men denne gangen fra Bob til Alice, slik at begge nodene kan sende og motta penger.

## Nodemon

For å unngå å måtte starte nodejs på nytt hver gang vi gjør en endring i koden, vil vi installere nodemon

```
$ npm install nodemon -D
```

Vi må opprette en oppføring i scripts-delen av package.json-filen, legg til denne linjen "dev": "nodemon ./bin/www", scripts-delen bør se slik ut:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Gå til konsollen der npm start kjører, trykk ctrl + c og start nodejs igjen, men denne gangen ved hjelp av nodemon

```
$ npm run dev
```

## Koble til LND

For å koble til en Lightning-node fra nodejs, vil vi bruke biblioteket ln-service, vi vil også installere dotenv for å håndtere miljøvariabler.

```
$ npm install ln-service dotenv
I vår lnapp-mappe, opprett en fil kalt .env, den skal inneholde disse variablene:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Gå tilbake til Polar, velg Bob, noden vi ønsker å koble til, gå til "Connect"-fanen, kopier innholdet av GRPC Host og plasser det i LND_GRPC_HOST-variabelen, i den nedre delen av connect-fanen velger du base64 og kopier innholdet av TLS Cert og plasser det i LND_CERT_BASE64-variabelen, og gjør det samme med admin macaroon i LND_MACAROON_BASE64.

Nå legger du til denne linjen i app.js-filen som ligger i roten av arbeidsmappen, vi må kopiere den på den første linjen i filen.

```
require('dotenv').config();
```

For å verifisere at nodejs kan koble til vår node, åpne routes/index.js-filen, denne rute-filen ble opprettet av express-generatoren, først krever vi ln-service-biblioteket, så vi legger det til på den første linjen

```
const lnservice = require('ln-service');
```

Vi legger til en ny rute som vil gi oss informasjon om vår node.

```
router.get('/info', async function(req, res, next) {
try {
// autentiser med lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// få nodeinformasjon
const info = await lnservice.getWalletInfo({ lnd });

    // vis info i json-format
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

Nå gå til denne adressen http://localhost:3000/info

Hvis du ser en json med informasjonen om LND-noden, gratulerer!!! appen din kan nå samhandle med Lightning Network.
Opprette en falsk modell

For å simulere en database, trenger vi å opprette en falsk modell, dette vil tillate oss å bruke appen uten å installere og konfigurere en database.

Først, installer uuid-pakken

```
$ npm install uuid
```

Opprett models-mappen og inni den, opprett Post.js-filen med følgende innhold:

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

```markdown
oppdatertInnlegg = { ...p, betalt: true };        return oppdatertInnlegg;
      }
      return p;
    });
    if (oppdatertInnlegg) {
      return true;
    }
    return false;
  }
}

const innlegg = new Post();

module.exports = innlegg;
```

## Forbered visningen

Vi trenger bootstrap for å få vår html til å se bedre ut, så vi endrer layout.pug-filen som ligger i views-mappen til å se slik ut:

```
doctype html
html
  head
    title= tittel
    link(rel='stylesheet', href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css')
    link(rel='stylesheet', href='/stylesheets/style.css')
  body
    block innhold
    block skript
      script(src="https://code.jquery.com/jquery-3.4.1.min.js")
      script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js")
      script(src="/javascripts/main.js")
```

## Lage et innlegg

For å lage et innlegg, trenger vi et skjema. Inne i views-mappen, opprett en fil kalt form.pug med følgende innhold:

```
.collapse#post-form
  form
    h2 Skriv en artikkel
    .form-group
      label(for="name") Navn
      input(id="name").form-control
    .form-group
      label(for="content") Innhold
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Send
```

## Javascript i frontend

Den mest direkte måten vi har for å samhandle med brukeren på er ved å bruke javascript i nettleseren. For dette, opprett en fil kalt main.js i javascript-mappen, som vi allerede kaller fra layout.pug. I denne filen, initialiser prosjektet. Det innledende innholdet av main.js er som følger:

```
const App = {
  endpoint: 'http://localhost:3000/api',
  intervall: null,
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

Klikk på "Send"-knappen og hvis alt er i orden, bør den vise en melding "!hola" i konsollen. Nå kan vi modifisere App.sendBtn()-metoden for å sende informasjonen til vår API.

```
App.sendBtn = async () => {
  const navn = $('#name').val();
  const innhold = $('#content').val();
  const respons = await App.makeRequest({
    api: "post",
    post: { navn, innhold },
  });
  if (!respons) console.error('Feil ved henting av data!');
  if (respons.success) {
    // Gjør noe med responsen
  }
};
```

```markdown
// Skriv ut dataene som kommer fra API-en til konsollen
console.log(respons.data);
}
};
```

Vi oppretter også metoden App.makeRequest() og legger den til i main.js

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

## Opprett API-et

For å gjøre dette, trenger vi å opprette en ny fil i routes/api.js og skrive metoden som svarer på forespørselen gjort innen App.sendBtn().

```markdown
const express = require('express');
```
```markdown
const lnservice = require('ln-service');
const router = express.Router();
const post = require('../models/Post');

router.post('/post', (req, res) => {
const { name, content } = req.body;
return res.json({
suksess: true,
data: { name, content },
});
});

module.exports = router;
```

Denne filen må inkluderes i app.js, så vi legger til disse linjene:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

La oss trykke på send-knappen igjen, og den skal svare med de samme dataene vi skrev inn i skjemaet.

## Opprette fakturaen

Metoden som utføres når en bruker oppretter et innlegg, skal generere en faktura, deretter opprette en post i databasen som lenker den til fakturaen, og returnere fakturaen til brukeren slik at de kan betale den.

```markdown
router.post('/post', async (req, res) => {
// Autentiser med lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

const { name, content } = req.body;
prøv {
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
suksess: true,
data: p,
});
}
} catch (e) {
console.log(e);
}
});
```

Hvis vi mottar et post-objekt som respons etter å ha trykket send, slik som dette, har alt gått riktig. Nå trenger vi å vise teksten slik at brukeren kan betale den.

```markdown
{
"suksess":true,
"data":{
"id":"0fb1544a-d7f9-487d-961a-d0004ecc515c",
"time":"2020-09-02T21:29:53.747Z",
"name":"epale",
"content":"contenido bla bla",
"betalt":false,
"hash":"0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
"preimage":null,
}
```

## Ny fakturavisning

I views-mappen trenger vi å opprette en fil kalt invoice.pug med følgende innhold:

```
.collapse#invoice-form
form
.h2 Betal denne fakturaen
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Og inkluder den i index.pug

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Modifisere App.sendBtn()

Nå modifiserer vi App.sendBtn() for å vise de oppnådde dataene:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Feil ved henting av data!');
if (response.suksess) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Motta betalingen
Vi trenger å vite når vi mottar betalingen, for dette vil vi bruke subscribeToInvoices()-metoden fra lnservice. Denne metoden lar oss utføre kode når statusen til en faktura har blitt oppdatert. For å bruke den legger vi til disse linjene i app.js.

```
// krever lnservice og vår post-tabell
const lnservice = require('ln-service');
const post = require('./models/Post');

// autentiser med lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// sjekk om fakturaen har blitt betalt hver gang en faktura blir oppdatert
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // marker fakturaen som 'betalt'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Faktura betalt!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// start abonnementet på faktura
subscribeInvoices();
```

Opprett en HTTP GET-metode i vår API slik at brukeren kan sjekke om en hash har blitt betalt.

````
router.get('/post/:hash', (req, res) => {
const { hash } = req.params;
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

Nå, fra main.js, lager vi en funksjon kalt App.waitPayment() som spør API-et om betalingen har blitt gjort.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Betaling utført");
  }
};
```

Nå støter vi på et problem, funksjonen App.waitPayment() blir bare utført én gang, brukeren kan ha gjort betalingen og vi har ikke kunnet indikere at deres betaling har blitt mottatt. For dette bruker vi en JavaScript-funksjon kalt setInterval() som lar oss utføre en funksjon på ubestemt tid med det tidsintervallet vi har angitt.

La oss modifisere funksjonene App.waitPayment() og App.sendBtn() inkludert setInterval() og clearInterval()

```javascript
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
    post: { name, content },
  });
  if (!response) console.error("Feil ved henting av data!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Og vi lager en visning for å indikere at betalingen har blitt mottatt, vi oppretter filen success.pug i visninger med følgende innhold:
```pug
.collapse#success
  h2 Betaling vellykket
  div Betalingsbevis:
    #preimage
```

Vi inkluderer den i index.pug.

```pug
extends layout

block content
  h1 Lyn App
  include form.pug
  include invoice.pug
  include success.pug
```

Hvis du etter å ha betalt fakturaen kan se meldingen "Betaling vellykket" og betalingsbeviset, gratulerer!!! du klarte det, du har fullført din første LApp.