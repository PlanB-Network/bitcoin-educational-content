---
term: BAYAR BAYAR

---
Dalam konteks umum komputasi, payload merujuk pada data penting yang dibawa dalam paket data yang lebih besar. Sebagai contoh, pada alamat SegWit V0 pada Bitcoin, payload berhubungan dengan hash dari kunci publik, tidak termasuk berbagai metadata (HRP, pemisah, versi SegWit, dan checksum). Sebagai contoh, pada alamat `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, kita mendapatkannya:


- `bc` : bagian yang dapat dibaca manusia (HRP);
- `1` : pemisah;
- `q` : versi SegWit. Di sini, ini adalah versi 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : muatan, di sini, hash dari kunci publik;
- `ys50gj` : checksum.