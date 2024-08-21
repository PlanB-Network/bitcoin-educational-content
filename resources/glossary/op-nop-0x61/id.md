---
term: OP_NOP (0X61)
---

Tidak memberikan efek apa pun pada tumpukan atau keadaan skrip. Tidak melakukan pergerakan, pemeriksaan, atau modifikasi. Ini hanya tidak melakukan apa-apa kecuali diputuskan lain melalui soft fork. Memang, sejak modifikasi oleh Satoshi Nakamoto pada tahun 2010, perintah `OP_NOP` (`OP_NOP1` (`0XB0`) hingga `OP_NOP10` (`0XB9`)) digunakan untuk menambahkan opcode baru dalam bentuk soft fork.

Dengan demikian, `OP_NOP2` (`0XB1`) dan `OP_NOP3` (`0XB2`) telah digunakan untuk mengimplementasikan `OP_CHECKLOCKTIMEVERIFY` dan `OP_CHECKSEQUENCEVERIFY`, masing-masing. Mereka digunakan bersama dengan `OP_DROP` untuk menghapus nilai temporal terkait dari tumpukan, sehingga memungkinkan eksekusi skrip untuk dilanjutkan, apakah node tersebut terbaru atau tidak. Perintah `OP_NOP`, oleh karena itu, memungkinkan penyisipan titik interupsi dalam skrip untuk memeriksa kondisi tambahan yang sudah ada atau mungkin ditambahkan dengan soft fork di masa depan. Sejak Tapscript, penggunaan `OP_NOP` telah digantikan oleh `OP_SUCCESS` yang lebih efisien.