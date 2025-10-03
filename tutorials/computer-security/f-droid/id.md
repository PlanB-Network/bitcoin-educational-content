---
name: F-Droid
description: Katalog aplikasi gratis dan sumber terbuka.
---

![cover](assets/cover.webp)

Di era digital, perusahaan dan institusi besar berupaya membuat Internet lebih tersentralisasi, menempatkan kendalinya di tangan mereka sendiri, dan dengan demikian menghambat privasi serta kebebasan semua pengguna. Ini bukan utopia, ini sudah terjadi. Sebagai seorang bitcoiner, desentralisasi, penghormatan terhadap privasi dan kebebasan individu adalah prinsip-prinsip yang Anda junjung tinggi, terutama dalam alat yang Anda gunakan setiap hari. Android, tidak seperti iOS, selama bertahun-tahun telah memungkinkan beberapa toko aplikasi untuk hidup berdampingan di dalam ekosistemnya, memberi Anda kebebasan untuk menemukan dan memasang aplikasi dari sumber favorit Anda.

Dalam tutorial ini, kita akan melihat F-droid, direktori aplikasi yang mewakili alternatif dari toko aplikasi seperti Google Play Store dan Microsoft Store.

## Memulai dengan F-Droid

F-Droid adalah toko aplikasi dan aplikasi yang memungkinkan Anda memasang aplikasi open source dan gratis di platform Android. F-droid sendiri adalah proyek sumber terbuka yang dimulai pada tahun 2010 oleh Ciaran Gultnieks dan beberapa kontributor lainnya. Tujuan utama dari proyek ini adalah untuk membuat aplikasi open source dapat diakses, dan untuk memungkinkan inisiator proyek open source menemukan platform tempat mereka dapat menerbitkan aplikasi mereka tanpa harus merujuk ke Google Play Store.

Sayangnya, F-Droid bukanlah aplikasi yang tersedia di iOS, dan berisi banyak aplikasi yang dirancang untuk sistem Android.

Anda dapat mengunduh F-droid dari [situs web resmi](https://f-droid.org/) dalam format APK dan menginstalnya secara manual di ponsel Android Anda.

![download](assets/fr/02.webp)

Pada Android, pastikan Anda memberikan izin instalasi untuk browser dari mana Anda mengunduh F-Droid.

Setelah instalasi selesai, F-Droid akan meluncurkan pembaruan direktori aplikasi open source untuk memperkaya aplikasi di toko.

![repositories](assets/fr/03.webp)

Anda sekarang dapat memasang aplikasi di smartphone Anda tanpa melalui Google Play Store.



## Toko Aplikasi F-Droid

Di Toko Aplikasi, Anda akan menemukan beberapa kategori aplikasi yang sesuai dengan kebutuhan Anda. Di tab **Categories**, Anda akan menemukan lebih dari 20 jenis aplikasi, mulai dari browser hingga editor teks gratis, dan semuanya membutuhkan informasi paling sedikit dari pihak Anda.

Apakah Anda ingin memasang aplikasi tertentu? Klik tombol **Search**, lalu masukkan nama aplikasi yang Anda cari.

![search](assets/fr/04.webp)

F-Droid menyediakan informasi yang komprehensif tentang setiap aplikasi yang ingin Anda instal.

Dengan mengklik aplikasi, Anda akan menemukan, antara lain:

- Fitur dan perubahan yang ditambahkan dalam versi terbaru yang tersedia
- Deskripsi rinci aplikasi, fiturnya, alasan untuk menggunakannya, dan komunitas Open Source di balik proyek tersebut.

![features](assets/fr/05.webp)
  
- Lisensi yang digunakan oleh proyek, tautan ke kode sumber, dan ke masalah yang ditemui saat menggunakan aplikasi
- Izin yang dibutuhkan oleh aplikasi

![permissions](assets/fr/06.webp)

Cari tahu lebih lanjut di tutorial Thunderbird kami:

https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid memberi Anda semua informasi yang Anda butuhkan untuk memutuskan apakah menggunakan aplikasi melindungi data Anda dan meningkatkan privasi Anda. Pindai semua aplikasi yang ingin Anda gunakan, lalu klik tombol **Install** untuk mengunduh dan memasang aplikasi Anda.

Berikan hak instalasi F-Droid dengan mengaktifkan opsi di pengaturan Anda.

![settings](assets/fr/07.webp)

## Berbagi aplikasi Anda

F-Droid mendorong penggunaan open source dan kontribusi komunitas, terutama melalui opsi pertukaran "**Near By**". Terhubung dengan pengguna di sekitar Anda melalui:

- Deteksi Bluetooth;
- Jaringan Wi-Fi yang sama;
- Kode QR atau alamat IP:PORT untuk dimasukkan ke dalam browser Anda.

Dengan opsi ini, Anda dapat berbagi dan menerima aplikasi yang terpasang di smartphone Android Anda dengan teman dan keluarga hanya dalam beberapa langkah.

![swap](assets/fr/08.webp)

## Pembaruan

Di tab **Update**, periksa daftar pembaruan yang tersedia, dan pastikan Anda juga membaca informasi tentang versi baru setiap aplikasi untuk mengetahui perubahan besar apa pun pada versi yang Anda gunakan.

![updates](assets/fr/09.webp)

Anda juga dapat memperbarui daftar aplikasi yang tersedia dengan menyegarkan halaman (swipe ke bawah).

## Tambahkan aplikasi Anda sendiri

F-Droid adalah proyek open source yang mendorong kontribusi pada aplikasi yang memprioritaskan privasi pengguna. Anda dapat menambahkan aplikasi smartphone Android Anda sendiri ke toko melalui kontribusi ke kode sumber F-Droid di GitLab.

Aplikasi Anda harus open source, dengan source code yang tersedia secara publik di GitHub atau GitLab, misalnya.

Anda kemudian harus menyiapkan file YAML (metadata) yang menjelaskan aplikasi Anda, termasuk semua informasi dan izin yang diperlukan untuk penggunaannya, mengikuti [template metadata](https://f-droid.org/docs/Build_Metadata_Reference/) yang diusulkan oleh F-Droid.

Di bagian **Developers** pada [dokumentasi] (https://f-droid.org/en/docs/), Anda akan menemukan semua sumber daya yang Anda butuhkan untuk menerbitkan dan memelihara aplikasi Anda di F-Droid.

### Integritas dan keamanan

Menjadikan aplikasi open source sering kali identik dengan peningkatan keamanan, tetapi juga dengan risiko yang cukup besar. Bagaimana Anda dapat memastikan bahwa tidak ada perubahan berbahaya pada source code aplikasi yang tersedia di F-Droid?

F-Droid mengompilasi aplikasi di server mereka sendiri, berdasarkan source code resmi dan instruksi kompilasi. Setiap aplikasi yang diterbitkan dibangun kembali dan diverifikasi untuk memastikan bahwa itu tidak disusupi. Ini memastikan bahwa APK yang ditawarkan sesuai dengan source code yang diterbitkan oleh para developer. Terlebih lagi, setiap aplikasi yang dipasang melalui F-Droid ditandatangani secara digital, dan kemudian fingerprint tanda tangan dibandingkan dengan yang diumumkan oleh developer aplikasi di situs web resmi atau di repositori Git.

Jika Anda menikmati tutorial ini, cari tahu lebih lanjut tentang kursus keamanan TI dan manajemen data kami:

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
