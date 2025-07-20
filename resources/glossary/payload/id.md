---
term: PAYLOAD
---

Dalam konteks umum komputasi, _payload_ adalah data penting yang dibawa dalam paket data yang lebih besar. Sebagai contoh, pada SegWit V0 di atas Bitcoin Address, _payload_ sesuai dengan _hash_ dari kunci publik, tanpa berbagai metadata (HRP, pemisah, versi SegWit, dan _checksum_). Sebagai contoh, untuk alamat `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`:




- `bc`: bagian yang dapat dibaca manusia (HRP) ;
- `1`: pemisah ;
- `q`: Versi SegWit. Ini adalah versi 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: _payload_, dalam hal ini, _hash_ dari kunci publik;
- `ys50gj`: _checksum_.
