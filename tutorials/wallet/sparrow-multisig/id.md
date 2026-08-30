---
name: Sparrow Wallet - Multisig
description: Membuat dompet multi-tanda tangan di Sparrow
---
![cover](assets/cover.webp)


Dompet multi-tanda tangan (sering disebut "*Multisig*") adalah sebuah struktur dompet Bitcoin yang membutuhkan beberapa tanda tangan kriptografi, dari kunci yang berbeda, untuk mengotorisasi sebuah pengeluaran. Berbeda dengan dompet konvensional ("*singlesig*"), di mana satu kunci privat sudah cukup untuk membuka sebuah UTXO, Multisig didasarkan pada model **m-of-n**: dari _n_ kunci yang terkait dengan dompet, _m_ di antaranya wajib menandatangani bersama (co-sign) setiap transaksi.


Mekanisme ini memungkinkan kendali atas sebuah dompet untuk dibagikan di antara beberapa entitas atau perangkat. Sebagai contoh, dalam konfigurasi 2-of-3, tiga set kunci independen dihasilkan, tetapi hanya dua yang dibutuhkan untuk mengeluarkan dana. Arsitektur ini secara drastis mengurangi risiko yang terkait dengan pembobolan atau kehilangan sebuah kunci: seorang pencuri yang memiliki akses hanya ke satu kunci tidak dapat mengosongkan dompet, dan seorang pengguna yang kehilangan satu kunci tetap dapat mengakses dananya dengan dua kunci yang tersisa.


![Image](assets/fr/01.webp)


Namun, keamanan yang lebih besar ini datang dengan kompleksitas yang lebih besar pula. Menyiapkan dompet Multisig membutuhkan pengamanan beberapa frasa mnemonic (satu per faktor tanda tangan) dan kunci publik tambahan ("*xpub*"). Sebagai contoh, jika Anda menggunakan dompet Multisig 2-of-3, untuk memulihkan dompet Anda harus memiliki ketiga frasa mnemonic, atau setidaknya dua dari tiga frasa tersebut. Namun jika Anda hanya memiliki dua dari tiga frasa, Anda juga membutuhkan akses ke ketiga *xpub*, tanpa itu tidak mungkin untuk mengambil kunci publik yang dibutuhkan untuk mengakses bitcoin yang mereka lindungi.


Sebagai ringkasan, untuk memulihkan sebuah dompet Multisig, Anda harus:


- Memiliki akses ke semua frasa mnemonic yang terkait dengan setiap faktor tanda tangan;
- Atau memiliki jumlah minimum frasa mnemonic yang dibutuhkan oleh ambang batas (threshold) untuk dapat menandatangani, dan juga memiliki akses ke xpub dari semua faktor untuk dapat mengambil kunci publik yang dibutuhkan.


![Image](assets/fr/02.webp)


Pengelolaan cadangan dompet Multisig ini dipermudah oleh *Output Script Descriptor*, yang mengumpulkan semua data publik yang dibutuhkan untuk mengakses dana. Namun, fungsi ini belum diimplementasikan di semua perangkat lunak pengelolaan dompet.


Multisig sangat cocok untuk para bitcoiner yang mencari keamanan yang lebih baik atau pengelolaan dana secara kolektif: perusahaan, asosiasi, keluarga, atau pengguna individu yang memegang jumlah bitcoin yang signifikan. Multisig dapat digunakan untuk membuat skema tata kelola yang terdesentralisasi, misalnya, untuk mendistribusikan wewenang penandatanganan di antara beberapa manajer atau anggota tim.


Dalam tutorial ini, kita akan belajar cara membuat dan menggunakan dompet multi-tanda tangan klasik dengan **Sparrow Wallet**. Jika Anda ingin membuat dompet multi-tanda tangan khusus dengan timelock, saya sarankan Anda menggunakan Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prasyarat


