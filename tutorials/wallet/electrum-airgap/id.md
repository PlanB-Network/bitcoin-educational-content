---
name: Electrum Airgap
description: Langkah pertama menuju keamanan, cold wallet dengan Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



Dalam tutorial ini saya akan menjelaskan cara membuat perangkat penandatanganan airgap pertama Anda, yang terputus dari Internet, bahkan tanpa memiliki Hardware Wallet khusus. Yang Anda perlukan hanyalah memiliki dua komputer:




- perangkat lama untuk selamanya dicegah agar tidak tersambung ke Internet;
- komputer yang Anda gunakan sehari-hari.



Konfigurasi ini memungkinkan tingkat keamanan yang lebih tinggi daripada `Hot Wallet` klasik: komputer lama - tanpa koneksi jaringan - adalah penjaga kunci pribadi Anda, yang tidak pernah diekspos di Internet, tetapi disimpan secara offline ("airgap" atau "Cold").



Sebagai gantinya, Anda akan memasang layar Wallet ("watch-only") di komputer harian Anda, yang terhubung ke jaringan dan dapat digunakan untuk, misalnya, memeriksa saldo dan menyiapkan transaksi penerimaan.



## Celah Udara Wallet: Apa dan Bagaimana



Dengan melakukan langkah-langkah dalam panduan ini, kita akan menginstal dua Software Wallet Electrum pada dua komputer yang berbeda dan akhirnya membuat dua Dompet dengan kunci yang berbeda: airgap Wallet akan menggunakan seluruh hirarki Wallet HD, sedangkan tampilan Wallet akan dibuat dengan kunci publik utama.



Kedua Dompet ini, dalam segala hal, akan sangat berbeda satu sama lain. Satu-satunya kesamaan dari keduanya, seperti yang akan kita lihat, adalah alamatnya:




- gW-13 pada komputer airgap hanya dapat menandatangani tetapi, jika terputus dari jaringan, tidak mengetahui saldo dan alamat yang digunakan;
- gW-12 pada komputer harian hanya akan dapat mempersiapkan dan menyebarkan transaksi, tanpa dapat membuang pengeluaran, tanpa adanya kunci pribadi.



## Persiapan Awal



Untuk mengunduh Electrum, saya sarankan Anda mengikuti langkah pertama dalam tutorial ini:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Setelah mengunduh, selalu verifikasi rilis sebelum menginstalnya, kemudian lanjutkan ke konfigurasi "One Server", seperti yang akan Anda temukan di bagian bantuan, di bawah `Mulai dengan Dummy Wallet`.



Operasi konfigurasi "Satu Server" hanya diperlukan untuk Wallet yang dipasang di komputer harian, karena komputer lainnya akan selalu offline.



Pengoperasian berikut ini melibatkan latihan pada dua komputer (dan Dompet) yang berbeda, jadi, demi kenyamanan dan fokus, saya memilih untuk menetapkan airgap Wallet dengan tema terang, sedangkan layar Wallet memiliki tema gelap.



## Penciptaan Celah Udara Wallet



Setelah mengunduh dan memverifikasi unduhan Electrum, ambil salinan file yang dapat dieksekusi dan bawa ke komputer Anda secara offline. Kemudian jalankan dan instal Electrum.



Klik dua kali untuk memulai Electrum: komputer tempat Anda akan menggunakan Wallet ini dalam keadaan offline, abaikan pengaturan jaringan dan lanjutkan ke pembuatan Wallet yang, dalam panduan ini, akan kita sebut sebagai `airgap`.



![image](assets/en/01.webp)



Pilih _Dompet standar_.



![image](assets/en/02.webp)



Lalu pilih _Buat seed baru_ untuk membuat perangkat lunak generate menjadi Mnemonic.



![image](assets/en/03.webp)



