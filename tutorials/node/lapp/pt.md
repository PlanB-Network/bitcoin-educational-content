---
name: LAPP bitcoin
description: Tutorial para desarrollar tu primera LApp
---

# Tutorial para desarrollar tu primera LApp

Aprende a codificar tu primera aplicación lightning
Francisco Calderón publicado el
14 de junio de 2021

https://grunch.dev/guides/lapp/

Requisitos:

- NodeJs >= 8
- LND >= 9

NodeJs se puede descargar desde su web oficial

En lugar de descargar y configurar un nodo LND, utilizaremos la herramienta polar, que hará esta tarea por nosotros.

Para construir nuestra aplicación Lightning, utilizaremos las siguientes tecnologías:

- Express para nuestro servidor web
- Pug + plantillas bootstrap para nuestro frontend

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

---

## Sistema Operativo

Se recomienda usar Linux, si estás en Windows 10, puedes tener una consola Linux siguiendo estos pocos pasos.
Sentar las bases

Utiliza la herramienta generadora de apps, express, para crear rápidamente un esqueleto de app.

```
$ sudo npm install express-generator -g
```

Con la siguiente instrucción, creamos una aplicación Express llamada lnapp. La aplicación se creará en un directorio llamado lnapp en el directorio de trabajo actual y el mecanismo de vista se asignará a Pug.

```
$ express --view=pug lnapp
```

A continuación, ve al directorio e instala los paquetes necesarios para ejecutar el servidor web.

```
$ cd myapp
$ npm install
```

Ahora, arranca el servidor

```
$ npm start
```

Em seguida, vá para este endereço http://localhost:3000 no navegador para acessar o aplicativo.

O aplicativo gerado tem a seguinte estrutura de diretórios:

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

Baixe o Polar, instale-o e crie uma rede com 2 nós LND (Alice e Bob) e 1 bitcoind, uma vez que vejamos no aplicativo o gráfico com nossos nós, clique no botão Iniciar e aguarde alguns segundos até que o indicador de cada nó mude de cor para verde.

Para poder enviar pagamentos no Lightning, é necessário que os nós estejam interconectados por meio de canais, criar canais com o Polar é muito simples, só precisamos clicar com o mouse em uma das orelhas do nó Alice e arrastá-lo até uma das orelhas do nó Bob, imediatamente uma janela modal intitulada Abrir novo canal deve aparecer, deixamos os valores padrão e pressionamos o botão abrir canal, agora repetimos a ação, mas desta vez de Bob para Alice, dessa forma os dois nós podem enviar e receber dinheiro.

## Nodemon

Para não precisar reiniciar o nodejs sempre que fizermos uma alteração no código, instalaremos o nodemon

```
$ npm install nodemon -D
```

'Devemos criar uma entrada na seção scripts do arquivo package.json, adicione esta linha "dev": "nodemon ./bin/www", a seção scripts deve ficar assim:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Vamos para o console onde o npm start está sendo executado, pressionamos ctrl + c e iniciamos o nodejs novamente, mas desta vez usando o nodemon

```
$ npm run dev
```

## Conectando-se ao LND

Para nos conectarmos a um nó Lightning a partir do nodejs, usaremos a biblioteca ln-service, também instalaremos o dotenv para gerenciar as variáveis de ambiente.

```
$ npm install ln-service dotenv
```

Em nosso diretório lnapp, criamos um arquivo chamado .env, ele deve conter essas variáveis:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Voltamos para o Polar, selecionamos o Bob, o nó ao qual queremos nos conectar, vamos para a guia "Conectar", copiamos o conteúdo de Host GRPC e o colocamos na variável LND_GRPC_HOST, na parte inferior da guia conectar selecionamos base64 e copiamos o conteúdo de TLS Cert e o colocamos na variável LND_CERT_BASE64 e finalizamos fazendo o mesmo com o admin macaroon em LND_MACAROON_BASE64.

Agora adicionamos esta linha ao arquivo app.js localizado na raiz do diretório de trabalho, devemos copiá-lo na primeira linha do arquivo.

```
require('dotenv').config();
```

Para verificar se o nodejs pode se conectar ao nosso nó, abrimos o arquivo routes/index.js, este arquivo de rotas foi criado pelo gerador express, primeiro requeremos a biblioteca ln-service, então adicionamos na primeira linha

```
const lnservice = require('ln-service');
```

Adicionamos uma nova rota que nos fornecerá as informações do nosso nó.

