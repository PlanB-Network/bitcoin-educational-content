---
name: Frase Mnemonik - Lemparan Dadu
description: Bagaimana cara menghasilkan frase pemulihan kamu sendiri dengan dadu?
---

![cover](assets/cover.webp)

Dalam tutorial ini, kamu akan belajar bagaimana cara membuat seed phrase untuk dompet Bitcoin secara manual menggunakan lemparan dadu.

**PERINGATAN:** Menghasilkan seed phrase secara aman mengharuskan kamu tidak meninggalkan jejak digital selama proses pembuatannya, yang hampir mustahil dilakukan. Jika tidak, dompet tersebut akan memiliki permukaan serangan yang terlalu besar, sehingga secara signifikan meningkatkan risiko bitcoin kamu dicuri. **Oleh karena itu, sangat disarankan untuk tidak mentransfer dana ke dompet yang bergantung pada seed phrase yang kamu hasilkan sendiri.** Meskipun kamu mengikuti tutorial ini dengan tepat, tetap ada risiko bahwa seed phrase bisa dikompromikan. **Karena itu, tutorial ini tidak boleh diterapkan untuk pembuatan dompet nyata.** Menggunakan hardware wallet untuk tugas ini jauh lebih aman, karena perangkat tersebut menghasilkan seed phrase secara offline, dan para kriptografer telah mempertimbangkan penggunaan sumber entropi yang andal.

Tutorial ini hanya boleh diikuti untuk tujuan eksperimental dalam pembuatan dompet fiktif, tanpa niat menggunakannya dengan bitcoin nyata. Namun, pengalaman ini menawarkan dua manfaat:

- Pertama, ini memungkinkan kamu untuk lebih memahami mekanisme dasar dompet Bitcoin kamu;
- Kedua, ini membuat kamu tahu bagaimana melakukannya. Aku tidak mengatakan ini pasti akan berguna suatu hari nanti, tapi siapa tahu!

## Apa itu frase mnemonik?

Seed phrase, yang juga terkadang disebut "mnemonik," "seedphrase," atau "frase rahasia," adalah urutan yang biasanya terdiri dari 12 atau 24 kata, yang dihasilkan secara pseudo-acak dari sumber entropi. Urutan pseudo-acak ini selalu dilengkapi dengan checksum.

Frase mnemonik, bersama dengan passphrase opsional, digunakan untuk menurunkan semua kunci yang terkait dengan dompet HD (Hierarchical Deterministic) secara deterministik. Artinya, dari frasa ini kamu bisa menghasilkan dan merekonstruksi semua kunci privat dan publik dari dompet Bitcoin, dan pada akhirnya mengakses dana yang terkait dengannya.

![mnemonic](assets/notext/1.webp)
Tujuan dari frasa ini adalah untuk menyediakan cara pencadangan dan pemulihan bitcoin yang mudah digunakan. Sangat penting untuk menyimpan frase mnemonik di tempat yang aman dan terlindungi, karena siapa pun yang memiliki frasa ini akan memiliki akses ke dana dari dompet yang terkait. Jika digunakan dalam konteks dompet tradisional, dan tanpa passphrase opsional, frasa ini sering kali menjadi SPOF (Single Point Of Failure).

Biasanya, frasa ini diberikan langsung kepadamu saat membuat dompet, baik oleh perangkat lunak maupun hardware wallet yang digunakan. Namun, kamu juga bisa menghasilkan frasa ini sendiri, lalu memasukkannya ke media yang kamu pilih untuk menurunkan kunci dompet. Itulah yang akan kita pelajari dalam tutorial ini.

## Persiapan bahan yang diperlukan

Untuk membuat seed phrase secara manual, kamu akan membutuhkan:

- Selembar kertas;
- Pena atau pensil, idealnya dengan warna berbeda agar lebih mudah diatur;
- Beberapa dadu, untuk meminimalkan risiko bias yang terkait dengan dadu yang tidak seimbang;

