---
term: CHECKSUM
---

_Checksum_ adalah nilai yang dihitung dari sekumpulan data, yang digunakan untuk memverifikasi integritas dan keabsahan data tersebut selama transmisi atau penyimpanan. Algoritma _checksum_ dirancang untuk mendeteksi kesalahan yang tidak disengaja atau perubahan yang tidak disengaja pada data, seperti kesalahan transmisi atau kerusakan file. Terdapat berbagai jenis algoritma checksum, seperti pemeriksaan paritas, _checksum_ modular, fungsi kriptografi Hash, atau kode BCH (*Bose, Ray-Chaudhuri, dan Hocquenghem*).


Pada Bitcoin, _checksum_ digunakan pada tingkat aplikasi untuk memastikan integritas alamat yang diterima. _Checksum_ dihitung dari _payload_ Address pengguna, kemudian ditambahkan ke Address tersebut untuk mendeteksi kesalahan pada masukannya. _Checksum_ juga ada dalam frasa pemulihan (mnemonik).


> ► *Dalam bahasa Indonesia, checksum biasanya disebut "checksum"*
