---
term: CHECKSUM
---

Checksum adalah nilai yang dihitung dari sekumpulan data, digunakan untuk memverifikasi integritas dan validitas data tersebut selama transmisi atau penyimpanannya. Algoritma checksum dirancang untuk mendeteksi kesalahan tidak sengaja atau perubahan data yang tidak diinginkan, seperti kesalahan transmisi atau kerusakan file. Berbagai jenis algoritma checksum ada, seperti pemeriksaan paritas, checksum modular, fungsi hash kriptografis, atau kode BCH (*Bose, Ray-Chaudhuri, dan Hocquenghem*).

Dalam Bitcoin, checksum digunakan pada level aplikasi untuk memastikan integritas alamat penerima. Sebuah checksum dihitung dari payload alamat pengguna, kemudian ditambahkan ke alamat ini untuk mendeteksi kemungkinan kesalahan selama entri. Checksum juga hadir dalam frasa pemulihan (mnemonik).

> ► *Terjemahan bahasa Inggris dari "somme de contrôle" adalah "checksum". Umumnya diterima untuk langsung menggunakan istilah "checksum" dalam bahasa Prancis.*