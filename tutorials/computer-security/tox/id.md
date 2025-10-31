---
name: Tox
description: Buka percakapan tanpa perantara pada protokol Tox yang terdesentralisasi
---
![cover](assets/cover.webp)

Enkripsi end-to-end adalah layanan yang ditawarkan oleh banyak aplikasi perpesanan seperti WhatsApp dan Telegram. Enkripsi di sini berarti bahwa sebelum pesan dikirim oleh pengirim, pesan tersebut diamankan oleh kunci kriptografi yang hanya dimiliki oleh penerima. Hari ini kita akan menemukan aplikasi perpesanan yang sepenuhnya terdesentralisasi, dengan enkripsi end-to-end, yang didasarkan pada prinsip yang mirip dengan Blockchain, untuk menawarkan komunikasi yang aman dan terenkripsi secara end-to-end tanpa perantara: Tox Chat.

| Aplikasi       | E2EE 1:1       | E2EE Grup   | Pendaftaran Anonim | Lisensi client open-source | Lisensi server open-source | Server Terdesentralisasi | Tahun Dibuat |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opsional) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (opsional) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federasi)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federasi)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(tanpa direktori)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Enkripsi end-to-end*

## Apa itu Tox?

Tox adalah protokol komunikasi gratis (open source dan terdesentralisasi yang menggunakan teknologi Networking and Cryptography Library (NaCl) ditambah kombinasi algoritma enkripsi untuk memastikan keamanan dan kerahasiaan penggunanya. Tox memungkinkan Anda bertukar pesan teks, melakukan panggilan audio dan video, berbagi file, dan berbagi layar Anda dengan teman secara aman, terdesentralisasi, dan tanpa perantara.

Teknologi yang digunakan oleh protokol Tox mirip dengan jaringan peer-to-peer seperti Blockchain, yang mendukung desentralisasi infrastruktur protokol. Tidak seperti jejaring sosial dan aplikasi pesan terenkripsi end-to-end, aplikasi Tox Chat dibangun di atas protokol terdesentralisasi yang tidak memiliki server pusat. Semua pengguna berkomunikasi dalam jaringan peer-to-peer bebas perantara dan tahan sensor. Untuk berkomunikasi, setiap pengguna diidentifikasi oleh ID unik (ToxID) yang berasal dari kunci publiknya, yang disimpan dalam tabel Hash terdistribusi.

## Bergabunglah dengan Tox

Anda dapat menggunakan protokol Tox melalui aplikasi klien pesan instan yang dapat Anda unduh dari [situs Tox Chat](https://tox.chat).

![download](assets/fr/01.webp)


Tergantung pada sistem operasi Anda, Anda dapat mengunduh dan install aplikasi klien Tox yang sesuai:

- aTox: [aTox](https://github.com/evilcorpltd/aTox), aplikasi klien Tox yang ditulis dalam bahasa Kotlin yang hanya tersedia di Android

![aTox](assets/fr/02.webp)

- qTox: Aplikasi klien Tox yang [open source](https://github.com/TokTok/qTox) yang berbasiskan Qt Framework (C++) yang tersedia di Windows, Linux, MacOS.

![qTox](assets/fr/03.webp)

- Toxic: [Toxic](https://github.com/JFreegman/toxic) adalah aplikasi klien Tox yang ditulis dalam bahasa C dan berjalan pada sistem dengan interface command line.

![Toxic](assets/fr/04.webp)

Dalam tutorial ini, kita akan menggunakan aplikasi klien qTox pada Windows dan aTox untuk berkomunikasi.

## Memulai dengan qTox

Setelah diunduh, instal aplikasi klien Tox Anda dan buat profil Anda.

![qTox-acount](assets/fr/05.webp)

Selamat, Anda baru saja bergabung dengan protokol Tox. Pada perangkat lunak qTox, Anda dapat menemukan informasi profil Anda dengan mengeklik nama pengguna Anda.

![profil](assets/fr/06.webp)

Secara khusus, Anda akan menemukan Tox ID Anda, yang dapat Anda simpan sebagai kode QR dan bagikan dengan orang-orang yang ingin menghubungi Anda.

Ekspor file profil Tox Anda sehingga Anda memiliki cadangan (backup) profil dan informasi kontak yang dapat Anda gunakan untuk memulihkan. Klik tombol "**Export**", lalu pilih folder untuk file cadangan Anda.

![export](assets/fr/07.webp)

Dari menu "**More**", tambahkan teman, impor kontak, dan kelola permintaan pertemanan yang Anda terima.

![friends](assets/fr/08.webp)

Anda bisa menghubungi saya melalui Tox ID ini misalnya: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F

Setelah permintaan pertemanan dikirim, penerima harus menerima atau menolak permintaan Anda sebelum Anda dapat menghubungi mereka.

![request](assets/fr/09.webp)

Aplikasi klien Tox Anda mencakup semua opsi yang ditawarkan oleh aplikasi pesan instan:

- Panggilan video
- Panggilan suara
- Berbagi file
- emoji

![chat](assets/fr/10.webp)

### Kelompok Peer-to-peer

Aplikasi klien Tox Anda juga memungkinkan Anda untuk berkomunikasi dengan sekelompok orang secara sepenuhnya terdesentralisasi: ini disebut konferensi. Di menu "**Groups**", buat konferensi baru atau lihat daftar undangan untuk bergabung dengan konferensi yang telah Anda terima.

![conferences](assets/fr/11.webp)

Setelah konferensi dibuat, Anda dapat mengundang teman-teman Anda untuk bergabung dengan konferensi di klien Tox Anda. Di daftar teman Anda, klik kanan pada nama pengguna (username) teman yang ingin Anda undang. Klik opsi "**Invite to conference**", lalu pilih nama konferensi yang telah Anda buat. Anda juga dapat mengundang teman dengan secara implisit membuat konferensi dengan opsi "**Create a new conference**".

⚠️ Aplikasi klien Tox masih dalam tahap pengembangan, jadi Anda mungkin mengalami kesalahan saat berinteraksi dengan perangkat lunak. Fungsionalitas konferensi dan panggilan video belum tersedia pada aplikasi klien Tox Android (aTox).

![invite](assets/fr/12.webp)

### Transfer file

Di menu **Transfer file**, Anda akan menemukan riwayat file yang telah Anda kirim dan yang telah Anda terima dari kontak Anda.

![files](assets/fr/13.webp)

Anda juga dapat menyesuaikan konfigurasi berbagi file untuk setiap diskusi yang Anda lakukan. Klik kanan pada nama pengguna penerima dan pilih "**Tampilkan detail lebih lanjut**".

![details](assets/fr/14.webp)

Dari Interface detail , Anda dapat mengelola otorisasi yang Anda berikan kepada penerima untuk file :

- Penerimaan otomatis undangan konferensi.
- Penerimaan file otomatis.
- Jalur cadangan untuk file diskusi Anda.
  
![permissions](assets/fr/15.webp)

### Parameter lainnya



Di menu **Settings**, Anda dapat menyesuaikan pengaturan aplikasi klien Tox Anda.

- Pada bagian **General**, ubah bahasa aplikasi klien Tox Anda, tentukan jalur pencadangan file dan ukuran file maksimum yang akan diterima secara otomatis.

![general](assets/fr/16.webp)

- Pada bagian **Interface user**, ubah jenis font dan ukuran pesan Anda. Anda juga dapat mengubah tema aplikasi klien Tox Anda.

![ui](assets/fr/17.webp)

- Tab **Privacy** memungkinkan Anda untuk menentukan pesan yang bersifat sementara dengan menghapus centang pada kotak "Keep chat history" (Simpan riwayat obrolan). Anda juga dapat mengubah kode Nospam Anda ketika Anda menyadari bahwa Anda sedang mendapatkan spam oleh permintaan pertemanan dengan mengklik tombol "Generate random NoSpam code" (Hasilkan kode NoSpam acak).
- 
![privacy](assets/fr/18.webp)

### Apa yang menjamin kerahasiaan pada Tox?

Protokol Tox menggunakan Distributed Hash Table (DHT) untuk membuat jaringan node terdesentralisasi. Setiap klien Tox adalah bagian dari jaringan DHT dan menyimpan informasi tentang node lainnya. Dalam kasus Tox, DHT menyimpan alamat IP sebagai nilai yang terkait dengan kunci publik Tox (Tox ID). Ini mempermudah pencarian perangkat Klien Tox tanpa harus menanyakan ke server pusat.

Bayangkan Anda menulis kepada pengguna kami `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` yang akan kita sebut **pengguna B**. Klien Tox Anda akan menemukan pengenal ini di tabel Distributed Hash dan mengambil alamat IP yang terkait. Setelah alamat IP ditemukan, klien Tox Anda akan membuat saluran komunikasi terenkripsi langsung dengan perangkat **pengguna B**, atau menggunakan node lain sebagai relai (relay) untuk mencapai **Pengguna B**. Algoritma enkripsi memastikan bahwa, terlepas dari saluran komunikasi, hanya **Pengguna B** yang akan dapat membaca isi pesan Anda.

Jika Anda menikmati penemuan Tox dan dapat memahami bagaimana kegunaannya untuk memperkuat privasi Anda, silakan berikan "suka" pada tutorial ini. Kami juga merekomendasikan tutorial kami tentang Simple Login, sebuah aplikasi yang memungkinkan Anda menerima dan mengirim email secara anonim.

https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41
