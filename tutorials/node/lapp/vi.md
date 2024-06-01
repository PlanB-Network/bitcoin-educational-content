---
name: LAPP bitcoin
description: Hướng dẫn phát triển ứng dụng Lightning đầu tiên của bạn
---

Học cách lập trình ứng dụng Lightning đầu tiên của bạn

Yêu cầu:

- NodeJs >= 8
- LND >= 9

NodeJs có thể được tải xuống từ trang web chính thức

Thay vì tải xuống và thiết lập một node LND, chúng ta sẽ sử dụng công cụ polar, công cụ này sẽ thực hiện nhiệm vụ này cho chúng ta.

Để xây dựng ứng dụng Lightning của mình, chúng ta sẽ sử dụng các công nghệ sau:

- Express cho webserver của chúng ta
- Pug templates + bootstrap cho frontend của chúng ta

## Hệ điều hành

Khuyến nghị sử dụng Linux, nếu bạn đang sử dụng Windows 10 bạn có thể có một bảng điều khiển Linux bằng cách thực hiện các bước sau.
Chuẩn bị cơ sở

Sử dụng công cụ tạo ứng dụng, express, để nhanh chóng tạo một bộ khung ứng dụng.

```
$ sudo npm install express-generator -g
```

Với lệnh sau, chúng ta tạo một ứng dụng Express có tên là lnapp. Ứng dụng sẽ được tạo trong một thư mục có tên là lnapp trong thư mục làm việc hiện tại, và view engine sẽ được gán cho Pug.

```
$ express --view=pug lnapp
```

Sau đó chúng ta vào thư mục và cài đặt các gói cần thiết để web server có thể chạy.

```
$ cd myapp
$ npm install
```

Bây giờ chúng ta chỉ cần chạy server

```
$ npm start
```

Tiếp theo, truy cập địa chỉ http://localhost:3000 trên trình duyệt để vào ứng dụng.

Ứng dụng được tạo có cấu trúc thư mục như sau:

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

Tải Polar, cài đặt nó và tạo một mạng với 2 node LND (Alice và Bob) và 1 bitcoind. Khi chúng ta thấy đồ thị trong ứng dụng hiển thị các node của mình, nhấn vào nút Start và đợi vài giây cho đến khi chỉ báo của mỗi node chuyển sang màu xanh.

Để gửi thanh toán trên Lightning, cần thiết để các node được kết nối với nhau thông qua các kênh. Tạo kênh với Polar rất đơn giản, chúng ta chỉ cần nhấp chuột vào một trong các tai của node Alice và kéo nó đến một trong các tai của node Bob. Ngay lập tức, một cửa sổ modal có tiêu đề Mở kênh mới sẽ xuất hiện, chúng ta để các giá trị mặc định và nhấn nút mở kênh. Bây giờ chúng ta lặp lại hành động nhưng lần này từ Bob đến Alice, như vậy cả hai node có thể gửi và nhận tiền.

## Nodemon

Để tránh phải khởi động lại nodejs mỗi khi chúng ta thay đổi trong mã, chúng ta sẽ cài đặt nodemon

```
$ npm install nodemon -D
```

Chúng ta phải tạo một mục trong phần scripts của tệp package.json, thêm dòng này "dev": "nodemon ./bin/www", phần scripts sẽ trông như thế này:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Chuyển đến bảng điều khiển nơi npm start đang chạy, nhấn ctrl + c và khởi động lại nodejs nhưng lần này sử dụng nodemon

```
$ npm run dev
```

## Kết nối với LND

Để kết nối với một node Lightning từ nodejs, chúng ta sẽ sử dụng thư viện ln-service, chúng ta cũng sẽ cài đặt dotenv để quản lý các biến môi trường.

