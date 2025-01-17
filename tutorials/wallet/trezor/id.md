---
name: Trezor model One
description: Pengaturan dan penggunaan Trezor model One
---

![cover](assets/cover.webp)

Portfolio perangkat keras dingin – 60€ – Pemula – Aman antara 2.000€ dan 50.000€.

Sebagai dompet fisik dingin, Trezor sangat ideal untuk memulai dengan Bitcoin. Mudah digunakan, tidak terlalu mahal, dan fungsional.

Kami telah membuat tutorial tentang cara menggunakannya:

1. Pengaturannya
2. Memulihkan bitcoin
3. Menggunakan, mengirim, dan menerima bitcoin

Apakah Anda ingin memiliki Trezor Anda sendiri juga?
Anda dapat berkontribusi pada proyek dengan mengklik di bawah ini!

pengaturan -https://www.youtube.com/watch?v=q-BlT6R4_bE

pemulihan: https://www.youtube.com/watch?v=3n4d4egjiFM

penggunaan: https://www.youtube.com/watch?v=syouZjLC1zY

## panduan penulisan

panduan yang diusulkan oleh https://armantheparman.com/trezor/

## Mengatur Trezor

Trezor dilengkapi dengan kabel mikro USB miliknya sendiri. Pastikan Anda menggunakan itu dan bukan sembarang kabel lama yang tergeletak di sekitar. Beberapa kabel USB hanya untuk daya. Yang ini mentransmisikan data DAN daya. Jika Anda menggunakan perangkat dengan kabel USB pengisian ponsel, perangkat mungkin gagal terhubung.

Hubungkan ke komputer Anda dan perangkat akan menyala. Anda akan mendapatkan pesan yang mengatakan "Pergi ke Trezor.io/start". Lakukan itu, dan unduh Trezor Suite ke komputer Anda.

![image](assets/0.webp)

Klik tombol unduh ("Dapatkan Aplikasi Desktop")

![image](assets/1.webp)

Perhatikan tautan Signature dan Signing key. Untuk memverifikasi unduhan (periksa bahwa unduhan Anda tidak telah diubah), ada langkah tambahan yang opsional jika Anda baru memulai, tetapi WAJIB jika Anda memiliki kekayaan signifikan untuk diamankan. Instruksi untuk itu ada di Lampiran A (akhir panduan)

Hubungkan Trezor ke komputer dengan kabel mikro USB, dan instal serta jalankan programnya. Begini tampilannya di Mac:

![image](assets/2.webp)

Anda akan mendapatkan peringatan konyol setelah menjalankan program, lanjutkan saja:

![image](assets/3.webp)

Klik pada Pengaturan Trezor

![image](assets/4.webp)

Jika firmware sudah usang, izinkan Trezor untuk memperbarui firmware.

Selanjutnya, Anda dapat membuat seed baru, atau memulihkan dompet dari perangkat lain dengan seed yang sudah Anda miliki. Saya akan melalui membuat seed baru.

![image](assets/5.webp)

Klik "Buat dompet baru" – dan konfirmasi Anda ingin melakukan ini di perangkat itu sendiri dengan mengklik tombol konfirmasi.

Kemudian klik satu-satunya opsi "Cadangan seed standar"

![image](assets/6.webp)

Kemudian klik "buat cadangan"

![image](assets/7.webp)

Klik pada tiga tanda centang untuk mengubahnya menjadi hijau (tentu saja baca setiap pesan), dan kemudian klik "mulai cadangan".

![image](assets/8.webp)

Selanjutnya, Anda akan melihat ini:

![image](assets/9.webp)

Di perangkat, lihat kata-kata yang disajikan kepada Anda satu per satu dan tulislah dengan RAPI dan BERURUTAN.

![image](assets/10.webp)

Atur PIN untuk mengunci perangkat (ini bukan bagian dari seed Anda, ini hanya untuk mengunci perangkat sehingga tidak ada yang dapat mengakses seed yang terkandung di dalamnya).

![image](assets/11.webp)
Anda memiliki opsi untuk menambahkan shitcoins ke dompet Anda - Saya menyarankan Anda untuk tidak melakukannya, dan hanya menyimpan dalam Bitcoin, seperti yang saya jelaskan di sini (mengapa bitcoin) dan di sini (mengapa hanya bitcoin).
![image](assets/12.webp)

Namai dompet Anda, dan klik "Access Suite":

![image](assets/13.webp)

Cara termudah adalah membuat dompet tanpa passphrase, tetapi lebih baik membuat satu dengan passphrase (dompet asli Anda) DAN satu tanpa passphrase (dompet pengalihan Anda). Setiap kali Anda mengakses perangkat melalui Trezor Suite, Anda akan ditanya apakah Anda ingin "menerapkan" passphrase atau tidak.

