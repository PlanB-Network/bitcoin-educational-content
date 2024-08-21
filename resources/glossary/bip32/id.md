---
term: BIP32
---

BIP32 memperkenalkan konsep dompet deterministik hierarkis (HD wallet). Proposal ini memungkinkan generasi hierarki pasangan kunci dari sebuah `master seed` bersama, menggunakan fungsi derivasi satu arah. Setiap pasangan kunci yang dihasilkan dapat menjadi induk dari kunci anak lainnya, sehingga membentuk struktur seperti pohon (hierarkis). Keuntungan dari BIP32 adalah memungkinkan pengelolaan berbagai pasangan kunci berbeda dengan hanya perlu menyimpan satu seed untuk meregenerasikannya. Inovasi ini telah membantu mengatasi masalah penggunaan ulang alamat, yang serius bagi privasi pengguna. BIP32 juga memungkinkan pembuatan sub-cabang dalam dompet yang sama untuk memudahkan pengelolaannya.