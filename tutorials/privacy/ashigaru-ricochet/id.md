---
name: Ashigaru - Ricochet
description: Memahami dan menggunakan transaksi Ricochet
---
![cover ricochet](assets/cover.webp)



> *Alat bantu premium yang memberi lompatan ekstra pada riwayat transaksi kamu. Menghapus blacklist dan membantu melindungi kamu dari penutupan akun pihak ketiga yang tidak adil.*

## Apa itu Ricochet?



Ricochet adalah teknik yang terdiri dari beberapa transaksi fiktif ke diri sendiri untuk mensimulasikan transfer kepemilikan bitcoin. Alat ini berbeda dengan transaksi Ashigaru lainnya (yang diwarisi dari Samurai Wallet) karena tidak memberikan anonimitas prospektif, melainkan anonimitas retrospektif. Faktanya, Ricochet mengaburkan ciri khusus yang bisa membahayakan kesesuaian bagian Bitcoin.

Sebagai contoh, jika kamu membuat coinjoin, bagian kamu yang keluar dari campuran akan diidentifikasi sebagai itu. Alat chain analysis bisa mendeteksi pola transaksi coinjoin dan memberi label pada bagian yang keluar darinya. Pada dasarnya, coinjoin bertujuan memutus hubungan historis sebuah koin, tetapi perjalanannya melalui coinjoin tetap bisa dideteksi. Sebagai analogi, fenomena ini mirip dengan enkripsi sebuah teks: meskipun teks asli tidak dapat diakses dalam teks yang jelas, mudah untuk mengidentifikasi bahwa enkripsi telah diterapkan.

Label coinjoined dapat memengaruhi kesesuaian UTXO. Entitas yang diatur, seperti platform exchange, bisa menolak menerima UTXO yang digabungkan bersama, atau bahkan meminta penjelasan dari pemiliknya, dengan risiko akun kamu diblokir atau dana kamu dibekukan. Dalam beberapa kasus, platform bahkan bisa melaporkan perilaku kamu ke pihak berwenang.

Di sinilah metode Ricochet berperan. Untuk memudarkan jejak yang ditinggalkan oleh coinjoin, Ricochet mengeksekusi empat transaksi berurutan di mana pengguna mentransfer dananya ke dirinya sendiri di alamat berbeda. Setelah rangkaian transaksi ini, alat Ricochet akhirnya merutekan bitcoin ke tujuan akhir, seperti platform exchange. Tujuannya adalah menciptakan jarak antara transaksi coinjoin asli dan tindakan akhir pembelanjaan. Dengan cara ini, alat analisis blockchain akan mengasumsikan bahwa kemungkinan besar telah terjadi transfer kepemilikan setelah coinjoin, sehingga tidak perlu dilakukan tindakan terhadap penerbitnya.



![image](assets/fr/01.webp)


Dihadapkan dengan metode Ricochet, orang mungkin membayangkan bahwa perangkat lunak chain analysis akan memperdalam pemeriksaannya lebih dari empat pantulan. Akan tetapi, platform-platform ini menghadapi dilema dalam mengoptimalkan ambang batas pendeteksian. Mereka perlu menetapkan ambang batas jumlah lompatan setelah itu mereka menerima bahwa perubahan kepemilikan kemungkinan besar sudah terjadi, dan bahwa tautan ke koin sebelumnya harus diabaikan. Namun, menentukan ambang batas ini berisiko, karena setiap penambahan jumlah lompatan yang diamati secara eksponensial meningkatkan volume *false positives,* yaitu individu yang secara keliru ditandai sebagai peserta coinjoin, padahal sebenarnya operasi tersebut dilakukan oleh orang lain. Skenario ini menimbulkan risiko besar bagi perusahaan-perusahaan ini, karena *false positives* menyebabkan ketidakpuasan yang bisa mendorong pelanggan terdampak ke kompetitor. Dalam jangka panjang, ambang batas deteksi yang terlalu ambisius membuat platform kehilangan lebih banyak pelanggan dibanding para pesaingnya, yang dapat mengancam kelangsungan hidupnya. Oleh karena itu, sulit bagi platform ini untuk meningkatkan jumlah lompatan yang diamati, dan 4 sering kali merupakan angka yang cukup untuk melawan analisis mereka.


