# Guide för att utveckla din första LApp med LAPP bitcoin

Lär dig att koda din första lightning-app

Krav:

- NodeJs >= 8
- LND >= 9

NodeJs kan laddas ner från dess officiella webbplats.

Istället för att ladda ner och installera en LND-nod kommer vi att använda verktyget polar, som kommer att utföra denna uppgift åt oss.

För att bygga vår Lightning-app kommer vi att använda följande teknologier:

- Express för vår webbserver
- Pug-templates + bootstrap för vår frontend

## Operativsystem

Det rekommenderas att använda Linux. Om du använder Windows 10 kan du få en Linux-konsol genom att följa dessa steg.
Förberedelse av basen

Använd verktyget för att snabbt skapa en applikationsstruktur.

```
$ sudo npm install express-generator -g
```

Med följande instruktion skapar vi en Express-applikation som heter lnapp. Applikationen kommer att skapas i en katalog som heter lnapp i den aktuella arbetskatalogen, och vy-motorn kommer att tilldelas Pug.

```
$ express --view=pug lnapp
```

Sedan går vi in i katalogen och installerar de nödvändiga paketen för att webbservern ska kunna köras.

```
$ cd myapp
$ npm install
```

Nu kör vi helt enkelt servern

```
$ npm start
```

Gå sedan till denna adress http://localhost:3000 i webbläsaren för att komma åt applikationen.

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

Ladda ner Polar, installera det och skapa ett nätverk med 2 LND-noder (Alice och Bob) och 1 bitcoind. När vi ser grafen i appen som visar våra noder, klicka på Start-knappen och vänta några sekunder tills indikatorn för varje nod ändrar färg till grön.

För att kunna skicka betalningar på Lightning måste noderna vara sammankopplade genom kanaler. Att skapa kanaler med Polar är mycket enkelt, vi behöver bara klicka med musen på en av öronen på Alice-noden och dra den till en av öronen på Bob-noden. Omedelbart bör ett modalfönster med titeln "Öppna ny kanal" visas, vi lämnar standardvärdena och trycker på knappen för att öppna kanalen. Nu upprepar vi åtgärden men denna gång från Bob till Alice, på så sätt kan båda noderna skicka och ta emot pengar.

## Nodemon

För att slippa starta om nodejs varje gång vi gör en ändring i koden kommer vi att installera nodemon.

```
$ npm install nodemon -D
```

Vi måste skapa en post i avsnittet "scripts" i filen package.json, lägg till denna rad "dev": "nodemon ./bin/www", avsnittet "scripts" ska se ut så här:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Gå till konsolen där npm start körs, tryck på ctrl + c och starta nodejs igen men denna gång med nodemon

```
$ npm run dev
```

## Anslutning till LND

För att ansluta till en Lightning-nod från nodejs kommer vi att använda biblioteket ln-service, vi kommer också att installera dotenv för att hantera miljövariabler.
```$ npm install ln-service dotenv
```

I vår lnapp-katalog, skapa en fil som heter .env, den ska innehålla dessa variabler:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Gå tillbaka till Polar, välj Bob, noden vi vill ansluta till, gå till fliken "Connect", kopiera innehållet i GRPC Host och placera det i variabeln LND_GRPC_HOST, i den nedre delen av anslutningsfliken välj base64 och kopiera innehållet i TLS-certifikatet och placera det i variabeln LND_CERT_BASE64, och gör samma sak med admin macaroon i LND_MACAROON_BASE64.

Lägg nu till denna rad i app.js-filen som finns i rotkatalogen för arbetskatalogen, vi måste kopiera den på första raden i filen.

```
require('dotenv').config();
```

För att verifiera att nodejs kan ansluta till vår nod, öppna filen routes/index.js, denna routes-fil skapades av express-generatorn, först kräver vi ln-service-biblioteket, så vi lägger till det på första raden

```
const lnservice = require('ln-service');
```

Vi lägger till en ny route som ger oss information om vår nod.

```
router.get('/info', async function(req, res, next) {
try {
// autentisera med lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// få nodinformation
const info = await lnservice.getWalletInfo({ lnd });

    // visa informationen i json-format
    res.send(`
      <h1>Nodinfo</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Gå nu till denna adress http://localhost:3000/info

