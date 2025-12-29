---
name: SMS4Sats
description: Menerima dan mengirim SMS secara anonim dengan membayar di Bitcoin Lightning
---

![cover](assets/cover.webp)



Verifikasi SMS telah menjadi suatu keharusan bagi banyak layanan online. Entah itu untuk membuat akun di sebuah platform, memvalidasi pendaftaran, atau mengonfirmasi identitas, situs web hampir secara sistematis memerlukan nomor telepon. Praktik yang meluas ini menimbulkan masalah besar bagi siapa pun yang ingin menjaga privasi mereka: nomor pribadi Anda menjadi pengenal permanen, menghubungkan berbagai aktivitas digital Anda dengan identitas asli Anda dan membuka pintu untuk permintaan komersial yang tidak diinginkan.



**SMS4Sats** menanggapi masalah ini dengan menawarkan nomor telepon sementara untuk menerima dan mengirim pesan SMS. Layanan ini menonjol karena model tanpa registrasi dan pembayaran Bitcoin eksklusif melalui Lightning Network. Untuk beberapa satoshi, Anda mendapatkan nomor sekali pakai yang memungkinkan Anda untuk memvalidasi registrasi tanpa harus mengungkapkan nomor pribadi Anda.



Tutorial ini memandu Anda melalui tiga fitur SMS4Sats: menerima SMS verifikasi, mengirim SMS anonim, dan menyewa nomor sementara selama beberapa jam.



## Apa itu SMS4Sats?



