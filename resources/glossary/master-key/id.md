---
term: MASTER KEY
---

Dalam konteks dompet HD (Hierarchical Deterministic), kunci privat utama adalah kunci privat unik yang berasal dari seed dompet tersebut. Untuk mendapatkan kunci utama, fungsi `HMAC-SHA512` diterapkan pada seed, menggunakan kata-kata "*Bitcoin seed*" secara harfiah sebagai kunci. Hasil dari operasi ini menghasilkan output 512-bit, dengan 256 bit pertama merupakan kunci utama, dan 256 bit sisanya membentuk master chain code. Kunci utama dan master chain code berfungsi sebagai titik awal untuk menurunkan semua kunci privat dan publik anak dalam struktur pohon dompet HD. Oleh karena itu, kunci privat utama berada pada kedalaman 0 dari derivasi.

![](../../dictionnaire/assets/19.png)