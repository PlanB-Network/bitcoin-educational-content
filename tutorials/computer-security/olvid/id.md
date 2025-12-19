---
name: Olvid
description: Pesan pribadi untuk semua orang
---

![cover](assets/cover.webp)

Olvid adalah aplikasi pesan instan asal Prancis yang diluncurkan pada tahun 2019, dirancang dengan menawarkan tingkat keamanan tinggi tanpa mengorbankan privasi. Berbeda dengan WhatsApp atau Signal, Olvid tidak meminta data pribadi apa pun saat pendaftaran: tidak ada nomor telepon, tidak ada alamat email, tidak ada sama sekali. Identifikasi antar pengguna didasarkan pada pertukaran kunci, tanpa server direktori atau buku alamat bersama.

Semua pesan dienkripsi ujung-ke-ujung (encrypted end-to-end ) menggunakan protokol kriptografi orisinal, yang juga dirancang untuk melindungi metadata: tidak ada yang tahu dengan siapa Anda berbicara, atau kapan. Kode klien bersifat open source, namun server pusat yang digunakan untuk merutekan pesan terenkripsi tetap milik sendiri dan di-hosting di AWS.

Model keamanan Olvid didasarkan pada prinsip utama: tidak adanya pihak ketiga tepercaya dalam pembentukan identitas digital. Berbeda dengan sebagian besar aplikasi pesan terenkripsi yang mengandalkan penyimpanan terpusat untuk mengelola identitas pengguna, Olvid tidak bergantung pada infrastruktur terpusat apa pun untuk memastikan integritas komunikasi. Arsitektur ini menghilangkan risiko yang terkait dengan kebocoran penyimpanan.

Meskipun demikian, Olvid menggunakan server distribusi pesan pusat yang secara ketat terbatas pada peran logistik: yang menangani transmisi pesan terenkripsi secara asinkron. Server ini tidak berperan dalam proses enkripsi, tidak mengetahui identitas asli pengguna maupun konten atau metadata pesan (kecuali kunci publik penerima, yang diperlukan untuk perutean). Oleh karena itu, server ini dapat dianggap tidak tepercaya secara default tanpa mengorbankan keamanan sistem secara keseluruhan. Bahkan jika server ini disusupi, ia tidak akan memberikan akses ke isi pesan. Olvid dengan demikian mengadopsi sentralisasi untuk pengiriman pesan (demi efisiensi dan kualitas layanan), sambil menjamin keamanan yang independen dari infrastruktur ini.

Olvid menawarkan versi gratis dan versi berlangganan seharga €4,99 per bulan. Versi gratis menawarkan fungsionalitas penuh, dengan pengecualian tidak dapat melakukan panggilan audio dan video (meskipun masih mungkin untuk menerimanya), dan tidak mengizinkan sinkronisasi akun di beberapa perangkat. Jadi, jika Anda berencana menggunakan ponsel cerdas Anda secara eksklusif, dan tidak perlu melakukan panggilan, Olvid adalah solusi yang sangat tepat.

Olvid telah tersertifikasi oleh ANSSI (otoritas keamanan siber Prancis). Aplikasi ini adalah alternatif yang sangat baik untuk layanan pesan tradisional (WhatsApp, Facebook Messenger, WeChat...) bagi mereka yang mencari privasi dengan tetap mempertahankan kesederhanaan penggunaan.


| Aplikasi             | E2EE 1:1       | E2EE grup      | Pendaftaran anonim  | Lisensi open-source Pengguna | Lisensi open-source Server | Server terdesentralisasi | Tahun pembuatan   |
| -------------------- | -------------- | -------------- | ------------------- | ------------------------- | -------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opsional) | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Telegram             | 🟡 (opsional) | ❌              | 🟡                  | ✅                         | ❌                          | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                         | ✅                          | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                         | ❌                          | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (gabungan)        | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                         | N/A                        | 🟡 (melalui email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (gabungan)        | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2021              |
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                         | **❌**                          | **🟡(tidak ada direktori pusat)** | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                         | N/A                        | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2013              |

*E2EE = Enkripsi End-to-end (End-to-end encryption)*

## Instal aplikasi Olvid

Olvid tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:

- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);

