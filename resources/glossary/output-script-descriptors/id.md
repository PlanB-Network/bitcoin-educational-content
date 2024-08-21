---
term: OUTPUT SCRIPT DESCRIPTORS
---

Deskriptor skrip keluaran, atau sederhananya deskriptor, adalah ekspresi terstruktur yang sepenuhnya mendeskripsikan sebuah skrip keluaran (`scriptPubKey`) dan menyediakan semua informasi yang diperlukan untuk melacak transaksi ke atau dari skrip tertentu. Deskriptor ini memfasilitasi pengelolaan kunci dalam dompet HD melalui deskripsi standar dari struktur dan jenis alamat yang digunakan.

Kepentingan utama dari deskriptor terletak pada kemampuannya untuk mengenkapsulasi semua informasi esensial untuk memulihkan dompet dalam satu string (selain dari frasa pemulihan). Dengan menyimpan deskriptor bersama dengan frasa mnemonik yang sesuai, dimungkinkan untuk memulihkan tidak hanya kunci privat tetapi juga struktur dompet yang tepat dan parameter skrip yang terkait. Memang, memulihkan dompet memerlukan tidak hanya pengetahuan tentang benih awal tetapi juga indeks spesifik untuk derivasi pasangan kunci anak, serta `xpub` dari setiap faktor dalam kasus dompet multisig. Sebelumnya, diasumsikan bahwa informasi ini secara implisit diketahui oleh semua orang. Namun, dengan diversifikasi skrip dan munculnya konfigurasi yang lebih kompleks, informasi ini bisa menjadi sulit untuk diekstrapolasi, sehingga mengubah data ini menjadi informasi privat dan sulit untuk ditebak. Penggunaan deskriptor sangat menyederhanakan proses: cukup dengan mengetahui frasa pemulihan dan deskriptor yang sesuai untuk memulihkan segalanya secara andal dan aman.

Sebuah deskriptor terdiri dari beberapa elemen:
* Fungsi skrip seperti `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature), dan `sortedmulti` (Multisignature dengan kunci yang diurutkan);
* Jalur derivasi, misalnya, `[d34db33f/44h/0h/0h]` menunjukkan jalur turunan dan sidik jari kunci induk tertentu;
* Kunci dalam berbagai format seperti kunci publik heksadesimal atau kunci publik terluas (`xpub`);
* Sebuah checksum, didahului oleh hash, untuk memverifikasi integritas deskriptor.

Sebagai contoh, sebuah deskriptor untuk dompet P2WPKH bisa terlihat seperti:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
Dalam deskriptor ini, fungsi derivasi `wpkh` menunjukkan tipe skrip Pay-to-Witness-Public-Key-Hash. Ini diikuti oleh jalur derivasi yang berisi:
* `cdeab12f`: sidik jari dari kunci induk;
* `84h`: yang menandakan penggunaan tujuan BIP84, dimaksudkan untuk alamat SegWit v0;
* `0h`: yang menunjukkan bahwa ini adalah mata uang BTC di mainnet;
* `0h`: yang merujuk pada nomor akun spesifik yang digunakan dalam dompet.

Deskriptor juga mencakup kunci publik terluas yang digunakan dalam dompet ini:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

Selanjutnya, notasi `/<0;1>/*` menunjukkan bahwa deskriptor dapat menghasilkan alamat dari rantai eksternal (`0`) dan internal (`1`), dengan wildcard (`*`) yang memungkinkan untuk derivasi sekuensial dari beberapa alamat secara konfigurabel, mirip dengan mengelola "batas gap" pada perangkat lunak dompet tradisional.

Akhirnya, `#jy0l7nr4` mewakili checksum untuk memverifikasi integritas dari deskriptor.