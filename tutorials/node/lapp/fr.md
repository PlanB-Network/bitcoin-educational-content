---
name: LAPP bitcoin
description: Tutorial pour développer votre première LApp
---

Apprenez à coder votre première application Lightning

Exigences:

- NodeJs >= 8
- LND >= 9

NodeJs peut être téléchargé sur son site officiel

Au lieu de télécharger et configurer un nœud LND, nous allons utiliser l'outil polar, qui effectuera cette tâche pour nous.

Pour construire notre application Lightning, nous utiliserons les technologies suivantes:

- Express pour notre serveur web
- Modèles Pug + bootstrap pour notre frontend

## Système d'exploitation

Il est recommandé d'utiliser Linux, si vous êtes sous Windows 10, vous pouvez avoir une console Linux en suivant ces quelques étapes.
Préparation de la base

Utilisez l'outil de génération d'applications, express, pour créer rapidement un squelette d'application.

```
$ sudo npm install express-generator -g
```

Avec l'instruction suivante, nous créons une application Express appelée lnapp. L'application sera créée dans un répertoire appelé lnapp dans le répertoire de travail actuel et le moteur de vues sera défini sur Pug.

```
$ express --view=pug lnapp
```

Ensuite, accédez au répertoire et installez les packages nécessaires pour que le serveur web fonctionne.

```
$ cd myapp
$ npm install
```

Maintenant, exécutez simplement le serveur

```
$ npm start
```

Ensuite, allez à cette adresse http://localhost:3000 dans le navigateur pour accéder à l'application.

L'application générée a la structure de répertoires suivante:

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

Téléchargez Polar, installez-le et créez un réseau avec 2 nœuds LND (Alice et Bob) et 1 bitcoind, une fois que nous voyons dans l'application le graphique montrant nos nœuds, cliquez sur le bouton "Commencer" et attendez quelques secondes jusqu'à ce que l'indicateur de chaque nœud passe au vert.

Pour pouvoir envoyer des paiements en Lightning, il est nécessaire que les nœuds soient interconnectés par des canaux, créer des canaux avec Polar est très simple, il suffit de cliquer avec la souris sur l'une des oreilles du nœud Alice et de la faire glisser jusqu'à l'une des oreilles du nœud Bob, une fenêtre modale intitulée "Ouvrir un nouveau canal" doit immédiatement apparaître, laissez les valeurs par défaut et appuyez sur le bouton "Ouvrir le canal", répétez maintenant l'action mais cette fois de Bob vers Alice, de cette manière les deux nœuds peuvent envoyer et recevoir de l'argent.

## Nodemon

Pour ne pas avoir à redémarrer nodejs à chaque fois que nous apportons une modification au code, nous installerons nodemon

```
$ npm install nodemon -D
```

Nous devons créer une entrée dans la section scripts du fichier package.json, ajoutez cette ligne "dev": "nodemon ./bin/www", la section scripts devrait ressembler à ceci:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Allons dans la console où npm start est en cours d'exécution, appuyez sur ctrl + c et redémarrez nodejs mais cette fois en utilisant nodemon

```
$ npm run dev
```

## Connexion à LND

Pour se connecter à un nœud Lightning depuis nodejs, nous utiliserons la bibliothèque ln-service, nous installerons également dotenv pour gérer les variables d'environnement.

```
$ npm install ln-service dotenv
```

Dans notre répertoire lnapp, créons un fichier appelé .env, il doit contenir ces variables:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Revenons à Polar, sélectionnons Bob, le nœud auquel nous voulons nous connecter, allons dans l'onglet "Connecter", copions le contenu de Host GRPC et le plaçons dans la variable LND_GRPC_HOST, dans la partie inférieure de l'onglet connecter, sélectionnons base64 et copions le contenu de TLS Cert et le plaçons dans la variable LND_CERT_BASE64, puis faisons de même avec le macaroon admin dans LND_MACAROON_BASE64.

Maintenant, ajoutons cette ligne au fichier app.js situé à la racine du répertoire de travail, nous devons la copier à la première ligne du fichier.

```
require('dotenv').config();
```

Pour vérifier que nodejs peut se connecter à notre nœud, ouvrons le fichier routes/index.js, ce fichier de routes a été créé par le générateur express, nous devons d'abord demander la bibliothèque ln-service, nous ajoutons donc à la première ligne

```
const lnservice = require('ln-service');
```

Ajoutons une nouvelle route qui nous donnera les informations de notre nœud.

```
router.get('/info', async function(req, res, next) {
try {
// nous authentifions avec lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// obtenons les informations du nœud
const info = await lnservice.getWalletInfo({ lnd });

    // affichons les informations au format json
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

Maintenant, allons à cette adresse http://localhost:3000/info

Si vous voyez un json avec les informations du nœud LND, félicitations !!! votre application peut maintenant interagir avec Lightning Network.
Création d'un modèle factice

Pour simuler une base de données, nous devons créer un modèle factice, cela nous permettra d'utiliser l'application sans avoir besoin d'installer et de configurer une base de données.

Tout d'abord, installons le package uuid

```
$ npm install uuid
```

Créez le répertoire models et à l'intérieur le fichier Post.js avec le contenu suivant:

```
const { v4: uuidv4 } = require('uuid');'
'class Post {constructor() {
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
`
```

