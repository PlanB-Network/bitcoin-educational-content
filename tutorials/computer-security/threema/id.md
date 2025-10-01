---
name: Threema
description: Pesan instan yang aman dan anonim
---
![cover](assets/cover.webp)

Didirikan pada tahun 2012 di Swiss, Threema adalah aplikasi pesan instan yang dirancang untuk menjamin privasi dan keamanan. Tidak seperti WhatsApp, Telegram, atau Signal, Threema tidak memerlukan nomor telepon atau alamat email untuk membuat akun. Setiap pengguna memiliki pengenal unik, memungkinkan pendaftaran yang sepenuhnya anonim.

Secara teknis, komunikasi di Threema menggunakan enkripsi end-to-end. Kode aplikasi selulernya sudah bersifat open source sejak tahun 2020, namun infrastruktur servernya tetap  menjadi hak milik dan terpusat. Server-server Threema di-host secara eksklusif di Swiss, (negara yang terkenal dengan kerangka hukum perlindungan datanya yang ketat).
![Image](assets/fr/01.webp)

Threema memiliki klien dasar untuk perangkat Android dan iOS. Selain itu, tersedia pula aplikasi web, serta perangkat lunak untuk sistem operasi Windows, Linux, dan macOS. Namun demikian, untuk menggunakan aplikasi-aplikasi tersebut, pengguna wajib melakukan registrasi awal pada perangkat seluler.

Aplikasi Threema tidak gratis. Aplikasi ini beroperasi dengan model pembelian sekali bayar: seharga €5.99 untuk penggunaan seumur hidup (atau €4.99 apabila dibeli secara langsung). Untuk benar-benar menggunakan Threema secara anonim, metode pembayaran juga perlu bersifat anonim. Oleh karena itu, pengguna dapat membeli kunci aktivasi menggunakan Bitcoin atau uang tunai melalui "*Threema Shop*" untuk mengaktifkan versi Android. Sebaliknya, pada perangkat iOS, pembelian harus dilakukan melalui App Store, mengingat adanya batasan dari pihak Apple terkait monetisasi aplikasi.

Threema juga memiliki versi khusus untuk keperluan bisnis yang disebut "*Threema Work*". Dalam tutorial ini, kita akan berfokus pada versi "Home".

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
| Olvid                | ✅              | ✅              | ✅                   | ✅                         | ❌                          | 🟡(tidak ada direktori pusat) | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                         | N/A                        | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2013              |

*E2EE = Enkripsi End-to-end (End-to-end encryption)*

## Instal Aplikasi Threema

Threema tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:
- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).

