---
name: LAPP bitcoin
description: Учебник по разработке вашего первого LApp
---

Научитесь программировать ваше первое приложение Lightning

Требования:

- NodeJs >= 8
- LND >= 9

NodeJs можно скачать с его официального сайта

Вместо загрузки и настройки узла LND мы будем использовать инструмент polar, который выполнит эту задачу за нас.

Для создания нашего приложения Lightning мы будем использовать следующие технологии:

- Express для нашего веб-сервера
- Шаблоны Pug + bootstrap для нашего фронтенда

## Операционная система

Рекомендуется использовать Linux, если вы используете Windows 10, вы можете иметь консоль Linux, следуя этим нескольким шагам.
Подготовка основы

Используйте инструмент для генерации приложений, express, чтобы быстро создать скелет приложения.

```
$ sudo npm install express-generator -g
```

Следующей инструкцией мы создаем приложение Express под названием lnapp. Приложение будет создано в директории под названием lnapp в текущем рабочем каталоге, и в качестве движка представлений будет назначен Pug.

```
$ express --view=pug lnapp
```

Затем мы входим в директорию и устанавливаем необходимые пакеты для работы веб-сервера.

```
$ cd myapp
$ npm install
```

Теперь просто запускаем сервер

```
$ npm start
```

Далее, перейдите по этому адресу http://localhost:3000 в браузере, чтобы получить доступ к приложению.

Сгенерированное приложение имеет следующую структуру директорий:

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

Скачайте Polar, установите его и создайте сеть с 2 узлами LND (Alice и Bob) и 1 bitcoind. Как только мы увидим график в приложении, показывающий наши узлы, нажмите кнопку Start и подождите несколько секунд, пока индикатор каждого узла не изменит цвет на зеленый.

Для отправки платежей по сети Lightning необходимо, чтобы узлы были соединены через каналы. Создание каналов с помощью Polar очень просто, нам просто нужно щелкнуть мышью на одном из ушей узла Alice и перетащить его на одно из ушей узла Bob. Сразу же должно появиться модальное окно с названием Открыть новый канал, мы оставляем значения по умолчанию и нажимаем кнопку открытия канала. Теперь мы повторяем действие, но на этот раз от Bob к Alice, таким образом оба узла могут отправлять и получать деньги.

## Nodemon

Чтобы не приходилось перезапускать nodejs каждый раз, когда мы вносим изменения в код, мы установим nodemon

```
$ npm install nodemon -D
```

Мы должны создать запись в разделе scripts файла package.json, добавьте эту строку "dev": "nodemon ./bin/www", раздел scripts должен выглядеть так:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Перейдите в консоль, где запущен npm start, нажмите ctrl + c и снова запустите nodejs, но на этот раз используя nodemon

```
$ npm run dev
```

## Подключение к LND

Для подключения к узлу Lightning из nodejs мы будем использовать библиотеку ln-service, также мы установим dotenv для управления переменными окружения.

