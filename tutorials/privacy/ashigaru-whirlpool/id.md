---
name: Ashigaru - Whirlpool Coinjoin
description: Bagaimana cara membuat koin bersama di aplikasi Ashigaru?
---

![cover](assets/cover.webp)



"*sebuah bitcoin wallet untuk jalanan*"



Dalam tutorial ini, Anda akan mempelajari apa itu coinjoin dan bagaimana cara membuatnya dengan aplikasi Ashigaru Terminal dan implementasi Whirlpool, protokol coinjoin yang diwarisi dari Samourai Wallet.



## Bagaimana cara kerja coinjoint Whirlpool



Dalam tutorial ini, saya tidak akan membahas kembali pengertian coinjoin, kegunaannya, atau operasi teoritis Whirlpool, karena topik-topik ini telah dijelaskan secara rinci di Bagian 5 dari kursus pelatihan BTC 204 di Plan ₿ Academy. Jika Anda belum menguasai pengoperasian Whirlpool atau prinsip coinjoin, saya sangat menyarankan Anda untuk membaca bagian 5 ini sebelum melanjutkan:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Namun demikian, berikut ini adalah beberapa fakta dan angka singkat yang mungkin berguna.



Portofolio yang kompatibel dengan Whirlpool menggunakan 4 akun terpisah untuk memenuhi kebutuhan proses coinjoin:




- Akun **Deposito**, diidentifikasi dengan indeks `0'`;
- Rekening **Bad Bank** (atau **pertukaran dummy**), yang diidentifikasi dengan indeks `2.147.483.644'`;
- Akun **Premix**, diidentifikasi dengan indeks `2 147 483 645'`;
- Akun **Postmix**, diidentifikasi dengan indeks `2 147 483 646'`.



Di Ashigaru, pada bulan November 2025, tersedia dua denominasi pool (daftar ini mungkin akan berkembang dalam beberapa bulan mendatang: jadi ingatlah untuk memeriksa nilainya saat Anda membaca):




