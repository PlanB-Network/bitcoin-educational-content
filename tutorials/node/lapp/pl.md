---
name: LAPP Bitcoin
description: Samouczek tworzenia pierwszej aplikacji LApp
---

Naucz się kodować swoją pierwszą aplikację Lightning


Wymagania:



- NodeJs >= 8
- LND >= 9


NodeJs można pobrać z jego oficjalnej strony internetowej


Zamiast pobierać i konfigurować węzeł LND, użyjemy narzędzia polar, które wykona to zadanie za nas.


Aby zbudować naszą aplikację Lightning, będziemy korzystać z następujących technologii:



- Express dla naszego serwera internetowego
- Szablony Pug + bootstrap dla naszego frontendu


## System operacyjny


Zaleca się korzystanie z systemu Linux, jeśli korzystasz z systemu Windows 10, możesz mieć konsolę Linux, wykonując te kilka kroków.

Przygotowanie bazy


Użyj narzędzia generatora aplikacji express, aby szybko utworzyć szkielet aplikacji.


```
$ sudo npm install express-generator -g
```


Za pomocą poniższej instrukcji tworzymy aplikację Express o nazwie lnapp. Aplikacja zostanie utworzona w katalogu o nazwie lnapp w bieżącym katalogu roboczym, a silnik widoku zostanie przypisany do Pug.


```
$ express --view=pug lnapp
```


Następnie wchodzimy do katalogu i instalujemy niezbędne pakiety do uruchomienia serwera WWW.


```
$ cd myapp
$ npm install
```


Teraz wystarczy uruchomić serwer


```
$ npm start
```


Następnie przejdź do Address http://localhost:3000 w przeglądarce, aby uzyskać dostęp do aplikacji.


Wygenerowana aplikacja ma następującą strukturę katalogów:


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


Pobieramy aplikację Polar, instalujemy ją i tworzymy sieć z 2 węzłami LND (Alice i Bob) i 1 bitcoind. Gdy zobaczymy wykres w aplikacji pokazujący nasze węzły, kliknij przycisk Start i poczekaj kilka sekund, aż wskaźnik każdego węzła zmieni kolor na Green.


Aby wysyłać płatności na Lightning, konieczne jest połączenie węzłów za pomocą kanałów. Tworzenie kanałów za pomocą Polar jest bardzo proste, wystarczy kliknąć myszką na jedno z uszu węzła Alice i przeciągnąć je na jedno z uszu węzła Bob. Natychmiast powinno pojawić się okno modalne zatytułowane Otwórz nowy kanał, pozostawiamy wartości domyślne i naciskamy przycisk Otwórz kanał. Teraz powtarzamy czynność, ale tym razem od Boba do Alicji, w ten sposób oba węzły mogą wysyłać i odbierać pieniądze.


## Nodemon


Aby uniknąć konieczności ponownego uruchamiania nodejs za każdym razem, gdy wprowadzamy zmiany w kodzie, zainstalujemy nodemon


```
$ npm install nodemon -D
```


Musimy utworzyć wpis w sekcji skryptów pliku package.json, dodać tę linię "dev": "nodemon ./bin/www", sekcja skryptów powinna wyglądać następująco:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Przejdź do konsoli, w której uruchomiony jest npm start, naciśnij ctrl + c i ponownie uruchom nodejs, ale tym razem używając nodemon


```
$ npm run dev
```


## Podłączanie do LND


Aby połączyć się z węzłem Lightning z nodejs, użyjemy biblioteki LN-service, zainstalujemy również dotenv do zarządzania zmiennymi środowiskowymi.


```
$ npm install ln-service dotenv
```


W naszym katalogu lnapp utwórz plik o nazwie .env, powinien on zawierać te zmienne:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Wracamy do Polara, wybieramy Bob, węzeł z którym chcemy się połączyć, przechodzimy do zakładki "Connect", kopiujemy zawartość GRPC Host i umieszczamy ją w zmiennej LND_GRPC_HOST, w dolnej części zakładki connect wybieramy base64 i kopiujemy zawartość TLS Cert i umieszczamy ją w zmiennej LND_CERT_BASE64, to samo robimy z admin macaroon w LND_MACAROON_BASE64.


Teraz dodaj tę linię do pliku app.js znajdującego się w katalogu głównym katalogu roboczego, musimy skopiować ją w pierwszej linii pliku.


```
require('dotenv').config();
```


Aby sprawdzić, czy nodejs może połączyć się z naszym węzłem, otwórz plik routes/index.js, ten plik tras został utworzony przez generator ekspresowy, najpierw wymagamy biblioteki LN-service, więc dodajemy ją w pierwszej linii