```
router.get('/info', async function(req, res, next) {
try {
// nos autenticamos com lnd
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

Agora vá para este endereço http://localhost:3000/info

Se você vir um json com as informações do nó LND, parabéns!!! seu aplicativo já pode interagir com a Lightning Network.
Criando um modelo falso

Para simular um banco de dados, precisamos criar um modelo falso, isso nos permitirá usar o aplicativo sem precisar instalar e configurar um banco de dados.

Primeiro, instale o pacote uuid

```
$ npm install uuid
```

Crie o diretório models e dentro dele o arquivo Post.js com o seguinte conteúdo:

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

## Preparamos a vista

Precisamos do bootstrap para que nosso html fique melhor, para isso modificamos o arquivo layout.pug localizado no diretório views para que fique assim:

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

## Criando um Post

Para criar um post precisamos de um formulário, dentro do diretório views criamos um arquivo chamado form.pug que contenha:

```
.collapse#post-form
  form
    h2 Escreva um artigo
    .form-group
      label(for="name") Nome
      input(id="name").form-control
    .form-group
      label(for="content") Conteúdo
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Enviar
```

## Javascript no frontend

A maneira mais direta de interagir com o usuário é usando javascript no navegador da web, para isso, no diretório javascript criamos um arquivo main.js que já estamos chamando do layout.pug, no qual inicializamos o projeto, o conteúdo inicial de main.js é o seguinte:

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

Pressionamos o botão Enviar e se tudo estiver correto, ele deve exibir a mensagem !hola no console, com isso já podemos modificar o método App.sendBtn() para enviar as informações para nossa API.

```
App.sendBtn = async () => {
  const name = $('#name').val();
  const content = $('#content').val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error('Erro ao obter dados!');
  if (response.success) {
    // Fazer algo com a resposta
  }
};
```

```javascript
// imprimimos en la consola la data que viene de la APIconsole.log(response.data);
}
};
```

Também criamos o método App.makeRequest() e também o adicionamos ao main.js

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

## Criamos a API

Para isso, devemos criar um novo arquivo em routes/api.js e dentro dele escrevemos o método que responde à solicitação feita dentro de App.sendBtn().

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

Este arquivo deve ser incluído em app.js, para isso adicionamos estas linhas:

```javascript
const apiRouter = require("./routes/api");
app.use("/api", apiRouter);
```

Vamos pressionar o botão enviar novamente e ele deve responder com os mesmos dados que escrevemos no formulário.

## Criar a fatura

O método que é executado quando um usuário cria um post deve gerar uma fatura, em seguida, criar um registro no banco de dados vinculando-o à fatura e retornar a fatura para que o usuário possa pagá-la.

```javascript
router.post("/post", async (req, res) => {
  // nos autenticamos com lnd
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

Se depois de pressionar enviar recebermos um objeto post como resposta, desse tipo, tudo correu bem, agora devemos mostrar o texto para que o usuário possa pagá-lo.

```json
{
  "success": true,
  "data": {
    "id": "0fb1544a-d7f9-487d-961a-d0004ecc515c",
    "time": "2020-09-02T21:29:53.747Z",
    "name": "epale",
    "content": "conteúdo bla bla",
    "paid": false,
    "hash": "0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
    "preimage": null
  }
}
```

## Nova vista de fatura

No diretório views, devemos criar um arquivo chamado invoice.pug com o seguinte conteúdo:

```
.collapse#invoice-form
form
.h2 Pague esta fatura
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

E incluímos isso em index.pug

```
extends layout

block content
h1 Aplicativo Lightning
include form.pug
include invoice.pug
```

## Modificando App.sendBtn()

Agora modificamos App.sendBtn() para exibir os dados obtidos:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Erro ao obter dados!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Recebendo o pagamento

Precisamos saber quando recebemos o pagamento, para isso vamos usar o método subscribeToInvoices() do lnservice, este método nos permite executar código quando o estado de uma fatura é atualizado, para usá-lo, adicionamos estas linhas no app.js.

```
// fazemos o require do lnservice e do nosso modelo de postagem
const lnservice = require('ln-service');
const post = require('./models/Post');

// autenticamos com o lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// sempre que houver uma alteração em uma fatura, verificamos se a fatura
// foi paga
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // altera a fatura para 'paga'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Fatura paga!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// iniciamos a assinatura de faturas
subscribeInvoices();
```

Criamos em nossa API um método HTTP GET para que o usuário possa verificar se um hash foi pago.

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

Agora temos um problema, a função App.waitPayment() é executada apenas uma vez, o utilizador pode ter pago e não conseguimos indicar que o seu pagamento foi recebido, para isso utilizamos uma função javascript chamada setInterval() que nos permite executar uma função indefinidamente a cada intervalo de tempo que tenhamos indicado.

Vamos modificar as funções App.waitPayment() e App.sendBtn() para incluir setInterval() e clearInterva().

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

E criamos uma vista para indicar que o pagamento foi recebido com êxito, criamos o ficheiro success.pug nas vistas com o seguinte conteúdo:

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

Se, depois de pagares a fatura, vires a mensagem Pagamento bem sucedido e o comprovativo de pagamento, parabéns!!! concluíste a tua primeira LApp.

> https://grunch.dev/guides/lapp/ -
> Francisco Calderón published on
> June 14, 2021
