---
name: Satodime
description: Ketahui cara menggunakan Satodime dengan aplikasi seluler
---
![cover](assets/cover.webp)



Panduan ini akan memandu Anda dalam instalasi, konfigurasi dan penggunaan aplikasi seluler Satodime. Anda akan belajar bagaimana cara mendapatkan kartu Anda, membuat brankas, menambah dana, membuka segel dan memulihkan kunci pribadi Anda. Lampiran menyediakan sumber daya, praktik terbaik, dan penjelasan teknis.



## Pendahuluan



**Satodime**, yang dikembangkan oleh **[Satochip](https://satochip.io/fr/)**, adalah sebuah kartu pembawa yang aman untuk menyimpan Bitcoin dengan cara yang sederhana dan nyata. Kartu ini bertindak sebagai perangkat keras wallet kustodian mandiri, di mana Anda memiliki kontrol penuh atas kunci pribadi Anda tanpa bergantung pada pihak ketiga. Bersifat open-source dan bersertifikasi EAL6+, kartu ini mendukung hingga tiga brankas independen.



### Latar belakang produk



Satodime, sebuah **carte au porteur, adalah milik siapa pun yang secara fisik memilikinya**, tanpa perlu registrasi atau identifikasi sebelumnya. Satodime memenuhi kebutuhan akan penyimpanan bitcoin yang aman dan portabel, yang memungkinkan siapa pun yang memegang kartu untuk menggunakannya atau mentransfer bitcoin dengan memindainya melalui aplikasi seluler untuk mengambil atau membuka segel brankas. Tidak seperti uang kertas, kartu ini menggunakan chip yang aman untuk menyegel kunci privat, yang hanya dapat dibuka setelah segelnya dibuka, membuat kartu ini mirip dengan uang tunai yang kepemilikannya ditentukan oleh kepemilikan fisik. Ideal untuk memberikan bitcoin sebagai hadiah, kartu ini memfasilitasi transfer bitcoin yang aman dari tangan ke tangan, sementara aplikasi seluler mengeksploitasi NFC untuk interaksi ponsel cerdas yang dapat diakses.





- Keamanan**: Kunci pribadi dibuat dan disimpan dalam chip anti-rusak; status yang terlihat (tersegel, tidak tersegel, kosong).
- Fitur**: Beli bitcoin secara langsung melalui aplikasi (mitra Paybis); kelola Mainnet dan Testnet.
- Sumber terbuka**: Kode di bawah lisensi AGPLv3, dapat diverifikasi di GitHub.



### Evolusi berkelanjutan



Aplikasi ini berkembang secara teratur. Periksa situs web atau toko Satochip untuk pembaruan. Misalnya, blockchain baru atau fungsi pembelian dapat ditambahkan. Periksa [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) untuk perkembangan yang sedang berlangsung.



## 1. Prasyarat



Sebelum memulai dengan **Satodime**, pastikan Anda memiliki hal-hal berikut ini:





- Ponsel cerdas yang kompatibel**: Perangkat Android atau iOS dengan NFC diaktifkan.
- Kartu Satodime**: Baru atau belum diinisialisasi.
- Koneksi internet**: Untuk mengunduh aplikasi.
- Pengetahuan dasar**: Memahami kunci privat/publik dan risiko kehilangan (tidak dapat dipulihkan).
- Media yang aman**: Tempat yang aman untuk menyimpan kunci pribadi setelah dibuka segelnya (kertas, logam; tidak pernah digital).



## 2. Instalasi





- Unduh aplikasi** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Periksa pengembang (Satochip) untuk menghindari penipuan.
 - Satodime adalah **sumber terbuka**. Kode sumber : [GitHub Satochip](https://github.com/Toporin/Satodime-Applet).





- Instal dan luncurkan aplikasi**: Aktifkan NFC pada ponsel Anda jika perlu.



![image](assets/fr/01.webp)



## 3. Konfigurasi awal



### 3.1 Luncurkan aplikasi dan pindai



Buka aplikasi dan ikuti panduannya. Letakkan kartu Satodime pada pembaca NFC ponsel Anda (biasanya di bagian belakang). Tekan terus selama pengoperasian untuk memastikan koneksi yang stabil.





- Jika NFC tidak berfungsi, periksa pengaturan ponsel Anda.
- Bersulang untuk menegaskan keberhasilan: "Pembacaan yang sukses".



![image](assets/fr/02.webp)



Sebagai aturan umum, **semua operasi berikut ini akan memerlukan konfirmasi dengan memindai kartu Satodime**



### 3.2 Mengambil kartu (*Ownership*)



Untuk penggunaan pertama, jadilah pemilik kartu untuk mengamankannya:





- Klik "*Take Ownership*" di aplikasi.
- Konfirmasikan operasi: ini akan menghasilkan kunci pemilik yang unik.
- Pindai peta sekali lagi untuk menerapkan perubahan.
- Peringatan**: Langkah ini tidak dapat diubah. Silakan merujuk ke [artikel tentang *kepemilikan*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Membuat brankas



Satodime mendukung hingga 3 brankas. Buat satu untuk menyimpan bitcoin:





- Pilih brankas kosong (mis. Brankas 01).
- Pilih blockchain (Bitcoin).
- Klik "*Buat & Seal*".
- Pindai kartu ke generate dan segel kunci privat (tidak akan diketahui sampai segel dibuka).
- Selamat**: Brankas Anda sekarang tersegel dan siap menerima dana.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Menambah dana



Setelah disegel, isi brankas dengan bitcoin:





- Pilih brankas.
- Klik "*Tambah dana*".
- Salin alamat publik atau pindai kode QR.
- Kirim dana dari wallet lain.
- Periksa saldo setelah konfirmasi di blockchain.
- Opsi pembelian: Klik "*Pembelian*" untuk membeli secara langsung melalui Paybis (Visa, Mastercard, dll.). Biaya yang berlaku.



![image](assets/fr/06.webp)



## 6. Membuka segel brankas



Untuk mengakses kunci privat dan mentransfer dana ke tempat lain, buka segel brankas:





- Pilih brankas yang tersegel.
- Klik "Buka segel".
- Konfirmasikan peringatan: operasi ini tidak dapat diubah.
- Pindai kartu untuk membuka segel.
- Brankas diatur ke "*Unsealed*"; kunci privat sekarang dapat dilihat/diekspor.
- Peringatan**: Setelah dibuka, kunci pribadi dapat diakses. Jika seseorang mengambil ponsel pintar Anda, mereka dapat mengakses kunci ini, dan dengan demikian memulihkan dana di brankas Anda (tidak dapat dipulihkan).



![image](assets/fr/07.webp)



## 7. Memulihkan kunci pribadi



Setelah membuka segel, ekspor kunci untuk digunakan di wallet lain:





- Pastikan Anda berada di lingkungan yang aman.
- Klik "*Tampilkan kunci pribadi*".
- Pilih format: Legacy, SegWit, WIF, dll.
- Salin kunci atau pindai kode QR.
- Keamanan**: Jangan pernah membagikan kunci pribadi Anda. Simpan secara offline.
- Impor ke dalam program perangkat lunak wallet yang kompatibel dengan pengelolaan dana (Sparrow Wallet atau Electrum, misalnya).



![image](assets/fr/08.webp)





## 8. Setel ulang bagasi



Mengatur ulang brankas akan menghapus kunci pribadi yang terkait secara permanen. Dengan kata lain, jika Anda belum mengamankan salinan kunci pribadi Anda, atau mengimpornya ke wallet lain, mengatur ulang brankas akan menyebabkan hilangnya dana yang ada di dalamnya secara permanen.



![image](assets/fr/09.webp)



Mengatur ulang bagasi akan membuat slot kosong dan siap untuk bagasi baru.



## 9. Mengalihkan kepemilikan



Untuk - misalnya - menawarkan bitcoin melalui Satodime, Anda harus :




- Mengambil alih kepemilikan kartu,
- Buat brankas Bitcoin,
- Pindahkan satss ke sana,
- Transfer kepemilikan kartu: orang berikutnya yang memindai kartu akan menjadi pemiliknya,
- Berikan kartu Satodime kepada orang yang Anda pilih, dan undang mereka untuk mengunduh aplikasi dan kemudian memindai kartu tersebut untuk mengambil alih kepemilikan - dan dengan demikian mengakses bitcoin yang 'tersimpan' di dalamnya.



![image](assets/fr/10.webp)




## LAMPIRAN



### A1. Praktik terbaik



Untuk menggunakan **Satodime** dengan aman:





- Amankan kartu**: Perlakukan seperti uang tunai; kehilangan = dana hilang jika bukan pemiliknya.
- Cadangan kunci**: Setelah membuka segel, catat kunci pribadi pada media fisik yang aman. Jangan pernah dalam bentuk digital.
- Periksa status**: Selalu pindai untuk mengonfirmasi kepemilikan kartu dan status brankas yang tersegel/tidak tersegel.
- Kerahasiaan**: Gunakan alamat baru; hindari pertukaran terpusat untuk transfer.
- Pembaruan**: Selalu perbarui aplikasi melalui toko.
- Pemulihan**: Jika kartu hilang tetapi dimiliki, dana ada di blockchain; gunakan kunci pribadi jika tidak tersegel.



### A2. Sumber daya tambahan



Khusus untuk Satodime:




- [Produk Satodime](https://satochip.io/fr/product/satodime/)
- [Panduan Seluler](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) untuk tutorial tentang penyimpanan mandiri, kunci pribadi, dll.



**Simpan frasa pemulihan Anda** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial mengenai Satochip (produk pertama merek ini) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tutorial pemelihara benih:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Tentang Satochip



**Tautan resmi** :




- [Situs Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Dukungan: info@satochip.io



**Satochip** adalah perusahaan Belgia yang mengembangkan solusi perangkat keras dan perangkat lunak untuk mengelola dan menyimpan bitcoin dan mata uang kripto lainnya. Produk andalannya, perangkat keras Satochip wallet, adalah kartu NFC yang dilengkapi dengan secure element bersertifikat EAL6+. Dilengkapi dengan Seedkeeper, sebuah frasa mnemonik dan pengelola rahasia, dan Satodime, sebuah kartu pembawa, Satochip menawarkan rangkaian lengkap yang disesuaikan dengan kebutuhan pengguna. Perangkatnya, yang didukung oleh perangkat lunak sumber terbuka, bertujuan untuk mendemokratisasi keamanan pada Bitcoin.