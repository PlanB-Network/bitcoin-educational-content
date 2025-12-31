---
name: Ashigaru - Whirlpool Coinjoin
description: Bagaimana cara membuat koin bersama di aplikasi Ashigaru?
---

![cover](assets/cover.webp)



"*sebuah bitcoin wallet untuk jalanan*"



Dalam tutorial ini, Kamu akan mempelajari apa itu coinjoin dan bagaimana cara membuatnya dengan aplikasi Ashigaru Terminal dan implementasi Whirlpool, protokol coinjoin yang diwarisi dari Samourai Wallet.



## Bagaimana cara kerja coinjoint Whirlpool



Dalam tutorial ini, aku tidak akan membahas kembali pengertian coinjoin, kegunaannya, atau operasi teoritis Whirlpool, karena topik-topik ini telah dijelaskan secara rinci di Bagian 5 dari kursus pelatihan BTC 204 di Plan ₿ Academy. Jika kamu belum menguasai pengoperasian Whirlpool atau prinsip coinjoin, aku sangat menyarankan kamu untuk membaca bagian 5 ini sebelum melanjutkan:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Namun demikian, berikut ini adalah beberapa fakta dan angka singkat yang mungkin berguna.



Portofolio yang kompatibel dengan Whirlpool menggunakan 4 akun terpisah untuk memenuhi kebutuhan proses coinjoin:




- Akun **Deposito**, diidentifikasi dengan indeks `0'`;
- Rekening **Bad Bank** (atau **pertukaran dummy**), yang diidentifikasi dengan indeks `2.147.483.644'`;
- Akun **Premix**, diidentifikasi dengan indeks `2 147 483 645'`;
- Akun **Postmix**, diidentifikasi dengan indeks `2 147 483 646'`.



Di Ashigaru, pada bulan November 2025, tersedia dua denominasi pool (daftar ini mungkin akan berkembang dalam beberapa bulan mendatang: jadi ingatlah untuk memeriksa nilainya saat kamu membaca):




