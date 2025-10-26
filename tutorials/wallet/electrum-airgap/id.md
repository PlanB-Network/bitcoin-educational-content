---
name: Electrum Air-Gapped
description: Langkah pertama menuju keselamatan, Cold Wallet dengan Electrum
---
![cover](assets/cover.webp)

## Cold Wallet

Di tutorial ini aku bakal jelasin cara bikin perangkat penandatanganan air-gapped pertamamu—yang benar-benar terputus dari internet, tanpa perlu punya hardware wallet khusus. Kamu cuma butuh dua komputer:

- perangkat lama untuk selamanya dicegah agar tidak tersambung ke Internet;
- komputer yang Anda gunakan sehari-hari.

Konfigurasi ini memungkinkan tingkat keamanan yang lebih tinggi daripada `Hot Wallet` klasik: komputer lama - tanpa koneksi jaringan - adalah penjaga private key milikmu, yang tidak pernah diekspos di Internet, tetapi disimpan secara offline ("airgap" atau "Cold").

Sebagai gantinya, kamu akan memasang layar Wallet ("watch-only") di komputer harian milikmu, yang terhubung ke jaringan dan dapat digunakan untuk, misalnya, memeriksa saldo dan menyiapkan transaksi penerimaan.

## Celah Udara Wallet: Apa dan Bagaimana

Dengan mengikuti langkah-langkah di panduan ini, kita akan menginstal dua software wallet Electrum di dua komputer berbeda dan akhirnya membuat dua dompet dengan kunci yang berbeda. Dompet air-gapped akan menggunakan seluruh hierarki dompet HD, sedangkan dompet tampilan akan dibuat menggunakan kunci publik utama.

Kedua dompet ini benar-benar berbeda satu sama lain dalam segala hal. Satu-satunya kesamaan di antara keduanya, seperti yang nanti bakal kita lihat, adalah alamatnya:

- gW-13 pada komputer airgap hanya dapat menandatangani tetapi, jika terputus dari jaringan, tidak mengetahui saldo dan alamat yang digunakan;
- gW-12 pada komputer harian hanya akan dapat mempersiapkan dan menyebarkan transaksi, tanpa dapat membuang pengeluaran, tanpa adanya kunci pribadi.

## Persiapan Awal

Untuk mengunduh Electrum, aku sarankan kamu mengikuti langkah pertama dalam tutorial ini:

https://planb.network/it/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Setelah mengunduh, selalu verifikasi rilis sebelum menginstalnya, kemudian lanjutkan ke konfigurasi "One Server", seperti yang akan kamu temukan di bagian bantuan, di bawah `Mulai dengan Dummy Wallet`.

Operasi konfigurasi "Satu Server" hanya diperlukan untuk Wallet yang dipasang di komputer harian, karena komputer lainnya akan selalu offline.

Langkah-langkah berikut melibatkan penggunaan dua komputer (dan dua dompet) yang berbeda. Supaya lebih mudah dan fokus, aku memilih untuk memberi tema terang pada dompet air-gapped, sementara dompet tampilan pakai tema gelap.

## Penciptaan Celah Udara Wallet

Setelah kamu mengunduh dan memverifikasi file Electrum, salin file executable-nya dan pindahkan ke komputer yang sepenuhnya offline. Lalu jalankan dan instal Electrum di sana.

Klik dua kali untuk membuka Electrum. Karena komputer ini akan digunakan untuk dompet yang offline, abaikan pengaturan jaringannya dan langsung lanjut ke proses pembuatan dompet yang dalam panduan ini akan kita sebut `airgap`.

![image](assets/en/01.webp)

Pilih _Dompet standar_.

![image](assets/en/02.webp)

Lalu pilih _Buat seed baru_ untuk membuat perangkat lunak generate menjadi Mnemonic.

![image](assets/en/03.webp)

Transkripsikan 12 kata generate dari Electrum secara akurat ke dalam kertas dan lanjutkan dengan langkah verifikasi, masukkan kembali kata-kata tersebut secara berurutan ketika Electrum memintanya.