Di Android, juga dapat untuk [menginstal melalui APK](https://shop.threema.ch/en/download).

Ada juga [versi komputer](https://threema.ch/download) (MacOS, Linux, dan Windows). Tutorial ini akan menunjukkan kepada Anda cara sinkronisasi keduanya.

## Beli Lisensi Threema

Setelah Anda menginstal aplikasi, jika Anda langsung melalui toko aplikasi, Anda telah membayar lisensi dan seharusnya memiliki akses langsung ke aplikasi tersebut. Jika Anda menggunakan F-Droid atau APK, Anda sekarang perlu membeli lisensi di situs web resminya.

Setelah Anda menginstal aplikasi, jika Anda mengunduh langsung melalui toko aplikasi, berarti Anda sudah membayar lisensi dan seharusnya bisa langsung mengaksesnya. Jika Anda mengunduh melalui F-Droid atau APK, Anda sekarang perlu membeli lisensi di situs web resmi.

[Buka "*Threema Shop*"](https://shop.threema.ch/) dan klik tombol "*Buy Threema for Android / Beli Threema untuk Android*".
![Image](assets/fr/02.webp)

Pilih jumlah lisensi yang ingin Anda beli (cukup satu saja jika hanya untuk Anda), pilih mata uang, dan pilih metode pengiriman lisensi. Anda bisa memilih untuk menerima lisensi melalui email, atau langsung di situs jika Anda ingin tetap anonim. Kemudian klik "*Lanjutkan ke pembayaran*".

Pilih jumlah lisensi yang ingin Anda beli (cukup satu jika hanya untuk Anda sendiri), lalu pilih mata uang yang diinginkan. Selanjutnya, pilih metode pengiriman lisensi. Anda bisa memilih untuk menerima lisensi melalui email, atau langsung di situs jika Anda ingin tetap anonim. Setelah itu, klik "*Proceed to payment*" (Lanjutkan ke pembayaran)
![Image](assets/fr/03.webp)

Pilih metode pembayaran Anda. Dalam kasus saya, saya akan membayar dengan Bitcoin, yang juga saya rekomendasikan Anda lakukan, karena memungkinkan Anda untuk tetap anonim (asalkan Anda menggunakan Bitcoin dengan tepat) dan jauh lebih nyaman daripada pembayaran tunai jarak jauh. Kemudian klik "*Next / Berikutnya*".
![Image](assets/fr/04.webp)

Jika Anda tidak memerlukan Invoice, klik "*Next / Berikutnya*" sekali lagi tanpa memasukkan informasi pribadi apa pun.

Kemudian konfirmasikan pembelian Anda dengan mengklik "*Confirm payment / Konfirmasi pembayaran*".
![Image](assets/fr/05.webp)

Anda kemudian perlu mengirimkan jumlah yang ditunjukkan ke alamat Bitcoin yang diberikan (sayangnya, Lightning belum didukung). Setelah transaksi dikonfirmasi di Blockchain, klik "Close" (Tutup) di samping Invoice.

Anda kemudian akan memiliki akses ke kunci lisensi Anda. Harap diperhatikan: jika Anda belum memasukkan email Address, kunci ini hanya akan ditampilkan di sini. Ingatlah untuk menyimpan URL halaman tersebut agar Anda dapat mengaksesnya nanti jika diperlukan.

Setelah itu, Anda akan memiliki akses ke kunci lisensi Anda. Penting: jika Anda tidak memasukkan alamat e-mail, kunci ini hanya akan ditampilkan di sini. Ingatlah untuk menyimpan URL halaman tersebut agar Anda dapat mengaksesnya nanti jika diperlukan.
![Image](assets/fr/06.webp)

## Buat Akun di Threema

Sekarang setelah Anda memiliki kunci lisensi, Anda akhirnya bisa meluncurkan aplikasinya. Saat pertama kali dibuka, jika Anda tidak membeli Threema melalui toko aplikasi, Anda akan diminta untuk memasukkan kunci lisensi Anda yang sudah dibeli dari situs.
![Image](assets/fr/07.webp)

Kemudian klik tombol "*Set up now / Siapkan sekarang*".
![Image](assets/fr/08.webp)

Gerakkan jari Anda pada layar untuk menghasilkan entropi (keacakan data) yang diperlukan untuk membuat "*Threema ID*".
![Image](assets/fr/09.webp)

"*Threema ID*" Anda akan ditampilkan. Ini akan memungkinkan Anda untuk menghubungi pengguna lain. Klik "*Next / Berikutnya*".
![Image](assets/fr/10.webp)

Pilih sebuah kata sandi. Ini akan memungkinkan Anda memulihkan akses ke akun Anda jika sewaktu-waktu diperlukan. Buatlah kata sandi Anda sepanjang dan seacak mungkin, dan simpan salinannya di tempat yang aman, misalnya di pengelola kata sandi.
![Image](assets/fr/11.webp)

Kemudian pilih nama pengguna, yang dapat berupa nama asli atau nama samaran.
![Image](assets/fr/12.webp)

Anda kemudian dapat menautkan ID Threema Anda ke nomor telepon Anda. Ini memudahkan Anda untuk mencari melalui kontak Anda, tetapi jika Anda menggunakan Threema, ini juga untuk menjaga anonimitas Anda: jadi yang terbaik adalah tidak menautkannya. Klik pada "*Selanjutnya*".

Anda kemudian dapat menautkan ID Threema Anda ke nomor telepon Anda. Ini akan memudahkan Anda mencari melalui kontak Anda. Namun, jika Anda menggunakan Threema, tujuannya juga untuk menjaga anonimitas Anda, jadi lebih baik untuk tidak menautkannya. Klik "*Next / Selanjutnya*".
![Image](assets/fr/13.webp)

Setelah Anda menyelesaikan langkah ini, klik "*Finish / Selesai*".
![Image](assets/fr/14.webp)

Anda sekarang sudah terhubung ke Threema dan dapat mulai berkomunikasi.
![Image](assets/fr/15.webp)

## Pengaturan Threema

Pertama-tama, akses pengaturan dengan mengeklik tiga titik kecil di sudut kanan atas, kemudian pilih "*Settings / Pengaturan*".
![Image](assets/fr/16.webp)

Pada tab "*Privacy / Privasi*", Anda akan menemukan beberapa opsi untuk menyesuaikan dengan kebutuhan Anda:
- Menyinkronkan kontak pada ponsel Anda;
- Menerima pesan dari orang yang tidak dikenal;
- Indikator penulisan selama entri data;
- Pemberitahuan penerimaan pesan ...
![Image](assets/fr/17.webp)

Pada tab "*Security / Keamanan*", saya sarankan untuk mengaktifkan opsi "*Locking mechanism / Mekanisme penguncian*" untuk melindungi akses ke aplikasi. Juga disarankan untuk mengaktifkan passphrase untuk mengamankan cadangan lokal Anda.
![Image](assets/fr/18.webp)

Jangan ragu untuk menjelajahi bagian lain dari pengaturan untuk menyesuaikan aplikasi dengan preferensi Anda.
![Image](assets/fr/19.webp)

## Mencadangkan Akun Threema Anda

Sebelum Anda mulai berkirim pesan, penting untuk merencanakan cara memulihkan akun Anda, terutama jika ponsel Anda diganti atau hilang. Untuk melakukannya, klik tiga titik di kanan atas antarmuka, lalu akses menu "*Backups / Cadangan*".
![Image](assets/fr/20.webp)

Di sini Anda akan menemukan dua opsi untuk mencadangkan data Anda:
- "*Threema Safe / Threema Aman*";
- "*Data Backup / Cadangan Data*".

"*Threema Safe*" menyimpan semua informasi akun Anda, kecuali percakapan Anda, di server Threema. Data ini dienkripsi dengan kata sandi yang Anda pilih saat membuat akun, memastikan Threema tidak memiliki akses ke data tersebut. Pencadangan dilakukan secara otomatis dan teratur.

Dengan "*Threema Safe*", untuk memulihkan akun Anda di perangkat baru, Anda hanya perlu memasukkan Threema ID dan kata sandi Anda. Jika salah satu dari informasi ini hilang, maka tidak mungkin untuk memulihkan akun Anda.

Opsi ini hanya memungkinkan Anda untuk memulihkan ID, profil, kontak, grup, dan pengaturan tertentu, tetapi **bukan riwayat percakapan**.

Untuk mengaktifkan "*Threema Safe*", cukup centang opsi di menu "*Backups / Cadangan*".
![Image](assets/fr/21.webp)

Apabila Anda juga ingin untuk mencadangkan dan memulihkan riwayat percakapan Anda, opsi "Data Backup / Cadangan Data" perlu digunakan. Fitur ini akan menghasilkan cadangan lengkap akun Anda yang tersimpan secara lokal pada ponsel Anda. Anda kemudian perlu mentransfer cadangan ini ke perangkat baru dan menggunakan kata sandi (dan mungkin passphrase) untuk memulihkan seluruh akun Anda.

Karena cadangan ini hanya bersifat lokal, sangat disarankan untuk secara teratur menyalinnya ke media eksternal. Jika tidak, apabila perangkat Anda hilang, pemulihan akun tidak akan mungkin dilakukan. Oleh karena itu, metode ini lebih cocok untuk proses transfer yang terencana dari satu perangkat ke perangkat lain, dibandingkan untuk situasi darurat.

Harap diperhatikan: "*Data Backup /Cadangan Data*" hanya berfungsi jika Anda menggunakan sistem operasi yang sama. Anda tidak akan dapat menggunakannya, misalnya, untuk bermigrasi dari Samsung ke iPhone.

## Sesuaikan profil Threema Anda

Di sudut kiri atas tampilan, klik foto profil Anda, kemudian pilih "*My Profile / Profil Saya*".
![Image](assets/fr/22.webp)

Di sini Anda bisa menyesuaikan profil Anda: menambahkan foto, memilih siapa yang bisa melihatnya, atau melihat login Threema Anda.
![Image](assets/fr/23.webp)

## Menyinkronkan perangkat lunak PC

Jika Anda ingin mengakses percakapan Anda di PC, Anda dapat menyinkronkan akun Threema Anda dengan perangkat lunak khusus. Unduh perangkat lunak untuk sistem operasi Anda [dari situs web resmi](https://threema.ch/en/download).
![Image](assets/fr/24.webp)

Pada ponsel Anda, klik pada tiga titik di kanan atas, lalu buka menu "*Threema 2.0 for Desktop / Threema 2.0 untuk Desktop*".
![Image](assets/fr/25.webp)

Klik "*Add device / Tambahkan perangkat*", lalu gunakan ponsel Anda untuk memindai kode QR yang ditampilkan oleh perangkat lunak di komputer Anda.
![Image](assets/fr/26.webp)

Untuk mengonfirmasi sinkronisasi, klik grup emoji yang ditampilkan dalam perangkat lunak.
![Image](assets/fr/27.webp)

Pada komputer Anda, masuk menggunakan kata sandi Anda.
![Image](assets/fr/28.webp)

Selain aplikasi seluler, Anda sekarang dapat mengakses akun Threema langsung dari komputer Anda.
![Image](assets/fr/29.webp)

## Mengirim Pesan Dengan Threema

Setelah semuanya diatur dengan benar, Anda dapat mulai berkomunikasi. Klik tombol "*Start chat / Mulai obrolan*".
![Image](assets/fr/30.webp)

Pilih "*New contact / Kontak baru*".
![Image](assets/fr/31.webp)

Masukkan atau pindai "*Threema ID*" penerima Anda.
![Image](assets/fr/32.webp)

Klik ikon pesan.
![Image](assets/fr/33.webp)

Kirim pesan pertama ke penerima Anda.
![Image](assets/fr/34.webp)

Ketika penerima Anda menjawab, koneksi akan terjalin, dan Anda akan dapat melihat nama dan foto profilnya. Anda kemudian dapat mengirim pesan, file multimedia, dan bahkan melakukan panggilan.
![Image](assets/fr/35.webp)

Selamat, Anda sekarang sudah mahir menggunakan aplikasi pesan Threema, sebuah alternatif yang bagus daripada WathsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di sosial media Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain , di mana saya memperkenalkan Anda pada Proton Mail, sebuah alternatif yang jauh lebih ramah privasi daripada Gmail:

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