Om du ser en json med information om LND-noden, grattis!!! din app kan nu interagera med Lightning-nätverket.
Skapa en falsk modell

För att simulera en databas måste vi skapa en falsk modell, detta kommer att tillåta oss att använda appen utan att installera och konfigurera en databas.

Först, installera paketet uuid

```
$ npm install uuid
```

Skapa modellkatalogen och inuti den, skapa filen Post.js med följande innehåll:

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
```javascript
const express = require('express');
const router = express.Router();

router.post('/post', (req, res) => {
  const { name, content } = req.body;
  // Do something with the name and content
  res.json({ success: true });
});

module.exports = router;
```

Now we need to import and use this router in our main app file, app.js.

```javascript
const express = require('express');
const app = express();
const apiRouter = require('./routes/api');

app.use(express.json());
app.use('/api', apiRouter);

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

Now, when we click the "Enviar" button, the information will be sent to the API and the success message will be displayed in the console.
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

Denna fil måste inkluderas i app.js, så vi lägger till dessa rader:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Låt oss trycka på skicka-knappen igen och den bör svara med samma data som vi angav i formuläret.

## Skapa fakturan

Metoden som körs när en användare skapar ett inlägg bör generera en faktura, sedan skapa en post i databasen som länkar till fakturan och returnera fakturan till användaren så att de kan betala den.

```markdown
router.post('/post', async (req, res) => {
  // Autentisera med lnd
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

Om vi får ett postobjekt som svar efter att ha tryckt på skicka, som detta, har allt gått korrekt. Nu behöver vi visa texten så att användaren kan betala den.

```markdown
{
  "success": true,
  "data": {
    "id": "0fb1544a-d7f9-487d-961a-d0004ecc515c",
    "time": "2020-09-02T21:29:53.747Z",
    "name": "epale",
    "content": "contenido bla bla",
    "paid": false,
    "hash": "0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
    "preimage": null
  }
}
```

## Ny fakturavy

I katalogen views måste vi skapa en fil som heter invoice.pug med följande innehåll:

```
.collapse#invoice-form
form
  .h2 Betala denna faktura
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

## Modifiera App.sendBtn()

Nu ändrar vi App.sendBtn() för att visa den erhållna datan:

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

## Ta emot betalningen
Vi behöver veta när vi får betalningen, för detta kommer vi att använda metoden subscribeToInvoices() från lnservice. Denna metod gör det möjligt för oss att köra kod när statusen för en faktura har uppdaterats. För att använda den lägger vi till dessa rader i app.js.

```
// kräver lnservice och vår posttabell
const lnservice = require('ln-service');
const post = require('./models/Post');

// autentisera med lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// kontrollera om fakturan har betalats varje gång en faktura uppdateras
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // markera fakturan som 'betald'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Fakturan är betald!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// starta fakturaprenumerationen
subscribeInvoices();
```

Skapa en HTTP GET-metod i vår API för användaren att kontrollera om en hash har betalats.

```javascript
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
```

Nu, från main.js, skapar vi en funktion som heter App.waitPayment() som frågar API:et om betalningen har gjorts.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Betalning gjord");
  }
};
```

Nu stöter vi på ett problem, funktionen App.waitPayment() körs bara en gång, användaren kan ha gjort betalningen och vi har inte kunnat indikera att deras betalning har mottagits. För detta använder vi en JavaScript-funktion som heter setInterval() som gör det möjligt för oss att köra en funktion oändligt med det angivna tidsintervallet.

Låt oss ändra funktionerna App.waitPayment() och App.sendBtn() genom att inkludera setInterval() och clearInterval()

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
  if (!response) console.error("Fel vid hämtning av data!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Och vi skapar en vy för att indikera att betalningen har mottagits framgångsrikt, vi skapar filen success.pug i vyer med följande innehåll:
```pug
.collapse#success
  h2 Betalning lyckades
  div Betalningsbevis:
    #preimage
```

Vi inkluderar den i index.pug.

```pug
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

Om du efter att ha betalat fakturan kan se meddelandet "Betalning lyckades" och betalningsbeviset, grattis!!! Du har gjort det, du har slutfört din första LApp.