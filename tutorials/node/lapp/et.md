---
nimi: LAPP bitcoin
kirjeldus: Juhend oma esimese LApp'i arendamiseks
---

Õpi kodeerima oma esimest välgu rakendust

Nõuded:

- NodeJs >= 8
- LND >= 9

NodeJs'i saab alla laadida selle ametlikult veebilehelt

LND sõlme allalaadimise ja seadistamise asemel kasutame polar tööriista, mis teeb selle ülesande meie eest ära.

Oma välgu rakenduse ehitamiseks kasutame järgmisi tehnoloogiaid:

- Express meie veebiserveri jaoks
- Pug mallid + bootstrap meie kasutajaliidese jaoks

## Operatsioonisüsteem

Soovitatav on kasutada Linuxit, kui olete Windows 10 peal, saate Linuxi konsooli järgides neid mõningaid samme.
Aluse ettevalmistamine

Kasutage rakenduse generaatori tööriista, express, et kiiresti luua rakenduse skelett.

```
$ sudo npm install express-generator -g
```

Järgneva juhisega loome Express rakenduse nimega lnapp. Rakendus luuakse praeguses töökataloogis asuvasse kausta nimega lnapp ja vaate mootoriks määratakse Pug.

```
$ express --view=pug lnapp
```

Seejärel sisenege kataloogi ja installige vajalikud paketid veebiserveri töötamiseks.

```
$ cd myapp
$ npm install
```

Nüüd lihtsalt käivitame serveri

```
$ npm start
```

Järgmiseks minge aadressile http://localhost:3000 brauseris, et pääseda rakendusele ligi.

Genereeritud rakendusel on järgmine kataloogistruktuur:

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

Laadige alla Polar, installige see ja looge võrk 2 LND sõlmega (Alice ja Bob) ning 1 bitcoind. Kui näeme rakenduses graafikut, mis näitab meie sõlmi, klõpsake nupul Start ja oodake mõni sekund, kuni iga sõlme indikaator muutub roheliseks.

Maksete saatmiseks Lightningis on vajalik, et sõlmed oleksid ühendatud kanalite kaudu. Kanalite loomine Polariga on väga lihtne, me lihtsalt peame klõpsama hiirega ühel Alice sõlme kõrvast ja lohistama selle ühele Bob sõlme kõrvale. Kohe peaks ilmuma modaalaken pealkirjaga Ava uus kanal, jätame vaikimisi väärtused ja vajutame kanali avamise nuppu. Nüüd kordame tegevust, aga seekord Bobist Aliceni, nii saavad mõlemad sõlmed raha saata ja vastu võtta.

## Nodemon

Selleks, et ei peaks iga koodimuudatuse järel nodejs'i uuesti käivitama, installime nodemoni

```
$ npm install nodemon -D
```

Peame looma sissekande package.json faili skriptide sektsiooni, lisage see rida "dev": "nodemon ./bin/www", skriptide sektsioon peaks välja nägema nii:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Minge konsooli, kus npm start töötab, vajutage ctrl + c ja käivitage nodejs uuesti, aga seekord kasutades nodemoni

```
$ npm run dev
```

## Ühendamine LND-ga

Lightning sõlmega ühenduse loomiseks nodejs'ist kasutame ln-service teeki, samuti installime dotenvi keskkonnamuutujate haldamiseks.

