---
term: KONSOLIDASI

---
Transaksi spesifik di mana beberapa UTXO kecil digabungkan menjadi satu input untuk membentuk satu UTXO yang lebih besar sebagai output. Operasi ini adalah transaksi yang dilakukan ke dompet sendiri. Tujuan konsolidasi adalah untuk mengambil keuntungan dari periode ketika biaya di jaringan Bitcoin rendah untuk menggabungkan beberapa UTXO kecil menjadi satu yang nilainya lebih besar. Dengan demikian, ini mengantisipasi pengeluaran wajib jika terjadi kenaikan biaya, sehingga memungkinkan penghematan biaya transaksi di masa mendatang.

Memang, transaksi dengan banyak input lebih berat dan, akibatnya, lebih mahal. Di luar penghematan yang dapat dicapai pada biaya transaksi, konsolidasi juga merupakan bentuk perencanaan jangka panjang. Jika dompet Anda berisi UTXO yang sangat kecil, maka dompet tersebut tidak dapat digunakan lagi jika jaringan Bitcoin memasuki periode biaya tinggi yang berkepanjangan. Sebagai contoh, jika Anda perlu mengeluarkan UTXO sebesar 10.000 sat namun biaya penambangan minimum mencapai 15.000 sat, maka biaya tersebut akan melebihi nilai UTXO itu sendiri. UTXO kecil ini kemudian menjadi tidak rasional secara ekonomi untuk digunakan dan tetap tidak dapat digunakan selama biayanya tidak berkurang. UTXO ini biasanya disebut sebagai "debu" Dengan mengkonsolidasikan UTXO kecil secara teratur, Anda mengurangi risiko yang terkait dengan kenaikan biaya.

Namun, penting untuk dicatat bahwa transaksi konsolidasi dapat dikenali selama analisis berantai. Transaksi seperti itu menunjukkan Common Input Ownership Heuristic (CIOH), yang berarti bahwa input dari transaksi konsolidasi dimiliki oleh satu entitas. Hal ini dapat berimplikasi pada privasi pengguna.

![](../../dictionnaire/assets/7.webp)