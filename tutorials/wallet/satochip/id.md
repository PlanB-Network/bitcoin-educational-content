---
name: Satochip
description: Pengaturan dan penggunaan kartu pintar Satochip
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang dibuat khusus buat ngelola dan ngamanin kunci privat dari dompet Bitcoin. Beda sama dompet perangkat lunak (atau dompet panas) yang dipasang di perangkat umum yang sering nyambung ke internet, dompet perangkat keras ngasih isolasi fisik buat kunci privat, sehingga bisa ngurangin risiko peretasan dan pencurian.

Tujuan utama dompet perangkat keras adalah meminimalisir fungsionalitas perangkat biar permukaan serangannya makin kecil. Permukaan serangan yang lebih kecil berarti lebih sedikit jalur serangan potensial, alias lebih sedikit celah di sistem yang bisa dimanfaatkan penyerang buat ngakses bitcoin.

Disarankan banget pake dompet perangkat keras buat ngamanin bitcoin kamu, terutama kalau jumlahnya signifikan, baik secara nilai absolut maupun proporsi dari total aset kamu.

Dompet perangkat keras dipakai bareng perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunaknya ngurus pembuatan transaksi, tapi tanda tangan kriptografis yang dibutuhin buat validasi transaksi dilakuin sepenuhnya di dalam dompet perangkat keras. Artinya, kunci privat nggak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras ngasih perlindungan ganda buat pengguna: di satu sisi, mereka ngejaga bitcoin kamu dari serangan jarak jauh dengan nyimpen kunci privat secara offline, dan di sisi lain, mereka umumnya punya ketahanan fisik lebih baik terhadap upaya ekstraksi kunci. Dan dari 2 kriteria keamanan inilah, kita bisa menilai dan ngeranking model-model berbeda yang ada di pasaran.

Di tutorial ini, aku bakal ngenalin salah satu solusi itu: **Satochip.**

## Pengenalan ke Satochip

Satochip adalah dompet perangkat keras berbentuk kartu dengan chip bersertifikat "*EAL6+,*" salah satu standar keamanan tertinggi "*(NXP JCOP)*". Produk ini dibuat oleh sebuah perusahaan asal Belgia.

![SATOCHIP](assets/notext/01.webp)

Kartu pintar ini dijual seharga €25, yang tergolong sangat terjangkau dibanding dompet perangkat keras lain di pasaran. Chip-nya adalah elemen aman yang punya resistensi sangat baik terhadap serangan fisik. Selain itu, kodenya bersifat open-source "*(AGPLv3).*"

Tapi karena formatnya, Satochip nggak punya banyak opsi kayak perangkat keras lain. Jelas nggak ada baterai, kamera, atau slot kartu micro SD, karena bentuknya memang kartu. Kekurangan terbesar menurut aku adalah nggak adanya layar di dompet perangkat keras ini, yang bikin lebih rentan terhadap beberapa jenis serangan jarak jauh. Soalnya, pengguna dipaksa buat tanda tangan secara buta dan percaya penuh sama apa yang mereka lihat di layar komputer.

Meski punya keterbatasan, Satochip tetap menarik berkat harganya yang murah. Dompet ini bisa dipakai buat ningkatin keamanan dompet pengeluaran, sementara dompet tabungan tetap dilindungi dompet perangkat keras yang ada layarnya. Satochip juga cocok buat yang punya jumlah bitcoin kecil dan nggak mau keluar seratus euro lebih buat perangkat yang lebih canggih. Selain itu, penggunaan Satochip dalam konfigurasi multisig, atau nantinya dalam sistem dompet dengan timelock, bisa ngasih keuntungan tambahan yang menarik.

Perusahaan Satochip juga nawarin 2 produk lain. Ada **Satodime,** yaitu kartu pemegang yang didesain buat nyimpen bitcoin secara offline tapi nggak bisa dipakai transaksi. Bisa dibilang kayak dompet kertas yang jauh lebih aman, cocok misalnya buat bikin hadiah. Terakhir ada **Seedkeeper,** yaitu manajer frasa mnemonik. Alat ini bisa dipakai buat nyimpen benih secara aman tanpa harus ditulis langsung di secarik kertas.

