---
name: RGB CLI
description: Bagaimana cara membuat dan menukar kontrak pintar di RGB?
---
![cover](assets/cover.webp)

Dalam tutorial ini, kita akan mengikuti proses langkah demi langkah dalam menulis kontrak, menggunakan alat bantu baris perintah `rgb` yang dibuat oleh asosiasi LNP/BP. Tujuannya adalah untuk menunjukkan cara menginstal dan memanipulasi CLI, mengkompilasi Skema, mengimpor Antarmuka dan Implementasi Antarmuka, dan kemudian mengeluarkan aset RGB. Kita juga akan melihat logika yang mendasarinya, termasuk kompilasi dan validasi state. Di akhir tutorial ini, Anda akan dapat mereproduksi proses tersebut dan membuat kontrak RGB Anda sendiri.

## Pengingat protokol RGB

RGB adalah sebuah protokol yang berjalan di atas Bitcoin dan meniru fungsionalitas smart contract dan manajemen aset digital, tanpa membebani blockchain yang menjadi basisnya. Tidak seperti smart contract on-chain konvensional (seperti pada Ethereum, misalnya), RGB bergantung pada sistem "*Validasi sisi klien*": sebagian besar data dan riwayat status dipertukarkan dan disimpan secara eksklusif oleh para partisipan yang terlibat, sedangkan blockchain Bitcoin hanya menyimpan komitmen kriptografi kecil (melalui mekanisme seperti *Tapret* atau *Opret*). Dalam protokol RGB, blockchain Bitcoin hanya berfungsi sebagai server pencatat waktu dan sistem proteksi pembelanjaan ganda.

Kontrak RGB terstruktur seperti mesin status evolusioner. Dimulai dengan Genesis yang mendefinisikan keadaan awal (menggambarkan, misalnya, pasokan, ticker, atau metadata lainnya) menurut Skema yang diketik dan dikompilasi secara ketat. State Transitions dan, jika perlu, State Extensions kemudian diterapkan untuk memodifikasi atau memperluas state ini. Setiap operasi, baik mentransfer aset yang dapat dipertukarkan (RGB20) atau membuat aset unik (RGB21), melibatkan *Segel Sekali Pakai*. Segel ini menghubungkan UTXO Bitcoin ke state off-chain dan mencegah pengeluaran ganda, sekaligus memastikan kerahasiaan dan skalabilitas.

Untuk mempelajari lebih lanjut mengenai cara kerja protokol RGB, saya sarankan Anda mengikuti kursus pelatihan komprehensif ini:

https://planb.network/courses/csv402
Logika internal RGB didasarkan pada pustaka Rust yang dapat Anda, sebagai pengembang, impor ke dalam proyek Anda untuk mengelola bagian *Client-side Validation*. Selain itu, tim LNP/BP sedang mengerjakan binding untuk bahasa lain, tetapi ini belum selesai. Selain itu, entitas lain seperti Bitfinex sedang mengembangkan tumpukan integrasi mereka sendiri, tetapi kita akan membicarakannya di tutorial lain. Untuk saat ini, CLI `rgb` adalah referensi resmi, meskipun masih relatif belum sempurna.

## Instalasi dan presentasi alat bantu CLI rgb

Perintah utamanya hanya disebut `rgb`. Perintah ini didesain untuk mengingatkan kita pada `git`, dengan serangkaian sub-perintah untuk memanipulasi kontrak, memintanya, menerbitkan aset, dan sebagainya. Dompet Bitcoin saat ini belum terintegrasi, namun akan segera hadir dalam versi berikutnya (0.11). Versi berikutnya ini akan memungkinkan pengguna untuk membuat dan mengelola dompet mereka (melalui deskriptor) secara langsung dari `rgb`, termasuk pembuatan PSBT, kompatibilitas dengan perangkat keras eksternal (mis. Dompet perangkat keras) untuk penandatanganan, dan interoperabilitas dengan perangkat lunak seperti Sparrow. Ini akan menyederhanakan seluruh skenario penerbitan dan transfer aset.

### Pemasangan melalui Kargo

Kami memasang alat ini di Karat dengan :

```bash
cargo install rgb-contracts --all-features
```

(Catatan: crate bernama `rgb-contracts`, dan perintah yang terinstal akan diberi nama `rgb`. Jika sebuah peti bernama `rgb` sudah ada, mungkin telah terjadi tabrakan, oleh karena itu namanya)

Instalasi mengkompilasi sejumlah besar dependensi (misalnya penguraian perintah, integrasi Electrum, manajemen bukti tanpa pengetahuan, dll.).

Setelah instalasi selesai, file :

```bash
rgb
```