![image](assets/en/04.webp)

![image](assets/en/05.webp)

Setelah pembuatan dompet selesai, tetapkan kata sandi yang kuat untuk mengenkripsi file dompet di perangkat air-gapped. Langkah ini sangat penting, karena kata sandi yang kuat akan mencegah siapa pun yang mendapat akses fisik ke perangkatmu mengakses dompet, menandatangani transaksi, atau menghabiskan dana.

![image](assets/en/06.webp)

Dengan mengklik _Finish_, Wallet akan ditetapkan dan muncul di layar. Tentu saja, indikator koneksi jaringan, yaitu titik berwarna di sudut kanan bawah, berwarna merah, karena komputer terputus dan tidak memungkinkan Wallet untuk mengekspos kunci online.

![image](assets/en/07.webp)

## Penciptaan Wallet dari Visualisasi

Sekarang setelah dompetmu memiliki private key secara offline, kamu perlu menyiapkan dompet tampilan atau `watch-only`. Dompet ini memungkinkan kamu untuk memantau saldo dan membuat transaksi penerimaan supaya kamu bisa terus mengakumulasi sats dengan aman.

Dari Wallet yang terletak di perangkat offline, pilih menu _Wallet_ -> _Information_

![image](assets/en/08.webp)

Akan muncul jendela yang menampilkan semua informasi tentang dompetmu. Di sana kamu bisa memeriksa `derivation path` dan `master fingerprint`—misalnya untuk kamu catat di samping kata-kata dalam seedphrase (sangat disarankan).

![image](assets/en/09.webp)

Ingat, kamu mengambil data ini dari komputer yang tidak terhubung ke internet, jadi salin `zpub` ke file teks dan simpan di flashdisk.

Sekarang kamu bisa pindah ke komputer yang terhubung ke internet untuk membuka Electrum dan membuat dompet baru..

Dari menu _File_, pilih _New/Restore_.

![image](assets/en/10.webp)

Wallet baru adalah view-only, jadi untuk panduan ini, kami akan menyebutnya `watch-only`.

![image](assets/en/12.webp)

Pada layar berikutnya, pilihlah _Dompet standar_ dan lanjutkan dengan mengklik _Next_.

![image](assets/en/13.webp)

Dalam memilih `Keystore`, berhati-hatilah: untuk membuat tampilan Wallet pilih _Use a master key_. Kemudian lanjutkan dengan _Next_.

![image](assets/en/14.webp)

Rekatkan di sini `zpub` yang disalin dari Wallet secara offline dan yang kamu bawa ke komputer ini melalui media USB.

![image](assets/en/15.webp)

Akhiri dengan menetapkan kata sandi yang kuat untuk dompet ini juga, sebaiknya berbeda dari yang kamu gunakan pada dompet cold yang sesuai.

Setelah itu, tampilan dompet akan muncul bersama sebuah peringatan. Pesan ini mengingatkan kamu bahwa dompet ini bersifat watch-only, jadi kamu tidak bisa menggunakan dana yang ada di dalamnya.

**Catat dengan baik**: **kamu harus selalu memiliki private key untuk membuang UTXO dari Wallet ini**. Dengan sistem pencadangan yang baik, tidak akan sulit bagi kamu untuk tetap memiliki Bitcoin Anda sepenuhnya.

![image](assets/en/16.webp)

Peringatan ini akan muncul setiap kali kamu membuka Wallet ini. Klik _Ok_ dan mari kita lanjutkan ke langkah verifikasi.

## Verifikasi Dua Wallet

Seperti yang sudah kita bahas di awal panduan ini, dompet air-gapped dan dompet tampilan adalah dua portofolio dengan fungsi yang berbeda, tetapi **memiliki alamat yang sama**.

Jika kita melihat kedua Dompet berdampingan, secara visual kita melihat bahwa pada airgap Wallet terdapat simbol "seed", sedangkan pada jam tangan tidak ada. Bahkan detail ini akan membantu kamu mengingat bahwa tampilan Wallet Wallet tidak memiliki kunci pribadi.

