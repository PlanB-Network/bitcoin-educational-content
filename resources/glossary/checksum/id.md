---
term: CHECKSUM
---

Checksum adalah nilai yang dihitung dari sekumpulan data, yang digunakan untuk memverifikasi integritas dan keabsahan data tersebut selama transmisi atau penyimpanan. Algoritme checksum dirancang untuk mendeteksi kesalahan yang tidak disengaja atau perubahan yang tidak disengaja pada data, seperti kesalahan transmisi atau kerusakan file. Terdapat berbagai jenis algoritma checksum, seperti pemeriksaan paritas, checksum modular, fungsi kriptografi Hash, atau kode BCH (*Bose, Ray-Chaudhuri, dan Hocquenghem*).


Pada Bitcoin, checksum digunakan pada tingkat aplikasi untuk memastikan integritas alamat yang diterima. Checksum dihitung dari muatan Address pengguna, kemudian ditambahkan ke Address tersebut untuk mendeteksi kesalahan pada masukannya. Checksum juga ada dalam frasa pemulihan (mnemonik).


> ► *Secara umum diterima untuk menggunakan istilah bahasa Inggris "checksum" secara langsung dalam bahasa Prancis.*