Menjalankan `rgb` (tanpa argumen) akan menampilkan daftar sub-perintah yang tersedia, seperti `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, dan lain-lain. Anda dapat mengubah direktori penyimpanan lokal (tempat penyimpanan yang menyimpan semua log, skema dan implementasi), memilih jaringan (testnet, mainnet) atau mengkonfigurasi server Electrum Anda.

![RGB-CLI](assets/fr/01.webp)

### Gambaran umum pertama tentang kontrol

Apabila Anda menjalankan perintah berikut ini, Anda akan melihat bahwa antarmuka `RGB20` sudah terintegrasi secara default:

```bash
rgb interfaces
```

Jika antarmuka ini tidak terintegrasi, kloning file :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompilasi itu:

```bash
cargo run
```

Kemudian, impor antarmuka pilihan Anda:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Namun, kami diberitahu bahwa belum ada skema yang diimpor ke dalam perangkat lunak. Juga tidak ada kontrak dalam simpanan. Untuk melihatnya, jalankan perintah :

```bash
rgb schemata
```

Anda kemudian dapat mengkloning repositori untuk mengambil skema tertentu:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Repositori ini berisi, dalam direktori `src/`, beberapa file Rust (misalnya `nia.rs`) yang mendefinisikan skema (NIA untuk "*Non Inflatable Asset*", UDA untuk "*Unique Digital Asset*", dll.). Untuk mengkompilasi, Anda kemudian dapat menjalankan file :

```bash
cd rgb-schemata
cargo run
```

Ini menghasilkan beberapa file `.rgb` dan `.rgba` yang sesuai dengan skema yang dikompilasi. Sebagai contoh, Anda akan menemukan `NonInflatableAsset.rgb`.

### Mengimpor Skema dan Implementasi Antarmuka

Anda sekarang dapat mengimpor skematik ke dalam `rgb`:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Ini akan menambahkannya ke simpanan lokal. Jika kita menjalankan perintah berikut, kita akan melihat bahwa skemanya sekarang muncul:

```bash
rgb schemata
```

## Pembuatan kontrak (penerbitan)

Ada dua pendekatan untuk membuat aset baru:


- Entah kita menggunakan skrip atau kode di Rust yang membangun Kontrak dengan mengisi bidang skema (negara global, Negara Milik, dll.) dan menghasilkan file `.rgb` atau `.rgba`;
- Atau gunakan sub-perintah `issue` secara langsung, dengan file YAML (atau TOML) yang menjelaskan properti token.

Anda dapat menemukan contoh di Rust dalam folder `examples`, yang mengilustrasikan bagaimana Anda membuat `ContractBuilder`, mengisi `global state` (nama aset, ticker, pasokan, tanggal, dll.), menentukan Owned State (ke mana UTXO ditugaskan), kemudian mengkompilasi semua ini menjadi *contract consignment* yang dapat Anda ekspor, validasi, dan impor ke dalam simpanan.

Cara lainnya adalah mengedit file YAML secara manual untuk menyesuaikan `ticker`, `nama`, `supply`, dan seterusnya. Misalkan file tersebut bernama `RGB20-demo.yaml`. Anda dapat menentukan ekstensi :


- `spec`: ticker, nama, presisi ;
- 'istilah': bidang untuk pemberitahuan hukum ;
- `issuedSupply`: jumlah token yang diterbitkan;
- 'assignments': menunjukkan Segel Sekali Pakai (*definisi segel*) dan jumlah yang dibuka.

Berikut ini adalah contoh file YAML yang akan dibuat:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Kemudian, jalankan saja perintah :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

Dalam kasus saya, pengenal skema unik (harus diapit dengan tanda kutip tunggal) adalah `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` dan saya tidak mencantumkan penerbit apa pun. Jadi pesanan saya adalah :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Jika Anda tidak mengetahui ID skema, jalankan perintah :

```bash
rgb schemata
```

CLI menjawab bahwa sebuah kontrak baru telah diterbitkan dan ditambahkan ke dalam simpanan. Jika kita mengetikkan perintah berikut, kita akan melihat bahwa sekarang ada sebuah kontrak tambahan, yang sesuai dengan kontrak yang baru saja diterbitkan:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Kemudian, perintah selanjutnya menampilkan status global (nama, ticker, pasokan...) dan daftar Status Milik, yaitu alokasi (misalnya, 1 juta token `PBN` yang didefinisikan dalam UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Ekspor, impor, dan validasi

Untuk berbagi kontrak ini dengan pengguna lain, kontrak ini dapat diekspor dari simpanan ke file :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

File `myContractPBN.rgb` dapat diteruskan ke pengguna lain, yang dapat menambahkannya ke simpanannya dengan perintah :

```bash
rgb import myContractPBN.rgb
```

Pada saat impor, jika ini adalah *kiriman kontrak* yang sederhana, kita akan mendapatkan pesan "`Importing consignment rgb`". Jika ini adalah *state transition consignment* yang lebih besar, perintahnya akan berbeda (`rgb accept`).

Untuk memastikan validitas, Anda juga dapat menggunakan fungsi validasi lokal. Misalnya, Anda dapat menjalankan :

```bash
rgb validate myContract.rgb
```

### Penggunaan, verifikasi, dan tampilan simpanan

Sebagai pengingat, stash adalah inventaris lokal dari skema, antarmuka, implementasi, dan kontrak (Genesis + transisi). Setiap kali Anda menjalankan "impor", Anda menambahkan sebuah elemen ke dalam stash. Stash ini dapat dilihat secara detail dengan perintah :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Ini akan menghasilkan folder dengan rincian seluruh simpanan.

## Transfer dan PSBT

Untuk melakukan transfer, Anda perlu memanipulasi dompet Bitcoin lokal untuk mengelola komitmen `Tapret` atau `Opret`.

### Membuat faktur

Dalam banyak kasus, interaksi antara peserta dalam kontrak (misalnya Alice dan Bob) terjadi melalui pembuatan faktur. Jika Alice ingin Bob melakukan sesuatu (transfer token, penerbitan ulang, tindakan dalam DAO, dll.), Alice membuat faktur yang merinci instruksinya kepada Bob. Jadi, kita memiliki :


- Alice** (penerbit faktur);
- Bob** (yang menerima dan melaksanakan faktur).

Tidak seperti ekosistem lainnya, faktur RGB tidak terbatas pada pengertian pembayaran. Faktur ini dapat menyematkan permintaan apa pun yang terkait dengan kontrak: mencabut kunci, memberikan suara, membuat ukiran (*engraving*) pada NFT, dll. Operasi yang sesuai dapat dijelaskan dalam antarmuka kontrak. Operasi yang sesuai dapat dijelaskan dalam antarmuka kontrak.

Perintah berikut ini menghasilkan faktur RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Dengan:


- `$KONTRAK`: Pengenal kontrak (*ContractId*) ;
- `$INTERFACE`: antarmuka yang akan digunakan (mis. `RGB20`);
- `$ACTION`: nama operasi yang ditentukan dalam antarmuka (untuk transfer token yang dapat dipertukarkan, ini bisa berupa "Transfer"). Jika antarmuka sudah menyediakan tindakan default, Anda tidak perlu memasukkannya lagi di sini;
- `$STATE`: data status yang akan ditransfer (misalnya, jumlah token jika token yang dapat ditukar ditransfer);
- `$SEAL`: Segel sekali pakai penerima (Alice), yaitu referensi eksplisit ke UTXO. Bob akan menggunakan informasi ini untuk membuat transaksi saksi, dan keluaran yang sesuai akan menjadi milik Alice (dalam bentuk *blinded UTXO* atau tidak terenkripsi).

Misalnya, dengan perintah berikut ini

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI akan menghasilkan faktur seperti :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Ini dapat dikirimkan ke Bob melalui saluran apa pun (teks, kode QR, dll.).

### Melakukan transfer

Untuk mentransfer dari faktur ini :


- Bob (yang menyimpan token dalam simpanannya) memiliki dompet Bitcoin. Dia perlu menyiapkan transaksi Bitcoin (dalam bentuk PSBT, misalnya `tx.psbt`) yang membelanjakan UTXO di mana token RGB yang diperlukan berada, ditambah satu UTXO untuk mata uang (penukaran);
- Bob menjalankan perintah berikut:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Ini menghasilkan file `konsinyasi.rgb` yang berisi file :
 - Riwayat transisi membuktikan kepada Alice bahwa token tersebut asli;
 - Transisi baru yang mentransfer token ke Segel Sekali Pakai Alice;
 - Transaksi saksi (tidak ditandatangani).
- Bob mengirimkan file `consignment.rgb` ini ke Alice (melalui email, server berbagi atau protokol RGB-RPC, Storm, dll.);
- Alice menerima `kiriman.rgb` dan menerimanya dalam simpanannya sendiri:

```bash
alice$ rgb accept consignment.rgb
```


- CLI memeriksa validitas transisi dan menambahkannya ke simpanan Alice. Jika tidak valid, perintah akan gagal dengan pesan kesalahan yang mendetail. Jika tidak, perintah tersebut berhasil, dan melaporkan bahwa contoh transaksi belum disiarkan di jaringan Bitcoin (Bob menunggu lampu hijau dari Alice);
- Sebagai konfirmasi, perintah `accept` mengembalikan tanda tangan (*payslip*) yang dapat dikirimkan Alice kepada Bob untuk menunjukkan kepadanya bahwa dia telah memvalidasi *kiriman*;
- Bob kemudian dapat menandatangani dan mempublikasikan (`-publish`) transaksi Bitcoin-nya:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Segera setelah transaksi ini dikonfirmasi secara on-chain, kepemilikan aset dianggap berpindah ke Alice. Dompet Alice, yang memantau penambangan transaksi, melihat Status Milik baru muncul di simpanannya.

Sekarang Anda sudah tahu cara menerbitkan dan mentransfer kontrak RGB. Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain di mana saya menjelaskan cara meluncurkan node Lightning yang kompatibel dengan RGB untuk menukar token secara instan:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea