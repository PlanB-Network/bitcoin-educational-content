---
term: STONEWALL X2

---
Sebuah bentuk transaksi Bitcoin khusus yang bertujuan untuk meningkatkan privasi pengguna selama melakukan pembelanjaan, dengan berkolaborasi dengan pihak ketiga yang tidak terlibat dalam pembelanjaan. Metode ini mensimulasikan penggabungan koin mini antara dua partisipan, saat melakukan pembayaran kepada pihak ketiga. Transaksi Stonewall x2 tersedia di aplikasi Samourai Wallet dan perangkat lunak Sparrow Wallet (keduanya dapat dioperasikan).

Pengoperasiannya relatif sederhana: menggunakan UTXO yang kami miliki untuk melakukan pembayaran dan mencari bantuan pihak ketiga yang juga berkontribusi dengan UTXO yang mereka miliki. Transaksi berakhir dengan empat keluaran: dua di antaranya dengan jumlah yang sama, satu ditujukan ke alamat penerima pembayaran, yang lainnya ke alamat milik kolaborator. UTXO ketiga dikirim kembali ke alamat kolaborator lain, memungkinkan mereka untuk mendapatkan kembali jumlah awal (tindakan netral bagi mereka, dikurangi biaya penambangan), dan UTXO terakhir kembali ke alamat yang kita miliki, yang merupakan perubahan dari pembayaran. Dengan demikian, ada tiga peran berbeda yang didefinisikan dalam transaksi Stonewall x2:


- Pengirim, yang melakukan pembayaran efektif;
- Kolaborator, yang menyediakan bitcoin untuk meningkatkan anonimitas transaksi secara keseluruhan, sambil memulihkan dana mereka sepenuhnya di akhir;
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya menunggu pembayaran dari pengirim.

![](../../dictionnaire/assets/3.webp)

Struktur Stonewall x2 menambahkan banyak entropi pada transaksi dan mengacaukan jejak analisis rantai. Dari luar, transaksi seperti itu dapat diartikan sebagai sebuah koin kecil antara dua orang. Namun pada kenyataannya, ini adalah sebuah pembayaran. Metode ini menghasilkan ketidakpastian dalam analisis rantai, atau bahkan mengarah ke jejak yang salah. Bahkan jika pengamat eksternal berhasil mengidentifikasi pola transaksi Stonewall x2, mereka tidak akan memiliki semua informasi. Mereka tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selain itu, mereka tidak akan dapat mengetahui siapa yang melakukan pembayaran. Terakhir, mereka tidak akan dapat menentukan apakah dua UTXO yang dimasukkan berasal dari dua orang yang berbeda atau apakah mereka milik satu orang yang menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall klasik mengikuti pola yang persis sama dengan transaksi Stonewall x2. Dari luar dan tanpa informasi tambahan mengenai konteksnya, tidak mungkin untuk membedakan transaksi Stonewall dengan transaksi Stonewall x2. Akan tetapi, yang pertama bukanlah transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Hal ini menambah keraguan akan pengeluaran tersebut.