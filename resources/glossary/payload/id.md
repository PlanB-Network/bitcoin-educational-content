---
term: PAYLOAD
---

Dalam konteks umum komputasi, payload merujuk pada data esensial yang dibawa dalam paket data yang lebih besar. Sebagai contoh, pada alamat SegWit V0 di Bitcoin, payload sesuai dengan hash dari kunci publik, dengan mengesampingkan berbagai metadata (HRP, pemisah, versi SegWit, dan checksum). Misalnya, pada alamat `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, kita memiliki:
* `bc` : bagian yang dapat dibaca manusia (HRP);
* `1` : pemisah;
* `q` : versi SegWit. Di sini, adalah versi 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : payload, di sini, hash dari kunci publik;
* `ys50gj` : checksum.