Dengan demikian, **kasus penggunaan yang paling umum untuk Ricochet muncul ketika diperlukan untuk menyembunyikan partisipasi sebelumnya dalam coinjoin pada UTXO yang kamu miliki** Idealnya, yang terbaik adalah menghindari mentransfer bitcoin yang telah melalui coinjoin ke entitas yang diatur. Namun, jika tidak ada pilihan lain, terutama jika ada kebutuhan mendesak untuk melikuidasi bitcoin ke mata uang negara, Ricochet menawarkan solusi yang efektif.



## Bagaimana cara kerja Ricochet di Ashigaru?

Ricochet hanyalah metode untuk mengirim bitcoin ke diri sendiri, yang awalnya diciptakan oleh pengembang Samurai Wallet. Karena itu, sangat mungkin untuk mensimulasikan Ricochet secara manual tanpa memerlukan alat khusus. Namun, bagi kamu yang ingin mengotomatiskan prosesnya sambil mendapatkan hasil yang lebih baik, alat Ricochet yang tersedia melalui aplikasi Ashigaru (yang merupakan fork Samourai) adalah solusi yang bagus.

Karena Ashigaru mengenakan biaya untuk layanannya, satu Ricochet dikenakan biaya `100.000 sats` sebagai biaya layanan, ditambah biaya mining. Karena itu, penggunaannya lebih direkomendasikan untuk transfer dalam jumlah besar.

Aplikasi Ashigaru menawarkan dua varian Ricochet:


- Reinforced Ricochet, atau "pengiriman bertahap", menawarkan keuntungan dengan menyebarkan biaya layanan Ashigaru ke dalam lima transaksi yang berurutan. Opsi ini juga memastikan bahwa setiap transaksi disiarkan pada waktu yang berbeda dan dicatat dalam blok yang berbeda, meniru sedekat mungkin perilaku perubahan kepemilikan. Meskipun lebih lambat, metode ini lebih disukai oleh mereka yang tidak terburu buru, karena metode ini memaksimalkan efisiensi Ricochet dengan memperkuat ketahanannya terhadap chain analysis.





- Ricochet klasik, yang dirancang untuk menjalankan operasi dengan cepat, menyiarkan semua transaksi dalam interval waktu yang singkat. Karena itu, metode ini menawarkan lebih sedikit kerahasiaan dan lebih sedikit resistensi terhadap analisis dibanding metode yang diperkuat. Metode ini hanya boleh digunakan untuk pengiriman yang mendesak.


## Bagaimana cara membuat Ricochet di Ashigaru?



Cara melakukan pengiriman uang di Ashigaru sangat mudah: cukup aktifkan opsi yang sesuai saat membuat transaksi pengiriman. Untuk memulai, klik tombol `+`, lalu `Kirim`, dan pilih akun dari mana kamu ingin mengirim dana.



![Image](assets/fr/02.webp)



Isi informasi transaksi: jumlah yang akan dikirim dan alamat akhir penerima setelah rangkaian Ricochet selesai. Lalu centang opsi 'Ricochet'.


![Image](assets/fr/03.webp)

Kamu kemudian bisa memilih di antara dua mode Ricochet yang dibahas di bagian teori: Ricochet klasik, di mana semua transaksi dimasukkan dalam blok yang sama, atau pengiriman bertahap, yang meningkatkan kualitas Ricochet dengan biaya penundaan yang lebih lama.

Setelah kamu menentukan pilihan, tekan panah di bagian bawah layar untuk mengonfirmasi.



![Image](assets/fr/04.webp)



Pada layar berikutnya, kamu akan melihat ringkasan lengkap transaksi kamu. Di sini kamu juga bisa menyesuaikan tingkat biaya untuk transaksi Ricochet sesuai kondisi pasar. Jika semuanya sudah sesuai dengan keinginan kamu, seret panah hijau untuk menandatangani dan mendistribusikan transaksi Ricochet.


![Image](assets/fr/05.webp)



Tunggu sementara berbagai tahap berjalan secara otomatis.



![Image](assets/fr/06.webp)



Transaksi kamu telah berhasil disiarkan.



![Image](assets/fr/07.webp)



Sekarang kamu sudah sangat familiar dengan opsi Ricochet yang tersedia di aplikasi Ashigaru. Untuk melangkah lebih jauh, aku sarankan kamu mengikuti kursus pelatihan BTC 204 aku, yang akan mengajarkan kamu secara detail cara memperkuat kerahasiaan onchain kamu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