```
$ npm install ln-service dotenv
Meie lnapp kataloogis looge fail nimega .env, see peaks sisaldama järgnevaid muutujaid:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Minge tagasi Polarisse, valige Bob, sõlm, millega soovime ühendust luua, minge vahekaardile "Connect", kopeerige GRPC Hosti sisu ja asetage see LND_GRPC_HOST muutujasse, valige ühenduse vahekaardi alumises osas base64 ja kopeerige TLS Certi sisu ning asetage see LND_CERT_BASE64 muutujasse, ning tehke sama administraatori macarooniga LND_MACAROON_BASE64.

Nüüd lisage see rida app.js faili, mis asub töökataloogi juurkaustas, me peame selle kopeerima faili esimesele reale.

```
require('dotenv').config();
```

Et kontrollida, kas nodejs saab meie sõlmega ühendust luua, avage fail routes/index.js, see marsruutide fail loodi express generaatori abil, esmalt nõuame ln-service teeki, seega lisame selle esimesele reale

```
const lnservice = require('ln-service');
```

Lisame uue marsruudi, mis annab meile teavet meie sõlme kohta.

```
router.get('/info', async function(req, res, next) {
try {
// autentige lnd-ga
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// saage sõlme teavet
const info = await lnservice.getWalletInfo({ lnd });

    // kuvage info json formaadis
    res.send(`
      <h1>Sõlme info</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Nüüd minge aadressile http://localhost:3000/info

Kui näete jsonit LND sõlme teabega, palju õnne!!! teie rakendus saab nüüd suhelda Lightning Networkiga.
Võltsmudeli loomine

Et simuleerida andmebaasi, peame looma võltsmudeli, see võimaldab meil rakendust kasutada ilma andmebaasi installimise ja seadistamiseta.

Esmalt installige uuid pakett

```
$ npm install uuid
```

Looge models kataloog ja selles looge fail Post.js järgneva sisuga:

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
uuendatudPostitus = { ...p, tasuline: true };        return uuendatudPostitus;
      }
      return p;
    });
    if (uuendatudPostitus) {
      return true;
    }
    return false;
  }
}

const postitused = new Postitus();

module.exports = postitused;
```

## Valmistage vaade ette

Meil on vaja bootstrapi, et meie html näeks parem välja, seega muudame layout.pug faili, mis asub vaadete kaustas, järgmiselt:

```
doctype html
html
  head
    title= pealkiri
    link(rel='stylesheet', href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css')
    link(rel='stylesheet', href='/stylesheets/style.css')
  body
    block sisu
    block skriptid
      script(src="https://code.jquery.com/jquery-3.4.1.min.js")
      script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js")
      script(src="/javascripts/main.js")
```

## Postituse loomine

Postituse loomiseks on meil vaja vormi. Vaadete kaustas looge fail nimega form.pug järgmise sisuga:

```
.collapse#postitus-vorm
  form
    h2 Kirjutage artikkel
    .form-group
      label(for="name") Nimi
      input(id="name").form-control
    .form-group
      label(for="content") Sisu
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Saada
```

## Javascript esiküljel

Kõige otsesem viis kasutajaga suhtlemiseks on javascripti kasutamine veebibrauseris. Selleks looge javascript kaustas fail nimega main.js, mida me juba kutsusime layout.pug'st. Selles failis algatage projekt. main.js algne sisu on järgmine:

```
const Rakendus = {
  endpoint: 'http://localhost:3000/api',
  intervall: null,
};

Rakendus.init = () => {
  $('#postitus-vorm').collapse('show');
  $('#send-btn').click(Rakendus.sendBtn);
}

Rakendus.sendBtn = () => {
  console.log('!hola');
};

$(() => Rakendus.init());
```

Klõpsake nuppu "Saada" ja kui kõik on korras, peaks konsoolis kuvama sõnumi "!hola". Nüüd saame muuta Rakendus.sendBtn() meetodit, et saata teave meie API-le.

```
Rakendus.sendBtn = async () => {
  const nimi = $('#name').val();
  const sisu = $('#content').val();
  const vastus = await Rakendus.makeRequest({
    api: "post",
    post: { nimi, sisu },
  });
  if (!vastus) console.error('Viga andmete saamisel!');
  if (vastus.success) {
    // Tee midagi vastusega
  }
};
```

```markdown
// Prindi konsooli andmed, mis tulevad API-st
console.log(vastus.data);
}
};
```

Samuti loome meetodi Rakendus.makeRequest() ja lisame selle main.js

```markdown
Rakendus.makeRequest = ({api, post}) => {
const tüüp = !post ? 'GET' : 'POST';
const andmed = !!post ? JSON.stringify(post) : null;
return $.ajax(`${Rakendus.endpoint}/${api}`, {
tüüp,
andmed,
contentType: 'application/json',
dataType: 'json',
});
};
```

## API loomine

Selleks peame looma uue faili routes/api.js ja kirjutama meetodi, mis vastab päringule, mida tehti Rakendus.sendBtn() sees.

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
edu: true,
andmed: { name, content },
});
});

