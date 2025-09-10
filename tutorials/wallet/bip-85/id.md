---
name: BIP-85
description: Bagaimana cara menggunakan BIP-85 ke generate beberapa seedphrase dari seed utama?
---
![cover](assets/cover.webp)



## 1. Memahami BIP-85



### 1.1 Apa itu BIP-85?



BIP-85 adalah fungsi lanjutan yang memungkinkan Anda membuat beberapa **frase sekunder seed** dari satu **frase utama seed**.



Setiap kalimat sekunder seed dapat digunakan untuk membuat portofolio Bitcoin yang sepenuhnya independen. Portofolio ini dapat digunakan untuk berbagai tujuan: Hot Wallet di ponsel, portofolio untuk kerabat, portofolio tabungan terpisah, dll.



Semua sub-frasa seed diturunkan secara matematis, tetapi tidak mungkin untuk melacak kembali ke frasa utama seed dari sub-frasa. Hal ini memastikan pemisahan yang lengkap antara setiap portofolio.



Selama Anda memiliki akses ke frasa utama seed Anda (dan passphrase yang terkait jika Anda menggunakannya), Anda dapat membuat ulang frasa sekunder seed **secara identik**, tanpa harus menyimpannya secara terpisah.



### 1.2 Mengapa menggunakan BIP-85?



BIP-85 berguna jika Anda ingin :





- Buat beberapa portofolio Bitcoin independen tanpa banyak cadangan
- Kelola dana Anda sesuai dengan penggunaan yang berbeda (tabungan, pengeluaran, keluarga, proyek)
- Menjamin perlindungan bagi kerabat (fungsi "Paman Jim")
- Menghapus portofolio tanpa kehilangan akses ke dana Anda
- Sederhanakan keamanan Anda: hanya satu frasa kunci seed untuk melindungi



### 1.3 Keunggulan dibandingkan BIP-32



Dengan BIP-32, satu kalimat seed dapat digunakan untuk membuat generate hirarki lengkap dari akun dan alamat Bitcoin, menggunakan jalur derivasi (misalnya: `m/44'/0'/0'/0/0`). Setiap jalur dapat mewakili akun yang terpisah, tetapi **semuanya tetap terhubung ke kalimat seed yang sama**. Jadi, jika kalimat seed ini terganggu, **semua akun turunan dapat diakses**.



Dengan BIP-85, sebuah kalimat utama seed dapat digunakan untuk generate beberapa kalimat sekunder seed yang benar-benar independen: **Jika salah satu dari biji sekunder ini disusupi, penyerang tidak akan pernah bisa kembali ke seed utama atau mengakses portofolio lainnya**.


Hal ini memungkinkan untuk mengkotak-kotakkan risiko:





- Anda dapat menggunakan seed sekunder untuk Hot Wallet atau penggunaan sementara, dengan menerima pencahayaan yang lebih tinggi.
- Bahkan jika Hot Wallet ini terganggu, dana Anda yang lain, yang dilindungi oleh benih sekunder lainnya atau disimpan secara offline, **tetap aman**.



Di sisi lain, untuk BIP-32 dan BIP-85, jika seed utama disusupi, **semua dana menjadi rentan**. Oleh karena itu, sangat penting untuk melindunginya dengan tingkat keamanan tertinggi.



![image](assets/fr/02.webp)


## 2. Kasus penggunaan praktis untuk BIP-85



BIP-85 memungkinkan Anda membuat beberapa portofolio Bitcoin dari satu frasa inti seed, masing-masing dengan frasa sekunder seed sendiri. Berikut adalah lima kasus penggunaan praktis untuk mengatur dan mengamankan dana Bitcoin Anda. Setiap kasus menjelaskan mengapa menggunakan BIP-85 lebih praktis daripada mengelola beberapa akun dengan satu frasa seed melalui BIP-32.



### 2.1 Membatasi risiko portofolio yang kurang aman





- Skenario**: Anda menggunakan "Hot Wallet" Wallet (dipasang pada perangkat yang terhubung ke Internet), untuk transaksi harian.
- Solusi BIP-85**: Anda membuat frasa sekunder seed yang didedikasikan untuk portofolio ini.
- Keunggulan dibandingkan BIP-32**: Anda tidak perlu mengimpor frasa primer seed ke ponsel Anda, sehingga mengurangi risiko peretasan. Hanya frasa sekunder seed yang dikompromikan, melindungi dompet Anda yang lain. Dengan BIP-32, Anda harus menggunakan frasa utama seed dan jalur bypass, mengekspos semua dana Anda.



### 2.2 Membuat portofolio untuk anggota keluarga





