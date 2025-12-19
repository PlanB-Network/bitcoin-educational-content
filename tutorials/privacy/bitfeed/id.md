---
name: Bitfeed
description: Jelajahi rantai protokol Bitcoin utama.
---

![cover](assets/cover.webp)



Bitfeed adalah sebuah platform untuk memvisualisasikan lapisan onchain protokol Bitcoin. Ini diprakarsai oleh salah satu kontributor proyek Mempool.space dan menonjol terutama karena tampilannya yang minimalis dan kemudahan penggunaannya.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dalam tutorial ini, kita akan melihat alat ini, yang memungkinkan Anda menjelajahi semua transaksi dan blok di jaringan.



## Memulai dengan Bitfeed



Bitfeed adalah platform yang berfokus pada tiga hal utama:





- Konsultasi Blockchain**,
- Pencarian transaksi**,
- Memvisualisasikan mempool**.



### Berkonsultasi dengan blockchain



Pada halaman beranda Bitfeed, Anda terutama akan menemukan :





- Bilah pencarian: Bagian ini adalah titik masuk untuk kueri blockchain. Di sini Anda bisa mencari blok tertentu berdasarkan nomor atau hash-nya. Anda juga bisa mencari transaksi tertentu dan alamat Bitcoin untuk memverifikasi informasi transaksi tertentu di jaringan.



![searchBar](assets/fr/01.webp)



Di pojok kiri atas, Anda bisa melihat harga bitcoin saat ini, yang diperkirakan dalam dolar AS (USD).



![price](assets/fr/02.webp)



Pada bilah sisi kanan adalah menu platform. Dari menu ini Anda dapat menyesuaikan antarmuka platform sesuai dengan keinginan Anda, menambah atau menghapus item, dan menyesuaikan filter tampilan. Sebagai contoh, melihat ukuran setiap blok berdasarkan nilai atau berat dalam byte virtual (vBytes).



![menu](assets/fr/03.webp)



Di bagian tengah halaman terdapat blok terakhir yang ditambang, dengan tampilan semua transaksi yang termasuk dalam blok tersebut. Bagian ini memberikan informasi mengenai stempel waktu, jumlah total bitcoin yang terlibat dalam blok tersebut, ukuran blok dalam byte, jumlah transaksi, dan rasio biaya transaksi rata-rata per byte virtual dalam blok tersebut.



![block](assets/fr/04.webp)



Anda dapat kembali menelusuri riwayat saluran dengan mencari blok tertentu di bilah pencarian, dan melihatnya sesuai dengan kriteria Anda.



Sebagai contoh, kita ingin melihat transaksi di blok `879488`.



![bloc](assets/fr/05.webp)



Transaksi pertama dari blok ini merupakan transaksi **coinbase** yang memungkinkan penambang blok ini untuk mendapatkan hadiah mining, yang hanya dapat digunakan setelah 100 blok ditambang, yang terdiri dari biaya transaksi yang disertakan dan hibah blok. Transaksi ini adalah transaksi yang memungkinkan bitcoin baru diterbitkan pada sistem.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Secara default, transaksi dalam sebuah blok direpresentasikan berdasarkan dua kriteria:




- Ukuran, yang dapat bervariasi antara nilai dan berat (vBytes);
- Warna dapat bervariasi antara usia dan rasio biaya transaksi per byte virtual.



![options](assets/fr/07.webp)



Oleh karena itu, kita dapat menyimpulkan bahwa semua transaksi yang termasuk dalam blok yang sama memiliki jumlah konfirmasi yang sama dalam blockchain. Kubus terbesar mewakili transaksi yang mengandung jumlah bitcoin tertinggi.



Interpretasi ini lebih lanjut dikonfirmasi oleh opsi menu **"Info "**, yang menginformasikan kepada kita tentang terjemahan warna dan ukuran transaksi blok.



![infos](assets/fr/08.webp)



Anda juga bisa melihat transaksi blok berdasarkan byte virtual dan rasio biaya. Tampilan ini mungkin berbeda dengan tampilan sebelumnya, karena nilai bitcoin yang disertakan dalam sebuah transaksi tidak menentukan ukurannya.



![visualisation](assets/fr/09.webp)



### Melihat transaksi



Anda dapat mencari transaksi dengan menggunakan pengenalnya melalui bilah pencarian. Anda juga dapat mengeklik sebuah kubus untuk melihat informasi yang terkait dengan transaksi tersebut.



Dalam kasus kita, mari kita ambil transaksi yang menempati ruang terbesar di blok `879488`.



![biggest](assets/fr/10.webp)



Anda akan melihat bahwa transaksi ini memiliki `42.989`, yang merepresentasikan perbedaan antara blok terakhir yang ditambang dengan blok yang kita pilih. Konfirmasi ini membantu memperkuat keamanan jaringan Bitcoin, karena untuk memodifikasi transaksi ini secara jahat, penyerang harus memiliki daya komputasi yang setara untuk menulis ulang seluruh rantai-blok utama.



Ukuran transaksi ini adalah `57.088 vByte`, terutama karena banyaknya jumlah UTXO yang digunakan dalam pembuatannya (842 entri). Anehnya, rasio biaya yang diterapkan tetap relatif rendah (hanya 4 sats/vByte) dibandingkan dengan rata-rata keseluruhan blok sebesar 5,82 sats/vByte.



Oleh karena itu, transaksi yang paling banyak menggunakan ruang belum tentu merupakan transaksi dengan rasio biaya transaksi tertinggi.



![transaction](assets/fr/11.webp)



Jika Anda mengikuti skala pada menu **Info**, transaksi dengan rasio biaya transaksi tertinggi adalah yang berwarna ungu. Ini adalah transaksi [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) dengan rasio biaya transaksi sebesar `147,49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualisasi Mempool



Mempool adalah lokasi virtual di mana transaksi Bitcoin yang menunggu untuk dimasukkan ke dalam blok dikelompokkan bersama. Bitfeed memungkinkan konsultasi [mempool](https://planb.academy/resources/glossary/mempool) dari beberapa penambang Bitcoin, yang menawarkan berbagai macam pelacakan transaksi.



![mempool](assets/fr/13.webp)



Pada bagian ini, Anda dapat melacak semua transaksi yang valid dan yang belum dikonfirmasi pada rantai utama jaringan Bitcoin.



![unconfirmed](assets/fr/14.webp)



Anda sekarang memiliki panduan untuk menggunakan platform Bitfeed untuk menganalisis blok dan transaksi untuk memvisualisasikan informasi yang tersedia di rantai utama jaringan Bitcoin, sambil memanfaatkan antarmuka yang minimalis dan mudah digunakan. Jika Anda menikmati tutorial ini, kami sarankan Anda untuk mengambil langkah selanjutnya: temukan Lightning Network melalui proyek Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017