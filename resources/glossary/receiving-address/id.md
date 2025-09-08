---
term: ALAMAT PENERIMA

---
Informasi yang digunakan untuk menerima bitcoin. Sebuah alamat biasanya dibuat dengan melakukan _hashing_ terhadap kunci publik, menggunakan `SHA256` dan `RIMPEMD160`, dan menambahkan metadata pada hal ini. Kunci publik yang digunakan untuk membuat alamat penerima adalah bagian dari dompet pengguna dan oleh karena itu berasal dari _seed_ mereka. Sebagai contoh, alamat SegWit terdiri dari informasi berikut ini:


- HRP untuk menunjuk "bitcoin": `bc`;
- Pemisah: `1`;
- Versi SegWit yang digunakan: `q` atau `p`;
- _Payload_: intisari dari kunci publik (atau langsung kunci publik dalam kasus Taproot);
- _Checksum_: kode BCH.

Namun, alamat penerima juga dapat merepresentasikan sesuatu yang lain tergantung pada model skrip yang digunakan. Sebagai contoh, alamat P2SH dibuat dengan menggunakan _hash_ skrip. Sebaliknya, alamat taproot berisi kunci publik yang sudah di-_tweak_ secara langsung tanpa melakukan _hash_.

Alamat penerima dapat direpresentasikan dalam bentuk _string_ alfanumerik atau sebagai kode QR. Setiap alamat dapat digunakan beberapa kali, namun hal ini sangat tidak disarankan. Memang, untuk menjaga tingkat privasi tertentu, disarankan untuk hanya menggunakan setiap alamat Bitcoin hanya sekali. Sebuah alamat baru harus dibuat untuk setiap pembayaran yang masuk ke dompet seseorang. Sebuah alamat dikodekan dalam `Bech32` untuk alamat SegWit V0, dalam `Bech32m` untuk alamat SegWit V1, dan dalam `Base58check` untuk alamat Legacy. Dari sudut pandang teknis, menerima bitcoin berarti memiliki kunci privat yang terkait dengan kunci publik (dan dengan demikian sebuah alamat). Ketika seseorang menerima bitcoin, pengirim akan memperbarui batasan yang ada pada pengeluaran mereka sehingga hanya penerima yang dapat memiliki kekuatan ini.

![](../../dictionnaire/assets/23.webp)
