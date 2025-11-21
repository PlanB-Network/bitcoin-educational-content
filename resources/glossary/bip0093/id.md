---
term: BIP0093
---

BIP Informatif yang menyarankan sebuah standar untuk menyimpan dan mengembalikan _seed_ dari portofolio deterministik hirarkis (menurut BIP32) dengan menggunakan Pembagian Kunci Rahasia Shamir. Protokol ini mendefinisikan format "codex32", yang terinspirasi dari format bech32, dengan memperkenalkan string terstruktur yang terdiri dari awalan, parameter ambang batas, pengenal, indeks pembagian, _payload_ dan _checksum_ (BCH). Metode ini memungkinkan _seed_ untuk dibagi menjadi hingga 31 bagian, di mana ambang batas yang ditentukan (antara 1 dan 9) diperlukan untuk pemulihan _seed_ secara penuh.
