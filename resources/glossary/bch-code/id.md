---
term: KODE BCH
---

Kelas kode koreksi kesalahan yang digunakan untuk mendeteksi dan mengoreksi kesalahan dalam urutan data. Dengan kata lain, kode koreksi kesalahan BCH digunakan untuk menemukan dan mengoreksi kesalahan acak dalam informasi yang ditransmisikan, untuk memastikan bahwa informasi tersebut tiba secara utuh di tempat tujuan. Akronim "BCH" adalah singkatan dari inisial nama-nama penemu kode-kode ini: Bose, Ray-Chaudhuri, dan Hocquenghem.


Alat ini digunakan di banyak bidang komputasi, termasuk SSD, DVD, dan kode QR. Sebagai contoh, berkat kode pengoreksi kesalahan ini, meskipun kode QR tertutup sebagian, informasi yang dikodekannya masih dapat diambil.


Sebagai bagian dari Bitcoin, kode BCH digunakan untuk checksum dalam format Address Bech32 dan Bech32m (pasca SegWit). Kode-kode ini mewakili kompromi yang lebih baik antara ukuran checksum dan kemampuan deteksi kesalahan daripada fungsi Hash sederhana yang sebelumnya digunakan pada alamat-alamat lama. Dalam konteks Bitcoin, kode BCH hanya digunakan untuk deteksi kesalahan, bukan untuk koreksi kesalahan. Dengan demikian, perangkat lunak portofolio Bitcoin akan mengidentifikasi dan melaporkan kepada pengguna setiap kesalahan dalam Address yang diterima, tetapi tidak akan mengubah Address yang salah secara otomatis. Pilihan ini dimotivasi oleh fakta bahwa mengintegrasikan koreksi kesalahan pasti mempengaruhi kemampuan deteksi kesalahan algoritma.