Transkripsikan 12 kata generate dari Electrum secara akurat ke dalam kertas dan lanjutkan dengan langkah verifikasi, masukkan kembali kata-kata tersebut secara berurutan ketika Electrum memintanya.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Setelah pembuatan Wallet selesai, tetapkan kata sandi yang rumit (`Strong`) untuk mengenkripsi file Wallet pada perangkat airgap. Langkah ini sangat rumit dan penting, karena kata sandi yang dipilih sekarang, mencegah akses ke Wallet yang memiliki kekuatan dispositif, dapat menghabiskan dana menandatangani transaksi.



![image](assets/en/06.webp)



Dengan mengklik _Finish_, Wallet akan ditetapkan dan muncul di layar. Tentu saja, indikator koneksi jaringan, yaitu titik berwarna di sudut kanan bawah, berwarna merah, karena komputer terputus dan tidak memungkinkan Wallet untuk mengekspos kunci online.



![image](assets/en/07.webp)



## Penciptaan Wallet dari Visualisasi



Sekarang setelah Wallet Anda memiliki private key offline, Anda perlu mengatur tampilan Wallet, atau `watch-only`, yang akan memungkinkan Anda untuk melihat saldo, serta menyiapkan transaksi penerimaan untuk terus mengakumulasi Sats dengan aman.



Dari Wallet yang terletak di perangkat offline, pilih menu _Wallet_ -> _Information_



![image](assets/en/08.webp)



Jendela yang berisi semua informasi Wallet Anda akan muncul, di mana Anda dapat memeriksa `derivation path` dan `master fingerprint`, misalnya untuk menandainya di samping kata-kata dalam kalimat Mnemonic (sangat disarankan).



![image](assets/en/09.webp)



Ingatlah bahwa Anda mengambil data ini dari komputer yang tidak terhubung, jadi Anda harus menyalin/menempelkan `zpub` ke sebuah file teks dan menyimpannya ke sebuah stik USB.



Sekarang Anda dapat berpindah ke komputer yang terhubung ke Internet, untuk meluncurkan Electrum dan membuat Wallet baru.



Dari menu _File_, pilih _New/Restore_.



![image](assets/en/10.webp)



Wallet baru adalah view-only, jadi untuk panduan ini, kami akan menyebutnya `watch-only`.



![image](assets/en/12.webp)



Pada layar berikutnya, pilihlah _Dompet standar_ dan lanjutkan dengan mengklik _Next_.



![image](assets/en/13.webp)



Dalam memilih `Keystore`, berhati-hatilah: untuk membuat tampilan Wallet pilih _Use a master key_. Kemudian lanjutkan dengan _Next_.



![image](assets/en/14.webp)



Rekatkan di sini `zpub` yang disalin dari Wallet secara offline dan yang Anda bawa ke komputer ini melalui media USB.



![image](assets/en/15.webp)



Akhiri dengan menetapkan kata sandi yang kuat untuk Wallet ini juga, mungkin berbeda dari yang dipilih untuk Cold yang sesuai.



Anda akan melihat tampilan Wallet muncul, dengan sebuah peringatan. Pesan ini mengingatkan Anda bahwa ini adalah Wallet yang hanya untuk tampilan dan Anda tidak dapat menggunakan dana yang terkait.



**Catat dengan baik**: **Anda harus selalu memiliki private key untuk membuang UTXO dari Wallet ini**. Dengan sistem pencadangan yang baik, tidak akan sulit bagi Anda untuk tetap memiliki Bitcoin Anda sepenuhnya.



![image](assets/en/16.webp)



Peringatan ini akan muncul setiap kali Anda membuka Wallet ini. Klik _Ok_ dan mari kita lanjutkan ke langkah verifikasi.



## Verifikasi Dua Wallet



Seperti yang kita pelajari di awal panduan ini, airgap Wallet dan display Wallet adalah dua portofolio yang memiliki fakultas yang berbeda, tetapi **memiliki alamat yang sama**.



Jika kita melihat kedua Dompet berdampingan, secara visual kita melihat bahwa pada airgap Wallet terdapat simbol "seed", sedangkan pada jam tangan tidak ada. Bahkan detail ini akan membantu Anda mengingat bahwa tampilan Wallet Wallet tidak memiliki kunci pribadi.



