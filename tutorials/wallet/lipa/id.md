---
name: Lipa
description: Menyiapkan dan Menggunakan Dompet Seluler Lipa Lightning
---
![cover](assets/cover.webp)

Dompet Bitcoin Lightning adalah aplikasi mobile yang bikin kamu bisa transaksi instan dengan biaya super rendah lewat jaringan Lightning Bitcoin. Berbeda dengan transaksi di blockchain utama (on-chain), pembayaran Lightning berlangsung hampir seketika dan butuh biaya minimal, jadi pas banget dipakai buat pembayaran kecil sehari-hari.

Dompet Lightning, sama kayak dompet ponsel lainnya, termasuk kategori dompet "panas" karena selalu terhubung ke Internet. Itu sebabnya dompet ini lebih cocok buat nyimpen jumlah kecil yang memang kamu pakai untuk kebutuhan harian. Kalau buat nyimpen jumlah besar, jauh lebih aman pakai solusi lain seperti dompet perangkat keras.

Kalau kamu pengin lebih dalam lagi belajar tentang jaringan Lightning dan cara kerjanya secara teknis, kamu bisa ikutin kursus ini:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Di tutorial ini, kita bakal ngebahas **Lipa,** dompet Lightning yang simpel tapi efektif, dikembangkan di Swiss.

## Memperkenalkan Lipa

Lipa adalah dompet Lightning non-kustodian yang punya ciri khas utama: simpel dipakai dan tampilannya rapi. Dibuat oleh tim asal Swiss, Lipa fokus pada privasi sekaligus kemudahan penggunaan, terutama buat pemula.

- Fitur-fitur utamanya antara lain:
- Antarmuka pengguna yang intuitif
- Manajemen saluran Lightning otomatis
- Dukungan protokol LNURL
- Fitur beli bitcoin langsung dari aplikasi

## Menginstalasi dan mengatur Lipa

Langkah pertama, unduh aplikasi Lipa. Untuk saat ini, aplikasi ini baru tersedia di iOS.


