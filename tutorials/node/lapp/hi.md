---
name: लैप जीडब्ल्यू-0
description: अपना पहला LApp विकसित करने के लिए ट्यूटोरियल
---

अपना पहला लाइटनिंग ऐप कोड करना सीखें


आवश्यकताएं:



- नोडजेएस >= 8
- जीडब्ल्यू-1 >= 9


NodeJs को इसकी आधिकारिक वेबसाइट से डाउनलोड किया जा सकता है


LND नोड को डाउनलोड करने और सेट अप करने के बजाय, हम पोलर टूल का उपयोग करेंगे, जो हमारे लिए यह कार्य करेगा।


अपना लाइटनिंग ऐप बनाने के लिए हम निम्नलिखित तकनीकों का उपयोग करेंगे:



- हमारे वेबसर्वर के लिए एक्सप्रेस
- हमारे फ्रंटएंड के लिए पग टेम्पलेट्स + बूटस्ट्रैप


## ऑपरेटिंग सिस्टम


लिनक्स का उपयोग करने की अनुशंसा की जाती है, यदि आप विंडोज 10 पर हैं तो आप इन कुछ चरणों का पालन करके लिनक्स कंसोल प्राप्त कर सकते हैं।

आधार तैयार करना


एप्लिकेशन कंकाल को शीघ्रता से बनाने के लिए एप्लिकेशन जनरेटर टूल, एक्सप्रेस का उपयोग करें।


```
$ sudo npm install express-generator -g
```


निम्नलिखित निर्देश के साथ, हम lnapp नामक एक एक्सप्रेस एप्लिकेशन बनाते हैं। एप्लिकेशन को वर्तमान कार्यशील निर्देशिका में lnapp नामक निर्देशिका में बनाया जाएगा, और व्यू इंजन को Pug को सौंपा जाएगा।


```
$ express --view=pug lnapp
```


फिर हम डायरेक्टरी में प्रवेश करते हैं और वेब सर्वर को चलाने के लिए आवश्यक पैकेज स्थापित करते हैं।


```
$ cd myapp
$ npm install
```


अब हम बस सर्वर चलाते हैं


```
$ npm start
```


इसके बाद, एप्लिकेशन तक पहुंचने के लिए ब्राउज़र में इस Address http://localhost:3000 पर जाएं।


उत्पन्न अनुप्रयोग की निर्देशिका संरचना निम्नलिखित है:


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


## ध्रुवीय


पोलर डाउनलोड करें, इसे इंस्टॉल करें, और 2 LND नोड्स (ऐलिस और बॉब) और 1 bitcoind के साथ एक नेटवर्क बनाएं। एक बार जब हम अपने नोड्स को दिखाते हुए ऐप में ग्राफ़ देखते हैं, तो स्टार्ट बटन पर क्लिक करें और कुछ सेकंड तक प्रतीक्षा करें जब तक कि प्रत्येक नोड का संकेतक Green में रंग न बदल जाए।


लाइटनिंग पर भुगतान भेजने के लिए, नोड्स का चैनलों के माध्यम से आपस में जुड़ा होना आवश्यक है। पोलर के साथ चैनल बनाना बहुत सरल है, हमें बस एलिस नोड के एक कान पर माउस से क्लिक करना है और इसे बॉब नोड के एक कान पर खींचना है। तुरंत, ओपन न्यू चैनल नामक एक मॉडल विंडो दिखाई देनी चाहिए, हम डिफ़ॉल्ट मानों को छोड़ देते हैं और ओपन चैनल बटन दबाते हैं। अब हम कार्रवाई को दोहराते हैं लेकिन इस बार बॉब से एलिस तक, इस तरह से दोनों नोड्स पैसे भेज और प्राप्त कर सकते हैं।


## नोडेमोन


कोड में कोई भी परिवर्तन करने पर हर बार नोडज को पुनः आरंभ करने से बचने के लिए, हम नोडमॉन स्थापित करेंगे


```
$ npm install nodemon -D
```


हमें package.json फ़ाइल के स्क्रिप्ट अनुभाग में एक प्रविष्टि बनानी होगी, यह पंक्ति "dev": "nodemon ./bin/www" जोड़नी होगी, स्क्रिप्ट अनुभाग इस तरह दिखना चाहिए:


```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```


कंसोल पर जाएं जहां npm start चल रहा है, ctrl + c दबाएं और nodejs को फिर से शुरू करें लेकिन इस बार nodemon का उपयोग करके


```
$ npm run dev
```


## LND से जुड़ना


