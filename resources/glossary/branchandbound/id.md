---
term: BRANCH-AND-BOUND
---

Metode yang digunakan untuk memilih input di dompet Bitcoin Core sejak versi 0.17 dan ditemukan oleh Murch. Branch-and-Bound (BnB) adalah pencarian untuk menemukan satu set UTXO yang cocok dengan jumlah output yang harus dipenuhi dalam sebuah transaksi, untuk meminimalkan perubahan dan biaya terkait. Tujuannya adalah untuk mengurangi kriteria pemborosan yang mempertimbangkan baik biaya langsung maupun biaya masa depan yang diharapkan untuk perubahan. Metode ini lebih akurat dalam hal biaya dibandingkan dengan heuristik sebelumnya seperti *Knapsack Solver*. *Branch-and-Bound* terinspirasi oleh metode pemecahan masalah dengan nama yang sama, yang ditemukan pada tahun 1960 oleh Ailsa Land dan Alison Harcourt.

> ► *Metode ini terkadang juga dinamakan "Algoritma Murch" sebagai referensi kepada penemunya.*