![image](assets/14.webp)

Saya memilih "Hidden Wallet" dan mengetik passphrase yang saya buat "craigwrightisaliarandafraud"

![image](assets/15.webp)

Saya suka bagaimana itu disebut "hidden" wallet, karena ini sebagian menjelaskan bagaimana fungsi passphrase.

Konfirmasi passphrase di perangkat.

Karena dompet ini kosong, saya diminta untuk mengonfirmasi bahwa passphrase tersebut benar:

![image](assets/16.webp)

Anda kemudian akan ditanya apakah Anda ingin mengaktifkan pelabelan. Bukan sesuatu yang telah saya jelajahi, tetapi terdengar seperti cara Anda dapat memberi label pada transaksi Anda dan menyimpan data ke komputer atau cloud Anda.

![image](assets/17.webp)

Akhirnya, dompet Anda akan tersedia:

![image](assets/18.webp)

Apa yang Anda miliki di komputer Anda disebut "watching wallet", karena memiliki kunci publik (dan alamat) Anda, tetapi tidak kunci pribadi Anda. Anda memerlukan kunci pribadi untuk menghabiskan (dengan menandatangani transaksi dengan kunci pribadi). Cara melakukannya adalah dengan menghubungkan dompet perangkat keras. Tujuan dari dompet perangkat keras adalah bahwa transaksi dapat dikirim bolak-balik antara komputer dan Trezor, tanda tangan dapat diterapkan di dalam Trezor, dan kunci pribadi selalu tetap berada di dalam perangkat (untuk keamanan terhadap malware komputer).

Trezor Suite adalah watching-wallet yang kurang baik untuk berbagai alasan. Ini OK untuk minimum, tetapi jika Anda ingin maju, baca terus dan pelajari cara menghubungkan perangkat ke Sparrow Bitcoin Wallet.

## Watching Wallet

Dalam artikel sebelumnya, saya menjelaskan cara mengunduh dan memverifikasi Sparrow Bitcoin Wallet, dan cara menghubungkannya ke node Anda sendiri, atau node publik. Anda dapat mengikuti panduan ini:

- Pasang Bitcoin Core
- Pasang Sparrow Bitcoin Wallet
- Hubungkan Sparrow Bitcoin Wallet ke Bitcoin Core

Alternatif untuk menggunakan Sparrow Bitcoin Wallet adalah Electrum Desktop Wallet, tetapi saya akan melanjutkan untuk menjelaskan Sparrow Bitcoin Wallet karena saya menilainya sebagai yang terbaik untuk kebanyakan orang. Pengguna lanjutan mungkin suka menggunakan Electrum sebagai alternatif (lihat panduan saya).

Sekarang kita akan memuat Sparrow dan menghubungkan Trezor (dengan frasa benih tetapi sekarang dengan passphrase). Dompet ini belum pernah terpapar ke Trezor Suite karena akan dibuat SETELAH kita menghubungkan perangkat ke Trezor Suite. Pastikan Anda tidak pernah menghubungkannya ke Trezor Suite lagi untuk tidak memaparkan dompet baru Anda. (Anda dapat menghubungkannya tanpa passphrase karena itu bisa menjadi dompet pengalihan Anda).

Buat Dompet Baru:

![image](assets/19.webp)

Namai dengan sesuatu yang cantik

![image](assets/20.webp)

Klik pada "Connected Hardware Wallet".

![image](assets/21.webp)

![image](assets/22.webp)
Klik "Scan" lalu "set passphrase" pada layar berikutnya untuk membuat dompet baru (gunakan passphrase yang benar-benar baru, misalnya passphrase lama dengan angka di belakangnya akan berfungsi). Kemudian "kirim passphrase", lalu konfirmasi di perangkat.
![image](assets/23.webp)

Kemudian klik "import keystore".

Tidak ada yang perlu diubah pada layar berikutnya, Trezor telah mengisinya untuk Anda. Klik "Apply"

![image](assets/24.webp)

Layar berikutnya memungkinkan Anda untuk menambahkan kata sandi. Jangan bingung ini dengan "passphrase"; banyak orang akan melakukannya. Penamaannya memang tidak beruntung. Kata sandi memungkinkan Anda untuk mengunci dompet ini di komputer Anda. Ini spesifik untuk perangkat lunak ini di komputer ini. Ini bukan bagian dari kunci privat Bitcoin Anda.

Klik "Apply"

![image](assets/25.webp)

Setelah jeda, saat komputer berpikir, Anda akan melihat tombol di sebelah kiri berubah dari abu-abu menjadi biru. Selamat, dompet Anda sekarang siap digunakan. Buat dan kirim transaksi sesuka hati Anda.

![image](assets/26.webp)

Menerima

