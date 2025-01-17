---
name: LAPP bitcoin
description: 最初のLAppを開発するためのチュートリアル
---

最初のライトニングアプリのコーディングを学ぼう

要件:

- NodeJs >= 8
- LND >= 9

NodeJsは公式ウェブサイトからダウンロードできます。

LNDノードをダウンロードして設定する代わりに、私たちはpolarツールを使用します。このツールはそのタスクを代わりに実行します。

私たちのライトニングアプリを構築するために、以下の技術を使用してください：

- ウェブサーバー用のExpress
- フロントエンド用のPugテンプレート + bootstrap

## オペレーティングシステム

Linuxの使用を推奨しますが、Windows 10を使用している場合は、これらのいくつかのステップに従ってLinuxコンソールを持つことができます。基盤の準備

アプリスケルトンを迅速に作成するために、アプリジェネレーターツールであるexpressを使用します。

```
$ sudo npm install express-generator -g
```

次の指示で、lnappという名前のExpressアプリを作成します。アプリは現在の作業ディレクトリ内のlnappというディレクトリに作成され、ビューエンジンはPugに割り当てられます。

```
$ express --view=pug lnapp
```

次に、ディレクトリに入り、ウェブサーバーが動作するために必要なパッケージをインストールします。

```
$ cd myapp
$ npm install
```

今、ただサーバーを実行してください。

```
$ npm start
```

次に、ブラウザでこのアドレス http://localhost:3000 にアクセスしてアプリにアクセスします。

生成されたアプリには、以下のディレクトリ構造があります：

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

Polarをダウンロードしてインストールしたのち、2つのLNDノード（AliceとBob）と1つのbitcoindでネットワークを作成します。アプリでノードのグラフを見たら、Startボタンをクリックし、各ノードのインジケーターが緑色に変わるまで数秒待ちます。

ライトニング上で支払いを送るためには、ノードがチャネルを介して相互接続されている必要があります。Polarでチャネルを作成するのは非常に簡単で、Aliceノードの耳の一つをマウスでクリックし、Bobノードの耳の一つにドラッグするだけです。すぐに、Open new channelと題されたモーダルウィンドウが表示されるので、デフォルト値のままにしてopen channelボタンを押します。今度はBobからAliceへと同じアクションを繰り返し、この方法で両方のノードがお金を送受金できるようにします。

## Nodemon

コードを変更するたびにnodejsを再起動する必要がないように、nodemonをインストールします

```
$ npm install nodemon -D
```

package.jsonファイルのscriptsセクションにエントリを作成する必要があります、この行を追加します "dev": "nodemon ./bin/www"、scriptsセクションは次のようになります：

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

npm startが実行されているコンソールに行き、ctrl + cを押してnodejsを再起動しますが、今回はnodemonを使用します。

```
$ npm run dev
```

## LNDに接続する

nodejsからLightningノードに接続するために、ln-serviceライブラリを使用します。また、環境変数を管理するためにdotenvもインストールします。

```
$ npm install ln-service dotenv
```

私たちのlnappディレクトリ内に、.envというファイルを作成してください。このファイルには以下の変数を含める必要があります：

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Polarに戻り、接続したいノードであるBobを選択し、「Connect」タブに進んでください。GRPC Hostの内容をコピーしてLND_GRPC_HOST変数に入れ、connectタブの下部でbase64を選択し、TLS Certの内容をコピーしてLND_CERT_BASE64変数に入れ、admin macaroonも同様にLND_MACAROON_BASE64に入れてください。

次に、作業ディレクトリのルートにあるapp.jsファイルにこの行を追加してください。ファイルの最初の行にコピーする必要があります。

```
require('dotenv').config();
```

nodejsが私たちのノードに接続できるかを確認するために、routes/index.jsファイルを開いてください。このルートファイルはexpress generatorによって作成されました。まず、ln-serviceライブラリを要求するため、最初の行に追加します。

```
const lnservice = require('ln-service');
```

私たちのノードに関する情報を提供する新しいルートを追加します。

```
router.get('/info', async function(req, res, next) {
try {
// lndで認証
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// ノード情報を取得
const info = await lnservice.getWalletInfo({ lnd });

    // 情報をjson形式で表示
    res.send(`/
      <h1>Node info</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

これで、http://localhost:3000/info にアクセスしてください。

LNDノードの情報がjsonで表示されたら、おめでとうございます！！！ あなたのアプリはこれでライトニングネットワークとやり取りできるようになりました。偽のモデルの作成

