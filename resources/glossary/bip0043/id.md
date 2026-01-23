---
term: BIP0043

definition: Standar yang memperkenalkan bidang purpose dalam jalur derivasi HD untuk mengidentifikasi jenis dompet yang digunakan (misalnya m/84' untuk SegWit).
---
Proposal untuk perbaikan yang memperkenalkan penggunaan level jalur derivasi untuk mendeskripsikan bidang tujuan dalam struktur dompet HD, yang sebelumnya diperkenalkan di BIP32. Menurut BIP43, level pertama dari derivasi dompet HD, tepat setelah kunci utama yang dilambangkan sebagai `m/`, dicadangkan untuk nomor tujuan yang mengindikasikan standar derivasi yang digunakan untuk jalur lainnya. Nomor ini dicatat sebagai sebuah indeks yang menggunakan _hardened derivation_. Sebagai contoh, jika dompet mengikuti standar SegWit (BIP84), awal dari jalur turunannya adalah: `m/84'/`. Dengan demikian, BIP43 memungkinkan klarifikasi standar yang diadopsi oleh setiap perangkat lunak dompet untuk memiliki interoperabilitas yang lebih baik di antara mereka. Standarisasi jalur derivasi lainnya dijelaskan dalam BIP44.
