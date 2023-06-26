Tutorial para desarrollar tu primera LApp

Aprende a codear tu primera lightning app
Francisco Calderón published on
June 14, 2021

https://grunch.dev/guides/lapp/

Requisitos:

- NodeJs >= 8
- LND >= 9

NodeJs puede ser descargado en su sitio oficial

En lugar de descargar y configurar un nodo LND, vamos a utilizar la herramienta polar, la cual realizará esta tarea por nosotros.

Para construir nuestra Lightning app, estaremos utilizando las siguientes tecnologías:

- Express para nuestro webserver
- Pug templates + bootstrap para nuestro frontend

## Sistema operativo

Se recomienda utilizar Linux, si estas en windows 10 puedes tener una consola linux siguiendo estos pocos pasos.
Preparando la base

Utilice la herramienta de generador de aplicaciones, express, para crear rápidamente un esqueleto de aplicación.

```
$ sudo npm install express-generator -g
```

Con la siguiente instrucción creamos una aplicación Express denominada lnapp. La aplicación será creada en un directorio llamado lnapp en el directorio de trabajo actual y el motor de vistas será asignado a Pug.

```
$ express --view=pug lnapp
```

Luego entramos al directorio e instalamos los paquetes necesarios para que el web server corra.

```
$ cd myapp
$ npm install
```

Ahora simplemente corremos el server

```
$ npm start
```

A continuación, vamos esta dirección http://localhost:3000 en el navegador para acceder a la aplicación.

La aplicación generada tiene la siguiente estructura de directorios:

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

Descargamos Polar, lo instalamos y creamos una red con 2 nodos LND (Alice y Bob) y 1 bitcoind, una vez veamos en la app el gráfico donde aparecen nuestros nodos hacemos clic en el botón Comienzo y espera unos segundos hasta que el indicador de cada nodo cambie de color a verde.

Para poder enviar pagos en Lightning es necesario que los nodos estén interconectados por medio de canales, crear canales con Polar es muy sencillo, solo necesitamos hacer clic con el mouse en una de las orejas del nodo Alice y arrastrarlo hasta una de las orejas del nodo Bob, inmediatamente te debe aparecer una ventana modal titulada Abrir nuevo canal, dejamos los valores por defecto y presionamos el botón de abrir canal, ahora repetimos la acción pero esta vez desde Bob hacia Alice, de esta manera los dos nodos pueden enviar y recibir dinero.

## Nodemon

Para no tener que reiniciar nodejs cada vez que realicemos un cambio en el código instalaremos nodemon

```
$ npm install nodemon -D
```

Debemos crear una entrada en la sección scripts del archivo package.json, agregue esta línea "dev": "nodemon ./bin/www", la sección scripts debería quedar así:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Vamos a la cónsola donde está corriendo npm start, hacemos ctrl + c y volvemos a iniciar nodejs pero esta vez utilizando nodemon

```
$ npm run dev
```

## Conectándonos a LND

Para poder conectarnos a un nodo Lightning desde nodejs, utilizaremos la librería ln-service, también instalaremos dotenv para administrar las variables de entorno.

```
$ npm install ln-service dotenv
```

En nuestro directorio lnapp creamos un archivo llamado .env, debe contener estas variables:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Volvemos a Polar, seleccionamos a Bob, el nodo al que nos queremos conectar, vamos a la pestaña "Conectar", copiamos el contenido de Host GRPC y lo colocamos en la variable LND_GRPC_HOST, en la parte de abajo de la pestaña conectar seleccionamos base64 y copiamos el contenido de TLS Cert y lo colocamos en la variable LND_CERT_BASE64 y finalizamos haciendo lo mismo con el admin macaroon en LND_MACAROON_BASE64.

Ahora agregamos esta línea al archivo app.js ubicado en la raíz del directorio de trabajo, debemos copiarlo en la primera línea del archivo.

```
require('dotenv').config();
```

Para verificar que nodejs puede conectarse con nuestro nodo abrimos el archivo routes/index.js, este archivo de rutas fue creado por el generador express, primero requerimos la libreria ln-service, así que agregamos en la primera línea

```
const lnservice = require('ln-service');
```

Añadimos una nueva ruta que nos dará la información de nuestro nodo.

