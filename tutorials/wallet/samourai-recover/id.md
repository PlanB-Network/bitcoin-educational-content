---
name: Samourai Wallet - Recover
description: Bagaimana cara memulihkan bitcoin yang terjebak di Samourai Wallet?
---
![cover](assets/cover.webp)

Menyusul penangkapan para pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, beberapa fungsi aplikasi kini tidak lagi beroperasi, dan pengguna yang tidak memiliki Dojo sendiri tidak lagi bisa menyiarkan transaksi.

Setelah membantu beberapa pengguna memulihkan bitcoin mereka dalam beberapa hari terakhir, aku merasa sudah menemukan sebagian besar kendala yang mungkin muncul saat proses pemulihan Samourai Wallet. Karena itu, tutorial ini akan diawali dengan laporan situasi untuk mengidentifikasi fungsi mana yang masih berjalan dan mana yang sudah tidak tersedia lagi dalam ekosistem Samourai Wallet, serta perangkat lunak yang terdampak oleh insiden ini. Selanjutnya, kita akan masuk langkah demi langkah untuk memulihkan Samourai Wallet menggunakan perangkat lunak Sparrow Wallet. Kita akan membahas semua hambatan potensial yang mungkin muncul selama proses tersebut dan melihat cara mengatasinya. Terakhir, di bagian penutup, kamu akan menemukan potensi risiko terhadap privasimu setelah penyitaan server tersebut.

