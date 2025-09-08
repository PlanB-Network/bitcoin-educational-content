---
term: BIP0173

---
Memperkenalkan format alamat bech32 untuk alamat SegWit V0. Format alamat ini ditandai dengan awalan `bc1q`. Format bech32 menawarkan beberapa keuntungan:


- Membutuhkan lebih sedikit ruang dalam kode QR;
- Hal ini lebih mudah ditafsirkan oleh manusia;
- Memiliki mekanisme _checksum_ inovatif yang lebih efisien dan memungkinkan pendeteksian serta potensi koreksi otomatis atas kesalahan pengetikan.

Fitur-fitur ini membuat penggunaan alamat penerima menjadi lebih mudah sekaligus meminimalkan risiko kesalahan.
