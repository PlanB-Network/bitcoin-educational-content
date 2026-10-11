---
name: Proton Wallet
description: Menginstal dan menggunakan dompet Bitcoin Proton
---
![cover](assets/cover.webp)

Proton adalah perusahaan Swiss yang fokus pada privasi digital, didirikan pada tahun 2014 oleh para ilmuwan CERN. Dikenal dengan solusi open-source-nya, Proton menawarkan berbagai layanan termasuk Proton Mail, Proton VPN, dan Proton Drive.

Baru-baru ini, Proton memperkenalkan Proton Wallet, sebuah dompet Bitcoin open-source dan self-custody yang tersedia sebagai aplikasi seluler atau klien web, yang terhubung ke akun Proton kamu. Fungsi dompet ini relatif klasik untuk saat ini, dengan alat penting yang biasanya ada di dompet Bitcoin yang baik, seperti RBF (*Replace-By-Fee*), penandaan, atau kemampuan untuk menambahkan seedphrase BIP39.

Fitur khusus dari dompet ini adalah kemampuan untuk mengirim bitcoin menggunakan alamat email penerima, di mana Proton secara otomatis membuat alamat Bitcoin kosong yang terhubung ke dompet pengguna. Proton berencana menambahkan fitur-fitur baru di masa depan, termasuk Lightning dan coinjoin (mungkin menggunakan Whirlpool, berdasarkan aktivitas di repositori GitHub mereka).

## Buat akun Proton

Untuk menggunakan Proton Wallet, kamu memerlukan akun Proton. Kamu bisa membuatnya secara gratis dengan mengikuti langkah pertama tutorial ini yang khusus membahas pembuatan kotak surat Proton (hanya bagian "*Membuat akun Proton*"). Setelah akun dibuat, kamu bisa melanjutkan ke bagian selanjutnya dari tutorial ini.

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Hubungkan ke Dompet Proton