- 0.25 BTC`, dengan biaya masuk sebesar `0,0125 BTC`;
- 0.025 BTC, dengan biaya masuk sebesar 0,00125 BTC.



Setiap siklus pencampuran dapat melibatkan antara 5 dan 10 UTXO dalam input dan output.



![Image](assets/fr/01.webp)



## Persyaratan perangkat lunak



Untuk membuat coinjoin dengan Whirlpool, kamu memerlukan tiga program terpisah:





- Ashigaru Terminal**, yang memungkinkan kamu mengelola koin langsung dari komputer;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, aplikasi pada ponsel cerdas kamu yang dapat digunakan untuk membelanjakan bitcoin kamu di *postmix* dari mana saja;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, implementasi node Bitcoin yang menjamin kamu memiliki koneksi yang berdaulat ke jaringan, tanpa ketergantungan pada server pihak ketiga.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Instal masing-masing alat ini dengan mengikuti tutorial masing-masing, kemudian kamu dapat mulai membuat coinjoin pertama kamu.



## Menerima bitcoin



Setelah membuat portofolio, kamu akan mulai dengan satu akun, yang diidentifikasi dengan indeks `0`. Ini adalah akun `Deposit`. Ke akun inilah kamu akan mengirim bitcoin yang ditujukan untuk coinjoin. Kamu dapat menerimanya melalui aplikasi Ashigaru (lihat bagian 5 dari tutorial khusus), atau melalui Ashigaru Terminal (juga dijelaskan di bagian 5 dari tutorial khusus).



Setelah akun deposit kamu berisi setidaknya jumlah yang diperlukan untuk berpartisipasi dalam pool terkecil (ditambah biaya layanan dan minimum yang diperlukan untuk menutupi biaya mining), Kamu akan siap untuk memulai koin pertama.



![Image](assets/fr/02.webp)



## Buatlah Tx0



Setelah dana masuk ke akun deposit kamu dan transaksi telah dikonfirmasi, Kamu dapat memulai proses coinjoin. Untuk melakukannya, pada Terminal Ashigaru, buka menu `Wallets`, lalu pilih wallet kamu. Jika wallet kamu terkunci, perangkat lunak akan meminta kata sandi dan passphrase.



![Image](assets/fr/03.webp)



Kemudian pilih akun `Deposit`.



![Image](assets/fr/04.webp)



Buka menu `UTXOs`.



![Image](assets/fr/05.webp)



Di sini kamu akan melihat daftar semua UTXO di akun deposit kamu. Pilih salah satu yang ingin kamu kirimkan dalam siklus coinjoin.



Untuk kerahasiaan yang lebih baik dan untuk menghindari *Common Input Ownership Heuristic (CIOH)*, disarankan untuk menggunakan hanya satu UTXO per input di Whirlpool (penjelasan rinci tentang prinsip ini dapat ditemukan di BTC 204).



Tekan tombol `ENTER` pada keyboard kamu untuk memilih UTXO: tanda bintang `(*)` akan muncul di sebelahnya untuk mengindikasikan bahwa UTXO telah dipilih.



![Image](assets/fr/06.webp)



Kemudian klik tombol `Mix Selected`.



![Image](assets/fr/07.webp)



Jika kamu memiliki UTXO yang cukup besar untuk berpartisipasi dalam salah satu dari dua pool yang tersedia, Kamu dapat memilih pool tujuan dengan menggunakan tanda panah. Pada halaman ini, kamu akan melihat rincian Tx0 milikmu:




- jumlah UTXO yang akan masuk ke dalam pool;
- berbagai biaya yang diterapkan (biaya layanan dan biaya mining);
- jumlah *perubahan *dolar*.



Periksa informasi dengan cermat, lalu klik `Broadcast` untuk menyiarkan Tx0.



![Image](assets/fr/08.webp)



Ashigaru kemudian akan menampilkan TXID dari Tx0 kamu, yang mengonfirmasi bahwa transaksi telah disiarkan di jaringan.



![Image](assets/fr/09.webp)



## Membuat coinjoin



Setelah Tx0 disiarkan, kembali ke halaman beranda akun deposito kamu, lalu klik `Akun` dan pilih akun `Premix`.



![Image](assets/fr/10.webp)



Dalam menu `UTXOs`, kamu akan melihat berbagai bagian yang disamakan, siap untuk memasuki siklus coinjoin. Segera setelah Tx0 dikonfirmasi, Ashigaru Terminal akan secara otomatis memulai siklus pencampuran pertama.



![Image](assets/fr/11.webp)



Setelah Tx0 dikonfirmasi, transaksi coinjoin pertama akan dibuat dan disiarkan secara otomatis oleh Ashigaru Terminal. Dengan masuk ke `Accounts > Postmix > UTXOs`, kamu dapat melihat UTXO yang disamakan, menunggu konfirmasi siklus pertama mereka.



![Image](assets/fr/12.webp)



Sekarang kamu dapat membiarkan Ashigaru Terminal berjalan di latar belakang: Ashigaru Terminal akan terus mencampur secara otomatis.



## Menyelesaikan coinjoin



Sekarang kamu bisa membiarkan koin melakukan pencampuran secara otomatis. Model Whirlpool berarti tidak ada biaya tambahan untuk mencampur ulang: tidak ada biaya layanan, tidak ada biaya mining. Jadi, membiarkan koin kamu berpartisipasi dalam lebih banyak siklus pencampuran hanya akan menguntungkan kerahasiaan kamhu.



Untuk pemahaman yang lebih baik mengenai mekanisme ini dan berapa banyak siklus yang perlu ditunggu, aku sarankan untuk membaca artikel ini:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Untuk melihat jumlah remix yang dilakukan oleh masing-masing karya kamu, buka menu `UTXOs` di akun `Postmix`.



![Image](assets/fr/13.webp)



Untuk membelanjakan koin campuran kamu, buka aplikasi Ashigaru, yang menggunakan wallet yang sama dengan perangkat lunak Ashigaru Terminal milikmu. wallet yang ditampilkan pada saat pembukaan sesuai dengan akun `Deposit`. Untuk mengakses akun `Postmix`, yang berisi UTXO campuran, klik simbol Whirlpool di sudut kanan atas.



![Image](assets/fr/14.webp)



Di akun ini, kamu akan melihat semua koin kamu yang sedang dicampur. Untuk membelanjakannya, tekan simbol `+` di bagian kanan bawah layar, lalu pilih `Kirim`.



![Image](assets/fr/15.webp)



Isi detail transaksi kamu: alamat penerima, jumlah yang akan dikirim, dan, jika Anda ingin, pilih struktur transaksi tertentu untuk lebih meningkatkan kerahasiaan kamu (lihat tutorial terkait).



![Image](assets/fr/16.webp)



Periksa detail transaksi dengan cermat, lalu seret panah di bagian bawah layar untuk mengonfirmasi pengiriman.



![Image](assets/fr/17.webp)



Transaksi kamu telah ditandatangani dan disiarkan di jaringan Bitcoin.



![Image](assets/fr/18.webp)



## Menghabiskan Uang Kembalian



Ingat: Model Whirlpool didasarkan pada penyetaraan pion kamu di Tx0, sebelum masuk ke pool. Mekanisme inilah yang mematahkan pelacakan UTXO. Menurutku, ini adalah model coinjoin yang paling efisien, tetapi ada satu kekurangannya: model ini menghasilkan *perubahan* yang tidak melalui proses coinjoin.



Perubahan ini sesuai dengan UTXO yang dibuat untuk setiap Tx0. Perubahan ini diisolasi dalam akun khusus bernama `Doxxic Change` atau `Bad Bank`, tergantung pada perangkat lunaknya, untuk menghindari penggunaannya dengan UTXO kamu yang lain. Ini sangat penting, karena UTXO ini belum tercampur: tautan penelusurannya tetap utuh, dan dapat membahayakan kerahasiaan dengan membuat koneksi antara kamu dan aktivitas coinjoin kamu. Jadi, tangani mereka dengan hati-hati dan **jangan pernah menggunakannya dengan UTXO lain**, baik yang sudah tercampur maupun belum. Menggabungkan UTXO yang beracun dengan UTXO campuran akan menghapus semua keuntungan privasi yang kamu dapatkan dari coinjoin.



Untuk saat ini, Ashigaru tidak menawarkan akses langsung ke akun `Doxxic Change` ini (setidaknya, aku belum menemukannya). Fitur ini mungkin akan ditambahkan di pembaruan mendatang. Sementara itu, satu-satunya cara untuk mengambil dana ini adalah dengan mengimpor seed kamu ke Sparrow Wallet. Yang terakhir ini biasanya akan secara otomatis mendeteksi bahwa ini adalah wallet yang digunakan dengan Whirlpool dan memberi kamu akses ke keempat akun, termasuk akun `Doxxic Change`. kamu kemudian dapat menggunakan UTXO ini seperti bitcoin biasa dari Sparrow.



Berikut adalah beberapa strategi yang memungkinkan untuk mengelola UTXO valuta asing kamu dari coinjoins tanpa mengorbankan privasi Anda:





- Menggabungkannya ke dalam pool yang lebih kecil:** Jika UTXO beracun kamu cukup besar untuk bergabung dengan pool yang lebih kecil, ini umumnya merupakan pilihan terbaik. Namun, berhati-hatilah, jangan pernah menggabungkan beberapa UTXO beracun untuk mencapai hal ini, karena hal ini akan menciptakan hubungan antara berbagai entri di Whirlpool.





- Tandai sebagai tidak dapat dibelanjakan:** Pendekatan lain yang bijaksana adalah dengan menyimpannya di rekening terpisah dan membiarkannya tidak tersentuh. Hal ini akan mencegahmu membelanjakannya secara tidak sengaja. Jika nilai bitcoin meningkat, pool baru yang disesuaikan dengan ukurannya dapat dibuka.





- Memberikan donasi:** kamu dapat memilih untuk mengubah UTXO beracun ini menjadi donasi kepada pengembang Bitcoin, proyek sumber terbuka, atau asosiasi yang menerima BTC. Dengan demikian, kamu dapat membuangnya secara bermanfaat sekaligus mendukung ekosistem.





- Beli kartu hadiah prabayar atau kartu Visa:** Platform seperti [Bitrefill] (https://www.bitrefill.com/) memungkinkanmu untuk menukar bitcoin Anda dengan kartu hadiah atau kartu Visa yang dapat diisi ulang yang dapat digunakan di toko-toko. Ini bisa menjadi cara yang sederhana dan bijaksana untuk membelanjakan UTXO beracun kamu.





- Tukar dengan Monero:** Samourai Wallet dulunya menawarkan layanan penukaran atom BTC/XMR yang sekarang sudah tidak ada lagi. Jika layanan serupa ada (aku tidak tahu secara pribadi), ini adalah solusi yang sangat baik untuk mengisolasi UTXO ini, mengonversinya menjadi Monero, dan kemudian mengirimkannya kembali ke Bitcoin. Namun, metode ini mahal dan bergantung pada likuiditas yang tersedia.





- Mentransfernya ke Lightning Network:** Mentransfer UTXO ini ke Lightning Network untuk mendapatkan keuntungan dari pengurangan biaya transaksi adalah opsi yang berpotensi menarik. Namun, metode ini dapat mengungkapkan informasi tertentu tergantung pada penggunaan Lightning kamu, dan oleh karena itu harus digunakan dengan hati-hati.



## Bagaimana aku dapat mengetahui tentang kualitas siklus coinjoin kami?



Agar coinjoin benar-benar efektif, coinjoin harus memiliki tingkat keseragaman yang tinggi antara jumlah input dan output. Keseragaman ini meningkatkan jumlah interpretasi yang mungkin untuk pengamat luar, yang pada gilirannya meningkatkan ketidakpastian tentang transaksi. Untuk mengukur ketidakpastian ini, kami menggunakan konsep entropi yang diterapkan pada transaksi. Model Whirlpool dikenal sebagai salah satu yang paling efektif dalam hal ini, karena model ini menjamin homogenitas yang sangat baik di antara para partisipan. Untuk melihat lebih dalam mengenai prinsip ini, aku sarankan kamu untuk membaca bab terakhir dari Bagian 5 kursus pelatihan BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Performa dari beberapa siklus koin diukur dari ukuran himpunan tempat koin disembunyikan. Himpunan ini mendefinisikan apa yang dikenal sebagai *anonset*. Ada dua jenis: yang pertama mengukur kerahasiaan dalam menghadapi analisis retrospektif (dari masa sekarang ke masa lalu), dan yang kedua mengukur resistensi terhadap analisis prospektif (dari masa lalu ke masa sekarang). Untuk penjelasan lengkap mengenai kedua indikator ini, silakan baca tutorial berikut ini (atau, sekali lagi, kursus pelatihan BTC 204):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Bagaimana cara mengelola postmix?



Setelah menjalankan beberapa siklus coinjoin, strategi terbaik adalah menyimpan UTXO kamu di akun `Postmix`, membiarkannya melakukan remix tanpa batas waktu hingga kamu benar-benar harus membelanjakannya.



Beberapa pengguna lebih memilih untuk mentransfer bitcoin campuran mereka ke wallet yang diamankan oleh perangkat keras wallet. Opsi ini memungkinkan, tetapi membutuhkan sejumlah ketelitian untuk memastikan bahwa kerahasiaan yang diperoleh dengan coinjoin tidak terganggu.



Menggabungkan UTXO adalah kesalahan yang paling sering terjadi. Sangatlah penting untuk tidak pernah menggabungkan UTXO yang tercampur dengan UTXO yang tidak tercampur dalam transaksi yang sama, jika tidak, kamu berisiko memicu *Common Input Ownership Heuristic (CIOH) *. Hal ini menyiratkan manajemen yang ketat terhadap UTXO kamu, terutama melalui pelabelan yang jelas dan tepat. Secara umum, menggabungkan UTXO adalah praktik buruk yang sering kali menyebabkan hilangnya kerahasiaan jika tidak dikelola dengan baik.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kamu juga harus berhati-hati dalam mengkonsolidasikan UTXO campuran. Konsolidasi terbatas dapat dipertimbangkan jika UTXO memiliki anonset yang signifikan, tetapi hal ini pasti akan mengurangi tingkat kerahasiaan kamu. Hindari konsolidasi yang masif atau terburu-buru, yang dilakukan sebelum jumlah remix yang cukup, karena hal ini dapat membuat hubungan inferensial antara karya sebelum dan sesudah remix. Jika ragu, sebaiknya tidak mengkonsolidasikan UTXO postmix kamu dan mentransfernya satu per satu ke perangkat keras wallet kamu, dengan membuat alamat penerimaan kosong yang baru setiap kali. Jangan lupa untuk memberi label pada setiap UTXO yang ditransfer.



Kami sangat menyarankan agar kamu tidak memindahkan UTXO postmix kamu ke portofolio yang menggunakan skrip minoritas. Sebagai contoh, jika kamu berpartisipasi dalam Whirlpool dari portofolio multi-sig di `P2WSH`, hanya akan ada sedikit dari kamu yang menggunakan skrip jenis ini. Dengan mengirimkan UTXO postmix kamu ke jenis skrip yang sama ini, kamu sangat mengurangi anonimitas kamu. Di luar jenis skrip tersebut, sidik jari wallet spesifik lainnya dapat membahayakan kerahasiaanmu, jadi hal terbaik yang harus dilakukan adalah menggunakannya dari aplikasi Ashigaru.



Terakhir, seperti halnya semua transaksi Bitcoin, jangan pernah menggunakan kembali alamat penerima. Setiap pembayaran harus dikirim ke alamat baru yang unik dan kosong.



Metode yang paling sederhana dan aman adalah dengan membiarkan UTXO campuran kamu beristirahat di akun `Postmix` mereka, biarkan mereka melakukan remix secara alami, dan hanya menggunakannya saat dibutuhkan dari Ashigaru.



Dompet Ashigaru dan Sparrow menggabungkan perlindungan tambahan terhadap kesalahan paling umum yang terkait dengan analisis blockchain, membantumu menjaga kerahasiaan transaksi kamu.