- 0.25 BTC`, dengan biaya masuk sebesar `0,0125 BTC`;
- 0.025 BTC, dengan biaya masuk sebesar 0,00125 BTC.



Setiap siklus pencampuran dapat melibatkan antara 5 dan 10 UTXO dalam input dan output.



![Image](assets/fr/01.webp)



## Persyaratan perangkat lunak



Untuk membuat coinjoin dengan Whirlpool, Anda memerlukan tiga program terpisah:





- Ashigaru Terminal**, yang memungkinkan Anda mengelola koin langsung dari komputer Anda;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, aplikasi pada ponsel cerdas Anda yang dapat digunakan untuk membelanjakan bitcoin Anda di *postmix* dari mana saja;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, implementasi node Bitcoin yang menjamin Anda memiliki koneksi yang berdaulat ke jaringan, tanpa ketergantungan pada server pihak ketiga.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Instal masing-masing alat ini dengan mengikuti tutorial masing-masing, kemudian Anda dapat mulai membuat coinjoin pertama Anda.



## Menerima bitcoin



Setelah membuat portofolio, Anda akan mulai dengan satu akun, yang diidentifikasi dengan indeks `0`. Ini adalah akun `Deposit`. Ke akun inilah Anda akan mengirim bitcoin yang ditujukan untuk coinjoin. Anda dapat menerimanya melalui aplikasi Ashigaru (lihat bagian 5 dari tutorial khusus), atau melalui Ashigaru Terminal (juga dijelaskan di bagian 5 dari tutorial khusus).



Setelah akun deposit Anda berisi setidaknya jumlah yang diperlukan untuk berpartisipasi dalam pool terkecil (ditambah biaya layanan dan minimum yang diperlukan untuk menutupi biaya mining), Anda akan siap untuk memulai koin pertama Anda.



![Image](assets/fr/02.webp)



## Buatlah Tx0



Setelah dana masuk ke akun deposit Anda dan transaksi telah dikonfirmasi, Anda dapat memulai proses coinjoin. Untuk melakukannya, pada Terminal Ashigaru, buka menu `Wallets`, lalu pilih wallet Anda. Jika wallet Anda terkunci, perangkat lunak akan meminta kata sandi dan passphrase Anda.



![Image](assets/fr/03.webp)



Kemudian pilih akun `Deposit`.



![Image](assets/fr/04.webp)



Buka menu `UTXOs`.



![Image](assets/fr/05.webp)



Di sini Anda akan melihat daftar semua UTXO di akun deposit Anda. Pilih salah satu yang ingin Anda kirimkan dalam siklus coinjoin.



Untuk kerahasiaan yang lebih baik dan untuk menghindari *Common Input Ownership Heuristic (CIOH)*, disarankan untuk menggunakan hanya satu UTXO per input di Whirlpool (penjelasan rinci tentang prinsip ini dapat ditemukan di BTC 204).



Tekan tombol `ENTER` pada keyboard Anda untuk memilih UTXO: tanda bintang `(*)` akan muncul di sebelahnya untuk mengindikasikan bahwa UTXO telah dipilih.



![Image](assets/fr/06.webp)



Kemudian klik tombol `Mix Selected`.



![Image](assets/fr/07.webp)



Jika Anda memiliki UTXO yang cukup besar untuk berpartisipasi dalam salah satu dari dua pool yang tersedia, Anda dapat memilih pool tujuan dengan menggunakan tanda panah. Pada halaman ini, Anda akan melihat rincian Tx0 Anda:




- jumlah UTXO yang akan masuk ke dalam pool;
- berbagai biaya yang diterapkan (biaya layanan dan biaya mining);
- jumlah *perubahan *dolar*.



Periksa informasi dengan cermat, lalu klik `Broadcast` untuk menyiarkan Tx0.



![Image](assets/fr/08.webp)



Ashigaru kemudian akan menampilkan TXID dari Tx0 Anda, yang mengonfirmasi bahwa transaksi telah disiarkan di jaringan.



![Image](assets/fr/09.webp)



## Membuat coinjoin



Setelah Tx0 disiarkan, kembali ke halaman beranda akun deposito Anda, lalu klik `Akun` dan pilih akun `Premix`.



![Image](assets/fr/10.webp)



Dalam menu `UTXOs`, Anda akan melihat berbagai bagian yang disamakan, siap untuk memasuki siklus coinjoin. Segera setelah Tx0 dikonfirmasi, Ashigaru Terminal akan secara otomatis memulai siklus pencampuran pertama.



![Image](assets/fr/11.webp)



Setelah Tx0 dikonfirmasi, transaksi coinjoin pertama akan dibuat dan disiarkan secara otomatis oleh Ashigaru Terminal. Dengan masuk ke `Accounts > Postmix > UTXOs`, Anda dapat melihat UTXO yang disamakan, menunggu konfirmasi siklus pertama mereka.



![Image](assets/fr/12.webp)



Sekarang Anda dapat membiarkan Ashigaru Terminal berjalan di latar belakang: Ashigaru Terminal akan terus mencampur dan meremix lagu Anda secara otomatis.



## Menyelesaikan coinjoin



Sekarang Anda bisa membiarkan koin Anda melakukan remix secara otomatis. Model Whirlpool berarti tidak ada biaya tambahan untuk mencampur ulang: tidak ada biaya layanan, tidak ada biaya mining. Jadi, membiarkan koin Anda berpartisipasi dalam lebih banyak siklus pencampuran hanya akan menguntungkan kerahasiaan Anda.



Untuk pemahaman yang lebih baik mengenai mekanisme ini dan berapa banyak siklus yang perlu ditunggu, saya sarankan untuk membaca artikel ini:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Untuk melihat jumlah remix yang dilakukan oleh masing-masing karya Anda, buka menu `UTXOs` di akun `Postmix`.



![Image](assets/fr/13.webp)



Untuk membelanjakan koin campuran Anda, buka aplikasi Ashigaru, yang menggunakan wallet yang sama dengan perangkat lunak Ashigaru Terminal Anda. wallet yang ditampilkan pada saat pembukaan sesuai dengan akun `Deposit` Anda. Untuk mengakses akun `Postmix`, yang berisi UTXO campuran Anda, klik simbol Whirlpool di sudut kanan atas.



![Image](assets/fr/14.webp)



Di akun ini, Anda akan melihat semua koin Anda yang sedang dicampur. Untuk membelanjakannya, tekan simbol `+` di bagian kanan bawah layar, lalu pilih `Kirim`.



![Image](assets/fr/15.webp)



Isi detail transaksi Anda: alamat penerima, jumlah yang akan dikirim, dan, jika Anda ingin, pilih struktur transaksi tertentu untuk lebih meningkatkan kerahasiaan Anda (lihat tutorial terkait).



![Image](assets/fr/16.webp)



Periksa detail transaksi dengan cermat, lalu seret panah di bagian bawah layar untuk mengonfirmasi pengiriman.



![Image](assets/fr/17.webp)



Transaksi Anda telah ditandatangani dan disiarkan di jaringan Bitcoin.



![Image](assets/fr/18.webp)



## Menghabiskan Uang Kembalian



Ingat: Model Whirlpool didasarkan pada penyetaraan bidak Anda di Tx0, sebelum masuk ke kolam. Mekanisme inilah yang mematahkan pelacakan UTXO. Menurut saya, ini adalah model coinjoin yang paling efisien, tetapi ada satu kekurangannya: model ini menghasilkan *perubahan* yang tidak melalui proses coinjoin.



Perubahan ini sesuai dengan UTXO yang dibuat untuk setiap Tx0. Perubahan ini diisolasi dalam akun khusus bernama `Doxxic Change` atau `Bad Bank`, tergantung pada perangkat lunaknya, untuk menghindari penggunaannya dengan UTXO Anda yang lain. Ini sangat penting, karena UTXO ini belum tercampur: tautan penelusurannya tetap utuh, dan dapat membahayakan kerahasiaan Anda dengan membuat koneksi antara Anda dan aktivitas coinjoin Anda. Jadi, tangani mereka dengan hati-hati dan **jangan pernah menggunakannya dengan UTXO lain**, baik yang sudah tercampur maupun belum. Menggabungkan UTXO yang beracun dengan UTXO campuran akan menghapus semua keuntungan privasi yang Anda dapatkan dari coinjoin.



Untuk saat ini, Ashigaru tidak menawarkan akses langsung ke akun `Doxxic Change` ini (setidaknya, saya belum menemukannya). Fitur ini mungkin akan ditambahkan di pembaruan mendatang. Sementara itu, satu-satunya cara untuk mengambil dana ini adalah dengan mengimpor seed Anda ke Sparrow Wallet. Yang terakhir ini biasanya akan secara otomatis mendeteksi bahwa ini adalah wallet yang digunakan dengan Whirlpool dan memberi Anda akses ke keempat akun, termasuk akun `Doxxic Change`. Anda kemudian dapat menggunakan UTXO ini seperti bitcoin biasa dari Sparrow.



Berikut adalah beberapa strategi yang memungkinkan untuk mengelola UTXO valuta asing Anda dari coinjoins tanpa mengorbankan privasi Anda:





- Menggabungkannya ke dalam pool yang lebih kecil:** Jika UTXO beracun Anda cukup besar untuk bergabung dengan pool yang lebih kecil, ini umumnya merupakan pilihan terbaik. Namun, berhati-hatilah, jangan pernah menggabungkan beberapa UTXO beracun untuk mencapai hal ini, karena hal ini akan menciptakan hubungan antara berbagai entri Anda di Whirlpool.





- Tandai sebagai tidak dapat dibelanjakan:** Pendekatan lain yang bijaksana adalah dengan menyimpannya di rekening terpisah dan membiarkannya tidak tersentuh. Hal ini akan mencegah Anda membelanjakannya secara tidak sengaja. Jika nilai bitcoin meningkat, pool baru yang disesuaikan dengan ukurannya dapat dibuka.





- Memberikan donasi:** Anda dapat memilih untuk mengubah UTXO beracun ini menjadi donasi kepada pengembang Bitcoin, proyek sumber terbuka, atau asosiasi yang menerima BTC. Dengan demikian, Anda dapat membuangnya secara bermanfaat sekaligus mendukung ekosistem.





- Beli kartu hadiah prabayar atau kartu Visa:** Platform seperti [Bitrefill](https://www.bitrefill.com/) memungkinkan Anda untuk menukar bitcoin Anda dengan kartu hadiah atau kartu Visa yang dapat diisi ulang yang dapat digunakan di toko-toko. Ini bisa menjadi cara yang sederhana dan bijaksana untuk membelanjakan UTXO beracun Anda.





- Tukar dengan Monero:** Samourai Wallet dulunya menawarkan layanan penukaran atom BTC/XMR yang sekarang sudah tidak ada lagi. Jika layanan serupa ada (saya tidak tahu secara pribadi), ini adalah solusi yang sangat baik untuk mengisolasi UTXO ini, mengonversinya menjadi Monero, dan kemudian mengirimkannya kembali ke Bitcoin. Namun, metode ini mahal dan bergantung pada likuiditas yang tersedia.





- Mentransfernya ke Lightning Network:** Mentransfer UTXO ini ke Lightning Network untuk mendapatkan keuntungan dari pengurangan biaya transaksi adalah opsi yang berpotensi menarik. Namun, metode ini dapat mengungkapkan informasi tertentu tergantung pada penggunaan Lightning Anda, dan oleh karena itu harus digunakan dengan hati-hati.



## Bagaimana saya dapat mengetahui tentang kualitas siklus coinjoin kami?



Agar coinjoin benar-benar efektif, coinjoin harus memiliki tingkat keseragaman yang tinggi antara jumlah input dan output. Keseragaman ini meningkatkan jumlah interpretasi yang mungkin untuk pengamat luar, yang pada gilirannya meningkatkan ketidakpastian tentang transaksi. Untuk mengukur ketidakpastian ini, kami menggunakan konsep entropi yang diterapkan pada transaksi. Model Whirlpool dikenal sebagai salah satu yang paling efektif dalam hal ini, karena model ini menjamin homogenitas yang sangat baik di antara para partisipan. Untuk melihat lebih dalam mengenai prinsip ini, saya sarankan Anda untuk membaca bab terakhir dari Bagian 5 kursus pelatihan BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Performa dari beberapa siklus koin diukur dari ukuran himpunan tempat koin disembunyikan. Himpunan ini mendefinisikan apa yang dikenal sebagai *anonset*. Ada dua jenis: yang pertama mengukur kerahasiaan dalam menghadapi analisis retrospektif (dari masa sekarang ke masa lalu), dan yang kedua mengukur resistensi terhadap analisis prospektif (dari masa lalu ke masa sekarang). Untuk penjelasan lengkap mengenai kedua indikator ini, silakan baca tutorial berikut ini (atau, sekali lagi, kursus pelatihan BTC 204):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Bagaimana cara mengelola postmix?



Setelah menjalankan beberapa siklus coinjoin, strategi terbaik adalah menyimpan UTXO Anda di akun `Postmix`, membiarkannya melakukan remix tanpa batas waktu hingga Anda benar-benar harus membelanjakannya.



Beberapa pengguna lebih memilih untuk mentransfer bitcoin campuran mereka ke wallet yang diamankan oleh perangkat keras wallet. Opsi ini memungkinkan, tetapi membutuhkan sejumlah ketelitian untuk memastikan bahwa kerahasiaan yang diperoleh dengan coinjoin tidak terganggu.



Menggabungkan UTXO adalah kesalahan yang paling sering terjadi. Sangatlah penting untuk tidak pernah menggabungkan UTXO yang tercampur dengan UTXO yang tidak tercampur dalam transaksi yang sama, jika tidak, Anda berisiko memicu *Common Input Ownership Heuristic (CIOH) *. Hal ini menyiratkan manajemen yang ketat terhadap UTXO Anda, terutama melalui pelabelan yang jelas dan tepat. Secara umum, menggabungkan UTXO adalah praktik buruk yang sering kali menyebabkan hilangnya kerahasiaan jika tidak dikelola dengan baik.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Anda juga harus berhati-hati dalam mengkonsolidasikan UTXO campuran. Konsolidasi terbatas dapat dipertimbangkan jika UTXO memiliki anonset yang signifikan, tetapi hal ini pasti akan mengurangi tingkat kerahasiaan Anda. Hindari konsolidasi yang masif atau terburu-buru, yang dilakukan sebelum jumlah remix yang cukup, karena hal ini dapat membuat hubungan inferensial antara karya sebelum dan sesudah remix. Jika ragu, sebaiknya tidak mengkonsolidasikan UTXO postmix Anda dan mentransfernya satu per satu ke perangkat keras wallet Anda, dengan membuat alamat penerimaan kosong yang baru setiap kali. Jangan lupa untuk memberi label pada setiap UTXO yang ditransfer.



Kami sangat menyarankan agar Anda tidak memindahkan UTXO postmix Anda ke portofolio yang menggunakan skrip minoritas. Sebagai contoh, jika Anda berpartisipasi dalam Whirlpool dari portofolio multi-sig di `P2WSH`, hanya akan ada sedikit dari Anda yang menggunakan skrip jenis ini. Dengan mengirimkan UTXO postmix Anda ke jenis skrip yang sama ini, Anda sangat mengurangi anonimitas Anda. Di luar jenis skrip tersebut, sidik jari wallet spesifik lainnya dapat membahayakan kerahasiaan Anda, jadi hal terbaik yang harus dilakukan adalah menggunakannya dari aplikasi Ashigaru.



Terakhir, seperti halnya semua transaksi Bitcoin, jangan pernah menggunakan kembali alamat penerima. Setiap pembayaran harus dikirim ke alamat baru yang unik dan kosong.



Metode yang paling sederhana dan aman adalah dengan membiarkan UTXO campuran Anda beristirahat di akun `Postmix` mereka, biarkan mereka melakukan remix secara alami, dan hanya menggunakannya saat dibutuhkan dari Ashigaru.



Dompet Ashigaru dan Sparrow menggabungkan perlindungan tambahan terhadap kesalahan paling umum yang terkait dengan analisis blockchain, membantu Anda menjaga kerahasiaan transaksi Anda.