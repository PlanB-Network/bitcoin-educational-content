---
name: LNP2PBot
description: Panduan lengkap untuk LNP2PBot dan perdagangan bitcoin P2P
---
![cover](assets/cover.webp)

## Pendahuluan

Pertukaran peer-to-peer (P2P) yang bebas KYC sangat penting untuk menjaga kerahasiaan dan otonomi keuangan pengguna. Bursa ini memungkinkan transaksi langsung antar individu tanpa memerlukan verifikasi identitas, yang sangat penting bagi mereka yang menghargai privasi. Untuk pemahaman yang lebih mendalam mengenai konsep teoretis, lihatlah kursus BTC204:

https://planb.network/courses/btc204
Membeli dan menjual bitcoin secara peer-to-peer (P2P) adalah salah satu metode yang paling privat untuk memperoleh atau membuang bitcoin. LNP2PBot adalah bot Telegram sumber terbuka yang memfasilitasi pertukaran P2P di jaringan Lightning, memungkinkan transaksi yang cepat, murah, dan bebas KYC.

### Mengapa menggunakan Lnp2pbot?


- Tidak diperlukan KYC
- Transaksi cepat di Jaringan Lightning
- Biaya rendah
- Antarmuka yang sederhana melalui Telegram, aplikasi perpesanan populer yang dapat diakses dari mana saja di seluruh dunia
- Sistem reputasi yang terintegrasi
- Eskro otomatis untuk perdagangan yang aman
- Dukungan multi-mata uang
- Komunitas yang aktif dan berkembang

### Prasyarat

Untuk menggunakan Lnp2pbot, Anda memerlukan :

1. Dompet Lightning Network (direkomendasikan Breez, Phoenix atau Blixt)

