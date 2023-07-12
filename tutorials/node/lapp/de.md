---
name: LAPP bitcoin
description: Tutorial zur Entwicklung Ihrer ersten LApp
---

# Tutorial zum Entwickeln deiner ersten LApp

Lerne, wie du deine erste Lightning-App programmierst
Francisco Calderón veröffentlicht am 14. Juni 2021

https://grunch.dev/guides/lapp/

Voraussetzungen:

- NodeJs >= 8
- LND >= 9

NodeJs kann von der offiziellen Website heruntergeladen werden.

Anstatt einen LND-Knoten herunterzuladen und einzurichten, werden wir das Polar-Tool verwenden, das diese Aufgabe für uns übernimmt.

Für die Erstellung unserer Lightning-Anwendung werden wir die folgenden Technologien verwenden:

- Express für unseren Webserver
- Pug-Vorlagen + Bootstrap für unser Frontend

## Betriebssystem

Es wird empfohlen, Linux zu verwenden. Wenn Sie mit Windows 10 arbeiten, können Sie eine Linux-Konsole einrichten, indem Sie die folgenden Schritte ausführen.
Vorbereiten der Basis

Benutzen Sie das Anwendungsgenerator-Tool express, um schnell ein Anwendungsskelett zu erstellen.

```
$ sudo npm install express-generator -g
```

Mit der folgenden Anweisung erstellen wir eine Express-Anwendung namens lnapp. Die Anwendung wird in einem Verzeichnis namens lnapp im aktuellen Arbeitsverzeichnis erstellt und die View Engine wird Pug zugewiesen.

```
$ express --view=pug lnapp
```

Dann betreten wir das Verzeichnis und installieren die notwendigen Pakete, damit der Webserver läuft.

```
$ cd myapp
$ npm install
```

Nun starten wir einfach den Server

```
$ npm start
```

Als Nächstes rufen Sie im Browser die Adresse http://localhost:3000 auf, um auf die Anwendung zuzugreifen.

Die generierte Anwendung hat die folgende Verzeichnisstruktur:

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

Laden Sie Polar herunter, installieren Sie es, und erstellen Sie ein Netzwerk mit 2 LND-Knoten (Alice und Bob) und 1 Bitcoin. Sobald das Diagramm in der App unsere Knoten anzeigt, klicken Sie auf die Schaltfläche "Start" und warten Sie ein paar Sekunden, bis die Anzeige jedes Knotens die Farbe zu grün ändert.

Um Zahlungen über Lightning zu senden, müssen die Knoten über Kanäle miteinander verbunden sein. Das Erstellen von Kanälen mit Polar ist sehr einfach: Klicken Sie mit der Maus auf eines der Ohren des Alice-Knotens und ziehen Sie es auf eines der Ohren des Bob-Knotens. Sofort sollte ein modales Fenster mit dem Titel Open new channel erscheinen, lassen Sie die Standardwerte und drücken Sie die Schaltfläche open channel. Wiederholen Sie nun den Vorgang, aber dieses Mal von Bob zu Alice, so dass beide Knoten Geld senden und empfangen können.

## Nodemon

Um zu vermeiden, dass wir nodejs jedes Mal neu starten müssen, wenn wir eine Änderung am Code vornehmen, installieren wir nodemon

```
$ npm install nodemon -D
```

Wir müssen einen Eintrag im Skriptbereich der package.json-Datei erstellen. Fügen Sie diese Zeile hinzu: "dev": "nodemon ./bin/www". Der Skriptbereich sollte wie folgt aussehen:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Gehen Sie zur Konsole, auf der npm start ausgeführt wird, drücken Sie Strg + C und starten Sie Node.js erneut, diesmal mit nodemon.

```
$ npm run dev
```

## Verbindung zu LND

Um sich mit einem Lightning-Knoten von Node.js aus zu verbinden, verwenden wir die ln-service-Bibliothek und installieren dotenv, um Umgebungsvariablen zu verwalten.

```
$ npm install ln-service dotenv
```

