---
name: Samourai Wallet - Pemulihan
description: Bagaimana cara memulihkan bitcoin yang terjebak di Samourai Wallet?
---
![cover](assets/cover.webp)

Menyusul penangkapan para pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, beberapa fungsi aplikasi kini tidak beroperasi, dan pengguna yang tidak memiliki Dojo mereka sendiri tidak lagi dapat melakukan transmisi transaksi.

Setelah membantu beberapa pengguna dalam memulihkan bitcoin mereka dalam beberapa hari terakhir, saya percaya saya telah menemui sebagian besar masalah yang mungkin muncul selama pemulihan Samourai Wallet. Oleh karena itu, tutorial ini akan dimulai dengan laporan situasi untuk mengidentifikasi fungsi yang masih beroperasi dan yang tidak lagi tersedia dalam ekosistem Samourai Wallet dan perangkat lunak yang terpengaruh oleh insiden ini. Selanjutnya, kita akan melanjutkan langkah demi langkah untuk memulihkan Samourai Wallet menggunakan perangkat lunak Sparrow Wallet. Kita akan memeriksa semua hambatan potensial yang ditemui selama proses ini dan melihat solusi untuk mengatasinya. Akhirnya, di bagian terakhir, Anda akan menemukan potensi risiko terhadap privasi Anda menyusul penyitaan server.

