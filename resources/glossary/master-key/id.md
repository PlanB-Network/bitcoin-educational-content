---
term: KUNCI UTAMA

---
Dalam konteks dompet HD (Hierarchical Deterministic), kunci pribadi utama adalah kunci pribadi unik yang berasal dari seed dompet. Untuk mendapatkan kunci utama, fungsi `HMAC-SHA512` diaplikasikan pada seed, dengan menggunakan kata "*Bitcoin seed*" secara harfiah sebagai kuncinya. Hasil dari operasi ini menghasilkan output 512-bit, dengan 256 bit pertama merupakan kunci utama, dan 256 bit sisanya membentuk kode rantai utama. Kunci utama dan kode rantai utama berfungsi sebagai titik awal untuk mendapatkan semua kunci privat dan publik anak dalam struktur pohon dompet HD. Oleh karena itu, kunci pribadi utama berada pada kedalaman 0 dalam penurunan.

![](../../dictionnaire/assets/19.webp)