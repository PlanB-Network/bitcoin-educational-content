---
term: MASTER KEY

---
Dalam konteks dompet HD (_Hierarchical Deterministic_), kunci pribadi utama adalah kunci pribadi unik yang berasal dari _seed_ dompet. Untuk mendapatkan kunci utama, fungsi `HMAC-SHA512` diaplikasikan pada _seed_, dengan menggunakan kata "*Bitcoin seed*" secara harfiah sebagai kuncinya. Operasi ini menghasilkan output 512-bit, dengan 256 bit pertama sebagai _master key_, dan 256 bit sisanya membentuk _master chain code_. Kunci utama dan kode rantai utama berfungsi sebagai titik awal untuk mendapatkan semua kunci privat dan publik anak dalam struktur pohon dompet HD. Oleh karena itu, kunci pribadi utama berada pada kedalaman 0 dalam proses derivasi.

![](../../dictionnaire/assets/19.webp)
