---
name: Whirlpool Stats Tools - Anonsets
description: Memahami konsep anonset dan cara menghitungnya dengan WST
---
![cover](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, Whirlpool Stats Tool tidak lagi tersedia untuk diunduh, karena dihosting di Gitlab Samourai. Meskipun Anda sebelumnya telah mengunduh alat ini secara lokal ke mesin Anda, atau telah terpasang di node RoninDojo Anda, WST saat ini tidak akan berfungsi. Alat ini bergantung pada data yang disediakan oleh OXT.me untuk operasinya, dan situs ini tidak lagi dapat diakses. Saat ini, WST tidak terlalu berguna karena protokol Whirlpool tidak aktif. Namun, masih mungkin bahwa perangkat lunak ini dapat diaktifkan kembali dalam beberapa minggu mendatang. Selain itu, bagian teoretis dari artikel ini tetap relevan untuk memahami prinsip dan tujuan coinjoins secara umum (bukan hanya Whirlpool), serta memahami efektivitas model Whirlpool. Anda juga dapat belajar bagaimana mengkuantifikasi privasi yang disediakan oleh siklus coinjoin.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

*"Putuskan jejak yang ditinggalkan oleh koin Anda"*

Dalam tutorial ini, kita akan mempelajari konsep anonsets, indikator yang memungkinkan kita untuk memperkirakan kualitas proses coinjoin di Whirlpool. Kita akan membahas metode perhitungan dan interpretasi dari indikator-indikator ini. Setelah bagian teoretis, kita akan beralih ke praktik dengan belajar menghitung anonsets dari transaksi tertentu menggunakan alat Python *Whirlpool Stats Tools* (WST).

## Apa itu coinjoin di Bitcoin?
**Coinjoin adalah teknik yang memutuskan pelacakan bitcoin di blockchain**. Teknik ini mengandalkan transaksi kolaboratif dengan struktur khusus yang bernama sama: transaksi coinjoin.

Transaksi coinjoin meningkatkan privasi pengguna Bitcoin dengan mempersulit analisis rantai bagi pengamat eksternal. Strukturnya memungkinkan penggabungan beberapa koin dari pengguna yang berbeda ke dalam satu transaksi, sehingga menyamarkan jejak dan membuatnya sulit untuk menentukan hubungan antara alamat input dan output.

Prinsip coinjoin didasarkan pada pendekatan kolaboratif: beberapa pengguna yang ingin mencampur bitcoin mereka menyetorkan jumlah yang identik sebagai input dari transaksi yang sama. Jumlah-jumlah ini kemudian didistribusikan kembali dalam output dengan nilai yang setara. Di akhir transaksi, menjadi mustahil untuk mengasosiasikan output tertentu dengan pengguna tertentu. Tidak ada hubungan langsung antara input dan output, sehingga memutuskan asosiasi antara pengguna dan UTXO mereka, serta sejarah setiap koin.

![coinjoin](assets/notext/1.webp)

Contoh transaksi coinjoin:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
Untuk melaksanakan coinjoin sambil memastikan bahwa setiap pengguna mempertahankan kontrol atas dana mereka setiap saat, proses dimulai dengan pembangunan transaksi oleh koordinator, yang kemudian mengirimkannya ke setiap peserta. Setiap pengguna kemudian menandatangani transaksi setelah memverifikasi bahwa itu sesuai dengan mereka. Semua tanda tangan yang terkumpul akhirnya diintegrasikan ke dalam transaksi. Jika ada upaya untuk mengalihkan dana oleh pengguna atau koordinator, dengan memodifikasi output dari transaksi coinjoin, tanda tangan akan terbukti tidak valid, yang mengarah pada penolakan transaksi oleh node.

Ada beberapa implementasi dari coinjoin, seperti Whirlpool, JoinMarket, atau Wabisabi, masing-masing bertujuan untuk mengelola koordinasi antar peserta dan meningkatkan efisiensi transaksi coinjoin.

Dalam tutorial ini, kita akan fokus pada implementasi favorit saya: Whirlpool, yang tersedia di Samourai Wallet dan Sparrow Wallet. Menurut saya, ini adalah implementasi yang paling efisien untuk coinjoins di Bitcoin.

## Apa kegunaan coinjoin di Bitcoin?
Kegunaan coinjoin terletak pada kemampuannya untuk menghasilkan plausible deniability, dengan menyamarkan koin Anda dalam sebuah kelompok koin yang tidak dapat dibedakan. Tujuan dari tindakan ini adalah untuk memutuskan tautan pelacakan, baik dari masa lalu ke masa kini maupun dari masa kini ke masa lalu.

Dengan kata lain, seorang analis yang mengetahui transaksi awal Anda pada masuknya siklus coinjoin seharusnya tidak dapat mengidentifikasi dengan pasti UTXO Anda pada keluaran siklus remix (analisis dari masuk siklus ke keluar siklus).

![coinjoin](assets/en/2.webp)

Sebaliknya, seorang analis yang mengetahui UTXO Anda pada keluaran siklus coinjoin seharusnya tidak dapat menentukan transaksi asli pada masuknya siklus (analisis dari keluar siklus ke masuk siklus).

![coinjoin](assets/en/3.webp)

Untuk menilai kesulitan bagi seorang analis untuk menghubungkan masa lalu dengan masa kini dan sebaliknya, perlu untuk mengkuantifikasi ukuran kelompok di mana koin Anda disembunyikan. Ukuran ini memberi tahu kita jumlah analisis yang memiliki probabilitas identik. Jadi, jika analisis yang benar tenggelam di antara 3 analisis lain dengan probabilitas yang sama, tingkat penyembunyian Anda sangat rendah. Di sisi lain, jika analisis yang benar berada dalam satu set 20.000 analisis yang semuanya sama-sama mungkin, koin Anda sangat tersembunyi.

Dan tepatnya, ukuran kelompok ini merupakan indikator yang disebut "anonsets".

## Memahami anonsets
Anonsets berfungsi sebagai indikator untuk mengevaluasi tingkat privasi dari UTXO tertentu. Lebih spesifik, mereka mengukur jumlah UTXO yang tidak dapat dibedakan dalam set yang mencakup koin yang diteliti. Kebutuhan akan set UTXO yang homogen berarti bahwa anonsets biasanya dihitung selama siklus coinjoin. Penggunaan indikator ini sangat relevan untuk coinjoins Whirlpool karena keseragamannya.

Anonsets memungkinkan, jika sesuai, untuk menilai kualitas dari coinjoins. Ukuran anonset yang besar berarti tingkat anonimitas yang meningkat, karena menjadi sulit untuk membedakan UTXO spesifik dalam set.

Ada dua jenis anonsets:
- **Set anonimitas prospektif;**
- **Set anonimitas retrospektif.**
Indikator pertama menunjukkan ukuran kelompok di mana UTXO yang diteliti disembunyikan di akhir siklus, mengetahui UTXO pada masuknya, yaitu, jumlah koin yang tidak dapat dibedakan yang hadir dalam kelompok ini. Indikator ini memungkinkan pengukuran ketahanan kerahasiaan koin terhadap analisis dari masa lalu ke masa kini (masuk ke keluar). Dalam bahasa Inggris, nama indikator ini adalah "*forward anonset*", atau "*forward-looking metrics*".
![coinjoin](assets/en/4.webp)
Metrik ini memperkirakan sejauh mana UTXO Anda dilindungi dari upaya untuk merekonstruksi sejarahnya dari titik masuk hingga titik keluar dalam proses coinjoin.

Sebagai contoh, jika transaksi Anda berpartisipasi dalam siklus coinjoin pertamanya dan dua siklus keturunan lainnya selesai, anonset prospektif dari koin Anda akan menjadi `13`:

![coinjoin](assets/en/5.webp)

Indikator kedua menunjukkan jumlah sumber yang mungkin untuk sebuah koin, dengan mengetahui UTXO di akhir siklus. Indikator ini mengukur ketahanan kerahasiaan koin terhadap analisis dari masa sekarang ke masa lalu (keluar masuk), yaitu, seberapa sulitnya bagi seorang analis untuk melacak kembali ke asal usul koin Anda, sebelum siklus coinjoin. Dalam bahasa Inggris, nama dari indikator ini adalah "*backward anonset*", atau "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Dengan mengetahui UTXO Anda di akhir siklus, anonset retrospektif menentukan jumlah transaksi Tx0 potensial yang mungkin telah membentuk masuknya Anda ke dalam siklus coinjoin. Dalam diagram di bawah ini, ini sesuai dengan jumlah semua gelembung oranye.

![coinjoin](assets/en/7.webp)

## Menghitung anonset dengan Whirlpool Stats Tools (WST)
Untuk menghitung indikator ini pada koin Anda sendiri yang telah melalui siklus coinjoin, Anda dapat menggunakan alat yang dikembangkan khusus oleh Samourai Wallet: *Whirlpool Stats Tools*.

Jika Anda memiliki RoninDojo, WST sudah terpasang di node Anda. Anda dapat langsung melewati langkah instalasi dan langsung mengikuti langkah penggunaan. Bagi yang tidak memiliki node RoninDojo, mari kita lihat cara melanjutkan dengan instalasi alat ini di komputer.

Anda akan membutuhkan: Tor Browser (atau Tor), Python 3.4.4 atau lebih tinggi, git, dan pip. Buka terminal. Untuk memeriksa keberadaan dan versi perangkat lunak ini di sistem Anda, masukkan perintah berikut:
```plaintext
python --version
git --version
pip --version
```

Jika diperlukan, Anda dapat mengunduhnya dari situs web masing-masing:
- https://www.python.org/downloads/ (pip langsung disertakan dengan Python sejak versi 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Setelah semua perangkat lunak ini terpasang, dari terminal, klon repositori WST:
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Navigasikan ke direktori WST:
```plaintext
cd whirlpool_stats
```

Pasang dependensi:
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Anda juga dapat memasangnya secara manual (opsional):
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Navigasikan ke subfolder `/whirlpool_stats`:
```plaintext
cd whirlpool_stats
```

Mulai WST:
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

Jalankan Tor atau Tor Browser di latar belakang.

**-> Untuk pengguna RoninDojo, Anda dapat melanjutkan tutorial langsung dari sini.**

Atur proxy ke Tor (RoninDojo),
```plaintext
socks5 127.0.0.1:9050
```
atau ke Tor Browser tergantung pada apa yang Anda gunakan:
```plaintext
socks5 127.0.0.1:9150
```

Manipulasi ini akan memungkinkan Anda untuk mengunduh data pada OXT melalui Tor, agar tidak membocorkan informasi tentang transaksi Anda. Jika Anda pemula dan langkah ini tampak rumit, ketahuilah bahwa ini hanya melibatkan pengalihan lalu lintas internet Anda melalui Tor. Metode paling sederhana terdiri dari menjalankan Tor Browser di latar belakang pada komputer Anda, kemudian menjalankan hanya perintah kedua untuk terhubung melalui browser ini (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Selanjutnya, navigasikan ke direktori kerja dari mana Anda berniat untuk mengunduh data WST menggunakan perintah `workdir`. Folder ini akan berfungsi untuk menyimpan data transaksional yang akan Anda ambil dari OXT dalam bentuk file `.csv`. Informasi ini penting untuk menghitung indikator yang Anda cari. Anda bebas memilih lokasi direktori ini. Mungkin bijaksana untuk membuat folder khusus untuk data WST. Sebagai contoh, mari kita pilih folder unduhan. Jika Anda menggunakan RoninDojo, langkah ini tidak diperlukan:
```plaintext
workdir path/to/your/directory
```

Prompt perintah kemudian harus berubah untuk menunjukkan direktori kerja Anda.

![WST](assets/notext/12.webp)

Kemudian unduh data dari kolam yang mengandung transaksi Anda. Sebagai contoh, jika saya berada di kolam `100,000 sats`, perintahnya adalah:
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

Kode denominasi pada WST adalah sebagai berikut:
- Kolam 0.5 bitcoin: `05`
- Kolam 0.05 bitcoin: `005`
- Kolam 0.01 bitcoin: `001`
- Kolam 0.001 bitcoin: `0001`
Setelah data diunduh, muatlah. Sebagai contoh, jika saya berada di kolam `100,000 sats`, perintahnya adalah:
```plaintext
load 0001
```

Langkah ini membutuhkan waktu beberapa menit tergantung pada komputer Anda. Sekarang adalah waktu yang tepat untuk membuat diri Anda secangkir kopi! :)

![WST](assets/notext/14.webp)

Setelah memuat data, ketik perintah `score` diikuti oleh TXID (identifier transaksi) Anda untuk mendapatkan anonsetnya:
```plaintext
score TXID
```

**Perhatian**, pilihan TXID yang digunakan bervariasi tergantung pada anonset yang ingin Anda hitung. Untuk menilai anonset prospektif dari sebuah koin, perlu untuk memasukkan, melalui perintah `score`, TXID yang sesuai dengan coinjoin pertamanya, yang merupakan pencampuran awal yang dilakukan dengan UTXO ini. Di sisi lain, untuk menentukan anonset retrospektif, Anda harus memasukkan TXID dari coinjoin terakhir yang dilakukan. Untuk merangkum, anonset prospektif dihitung dari TXID dari pencampuran pertama, sementara anonset retrospektif dihitung dari TXID dari pencampuran terakhir.

WST kemudian menampilkan skor retrospektif (*Backward-looking metrics*) dan skor prospektif (*Forward-looking metrics*). Sebagai contoh, saya mengambil TXID dari sebuah koin acak di Whirlpool yang bukan milik saya.

![WST](assets/notext/15.webp)
Transaksi yang dimaksud: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
Jika kita menganggap transaksi ini sebagai coinjoin pertama yang dilakukan untuk koin yang bersangkutan, maka ia mendapatkan keuntungan dari anonset prospektif sebesar `86,871`. Ini berarti ia tersembunyi di antara `86,871` koin yang tidak dapat dibedakan. Bagi pengamat eksternal yang mengetahui koin ini di awal siklus coinjoin dan mencoba melacak keluarannya, mereka akan dihadapkan pada `86,871` UTXO yang mungkin, masing-masing dengan kemungkinan identik sebagai koin yang dicari.

Jika kita menganggap transaksi ini sebagai coinjoin terakhir dari koin tersebut, maka ia memiliki anonset retrospektif sebesar `42,185`. Ini berarti ada `42,185` sumber potensial untuk UTXO ini. Jika pengamat eksternal mengidentifikasi koin ini di akhir siklus dan berusaha melacak asal-usulnya, mereka akan dihadapkan pada `42,185` sumber yang mungkin, semua dengan kemungkinan yang sama untuk menjadi asal yang dicari.
Selain skor anonset, WST juga memberi Anda tingkat difusi keluaran Anda dalam kolam berdasarkan anonset. Indikator lain ini hanya memungkinkan Anda untuk menilai potensi peningkatan bagi bagian Anda. Tingkat ini sangat berguna untuk anonset prospektif. Memang, jika bagian Anda memiliki tingkat difusi 15%, itu berarti ia dapat dikacaukan dengan 15% dari bagian dalam kolam. Itu bagus, tetapi Anda masih memiliki margin yang sangat besar untuk peningkatan dengan terus melakukan remix. Di sisi lain, jika bagian Anda memiliki tingkat difusi 95%, maka Anda mendekati batas kolam. Anda dapat terus melakukan remix, tetapi anonset Anda tidak akan meningkat banyak.

Penting untuk dicatat bahwa anonset yang dihitung oleh WST tidak sepenuhnya akurat. Mengingat volume data yang sangat besar yang harus diproses, WST menggunakan algoritma *HyperLogLogPlusPlus* untuk secara signifikan mengurangi beban yang terkait dengan pemrosesan data lokal dan memori yang diperlukan. Ini adalah algoritma yang memungkinkan estimasi jumlah nilai unik dalam set data yang sangat besar sambil mempertahankan akurasi tinggi dalam hasilnya. Oleh karena itu, skor yang diberikan cukup baik untuk digunakan dalam analisis Anda, karena mereka adalah perkiraan yang sangat dekat dengan kenyataan, tetapi mereka tidak boleh diinterpretasikan sebagai nilai eksak hingga satuan.

Kesimpulannya, ingatlah bahwa tidak wajib untuk secara sistematis menghitung anonset untuk setiap bagian Anda dalam coinjoins. Desain Whirlpool sendiri sudah memberikan jaminan. Memang, anonset retrospektif jarang menjadi perhatian. Dari campuran awal Anda, Anda memperoleh skor retrospektif yang sangat tinggi berkat warisan dari campuran sebelumnya sejak coinjoin Genesis. Sedangkan untuk anonset prospektif, cukup untuk menjaga bagian Anda dalam akun pasca-campuran untuk periode waktu yang cukup lama.
Inilah mengapa saya menganggap penggunaan Whirlpool sangat relevan dalam strategi *Hodl -> Mix -> Spend -> Replace*. Menurut saya, pendekatan yang paling logis adalah menyimpan sebagian besar tabungan bitcoin seseorang dalam dompet dingin, sambil terus memelihara sejumlah tertentu dalam coinjoins di Samourai untuk menutupi pengeluaran sehari-hari. Setelah bitcoin dari coinjoins tersebut dihabiskan, mereka digantikan dengan yang baru, untuk kembali ke ambang batas yang ditentukan dari potongan yang dicampur. Metode ini memungkinkan seseorang untuk membebaskan diri dari kekhawatiran tentang anonset UTXO kita, sambil membuat waktu yang diperlukan untuk efektivitas coinjoins jauh lebih tidak membatasi.
**Sumber Eksternal:**

- [Podcast dalam bahasa Prancis tentang analisis rantai](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Artikel Wikipedia tentang HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Repositori Samourai untuk Statistik Whirlpool
- Situs web Whirlpool oleh Samourai
- [Artikel Medium dalam bahasa Inggris tentang privasi dan Bitcoin oleh Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Artikel Medium dalam bahasa Inggris tentang konsep set anonimitas oleh Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)