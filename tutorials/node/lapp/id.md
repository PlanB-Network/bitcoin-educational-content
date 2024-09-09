---
name: LAPP bitcoin
description: Tutorial untuk mengembangkan LApp pertama Anda
---

Belajar untuk mengkodekan aplikasi lightning pertama Anda

Persyaratan:

- NodeJs >= 8
- LND >= 9

NodeJs dapat diunduh dari situs web resminya

Alih-alih mengunduh dan menyiapkan node LND, kita akan menggunakan alat polar, yang akan melakukan tugas ini untuk kita.

Untuk membangun aplikasi Lightning kita, kita akan menggunakan teknologi berikut:

- Express untuk webserver kita
- Template Pug + bootstrap untuk frontend kita

## Sistem Operasi

Disarankan untuk menggunakan Linux, jika Anda menggunakan Windows 10, Anda dapat memiliki konsol Linux dengan mengikuti beberapa langkah ini.
Menyiapkan dasar

Gunakan alat generator aplikasi, express, untuk dengan cepat membuat kerangka aplikasi.

```
$ sudo npm install express-generator -g
```

Dengan instruksi berikut, kita membuat aplikasi Express yang disebut lnapp. Aplikasi akan dibuat dalam direktori yang disebut lnapp di direktori kerja saat ini, dan mesin tampilan akan ditetapkan ke Pug.

```
$ express --view=pug lnapp
```

Kemudian kita masuk ke direktori dan menginstal paket yang diperlukan agar web server dapat berjalan.

```
$ cd myapp
$ npm install
```

Sekarang kita cukup menjalankan server

```
$ npm start
```

Selanjutnya, buka alamat ini http://localhost:3000 di browser untuk mengakses aplikasi.

Aplikasi yang dihasilkan memiliki struktur direktori sebagai berikut:

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

Unduh Polar, instal, dan buat jaringan dengan 2 node LND (Alice dan Bob) dan 1 bitcoind. Setelah kita melihat grafik di aplikasi yang menunjukkan node kita, klik tombol Start dan tunggu beberapa detik sampai indikator setiap node berubah warna menjadi hijau.

Untuk mengirim pembayaran di Lightning, diperlukan agar node terhubung melalui saluran. Membuat saluran dengan Polar sangat sederhana, kita hanya perlu mengklik dengan mouse pada salah satu telinga node Alice dan menyeretnya ke salah satu telinga node Bob. Segera, jendela modal bertajuk Open new channel harus muncul, kita biarkan nilai default dan tekan tombol buka saluran. Sekarang kita ulangi aksi tetapi kali ini dari Bob ke Alice, dengan cara ini kedua node dapat mengirim dan menerima uang.

## Nodemon

Untuk menghindari harus memulai ulang nodejs setiap kali kita membuat perubahan dalam kode, kita akan menginstal nodemon

```
$ npm install nodemon -D
```

Kita harus membuat entri di bagian skrip dari file package.json, tambahkan baris ini "dev": "nodemon ./bin/www", bagian skrip harus terlihat seperti ini:

```
"scripts": {
"start": "node ./bin/www",
"dev": "nodemon ./bin/www"
},
```

Pergi ke konsol di mana npm start sedang berjalan, tekan ctrl + c dan mulai nodejs lagi tetapi kali ini menggunakan nodemon

```
$ npm run dev
```

## Menghubungkan ke LND

Untuk terhubung ke node Lightning dari nodejs, kita akan menggunakan perpustakaan ln-service, kita juga akan menginstal dotenv untuk mengelola variabel lingkungan.

