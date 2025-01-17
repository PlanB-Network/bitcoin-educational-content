---
name: LAPP bitcoin
description: Tutoriál k vývoji vaší první LApp
---

Naučte se kódovat svou první lightning aplikaci

Požadavky:

- NodeJs >= 8
- LND >= 9

NodeJs můžete stáhnout z jeho oficiálních stránek

Místo stahování a nastavování LND uzlu použijeme nástroj polar, který tuto úlohu za nás provede.

Pro výstavbu naší Lightning aplikace budeme používat následující technologie:

- Express pro náš webový server
- Pug šablony + bootstrap pro naše frontend

## Operační systém

Doporučuje se použít Linux, pokud jste na Windows 10, můžete mít Linuxovou konzoli následováním těchto několika kroků.
Příprava základu

Použijte nástroj pro generování aplikací, express, pro rychlé vytvoření kostry aplikace.

```
$ sudo npm install express-generator -g
```

S následujícím příkazem vytvoříme Express aplikaci s názvem lnapp. Aplikace bude vytvořena ve složce s názvem lnapp v aktuálním pracovním adresáři a jako šablonovací engine bude přiřazen Pug.

```
$ express --view=pug lnapp
```

Poté vstoupíme do adresáře a nainstalujeme potřebné balíčky pro běh webového serveru.

```
$ cd myapp
$ npm install
```

Nyní jednoduše spustíme server

```
$ npm start
```

Dále přejděte na tuto adresu http://localhost:3000 v prohlížeči pro přístup k aplikaci.

Vygenerovaná aplikace má následující strukturu adresářů:

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

Stáhněte Polar, nainstalujte ho a vytvořte síť se 2 LND uzly (Alice a Bob) a 1 bitcoind. Jakmile v aplikaci uvidíme graf zobrazující naše uzly, klikneme na tlačítko Start a počkáme několik sekund, dokud se indikátor každého uzlu nezmění na zelenou.

Pro odesílání plateb přes Lightning je nutné, aby byly uzly propojeny prostřednictvím kanálů. Vytvoření kanálů s Polar je velmi jednoduché, stačí kliknout myší na jedno ucho uzlu Alice a přetáhnout ho na jedno ucho uzlu Boba. Okamžitě by se mělo objevit modální okno s názvem Otevřít nový kanál, ponecháme výchozí hodnoty a stiskneme tlačítko otevřít kanál. Nyní akci opakujeme, ale tentokrát od Boba k Alici, takto oba uzly mohou posílat a přijímat peníze.

## Nodemon

Abychom nemuseli restartovat nodejs pokaždé, když provedeme změnu v kódu, nainstalujeme nodemon

```
$ npm install nodemon -D
```

Musíme vytvořit záznam v sekci skriptů souboru package.json, přidejte tento řádek "dev": "nodemon ./bin/www", sekce skriptů by měla vypadat takto:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Přejděte na konzolu, kde běží npm start, stiskněte ctrl + c a znovu spusťte nodejs, ale tentokrát pomocí nodemonu

```
$ npm run dev
```

## Připojení k LND

Pro připojení k Lightning uzlu z nodejs použijeme knihovnu ln-service, také nainstalujeme dotenv pro správu environmentálních proměnných.