![image](assets/en/17.webp)



Namun, untuk melakukan pemeriksaan pertama yang akurat, pilihlah menu `Alamat` di kedua Dompet: karena keduanya memiliki alamat yang sama, daftar alamat harus sama untuk keduanya.



![image](assets/en/18.webp)



⚠️ **PERHATIAN**: **tidak boleh ada jalan tengah; alamatnya harus sama. Jika berbeda, Anda harus menghapus semua pekerjaan yang telah dilakukan sejauh ini dan memulai dari awal**.



Sekarang Anda dapat melanjutkan untuk melakukan dua pemeriksaan yang berbeda. Pertama, coba hapus dua Dompet dan pulihkan dari awal, masing-masing pada komputer yang sesuai. Apabila Anda melanjutkan untuk melakukan verifikasi ini, prosedur untuk tampilan Wallet identik dengan yang ditetapkan di atas.



Namun, untuk airgap Wallet, pada layar `keystore` Anda harus memilih _Saya sudah memiliki seed_ dan memasukkan kata-kata dengan menyalinnya dari cadangan kertas Anda.



Setelah uji coba "tanpa beban" selesai, Anda dapat mencoba melakukan transaksi dalam jumlah kecil dan langsung membelanjakannya.



## Transaksi Penerimaan dan Pengeluaran



Untuk mulai menggunakan airgap Electrum Anda, Anda dapat melakukan transaksi penerimaan dengan jumlah kecil, kemudian membelanjakannya untuk membeli Address milik Anda sendiri. Anda kemudian dapat membiasakan diri dengan prosedurnya, memverifikasi bahwa Anda memiliki kendali penuh atas dana tersebut.



**Catatan**: Saya tidak menyarankan Anda untuk menyetor dana dalam jumlah besar pada Wallet sebelum Anda yakin bahwa Anda dapat melakukan semua operasi dengan lancar.



Langkah-langkah yang dijelaskan di bawah ini mungkin, sekilas tampak rumit. Jangan biarkan hal ini membuat Anda kecewa: setelah Anda mencobanya untuk pertama kali, Anda akan mendapati bahwa langkah-langkah ini hanya membutuhkan waktu beberapa menit saja.



Untuk menerima dana, Anda harus menggunakan tampilan Wallet yang terletak di komputer Anda yang terhubung ke Internet. Dari menu `Terima`, klik pada `Buat permintaan` untuk meminta Electrum generate sebagai Address pertama yang tersedia dan menggunakannya untuk mengirimkan beberapa Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Setelah transaksi disebarkan, Anda sudah dapat melihat bahwa-seperti yang sudah sewajarnya- transaksi tersebut hanya terlihat di layar Wallet dan bukan di airgap Wallet.



![image](assets/en/21.webp)



Setelah transaksi Anda menerima konfirmasi, Anda dapat menyiapkan biaya dan kemudian mencoba prosedur penandatanganan dari Wallet di luar jaringan. Kemudian siapkan transaksi pada watch-only dan tekan _Preview_ untuk memeriksanya



![image](assets/en/22.webp)



Anda akan mendapatkan jendela transaksi lanjutan di mana Anda dapat melihatnya:




- transaksi tidak ditandatangani (`Status: Unsigned);
- perintah `Tanda` dan `Siaran` terhambat.



Satu-satunya hal yang dapat Anda lakukan adalah mengekspor transaksi apa adanya, membawanya ke celah udara Wallet dan menandatanganinya.



Masukkan USB flash drive ke komputer Anda dan, dari menu di bagian kiri bawah, pilih _Share_.



![image](assets/en/23.webp)



Setelah itu pilih _Save to file_.



![image](assets/en/24.webp)



Simpan transaksi ke stik USB.



Anda akan melihat bahwa Electrum memberi nama file dengan angka pertama transaction ID, dan ekstensi file adalah `.PSBT`, yang berarti `Partially Signed Bitcoin Transaction`.



Ekstrak media dengan file `.PSBT` dan hubungkan ke komputer secara offline.



Dari airgap Wallet, sekarang pilih menu _Tools_, lalu _Load transaction_ dan ikuti From file_.



![image](assets/en/25.webp)



Dengan pengelola file, pilih `.PSBT` dari lokasinya.



![image](assets/en/29.webp)



Perangkat lunak komputer di luar jaringan akan secara otomatis membuka jendela transaksi lanjutan, sepenuhnya identik dengan yang Anda lihat pada layar Wallet. Statusnya adalah `Tidak Ditandatangani`, tetapi perbedaannya adalah perintah `Tanda tangani` di sini aktif. Dan itulah yang harus Anda jalankan.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Setelah transaksi ditandatangani, ingatlah bahwa Wallet Anda berada pada mesin offline. Oleh karena itu, meskipun Anda melihat perintah `Broadcast` aktif, Wallet Anda tidak akan dapat menyebarkan transaksi ke jaringan Bitcoin.



Yang perlu Anda lakukan sekarang adalah mengulangi operasi mengekspor transaksi yang telah ditandatangani ke stik usb, sehingga Anda bisa mengimpornya ke komputer yang terhubung ke Internet dan menyebarkannya.



Dari menu kiri bawah, pilih _Berbagi_ lagi dan kemudian _Simpan ke file_.



![image](assets/en/28.webp)



Sekarang file tersebut memiliki ekstensi yang berbeda: **alih-alih `.PSBT`, sekarang transaksi memiliki ekstensi `.txn`. Mulai sekarang, inilah cara Electrum untuk mengenali transaksi yang ditandatangani dan yang tidak ditandatangani**.



![image](assets/en/30.webp)



Untuk penyebaran akhir transaksi, keluarkan stik usb dari komputer off-line dan masukkan ke dalam komputer yang terhubung ke Internet.



Dari watch-only, ulangi prosedur impor, yaitu dari menu _Tools_ pilih _Load transaction_ dan terakhir _From file_.



![image](assets/en/31.webp)



Electrum akan membuka jendela transaksi untuk Anda, yang sangat berbeda dari yang ditunjukkan sebelumnya pada Wallet ini, karena sekarang sudah ditandatangani (`Status: Signed`) dan perintah `Broadcast` dapat diakses.



Operasi terakhir yang perlu Anda lakukan hanyalah itu:



![image](assets/en/32.webp)



## Kesimpulan



Pengujian Anda sekarang sudah selesai. Jika Anda mengikuti panduan ini dan mendapatkan hasil yang sama, Anda telah membuat Wallet Cold dengan Electrum, di dua komputer yang berbeda, yang dapat Anda gunakan untuk menyimpan Bitcoin Anda.



Satu-satunya hal yang harus Anda perhatikan adalah dua hal:


1) **Jangan pernah menggunakan airgap Wallet ke alamat penerima generate**. Karena ini offline, maka akan selalu menawarkan Address pertama, yang sama dengan Address yang baru saja Anda gunakan untuk melakukan transaksi uji coba;



![image](assets/en/33.webp)



seperti yang dapat Anda lihat dari gambar di atas, Wallet offline tidak mengetahui sejarah Address-nya sendiri. Ia benar-benar buta dalam hal ini. **Satu-satunya tugas yang dapat dilakukannya untuk Anda adalah menyimpan kunci offline Anda dan menandatangani transaksi Anda**_.



2) Gunakan USB flash drive yang didedikasikan hanya untuk tujuan ini, **jangan gunakan media yang sering Anda gunakan**. Alat sehari-hari lebih mungkin diserang cyber, dan secara tidak sengaja, Anda dapat menyerang komputer yang Anda jaga agar tetap terputus dari jaringan. Stik USB yang Anda gunakan hanya untuk tujuan ini memiliki peluang yang sangat kecil untuk melakukan kontak dengan PC Anda secara online, terutama jika Anda adalah penjaja yang tidak perlu mengeluarkan uang, sehingga mengurangi kemungkinan menerima dan kemudian mengirimkan virus, malware, dll.