- [Untuk Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Versi Android saat ini masih dalam pengembangan dan bakal segera tersedia.

![Installation de Lipa](assets/fr/01.webp)

Begitu kamu buka aplikasi, kamu bakal langsung sampai di layar beranda yang kasih dua pilihan:

- Bikin dompet baru

 Pulihkan dompet yang sudah ada dari cadangan

Setelah kamu pilih salah satu, aplikasi bakal minta izin buat nyalain notifikasi. Ini penting banget, karena notifikasi dipakai aplikasi untuk:

- Kasih peringatan saat ada pembayaran masuk, bahkan kalau aplikasinya lagi ditutup

- Ngasih info soal langkah-langkah pembelian bitcoin lewat solusi terintegrasi mereka

Setelah itu, aplikasi ngenalin fitur-fitur utamanya lewat beberapa layar pengantar:

- Penerimaan pembayaran mulus:** Kamu bisa tetap nerima pembayaran Bitcoin meskipun aplikasinya ditutup, jadi lebih andal dan nyaman.

- Alamat Lightning non-kustodian:** Lipa sekarang dukung alamat Lightning non-kustodian, bikin privasi lebih terjaga dan kamu tetap punya kontrol penuh atas bitcoin milikmu.

- Kontrol atas data analitik:** Demi transparansi dan privasi, kamu bisa lihat data apa aja yang dikumpulin dan atur sendiri preferensi berbagi.

- Kirim via nomor telepon:** Gak perlu ribet pakai alamat panjang, cukup pilih kontak, masukin jumlahnya, dan kirim bitcoin langsung ke nomor telepon mereka.

Lipa juga terus dapet peningkatan rutin soal stabilitas, keamanan, dan keandalan, supaya pengalaman pengguna makin optimal.

## Navigasi aplikasi

Antarmuka Lipa diatur di sekitar 4 tab utama yang dapat diakses melalui bilah navigasi di bagian bawah layar:

![Navigation principale](assets/fr/02.webp)


- Beranda**: Nampilin saldo dan riwayat transaksi kamu saat ini
- Pemindai**: Buat nge-scan kode QR waktu mau bayar
- Peta**: Nampilin peta interaktif berisi bisnis yang nerima Bitcoin di sekitarmu
- Pengaturan**: Akses ke setelan aplikasi, cadangan, dan preferensi pribadi

Selain itu, ada menu tambahan yang bisa kamu buka dengan menarik layar beranda ke bawah.

![Menu supplémentaire](assets/fr/03.webp)

Gerakan ini bakal munculin fitur tambahan, seperti:


- Membeli bitcoin
- Setoran bitcoin on-chain
- Membuat faktur Lightning untuk menerima bitcoin
- Pembayaran faktur kilat

## Simpan portofolio 

Untuk mencadangkan dompetmu, buka tab **Pengaturan** lalu pilih **frasa pemulihan**. Lipa pakai frasa pemulihan yang wajib banget kamu catat dengan hati-hati di media fisik (misalnya kertas atau logam). Frasa ini adalah satu-satunya cara buat balikin dana kamu kalau ponsel hilang atau dicuri.

Buat validasi cadangan, aplikasi bakal minta kamu konfirmasi 3 kata acak dari frasa tersebut.

![Backup](assets/fr/04.webp)

Kalau kamu mau info lebih lengkap soal cara mencadangkan dan ngatur frasa pemulihan dengan benar, aku saranin banget buat ikutin tutorial lain, apalagi kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Menerima bitcoin

Buat nerima bitcoin, kamu punya dua opsi. Caranya, balik dulu ke layar beranda lalu tarik layar ke bawah. Setelah itu kamu bisa pilih:

Pilih **Transfer BTC** buat nerima bitcoin secara on-chain. Tinggal scan aja kode QR pakai dompet lainmu lalu selesaikan transaksinya.

Pilih **Request** buat nerima lewat jaringan Lightning, lalu masukin jumlah yang pengin kamu terima.

Di kedua opsi ini, **ada biaya sekitar 0,4% dari jumlah transaksi, atau kira-kira 2.500 sat kalau aplikasi perlu buka saluran pembayaran baru** (biasanya ini kejadian di pembayaran pertama).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Kirim bitcoin

Buat ngirim bitcoin, buka layar beranda, tarik layar ke bawah lalu pilih "Bayar". Setelah itu kamu bisa:

- Masukin alamat Lightning (LNURL)
- Scan kode QR Lightning buat langsung bayar
- Kamu juga bisa langsung buka tab kedua di bagian bawah layar buat nge-scan kode QR secara instan.

![Envoi de bitcoins](assets/fr/07.webp)

## Beli bitcoin

Lipa juga kasih opsi buat beli bitcoin langsung di dalam aplikasi dengan biaya 1,5%. Caranya gampang: buka layar beranda, tarik ke bawah buat munculin menu, lalu pilih "Beli BTC". Setelah itu, bakal ada tiga layar pengantar yang ngejelasin langkah-langkah pembeliannya.

![Menu d'achat](assets/fr/08.webp)

Selanjutnya, masukin detail bank dari akun yang mau kamu pakai buat beli. Pilih mata uang, lalu masukin alamat email kamu.

Setelah layar loading selesai, kamu bakal dapet nomor referensi yang harus dicantumin di transfer, plus detail bank tujuan buat penukarannya.

![Sélection du montant](assets/fr/09.webp)

Yang perlu kamu lakukan cuma transfer jumlah yang kamu mau lewat bank kamu, pakai RIB yang tadi udah dicatat, lalu masukin nomor referensi saat transaksi. Dengan begitu, Lipa bisa nyocokin transfer bank itu dengan dompet Lipa kamu.

![Confirmation d'achat](assets/fr/10.webp)

## Keuntungan dan kerugian

### Manfaat


- Antarmuka yang intuitif
- Biaya layanan yang benar
- Non kustodian
- Fitur beli bitcoin langsung di aplikasi
- Integrasi BTCmap
- Dukungan NFC

### Kekurangan


- Kamu nggak bisa mengirim bitcoin secara berantai
- Pembayaran sedikit lebih lama dari rata-rata

Lipa adalah pilihan yang sangat pas buat mulai pakai Lightning Network, terutama kalau kamu nyari solusi simpel buat pembayaran harian. Dengan kemudahan penggunaan dan tampilan yang rapi, Lipa jadi dompet ideal buat pemula, tapi tetap nyediain fitur penting yang dibutuhin buat penggunaan Lightning sehari-hari.

## Sumber informasi:


- [Situs web resmi Lipa](https://lipa.swiss/)
- [Dukungan Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)