```
$ npm install ln-service dotenv
Trong thư mục lnapp của chúng ta, hãy tạo một tệp có tên .env, nó nên chứa các biến sau:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Quay lại Polar, chọn Bob, nút mà chúng ta muốn kết nối, đi đến tab "Kết nối", sao chép nội dung của GRPC Host và đặt nó vào biến LND_GRPC_HOST, ở phần dưới của tab kết nối chọn base64 và sao chép nội dung của TLS Cert và đặt nó vào biến LND_CERT_BASE64, và làm tương tự với admin macaroon trong LND_MACAROON_BASE64.

Bây giờ thêm dòng này vào tệp app.js nằm ở gốc của thư mục làm việc, chúng ta phải sao chép nó vào dòng đầu tiên của tệp.

```
require('dotenv').config();
```

Để xác minh rằng nodejs có thể kết nối với nút của chúng ta, mở tệp routes/index.js, tệp routes này được tạo bởi express generator, đầu tiên chúng ta yêu cầu thư viện ln-service, vì vậy chúng ta thêm nó vào dòng đầu tiên

```
const lnservice = require('ln-service');
```

Chúng ta thêm một tuyến đường mới sẽ cung cấp cho chúng ta thông tin về nút của chúng ta.

```
router.get('/info', async function(req, res, next) {
try {
// xác thực với lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// lấy thông tin nút
const info = await lnservice.getWalletInfo({ lnd });

    // hiển thị thông tin dưới dạng json
    res.send(`
      <h1>Thông tin Nút</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Bây giờ hãy truy cập địa chỉ này http://localhost:3000/info

Nếu bạn thấy một json với thông tin của nút LND, xin chúc mừng!!! ứng dụng của bạn giờ đây có thể tương tác với Mạng Lưới Lightning.
Tạo một mô hình giả

Để mô phỏng một cơ sở dữ liệu, chúng ta cần tạo một mô hình giả, điều này sẽ cho phép chúng ta sử dụng ứng dụng mà không cần cài đặt và cấu hình cơ sở dữ liệu.

Đầu tiên, cài đặt gói uuid

```
$ npm install uuid
```

Tạo thư mục models và bên trong đó, tạo tệp Post.js với nội dung sau:

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
    res.status(500).json({ success: false, error: 'Lỗi máy chủ' });
  }
});

module.exports = router;
```

## Chuẩn bị giao diện

Chúng ta cần bootstrap để làm cho html của mình trông đẹp hơn, vì vậy chúng ta chỉnh sửa tệp layout.pug nằm trong thư mục views để trông như sau:

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

## Tạo một Bài Viết

Để tạo một bài viết, chúng ta cần một biểu mẫu. Trong thư mục views, tạo một tệp gọi là form.pug với nội dung sau:

```
.collapse#post-form
  form
    h2 Viết một bài báo
    .form-group
      label(for="name") Tên
      input(id="name").form-control
    .form-group
      label(for="content") Nội dung
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Gửi
```

## Javascript ở phía frontend

Cách trực tiếp nhất chúng ta có để tương tác với người dùng là sử dụng javascript trong trình duyệt web. Để làm điều này, tạo một tệp gọi là main.js trong thư mục javascript, mà chúng ta đã gọi từ layout.pug. Trong tệp này, khởi tạo dự án. Nội dung ban đầu của main.js như sau:

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

Nhấn nút "Gửi" và nếu mọi thứ ổn, nó sẽ hiển thị một thông báo "!hola" trong console. Bây giờ chúng ta có thể chỉnh sửa phương thức App.sendBtn() để gửi thông tin đến API của chúng ta.

```
App.sendBtn = async () => {
  const name = $('#name').val();
  const content = $('#content').val();
  const response = await App.makeRequest({
    api: "post",
    post: { name, content },
  });
  if (!response) console.error('Lỗi khi lấy dữ liệu!');
  if (response.success) {
    // Làm gì đó với phản hồi
  }
};
```

```markdown
// In dữ liệu đến từ API ra console
console.log(response.data);
}
};
```

Chúng ta cũng tạo phương thức App.makeRequest() và thêm nó vào main.js

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

## Tạo API

Để làm điều này, chúng ta cần tạo một tệp mới trong routes/api.js và viết phương thức phản hồi cho yêu cầu được thực hiện trong App.sendBtn().

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

Tệp này phải được bao gồm trong app.js, vì vậy chúng ta thêm các dòng sau:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Hãy nhấn nút gửi lại và nó sẽ phản hồi với cùng dữ liệu mà chúng ta đã nhập vào form.

## Tạo hóa đơn

Phương thức được thực thi khi người dùng tạo một bài viết nên tạo một hóa đơn, sau đó tạo một bản ghi trong cơ sở dữ liệu liên kết nó với hóa đơn, và trả lại hóa đơn cho người dùng để họ có thể thanh toán.

```markdown
router.post('/post', async (req, res) => {
// Xác thực với lnd
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

Nếu chúng ta nhận được một đối tượng bài viết như phản hồi sau khi nhấn gửi, như thế này, mọi thứ đã diễn ra đúng đắn. Bây giờ chúng ta cần hiển thị văn bản để người dùng có thể thanh toán.

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

## Giao diện hóa đơn mới

Trong thư mục views, chúng ta cần tạo một tệp gọi là invoice.pug với nội dung sau:

```
.collapse#invoice-form
form
.h2 Thanh toán hóa đơn này
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Và bao gồm nó trong index.pug

```
extends layout

block content
h1 Ứng dụng Lightning
include form.pug
include invoice.pug
```

## Chỉnh sửa App.sendBtn()

Bây giờ chúng ta chỉnh sửa App.sendBtn() để hiển thị dữ liệu đã nhận được:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Lỗi khi lấy dữ liệu!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Nhận thanh toán
Chúng ta cần biết khi nào chúng ta nhận được thanh toán, để làm điều này chúng ta sẽ sử dụng phương thức `subscribeToInvoices()` từ `lnservice`, phương thức này cho phép chúng ta thực thi mã khi trạng thái của một hóa đơn đã được cập nhật, để sử dụng nó chúng ta thêm những dòng sau vào `app.js`.

```
// yêu cầu lnservice và bảng post của chúng ta
const lnservice = require('ln-service');
const post = require('./models/Post');

// xác thực với lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

// kiểm tra xem hóa đơn đã được thanh toán mỗi khi một hóa đơn được cập nhật
const subscribeInvoices = async () => {
try {
const sub = lnservice.subscribeToInvoices({lnd});
sub.on('invoice_updated', async invoice => {
if (!invoice.is_confirmed) return;

      // đánh dấu hóa đơn là 'đã thanh toán'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Hóa đơn đã thanh toán!');
    });

} catch (e) {
console.log(e);
return e;
}
};
// bắt đầu đăng ký hóa đơn
subscribeInvoices();
```

Tạo một phương thức HTTP GET trong API của chúng ta để người dùng kiểm tra xem một hash đã được thanh toán hay chưa.

````
router.get('/post/:hash', (req, res) => {
const { hash } = req.params;
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

Bây giờ, từ `main.js`, chúng ta tạo một hàm gọi là `App.waitPayment()` để truy vấn API nếu thanh toán đã được thực hiện.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Thanh toán đã được thực hiện");
  }
};
```

Bây giờ chúng ta gặp một vấn đề, hàm `App.waitPayment()` chỉ được thực thi một lần, người dùng có thể đã thực hiện thanh toán và chúng ta không thể chỉ ra rằng thanh toán của họ đã được nhận. Để làm điều này, chúng ta sử dụng một hàm JavaScript gọi là `setInterval()` cho phép chúng ta thực thi một hàm vô thời hạn tại khoảng thời gian mà chúng ta đã chỉ định.

Hãy chỉnh sửa các hàm `App.waitPayment()` và `App.sendBtn()` bao gồm `setInterval()` và `clearInterval()`

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
  if (!response) console.error("Lỗi khi lấy dữ liệu!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Và chúng tôi tạo một giao diện để chỉ ra rằng việc thanh toán đã được nhận thành công, chúng tôi tạo file success.pug trong thư mục views với nội dung sau:
```pug
.collapse#success
  h2 Thanh toán thành công
  div Bằng chứng thanh toán:
    #preimage
```

Chúng tôi bao gồm nó trong index.pug.

```pug
extends layout

block content
  h1 Ứng dụng Lightning
  include form.pug
  include invoice.pug
  include success.pug
```

Nếu sau khi thanh toán hóa đơn bạn có thể thấy thông điệp "Thanh toán thành công" và bằng chứng thanh toán, xin chúc mừng!!! bạn đã làm được, bạn đã hoàn thành ứng dụng LApp đầu tiên của mình.