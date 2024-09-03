---
name: RGB
description: Pengenalan dan pembuatan aset pada RGB
---

![RGB vs Ethereum](assets/0.webp)

## Pengenalan

Pada tanggal 3 Januari 2009, Satoshi Nakamoto meluncurkan node Bitcoin pertama, dari saat itu node baru bergabung dan Bitcoin mulai berperilaku seolah-olah itu adalah bentuk kehidupan baru, bentuk kehidupan yang tidak pernah berhenti berkembang, sedikit demi sedikit menjadi jaringan paling aman di dunia sebagai hasil dari desain uniknya, yang sangat dipikirkan dengan baik oleh Satoshi karena, melalui insentif ekonomi, itu menarik pengguna yang biasa disebut penambang untuk berinvestasi dalam energi dan kekuatan komputasi yang berkontribusi pada keamanan jaringan.

Seiring dengan pertumbuhan dan adopsi Bitcoin, ia menghadapi masalah skalabilitas, jaringan Bitcoin memungkinkan blok baru dengan transaksi untuk ditambang dalam waktu sekitar 10 menit, dengan asumsi kita memiliki 144 blok dalam sehari dengan nilai maksimum 2700 transaksi per blok, Bitcoin hanya akan memungkinkan 4,5 transaksi per detik, Satoshi menyadari keterbatasan ini, kita dapat melihatnya dalam email yang dikirim kepada Mike Hearn pada Maret 2011 di mana dia menjelaskan bagaimana apa yang kita kenal hari ini sebagai saluran pembayaran bekerja. mikropembayaran dengan cepat dan aman tanpa menunggu konfirmasi. Inilah di mana protokol off-chain masuk.

Menurut Christian Decker, protokol off-chain biasanya adalah sistem di mana pengguna menggunakan data dari blockchain dan mengelolanya tanpa menyentuh blockchain itu sendiri sampai menit terakhir. Berdasarkan konsep ini, Lightning Network lahir, sebuah jaringan yang menggunakan protokol off-chain untuk memungkinkan pembayaran Bitcoin dilakukan hampir secara instan dan karena tidak semua operasi ini ditulis di blockchain, itu memungkinkan ribuan transaksi per detik dan skala Bitcoin.

Penelitian dan pengembangan di area protokol off-chain pada Bitcoin telah membuka kotak pandora, hari ini kita tahu bahwa kita dapat mencapai lebih banyak daripada transfer nilai secara terdesentralisasi, asosiasi nirlaba LNP/BP Standards Association fokus pada pengembangan protokol lapis 2 dan 3 pada Bitcoin dan Lightning Network, di antara proyek-proyek ini RGB menonjol.

## Apa itu RGB?

RGB muncul dari penelitian oleh Peter Todd tentang single-use-seals dan client-side-validation, yang dicetuskan pada tahun 2016-2019 oleh Giacomo Zucco dan komunitas menjadi protokol aset yang lebih baik untuk Bitcoin dan Lightning network. Evolusi lebih lanjut dari ide-ide ini mengarah pada pengembangan RGB menjadi sistem kontrak pintar yang lengkap oleh Maxim Orlovsky, yang memimpin implementasinya sejak 2019 dengan partisipasi komunitas.

Kita dapat mendefinisikan RGB sebagai seperangkat protokol sumber terbuka yang memungkinkan kita untuk menjalankan kontrak pintar yang kompleks secara skalabel dan rahasia. Ini bukan jaringan tertentu (seperti Bitcoin atau Lightning); setiap kontrak pintar hanyalah seperangkat peserta kontrak yang dapat berinteraksi menggunakan saluran komunikasi yang berbeda (default ke Lightning network). RGB menggunakan blockchain Bitcoin sebagai lapisan komitmen status dan mempertahankan kode kontrak pintar dan data off-chain, yang membuatnya skalabel, memanfaatkan transaksi Bitcoin (dan Script) sebagai sistem kontrol kepemilikan untuk kontrak pintar; sementara evolusi kontrak pintar didefinisikan oleh skema off-chain, akhirnya penting untuk dicatat bahwa semuanya divalidasi di sisi klien.