- [Daftar 2048 kata BIP39](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/tutorials/wallet/generate-mnemonic-phrase/assets/BIP39-WORDLIST.pdf) yang dicetak.

Selanjutnya, kamu perlu menggunakan komputer dengan terminal untuk menghitung checksum. Inilah alasan utama kenapa aku tidak menyarankan pembuatan seed phrase secara manual. Menurutku, keterlibatan komputer, bahkan dengan langkah pencegahan yang disebutkan dalam tutorial ini, secara signifikan meningkatkan kerentanan dompet. Untuk pendekatan eksperimental dalam membuat "dompet fiktif", kamu bisa menggunakan komputer biasa beserta terminalnya. Namun, untuk pendekatan yang lebih ketat dengan tujuan membatasi risiko kompromi pada frasamu, idealnya gunakan PC yang terputus dari internet, lebih baik lagi tanpa komponen WiFi atau koneksi kabel RJ45, dan hanya dilengkapi periferal minimum (semua harus terhubung melalui kabel, untuk menghindari Bluetooth), dan yang terpenting, berjalan pada distribusi Linux amnesik seperti [Tails](https://tails.boum.org/index.fr.html), yang dimulai dari media yang dapat dilepas.
![mnemonic](assets/notext/2.webp)

Dalam konteks nyata, sangat penting untuk memastikan kerahasiaan ruang kerja kamu dengan memilih lokasi yang jauh dari pandangan orang lain, tanpa lalu lalang, dan bebas dari kamera, baik webcam maupun ponsel.

Disarankan untuk menggunakan beberapa dadu sekaligus guna mengurangi dampak dadu yang mungkin tidak seimbang terhadap entropi. Sebelum digunakan, sebaiknya dadu diperiksa terlebih dahulu. Kamu bisa melakukannya dengan menguji dadu dalam mangkuk berisi air garam jenuh hingga dadu mengapung. Lalu gulirkan setiap dadu sekitar dua puluh kali di dalam air tersebut sambil mengamati hasilnya. Jika satu atau dua sisi muncul secara tidak proporsional dibanding sisi lainnya, lanjutkan pengujian dengan lebih banyak lemparan. Jika hasilnya terdistribusi merata, dadu tersebut bisa dianggap andal. Namun, jika satu atau dua sisi secara konsisten mendominasi, dadu itu sebaiknya disisihkan karena dapat mengompromikan entropi seed phrase kamu dan, pada akhirnya, keamanan dompet kamu.

Dalam kondisi nyata, setelah melakukan pemeriksaan ini, kamu siap untuk menghasilkan entropi yang diperlukan. Untuk dompet fiktif eksperimental yang dibuat sebagai bagian dari tutorial ini, tentu saja kamu bisa melewati tahap persiapan ini.

## Beberapa Pengingat tentang Frasa Pemulihan

Sebagai awal, kita akan meninjau kembali dasar pembuatan frasa mnemonik menurut BIP39. Seperti yang sudah dijelaskan sebelumnya, frasa ini berasal dari informasi pseudo-acak dengan ukuran tertentu, lalu ditambahkan checksum untuk memastikan integritasnya.

Ukuran informasi awal ini, yang sering disebut sebagai "entropi", ditentukan oleh jumlah kata yang kamu inginkan dalam seed phrase. Format yang paling umum adalah frasa 12 kata dan 24 kata, yang masing-masing berasal dari entropi 128 bit dan 256 bit. Berikut adalah tabel yang menunjukkan berbagai ukuran entropi menurut BIP39:


| Frasa (kata) | Entropi (bit) | Checksum (bit) | Entropi + Checksum (bit) |
| ------------ | ------------- | -------------- | ------------------------ |
| 12           | 128           | 4              | 132                      |
| 15           | 160           | 5              | 165                      |
| 18           | 192           | 6              | 198                      |
| 21           | 224           | 7              | 231                      |
| 24           | 256           | 8              | 264                      |

Entropi adalah angka acak dengan panjang antara 128 hingga 256 bit. Dalam tutorial ini, kita akan menggunakan contoh frasa 12 kata, di mana entropinya berukuran 128 bit. Artinya, kita akan menghasilkan urutan acak yang terdiri dari 128 `0` atau `1`. Ini merepresentasikan sebuah angka dengan 128 digit dalam basis 2, atau biner. Berdasarkan entropi ini, checksum akan dihasilkan. Checksum adalah nilai yang dihitung dari sekumpulan data dan digunakan untuk memverifikasi integritas serta validitas data tersebut saat ditransmisikan atau disimpan. Algoritma checksum dirancang untuk mendeteksi kesalahan atau perubahan yang tidak disengaja dalam data. Dalam kasus frasa mnemonik, fungsi checksum adalah untuk mendeteksi kesalahan input saat kamu memasukkan frasa ke dalam perangkat lunak dompet. Checksum yang tidak valid menandakan adanya kesalahan dalam frasa tersebut. Sebaliknya, checksum yang valid menunjukkan bahwa frasa tersebut kemungkinan besar benar.

Untuk mendapatkan checksum ini, entropi dijalankan melalui fungsi hash SHA256. Operasi ini menghasilkan output berupa urutan 256 bit, di mana hanya `N` bit pertama yang akan diambil, dengan `N` bergantung pada panjang seed phrase yang diinginkan, seperti yang ditunjukkan pada tabel di atas. Jadi, untuk frasa 12 kata, 4 bit pertama dari hash akan digunakan.


![mnemonic](assets/en/3.webp)

4 bit pertama ini, yang membentuk checksum, kemudian akan ditambahkan ke entropi asli. Pada tahap ini, frasa pemulihan praktis telah terbentuk, namun masih dalam bentuk biner. Untuk mengonversi urutan biner ini menjadi kata-kata sesuai dengan standar BIP39, kita akan pertama-tama membagi urutan tersebut menjadi segmen-segmen 11-bit.

![mnemonic](assets/notext/4.webp)

Setiap paket ini mewakili sebuah angka dalam biner yang kemudian akan dikonversi menjadi angka desimal (basis 10). Kita akan menambahkan `1` ke setiap angka, karena dalam komputasi, penghitungan dimulai dari `0`, namun daftar BIP39 dinomori mulai dari `1`.

![mnemonic](assets/notext/5.webp)

Akhirnya, angka dalam desimal memberitahu kita posisi kata yang sesuai dalam [daftar 2048 kata BIP39](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/tutorials/wallet/generate-mnemonic-phrase/assets/BIP39-WORDLIST.pdf). Yang tersisa hanyalah memilih kata-kata ini untuk menyusun frasa pemulihan untuk dompet kita.

![mnemonic](assets/notext/6.webp)

Sekarang, mari kita lanjut ke praktik. Kita akan menghasilkan seed phrase 12 kata. Prosesnya tetap sama untuk frasa 24 kata, hanya saja kamu akan membutuhkan 256 bit entropi dan checksum 8 bit, seperti yang ditunjukkan pada tabel kesetaraan di awal bagian ini.

## Langkah 1: Menghasilkan Entropi

Siapkan lembaran kertas Anda, pena Anda, dan dadu Anda. Untuk memulai, kita perlu menghasilkan 128 bit secara acak, yaitu, sebuah urutan dari 128 `0` dan `1` berturut-turut. Untuk melakukan ini, kita akan menggunakan dadu.
![mnemonic](assets/notext/7.webp)

Dadu memiliki 6 sisi, masing-masing dengan peluang yang sama untuk muncul saat dilempar. Namun, tujuan kita adalah menghasilkan keluaran biner, yang berarti hanya ada dua kemungkinan hasil. Karena itu, kita akan menetapkan nilai `0` untuk setiap lemparan yang menghasilkan angka genap, dan `1` untuk setiap angka ganjil. Dengan begitu, kita perlu melakukan 128 lemparan untuk menghasilkan entropi 128 bit. Jika dadu menunjukkan `2`, `4`, atau `6`, kamu tulis `0`; jika menunjukkan `1`, `3`, atau `5`, tulis `1`. Setiap hasil dicatat secara berurutan, dari kiri ke kanan dan dari atas ke bawah.

Untuk mempermudah langkah berikutnya, kita akan mengelompokkan bit-bit tersebut ke dalam paket berisi empat dan tiga bit, seperti yang ditunjukkan pada gambar di bawah. Setiap baris harus terdiri dari 11 bit: dua paket 4 bit dan satu paket 3 bit.

![mnemonic](assets/notext/8.webp)
Seperti yang kamu lihat dalam contohku, kata kedua belas saat ini hanya terdiri dari 7 bit. Ini akan dilengkapi dengan 4 bit dari checksum pada langkah selanjutnya untuk membentuk 11 bit.
![mnemonic](assets/notext/9.webp)

## Langkah 2: Menghitung checksum

Langkah ini adalah yang paling krusial dalam pembuatan frasa mnemonic secara manual, karena mengharuskan penggunaan komputer. Seperti yang sudah disebutkan sebelumnya, checksum diambil dari bagian awal hash SHA256 yang dihasilkan dari entropi. Secara teori, memang mungkin menghitung SHA256 dengan tangan untuk input 128 atau 256 bit, tetapi proses ini bisa memakan waktu hingga berminggu-minggu. Selain itu, kesalahan sekecil apa pun dalam perhitungan manual kemungkinan besar baru akan terdeteksi di akhir proses, sehingga kamu harus mengulang semuanya dari awal. Karena itu, hampir mustahil melakukan langkah ini hanya dengan kertas dan pena. Penggunaan komputer pada praktiknya hampir tidak terhindarkan. Jika kamu tetap ingin belajar cara menghitung SHA256 secara manual, kami juga menjelaskan caranya di [kursus CRYPTO301](https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).

Karena alasan ini, aku sangat menyarankan untuk tidak membuat seed phrase secara manual untuk dompet yang benar-benar akan digunakan. Menurutku, menggunakan komputer pada tahap ini, bahkan dengan semua langkah pencegahan yang diperlukan, tetap secara tidak masuk akal memperbesar permukaan serangan dompet. Untuk menghitung checksum sambil meminimalkan jejak sebisa mungkin, kita akan menggunakan distribusi Linux amnesik dari media yang dapat dilepas bernama **Tails**. Sistem operasi ini dijalankan dari USB flash drive dan beroperasi sepenuhnya di RAM komputer, tanpa berinteraksi dengan hard drive. Dengan begitu, secara teori, tidak ada jejak yang tertinggal di komputer setelah dimatikan. Perlu dicatat bahwa Tails hanya kompatibel dengan prosesor tipe x86_64, dan tidak dengan prosesor tipe ARM.

Untuk memulai, dari komputer biasa milikmu, [unduh gambar Tails dari situs web resminya](https://tails.net/install/index.fr.html). Pastikan keaslian unduhan dengan menggunakan tanda tangan pengembang atau alat verifikasi yang ditawarkan oleh situs tersebut.
![mnemonic](assets/notext/10.webp)
Pertama, lanjutkan untuk memformat USB stick kamu, kemudian instal Tails menggunakan alat seperti [Balena Etcher](https://etcher.balena.io/).
![mnemonic](assets/notext/11.webp)
Setelah memastikan proses flashing berhasil, matikan komputer kamu. Lalu putuskan sambungan catu daya dan lepaskan hard drive dari motherboard PC. Jika ada kartu WiFi, sebaiknya ikut dilepas. Begitu juga dengan kabel Ethernet RJ45. Untuk meminimalkan risiko kebocoran data, disarankan mencabut router internet dan mematikan ponsel kamu. Selain itu, pastikan semua periferal yang tidak perlu, seperti mikrofon, webcam, speaker, atau headset, sudah dilepas, dan pastikan periferal lain hanya terhubung melalui kabel. Semua langkah persiapan ini sebenarnya tidak wajib, tetapi membantu mengurangi permukaan serangan semaksimal mungkin dalam konteks nyata.

Pastikan BIOS kamu dikonfigurasi agar mengizinkan boot dari perangkat eksternal. Jika belum, ubah pengaturannya lalu restart komputer. Setelah lingkungan komputer kamu aman, jalankan ulang komputer dan boot dari USB flash drive yang berisi OS Tails.

Di layar sambutan Tails, pilih bahasa pilihan kamu, kemudian luncurkan sistem dengan mengklik `Start Tails`.

![mnemonic](assets/notext/12.webp)

Dari desktop, klik pada tab `Applications`.

![mnemonic](assets/notext/13.webp)

Navigasikan ke menu `Utilities`.
Dan akhirnya, klik pada aplikasi `Terminal`.

![mnemonic](assets/notext/15.webp)

Anda akan sampai pada terminal perintah baru yang kosong.

![mnemonic](assets/notext/16.webp)
Ketik perintah `echo`, diikuti oleh entropi yang sebelumnya kamu hasilkan, pastikan untuk memasukkan spasi antara `echo` dan urutan digit biner kamu.
![mnemonic](assets/notext/17.webp)

Tambahkan spasi tambahan, lalu masukkan perintah berikut, menggunakan _pipe_ (`|`):

```plaintext
| shasum -a 256 -0
```

![mnemonic](assets/notext/18.webp)

Dalam contoh dengan entropi milikku, total perintahnya adalah sebagai berikut:

```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```

Dalam perintah ini:

- `echo` digunakan untuk mengirimkan urutan bit;
- `|`, _pipe_, digunakan untuk mengarahkan output dari perintah `echo` ke input dari perintah selanjutnya;
- `shasum` memulai fungsi hashing yang termasuk dalam keluarga SHA (_Secure Hash Algorithm_);
- `-a` menentukan pilihan algoritma hashing tertentu;
- `256` menunjukkan bahwa algoritma SHA256 digunakan;
- `-0` memungkinkan input diinterpretasikan sebagai angka biner.

Setelah memeriksa dengan teliti bahwa urutan biner kamu tidak mengandung kesalahan ketik, tekan tombol `Enter` untuk menjalankan perintah. Terminal kemudian akan menampilkan hash SHA256 dari entropi kamu.

![mnemonic](assets/notext/19.webp)

Untuk saat ini, hash dinyatakan dalam format heksadesimal (basis 16). Sebagai contoh, milik saya adalah:

```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```

Untuk menyelesaikan frasa mnemonik kita, kita hanya membutuhkan 4 bit pertama dari hash, yaitu checksum. Dalam format heksadesimal, setiap karakter merepresentasikan 4 bit. Jadi, kita cukup mengambil karakter pertama dari hash tersebut. Untuk frasa 24 kata, kamu perlu mengambil dua karakter pertama. Dalam contohku, karakter yang diperoleh adalah: `a`. Catat karakter ini dengan hati-hati di lembar kertas kamu, lalu matikan komputer.

Langkah selanjutnya adalah mengonversi karakter heksadesimal ini (basis 16) menjadi nilai biner (basis 2), karena frasa kita dibangun dalam format ini. Untuk melakukan ini, Anda dapat menggunakan tabel konversi berikut:

| Desimal (basis 10) | Heksadesimal (basis 16) | Biner (basis 2) |
| ------------------ | ----------------------- | --------------- |
| 0                  | 0                       | 0000            |
| 1                  | 1                       | 0001            |
| 2                  | 2                       | 0010            |
| 3                  | 3                       | 0011            |
| 4                  | 4                       | 0100            |
| 5                  | 5                       | 0101            |
| 6                  | 6                       | 0110            |
| 7                  | 7                       | 0111            |
| 8                  | 8                       | 1000            |

Dalam contoh saya, huruf `a` sesuai dengan angka biner `1010`. Keempat bit ini membentuk checksum dari frasa pemulihan kita. Kamu sekarang dapat menambahkannya ke entropi yang sudah kamu catat di lembaran kertas, menempatkannya di akhir kata terakhir.

![mnemonic](assets/notext/20.webp)

Seed phrase kamu sekarang sudah lengkap, tetapi masih dalam format biner. Langkah berikutnya adalah mengonversinya ke sistem desimal agar setiap angka bisa dipasangkan dengan kata yang sesuai dalam daftar BIP39.

## Langkah 3: Mengonversi Kata-kata ke Desimal

Untuk mengonversi setiap baris biner menjadi angka desimal, kita akan memakai metode yang memudahkan perhitungan manual. Saat ini, kamu memiliki dua belas baris di kertas, masing-masing terdiri dari 11 digit biner `0` atau `1`. Untuk mulai konversi ke desimal, beri nilai pada digit pertama sebesar `1024` jika bernilai `1`, jika tidak maka `0`. Untuk digit kedua, beri nilai `512` jika bernilai `1`, jika tidak `0`, dan lanjutkan dengan pola yang sama hingga digit kesebelas. Korespondensinya adalah sebagai berikut:

- Bit pertama: `1024`;
- Bit kedua: `512`;
- Bit ketiga: `256`;
- Bit keempat: `128`;
- Bit kelima: `64`;
- Bit keenam: `32`;
- Bit ketujuh: `16`;
- Bit kedelapan: `8`;
- Bit kesembilan: `4`;
- Bit kesepuluh: `2`;
- Bit kesebelas: `1`.

Untuk setiap baris, kita akan menjumlahkan nilai-nilai yang sesuai dengan digit `1` untuk mendapatkan angka desimal yang setara dengan angka biner. Mari kita ambil contoh baris biner yang sama dengan:

```plaintext
1010 1101 101
```

Konversinya akan sebagai berikut:
![mnemonic](assets/notext/21.webp)
Hasilnya kemudian akan menjadi:

```plaintext
1389
```

Untuk setiap bit yang sama dengan `1`, laporkan angka yang terkait di bawah ini. Untuk setiap bit yang sama dengan `0`, laporkan tidak ada.

![mnemonic](assets/notext/22.webp)
Kemudian, cukup jumlahkan semua angka yang divalidasi oleh `1` untuk mendapatkan angka desimal yang mewakili setiap baris biner. Misalnya, inilah tampilannya untuk lembaran saya:
![mnemonic](assets/notext/23.webp)

## Langkah 4: Mencari Kata-kata dari Frasa Mnemonik

Dengan angka desimal yang diperoleh, kita sekarang dapat menemukan kata-kata yang sesuai dalam daftar untuk menyusun frasa mnemonik. Namun, penomoran dari 2048 kata dalam daftar BIP39 berkisar dari `1` hingga `2048`. Tetapi, hasil biner yang dihitung berkisar dari `0` hingga `2047`. Oleh karena itu, ada pergeseran satu unit yang perlu diperbaiki. Untuk memperbaiki pergeseran ini, cukup tambahkan `1` ke dua belas angka desimal yang sebelumnya dihitung.

![mnemonic](assets/notext/24.webp)
Setelah penyesuaian ini, kamu sekarang memiliki indeks setiap kata dalam daftar. Langkah terakhir tinggal mengidentifikasi masing-masing kata berdasarkan nomornya. Tentu saja, seperti semua langkah sebelumnya, kamu tidak boleh menggunakan komputer untuk melakukan konversi ini. Karena itu, pastikan kamu sudah mencetak daftar tersebut sebelumnya.
[**-> Cetak daftar BIP39 dalam format A4.**](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/tutorials/wallet/generate-mnemonic-phrase/assets/BIP39-WORDLIST.pdf)

Sebagai contoh, jika nomor yang diperoleh dari baris pertama adalah 1721, kata yang sesuai akan menjadi kata ke-1721 dalam daftar:

```plaintext
1721. strike
```

![mnemonic](assets/notext/25.webp)
Dengan cara ini, kita melanjutkan secara bertahap dengan 12 kata untuk membentuk frasa mnemonik kita.

![mnemonic](assets/notext/26.webp)

## Langkah 5: Membuat Dompet Bitcoin

Pada titik ini, yang tersisa hanyalah mengimpor frasa mnemonik kita ke dalam perangkat lunak dompet Bitcoin. Tergantung pada preferensi kita, ini dapat dilakukan pada perangkat lunak desktop untuk mendapatkan hot wallet, atau pada hardware wallet untuk cold wallet.

![mnemonic](assets/notext/27.webp)

Baru saat proses impor kamu bisa memverifikasi apakah checksum yang kamu hasilkan valid. Jika perangkat lunak menampilkan pesan seperti `Invalid Checksum`, itu berarti ada kesalahan yang terjadi selama proses pembuatan. Biasanya, kesalahan ini berasal dari perhitungan yang keliru saat konversi dan penjumlahan manual, atau dari salah ketik ketika memasukkan entropi ke terminal di Tails. Untuk memperbaikinya, kamu perlu mengulang seluruh proses dari awal.

![mnemonic](assets/notext/28.webp)
Setelah membuat dompet kamu, jangan lupa untuk mencadangkan seed phrase di media fisik, seperti kertas atau logam, lalu hancurkan lembar kerja yang digunakan selama proses pembuatannya untuk mencegah kebocoran informasi.

## Kasus Spesifik Opsi Dice Roll pada Coldcards

Dompet hardware dari keluarga Coldcard menawarkan [fitur yang dinamakan _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), untuk menghasilkan frasa pemulihan dompet kamu dengan dadu. Metode ini sangat menarik karena memberi kamu kendali langsung atas proses pembuatan entropi, tanpa perlu menggunakan perangkat eksternal untuk menghitung checksum seperti pada pendekatan lain di tutorial ini.

Namun, beberapa insiden pencurian bitcoin pernah dilaporkan akibat penggunaan fitur ini yang kurang tepat. Jumlah lemparan dadu yang terlalu sedikit dapat menghasilkan entropi yang tidak memadai, sehingga secara teoretis memungkinkan seed phrase di-brute force dan bitcoin yang terkait dicuri. Untuk menghindari risiko ini, disarankan melakukan setidaknya 99 lemparan dadu pada Coldcard, agar entropi yang dihasilkan cukup kuat.

Metode interpretasi hasil yang diusulkan oleh Coldcard berbeda dari yang disajikan dalam tutorial ini. Dalam tutorial ini, kita merekomendasikan 128 lemparan untuk mencapai 128 bit keamanan. Sementara itu, Coldcard menyarankan 99 lemparan untuk mencapai 256 bit keamanan. Perbedaannya terletak pada cara hasil dadu diolah. Dalam pendekatan kita, setiap lemparan hanya memiliki dua kemungkinan hasil: genap (`0`) atau ganjil (`1`). Karena itu, entropi per lemparan adalah `log2(2)`. Pada pendekatan Coldcard, keenam sisi dadu, dari `1` sampai `6`, dimanfaatkan sepenuhnya. Dengan demikian, entropi per lemparan adalah `log2(6)`. Inilah alasan mengapa dalam tutorial ini kita membutuhkan lebih banyak lemparan untuk mencapai tingkat entropi yang setara.

Entropi = jumlah lemparan \* log2(jumlah kemungkinan hasil pada dadu)
Coldcard :

Entropi = 99 \* log2(6)
Entropi = 255.91

Tutorial Kami :

Entropi = 128 \* log2(2)
Entropi = 128
