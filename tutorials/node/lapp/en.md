---
name: LAPP bitcoin
description: Tutorial to develop your first LApp
---

# Tutorial to develop your first LApp

Learn to code your first lightning app

Requirements:

- NodeJs >= 8
- LND >= 9

NodeJs can be downloaded from its official website

Instead of downloading and setting up an LND node, we will use the polar tool, which will perform this task for us.

To build our Lightning app, we will be using the following technologies:

- Express for our webserver
- Pug templates + bootstrap for our frontend

## Operating system

It is recommended to use Linux, if you are on Windows 10 you can have a Linux console by following these few steps.
Preparing the base

Use the application generator tool, express, to quickly create an application skeleton.

```
$ sudo npm install express-generator -g
```

With the following instruction, we create an Express application called lnapp. The application will be created in a directory called lnapp in the current working directory, and the view engine will be assigned to Pug.

```
$ express --view=pug lnapp
```

Then we enter the directory and install the necessary packages for the web server to run.

```
$ cd myapp
$ npm install
```

Now we simply run the server

```
$ npm start
```

Next, go to this address http://localhost:3000 in the browser to access the application.

The generated application has the following directory structure:

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

Download Polar, install it, and create a network with 2 LND nodes (Alice and Bob) and 1 bitcoind. Once we see the graph in the app showing our nodes, click on the Start button and wait a few seconds until the indicator of each node changes color to green.

In order to send payments on Lightning, it is necessary for the nodes to be interconnected through channels. Creating channels with Polar is very simple, we just need to click with the mouse on one of the ears of the Alice node and drag it to one of the ears of the Bob node. Immediately, a modal window titled Open new channel should appear, we leave the default values and press the open channel button. Now we repeat the action but this time from Bob to Alice, this way both nodes can send and receive money.

## Nodemon

To avoid having to restart nodejs every time we make a change in the code, we will install nodemon

```
$ npm install nodemon -D
```

We must create an entry in the scripts section of the package.json file, add this line "dev": "nodemon ./bin/www", the scripts section should look like this:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Go to the console where npm start is running, press ctrl + c and start nodejs again but this time using nodemon

```
$ npm run dev
```

## Connecting to LND

To connect to a Lightning node from nodejs, we will use the ln-service library, we will also install dotenv to manage environment variables.

```
$ npm install ln-service dotenv
```

In our lnapp directory, create a file called .env, it should contain these variables:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Go back to Polar, select Bob, the node we want to connect to, go to the "Connect" tab, copy the content of GRPC Host and place it in the LND_GRPC_HOST variable, in the bottom part of the connect tab select base64 and copy the content of TLS Cert and place it in the LND_CERT_BASE64 variable, and do the same with the admin macaroon in LND_MACAROON_BASE64.

Now add this line to the app.js file located in the root of the working directory, we must copy it on the first line of the file.

```
require('dotenv').config();
```

To verify that nodejs can connect to our node, open the routes/index.js file, this routes file was created by the express generator, first we require the ln-service library, so we add it on the first line

```
const lnservice = require('ln-service');
```

We add a new route that will give us information about our node.

```
router.get('/info', async function(req, res, next) {
try {
// authenticate with lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// get node information
const info = await lnservice.getWalletInfo({ lnd });

    // display info in json format
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

Now go to this address http://localhost:3000/info

If you see a json with the information of the LND node, congratulations!!! your app can now interact with the Lightning Network.
Creating a fake model

To simulate a database, we need to create a fake model, this will allow us to use the app without installing and configuring a database.

First, install the uuid package

```
$ npm install uuid
```

Create the models directory and inside it, create the Post.js file with the following content:

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

## Prepare the view

We need bootstrap to make our html look better, so we modify the layout.pug file located in the views directory to look like this:

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

## Creating a Post

To create a post, we need a form. Inside the views directory, create a file called form.pug with the following content:

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

## Javascript in the frontend

The most direct way we have to interact with the user is by using javascript in the web browser. For this, create a file called main.js in the javascript directory, which we are already calling from layout.pug. In this file, initialize the project. The initial content of main.js is as follows:

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

Click the "Enviar" button and if everything is fine, it should show a message "!hola" in the console. Now we can modify the App.sendBtn() method to send the information to our API.

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
    // Do something with the response
  }
};
```

```markdown
// Print the data that comes from the API to the console
console.log(response.data);
}
};
```

We also create the method App.makeRequest() and add it to main.js

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

## Create the API

To do this, we need to create a new file in routes/api.js and write the method that responds to the request made within App.sendBtn().

```markdown
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

This file must be included in app.js, so we add these lines:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Let's press the send button again and it should respond with the same data we entered in the form.

## Create the invoice

The method that is executed when a user creates a post should generate an invoice, then create a record in the database linking it to the invoice, and return the invoice to the user so they can pay it.

```markdown
router.post('/post', async (req, res) => {
// Authenticate with lnd
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

If we receive a post object as a response after pressing send, like this, everything has gone correctly. Now we need to display the text so that the user can pay it.

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

## New invoice view

In the views directory, we need to create a file called invoice.pug with the following content:

```
.collapse#invoice-form
form
.h2 Pay this invoice
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

And include it in index.pug

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## Modifying App.sendBtn()

Now we modify App.sendBtn() to display the obtained data:

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

## Receiving the payment

We need to know when we receive the payment, for this we will use the subscribeToInvoices() method from lnservice, this method allows us to execute code when the status of an invoice has been updated, to use it we add these lines in app.js.

```
// require lnservice and our post table
const lnservice = require('ln-service');
const post = require('./models/Post');

// authenticate with lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// check if the invoice has been paid every time an invoice is updated
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // mark the invoice as 'paid'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Invoice paid!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// start the invoice subscription
subscribeInvoices();
```

Create an HTTP GET method in our API for the user to check if a hash has been paid.

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

Now, from main.js, we create a function called App.waitPayment() that queries the API if the payment has been made.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Payment made");
  }
};
```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

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
  if (!response) console.error("Error getting data!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```pug
.collapse#success
  h2 Payment successful
  div Payment proof:
    #preimage
```

We include it in index.pug.

```pug
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

If after paying the invoice you can see the message "Payment successful" and the payment proof, congratulations!!! you did it, you have finished your first LApp.
