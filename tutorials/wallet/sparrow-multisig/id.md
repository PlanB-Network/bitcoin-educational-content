---
name: Sparrow - Multisig
description: Membuat portofolio multi-tanda tangan di Sparrow
---
![cover](assets/cover.webp)



Wallet multi-tanda tangan (sering disebut Multisig) adalah struktur Bitcoin wallet yang membutuhkan beberapa tanda tangan kriptografi dari kunci yang berbeda untuk mengesahkan pengeluaran. Berbeda dengan wallet konvensional (singlesig), di mana satu kunci pribadi sudah cukup untuk membuka kunci UTXO, Multisig didasarkan pada model m-of-n: dari total n kunci yang terhubung dengan wallet, m di antaranya harus ikut menandatangani setiap transaksi.

Mekanisme ini memungkinkan kontrol portofolio dibagi antara beberapa entitas atau perangkat. Misalnya, dalam konfigurasi 2 dari 3, tiga set kunci independen dihasilkan, tetapi hanya dua yang dibutuhkan untuk melepaskan dana. Arsitektur seperti ini secara signifikan mengurangi risiko yang muncul akibat kebocoran atau hilangnya satu kunci: pencuri yang hanya memiliki satu kunci tidak bisa menguras wallet, dan pengguna yang kehilangan satu kunci tetap bisa mengakses dananya dengan dua kunci yang tersisa.



![Image](assets/fr/01.webp)

Tapi, keamanan yang lebih baik ini datang dengan tingkat kompleksitas yang lebih tinggi. Menyiapkan wallet Multisig berarti kamu harus mengamankan beberapa seedphrase (satu untuk setiap faktor tanda tangan) dan kunci publik yang diperluas (xpub). Misalnya, kalau kamu pakai Multisig 2-of-3 wallet, untuk bisa memulihkan wallet kamu harus punya ketiga seedphrase, atau setidaknya dua dari tiga seedphrase itu. Tapi kalau kamu cuma punya dua dari tiga seedphrase, kamu juga butuh akses ke tiga xpub, karena tanpa itu kamu nggak bisa mengambil public key yang dibutuhkan untuk mengakses bitcoin yang dilindungi.

Sebagai rangkuman, untuk memulihkan portofolio Multisig, kamu harus:

- Punya semua seedphrase yang terkait dengan setiap faktor tanda tangan; atau
- Punya jumlah minimum seedphrase sesuai ambang batas untuk bisa menandatangani, dan juga akses ke xpub dari semua faktor untuk mengambil kunci publik yang dibutuhkan.

![Image](assets/fr/02.webp)

Manajemen cadangan portofolio Multisig difasilitasi oleh Output Script Descriptors, yang mengelompokkan semua data publik yang dibutuhkan untuk mengakses dana. Tapi, fungsi ini belum sepenuhnya tersedia di semua perangkat lunak manajemen portofolio.

Multisig sangat cocok untuk pengguna Bitcoin yang mencari keamanan lebih tinggi atau pengelolaan dana secara kolektif—seperti perusahaan, komunitas, keluarga, atau individu yang memegang bitcoin dalam jumlah besar. Skema ini juga bisa dipakai untuk membuat sistem tata kelola yang terdesentralisasi, misalnya dengan membagi otoritas penandatanganan di antara beberapa manajer atau anggota tim.

Dalam tutorial ini, kita akan belajar cara membuat dan menggunakan wallet multisignature klasik dengan Sparrow Wallet. Kalau kamu ingin membuat portofolio multisignature yang dilengkapi dengan timelock (kunci waktu), aku sarankan pakai Liana.

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prasyarat



Untuk tutorial ini, saya akan menunjukkan kepada kamu cara membuat Multisig dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Kalau kamu belum menginstal perangkat lunak ini, silakan lakukan sekarang. Jika kamu memerlukan bantuan, kami juga memiliki tutorial terperinci tentang cara mengonfigurasi Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Untuk menyiapkan Wallet multi-tanda tangan, kamu memerlukan dompet perangkat keras yang berbeda. Untuk Multisig 2-de-3, misalnya, kamu dapat menggunakan :

