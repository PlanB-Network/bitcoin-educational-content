---
term: CISA
---

Singkatan dari "Agregasi Tanda Tangan Masukan Silang". Ini adalah proposal teknis yang dirancang untuk mengoptimalkan ukuran transaksi Bitcoin dengan mengurangi jumlah tanda tangan yang diperlukan untuk memvalidasinya.


Saat ini, pada Bitcoin, setiap input dalam sebuah transaksi harus memiliki tanda tangan individu sebelum dapat digunakan. Hal ini membuktikan bahwa pemilik UTXO yang bersangkutan telah mengesahkan transaksi tersebut. Dengan CISA, tujuannya adalah untuk menggabungkan tanda tangan dari semua input ke dalam satu transaksi menjadi satu tanda tangan yang mencakup semua input. Hal ini akan memungkinkan untuk mengurangi ukuran transaksi dengan banyak input, dan dengan demikian juga mengurangi biayanya. Ini akan sangat berguna bagi mereka yang melakukan coinjoin atau konsolidasi, sekaligus memungkinkan lebih banyak transaksi untuk dikonfirmasi pada Bitcoin tanpa mengubah ukuran atau interval blok. CISA didasarkan pada protokol Schnorr, yang memungkinkan agregasi tanda tangan secara linear. Ini berarti bahwa satu tanda tangan dapat membuktikan kepemilikan beberapa kunci independen.


Namun, mengimplementasikan CISA pada Bitcoin sangat kompleks, karena membutuhkan perubahan besar dalam cara kerja skrip. Saat ini, verifikasi skrip pada Bitcoin dilakukan secara input per input. Beralih ke model di mana seluruh transaksi diperiksa sekaligus, seperti yang diusulkan oleh CISA, bukanlah perubahan yang sepele.