## Nous préparons la vue

Nous avons besoin de boostrap pour améliorer l'aspect de notre html, nous modifions donc le fichier layout.pug situé dans le répertoire views pour qu'il ressemble à ceci :

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

## Créer un message

Pour créer un message, nous avons besoin d'un formulaire, dans le répertoire views nous créons un fichier appelé form.pug contenant :

```
.collapse#post-form
form
.h2 Escriba un artículo
.form-group
label(for="name") Nombre
input(id="name").form-control
.form-group
label(for="content") Contenido
textarea(id="content").form-control
button.btn.btn-primary#send-btn(type="button") Enviar
```

## Javascript dans le frontend

La façon la plus directe d'interagir avec l'utilisateur est d'utiliser le javascript dans le navigateur web, pour cela, dans le répertoire javascript nous créons un fichier main.js que nous appelons déjà depuis le layout.pug, dans lequel nous initialisons le projet, le contenu initial de main.js est le suivant :

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

Nous appuyons sur le bouton Send et si tout est OK, la console devrait afficher un message !hello, ce qui nous permet de modifier la méthode App.sendBtn() pour envoyer les informations à notre API.

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Error getting data!');
if (response.success) {'
'// nous imprimons les données provenant de l'API dans la consoleconsole.log(response.data);
}
};
```

Nous créons également la méthode App.makeRequest() et l'ajoutons à main.js

```
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

## Créons l'API

Pour cela, nous devons créer un nouveau fichier dans routes/api.js et écrire la méthode qui répond à la demande faite dans App.sendBtn().

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

Ce fichier doit être inclus dans app.js, pour cela, nous ajoutons ces lignes:

```
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Appuyons à nouveau sur le bouton d'envoi et il devrait nous répondre avec les mêmes données que nous avons écrites dans le formulaire.

## Créer la facture

La méthode qui s'exécute lorsque l'utilisateur crée un post doit générer une facture, puis créer un enregistrement dans la base de données en le liant à la facture et renvoyer la facture à l'utilisateur pour qu'il puisse la payer.

```
router.post('/post', async (req, res) => {
// nous nous authentifions avec lnd
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

Si après avoir appuyé sur envoyer, nous recevons un objet post en réponse, de ce type, tout s'est bien passé, maintenant nous devons afficher le texte pour que l'utilisateur puisse le payer.

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
```

## Nouvelle vue facture

Dans le répertoire views, nous devons créer un fichier appelé invoice.pug avec le contenu suivant :

```
.collapse#invoice-form
form
.h2 Payez cette facture
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Et nous l'incluons dans index.pug

```
extends layout

block content
h1 Application Lightning
include form.pug
include invoice.pug
```

## Modification de App.sendBtn()

Maintenant, nous modifions App.sendBtn() pour afficher les données obtenues :

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Erreur lors de la récupération des données !');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Réception du paiement

Nous devons savoir quand nous recevons le paiement, pour cela nous allons utiliser la méthode subscribeToInvoices() de lnservice, cette méthode nous permet d'exécuter du code lorsque l'état d'une facture est mis à jour, pour l'utiliser, nous ajoutons ces lignes dans app.js.

```
// nous faisons le require de lnservice et de notre tableau post
const lnservice = require('ln-service');
const post = require('./models/Post');

// nous nous authentifions avec lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// chaque fois qu'un changement se produit dans une facture, nous vérifions si la facture
// a été payée
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // change la facture en 'payée'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Facture payée !');
    });

} catch (e) {
console.log(e);
return e;
}
};
// nous commençons la souscription aux factures
subscribeInvoices();
```

Nous créons dans notre API une méthode HTTP GET pour que l'utilisateur puisse vérifier si un hash a été payé.

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

Ahora desde main.js creamos una función llamada App.waitPayment() que consulta a la api si el pago ha sido realizado.

App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("pago realizado");
  }
};

````

Maintenant nous avons un problème, la fonction App.waitPayment() n'est exécutée qu'une seule fois, l'utilisateur peut avoir payé et nous n'avons pas pu indiquer que son paiement a été reçu, pour cela nous utilisons une fonction javascript appelée setInterval() qui nous permet d'exécuter une fonction indéfiniment à chaque intervalle de temps que nous avons indiqué.

Modifiquemos las funciones App.waitPayment() y App.sendBtn() incluyendo setInterval() y clearInterva()

```

App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    clearInterval(App.interval);
    App.interval = null;
    $('#invoice-form').collapse('hide');
    $('#preimage').text(response.data.preimage);
    $('#success').collapse('show');
  }
};

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
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```

Et nous créons une vue pour indiquer que le paiement a été reçu avec succès, nous créons le fichier success.pug dans views avec le contenu suivant :

```
.collapse#success
  h2 Pago exitoso
  div Prueba de pago:
    #preimage

```

Nous l'incluons dans l'indice.

```pug.
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

Si, après avoir payé la facture, vous voyez le message "Paiement réussi" et la preuve de paiement, félicitations !!! vous avez terminé votre premier LApp.