*Terima kasih banyak kepada [@Louferlou](https://twitter.com/Louferlou), yang telah membantu beberapa pengguna dalam pemulihan mereka dan berbagi pengalamannya denganku, dan yang juga telah berkontribusi dalam pengujian untuk menentukan apa yang masih berfungsi.*

## Apakah Samourai Wallet masih berfungsi?

Ya, **aplikasi Samourai Wallet masih berfungsi**, tetapi dengan beberapa syarat.

Pertama, aplikasinya harus sudah terpasang sebelumnya di smartphone kamu. Google Play Store telah menghapus aplikasi tersebut, dan file APK sebelumnya di-hosting di situs web yang kini disita. Karena itu, saat ini cukup sulit untuk menginstal Samourai. Kamu mungkin menemukan APK beredar secara online, tetapi aku menyarankan untuk tidak mengunduhnya kecuali kamu benar-benar yakin dengan sumbernya.

Karena halaman Samourai Wallet sudah tidak tersedia lagi di Google Play Store, tidak ada lagi opsi untuk mengelola pembaruan dari sana. Jika suatu saat aplikasi ini kembali ke platform unduhan, akan lebih aman untuk **menonaktifkan pembaruan otomatis** sampai ada kejelasan lebih lanjut mengenai perkembangan kasusnya.

Jika Samourai Wallet sudah terpasang di smartphone kamu, seharusnya kamu masih bisa mengakses aplikasinya. Untuk menggunakan fungsi wallet dari Samourai, sangat penting untuk terhubung ke Dojo. Sebelumnya, pengguna yang tidak memiliki Dojo pribadi bergantung pada server Samourai untuk mengakses data blockchain Bitcoin dan untuk menyiarkan transaksi. Setelah server tersebut disita, aplikasi tidak lagi bisa mengakses data ini.

Jika sebelumnya kamu tidak memiliki Dojo yang terhubung tetapi sekarang sudah punya, kamu tetap bisa mengonfigurasinya agar aplikasi Samourai dapat digunakan kembali. Prosesnya melibatkan verifikasi cadangan kamu, menghapus wallet (wallet-nya, bukan aplikasinya), lalu memulihkannya kembali dengan menghubungkan Dojo ke aplikasi. Untuk detail langkah-langkahnya, kamu bisa melihat tutorial pada bagian "_Menyiapkan Samourai Wallet Kamu_": COINJOIN - DOJO.

Jika aplikasi Samourai kamu sudah terhubung ke Dojo sendiri, maka bagian wallet akan tetap berfungsi normal. Kamu masih bisa melihat saldo dan menyiarkan transaksi. Terlepas dari situasi yang ada, menurutku Samourai Wallet tetap menjadi salah satu perangkat lunak wallet mobile terbaik saat ini. Secara pribadi, aku berencana untuk terus menggunakannya.

Masalah utama yang mungkin kamu hadapi adalah ketidakmampuan mengakses akun Whirlpool dari aplikasi. Biasanya, Samourai mencoba membangun koneksi dengan Whirlpool CLI milikmu dan memulai siklus coinjoin sebelum memberikan akses ke akun-akun tersebut. Namun, karena koneksi ini sudah tidak memungkinkan, aplikasi akan terus mencoba terhubung tanpa pernah benar-benar memberi akses ke akun Whirlpool. Dalam kondisi seperti ini, kamu bisa memulihkan akun-akun tersebut di perangkat lunak wallet lain, sementara akun deposit tetap disimpan di Samourai.

### Apa saja alat yang masih tersedia di Samourai?

Di sisi lain, beberapa alat terdampak oleh penutupan server atau bahkan sepenuhnya tidak tersedia.

Untuk alat pengeluaran individu, semuanya tetap berfungsi normal selama kamu memiliki Dojo sendiri. Transaksi Stonewall biasa, bukan Stonewall x2, tetap berjalan tanpa kendala.

Beberapa komentar di Twitter menyoroti bahwa tingkat privasi dari transaksi Stonewall sekarang mungkin berkurang. Nilai tambah transaksi Stonewall terletak pada strukturnya yang tidak dapat dibedakan dari Stonewall x2. Ketika seorang analis menemukan pola khusus ini, mereka tidak bisa memastikan apakah itu Stonewall standar dengan satu pengguna atau Stonewall x2 yang melibatkan dua pengguna. Namun, seperti yang akan kita bahas di paragraf berikutnya, melakukan transaksi Stonewall x2 kini menjadi lebih rumit karena Soroban tidak lagi tersedia. Karena itu, sebagian orang berpendapat bahwa analis mungkin akan menganggap setiap transaksi dengan struktur tersebut sebagai Stonewall biasa. Secara pribadi, aku tidak sependapat dengan asumsi ini. Meskipun transaksi Stonewall x2 mungkin menjadi lebih jarang, dan menurutku memang sudah jarang bahkan sebelum insiden ini, fakta bahwa transaksi tersebut masih mungkin dilakukan sudah cukup untuk menggugurkan analisis yang hanya bergantung pada asumsi bahwa Stonewall x2 tidak lagi terjadi.

**[-> Pelajari lebih lanjut tentang transaksi Stonewall.](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Mengenai Ricochet, aku belum bisa memverifikasi apakah layanan ini masih beroperasi, karena aku tidak memiliki Dojo di Testnet, dan aku lebih memilih untuk tidak mengambil risiko menghabiskan `100 000 sats` ke wallet yang mungkin dikendalikan oleh otoritas. Jika kamu sempat menguji alat ini baru-baru ini, aku mengundangmu untuk menghubungiku agar kita bisa memperbarui artikel ini.

Jika kamu perlu menggunakan Ricochet, perlu diketahui bahwa kamu selalu bisa melakukan operasi ini secara manual dengan perangkat lunak wallet apa pun. Untuk mempelajari cara melakukan beberapa lompatan secara manual dengan benar, aku sarankan membaca artikel berikut ini: [**RICOCHET**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

Alat JoinBot sudah tidak lagi beroperasi, karena sepenuhnya bergantung pada partisipasi wallet yang dikelola oleh Samourai.

Untuk jenis transaksi kolaboratif lainnya, yang sering disebut sebagai "cahoots", transaksi tersebut masih bisa dilakukan, tetapi hanya secara manual. Sebelum penutupan server, kamu punya dua opsi untuk melakukan transaksi Stonewall x2 atau Stowaway (PayJoin):
- Menggunakan jaringan Soroban untuk secara otomatis dan jarak jauh bertukar PSBT;
- Atau melakukan pertukaran ini secara manual dengan memindai beberapa kode QR.

Setelah beberapa pengujian, tampaknya Soroban sudah tidak berfungsi. Jadi, untuk melakukan transaksi kolaboratif ini, pertukaran data harus dilakukan secara manual. Berikut dua opsi yang bisa kamu gunakan:
- Jika kamu berada secara fisik dekat dengan kolaborator, kamu bisa memindai kode QR secara bergantian;
- Jika kamu berjauhan, kamu bisa bertukar PSBT melalui saluran komunikasi eksternal di luar aplikasi.

Namun, perlu hati-hati karena data yang terdapat dalam PSBT bersifat sensitif dari sisi privasi. Aku menyarankan menggunakan layanan pesan terenkripsi agar pertukaran data tetap rahasia.
**[-> Pelajari lebih lanjut tentang transaksi Stonewall x2.](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**

**[-> Pelajari lebih lanjut tentang transaksi Stowaway.](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stowaway-48a5c711-ee3d-44db-b812-c55913080eab)**

Mengenai Whirlpool, protokol ini tampaknya sudah tidak berfungsi lagi, bahkan bagi pengguna yang memiliki Dojo sendiri. Selama beberapa hari terakhir aku memantau RoninDojo milikku dan mencoba beberapa pengujian dasar, tetapi Whirlpool CLI tidak bisa terhubung sejak server dimatikan.

Meski begitu, aku tetap berharap protokol ini bisa diaktifkan kembali atau mungkin dirancang ulang dalam beberapa minggu ke depan, tergantung bagaimana situasinya berkembang. Jeda ini bisa menjadi kesempatan untuk mengeksplorasi pendekatan baru atau potensi peningkatan pada sistem tersebut.

### Alat eksternal apa yang masih tersedia?

Untuk alat lain yang terkait dengan ekosistem Samourai, sebagian masih tersedia sementara yang lain tidak.

Situs analisis chain gratis OXT.me untuk sementara sudah tidak dapat diakses.

Alat Whirlpool Statistics Tool tidak lagi tersedia untuk diunduh karena sebelumnya di-hosting di GitLab Samourai. Bahkan jika kamu sudah mengunduh alat Python ini secara lokal di komputermu, atau jika sudah terpasang di node RoninDojo, WST tetap tidak akan berfungsi saat ini. Alat ini bergantung pada data dari OXT.me, dan karena situs tersebut tidak bisa diakses, WST menjadi tidak berguna, terlebih lagi karena protokol Whirlpool sendiri sedang tidak aktif.

Situs KYCP.org juga saat ini tidak dapat diakses.

GitLab yang meng-host kode untuk alat Python Boltzmann Calculator juga telah disita. Karena itu, saat ini sudah tidak memungkinkan lagi untuk mengunduh alat tersebut. Namun, jika kamu memiliki RoninDojo, kamu masih bisa menggunakan Boltzmann Calculator seperti sebelumnya.

Untuk RoninDojo sendiri, perangkat lunak node-in-a-box ini tetap berfungsi normal meskipun beberapa alat spesifik seperti Whirlpool CLI dan WST tidak tersedia. RoninDojo masih bisa digunakan bersama perangkat lunak wallet lain melalui Fulcrum atau Electrs. Jika kamu ingin tahu lebih lanjut tentang RoninDojo atau punya pertanyaan spesifik, aku sarankan untuk bergabung dengan [grup Telegram mereka](https://t.me/RoninDojoNode).

Namun, kode sumber RoninDojo saat ini sudah tidak dapat diakses karena sebelumnya di-hosting di GitLab Samourai. Jadi, untuk saat ini tidak memungkinkan menginstalnya secara manual di Raspberry Pi.

Untuk perangkat lunak wallet watch-only Sentinel, situasinya mirip dengan aplikasi Samourai. Jika kamu memiliki Dojo sendiri, kamu masih bisa menggunakan Sentinel tanpa kendala. Namun, jika kamu tidak memiliki Dojo, kamu tidak akan bisa lagi membuat koneksi. Berbeda dengan Samourai, situs web Sentinel masih bisa diakses secara online. Meski begitu, tetap berhati-hati dengan situs tersebut dan file APK yang ditawarkan, karena tidak jelas siapa yang saat ini mengendalikan sumber daya itu.

### Apakah Sparrow Wallet terpengaruh?

Sparrow Wallet tetap beroperasi seperti biasa, kecuali untuk alat-alat Samourai yang memang sudah tidak tersedia. Saat ini sudah tidak mungkin lagi melakukan coinjoin melalui Sparrow. Begitu juga dengan alat pengeluaran kolaboratif, yang tidak lagi bisa digunakan karena Sparrow tidak menyediakan opsi pertukaran PSBT secara manual seperti Samourai. Untuk fungsi lainnya, Sparrow tetap berjalan normal. Kamu juga bisa menggunakan perangkat lunak ini untuk memulihkan wallet Samourai jika diperlukan.

## Bagaimana Cara Memulihkan Wallet Samourai?

Seperti yang sudah kita bahas sebelumnya, jika kamu memiliki Dojo sendiri, tidak selalu perlu mengganti perangkat lunak. **Samourai tetap menjadi pilihan yang sangat baik sebagai hot wallet** untuk kebutuhan pengeluaran harianmu. Namun, jika kamu tidak memiliki Dojo atau ingin beralih ke perangkat lunak lain, di bagian ini aku akan menjelaskan proses pemulihan secara lengkap, termasuk berbagai kendala yang mungkin kamu temui.

Dalam semua kasus, luangkan waktu dan pastikan kamu tidak melakukan kesalahan. Tidak ada yang perlu diburu-buru, karena kamu memegang kunci privatmu sendiri, dan penyitaan server Samourai sama sekali tidak memengaruhi hal tersebut. Apa pun yang terjadi, mereka jelas tidak bisa mengakses kunci privatmu.

### Verifikasi seedphrase

Untuk memulihkan wallet, kamu harus memiliki seedphrase, bahkan jika kamu memilih untuk memulihkannya melalui file cadangan. Mulailah dengan memverifikasi bahwa seedphrase tersebut valid. Buka aplikasi Samourai Wallet, ketuk ikon Paynym di kiri atas, lalu pilih `Settings`.

![samourai](assets/1.webp)

Selanjutnya, klik pada `Troubleshooting` dan kemudian pada `Passphrase/backup test`.

![samourai](assets/2.webp)

Masukkan frasa sandi dan klik `Ok`. Jika benar, Samourai akan mengonfirmasinya. Kamu juga memiliki opsi untuk memverifikasi file cadangan jika Anda berencana menggunakannya nanti.

![samourai](assets/3.webp)

Langkah ini opsional tetapi sangat disarankan. Tujuannya untuk memastikan seedphrase yang kamu simpan memang benar, sehingga menghindari potensi masalah saat proses pemulihan nanti. Jika pada tahap ini Samourai menunjukkan bahwa seedphrase salah, maka pemulihan tidak akan bisa dilakukan. Pastikan kamu memasukkan seedphrase dengan tepat dan periksa kembali dengan teliti.

### Opsi 1: Memulihkan wallet di Sparrow dengan file cadangan

Sejak versi 1.8.6 Sparrow Wallet, kamu bisa langsung mengimpor wallet Samourai menggunakan file cadangan teks bernama `samourai.txt`, yang secara otomatis dibuat oleh aplikasi. File ini berisi semua informasi yang dibutuhkan untuk memulihkan wallet dan dienkripsi menggunakan seedphrase untuk alasan keamanan.

Jika kamu memilih opsi ini, kamu memerlukan file `samourai.txt` terbaru dan seedphrase milikmu. Untuk menghasilkan file tersebut di Samourai Wallet, ketuk tiga titik di kanan atas, lalu pilih `Export wallet backup`.

![samourai](assets/4.webp)
Selanjutnya, pilih `Export to Clipboard`. Setelah itu, kamu perlu memindahkan file ini ke PC secara aman. Meskipun file tersebut dienkripsi, seedphrase saja sudah cukup untuk mendekripsinya, jadi tetap penting mengambil langkah pencegahan selama proses transfer. Jika kamu memilih untuk mentransfernya sebagai teks biasa, buat file `samourai.txt` di PC lalu tempelkan isi clipboard ke dalamnya. Alternatifnya, kamu bisa langsung mengambil file `samourai.txt` dari berkas yang tersimpan di ponselmu.

Setelah file tersebut tersedia di PC, buka Sparrow Wallet, klik tab `File`, lalu pilih `Import Wallet` untuk mulai mengimpor wallet.

![samourai](assets/5.webp)
Gulir ke bawah ke `Samourai Backup`, klik pada `Import File`, dan kemudian pilih file `samourai.txt` Anda.
![samourai](assets/6.webp)

Sparrow kemudian akan memintamu memasukkan kata sandi untuk mendekripsi file tersebut. Kata sandi ini sebenarnya adalah passphrase kamu. Masukkan di kolom yang sesuai dan klik pada `Import`.

![samourai](assets/7.webp)

Jika pada tahap ini, dompet kamu tidak muncul, mungkin kamu membuat kesalahan saat menyalin file `samourai.txt` atau saat memasukkan passphrase. Kamu bisa mengunjungi bagian pemecahan masalah untuk mendapatkan bantuan lebih lanjut.

![samourai](assets/8.webp)

Untuk tipe skrip, jika kamu belum mengonfigurasi skrip lain di Samourai, kamu seharusnya hanya menggunakan SegWit V0 (Native SegWit / P2WPKH). Pertahankan skrip default ini dan klik pada `Import`.

![samourai](assets/9.webp)

Namai dompet kamu, misalnya, "Samourai Recovery", dan kemudian klik pada `Create Wallet`.

![samourai](assets/10.webp)

Sparrow kemudian akan meminta kamu memilih kata sandi. Kata sandi ini hanya melindungi akses ke dompet kamu di PC ini dan tidak berkaitan dengan derivasi kunci dompet. Pastikan untuk memilih kata sandi yang kuat, catat untuk mengingatnya, dan klik pada `Set Password`.

![samourai](assets/11.webp)

Sparrow kemudian akan mendapatkan kunci dompet kamu dan mencari transaksi yang sesuai.

![samourai](assets/12.webp)

Untuk saat ini, hanya akun deposit yang bisa kamu akses. Jika kamu memang hanya menggunakan Samourai untuk akun ini, seharusnya seluruh dana sudah terlihat. Namun, jika kamu juga menggunakan Whirlpool, kamu perlu menambahkan akun `premix`, `postmix`, dan `badbank`.  

Di Sparrow, klik tab `Settings`, lalu pilih `Add Accounts...`.

![samourai](assets/13.webp)
Di jendela yang terbuka, pilih `Whirlpool Accounts` dari menu dropdown, kemudian klik pada `OK`.
![samourai](assets/14.webp)

Kemudian kamu akan melihat berbagai akun Whirlpool kamu muncul, dan Sparrow akan mendapatkan kunci yang diperlukan untuk menggunakan bitcoin yang terkait.

![samourai](assets/15.webp)

Jika Anda menggunakan perangkat lunak lain selain Sparrow, seperti Electrum, untuk memulihkan dompet Samourai Anda, berikut adalah indeks akun Whirlpool untuk pemulihan manual:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Sekarang kamu memiliki akses ke bitcoin Anda di Sparrow. Jika kamu memerlukan bantuan menggunakan Sparrow Wallet, Ankamu juga dapat melihat [tutorial khusus kami](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

Aku juga menyarankan untuk mengimpor secara manual label yang sebelumnya kamu kaitkan dengan UTXO di Samourai. Dengan begitu, kamu bisa melakukan coin control secara efektif di Sparrow nantinya.

### Opsi 2: Memulihkan wallet di Sparrow dengan seedphrase mnemonik

Jika kamu tidak ingin menggunakan file cadangan, kamu bisa memilih metode yang lebih klasik dengan hanya memakai seedphrase 12 kata dan passphrase milikmu. Opsi kedua ini sering kali terasa lebih sederhana.

Untuk memulai, pastikan kamu sudah menyiapkan seedphrase dan passphrase. Lalu buka perangkat lunak Sparrow Wallet, klik tab `File`, dan pilih `Import Wallet` untuk memulai proses impor wallet.
![samourai](assets/16.webp)

Pilih `Mnemonic Words (BIP39)` dan, di menu dropdown, klik pada `Use 12 Words`.

![samourai](assets/17.webp)

Masukkan 12 kata dari frasa pemulihan dalam urutan yang benar.

![samourai](assets/18.webp)

Jika Sparrow menampilkan pesan `Invalid Checksum`, ini menunjukkan bahwa checksum dari frasa pemulihan tidak valid, yang kemungkinan berarti kamu membuat kesalahan saat memasukkan kata-katanya.

![samourai](assets/19.webp)

Jika frasa benar, centang kotak `Use Passphrase?` dan masukkan kata sandi Anda di kolom yang disediakan. Akhirnya, jika semuanya tampak benar, klik pada tombol `Discover Wallet`.

![samourai](assets/20.webp)

Namai dompet kamu, misalnya, "Samourai Recovery", kemudian klik pada `Create Wallet`.

![samourai](assets/21.webp)
Sparrow kemudian akan meminta kamu membuat kata sandi. Kata sandi ini hanya berfungsi untuk melindungi akses ke wallet di PC tersebut dan tidak ada kaitannya dengan proses derivasi kunci wallet. Pastikan kamu memilih kata sandi yang kuat, simpan atau catat agar tidak lupa, lalu klik `Set Password`.
![samourai](assets/22.webp)

Sparrow kemudian akan mendapatkan kunci untuk dompet dan mencari transaksi yang sesuai.

![samourai](assets/23.webp)

Jika pada tahap ini wallet kamu tidak muncul, kemungkinan ada kesalahan saat memasukkan passphrase atau seedphrase. Kamu bisa melihat bagian pemecahan masalah untuk mendapatkan bantuan lebih lanjut.

Untuk sementara, hanya akun deposit yang bisa kamu akses. Jika kamu memang hanya menggunakan Samourai untuk akun ini, seharusnya seluruh dana sudah terlihat. Namun, jika kamu juga menggunakan Whirlpool, kamu perlu menambahkan akun `premix`, `postmix`, dan `badbank`. Di Sparrow, klik tab `Settings`, lalu pilih `Add Accounts...`.
![samourai](assets/24.webp)

Di jendela yang terbuka, pilih `Whirlpool Accounts` dari daftar dropdown, kemudian klik pada `OK`.

![samourai](assets/25.webp)

Kemudian kamu akan melihat berbagai akun Whirlpool kamu muncul, dan Sparrow akan mendapatkan kunci yang diperlukan untuk menggunakan bitcoin yang terkait.

![samourai](assets/26.webp)

Jika kamu menggunakan perangkat lunak lain seperti Electrum untuk memulihkan dompet Samourai, berikut adalah indeks akun Whirlpool untuk pemulihan manual:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Sekarang kamu memiliki akses ke bitcoin Anda di Sparrow. Jika kamu memerlukan bantuan menggunakan Sparrow Wallet, Anda juga dapat mengonsultasikan [tutorial khusus kami](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

Aku juga menyarankan untuk mengimpor secara manual label yang sebelumnya kamu kaitkan dengan UTXO di Samourai. Dengan begitu, kamu bisa melakukan coin control secara efektif di Sparrow nantinya.

### Apa masalah umum yang sering muncul?

Setelah membantu beberapa orang dalam beberapa hari terakhir, aku merasa sudah menemukan sebagian besar kendala yang bisa menghambat pemulihan wallet. Jika kamu masih belum bisa mengakses wallet meskipun sudah mengikuti tutorial sebelumnya, berikut beberapa rekomendasi tambahan.

Pertama dan paling penting, agar pemulihan berhasil, seedphrase harus benar. Jika kamu tidak dapat menemukan 12 kata tersebut, kamu bisa menggunakan *opsi 1* untuk memulihkan melalui file cadangan Samourai. Kamu juga bisa melihat seedphrase langsung di Samourai Wallet dengan masuk ke `Settings`, lalu `Wallet`, kemudian pilih `Show 12-word recovery phrase`.

Selain itu, kesalahan pengetikan pada passphrase saat proses pemulihan akan menghasilkan kunci turunan yang berbeda, sehingga wallet tidak bisa dipulihkan di Sparrow. **Passphrase harus benar-benar akurat!**

Untuk mengatasinya, pertama-tama periksa validitas passphrase di aplikasi Samourai seperti dijelaskan pada bagian "_Verify the passphrase_" dalam artikel ini:

1. **Validasi di Samourai:** Jika Samourai mengonfirmasi bahwa passphrase benar, ulangi proses pemulihan dari awal dan pastikan kamu memasukkan passphrase di Sparrow dengan tepat tanpa kesalahan;
2. **Passphrase salah:** Jika Samourai menunjukkan bahwa passphrase salah, tidak ada gunanya melanjutkan percobaan di Sparrow. Selama passphrase yang benar belum ditemukan, wallet tidak bisa dipulihkan. Jika kamu benar-benar kehilangan passphrase secara permanen, jaga aplikasi Samourai tetap aman. Satu-satunya harapan adalah server diaktifkan kembali sehingga kamu bisa melakukan pengeluaran langsung dari aplikasi tanpa perlu pemulihan. **Jangan mencoba menghubungkan Dojo dalam kondisi ini**, karena itu akan mengatur ulang wallet di Samourai dan memerlukan akses ke passphrase.

Kesalahan lain yang cukup sering terjadi berkaitan dengan konfigurasi jaringan di Sparrow.

Pastikan Sparrow dikonfigurasi dalam mode `mainnet`, bukan `testnet`. Jika Sparrow mencari transaksi di Testnet, tentu tidak akan menemukan apa pun karena wallet kamu berada di Mainnet. Testnet adalah jaringan alternatif Bitcoin yang digunakan hanya untuk pengujian dan pengembangan, dengan blockchain dan transaksinya sendiri yang terpisah dari jaringan utama. Untuk memeriksa jaringan yang sedang digunakan, klik tab `Tools`, lalu pilih `Restart In`. Jika opsi `Mainnet` tersedia, berarti kamu sedang tidak berada di jaringan utama. Pilih opsi tersebut untuk memulai ulang Sparrow di Mainnet, lalu ulangi proses pemulihan.

![samourai](assets/27.webp)
Beberapa orang juga mengalami kendala saat menghubungkan Sparrow ke node mereka. Di bagian kanan bawah Sparrow, ada indikator berwarna yang menunjukkan apakah perangkat lunak sudah terhubung dengan benar ke node Bitcoin. Agar transaksi Samourai kamu bisa dimuat, Sparrow harus benar-benar terhubung ke node. Pastikan indikator tersebut aktif seperti pada contoh di bawah ini: kuning untuk node publik, hijau untuk Bitcoin Core, dan biru untuk server Electrum.
![samourai](assets/28.webp)

Jika sakelar tidak diaktifkan, klik padanya untuk mengaktifkan kembali koneksi.

![samourai](assets/29.webp)

Jika masalah masih berlanjut, berikut beberapa solusi yang bisa kamu coba:

- Jika kamu mencoba terhubung ke server Electrum sendiri (biru) atau ke Bitcoin Core (hijau) dan Sparrow gagal terhubung, periksa kembali informasi koneksi di `File > Preferences... > Server`;

![samourai](assets/30.webp)
- Jika masalah koneksi tetap terjadi, kemungkinan node atau indexer kamu belum tersinkronisasi sepenuhnya. Pastikan keduanya sudah sinkron 100%. Jika perlu sebagai langkah terakhir, putuskan koneksi node tersebut dari Sparrow lalu sambungkan ke node publik;

- Jika kamu memang sudah menggunakan node publik dan koneksi tetap gagal, coba pilih node lain dari daftar dropdown yang tersedia.
![samourai](assets/31.webp)

Jika kamu sudah berhasil memulihkan wallet tetapi isinya terasa tidak lengkap, kemungkinan ada masalah terkait jalur derivasi.

Masalah ini bisa muncul jika akun deposit Samourai kamu menggunakan tipe skrip yang berbeda dari `P2WPKH`. Secara default, Samourai memang memakai tipe skrip ini. Namun, jika sebelumnya kamu pernah mengubahnya secara manual, maka pengaturan yang sama juga harus dipilih saat melakukan pemulihan di Sparrow.

Untuk mengakses cabang dengan tipe skrip lain, kamu perlu mengulangi proses pemulihan untuk setiap tipe skrip yang pernah digunakan. Caranya, buka `File > New Wallet` di Sparrow, pilih tipe skrip yang berbeda dari daftar dropdown, klik `New or Imported Software Wallet`, lalu ikuti langkah yang sama seperti pada tutorial sebelumnya.

![samourai](assets/32.webp)

Masalah derivasi lain yang pernah aku temui berkaitan dengan nilai Gap Limit. Parameter ini memberi tahu Sparrow setelah berapa banyak alamat kosong ia harus berhenti melakukan pencarian alamat baru. Jika setelah pemulihan kamu merasa ada beberapa transaksi yang tidak muncul, bisa jadi penyebabnya adalah Gap Limit yang terlalu rendah.

Untuk mengatasinya, buka akun yang bermasalah, misalnya akun `postmix`. Jika beberapa akun terdampak, ulangi langkah ini untuk masing-masing akun.

![samourai](assets/33.webp)

Klik pada tab `Settings` kemudian pada tombol `Advanced...`.
![samourai](assets/34.webp)
Secara bertahap tingkatkan nilai Gap Limit, misalnya, aku menetapkannya menjadi `400` di sini. Kemudian, klik tombol `Close`.

![samourai](assets/35.webp)

Klik pada `Apply` untuk menyelesaikan. Sparrow kemudian akan mendapatkan sejumlah alamat yang lebih besar dan mencari dana di dalamnya, yang seharusnya membantu memulihkan semua transaksi Anda.

![samourai](assets/36.webp)

Itu mencakup berbagai masalah pemulihan yang aku temui dalam beberapa hari terakhir. Jika setelah mencoba semua solusi ini kamu masih mengalami kendala, kamu bisa bergabung ke [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) untuk meminta bantuan. Aku cukup sering aktif di sana dan akan dengan senang hati membantu jika aku tahu solusinya. Pengguna bitcoin lain juga bisa berbagi pengalaman dan membantu. **Dalam kondisi apa pun, sangat penting untuk menjaga kerahasiaan seedphrase, file cadangan, dan passphrase milikmu.** Jangan pernah membagikannya kepada siapa pun, karena itu bisa memungkinkan mereka mencuri bitcoin kamu.

Setelah proses pemulihan selesai, sekarang kamu sudah kembali memiliki akses ke bitcoin kamu. Itu tentu kabar baik, tetapi mungkin belum cukup. Penyitaan server ini berpotensi menimbulkan risiko baru terhadap privasimu. Di bagian berikut, kita akan membahas risiko tersebut secara rinci dan langkah pencegahan yang bisa kamu ambil untuk melindungi privasi.

## Apa konsekuensinya terhadap privasi transaksi kamu?

### Sebagai pengguna Samourai tanpa Dojo

Jika kamu menggunakan Samourai Wallet tanpa pernah menghubungkannya ke Dojo sendiri, maka xpub kamu harus dikirim ke server Samourai agar aplikasi bisa berfungsi. Dengan penyitaan server tersebut, ada kemungkinan otoritas kini memiliki akses ke xpub tersebut.

Skenario ini masih bersifat hipotesis. Kita tidak tahu apakah xpub tersebut benar-benar disimpan, apakah penyimpanannya telah dihancurkan, apakah berhasil dipulihkan oleh otoritas, atau apakah akan digunakan untuk analisis chain. Namun, dalam situasi seperti ini, lebih bijak untuk mempertimbangkan skenario terburuk, yaitu otoritas memiliki xpub pengguna yang tidak menggunakan Dojo sendiri.

Sebagai pengingat, xpub adalah rangkaian karakter yang berisi semua elemen yang diperlukan untuk menghasilkan kunci publik turunan, yaitu kunci publik dan chain code. Dalam wallet deterministik hierarkis, xpub digunakan untuk menghasilkan alamat penerima dan memantau transaksi tanpa mengungkapkan kunci privat. Inilah yang memungkinkan pembuatan wallet watch-only. Namun, jika xpub bocor, privasi pengguna bisa terganggu karena pihak ketiga dapat melacak transaksi dan melihat saldo akun terkait.

Siapa pun yang mengetahui xpub kamu dapat melihat semua alamat penerima wallet kamu, baik yang sudah digunakan maupun yang akan dihasilkan di masa depan.

Bagi pengguna tanpa Dojo, kebocoran xpub memiliki dua konsekuensi utama:
- Coinjoin yang mungkin sudah kamu lakukan menjadi tidak efektif dari sisi privasi bagi siapa pun yang mengetahui xpub tersebut, sehingga koin kamu kehilangan anonset;
- Pihak tersebut juga dapat melacak semua alamat penerima Samourai Wallet kamu.

Karena itu, sebaiknya pertimbangkan skenario terburuk dan berhenti menggunakan wallet ini yang berpotensi sudah terkompromi dari sisi privasi. Buat wallet baru dari awal menggunakan perangkat lunak lain, misalnya Sparrow Wallet. Setelah memastikan cadangan kamu valid, transfer seluruh dana melalui transaksi on-chain. Meskipun langkah ini tidak memutus histori pelacakan koin sebelumnya, setidaknya ini mencegah otoritas mengetahui dengan pasti alamat wallet baru kamu.

Saat melakukan transfer ini, aku menyarankan untuk menghindari konsolidasi koin secara berlebihan. Jika kita berasumsi xpub kamu sudah terkompromi, konsolidasi tidak mengubah apa pun bagi pihak yang memiliki xpub tersebut karena privasi kamu sudah terbuka bagi mereka. Namun, konsolidasi bisa merusak privasi kamu terhadap pihak lain. Dalam skenario terburuk, mungkin hanya otoritas yang memiliki xpub tersebut, sementara pihak lain tidak. Dari sudut pandang pihak lain, konsolidasi dapat merusak privasi karena Heuristik Kepemilikan Input Bersama.

Untuk benar-benar meningkatkan kembali tingkat privasi, kamu juga bisa mempertimbangkan melakukan coinjoin dari wallet baru tersebut.

**Peringatan:** Hanya memulihkan wallet Samourai di Sparrow Wallet tidaklah cukup. Kamu perlu membuat wallet yang benar-benar baru dengan seedphrase baru jika ingin menghindari penggunaan xpub yang mungkin sudah bocor. Jika kamu hanya mengimpor seed yang sama ke Sparrow, kamu memang mengganti perangkat lunak pengelola, tetapi wallet yang digunakan tetap sama.

### Sebagai pengguna Sparrow atau Samourai dengan Dojo

Jika wallet kamu hanya dikelola di Sparrow Wallet, kecil kemungkinan xpub kamu pernah bocor, baik kamu menggunakan node publik maupun node Bitcoin sendiri. Begitu juga jika kamu menggunakan aplikasi Samourai dan sejak awal selalu menghubungkannya ke Dojo sendiri, maka xpub kamu tetap aman.

Namun, jika kamu pernah menggunakan wallet yang sama dalam periode **tanpa Dojo sendiri**, lalu kemudian menggunakannya dengan Dojo, ada kemungkinan server Samourai pernah menerima xpub kamu, sehingga secara teoritis bisa diakses oleh otoritas. Jika kamu berada dalam situasi ini, sebaiknya ikuti rekomendasi di bagian sebelumnya dan anggap xpub kamu sudah terkompromi.

Bagi mereka yang selalu menggunakan Sparrow atau Samourai dengan Dojo sendiri, risiko utamanya adalah anonset koin kamu berpotensi berkurang. Bayangkan dalam skenario terburuk bahwa semua pengguna tanpa Dojo memiliki xpub mereka di tangan otoritas, maka jalur koin mereka melalui siklus coinjoin bisa dilacak oleh otoritas tersebut.

Sebagai ilustrasi, bayangkan kamu ikut satu siklus coinjoin awal, lalu dua siklus tambahan setelahnya. Jika xpub pengguna tanpa Dojo tidak bocor, maka anonset prospektif koin kamu bisa mencapai 13.

![samourai](assets/37.webp)
Namun, jika kita mengasumsikan bahwa xpub memang telah bocor dan kamu bertemu dengan satu pengguna tanpa Dojo pada coinjoin pertama, lalu dua pengguna tanpa Dojo pada coinjoin hilir berikutnya, maka anonset prospektif kamu dari sudut pandang otoritas hanya menjadi 10, bukan 13.

![samourai](assets/38.webp)
Penurunan potensial dalam anonset ini cukup kompleks untuk diukur, karena bergantung pada banyak faktor dan setiap koin terdampak secara berbeda. Misalnya, pengguna tanpa Dojo yang kamu temui pada siklus awal akan jauh lebih memengaruhi anonset prospektif dibandingkan yang ditemui pada siklus berikutnya. Sebagai gambaran, yang tetap bersifat hipotetis, statistik terakhir yang dibagikan oleh Samourai menunjukkan bahwa antara 85% hingga 90% koin yang ikut coinjoin berasal dari pengguna dengan Dojo, Sparrow, atau Bitcoin Keeper, yaitu pengguna yang bahkan dalam skenario terburuk tidak akan mengalami kebocoran xpub.

Meskipun angka ini sulit diverifikasi secara independen, menurutku angka tersebut cukup masuk akal karena dua alasan:
- Sparrow Wallet digunakan secara luas;
- Sebagian besar perangkat lunak node-in-a-box menawarkan implementasi Dojo, dan solusi populer seperti Umbrel banyak digunakan saat ini.

Karena itu, ada beberapa hal yang perlu kamu pertimbangkan. Jika privasi koin kamu terhadap otoritas sangat penting, maka sebaiknya kamu bersiap menghadapi skenario terburuk. Sulit untuk menjamin 100% bahwa siklus coinjoin Whirlpool kamu tidak bisa dilacak jika memang terjadi kebocoran xpub dari pengguna tanpa Dojo. Meskipun kemungkinan ini kecil, tetap saja bukan tidak mungkin.

Sebaliknya, jika privasi terhadap otoritas yang berpotensi memiliki xpub tersebut bukan prioritas utama bagimu, maka situasinya bisa dinilai secara berbeda.

Aku menekankan “terhadap otoritas” karena penting untuk diingat bahwa hanya otoritas yang menyita server yang berpotensi memiliki akses ke xpub tersebut. Jika tujuan kamu melakukan coinjoin adalah agar tukang roti di sekitar rumah tidak bisa melacak dana kamu, maka posisinya tidak berubah dibanding sebelum penyitaan server.

Hal lain yang sangat penting adalah mempertimbangkan anonset awal koin kamu sebelum penyitaan server. Misalnya, jika sebuah koin sudah memiliki anonset prospektif sebesar 40.000, maka penurunan potensialnya kemungkinan tidak signifikan. Dengan anonset dasar yang sangat tinggi, kecil kemungkinan kehadiran beberapa pengguna tanpa Dojo akan mengubah situasi secara drastis. Namun, jika anonset koin kamu hanya 40, maka potensi kebocoran ini bisa berdampak serius dan membuka kemungkinan pelacakan.

Karena WST tidak lagi berfungsi setelah OXT.me ditutup, kamu hanya bisa memperkirakan anonset tersebut. Untuk anonset retrospektif, biasanya tidak terlalu mengkhawatirkan karena model Whirlpool memastikan nilainya sangat tinggi sejak coinjoin pertama, berkat warisan dari peserta lain. Satu-satunya situasi yang mungkin bermasalah adalah jika koin kamu tidak diremix selama beberapa tahun dan hanya dicampur di awal peluncuran pool. Untuk anonset prospektif, kamu bisa melihat sudah berapa lama koin tersedia untuk coinjoin. Jika sudah berbulan-bulan, kemungkinan anonsetnya tinggi. Sebaliknya, jika baru masuk ke pool beberapa jam sebelum server disita, anonset prospektifnya mungkin sangat rendah.

**-> Pelajari lebih lanjut tentang anonset dan metode perhitungannya.**

Aspek lain yang perlu diperhatikan adalah dampak konsolidasi terhadap anonset koin yang sudah dicampur. Karena akun Whirlpool tidak lagi bisa diakses melalui aplikasi Samourai, kemungkinan banyak pengguna memindahkan wallet mereka ke perangkat lunak lain dan mencoba menarik dana dari Whirlpool. Akhir pekan lalu, ketika biaya transaksi di jaringan Bitcoin cukup tinggi, ada insentif teknis dan ekonomi yang kuat untuk melakukan konsolidasi koin postmix. Artinya, kemungkinan besar banyak pengguna melakukan konsolidasi besar-besaran.

Masalahnya, konsolidasi postmix selalu mengurangi anonset, bukan hanya bagi pengguna yang melakukan konsolidasi tetapi juga bagi pengguna lain yang pernah satu siklus coinjoin dengannya. Meskipun aku belum bisa memverifikasi atau mengukur fenomena ini secara akurat, insentif ekonomi akibat biaya transaksi saat itu memberi alasan kuat untuk mengasumsikan bahwa anonset secara umum mungkin menurun.

### Sebagai Pengguna Sentinel

Cara kerja jaringan aplikasi wallet watch-only Sentinel mirip dengan Samourai. Untuk menampilkan informasi wallet, aplikasi perlu mengirimkan xpub, kunci publik, dan alamat yang kamu gunakan ke Dojo. Jika kamu selalu menggunakan Dojo sendiri di Sentinel, tidak ada masalah dan kamu bisa tetap memakainya dengan tenang. Namun, jika kamu mengandalkan server Samourai untuk Sentinel, ada kemungkinan xpub kamu telah terekspos. Dalam kasus ini, sebaiknya ikuti proses pembuatan wallet baru seperti yang direkomendasikan untuk Samourai Wallet yang sebelumnya terhubung ke server Samourai.

Dalam skenario yang jarang terjadi di mana kamu menggunakan Dojo sendiri dengan Samourai tetapi tidak dengan Sentinel, akan lebih aman untuk menganggap bahwa xpub kamu sudah terkompromi.

## Kesimpulan

Terima kasih sudah membaca artikel ini sampai akhir. Jika menurutmu ada informasi yang kurang atau kamu punya saran, jangan ragu untuk menghubungiku dan berbagi pendapat. Jika kamu masih membutuhkan bantuan untuk memulihkan Samourai Wallet meskipun sudah mengikuti tutorial ini, kamu bisa bergabung dengan [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) untuk meminta bantuan. Aku cukup sering aktif di sana dan akan dengan senang hati membantu jika aku tahu solusinya. Bitcoiner lain juga bisa berbagi pengalaman dan memberikan dukungan. **Dalam kondisi apa pun, sangat penting untuk menjaga kerahasiaan seedphrase, file cadangan, dan passphrase milikmu.** Jangan pernah membagikannya kepada siapa pun, karena itu bisa memungkinkan mereka mencuri bitcoin kamu.