- Skenario**: Anda menyiapkan Bitcoin Wallet untuk seseorang yang dekat dengan Anda (misalnya ibu Anda), sekaligus dapat memulihkannya jika hilang.
- Solusi BIP-85**: Anda membuat kalimat sekunder seed khusus dan hanya membagikan kalimat ini.
- Keunggulan dibandingkan BIP-32**: Dengan BIP-32, membuat akun untuk orang yang Anda cintai mengharuskan Anda untuk berbagi frasa seed utama Anda, mempertaruhkan semua dana Anda dan manajemen yang rumit untuk orang yang Anda cintai (mengelola jalur percabangan), atau membuat frasa seed baru untuk disimpan di samping frasa seed utama Anda.



### 2.3 Memfasilitasi pengelolaan portofolio terpisah





- Skenario**: Anda memisahkan bitcoin Anda untuk tujuan yang berbeda (mis. tabungan jangka panjang, dana non-KYC).
- Solusi BIP-85**: Anda membuat frasa sekunder seed yang didedikasikan untuk setiap tujuan.
- Keunggulan dibandingkan BIP-32**: Dengan BIP-32, semua akun memiliki frasa seed yang sama, yang mempersulit pengelolaan dalam portofolio pihak ketiga karena memerlukan jalur turunan seperti `m/44'/0'/0'` untuk dikelola. Selain itu, tidak memungkinkan untuk menetapkan akun terpisah per perangkat (mis. "tabungan di Coldcard", "harian di ponsel", "liburan di Trezor"). BIP-85 menetapkan frasa sekunder seed yang unik per tujuan, yang mudah diidentifikasi dan diimpor secara terpisah pada setiap perangkat.



### 2.4 Menggunakan Wallet sementara untuk transaksi





- Skenario**: Anda memerlukan portofolio sementara untuk transaksi satu kali atau untuk menjaga kerahasiaan (misal: pencampuran dana, interaksi dengan KYC Exchange, dll.).
- Solusi BIP-85**: Anda membuat kalimat sekunder seed, menggunakannya untuk transaksi, kemudian menghancurkannya jika perlu, karena mengetahui bahwa kalimat tersebut dapat dibuat ulang.
- Keuntungan dibandingkan BIP-32**: Dengan BIP-32, akun sementara bergantung pada kalimat utama seed, yang mengekspos semua dana Anda jika disusupi.





## 3. Sebelum Anda mulai





- Perangkat keras** (opsional)
 - Coldcard Mk4 atau Q1
 - Kartu microSD





- Pengetahuan dasar
 - Memahami frasa Mnemonic (BIP-39): daftar 12 hingga 24 kata untuk menyimpan portofolio.
 - Ketahui apa itu Bitcoin Wallet: perangkat lunak atau perangkat untuk mengelola bitcoin Anda, dan cara mengembalikannya dengan frasa Mnemonic.
 - Lebih banyak sumber daya di Lampiran.





- Perangkat lunak** yang kompatibel
 - Sparrow wallet (komputer, untuk manajemen khusus jam tangan atau manajemen tingkat lanjut)
 - Nunchuck (seluler, untuk tanda tangan banyak)
 - BlueWallet (seluler)
 - ...





- 3.4 Konfigurasi kartu dingin**
 - Inisialisasi kalimat seed yang terdiri dari 24 kata pada Coldcard.
 - Opsional: Tambahkan passphrase untuk mengamankan akses ke cabang BIP-85.
 - Mengaktifkan opsi yang berguna: NFC (untuk ekspor), nonaktifkan USB pada baterai (keamanan).




## 4. Tutorial langkah demi langkah



Ikuti langkah-langkah berikut untuk membuat, menggunakan, dan mengambil Mnemonic sekunder dengan BIP-85 pada Coldcard Anda.



### 4.1 generate sebuah kalimat sekunder seed



Anda akan membuat frasa sekunder seed dari frasa utama seed Anda.


Nyalakan Coldcard Anda, masukkan kode PIN Anda.





- 1. Jika Anda telah menerapkan passphrase ke seed utama Anda:**
 - Dari layar Beranda, buka `passphrase`.
    - Pilih `Tambah Kata` dan masukkan kata sandi Anda.
    - Tekan `Terapkan`.
    - Periksa identitas Wallet: Buka `Advanced > View Identity` untuk mencatat sidik jari Wallet.





- 2. Buka menu BIP-85**
 - Dari layar Beranda, buka `Advanced > Derive seed B85`
 - Baca peringatan dan konfirmasikan.



ColdCard menginformasikan kepada Anda bahwa benih yang dihasilkan secara matematis berasal dari seed utama Anda, tetapi secara kriptografis benar-benar independen.


![image](assets/fr/03.webp)





- 3. Pilih format


Pilih format frasa seed: 12, 18 atau 24 kata. Periksa jumlah kata yang diterima oleh Wallet yang ingin Anda impor frasa seed Anda.


![image](assets/fr/04.webp)