Dengan kata sederhana, RGB adalah sistem yang memungkinkan pengguna untuk mengaudit kontrak pintar, menjalankannya, dan memverifikasinya secara individu kapan saja tanpa biaya tambahan karena untuk ini tidak menggunakan blockchain seperti sistem "tradisional" lakukan, sistem kontrak pintar yang kompleks dipelopori oleh Ethereum tetapi karena membutuhkan pengguna untuk menghabiskan jumlah gas yang signifikan untuk setiap operasi, mereka tidak pernah mencapai skalabilitas yang mereka janjikan akibatnya tidak pernah menjadi opsi untuk membankkan pengguna yang dikecualikan dari sistem keuangan saat ini.
Saat ini, industri blockchain mendorong agar baik kode kontrak pintar maupun data harus disimpan dalam blockchain dan dieksekusi oleh setiap node dalam jaringan, terlepas dari peningkatan ukuran yang berlebihan atau penyalahgunaan sumber daya komputasi. Skema yang diusulkan oleh RGB jauh lebih cerdas dan efisien karena memotong paradigma blockchain dengan memiliki kontrak pintar dan data yang dipisahkan dari blockchain dan dengan demikian menghindari kejenuhan jaringan yang terlihat di platform lain, sekaligus tidak memaksa setiap node untuk mengeksekusi setiap kontrak tetapi lebih kepada pihak-pihak yang terlibat yang menambahkan tingkat kerahasiaan yang belum pernah terlihat sebelumnya.
![RGB vs Ethereum](assets/1.webp)

## Kontrak Pintar di RGB

Dalam kontrak pintar RGB, pengembang mendefinisikan skema yang menentukan aturan bagaimana kontrak berkembang seiring waktu. Skema tersebut adalah standar untuk pembangunan kontrak pintar di RGB, dan baik penerbit saat mendefinisikan kontrak untuk penerbitan maupun dompet atau bursa harus mengikuti skema tertentu yang harus mereka validasi terhadap kontrak tersebut. Hanya jika validasi tersebut benar maka setiap pihak dapat menerima permintaan dan bekerja dengan aset tersebut.

Kontrak pintar di RGB adalah grafik acyclic terarah (DAG) dari perubahan status, di mana hanya sebagian dari grafik yang selalu diketahui dan tidak ada akses ke sisanya. Skema RGB adalah seperangkat aturan inti untuk evolusi grafik yang dimulai dengan kontrak pintar tersebut. Setiap peserta kontrak dapat menambahkan aturan tersebut (jika ini diizinkan oleh skema) dan grafik yang dihasilkan dibangun dari aplikasi iteratif dari aturan tersebut.

## Aset Fungible

Aset fungible di RGB mengikuti spesifikasi LNPBP RGB-20, ketika RGB-20 didefinisikan, data aset yang dikenal sebagai "data genesis" didistribusikan melalui jaringan Lightning, yang berisi apa yang diperlukan untuk menggunakan aset tersebut. Bentuk aset paling dasar tidak mengizinkan penerbitan sekunder, pembakaran token, penamaan ulang, atau penggantian.

Terkadang penerbit akan perlu menerbitkan lebih banyak token di masa depan, misalnya stablecoin seperti USDT, yang menjaga nilai setiap token terikat pada nilai mata uang inflasi seperti USD. Untuk mencapai ini skema RGB-20 yang lebih kompleks ada, dan selain data genesis mereka memerlukan penerbit untuk menghasilkan konsinyasi, yang juga akan beredar di jaringan lightning; dengan informasi ini kita dapat mengetahui total pasokan aset yang beredar. Hal yang sama berlaku untuk pembakaran aset, atau mengubah namanya.

Informasi terkait aset dapat bersifat publik atau pribadi: jika penerbit memerlukan kerahasiaan, ia dapat memilih untuk tidak berbagi informasi tentang token dan melakukan operasi dalam privasi mutlak, tetapi kita juga memiliki kasus sebaliknya di mana penerbit dan pemegang memerlukan seluruh proses untuk menjadi transparan. Ini dicapai dengan berbagi data token.

## Prosedur RGB-20

Prosedur pembakaran menonaktifkan token, token yang dibakar tidak dapat digunakan lagi.

Prosedur penggantian terjadi ketika token dibakar dan jumlah baru token yang sama diciptakan. Ini membantu mengurangi ukuran data historis aset, yang penting untuk menjaga kecepatan aset.

Untuk mendukung kasus penggunaan di mana dimungkinkan untuk membakar aset tanpa harus menggantinya, sub-skema RGB-20 digunakan yang hanya memungkinkan pembakaran aset.

