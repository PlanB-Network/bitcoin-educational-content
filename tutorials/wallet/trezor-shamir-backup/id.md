---
name: Cadangan Trezor Shamir
description: Frasa Mnemonic satu-bagi dan multi-bagi di Trezor
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*



## Opsi pencadangan baru di Trezor



Sejak tahun 2023, Trezor telah menawarkan format pencadangan baru yang disebut ***Cadangan Saham Tunggal***, secara bertahap menggantikan pendekatan klasik berbasis BIP39 yang ditemukan pada sebagian besar portofolio. Tidak seperti frasa Mnemonic 12 atau 24 kata tradisional, format baru ini didasarkan pada frasa 20 kata tunggal yang berasal dari standar yang dikembangkan oleh SatoshiLabs: **SLIP39**. Tujuannya adalah untuk meningkatkan ketahanan dan keterbacaan cadangan, sekaligus memungkinkan migrasi yang lancar ke model cadangan terdistribusi.



Model terdistribusi ini disebut ***Cadangan Multi-Bagi***. Model ini didasarkan pada prinsip yang sama, tetapi alih-alih menghasilkan satu frasa Mnemonic, model ini membaginya menjadi beberapa fragmen yang disebut ***share***, yang masing-masing merupakan frasa Mnemonic dengan sendirinya. Untuk memulihkan portofolio, sejumlah *saham* ini (ditentukan oleh *ambang batas*) harus disatukan kembali. Misalnya, dalam skema 3 dari 5, 3 *saham* dari 5 *saham* akan memulihkan portofolio. Harap diperhatikan bahwa sistem cadangan terdistribusi Trezor berbeda dengan dompet Multisig. Untuk membelanjakan bitcoin Anda, hanya Hardware Wallet Trezor Anda yang diperlukan. Hanya satu tanda tangan yang diperlukan. Distribusi hanya berlaku pada tingkat frasa Mnemonic, yaitu cadangan.



![Image](assets/fr/01.webp)



Sistem ini memecahkan masalah satu titik kegagalan frasa Mnemonic tanpa kerugian yang terkait dengan pengelolaan Multisig atau passphrase BIP39. Proses pemulihan tidak lagi didasarkan pada satu informasi, tetapi pada beberapa informasi, dengan manfaat tambahan berupa toleransi kerugian berkat ambang batas.



Pengguna yang telah membuat portofolio dengan *Cadangan Single-share* dapat beralih ke *Cadangan Multi-share* kapan saja tanpa harus memindahkan portofolio mereka. Alamat dan akun penerima akan tetap sama. Sistem *Multi-share* hanya memengaruhi cadangan, sementara portofolio lainnya tetap tidak berubah.



Multi-share Backup* tersedia pada Trezor Model T, Safe 3 dan Safe 5. Fitur ini tidak didukung oleh Trezor Model One.



**Catatan penting:** Sistem *Multi-share* Trezor aman secara kriptografis, karena menggunakan skema *Shamir's Secret Sharing* untuk distribusi. Kami sangat menyarankan untuk tidak menerapkan sistem serupa secara manual, dengan membagi frase Mnemonic klasik secara manual. Ini adalah praktik buruk yang secara signifikan meningkatkan risiko pencurian dan kehilangan bitcoin Anda, jadi jangan lakukan itu. Frase Mnemonic klasik disimpan secara keseluruhan.



## Berbagi Rahasia Shamir di SLIP39



Mekanisme kriptografi yang mendasari cadangan *Multi-share* di Trezor adalah *Shamir's Secret Sharing Scheme* (SSSS). Prinsipnya adalah sebagai berikut: informasi rahasia (dalam hal ini, seed portofolio) diubah menjadi sebuah polinomial matematika. Beberapa titik dari polinomial ini kemudian dihitung, yang masing-masing menjadi bagian. Rahasia asli direkonstruksi dengan interpolasi polinomial, dengan mengumpulkan jumlah titik minimum (ambang batas).



