---
name: Sparrow Wallet - Multisig
description: Membuat portofolio multi-tanda tangan di Sparrow
---
![cover](assets/cover.webp)



Wallet multi-tanda tangan (sering disebut "*Multisig*") adalah struktur Bitcoin Wallet yang membutuhkan beberapa tanda tangan kriptografi, dari kunci yang berbeda, untuk mengesahkan pengeluaran. Tidak seperti Wallet konvensional ("*singlesig*"), di mana satu kunci pribadi cukup untuk membuka kunci UTXO, Multisig didasarkan pada model *m-of-n*: dari kunci _n_ yang terkait dengan Wallet, _m_ harus ikut menandatangani setiap transaksi.



Mekanisme ini memungkinkan kontrol portofolio dibagi antara beberapa entitas atau perangkat. Sebagai contoh, dalam konfigurasi 2 dari 3, tiga set kunci independen dihasilkan, tetapi hanya dua yang diperlukan untuk melepaskan dana. Arsitektur ini secara drastis mengurangi risiko yang terkait dengan kompromi atau hilangnya sebuah kunci: pencuri yang memiliki akses ke satu kunci tidak dapat mengosongkan Wallet, dan pengguna yang kehilangan satu kunci masih dapat mengakses dananya dengan dua kunci yang tersisa.



![Image](assets/fr/01.webp)



Akan tetapi, keamanan yang lebih baik ini memiliki kompleksitas yang lebih tinggi. Menyiapkan Multisig Wallet membutuhkan pengamanan beberapa frasa Mnemonic (satu per faktor tanda tangan) dan kunci publik yang diperluas ("*xpub*"). Memang, jika Anda menggunakan Multisig 2-of-3 Wallet, untuk mendapatkan Wallet Anda harus memiliki ketiga frasa Mnemonic, atau setidaknya dua dari ketiga frasa tersebut. Akan tetapi, jika Anda hanya memiliki dua dari tiga frasa tersebut, Anda juga membutuhkan akses ke tiga *xpub*, yang tanpanya Anda tidak dapat mengambil public key yang dibutuhkan untuk mengakses bitcoin yang dilindungi.



Sebagai rangkuman, untuk memulihkan portofolio Multisig, Anda harus :




- Atau akses semua frasa Mnemonic yang terkait dengan setiap faktor tanda tangan;
- Memiliki jumlah minimum frasa Mnemonic yang dibutuhkan oleh ambang batas untuk dapat menandatangani, dan juga memiliki akses ke xpubs dari semua faktor untuk mengambil kunci publik yang diperlukan.



![Image](assets/fr/02.webp)



Manajemen cadangan portofolio Multisig ini difasilitasi oleh *Output Script Descriptors*, yang mengelompokkan semua data publik yang diperlukan untuk mengakses dana. Namun, fungsi ini belum diimplementasikan di semua perangkat lunak manajemen portofolio.



Multisig sangat cocok untuk para pengguna bitcoin yang mencari keamanan yang lebih baik atau pengelolaan dana secara kolektif: perusahaan, asosiasi, keluarga, atau pengguna individu yang memiliki bitcoin dalam jumlah yang signifikan. Ini dapat digunakan untuk membuat skema tata kelola yang terdesentralisasi, misalnya, untuk mendistribusikan otoritas penandatanganan di antara beberapa manajer atau anggota tim.



Dalam tutorial ini, kita akan mempelajari cara membuat dan menggunakan multisignature klasik Wallet dengan **Sparrow Wallet**. Jika Anda ingin membuat portofolio multisignature yang disesuaikan dengan kunci waktu, saya sarankan untuk menggunakan Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prasyarat



Untuk tutorial ini, saya akan menunjukkan kepada Anda cara membuat Multisig dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Jika Anda belum menginstal perangkat lunak ini, silakan lakukan sekarang. Jika Anda memerlukan bantuan, kami juga memiliki tutorial terperinci tentang cara mengonfigurasi Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Untuk menyiapkan Wallet multi-tanda tangan, Anda memerlukan dompet perangkat keras yang berbeda. Untuk Multisig 2-de-3, misalnya, Anda dapat menggunakan :