नोडजेएस से लाइटनिंग नोड से कनेक्ट करने के लिए, हम LN-service लाइब्रेरी का उपयोग करेंगे, हम पर्यावरण चर को प्रबंधित करने के लिए dotenv भी इंस्टॉल करेंगे।


```
$ npm install ln-service dotenv
```


हमारी lnapp निर्देशिका में, .env नामक एक फ़ाइल बनाएं, इसमें ये चर शामिल होने चाहिए:


```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```


पोलर पर वापस जाएं, बॉब का चयन करें, वह नोड जिससे हम कनेक्ट करना चाहते हैं, "कनेक्ट" टैब पर जाएं, GRPC होस्ट की सामग्री की प्रतिलिपि बनाएं और इसे LND_GRPC_HOST वेरिएबल में रखें, कनेक्ट टैब के निचले भाग में बेस64 का चयन करें और TLS प्रमाणपत्र की सामग्री की प्रतिलिपि बनाएं और इसे LND_CERT_BASE64 वेरिएबल में रखें, और LND_MACAROON_BASE64 में एडमिन मैकरून के साथ भी ऐसा ही करें।


अब इस लाइन को कार्यशील निर्देशिका के रूट में स्थित app.js फ़ाइल में जोड़ें, हमें इसे फ़ाइल की पहली पंक्ति पर कॉपी करना होगा।


```
require('dotenv').config();
```


यह सत्यापित करने के लिए कि nodejs हमारे नोड से कनेक्ट हो सकता है, रूट्स/index.js फ़ाइल खोलें, यह रूट्स फ़ाइल एक्सप्रेस जनरेटर द्वारा बनाई गई थी, सबसे पहले हमें LN-service लाइब्रेरी की आवश्यकता होती है, इसलिए हम इसे पहली पंक्ति में जोड़ते हैं


```
const lnservice = require('ln-service');
```


हम एक नया रूट जोड़ते हैं जो हमें हमारे नोड के बारे में जानकारी देगा।


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


अब इस Address http://localhost:3000/info पर जाएं


यदि आपको LND नोड की जानकारी वाला JSON दिखाई देता है, तो बधाई हो!!! अब आपका ऐप Lightning Network के साथ इंटरैक्ट कर सकता है।

नकली मॉडल बनाना


डेटाबेस का अनुकरण करने के लिए, हमें एक नकली मॉडल बनाने की आवश्यकता है, इससे हम डेटाबेस को स्थापित और कॉन्फ़िगर किए बिना ऐप का उपयोग करने की अनुमति देंगे।


सबसे पहले, uuid पैकेज स्थापित करें


```
$ npm install uuid
```


मॉडल्स निर्देशिका बनाएं और उसके अंदर निम्नलिखित सामग्री के साथ Post.js फ़ाइल बनाएं:


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


## दृश्य तैयार करें


हमें अपने HTML को बेहतर बनाने के लिए बूटस्ट्रैप की आवश्यकता है, इसलिए हम दृश्य निर्देशिका में स्थित layout.pug फ़ाइल को इस तरह से संशोधित करते हैं:


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


## पोस्ट बनाना


पोस्ट बनाने के लिए हमें एक फ़ॉर्म की ज़रूरत होती है। व्यूज़ डायरेक्टरी के अंदर, निम्न सामग्री के साथ form.pug नामक एक फ़ाइल बनाएँ:


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


## फ्रंटएंड में जावास्क्रिप्ट


उपयोगकर्ता के साथ बातचीत करने का सबसे सीधा तरीका वेब ब्राउज़र में जावास्क्रिप्ट का उपयोग करना है। इसके लिए, जावास्क्रिप्ट निर्देशिका में main.js नामक एक फ़ाइल बनाएँ, जिसे हम पहले से ही layout.pug से कॉल कर रहे हैं। इस फ़ाइल में, प्रोजेक्ट को इनिशियलाइज़ करें। main.js की प्रारंभिक सामग्री इस प्रकार है:


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


"Enviar" बटन पर क्लिक करें और अगर सब कुछ ठीक है, तो कंसोल में "!hola" संदेश दिखना चाहिए। अब हम अपने API को जानकारी भेजने के लिए App.sendBtn() विधि को संशोधित कर सकते हैं।


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


हम App.makeRequest() विधि भी बनाते हैं और इसे main.js में जोड़ते हैं


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


## एपीआई बनाएं


ऐसा करने के लिए, हमें roots/api.js में एक नई फ़ाइल बनानी होगी और App.sendBtn() में किए गए अनुरोध का जवाब देने वाली विधि लिखनी होगी।


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


