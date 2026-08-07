---
name: Memperbarui BTCPay Server
description: Terapkan pembaruan keamanan pada instance BTCPay Server Anda dan rotasi kredensial yang penting
---

![cover](assets/cover.webp)

Menjalankan payment processor Anda sendiri berarti Anda juga menjadi tim keamanan Anda sendiri. Ketika para maintainer BTCPay Server merilis security release, tidak ada yang akan menambal instance Anda untuk Anda: pembaruan, verifikasi, dan rotasi kredensial setelahnya adalah tanggung jawab Anda untuk dilakukan.

Tutorial ini membahas seluruh prosedurnya, apa pun cara Anda men-deploy BTCPay Server: periksa versi yang sedang berjalan, terapkan pembaruan sesuai jenis deployment Anda, verifikasi bahwa pembaruan benar-benar berhasil, dan rotasi rahasia (secret) yang mungkin telah dicuri penyerang selama instance Anda rentan.

Jika Anda belum men-deploy BTCPay Server, mulailah dengan panduan instalasi:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Kerentanan kritis Agustus 2026

⚠️ **Peringatan keamanan kritis (7 Agustus 2026):** kerentanan kritis yang memengaruhi BTCPay Server sedang secara aktif dieksploitasi dan dapat menyebabkan hilangnya dana. Perbarui instance Anda ke **versi 2.4.2** segera melalui `Admin Dashboard > Server > Maintenance > Update`, lalu periksa bahwa footer menampilkan `2.4.2`. Jika Anda tidak dapat memperbarui segera, matikan BTCPay Server Anda. Setelah diperbarui, Anda juga harus sepenuhnya menyegarkan (refresh) macaroon Anda beserta `macaroons.db`, sepenuhnya menyegarkan authentication string dari backend Lightning lainnya, dan, jika Anda membuat hot on-chain wallet di dalam BTCPay Server, pindahkan dana tersebut dan buat ulang wallet-nya. Integrator juga harus memperbarui NBXplorer ke versi 2.6.10. Sumber: [catatan rilis BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versi 2.4.2 dipublikasikan pada 7 Agustus 2026. Catatan rilisnya menyatakan bahwa versi ini memperbaiki kerentanan kritis yang sudah dieksploitasi secara aktif di dunia nyata, dilaporkan oleh `brunoerg` dan `benthecarman` melalui upaya Bitcoin Red Team. Rilis yang sama juga memperbaiki bypass otentikasi dua faktor TOTP melalui Greenfield Basic authentication, dan menonaktifkan Greenfield Basic authentication secara default lima menit setelah akun dibuat.

Dua konsekuensi muncul dari "dieksploitasi secara aktif":

- **Memperbarui bukanlah hal opsional dan bukan sesuatu yang bisa dijadwalkan untuk minggu depan.** Instance yang belum ditambal dan dapat diakses dari internet harus segera diperbarui atau dimatikan.
- **Memperbarui saja tidak cukup.** Jika instance Anda sudah disusupi sebelum Anda menambalnya, penyerang mungkin sudah memegang salinan kredensial Lightning Anda dan material kunci hot wallet apa pun yang dibuat BTCPay Server untuk Anda. Rahasia-rahasia tersebut tetap valid setelah pembaruan hingga Anda merotasinya. Bagian rotasi di bawah ini adalah bagian yang sering dilewatkan orang, dan justru bagian inilah yang benar-benar melindungi dana Anda.

## Langkah 1 — Cari tahu versi yang sedang Anda jalankan

Login ke BTCPay Server Anda dan lihat **footer di halaman mana pun**: version string ditampilkan di sana. Anda juga bisa membuka `Admin Dashboard > Server > Maintenance`, yang menampilkan versi saat ini dan kontrol pembaruan.

Jika instance Anda mengekspos Greenfield API, `GET /api/v1/server/info` juga mengembalikan versinya.

Apa pun yang di bawah `2.4.2` rentan.

## Langkah 2 — Perbarui

### Deployment Docker self-hosted (instalasi standar)

Ini mencakup deployment Docker resmi, yang Anda dapatkan dari dokumentasi BTCPay Server, dari one-click launcher LunaNode, dan dari sebagian besar instalasi VPS.

Jalur paling sederhana adalah antarmuka web:

1. Buka `Admin Dashboard > Server > Maintenance`.
2. Klik **Update**.
3. Tunggu hingga container ditarik (pulled) dan di-restart. Antarmuka akan tidak tersedia selama beberapa menit.

Jika antarmuka web tidak dapat diakses, atau Anda lebih suka melihat log, lakukan lewat SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Pada instalasi default, `$BTCPAY_BASE_DIRECTORY` adalah `/root`, sehingga direktorinya adalah `/root/btcpayserver-docker`. Script ini menarik image terbaru, membuat ulang container, dan mencetak versi hasilnya.

Deployment Docker menyertakan NBXplorer bersama BTCPay Server, sehingga pembaruan standar juga membawa NBXplorer ke versi yang direkomendasikan, `2.6.10`. Jika Anda menjalankan NBXplorer secara terpisah — umum bagi integrator dan untuk stack kustom — perbarui secara eksplisit.

### Umbrel

Buka dashboard Umbrel, masuk ke **App Store**, cari BTCPay Server dan terapkan pembaruan jika tersedia.

⚠️ **Penting:** paket app-store dikemas ulang oleh tim Umbrel dan bisa tertinggal dari upstream selama berjam-jam atau berhari-hari. Periksa versi di footer BTCPay Server setelah memperbarui. Jika masih di bawah `2.4.2`, **hentikan aplikasi** dari dashboard Umbrel dan tunggu rilis paketnya, daripada membiarkan instance yang rentan tetap berjalan.

Panduan Umbrel khusus membahas aplikasinya sendiri:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Logikanya sama: perbarui BTCPay Server dari marketplace StartOS, lalu verifikasi versinya di footer. Jika versi paketnya belum `2.4.2`, hentikan layanan tersebut sampai tersedia.

### Hosting terkelola dan pihak ketiga

Jika ada pihak lain yang mengoperasikan instance Anda (penyedia hosting, sebuah asosiasi, server milik teman), Anda tetap perlu konfirmasi. Tanyakan kepada operator version string yang ditampilkan di footer, dan tanyakan secara eksplisit apakah rotasi kredensial pasca-pembaruan yang dijelaskan di bawah ini sudah dilakukan. "Kami sudah memperbarui" bukan jawaban yang sama dengan "kami sudah merotasi macaroon Anda".

## Langkah 3 — Verifikasi bahwa pembaruan benar-benar berhasil

Muat ulang antarmuka BTCPay Server dan baca versinya di footer. Versi tersebut harus menunjukkan `2.4.2` atau lebih tinggi.

Jangan hanya mengandalkan perintah update yang keluar tanpa error: pada mesin dengan sumber daya terbatas, image pull bisa gagal secara diam-diam dan membiarkan container lama tetap berjalan. Baca versinya, setiap kali.

## Langkah 4 — Rotasi kredensial Anda

Inilah langkah yang mengubah "sudah ditambal" menjadi "aman". Karena kerentanan ini sudah dieksploitasi sebelum perbaikannya dirilis, perlakukan setiap rahasia yang dipegang instance Anda sebagai berpotensi sudah diketahui penyerang.

### Lightning: LND

Buat ulang macaroon **dan** file `macaroons.db`. Hanya menghapus file macaroon saja tidak cukup — LND menurunkan macaroon dari root key yang tersimpan di `macaroons.db`, sehingga penyerang yang memegang salinan macaroon lama tetap memiliki akses sampai database tersebut dibuat ulang.

Prosedurnya adalah: hentikan LND, hapus `macaroons.db` dan file `*.macaroon` dari direktori jaringan (untuk mainnet, `data/chain/bitcoin/mainnet/` di dalam direktori data LND), lalu restart dan unlock LND, yang akan membuat ulang file-file tersebut. Backup direktorinya terlebih dahulu, dan pasangkan ulang (re-pair) setiap aplikasi yang menggunakan macaroon lama — BTCPay Server itu sendiri, Zeus, Thunderhub, RTL, Alby, dan script apa pun yang Anda buat.

Jika Anda juga mengekspos LND ke internet, tinjau juga sertifikat TLS-nya dan kredensial `lnd.conf` apa pun pada saat yang sama.

### Lightning: backend lain

Apa pun yang mengotentikasi ke node Anda dengan sebuah string harus mendapatkan string baru:

- **Core Lightning**: buat ulang rune atau kredensial akses yang digunakan oleh koneksi tersebut.
- **Phoenixd**: rotasi password HTTP.
- **LNbits dan sejenisnya**: cabut dan terbitkan ulang admin key dan invoice key.
- **Remote node connection string** yang tersimpan di pengaturan store BTCPay Server: tulis ulang dengan rahasia yang baru.

### Hot on-chain wallet yang dibuat di dalam BTCPay Server

Jika Anda membiarkan BTCPay Server membuat on-chain wallet untuk Anda — berbeda dengan menghubungkan hardware wallet atau mengimpor xpub yang kuncinya tidak pernah menyentuh server — seed tersebut pernah berada di mesin itu.

Anggap saja sudah terbakar (burned):

1. Buat wallet baru, idealnya dengan hardware wallet agar kuncinya tidak pernah lagi berada di server.
2. Pindahkan (sweep) dana dari wallet lama ke wallet baru.
3. Ganti derivation scheme di pengaturan store dengan wallet baru.
4. Jangan pernah menggunakan kembali seed lama.

Setup watch-only (xpub atau hardware wallet) tidak memerlukan ini: private key-nya tidak pernah berada di server. Inilah tepatnya alasan panduan instalasi merekomendasikannya.

### Akun BTCPay Server dan API key

Sekalian saja:

- Ubah password setiap akun pengguna pada instance tersebut.
- Cabut dan terbitkan ulang semua **API key** Greenfield.
- Daftarkan ulang otentikasi dua faktor, mengingat 2.4.2 memperbaiki bypass 2FA.
- Buka `Admin Dashboard > Server > Users` dan periksa apakah ada akun tak terduga.
- Tinjau **payout**, **pull payment**, dan **refund** terbaru untuk entri yang tidak Anda buat.
- Tinjau webhook Anda beserta rahasianya.

## Langkah 5 — Tetap ikuti informasi untuk selanjutnya

Security release hanya membantu operator yang mendengar tentangnya:

- Pantau [rilis BTCPay Server di GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub dapat mengirimkan email kepada Anda setiap kali ada rilis baru dari sebuah repository.
- Ikuti kanal pengumuman proyek dan [blog resminya](https://blog.btcpayserver.org/).
- Jaga instance Anda tetap pada versi yang bisa Anda perbarui dengan cepat: semakin jauh Anda tertinggal, semakin menyakitkan pembaruan darurat nantinya.

Self-hosting memberi Anda kedaulatan atas pembayaran Anda. Harga dari kedaulatan itu tepatnya adalah ini: membaca catatan rilis dan menjadi orang yang menambalnya.
</content>
<parameter name="i">Write Indonesian translation