## Aset Non Fungible
Aset non-fungible dalam RGB mengikuti spesifikasi LNPBP RGB-21, ketika kita bekerja dengan NFT, kita juga memiliki skema utama dan sub-skema. Skema ini memiliki prosedur pengukiran, yang memungkinkan kita untuk melampirkan data khusus oleh pemilik token, contoh paling umum yang kita lihat dalam NFT saat ini adalah seni digital yang terkait dengan token. Penerbit token dapat melarang pengukiran data ini dengan menggunakan sub-skema RGB-21. Tidak seperti sistem blockchain NFT lainnya, RGB memungkinkan distribusi data media token ukuran besar secara lengkap terdesentralisasi dan tahan sensor, menggunakan ekstensi ke jaringan P2P Lightning yang disebut Bifrost, yang juga digunakan untuk membangun banyak bentuk lain dari fungsi kontrak pintar spesifik RGB.
Selain aset fungible dan NFT, RGB dan Bifrost dapat digunakan untuk menghasilkan bentuk kontrak pintar lainnya, termasuk DEX, kolam likuiditas, koin stabil algoritmik, dll, yang akan kita bahas dalam artikel mendatang.

## NFT dari RGB vs NFT dari platform lain

- Tidak perlu penyimpanan blockchain yang mahal
- Tidak perlu IPFS, sebuah ekstensi jaringan Lightning (disebut Bifrost) digunakan sebagai gantinya (dan sepenuhnya terenkripsi ujung-ke-ujung)
- Tidak perlu solusi manajemen data khusus – lagi, Bifrost mengambil peran itu
- Tidak perlu mempercayai situs web untuk memelihara data untuk token NFT atau tentang aset yang diterbitkan / ABIs kontrak
- Enkripsi DRM bawaan dan manajemen kepemilikan
- Infrastruktur untuk cadangan menggunakan Jaringan Lightning (Bifrost)
- Cara untuk memonetisasi konten (tidak hanya menjual NFT itu sendiri, tetapi akses ke konten, beberapa kali)

## Kesimpulan

Sejak peluncuran Bitcoin, hampir 13 tahun yang lalu telah banyak penelitian dan eksperimen di area ini, baik kesuksesan maupun kesalahan telah memungkinkan kita untuk memahami sedikit lebih banyak bagaimana sistem terdesentralisasi berperilaku dalam praktik, apa yang membuat mereka benar-benar terdesentralisasi dan tindakan apa yang cenderung membawa mereka ke sentralisasi, semua ini telah membawa kita untuk menyimpulkan bahwa desentralisasi sejati adalah fenomena yang langka dan sulit untuk dicapai, desentralisasi sejati hanya telah dicapai oleh Bitcoin dan itulah alasan kami fokus upaya kami untuk membangun di atasnya.

RGB memiliki lubang kelinci sendiri di dalam lubang kelinci Bitcoin, sementara saya terjatuh melalui mereka saya akan memposting apa yang telah saya pelajari, dalam artikel berikutnya kita akan memiliki pengenalan ke node LNP dan RGB dan bagaimana menggunakannya.

# Tutorial RGB-node

## Pengantar

Dalam tutorial ini kami menjelaskan cara menggunakan RGB-node untuk membuat token fungible dan cara mentransfernya, dokumen ini berdasarkan demo RGB-node dan berbeda karena tutorial ini menggunakan data testnet nyata dan untuk itu, kita harus membangun Partially Signed Bitcoin Transaction (psbt) kita sendiri.

## Persyaratan

Penggunaan distribusi Linux direkomendasikan, tutorial ini ditulis menggunakan Pop!OS, yang berbasis pada Ubuntu dan Anda akan memerlukan:

- cargo
- Bitcoin core
- git
Catatan: Tutorial ini menunjukkan eksekusi perintah dalam terminal Linux, untuk membedakan apa yang ditulis pengguna dan respons yang dia dapatkan di terminal, kami menyertakan simbol $ yang melambangkan prompt bash.
Anda perlu menginstal beberapa dependensi:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Bangun & Jalankan

RGB-node masih dalam tahap pengembangan (WIP), itulah sebabnya kita harus menempatkan diri kita pada commit tertentu (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) untuk dapat mengompilasi dan menggunakannya dengan benar, untuk ini kita menjalankan perintah berikut.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Sekarang kita mengompilasinya, jangan lupa menggunakan bendera --locked karena ada perubahan besar yang diperkenalkan pada versi clap.

