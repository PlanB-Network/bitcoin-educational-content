```
---
nimi: LAPP bitcoin
kuvaus: Opas ensimmäisen LAppisi kehittämiseen
---

Opi koodaamaan ensimmäinen salamaverkko-sovelluksesi

Vaatimukset:

- NodeJs >= 8
- LND >= 9

NodeJs:n voi ladata sen virallisilta verkkosivuilta

Sen sijaan, että lataisit ja asentaisit LND-noden, käytämme polar-työkalua, joka suorittaa tämän tehtävän puolestamme.

Salamaverkko-sovelluksemme rakentamiseen käytämme seuraavia teknologioita:

- Express web-palvelimellemme
- Pug-mallit + bootstrap käyttöliittymällemme

## Käyttöjärjestelmä

Linuxin käyttöä suositellaan, jos käytät Windows 10:tä, voit saada Linux-konsolin noudattamalla näitä muutamia vaiheita.
Perustan valmistelu

Käytä sovellusgeneraattorityökalua, express, luodaksesi nopeasti sovellusrungon.

```
$ sudo npm install express-generator -g
```

Seuraavalla komennolla luomme Express-sovelluksen nimeltä lnapp. Sovellus luodaan hakemistoon nimeltä lnapp nykyisessä työhakemistossa, ja näkymämoottoriksi määritetään Pug.

```
$ express --view=pug lnapp
```

Sitten menemme hakemistoon ja asennamme tarvittavat paketit web-palvelimen ajamiseksi.

```
$ cd myapp
$ npm install
```

Nyt käynnistämme palvelimen yksinkertaisesti

```
$ npm start
```

Seuraavaksi, mene osoitteeseen http://localhost:3000 selaimessa päästäksesi sovellukseen.

Luodulla sovelluksella on seuraava hakemistorakenne:

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

Lataa Polar, asenna se ja luo verkko, jossa on 2 LND-nodia (Alice ja Bob) ja 1 bitcoind. Kun näemme sovelluksessa graafin, joka näyttää nodemme, klikkaa Aloita-painiketta ja odota muutama sekunti, kunnes kunkin noden indikaattori vaihtaa väriä vihreäksi.

Maksujen lähettämiseksi salamaverkossa nodien on oltava yhdistettyinä kanavien kautta. Kanavien luominen Polarilla on hyvin yksinkertaista, meidän tarvitsee vain klikata hiirellä yhtä Alicen noden korvista ja vetää se yhteen Bobin noden korvista. Välittömästi pitäisi ilmestyä modaalinen ikkuna, jonka otsikko on Avaa uusi kanava, jätämme oletusarvot ja painamme avaa kanava -painiketta. Nyt toistamme toimenpiteen, mutta tällä kertaa Bobista Aliceen, näin molemmat nodet voivat lähettää ja vastaanottaa rahaa.

## Nodemon

Välttääksemme NodeJS:n uudelleenkäynnistyksen joka kerta, kun teemme muutoksen koodiin, asennamme nodemonin

```
$ npm install nodemon -D
```

Meidän on luotava merkintä package.json-tiedoston scripts-osioon, lisää tämä rivi "dev": "nodemon ./bin/www", scripts-osion pitäisi näyttää tältä:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Mene konsoliin, jossa npm start on käynnissä, paina ctrl + c ja käynnistä nodejs uudelleen, mutta tällä kertaa käyttäen nodemonia

```
$ npm run dev
```

## Yhdistäminen LND:hen

Yhdistääksemme salamaverkon nodeen nodejs:stä, käytämme ln-service-kirjastoa, asennamme myös dotenvin ympäristömuuttujien hallintaan.

```
$ npm install ln-service dotenv
```
Meidän lnapp-hakemistossa, luo tiedosto nimeltä .env, sen tulisi sisältää nämä muuttujat:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Palaa takaisin Polar-sovellukseen, valitse Bob, solmu johon haluamme yhdistää, mene "Yhdistä" välilehdelle, kopioi GRPC Hostin sisältö ja sijoita se LND_GRPC_HOST muuttujaan, alaosassa valitse base64 ja kopioi TLS Certin sisältö ja sijoita se LND_CERT_BASE64 muuttujaan, ja tee sama admin macaroonille LND_MACAROON_BASE64 muuttujaan.

Lisää nyt tämä rivi app.js tiedostoon, joka sijaitsee työhakemiston juuressa, meidän täytyy kopioida se tiedoston ensimmäiselle riville.

```
require('dotenv').config();
```

Varmistaaksemme, että nodejs voi yhdistää solmuumme, avaa routes/index.js tiedosto, tämä reittitiedosto luotiin express-generaattorilla, ensin vaadimme ln-service kirjaston, joten lisäämme sen ensimmäiselle riville

```
const lnservice = require('ln-service');
```

Lisäämme uuden reitin, joka antaa meille tietoa solmustamme.

```
router.get('/info', async function(req, res, next) {
try {
// todenna lnd:hen
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// hanki solmun tiedot
const info = await lnservice.getWalletInfo({ lnd });

    // näytä tiedot json-muodossa
    res.send(`
      <h1>Solmun tiedot</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Mene nyt osoitteeseen http://localhost:3000/info

Jos näet jsonin LND-solmun tiedoilla, onnittelut!!! sovelluksesi voi nyt olla vuorovaikutuksessa Lightning-verkon kanssa.
Luodaan feikkimalli

Simuloidaksemme tietokantaa, meidän tarvitsee luoda feikkimalli, tämä mahdollistaa sovelluksen käytön ilman tietokannan asentamista ja konfigurointia.

Asenna ensin uuid-paketti

```
$ npm install uuid
```

Luo models-hakemisto ja sen sisälle, luo Post.js tiedosto seuraavalla sisällöllä:

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
```javascript
päivitettyPosti = { ...p, paid: true };        return päivitettyPosti;
      }
      return p;
    });
    if (päivitettyPosti) {
      return true;
    }
    return false;
  }
}