- Trezor Model Satu;
- Ledger Flex;
- Kartu Dingin MK3.



![Image](assets/fr/03.webp)



Sebaiknya gunakan model Hardware Wallet yang berbeda dalam konfigurasi Multisig Anda. Hal ini memastikan bahwa jika model tertentu mengalami masalah serius, hal itu tidak akan memengaruhi keamanan Multisig Anda secara keseluruhan. Selain itu, ini memungkinkan Anda untuk mendapatkan keuntungan dari keunggulan spesifik masing-masing perangkat. Misalnya, dalam konfigurasi saya:





- Trezor Model One sepenuhnya merupakan sumber terbuka, yang memungkinkan untuk memverifikasi generasi seed. Namun, karena tidak dilengkapi dengan Secure Element, ia tetap rentan terhadap serangan fisik;





- Di sisi lain, Ledger Flex mendapatkan keuntungan dari firmware eksklusif yang tidak dapat diverifikasi, tetapi dilengkapi dengan Secure Element yang menawarkan perlindungan fisik yang sangat baik;





- Coldcard dilengkapi dengan Elemen Aman dan kodenya dapat dicari. Ini adalah pilihan yang menarik untuk konfigurasi kami, karena menawarkan fitur verifikasi yang tidak tersedia pada model lain.



Sebelum mengonfigurasi Multisig Wallet Anda, pastikan bahwa setiap Hardware Wallet telah dikonfigurasi dengan benar (pembuatan dan penyimpanan Mnemonic, definisi PIN). Untuk petunjuk terperinci, Anda dapat membaca tutorial kami untuk setiap Hardware Wallet, misalnya :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Seperti yang akan kita lihat nanti dalam tutorial ini, Anda juga dapat mengintegrasikan ke dalam konfigurasi Multisig Anda sebuah faktor yang tidak terkait dengan Hardware Wallet, tetapi kunci privatnya disimpan pada PC Anda. Metode ini jelas kurang aman dibandingkan dengan penggunaan eksklusif dompet perangkat keras, tetapi mungkin relevan untuk kasus-kasus tertentu. Sebagai contoh, untuk Multisig 2-de-3, Anda dapat memilih dua dompet perangkat keras dan satu Software Wallet.



## Membuat portofolio Multisig



Buka Sparrow Wallet, klik tab "*File*", lalu pilih "*New Wallet*".



![Image](assets/fr/04.webp)



Tetapkan nama untuk portofolio multisignature Anda, lalu klik "*Buat Wallet*" untuk mengonfirmasi.



![Image](assets/fr/05.webp)



Pada menu tarik-turun "*Jenis Polis*", pilih opsi "*Tanda Tangan Ganda*".



![Image](assets/fr/06.webp)



Di sudut kanan atas, Anda sekarang dapat menentukan jumlah total kunci dalam Multisig Anda, serta jumlah penandatangan bersama yang diperlukan untuk mengesahkan pengeluaran. Dalam contoh saya, ini adalah skema 2-dari-3.



![Image](assets/fr/07.webp)



Pada bagian bawah jendela, Sparrow Wallet menampilkan tiga "*Keystore*". Masing-masing mewakili satu set kunci. Di sini, saya menggunakan tiga portofolio perangkat keras, jadi setiap "*Keystore*" berhubungan dengan salah satunya. Sekarang kita akan mengkonfigurasinya.



Saya mulai dengan Coldcard. Pada tab "*Keystore 1*", saya memilih opsi "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Pada Coldcard, setelah perangkat dibuka kuncinya, saya masuk ke menu "*Settings*", kemudian ke "*Multisig Wallets*".



![Image](assets/fr/09.webp)



Menu ini memungkinkan Anda mengelola portofolio Multisig yang berpartisipasi dalam Coldcard. Saya ingin membuat yang baru, jadi saya memilih "*Export XPUB*".



