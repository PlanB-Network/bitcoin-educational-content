---
term: OP_SUCCESS

---
`OP_SUCCESS` mewakili serangkaian _opcode_ yang telah dinonaktifkan di masa lalu dan sekarang dicadangkan untuk digunakan di masa depan dalam Tapscript. Tujuan utamanya adalah untuk memfasilitasi pembaruan dan perluasan bahasa skrip, dengan mengizinkan pengenalan fungsi-fungsi baru melalui _soft fork_. Ketika salah satu dari _opcode_ ini ditemukan dalam sebuah skrip, hal ini mengindikasikan keberhasilan otomatis dari bagian skrip tersebut, terlepas dari data atau kondisi yang ada. Hal ini berarti bahwa skrip melanjutkan eksekusi tanpa kegagalan, terlepas dari operasi sebelumnya.

Dengan demikian, ketika sebuah _opcode_ baru ditambahkan pada `OP_SUCCESS`, hal ini merepresentasikan penambahan aturan yang lebih ketat daripada yang sebelumnya. Node yang diperbarui kemudian dapat memverifikasi kepatuhan terhadap aturan ini, dan node yang tidak diperbarui tidak akan menolak transaksi yang terkait dan blok yang menyertakannya, karena `OP_SUCCESS` memvalidasi bagian skrip tersebut. Oleh karena itu, tidak ada _hard fork_.

Sebagai perbandingan, `OP_NOP` (*No Operation*) juga berfungsi sebagai penampung di dalam skrip, tetapi tidak berpengaruh pada eksekusi skrip. Ketika `OP_NOP` ditemukan, skrip akan terus berlanjut tanpa mengubah status _stack_ atau perkembangan skrip. Oleh karena itu, perbedaan utamanya adalah pada dampaknya pada eksekusi: `OP_SUCCESS` menjamin bagian skrip tersebut berhasil, sementara `OP_NOP` bersifat netral, dan tidak mempengaruhi _stack_ atau alur skrip. Opcode ini ditandai dengan `OP_SUCCESSN` di mana `N` adalah sebuah angka yang digunakan untuk membedakannya dari `OP_SUCCESS`.
