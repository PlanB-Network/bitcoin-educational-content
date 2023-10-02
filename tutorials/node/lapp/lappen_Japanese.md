名前：LAPPビットコイン
説明：最初のLAppを開発するためのチュートリアル

# 最初のLAppを開発するためのチュートリアル

最初のライトニングアプリをコーディングする方法を学びます。

要件：

- NodeJs >= 8
- LND >= 9

NodeJsは公式ウェブサイトからダウンロードできます。

LNDノードをダウンロードしてセットアップする代わりに、このタスクを実行するpolarツールを使用します。

ライトニングアプリを構築するために、以下の技術を使用します：

- ウェブサーバーにはExpressを使用します。
- フロントエンドにはPugテンプレート+Bootstrapを使用します。

## オペレーティングシステム

Linuxを使用することをおすすめします。Windows 10を使用している場合は、以下の手順に従ってLinuxコンソールを使用できます。

ベースの準備

アプリケーションジェネレーターツールであるExpressを使用して、アプリケーションの骨組みを素早く作成します。

```
$ sudo npm install express-generator -g
```

以下の命令で、lnappという名前のExpressアプリケーションを作成します。アプリケーションは現在の作業ディレクトリ内のlnappというディレクトリに作成され、ビューエンジンにはPugが割り当てられます。

```
$ express --view=pug lnapp
```

次に、ディレクトリに移動し、ウェブサーバーの実行に必要なパッケージをインストールします。

```
$ cd myapp
$ npm install
```

これでサーバーを実行するだけです。

```
$ npm start
```

次に、ブラウザでこのアドレスhttp://localhost:3000にアクセスしてアプリケーションにアクセスします。

生成されたアプリケーションのディレクトリ構造は次のようになります。

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

Polarをダウンロードし、インストールし、2つのLNDノード（AliceとBob）と1つのbitcoindでネットワークを作成します。アプリでノードを表示するグラフを見たら、Startボタンをクリックし、各ノードのインジケータが緑色に変わるまで数秒待ちます。

ライトニングで支払いを送信するためには、ノードがチャネルを介して相互接続されている必要があります。Polarを使用してチャネルを作成するには、Aliceノードの片耳をマウスでクリックし、Bobノードの片耳にドラッグします。すると、Open new channelというタイトルのモーダルウィンドウが表示されます。デフォルトの値のままで、open channelボタンを押します。次に、同じ操作をBobからAliceに行います。これにより、両方のノードでお金を送受信できるようになります。

## Nodemon

コードを変更するたびにnodejsを再起動する手間を省くために、nodemonをインストールします。

```
$ npm install nodemon -D
```

package.jsonファイルのscriptsセクションにエントリを作成し、この行を追加します。「dev」: "nodemon ./bin/www"、scriptsセクションは次のようになります。

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

npm startが実行されているコンソールに移動し、ctrl + cを押してnodejsを再起動しますが、今回はnodemonを使用します。

```
$ npm run dev
```

## LNDへの接続

nodejsからライトニングノードに接続するために、ln-serviceライブラリを使用します。環境変数を管理するためにdotenvもインストールします。
```$ npm install ln-service dotenv
```

lnappディレクトリ内に.envというファイルを作成し、以下の変数を含めてください。

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Polarに戻り、接続したいノードであるBobを選択し、「Connect」タブに移動して、GRPC Hostの内容をコピーしてLND_GRPC_HOST変数に配置し、接続タブの下部でbase64を選択し、TLS Certの内容をLND_CERT_BASE64変数に配置し、同様にadmin macaroonもLND_MACAROON_BASE64に配置してください。

次に、作業ディレクトリのルートにあるapp.jsファイルに以下の行を追加し、ファイルの最初の行にコピーする必要があります。

```
require('dotenv').config();
```

nodejsがノードに接続できるかどうかを確認するために、routes/index.jsファイルを開きます。このroutesファイルはexpress generatorによって作成されたもので、最初の行にln-serviceライブラリを追加するため、以下のように追加します。

```
const lnservice = require('ln-service');
```

ノードに関する情報を提供する新しいルートを追加します。