```
router.get('/info', async function(req, res, next) {
try {
// nos autenticamos con lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// obtenemos información del nodo
const info = await lnservice.getWalletInfo({ lnd });

    // mostramos la info en formato json
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

Ahora vamos esta dirección http://localhost:3000/info

Si ves un json con la información del nodo LND, felicidades!!! tu app ya puede interactual con Lightning Network.
Creando un modelo falso

Para simular una base de datos necesitamos crear un modelo falso, esto nos permitirá utilizar la app sin necesidad de instalar y configurar una base de datos.

Primero instalamos el paquete uuid

```
$ npm install uuid
```

Crea el directorio models y dentro el archivo Post.js con el siguiente contenido:

```
const { v4: uuidv4 } = require('uuid');

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

## Preparamos la vista

Necesitamos boostrap para que nuestro html se vea mejor, para ello modificamos el archivo layout.pug ubicado en el directorio views para que quede así:

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

## Creando un Post

Para crear un post necesitamos un formulario, dentro del directiorio views creamos un archivo llamado form.pug que contenga:

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

Presionamos el botón Enviar y si todo está bien debe mostrarnos en la cónsola un mensaje !hola, con esto ya podemos modificar el método App.sendBtn() para que envíe la información a nuestra API.

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
// imprimimos en la consola la data que viene de la API
console.log(response.data);
}
};
```

Tambien creamos el método App.makeRequest() y también lo agregamos a main.js

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

## Creamos la API

Para esto debemos crear un nuevo archivo en routes/api.js con y dentro escribimos el método que responde a la solicitud que hacemos dentro de App.sendBtn().

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

Este archivo debe ser incluido en app.js, para esto agregamos estas líneas:

```
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Volvamos a presionar el botón enviar y nos debe responder con la misma data que escribimos en el formulario.

## Crear la invoice

El método que se ejecuta cuando un usuario crea un post, debe generar una invoice, luego crear un registro en la base de datos vinculándolo a la invoice y retornarle al usuario la invoice para que pueda pagarla.

```
router.post('/post', async (req, res) => {
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

Si luego de presionar enviar recibimos un objeto post como respuesta, de este tipo, todo ha salido correctamente, ahora debemos mostrar el texto para que el usuario pueda pagarlo.

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
"preimage":null,
"request":"lnbcrt10u1p04qrk3pp5pc785y23mru0yq4uwfjdhql92nysp8um6vkqljcyzfmjkvgt2g8qdqgv4cxzmr9cqzpgxq92fjuqsp534n0k3up43xlrnwmh97kk9mtl89n7yvkrznhrmqd47yll8eux35s9qy9qsqc2nlv8nd5k9tam8m9tzrqr05n3dzllsqxzsxs62j2zl7k49up834eazq4lhpfkjysmgevu5memgj7g7cq0fujsqvf49et88sl7v8zlcq4mgxx9"
}
}
```

## Nueva vista invoice

En el directorio views debemos crear un archivo llamado invoice.pug con el siguiente contenido:

```
.collapse#invoice-form
form
.h2 Pague esta factura
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Y la incluimos en index.pug

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Modificando App.sendBtn()

Ahora modificamos App.sendBtn() para que muestre la data obtenida:

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

## Recibiendo el pago

Necesitamos saber cuándo recibimos el pago, para esto vamos a utilizar el método subscribeToInvoices() de lnservice, este método nos permite ejecutar código cuando el estado de una invoice ha sido actualizado, para utilizarlo agregamos estas líneas en app.js.

```
// hacemos el require de lnservice y de nuestra tabla post
const lnservice = require('ln-service');
const post = require('./models/Post');

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
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // cambia la invoice a 'pagada'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Invoice paid!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// iniciamos la subscripcion a invoices
subscribeInvoices();
```

Creamos en nuestra API un método HTTP GET para que el usuario pueda consultar si un hash ha sido pagado.

```
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

Y creamos una vista para indicar que el pago ha sido recibido exitosamente, creamos el archivo success.pug en views con el siguiente contenido:

```
.collapse#success
.h2 Pago exitoso
.div Prueba de pago:
#preimage
```

Lo incluimos en index.pug.

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
include success.pug
```

Si luego de pagar la invoice puedes ver el mensaje de Pago exitoso y la prueba de pago felicidades!!! lo lograste, has terminado tu primera LApp.

https://grunch.dev/guides/lapp/ -
Francisco Calderón published on
June 14, 2021
