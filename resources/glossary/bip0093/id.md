---
term: BIP0093
---

BIP Informasi yang menyarankan sebuah standar untuk menyimpan dan mengembalikan seed dari portofolio deterministik hirarkis (menurut BIP32) dengan menggunakan Pembagian Kunci Rahasia Shamir. Protokol ini mendefinisikan format "codex32", yang terinspirasi dari format bech32, dengan memperkenalkan string terstruktur yang terdiri dari awalan, parameter ambang batas, pengenal, indeks pembagian, muatan dan checksum (BCH). Metode ini memungkinkan seed untuk dibagi menjadi hingga 31 bagian, di mana ambang batas yang ditentukan (antara 1 dan 9) diperlukan untuk pemulihan seed secara penuh.