- 4. Pilih indeks
 - Masukkan indeks antara 0 dan 9999.
 - Indeks ini sangat penting untuk meregenerasi seed sekunder di kemudian hari. Simpanlah dengan hati-hati dengan label seperti: "Indeks 1 = Wallet mobile", "Indeks 2 = proyek keluarga", "Indeks 4 = campuran uji", ...
 - Jika Anda kehilangannya, Anda tidak akan kehilangan akses ke dana Anda, tetapi Anda harus menguji kombinasi dari 0 hingga 9999 untuk menemukannya.


![image](assets/fr/05.webp)





- 5. Catat atau ekspor kalimat sekunder seed****


ColdCard sekarang menampilkan kalimat sekunder seed yang baru. Anda bisa:




 - Catatan **catatan secara manual**.
 - Tekan :
     - 1` untuk menyimpannya di kartu SD
     - `2` untuk **memasukkan mode "gunakan seed ini "** pada ColdCard (berguna untuk mengekspor atau menandatangani transaksi)
     - 3` untuk menampilkan **kode QR** (untuk dipindai dengan aplikasi seluler seperti BlueWallet atau Nunchuck)
     - 4` untuk mengirimnya dengan **NFC**



💡 Pada titik ini, Anda memiliki frasa seed yang independen, dapat digunakan dalam Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Menggunakan seed sekunder



Anda sekarang dapat menggunakan turunan seed ini untuk membuat portofolio baru dalam format :




- aplikasi seluler
- gW-68 lainnya
- portofolio Multisig



### 4.3 Memulihkan frasa sekunder seed yang hilang



Untuk mengambil seed sekunder kapan saja, ulangi prosesnya:


1. Mulai ulang ColdCard Anda


2. Masukkan PIN Anda


3. Masukkan passphrase Anda, jika sudah ditentukan


4. Pergi ke `Advanced > Derive seed B85`


5. Pilih format (12/18/24 kata)


6. Masukkan indeks yang sama (misalnya `1`)


7. Anda akan mendapatkan seed sekunder yang sama persis




## 5. Batasan, risiko, dan praktik terbaik



### 5.1 Ketergantungan pada kalimat utama seed + passphrase



Penggunaan BIP85 sepenuhnya bergantung pada kalimat utama seed 24 kata, serta passphrase jika Anda telah menerapkannya.




- Dari kedua Elements ini, semua frasa sekunder seed dapat dibuat ulang.
- Tanpa salah satu dari 2 Elements ini, Anda akan kehilangan akses ke semua portofolio derivatif.



### 5.2 Risiko dalam konfigurasi multi-tanda tangan



Kami sangat menyarankan untuk tidak menggunakan frasa seed sekunder yang dihasilkan dari frasa seed primer yang sama dalam konfigurasi multi-sig: jika perangkat atau frasa seed primer disusupi, semua kunci multi-sig dapat dibuat ulang oleh penyerang.



### 5.3 Kompatibilitas perangkat lunak



Tidak semua aplikasi secara langsung mendukung derivasi BIP85. Namun, seed yang dihasilkan melalui BIP85 adalah seed BIP39 standar (12, 18 atau 24 kata), dan oleh karena itu dapat digunakan dalam portofolio yang kompatibel dengan BIP39.



### 5.4 Daftar akun BIP85



Dianjurkan untuk menyimpan daftar pribadi frasa sekunder seed yang selalu diperbarui.




- Hal ini memungkinkan Anda untuk mengetahui dengan cepat indeks BIP85 mana yang sesuai dengan portofolio yang mana, tanpa harus menyimpan frasa sekunder seed.
- Register ini harus tetap minimalis, tanpa menyebutkan Bitcoin secara eksplisit, dan harus disimpan secara terpisah dari seed utama. Ingatlah untuk menyebutkannya dalam rencana warisan Anda.



Register dapat berisi :




- indeks bIP85 yang digunakan (angka dari 0 hingga 9999)
- nama penggunaan atau referensi (mis. Hot Wallet, tabungan pribadi, Wallet dari Ibu)
- jika perlu, sidik jari Wallet untuk verifikasi di ColdCard



### 5.5 Pencadangan



Cadangan harus menyertakan file :




- gW-91 utama
- gW-76 (jika digunakan)



Jangan pernah menyimpan bersama:




- gW-93 dan passphrase utama
- gW-94 utama dan daftar akun BIP85



Lebih banyak sumber daya di Lampiran.




## LAMPIRAN



## A.1 Daftar Istilah





- [BUNYI] (https://planb.network/resources/glossary/bip)
- [BIP-32] (https://planb.network/resources/glossary/bip0032)
- [BIP-39] (https://planb.network/resources/glossary/bip0039)
- [BIP-85] (https://planb.network/resources/glossary/bip0085)
- [Frasa seed] (https://planb.network/resources/glossary/recovery-phrase)
- [passphrase] (https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig] (https://planb.network/resources/glossary/multisig)




### A.2 Simpan frasa pemulihan Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Memahami passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Cara kerja portofolio Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f