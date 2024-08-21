`Bech32` dan `Bech32m` adalah dua format pengkodean alamat untuk menerima bitcoin. Kedua format ini berbasis pada base 32 yang sedikit dimodifikasi. Mereka menggabungkan checksum berdasarkan algoritma koreksi kesalahan yang disebut BCH (*Bose-Chaudhuri-Hocquenghem*). Dibandingkan dengan alamat Legacy yang dikodekan dalam `Base58check`, alamat `Bech32` dan `Bech32m` memiliki checksum yang lebih efisien, memungkinkan deteksi dan potensi koreksi otomatis dari kesalahan ketik. Format mereka juga menawarkan keterbacaan yang lebih baik, dengan hanya menggunakan karakter huruf kecil. Berikut adalah matriks penambahan untuk format ini dari basis 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 dan Bech32m adalah format pengkodean yang digunakan untuk merepresentasikan alamat SegWit. Bech32 adalah format pengkodean alamat yang diperkenalkan oleh BIP173 pada tahun 2017. Format ini menggunakan set karakter spesifik, yang terdiri dari angka dan huruf kecil, untuk meminimalkan kesalahan ketik dan memudahkan pembacaan. Alamat Bech32 umumnya dimulai dengan `bc1` untuk menunjukkan bahwa mereka asli untuk SegWit. Format ini hanya digunakan pada alamat SegWit V0, dengan skrip P2WPKH (Pay to Witness Public Key Hash) dan P2WSH (Pay to Witness Script Hash). Namun, ada kecacatan kecil dan tak terduga khusus pada format Bech32. Kapan pun karakter terakhir dari alamat adalah `p`, menambahkan atau mengurangi jumlah karakter `q` yang langsung mendahuluinya tidak akan membuat checksum menjadi tidak valid. Ini tidak mempengaruhi penggunaan eksisting dari alamat SegWit V0 (BIP173) karena pembatasan mereka pada dua panjang yang ditentukan. Namun, ini bisa mempengaruhi penggunaan masa depan dari pengkodean Bech32. Format Bech32m hanyalah format Bech32 dengan kesalahan ini diperbaiki. Format ini diperkenalkan dengan BIP350 pada tahun 2020. Alamat Bech32m juga dimulai dengan `bc1`, tetapi mereka secara khusus dirancang untuk kompatibel dengan SegWit V1 (Taproot) dan versi selanjutnya, dengan skrip P2TR (Pay to TapRoot).