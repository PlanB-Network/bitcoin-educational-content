---
name: Tox
description: Buka percakapan tanpa perantara pada protokol Tox yang terdesentralisasi
---
![cover](assets/cover.webp)



Enkripsi end-to-end adalah layanan yang ditawarkan oleh banyak aplikasi perpesanan seperti WhatsApp dan Telegram. Enkripsi di sini berarti bahwa sebelum pesan dikirim oleh pengirim, pesan tersebut diamankan dengan kunci kriptografi yang hanya dimiliki oleh penerima. Hari ini kita akan menemukan sebuah aplikasi perpesanan terenkripsi yang sepenuhnya terdesentralisasi, end-to-end, berdasarkan prinsip-prinsip yang mirip dengan Blockchain, untuk menawarkan komunikasi terenkripsi yang aman dan end-to-end tanpa perantara: Tox Chat.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Enkripsi ujung ke ujung*



## Apa itu Tox?



Tox adalah protokol komunikasi terdesentralisasi gratis (open source) yang menggunakan teknologi *Networking and Cryptography Library* (NaCl) ditambah dengan kombinasi algoritma enkripsi untuk memastikan keamanan dan kerahasiaan penggunanya. Tox memungkinkan Anda mengirim pesan teks Exchange, melakukan panggilan audio dan video, berbagi file, dan berbagi layar dengan teman secara aman, terdesentralisasi, dan tanpa perantara.



Teknologi yang digunakan protokol Tox mirip dengan jaringan peer-to-peer seperti blockchain, yang mendukung desentralisasi infrastruktur protokol. Tidak seperti jejaring sosial dan aplikasi pesan terenkripsi end-to-end, aplikasi Tox Chat dibangun di atas protokol terdesentralisasi yang tidak memiliki server pusat. Semua pengguna berkomunikasi dalam jaringan peer-to-peer yang bebas perantara dan tahan sensor. Untuk berkomunikasi, setiap pengguna diidentifikasi dengan ID unik (ToxID) yang berasal dari kunci publiknya, yang disimpan dalam tabel Hash yang didistribusikan.



## Bergabunglah dengan Tox



Anda dapat menggunakan protokol Tox melalui klien pesan instan yang dapat Anda unduh dari [situs Tox Chat](https://tox.chat).



![download](assets/fr/01.webp)



Tergantung pada sistem operasi Anda, Anda dapat mengunduh dan menginstal klien Tox yang cocok dengan:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), klien Tox yang ditulis dalam bahasa Kotlin yang hanya tersedia di Android



![aTox](assets/fr/02.webp)