```
$ npm install ln-service dotenv
Di direktori lnapp kita, buatlah sebuah file bernama .env, file tersebut harus mengandung variabel-variabel berikut:

```
LND_GRPC_HOST=''
LND_CERT_BASE64=''
LND_MACAROON_BASE64=''
```

Kembali ke Polar, pilih Bob, node yang ingin kita sambungkan, pergi ke tab "Connect", salin isi dari GRPC Host dan tempatkan pada variabel LND_GRPC_HOST, di bagian bawah tab connect pilih base64 dan salin isi dari TLS Cert dan tempatkan pada variabel LND_CERT_BASE64, dan lakukan hal yang sama dengan admin macaroon pada LND_MACAROON_BASE64.

Sekarang tambahkan baris ini ke file app.js yang terletak di root direktori kerja, kita harus menyalinnya pada baris pertama file tersebut.

```
require('dotenv').config();
```

Untuk memverifikasi bahwa nodejs dapat terhubung ke node kita, buka file routes/index.js, file routes ini dibuat oleh generator express, pertama kita memerlukan library ln-service, jadi kita tambahkan di baris pertama

```
const lnservice = require('ln-service');
```

Kita menambahkan rute baru yang akan memberi kita informasi tentang node kita.

```
router.get('/info', async function(req, res, next) {
try {
// autentikasi dengan lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});
// mendapatkan informasi node
const info = await lnservice.getWalletInfo({ lnd });

    // menampilkan info dalam format json
    res.send(`
      <h1>Info Node</h1>
      <pre>${JSON.stringify(info, null, 2)}</pre>
    `);
    next();

} catch (e) {
console.log(e);
}
});
```

Sekarang pergi ke alamat ini http://localhost:3000/info

Jika Anda melihat json dengan informasi dari node LND, selamat!!! aplikasi Anda sekarang dapat berinteraksi dengan Lightning Network.
Membuat model palsu

Untuk mensimulasikan database, kita perlu membuat model palsu, ini akan memungkinkan kita untuk menggunakan aplikasi tanpa perlu menginstal dan mengonfigurasi database.

Pertama, instal paket uuid

```
$ npm install uuid
```

Buat direktori models dan di dalamnya, buat file Post.js dengan konten berikut:

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
updatedPost = { ...p, paid: true };        return updatedPost;
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

## Persiapkan tampilan

Kita memerlukan bootstrap untuk membuat tampilan html kita lebih baik, jadi kita modifikasi file layout.pug yang berada di direktori views agar terlihat seperti ini:

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

## Membuat sebuah Post

Untuk membuat sebuah post, kita memerlukan sebuah form. Di dalam direktori views, buatlah sebuah file bernama form.pug dengan konten berikut:

```
.collapse#post-form
  form
    h2 Tulis sebuah artikel
    .form-group
      label(for="name") Nama
      input(id="name").form-control
    .form-group
      label(for="content") Konten
      textarea(id="content").form-control
    button.btn.btn-primary#send-btn(type="button") Kirim
```

## Javascript di frontend

Cara paling langsung yang kita miliki untuk berinteraksi dengan pengguna adalah dengan menggunakan javascript di web browser. Untuk ini, buatlah sebuah file bernama main.js di direktori javascript, yang sudah kita panggil dari layout.pug. Di dalam file ini, inisialisasilah proyek. Konten awal dari main.js adalah sebagai berikut:

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

Klik tombol "Kirim" dan jika semuanya baik, seharusnya akan menampilkan pesan "!hola" di konsol. Sekarang kita dapat memodifikasi metode App.sendBtn() untuk mengirim informasi ke API kita.

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
    // Lakukan sesuatu dengan respons
  }
};
```

```markdown
// Cetak data yang datang dari API ke konsol
console.log(response.data);
}
};
```

Kita juga membuat metode App.makeRequest() dan menambahkannya ke main.js

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

## Membuat API

Untuk melakukan ini, kita perlu membuat sebuah file baru di routes/api.js dan menulis metode yang merespons permintaan yang dibuat dalam App.sendBtn().

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

File ini harus disertakan dalam app.js, jadi kita tambahkan baris-baris ini:

```markdown
const apiRouter = require('./routes/api');
app.use('/api', apiRouter);
```

Mari kita tekan tombol kirim lagi dan seharusnya akan merespons dengan data yang sama yang kita masukkan dalam formulir.

## Membuat invoice

Metode yang dieksekusi ketika pengguna membuat post harus menghasilkan invoice, kemudian membuat catatan dalam database yang menghubungkannya dengan invoice, dan mengembalikan invoice kepada pengguna agar mereka dapat membayarnya.

```markdown
router.post('/post', async (req, res) => {
// Otentikasi dengan lnd
const { lnd } = lnservice.authenticatedLndGrpc({
cert: process.env.LND_CERT_BASE64,
macaroon: process.env.LND_MACAROON_BASE64,
socket: process.env.LND_GRPC_HOST,
});

const { name, content } = req.body;
coba {
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

Jika kita menerima objek post sebagai respons setelah menekan kirim, seperti ini, semuanya telah berjalan dengan benar. Sekarang kita perlu menampilkan teks agar pengguna dapat membayarnya.

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

## Tampilan invoice baru

Di direktori views, kita perlu membuat file yang disebut invoice.pug dengan konten berikut:

```
.collapse#invoice-form
form
.h2 Bayar invoice ini
.form-group
textarea(
id="invoice",
readonly,
rows="5"
).form-control
```

Dan sertakan dalam index.pug

```
extends layout

