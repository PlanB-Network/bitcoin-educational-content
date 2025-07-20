---
term: LIBSECP256K1
---

_Library_ C berkinerja tinggi dan keamanan tinggi untuk tanda tangan digital dan primitif kriptografi lainnya pada kurva eliptik `secp256k1`. Karena kurva ini tidak pernah digunakan secara luas di luar Bitcoin (tidak seperti kurva `secp256r1` yang sering digunakan), pustaka ini bertujuan untuk menjadi referensi yang paling komprehensif untuk penggunaannya. Pengembangan libsecp256k1 terutama ditujukan untuk kebutuhan Bitcoin, dan fitur-fitur yang ditujukan untuk aplikasi lain mungkin kurang teruji atau terverifikasi. Penggunaan yang tepat dari _library_ ini membutuhkan perhatian yang cermat, untuk memastikan bahwa _library_ ini sesuai untuk tujuan spesifik aplikasi selain Bitcoin.


_Library_ libsecp256k1 menawarkan berbagai fitur, termasuk:




- Tanda tangan dan verifikasi ECDSA-secp256k1, dan pembuatan kunci kriptografi;
- Operasi penjumlahan dan perkalian pada kunci rahasia dan kunci publik;
- Serialisasi dan analisis kunci rahasia, kunci publik, dan tanda tangan;
- Penandatanganan dan pembuatan kunci publik waktu konstan dengan akses memori yang konstan;
- Dan sejumlah kriptografi primitif lainnya.