```
$ npm install ln-service dotenv
В нашем каталоге lnapp создайте файл с именем .env, он должен содержать следующие переменные:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Вернитесь в Polar, выберите Bob, узел, к которому мы хотим подключиться, перейдите на вкладку "Подключение", скопируйте содержимое GRPC Host и поместите его в переменную LND_GRPC_HOST, в нижней части вкладки подключения выберите base64 и скопируйте содержимое TLS Cert и поместите его в переменную LND_CERT_BASE64, и сделайте то же самое с административным macaroon в LND_MACAROON_BASE64.

Теперь добавьте эту строку в файл app.js, расположенный в корне рабочего каталога, мы должны скопировать ее в первую строку файла.

```
require('dotenv').config();
```

Чтобы проверить, может ли nodejs подключиться к нашему узлу, откройте файл routes/index.js, этот файл маршрутов был создан с помощью генератора express, сначала мы требуем библиотеку ln-service, поэтому добавляем ее на первую строку

```
const lnservice = require('ln-service');
```

Мы добавляем новый маршрут, который даст нам информацию о нашем узле.

```
router.get('/info', async function(req, res, next) {
try {
// аутентификация с lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// получить информацию об узле
const info = await lnservice.getWalletInfo({ lnd });

    // отобразить информацию в формате json
    res.send(`
      <h1>Информация об узле</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Теперь перейдите по этому адресу http://localhost:3000/info

Если вы видите json с информацией об узле LND, поздравляем!!! ваше приложение теперь может взаимодействовать с Lightning Network.
Создание фиктивной модели

Чтобы симулировать базу данных, нам нужно создать фиктивную модель, это позволит нам использовать приложение без установки и настройки базы данных.

Сначала установите пакет uuid

```
$ npm install uuid
```

Создайте каталог models и внутри него создайте файл Post.js со следующим содержимым:

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
```markdown
const router = express.Router();
const posts = require('../models/posts');

router.post('/post', async (req, res) => {
  try {
    const { name, content } = req.body;
    const newPost = await posts.createPost(name, content);
    if (newPost) {
      res.json({ success: true, data: newPost });
    } else {
      res.json({ success: false });
    }
  } catch (error) {
    res.status(500).json({ success: false, error: 'Ошибка сервера' });
  }
});

module.exports = router;
```

## Подготовка представления

Нам нужен Bootstrap, чтобы наш HTML выглядел лучше, поэтому мы модифицируем файл layout.pug, расположенный в директории views, чтобы он выглядел так:

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

## Создание поста

Чтобы создать пост, нам нужна форма. Внутри директории views создайте файл с именем form.pug со следующим содержанием:

```
.collapse#post-form
  form
    h2 Напишите статью
    .form-group
      label(for="name") Имя
      input(id="name").form-control
    .form-group
      label(for="content") Содержание
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Отправить
```

## Javascript на клиенте

Самый прямой способ взаимодействия с пользователем - использование javascript в веб-браузере. Для этого создайте файл с именем main.js в директории javascript, который мы уже вызываем из layout.pug. В этом файле инициализируйте проект. Исходное содержание main.js следующее:

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
  console.log('!привет');
};

$(() => App.init());
```

Нажмите кнопку "Отправить", и если все в порядке, в консоли должно появиться сообщение "!привет". Теперь мы можем модифицировать метод App.sendBtn(), чтобы отправить информацию в наш API.

```
App.sendBtn = async () => {
  const name = $('#name').val();
  const content = $('#content').val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error('Ошибка получения данных!');
  if (response.success) {
    // Что-то делаем с ответом
  }
};
```

```markdown
// Выводим в консоль данные, полученные от API
console.log(response.data);
}
};
```

Также создаем метод App.makeRequest() и добавляем его в main.js

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

## Создание API

Для этого нам нужно создать новый файл в routes/api.js и написать метод, который отвечает на запрос, сделанный в App.sendBtn().

```markdown
const express = require('express');
```
```markdown
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

Этот файл должен быть включен в app.js, поэтому мы добавляем следующие строки:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Давайте снова нажмем кнопку отправки, и она должна ответить теми же данными, которые мы ввели в форму.

## Создание счета

Метод, который выполняется при создании пользователем поста, должен генерировать счет, затем создавать запись в базе данных, связывая ее со счетом, и возвращать счет пользователю, чтобы он мог его оплатить.

```markdown
router.post('/post', async (req, res) => {
// Аутентификация с lnd
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

Если в ответ на отправку мы получаем объект поста, как это, значит, все прошло правильно. Теперь нам нужно отобразить текст, чтобы пользователь мог его оплатить.

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

## Новый вид счета

В директории views нам нужно создать файл с именем invoice.pug со следующим содержимым:

```
.collapse#invoice-form
form
.h2 Оплатите этот счет
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

И включить его в index.pug

```
extends layout

block content
h1 Приложение Lightning
include form.pug
include invoice.pug
```

## Изменение App.sendBtn()

Теперь мы изменяем App.sendBtn(), чтобы отобразить полученные данные:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Ошибка получения данных!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Получение платежа
Нам необходимо знать, когда мы получаем платеж, для этого мы будем использовать метод subscribeToInvoices() из lnservice. Этот метод позволяет нам выполнять код, когда статус счета был обновлен. Чтобы использовать его, добавим следующие строки в app.js.

```javascript
// подключаем lnservice и нашу таблицу post
const lnservice = require('ln-service');
const post = require('./models/Post');

// аутентификация с lnd
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// проверяем, был ли счет оплачен каждый раз при обновлении счета
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // отмечаем счет как 'оплаченный'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Счет оплачен!');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// запускаем подписку на счета
subscribeInvoices();
```

Создаем метод HTTP GET в нашем API, чтобы пользователь мог проверить, был ли оплачен хеш.

```javascript
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

Теперь, из main.js, создаем функцию под названием App.waitPayment(), которая запрашивает API, был ли совершен платеж.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Платеж совершен");
  }
};
```

Теперь мы сталкиваемся с проблемой, функция App.waitPayment() выполняется только один раз, пользователь мог совершить платеж, и мы не смогли указать, что его платеж был получен. Для этого мы используем функцию JavaScript под названием setInterval(), которая позволяет нам бесконечно выполнять функцию через указанные интервалы времени.

Давайте модифицируем функции App.waitPayment() и App.sendBtn(), включив setInterval() и clearInterval()

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
  if (!response) console.error("Ошибка получения данных!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
И мы создаем представление, чтобы указать, что платеж был успешно получен, мы создаем файл success.pug в папке views со следующим содержанием:
```pug
.collapse#success
  h2 Платеж успешно выполнен
  div Доказательство платежа:
    #preimage
```

Мы включаем его в index.pug.

```pug
extends layout

block content
  h1 Приложение Lightning
  include form.pug
  include invoice.pug
  include success.pug
```

Если после оплаты счета вы можете увидеть сообщение "Платеж успешно выполнен" и доказательство платежа, поздравляем!!! Вы сделали это, вы завершили свое первое LApp.