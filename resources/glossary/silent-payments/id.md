---
term: PEMBAYARAN SILENT
---

Metode untuk menggunakan alamat Bitcoin statis untuk menerima pembayaran tanpa penggunaan ulang alamat, tanpa interaksi, dan tanpa tautan on-chain yang terlihat antara pembayaran yang berbeda dan alamat statis tersebut. Teknik ini menghilangkan kebutuhan untuk menghasilkan alamat penerima baru yang belum digunakan untuk setiap transaksi, sehingga menghindari interaksi biasa dalam Bitcoin di mana penerima harus menyediakan alamat baru kepada pembayar.

Dengan Pembayaran Silent, pembayar menggunakan kunci publik penerima (kunci publik pengeluaran dan kunci publik pemindaian) dan jumlah kunci privat mereka sendiri sebagai input untuk menghasilkan alamat baru untuk setiap pembayaran. Hanya penerima, dengan kunci privat mereka, yang dapat menghitung kunci privat yang sesuai dengan alamat pembayaran ini. ECDH (*Elliptic-Curve Diffie-Hellman*), algoritma pertukaran kunci kriptografis, digunakan untuk menetapkan rahasia bersama yang kemudian digunakan untuk menurunkan alamat penerima dan kunci privat (hanya di sisi penerima). Untuk mengidentifikasi Pembayaran Silent yang ditujukan untuk mereka, penerima harus memindai blockchain dan memeriksa setiap transaksi yang sesuai dengan kriteria protokol. Tidak seperti BIP47, yang menggunakan transaksi notifikasi untuk menetapkan saluran pembayaran, Pembayaran Silent menghilangkan langkah ini, menghemat sebuah transaksi. Namun, komprominya adalah bahwa penerima harus memindai semua transaksi potensial untuk menentukan, dengan menerapkan ECDH, apakah mereka ditujukan kepada mereka.

Sebagai contoh, alamat statis Bob $B$ mewakili penggabungan kunci publik pemindaian dan kunci publik pengeluarannya:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Kunci-kunci ini hanya diturunkan dari jalur berikut:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Alamat statis ini dipublikasikan oleh Bob. Alice mengambilnya untuk membuat Pembayaran Silent kepada Bob. Dia menghitung alamat pembayaran Bob $P_0$ dengan cara ini:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Dimana:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Dengan:
* $B_{\text{scan}}$: Kunci publik pemindaian Bob (alamat statis);
* $B_{\text{spend}}$: Kunci publik pengeluaran Bob (alamat statis);
* $A$: Jumlah kunci publik dalam input (tweak);
* $a$: Kunci privat dari tweak, yaitu, jumlah semua pasangan kunci yang digunakan dalam `scriptPubKey` dari UTXO yang dikonsumsi sebagai input dalam transaksi Alice;
* $\text{outpoint}_L$: UTXO terkecil (secara leksikografis) yang digunakan sebagai input dalam transaksi Alice;
* $\text{ ‖ }$: Konkatenasi (operasi menggabungkan operand dari ujung ke ujung);
* $G$: Titik generator dari kurva elips `secp256k1`;
* $\text{hash}$: Fungsi hash SHA256 yang ditandai dengan `BIP0352/SharedSecret`;
* $P_0$: Kunci publik pertama / alamat unik untuk pembayaran kepada Bob;
* $0$: Sebuah bilangan bulat yang digunakan untuk menghasilkan beberapa alamat pembayaran unik.

Bob memindai blockchain untuk menemukan Pembayaran Silent-nya dengan cara ini:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Dengan:
* $b_{\text{scan}}$: Kunci pemindaian privat Bob.

Jika dia menemukan $P_0$ sebagai alamat yang mengandung Pembayaran Senyap yang ditujukan kepadanya, dia menghitung $p_0$, kunci privat yang memungkinkan dia untuk menghabiskan dana yang dikirim oleh Alice ke $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Dengan:
* $b_{\text{spend}}$: Kunci pengeluaran privat Bob;
* $n$: urutan kurva eliptik `secp256k1`.

Selain versi dasar ini, label juga dapat digunakan untuk menghasilkan beberapa alamat statis yang berbeda dari alamat statis dasar yang sama, dengan tujuan memisahkan beberapa penggunaan tanpa tidak wajar menggandakan pekerjaan yang diperlukan selama pemindaian.