- qTox: Klien Tox dari [open source] (https://github.com/TokTok/qTox) yang berbasiskan Qt Framework (C++) yang tersedia di Windows, Linux, MacOS.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic] (https://github.com/JFreegman/toxic) adalah klien Tox yang ditulis dalam bahasa C dan berjalan pada sistem dengan antarmuka baris perintah.



![Toxic](assets/fr/04.webp)



Dalam tutorial ini, kita akan menggunakan klien qTox pada Windows dan aTox untuk berkomunikasi.



## Memulai dengan qTox



Setelah diunduh, instal klien Tox Anda dan buat profil Anda.



![qTox-acount](assets/fr/05.webp)



Selamat, Anda baru saja bergabung dengan protokol Tox. Pada perangkat lunak qTox, Anda dapat menemukan informasi profil Anda dengan mengeklik nama pengguna Anda.



![profil](assets/fr/06.webp)



Secara khusus, Anda akan menemukan Tox ID Anda, yang dapat Anda simpan sebagai kode QR dan bagikan dengan orang-orang yang ingin menghubungi Anda.



Ekspor file profil Tox Anda sehingga Anda memiliki cadangan profil dan informasi kontak yang dapat Anda gunakan untuk memulihkan. Klik tombol **Export**, lalu pilih jalur ke file cadangan Anda.



![export](assets/fr/07.webp)



Dari menu **Lainnya**, tambahkan teman, impor kontak, dan kelola permintaan pertemanan yang Anda terima.



![friends](assets/fr/08.webp)



Anda bisa menghubungi saya melalui Tox ID ini misalnya: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Setelah permintaan pertemanan dikirim, penerima harus menerima atau menolak permintaan Anda sebelum Anda dapat menghubungi mereka.



![request](assets/fr/09.webp)



Klien Tox Anda mencakup semua opsi yang ditawarkan oleh aplikasi pesan instan:





- Panggilan video





- Panggilan suara





- Berbagi file





- emoji



![chat](assets/fr/10.webp)



### Kelompok rekan kerja



Klien Tox Anda juga memungkinkan Anda untuk berkomunikasi dengan sekelompok orang dengan cara yang sepenuhnya terdesentralisasi: ini disebut konferensi. Di menu **Groups**, buat konferensi baru atau lihat daftar undangan untuk bergabung dengan konferensi yang telah Anda terima.



![conferences](assets/fr/11.webp)



Setelah konferensi dibuat, Anda dapat mengundang teman Anda untuk bergabung dengan konferensi di klien Tox Anda. Dalam daftar teman Anda, klik kanan pada nama pengguna teman yang ingin Anda undang. Klik opsi **Unggah ke konferensi**, lalu pilih nama konferensi yang telah Anda buat. Anda juga dapat mengundang teman dengan membuat konferensi secara implisit dengan opsi **Buat konferensi baru**.



⚠️ Klien Tox masih dalam tahap pengembangan, sehingga Anda mungkin akan mengalami kesalahan saat berinteraksi dengan perangkat lunak. Fungsi konferensi dan panggilan video belum tersedia di klien Android Tox (aTox).



![invite](assets/fr/12.webp)



### Transfer file



Di menu **Transfer file**, Anda akan menemukan riwayat file yang telah Anda kirim dan yang telah Anda terima dari kontak Anda.



![files](assets/fr/13.webp)



Anda juga dapat menyesuaikan konfigurasi berbagi file untuk setiap diskusi yang Anda lakukan. Klik kanan pada nama pengguna penerima dan pilih "Tampilkan detail lebih lanjut".



![details](assets/fr/14.webp)



Dari detail Interface, Anda dapat mengelola otorisasi yang Anda berikan kepada penerima untuk file:





- Penerimaan otomatis undangan konferensi.





- Penerimaan file otomatis.





- Jalur cadangan untuk file diskusi Anda.



![permissions](assets/fr/15.webp)



### Lebih banyak parameter



Di menu **Pengaturan**, Anda dapat menyesuaikan pengaturan klien Tox Anda.





- Pada bagian **Umum**, ubah bahasa dasar klien Tox Anda, tentukan jalur pencadangan file dan ukuran file maksimum yang akan diterima secara otomatis.



![general](assets/fr/16.webp)





- Pada bagian **Pengguna Interface**, ubah font dan ukuran pesan Anda. Anda juga dapat mengubah tema klien Tox Anda.



![ui](assets/fr/17.webp)





- Tab **Privasi** memungkinkan Anda menentukan pesan yang bersifat sementara dengan menghapus centang pada kotak "Simpan riwayat obrolan". Anda juga dapat mengubah kode Nospam Anda ketika Anda menyadari bahwa Anda menerima spam dari permintaan pertemanan dengan mengeklik tombol "generate kode NoSpam acak".



![privacy](assets/fr/18.webp)



### Apa yang menjamin kerahasiaan pada Tox?



Protokol Tox menggunakan Tabel Hash Terdistribusi untuk membuat jaringan node yang terdesentralisasi. Setiap klien Tox adalah bagian dari jaringan DHT dan menyimpan informasi tentang node lain. Dalam kasus Tox, DHT menyimpan alamat IP sebagai nilai yang terkait dengan kunci publik Tox (Tox ID). Hal ini memudahkan untuk mencari perangkat Klien Tox tanpa harus meminta server pusat.



Bayangkan menulis kepada pengguna kita `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` yang akan kita beri nama **pengguna B**. Klien Tox Anda akan mencari pengenal ini di tabel Hash Distributed dan mengambil IP Address yang terkait. Setelah IP Address ditemukan, klien Tox Anda akan membuat saluran komunikasi terenkripsi langsung dengan mesin **pengguna B**, atau menggunakan node lain sebagai relay untuk mencapai **Pengguna B**. Algoritma enkripsi memastikan bahwa, terlepas dari saluran komunikasi, hanya **Pengguna B** yang dapat membaca isi pesan Anda.



Jika Anda telah menikmati menemukan Tox dan telah mampu memahami bagaimana ia berguna untuk memperkuat privasi Anda, silakan berikan jempol pada tutorial ini. Kami juga merekomendasikan tutorial kami tentang Login Sederhana, sebuah alat yang memungkinkan Anda menerima dan mengirim email secara anonim.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41