![Image](assets/fr/10.webp)



Untuk kolom "*Nomor akun*", jika Anda hanya mengelola satu akun, Anda bisa mengosongkannya dan langsung memvalidasi dengan menekan tombol konfirmasi.



![Image](assets/fr/11.webp)



Coldcard kemudian akan generate file yang berisi xpub Anda, yang disimpan pada kartu Micro SD.



![Image](assets/fr/12.webp)



Masukkan Micro SD ini ke dalam komputer Anda. Pada Sparrow Wallet, klik tombol "*Import File...*" di samping "*Coldcard Multisig*", kemudian pilih file yang dibuat oleh Coldcard pada kartu.



![Image](assets/fr/13.webp)



Xpub Anda telah berhasil diimpor. Sekarang kita akan mengulangi prosedur ini dengan dua dompet perangkat keras lainnya.



![Image](assets/fr/14.webp)



Untuk Ledger Flex, saya memilih "*Keystore 2*", kemudian klik "*Connected Hardware Wallet*". Pastikan Ledger terhubung ke komputer, tidak terkunci, dan aplikasi Bitcoin terbuka.



![Image](assets/fr/15.webp)



Kemudian, klik tombol "*Pindai...*".



![Image](assets/fr/16.webp)



Di samping nama portofolio perangkat keras Anda, klik "*Import Keystore*".



![Image](assets/fr/17.webp)



Penandatangan kedua sekarang sudah terdaftar dengan benar di Sparrow Wallet.



![Image](assets/fr/18.webp)



Saya mengulangi prosedur yang persis sama dengan Trezor One untuk menyelesaikan konfigurasi Multisig.



![Image](assets/fr/19.webp)



Dalam konfigurasi saya, kami tidak membahas kasus ini, tetapi jika Anda ingin menyertakan tanda tangan melalui Software Wallet di Sparrow (Hot Wallet) di dalam Multisig Anda, cukup klik tombol "*New or Imported Software Wallet*".



Sekarang, setelah semua perangkat tanda tangan Anda diimpor ke dalam Sparrow Wallet, Anda bisa menyelesaikan pembuatan Multisig dengan mengeklik "*Apply*".



![Image](assets/fr/20.webp)



Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet Wallet Anda. Kata sandi ini melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah.



Ingatlah untuk menyimpan kata sandi ini di tempat yang aman, seperti pengelola kata sandi, untuk menghindari kehilangannya.



![Image](assets/fr/21.webp)



## Mencadangkan portofolio Multisig



Sekarang kita akan menyimpan *Output Script Descriptor* pada Coldcard (ini hanya berlaku untuk pengguna dengan Coldcard pada Multisig mereka), dan yang terpenting, kita akan menyimpan cadangannya pada media independen.



*Descriptor* berisi semua xpub dalam portofolio Multisig Anda, serta jalur turunan yang digunakan untuk generate kunci. Ingat apa yang kita lihat di Bagian 1: untuk memulihkan portofolio Multisig, Anda harus memiliki **semua** frasa Mnemonic, atau hanya jumlah minimum yang diperlukan untuk mencapai ambang tanda tangan. Namun, dalam kasus terakhir, Anda juga harus memiliki ** xpubs** dari penandatangan yang hilang. *Descriptor* berisi semua xpubs Multisig Anda.



Jika hal ini belum jelas, ingatlah ini: untuk mengambil Multisig, Anda memerlukan jumlah minimum frasa Mnemonic untuk setiap Hardware Wallet yang digunakan, tergantung pada ambang batas (dalam kasus saya: 2 frasa), serta *Descriptor*.



*Descriptor* ini tidak mengandung kunci pribadi, hanya kunci publik. Ini berarti tidak memberikan akses ke dana. Oleh karena itu, ini tidak sepenting frasa Mnemonic, yang memberikan akses penuh ke bitcoin Anda. Resiko dengan *Descriptor* hanya terkait dengan kerahasiaan: jika terjadi pembobolan, pihak ketiga dapat mengamati semua transaksi Anda, tetapi tidak dapat menggunakan dana Anda.



