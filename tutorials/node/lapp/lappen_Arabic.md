# دليل لتطوير أول تطبيق LApp للبيتكوين

تعلم كيفية برمجة أول تطبيق لايتنينغ

المتطلبات:

- NodeJs >= 8
- LND >= 9

يمكن تنزيل NodeJs من موقعه الرسمي

بدلاً من تنزيل وإعداد عقدة LND، سنستخدم أداة polar التي ستقوم بهذه المهمة بالنيابة عنا.

لبناء تطبيق Lightning الخاص بنا، سنستخدم التقنيات التالية:

- Express لخادم الويب الخاص بنا
- قوالب Pug + bootstrap لواجهة المستخدم الأمامية

## نظام التشغيل

من المستحسن استخدام نظام Linux، إذا كنت تستخدم Windows 10 يمكنك الحصول على وحدة تحكم Linux عن طريق اتباع هذه الخطوات البسيطة.
التحضير الأساسي

استخدم أداة مولد التطبيق، express، لإنشاء هيكل تطبيق بسرعة.

```
$ sudo npm install express-generator -g
```

باستخدام التعليمات التالية، ننشئ تطبيق Express يسمى lnapp. سيتم إنشاء التطبيق في دليل يسمى lnapp في دليل العمل الحالي، وسيتم تعيين محرك العرض إلى Pug.

```
$ express --view=pug lnapp
```

ثم ندخل إلى الدليل ونقوم بتثبيت الحزم اللازمة لتشغيل خادم الويب.

```
$ cd myapp
$ npm install
```

الآن نقوم ببساطة بتشغيل الخادم

```
$ npm start
```

بعد ذلك، انتقل إلى هذا العنوان http://localhost:3000 في المتصفح للوصول إلى التطبيق.

يحتوي التطبيق الذي تم إنشاؤه على الهيكل الدليلي التالي:

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

قم بتنزيل Polar، قم بتثبيته، وأنشئ شبكة تحتوي على عقدتين LND (أليس وبوب) وعقدة bitcoind واحدة. بمجرد رؤية الرسم البياني في التطبيق يعرض العقدتين، انقر على زر البدء وانتظر بضع ثوانٍ حتى يتغير لون مؤشر كل عقدة إلى اللون الأخضر.

لإرسال المدفوعات على الشبكة البرقية، من الضروري أن تكون العقدتين متصلتين ببعضهما البعض من خلال القنوات. إن إنشاء قنوات باستخدام Polar أمر بسيط جدًا، فقط نحتاج إلى النقر بالماوس على أحد الأذنين لعقدة أليس وسحبها إلى أحد الأذنين لعقدة بوب. على الفور، يجب أن تظهر نافذة نموذجية بعنوان "فتح قناة جديدة"، نترك القيم الافتراضية ونضغط على زر فتح القناة. الآن نكرر الإجراء ولكن هذه المرة من بوب إلى أليس، بهذه الطريقة يمكن لكلتا العقدتين إرسال واستقبال الأموال.

## Nodemon

لتجنب الحاجة إلى إعادة تشغيل nodejs في كل مرة نقوم فيها بتغيير في الشفرة، سنقوم بتثبيت nodemon

```
$ npm install nodemon -D
```

يجب علينا إنشاء إدخال في قسم النصوص في ملف package.json، أضف هذا السطر "dev": "nodemon ./bin/www"، يجب أن يبدو قسم النصوص كالتالي:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

انتقل إلى وحدة التحكم حيث يتم تشغيل npm start، اضغط على ctrl + c وابدأ nodejs مرة أخرى ولكن هذه المرة باستخدام nodemon

```
$ npm run dev
```

## الاتصال بـ LND

للاتصال بعقدة Lightning من nodejs، سنستخدم مكتبة ln-service، وسنقوم أيضًا بتثبيت dotenv لإدارة المتغيرات البيئية.
```$ npm install ln-service dotenv
```

في دليل lnapp الخاص بنا، قم بإنشاء ملف يسمى .env، يجب أن يحتوي على هذه المتغيرات:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

عد إلى Polar، حدد Bob، العقدة التي نريد الاتصال بها، انتقل إلى علامة "الاتصال"، انسخ محتوى GRPC Host وضعه في المتغير LND_GRPC_HOST، في الجزء السفلي من علامة الاتصال، حدد base64 وانسخ محتوى TLS Cert وضعه في المتغير LND_CERT_BASE64، وافعل الشيء نفسه مع admin macaroon في المتغير LND_MACAROON_BASE64.

الآن أضف هذا السطر إلى ملف app.js الموجود في جذر دليل العمل، يجب نسخه في السطر الأول من الملف.

```
require('dotenv').config();
```

للتحقق من قدرة nodejs على الاتصال بالعقدة الخاصة بنا، افتح ملف routes/index.js، هذا الملف المسارات تم إنشاؤه بواسطة مولد express، أولاً نحتاج إلى المكتبة ln-service، لذا نضيفها في السطر الأول

```
const lnservice = require('ln-service');
```

نضيف مسارًا جديدًا سيعطينا معلومات حول العقدة الخاصة بنا.

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

الآن انتقل إلى هذا العنوان http://localhost:3000/info

إذا رأيت json يحتوي على معلومات عقدة LND، تهانينا!!! يمكن لتطبيقك الآن التفاعل مع شبكة Lightning.
إنشاء نموذج وهمي