![image](assets/en/17.webp)

Namun, untuk melakukan pemeriksaan pertama yang akurat, pilihlah menu `Alamat` di kedua Dompet: karena keduanya memiliki alamat yang sama, daftar alamat harus sama untuk keduanya.

![image](assets/en/18.webp)

⚠️ **PERHATIAN**: **tidak boleh ada jalan tengah; alamatnya harus sama. Jika berbeda, Anda harus menghapus semua pekerjaan yang telah dilakukan sejauh ini dan memulai dari awal**.

Sekarang kamu bisa melanjutkan dengan dua pemeriksaan berbeda. Pertama, coba hapus kedua dompet dan pulihkan dari awal di masing-masing komputer yang sesuai. Prosedur verifikasi untuk dompet tampilan sama persis seperti yang sudah dijelaskan sebelumnya.

Untuk dompet air-gapped, di layar keystore pilih _Saya sudah memiliki seed_ dan masukkan kata-kata dengan menyalinnya dari cadangan kertasmu.

Setelah uji coba "tanpa beban" selesai, kamu dapat mencoba melakukan transaksi dalam jumlah kecil dan langsung membelanjakannya.



## Transaksi Penerimaan dan Pengeluaran

Untuk mulai menggunakan Electrum air-gapped, kamu bisa melakukan transaksi penerimaan dengan jumlah kecil, lalu menggunakannya untuk mengirim ke alamatmu sendiri. Dengan cara ini, kamu bisa membiasakan diri dengan prosedurnya dan memverifikasi bahwa kamu memiliki kendali penuh atas dana tersebut.

**Catatan**: Aku tidak menyarankan kamu menyetor dana dalam jumlah besar ke dompet sebelum yakin bisa melakukan semua operasi dengan lancar.

Langkah-langkah berikut mungkin terlihat rumit pada awalnya, tapi jangan khawatir: setelah dicoba sekali, kamu akan menyadari bahwa semuanya hanya butuh beberapa menit.

Untuk menerima dana, gunakan dompet tampilan di komputer yang terhubung ke internet. Dari menu Terima, klik Buat permintaan agar Electrum menghasilkan alamat pertama yang tersedia, lalu gunakan alamat itu untuk mengirim beberapa sats.

![image](assets/en/19.webp)

![image](assets/en/20.webp)

Setelah transaksi dikirim, kamu akan melihat bahwa transaksi tersebut, seperti seharusnya, hanya terlihat di dompet tampilan dan tidak muncul di dompet air-gapped.

![image](assets/en/21.webp)

Setelah transaksimu menerima konfirmasi, kamu dapat menyiapkan biaya dan kemudian mencoba prosedur penandatanganan dari Wallet di luar jaringan. Kemudian siapkan transaksi pada watch-only dan tekan _Preview_ untuk memeriksanya

![image](assets/en/22.webp)

Kamu akan mendapatkan jendela transaksi lanjutan di mana kamu dapat melihatnya:

- transaksi tidak ditandatangani (`Status: Unsigned);
- perintah `Tanda` dan `Siaran` terhambat.

Satu-satunya hal yang dapat kamu lakukan adalah mengekspor transaksi apa adanya, membawanya ke air-gapped Wallet dan menandatanganinya.

Masukkan USB flash drive ke komputer kamu dan dari menu di bagian kiri bawah, pilih _Share_.

![image](assets/en/23.webp)

Setelah itu pilih _Save to file_.

![image](assets/en/24.webp)

Simpan transaksi ke stik USB.

Kamu akan melihat bahwa Electrum memberi nama file dengan angka pertama transaction ID, dan ekstensi file adalah `.PSBT`, yang berarti `Partially Signed Bitcoin Transaction`.

Ekstrak media dengan file `.PSBT` dan hubungkan ke komputer secara offline.

Dari airgap Wallet, sekarang pilih menu _Tools_, lalu _Load transaction_ dan ikuti From file_.

![image](assets/en/25.webp)

Dengan pengelola file, pilih `.PSBT` dari lokasinya.

![image](assets/en/29.webp)

Perangkat lunak di komputer yang offline akan otomatis membuka jendela transaksi lanjutan, yang sepenuhnya sama dengan yang kamu lihat di dompet tampilan. Statusnya `Tidak Ditandatangani`, tapi perbedaannya adalah tombol `Tandatangani` di sini aktif. Nah, di sinilah kamu harus mengeksekusinya.

![image](assets/en/26.webp)

![image](assets/en/27.webp)


Setelah transaksi ditandatangani, ingatlah bahwa Wallet kamu berada pada mesin offline. Oleh karena itu, meskipun kamu melihat perintah `Broadcast` aktif, Wallet kamu tidak akan dapat menyebarkan transaksi ke jaringan Bitcoin.

Yang perlu Anda lakukan sekarang adalah mengulangi operasi mengekspor transaksi yang telah ditandatangani ke stik usb, sehingga kamu bisa mengimpornya ke komputer yang terhubung ke Internet dan menyebarkannya.

Dari menu kiri bawah, pilih _Berbagi_ lagi dan kemudian _Simpan ke file_.

![image](assets/en/28.webp)

Sekarang file tersebut memiliki ekstensi yang berbeda: **alih-alih `.PSBT`, sekarang transaksi memiliki ekstensi `.txn`. Mulai sekarang, inilah cara Electrum untuk mengenali transaksi yang ditandatangani dan yang tidak ditandatangani**.

![image](assets/en/30.webp)

Untuk penyebaran akhir transaksi, keluarkan stik usb dari komputer off-line dan masukkan ke dalam komputer yang terhubung ke Internet.

Dari watch-only, ulangi prosedur import, yaitu dari menu _Tools_ pilih _Load transaction_ dan terakhir _From file_.

![image](assets/en/31.webp)

Electrum akan membuka jendela transaksi untukmu, yang sangat berbeda dari yang ditunjukkan sebelumnya pada Wallet ini, karena sekarang sudah ditandatangani (`Status: Signed`) dan perintah `Broadcast` dapat diakses.

Hal terakhir yang perlu kamu lakukan hanyalah itu:

![image](assets/en/32.webp)

## Kesimpulan

Pengujianmu sekarang sudah selesai. Jika kamu mengikuti panduan ini dan mendapatkan hasil yang sama, berarti kamu sudah berhasil membuat dompet cold dengan Electrum di dua komputer berbeda, yang siap digunakan untuk menyimpan Bitcoin.

Satu-satunya hal yang perlu kamu perhatikan ada dua:


1) **Jangan pernah menggunakan airgap Wallet ke alamat penerima generate**. Karena ini offline, maka akan selalu menawarkan Address pertama, yang sama dengan Address yang baru saja kamu gunakan untuk melakukan transaksi uji coba;

![image](assets/en/33.webp)

seperti yang dapat kamu lihat dari gambar di atas, Wallet offline tidak mengetahui sejarah Address-nya sendiri. Ia benar-benar buta dalam hal ini. **Satu-satunya tugas yang dapat dilakukannya untukmu adalah menyimpan kunci offline kamu dan menandatangani transaksi**_.

2) Gunakan USB flash drive yang didedikasikan hanya untuk tujuan ini, **jangan gunakan media yang sering kamu gunakan**. Alat sehari-hari lebih mungkin diserang cyber, dan secara tidak sengaja, kamu dapat menyerang komputer yang kamu jaga agar tetap terputus dari jaringan. Stik USB yang kamu gunakan hanya untuk tujuan ini memiliki peluang yang sangat kecil untuk melakukan kontak dengan PC kamu secara online, terutama jika kamu adalah penjaja yang tidak perlu mengeluarkan uang, sehingga mengurangi kemungkinan menerima dan kemudian mengirimkan virus, malware, dll.
