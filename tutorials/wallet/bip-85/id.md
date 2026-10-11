---
name: BIP-85
description: Bagaimana cara menggunakan BIP-85 ke generate beberapa seedphrase dari seed utama?
---
![cover](assets/cover.webp)



## 1. Memahami BIP-85



### 1.1 Apa itu BIP-85?



BIP-85 adalah fungsi lanjutan yang memungkinkan kamu membuat beberapa **seedphrase sekunder** dari satu **seedphrase utama**.



Setiap seedphrase sekunder dapat digunakan untuk membuat portofolio Bitcoin yang sepenuhnya independen. Portofolio ini bisa digunakan untuk berbagai tujuan: hot wallet di ponsel, portofolio untuk kerabat, portofolio tabungan terpisah, dan sebagainya.



Semua seedphrase sekunder diturunkan secara matematis, tetapi tidak mungkin untuk melacak kembali ke seedphrase utama dari seedphrase turunan tersebut. Ini memastikan pemisahan yang sepenuhnya antara setiap portofolio.



Selama kamu memiliki akses ke seedphrase utama kamu (dan passphrase terkait jika kamu menggunakannya), kamu dapat membuat ulang seedphrase sekunder **secara identik**, tanpa perlu menyimpannya secara terpisah.




### 1.2 Mengapa menggunakan BIP-85?



BIP-85 berguna jika kamu ingin :





- Buat beberapa portofolio Bitcoin independen tanpa banyak cadangan
- Kelola dana Anda sesuai dengan penggunaan yang berbeda (tabungan, pengeluaran, keluarga, proyek)
- Menjamin perlindungan bagi kerabat (fungsi "Paman Jim")
- Menghapus portofolio tanpa kehilangan akses ke dana kamu
- Sederhanakan keamanan Anda: hanya satu frasa kunci seed untuk melindungi



### 1.3 Keunggulan dibandingkan BIP-32



Dengan BIP-32, satu kalimat seed dapat digunakan untuk membuat generate hirarki lengkap dari akun dan alamat Bitcoin, menggunakan jalur derivasi (misalnya: `m/44'/0'/0'/0/0`). Setiap jalur dapat mewakili akun yang terpisah, tetapi **semuanya tetap terhubung ke kalimat seed yang sama**. Jadi, jika kalimat seed ini terganggu, **semua akun turunan dapat diakses**.



Dengan BIP-85, sebuah kalimat utama seed dapat digunakan untuk generate beberapa kalimat sekunder seed yang benar-benar independen: **Jika salah satu dari biji sekunder ini disusupi, penyerang tidak akan pernah bisa kembali ke seed utama atau mengakses portofolio lainnya**.


Hal ini memungkinkan untuk mengkotak-kotakkan risiko:





- Kamu dapat menggunakan seedphrase sekunder untuk hot wallet atau penggunaan sementara, dengan tingkat eksposur yang lebih tinggi.
- Bahkan jika hot wallet ini terganggu, dana kamu yang lain, yang dilindungi oleh seedphrase sekunder lainnya atau disimpan secara offline, **tetap aman**.



Di sisi lain, untuk BIP-32 dan BIP-85, jika seedphrase utama disusupi, **semua dana menjadi rentan**. Oleh karena itu, sangat penting untuk melindunginya dengan tingkat keamanan tertinggi.



![image](assets/fr/02.webp)


## 2. Kasus penggunaan praktis untuk BIP-85



BIP-85 memungkinkan kamu membuat beberapa portofolio Bitcoin dari satu seedphrase utama, masing-masing dengan seedphrase sekunder miliknya sendiri. Berikut lima kasus penggunaan praktis untuk mengatur dan mengamankan dana Bitcoin kamu. Setiap kasus menjelaskan mengapa menggunakan BIP-85 lebih praktis dibandingkan mengelola beberapa akun dengan satu seedphrase melalui BIP-32.



### 2.1 Membatasi risiko portofolio yang kurang aman





- **Skenario**: Kamu menggunakan "hot wallet" (dipasang pada perangkat yang terhubung ke internet) untuk transaksi harian.
- **Solusi BIP-85**: Kamu membuat seedphrase sekunder yang didedikasikan untuk portofolio ini.
- **Keunggulan dibandingkan BIP-32**: Kamu tidak perlu mengimpor seedphrase utama ke ponsel kamu, sehingga mengurangi risiko peretasan. Hanya seedphrase sekunder yang dapat dikompromikan, sehingga melindungi dompet kamu yang lain. Dengan BIP-32, kamu harus menggunakan seedphrase utama dan jalur derivasi, yang berarti mengekspos semua dana kamu.




### 2.2 Membuat portofolio untuk anggota keluarga