Erstellen Sie in unserem lnapp-Verzeichnis eine Datei namens .env mit den folgenden Variablen:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Gehen Sie zurück zu Polar, wählen Sie Bob, den Knoten, mit dem wir uns verbinden möchten, wechseln Sie zum "Verbinden"-Tab, kopieren Sie den Inhalt von Host GRPC und fügen Sie ihn in die Variable LND_GRPC_HOST ein. Wählen Sie unten im Verbinden-Tab base64 aus und kopieren Sie den Inhalt von TLS Cert in die Variable LND_CERT_BASE64. Wiederholen Sie dies mit dem Admin-Macaroon in LND_MACAROON_BASE64.

Fügen Sie nun diese Zeile zur app.js-Datei im Stammverzeichnis des Arbeitsverzeichnisses hinzu. Kopieren Sie sie in die erste Zeile der Datei.

```
require('dotenv').config();
```

Um zu überprüfen, ob Node.js eine Verbindung zu unserem Knoten herstellen kann, öffnen Sie die Datei routes/index.js. Diese Routendatei wurde vom Express-Generator erstellt. Importieren Sie zuerst die ln-service-Bibliothek, indem Sie die erste Zeile hinzufügen:

```
const lnservice = require('ln-service');
```

Fügen Sie eine neue Route hinzu, die uns Informationen über unseren Knoten liefert.

```
router.get('/info', async function(req, res, next) {
try {
// Authentifizierung bei lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// Knoteninformationen abrufen
const info = await lnservice.getWalletInfo({ lnd });

    // Informationen im JSON-Format anzeigen
    res.send(`
      <h1>Knoteninformationen</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Gehen Sie nun zu dieser Adresse: http://localhost:3000/info

Wenn Sie ein JSON mit den Informationen des LND-Knotens sehen, herzlichen Glückwunsch! Ihre App kann nun mit dem Lightning-Netzwerk interagieren.
Erstellen eines falschen Modells

Um eine Datenbank zu simulieren, müssen wir ein falsches Modell erstellen. Dadurch können wir die App verwenden, ohne eine Datenbank installieren und konfigurieren zu müssen.

Installieren Sie zunächst das Paket uuid.

```
$ npm install uuid
```

Erstellen Sie das Verzeichnis "models" und darin die Datei "Post.js" mit dem folgenden Inhalt:

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
};

const posts = new Post();

module.exports = posts;
```

## Wir bereiten die Ansicht vor

Wir brauchen boostrap, um unser HTML besser aussehen zu lassen, also ändern wir die Datei layout.pug, die sich im Verzeichnis views befindet, so, dass sie wie folgt aussieht:

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

## Erstellen eines Beitrags

Um einen Beitrag zu erstellen, benötigen wir ein Formular. Im Verzeichnis views erstellen wir eine Datei namens form.pug, die Folgendes enthält:

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

## Javascript im Frontend

Der direkteste Weg, um mit dem Benutzer zu interagieren, ist die Verwendung von Javascript im Webbrowser. Dazu erstellen wir im Verzeichnis javascript eine Datei main.js, die wir bereits aus der layout.pug aufrufen, in der wir das Projekt initialisieren. main.js hat folgenden Inhalt

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

Wir drücken auf die Schaltfläche Senden und wenn alles in Ordnung ist, sollte in der Konsole eine !hello-Nachricht angezeigt werden. Damit können wir die Methode App.sendBtn() ändern, um die Informationen an unsere API zu senden.

```js
App.sendBtn = async () => {
  const name = $("#name").val();
  const content = $("#content").val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error("Error getting data!");
  if (response.success) {
    // imprimimos en la consola la data que viene de la API
    console.log(response.data);
  }
};
```

Tambien creamos el método App.makeRequest() y también lo agregamos a main.js

```js
App.makeRequest = ({ api, post }) => {
  const type = !post ? "GET" : "POST";
  const data = !!post ? JSON.stringify(post) : null;
  return $.ajax(`${App.endpoint}/${api}`, {
    type,
    data,
    contentType: "application/json",
    dataType: "json",
  });
};
```

## Wir erstellen die API

Dazu müssen wir eine neue Datei in routes/api.js erstellen und darin die Methode schreiben, die auf die Anfrage antwortet, die wir in App.sendBtn() machen.

```
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

Diese Datei muss in app.js eingebunden werden, indem wir diese Zeilen hinzufügen:

