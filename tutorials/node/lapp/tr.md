---
name: Lightning App
description: İlk Lightning Uygulamanızı (LAPP) geliştirmek için eğitim
---

![cover](assets/cover.webp)

## İlk lightning uygulamanızı kodlamayı öğrenin


Gereksinimler:



- NodeJs >= 8
- LND >= 9


NodeJs resmi web sitesinden indirilebilir


Bir LND düğümü indirip kurmak yerine, bu görevi bizim için gerçekleştirecek olan polar aracını kullanacağız.


Lightning uygulamamızı oluşturmak için aşağıdaki teknolojileri kullanacağız:



- Web sunucumuz için Express
- Ön yüzümüz için pug şablonları + bootstrap


https://planb.network/courses/bbf08a64-84ca-11f0-9d7a-c3c481a45799

## İşletim sistemi


Linux kullanmanız önerilir, Windows 10 kullanıyorsanız aşağıdaki birkaç adımı izleyerek bir Linux konsoluna sahip olabilirsiniz.

Tabanın hazırlanması


Hızlı bir şekilde uygulama iskeleti oluşturmak için uygulama oluşturma aracı express'i kullanın.


```
$ sudo npm install express-generator -g
```


Aşağıdaki yönerge ile lnapp adında bir Express uygulaması oluşturuyoruz. Uygulama, geçerli çalışma dizininde lnapp adlı bir dizinde oluşturulacak ve görünüm motoru Pug'a atanacaktır.


```
$ express --view=pug lnapp
```


Daha sonra dizine girip web sunucusunun çalışması için gerekli paketleri kuruyoruz.


```
$ cd myapp
$ npm install
```


Şimdi basitçe sunucuyu çalıştırıyoruz


```
$ npm start
```


Ardından, uygulamaya erişmek için tarayıcıda bu Address http://localhost:3000 adresine gidin.


Oluşturulan uygulama aşağıdaki dizin yapısına sahiptir:


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


Polar'ı indirin, kurun ve 2 LND düğümü (Alice ve Bob) ve 1 bitcoind ile bir ağ oluşturun. Uygulamada düğümlerimizi gösteren grafiği gördüğümüzde, Başlat düğmesine tıklayın ve her düğümün göstergesi Green olarak renk değiştirene kadar birkaç saniye bekleyin.


Lightning'de ödeme göndermek için düğümlerin kanallar aracılığıyla birbirine bağlanması gerekir. Polar ile kanal oluşturmak çok basittir, sadece Alice düğümünün kulaklarından birine fare ile tıklamamız ve Bob düğümünün kulaklarından birine sürüklememiz gerekir. Hemen, Yeni kanal aç başlıklı modal bir pencere görünmelidir, varsayılan değerleri bırakıyoruz ve kanal aç düğmesine basıyoruz. Şimdi eylemi tekrarlıyoruz, ancak bu sefer Bob'dan Alice'a, bu şekilde her iki düğüm de para gönderip alabilir.


## Nodemon


Kodda her değişiklik yaptığımızda nodejs'i yeniden başlatmak zorunda kalmamak için nodemon'u kuracağız


```
$ npm install nodemon -D
```


Package.json dosyasının scripts bölümünde bir giriş oluşturmalıyız, bu satırı "dev" ekleyin: "nodemon ./bin/www", scripts bölümü şöyle görünmelidir:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


Npm start'ın çalıştığı konsola gidin, ctrl + c tuşlarına basın ve nodejs'i tekrar başlatın, ancak bu sefer nodemon'u kullanın


```
$ npm run dev
```


## LND'e Bağlanma


Nodejs'ten bir Lightning düğümüne bağlanmak için LN-service kütüphanesini kullanacağız, ayrıca ortam değişkenlerini yönetmek için dotenv'i kuracağız.


```
$ npm install ln-service dotenv
```


Lnapp dizinimizde .env adında bir dosya oluşturun, bu değişkenleri içermelidir:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


Polar'a geri dönün, bağlanmak istediğimiz düğüm olan Bob'ü seçin, "Bağlan" sekmesine gidin, GRPC Host'un içeriğini kopyalayın ve LND_GRPC_HOST değişkenine yerleştirin, bağlan sekmesinin alt kısmında base64'ü seçin ve TLS Cert'in içeriğini kopyalayın ve LND_CERT_BASE64 değişkenine yerleştirin ve aynı şeyi LND_MACAROON_BASE64'teki yönetici makaronuyla yapın.


Şimdi bu satırı çalışma dizininin kök dizininde bulunan app.js dosyasına ekleyin, dosyanın ilk satırına kopyalamalıyız.


```
require('dotenv').config();
```


Nodejs'in node'umuza bağlanabildiğini doğrulamak için routes/index.js dosyasını açın, bu routes dosyası express generator tarafından oluşturuldu, önce LN-service kütüphanesine ihtiyacımız var, bu yüzden ilk satıra ekliyoruz