- Trezor Model Satu;
- Ledger Flex;
- Coldcard MK3.

![Image](assets/fr/03.webp)

Sebaiknya kamu gunakan model hardware wallet yang berbeda dalam konfigurasi Multisig kamu. Ini penting supaya kalau ada satu model yang mengalami masalah serius, hal itu nggak memengaruhi keamanan Multisig secara keseluruhan. Selain itu, kamu juga bisa memanfaatkan keunggulan khusus dari masing-masing perangkat. Misalnya, dalam konfigurasi aku:

- Trezor Model One sepenuhnya bersifat open-source, jadi proses pembuatan seed bisa diverifikasi. Tapi karena tidak dilengkapi Secure Element, perangkat ini tetap rentan terhadap serangan fisik.
- Ledger Flex di sisi lain menggunakan firmware eksklusif yang tidak bisa diverifikasi, tapi punya Secure Element yang memberikan perlindungan fisik sangat baik.
- Coldcard dilengkapi dengan Secure Element dan kodenya bisa diperiksa. Ini jadi pilihan menarik untuk konfigurasi kita karena menawarkan fitur verifikasi yang nggak tersedia di model lain.

Sebelum mengonfigurasi wallet Multisig kamu, pastikan setiap hardware wallet sudah disiapkan dengan benar (pembuatan dan penyimpanan seedphrase, serta penentuan PIN). Untuk panduan lengkapnya, kamu bisa baca tutorial kami untuk masing-masing hardware wallet, misalnya:

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Seperti yang akan kita lihat nanti di tutorial ini, kamu juga bisa menambahkan faktor yang tidak terhubung dengan hardware wallet ke dalam konfigurasi Multisig kamu, yaitu kunci privat yang disimpan di PC kamu. Metode ini jelas kurang aman dibandingkan penggunaan penuh hardware wallet, tapi bisa jadi relevan untuk situasi tertentu. Misalnya, dalam konfigurasi Multisig 2-dari-3, kamu bisa memilih dua hardware wallet dan satu software wallet.

## Membuat portofolio Multisig

Buka Sparrow Wallet, klik tab "*File*", lalu pilih "*New Wallet*".

![Image](assets/fr/04.webp)

Tetapkan nama untuk portofolio multisignature kamu, lalu klik "*Buat Wallet*" untuk mengonfirmasi.

![Image](assets/fr/05.webp)

Pada menu tarik-turun "*Jenis Polis*", pilih opsi "*Tanda Tangan Ganda*".

![Image](assets/fr/06.webp)

Di sudut kanan atas, sekarang kamu bisa menentukan jumlah total kunci dalam Multisig kamu, serta jumlah penandatangan yang dibutuhkan untuk mengesahkan pengeluaran. Dalam contoh aku, konfigurasinya adalah skema 2-dari-3.

![Image](assets/fr/07.webp)

Di bagian bawah jendela, Sparrow Wallet menampilkan tiga keystore. Masing-masing mewakili satu set kunci. Di sini aku menggunakan tiga hardware wallet, jadi setiap keystore terhubung dengan salah satunya. Sekarang kita akan mengonfigurasinya.

Saya mulai dengan Coldcard. Pada tab "*Keystore 1*", saya memilih opsi "*Airgapped Hardware Wallet*".

![Image](assets/fr/08.webp)

Pada Coldcard, setelah perangkat dibuka kuncinya, aku masuk ke menu "*Settings*", kemudian ke "*Multisig Wallets*".

![Image](assets/fr/09.webp)

Menu ini memungkinkan kamu mengelola portofolio Multisig yang berpartisipasi dalam Coldcard. Aku ingin membuat yang baru, jadi aku memilih "*Export XPUB*".

![Image](assets/fr/10.webp)