Di Android, juga memungkinkan untuk [menginstal melalui APK](https://www.olvid.io/download/).

Dalam tutorial ini, kita akan berfokus pada versi seluler. Namun, perlu diketahui bahwa [versi komputer juga tersedia](https://www.olvid.io/download/) (macOS, Linux, dan Windows). Jika Anda memilih versi berbayar, Anda dapat menyinkronkan akun Anda di beberapa perangkat.
![Image](assets/fr/01.webp)

## Buat akun di Olvid

Ketika Anda menggunakan aplikasi untuk pertama kalinya, klik tombol "*Saya pengguna baru(I am a new user)*".
![Image](assets/fr/02.webp)

Pilih nama panggilan atau masukkan nama depan dan belakang Anda.
![Image](assets/fr/03.webp)

Tambahkan foto profil.
![Image](assets/fr/04.webp)

Akun Anda sekarang sudah dibuat.
![Image](assets/fr/05.webp)

Untuk mencegah hilangnya akses ke akun Olvid Anda, kami sarankan untuk mengatur pencadangan otomatis. Caranya, buka pengaturan dengan mengeklik tiga titik di kanan atas antarmuka, lalu pilih "*Settings*" (Pengaturan).

⚠️ **Perhatian**: sejak versi 3.7 Olvid, prosedur untuk mencadangkan profil dan kontak Anda telah digantikan dengan yang baru. Tutorial ini masih menyajikan versi lama. Anda dapat menemukan versi baru di FAQ mereka: [💾 Mencadangkan profil Anda](https://www.olvid.io/faq/sauvegarder-vos-profils/)
![Image](assets/fr/06.webp)

Buka menu "*Save keys and contacts (Simpan kunci dan kontak)*".
![Image](assets/fr/07.webp)

Kemudian klik "*Generate a backup key (hasilkan kunci cadangan)*". Kunci ini akan mengenkripsi cadangan Anda. Jika Anda perlu memulihkan akun di perangkat lain dan tidak lagi memiliki akses ke sana, Anda akan memerlukan cadangan dan kunci ini untuk mendekripsinya.
![Image](assets/fr/08.webp)

Simpan kunci ini di tempat yang aman. Anda juga dapat membuat salinan kertas.
![Image](assets/fr/09.webp)

Anda kemudian dapat memilih untuk membuat cadangan lokal atau cadangan otomatis pada layanan cloud. Opsi kedua ini sangat direkomendasikan untuk menjamin akses ke akun Olvid Anda dalam segala situasi, bahkan jika Anda kehilangan ponsel Anda.
![Image](assets/fr/10.webp)

Pastikan opsi "*Enable automatic backup (aktifkan pencadangan otomatis)*" dicentang.
![Image](assets/fr/11.webp)

Anda juga dapat menjelajahi pengaturan lain yang tersedia untuk menyesuaikan aplikasi sesuai kebutuhan Anda.
![Image](assets/fr/12.webp)

## Mengirim pesan dengan Olvid

Untuk dapat mengirim pesan, Anda harus menambahkan kontak terlebih dahulu. Dari halaman utama, klik tombol biru "*+*".
![Image](assets/fr/13.webp)

Olvid kemudian akan menampilkan ID pengguna Anda. Anda bisa memberikannya kepada orang yang ingin Anda ajak berkomunikasi agar mereka dapat menambahkan Anda sebagai kontak.

Untuk menambahkan seseorang, pindai ID mereka dengan kamera Anda, atau tempelkan secara manual dengan mengeklik tiga titik kecil di sudut kanan atas.
![Image](assets/fr/14.webp)

Setelah ID berhasil dipindai, Anda dapat meminta kontak Anda untuk memindai kode QR yang ditampilkan, atau Anda bisa mengirimkan permintaan koneksi jarak jauh dengan mengeklik "*Remote contact*" (Kontak Jarak Jauh).
![Image](assets/fr/15.webp)

Koneksi sekarang sudah terbentuk.
![Image](assets/fr/16.webp)

Sekarang Anda bisa mulai bertukar pesan dan konten lainnya dengan kenalan Anda!
![Image](assets/fr/17.webp)

Dari halaman beranda, Anda akan menemukan semua percakapan Anda.
![Image](assets/fr/18.webp)

Tab kedua berisi semua kontak Anda.
![Image](assets/fr/19.webp)

Anda juga dapat membuat diskusi kelompok.
![Image](assets/fr/20.webp)

Selamat, Anda sekarang sudah mahir menggunakan pesan Olvid, sebuah alternatif yang bagus selain WathsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!

Selamat! Kini Anda telah memahami cara menggunakan Olvid messaging, sebuah alternatif yang hebat selain WhatsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda dapat memberikan jempol hijau di bawah. Jangan ragu untuk membagikan tutorial ini di sosial media Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain, di mana saya memperkenalkan Anda pada Proton Mail, sebuah alternatif yang jauh lebih ramah privasi dibandingkan Gmail:

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