Tidak ada informasi rahasia yang dapat disimpulkan dari sejumlah saham di bawah ambang batas, menjamin keamanan teoritis yang sempurna dari informasi rahasia. Dengan kata lain, bahkan penyerang dengan kekuatan komputasi yang tidak terbatas tidak dapat menebak seed jika ambang batas tidak tercapai.



SLIP39 menggunakan skema ini untuk mendistribusikan portofolio seed. Setiap bagian terdiri dari 20 kata, dibangun dari daftar 1024 kata (berbeda dari daftar BIP39).



## Menyiapkan Cadangan Multi-share pada Trezor



Ketika membuat portofolio Anda di Trezor, Anda memiliki tiga opsi berbeda:




- Gunakan frasa klasik BIP39 Mnemonic yang terdiri dari 12 atau 24 kata;
- Gunakan frasa Mnemonic satu saham (SLIP39);
- Konfigurasikan beberapa frasa Mnemonic dalam Multi-share (SLIP39).



Jika Anda memilih frasa Single-share SLIP39 Mnemonic, Anda akan dapat meningkatkan ke Multi-share di kemudian hari tanpa harus mengatur ulang portofolio. Di sisi lain, jika Anda memulai dengan portofolio BIP39 klasik (frasa 12 atau 24 kata), Anda tidak akan dapat mengonversinya secara langsung ke Multi-share. Anda harus membuat portofolio Multi-share baru dari awal dan mentransfer dana Anda dari portofolio lama ke portofolio baru melalui satu atau beberapa transaksi Bitcoin. Ini adalah operasi yang lebih kompleks dan mahal. Jika Anda ingin melakukan migrasi ini, saya sarankan Anda membeli Hardware Wallet Trezor baru untuk menghindari keharusan memasukkan seed Anda pada perangkat lunak portofolio.



Dalam tutorial ini, pertama-tama kita akan melihat cara mengatur Multi-share saat membuat portofolio, kemudian, di bagian selanjutnya, kita akan melihat cara mengonversi Single-share menjadi Multi-share pada portofolio yang sudah ada.



Jika Anda memerlukan bantuan dengan pengaturan awal perangkat Anda, kami juga memiliki tutorial terperinci untuk setiap model Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Pada portofolio baru



Anda sekarang telah menyelesaikan konfigurasi awal Trezor Anda dan siap untuk membuat portofolio. Di Trezor Suite, klik tombol "*Buat Wallet baru*".



![Image](assets/fr/02.webp)



Pilih opsi "*Cadangan Multi-Bagi*", lalu klik "*Buat Wallet*".



![Image](assets/fr/03.webp)



Terima persyaratan penggunaan di Trezor Anda dan konfirmasikan pembuatan portofolio.



![Image](assets/fr/04.webp)



Di Trezor Suite, klik "*Lanjutkan pencadangan*".



![Image](assets/fr/05.webp)



Baca instruksi dengan cermat, konfirmasikan, lalu klik "*Buat cadangan Wallet*".



![Image](assets/fr/06.webp)



Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa Mnemonic Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pada Trezor, pilih jumlah total saham yang ingin Anda konfigurasi. Konfigurasi yang paling umum adalah 2-de-3 dan 3-de-5. Untuk contoh ini, saya akan membuat 2-de-3, jadi saya akan memilih 3 bagian. Setiap bagian akan mewakili frasa Mnemonic yang terdiri dari 20 kata.



*Untuk pengguna Safe 5, meskipun layar akan mengatakan "*Ketuk untuk melanjutkan*", Anda sebenarnya harus menggeser ke atas untuk mengonfirmasi



![Image](assets/fr/07.webp)



Kemudian konfirmasikan ambang batasnya, yaitu jumlah saham yang diperlukan untuk mendapatkan kembali akses ke Wallet dan bitcoin yang ada di dalamnya.



![Image](assets/fr/08.webp)



Trezor akan membuat berbagai macam saham Anda (frasa Mnemonic) menggunakan generator angka acak. Pastikan Anda tidak diawasi selama operasi ini. Tuliskan kata-kata yang disediakan di layar pada media fisik pilihan Anda. Sangat penting untuk menjaga agar kata-kata tersebut diberi nomor dan dalam urutan yang berurutan.



