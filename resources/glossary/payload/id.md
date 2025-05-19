---
term: BEBAN BERGUNA
---

Dalam konteks umum komputasi, payload adalah data penting yang dibawa dalam paket data yang lebih besar. Sebagai contoh, pada SegWit V0 di atas Bitcoin Address, payload sesuai dengan Hash dari kunci publik, tanpa berbagai metadata (HRP, pemisah, versi SegWit, dan checksum). Sebagai contoh, pada Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, kita memiliki :




- `bc`: bagian yang dapat dibaca manusia (HRP) ;
- `1`: pemisah ;
- `q`: Versi SegWit. Ini adalah versi 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: muatan, dalam hal ini, Hash dari kunci publik;
- `ys50gj`: checksum.