const postaukset = new Post();

module.exports = postaukset;
```

## Valmistele näkymä

Tarvitsemme bootstrapin, jotta HTML näyttäisi paremmalta, joten muokkaamme layout.pug-tiedostoa views-kansiossa näyttämään tältä:

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

## Postauksen luominen

Postauksen luomiseen tarvitsemme lomakkeen. Luo views-kansioon tiedosto nimeltä form.pug seuraavalla sisällöllä:

```
.collapse#post-form
  form
    h2 Kirjoita artikkeli
    .form-group
      label(for="name") Nimi
      input(id="name").form-control
    .form-group
      label(for="content") Sisältö
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Lähetä
```

## Javascript etupäässä

Suorin tapa vuorovaikuttaa käyttäjän kanssa on käyttämällä javascriptiä web-selaimessa. Tätä varten, luo tiedosto nimeltä main.js javascript-kansioon, jota layout.pug jo kutsuu. Tiedoston alkuun tuleva sisältö on seuraava:

```javascript
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

Klikkaa "Lähetä"-painiketta ja jos kaikki on kunnossa, sen pitäisi näyttää viesti "!hola" konsolissa. Nyt voimme muokata App.sendBtn()-metodia lähettämään tiedot API:lle.

```javascript
App.sendBtn = async () => {
  const nimi = $('#name').val();
  const sisältö = $('#content').val();
  const vastaus = await App.makeRequest({
    api: "post",
    post: { nimi, sisältö },
  });
  if (!vastaus) console.error('Virhe tiedon haussa!');
  if (vastaus.success) {
    // Tee jotain vastauksen kanssa
  }
};
```

```markdown
// Tulosta konsoliin tieto, joka tulee API:lta
console.log(vastaus.data);
}
};
```

Lisäämme myös metodin App.makeRequest() ja lisäämme sen main.js-tiedostoon

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

## Luo API

