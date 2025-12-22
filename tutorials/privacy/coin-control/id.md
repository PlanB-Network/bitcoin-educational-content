---
name: Coin Control
description: Mulailah dengan Coin Control, alat penting untuk melindungi privasi kamu di Bitcoin
---
![cover](assets/cover.webp)


*Tutorial ini diimpor dari [sebuah pelajaran dari Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Pendahuluan



Kekuatan protokol Bitcoin dijamin oleh konsep-konsep kunci yang sederhana. Di antaranya, transparansi menonjol: semua transaksi Bitcoin bersifat publik dan mudah diverifikasi oleh siapa pun. Meskipun fitur ini merupakan tonggak penting dari protokol, karena mencegah penipuan dan menjamin keaslian dana, hal ini juga bisa menjadi tantangan bagi kerahasiaan. **Pernahkah kamu bertanya-tanya apakah transparansi sebesar ini bisa mengganggu privasi kamu?**

Kamu seharusnya memikirkannya. Meskipun mengumpulkan Satoshi non-kyc cukup mudah, privasi kamu justru paling berisiko pada tahap pembelanjaan.


### Apa yang terjadi ketika kamu menggunakan UTXO



Membelanjakan Bitcoin bukan sekadar transfer nilai kepada orang lain.

Dengan menggunakan salah satu UTXO kamu, kamu harus memenuhi persyaratan yang diberlakukan oleh transparansi protokol, karena kamu berkewajiban membuktikan bahwa kamu memang memiliki dana tersebut. Oleh karena itu, kamu bertanggung jawab untuk:

- Mengekspos kunci publik kamu;

- Menghasilkan tanda tangan digital.

Karena itu, momen pembelanjaan adalah yang paling krusial: **Membelanjakan Bitcoin adalah tindakan yang harus dilakukan secara sadar dan dengan kontrol sebanyak mungkin.**



## Kontrol Coin



Dalam protokol Bitcoin, item seperti _account_ atau _unit moneter_ tidak ada. Konsep UTXO dijelaskan dengan sangat baik dalam kursus berikut ini, yang sangat aku rekomendasikan:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dengan Bitcoin, apa yang kamu kumpulkan dan kemudian belanjakan adalah unit akun kecil atau besar yang diukur dalam Satoshi, yang direpresentasikan oleh unspent transaction output, yaitu **UTXO,** yang juga sering disebut sebagai “koin”. Ketika kamu menggunakan sebuah UTXO untuk membuat transaksi, UTXO tersebut akan dihancurkan sepenuhnya dan UTXO lain akan dibuat sebagai gantinya.

Dompet perangkat lunak dikembangkan untuk membuat pilihan ini secara otomatis, dengan menggunakan koin yang dipilih secara “acak” melalui algoritma tertentu yang disediakan oleh protokol. Satu-satunya kriteria yang dipenuhi oleh algoritma ini adalah tercapainya jumlah yang dibutuhkan untuk pembelanjaan.

Algoritma tersebut dapat menggabungkan UTXO dari berbagai usia, atau memprioritaskan pengeluaran yang paling baru atau yang “tertua”, tergantung pada algoritma yang dipilih oleh pengembang. Dompet perangkat lunak terbaik juga berencana memberikan pilihan penting ini kepada pengguna.

Manual 'Coin Control', yang juga bisa kamu temukan dengan nama 'Coin Selection', adalah fitur dari beberapa dompet perangkat lunak yang memungkinkan kamu untuk **memilih secara manual UTXO yang akan dibelanjakan saat kamu melakukan transaksi.**

Misalkan kita memiliki sebuah wallet dengan 3 UTXO masing-masing sebesar 21.000, 42.000, dan 63.000 Satoshi.


![img](assets/en/01.webp)



Jika kamu harus mengeluarkan 24.000 sats dan membiarkan algoritme melakukan pemilihan otomatis, dompet perangkat lunak yang baik kemungkinan akan memilih untuk menggabungkan UTXO 1 + UTXO 2 guna membayar 24k sats beserta biaya penambang, lalu menciptakan sisa dana yang dikembalikan ke address internal dari wallet awal.



![img](assets/en/02.webp)



Setelah transaksi, situasi baru di Wallet, dengan hanya menghitung UTXO, dapat diringkas sebagai berikut.



![img](assets/en/03.webp)



Namun demikian, dengan perangkat lunak yang tepat dan kesadaran kamu, kamu bisa membuat pilihan yang berbeda, dan dalam beberapa kasus, pilihan yang lebih tepat. Contohnya, dengan hanya memilih UTXO2 yang bernilai 42.000 sats.


![img](assets/en/04.webp)



Dengan situasi akhir di Wallet kamu, pada level UTXO, yang terlihat berbeda dari sebelumnya.



![img](assets/en/05.webp)



## Mengapa coin control manual?



![img](assets/en/06.webp)



Pada dua contoh di atas, saldo sebenarnya sama yaitu `108.280 Sats`. Setelah menghabiskan 24.000 Sats, tanpa pemilihan manual kita akan memiliki 2 UTXO di Wallet; dengan kontrol manual Coin kita akan memiliki total 3.



Pertanyaan yang mungkin kita ajukan pada diri kita adalah sebagai berikut: **mengapa melakukan semua ini?** Ada, atau mungkin ada, beberapa alasan mengapa kita tidak menggunakan `UTXO1` **dan semuanya menjadi dasar mengapa—pada saat membelanjakan—mengaktifkan coin control manual adalah salah satu praktik terbaik yang harus diikuti**.



Dengan memilih UTXO, kamu dapat mengutamakan beberapa aspek daripada aspek lainnya. Pilihannya benar-benar tergantung pada tujuan yang ingin kamu capai.



### Privasi



Salah satu keuntungan utama, apabila menyangkut kontrol Coin secara manual, adalah **privasi yang lebih besar bagi pembelanja**. Mari kita ambil contoh: pengeluaran 24.000 Satoshi _tanpa pemilihan Coin secara manual_. Karena Blockchain dari Bitcoin adalah catatan publik, pengamat luar dapat menyatakan, tanpa keraguan sedikit pun, bahwa input `UTXO1 dari 21.000 Sats` dan `UTXO2 dari 42.000 Sats`, serta sisanya, `UTXO5 dari 38.280 Sats` **ketiganya adalah milik pengguna yang sama**.



Sebaliknya, dengan memilih `UTXO2` secara manual, `UTXO1` tetap dicadangkan sepenuhnya, berada di set UTXO menunggu untuk digunakan pada waktu yang lebih tepat.



`UTXO1` dapat berasal dari sumber KYC, seperti pembayaran yang diterima dalam Exchange untuk barang dan jasa, sedangkan UTXO lainnya tidak. Mencampur UTXO-kyc dengan yang lain yang lebih rahasia akan membahayakan anonimitas dana non-kyc.



**Dana KYC akan secara tak terhindarkan menelusuri kembali identitas pembayar. Jika itu dompetmu, apakah kamu ingin seorang pengamat eksternal dapat menelusuri identitasmu dengan kepastian yang begitu mutlak?**



Kemudian cobalah untuk mempertimbangkan bahwa Dompet yang mengimplementasikan pemilihan UTXO secara manual, misalnya, memungkinkan **pemisahan satu atau beberapa UTXO**, sebuah fungsi yang dapat digunakan ketika situasi seperti itu muncul.



Meskipun aku yakin bahwa dana KYC harus disimpan di Wallet yang terpisah dari Bitcoin yang dibeli tanpa kyc, jika ini adalah kasus kamu, pemisahan beberapa alamat kamu adalah bantuan utama, yang dapat kamu manfaatkan dengan mempelajari cara memilih input pengeluaran secara manual.



### Menghemat biaya



Memilih UTXO yang tepat untuk melakukan pengeluaran, **memungkinkan optimalisasi biaya**. Sekali lagi mulai dari contoh awal kita, Software Wallet memilih dua UTXO untuk menutupi biaya yang harus dikeluarkan. Dua UTXO menyiratkan dua tanda tangan yang akan ditampilkan ke jaringan. Oleh karena itu, transaksi tersebut memiliki "bobot" yang lebih besar dalam hal vBytes.



Sebaliknya, dengan menggunakan kontrol manual Coin, kamu dapat memilih hanya satu yang cukup untuk menutupi jumlah tersebut, sehingga menghemat biaya dengan mengurangi "bobot" transaksi.



Pada saat biaya tinggi, tetapi kamu terpaksa menghabiskan Bitcoin On-Chain (misalnya, untuk membuka saluran Lightning Network), pada saat itulah kontrol Coin menjadi insentif ekonomi yang tepat untuk digunakan.



### Agregasi sisa-sisa



Ketika kamu melakukan pembayaran dan menggunakan Bitcoin On-Chain, kemungkinan menerima kembalian hampir selalu menjadi sebuah kepastian. Setiap sisa uang kembalian itu sendiri merupakan kehilangan privasi yang kecil, karena hal ini menunjukkan kepada jaringan (dan terutama kepada penerima pembayaran) sebuah Address milik kamu yang dapat dikaitkan dengan input sumber.



Dengan mempertimbangkan bahwa Wallet HD terbaik generate alamat khusus untuk sisa-sisa, kamu dapat dengan mudah mengenalinya dan "memisahkan" semua sisa-sisa dari berbagai transaksi yang dilakukan; ketika mereka telah mencapai jumlah tertentu, kamu dapat memilihnya secara manual dan mengkonsolidasikannya, atau menukar ke Lightning Network (metode pilihanku) dan memprosesnya untuk mendapatkan kembali privasi yang hilang dalam pembelanjaan.



### Pengeluaran dari Cold Wallet



Cold Wallet adalah instrumen yang dapat digunakan untuk mendapatkan tingkat keamanan yang baik, untuk menyimpan sejumlah dana untuk disisihkan dalam jangka waktu yang lama. Namun, kejadian tak terduga dapat terjadi, sehingga muncul kebutuhan untuk mendapatkan tabungan dan memenuhi beberapa pengeluaran tak terduga.



Aku tidak tahu berapa banyak yang dapat berbagi pendekatanku, tetapi saranku adalah **jangan pernah melakukan pengeluaran langsung dari Cold Wallet, untuk menghindari menerima kembalian di antara alamat yang sama**. Belajarlah untuk memilih secara manual UTXO yang diperlukan untuk menutupi pengeluaran, mentransfernya ke Wallet Hot dan menyiapkan transaksi kamu dari yang terakhir. Setiap kembaliannya, kamu dapat mengirimkannya kembali ke Cold Wallet Address (jika jumlahnya mencukupi), menggunakannya untuk pengeluaran lain, atau tetap memisahkannya seperti yang baru saja kita lihat.



## Presentasi praktis


Setelah pengenalan teknis tentang `mengapa`, mari kita lihat bagaimana mempraktikkan kontrol manual Coin dengan perangkat lunak yang berbeda, desktop dan seluler. Kami akan selalu menggunakan Wallet BIP39 yang sama, yang diimpor ke masing-masing alat yang dipilih, untuk menunjukkan kepada kamu perbedaan kecil di antara keduanya.



## Desktop Wallet



### Sparrow



Jika kamu menggunakan Sparrow, buka Wallet kamu dan pilih _UTXOs_ dari menu di sebelah kiri. kamu akan melihat daftar semua UTXO yang terkait dengan Wallet kamu.



Cukup klik dengan mouse pada salah satu dari mereka dan kemudian pilih _Kirim Terpilih_. Sparrow juga menunjukkan kepada kamu total yang tersedia untuk dibelanjakan setelah pemilihan, tepat di sebelah perintah. Secara grafis Sparrow menunjukkan kepada kamu UTXO yang dipilih dengan menyorotnya dengan warna biru.



![img](assets/en/07.webp)



Kamu juga dapat memilih lebih dari satu. Bantu diri kamu sendiri dengan tombol _CTRL_ untuk memilih UTXO yang tidak berdekatan dalam daftar.



![img](assets/en/08.webp)



Setelah memilih UTXO secara manual, kamu dapat mulai membuat transaksi, dan Sparrow akan menunjukkan kepada kamu dengan baik, secara grafis, bagaimana transaksi tersebut terbentuk.



![img](assets/en/09.webp)



#### Pemisahan UTXO



Memisahkan dana berarti "mengunci" dana tersebut di dalam Wallet sehingga tidak dapat digunakan sebagai input pada sebuah transaksi. Sparrow memungkinkan fungsi ini, yang selalu diakses dari menu _UTXOs_: kamu meletakkan mouse di atas UTXO yang akan "dikunci" dan klik tombol kanan mouse. Di antara fitur-fitur prosedur ini akan muncul _Freeze UTXO_. Dengan cara inilah kamu dapat memisahkan Koin dengan dompet Sparrow.



![img](assets/en/29.webp)



### Electrum



Jika desktop Wallet kamu adalah Electrum, kamu harus mengetahui bahwa kamu dapat memilih UTXO secara manual dari menu _Addresses_ atau menu _Coins_. Pada kedua menu tersebut, pemilihan dilakukan dengan mengarahkan mouse ke UTXO yang diinginkan dan memilih _Add to Coin control_ setelah mengklik kanan.



![img](assets/en/10.webp)



Bahkan dengan perangkat lunak ini, kamu dapat memilih lebih dari satu UTXO, dibantu dengan tombol __CTRL_ pada keyboard jika mereka tidak berdekatan satu sama lain.



![img](assets/en/11.webp)



Secara grafis Electrum akan menunjukkan kepada kamu pilihan dengan menyorot UTXO yang dipilih di Green, sementara sebuah bar muncul di bagian bawah, disorot dengan warna yang sama, yang menunjukkan saldo yang tersedia setelah kontrol Coin.



![img](assets/en/12.webp)



Setelah kamu memilih output, atau keluaran, kamu dapat membuat transaksi seperti yang biasa kamu lakukan dari menu _Send_.



#### Pemisahan UTXO



Electrum menyediakan fungsi ini dengan masuk ke menu _Coins_, di mana kamu akan memilih UTXO tertentu dan kemudian memilih _Freeze_ dengan klik kanan. Kamu dapat "membekukan" Address bahkan tanpa dana dari menu _Addresses_, atau "Coin" untuk tidak membelanjakannya.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk memungkinkanmu untuk memilih UTXO secara manual dari menu utama setelah menu tersebut terbuka. Luncurkan Nunchuk dan klik _Lihat koin_.



![img](assets/en/13.webp)



Ini akan membuka jendela yang berisi semua UTXO di Wallet kamu, di mana kamu dapat memilih satu atau lebih dengan mengaktifkan tanda centang di samping setiap jumlah. Setelah menentukan pilihan, lanjutkan dengan _Buat transaksi_.



![img](assets/en/14.webp)



Setelah itu kamu dapat memasukkan tujuan Address dan mengatur jumlah dan biaya.



![img](assets/en/15.webp)



#### Pemisahan UTXO



Demi kelengkapan, Nunchuk juga memungkinkan di antara fitur-fiturnya, untuk memisahkan satu (atau lebih) UTXO dan melakukannya dengan dua cara yang berbeda. Akses menu _Lihat koin_ dan pilih secara manual dari daftar koin. Kemudian klik menu _Lebih_ di kanan bawah: daftar opsi akan muncul, di mana kamu dapat memilih _Kunci koin_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Kamu juga dapat mengklik di tempat yang disediakan untuk UTXO, untuk mengakses jendela _Rincian koin_. Di sini, perintah untuk mengunci/membuka kunci UTXO yang bersangkutan muncul di sudut kanan atas.



![img](assets/en/41.webp)



### Aplikasi Blockstream



Desktop Blockstream App, yang sebelumnya dikenal sebagai Green, memungkinkan kamu untuk membuat pilihan Coin ketika kamu sudah mulai membangun transaksi. Oleh karena itu, buka Wallet kamu dan klik _Kirim_.



![img](assets/en/16.webp)



Tempelkan Address yang dituju ke dalam bidang yang sesuai, lalu pilih _Pemilihan Coin manual_.



![img](assets/en/17.webp)



Ini akan membuka jendela di mana kamu bisa memilih satu atau beberapa koin UTXO. Pada contoh di bawah ini, kita telah memilih dua koin. Setelah itu, konfirmasikan pilihan kamu dengan mengklik _Konfirmasi Pilihan Coin_.



![img](assets/en/18.webp)



Tetapkan jumlah dan biaya, lalu lanjutkan transaksi kamu seperti biasa.



![img](assets/en/19.webp)



⚠️ N.B. Dalam menu _Coins_ pada Green terdapat item _Lock_/_Unlock_ yang menandakan kemungkinan untuk memisahkan UTXO. Fitur ini hanya diaktifkan di akun yang disebut Multisig; fitur ini juga diaktifkan hanya dengan memilih UTXO dalam jumlah yang sangat kecil, mendekati ambang batas `Dust`.



## Ponsel Wallet



Dompet juga dapat dipilih dari ponsel, yang memungkinkan UTXO dipilih secara manual. Mari kita lihat Blue Wallet sebagai contoh pertama.



### Biru Wallet



Jika kamu adalah pengguna Wallet ini, buka dan klik untuk masuk ke layar kontrol yang terkait dengan salah satu Dompet kamu. Untuk mengakses manual kontrol Coin, kamu harus masuk ke fase pembelanjaan, lalu klik _Kirim_.



![img](assets/en/21.webp)



Pada layar berikutnya, pilih menu yang ditunjukkan oleh tiga titik di sudut kanan atas. Jendela tarik-turun akan terbuka dengan serangkaian perintah. Pilih yang terakhir: kontrol Koin.



![img](assets/en/22.webp)



Pada titik ini, Blue Wallet menunjukkan semua UTXO kamu. Selain jumlah, mereka dibedakan secara grafis dengan warna yang berbeda.



![img](assets/en/27.webp)



Pilih UTXO yang akan dipilih, kemudian pilih _Use Coin_.



![img](assets/en/23.webp)



Wallet biru akan membawa kamu kembali ke jendela _Send_ untuk melanjutkan transaksi. Sesuaikan jumlah dan biaya, setelah itu pilih _Next_.



![img](assets/en/24.webp)



Pada titik ini kamu dapat mengakhiri transaksi, seperti yang biasa kamu lakukan.



#### Pemisahan UTXO



Wallet biru juga memungkinkan kamu untuk memisahkan UTXO, membuatnya tidak tersedia untuk dibelanjakan, yang merupakan fungsi yang baik untuk Wallet dari perangkat seluler. kamu mengakses kontrol Coin dengan prosedur yang baru saja dijelaskan dan, setelah memilih UTXO, pilih _Freeze_ daripada _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Versi mobile Nunchuk juga menyediakan kemampuan bagi pengguna untuk melakukan kontrol Coin. Jika kamu menggunakan aplikasi ini dari ponsel, buka aplikasi ini dan masuk ke menu _Wallet_. Dari sana pilih _Lihat koin_.



![img](assets/en/30.webp)



Pada jendela tempat daftar UTXO muncul, klik _Pilih_.



![img](assets/en/38.webp)



Fungsi pemilihan muncul di samping setiap UTXO. Seperti pada versi desktop, pemilihan manual pada Nunchuk mobile dilakukan dengan mencentang kotak kecil di sebelah jumlah. Layar menunjukkan jumlah UTXO yang dipilih dan jumlah total yang tersedia. Setelah selesai, klik simbol ₿ di pojok kiri bawah, yang merupakan perintah untuk mulai membangun transaksi.



![img](assets/en/31.webp)



Sekarang kamu dapat menyelesaikan transaksi, memilih jumlah yang ingin kamu bayarkan dan klik _Continue_.



![img](assets/en/32.webp)



Lanjutkan seperti yang biasa kamu lakukan, tempelkan tujuan Address, deskripsi, dan sesuaikan pengaturan biaya.



#### Pemisahan UTXO



Kamu juga dapat memisahkan UTXO dengan Nunchuk seluler. Akses jendela daftar koin khusus dan pilih panah di samping UTXO yang ingin kamu pisahkan.



![img](assets/en/42.webp)



Kamu akan melihat ruang yang disediakan untuk _Rincian koin_, di mana kamu dapat memilih _Kunci koin ini_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper adalah Wallet terakhir yang akan kita lihat dalam panduan ini. Kami melihat fungsinya diterapkan pada kontrol Coin dengan Wallet single-sig, meskipun penggunaan seperti itu bukanlah tujuan dari aplikasi yang sangat khusus ini. Setelah menyiapkan Keeper di ponsel kamu, luncurkan dan buka Wallet yang berisi sejumlah dana. Di tengah layar utama, klik _Lihat Semua Koin_.



![img](assets/en/34.webp)



Keeper menunjukkan gambaran umum UTXO. Untuk mengakses layar pemilihan, klik _Pilih Untuk Dikirim_.



![img](assets/en/35.webp)



Kamu bisa memilih koin dengan mencentangnya dengan mengklik perintah yang sesuai. Setelah selesai, klik _Kirim_.



![img](assets/en/36.webp)



Bitcoin Keeper membawakamu langsung ke menu _Send_, di mana kamu dapat membuat transaksi dengan UTXO yang dipilih.



![img](assets/en/37.webp)



## Hardware Wallet



Setiap Dompet Perangkat Lunak yang terlihat dalam panduan ini dapat menjadi Interface khusus jam tangan ke salah satu Dompet Perangkat Keras kamu. Ini berarti kontrol Coin untuk perangkat penandatanganan offline dilakukan dengan langkah-langkah yang terlihat sejauh ini.



### Rekomendasi umum



Kontrol Coin adalah praktik yang sangat efektif untuk memilih input transaksi kamu. Pemilihan secara manual bahkan lebih efisien jika, ketika membeli/menerima dana kamu, kamu telah melabeli sumber Satoshi dengan baik. Jika kamu ingin mempelajari teknik ini dengan baik, aku sarankan tutorial berikut ini:



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kami telah berbicara sebelumnya tentang `pemisahan sisa-sisa`. Jika kamu ingin mengunci sisa-sisa untuk diproses nanti dan mendapatkan kembali privasi (menukar pada Layer 2), kamu harus berhati-hati dalam memberi label setiap kali kamu menerimanya. Dari Dompet Perangkat Lunak yang terlihat sejauh ini, hanya Electrum yang secara grafis mewarnai sisa UTXO untuk membuatnya terlihat sekilas. Yang lainnya, seperti Sparrow, menunjukkan kepada kamu rantai di jalur derivasi dari masing-masing UTXO (`m/84'/0'/0'/1/11`).



Untuk menerapkan teknik ini secara efektif, ingatlah untuk selalu menambahkan deskripsi pada kembalian yang kamu terima: orang yang kamu kirimi dana (pembayaran, tutorial, atau lainnya), mengetahui Address yang terkait dengan kembalian tersebut dan mengetahui bahwa itu adalah milik kamu, karena berasal dari transaksi yang kamu lakukan bersama!