Untuk kolom "*Nomor akun*", jika kamu hanya mengelola satu akun, kamu bisa mengosongkannya dan langsung memvalidasi dengan menekan tombol konfirmasi.

![Image](assets/fr/11.webp)

Coldcard kemudian akan generate file yang berisi xpub kamu, yang disimpan pada kartu Micro SD.

![Image](assets/fr/12.webp)

Masukkan Micro SD ini ke dalam komputermu. Pada Sparrow Wallet, klik tombol "*Import File...*" di samping "*Coldcard Multisig*", kemudian pilih file yang dibuat oleh Coldcard pada kartu.

![Image](assets/fr/13.webp)

Xpub kamu telah berhasil diimpor. Sekarang kita akan mengulangi prosedur ini dengan dua dompet perangkat keras lainnya.

![Image](assets/fr/14.webp)

Untuk Ledger Flex, saya memilih "*Keystore 2*", kemudian klik "*Connected Hardware Wallet*". Pastikan Ledger terhubung ke komputer, tidak terkunci, dan aplikasi Bitcoin terbuka.

![Image](assets/fr/15.webp)

Kemudian, klik tombol "*Pindai...*".

![Image](assets/fr/16.webp)

Di samping nama portofolio perangkat keras milikmu, klik "*Import Keystore*".

![Image](assets/fr/17.webp)

Penandatangan kedua sekarang sudah terdaftar dengan benar di Sparrow Wallet.

![Image](assets/fr/18.webp)

Aku mengulangi prosedur yang persis sama dengan Trezor One untuk menyelesaikan konfigurasi Multisig.

![Image](assets/fr/19.webp)

Dalam konfigurasi yang aku lakukan, kita nggak membahas kasus ini, tapi kalau kamu ingin menambahkan tanda tangan lewat software wallet di Sparrow (hot wallet) ke dalam Multisig kamu, cukup klik tombol New or Imported Software Wallet.

Sekarang, setelah semua perangkat penandatangan kamu diimpor ke Sparrow Wallet, kamu bisa menyelesaikan pembuatan Multisig dengan klik Apply.