यह फ़ाइल app.js में शामिल होनी चाहिए, इसलिए हम ये पंक्तियाँ जोड़ते हैं:


```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```


आइए पुनः भेजें बटन दबाएं और यह उसी डेटा के साथ प्रतिक्रिया देगा जो हमने फॉर्म में दर्ज किया था।


## Invoice बनाएं


जब कोई उपयोगकर्ता कोई पोस्ट बनाता है तो जो विधि क्रियान्वित होती है, उसमें generate को Invoice बनाना चाहिए, फिर डेटाबेस में इसे Invoice से जोड़ते हुए एक रिकॉर्ड बनाना चाहिए, तथा उपयोगकर्ता को Invoice वापस करना चाहिए, ताकि वे उसका भुगतान कर सकें।


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


अगर हमें सेंड बटन दबाने के बाद प्रतिक्रिया के रूप में पोस्ट ऑब्जेक्ट मिलता है, तो इसका मतलब है कि सब कुछ सही तरीके से हो गया है। अब हमें टेक्स्ट दिखाना होगा ताकि यूजर उसका भुगतान कर सके।


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


## नया Invoice दृश्य


दृश्य निर्देशिका में, हमें निम्नलिखित सामग्री के साथ Invoice.pug नामक एक फ़ाइल बनाने की आवश्यकता है:


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


और इसे index.pug में शामिल करें


```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```


## App.sendBtn() को संशोधित करना


अब हम प्राप्त डेटा को प्रदर्शित करने के लिए App.sendBtn() को संशोधित करते हैं:


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


## भुगतान प्राप्त करना


हमें यह जानना होगा कि हमें भुगतान कब प्राप्त हुआ है, इसके लिए हम lnservice से subscribeToInvoices() विधि का उपयोग करेंगे, यह विधि हमें Invoice की स्थिति अपडेट होने पर कोड निष्पादित करने की अनुमति देती है, इसका उपयोग करने के लिए हम app.js में ये पंक्तियाँ जोड़ते हैं।


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


हमारे API में एक HTTP GET विधि बनाएं जिससे उपयोगकर्ता यह जांच सके कि Hash का भुगतान किया गया है या नहीं।


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

const प्रतिक्रिया = App.makeRequest का इंतजार करें({

एपीआई: `पोस्ट/${Hash}`,

});

यदि (प्रतिक्रिया.सफलता और प्रतिक्रिया.डेटा.भुगतान) {

कंसोल.लॉग("भुगतान किया गया");

}

};

```

Now we encounter a problem, the function App.waitPayment() is only executed once, the user may have made the payment and we have not been able to indicate that their payment has been received. For this, we use a JavaScript function called setInterval() that allows us to execute a function indefinitely at the interval of time we have indicated.

Let's modify the functions App.waitPayment() and App.sendBtn() including setInterval() and clearInterval()

```

App.waitPayment = async (Hash) => {

const प्रतिक्रिया = App.makeRequest का इंतजार करें({

एपीआई: `पोस्ट/${Hash}`,

});

यदि (प्रतिक्रिया.सफलता और प्रतिक्रिया.डेटा.भुगतान) {

क्लियरइंटरवल(ऐप.इंटरवल);

ऐप.अंतराल = शून्य;

$("#Invoice-form").collapse("छिपाएं");

$("#preimage").text(response.data.preimage);

$("#सफलता").collapse("दिखाएँ");

}

};


App.sendBtn = async () => {

const नाम = $("#name").val();

const सामग्री = $("#content").val();

const प्रतिक्रिया = App.makeRequest का इंतजार करें({

एपीआई: "पोस्ट",

पोस्ट: { नाम, सामग्री },

});

if (!response) console.error("डेटा प्राप्त करने में त्रुटि!");

यदि (प्रतिक्रिया.सफलता) {

$("#पोस्ट-फॉर्म").collapse("छिपाएं");

$("#Invoice-form").collapse("दिखाएँ");

$("#Invoice").val(response.data.request);

ऐप.इंटरवल = सेटइंटरवल(ऐप.वेटपेमेंट, 1000, रिस्पॉन्स.डेटा.Hash);

}

};

```

And we create a view to indicate that the payment has been successfully received, we create the file success.pug in views with the following content:

```

.collapse#सफलता

h2 भुगतान सफल

भुगतान प्रमाण:

#पूर्व छवि

```

We include it in index.pug.

```

लेआउट का विस्तार


सामग्री ब्लॉक करें

h1 लाइटनिंग ऐप

फॉर्म.पग शामिल करें

Invoice.pug शामिल करें

सफलता शामिल करें.pug

```