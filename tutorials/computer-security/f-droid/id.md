---
name: F-Cold
description: Katalog aplikasi gratis dan sumber terbuka.
---

![cover](assets/cover.webp)



Di era digital, perusahaan dan institusi besar bekerja untuk membuat Internet menjadi lebih tersentralisasi, menempatkan kontrolnya di tangan mereka sendiri, dan dengan demikian menghambat privasi dan kebebasan semua pengguna. Ini bukan utopia, ini sudah terjadi. Sebagai seorang bitcoiner, desentralisasi, penghormatan terhadap privasi dan kebebasan individu merupakan prinsip-prinsip yang Anda junjung tinggi, terutama pada perangkat yang Anda gunakan sehari-hari. Android, tidak seperti iOS, selama bertahun-tahun mengizinkan beberapa toko aplikasi untuk hidup berdampingan dalam ekosistemnya, memberikan Anda kebebasan untuk menemukan dan menginstal aplikasi dari sumber favorit Anda.



Dalam tutorial ini, kita akan melihat F-droid, direktori aplikasi yang merupakan alternatif dari toko aplikasi seperti Google Play Store dan Microsoft Store.



## Memulai dengan F-Droid



F-Droid adalah sebuah toko aplikasi dan peralatan yang memungkinkan Anda menginstal aplikasi sumber terbuka gratis pada platform Android. F-droid sendiri merupakan proyek open source yang dimulai pada tahun 2010 oleh Ciaran Gultnieks dan beberapa kontributor lainnya. Tujuan utama dari proyek ini adalah untuk membuat aplikasi open source dapat diakses, dan untuk memungkinkan para penggagas proyek open source untuk menemukan sebuah platform di mana mereka dapat mempublikasikan alat mereka tanpa harus merujuk ke Google Play Store.



Sayangnya, F-Droid bukanlah aplikasi yang tersedia di iOS, dan berisi banyak alat yang dirancang untuk sistem Android.



Anda dapat mengunduh F-droid dari [situs web resmi] (https://f-droid.org/) dalam format APK dan menginstalnya secara manual di ponsel Android Anda.



![download](assets/fr/02.webp)



Di Android, pastikan Anda memberikan izin pemasangan untuk peramban yang Anda unduh F-Droid.



Setelah instalasi selesai, F-Droid akan meluncurkan pembaruan direktori aplikasi Open Source untuk memperkaya aplikasi di toko.



![repositories](assets/fr/03.webp)



Sekarang Anda dapat menginstal aplikasi di ponsel tanpa melalui Google Play Store.



## Toko buku F-Droid



Di Toko Aplikasi, Anda akan menemukan beberapa kategori aplikasi yang sesuai dengan kebutuhan Anda. Pada tab **Kategori**, Anda akan menemukan lebih dari 20 jenis aplikasi, mulai dari peramban hingga editor teks gratis, dan semuanya membutuhkan sedikit informasi dari Anda.



Apakah Anda ingin menginstal aplikasi tertentu? Klik tombol **Cari**, lalu masukkan nama aplikasi yang Anda cari.



![search](assets/fr/04.webp)



F-Droid menyediakan informasi yang komprehensif tentang setiap aplikasi yang ingin Anda instal.



Dengan mengeklik aplikasi, Anda akan menemukan, antara lain:




- Fitur dan perubahan yang ditambahkan dalam versi terbaru yang tersedia
- Penjelasan rinci tentang aplikasi, fitur-fiturnya, alasan penggunaannya, dan komunitas Open Source di balik proyek ini.



![features](assets/fr/05.webp)





- Lisensi yang digunakan oleh proyek, tautan ke kode sumber dan masalah yang dihadapi saat menggunakan aplikasi
- Izin yang diperlukan oleh aplikasi



![permissions](assets/fr/06.webp)



Cari tahu lebih lanjut di tutorial Thunderbird kami:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid memberikan semua informasi yang Anda perlukan untuk memutuskan apakah menggunakan sebuah aplikasi akan melindungi data Anda dan meningkatkan privasi Anda. Pindai semua aplikasi yang ingin Anda gunakan, lalu klik tombol **Instal** untuk mengunduh dan menginstal aplikasi Anda.


Berikan hak instalasi F-Droid dengan mengaktifkan opsi di pengaturan Anda.



![settings](assets/fr/07.webp)



## Exchange aplikasi Anda



F-Droid mendorong praktik open source dan kontribusi komunitas, terutama melalui opsi **Near By** Exchange. Terhubung dengan pengguna di sekitar Anda melalui:




- Deteksi Bluetooth;
- Jaringan Wi-Fi yang sama;
- Kode QR atau IP: PORT Address untuk dimasukkan ke browser Anda.



Dengan opsi ini, Anda dapat berbagi dan menerima aplikasi yang terinstal di ponsel Android dengan teman dan keluarga hanya dalam beberapa langkah.



![swap](assets/fr/08.webp)



## Pembaruan



Pada tab **Update**, lihat daftar pembaruan yang tersedia, dan pastikan Anda juga membaca informasi tentang versi baru setiap aplikasi untuk mengetahui perubahan besar pada versi yang Anda gunakan.



![updates](assets/fr/09.webp)



Anda juga dapat memperbarui daftar aplikasi yang tersedia dengan menyegarkan halaman (gulir ke bawah).



## Tambahkan aplikasi Anda sendiri



F-Droid adalah proyek Open Source yang mendorong kontribusi pada aplikasi yang memprioritaskan privasi pengguna. Anda dapat menambahkan aplikasi seluler Android Anda sendiri ke toko melalui kontribusi ke kode sumber F-Droid GitLab.



Aplikasi Anda harus bersifat open source, dengan kode sumber yang tersedia untuk umum di GitHub atau GitLab, misalnya.


Anda kemudian harus menyiapkan file YAML (metadata) yang menjelaskan aplikasi Anda, termasuk semua informasi dan izin yang diperlukan untuk penggunaannya, dengan mengikuti [template metadata] (https://f-droid.org/docs/Build_Metadata_Reference/) yang diusulkan oleh F-Droid.



Di bagian **Pengembang** pada [dokumentasi] (https://f-droid.org/en/docs/), Anda akan menemukan semua sumber daya yang Anda butuhkan untuk mempublikasikan dan memelihara aplikasi Anda di F-Droid.



### Integritas dan keamanan



Menempatkan aplikasi ke dalam sumber terbuka sering kali identik dengan peningkatan keamanan, tetapi juga dengan risiko yang cukup besar. Bagaimana Anda dapat memastikan bahwa tidak ada perubahan berbahaya dalam kode sumber aplikasi yang tersedia di F-Droid?



F-Droid mengkompilasi aplikasi di server mereka sendiri, berdasarkan kode sumber resmi dan instruksi kompilasi. Setiap aplikasi yang diterbitkan dibangun ulang dan diverifikasi untuk memastikan bahwa aplikasi tersebut tidak dikompromikan. Hal ini memastikan bahwa APK yang ditawarkan sesuai dengan kode sumber yang diterbitkan oleh pengembang. Selain itu, setiap aplikasi yang diinstal melalui F-Droid ditandatangani secara digital, dan kemudian sidik jari tanda tangan tersebut dibandingkan dengan yang diumumkan oleh pengembang aplikasi di situs web resmi atau di repositori Git.



Jika Anda menikmati tutorial ini, cari tahu lebih lanjut tentang kursus keamanan TI dan manajemen data kami:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1