```
const lnservice = require('ln-service');
```


Bize düğümümüz hakkında bilgi verecek yeni bir rota ekliyoruz.


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


Şimdi bu Address'e gidin http://localhost:3000/info


LND düğümünün bilgilerini içeren bir json görürseniz, tebrikler!!! uygulamanız artık Lightning Network ile etkileşime girebilir.

Sahte bir model oluşturma


Bir veritabanını simüle etmek için sahte bir model oluşturmamız gerekir, bu, bir veritabanı kurmadan ve yapılandırmadan uygulamayı kullanmamıza izin verecektir.


İlk olarak uuid paketini yükleyin


```
$ npm install uuid
```


Models dizinini oluşturun ve içinde aşağıdaki içeriğe sahip Post.js dosyasını oluşturun:


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


## Görünümü hazırlayın


Html'imizin daha iyi görünmesi için bootstrap'e ihtiyacımız var, bu yüzden views dizininde bulunan layout.pug dosyasını aşağıdaki gibi görünecek şekilde değiştiriyoruz:


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


## Gönderi Oluşturma


Bir gönderi oluşturmak için bir forma ihtiyacımız var. Görünümler dizini içinde, aşağıdaki içeriğe sahip form.pug adlı bir dosya oluşturun:


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


## Ön uçta Javascript


Kullanıcı ile etkileşime geçmenin en doğrudan yolu web tarayıcısında javascript kullanmaktır. Bunun için javascript dizininde main.js adında, zaten layout.pug'dan çağırdığımız bir dosya oluşturun. Bu dosyada projeyi başlatın. Main.js'nin başlangıç içeriği aşağıdaki gibidir:


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


"Enviar" düğmesine tıklayın ve her şey yolundaysa konsolda bir "!hola" mesajı göstermelidir. Şimdi bilgileri API'mize göndermek için App.sendBtn() yöntemini değiştirebiliriz.


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


Ayrıca App.makeRequest() metodunu oluşturuyoruz ve main.js dosyasına ekliyoruz


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


## API oluşturma


Bunu yapmak için routes/api.js içinde yeni bir dosya oluşturmamız ve App.sendBtn() içinde yapılan isteğe yanıt veren yöntemi yazmamız gerekiyor.


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


Bu dosya app.js dosyasına dahil edilmelidir, bu yüzden bu satırları ekliyoruz:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


Gönder düğmesine tekrar basalım ve forma girdiğimiz aynı verilerle yanıt vermelidir.


## Invoice'i oluşturun


Bir kullanıcı bir gönderi oluşturduğunda çalıştırılan yöntem, generate bir Invoice oluşturmalı, ardından veritabanında Invoice'ye bağlayan bir kayıt oluşturmalı ve Invoice'yi kullanıcıya iade etmelidir, böylece kullanıcı bunu ödeyebilir.


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


Gönder tuşuna bastıktan sonra yanıt olarak bu şekilde bir post nesnesi alırsak, her şey doğru gitmiş demektir. Şimdi kullanıcının ödeme yapabilmesi için metni görüntülememiz gerekiyor.


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


## Yeni Invoice görünümü


Görünümler dizininde, aşağıdaki içeriğe sahip Invoice.pug adlı bir dosya oluşturmamız gerekir:


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


Ve index.pug dosyasına ekleyin


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## App.sendBtn() işlevini değiştirme


Şimdi elde edilen verileri görüntülemek için App.sendBtn() işlevini değiştiriyoruz:


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


## Ödemenin alınması


Ödemeyi ne zaman aldığımızı bilmemiz gerekiyor, bunun için lnservice'den subscribeToInvoices() yöntemini kullanacağız, bu yöntem bir Invoice'ün durumu güncellendiğinde kod çalıştırmamıza izin veriyor, kullanmak için app.js'ye bu satırları ekliyoruz.


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


Kullanıcının bir Hash'ün ödenip ödenmediğini kontrol etmesi için API'mizde bir HTTP GET yöntemi oluşturun.


````

router.get('/post/:Hash', (req, res) => {

const { Hash } = req.params;'

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

const yanıt = await App.makeRequest({

api: `post/${Hash}`,

});

if (response.success && response.data.paid) {

console.log("Ödeme yapıldı");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

const yanıt = await App.makeRequest({

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

const isim = $("#isim").val();

const content = $("#content").val();

const yanıt = await App.makeRequest({

api: "post",

post: { isim, içerik },

});

if (!response) console.error("Veri alınırken hata oluştu!");

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

h2 Ödeme başarılı

div Ödeme kanıtı:

#preimage

```

We include it in index.pug.

```

düzeni genişletir


blok içeriği

h1 Lightning Uygulaması

include form.pug

include Invoice.pug

include success.pug

```