Saya sangat menyarankan agar Anda membuat beberapa salinan *Descriptor* ini, dan menyimpannya di setiap perangkat penandatanganan pada Multisig Anda. Sebagai contoh, dalam kasus saya, saya mencetak *Descriptor* di atas kertas dan menyimpan satu salinan di Coldcard, satu salinan di Trezor, dan satu salinan di Ledger. Saya juga menyimpan *Descriptor* ini sebagai file PDF pada tiga stik USB, masing-masing disimpan di salah satu portofolio perangkat keras. Dengan cara ini, saya memaksimalkan peluang saya untuk tidak pernah kehilangan *Descriptor* ini, dan saya yakin memiliki dua salinan (satu fisik dan satu digital) untuk setiap perangkat.



Setelah portofolio Multisig Anda dibuat, Sparrow secara otomatis memberikan Anda *Descriptor* ini. Klik tombol "*Save PDF...*" untuk menyimpannya baik sebagai teks maupun kode QR.



![Image](assets/fr/22.webp)



Anda kemudian dapat mencetak PDF ini dan menyalinnya ke stik USB Anda.



![Image](assets/fr/23.webp)



Kami juga akan mendaftarkan *Descriptor* ini di Coldcard (jika Anda menggunakannya dalam konfigurasi Anda). Hal ini akan memungkinkan Coldcard untuk memverifikasi bahwa setiap transaksi yang ditandatangani nantinya sesuai dengan Wallet asli: xpubs yang benar, format Address yang benar, jalur turunan yang benar... Tanpa *Descriptor* yang diimpor ini, Coldcard tidak dapat mengonfirmasi bahwa alamat Exchange tidak dibajak atau bahwa PSBT tidak dirusak.



Inilah yang membuat Coldcard begitu menarik pada Multisig: Coldcard menawarkan pemeriksaan tambahan terhadap serangan canggih tertentu, yang tidak dapat dilakukan oleh dompet perangkat keras lainnya (dengan catatan, tentu saja, Anda menggunakannya untuk menandatangani).



Di Sparrow, akses menu "*Settings*", lalu klik "*Export...*".



![Image](assets/fr/24.webp)



Di samping opsi "*Coldcard Multisig*", klik "*Export File...*" dan simpan file teks ke kartu Micro SD.



![Image](assets/fr/25.webp)



Kemudian masukkan kartu ke dalam Coldcard. Buka menu "*Settings*", lalu "*Multisig Wallets*", dan pilih "*Import from SD*".



![Image](assets/fr/26.webp)



Pilih file yang sesuai dan konfirmasikan impor.



![Image](assets/fr/27.webp)



Klik pada nama Multisig yang baru Anda impor.



![Image](assets/fr/28.webp)



Periksa parameter konfigurasi Multisig, lalu konfirmasikan pendaftaran.



![Image](assets/fr/29.webp)



Multisig Anda sekarang tersimpan dengan benar dalam Coldcard Anda. Jika Anda memiliki beberapa Coldcard dalam Multisig yang sama, ulangi prosedur ini untuk setiap Coldcard.



Selain menyimpan *Descriptor*, jangan lupa memberikan perhatian khusus untuk menyimpan frasa Mnemonic untuk masing-masing perangkat tanda tangan Anda. Jika Anda baru memulai, saya sangat menyarankan agar Anda membaca tutorial lainnya untuk mempelajari cara menyimpan dan mengelolanya dengan benar:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sebelum menerima bitcoin pertama Anda di Multisig, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Catatlah beberapa informasi referensi, seperti Address yang pertama kali diterima, kemudian setel ulang dompet perangkat keras Anda saat Wallet masih kosong. Selanjutnya, coba pulihkan Multisig Wallet Anda pada Dompet Perangkat Keras menggunakan cadangan kertas frase Mnemonic Anda, kemudian pada Sparrow menggunakan *Descriptor*. Periksa apakah Address pertama yang dihasilkan setelah pemulihan sesuai dengan yang Anda tuliskan. Jika cocok, Anda dapat yakin bahwa cadangan kertas Anda dapat diandalkan.



Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, saya sarankan Anda membaca tutorial lain ini:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Terima bitcoin di Multisig Anda