*Terima kasih banyak kepada [@Louferlou](https://twitter.com/Louferlou), yang telah membantu beberapa pengguna dalam pemulihan mereka dan berbagi pengalamannya dengan saya, dan yang juga telah berkontribusi dalam pengujian untuk menentukan apa yang masih berfungsi.*

## Apakah Samourai Wallet masih berfungsi?

Ya, **aplikasi Samourai Wallet masih berfungsi**, tetapi dengan beberapa kondisi.

Pertama, aplikasi tersebut harus telah terpasang sebelumnya di smartphone Anda. Google Play Store telah menghapus aplikasi tersebut, dan APK di-hosting di situs web yang disita. Oleh karena itu, saat ini cukup rumit untuk menginstal Samourai. Anda mungkin menemukan APK secara online, tetapi saya menyarankan agar tidak mengunduhnya kecuali Anda yakin dengan sumbernya.

Mengingat halaman Samourai Wallet tidak lagi tersedia di Google Play Store, tidak mungkin untuk menonaktifkan pembaruan otomatis. Jika aplikasi kembali ke platform unduhan, akan bijaksana untuk **menonaktifkan pembaruan otomatis** sampai informasi lebih lanjut tersedia mengenai pengembangan kasus tersebut.

Jika Samourai Wallet sudah terpasang di smartphone Anda, Anda seharusnya masih bisa mengakses aplikasi tersebut. Untuk menggunakan fungsi dompet dari Samourai, sangat penting untuk menghubungkan Dojo. Sebelumnya, pengguna tanpa Dojo pribadi bergantung pada server Samourai untuk mengakses informasi blockchain Bitcoin dan untuk melakukan transmisi transaksi. Dengan penyitaan server ini, aplikasi tidak lagi dapat mengakses data ini.
Jika Anda tidak memiliki Dojo yang terhubung sebelumnya tetapi memiliki satu sekarang, Anda dapat mengaturnya untuk menggunakan aplikasi Samourai Anda lagi. Ini melibatkan pengecekan cadangan Anda, menghapus dompet (dompet, bukan aplikasi), dan memulihkan dompet dengan menghubungkan Dojo Anda ke aplikasi. Untuk lebih detail tentang langkah-langkah ini, Anda dapat berkonsultasi [tutorial ini, di bagian "_Menyiapkan Samourai Wallet Anda_": COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
Jika aplikasi Samourai Anda sudah terhubung ke Dojo Anda sendiri, maka bagian dompet bekerja dengan sempurna untuk Anda. Anda masih dapat melihat saldo Anda dan melakukan transmisi transaksi. Meskipun semua yang terjadi, saya pikir Samourai Wallet tetap menjadi perangkat lunak dompet mobile terbaik saat ini. Secara pribadi, saya berencana untuk terus menggunakannya.
Masalah utama yang mungkin Anda temui adalah ketidakmampuan untuk mengakses akun Whirlpool dari aplikasi. Biasanya, Samourai mencoba untuk membangun koneksi dengan Whirlpool CLI Anda dan memulai siklus coinjoin sebelum memberi Anda akses ke akun-akun ini. Namun, karena koneksi ini tidak lagi mungkin, aplikasi terus mencari tanpa pernah memberi Anda akses ke akun Whirlpool. Dalam kasus ini, Anda dapat memulihkan akun-akun ini di perangkat lunak dompet lain sambil hanya menyimpan akun deposit di Samourai.

### Apa saja alat yang masih tersedia di Samourai?

Di sisi lain, beberapa alat terpengaruh oleh penutupan server atau sepenuhnya tidak tersedia.

Mengenai alat pengeluaran individu, semuanya berfungsi normal asalkan, tentu saja, Anda memiliki Dojo Anda sendiri. Transaksi Stonewall normal (dan bukan Stonewall x2) berfungsi tanpa masalah.

Komentar di Twitter telah menyoroti bahwa privasi yang ditawarkan oleh transaksi Stonewall sekarang mungkin berkurang. Nilai tambah dari transaksi Stonewall terletak pada fakta bahwa strukturnya tidak dapat dibedakan dari transaksi Stonewall x2. Ketika seorang analis menemukan pola spesifik ini, mereka tidak dapat menentukan apakah itu Stonewall standar dengan satu pengguna atau Stonewall x2 yang melibatkan dua pengguna. Namun, seperti yang akan kita lihat dalam paragraf berikutnya, melakukan transaksi Stonewall x2 menjadi lebih kompleks karena ketidaktersediaan Soroban. Beberapa oleh karena itu berpikir bahwa seorang analis sekarang mungkin mengasumsikan bahwa setiap transaksi dengan struktur ini adalah Stonewall normal. Secara pribadi, saya tidak berbagi asumsi ini. Meskipun transaksi Stonewall x2 mungkin kurang sering terjadi (dan saya pikir mereka sudah sebelum insiden ini), fakta bahwa mereka masih mungkin dapat membatalkan seluruh analisis berdasarkan asumsi bahwa mereka tidak.

**[-> Pelajari lebih lanjut tentang transaksi Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Mengenai Ricochet, saya belum dapat memverifikasi apakah layanan ini masih beroperasi, karena tidak memiliki Dojo di Testnet, dan saya lebih memilih untuk tidak mengambil risiko menghabiskan `100 000 sats` ke dompet yang mungkin dikendalikan oleh otoritas. Jika Anda telah memiliki kesempatan untuk menguji alat ini baru-baru ini, saya mengundang Anda untuk menghubungi saya agar kami dapat memperbarui artikel ini.

Jika Anda perlu menggunakan Ricochet, perlu diketahui bahwa Anda selalu dapat melakukan operasi ini secara manual dengan perangkat lunak dompet apa pun. Untuk mempelajari cara melakukan berbagai lompatan secara manual dengan benar, saya merekomendasikan untuk berkonsultasi dengan artikel lain ini: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

Alat JoinBot tidak lagi beroperasi, karena sepenuhnya bergantung pada partisipasi dompet yang dikelola oleh Samourai.

Mengenai jenis transaksi kolaboratif lainnya, sering disebut sebagai "cahoots," mereka tetap mungkin, tetapi hanya secara manual. Sebelum penutupan server, Anda memiliki dua opsi untuk melakukan transaksi Stonewall x2 atau Stowaway (PayJoin):
- Gunakan jaringan Soroban untuk secara otomatis dan jarak jauh bertukar PSBTs;
- Atau lakukan pertukaran ini secara manual dengan memindai beberapa kode QR.

Setelah beberapa pengujian, tampaknya Soroban tidak lagi berfungsi. Untuk melakukan transaksi kolaboratif ini, pertukaran data harus dilakukan secara manual. Berikut adalah dua opsi untuk melakukan pertukaran ini:
- Jika Anda secara fisik dekat dengan kolaborator Anda, Anda dapat memindai kode QR secara berurutan;
Jika Anda berjarak jauh dari rekan kerja Anda, Anda dapat bertukar PSBT melalui saluran komunikasi eksternal ke aplikasi. Namun, berhati-hatilah, karena data yang terkandung dalam PSBT ini sensitif dalam hal privasi. Saya merekomendasikan menggunakan layanan pesan terenkripsi untuk memastikan kerahasiaan pertukaran.
**[-> Pelajari lebih lanjut tentang transaksi Stonewall x2.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Pelajari lebih lanjut tentang transaksi Stowaway.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Mengenai Whirlpool, protokol ini tampaknya tidak lagi berfungsi, bahkan untuk pengguna yang memiliki Dojo mereka sendiri. Saya telah memantau RoninDojo saya beberapa hari ini dan mencoba beberapa manipulasi dasar, tetapi CLI Whirlpool tidak dapat terhubung sejak server dimatikan.

Namun, saya tetap berharap bahwa protokol ini dapat diaktifkan kembali atau mungkin dibayangkan secara berbeda dalam beberapa minggu mendatang, tergantung pada bagaimana situasi berkembang. Jeda ini bisa menjadi kesempatan untuk menjelajahi pendekatan baru atau potensi peningkatan pada sistem ini.
### Alat eksternal apa yang masih tersedia?
Mengenai alat lain yang terkait dengan lingkungan Samourai, beberapa masih tersedia sementara yang lain tidak.

Situs analisis rantai gratis OXT.me sayangnya tidak lagi tersedia untuk saat ini.

Alat Statistik Whirlpool tidak lagi tersedia untuk diunduh, karena dihosting di GitLab Samourai. Bahkan jika Anda sebelumnya telah mengunduh alat Python ini secara lokal di mesin Anda, atau jika itu diinstal di node RoninDojo Anda, WST tidak akan berfungsi untuk saat ini. Memang, itu bergantung pada data yang disediakan oleh OXT.me untuk operasinya, dan situs ini tidak lagi dapat diakses. Saat ini, WST tidak terlalu berguna karena protokol Whirlpool tidak aktif.

Situs KYCP.org saat ini tidak lagi dapat diakses.

GitLab yang menghosting kode untuk alat Kalkulator Boltzmann Python juga telah disita. Saat ini, oleh karena itu tidak lagi mungkin untuk mengunduh alat ini. Tetapi jika Anda memiliki RoninDojo, Anda dapat terus menggunakan Kalkulator Boltzmann dengan cara yang sama seperti sebelumnya.

Mengenai RoninDojo, perangkat lunak node-in-box ini terus berfungsi dengan benar meskipun ketersediaan beberapa alat spesifik seperti CLI Whirlpool dan WST tidak ada. Ini masih dapat digunakan untuk perangkat lunak dompet lain berkat Fulcrum atau Electrs. Jika Anda ingin mendapatkan informasi lebih lanjut tentang RoninDojo atau jika Anda memiliki pertanyaan spesifik, saya mendorong Anda untuk bergabung dengan [grup Telegram mereka](https://t.me/RoninDojoNode).

Namun, kode sumber untuk RoninDojo saat ini tidak lagi dapat diakses, karena dihosting di GitLab Samourai. Oleh karena itu, tidak mungkin untuk menginstalnya secara manual di Raspberry Pi saat ini.

Mengenai perangkat lunak dompet hanya-baca Sentinel, situasinya mirip dengan aplikasi Samourai. Jika Anda memiliki Dojo Anda sendiri, Anda dapat terus menggunakan Sentinel tanpa masalah. Namun, jika Anda tidak memiliki Dojo, Anda tidak akan lagi dapat membuat koneksi. Tidak seperti Samourai, situs web Sentinel masih dapat diakses secara online. Tetapi berhati-hatilah dengan situs ini dan APK yang ditawarkan di sana, karena tidak jelas siapa yang saat ini mengontrol sumber daya ini.

### Apakah Sparrow Wallet terpengaruh?
Sparrow Wallet terus beroperasi seperti biasa, kecuali alat Samourai yang tidak lagi tersedia. Saat ini, tidak lagi mungkin untuk melakukan coinjoins melalui Sparrow. Demikian pula, alat pengeluaran kolaboratif tidak lagi dapat diakses, karena Sparrow tidak menawarkan opsi pertukaran manual PSBT, tidak seperti Samourai. Untuk semua fungsionalitas lainnya, Sparrow beroperasi tanpa masalah. Anda juga dapat menggunakan perangkat lunak ini untuk memulihkan dompet Samourai jika diperlukan.

## Bagaimana Cara Memulihkan Dompet Samourai?
Seperti yang telah kita lihat di bagian sebelumnya, jika Anda memiliki Dojo Anda sendiri, tidak selalu diperlukan untuk mengganti perangkat lunak. **Samourai tetap menjadi pilihan yang sangat baik untuk dompet hot** untuk pengeluaran sehari-hari Anda. Namun, jika Anda tidak memiliki Dojo atau jika Anda lebih memilih untuk memilih perangkat lunak lain, saya akan menjelaskan proses pemulihan lengkap, merinci setiap potensi hambatan yang mungkin Anda temui.

Dalam setiap kasus, penting untuk meluangkan waktu Anda dan memastikan untuk tidak membuat kesalahan. Ingat, tidak ada terburu-buru, karena Anda memegang kunci pribadi Anda, dan penyitaan server Samourai tidak mempengaruhi ini dengan cara apa pun. Apa pun yang terjadi, mereka jelas tidak dapat mengakses kunci pribadi Anda.

### Verifikasi frasa sandi

Untuk memulihkan dompet Anda, Anda harus memiliki frasa sandi Anda, bahkan jika Anda memilih pemulihan melalui file cadangan. Mulailah dengan memverifikasi validitas frasa sandi ini. Buka aplikasi Samourai Wallet Anda, klik pada ikon Paynym Anda di kiri atas, lalu pilih `Settings`.

![samourai](assets/1.webp)

Selanjutnya, klik pada `Troubleshooting` dan kemudian pada `Passphrase/backup test`.

![samourai](assets/2.webp)

Masukkan frasa sandi Anda dan klik `Ok`. Jika benar, Samourai akan mengonfirmasinya. Anda juga memiliki opsi untuk memverifikasi file cadangan jika Anda berencana menggunakannya nanti.

![samourai](assets/3.webp)

Langkah ini opsional tetapi disarankan. Ini mengonfirmasi bahwa frasa sandi benar, menghilangkan sumber potensial masalah nanti. Jika Samourai menunjukkan bahwa frasa sandi salah pada tahap ini, pemulihan tidak akan mungkin dilakukan. Pastikan Anda telah memasukkan frasa sandi dengan benar dan periksa lagi.

### Opsi 1: Memulihkan dompet di Sparrow dengan file cadangan

Sejak versi 1.8.6 dari Sparrow Wallet, dimungkinkan untuk langsung mengimpor dompet Samourai Anda menggunakan file teks cadangan bernama `samourai.txt`, yang secara otomatis dihasilkan oleh aplikasi Anda. File ini berisi semua informasi yang diperlukan untuk memulihkan dompet Anda dan dienkripsi dengan frasa sandi Anda untuk keamanan.

Jika Anda memilih opsi ini, Anda akan memerlukan file `samourai.txt` Anda yang terbaru dan frasa sandi Anda. Untuk menghasilkan file ini di Samourai Wallet, klik pada tiga titik kecil di kanan atas, lalu pilih `Export wallet backup`.

![samourai](assets/4.webp)
Selanjutnya, pilih `Export to Clipboard`. Setelah itu, Anda perlu mentransfer file ini ke PC Anda secara aman. Karena file dienkripsi, tetapi frasa sandi saja sudah cukup untuk mendekripsinya, penting untuk mengambil tindakan pencegahan selama transmisinya. Jika Anda memilih transfer langsung sebagai teks biasa, Anda perlu membuat file `samourai.txt` di PC Anda dan menempelkan isi clipboard ke dalamnya. Alternatif lainnya adalah langsung mengambil file `samourai.txt` dari file yang tersimpan di ponsel Anda.
Setelah Anda memiliki akses ke file di PC Anda, buka Sparrow Wallet, klik pada tab `File`, dan pilih `Import Wallet` untuk memulai mengimpor dompet Anda.

![samourai](assets/5.webp)
Gulir ke bawah ke `Samourai Backup`, klik pada `Import File`, dan kemudian pilih file `samourai.txt` Anda.
![samourai](assets/6.webp)

Sparrow kemudian akan meminta Anda memasukkan kata sandi untuk mendekripsi file tersebut. Kata sandi ini sebenarnya adalah frasa sandi Anda. Masukkan di kolom yang sesuai dan klik pada `Import`.

![samourai](assets/7.webp)

Jika pada tahap ini, dompet Anda tidak muncul, mungkin Anda membuat kesalahan saat menyalin file `samourai.txt` atau saat memasukkan frasa sandi. Anda dapat mengunjungi bagian pemecahan masalah untuk mendapatkan bantuan lebih lanjut.

![samourai](assets/8.webp)

Untuk tipe skrip, jika Anda belum mengonfigurasi skrip lain di Samourai, Anda seharusnya hanya menggunakan SegWit V0 (Native SegWit / P2WPKH). Pertahankan skrip default ini dan klik pada `Import`.

![samourai](assets/9.webp)

Namai dompet Anda, misalnya, "Samourai Recovery", dan kemudian klik pada `Create Wallet`.

![samourai](assets/10.webp)

Sparrow kemudian akan meminta Anda memilih kata sandi. Kata sandi ini hanya melindungi akses ke dompet Anda di PC ini dan tidak berkaitan dengan derivasi kunci dompet Anda. Pastikan untuk memilih kata sandi yang kuat, catat untuk mengingatnya, dan klik pada `Set Password`.

![samourai](assets/11.webp)

Sparrow kemudian akan mendapatkan kunci dompet Anda dan mencari transaksi yang sesuai.

![samourai](assets/12.webp)

Untuk saat ini, hanya akun deposito Anda yang dapat diakses. Jika Anda hanya menggunakan Samourai untuk akun ini, Anda seharusnya melihat semua dana Anda. Namun, jika Anda juga menggunakan Whirlpool, Anda perlu mendapatkan akun `premix`, `postmix`, dan `badbank`. Di Sparrow, cukup klik pada tab `Settings`, kemudian pada `Add Accounts...`.

![samourai](assets/13.webp)
Di jendela yang terbuka, pilih `Whirlpool Accounts` dari menu dropdown, kemudian klik pada `OK`.
![samourai](assets/14.webp)

Anda kemudian akan melihat berbagai akun Whirlpool Anda muncul, dan Sparrow akan mendapatkan kunci yang diperlukan untuk menggunakan bitcoin yang terkait.

![samourai](assets/15.webp)

Jika Anda menggunakan perangkat lunak lain selain Sparrow, seperti Electrum, untuk memulihkan dompet Samourai Anda, berikut adalah indeks akun Whirlpool untuk pemulihan manual:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Anda sekarang memiliki akses ke bitcoin Anda di Sparrow. Jika Anda memerlukan bantuan menggunakan Sparrow Wallet, Anda juga dapat melihat [tutorial khusus kami](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Saya juga merekomendasikan untuk secara manual mengimpor label yang Anda asosiasikan dengan UTXO Anda di Samourai. Ini akan memungkinkan Anda untuk melakukan kontrol koin yang efektif di Sparrow selanjutnya.

### Opsi 2: Memulihkan dompet di Sparrow dengan frasa pemulihan mnemonik

Jika Anda tidak ingin melakukan pemulihan dengan file cadangan, Anda dapat memilih metode yang lebih tradisional dengan hanya menggunakan frasa pemulihan 12 kata dan frasa sandi Anda. Opsi kedua ini seringkali lebih sederhana.
Untuk memulai, pastikan Anda memiliki frasa pemulihan dan kata sandi Anda di tangan. Kemudian, buka perangkat lunak Sparrow Wallet, klik pada tab `File`, dan pilih `Import Wallet` untuk memulai proses impor dompet Anda.
![samourai](assets/16.webp)

Pilih `Mnemonic Words (BIP39)` dan, di menu dropdown, klik pada `Use 12 Words`.

![samourai](assets/17.webp)

Masukkan 12 kata dari frasa pemulihan Anda dalam urutan yang benar.

![samourai](assets/18.webp)

Jika Sparrow menampilkan pesan `Invalid Checksum`, ini menunjukkan bahwa checksum dari frasa pemulihan tidak valid, yang kemungkinan berarti Anda membuat kesalahan saat memasukkan kata-katanya.

![samourai](assets/19.webp)

Jika frasa Anda benar, centang kotak `Use Passphrase?` dan masukkan kata sandi Anda di kolom yang disediakan. Akhirnya, jika semuanya tampak benar, klik pada tombol `Discover Wallet`.

![samourai](assets/20.webp)

Namai dompet Anda, misalnya, "Samourai Recovery", kemudian klik pada `Create Wallet`.

![samourai](assets/21.webp)
Sparrow kemudian akan meminta Anda untuk memilih kata sandi. Kata sandi ini hanya melindungi akses ke dompet Anda di PC ini dan tidak terkait dengan derivasi kunci dompet Anda. Pastikan untuk memilih kata sandi yang kuat, tulis untuk mengingatnya, dan klik pada `Set Password`.
![samourai](assets/22.webp)

Sparrow kemudian akan mendapatkan kunci untuk dompet Anda dan mencari transaksi yang sesuai.

![samourai](assets/23.webp)

Jika pada tahap ini, dompet Anda tidak muncul, mungkin Anda membuat kesalahan saat memasukkan kata sandi atau frasa pemulihan. Anda dapat mengonsultasikan bagian pemecahan masalah yang khusus untuk bantuan lebih lanjut.

Untuk saat ini, hanya akun deposito Anda yang dapat diakses. Jika Anda hanya menggunakan Samourai untuk akun ini, Anda seharusnya dapat melihat semua dana Anda. Namun, jika Anda juga menggunakan Whirlpool, Anda perlu mendapatkan akun `premix`, `postmix`, dan `badbank`. Di Sparrow, cukup klik pada tab `Settings`, kemudian pada `Add Accounts...`.

![samourai](assets/24.webp)

Di jendela yang terbuka, pilih `Whirlpool Accounts` dari daftar dropdown, kemudian klik pada `OK`.

![samourai](assets/25.webp)

Anda kemudian akan melihat berbagai akun Whirlpool Anda muncul, dan Sparrow akan mendapatkan kunci yang diperlukan untuk menggunakan bitcoin yang terkait.

![samourai](assets/26.webp)

Jika Anda menggunakan perangkat lunak lain seperti Electrum untuk memulihkan dompet Samourai Anda, berikut adalah indeks akun Whirlpool untuk pemulihan manual:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Anda sekarang memiliki akses ke bitcoin Anda di Sparrow. Jika Anda memerlukan bantuan menggunakan Sparrow Wallet, Anda juga dapat mengonsultasikan [tutorial khusus kami](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Saya juga merekomendasikan untuk secara manual mengimpor label yang Anda asosiasikan dengan UTXO Anda di Samourai. Ini akan memungkinkan Anda untuk melakukan kontrol koin yang efektif di Sparrow selanjutnya.

### Apa masalah umum yang dihadapi?
Setelah membantu beberapa orang dalam beberapa hari terakhir, saya percaya saya telah menemui sebagian besar masalah yang dapat mencegah pemulihan dompet Anda. Jika Anda masih tidak dapat mengakses dompet Anda meskipun telah mengikuti tutorial sebelumnya, berikut adalah beberapa rekomendasi tambahan. Pertama dan terutama, untuk pemulihan agar berhasil, sangat penting bahwa frasa pemulihan itu benar. Jika Anda tidak dapat menemukan frasa 12 kata Anda, Anda dapat menggunakan *opsi 1* untuk memulihkan dari file cadangan Samourai. Anda juga dapat mengakses frasa pemulihan Anda langsung di Samourai Wallet dengan menavigasi ke `Settings`, kemudian `Wallet`, dan akhirnya memilih `Show 12-word recovery phrase`.

Selanjutnya, kesalahan ketik dalam frasa sandi Anda selama pemulihan akan menghasilkan kunci turunan yang salah, yang akan mencegah pemulihan dompet Anda di Sparrow. **Frasa sandi harus benar-benar akurat!**

Untuk mengatasi ini, saya pertama-tama menyarankan Anda untuk memeriksa validitas frasa sandi Anda di aplikasi Samourai seperti yang dijelaskan di bagian "_Verify the passphrase_" dari artikel ini:
1. **Validasi di Samourai:** Jika Samourai mengonfirmasi bahwa frasa sandi itu benar, coba pemulihan lagi dari awal, pastikan untuk memasukkan frasa sandi di Sparrow dengan akurat tanpa kesalahan;
2. **Kesalahan Frasa Sandi:** Jika Samourai menunjukkan bahwa frasa sandi itu salah, tidak ada gunanya melanjutkan percobaan di Sparrow. Selama frasa sandi yang benar tidak ditemukan, pemulihan dompet Anda tidak mungkin. Jika Anda telah kehilangan frasa sandi Anda secara permanen, jaga aplikasi Samourai Anda tetap aman. Yang dapat Anda lakukan hanyalah berharap server dihidupkan ulang sehingga Anda dapat melakukan pengeluaran langsung dari aplikasi tanpa memerlukan pemulihan. **Jangan mencoba untuk menghubungkan Dojo dalam kasus ini**, karena ini akan menyiratkan pengaturan ulang dompet Anda di Samourai, yang memerlukan akses ke frasa sandi.

Di antara kesalahan lain yang ditemui, banyak yang terkait dengan konfigurasi jaringan di Sparrow.

Pertama, pastikan bahwa Sparrow dikonfigurasi dengan benar dalam mode `mainnet` daripada dalam mode `testnet`. Memang, jika Sparrow mencari transaksi Anda di Testnet, itu tidak akan menemukan apa-apa, karena dompet Anda berada di Mainnet. Testnet adalah versi alternatif dari Bitcoin, digunakan semata-mata untuk pengujian dan pengembangan, dan beroperasi pada jaringan terpisah dari jaringan utama (Mainnet), dengan blok dan transaksi sendiri. Untuk memeriksa jaringan mana yang Anda gunakan, klik pada tab `Tools`, kemudian pada `Restart In`. Jika opsi `Mainnet` ditampilkan, maka Anda tidak berada di jaringan utama. Pilih itu untuk memulai ulang Sparrow di Mainnet, dan kemudian mulai proses pemulihan Anda lagi.

![samourai](assets/27.webp)
Beberapa juga mengalami kesulitan menghubungkan Sparrow ke node mereka. Di bagian bawah kanan Sparrow, sebuah sakelar berwarna menunjukkan apakah perangkat lunak Anda terhubung dengan benar ke node Bitcoin. Untuk mengambil transaksi Samourai Anda, sangat penting bahwa perangkat lunak terhubung dengan baik. Periksa bahwa sakelar diaktifkan, seperti pada gambar saya di bawah ini (kuning untuk node publik, hijau untuk Bitcoin Core, dan biru untuk server Electrum).
![samourai](assets/28.webp)

Jika sakelar tidak diaktifkan, klik padanya untuk mengaktifkan kembali koneksi.

![samourai](assets/29.webp)

Jika masalah berlanjut, berikut adalah beberapa solusi yang mungkin:
- Jika Anda mencoba untuk terhubung ke server Electrum Anda sendiri (biru) atau Bitcoin Core Anda (hijau) dan Sparrow tidak dapat terhubung, periksa informasi koneksi di bawah `File > Preferences... > Server`;

![samourai](assets/30.webp)
- Jika masalah koneksi terus berlanjut, itu bisa disebabkan oleh sinkronisasi node Anda yang tidak lengkap. Pastikan node dan indexer Anda tersinkronisasi 100%. Jika perlu sebagai langkah terakhir, putuskan koneksi node Anda dari Sparrow dan sambungkan ke node publik; - Jika Anda sudah terhubung ke node publik dan koneksi gagal, coba ganti node dengan memilih yang lain dari daftar dropdown.

![samourai](assets/31.webp)

Jika Anda telah berhasil memulihkan dompet Anda, tetapi terasa tidak lengkap, mungkin ada masalah terkait dengan derivasi.

Masalah bisa terjadi jika Anda menggunakan akun deposit Samourai Anda dengan tipe skrip yang berbeda dari `P2WPKH`. Secara default, Samourai menggunakan tipe skrip ini, tetapi jika Anda telah mengubahnya secara manual, Anda juga harus menyesuaikan ini saat memulihkan di Sparrow.

Untuk mendapatkan cabang untuk tipe skrip lain, Anda perlu mengulangi proses pemulihan untuk setiap tipe skrip yang digunakan. Untuk ini, pergi ke `File > New Wallet` di Sparrow, pilih tipe skrip lain dari daftar dropdown, klik pada `New or Imported Software Wallet`, dan ikuti langkah yang sama seperti dalam tutorial awal.

![samourai](assets/32.webp)

Masalah derivasi lain yang saya temui terkait dengan nilai Gap Limit. Nilai ini memberitahu Sparrow setelah berapa banyak alamat kosong harus berhenti mendapatkan alamat baru. Jika setelah pemulihan, Anda melihat bahwa beberapa transaksi hilang, ini bisa disebabkan oleh Gap Limit yang terlalu rendah. Untuk menyelesaikannya, pergi ke akun yang bermasalah, misalnya akun postmix (jika beberapa akun terkait, ulangi operasi ini untuk masing-masing).

![samourai](assets/33.webp)

Klik pada tab `Settings` kemudian pada tombol `Advanced...`.
![samourai](assets/34.webp)
Secara bertahap tingkatkan nilai Gap Limit, misalnya, saya menetapkannya menjadi `400` di sini. Kemudian, klik tombol `Close`.

![samourai](assets/35.webp)

Klik pada `Apply` untuk menyelesaikan. Sparrow kemudian akan mendapatkan sejumlah alamat yang lebih besar dan mencari dana di dalamnya, yang seharusnya membantu memulihkan semua transaksi Anda.

![samourai](assets/36.webp)

Itu mencakup berbagai masalah pemulihan yang saya temui selama beberapa hari terakhir. Jika, setelah mencoba semua solusi ini, Anda masih mengalami masalah, saya mengundang Anda untuk bergabung dengan [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) untuk meminta bantuan. Saya secara rutin mengunjungi Discord ini dan akan senang membantu jika saya memiliki solusinya. Pengguna bitcoin lainnya juga akan dapat berbagi pengalaman mereka dan menawarkan bantuan. **Dalam hal apapun, sangat penting untuk menjaga kerahasiaan frasa pemulihan, file cadangan, dan passphrase Anda**. Jangan berbagi dengan siapapun, karena ini bisa memungkinkan mereka untuk mencuri bitcoin Anda.

Setelah pemulihan selesai, Anda sekarang memiliki akses ke bitcoin Anda. Itu hal yang baik, tetapi mungkin tidak cukup. Memang, penyitaan server menimbulkan risiko baru yang potensial bagi privasi Anda. Dalam bagian berikut, kami akan memeriksa risiko ini secara detail dan menguraikan langkah-langkah pencegahan yang harus diambil untuk melindungi privasi Anda.

## Apa konsekuensi untuk privasi transaksi Anda?

### Sebagai pengguna Samourai tanpa Dojo

Jika Anda menggunakan Dompet Samourai tanpa telah menghubungkan Dojo Anda sendiri, xpubs Anda harus dikomunikasikan ke server Samourai agar aplikasi dapat berfungsi. Dengan penyitaan server ini, mungkin saja otoritas sekarang memiliki akses ke xpubs tersebut.
Skenario ini tetap hipotetis. Kita tidak tahu apakah xpub ini telah direkam, apakah penyimpanan potensial telah dihancurkan, apakah otoritas telah memulihkannya, dan apakah mereka berencana menggunakannya untuk analisis rantai. Namun, dalam situasi seperti itu, bijaksana untuk mempertimbangkan skenario terburuk, di mana otoritas memiliki xpub pengguna yang tidak menghubungkan Dojo mereka sendiri. Sebagai referensi, xpub adalah rangkaian karakter yang berisi semua elemen yang diperlukan untuk menghasilkan kunci publik anak (kunci publik + kode rantai). Ini digunakan dalam dompet deterministik hierarkis untuk menghasilkan alamat penerima dan mengamati transaksi akun tanpa mengungkapkan kunci privat yang terkait. Ini memungkinkan, misalnya, pembuatan dompet "hanya-pantau". Namun, mengungkapkan xpub dapat membahayakan privasi pengguna, karena mereka memungkinkan pihak ketiga untuk melacak transaksi dan melihat saldo akun yang terkait.
Siapa pun yang mengetahui xpub Anda dapat melihat semua alamat penerima dompet Anda, yang digunakan di masa lalu, dan yang akan dihasilkan di masa depan.

Bagi pengguna tanpa Dojo, kebocoran xpub Anda memiliki dua konsekuensi utama:
- Coinjoins yang mungkin telah Anda lakukan menjadi tidak efektif dari sudut pandang privasi bagi siapa pun yang mengetahui xpub Anda, sehingga koin Anda kehilangan semua anonset;
- Orang ini juga dapat melacak semua alamat penerima Samourai Wallet Anda.

Oleh karena itu, penting untuk mempertimbangkan skenario terburuk dan berpisah dengan dompet ini, yang berpotensi terkompromi dalam hal privasi. Untuk melakukan ini, buat dompet baru dari awal dengan perangkat lunak lain, seperti Sparrow Wallet. Setelah memverifikasi validitas cadangan Anda, transfer semua dana Anda dengan melakukan transaksi. Meskipun operasi ini tidak memutuskan tautan pelacakan koin Anda, ini akan mencegah otoritas mengetahui dengan pasti alamat dompet baru Anda.

Selama operasi transfer ini, saya menyarankan untuk menghindari konsolidasi koin Anda. Jika kita asumsikan bahwa xpub Anda terkompromi, konsolidasi tidak akan berdampak dari sudut pandang orang yang memiliki akses ke xpub ini, karena privasi Anda sudah terkompromi dengan mereka. Namun, saya menyarankan Anda untuk tidak terlalu banyak mengkonsolidasikan koin Anda terutama untuk melindungi privasi Anda dari orang lain. Dalam kasus terburuk, hanya otoritas yang mungkin memiliki akses ke xpub Anda, tetapi sisanya dunia tidak tahu tentang mereka. Jadi, dari sudut pandang orang lain, mengkonsolidasikan koin Anda dapat secara signifikan membahayakan privasi Anda karena Heuristik Kepemilikan Input Bersama (CIOH).

Akhirnya, untuk secara definitif memutus pelacakan, pertimbangkan juga melakukan coinjoins dari dompet baru ini.
**Peringatan:** Hanya mengambil kembali dompet Samourai Anda di Sparrow Wallet tidak cukup. Diperlukan untuk membuat dompet baru yang sepenuhnya baru dengan frasa pemulihan baru jika Anda ingin menghindari menggunakan xpub yang mungkin telah bocor. Jika Anda mengimpor benih yang ada ke Sparrow, Anda hanya mengubah perangkat lunak manajemen dompet, tetapi dompet tetap sama.

### Sebagai pengguna Sparrow atau Samourai dengan Dojo

Jika dompet Anda hanya dikelola di Sparrow Wallet, xpub Anda tidak mungkin telah bocor, apakah Anda menggunakan node publik atau node Bitcoin Anda sendiri. Demikian pula, jika Anda menggunakan aplikasi Samourai dan selalu menghubungkan aplikasi ini ke Dojo Anda sendiri sejak pembuatan dompet Anda, xpub Anda juga aman.
Namun, jika Anda telah menggunakan dompet yang sama selama periode **tanpa Dojo Anda sendiri** dan kemudian dengan Dojo Anda sendiri, ada kemungkinan server Samourai mungkin telah memiliki akses ke xpubs Anda, dan oleh karena itu otoritas bisa mengetahuinya. Jika Anda berada dalam situasi khusus ini, saya menyarankan Anda untuk mengikuti rekomendasi dari bagian sebelumnya dan menganggap xpubs Anda sebagai yang telah dikompromikan.
Bagi mereka yang selalu menggunakan Sparrow atau Samourai dengan Dojo mereka sendiri, risiko utamanya adalah anonsets dari koin Anda berpotensi bisa berkurang. Bayangkan, dalam skenario terburuk, bahwa semua pengguna tanpa Dojo memiliki xpubs mereka di tangan otoritas, maka jalur koin mereka melalui siklus coinjoin bisa dilacak oleh otoritas tersebut.

Untuk mengilustrasikan ini, mari kita ambil contoh konkret. Bayangkan Anda berpartisipasi dalam siklus coinjoin pertama, diikuti oleh dua siklus coinjoin tambahan di hilir. Jika xpubs dari pengguna tanpa Dojo tidak bocor, maka anonset prospektif dari koin Anda akan menjadi 13.

![samourai](assets/37.webp)

Namun, jika kita menganggap bahwa xpubs telah bocor dan bahwa Anda bertemu dengan pengguna tanpa dojo selama coinjoin awal, dan kemudian 2 selama coinjoin hilir pertama, maka anonset prospektif Anda hanya akan menjadi 10 bukan 13 dari sudut pandang otoritas.

![samourai](assets/38.webp)
Penurunan potensial dalam anonset ini kompleks untuk diukur, karena tergantung pada banyak faktor, dan setiap koin terpengaruh secara berbeda. Misalnya, pengguna tanpa Dojo yang ditemui dalam siklus awal mempengaruhi anonset prospektif jauh lebih banyak daripada yang ditemui dalam siklus selanjutnya. Untuk memberi Anda gambaran tentang situasi, yang tetap hipotetis, statistik terbaru yang disediakan oleh Samourai menunjukkan bahwa antara 85% hingga 90% koin yang terlibat dalam coinjoins berasal dari pengguna dengan Dojo, Sparrow, atau Bitcoin Keeper, yaitu, pengguna yang, bahkan dalam skenario terburuk, tidak akan melihat xpubs mereka bocor.
Meskipun angka-angka ini sulit untuk diverifikasi, mereka tampak konsisten bagi saya karena dua alasan:
- Sparrow Wallet banyak digunakan;
- Sebagian besar perangkat lunak node-in-box menawarkan implementasi Dojo, dan perangkat lunak mainstream seperti Umbrel sangat populer saat ini.

Dengan demikian, beberapa aspek perlu dipertimbangkan. Jika privasi koin Anda vis-à-vis otoritas sangat penting bagi Anda, akan bijaksana untuk bersiap untuk skenario terburuk, dan sulit untuk menjamin 100% bahwa siklus coinjoin Whirlpool Anda tidak bisa dilacak karena kebocoran potensial xpubs dari pengguna tanpa Dojo. Meskipun asumsi ini sangat tidak mungkin, itu bukan tidak mungkin.

Di sisi lain, jika privasi koin Anda vis-à-vis otoritas yang berpotensi memiliki xpubs ini tidak penting bagi Anda, maka situasinya bisa dipertimbangkan secara berbeda.

Saya menyebutkan "vis-à-vis otoritas" karena penting untuk diingat bahwa hanya otoritas yang menyita server yang berpotensi mengetahui xpubs ini. Jika tujuan Anda menggunakan coinjoin adalah untuk mencegah tukang roti Anda dapat mengikuti dana Anda, maka dia tidak lebih tahu daripada sebelum penyitaan server.
Akhirnya, sangat penting untuk mempertimbangkan anonset awal koin Anda, sebelum penyitaan server. Mari kita ambil contoh sebuah koin yang telah mencapai anonset prospektif sebesar 40.000; penurunan potensial dalam anonset ini kemungkinan kecil. Memang, dengan anonset dasar yang sudah sangat tinggi, tidak mungkin kehadiran beberapa pengguna tanpa Dojo dapat secara radikal mengubah situasi. Namun, jika koin Anda memiliki anonset 40, maka kebocoran potensial ini bisa serius mempengaruhi anonset Anda dan berpotensi memungkinkan pelacakan. Dengan alat WST sekarang tidak berfungsi menyusul penutupan OXT.me, Anda hanya dapat memperkirakan anonset ini. Untuk anonset retrospektif, tidak terlalu banyak yang perlu dikhawatirkan karena model Whirlpool memastikan bahwa itu sangat tinggi dari coinjoin pertama, berkat warisan dari rekan-rekan Anda. Satu-satunya kasus di mana ini bisa menjadi masalah adalah jika koin Anda tidak telah diremix selama beberapa tahun dan itu dicampur di awal peluncuran sebuah kolam. Mengenai anonset prospektif, Anda dapat memeriksa durasi koin Anda telah tersedia untuk coinjoins. Jika sudah beberapa bulan, maka kemungkinan memiliki anonset prospektif yang sangat tinggi. Sebaliknya, jika ditambahkan ke kolam hanya beberapa jam sebelum server disita, maka anonset prospektifnya kemungkinan sangat rendah.
[**-> Pelajari lebih lanjut tentang anonset dan metode perhitungannya.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Aspek lain yang perlu dipertimbangkan adalah dampak konsolidasi pada anonset koin yang telah dicampur. Mengingat akun Whirlpool tidak lagi dapat diakses melalui aplikasi Samourai, kemungkinan banyak pengguna telah mentransfer dompet mereka ke perangkat lunak lain dan mencoba menarik dana mereka dari Whirlpool. Khususnya, akhir pekan lalu, ketika biaya transaksi di jaringan Bitcoin relatif tinggi, ada insentif teknis dan ekonomi yang kuat untuk mengkonsolidasikan koin pasca-campuran. Ini berarti kemungkinan banyak pengguna telah melakukan konsolidasi yang signifikan.

Masalah dengan konsolidasi pasca-campuran ini adalah mereka selalu mengurangi anonset, tidak hanya untuk pengguna yang melakukan konsolidasi tetapi juga untuk pengguna yang mereka temui selama siklus coinjoin mereka. Meskipun saya belum dapat memverifikasi atau mengkuantifikasi fenomena ini secara tepat, insentif ekonomi terkait biaya transaksi pada saat itu dapat membuat kita berasumsi bahwa anonset berpotensi lebih rendah.

### Sebagai Pengguna Sentinel

Operasi jaringan dari aplikasi dompet hanya-pantau Sentinel mirip dengan Samourai. Untuk mengakses informasi dompet Anda, aplikasi harus mentransmisikan xpubs, kunci publik, dan alamat yang telah Anda berikan ke Dojo. Jika Anda selalu menggunakan Dojo Anda sendiri di Sentinel, tidak ada masalah, dan Anda dapat terus menggunakan aplikasi tanpa khawatir. Namun, jika Anda bergantung pada server Samourai untuk Sentinel Anda, kemungkinan xpubs Anda telah terpapar. Dalam kasus ini, disarankan untuk mengikuti proses perubahan dompet yang sama yang direkomendasikan untuk Samourai Wallet ketika terhubung ke server Samourai.

Dalam kejadian yang tidak mungkin bahwa Anda menggunakan Dojo Anda dengan Samourai tetapi tidak dengan Sentinel, akan lebih bijaksana untuk menganggap bahwa xpubs Anda terkompromi.

## Kesimpulan
Terima kasih telah membaca artikel ini sampai selesai. Jika Anda merasa ada informasi yang hilang atau jika Anda memiliki saran, jangan ragu untuk menghubungi saya untuk berbagi pikiran Anda. Selain itu, jika Anda memerlukan bantuan lebih lanjut dalam memulihkan Samourai Wallet Anda meskipun telah mengikuti tutorial ini, saya mengundang Anda untuk bergabung dengan [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) untuk meminta bantuan. Saya secara rutin mengunjungi Discord ini dan akan sangat senang membantu Anda jika saya memiliki solusinya. Bitcoiner lainnya juga akan dapat berbagi pengalaman mereka dan menawarkan dukungan mereka. **Dalam setiap kasus, sangat penting untuk menjaga kerahasiaan frasa pemulihan, file cadangan, dan passphrase Anda**. Jangan berbagi dengan siapapun, karena ini dapat memungkinkan mereka untuk mencuri bitcoin Anda.