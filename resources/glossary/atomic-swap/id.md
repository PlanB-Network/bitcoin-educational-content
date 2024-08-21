---
term: ATOMIC SWAP
---

Teknologi yang memungkinkan pertukaran langsung mata uang kripto antara dua pihak, tanpa memerlukan kepercayaan dan tanpa membutuhkan perantara. Pertukaran ini disebut "atomik" karena hanya dapat menghasilkan dua hasil:
* Entah pertukaran berhasil, dan kedua peserta telah efektif menukar mata uang kripto mereka;
* Atau pertukaran gagal, dan kedua peserta meninggalkan dengan mata uang kripto asli mereka.

Atomic Swap dapat dilakukan baik dengan mata uang kripto yang sama, dalam hal ini juga disebut sebagai "*coinswap*," atau antara mata uang kripto yang berbeda. Secara historis, mereka mengandalkan "Hash Time-Locked Contracts" (HTLC), sistem penguncian waktu yang menjamin penyelesaian atau pembatalan total pertukaran, sehingga menjaga integritas dana dari pihak-pihak yang terlibat. Metode ini memerlukan protokol yang mampu menangani baik skrip maupun timelock. Namun, dalam beberapa tahun terakhir, tren telah bergeser ke penggunaan *Adaptor Signatures*. Pendekatan kedua ini memiliki keuntungan menghilangkan kebutuhan akan skrip, sehingga mengurangi biaya operasional. Keuntungan besar lainnya adalah tidak memerlukan penggunaan hashing yang identik untuk kedua bagian transaksi, yang membantu menghindari pengungkapan tautan di antara mereka.