Wallet Anda sekarang siap untuk menerima bitcoin. Di Sparrow, klik pada tab "*Receive*".



![Image](assets/fr/30.webp)



Sebelum menggunakan Address yang dihasilkan oleh Sparrow Wallet, luangkan waktu untuk memeriksanya secara langsung pada layar dompet perangkat keras Anda. Hal ini akan memastikan bahwa Address belum diubah, dan bahwa perangkat Anda memiliki private key yang dibutuhkan untuk membelanjakan dana terkait. Hal ini akan membantu melindungi Anda dari sejumlah vektor serangan.



Untuk melakukan ini, klik "*Display Address*" untuk menampilkan Address pada Trezor atau Ledger Anda, ketika terhubung dengan kabel.



![Image](assets/fr/31.webp)



Dengan Coldcard, verifikasi ini dapat dilakukan tanpa interaksi apa pun dengan Sparrow. Cukup buka menu "*Address Explorer*", lalu pilih Multisig Anda di bagian paling bawah.



![Image](assets/fr/32.webp)



Anda kemudian akan melihat alamat penerimaan yang dihasilkan oleh Multisig.



![Image](assets/fr/33.webp)



Periksa apakah Address yang ditampilkan pada setiap Hardware Wallet sama persis dengan yang ada di Sparrow Wallet. Dianjurkan untuk melakukan hal ini sebelum membagikan Address kepada pembayar, untuk memastikan integritasnya.



Anda kemudian dapat memberikan "*Label*" pada Address ini, untuk menunjukkan asal bitcoin yang diterima. Ini adalah cara yang baik untuk mengatur pengelolaan UTXO Anda.



![Image](assets/fr/34.webp)



Setelah diverifikasi, Anda dapat menggunakan Address untuk menerima bitcoin.



![Image](assets/fr/35.webp)



## Mengirim bitcoin dengan Multisig Anda



Sekarang setelah Anda menerima Satss pertama Anda di Multisig Wallet, Anda dapat membelanjakannya juga! Di Sparrow, buka tab "*Kirim*" untuk membuat transaksi baru.



![Image](assets/fr/36.webp)



Jika Anda ingin menggunakan *Coin Control*, yaitu memilih secara manual UTXO yang ingin Anda belanjakan, buka tab "*UTXOs*". Pilih UTXO yang ingin Anda belanjakan, lalu klik "*Kirim Terpilih*". Anda akan secara otomatis diarahkan ke tab "*Kirim*", dengan UTXO yang sudah diisi sebelumnya.



![Image](assets/fr/37.webp)



Masukkan Address yang dituju. Beberapa alamat dapat ditambahkan dengan mengeklik "*+ Tambah*".



![Image](assets/fr/38.webp)



Tambahkan "*Label*" untuk menjelaskan tujuan dari pengeluaran ini, untuk memudahkan pelacakan transaksi Anda.



![Image](assets/fr/39.webp)



Masukkan jumlah yang akan dikirim ke Address yang dipilih.



![Image](assets/fr/40.webp)



