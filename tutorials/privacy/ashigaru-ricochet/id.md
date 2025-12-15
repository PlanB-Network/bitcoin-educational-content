---
name: Ashigaru - Ricochet
description: Memahami dan menggunakan transaksi Ricochet
---
![cover ricochet](assets/cover.webp)



> *Alat bantu premium yang menambahkan lompatan ekstra pada riwayat transaksi Anda. Menghapus daftar hitam dan membantu melindungi Anda dari penutupan akun pihak ketiga yang tidak adil*

## Apa itu Ricochet?



Ricochet adalah sebuah teknik yang terdiri dari beberapa transaksi fiktif terhadap diri sendiri untuk mensimulasikan transfer kepemilikan bitcoin. Alat ini berbeda dengan transaksi Ashigaru yang lain (yang diwarisi dari Samurai Wallet) karena tidak memberikan anonimitas prospektif, melainkan sebuah bentuk anonimitas retrospektif. Faktanya, Ricochet mengaburkan kekhususan yang dapat membahayakan kesesuaian bagian Bitcoin.



Sebagai contoh, jika Anda membuat coinjoin, bagian Anda yang keluar dari campuran akan diidentifikasi seperti itu. Alat analisis rantai dapat mendeteksi pola transaksi coinjoin dan memberikan label pada bagian yang keluar darinya. Pada dasarnya, coinjoin bertujuan untuk memutus hubungan historis sebuah koin, tetapi perjalanannya melalui coinjoin tetap dapat dideteksi. Sebagai analogi, fenomena ini mirip dengan enkripsi sebuah teks: meskipun teks asli tidak dapat diakses dalam teks yang jelas, mudah untuk mengidentifikasi bahwa enkripsi telah diterapkan.



Label "coinjoined" dapat memengaruhi kesesuaian UTXO. Entitas yang diatur, seperti platform pertukaran, dapat menolak untuk menerima UTXO yang digabungkan bersama, atau bahkan meminta penjelasan dari pemiliknya, dengan risiko akun Anda diblokir atau dana Anda dibekukan. Dalam beberapa kasus, platform bahkan dapat melaporkan perilaku Anda kepada pihak berwenang.



Di sinilah metode Ricochet berperan. Untuk memudarkan jejak yang ditinggalkan oleh coinjoin, Ricochet mengeksekusi empat transaksi berurutan di mana pengguna mentransfer dananya ke dirinya sendiri di alamat yang berbeda. Setelah rangkaian transaksi ini, alat Ricochet akhirnya merutekan bitcoin ke tujuan akhir, seperti platform bursa. Tujuannya adalah untuk menciptakan jarak antara transaksi coinjoin asli dan tindakan akhir pembelanjaan. Dengan cara ini, alat analisis blockchain akan mengasumsikan bahwa kemungkinan besar telah terjadi transfer kepemilikan setelah coinjoin, dan oleh karena itu tidak perlu dilakukan tindakan terhadap penerbitnya.



![image](assets/fr/01.webp)



Dihadapkan dengan metode Ricochet, orang mungkin membayangkan bahwa perangkat lunak analisis rantai akan memperdalam pemeriksaannya lebih dari empat pantulan. Akan tetapi, platform-platform ini menghadapi dilema dalam mengoptimalkan ambang batas pendeteksian. Mereka perlu menetapkan ambang batas jumlah lompatan setelah itu mereka menerima bahwa perubahan kepemilikan kemungkinan besar telah terjadi, dan bahwa tautan ke koin sebelumnya harus diabaikan. Namun, menentukan ambang batas ini berisiko: setiap penambahan jumlah lompatan yang diamati secara eksponensial meningkatkan volume positif palsu, yaitu individu yang secara keliru ditandai sebagai peserta dalam coinjoin, padahal sebenarnya operasi tersebut dilakukan oleh orang lain. Skenario ini menimbulkan risiko besar bagi perusahaan-perusahaan ini, karena positif palsu menyebabkan ketidakpuasan, yang dapat mendorong pelanggan yang terkena dampak ke kompetisi. Dalam jangka panjang, ambang batas deteksi yang terlalu ambisius menyebabkan platform kehilangan lebih banyak pelanggan daripada pesaingnya, yang dapat mengancam kelangsungan hidupnya. Oleh karena itu, sulit bagi platform ini untuk meningkatkan jumlah pantulan yang diamati, dan 4 sering kali merupakan angka yang cukup untuk melawan analisis mereka.



