---
term: BECH32 DAN BECH32M

---
`Bech32` dan `Bech32m` adalah dua format pengkodean alamat untuk menerima bitcoin. Keduanya didasarkan pada basis 32 yang sedikit dimodifikasi. Format ini menggunakan checksum berdasarkan algoritma pengoreksi kesalahan yang disebut BCH (*Bose-Chaudhuri-Hocquenghem*). Dibandingkan dengan alamat Legacy, yang dikodekan dalam `Base58check`, alamat `Bech32` dan `Bech32m` memiliki checksum yang lebih efisien, sehingga dapat mendeteksi dan mengoreksi kesalahan pengetikan secara otomatis. Format ini juga menawarkan keterbacaan yang lebih baik, dengan hanya menggunakan karakter huruf kecil. Berikut ini adalah matriks penjumlahan untuk format ini dari basis 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |



| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 dan Bech32m adalah format pengkodean yang digunakan untuk merepresentasikan alamat SegWit. Bech32 adalah format pengkodean alamat yang diperkenalkan oleh BIP173 pada tahun 2017. Format ini menggunakan sekumpulan karakter tertentu, yang terdiri dari angka dan huruf kecil, untuk meminimalkan kesalahan pengetikan dan memudahkan pembacaan. Alamat Bech32 umumnya dimulai dengan `bc1` untuk menunjukkan bahwa alamat tersebut berasal dari SegWit. Format ini hanya digunakan pada alamat SegWit V0, dengan skrip P2WPKH (Pay to Witness Public Key Hash) dan P2WSH (Pay to Witness Script Hash). Akan tetapi, terdapat sebuah kelemahan kecil yang tidak terduga khusus untuk format Bech32. Setiap kali karakter terakhir dari alamat adalah `p`, menambahkan atau menghapus sejumlah karakter `q` sebelum karakter tersebut tidak akan membatalkan checksum. Hal ini tidak memengaruhi penggunaan alamat SegWit V0 (BIP173) yang sudah ada karena dibatasi pada dua panjang yang ditentukan. Namun, hal ini dapat memengaruhi penggunaan pengkodean Bech32 di masa mendatang. Format Bech32m hanyalah format Bech32 dengan kesalahan ini diperbaiki. Format ini diperkenalkan dengan BIP350 pada tahun 2020. Alamat Bech32m juga dimulai dengan `bc1`, tetapi secara khusus dirancang agar kompatibel dengan SegWit V1 (Taproot) dan versi yang lebih baru, dengan skrip P2TR (Bayar ke TapRoot).