```
router.get('/info', async function(req, res, next) {
try {
// lndで認証する
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// ノード情報を取得する
const info = await lnservice.getWalletInfo({ lnd });

    // json形式で情報を表示する
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

次に、http://localhost:3000/infoにアクセスしてください。

LNDノードの情報が含まれたjsonが表示されれば、おめでとうございます！アプリはLightning Networkとやり取りできるようになりました。
フェイクモデルの作成

データベースをシミュレートするために、フェイクモデルを作成する必要があります。これにより、データベースのインストールと設定なしでアプリを使用することができます。

まず、uuidパッケージをインストールします。

```
$ npm install uuid
```

modelsディレクトリを作成し、その中にPost.jsファイルを以下の内容で作成してください。

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
if (p.hash === hash) {        updatedPost = { ...p, paid: true };
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

## ビューの準備

見た目を良くするために、htmlにbootstrapを使用する必要があるため、viewsディレクトリにあるlayout.pugファイルを以下のように変更します。

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

## 投稿の作成

投稿を作成するには、フォームが必要です。viewsディレクトリ内に、以下の内容のform.pugというファイルを作成します。

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

## フロントエンドのJavascript

ユーザーとの直接的なやり取り方法は、ウェブブラウザでJavascriptを使用することです。そのため、既にlayout.pugから呼び出しているjavascriptディレクトリにmain.jsというファイルを作成します。このファイルでプロジェクトを初期化します。main.jsの初期内容は以下の通りです。

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

「Enviar」ボタンをクリックし、すべてが正常であれば、コンソールに「!hola」というメッセージが表示されるはずです。これで、App.sendBtn()メソッドを変更して情報をAPIに送信することができます。

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
// APIからのデータをコンソールに表示する
console.log(response.data);
}
};
```

また、main.jsにApp.makeRequest()メソッドを作成し、追加します。

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

## APIの作成

これを行うには、routes/api.jsという新しいファイルを作成し、App.sendBtn()内で行われるリクエストに応答するメソッドを記述する必要があります。

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

このファイルはapp.jsに含まれる必要があるため、次の行を追加します。

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

再度送信ボタンを押すと、フォームに入力したデータと同じデータが返されるはずです。

## 請求書の作成

ユーザーが投稿を作成すると実行されるメソッドは、請求書を生成し、それを請求書と関連付けてデータベースにレコードを作成し、ユーザーに請求書を返して支払いを行えるようにする必要があります。

```markdown
router.post('/post', async (req, res) => {
  // lndで認証する
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

送信ボタンを押した後にpostオブジェクトを受け取る場合、上記のようにすべてが正常に行われています。次に、ユーザーが支払いを行えるようにテキストを表示する必要があります。

```markdown
{
  "success": true,
  "data": {
    "id": "0fb1544a-d7f9-487d-961a-d0004ecc515c",
    "time": "2020-09-02T21:29:53.747Z",
    "name": "epale",
    "content": "contenido bla bla",
    "paid": false,
    "hash": "0e3c7a1151d8f8f202bc7264db83e554c9009f9bd32c0fcb0412772b310b520e",
    "preimage": null
  }
}
```

## 新しい請求書ビュー

viewsディレクトリに、次の内容のinvoice.pugというファイルを作成する必要があります。

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

そして、index.pugにそれを含めます。

```
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
```

## App.sendBtn()の変更

次に、App.sendBtn()を変更して取得したデータを表示します。

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

## 支払いの受け取り
支払いを受け取った時に知る必要があります。そのために、lnserviceのsubscribeToInvoices()メソッドを使用します。このメソッドは、請求書のステータスが更新されたときにコードを実行することを可能にします。使用するためには、app.jsに以下の行を追加します。

```javascript
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

ユーザーがハッシュが支払われたかどうかを確認するために、APIにHTTP GETメソッドを作成します。

```javascript
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
```

次に、main.jsから、支払いが行われたかどうかをAPIに問い合わせるApp.waitPayment()という関数を作成します。

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

ここで問題が発生します。関数App.waitPayment()は一度しか実行されません。ユーザーが支払いを行った場合、その支払いが受け取られたことを示すことができません。そのため、setInterval()というJavaScriptの関数を使用して、指定した時間間隔で関数を無期限に実行することができます。

setInterval()とclearInterval()を含めて、関数App.waitPayment()とApp.sendBtn()を修正しましょう。

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
支払いが正常に受け取られたことを示すビューを作成し、success.pugというファイルをviewsに作成します。内容は以下の通りです。

```pug
.collapse#success
  h2 支払いが成功しました
  div 支払いの証拠:
    #preimage
```

これをindex.pugに含めます。

```pug
extends layout

block content
  h1 Lightningアプリ
  include form.pug
  include invoice.pug
  include success.pug
```

請求書の支払い後に「支払いが成功しました」と支払いの証拠が表示されれば、おめでとうございます！あなたは最初のLAppを完成させました。