- **Skenario**: Kamu menyiapkan Bitcoin wallet untuk seseorang yang dekat dengan kamu (misalnya ibu kamu), sambil tetap bisa memulihkannya jika hilang.
- **Solusi BIP-85**: Kamu membuat seedphrase sekunder khusus dan hanya membagikan seedphrase ini.
- **Keunggulan dibandingkan BIP-32**: Dengan BIP-32, membuat akun untuk orang yang kamu cintai mengharuskan kamu membagikan seedphrase utama kamu, yang mempertaruhkan semua dana kamu dan membuat pengelolaan menjadi rumit bagi orang tersebut (harus mengelola jalur derivasi), atau kamu harus membuat seedphrase baru untuk disimpan terpisah dari seedphrase utama kamu




### 2.3 Memfasilitasi pengelolaan portofolio terpisah





- **Skenario**: Kamu memisahkan bitcoin kamu untuk tujuan yang berbeda (misalnya tabungan jangka panjang, dana non-KYC).
- **Solusi BIP-85**: Kamu membuat seedphrase sekunder yang didedikasikan untuk setiap tujuan.
- **Keunggulan dibandingkan BIP-32**: Dengan BIP-32, semua akun menggunakan seedphrase yang sama, yang mempersulit pengelolaan di portofolio pihak ketiga karena memerlukan jalur derivasi seperti `m/44'/0'/0'` untuk dikelola. Selain itu, tidak memungkinkan untuk menetapkan akun terpisah per perangkat (misalnya "tabungan di Coldcard", "harian di ponsel", "liburan di Trezor"). BIP-85 menetapkan seedphrase sekunder yang unik untuk setiap tujuan, yang mudah diidentifikasi dan diimpor seca



### 2.4 Menggunakan Wallet sementara untuk transaksi





- **Skenario**: Kamu memerlukan portofolio sementara untuk transaksi satu kali atau untuk menjaga privasi (misalnya pencampuran dana, interaksi dengan KYC exchange, dan lain-lain).
- **Solusi BIP-85**: Kamu membuat seedphrase sekunder, menggunakannya untuk transaksi tersebut, lalu menghancurkannya jika perlu, dengan mengetahui bahwa seedphrase ini dapat dibuat ulang kapan saja.
- **Keunggulan dibandingkan BIP-32**: Dengan BIP-32, akun sementara tetap bergantung pada seedphrase utama, yang berarti semua dana kamu terekspos jika terjadi kompromi.





## 3. Sebelum kamu mulai





- **Perangkat keras** (opsional)
 - Coldcard Mk4 atau Q1
 - Kartu microSD





- Pengetahuan dasar
 - Memahami frasa Mnemonic (BIP-39): daftar 12 hingga 24 kata untuk menyimpan portofolio.
- Pahami apa itu Bitcoin wallet: perangkat lunak atau perangkat keras untuk mengelola bitcoin kamu, serta cara memulihkannya menggunakan seedphrase.
- Sumber daya tambahan tersedia di bagian Lampiran.





- **Perangkat lunak** yang kompatibel
  - Sparrow Wallet (komputer, untuk manajemen watch-only atau manajemen tingkat lanjut)
  - Nunchuck (seluler, untuk multisignature)
  - BlueWallet (seluler)
  - ...



- 3.4 **Konfigurasi Coldcard**
  - Inisialisasi seedphrase 24 kata di Coldcard.
  - Opsional: tambahkan passphrase untuk mengamankan akses ke cabang BIP-85.
  - Aktifkan opsi yang berguna: NFC (untuk ekspor), nonaktifkan USB saat menggunakan baterai (keamanan).




## 4. Tutorial langkah demi langkah



Ikuti langkah-langkah berikut untuk membuat, menggunakan, dan mengambil Mnemonic sekunder dengan BIP-85 pada Coldcard.



### 4.1 generate sebuah kalimat sekunder seed



Kamj akan membuat frasa sekunder seed dari frasa utama seed milikmu.


Nyalakan Coldcard Anda, masukkan kode PIN.





- 1. Jika kamu telah menerapkan passphrase ke seed utama:
 - Dari layar Beranda, buka `passphrase`.
    - Pilih `Tambah Kata` dan masukkan kata sandi Anda.
    - Tekan `Terapkan`.
    - Periksa identitas Wallet: Buka `Advanced > View Identity` untuk mencatat sidik jari Wallet.





- 2. Buka menu **BIP-85**
 - Dari layar Beranda, buka `Advanced > Derive seed B85`
 - Baca peringatan dan konfirmasikan.



ColdCard menginformasikan kepada kamu bahwa benih yang dihasilkan secara matematis berasal dari seed utama milikmu, tetapi secara kriptografis benar-benar independen.


![image](assets/fr/03.webp)





- 3. Pilih format


Pilih format frasa seed: 12, 18 atau 24 kata. Periksa jumlah kata yang diterima oleh Wallet yang ingin kamu impor frasa seed.


![image](assets/fr/04.webp)