2. Aplikasi Telegram terinstal (https://telegram.org/)

3. Akun Telegram dengan nama pengguna yang ditentukan

## Instalasi dan konfigurasi

### 1. Mengonfigurasi dompet Lightning Anda

Mulailah dengan memasang dompet Lightning yang kompatibel. Berikut adalah rekomendasi terperinci kami:

**Portofolio yang direkomendasikan**


- (https://breez.technology)**:
  - Sangat bagus untuk pemula
  - Antarmuka yang intuitif dan modern
  - Non-kustodian (Anda tetap memegang kendali atas dana Anda)
  - Sangat kompatibel dengan Lnp2pbot
  - Tersedia di iOS dan Android

Di bawah ini adalah tautan ke tutorial untuk dompet ini:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co)** :
  - Sederhana dan dapat diandalkan
  - Konfigurasi saluran otomatis
  - Dukungan asli untuk faktur BOLT11
  - Sangat baik untuk transaksi sehari-hari
  - Tersedia di iOS dan Android

Di bawah ini adalah tautan ke tutorial untuk dompet ini:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** :
  - Lebih teknis tetapi sangat lengkap
  - Opsi konfigurasi lanjutan
  - Sempurna untuk pengguna berpengalaman
  - Sumber terbuka
  - Tersedia di Android

Di bawah ini adalah tautan ke tutorial untuk dompet ini:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**Catatan penting tentang portofolio lainnya**

⚠️ **Penting**: Sebelum menjual satwa, pastikan portofolio Anda mendukung faktur "tahan", yang digunakan oleh bot sebagai sistem escrow.


- Dompet Satoshi**: Berfungsi dengan baik untuk menerima satoshi, tetapi dapat mengalami penundaan dalam memperbarui saldo jika penjualan dibatalkan.
- Muun**: Tidak disarankan karena pembayaran mungkin gagal karena batas biaya perutean bot (maksimum 0,2%).
- Aqua**: Berfungsi untuk menerima sat, tetapi dapat mengalami penundaan yang lama (hingga 48 jam) untuk pembaruan saldo jika terjadi pembatalan penjualan.

💡 **Tip**: Untuk pengalaman yang optimal, pilihlah portofolio yang direkomendasikan (Breez, Phoenix atau Blixt).

⚠️ **Penting**: Jangan lupa untuk menyimpan frasa pemulihan Anda di tempat yang aman.

### 2. Memulai dengan Lnp2pbot

1. Klik tautan ini untuk mengakses bot: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram akan terbuka secara otomatis

3. Klik "Start" atau kirim perintah "/start"

4. Bot akan meminta Anda untuk membuat nama pengguna jika Anda belum memilikinya

5. Bot akan memandu Anda melalui konfigurasi awal

### 3. Bergabunglah dengan komunitas


- Bergabunglah dengan saluran utama: [@p2plightning](https://t.me/p2plightning)
- Dukungan: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Membeli dan Menjual Bitcoin

Ada dua cara utama untuk menukar bitcoin di Lnp2pbot:

1. Jelajahi dan tanggapi penawaran yang ada di pasar

2. Buat penawaran Anda sendiri untuk membeli atau menjual

Dalam panduan ini, kita akan mencermati secara detail tentang cara :


- Beli bitcoin dari penawaran yang sudah ada
- Jual bitcoin dengan membuat penawaran Anda sendiri

### Cara membeli Bitcoin

**1. Temukan dan pilih penawaran**

![Sélection d'une offre de vente](assets/fr/01.webp)

Jelajahi penawaran di [@p2plightning](https://t.me/p2plightning) dan klik tombol "Beli satoshi" di bawah iklan yang Anda minati.

**2. Memvalidasi penawaran dan jumlah**

![Validation de l'offre](assets/fr/02.webp)

1. Kembali ke obrolan bot

2. Konfirmasikan pilihan penawaran Anda

3. Masukkan jumlah dalam mata uang fiat yang ingin Anda beli

4. Bot akan meminta Anda untuk memberikan faktur Lightning untuk jumlah dalam satoshi

**3. Menghubungi penjual**

![Mise en relation](assets/fr/03.webp)

Setelah faktur dikirim, bot akan menghubungkan Anda dengan penjual.

**4. Komunikasi dengan penjual**

![Chat privé](assets/fr/04.webp)

Klik nama panggilan penjual untuk membuka saluran obrolan pribadi di mana Anda bisa bertukar detail pembayaran fiat.

**5. Konfirmasi pembayaran

![Confirmation du paiement](assets/fr/05.webp)

Setelah melakukan pembayaran fiat, gunakan perintah `/fiatsent` di obrolan bot. Setelah transaksi selesai, Anda akan dapat memberi nilai pada penjual dan transaksi akan ditutup.

### Cara menjual Bitcoin

**1. Membuat penawaran penjualan**

![Création d'une offre de vente](assets/fr/06.webp)

Untuk membuat penawaran penjualan, cukup gunakan perintah :

`/sell`

Bot kemudian akan memandu Anda langkah demi langkah:

1. Pilih mata uang Anda

2. Tunjukkan jumlah satoshi yang akan dijual

3. Untuk harga, Anda memiliki dua pilihan:


   - Menetapkan harga tetap untuk jumlah satoshi
   - Gunakan harga pasar dengan opsi penerapan premi (positif atau negatif)

💡 **Tip**: Premi memungkinkan Anda untuk menyesuaikan harga Anda dengan harga pasar. Misalnya, premi -1% berarti Anda menjual dengan harga 1% lebih rendah dari harga pasar.

**2. Konfirmasi pembuatan pesanan**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Setelah pesanan dibuat, Anda akan melihat konfirmasi dengan opsi untuk membatalkan pesanan menggunakan perintah `/cancel`.

**3. Mengelola penjualan**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Ketika pembeli merespons penawaran Anda, Anda akan menerima notifikasi dengan kode QR dan faktur pembayaran.
- Periksa profil dan reputasi pembeli.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Klik nama panggilan pembeli untuk membuka saluran diskusi pribadi.
- Mengkomunikasikan detail pembayaran fiat kepada pembeli.
- Tunggu konfirmasi pembayaran fiat dari pembeli.
- Periksa apakah pembayaran telah diterima di akun Anda.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Konfirmasikan transaksi dengan `/release` dan selesaikan pesanan. Anda akan memiliki kesempatan untuk memberi peringkat pada pembeli.

## Praktik yang Baik dan Keselamatan

### Kiat keselamatan


- Mulailah dengan jumlah kecil
- Selalu periksa reputasi pengguna
- Gunakan hanya metode pembayaran yang disarankan
- Simpan semua komunikasi dalam obrolan bot
- Jangan pernah membagikan informasi sensitif

### Sistem reputasi


- Setiap pengguna memiliki skor reputasi
- Transaksi yang berhasil meningkatkan skor Anda
- Pilih pengguna dengan reputasi yang baik
- Laporkan perilaku yang mencurigakan kepada moderator

### Penyelesaian sengketa

1. Ketika masalah muncul, tetaplah tenang dan profesional

2. Gunakan perintah `/dispute` untuk membuka tiket

3. Berikan semua bukti yang diperlukan

4. Tunggu moderator

## Perbandingan dengan solusi lain

Lnp2pbot memiliki beberapa kelebihan dan kekurangan dibandingkan solusi pertukaran P2P lainnya seperti Peach, Bisq, HodlHodl, dan Robosat:

### Keuntungan dari Lnp2pbot


- Tidak diperlukan KYC**: Tidak seperti beberapa platform, Lnp2pbot tidak memerlukan verifikasi identitas, sehingga menjaga kerahasiaan pengguna.
- Transaksi cepat**: Berkat jaringan Lightning, transaksi hampir seketika.
- Biaya rendah**: Biaya transaksi lebih rendah dibandingkan dengan bursa tradisional.
- Ketersediaan untuk perangkat seluler**: LNP2PBot dapat diakses melalui Telegram, sehingga mudah digunakan pada perangkat seluler.
- Mudah digunakan** : Antarmuka Lnp2pbot yang intuitif membuatnya mudah digunakan, bahkan untuk pengguna yang kurang berpengalaman.

### Kekurangan dari Lnp2pbot


- Ketergantungan pada Telegram**: Menggunakan Lnp2pbot membutuhkan akun Telegram, yang mungkin tidak cocok untuk semua pengguna.
- Likuiditas yang lebih sedikit**: Dibandingkan dengan platform yang lebih mapan seperti Bisq, likuiditas bisa lebih terbatas.

Sebagai perbandingan, solusi seperti Bisq menawarkan likuiditas yang lebih besar dan antarmuka desktop, tetapi mungkin melibatkan biaya yang lebih tinggi dan waktu transaksi yang lebih lama. Sementara itu, HodlHodl dan Robosat, juga menawarkan perdagangan bebas KYC, tetapi dengan struktur biaya dan antarmuka yang berbeda.

## Sumber daya yang berguna


- Situs web resmi: https://lnp2pbot.com/
- Dokumentasi: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Dukungan: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)