![Image](assets/fr/20.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet Wallet kamu. Kata sandi ini melindungi kunci publik, alamat, label, dan riwayat transaksimu dari akses yang tidak sah.

Ingatlah untuk menyimpan kata sandi ini di tempat yang aman, seperti pengelola kata sandi, untuk menghindari kehilangannya.

![Image](assets/fr/21.webp)



## Mencadangkan portofolio Multisig

Sekarang kita akan menyimpan *Output Script Descriptor* di Coldcard (ini hanya berlaku kalau kamu menggunakan Coldcard dalam konfigurasi Multisig), dan yang paling penting, kita juga akan membuat cadangannya di media yang terpisah.

*Descriptor* berisi semua xpub dalam portofolio Multisig kamu, serta jalur turunan yang digunakan untuk menghasilkan kunci. Ingat yang sudah kita bahas di Bagian 1: untuk memulihkan portofolio Multisig, kamu harus punya semua seedphrase, atau setidaknya jumlah minimum yang dibutuhkan sesuai ambang tanda tangan. Tapi dalam kasus kedua, kamu juga harus punya xpub dari penandatangan yang hilang. Descriptor ini berisi semua xpub dari konfigurasi Multisig kamu.

Kalau masih belum jelas, ingat hal ini: untuk memulihkan Multisig, kamu perlu jumlah minimum seedphrase dari setiap hardware wallet yang digunakan (dalam kasus aku: 2 seedphrase), serta Descriptor-nya.

*Descriptor* ini tidak berisi kunci privat, hanya kunci publik. Artinya, Descriptor tidak bisa digunakan untuk mengakses dana. Jadi, meskipun penting, Descriptor tidak sepenting seedphrase, karena seedphrase memberi akses penuh ke bitcoin kamu. Risiko dari Descriptor hanya terkait dengan kerahasiaan: kalau sampai bocor, pihak ketiga bisa melihat semua transaksi kamu, tapi tetap nggak bisa mengakses dana kamu.

Aku sangat menyarankan kamu membuat beberapa salinan Descriptor ini dan menyimpannya di setiap perangkat penandatangan dalam konfigurasi Multisig kamu. Misalnya, dalam kasus aku, aku mencetak Descriptor di atas kertas dan menyimpan satu salinan di Coldcard, satu di Trezor, dan satu di Ledger. Aku juga menyimpan Descriptor ini sebagai file PDF di tiga flashdisk, masing-masing disimpan bersama setiap hardware wallet. Dengan cara ini, aku memaksimalkan peluang untuk tidak pernah kehilangan Descriptor ini, dan punya dua salinan (satu fisik dan satu digital) untuk tiap perangkat.

Setelah portofolio Multisig kamu dibuat, Sparrow secara otomatis memberikan Descriptor ini. Klik tombol Save PDF... untuk menyimpannya, baik dalam bentuk teks maupun kode QR.

![Image](assets/fr/22.webp)

Kemudian kamu dapat mencetak PDF ini dan menyalinnya ke stik USB Anda.

![Image](assets/fr/23.webp)

Kita juga akan mendaftarkan Descriptor ini ke Coldcard (kalau kamu menggunakannya dalam konfigurasi kamu). Langkah ini memungkinkan Coldcard untuk memverifikasi bahwa setiap transaksi yang nantinya ditandatangani benar-benar sesuai dengan wallet asli: xpub yang tepat, format alamat yang benar, dan jalur turunan yang sesuai. Tanpa Descriptor yang diimpor ini, Coldcard tidak bisa memastikan apakah alamat tujuan sudah dibajak atau apakah PSBT telah dimodifikasi.

Inilah yang membuat Coldcard begitu menarik dalam konfigurasi Multisig: Coldcard memberikan lapisan pemeriksaan tambahan terhadap jenis serangan canggih tertentu yang nggak bisa dilakukan oleh hardware wallet lain (tentu saja dengan catatan kamu menggunakannya untuk menandatangani).

Di Sparrow, buka menu Settings, lalu klik Export....

![Image](assets/fr/24.webp)

Di samping opsi "*Coldcard Multisig*", klik "*Export File...*" dan simpan file teks ke kartu Micro SD.

![Image](assets/fr/25.webp)

Kemudian masukkan kartu ke dalam Coldcard. Buka menu "*Settings*", lalu "*Multisig Wallets*", dan pilih "*Import from SD*".

![Image](assets/fr/26.webp)

Pilih file yang sesuai dan konfirmasikan impor.

![Image](assets/fr/27.webp)

Klik pada nama Multisig yang baru kamu impor.

![Image](assets/fr/28.webp)

Periksa parameter konfigurasi Multisig, lalu konfirmasikan pendaftaran.

![Image](assets/fr/29.webp)

Multisig kamu sekarang sudah tersimpan dengan benar di Coldcard. Kalau kamu punya beberapa Coldcard dalam konfigurasi Multisig yang sama, ulangi langkah ini untuk masing-masing perangkat.

Selain menyimpan *Descriptor,* jangan lupa juga untuk memberi perhatian khusus pada penyimpanan seedphrase dari setiap perangkat penandatangan kamu. Kalau kamu masih baru dalam hal ini, aku sangat menyarankan kamu membaca tutorial lainnya untuk belajar cara menyimpan dan mengelolanya dengan benar.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sebelum kamu menerima bitcoin pertama di Multisig, aku sangat menyarankan kamu untuk melakukan tes pemulihan kosong. Catat beberapa informasi penting seperti alamat penerimaan pertama, lalu reset hardware wallet kamu selagi wallet masih kosong. Setelah itu, coba pulihkan Multisig wallet kamu di hardware wallet menggunakan cadangan kertas seedphrase, lalu di Sparrow menggunakan Descriptor. Pastikan alamat pertama yang dihasilkan setelah pemulihan sama persis dengan yang kamu catat. Kalau hasilnya cocok, berarti cadangan kertas kamu bisa diandalkan.

Untuk belajar lebih lanjut tentang cara melakukan tes pemulihan, aku sarankan kamu baca tutorial berikut:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Terima bitcoin di Multisig Anda

Sekarang wallet kamu siap untuk menerima bitcoin. Di Sparrow, klik pada tab "*Receive*".

![Image](assets/fr/30.webp)

Sebelum menggunakan alamat yang dihasilkan oleh Sparrow Wallet, luangkan waktu untuk memverifikasinya langsung di layar hardware wallet kamu. Ini penting untuk memastikan bahwa alamat tersebut tidak dimodifikasi, dan bahwa perangkat kamu memang memiliki private key yang diperlukan untuk membelanjakan dana terkait. Langkah ini membantu melindungi kamu dari berbagai jenis serangan.

Untuk melakukannya, klik Display Address agar alamat muncul di layar Trezor atau Ledger kamu saat perangkat terhubung dengan kabel.

![Image](assets/fr/31.webp)

Dengan Coldcard, verifikasi ini bisa dilakukan tanpa perlu interaksi apa pun dengan Sparrow. Cukup buka menu Address Explorer, lalu pilih Multisig kamu di bagian paling bawah.

![Image](assets/fr/32.webp)

Kemudian kamu akan melihat alamat penerimaan yang dihasilkan oleh Multisig.

![Image](assets/fr/33.webp)

Periksa apakah alamat yang ditampilkan di setiap hardware wallet sama persis dengan yang muncul di Sparrow Wallet. Disarankan untuk melakukan langkah ini sebelum kamu membagikan alamat tersebut ke pihak yang akan membayar, supaya kamu bisa memastikan integritasnya.

Setelah itu, kamu bisa menambahkan label pada alamat tersebut untuk menandai asal bitcoin yang diterima. Ini adalah cara yang bagus untuk membantu mengatur dan mengelola UTXO kamu.

![Image](assets/fr/34.webp)

Setelah diverifikasi, kamu dapat menggunakan Address untuk menerima bitcoin.

![Image](assets/fr/35.webp)

## Mengirim bitcoin dengan Multisig Anda

Sekarang setelah kamu menerima sats pertama Anda di Multisig Wallet, kamu dapat membelanjakannya juga! Di Sparrow, buka tab "*Kirim*" untuk membuat transaksi baru.

![Image](assets/fr/36.webp)

Kalau kamu ingin menggunakan Coin Control, yaitu memilih secara manual UTXO yang mau kamu belanjakan, buka tab UTXOs. Pilih UTXO yang ingin kamu gunakan, lalu klik Kirim Terpilih. Kamu akan otomatis diarahkan ke tab Kirim dengan UTXO yang sudah terisi sebelumnya.

![Image](assets/fr/37.webp)

Masukkan Address yang dituju. Beberapa alamat dapat ditambahkan dengan mengeklik "*+ Tambah*".

![Image](assets/fr/38.webp)

Tambahkan "*Label*" untuk menjelaskan tujuan dari pengeluaran ini, untuk memudahkan pelacakan transaksimu.

![Image](assets/fr/39.webp)

Masukkan jumlah yang akan dikirim ke Address yang dipilih.

![Image](assets/fr/40.webp)

Sesuaikan tingkat pengisian daya sesuai dengan kondisi jaringan saat ini. Sebagai contoh, lihat [Mempool.space] (https://Mempool.space/) untuk memilih tingkat pengisian daya yang sesuai.

Setelah memeriksa semua parameter transaksi, klik "*Buat Transaksi*".

![Image](assets/fr/41.webp)

Kalau kamu puas dengan semuanya, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/42.webp)

Di bagian bawah layar, kamu akan melihat bahwa Sparrow sedang menunggu 2 tanda tangan. Ini normal, karena wallet yang kamu gunakan di sini adalah Multisig 2-dari-3.

![Image](assets/fr/43.webp)

Aku mulai melakukan penandatanganan dengan Coldcard. Untuk melakukan ini, aku memasukkan kartu Micro SD ke dalam komputer, lalu klik "*Save Transaction*".

![Image](assets/fr/44.webp)

Ada tiga cara untuk mengirim transaksi yang akan ditandatangani ke hardware wallet kamu, lalu mengambil hasilnya kembali ke Sparrow. Pertama, menggunakan kartu microSD, seperti yang akan kita lakukan di sini untuk Coldcard. Kedua, melalui koneksi kabel, yang akan kita pakai untuk tanda tangan kedua (Ledger dan Trezor). Terakhir, kamu bisa menggunakan komunikasi lewat kode QR untuk perangkat yang dilengkapi kamera, seperti Coldcard Q, Jade Plus, atau Passport V2.

Setelah PSBT (*Partially Signed Bitcoin Transaction*) disimpan dalam Micro SD, aku memasukkannya ke dalam Coldcard MK3, kemudian memilih menu "*Siap untuk Ditandatangani*".



![Image](assets/fr/45.webp)

Pada layar Hardware Wallet kamu, periksa dengan cermat parameter transaksi: Address penerima, jumlah yang dikirim, dan biaya. Setelah transaksi dikonfirmasi, validasi untuk melanjutkan ke penandatanganan.

![Image](assets/fr/46.webp)

Kemudian kembalikan Micro SD ke komputermu, dan klik "*Muat Transaksi*" di Sparrow. Pilih PSBT yang ditandatangani oleh Coldcard dari file milikmu.

![Image](assets/fr/47.webp)

Kamu dapat melihat bahwa tanda tangan Coldcard telah ditambahkan. Sekarang aku akan menggunakan perangkat kedua, dalam hal ini Ledger, untuk melakukan tanda tangan kedua yang diperlukan. Aku menghubungkannya, membukanya, lalu klik "*Sign*" pada Sparrow.

![Image](assets/fr/48.webp)

Klik "*Tanda Tangan*" di samping nama Hardware Wallet kamu.

![Image](assets/fr/49.webp)

Saat pertama kali kamu menggunakan Ledger dengan Multisig ini, Sparrow akan meminta kamu untuk memverifikasi kunci publik yang diperluas (xpub) dari para penandatangan lain. Sama seperti pada Coldcard, langkah ini berguna untuk mencegah kamu menandatangani transaksi secara membabi buta di kemudian hari. Untuk memvalidasi informasi ini, bandingkan xpub yang ditampilkan di layar Ledger dengan yang ditampilkan langsung oleh hardware wallet kamu yang lain.

![Image](assets/fr/50.webp)

Periksa Address penerima, jumlah yang ditransfer dan biaya transaksi, lalu tandatangani transaksi.

![Image](assets/fr/51.webp)

Tekan layar untuk menandatangani.

![Image](assets/fr/52.webp)

Sparrow sekarang memiliki dua tanda tangan yang dibutuhkan untuk melepaskan dana dari portofolio Multisig. Periksa transaksi untuk terakhir kalinya, dan jika semuanya berjalan dengan baik, klik "*Broadcast Transaction*" untuk menyiarkannya melalui jaringan.

![Image](assets/fr/53.webp)

Kamu akan menemukan transaksi ini di tab "*Transactions*" Sparrow Wallet.

![Image](assets/fr/54.webp)

Selamat, sekarang kamu sudah tahu cara mengatur dan menggunakan wallet multisignature di Sparrow. Kalau kamu merasa tutorial ini bermanfaat, aku bakal sangat berterima kasih kalau kamu mau kasih jempol hijau di bawah ini. Jangan ragu juga buat membagikan artikel ini di media sosial kamu. Terima kasih sudah ikut berbagi!

Untuk melangkah lebih jauh, aku sarankan kamu baca tutorial berikut tentang metode lain untuk meningkatkan keamanan Bitcoin wallet kamu, yaitu passphrase BIP39:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