```
const lnservice = require('ln-service');
```


Dodajemy nową trasę, która dostarczy nam informacji o naszym węźle.


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


Teraz przejdź do Address http://localhost:3000/info


Jeśli zobaczysz json z informacjami o węźle LND, gratulacje!!! Twoja aplikacja może teraz wchodzić w interakcje z Lightning Network.

Tworzenie fałszywego modelu


Aby symulować bazę danych, musimy stworzyć fałszywy model, który pozwoli nam korzystać z aplikacji bez instalowania i konfigurowania bazy danych.


Najpierw zainstaluj pakiet uuid


```
$ npm install uuid
```


Utwórz katalog models i utwórz w nim plik Post.js o następującej zawartości:


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


## Przygotowanie widoku


Potrzebujemy bootstrapa, aby nasz html wyglądał lepiej, więc zmodyfikujemy plik layout.pug znajdujący się w katalogu views, aby wyglądał tak:


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


## Tworzenie postu


Aby utworzyć post, potrzebujemy formularza. Wewnątrz katalogu views utwórz plik o nazwie form.pug z następującą zawartością:


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


## Javascript w interfejsie użytkownika


Najbardziej bezpośrednim sposobem interakcji z użytkownikiem jest użycie javascript w przeglądarce internetowej. W tym celu utwórz plik o nazwie main.js w katalogu javascript, który już wywołujemy z layout.pug. W tym pliku należy zainicjować projekt. Początkowa zawartość main.js jest następująca:


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


Kliknij przycisk "Enviar" i jeśli wszystko jest w porządku, w konsoli powinien pojawić się komunikat "!hola". Teraz możemy zmodyfikować metodę App.sendBtn(), aby wysłać informacje do naszego API.


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


Tworzymy również metodę App.makeRequest() i dodajemy ją do main.js


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


## Tworzenie interfejsu API


Aby to zrobić, musimy utworzyć nowy plik w routes/api.js i napisać metodę, która odpowiada na żądanie wykonane w App.sendBtn().


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


Ten plik musi być dołączony do app.js, więc dodajemy te linie:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Naciśnijmy ponownie przycisk wysyłania, a powinien on odpowiedzieć tymi samymi danymi, które wprowadziliśmy w formularzu.


## Utwórz Invoice


Metoda, która jest wykonywana, gdy użytkownik tworzy post, powinna generate i Invoice, a następnie utworzyć rekord w bazie danych łączący go z Invoice i zwrócić Invoice użytkownikowi, aby mógł go zapłacić.


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


Jeśli po naciśnięciu przycisku wyślij otrzymamy obiekt post jako odpowiedź, wszystko poszło poprawnie. Teraz musimy wyświetlić tekst, aby użytkownik mógł zapłacić.


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


## Nowy widok Invoice


W katalogu widoków musimy utworzyć plik o nazwie Invoice.pug z następującą zawartością:


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


I dołącz go do index.pug


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## Modyfikacja App.sendBtn()


Teraz modyfikujemy App.sendBtn(), aby wyświetlić uzyskane dane:


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


## Otrzymywanie płatności


Musimy wiedzieć, kiedy otrzymamy płatność, w tym celu użyjemy metody subscribeToInvoices() z lnservice, ta metoda pozwala nam wykonać kod, gdy status Invoice został zaktualizowany, aby z niej skorzystać dodajemy te linie w app.js.


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


Utwórz metodę HTTP GET w naszym API, aby użytkownik mógł sprawdzić, czy Hash został opłacony.


````

router.get('/post/:Hash', (req, res) => {

const { Hash } = req.params

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

```

App.waitPayment = async (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`,

});

if (response.success && response.data.paid) {

console.log("Płatność dokonana");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

const response = await App.makeRequest({

api: `post/${Hash}`,

});

if (response.success && response.data.paid) {

clearInterval(App.interval);

App.interval = null;

$("#Invoice-form").collapse("hide");

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

if (!response) console.error("Błąd pobierania danych!");

if (response.success) {

$("#post-form").collapse("hide");

$("#Invoice-form").collapse("show");

$("#Invoice").val(response.data.request);

App.interval = setInterval(App.waitPayment, 1000, response.data.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#success

h2 Płatność powiodła się

div Dowód wpłaty:

#preimage

```

We include it in index.pug.

```

rozszerza układ


zawartość bloku

h1 Aplikacja Lightning

include form.pug

include Invoice.pug

include success.pug

```