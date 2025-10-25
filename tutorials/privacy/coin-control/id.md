---
name: Coin Control
description: Mulailah dengan Coin Control, alat penting untuk melindungi privasi Anda di Bitcoin
---
![cover](assets/cover.webp)


*Tutorial ini diimpor dari [sebuah pelajaran dari Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Pendahuluan



Kekuatan protokol Bitcoin dijamin oleh konsep-konsep kunci yang sederhana. Di antaranya, transparansi menonjol: semua transaksi Bitcoin bersifat publik dan mudah diverifikasi oleh siapa pun. Meskipun fitur ini merupakan tonggak penting dari protokol, karena mencegah penipuan dan menjamin keaslian dana, hal ini juga dapat menjadi tantangan bagi kerahasiaan. **Pernahkah Anda bertanya-tanya apakah transparansi sebesar ini bisa mengganggu privasi Anda?**



Anda harus melakukannya. Meskipun mengumpulkan Satoshi non-kyc cukup mudah, privasi Anda paling berisiko pada tahap pembelanjaan.



### Apa yang terjadi ketika Anda menggunakan UTXO



Membelanjakan Bitcoin bukan sekadar transfer nilai kepada orang lain.



Dengan menggunakan salah satu UTXO Anda, Anda harus memenuhi persyaratan yang diberlakukan untuk transparansi protokol, karena Anda berkewajiban untuk membuktikan bahwa Anda memiliki dana tersebut. Oleh karena itu, Anda bertanggung jawab untuk :




- mengekspos kunci publik Anda;
- menghasilkan tanda tangan digital.



Oleh karena itu, waktu pembelanjaan adalah yang paling penting: **Membelanjakan Bitcoin adalah tindakan yang harus dilakukan secara sadar dan dengan kontrol sebanyak mungkin**.



## Kontrol Coin



Dalam protokol Bitcoin, item seperti _account_ atau _unit moneter_ tidak ada. Konsep UTXO dijelaskan dengan sangat baik dalam kursus berikut ini, yang sangat saya rekomendasikan:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dengan Bitcoin, apa yang Anda kumpulkan dan kemudian dibelanjakan adalah unit akun kecil atau besar yang diukur dalam Satoshi, yang diwakili oleh 'hasil transaksi yang tidak terpakai', yaitu **UTXO**, yang juga disebut 'koin'. Ketika Anda menggunakan UTXO untuk membuat transaksi, UTXO tersebut akan dihancurkan sepenuhnya dan UTXO lain akan dibuat sebagai gantinya.



Dompet Perangkat Lunak dikembangkan untuk membuat pilihan ini secara otomatis, menggunakan koin yang dipilih secara "acak", dengan menggunakan algoritma tertentu yang disediakan oleh protokol. Satu-satunya kriteria yang dipenuhi oleh algoritma ini adalah untuk memenuhi jumlah yang dibutuhkan untuk pembelanjaan.



Mereka dapat menggabungkan UTXO dari berbagai usia, atau mendukung pengeluaran yang terbaru atau "tertua", tergantung pada algoritme yang dipilih oleh pengembang. Dompet Perangkat Lunak terbaik, juga berencana untuk memberikan pilihan penting kepada pengguna.



Manual `Coin Control`, yang juga dapat Anda temukan sebagai `Coin Selection`, adalah fitur dari beberapa Dompet Perangkat Lunak yang memungkinkan Anda untuk **memilih secara manual UTXO yang akan dibelanjakan saat Anda melakukan transaksi**.



Misalkan kita memiliki Wallet dengan 3 UTXO masing-masing 21.000, 42.000 dan 63.000 Satoshi.



![img](assets/en/01.webp)



Jika Anda harus mengeluarkan 24.000 Sats dan membiarkan algoritme melakukan pemilihan otomatis, Software Wallet yang baik mungkin memilih untuk menggabungkan UTXO 1 + UTXO 2 untuk membayar biaya Sats dan Miner sebesar 24k, menciptakan sisa yang kembali ke Address internal dari Wallet awal.



![img](assets/en/02.webp)



Setelah transaksi, situasi baru di Wallet, dengan hanya menghitung UTXO, dapat diringkas sebagai berikut.



![img](assets/en/03.webp)



Namun demikian, dengan perangkat lunak yang tepat dan kesadaran Anda, Anda dapat membuat pilihan yang berbeda, dalam beberapa hal, pilihan yang lebih tepat. Contohnya, dengan hanya memilih UTXO2 (dari 42.000 Sats).



![img](assets/en/04.webp)



Dengan situasi akhir di Wallet Anda, pada level UTXO, yang terlihat berbeda dari sebelumnya.



![img](assets/en/05.webp)



## Mengapa coin control manual?



![img](assets/en/06.webp)



Pada dua contoh di atas, saldo sebenarnya sama yaitu `108.280 Sats`. Setelah menghabiskan 24.000 Sats, tanpa pemilihan manual kita akan memiliki 2 UTXO di Wallet; dengan kontrol manual Coin kita akan memiliki total 3.



Pertanyaan yang mungkin kita ajukan pada diri kita adalah sebagai berikut: **mengapa melakukan semua ini?** Ada, atau mungkin ada, beberapa alasan mengapa kita tidak menggunakan `UTXO1` **dan semuanya menjadi dasar mengapa—pada saat membelanjakan—mengaktifkan coin control manual adalah salah satu praktik terbaik yang harus diikuti**.



Dengan memilih UTXO, Anda dapat mengutamakan beberapa aspek daripada aspek lainnya. Pilihannya benar-benar tergantung pada tujuan yang ingin Anda capai.



### Privasi



Salah satu keuntungan utama, apabila menyangkut kontrol Coin secara manual, adalah **privasi yang lebih besar bagi pembelanja**. Mari kita ambil contoh: pengeluaran 24.000 Satoshi _tanpa pemilihan Coin secara manual_. Karena Blockchain dari Bitcoin adalah catatan publik, pengamat luar dapat menyatakan, tanpa keraguan sedikit pun, bahwa input `UTXO1 dari 21.000 Sats` dan `UTXO2 dari 42.000 Sats`, serta sisanya, `UTXO5 dari 38.280 Sats` **ketiganya adalah milik pengguna yang sama**.



Sebaliknya, dengan memilih `UTXO2` secara manual, `UTXO1` tetap dicadangkan sepenuhnya, berada di set UTXO menunggu untuk digunakan pada waktu yang lebih tepat.



`UTXO1` dapat berasal dari sumber KYC, seperti pembayaran yang diterima dalam Exchange untuk barang dan jasa, sedangkan UTXO lainnya tidak. Mencampur UTXO-kyc dengan yang lain yang lebih rahasia akan membahayakan anonimitas dana non-kyc.



**Dana KYC akan secara tak terhindarkan menelusuri kembali identitas pembayar. Jika itu dompetmu, apakah kamu ingin seorang pengamat eksternal dapat menelusuri identitasmu dengan kepastian yang begitu mutlak?**



Kemudian cobalah untuk mempertimbangkan bahwa Dompet yang mengimplementasikan pemilihan UTXO secara manual, misalnya, memungkinkan **pemisahan satu atau beberapa UTXO**, sebuah fungsi yang dapat digunakan ketika situasi seperti itu muncul.



Meskipun saya yakin bahwa dana KYC harus disimpan di Wallet yang terpisah dari Bitcoin yang dibeli tanpa kyc, jika ini adalah kasus Anda, pemisahan beberapa alamat Anda adalah bantuan utama, yang dapat Anda manfaatkan dengan mempelajari cara memilih input pengeluaran secara manual.



### Menghemat biaya



Memilih UTXO yang tepat untuk melakukan pengeluaran, **memungkinkan optimalisasi biaya**. Sekali lagi mulai dari contoh awal kita, Software Wallet memilih dua UTXO untuk menutupi biaya yang harus dikeluarkan. Dua UTXO menyiratkan dua tanda tangan yang akan ditampilkan ke jaringan. Oleh karena itu, transaksi tersebut memiliki "bobot" yang lebih besar dalam hal vBytes.



Sebaliknya, dengan menggunakan kontrol manual Coin, Anda dapat memilih hanya satu yang cukup untuk menutupi jumlah tersebut, sehingga menghemat biaya dengan mengurangi "bobot" transaksi.



Pada saat biaya tinggi, tetapi Anda terpaksa menghabiskan Bitcoin On-Chain (misalnya, untuk membuka saluran Lightning Network), pada saat itulah kontrol Coin menjadi insentif ekonomi yang tepat untuk digunakan.



### Agregasi sisa-sisa



Ketika Anda melakukan pembayaran dan menggunakan Bitcoin On-Chain, kemungkinan menerima kembalian hampir selalu menjadi sebuah kepastian. Setiap sisa uang kembalian itu sendiri merupakan kehilangan privasi yang kecil, karena hal ini menunjukkan kepada jaringan (dan terutama kepada penerima pembayaran) sebuah Address milik Anda yang dapat dikaitkan dengan input sumber Anda.



Dengan mempertimbangkan bahwa Wallet HD terbaik generate alamat khusus untuk sisa-sisa, Anda dapat dengan mudah mengenalinya dan "memisahkan" semua sisa-sisa dari berbagai transaksi yang dilakukan; ketika mereka telah mencapai jumlah tertentu, Anda dapat memilihnya secara manual dan mengkonsolidasikannya, atau menukar ke Lightning Network (metode pilihan saya) dan memprosesnya untuk mendapatkan kembali privasi yang hilang dalam pembelanjaan.



### Pengeluaran dari Cold Wallet



Cold Wallet adalah instrumen yang dapat digunakan untuk mendapatkan tingkat keamanan yang baik, untuk menyimpan sejumlah dana untuk disisihkan dalam jangka waktu yang lama. Namun, kejadian tak terduga dapat terjadi, sehingga muncul kebutuhan untuk mendapatkan tabungan dan memenuhi beberapa pengeluaran tak terduga.



Saya tidak tahu berapa banyak yang dapat berbagi pendekatan saya, tetapi saran saya adalah **jangan pernah melakukan pengeluaran langsung dari Cold Wallet, untuk menghindari menerima kembalian di antara alamat yang sama**. Belajarlah untuk memilih secara manual UTXO yang diperlukan untuk menutupi pengeluaran, mentransfernya ke Wallet Hot dan menyiapkan transaksi Anda dari yang terakhir. Setiap kembaliannya, Anda dapat mengirimkannya kembali ke Cold Wallet Address (jika jumlahnya mencukupi), menggunakannya untuk pengeluaran lain, atau tetap memisahkannya seperti yang baru saja kita lihat.



## Presentasi praktis


Setelah pengenalan teknis tentang `mengapa`, mari kita lihat bagaimana mempraktikkan kontrol manual Coin dengan perangkat lunak yang berbeda, desktop dan seluler. Kami akan selalu menggunakan Wallet BIP39 yang sama, yang diimpor ke masing-masing alat yang dipilih, untuk menunjukkan kepada Anda perbedaan kecil di antara keduanya.



## Desktop Wallet



### Sparrow



Jika Anda menggunakan Sparrow, buka Wallet Anda dan pilih _UTXOs_ dari menu di sebelah kiri. Anda akan melihat daftar semua UTXO yang terkait dengan Wallet Anda.



Cukup klik dengan mouse pada salah satu dari mereka dan kemudian pilih _Kirim Terpilih_. Sparrow juga menunjukkan kepada Anda total yang tersedia untuk dibelanjakan setelah pemilihan, tepat di sebelah perintah. Secara grafis Sparrow menunjukkan kepada Anda UTXO yang dipilih dengan menyorotnya dengan warna biru.



![img](assets/en/07.webp)



Anda juga dapat memilih lebih dari satu. Bantu diri Anda sendiri dengan tombol _CTRL_ untuk memilih UTXO yang tidak berdekatan dalam daftar.



![img](assets/en/08.webp)



Setelah memilih UTXO secara manual, Anda dapat mulai membuat transaksi, dan Sparrow akan menunjukkan kepada Anda dengan baik, secara grafis, bagaimana transaksi tersebut terbentuk.



![img](assets/en/09.webp)



#### Pemisahan UTXO



Memisahkan dana berarti "mengunci" dana tersebut di dalam Wallet sehingga tidak dapat digunakan sebagai input pada sebuah transaksi. Sparrow memungkinkan fungsi ini, yang selalu diakses dari menu _UTXOs_: Anda meletakkan mouse di atas UTXO yang akan "dikunci" dan klik tombol kanan mouse. Di antara fitur-fitur prosedur ini akan muncul _Freeze UTXO_. Dengan cara inilah Anda dapat memisahkan Koin dengan dompet Sparrow.



![img](assets/en/29.webp)



### Electrum



Jika desktop Wallet Anda adalah Electrum, Anda harus mengetahui bahwa Anda dapat memilih UTXO secara manual dari menu _Addresses_ atau menu _Coins_. Pada kedua menu tersebut, pemilihan dilakukan dengan mengarahkan mouse ke UTXO yang diinginkan dan memilih _Add to Coin control_ setelah mengklik kanan.



![img](assets/en/10.webp)



Bahkan dengan perangkat lunak ini, Anda dapat memilih lebih dari satu UTXO, dibantu dengan tombol __CTRL_ pada keyboard Anda jika mereka tidak berdekatan satu sama lain.



![img](assets/en/11.webp)



Secara grafis Electrum akan menunjukkan kepada Anda pilihan dengan menyorot UTXO yang dipilih di Green, sementara sebuah bar muncul di bagian bawah, disorot dengan warna yang sama, yang menunjukkan saldo yang tersedia setelah kontrol Coin.



![img](assets/en/12.webp)



Setelah Anda memilih output, atau keluaran, Anda dapat membuat transaksi Anda seperti yang biasa Anda lakukan dari menu _Send_.



#### Pemisahan UTXO



Electrum menyediakan fungsi ini dengan masuk ke menu _Coins_, di mana Anda akan memilih UTXO tertentu dan kemudian memilih _Freeze_ dengan klik kanan. Anda dapat "membekukan" Address bahkan tanpa dana dari menu _Addresses_, atau "Coin" untuk tidak membelanjakannya.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk memungkinkan Anda untuk memilih UTXO secara manual dari menu utama setelah menu tersebut terbuka. Luncurkan Nunchuk dan klik _Lihat koin_.



![img](assets/en/13.webp)



Ini akan membuka jendela yang berisi semua UTXO di Wallet Anda, di mana Anda dapat memilih satu atau lebih dengan mengaktifkan tanda centang di samping setiap jumlah. Setelah menentukan pilihan, lanjutkan dengan _Buat transaksi_.



![img](assets/en/14.webp)



Setelah itu Anda dapat memasukkan tujuan Address dan mengatur jumlah dan biaya.



![img](assets/en/15.webp)



#### Pemisahan UTXO



Demi kelengkapan, Nunchuk juga memungkinkan di antara fitur-fiturnya, untuk memisahkan satu (atau lebih) UTXO dan melakukannya dengan dua cara yang berbeda. Akses menu _Lihat koin_ dan pilih secara manual dari daftar koin. Kemudian klik menu _Lebih_ di kanan bawah: daftar opsi akan muncul, di mana Anda dapat memilih _Kunci koin_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Anda juga dapat mengklik di tempat yang disediakan untuk UTXO, untuk mengakses jendela _Rincian koin_. Di sini, perintah untuk mengunci/membuka kunci UTXO yang bersangkutan muncul di sudut kanan atas.



![img](assets/en/41.webp)



### Aplikasi Blockstream



Desktop Blockstream App, yang sebelumnya dikenal sebagai Green, memungkinkan Anda untuk membuat pilihan Coin ketika Anda sudah mulai membangun transaksi. Oleh karena itu, buka Wallet Anda dan klik _Kirim_.



![img](assets/en/16.webp)



Tempelkan Address yang dituju ke dalam bidang yang sesuai, lalu pilih _Pemilihan Coin manual_.



![img](assets/en/17.webp)



Ini akan membuka jendela di mana Anda bisa memilih satu atau beberapa koin UTXO. Pada contoh di bawah ini, kita telah memilih dua koin. Setelah itu, konfirmasikan pilihan Anda dengan mengklik _Konfirmasi Pilihan Coin_.



![img](assets/en/18.webp)



Tetapkan jumlah dan biaya, lalu lanjutkan transaksi Anda seperti biasa.



![img](assets/en/19.webp)



⚠️ N.B. Dalam menu _Coins_ pada Green terdapat item _Lock_/_Unlock_ yang menandakan kemungkinan untuk memisahkan UTXO. Fitur ini hanya diaktifkan di akun yang disebut Multisig; fitur ini juga diaktifkan hanya dengan memilih UTXO dalam jumlah yang sangat kecil, mendekati ambang batas `Dust`.



## Ponsel Wallet



Dompet juga dapat dipilih dari ponsel, yang memungkinkan UTXO dipilih secara manual. Mari kita lihat Blue Wallet sebagai contoh pertama.



### Biru Wallet



Jika Anda adalah pengguna Wallet ini, buka dan klik untuk masuk ke layar kontrol yang terkait dengan salah satu Dompet Anda. Untuk mengakses manual kontrol Coin, Anda harus masuk ke fase pembelanjaan, lalu klik _Kirim_.



![img](assets/en/21.webp)



Pada layar berikutnya, pilih menu yang ditunjukkan oleh tiga titik di sudut kanan atas. Jendela tarik-turun akan terbuka dengan serangkaian perintah. Pilih yang terakhir: kontrol Koin.



![img](assets/en/22.webp)



Pada titik ini, Blue Wallet menunjukkan semua UTXO Anda. Selain jumlah, mereka dibedakan secara grafis dengan warna yang berbeda.



![img](assets/en/27.webp)



Pilih UTXO yang akan dipilih, kemudian pilih _Use Coin_.



![img](assets/en/23.webp)



Wallet biru akan membawa Anda kembali ke jendela _Send_ untuk melanjutkan transaksi. Sesuaikan jumlah dan biaya, setelah itu pilih _Next_.



![img](assets/en/24.webp)



Pada titik ini Anda dapat mengakhiri transaksi, seperti yang biasa Anda lakukan.



#### Pemisahan UTXO



Wallet biru juga memungkinkan Anda untuk memisahkan UTXO, membuatnya tidak tersedia untuk dibelanjakan, yang merupakan fungsi yang baik untuk Wallet dari perangkat seluler. Anda mengakses kontrol Coin dengan prosedur yang baru saja dijelaskan dan, setelah memilih UTXO, pilih _Freeze_ daripada _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Versi mobile Nunchuk juga menyediakan kemampuan bagi pengguna untuk melakukan kontrol Coin. Jika Anda menggunakan aplikasi ini dari ponsel, buka aplikasi ini dan masuk ke menu _Wallet_. Dari sana pilih _Lihat koin_.



![img](assets/en/30.webp)



Pada jendela tempat daftar UTXO muncul, klik _Pilih_.



![img](assets/en/38.webp)



Fungsi pemilihan muncul di samping setiap UTXO. Seperti pada versi desktop, pemilihan manual pada Nunchuk mobile dilakukan dengan mencentang kotak kecil di sebelah jumlah. Layar menunjukkan jumlah UTXO yang dipilih dan jumlah total yang tersedia. Setelah selesai, klik simbol ₿ di pojok kiri bawah, yang merupakan perintah untuk mulai membangun transaksi.



![img](assets/en/31.webp)



Sekarang Anda dapat menyelesaikan transaksi, memilih jumlah yang ingin Anda bayarkan dan klik _Continue_.



![img](assets/en/32.webp)



Lanjutkan seperti yang biasa Anda lakukan, tempelkan tujuan Address, deskripsi, dan sesuaikan pengaturan biaya.



#### Pemisahan UTXO



Anda juga dapat memisahkan UTXO dengan Nunchuk seluler. Akses jendela daftar koin khusus dan pilih panah di samping UTXO yang ingin Anda pisahkan.



![img](assets/en/42.webp)



Anda akan melihat ruang yang disediakan untuk _Rincian koin_, di mana Anda dapat memilih _Kunci koin ini_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper adalah Wallet terakhir yang akan kita lihat dalam panduan ini. Kami melihat fungsinya diterapkan pada kontrol Coin dengan Wallet single-sig, meskipun penggunaan seperti itu bukanlah tujuan dari aplikasi yang sangat khusus ini. Setelah menyiapkan Keeper di ponsel Anda, luncurkan dan buka Wallet yang berisi sejumlah dana. Di tengah layar utama, klik _Lihat Semua Koin_.



![img](assets/en/34.webp)



Keeper menunjukkan gambaran umum UTXO. Untuk mengakses layar pemilihan, klik _Pilih Untuk Dikirim_.



![img](assets/en/35.webp)



Anda bisa memilih koin dengan mencentangnya dengan mengklik perintah yang sesuai. Setelah selesai, klik _Kirim_.



![img](assets/en/36.webp)



Bitcoin Keeper membawa Anda langsung ke menu _Send_, di mana Anda dapat membuat transaksi dengan UTXO yang dipilih.



![img](assets/en/37.webp)



## Hardware Wallet



Setiap Dompet Perangkat Lunak yang terlihat dalam panduan ini dapat menjadi Interface khusus jam tangan ke salah satu Dompet Perangkat Keras Anda. Ini berarti kontrol Coin untuk perangkat penandatanganan offline dilakukan dengan langkah-langkah yang terlihat sejauh ini.



### Rekomendasi umum



Kontrol Coin adalah praktik yang sangat efektif untuk memilih input transaksi Anda. Pemilihan secara manual bahkan lebih efisien jika, ketika membeli/menerima dana Anda, Anda telah melabeli sumber Satoshi Anda dengan baik. Jika Anda ingin mempelajari teknik ini dengan baik, saya sarankan tutorial berikut ini:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kami telah berbicara sebelumnya tentang `pemisahan sisa-sisa`. Jika Anda ingin mengunci sisa-sisa untuk diproses nanti dan mendapatkan kembali privasi (menukar pada Layer 2), Anda harus berhati-hati dalam memberi label setiap kali Anda menerimanya. Dari Dompet Perangkat Lunak yang terlihat sejauh ini, hanya Electrum yang secara grafis mewarnai sisa UTXO untuk membuatnya terlihat sekilas. Yang lainnya, seperti Sparrow, menunjukkan kepada anda rantai di jalur derivasi dari masing-masing UTXO (`m/84'/0'/0'/1/11`).



Untuk menerapkan teknik ini secara efektif, ingatlah untuk selalu menambahkan deskripsi pada kembalian yang Anda terima: orang yang Anda kirimi dana (pembayaran, tutorial, atau lainnya), mengetahui Address yang terkait dengan kembalian tersebut dan mengetahui bahwa itu adalah milik Anda, karena berasal dari transaksi yang Anda lakukan bersama!