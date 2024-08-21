---
term: COIN SELECTION
---

Proses di mana perangkat lunak dompet Bitcoin memilih UTXO mana yang akan digunakan sebagai input untuk memenuhi output dari sebuah transaksi. Metode pemilihan koin sangat penting karena memiliki konsekuensi pada biaya transaksi dan privasi pengguna. Ini sering bertujuan untuk meminimalkan jumlah input yang digunakan, dalam rangka mengurangi ukuran transaksi dan biaya terkait, sambil mencoba mempertahankan privasi dengan menghindari penggabungan koin dari sumber yang berbeda (CIOH). Beberapa metode ada untuk pemilihan koin, seperti *Knapsack Solver* atau *Branch-and-Bound*. Ketika pemilihan koin dilakukan secara manual oleh pengguna, ini disebut sebagai “*Coin Control*”.

> ► *Dalam bahasa Inggris, ini disebut sebagai "Coin Selection".*