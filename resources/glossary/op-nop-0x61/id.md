---
term: OP_NOP (0X61)

---
Tidak menghasilkan efek apapun pada stack atau status skrip. Ia tidak melakukan pergerakan, pengecekan, atau modifikasi. Ia tidak melakukan apa pun kecuali jika diputuskan sebaliknya melalui soft fork. Memang, sejak dimodifikasi oleh Satoshi Nakamoto pada tahun 2010, perintah `OP_NOP` (`OP_NOP1` (`0XB0`) hingga `OP_NOP10` (`0XB9`)) digunakan untuk menambahkan opcode baru dalam bentuk soft fork.

Dengan demikian, `OP_NOP2` (`0XB1`) dan `OP_NOP3` (`0XB2`) telah digunakan untuk mengimplementasikan `OP_CHECKLOCKTIMEVERIFY` dan `OP_CHECKSEQUENCEVERIFY`. Keduanya digunakan bersama dengan `OP_DROP` untuk menghapus nilai temporal yang terkait dari stack, sehingga memungkinkan eksekusi skrip untuk dilanjutkan, baik node yang bersangkutan sudah diperbarui atau belum. Oleh karena itu, perintah `OP_NOP` memungkinkan penyisipan titik interupsi dalam skrip untuk memeriksa kondisi tambahan yang sudah ada atau dapat ditambahkan dengan soft fork di masa mendatang. Sejak Tapscript, penggunaan `OP_NOP` telah digantikan oleh `OP_SUCCESS` yang lebih efisien.