لمحاكاة قاعدة بيانات، نحتاج إلى إنشاء نموذج وهمي، وهذا سيسمح لنا باستخدام التطبيق بدون تثبيت وتكوين قاعدة بيانات.

أولاً، قم بتثبيت حزمة uuid

```
$ npm install uuid
```

قم بإنشاء دليل models وداخله، قم بإنشاء ملف Post.js بالمحتوى التالي:

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
إذا (p.hash === hash) {        updatedPost = { ...p, paid: true };
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

## إعداد العرض

نحتاج إلى Bootstrap لجعل صفحتنا تبدو أفضل، لذا نقوم بتعديل ملف layout.pug الموجود في مجلد العروض ليبدو على النحو التالي:

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

## إنشاء منشور

لإنشاء منشور، نحتاج إلى نموذج. داخل مجلد العروض، قم بإنشاء ملف يسمى form.pug بالمحتوى التالي:

```
.collapse#post-form
  form
    h2 اكتب مقالًا
    .form-group
      label(for="name") الاسم
      input(id="name").form-control
    .form-group
      label(for="content") المحتوى
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") إرسال
```

## جافا سكريبت في الواجهة الأمامية

أكثر الطرق المباشرة التي لدينا للتفاعل مع المستخدم هي باستخدام جافا سكريبت في متصفح الويب. لذلك، قم بإنشاء ملف يسمى main.js في مجلد الجافا سكريبت، الذي نستدعيه بالفعل من layout.pug. في هذا الملف، قم بتهيئة المشروع. المحتوى الأولي لملف main.js هو كالتالي:

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

انقر على زر "إرسال" وإذا كان كل شيء على ما يرام، يجب أن يظهر رسالة "!hola" في وحدة التحكم. الآن يمكننا تعديل طريقة App.sendBtn() لإرسال المعلومات إلى واجهة برمجة التطبيقات الخاصة بنا.

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

نقوم أيضًا بإنشاء طريقة App.makeRequest() وإضافتها إلى main.js

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

## إنشاء واجهة برمجة التطبيقات

للقيام بذلك، نحتاج إلى إنشاء ملف جديد في routes/api.js وكتابة الطريقة التي تستجيب للطلب الذي تم إجراؤه داخل App.sendBtn().

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

يجب تضمين هذا الملف في app.js ، لذا نضيف هذه الأسطر:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

لنضغط على زر الإرسال مرة أخرى ويجب أن يستجيب بنفس البيانات التي أدخلناها في النموذج.

## إنشاء الفاتورة

يجب أن يقوم الطريقة التي يتم تنفيذها عندما يقوم المستخدم بإنشاء منشور بإنشاء فاتورة ، ثم إنشاء سجل في قاعدة البيانات يربطه بالفاتورة ، وإرجاع الفاتورة إلى المستخدم حتى يتمكنوا من دفعها.

```markdown
router.post('/post', async (req, res) => {
// المصادقة مع lnd
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

إذا تلقينا كائن منشور كاستجابة بعد الضغط على الزر إرسال ، مثل هذا ، فقد تم كل شيء بشكل صحيح. الآن نحتاج إلى عرض النص حتى يتمكن المستخدم من دفعه.

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

## عرض الفاتورة الجديدة

في دليل العروض ، نحتاج إلى إنشاء ملف يسمى invoice.pug بالمحتوى التالي:

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

وتضمينه في index.pug

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## تعديل App.sendBtn()

الآن نقوم بتعديل App.sendBtn() لعرض البيانات المحصلة:

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

## استلام الدفعة
نحتاج أن نعرف متى نتلقى الدفعة، ولهذا سنستخدم طريقة subscribeToInvoices() من lnservice، تسمح لنا هذه الطريقة بتنفيذ الكود عند تحديث حالة الفاتورة، لاستخدامها نضيف هذه الأسطر في app.js.

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

أنشئ طريقة HTTP GET في واجهة برمجة التطبيقات (API) الخاصة بنا للمستخدم للتحقق مما إذا تم دفع الهاش.

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

الآن، من main.js، ننشئ وظيفة تسمى App.waitPayment() التي تستعلم الواجهة البرمجية إذا تم الدفع.

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

الآن نواجه مشكلة، وظيفة App.waitPayment() تُنفذ مرة واحدة فقط، قد يكون المستخدم قد قام بالدفع ولم نتمكن من إشعارهم بأن دفعتهم قد تم استلامها. لهذا، نستخدم وظيفة JavaScript تُسمى setInterval() التي تسمح لنا بتنفيذ وظيفة بشكل مستمر بفاصل زمني نحدده.

لنعدل الوظائف App.waitPayment() و App.sendBtn() بما في ذلك setInterval() و clearInterval()

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
ونقوم بإنشاء عرض للإشارة إلى أن الدفع تم استلامه بنجاح، نقوم بإنشاء ملف success.pug في المجلد views بالمحتوى التالي:
```pug
.collapse#success
  h2 تم الدفع بنجاح
  div دليل الدفع:
    #preimage
```

نضمن تضمينه في index.pug.

```pug
extends layout

block content
  h1 تطبيق Lightning
  include form.pug
  include invoice.pug
  include success.pug
```

إذا بعد دفع الفاتورة يمكنك رؤية الرسالة "تم الدفع بنجاح" ودليل الدفع، مبروك!!! لقد قمت بذلك، لقد انتهيت من أول تطبيق Lightning لديك.