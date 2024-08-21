---
term: TARGET KESULITAN
---

Faktor kesulitan, yang juga dikenal sebagai target kesulitan, adalah parameter yang digunakan dalam mekanisme konsensus oleh proof of work (Bukti Kerja, PoW) pada Bitcoin. Target tersebut merupakan nilai numerik yang menentukan kesulitan bagi penambang untuk menyelesaikan masalah kriptografis tertentu, yang disebut bukti kerja, saat membuat blok baru pada blockchain.

Target kesulitan adalah angka yang dapat disesuaikan sebesar 256-bit (64 byte) yang menentukan batas penerimaan untuk hashing dari header blok. Dengan kata lain, agar sebuah blok valid, hash dari header-nya dengan `SHA256d` (ganda `SHA256`) harus secara numerik lebih rendah atau sama dengan target kesulitan. Bukti kerja terdiri dari memodifikasi `nonce` pada header blok atau transaksi coinbase sampai hash yang dihasilkan lebih rendah dari nilai target.

Target ini disesuaikan setiap 2016 blok (sekitar setiap dua minggu), selama sebuah peristiwa yang disebut "penyesuaian." Faktor kesulitan dihitung ulang berdasarkan waktu yang diperlukan untuk menambang 2016 blok sebelumnya. Jika total waktu kurang dari dua minggu, kesulitan meningkat dengan menyesuaikan target ke bawah. Jika total waktu lebih dari dua minggu, kesulitan menurun dengan menyesuaikan target ke atas. Tujuannya adalah untuk mempertahankan waktu penambangan rata-rata 10 menit per blok. Waktu antar setiap blok ini membantu mencegah pembagian jaringan Bitcoin, yang mengakibatkan pemborosan daya komputasi. Target kesulitan ditemukan di setiap header blok, dalam bidang `nBits`. Karena bidang ini direduksi menjadi 32 bit dan targetnya sebenarnya 256 bit, target dikompresi ke dalam format ilmiah yang kurang presisi.

![](../../dictionnaire/assets/34.png)

> ► *Target kesulitan terkadang juga disebut "faktor kesulitan." Secara ekstensi, ini juga dapat disebut dengan pengkodeannya dalam header blok dengan istilah "nBits."*