```
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Drücken wir erneut die Senden-Schaltfläche, sollte sie mit denselben Daten antworten, die wir im Formular eingegeben haben.

## Rechnung erstellen

Die Methode, die ausgeführt wird, wenn ein Benutzer einen Beitrag erstellt, sollte eine Rechnung generieren, dann einen Eintrag in der Datenbank erstellen, der mit der Rechnung verknüpft ist, und dem Benutzer die Rechnung zur Zahlung zurückgeben.

```
router.post('/post', async (req, res) => {
// Authentifizierung mit lnd
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

Wenn wir nach dem Drücken der Senden-Schaltfläche eine Post-Objektantwort erhalten, hat alles geklappt. Jetzt müssen wir den Text anzeigen, damit der Benutzer ihn bezahlen kann.

```
{
"success":true,
"data":{
"id":"0fb1544a-d7f9-487d-961a-d0004ecc515c",
"time":"2020-09-02T21:29:53.747Z",
"name":"epale",
"content":"contenido bla bla",
"paid":false,
"hash":"0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
"preimage":null,'
## Neue Rechnungsansicht
```

Im Verzeichnis "views" müssen wir eine Datei namens "invoice.pug" mit dem folgenden Inhalt erstellen:

```
.collapse#invoice-form
form
.h2 Bezahlen Sie diese Rechnung
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Und wir fügen es in "index.pug" ein:

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Ändern von App.sendBtn()

Jetzt ändern wir "App.sendBtn()", um die erhaltenen Daten anzuzeigen:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Fehler beim Abrufen der Daten!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Zahlungseingang

Wir müssen wissen, wann die Zahlung eingegangen ist. Dazu verwenden wir die Methode "subscribeToInvoices()" von "lnservice". Diese Methode ermöglicht es uns, Code auszuführen, wenn der Status einer Rechnung aktualisiert wurde. Um dies zu verwenden, fügen wir diese Zeilen in "app.js" hinzu.

```js
// hacemos el require de lnservice y de nuestra tabla post
const lnservice = require("ln-service");
const post = require("./models/Post");

// nos autenticamos con lnd
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// cada vez que ocurra un cambio en una invoice se chequea si la invoice
// ha sido pagada
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({ lnd });
    sub.on("invoice_updated", async (invoice) => {
      if (!invoice.is_confirmed) return;

      // cambia la invoice a 'pagada'
      const paid = post.paid(invoice.id);
      if (paid) console.log("Invoice paid!");
    });
  } catch (e) {
    console.log(e);
    return e;
  }
};
// iniciamos la subscripcion a invoices
subscribeInvoices();
```

Wir erstellen in unserer API eine HTTP GET-Methode, damit der Benutzer überprüfen kann, ob ein Hash bezahlt wurde.

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

Jetzt erstellen wir in main.js eine Funktion namens App.waitPayment(), die die API abfragt, ob die Zahlung erfolgt ist.

```
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("pago realizado");
  }
};
```

Jetzt haben wir ein Problem, die Funktion App.waitPayment() wird nur einmal ausgeführt, der Benutzer kann bezahlt haben und wir waren nicht in der Lage, anzuzeigen, dass seine Zahlung eingegangen ist, dafür verwenden wir eine Javascript-Funktion namens setInterval(), die es uns ermöglicht, eine Funktion auf unbestimmte Zeit jedes Zeitintervall auszuführen, das wir angegeben haben.

Ändern wir die Funktionen App.waitPayment() und App.sendBtn(), um setInterval() und clearInterva() einzubinden.

```js
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
  if (!response) console.error("Error getting data!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```

Und wir erstellen eine Ansicht, die anzeigt, dass die Zahlung erfolgreich eingegangen ist. Wir erstellen die Datei success.pug in views mit dem folgenden Inhalt:

```js
.collapse#success
  h2 Pago exitoso
  div Prueba de pago:
    #preimage

```

Wir nehmen sie in den Index auf.

```pug.
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

Wenn Sie nach dem Bezahlen der Rechnung die Meldung "Zahlung erfolgreich" und den Zahlungsnachweis sehen, herzlichen Glückwunsch!!! Sie haben es geschafft, Sie haben Ihre erste LApp abgeschlossen.

> [Link zum Originalartikel](https://grunch.dev/guides/lapp/) - Francisco Calderón veröffentlicht am 14. Juni 2021
