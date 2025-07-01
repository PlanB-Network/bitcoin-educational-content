---
term: OUTPUT SCRIPT DESCRIPTOR

---
_Output script descriptor_, atau secara sederhana disebut deskriptor, merupakan ekspresi terstruktur yang menjelaskan secara lengkap sebuah skrip keluaran (`scriptPubKey`) yang memberikan semua informasi yang diperlukan untuk melacak transaksi ke atau dari sebuah skrip tertentu. Deskriptor ini memfasilitasi pengelolaan kunci dalam dompet HD melalui deskripsi standar struktur dan jenis alamat yang digunakan.

Kegunaan utama dari deskriptor terletak pada kemampuannya untuk merangkum semua informasi penting untuk memulihkan sebuah dompet dalam satu string (selain frasa pemulihan). Dengan menyimpan deskriptor dengan frasa mnemonik yang sesuai, maka memungkinkan untuk memulihkan tidak hanya kunci pribadi tetapi juga struktur yang tepat dari dompet dan parameter skrip yang terkait. Memang, memulihkan sebuah dompet tidak hanya membutuhkan pengetahuan mengenai _seed_ awal tetapi juga indeks spesifik untuk menurunkan pasangan kunci anak, serta `xpub` dari setiap faktor dalam kasus dompet multisig. Sebelumnya, diasumsikan bahwa informasi ini secara implisit diketahui oleh semua orang. Akan tetapi, dengan adanya diversifikasi skrip dan munculnya konfigurasi yang lebih kompleks, informasi ini dapat menjadi sulit untuk diekstrapolasi, sehingga mengubah data ini menjadi informasi yang bersifat pribadi dan sulit untuk dipaksakan. Penggunaan deskriptor sangat menyederhanakan prosesnya: cukup dengan mengetahui frasa pemulihan dan deskriptor yang sesuai untuk memulihkan semuanya dengan andal dan aman.

Deskriptor terdiri dari beberapa elemen:


- Fungsi-fungsi skrip seperti `pk` (Bayar-ke-PubKey), `pkh` (Bayar-ke-PubKey-Hash), `wpkh` (Bayar-ke-Witness-PubKey-Hash), `sh` (Bayar-ke-Script-Hash), `wsh` (Bayar-ke-Script-Hash), `tr` (Bayar-ke-Taproot), `multi` (Multisignature), dan `sortedmulti` (Multisignature dengan kunci yang diurutkan);
- Jalur turunan, misalnya, `[d34db33f/44h/0h/0h]` yang mengindikasikan jalur turunan dan sidik jari kunci _master_ tertentu;
- Kunci dalam berbagai format seperti kunci publik heksadesimal atau _extended public key_ (`xpub`);
- _Checksum_, yang didahului dengan _hash_, untuk memverifikasi integritas deskriptor.

Sebagai contoh, deskriptor untuk dompet P2WPKH dapat terlihat seperti:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Dalam deskriptor ini, fungsi derivasi `wpkh` menunjukkan jenis skrip _Pay-to-Witness-Public-Key-Hash_. Diikuti oleh jalur derivasi yang berisi:


- `cdeab12f`: sidik jari dari kunci utama;
- `84h`: indikator yang menandakan penggunaan tujuan BIP84, yang ditujukan untuk alamat SegWit v0;
- `0h`: indikator yang mengindikasikan bahwa itu adalah mata uang BTC di _mainnet_;
- `0h`: mengacu pada nomor rekening tertentu yang digunakan dalam dompet.

Deskriptor juga termasuk _extended public key_ yang digunakan dalam dompet ini:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Selanjutnya, notasi `/<0;1>/*` menetapkan bahwa deskriptor dapat menghasilkan alamat dari rantai eksternal (`0`) dan internal (`1`), dengan _wildcard_ (`*`) yang mengizinkan derivasi berurutan dari beberapa alamat dengan cara yang dapat dikonfigurasi, mirip dengan mengelola "batas celah" pada perangkat lunak dompet tradisional.

Terakhir, `#jy0l7nr4` mewakili _checksum_ untuk memverifikasi integritas deskriptor.
