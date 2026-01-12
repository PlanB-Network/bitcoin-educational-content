---
name: Bitfeed
description: Jelajahi rantai protokol Bitcoin utama.
---

![cover](assets/cover.webp)


Bitfeed adalah platform buat memvisualisasikan layer onchain di protokol Bitcoin. Ini diprakarsai oleh salah satu kontributor proyek Mempool.space dan menonjol terutama karena tampilannya yang minimalis dan cara pakainya yang gampang.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dalam tutorial ini, kita akan melihat alat ini, yang memungkinkan kamu menjelajahi semua transaksi dan blok di jaringan.



## Memulai dengan Bitfeed



Bitfeed adalah platform yang berfokus pada tiga hal utama:





- Konsultasi Blockchain**,
- Pencarian transaksi**,
- Memvisualisasikan mempool**.



### Berkonsultasi dengan blockchain



Pada halaman beranda Bitfeed, kamu terutama akan menemukan :





- Bilah pencarian: Bagian ini jadi titik masuk buat ngekueri blockchain. Di sini kamu bisa nyari blok tertentu berdasarkan nomor atau hash-nya. Kamu juga bisa nyari transaksi tertentu dan alamat Bitcoin buat ngecek informasi transaksi tertentu di jaringan.


![searchBar](assets/fr/01.webp)



Di pojok kiri atas, kamu bisa melihat harga bitcoin saat ini, yang diperkirakan dalam dolar AS (USD).



![price](assets/fr/02.webp)



Di bilah sisi kanan ada menu platform. Dari menu ini kamu bisa sesuaikan antarmuka platform sesuai kebutuhan kamu, tambah atau hapus item, dan ngatur filter tampilan. Misalnya, ngeliat ukuran tiap blok berdasarkan nilai atau beratnya dalam virtual bytes (vBytes).


![menu](assets/fr/03.webp)



Di bagian tengah halaman ada blok terbaru yang ditambang, lengkap dengan semua transaksi yang masuk ke blok itu. Bagian ini menunjukkan info tentang stempel waktu, total jumlah bitcoin yang ada di dalam blok itu, ukuran blok dalam byte, jumlah transaksi, dan rasio biaya transaksi rata-rata per virtual byte di blok tersebut.


![block](assets/fr/04.webp)



Kamu bisa mundur menelusuri riwayat chain dengan nyari blok tertentu lewat bilah pencarian, lalu ngeliatnya sesuai kriteria kamu.


Sebagai contoh, kita ingin melihat transaksi di blok `879488`.



![bloc](assets/fr/05.webp)



Transaksi pertama di blok ini adalah transaksi **coinbase** yang ngasih penambang blok ini hadiah mining. Hadiah ini cuma bisa dipakai setelah 100 blok berikutnya ditambang, dan terdiri dari biaya transaksi yang masuk plus block subsidy. Transaksi ini adalah transaksi yang bikin bitcoin baru diterbitin ke dalam sistem.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Secara default, transaksi dalam sebuah blok direpresentasikan berdasarkan dua kriteria:




- Ukuran, yang dapat bervariasi antara nilai dan berat (vBytes);
- Warna dapat bervariasi antara usia dan rasio biaya transaksi per byte virtual.



![options](assets/fr/07.webp)



Karena itu, kita bisa nyimpulin kalau semua transaksi yang ada di dalam blok yang sama punya jumlah konfirmasi yang sama di blockchain. Kubus terbesar mewakili transaksi yang punya jumlah bitcoin paling gede.


Interpretasi ini lebih lanjut dikonfirmasi oleh opsi menu **"Info "**, yang menginformasikan kepada kita tentang terjemahan warna dan ukuran transaksi blok.



![infos](assets/fr/08.webp)



Kamu juga bisa lihat transaksi di blok berdasarkan virtual bytes dan rasio biayanya. Tampilan ini bisa beda dari tampilan sebelumnya, soalnya nilai bitcoin yang ada di sebuah transaksi nggak menentukan ukuran transaksinya.


![visualisation](assets/fr/09.webp)



### Melihat transaksi



Kamu bisa nyari transaksi pakai ID-nya lewat bilah pencarian. Kamu juga bisa ngeklik sebuah kubus buat ngeliat info terkait transaksi itu.

Di kasus kita, mari kita ambil transaksi yang paling banyak makan ruang di blok '879488'.


![biggest](assets/fr/10.webp)



Kamu bakal liat kalau transaksi ini punya '42.989', yang nunjukin selisih antara blok terakhir yang ditambang dan blok yang kita pilih. Jumlah konfirmasi ini bantu ngekuatin keamanan jaringan Bitcoin, soalnya kalau ada penyerang yang mau ngubah transaksi ini dengan niat jahat, dia harus punya daya komputasi yang cukup buat nulis ulang seluruh rantai blok utama.

Ukuran transaksi ini adalah '57.088' vByte, terutama karena banyaknya UTXO yang dipakai waktu transaksi ini dibuat (842 entri). Uniknya, rasio biaya yang dipakai tetap relatif rendah, cuma 4 sats/vByte, dibanding rata-rata keseluruhan blok yang sebesar 5,82 sats/vByte.

Jadi, transaksi yang paling banyak makan ruang belum tentu jadi transaksi dengan rasio biaya transaksi paling tinggi.



![transaction](assets/fr/11.webp)



Jika Anda mengikuti skala pada menu **Info**, transaksi dengan rasio biaya transaksi tertinggi adalah yang berwarna ungu. Ini adalah transaksi [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) dengan rasio biaya transaksi sebesar `147,49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualisasi Mempool



Mempool adalah lokasi virtual di mana transaksi Bitcoin yang menunggu untuk dimasukkan ke dalam blok dikelompokkan bersama. Bitfeed memungkinkan konsultasi [mempool](https://planb.academy/resources/glossary/mempool) dari beberapa penambang Bitcoin, yang menawarkan berbagai macam pelacakan transaksi.



![mempool](assets/fr/13.webp)



Pada bagian ini, kamu dapat melacak semua transaksi yang valid dan yang belum dikonfirmasi pada rantai utama jaringan Bitcoin.



![unconfirmed](assets/fr/14.webp)



Sekarang kamu punya panduan buat pake platform Bitfeed buat menganalisis blok dan transaksi supaya bisa memvisualisasikan info yang ada di rantai utama jaringan Bitcoin, sambil manfaatin antarmuka yang minimalis dan gampang dipakai. Kalau kamu suka tutorial ini, aku saranin kamu lanjut ke langkah berikutnya: kenalan sama Lightning Network lewat proyek Amboss.

https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017