Tämän tekemiseksi meidän on luotava uusi tiedosto routes/api.js-kansioon ja kirjoitettava metodi, joka vastaa App.sendBtn()-metodissa tehtyyn pyyntöön.

```javascript
const express = require('express');
```
```markdown
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

Tämä tiedosto on sisällytettävä app.js-tiedostoon, joten lisäämme seuraavat rivit:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Painaessamme lähetä-painiketta uudelleen, sen pitäisi vastata samalla datalla, jonka syötämme lomakkeeseen.

## Luo lasku

Metodi, joka suoritetaan kun käyttäjä luo postauksen, pitäisi generoida lasku, luoda tietue tietokantaan ja linkittää se laskuun, ja palauttaa lasku käyttäjälle, jotta hän voi maksaa sen.

```markdown
router.post('/post', async (req, res) => {
// Autentikoi lnd:n kanssa
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

Jos vastauksena saamme post-objektin painettuamme lähetä-painiketta, kuten tässä, kaikki on mennyt oikein. Nyt meidän tarvitsee näyttää teksti, jotta käyttäjä voi maksaa sen.

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

## Uusi laskunäkymä

Views-hakemistossa meidän tarvitsee luoda tiedosto nimeltä invoice.pug seuraavalla sisällöllä:

```
.collapse#invoice-form
form
.h2 Maksa tämä lasku
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Ja sisällytä se index.pug-tiedostoon

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Muokataan App.sendBtn()

Nyt muokkaamme App.sendBtn() näyttämään saadut tiedot:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Virhe datan saamisessa!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Maksun vastaanottaminen
Meidän on tiedettävä, milloin maksu on vastaanotettu, tätä varten käytämme `subscribeToInvoices()`-metodia lnservice-palvelusta. Tämä metodi mahdollistaa koodin suorittamisen, kun laskun tila on päivitetty. Käyttääksemme sitä lisäämme seuraavat rivit tiedostoon app.js.
```
// vaaditaan lnservice ja meidän post-taulukko
const lnservice = require('ln-service');
const post = require('./models/Post');

// todennetaan lnd:n kanssa
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// tarkistetaan onko lasku maksettu aina kun laskun tila päivittyy
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // merkitään lasku 'maksetuksi'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Lasku maksettu!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// aloitetaan laskujen tilauksen seuranta
subscribeInvoices();
```

Luo HTTP GET -metodi API:ssamme, jotta käyttäjä voi tarkistaa, onko hash maksettu.

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

Nyt, main.js-tiedostosta, luomme funktion nimeltä App.waitPayment(), joka kysyy API:lta, onko maksu suoritettu.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Maksu suoritettu");
  }
};
```

Nyt kohtaamme ongelman, funktio App.waitPayment() suoritetaan vain kerran, käyttäjä on saattanut suorittaa maksun, emmekä ole pystyneet ilmoittamaan, että heidän maksunsa on vastaanotettu. Tätä varten käytämme JavaScript-funktiota nimeltä setInterval(), joka mahdollistaa funktion suorittamisen toistuvasti määrittämämme aikavälin välein.

Muokataan funktioita App.waitPayment() ja App.sendBtn() sisällyttämällä setInterval() ja clearInterval()

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
  if (!response) console.error("Virhe tiedon haussa!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Ja luomme näkymän osoittamaan, että maksu on onnistuneesti vastaanotettu, luomme tiedoston success.pug näkymiin seuraavalla sisällöllä:
```pug
.collapse#success
  h2 Maksu onnistui
  div Maksutodiste:
    #preimage
```

Sisällytämme sen index.pug-tiedostoon.

```pug
extends layout

block content
  h1 Lightning-sovellus
  include form.pug
  include invoice.pug
  include success.pug
```

Jos maksun suorittamisen jälkeen näet viestin "Maksu onnistui" ja maksutodisteen, onneksi olkoon!!! olet onnistunut, olet saanut valmiiksi ensimmäisen LAppisi.