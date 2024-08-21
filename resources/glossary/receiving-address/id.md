---
term: ALAMAT PENERIMAAN
---

Informasi yang digunakan untuk menerima bitcoin. Sebuah alamat biasanya dibuat dengan meng-hash kunci publik, menggunakan `SHA256` dan `RIMPEMD160`, dan menambahkan metadata ke digest ini. Kunci publik yang digunakan untuk membuat alamat penerimaan adalah bagian dari dompet pengguna dan oleh karena itu berasal dari seed mereka. Sebagai contoh, alamat SegWit terdiri dari informasi berikut:
* Sebuah HRP untuk menunjukkan "bitcoin": `bc`;
* Sebuah pemisah: `1`;
* Versi SegWit yang digunakan: `q` atau `p`;
* Payload: digest dari kunci publik (atau langsung kunci publik dalam kasus Taproot);
* Checksum: kode BCH.

Namun, alamat penerimaan juga bisa mewakili sesuatu yang lain tergantung pada model skrip yang digunakan. Sebagai contoh, alamat P2SH dibuat menggunakan hash dari skrip. Di sisi lain, alamat Taproot mengandung kunci publik yang telah dimodifikasi langsung tanpa meng-hash-nya.

Alamat penerimaan dapat direpresentasikan dalam bentuk string alfanumerik atau sebagai kode QR. Setiap alamat dapat digunakan beberapa kali, tetapi ini adalah praktik yang sangat tidak disarankan. Memang, untuk menjaga tingkat privasi tertentu, disarankan untuk menggunakan setiap alamat Bitcoin hanya sekali. Alamat baru harus dihasilkan untuk setiap pembayaran masuk ke dompet seseorang. Alamat dienkod dalam `Bech32` untuk alamat SegWit V0, dalam `Bech32m` untuk alamat SegWit V1, dan dalam `Base58check` untuk alamat Legacy. Dari sudut pandang teknis, menerima bitcoin berarti memiliki kunci privat yang terkait dengan kunci publik (dan dengan demikian sebuah alamat). Ketika seseorang menerima bitcoin, pengirim memperbarui batasan yang ada pada pengeluaran mereka sehingga hanya penerima yang sekarang memiliki kekuatan ini.

![](../../dictionnaire/assets/23.png)