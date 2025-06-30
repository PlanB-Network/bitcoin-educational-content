---
term: BIP0032

---
BIP32 memperkenalkan konsep dari sebuah dompet deterministik hirarkis (dompet HD). Proposal ini memungkinkan untuk menghasilkan sebuah hirarki pasangan kunci dari sebuah `master seed` yang sama, menggunakan fungsi derivasi satu arah. Setiap pasangan kunci yang dihasilkan dapat menjadi induk dari anak kunci lainnya, sehingga membentuk struktur seperti pohon (hirarki). Keuntungan dari BIP32 adalah memungkinkan pengelolaan beberapa pasangan kunci yang berbeda dengan kebutuhan untuk hanya menyimpan satu seed untuk meregenerasinya. Inovasi ini secara khusus telah membantu menyelesaikan masalah penggunaan ulang alamat, yang merupakan masalah serius bagi privasi pengguna. BIP32 juga memungkinkan pembuatan sub-cabang dalam dompet yang sama untuk memudahkan pengelolaannya.