```
$ npm install ln-service dotenv
V našem adresáři lnapp vytvořte soubor s názvem .env, který by měl obsahovat tyto proměnné:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Vraťte se do Polar, vyberte Boba, uzel, ke kterému se chceme připojit, přejděte na kartu "Connect", zkopírujte obsah GRPC Host a vložte jej do proměnné LND_GRPC_HOST, ve spodní části karty connect vyberte base64 a zkopírujte obsah TLS Cert a vložte jej do proměnné LND_CERT_BASE64 a to samé proveďte s admin macaroon do LND_MACAROON_BASE64.

Nyní přidejte tento řádek do souboru app.js umístěného v kořenovém adresáři pracovního adresáře, musíme jej zkopírovat na první řádek souboru.

```
require('dotenv').config();
```

Abychom ověřili, že nodejs se může připojit k našemu uzlu, otevřete soubor routes/index.js, tento soubor s trasami byl vytvořen generátorem express, nejprve vyžadujeme knihovnu ln-service, takže ji přidáme na první řádek

```
const lnservice = require('ln-service');
```

Přidáme novou trasu, která nám poskytne informace o našem uzlu.

```
router.get('/info', async function(req, res, next) {
try {
// autentizace s lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// získání informací o uzlu
const info = await lnservice.getWalletInfo({ lnd });

    // zobrazení informací ve formátu json
    res.send(`
      <h1>Informace o uzlu</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Nyní přejděte na tuto adresu http://localhost:3000/info

Pokud vidíte json s informacemi o uzlu LND, gratulujeme!!! vaše aplikace nyní může interagovat s Lightning Network.
Vytvoření falešného modelu

Abychom simulovali databázi, potřebujeme vytvořit falešný model, což nám umožní používat aplikaci bez instalace a konfigurace databáze.

Nejprve nainstalujte balíček uuid

```
$ npm install uuid
```

Vytvořte adresář models a uvnitř něj vytvořte soubor Post.js s následujícím obsahem:

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
aktualizovanýPříspěvek = { ...p, paid: true };        return aktualizovanýPříspěvek;
      }
      return p;
    });
    if (aktualizovanýPříspěvek) {
      return true;
    }
    return false;
  }
}

const příspěvky = new Post();

module.exports = příspěvky;
```

## Připravte zobrazení

Potřebujeme bootstrap, aby náš html vypadal lépe, takže upravíme soubor layout.pug umístěný ve složce views, aby vypadal takto:

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

## Vytvoření příspěvku

Pro vytvoření příspěvku potřebujeme formulář. Uvnitř složky views vytvořte soubor s názvem form.pug s následujícím obsahem:

```
.collapse#post-form
  form
    h2 Napište článek
    .form-group
      label(for="name") Jméno
      input(id="name").form-control
    .form-group
      label(for="content") Obsah
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Odeslat
```

## Javascript na frontendu

Nejpřímější způsob, jakým můžeme interagovat s uživatelem, je použití javascriptu ve webovém prohlížeči. Pro tento účel vytvořte soubor s názvem main.js ve složce javascript, který již voláme z layout.pug. V tomto souboru inicializujte projekt. Počáteční obsah main.js je následující:

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
  console.log('!ahoj');
};

$(() => App.init());
```

Klikněte na tlačítko "Odeslat" a pokud je vše v pořádku, mělo by se v konzoli zobrazit zpráva "!ahoj". Nyní můžeme upravit metodu App.sendBtn() tak, aby posílala informace na naše API.

```
App.sendBtn = async () => {
  const name = $('#name').val();
  const content = $('#content').val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error('Chyba při získávání dat!');
  if (response.success) {
    // Něco udělejte s odpovědí
  }
};
```

```markdown
// Vytiskněte data, která přicházejí z API do konzole
console.log(response.data);
}
};
```

Také vytvoříme metodu App.makeRequest() a přidáme ji do main.js

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

## Vytvořte API

Pro toto potřebujeme vytvořit nový soubor v routes/api.js a napsat metodu, která reaguje na požadavek učiněný v rámci App.sendBtn().

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
success: true,
data: { name, content },
});
});

module.exports = router;
```

Tento soubor musí být zahrnut v app.js, takže přidáme tyto řádky:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Zmáčkněme znovu tlačítko odeslat a mělo by odpovědět stejnými daty, které jsme zadali do formuláře.

## Vytvoření faktury

Metoda, která se spustí, když uživatel vytvoří příspěvek, by měla generovat fakturu, poté vytvořit záznam v databázi, který ji propojí s fakturou, a vrátit fakturu uživateli, aby ji mohl zaplatit.

```markdown
router.post('/post', async (req, res) => {
// Autentizace s lnd
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

Pokud jako odpověď po stisknutí tlačítka Odeslat obdržíme objekt příspěvku, jako je tento, vše proběhlo správně. Nyní potřebujeme zobrazit text, aby uživatel mohl platbu provést.

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

## Nový pohled na fakturu

Ve složce views potřebujeme vytvořit soubor s názvem invoice.pug s následujícím obsahem:

```
.collapse#invoice-form
form
.h2 Zaplaťte tuto fakturu
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

A zahrnout ho do index.pug

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Úprava App.sendBtn()

Nyní upravíme App.sendBtn(), aby zobrazil získaná data:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Chyba při získávání dat!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Přijetí platby
Potřebujeme vědět, kdy obdržíme platbu, k tomu použijeme metodu `subscribeToInvoices()` z `lnservice`. Tato metoda nám umožňuje spustit kód, když byl stav faktury aktualizován. Abychom ji použili, přidáme tyto řádky do `app.js`.

```javascript
// vyžadujeme lnservice a naši tabulku post
const lnservice = require('ln-service');
const post = require('./models/Post');

// autentizace s lnd
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// kontrola, zda byla faktura zaplacena pokaždé, když je faktura aktualizována
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // označit fakturu jako 'zaplacenou'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Faktura zaplacena!');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// spustit odběr faktur
subscribeInvoices();
```

Vytvořte HTTP GET metodu v našem API, aby uživatel mohl zkontrolovat, zda byl hash zaplacen.

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

Nyní, z `main.js`, vytvoříme funkci nazvanou `App.waitPayment()`, která dotazuje API, zda byla platba provedena.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Platba provedena");
  }
};
```

Nyní narazíme na problém, funkce `App.waitPayment()` je spuštěna pouze jednou, uživatel mohl provést platbu a my jsme nemohli indikovat, že jejich platba byla přijata. K tomu použijeme JavaScriptovou funkci nazvanou `setInterval()`, která nám umožňuje neustále spouštět funkci v intervalu času, který jsme určili.

Upravme funkce `App.waitPayment()` a `App.sendBtn()` včetně `setInterval()` a `clearInterval()`

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
  if (!response) console.error("Chyba při získávání dat!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
A vytvoříme pohled, který naznačuje, že platba byla úspěšně přijata, vytvoříme soubor success.pug ve složce views s následujícím obsahem:
```pug
.collapse#success
  h2 Platba úspěšná
  div Důkaz platby:
    #preimage
```

Zahrneme ho do index.pug.

```pug
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

Pokud po zaplacení faktury uvidíte zprávu "Platba úspěšná" a důkaz o platbě, gratulujeme!!! podařilo se vám, dokončili jste svou první LApp.