Saya sarankan Anda mencatat setiap berbagi pada media yang terpisah dan mengatur penyimpanannya dengan hati-hati untuk menghindari beberapa dapat diakses di tempat yang sama. Sebagai contoh, untuk konfigurasi 2-dari-3 seperti milik saya, salah satu pilihannya adalah menyimpan satu file di rumah saya, satu lagi di rumah teman tepercaya, dan yang terakhir di brankas bank. Pilihan lokasi penyimpanan akan tergantung pada strategi keamanan pribadi Anda.



Anda dapat melihat di bagian atas layar, share mana yang sedang Anda lihat.



tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.**_



![Image](assets/fr/09.webp)



Untuk beralih ke kata berikutnya, klik di bagian bawah layar. Anda dapat mundur dengan menggeser ke bawah. Setelah Anda menuliskan semua kata, pertahankan jari Anda pada layar untuk beralih ke bagian berikutnya, dan ulangi operasi.



![Image](assets/fr/10.webp)



Di akhir setiap perekaman berbagi, Anda akan diminta untuk memilih kata-kata dalam frasa Mnemonic Anda untuk mengonfirmasi bahwa Anda telah menuliskannya dengan benar.



![Image](assets/fr/11.webp)



Dan selesai, Anda telah berhasil mencadangkan portofolio Anda menggunakan opsi Multi-share. Anda sekarang dapat melanjutkan dengan petunjuk konfigurasi lainnya.



### Pada portofolio saham tunggal yang sudah ada



Jika Anda sudah memiliki Trezor Wallet dengan cadangan satu-saham (frasa SLIP39 Mnemonic, bukan frasa BIP39 klasik), dan ingin meningkatkan ketersediaan dan keamanan cadangan Wallet Anda, Anda dapat mengatur sistem multi-saham tanpa harus mentransfer bitcoin Anda.



Untuk melakukannya, hubungkan dan buka kunci Hardware Wallet Anda. Di Trezor Suite, buka Pengaturan.



![Image](assets/fr/12.webp)



Buka tab "*Perangkat*".



![Image](assets/fr/13.webp)



Kemudian klik "*Buat Cadangan Multi-Bagi*".



![Image](assets/fr/14.webp)



Baca petunjuknya, lalu klik "*Buat Cadangan Multi-Bagi*".



![Image](assets/fr/15.webp)



Anda kemudian harus memasukkan frasa Mnemonic Anda saat ini (single-share) pada layar Trezor Anda. Pilih jumlah kata (standarnya adalah 20).



![Image](assets/fr/16.webp)



Kemudian gunakan keyboard di layar Trezor untuk memasukkan setiap kata dari frasa Mnemonic Anda saat ini.



![Image](assets/fr/17.webp)



Anda kemudian dapat memilih konfigurasi Cadangan Multi-Bagi Anda dengan mengikuti petunjuk yang disediakan di bagian sebelumnya.



![Image](assets/fr/18.webp)



Setelah Anda membuat Cadangan Multi-share, Anda harus memutuskan apa yang harus dilakukan dengan frasa Mnemonic Single-share asli Anda. Karena portofolio Bitcoin tetap sama, frasa tunggal ini akan selalu mengizinkan akses ke sana. Hal ini akan tergantung pada strategi keamanan Anda, tetapi secara umum, disarankan untuk menghancurkan frasa ini untuk menghilangkan titik kegagalan tunggal ini, yang merupakan tujuan dari Cadangan Multi-share. Jika Anda memutuskan untuk menghancurkannya, pastikan Anda melakukannya dengan aman, karena frasa ini masih memberikan akses ke bitcoin Anda.



Selamat, anda sekarang sudah memahami penggunaan Single-share dan Multi-share Backup pada dompet perangkat keras Trezor. Jika Anda ingin meningkatkan keamanan Wallet Anda selangkah lebih maju, lihat tutorial mengenai kata sandi BIP39 ini:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!



## Sumber daya tambahan





- [SLIP-0039: Pembagian Rahasia Shamir untuk Kode Mnemonic] (https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup di Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).