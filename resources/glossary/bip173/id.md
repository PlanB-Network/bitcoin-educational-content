---
term: BIP173
---

Memperkenalkan format alamat bech32 untuk alamat SegWit V0. Format alamat ini ditandai dengan awalan `bc1q`. Format bech32 menawarkan beberapa keuntungan:
* Membutuhkan ruang lebih sedikit dalam kode QR;
* Lebih mudah diinterpretasikan oleh manusia;
* Memiliki mekanisme checksum inovatif yang lebih efisien dan memungkinkan deteksi dan potensi koreksi otomatis kesalahan ketik.
Fitur-fitur ini membuat penggunaan alamat penerima lebih mudah sambil meminimalkan risiko kesalahan.