Kunjungi [situs web Proton Wallet](https://proton.me/wallet) dan klik tombol "*Dapatkan Proton Wallet*".

![Image](assets/fr/01.webp)

Pilih opsi berlangganan "*Gratis*", lalu klik "*Masuk*".

![Image](assets/fr/02.webp)

Masukkan email dan kata sandi yang terkait dengan akun Proton kamu untuk masuk.

![Image](assets/fr/03.webp)

Akun kamu sekarang akan ditampilkan. Klik "*Mulai menggunakan Proton Wallet sekarang*".

![Image](assets/fr/04.webp)

## Membuat dompet Bitcoin

Pilih mata uang fiat default untuk akun kamu, lalu klik "*Buat dompet baru*".

![Image](assets/fr/05.webp)

Dompet Bitcoin kamu sekarang telah dibuat. Secara teori, kamu bisa langsung menggunakannya, tetapi sangat penting untuk menyimpan mnemonic Anda terlebih dahulu. Untuk melakukannya, klik "*Secure your wallet*" di sudut kanan atas antarmuka.

![Image](assets/fr/06.webp)

Jika Anda belum melakukannya di Proton, Anda akan diminta untuk membuat cadangan untuk akun kamu dan mengamankannya menggunakan metode 2FA. Langkah-langkah keamanan ini, meskipun berlaku untuk seluruh akun Proton kamu, akan lebih relevan ketika dompet Bitcoin Anda terintegrasi ke dalamnya. Aku sangat menyarankan untuk menerapkannya.

![Image](assets/fr/07.webp)

Untuk menyimpan frasa mnemonik kamu, klik "*Cadangkan frasa unggulan dompet ini*".

![Image](assets/fr/08.webp)

Masukkan kata sandi Proton kamu.

![Image](assets/fr/09.webp)

Kemudian klik "*Lihat frasa seed wallet*" untuk menampilkan frasa mnemonik wallet kamu.

![Image](assets/fr/10.webp)

Dompet Proton menampilkan frasa mnemonik 12 kata kamu. **Mnemonik ini memberi kamu akses penuh dan tidak terbatas ke semua bitcoin kamu**. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa akses ke akun Proton kamu. Frasa 12 kata ini bisa digunakan untuk memulihkan akses ke bitcoin kamu jika kamu kehilangan akses ke akun kamu. Karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang aman.

Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan tambahan, aku sarankan mengukirnya di baja tahan karat agar terlindung dari kebakaran, banjir, atau keruntuhan.

![Image](assets/fr/11.webp)

Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola frasa mnemonik kamu, aku sangat merekomendasikan mengikuti tutorial lainnya, terutama jika kamu seorang pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Tentu saja, kamu tidak boleh memotret kata-kata ini, tidak seperti yang aku lakukan dalam tutorial ini.**_

Klik tombol "*Selesai*" setelah kamu menyimpan phrase milikmu.

![Image](assets/fr/12.webp)

## Temukan antarmuka

Antarmuka Proton Wallet sangat intuitif. Di sebelah kiri, kamu akan menemukan berbagai dompet dan akun terkait. Akun "*Primary*" adalah akun utama kamu. Untuk alasan privasi, bitcoin yang diterima melalui alamat email Proton ditempatkan di akun terpisah, bernama "*Bitcoin via Email*".

![Image](assets/fr/13.webp)

Untuk menambahkan akun baru, klik "*Tambah akun*".

![Image](assets/fr/14.webp)

Untuk membuat portofolio baru, klik simbol "*+*" di sebelah "*Dompet*".

![Image](assets/fr/15.webp)

Di sinilah kamu dapat menambahkan kata sandi BIP39 ke dompet baru.

![Image](assets/fr/16.webp)

Untuk memperdalam pengetahuan kamu mengenai frasa sandi, aku merekomendasikan tutorial ini:

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Menerima bitcoin

Untuk menerima bitcoin di dompet kamu, pilih akun yang diinginkan di sebelah kiri antarmuka, lalu klik tombol "*Terima*".

![Image](assets/fr/17.webp)

Proton Wallet kemudian secara otomatis menghasilkan alamat baru yang kosong.

![Image](assets/fr/18.webp)

Setelah transaksi selesai, kamu akan menemukannya di bagian "*Transaksi*". Klik "*+Tambah*" untuk memberikan label pada transaksi.

![Image](assets/fr/19.webp)

## Kirim bitcoin

Setelah Anda memiliki bitcoin di dalam dompet, kamu bisa mengirimkannya. Pilih akun pilihan kamu di sisi kiri antarmuka, lalu klik "*Kirim*".

![Image](assets/fr/20.webp)

Masukkan alamat Bitcoin penerima. Kamu bisa memindai kode QR dengan mengeklik logo kecil. Untuk mengirim ke alamat email, masukkan langsung di kolom ini. Setelah memasukkan alamat Bitcoin, klik tanda panah kecil lalu klik "*Konfirmasi*".

![Image](assets/fr/21.webp)

Masukkan jumlah yang akan dikirim, baik dalam mata uang fiat atau bitcoin, lalu klik "*Tinjau*".

![Image](assets/fr/22.webp)

Pilih biaya transaksi berdasarkan situasi pasar saat ini.

![Image](assets/fr/23.webp)

Tambahkan label pada transaksi kamu, lalu periksa kembali semua detailnya. Jika semuanya sudah benar, klik "*Konfirmasi dan kirim*" untuk menandatangani dan mengirim transaksi.

![Image](assets/fr/24.webp)

Transaksi kamu sekarang akan muncul menunggu konfirmasi di bagian "*Transaksi*" di akun kamu.

![Image](assets/fr/25.webp)

## Masuk ke aplikasi

Selain klien web, Proton Wallet juga bisa diakses melalui aplikasi seluler. Dengan menautkan dompet ke akun Proton kamu, kamu bisa menyinkronkan dompet antara klien web dan aplikasi seluler.

Unduh Proton Wallet dari toko aplikasi Anda:


- [Di App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [Di Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Setelah instalasi, klik "*Log in*" dan masukkan alamat email dan kata sandi Proton kamu.

![Image](assets/fr/27.webp)

Kemudian kamu akan memiliki akses ke dompet Bitcoin kamu, dengan fitur yang sama seperti di klien web.

![Image](assets/fr/28.webp)

Selamat, kamu sekarang tahu cara mengatur dan menggunakan Proton Wallet. Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih sudah berbagi!

Untuk melangkah lebih jauh, aku merekomendasikan tutorial tentang Jade Plus, dompet perangkat keras terbaru dari Blockstream:

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
