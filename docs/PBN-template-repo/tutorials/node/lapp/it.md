---
name: LAPP bitcoin
description: Tutorial per sviluppare la tua prima LApp
---

Impara a codificare la tua prima app Lightning

Requisiti:

- NodeJs >= 8
- LND >= 9

NodeJs può essere scaricato dal suo sito ufficiale

Invece di scaricare e configurare un nodo LND, utilizzeremo lo strumento Polar, che svolgerà questo compito per noi.

Per costruire la nostra app Lightning, utilizzeremo le seguenti tecnologie:

- Express per il nostro webserver
- Pug templates + bootstrap per il nostro frontend

## Sistema operativo

Si consiglia di utilizzare Linux, se si è su Windows 10 è possibile avere una console Linux seguendo questi pochi passaggi.
Preparazione della base

Utilizza lo strumento di generazione di applicazioni, express, per creare rapidamente uno scheletro di applicazione.

```
$ sudo npm install express-generator -g
```

Con il seguente comando creiamo un'applicazione Express chiamata lnapp. L'applicazione verrà creata in una directory chiamata lnapp nella directory di lavoro corrente e il motore di visualizzazione sarà impostato su Pug.

```
$ express --view=pug lnapp
```

Successivamente, entriamo nella directory e installiamo i pacchetti necessari per far funzionare il web server.

```
$ cd myapp
$ npm install
```

Ora avviamo semplicemente il server

```
$ npm start
```

Successivamente, visitiamo questo indirizzo http://localhost:3000 nel browser per accedere all'applicazione.

L'applicazione generata ha la seguente struttura delle directory:

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

Scarichiamo Polar, lo installiamo e creiamo una rete con 2 nodi LND (Alice e Bob) e 1 bitcoind, una volta che vediamo nel'app il grafico con i nostri nodi, facciamo clic sul pulsante Inizio e attendiamo alcuni secondi fino a quando l'indicatore di ogni nodo cambia colore in verde.

Per poter inviare pagamenti su Lightning è necessario che i nodi siano interconnessi tramite canali, creare canali con Polar è molto semplice, abbiamo solo bisogno di fare clic con il mouse su una delle orecchie del nodo Alice e trascinarla fino a una delle orecchie del nodo Bob, immediatamente dovrebbe apparire una finestra modale intitolata Apri nuovo canale, lasciamo i valori predefiniti e premiamo il pulsante apri canale, ora ripetiamo l'azione ma questa volta da Bob ad Alice, in questo modo entrambi i nodi possono inviare e ricevere denaro.

## Nodemon

Per non dover riavviare nodejs ogni volta che apportiamo una modifica al codice, installeremo nodemon

```
$ npm install nodemon -D
```

Dobbiamo creare una voce nella sezione degli script del file package.json, aggiungi questa riga "dev": "nodemon ./bin/www", la sezione degli script dovrebbe essere così:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Andiamo alla console dove npm start è in esecuzione, premiamo ctrl + c e riavviamo nodejs ma questa volta utilizzando nodemon

```
$ npm run dev
```

## Connettersi a LND

Per connetterci a un nodo Lightning da nodejs, utilizzeremo la libreria ln-service, installeremo anche dotenv per gestire le variabili di ambiente.

```
$ npm install ln-service dotenv
```

Nella nostra directory lnapp creiamo un file chiamato .env, dovrebbe contenere queste variabili:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Torniamo a Polar, selezioniamo Bob, il nodo a cui vogliamo connetterci, andiamo alla scheda "Connetti", copiamo il contenuto di Host GRPC e lo inseriamo nella variabile LND_GRPC_HOST, nella parte inferiore della scheda connetti selezioniamo base64 e copiamo il contenuto di TLS Cert e lo inseriamo nella variabile LND_CERT_BASE64 e facciamo lo stesso con l'admin macaroon in LND_MACAROON_BASE64.

Ora aggiungiamo questa riga al file app.js situato nella radice della directory di lavoro, dobbiamo copiarlo nella prima riga del file.

```
require('dotenv').config();
```

Per verificare che nodejs possa connettersi al nostro nodo apriamo il file routes/index.js, questo file di route è stato creato dal generatore express, prima richiediamo la libreria ln-service, quindi aggiungiamo nella prima riga

```
const lnservice = require('ln-service');
```

Aggiungiamo una nuova route che ci fornirà le informazioni sul nostro nodo.

```
router.get('/info', async function(req, res, next) {
try {
// ci autentichiamo con lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// otteniamo le informazioni sul nodo
const info = await lnservice.getWalletInfo({ lnd });

    // mostriamo le informazioni in formato json
    res.send(`
      <h1>Informazioni sul nodo</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Ora vai a questo indirizzo http://localhost:3000/info

Se vedi un json con le informazioni sul nodo LND, congratulazioni!!! la tua app può già interagire con Lightning Network.
Creazione di un modello falso

Per simulare un database, dobbiamo creare un modello falso, che ci permetterà di utilizzare l'app senza dover installare e configurare un database.

Prima installiamo il pacchetto uuid

```
$ npm install uuid
```

Crea la directory models e all'interno il file Post.js con il seguente contenuto:

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

## Prepariamo la vista

Abbiamo bisogno di boostrap per migliorare l'aspetto del nostro html, quindi modifichiamo il file layout.pug che si trova nella cartella views in questo modo:

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

## Creare un post