Untuk tutorial ini, saya akan menunjukkan kepada Anda cara membuat Multisig dengan [perangkat lunak pengelolaan dompet Sparrow Wallet](https://sparrowwallet.com/download/). Jika Anda belum menginstal perangkat lunak ini, silakan instal sekarang. Jika Anda membutuhkan bantuan, kami juga memiliki tutorial terperinci tentang konfigurasi Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Untuk menyiapkan dompet multi-tanda tangan, Anda membutuhkan beberapa dompet perangkat keras (hardware wallet) yang berbeda. Untuk Multisig 2-of-3, misalnya, Anda dapat menggunakan:


- Sebuah Trezor Model One;
- Ledger Flex;
- Sebuah Passport Core.


![Image](assets/fr/03.webp)


Sebaiknya Anda menggunakan merek Hardware Wallet yang berbeda dalam konfigurasi Multisig Anda. Ini memastikan bahwa jika sebuah model tertentu mengalami masalah serius, hal itu tidak akan memengaruhi keamanan keseluruhan Multisig Anda. Selain itu, ini memungkinkan Anda memperoleh manfaat dari keunggulan khusus setiap perangkat. Sebagai contoh, dalam konfigurasi saya:



- Trezor Model One sepenuhnya open-source, yang memungkinkan verifikasi pembuatan seed. Namun, karena tidak dilengkapi dengan Secure Element, perangkat ini tetap rentan terhadap serangan fisik;



- Ledger Flex, di sisi lain, mendapat manfaat dari firmware proprietary yang tidak dapat diverifikasi, tetapi dilengkapi dengan Secure Element yang menawarkan perlindungan fisik yang sangat baik;



- Passport Core menggabungkan firmware yang sepenuhnya open-source, sebuah Secure Element, dan pertukaran kode QR air-gapped. Perangkat ini adalah penanda tangan ketiga yang independen yang dapat memverifikasi alamat dan menandatangani PSBT tanpa koneksi data USB.


Sebelum mengonfigurasi dompet Multisig Anda, pastikan setiap Hardware Wallet telah dikonfigurasi dengan benar (pembuatan dan penyimpanan mnemonic, penentuan PIN). Untuk instruksi terperinci, Anda dapat merujuk pada tutorial kami untuk setiap Hardware Wallet, misalnya:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Seperti yang akan kita lihat nanti dalam tutorial ini, dimungkinkan juga untuk memasukkan ke dalam konfigurasi Multisig Anda sebuah faktor yang tidak terkait dengan Hardware Wallet, tetapi kunci privatnya disimpan di komputer Anda. Metode ini jelas kurang aman dibandingkan dengan penggunaan eksklusif dompet perangkat keras, tetapi mungkin relevan dalam kasus-kasus tertentu. Sebagai contoh, untuk Multisig 2-of-3, Anda dapat memilih dua hardware wallet dan satu Software Wallet.

> ⚠️ **Peringatan keamanan Coldcard MK3:** jangan membuat seed baru pada MK3 yang menjalankan firmware sebelum versi 4.2.0. Seed yang dibuat pada firmware yang lebih lama harus diganti dan dananya dipindahkan. Karena itu, tutorial ini menggunakan Passport Core sebagai penanda tangan referensi air-gapped-nya.


## Membuat dompet Multisig


Buka Sparrow Wallet, klik tab "*File*", lalu pilih "*New Wallet*".


![Image](assets/fr/04.webp)


Berikan nama untuk dompet multi-tanda tangan Anda, lalu klik "*Create Wallet*" untuk mengonfirmasi.


![Image](assets/fr/05.webp)


Pada menu drop-down "*Policy Type*", pilih opsi "*Multi Signature*".


![Image](assets/fr/06.webp)


Di sudut kanan atas, Anda sekarang dapat menentukan jumlah total kunci dalam Multisig Anda, serta jumlah co-signer yang dibutuhkan untuk mengotorisasi sebuah pengeluaran. Dalam contoh saya, ini adalah skema 2-of-3.


![Image](assets/fr/07.webp)


Di bagian bawah jendela, Sparrow Wallet menampilkan tiga "*Keystore*". Masing-masing mewakili satu set kunci. Di sini, saya menggunakan tiga hardware wallet, jadi setiap "*Keystore*" sesuai dengan salah satu di antaranya. Sekarang kita akan mengonfigurasinya.


Saya mulai dengan Passport Core. Pada tab "*Keystore 1*", saya memilih opsi "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Pada Passport, buka akun yang ingin Anda gunakan, lalu pilih "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport akan menampilkan kode QR animasi yang berisi informasi kunci publiknya.

Di Sparrow, pilih "*Scan...*" di sebelah "*Passport*" dan pindai kode QR animasi tersebut dengan webcam komputer Anda. Periksa sidik jari (fingerprint) kunci utama yang ditampilkan Sparrow terhadap yang ditampilkan oleh Passport, lalu impor keystore-nya.

Xpub Passport Anda kini telah diimpor. Ulangi prosedur yang sesuai untuk Ledger Flex dan Trezor Model One.


Untuk Ledger Flex, saya memilih "*Keystore 2*", lalu klik "*Connected Hardware Wallet*". Pastikan Ledger terhubung ke komputer, dalam keadaan terbuka kuncinya (unlocked), dan aplikasi Bitcoin sedang terbuka.


![Image](assets/fr/15.webp)


Kemudian klik tombol "*Scan...*".


![Image](assets/fr/16.webp)


Di sebelah nama hardware wallet Anda, klik "*Import Keystore*".


![Image](assets/fr/17.webp)


Penanda tangan kedua kini telah terdaftar dengan benar di Sparrow Wallet.


![Image](assets/fr/18.webp)


Saya mengulangi persis prosedur yang sama dengan Trezor One untuk menyelesaikan konfigurasi Multisig.


![Image](assets/fr/19.webp)


Dalam konfigurasi saya, kita tidak membahas kasus ini, tetapi jika Anda ingin menyertakan sebuah tanda tangan melalui dompet perangkat lunak di Sparrow (hot wallet) dalam Multisig Anda, cukup klik tombol "*New or Imported Software Wallet*".


Sekarang setelah semua perangkat penanda tangan Anda diimpor ke Sparrow Wallet, Anda dapat menyelesaikan pembuatan Multisig dengan mengklik "*Apply*".


![Image](assets/fr/20.webp)


Pilih kata sandi yang kuat untuk mengamankan akses ke dompet Sparrow Wallet Anda. Kata sandi ini melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah.


Ingatlah untuk menyimpan kata sandi ini di tempat yang aman, seperti pengelola kata sandi (password manager), agar tidak hilang.


![Image](assets/fr/21.webp)


## Membuat cadangan dompet Multisig


Sekarang kita akan menyimpan *Output Script Descriptor* pada media independen dan menyimpan beberapa salinannya.


*Descriptor* ini berisi semua xpub dalam dompet Multisig Anda, serta jalur turunan (derivation path) yang digunakan untuk menghasilkan kunci-kunci tersebut. Ingat apa yang kita lihat di Bagian 1: untuk memulihkan dompet Multisig, Anda harus memiliki **semua** frasa mnemonic, atau hanya jumlah minimum yang dibutuhkan untuk mencapai ambang batas (threshold) tanda tangan. Namun, dalam kasus terakhir, penting juga untuk memiliki **xpub** dari penanda tangan yang tidak dimiliki. *Descriptor* berisi semua xpub Multisig Anda.


Jika ini belum jelas, ingatlah saja hal berikut: untuk mengambil kembali sebuah Multisig, Anda membutuhkan jumlah minimum frasa mnemonic untuk setiap Hardware Wallet yang digunakan, tergantung pada ambang batas (dalam kasus saya: 2 frasa), serta *Descriptor*-nya.


*Descriptor* ini tidak berisi kunci privat, hanya kunci publik. Ini berarti bahwa deskriptor tidak memberikan akses ke dana. Oleh karena itu, deskriptor tidak sekritis frasa mnemonic, yang memberikan akses penuh ke bitcoin Anda. Risiko dengan *Descriptor* hanya berkaitan dengan kerahasiaan: jika terjadi pembobolan, pihak ketiga dapat mengamati semua transaksi Anda, tetapi tidak dapat membelanjakan dana Anda.


Saya sangat menyarankan Anda untuk membuat beberapa salinan *Descriptor* ini, dan menyimpannya bersama setiap perangkat penanda tangan pada Multisig Anda. Sebagai contoh, dalam kasus saya, saya mencetak *Descriptor* di atas kertas dan menyimpan satu salinan bersama Passport, satu lagi bersama Trezor, dan satu bersama Ledger. Saya juga menyimpan *Descriptor* ini sebagai file PDF pada tiga USB stick, masing-masing disimpan bersama salah satu hardware wallet. Dengan cara ini, saya memaksimalkan peluang saya untuk tidak pernah kehilangan *Descriptor* ini, dan saya yakin memiliki dua salinan (satu fisik dan satu digital) dengan setiap perangkat.


Setelah dompet Multisig Anda dibuat, Sparrow secara otomatis memberi Anda *Descriptor* ini. Klik tombol "*Save PDF...*" untuk menyimpannya baik sebagai teks maupun sebagai kode QR.


![Image](assets/fr/22.webp)


Anda kemudian dapat mencetak PDF ini dan menyalinnya ke USB stick Anda.


![Image](assets/fr/23.webp)


Passport menggunakan konfigurasi multisig yang diimpor oleh Sparrow untuk menampilkan dan memverifikasi informasi kunci yang relevan selama alur pemasangan (pairing) QR dan penandatanganan. Simpan *Descriptor* secara independen: deskriptor ini tetap penting untuk memulihkan dompet jika salah satu penanda tangan tidak tersedia.


Selain menyimpan *Descriptor*, jangan lupa untuk memberikan perhatian khusus pada penyimpanan frasa mnemonic untuk setiap perangkat penanda tangan Anda. Jika Anda baru memulai, saya sangat menyarankan Anda untuk merujuk pada tutorial lain ini untuk mempelajari cara menyimpan dan mengelolanya dengan benar:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sebelum menerima bitcoin pertama Anda di Multisig, **saya sangat menyarankan Anda untuk melakukan uji pemulihan kosong (empty recovery test)**. Catat beberapa informasi referensi, seperti alamat penerima pertama, lalu reset hardware wallet Anda selagi dompet masih kosong. Selanjutnya, coba pulihkan dompet Multisig Anda pada Hardware Wallet menggunakan cadangan kertas frasa mnemonic Anda, lalu di Sparrow menggunakan *Descriptor*. Periksa apakah alamat pertama yang dihasilkan setelah pemulihan sesuai dengan yang Anda catat sebelumnya. Jika sesuai, Anda dapat yakin bahwa cadangan kertas Anda dapat diandalkan.


Untuk mempelajari lebih lanjut tentang cara melakukan uji pemulihan, saya sarankan Anda merujuk pada tutorial lain ini:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Menerima bitcoin di Multisig Anda


Dompet Anda kini siap untuk menerima bitcoin. Di Sparrow, klik tab "*Receive*".


![Image](assets/fr/30.webp)


Sebelum menggunakan alamat yang dihasilkan oleh Sparrow Wallet, luangkan waktu untuk memeriksanya langsung di layar hardware wallet Anda. Ini akan memastikan bahwa alamat tersebut tidak diubah, dan bahwa perangkat Anda memegang kunci privat yang dibutuhkan untuk membelanjakan dana yang terkait. Ini membantu melindungi Anda dari sejumlah vektor serangan.


Untuk melakukannya, klik "*Display Address*" untuk menampilkan alamat pada Trezor atau Ledger Anda, saat terhubung melalui kabel.


![Image](assets/fr/31.webp)


Dengan Passport, pilih akun multisig dan pilih "*Verify Address*". Pindai kode QR dari alamat penerimaan yang ditampilkan oleh Sparrow. Passport akan mengonfirmasi di layarnya apakah alamat tersebut milik dompet multisig.


Periksa apakah alamat yang ditampilkan pada setiap hardware wallet sesuai persis dengan yang ada di Sparrow Wallet. Sebaiknya lakukan ini tepat sebelum membagikan alamat kepada pembayar, untuk memastikan integritasnya.


Anda kemudian dapat menetapkan "*Label*" pada alamat ini, untuk menunjukkan asal bitcoin yang diterima. Ini adalah cara yang baik untuk mengatur pengelolaan UTXO Anda.


![Image](assets/fr/34.webp)


Setelah ini diverifikasi, Anda dapat menggunakan alamat tersebut untuk menerima bitcoin.


![Image](assets/fr/35.webp)


## Mengirim bitcoin dengan Multisig Anda


Sekarang setelah Anda menerima satoshi pertama Anda di dompet Multisig, Anda juga dapat membelanjakannya! Di Sparrow, buka tab "*Send*" untuk membuat transaksi baru.


![Image](assets/fr/36.webp)


Jika Anda ingin menggunakan *Coin Control*, yaitu memilih secara manual UTXO yang ingin Anda belanjakan, buka tab "*UTXOs*". Pilih UTXO yang ingin Anda belanjakan, lalu klik "*Send Selected*". Anda akan secara otomatis diarahkan ke tab "*Send*", dengan UTXO yang sudah terisi otomatis.


![Image](assets/fr/37.webp)


Masukkan alamat tujuan. Beberapa alamat dapat ditambahkan dengan mengklik "*+ Add*".


![Image](assets/fr/38.webp)


Tambahkan "*Label*" untuk menjelaskan tujuan pengeluaran ini, agar lebih mudah melacak transaksi Anda.


![Image](assets/fr/39.webp)


Masukkan jumlah yang akan dikirim ke alamat yang dipilih.


![Image](assets/fr/40.webp)


Sesuaikan tarif biaya (fee rate) sesuai dengan kondisi jaringan saat ini. Misalnya, kunjungi [Mempool.space](https://Mempool.space/) untuk memilih tingkat biaya yang sesuai.


Setelah memeriksa semua parameter transaksi, klik "*Create Transaction*".


![Image](assets/fr/41.webp)


Jika Anda puas dengan semuanya, klik "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Di bagian bawah layar, Anda akan melihat bahwa Sparrow sedang menunggu 2 tanda tangan. Ini normal: dompet yang digunakan di sini adalah Multisig 2-of-3.


![Image](assets/fr/43.webp)


Saya mulai menandatangani dengan Passport saya. Di Sparrow, klik "*Show QR*" untuk menampilkan PSBT (*Partially Signed Bitcoin Transaction*) sebagai kode QR animasi. Pada Passport, pilih akun multisig dan pilih "*Sign with QR Code*", lalu pindai kode QR yang ditampilkan oleh Sparrow.


Di layar Hardware Wallet Anda, periksa dengan saksama parameter transaksi: alamat penerima, jumlah yang dikirim, dan biaya. Setelah transaksi dikonfirmasi, validasi untuk melanjutkan ke penandatanganan.


Setelah Anda menyetujui transaksi, Passport akan menampilkan PSBT yang telah ditandatangani sebagai kode QR animasi. Di Sparrow, klik "*Scan QR*" dan pindai kode-kode tersebut dengan webcam Anda. Tanda tangan Passport kemudian akan ditambahkan. Sekarang saya menggunakan Ledger untuk tanda tangan kedua yang dibutuhkan: saya menghubungkan dan membuka kuncinya, lalu klik "*Sign*" di Sparrow.


![Image](assets/fr/48.webp)


Klik "*Sign*" di sebelah nama Hardware Wallet Anda.


![Image](assets/fr/49.webp)


Saat pertama kali Anda menggunakan Ledger Anda dengan Multisig ini, Sparrow akan meminta Anda untuk memverifikasi kunci publik tambahan (xpub) dari para co-signer. Seperti halnya dengan Passport, langkah ini mencegah Anda menandatangani secara membabi buta di kemudian hari. Untuk memvalidasi informasi ini, bandingkan xpub yang ditampilkan pada layar Ledger dengan yang diberikan langsung oleh hardware wallet Anda yang lain.


![Image](assets/fr/50.webp)


Periksa alamat penerima, jumlah yang ditransfer, dan biaya transaksi, lalu tandatangani transaksi tersebut.


![Image](assets/fr/51.webp)


Tekan layar untuk menandatangani.


![Image](assets/fr/52.webp)


Sparrow kini memiliki dua tanda tangan yang dibutuhkan untuk mengeluarkan dana dari dompet Multisig. Periksa transaksi sekali lagi, dan jika semuanya baik-baik saja, klik "*Broadcast Transaction*" untuk menyiarkannya ke jaringan.


![Image](assets/fr/53.webp)


Anda akan menemukan transaksi ini di tab "*Transactions*" pada Sparrow Wallet.


![Image](assets/fr/54.webp)


Selamat, Anda kini tahu cara menyiapkan dan menggunakan dompet multi-tanda tangan di Sparrow. Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda meninggalkan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial Anda. Terima kasih telah membagikannya!


Untuk melangkah lebih jauh, saya sarankan Anda merujuk pada tutorial ini tentang metode lain untuk meningkatkan keamanan dompet Bitcoin Anda, passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
</content>