block content
h1 Aplikasi Lightning
include form.pug
include invoice.pug
```

## Memodifikasi App.sendBtn()

Sekarang kita modifikasi App.sendBtn() untuk menampilkan data yang diperoleh:

```
App.sendBtn = async () => {
const name = $('#name').val();
const content = $('#content').val();
const response = await App.makeRequest({
api: "post",
post: { name, content },
});
if (!response) console.error('Kesalahan mendapatkan data!');
if (response.success) {
$('#post-form').collapse('hide');
$('#invoice-form').collapse('show');
$('#invoice').val(response.data.request);
}
};
```

## Menerima pembayaran
Kita perlu mengetahui kapan kita menerima pembayaran, untuk ini kita akan menggunakan metode `subscribeToInvoices()` dari `lnservice`, metode ini memungkinkan kita untuk menjalankan kode ketika status sebuah invoice telah diperbarui, untuk menggunakannya kita tambahkan baris-baris ini di `app.js`.

```
// memerlukan lnservice dan tabel post kita
const lnservice = require('ln-service');
const post = require('./models/Post');

// otentikasi dengan lnd
const { lnd } = lnservice.authenticatedLndGrpc({
  cert: process.env.LND_CERT_BASE64,
  macaroon: process.env.LND_MACAROON_BASE64,
  socket: process.env.LND_GRPC_HOST,
});

// periksa apakah invoice telah dibayar setiap kali sebuah invoice diperbarui
const subscribeInvoices = async () => {
  try {
    const sub = lnservice.subscribeToInvoices({lnd});
    sub.on('invoice_updated', async invoice => {
      if (!invoice.is_confirmed) return;

      // tandai invoice sebagai 'dibayar'
      const paid = post.paid(invoice.id);
      if (paid) console.log('Invoice dibayar!');
    });

  } catch (e) {
    console.log(e);
    return e;
  }
};
// mulai langganan invoice
subscribeInvoices();
```

Buat metode HTTP GET dalam API kita agar pengguna dapat memeriksa apakah sebuah hash telah dibayar.

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

Sekarang, dari `main.js`, kita membuat fungsi yang disebut `App.waitPayment()` yang menanyakan API jika pembayaran telah dilakukan.

```javascript
App.waitPayment = async (hash) => {
  const response = await App.makeRequest({
    api: `post/${hash}`,
  });
  if (response.success && response.data.paid) {
    console.log("Pembayaran dilakukan");
  }
};
```

Sekarang kita menghadapi masalah, fungsi `App.waitPayment()` hanya dijalankan sekali, pengguna mungkin telah melakukan pembayaran dan kita belum dapat menunjukkan bahwa pembayaran mereka telah diterima. Untuk ini, kita menggunakan fungsi JavaScript yang disebut `setInterval()` yang memungkinkan kita untuk menjalankan fungsi secara tak terbatas pada interval waktu yang telah kita tentukan.

Mari kita modifikasi fungsi `App.waitPayment()` dan `App.sendBtn()` termasuk `setInterval()` dan `clearInterval()`

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
  if (!response) console.error("Kesalahan mendapatkan data!");
  if (response.success) {
    $("#post-form").collapse("hide");
    $("#invoice-form").collapse("show");
    $("#invoice").val(response.data.request);
    App.interval = setInterval(App.waitPayment, 1000, response.data.hash);
  }
};
```
Dan kami membuat sebuah tampilan untuk menunjukkan bahwa pembayaran telah berhasil diterima, kami membuat file success.pug di views dengan konten berikut:
```pug
.collapse#success
  h2 Pembayaran berhasil
  div Bukti pembayaran:
    #preimage
```

Kami memasukkannya dalam index.pug.

```pug
extends layout

block content
  h1 Aplikasi Lightning
  include form.pug
  include invoice.pug
  include success.pug
```

Jika setelah membayar faktur Anda dapat melihat pesan "Pembayaran berhasil" dan bukti pembayaran, selamat!!! Anda berhasil, Anda telah menyelesaikan LApp pertama Anda.