Untuk menerima bitcoin, pergi ke tab Addresses di sebelah kiri dan pilih salah satu alamat untuk menerima. Cukup klik kanan alamat yang Anda inginkan, dan pilih "copy address". Kemudian pergi ke bursa tempat uang dikirim dari dan tempelkan di sana. Atau Anda dapat memberikan alamat kepada pelanggan yang dapat menggunakannya untuk membayar Anda.

Ketika Anda menggunakan dompet untuk pertama kalinya, Anda harus menerima jumlah yang sangat kecil, berlatih mengirimkannya ke alamat lain, baik di dalam dompet atau kembali ke bursa, untuk membuktikan bahwa dompet berfungsi seperti yang diharapkan.

Setelah Anda melakukan itu, Anda harus mencadangkan kata-kata yang Anda tulis. Satu salinan saja tidak cukup. Miliki setidaknya dua salinan kertas (logam lebih baik), dan simpan di dua lokasi yang berbeda dan aman. Ini mengurangi risiko bencana alam menghancurkan HWW dan cadangan kertas Anda dalam satu insiden. Lihat "Menggunakan Bitcoin Hardware Wallets" untuk diskusi lengkap tentang ini.

## Mengirim

![image](assets/27.webp)

Saat melakukan pembayaran, Anda perlu menempelkan alamat yang Anda bayar di bidang "Pay to". Anda sebenarnya tidak bisa meninggalkan Label kosong, itu hanya untuk catatan dompet Anda sendiri, tetapi Sparrow tidak mengizinkannya - cukup masukkan sesuatu (hanya Anda yang akan melihatnya). Masukkan jumlah dan Anda juga dapat secara manual menyesuaikan biaya yang Anda inginkan.

Dompet tidak dapat menandatangani transaksi kecuali HWW terhubung. Itulah tugas HWW - untuk menerima transaksi, menandatanganinya, dan mengembalikannya, sudah ditandatangani. Pastikan saat Anda menandatangani di perangkat, Anda secara visual memeriksa alamat yang Anda bayar sama di perangkat dan di layar komputer, dan faktur yang Anda terima (misalnya Anda mungkin telah menerima email untuk membayar alamat tertentu).

Perhatikan juga jika Anda memilih untuk menggunakan koin yang lebih besar dari jumlah pembayaran, maka sisanya akan dikirim kembali ke salah satu alamat perubahan dompet Anda. Beberapa orang tidak mengetahui ini, dan melihat transaksi mereka di blockchain publik, dan berpikir bahwa beberapa bitcoin dikirim ke alamat penyerang, tetapi sebenarnya, itu adalah alamat perubahan mereka sendiri.
Firmware

Untuk memperbarui firmware, Anda perlu terhubung ke Trezor Suite. Jika Anda ingin melakukan ini, pastikan Anda memiliki kata-kata cadangan dan passphrase Anda tersedia untuk mengembalikan perangkat, hanya untuk berjaga-jaga jika perangkat tersebut direset.
Kesimpulan
Artikel ini menunjukkan cara menggunakan Trezor HWW dengan cara yang lebih aman dan lebih privat daripada yang diiklankan – namun, artikel ini saja tidak cukup. Seperti yang saya katakan di awal, Anda harus menggabungkannya dengan informasi yang disediakan dalam "Menggunakan Dompet Hardware Bitcoin".

## Lampiran A - Verifikasi Unduhan Perangkat Lunak

![image](assets/28 .webp)

Unduh Tanda Tangan (file teks) dan Kunci Tanda Tangan (file teks) serta catat nama file dan lokasi Anda mengunduh file tersebut.

Selanjutnya, untuk Mac, Anda perlu mengunduh GPG Suite (Lihat instruksi di sini).

Untuk Windows, Anda perlu GPG4win (Lihat instruksi di sini).

Untuk Linux, GPG sudah menjadi bagian dari setiap paket. Jika Anda tidak memilikinya, dapatkan dengan perintah: sudo apt-get install gpg

Selanjutnya, untuk Mac/Windows atau Linux, buka terminal, dan masukkan perintah:

```bash
gpg –import XXXXXXXXXX
```

di mana XXXXXXXXXX adalah jalur lengkap ke file kunci tanda tangan (jalur lengkap berarti direktori dan nama file tempat file tersebut berada). Anda seharusnya melihat konfirmasi dari impor kunci yang berhasil.

Kemudian

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

di mana ZZZZZZZZZZ adalah jalur lengkap ke file tanda tangan dan WWWWWWWWWW adalah jalur lengkap ke program Trezor Suite yang Anda unduh.

Anda seharusnya melihat pesan “Good signature from SatoshiLabs” di suatu tempat dalam output. Ada peringatan di bagian bawah yang aman untuk diabaikan.