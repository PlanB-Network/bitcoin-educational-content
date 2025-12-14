---
term: KODE BCH

---

Kelas kode koreksi kesalahan yang digunakan untuk mendeteksi dan mengoreksi kesalahan dalam urutan data. Dengan kata lain, kode koreksi kesalahan BCH digunakan untuk menemukan dan mengoreksi kesalahan acak dalam informasi yang ditransmisikan, untuk memastikan bahwa informasi tersebut tiba secara utuh di tempat tujuan. Akronim "BCH" adalah singkatan dari inisial nama-nama penemu kode-kode ini: Bose, Ray-Chaudhuri, dan Hocquenghem.

Alat ini digunakan di banyak bidang komputasi, termasuk SSD, DVD, dan kode QR. Sebagai contoh, berkat kode pengoreksi kesalahan ini, meskipun ada bagian kode QR yang tertutup, informasi yang ada di dalamnya masih dapat diakses.

Sebagai bagian dari Bitcoin, kode BCH digunakan untuk _checksum_ dalam format Address Bech32 dan Bech32m (pasca SegWit). Mereka mewakili keseimbangan yang lebih baik antara ukuran _checksum_ dan kemampuan deteksi kesalahan dibandingkan dengan fungsi _hash_ sederhana yang sebelumnya digunakan pada alamat _Legacy_. Dalam konteks Bitcoin, kode BCH hanya digunakan untuk deteksi kesalahan, bukan untuk koreksi kesalahan. Dengan demikian, perangkat lunak portofolio Bitcoin akan mengidentifikasi dan melaporkan setiap kesalahan dalam alamat yang diterima kepada pengguna, tetapi tidak akan mengubah alamat yang salah secara otomatis. Pilihan ini dikarenakan oleh fakta bahwa mengintegrasikan koreksi kesalahan pasti mempengaruhi kemampuan deteksi kesalahan algoritma.
