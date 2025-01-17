---
term: CABANG-DAN-TERIKAT

---
Metode yang digunakan untuk memilih input dalam dompet Bitcoin Core sejak versi 0.17 dan diciptakan oleh Murch. Branch-and-Bound (BnB) adalah pencarian untuk menemukan sekumpulan UTXO yang sesuai dengan jumlah output yang harus dipenuhi dalam sebuah transaksi, untuk meminimalkan perubahan dan biaya yang terkait. Tujuannya adalah untuk mengurangi kriteria pemborosan yang memperhitungkan biaya langsung dan biaya masa depan yang diharapkan untuk perubahan tersebut. Metode ini lebih akurat dalam hal biaya dibandingkan dengan heuristik sebelumnya seperti *Knapsack Solver*. *Branch-and-Bound* terinspirasi dari metode pemecahan masalah dengan nama yang sama, yang ditemukan pada tahun 1960 oleh Ailsa Land dan Alison Harcourt.

> ► *Metode ini juga terkadang dinamai "Algoritma Murch" untuk merujuk pada penemunya*