Sesuaikan tingkat pengisian daya sesuai dengan kondisi jaringan saat ini. Sebagai contoh, lihat [Mempool.space] (https://Mempool.space/) untuk memilih tingkat pengisian daya yang sesuai.



Setelah memeriksa semua parameter transaksi, klik "*Buat Transaksi*".



![Image](assets/fr/41.webp)



Jika Anda puas dengan semuanya, klik "*Finalisasi Transaksi untuk Penandatanganan*".



![Image](assets/fr/42.webp)



Di bagian bawah layar, Anda akan melihat bahwa Sparrow sedang menunggu 2 tanda tangan. Ini normal: Wallet yang digunakan di sini adalah Multisig 2-de-3.



![Image](assets/fr/43.webp)



Saya mulai melakukan penandatanganan dengan Coldcard saya. Untuk melakukan ini, saya memasukkan kartu Micro SD ke dalam komputer, lalu klik "*Save Transaction*".



![Image](assets/fr/44.webp)



Ada 3 cara untuk mengirimkan transaksi yang akan ditandatangani ke Hardware Wallet Anda, kemudian mengambilnya dari Sparrow. Yang pertama adalah menggunakan kartu Micro SD, seperti yang akan kita lakukan di sini untuk Coldcard. Yang kedua adalah melalui koneksi kabel, yang akan kita gunakan untuk tanda tangan kedua (Ledger dan Trezor). Terakhir, Anda dapat menggunakan komunikasi kode QR, untuk perangkat yang dilengkapi kamera seperti Coldcard Q, Jade Plus atau Passport V2.



Setelah PSBT (*Partially Signed Bitcoin Transaction*) disimpan dalam Micro SD, saya memasukkannya ke dalam Coldcard MK3, kemudian memilih menu "*Siap untuk Ditandatangani*".



![Image](assets/fr/45.webp)



Pada layar Hardware Wallet Anda, periksa dengan cermat parameter transaksi: Address penerima, jumlah yang dikirim, dan biaya. Setelah transaksi dikonfirmasi, validasi untuk melanjutkan ke penandatanganan.



![Image](assets/fr/46.webp)



Kemudian kembalikan Micro SD ke komputer Anda, dan klik "*Muat Transaksi*" di Sparrow. Pilih PSBT yang ditandatangani oleh Coldcard dari file Anda.



![Image](assets/fr/47.webp)



Anda dapat melihat bahwa tanda tangan Coldcard telah ditambahkan. Sekarang saya akan menggunakan perangkat kedua, dalam hal ini Ledger, untuk melakukan tanda tangan kedua yang diperlukan. Saya menghubungkannya, membukanya, lalu klik "*Sign*" pada Sparrow.



![Image](assets/fr/48.webp)



Klik "*Tanda Tangan*" di samping nama Hardware Wallet Anda.



![Image](assets/fr/49.webp)



Pertama kali Anda menggunakan Ledger dengan Multisig ini, Sparrow akan meminta Anda untuk memverifikasi kunci publik yang diperluas (xpubs) dari penandatangan bersama. Seperti halnya dengan Coldcard, langkah ini mencegah Anda menandatangani secara membabi buta di kemudian hari. Untuk memvalidasi informasi ini, bandingkan xpub yang ditampilkan pada layar Ledger dengan yang disediakan secara langsung oleh dompet perangkat keras Anda yang lain.



![Image](assets/fr/50.webp)



Periksa Address penerima, jumlah yang ditransfer dan biaya transaksi, lalu tandatangani transaksi.



![Image](assets/fr/51.webp)



Tekan layar untuk menandatangani.



![Image](assets/fr/52.webp)



Sparrow sekarang memiliki dua tanda tangan yang dibutuhkan untuk melepaskan dana dari portofolio Multisig. Periksa transaksi untuk terakhir kalinya, dan jika semuanya berjalan dengan baik, klik "*Broadcast Transaction*" untuk menyiarkannya melalui jaringan.



![Image](assets/fr/53.webp)



Anda akan menemukan transaksi ini di tab "*Transactions*" Sparrow Wallet.



![Image](assets/fr/54.webp)



Selamat, Anda sekarang tahu cara mengatur dan menggunakan multisignature Wallet pada Sparrow. Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih telah berbagi!



Untuk melangkah lebih jauh, saya sarankan Anda membaca tutorial ini tentang metode lain untuk meningkatkan keamanan Bitcoin Wallet Anda, yaitu passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7