Per creare un post abbiamo bisogno di un modulo, all'interno della cartella views creiamo un file chiamato form.pug contenente:

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

## Javascript en el frontend

La manera más directa que tenemos para interactuar con el usuario es utilizando javascript en el web browser, para esto, en el directorio javascript creamos un archivo main.js que ya estamos llamando desde el layout.pug, en el cual inicializamos el proyecto, el contenido inicial de main.js es el siguiente:

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

Premiamo il pulsante Send e, se tutto è a posto, dovrebbe mostrarci nella console un messaggio !hello, con il quale possiamo modificare il metodo App.sendBtn() per inviare le informazioni alla nostra API.

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
    // Do something
  }
};
```

```javascript
// imprimimos en la consola la data que viene de la APIconsole.log(response.data);
}
};
```

Creiamo anche il metodo App.makeRequest() e lo aggiungiamo a main.js.

```javascript
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

## Creiamo l'API

Per questo dobbiamo creare un nuovo file in routes/api.js e al suo interno scrivere il metodo che risponde alla richiesta che facciamo all'interno di App.sendBtn().

```javascript
const express = require("express");
const lnservice = require("ln-service");
const router = express.Router();
const post = require("../models/Post");

router.post("/post", (req, res) => {
  const { name, content } = req.body;
  return res.json({
    success: true,
    data: { name, content },
  });
});

module.exports = router;
```

Questo file deve essere incluso in app.js, per cui aggiungiamo queste righe:

```javascript
const apiRouter = require("./routes/api");
app.use("/api", apiRouter);
```

Premendo nuovamente il pulsante di invio, si dovrebbe ricevere una risposta con gli stessi dati digitati nel modulo.

## Creare la fattura

Il metodo che viene eseguito quando un utente crea un post, deve generare una fattura, quindi creare un record nel database collegandolo alla fattura e restituire la fattura all'utente in modo che possa pagarla.

```js
router.post("/post", async (req, res) => {
  // nos autenticamos con lnd
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

Se dopo aver premuto invio riceviamo come risposta un oggetto post, di questo tipo, tutto è andato correttamente, ora dobbiamo mostrare il testo in modo che l'utente possa pagare.

```json
{
  "success": true,
  "data": {
    "id": "0fb1544a-d7f9-487d-961a-d0004ecc515c",
    "time": "2020-09-02T21:29:53.747Z",
    "name": "epale",
    "content": "contenido bla bla",
    "paid": false,
    "hash": "0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
    "preimage": null,
    "request": "lnbcrt10u1p04qrk3pp5pc785y23mru0yq4uwfjdhql92nysp8um6vkqljcyzfmjkvgt2g8qdqgv4cxzmr9cqzpgxq92fjuqsp534n0k3up43xlrnwmh97kk9mtl89n7yvkrznhrmqd47yll8eux35s9qy9qsqc2nlv8nd5k9tam8m9tzrqr05n3dzllsqxzsxs62j2zl7k49up834eazq4lhpfkjysmgevu5memgj7g7cq0fujsqvf49et88sl7v8zlcq4mgxx9"
  }
}
```

## Nuova vista fattura

Nella directory views dobbiamo creare un file chiamato invoice.pug con il seguente contenuto:

```pug
.collapse#invoice-form
  form
    h2 Pague esta factura
    .form-group
      textarea(id="invoice", readonly, rows="5").form-control
```

E lo includiamo in index.pug

```
extends layout

block content
h1 App Lightning
include form.pug
include invoice.pug
```

## Modifica di App.sendBtn()

Ora modifichiamo App.sendBtn() per mostrare i dati ottenuti:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Errore nel recupero dei dati!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Ricezione del pagamento

Abbiamo bisogno di sapere quando riceviamo il pagamento, per questo utilizzeremo il metodo subscribeToInvoices() di lnservice, questo metodo ci permette di eseguire del codice quando lo stato di una fattura viene aggiornato, per utilizzarlo aggiungiamo queste righe in app.js.

```
// facciamo il require di lnservice e del nostro modello post
const lnservice = require('ln-service');
const post = require('./models/Post');

// ci autentichiamo con lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// ogni volta che avviene una modifica in una fattura controlliamo se la fattura
// è stata pagata
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // cambia la fattura a 'pagata'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Fattura pagata!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// avviamo la sottoscrizione alle fatture
subscribeInvoices();
```

Creiamo nella nostra API un metodo HTTP GET in modo che l'utente possa verificare se un hash è stato pagato.

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

Ahora desde main.js creamos una función llamada App.waitPayment() que consulta a la api si el pago ha sido realizado.

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

Ahora nos encontramos un problema, la función App.waitPayment() se ejecuta solo una vez, el usuario puede haber pagado y no le hemos podido indicar que su pago ha sido recibido, para esto utilizamos una función de javascript llamada setInterval() que nos permite ejecutar una función indefinidamente cada intérvalo de tiempo que le hayamos indicado.

Modifiquemos las funciones App.waitPayment() y App.sendBtn() incluyendo setInterval() y clearInterva()

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

Y creamos una vista para indicar que el pago ha sido recibido exitosamente, creamos el archivo success.pug en views con el siguiente contenido:

```
.collapse#success
  h2 Pago exitoso
  div Prueba de pago:
    #preimage
```

Lo incluimos en index.

```pug.
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

Si luego de pagar la invoice puedes ver el mensaje de Pago exitoso y la prueba de pago felicidades!!! lo lograste, has terminado tu primera LApp.
