---
term: RGB
---

Sistem kontrak pintar yang terdesentralisasi dan rahasia yang dirancang untuk bekerja dengan Bitcoin dan Jaringan Lightning. RGB bekerja pada model _Client-side Validation_ dan memisahkan penyimpanan _Contract State_ dari _Blockchain_, sehingga hanya komitmen kriptografi yang disimpan di dalamnya. Dengan cara ini, riwayat status lengkap disimpan di luar rantai, memungkinkan skalabilitas dan kerahasiaan yang lebih besar. Dengan demikian, RGB memungkinkan pembuatan kontrak yang kompleks untuk menyimpan token, NFT, identitas terdesentralisasi, atau solusi DeFi, langsung di atas Bitcoin.


Pada RGB, ketahanan terhadap _Double-spending_ dijamin dengan penggunaan _Single-Use Seal_, sebuah mekanisme kriptografi yang mengambil keuntungan dari fakta bahwa UTXO pada Bitcoin hanya dapat digunakan satu kali. Untuk keaslian token, hal ini dijamin dengan verifikasi riwayat status di sisi klien, mulai dari pembuatan _Contract_ hingga status terbarunya.