Dengan demikian, **kasus penggunaan yang paling umum untuk Ricochet muncul ketika diperlukan untuk menyembunyikan partisipasi sebelumnya dalam coinjoin pada UTXO yang Anda miliki** Idealnya, yang terbaik adalah menghindari mentransfer bitcoin yang telah mengalami coinjoin ke entitas yang diatur. Namun demikian, jika tidak ada pilihan lain, terutama jika ada kebutuhan mendesak untuk melikuidasi bitcoin dalam mata uang negara, Ricochet menawarkan solusi yang efektif.



## Bagaimana cara kerja Ricochet di Ashigaru?



Ricochet hanyalah sebuah metode untuk mengirim bitcoin ke diri sendiri, yang pada awalnya diciptakan oleh pengembang Samurai Wallet. Oleh karena itu, sangat mungkin untuk mensimulasikan Ricochet secara manual, tanpa memerlukan alat khusus. Namun, bagi mereka yang ingin mengotomatiskan prosesnya sambil menikmati hasil yang lebih baik, alat Ricochet yang tersedia melalui aplikasi Ashigaru (yang merupakan Samourai fork) merupakan solusi yang baik.



Karena Ashigaru mengenakan biaya untuk layanannya, sebuah Ricochet dikenakan biaya `100.000 sats` sebagai biaya layanan, ditambah biaya mining. Oleh karena itu, penggunaannya direkomendasikan untuk transfer dalam jumlah besar.



Aplikasi Ashigaru menawarkan dua varian Ricochet:





- Reinforced Ricochet, atau "pengiriman terhuyung-huyung", yang menawarkan keuntungan menyebarkan biaya layanan Ashigaru ke dalam lima transaksi yang berurutan. Opsi ini juga memastikan bahwa setiap transaksi disiarkan pada waktu yang berbeda dan dicatat dalam blok yang berbeda, meniru semirip mungkin dengan perilaku perubahan kepemilikan. Meskipun lebih lambat, metode ini lebih disukai oleh mereka yang tidak terburu-buru, karena metode ini memaksimalkan efisiensi Ricochet dengan memperkuat ketahanannya terhadap analisis rantai;





- Ricochet klasik, yang dirancang untuk menjalankan operasi dengan cepat, menyiarkan semua transaksi dalam interval waktu yang singkat. Oleh karena itu, metode ini menawarkan lebih sedikit kerahasiaan dan lebih sedikit resistensi terhadap analisis daripada metode yang diperkuat. Metode ini hanya boleh digunakan untuk pengiriman yang mendesak.



## Bagaimana cara membuat Ricochet di Ashigaru?



Cara melakukan pengiriman uang di Ashigaru sangat mudah: cukup aktifkan opsi yang sesuai saat membuat transaksi pengiriman. Untuk memulai, klik tombol `+`, lalu `Kirim`, dan pilih akun dari mana Anda ingin mengirim dana.



![Image](assets/fr/02.webp)



Isi informasi transaksi: jumlah yang akan dikirim dan alamat akhir penerima setelah Ricochet melompat. Kemudian centang opsi `Ricochet`.



![Image](assets/fr/03.webp)



Anda kemudian dapat memilih di antara dua mode Ricochet yang dibahas di bagian teori: Ricochet klasik, di mana semua transaksi dimasukkan dalam blok yang sama, atau pengiriman terhuyung-huyung, yang meningkatkan kualitas Ricochet dengan biaya penundaan yang lebih lama.



Setelah Anda menentukan pilihan, tekan panah di bagian bawah layar untuk mengonfirmasi.



![Image](assets/fr/04.webp)



Pada layar berikutnya, Anda akan melihat ringkasan lengkap transaksi Anda. Di sini Anda juga dapat menyesuaikan tingkat biaya untuk transaksi Ricochet Anda sesuai dengan kondisi pasar. Jika semuanya sudah sesuai dengan keinginan Anda, seret panah hijau untuk menandatangani dan mendistribusikan transaksi Ricochet.



![Image](assets/fr/05.webp)



Tunggu sementara berbagai lompatan berjalan secara otomatis.



![Image](assets/fr/06.webp)



Transaksi Anda telah berhasil disiarkan.



![Image](assets/fr/07.webp)



Anda sekarang sudah sangat familiar dengan opsi Ricochet yang tersedia di aplikasi Ashigaru. Untuk melangkah lebih jauh, saya sarankan Anda mengikuti kursus pelatihan BTC 204 saya, yang akan mengajarkan Anda secara detail cara memperkuat kerahasiaan onchain Anda.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c