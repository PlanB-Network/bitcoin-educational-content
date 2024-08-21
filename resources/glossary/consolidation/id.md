---
term: KONSOLIDASI
---

Transaksi spesifik di mana beberapa UTXO kecil digabungkan menjadi satu input untuk membentuk satu UTXO yang lebih besar sebagai output. Operasi ini merupakan transaksi yang dilakukan ke dompet milik sendiri. Tujuan dari konsolidasi adalah untuk memanfaatkan periode ketika biaya di jaringan Bitcoin rendah untuk menggabungkan beberapa UTXO kecil menjadi satu yang lebih besar nilainya. Dengan demikian, ini mengantisipasi pengeluaran wajib dalam kasus peningkatan biaya, memungkinkan penghematan pada biaya transaksi di masa depan.

Memang, transaksi dengan banyak input lebih berat dan, akibatnya, lebih mahal. Di luar penghematan yang dapat dicapai pada biaya transaksi, konsolidasi juga merupakan bentuk perencanaan jangka panjang. Jika dompet Anda berisi UTXO yang sangat kecil, ini bisa menjadi tidak dapat digunakan jika jaringan Bitcoin memasuki periode biaya tinggi yang berkepanjangan. Misalnya, jika Anda perlu menghabiskan UTXO sebesar 10.000 sats tetapi biaya penambangan minimum berjumlah 15.000 sats, pengeluaran akan melebihi nilai dari UTXO itu sendiri. UTXO kecil ini kemudian menjadi tidak rasional secara ekonomi untuk digunakan dan tetap tidak dapat digunakan selama biaya tidak menurun. UTXO ini umumnya disebut sebagai "debu." Dengan secara rutin mengkonsolidasikan UTXO kecil Anda, Anda mengurangi risiko ini yang terkait dengan peningkatan biaya.

Namun, penting untuk dicatat bahwa transaksi konsolidasi dapat dikenali selama analisis rantai. Transaksi semacam itu menunjukkan Heuristik Kepemilikan Input Bersama (Common Input Ownership Heuristic - CIOH), yang berarti bahwa input dari transaksi konsolidasi dimiliki oleh satu entitas. Ini dapat memiliki implikasi dalam hal privasi bagi pengguna.

![](../../dictionnaire/assets/7.png)