- 4. Pilih indeks
 - Masukkan indeks antara 0 dan 9999.
 - Indeks ini sangat penting untuk meregenerasi seed sekunder di kemudian hari. Simpanlah dengan hati-hati dengan label seperti: "Indeks 1 = Wallet mobile", "Indeks 2 = proyek keluarga", "Indeks 4 = campuran uji", ...
 - Jika kamu kehilangannya, Anda tidak akan kehilangan akses ke dana Anda, tetapi Anda harus menguji kombinasi dari 0 hingga 9999 untuk menemukannya.


![image](assets/fr/05.webp)





- 5. Catat atau ekspor kalimat sekunder seed****


ColdCard sekarang menampilkan kalimat sekunder seed yang baru. Anda bisa:




 - Catatan **catatan secara manual**.
 - Tekan :
     - 1` untuk menyimpannya di kartu SD
     - `2` untuk **memasukkan mode "gunakan seed ini "** pada ColdCard (berguna untuk mengekspor atau menandatangani transaksi)
     - 3` untuk menampilkan **kode QR** (untuk dipindai dengan aplikasi seluler seperti BlueWallet atau Nunchuck)
     - 4` untuk mengirimnya dengan **NFC**



💡 Pada titik ini, kamu memiliki frasa seed yang independen, dapat digunakan dalam Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Menggunakan seed sekunder



Kamu sekarang dapat menggunakan turunan seed ini untuk membuat portofolio baru dalam format :




- aplikasi seluler
- gW-68 lainnya
- portofolio Multisig



### 4.3 Memulihkan frasa sekunder seed yang hilang



Untuk mengambil seed sekunder kapan saja, ulangi prosesnya:


1. Mulai ulang ColdCard kamu


2. Masukkan PIN kamu


3. Masukkan passphrase kamu, jika sudah ditentukan


4. Pergi ke `Advanced > Derive seed B85`


5. Pilih format (12/18/24 kata)


6. Masukkan indeks yang sama (misalnya `1`)


7. Kamu akan mendapatkan seed sekunder yang sama persis




## 5. Batasan, risiko, dan praktik terbaik



### 5.1 Ketergantungan pada kalimat utama seed + passphrase



Penggunaan BIP85 sepenuhnya bergantung pada kalimat utama seed 24 kata, serta passphrase jika kamu telah menerapkannya.




- Dari kedua Elements ini, semua frasa sekunder seed dapat dibuat ulang.
- Tanpa salah satu dari 2 Elements ini, Anda akan kehilangan akses ke semua portofolio derivatif.



### 5.2 Risiko dalam konfigurasi multi-tanda tangan



Kami sangat menyarankan agar kamu tidak menggunakan seedphrase sekunder yang dihasilkan dari seedphrase utama yang sama dalam konfigurasi multisig. Jika perangkat atau seedphrase utama disusupi, semua kunci multisig dapat dibuat ulang oleh penyerang.



### 5.3 Kompatibilitas perangkat lunak



Tidak semua aplikasi secara langsung mendukung derivasi BIP85. Namun, seed yang dihasilkan melalui BIP85 adalah seed BIP39 standar (12, 18, atau 24 kata), sehingga dapat digunakan di Bitcoin wallet yang kompatibel dengan BIP39.



### 5.4 Daftar akun BIP85



Disarankan untuk menyimpan daftar pribadi seedphrase sekunder yang selalu diperbarui.



- Ini memungkinkan kamu dengan cepat mengetahui indeks BIP85 mana yang sesuai dengan portofolio tertentu, tanpa harus menyimpan seedphrase sekunder.
- Daftar ini harus tetap minimalis, tanpa menyebutkan Bitcoin secara eksplisit, dan harus disimpan terpisah dari seedphrase utama. Pastikan juga untuk mencantumkannya dalam rencana warisan kamu.



Daftar tersebut dapat berisi:



- indeks BIP85 yang digunakan (angka dari 0 hingga 9999)
- nama penggunaan atau referensi (misalnya hot wallet, tabungan pribadi, wallet ibu)
- jika diperlukan, fingerprint wallet untuk verifikasi di Coldcard



### 5.5 Pencadangan



Cadangan harus menyertakan file:



- gW-91 utama
- gW-76 (jika digunakan)



Jangan pernah menyimpan bersama:



- gW-93 dan passphrase utama
- gW-94 utama dan daftar akun BIP85



Sumber daya tambahan tersedia di Lampiran.



## LAMPIRAN



## A.1 Daftar Istilah





- [BUNYI](https://planb.academy/resources/glossary/bip)
- [BIP-32](https://planb.academy/resources/glossary/bip0032)
- [BIP-39](https://planb.academy/resources/glossary/bip0039)
- [BIP-85](https://planb.academy/resources/glossary/bip0085)
- [Frasa seed](https://planb.academy/resources/glossary/recovery-phrase)
- [passphrase](https://planb.academy/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.academy/resources/glossary/multisig)




### A.2 Simpan frasa pemulihan Anda



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Memahami passphrase BIP39



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Cara kerja portofolio Bitcoin



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
