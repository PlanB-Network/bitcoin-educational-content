---
term: SILENT PAYMENT
---
Metode untuk menggunakan alamat Bitcoin statis untuk menerima pembayaran tanpa penggunaan ulang alamat, tanpa interaksi, dan tanpa tautan _on-chain_ yang terlihat antara pembayaran yang berbeda dan alamat statis. Teknik ini menghilangkan kebutuhan untuk membuat alamat penerima baru yang tidak terpakai untuk setiap transaksi, sehingga menghindari interaksi yang biasa terjadi pada Bitcoin di mana penerima harus memberikan alamat baru kepada pembayar.

Dengan _Silent Payment_, pembayar menggunakan kunci publik penerima (menghabiskan kunci publik dan memindai kunci publik) dan jumlah kunci privat mereka sendiri sebagai input untuk menghasilkan alamat baru untuk setiap pembayaran. Hanya penerima, dengan kunci pribadi mereka, yang dapat menghitung kunci pribadi yang sesuai dengan alamat pembayaran ini. ECDH (*Eliptic-Curve Diffie-Hellman*), sebuah algoritma pertukaran kunci kriptografi, digunakan untuk membuat sebuah rahasia bersama yang kemudian digunakan untuk mendapatkan alamat penerima dan kunci privat (hanya di sisi penerima). Untuk mengidentifikasi _Silent Payment_ yang ditujukan kepada mereka, penerima harus memindai _blockchain_ dan memeriksa setiap transaksi yang sesuai dengan kriteria protokol. Tidak seperti BIP47, yang menggunakan transaksi notifikasi untuk membuat saluran pembayaran, _Silent Payment_ menghilangkan langkah ini, sehingga menghemat data transaksi. Akan tetapi, komprominya adalah penerima harus memindai semua transaksi potensial untuk menentukan, dengan menerapkan ECDH, apakah transaksi tersebut ditujukan kepada mereka.

Sebagai contoh, alamat statis Bob, $B$, merepresentasikan gabungan dari kunci publik pemindaian dan kunci publik pengeluarannya:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{membelanjakan}} $$

Kunci-kunci ini secara sederhana diderivasi dari jalur berikut ini:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Alamat statis ini diterbitkan oleh Bob. Alice mengambilnya untuk melakukan _Silent Payment_ kepada Bob. Dia menghitung alamat pembayaran Bob $P_0$ dengan cara ini:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Dimana:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

Dengan:


- $B_{\text{scan}}$: Kunci publik pemindaian Bob (alamat statis);
- $B_{\text{spend}}$: Kunci publik pengeluaran Bob (alamat statis);
- $A$: Jumlah kunci publik dalam input (_tweak_);
- $a$: Kunci pribadi dari _tweak_, yaitu jumlah dari semua pasangan kunci yang digunakan dalam `scriptPubKey` dari UTXO yang digunakan sebagai input dalam transaksi Alice;
- $\text{outpoint}_L$: UTXO terkecil (secara leksikografis) yang digunakan sebagai _input_ dalam transaksi Alice;
- $\text{ ‖ }$: Penggabungan (operasi penggabungan operan dari ujung ke ujung);
- $G$: Titik generator kurva elips `secp256k1`;
- $\text{hash}$: Fungsi hash SHA256 yang ditandai dengan `BIP0352/SharedSecret`;
- $P_0$: Kunci publik pertama/alamat unik untuk pembayaran ke Bob;
- $0$: Bilangan bulat yang digunakan untuk menghasilkan beberapa alamat pembayaran yang unik.

Bob memindai _blockchain_ untuk menemukan _Silent Payment_-nya dengan cara ini:

$$ P_0 = B_{\text{buang}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Dengan:


- $b_{\text{scan}}$: Kunci pemindaian pribadi Bob.

Jika ia menemukan $P_0$ sebagai alamat yang berisi Silent Payment yang ditujukan kepadanya, ia akan menghitung $p_0$, kunci privat yang mengijinkannya untuk membelanjakan dana yang dikirim oleh Alice ke $P_0$:

$$ p_0 = (b_{\text{pengeluaran}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Dengan:


- $b_{\text{spend}}$: Kunci pengeluaran pribadi Bob;
- $n$: urutan kurva elips `secp256k1`.

Selain versi dasar ini, label juga dapat digunakan untuk menghasilkan beberapa alamat statis yang berbeda dari alamat statis dasar yang sama, dengan tujuan memisahkan beberapa penggunaan tanpa melipatgandakan pekerjaan yang diperlukan selama pemindaian.