```
$ cargo install --path . --all-features --locked

....
....
    Selesai rilis [dioptimalkan] target(s) dalam 2m 14s
  Memasang /home/user/.cargo/bin/fungibled
  Memasang /home/user/.cargo/bin/rgb-cli
  Memasang /home/user/.cargo/bin/rgbd
  Memasang /home/user/.cargo/bin/stashd
   Paket terpasang `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (eksekutabel `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Seperti yang dikatakan oleh kompiler rust kepada kita, binari telah disalin ke direktori $HOME/.cargo/bin, jika kompiler Anda menyalinnya ke tempat yang berbeda Anda harus memastikan direktori tersebut harus dimasukkan dalam $PATH.

Di antara binari yang terpasang, kita dapat melihat tiga daemon atau layanan (file yang berakhir dengan d) dan sebuah cli (antarmuka baris perintah), cli memungkinkan kita untuk berinteraksi dengan daemon rgbd utama. Karena dalam tutorial ini kita akan menjalankan dua node, kita juga akan memerlukan dua klien, masing-masing harus terhubung ke node-nya sendiri, untuk itu kita membuat dua alias.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Kita bisa saja menjalankan alias atau menambahkannya ke akhir file $HOME/.bashrc dan menjalankan source $HOME/.bashrc.
Premis

RGB-node tidak menangani fungsionalitas terkait dompet apa pun, ia hanya melakukan tugas-tugas spesifik RGB pada data yang akan disediakan oleh dompet eksternal seperti bitcoin core. Khususnya, untuk menunjukkan alur kerja dasar dengan penerbitan dan transfer, kita akan memerlukan:

- Sebuah issuance_utxo di mana rgb-node-0 akan mengikat aset yang baru diterbitkan
- Sebuah receive_utxo di mana rgb-node-1 menerima aset
- Sebuah change_utxo di mana rgb-node-0 menerima perubahan aset
- Sebuah transaksi bitcoin yang ditandatangani sebagian (tx.psbt), yang output public key-nya akan diubah untuk menyertakan komitmen terhadap transfer.

Kita akan menggunakan bitcoin core cli, kita perlu memiliki daemon bitcoind yang berjalan pada testnet, ini akan memberi kita interoperabilitas dan pada akhirnya kita akan dapat mengirim aset kita sendiri ke pengguna RGB lain yang mengikuti tutorial ini.
Demi kesederhanaan, kita akan menambahkan alias ini di akhir file ~/.bashrc kita.
```
alias bcli="bitcoin-cli -testnet"
```

Mari kita daftar transaksi output yang belum terpakai kita dan pilih dua, satu akan menjadi issuance_utxo dan yang lainnya change_utxo, tidak masalah mana yang mana, yang penting adalah penerbit memiliki kontrol atas kedua UTXO ini.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Sebelum melangkah lebih jauh, kita perlu membahas tentang outpoints, sebuah transaksi tunggal dapat mencakup beberapa output, outpoint mencakup baik TXID 32-byte dan nomor indeks output 4-byte (vout) untuk merujuk pada output spesifik yang dipisahkan dengan titik dua :. Dalam daftar output yang belum terpakai kita, kita dapat menemukan dua UTXO, pada masing-masing kita dapat melihat txid dan vout, itu adalah outpoint dari issuance_utxo dan change_utxo kita.

receive_utxo adalah UTXO yang dikontrol oleh penerima, dalam kasus ini kita akan menggunakan e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 yang merupakan outpoint dari dompet lain.
- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Kita sekarang akan membuat transaksi yang ditandatangani sebagian (tx.psbt) yang output-nya akan dimodifikasi untuk menyertakan komitmen transfer, ingat untuk mengganti txid dan vout dengan milik Anda sendiri, alamat tujuan tidak terlalu penting, bisa jadi milik Anda atau orang lain, tidak masalah kemana sats tersebut pergi, yang penting adalah kita menggunakan issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

Output memberikan kita psbt dalam encoding base64 yang akan kita gunakan untuk membuat tx.psbt.
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Mari kita buat direktori baru yang disebut rgbdata di mana direktori data dari setiap node disimpan.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Sudah berada di $HOME/rgbdata, kita mulai setiap node di terminal yang berbeda, di mana ~/.cargo/bin adalah direktori di mana cargo menyalin semua biner setelah instalasi rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Penerbitan

Untuk menerbitkan aset, kita menjalankan rgb0-cli dengan subperintah fungible issue, kemudian argumennya, ticker USDT, nama "USD Tether" dan dalam alokasi kita akan menggunakan jumlah penerbitan dan issuance_utxo seperti yang kita lihat di bawah ini:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Aset berhasil diterbitkan. Gunakan informasi ini untuk berbagi:
Informasi Aset:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
Kami mendapatkan assetId, kami membutuhkannya untuk mentransfer aset tersebut.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Membuat UTXO yang Disamarkan

Untuk menerima USDT baru, rgb-node-1 perlu membuat UTXO yang disamarkan yang sesuai dengan receive_utxo untuk menampung aset tersebut.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```

Untuk dapat menerima transfer yang terkait dengan UTXO ini, kita akan memerlukan receive_utxo asli dan blinding_factor.

## Transfer

Untuk mentransfer sejumlah aset ke rgb-node-1, kita perlu mengirimkannya ke UTXO yang disamarkan, rgb-node-0 perlu membuat sebuah consignment dan disclosure, dan mengkomitkannya ke dalam transaksi bitcoin. Kemudian kita akan memerlukan psbt yang akan kita modifikasi untuk menyertakan komitmen. Selain itu, opsi -i dan -a memungkinkan kita untuk menyediakan outpoint input yang akan menjadi asal dari aset dan alokasi di mana kita akan menerima kembalian, kita harus menunjukkannya dengan cara berikut @<change_utxo>.
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Transfer berhasil, konsinyasi dan pengungkapan ditulis ke "consignment.rgb" dan "disclosure.rgb", transaksi saksi yang ditandatangani sebagian ke "witness.psbt"
Data Kiriman untuk Dibagikan: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
Ini akan menulis tiga file baru, consignment, disclosure, dan psbt termasuk tweak, psbt ini disebut transaksi saksi, consignment dikirim ke rgb-node-1.

## Saksi

Transaksi saksi harus ditandatangani dan disiarkan, untuk ini kita perlu mengenkodkannya kembali ke base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Tandatangani dengan subperintah walletprocesspsbt.
```yaml
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
Untuk menerjemahkan konten teknis yang diberikan ke dalam bahasa Indonesia dengan mempertahankan integritas teknis dan format aslinya, berikut adalah terjemahannya:

```json
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
```

Sekarang finalisasikan dan dapatkan hex-nya.

```json

Konten di atas merupakan sebuah string PSBT (Partially Signed Bitcoin Transaction) yang telah dikodekan dalam format Base64, dan tidak memerlukan terjemahan ke dalam bahasa Indonesia karena merupakan data teknis yang spesifik. "complete": true menunjukkan bahwa transaksi telah sepenuhnya ditandatangani.
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}