データベースをシミュレートするために、偽のモデルを作成する必要があります。これにより、データベースのインストールや設定を行わずにアプリを使用できるようになります。

まず、uuidパッケージをインストールしてください。

```
$ npm install uuid
```

modelsディレクトリを作成し、その中に以下の内容でPost.jsファイルを作成してください：

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
```

## ビューの準備

HTMLをより良く見せるために、bootstrapが必要です。そのため、viewsディレクトリにあるlayout.pugファイルを以下のように変更します：

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

投稿を作成するには、フォームが必要です。viewsディレクトリ内にform.pugというファイルを作成し、以下の内容を入れます：

```
.collapse#post-form
  form
    h2 記事を書く
    .form-group
      label(for="name") Name
      input(id="name").form-control
    .form-group
      label(for="content") Content
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Send
```

## フロントエンド内のJavascript

ユーザーと直接やり取りする最も直接的な方法は、ウェブブラウザでjavascriptを使用することです。これを行うには、layout.pugから既に呼び出しているjavascriptディレクトリにmain.jsというファイルを作成し、プロジェクトを初期化します。main.jsの初期内容は以下の通りです：

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

"Send（送信）"ボタンをクリックすると、すべてが正しければコンソールに"!hola"というメッセージが表示されるはずです。これで、App.sendBtn()メソッドを変更して、情報をAPIに送信することができます。

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

```
// APIから来るデータをコンソールに表示
console.log(response.data);
}
};
```

また、main.jsにApp.makeRequest()メソッドを作成して追加します。

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

## APIの作成

これを行うには、routes/api.jsに新しいファイルを作成し、App.sendBtn()内で行われたリクエストに応答するメソッドを記述する必要があります。

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

このファイルはapp.jsに含める必要がありますので、以下の行を追加します：

```
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

もう一度送信ボタンを押すと、フォームに入力したデータと同じデータで応答するはずです。

## インボイスの作成

ユーザーが投稿を作成するときに実行されるメソッドは、請求書を生成し、それを請求書にリンクするデータベースレコードを作成し、ユーザーが支払いを行えるように請求書をユーザーに返す必要があります。

```
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

送信後にこのような投稿オブジェクトがレスポンスとして返された場合、すべて正しく行われています。続いて、ユーザーが支払いを行えるようにテキストを表示する必要があります。

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
}
```

## 新しいインボイスview

viewsディレクトリには、以下の内容を含むinvoice.pugというファイルを作成する必要があります：

```
.collapse#invoice-form
form
.h2 この請求書を支払う
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

そして、それをindex.pugに含めます

```
extends layout

block content
h1 Lightning App
include form.pug
include invoice.pug
```

## App.sendBtn()の修正

次に、取得したデータを表示するようにApp.sendBtn()を修正します：

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

支払いを受け取ったことを知る必要があります。そのためには、lnserviceのsubscribeToInvoices()メソッドを使用します。このメソッドにより、インボイスのステータスが更新された時にコードを実行することができます。これを使用するには、app.jsに以下の行を追加します。

```javascript
// lnserviceと投稿テーブルを要求
const lnservice = require('ln-service');
const post = require('./models/Post');

// lndで認証する
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// 請求書が更新されるたびに、請求書が支払われたかどうかを確認する
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // 請求書を「支払済み」としてマークする
      const paid = post.paid(invoice.id);
      if (paid) console.log('Invoice paid!');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// 請求書のサブスクリプションを開始する
subscribeInvoices();
```

ユーザーがハッシュが支払われたかどうかを確認できるように、APIにHTTP GETメソッドを作成します。

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

しかし、問題に直面します。関数App.waitPayment()は一度だけ実行され、ユーザーが支払いを行ったにも関わらず、その支払いを受け取ったことを示すことができません。これに対処するために、setInterval()というJavaScript関数を使用します。これにより、指定した時間間隔で関数を無期限に実行することができます。

関数App.waitPayment()とApp.sendBtn()をsetInterval()とclearInterval()を含むように修正しましょう。

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

支払いが正常に受け取られたことを示すビューを作成します。viewsにsuccess.pugファイルを以下の内容で作成します：

```
.collapse#success
  h2 支払い成功
  div 支払い証明：
    #preimage
```

これをindex.pugに含めます。

```
extends layout

block content
  h1 Lightning App
  include form.pug
  include invoice.pug
  include success.pug
```

インボイス支払い後に「支払い成功」というメッセージと支払い証明が表示されたら、おめでとうございます！！！ あなたは最初のLAppを完成しました。