## Bagaimana cara membeli Satochip?
Satochip sudah tersedia di [di situs resmi](https://satochip.io/product/satochip/). Untuk membelinya di toko fisik, kamu juga bisa menemukan [daftar reseller resmi](https://satochip.io/resellers/) di situs web Satochip.
Buat berinteraksi dengan perangkat lunak manajemen dompet kamu, Satochip nawarin dua cara: lewat komunikasi NFC atau pakai pembaca kartu pintar. Buat opsi NFC, pastiin perangkat kamu kompatibel sama teknologi ini, atau bisa juga pakai pembaca NFC eksternal. Satochip jalan di frekuensi standar 13,56 MHz. Kalau nggak, kamu bisa beli pembaca kartu pintar, yang bisa ditemuin di situs web Satochip atau tempat lain.

![SATOCHIP](assets/notext/02.webp)

## Bagaimana cara mengatur Satochip dengan Sparrow?

Setelah kamu nerima Satochip, langkah pertama adalah ngecek kemasannya buat pastiin nggak ada yang kebuka. Kemasan Satochip harus dilengkapi stiker segel. Kalau stiker ini hilang atau rusak, bisa jadi itu tanda kalau kartu pintar udah dikompromikan dan mungkin nggak asli.
![SATOCHIP](assets/notext/03.webp)
Kamu akan menemukan Satochip di dalamnya.

![SATOCHIP](assets/notext/04.webp)

Buat ngelola dompet, di tutorial ini aku nyaranin pakai Sparrow. Kalau kamu belum punya perangkat lunaknya, [kunjungi situs resmi untuk mengunduhnya](https://sparrowwallet.com/download/). Kamu juga bisa cek tutorial kami tentang Sparrow Wallet (segera hadir).
![SATOCHIP](assets/notext/05.webp)

Masukin Satochip kamu ke pembaca kartu pintar atau tempelin di atas pembaca NFC, lalu sambungkan pembaca ke komputer yang udah buka Sparrow.

![SATOCHIP](assets/notext/06.webp)

Buka Sparrow Wallet dan pastiin kamu terhubung dengan benar ke node Bitcoin. Buat ngeceknya, lihat tanda centang di kanan bawah: kuning berarti terhubung ke node publik, hijau untuk koneksi ke Bitcoin Core, dan biru untuk Electrum.

![SATOCHIP](assets/notext/07.webp)

Di Sparrow Wallet, klik pada tab "*File*".

![SATOCHIP](assets/notext/08.webp)

Kemudian pada menu "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Pilih nama untuk dompet, kemudian klik pada "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Klik pada tombol "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Klik pada tombol "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Satochip milikmu harusnya muncul. Klik pada "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

Selanjutnya, kamu perlu atur kode PIN buat buka kunci Satochip. Pilih kata sandi yang kuat, antara 4 sampai 16 karakter, dan pastiin buat bikin cadangannya.

Perlu dicatat, kata sandi ini bukan passphrase. Artinya, walaupun nggak punya kata sandi ini, frasa mnemonik kamu tetap bisa dipakai buat impor ulang dompet ke perangkat lunak kalau dibutuhin. Kata sandi cuma dipakai buat ngamanin akses ke Satochip itu sendiri, mirip kode PIN di dompet perangkat keras lain.

Setelah kata sandi dimasukkan, klik lagi pada tombol "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Catat lagi kata sandi tersebut, kemudian klik pada tombol "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Anda kemudian sampai pada jendela untuk menghasilkan frasa mnemonik Anda. Klik tombol "*Generate New*".

![SATOCHIP](assets/notext/16.webp)

Buat satu atau lebih salinan fisik dari frasa pemulihan kamu dengan menulisnya di kertas atau media logam. Ingat, frasa ini ngasih akses penuh ke bitcoin kamu tanpa perlindungan tambahan. Jadi, kalau ada orang yang nemuin, mereka bisa langsung nyuri bitcoin kamu, bahkan tanpa akses ke Satochip atau kode PIN. Makanya penting banget buat ngamanin cadangan ini. Selain itu, frasa ini juga memungkinkan kamu buat balik lagi akses ke bitcoin kalau Satochip hilang, rusak, atau kamu lupa kode PIN.

![SATOCHIP](assets/notext/17.webp)

Dompet Bitcoin-mu sudah berhasil dibuat.

![SATOCHIP](assets/notext/18.webp)

Klik lagi pada tombol "*Import Keystore*".

![SATOCHIP](assets/notext/19.webp)

Dompet kamu sekarang udah dibuat. Kunci privat kamu sekarang tersimpan di smartcard Satochip. Klik tombol "Apply" buat lanjut.

![SATOCHIP](assets/notext/20.webp)

Disarankan buat bikin kata sandi tambahan buat ngamanin informasi publik yang dikelola Sparrow Wallet, selain kode PIN Satochip. Kata sandi ini bakal ngejaga keamanan akses ke Sparrow Wallet, sehingga ngebantu melindungi kunci publik, alamat, dan riwayat transaksi dari akses yang nggak sah.

![SATOCHIP](assets/notext/21.webp)

Masukkan kata sandi di dua kolom, lalu klik pada tombol "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Dan begitulah, Satochip kamu sekarang udah diatur di Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Sekarang dompet kamu udah dibuat, kamu bisa cabut Satochip kamu. Simpan di tempat yang aman!

## Bagaimana cara menerima bitcoin dengan Satochip?

Setelah berada di dompet, klik pada tab "*Receive*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet bakal bikin alamat untuk dompet kamu. Biasanya, di dompet hardware lain, disarankan klik "*Display Address*" buat verifikasi alamat langsung di layar perangkat. Sayangnya, opsi ini nggak tersedia di Satochip, tapi pastiin buat pakai cara ini di dompet lain kamu.

![SATOCHIP](assets/notext/25.webp)

Kamu bisa nambahin "*Label*" buat mendeskripsikan sumber bitcoin yang bakal diamankan di alamat ini. Ini praktik yang bagus karena ngebantu kamu ngatur UTXO dengan lebih rapi.

![SATOCHIP](assets/notext/26.webp)

Buat info lebih lanjut tentang pelabelan, aku juga nyaranin cek tutorial lain ini:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Setelah itu, kamu bisa pakai alamat ini buat nerima bitcoin.

![SATOCHIP](assets/notext/27.webp)
## Bagaimana cara Mengirim Bitcoin dengan Satochip?

Sekarang setelah kamu nerima sats pertama di dompet aman kamu pakai Satochip, kamu juga bisa mulai ngabisinnya! Sambungkan Satochip ke komputer, buka Sparrow Wallet, lalu pergi ke tab "*Send*" buat bikin transaksi baru.

![SATOCHIP](assets/notext/28.webp)

Kalau kamu mau kontrol koin secara spesifik, alias milih UTXO mana yang dipakai dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang mau dipakai, lalu klik "*Kirim Terpilih*". Kamu bakal dibawa ke layar yang sama dengan tab "*Send*", tapi UTXO yang kamu pilih udah siap dipakai buat transaksi.

![SATOCHIP](assets/notext/29.webp)

Masukin alamat tujuan. Kamu juga bisa nambah alamat lain dengan klik tombol "*+ Tambah*".

![SATOCHIP](assets/notext/30.webp)

Catat sebuah "*Label*" untuk mengingat tujuan dari pengeluaran ini.

![SATOCHIP](assets/notext/31.webp)

Pilih jumlah yang akan dikirim ke alamat ini.

![SATOCHIP](assets/notext/32.webp)

Atur tarif biaya transaksi kamu sesuai kondisi pasar saat ini.

![SATOCHIP](assets/notext/33.webp)

Pastikan semua parameter transaksi  sudah benar, kemudian klik pada "*Buat Transaksi*".

![SATOCHIP](assets/notext/34.webp)

Jika semuanya sesuai dengan keinginan, klik pada "*Finalisasi Transaksi untuk Ditandatangani*".

![SATOCHIP](assets/notext/35.webp)

Klik pada "*Tanda Tangan*".

![SATOCHIP](assets/notext/36.webp)

Klik pada "*Tanda Tangan*" lagi di sebelah Satochip-mu.

![SATOCHIP](assets/notext/37.webp)

Masukkan kode PIN Satochip milikmu, kemudian klik pada "*Tanda Tangan*" lagi untuk menandatangani transaksimu.

![SATOCHIP](assets/notext/38.webp)

Sekarang transaksimu sudah ditandatangani. Klik pada "*Siarkan Transaksi*" untuk menyiarkannya ke jaringan Bitcoin.

![SATOCHIP](assets/notext/39.webp)

Kamu bisa menemukannya di tab "*Transaksi*" dari Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

Selamat, sekarang kamu udah paham cara pakai Satochip! Kalau kamu ngerasa tutorial ini bermanfaat, aku bakal sangat senang kalau kamu mau kasih jempol ke atas di bawah ini. Jangan ragu juga buat bagiin artikel ini ke jaringan sosial kamu. Makasih banyak!