## Siarkan

Siarkan menggunakan subperintah sendrawtransaction untuk mendapatkannya dikonfirmasi ke dalam blockchain.
```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000" 8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```

## Terima

Untuk menerima transfer masuk, rgb-node-1 seharusnya telah menerima file konsinyasi dari rgb-node-0, memiliki receive_utxo dan blinding_factor yang sesuai yang dihasilkan selama pembuatan UTXO yang diblind.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Transfer aset berhasil diterima.
```

Sekarang kita dapat melihat (di dalam field knownAllocations) alokasi baru dari 100 unit aset di <receive_utxo> dengan menjalankan:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```
```yaml
name: USD Tether
description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 1
      outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
      revealedAmount:
        value: 100
        blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

Karena receive_utxo dibutakan saat transfer dilakukan, pemilik pembayaran rgb-node-0 tidak memiliki informasi tentang ke mana 100 USDT dikirim, sehingga lokasi tidak ditampilkan dalam knownAllocations.

```bash
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  nama: USD Tether
  deskripsi: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  tanggal: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      jumlah: 1000
      asal: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        nilai: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"

Tetapi seperti yang Anda lihat, rgb-node-0 tidak dapat melihat perubahan aset 900 yang kami berikan ke perintah transfer dengan argumen -a. Untuk mendaftarkan perubahan tersebut, rgb-node-0 perlu menerima pengungkapan.

```
$ rgb0-cli fungible enclose disclosure.rgb

Data pengungkapan berhasil disertakan.
```

Jika rgb-node-0 berhasil, Anda dapat melihat perubahan dengan mencantumkan aset tersebut.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  nama: USD Tether
Deskripsi: ~ knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  tanggal: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      jumlah: 1000
      asal: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        nilai: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        nilai: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2

## Kesimpulan

Kami telah berhasil menciptakan aset yang dapat ditukar dan memindahkannya dari satu transaksi ke transaksi lainnya secara privat. Jika kita memeriksa transaksi yang telah dikonfirmasi di block explorer, kita tidak akan menemukan perbedaan apa pun dari transaksi reguler. Hal ini berkat RGB yang menggunakan segel penggunaan tunggal untuk menyesuaikan transaksi. Dalam postingan ini, saya memperkenalkan cara kerja RGB.

Postingan ini mungkin memiliki bug, jika Anda menemukan sesuatu, mohon beritahu saya untuk meningkatkan panduan ini. Saran dan kritik juga selalu diterima, selamat hacking! 🖖