SMS4Sats adalah layanan online yang dapat diakses di [sms4sats.com] (https://sms4sats.com), memungkinkan manajemen SMS anonim melalui pembayaran di Bitcoin Lightning. Layanan ini menawarkan tiga fungsi yang berbeda: penerimaan kode verifikasi sekali pakai, pengiriman SMS ke nomor manapun, dan penyewaan nomor sementara selama beberapa jam.



### Filosofi dan model operasi



Proyek ini dirancang untuk memastikan kerahasiaan maksimum dan kedaulatan keuangan. Dengan tidak memerlukan pembuatan akun dan hanya menerima pembayaran Bitcoin Lightning, SMS4Sats sepenuhnya menghilangkan kebutuhan untuk memberikan data pribadi. Tidak ada alamat email, tidak ada kartu kredit, tidak ada informasi pribadi yang diperlukan. Hanya pembayaran Lightning yang diperlukan untuk mengakses layanan.



Layanan ini mendukung lebih dari 400 situs dan aplikasi di sekitar 120 negara, yang mencakup sebagian besar kebutuhan verifikasi yang umum. Cakupan geografis yang luas ini memungkinkan validasi pendaftaran di berbagai platform, mulai dari jejaring sosial hingga layanan perpesanan.



### Model pembayaran bersyarat



SMS4Sats menggunakan faktur Lightning bersyarat (faktur hodl) untuk fungsionalitas penerimaan SMS. Mekanisme ini memastikan bahwa Anda hanya ditagih jika SMS benar-benar diterima. Jika tidak ada pesan yang masuk dalam waktu yang ditentukan (maksimum 20 menit), pembayaran secara otomatis dibatalkan dan satelit dikembalikan ke wallet Anda. Jaminan ini tidak berlaku untuk fitur pengiriman dan penyewaan, yang tidak dapat dikembalikan.



## Tiga fitur SMS4Sats



Antarmuka SMS4Sats diatur dalam tiga tab yang berhubungan dengan tiga penggunaan yang berbeda: **TERIMA** untuk menerima kode verifikasi, **KIRIM** untuk mengirim SMS anonim, dan **SEWA** untuk menyewa nomor sementara.



### Menerima SMS



Fitur utama memungkinkan Anda mendapatkan nomor sementara untuk menerima kode verifikasi unik. Setelah kode diterima dan digunakan, nomor tersebut akan dinonaktifkan secara permanen.



### Kirim SMS



Fitur ini memungkinkan Anda mengirim SMS ke nomor telepon mana pun tanpa mengungkapkan identitas Anda. Penerima akan menerima pesan dari nomor anonim.



### Menyewa tindakan



Untuk pengguna yang perlu menerima beberapa pesan SMS pada satu nomor, SMS4Sats menawarkan opsi penyewaan sementara. Opsi ini memungkinkan Anda untuk menerima dan mengirim beberapa pesan selama periode sewa.



**Catatan mengenai harga**: Harga yang ditampilkan dalam tutorial ini bersifat indikatif. Harga bervariasi sesuai dengan negara tujuan, target layanan dan permintaan saat ini. Sebagai contoh, SMS ke Telegram Prancis dapat dikenakan biaya antara 1.500 hingga 5.000 satoshi, tergantung kondisi. Selalu periksa jumlah tagihan Lightning yang tepat sebelum membayar.



## Menerima SMS verifikasi



Mari kita lihat secara rinci cara menggunakan SMS4Sats untuk menerima kode verifikasi, diilustrasikan dengan pembuatan akun Telegram.



### Langkah 1: Pilih negara dan layanan



Buka [sms4sats.com](https://sms4sats.com) dan tetap pada tab **TERIMA**. Pilih negara dari nomor yang diinginkan dari menu tarik-turun. Jika layanan target langganan Anda terdaftar, pilih layanan tersebut untuk mengoptimalkan peluang penerimaan.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Dalam contoh ini, kami memilih Prancis sebagai negara dan Telegram sebagai layanan target. Klik **NEXT** untuk melanjutkan ke langkah berikutnya.



### Langkah 2: Bayar faktur Lightning



Faktur Lightning ditampilkan dalam bentuk kode QR. Jumlahnya bervariasi menurut negara dan layanan yang dipilih. Pindai kode QR dengan Lightning wallet Anda atau salin faktur untuk membayar secara manual.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Perhatikan pesan penting: "Tidak Ada Kode SMS = Tidak Ada Pembayaran". Jika Anda tidak menerima SMS, pembayaran Anda akan secara otomatis dibatalkan dan dikembalikan dalam waktu maksimal 20 menit.



### Langkah 3: Dapatkan nomor sementara



Setelah pembayaran dikonfirmasi, nomor telepon sementara akan segera ditampilkan. Penghitung menunjukkan waktu yang tersisa untuk menerima SMS.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Salin nomor ini (di sini +33 7 74 70 09 66) untuk menggunakannya pada layanan yang ingin Anda daftarkan.



### Langkah 4: Gunakan nomor pada layanan target



Masukkan nomor sementara pada aplikasi atau situs web tempat Anda membuat akun. Dalam contoh Telegram kami, masukkan nomor, konfirmasikan, dan tunggu kode verifikasi.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Prosesnya sama dengan pendaftaran konvensional: Anda memasukkan nomor, Telegram mengirimkan kode verifikasi melalui SMS, lalu Anda menyelesaikan pembuatan akun.



### Langkah 5: Ambil kode verifikasi



Kembali ke antarmuka SMS4Sats. Segera setelah SMS diterima, kode aktivasi akan ditampilkan secara otomatis. Klik **SALIN KODE** untuk menyalinnya dengan mudah.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Masukkan kode ini pada layanan yang dituju untuk menyelesaikan pendaftaran Anda. Nomor sementara kemudian dinonaktifkan secara permanen.



## Mengirim SMS anonim



SMS4Sats juga memungkinkan Anda mengirim pesan SMS ke nomor mana pun tanpa mengungkapkan identitas Anda.



### Langkah 1: Menulis pesan



Klik tab **KIRIM**. Masukkan nomor telepon tujuan dengan kode panggilan internasionalnya dan tulis pesan Anda (maksimum 1600 karakter).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Klik **NEXT** untuk melanjutkan ke pembayaran.



### Langkah 2: Bayar dan kirim



Bayar faktur Lightning yang ditampilkan. Setelah pembayaran dikonfirmasi, SMS akan segera dikirim ke penerima.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Kode konfirmasi akan ditampilkan untuk mengonfirmasi bahwa pesan telah terkirim. Penerima akan menerima SMS dari nomor anonim.



## Menyewa nomor sementara



Untuk penggunaan yang membutuhkan beberapa pesan SMS pada nomor yang sama, fitur SEWA memungkinkan Anda menyewa nomor selama beberapa jam.



### Konfigurasi penyewaan



Klik tab **SEWA**. Pilih negara dan durasi.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Hal-hal penting yang perlu diperhatikan:**




- Harga bervariasi sesuai dengan negara dan lama tinggal
- Biaya sewa tidak dapat dikembalikan**, tidak seperti pesan SMS sekali pakai
- Nomor yang disewakan umumnya tidak dapat digunakan dengan Telegram
- Opsi ini cocok untuk berlangganan beberapa layanan secara berurutan



Setelah Anda mengeklik **NEXT** dan membayar faktur Lightning, Anda akan mendapatkan nomor yang bisa Anda gunakan selama masa sewa untuk menerima dan mengirim pesan SMS.



## Keuntungan dan keterbatasan



### Sorotan



**Tidak diperlukan data pribadi**: Model tanpa registrasi menjamin bahwa tidak ada informasi pribadi yang dikumpulkan.



**Tiga fungsi tambahan**: Menerima, mengirim, dan menyewakan mencakup sebagian besar kebutuhan.



**Pembayaran hanya dalam Bitcoin saja**: Lightning Network memungkinkan transaksi instan dan pseudonim.



**Penggantian biaya secara otomatis**: Saat menerima pesan SMS, sistem faktur hodl menjamin bahwa Anda hanya membayar jika SMS masuk.



### Kendala yang perlu dipertimbangkan



**Keamanan saluran SMS relatif**: Kode SMS bukanlah metode autentikasi yang kuat dan tidak boleh digunakan untuk akun yang sensitif.



**Kompatibilitas variabel**: Banyak situs yang mendeteksi dan memblokir nomor virtual. Mungkin diperlukan beberapa kali percobaan.



**Nomor yang tidak dapat digunakan kembali**: Setelah sekali pakai, nomor tersebut akan didaur ulang dan tidak dapat dipulihkan.



**Penyewaan tidak dapat dikembalikan**: Tidak seperti pesan SMS sekali pakai, penyewaan tidak disertai jaminan uang kembali.



## Praktik terbaik



### Gunakan Tor untuk privasi yang lebih baik



SMS4Sats dapat diakses melalui [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Konfigurasi ini menyamarkan alamat IP Anda ketika mengakses layanan.



### Hindari akun-akun penting



Jangan pernah menggunakan nomor sekali pakai untuk akun-akun penting Anda (bank, email utama). Jika platform ini mengharuskan Anda untuk memvalidasi ulang nomor Anda di kemudian hari, Anda akan kehilangan akses ke akun tersebut.



### Pisahkan identitas digital Anda



Untuk akun pseudonim, gabungkan nomor sementara dengan alamat email sekali pakai dan peramban yang terisolasi dari penggunaan biasa.



### Pilih 2FA yang kokoh



Setelah akun Anda dibuat, aktifkan solusi autentikasi yang lebih kuat: Aplikasi TOTP (Aegis, Ente Auth) atau kunci keamanan fisik FIDO2.



## Kesimpulan



SMS4Sats adalah solusi lengkap untuk manajemen SMS rahasia. Apakah Anda ingin menerima kode verifikasi, mengirim pesan anonim, atau menyewa nomor sementara, layanan ini memenuhi berbagai kebutuhan kerahasiaan, berkat pembayaran dalam Bitcoin Lightning.



Namun, harap diingat keterbatasannya: layanan ini tidak menjamin anonimitas mutlak, dan tidak cocok untuk akun sensitif atau jangka panjang. Jika digunakan dengan bijak dan dengan kesadaran akan keterbatasannya, SMS4Sats adalah alat yang praktis untuk mendapatkan kembali kendali atas komunikasi telepon Anda.



## Sumber daya





- [Situs web resmi SMS4Sats](https://sms4sats.com)
- [FAQ Layanan](https://sms4sats.com/faq)
- [Alamat Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)