module.exports = router;
```

See fail tuleb lisada app.js faili, seega lisame järgmised read:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Vajutame uuesti saatmisnuppu ja see peaks vastama samade andmetega, mida vormis sisestasime.

## Arve loomine

Meetod, mis käivitatakse, kui kasutaja loob postituse, peaks genereerima arve, seejärel looma andmebaasis kirje, mis on seotud arvega, ja tagastama arve kasutajale, et ta saaks selle eest maksta.

```markdown
router.post('/post', async (req, res) => {
// Autentimine lnd-ga
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

const { name, content } = req.body;
proovi {
const invoice = await lnservice.createInvoice({
lnd,
tokens: 1000,
kirjeldus: name,
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
edu: true,
andmed: p,
});
}
} catch (e) {
console.log(e);
}
});
```

Kui saame vastuseks postituse objekti pärast saatmisnupu vajutamist, nagu see, on kõik õigesti läinud. Nüüd peame kuvama teksti, et kasutaja saaks selle eest maksta.

```markdown
{
"edu":true,
"andmed":{
"id":"0fb1544a-d7f9-487d-961a-d0004ecc515c",
"aeg":"2020-09-02T21:29:53.747Z",
"nimi":"epale",
"sisu":"contenido bla bla",
"makstud":false,
"hash":"0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
"preimage":null,
}
```

## Uus arve vaade

Vaadete kataloogis peame looma faili nimega invoice.pug järgmise sisuga:

```
.collapse#invoice-form
form
.h2 Maksa see arve
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Ja lisama selle index.pug faili

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Muudame App.sendBtn()

Nüüd muudame App.sendBtn(), et kuvada saadud andmed:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Viga andmete saamisel!');
if (response.edu) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.andmed.request);
}
};
```

## Makse vastuvõtmine
Me peame teadma, millal me makse kätte saame, selleks kasutame meetodit `subscribeToInvoices()` teenusest `lnservice`. See meetod võimaldab meil käivitada koodi, kui arve olek on uuendatud. Selle kasutamiseks lisame järgmised read faili `app.js`.

```javascript
// nõuame lnservice'i ja meie postituste tabelit
const lnservice = require('ln-service');
const post = require('./models/Post');

// autentime end lnd-ga
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// kontrollime, kas arve on makstud iga kord, kui arvet uuendatakse
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // märgime arve kui 'makstud'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Arve makstud!');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// alustame arvete tellimust
subscribeInvoices();
```

Loome meie API-s HTTP GET meetodi, et kasutaja saaks kontrollida, kas hash on makstud.

```javascript
router.get('/post/:hash', (req, res) => {
  const { hash } = req.params;
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
```

Nüüd, failist `main.js`, loome funktsiooni `App.waitPayment()`, mis pärib API-st, kas makse on tehtud.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Makse tehtud");
  }
};
```

Nüüd seisame silmitsi probleemiga, funktsioon `App.waitPayment()` käivitatakse ainult üks kord, kasutaja võib olla makse sooritanud ja me ei ole suutnud näidata, et nende makse on kätte saadud. Selleks kasutame JavaScripti funktsiooni `setInterval()`, mis võimaldab meil funktsiooni lõputult käivitada määratud ajavahemiku järel.

Muudame funktsioone `App.waitPayment()` ja `App.sendBtn()`, lisades `setInterval()` ja `clearInterval()`

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
  if (!response) console.error("Viga andmete saamisel!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Ja me loome vaate, et näidata, et makse on edukalt vastu võetud, loome faili success.pug vaadetes järgmise sisuga:
```pug
.collapse#success
  h2 Makse õnnestus
  div Maksetõend:
    #preimage
```

Lisame selle index.pug faili.

```pug
extends layout

block content
  h1 Lightning Rakendus
  include form.pug
  include invoice.pug
  include success.pug
```

Kui pärast arve tasumist näete sõnumit "Makse õnnestus" ja maksetõendit, palju õnne!!! Te tegite seda, olete lõpetanud oma esimese LApp'i.