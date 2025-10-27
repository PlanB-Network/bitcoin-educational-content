---
name: Passphrase BIP39 Ledger
description: Bagaimana cara menambahkan passphrase ke dompet Ledger kamu?
---
![cover](assets/cover.webp)

Passphrase BIP39 adalah kata sandi opsional yang, saat digabungkan dengan seedphrase kamu, menambahkan lapisan keamanan ekstra ke dompet Bitcoin deterministik dan hierarkis. Dalam tutorial ini, kita bakal bahas bareng cara mengatur passphrase di dompet Bitcoin kamu lewat perangkat Ledger, apa pun modelnya.

Sebelum mulai, kalau kamu belum familiar dengan konsep passphrase, cara kerjanya, dan dampaknya terhadap dompet Bitcoin kamu, aku sangat nyaranin buat baca dulu artikel teoretis lain ini, di mana aku jelasin semuanya secara detail.

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Bagaimana fungsi passphrase pada Ledger?

Dengan perangkat Ledger, kamu punya dua pilihan berbeda untuk mengonfigurasi passphrase pada dompet milikmu: opsi "*PIN-tied*" dan opsi "*temporary*".

Dengan opsi "*PIN-tied*", kamu mengaitkan passphrase dengan PIN kedua pada Ledger kamu. Ini berarti kamu akan memiliki 2 PIN: satu untuk mengakses dompet reguler kamu tanpa passphrase, dan yang lainnya untuk mengakses dompet kedua kau yang dilindungi oleh passphrase.

![PASSPHRASE BIP39](assets/notext/03.webp)

Pada dasarnya, bahkan dengan opsi passphrase yang terhubung ke PIN kedua, passphrase kamu tetaplah passphrase kamu. Artinya, kalau kamu kehilangan Ledger dan ingin memulihkan bitcoin di perangkat atau software lain, kamu bakal benar-benar butuh seedphrase 24 kata dan **passphrase lengkap kamu.** PIN yang terhubung dengan passphrase cuma berfungsi untuk mengaksesnya di Ledger kamu saat ini, tapi nggak bisa dipakai di Ledger lain atau software lain. Karena itu, sangat penting buat mencadangkan passphrase kamu secara fisik. **Mengetahui PIN sekunder aja nggak cukup buat mendapatkan kembali akses ke dompet kamu; itu cuma fitur kemudahan di Ledger kamu.**

Opsi PIN kedua ini sangat berguna untuk menghadapi serangan fisik. Misalnya, kalau ada orang maksa kamu buka perangkat buat nyuri dana, kamu bisa pakai PIN pertama untuk membuka dompet umpan yang berisi sedikit bitcoin, sementara dana utama kamu tetap aman di balik PIN kedua.

Selain itu, fitur ini ngasih semua manfaat keamanan dari passphrase BIP39 tanpa repot harus memasukkannya setiap kali kamu pakai perangkat penandatanganan. Kamu bisa pakai passphrase yang panjang dan acak untuk memperkuat perlindungan dari serangan brute force, tanpa harus susah-susah mengetiknya di tombol kecil perangkat setiap kali digunakan.

Opsi “passphrase sementara” nggak menyimpan passphrase di perangkat. Setiap kali kamu mau mengakses dompet terlindungi, kamu harus memasukkan passphrase secara manual di Ledger. Ini memang lebih ribet, tapi sedikit lebih aman karena nggak meninggalkan jejak passphrase di perangkat. Begitu kamu mematikan perangkat, Ledger bakal kembali ke keadaan awal dan kamu perlu masukin ulang passphrase lengkap untuk mengakses akun tersembunyi. Opsi “passphrase sementara” ini mirip dengan cara kerja sebagian besar dompet perangkat keras lainnya.

Di tutorial ini, aku bakal pakai Ledger Flex sebagai contoh. Tapi kalau kamu pakai model Ledger lain, prosesnya sama aja. Untuk Ledger Stax, tampilannya identik dengan Ledger Flex. Sedangkan untuk Nano S, Nano S Plus, dan Nano X, meskipun tampilannya agak beda, proses dan nama menunya tetap sama.

**Perhatian:** Kalau kamu udah pernah menerima bitcoin di Ledger sebelum mengaktifkan passphrase, kamu perlu mentransfernya lewat transaksi Bitcoin. Passphrase bakal menghasilkan satu set kunci baru, jadi dompet yang terbentuk sepenuhnya terpisah dari dompet awal kamu. Saat menambahkan passphrase, kamu bakal punya dompet baru yang awalnya kosong. **Tapi ini nggak menghapus dompet pertama yang tanpa passphrase.** Kamu masih bisa mengaksesnya, baik langsung lewat Ledger tanpa masukin passphrase, atau lewat software lain dengan seedphrase 24 kata kamu.

Sebelum mulai tutorial ini, pastikan kamu udah menginisialisasi Ledger dan menghasilkan seedphrase kamu. Kalau belum, dan Ledger kamu masih baru, ikuti dulu tutorial khusus untuk modelmu yang tersedia di PlanB Network. Setelah itu selesai, baru lanjut ke tutorial ini.
https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Bagaimana cara mengatur passphrase sementara dengan Ledger?

Di halaman utama Ledger milikmu, klik pada icon roda gigi pengaturan.

![PASSPHRASE BIP39](assets/notext/04.webp)

Pilih menu "Advanced", kemudian "Set passphrase".

![PASSPHRASE BIP39](assets/notext/05.webp)

Ini adalah langkah di mana kamu dapat memilih antara opsi "linked to PIN" atau opsi "temporary" yang telah kita bahas di bagian sebelumnya. Di sini, aku akan menjelaskan cara mengatur passphrase sementara, jadi klik pada "Set temporary passphrase".

![PASSPHRASE BIP39](assets/notext/06.webp)

Kamu kemudian diminta untuk memasukkan passphrase milikmu. Pilih passphrase yang kuat dan segera lanjutkan ke cadangan fisik, pada media seperti kertas atau logam. Dalam contoh ini, saya memilih passphrase: `fH3&kL@9mP#2sD5qR!82`. Setelah memasukkan passphrase milikmu, klik tombol "*Continue*".

![PASSPHRASE BIP39](assets/notext/07.webp)

Verifikasi bahwa passphrase kamu cocok dengan yang sudah kamu catat pada backup fisik milikmu, kemudian klik tombol "*Yes, it's correct*" untuk mengonfirmasi.

![PASSPHRASE BIP39](assets/notext/08.webp)

Untuk menyelesaikan pembuatan passphrase, masukkan kode PIN Ledger milikmu. Mulai sekarang, setiap kali kamu ingin mengakses dompet kamu dengan passphrase di Ledger, kamu perlu mengikuti langkah-langkah yang sama seperti yang dijelaskan di sini.

![PASSPHRASE BIP39](assets/notext/09.webp)

Sekarang kamu bisa impor set kunci publik kamu ke Sparrow Wallet untuk mengelola dompetmu. Di Sparrow, dompet ini bakal muncul sebagai dompet yang berbeda dari dompet awal kamu yang nggak pakai passphrase.

Buka Sparrow Wallet. Pastikan perangkat lunak terhubung ke node, kemudian klik pada tab "*File*" dan pilih "*New Wallet*".

![PASSPHRASE BIP39](assets/notext/10.webp)

Pilih nama untuk dompet kamu yang dilindungi oleh passphrase. Di contoh ini, aku pakai nama yang secara jelas menyertakan istilah *passphrase.* Tapi kalau kamu lebih suka menjaga kerahasiaan dompet ini di komputermu, kamu bisa pilih nama yang lebih netral dan nggak terlalu mencolok.

![PASSPHRASE BIP39](assets/notext/11.webp)

Pilih jenis skrip untuk dompet Anda. Saya menyarankan Anda untuk memilih "*Taproot*" atau alternatifnya "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/12.webp)

Hubungkan Ledger kamu ke komputer, kemudian klik pada "*Connected Hardware Wallet*". Pastikan kamu sudah memasukkan passphrase pada Ledger milikmu. Jika belum, silakan kembali ke langkah sebelumnya untuk memasukkan passphrase milikmu. Sebelum melanjutkan ke pemindaian, ingat juga untuk membuka aplikasi "*Bitcoin*" pada Ledger milikmu.

Klik pada tombol "*Scan...*".

Klik pada "*Import Keystore*" dibagian samping Ledger.

Dompet milikmu yang dilindungi oleh passphrase sekarang telah dibuat di Sparrow. Untuk mengonfirmasi, klik pada tombol "*Apply*".

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini bakal memastikan keamanan data dompet kamu di Sparrow, termasuk kunci publik, alamat, label, dan riwayat transaksi dari akses yang nggak sah.
Aku nyaranin kamu menyimpan kata sandi ini di password manager biar nggak lupa.

Sekarang, dompet kamu sudah jadi! Di menu Settings, Sparrow bakal menampilkan Master fingerprint. Ini adalah sidik jari dari kunci induk kamu yang jadi dasar penurunan seluruh struktur dompet. Aku sangat nyaranin kamu buat menyimpan salinan sidik jari ini. Di contohku, nilainya adalah `281ee33a`.

Ingat apa yang sudah kita bahas sebelumnya: kesalahan sekecil apa pun saat memasukkan passphrase bakal bikin dompet baru yang sepenuhnya berbeda dengan kunci yang juga berbeda. Jadi, setiap kali kamu mau memastikan bahwa kamu sedang mengakses dompet yang benar dengan passphrase yang tepat, periksa apakah sidik jari kunci induk kamu cocok dengan yang sudah kamu catat. Info ini sendiri nggak berisiko terhadap keamanan atau privasi dana kamu.

Sebelum mulai pakai dompet dengan passphrase, aku sangat nyaranin kamu buat melakukan tes pemulihan (dry-run). Catat dulu informasi penting seperti xpub atau sidik jari kunci induk kamu, lalu reset Ledger kamu sementara dompetnya masih kosong. Setelah itu, coba pulihkan dompet kamu di Ledger pakai cadangan kertas berisi seedphrase 24 kata dan passphrase. Pastikan hasil yang muncul setelah pemulihan cocok dengan data yang kamu catat sebelumnya. Kalau cocok, berarti cadangan kertas kamu bisa diandalkan.

## Bagaimana cara mengatur passphrase yang terkait dengan PIN pada Ledger?

Di halaman utama Ledger kamu, klik pada roda gigi pengaturan.

Pilih menu "*Advanced*", kemudian "*Set passphrase*".

Ini adalah langkah di mana kamu dapat memilih antara opsi "*linked to PIN*" atau "*temporary*" yang kami bahas di bagian sebelumnya. Di sini, aku akan menjelaskan cara mengatur passphrase yang terkait dengan PIN, jadi klik pada "*Set passphrase and attach it to a new PIN*".

Selanjutnya, kamu perlu memilih kode PIN yang akan dikaitkan dengan passphrase kamu. Sama seperti PIN utama, disarankan untuk pakai PIN 8 digit yang acak. Pastikan juga kamu menyimpan kode ini di tempat yang berbeda dari lokasi penyimpanan Ledger Flex kamu.

Di contohku, PIN utama adalah `58293647`, dan aku pilih `71425839` sebagai PIN sekunder yang terhubung dengan passphrase.

![PASSPHRASE BIP39](assets/notext/22.webp)

Selanjutnya, kamu bakal diminta untuk memasukkan passphrase kamu. Pilih passphrase yang kuat dan segera buat cadangannya secara fisik, misalnya di kertas atau logam. Di contoh ini, aku pakai passphrase: `fH3&kL@9mP#2sD5qR!82`. Setelah kamu masukin passphrase, klik tombol Continue.

![PASSPHRASE BIP39](assets/notext/23.webp)

Verifikasi bahwa passphrase kamu sesuai dengan yang telah kamu catat pada backup fisik, kemudian klik tombol "*Yes, it's correct*" untuk mengonfirmasi.

![PASSPHRASE BIP39](assets/notext/24.webp)

Untuk menyelesaikan pembuatan passphrase kamu, masukkan kode PIN utama Ledger milikmu (bukan yang terkait dengan passphrase).

![PASSPHRASE BIP39](assets/notext/25.webp)

Mulai sekarang, setiap kali kamu ingin mengakses dompet milikmu dengan passphrase di Ledger, kamu perlu memasukkan bukan kode PIN utama, melainkan kode PIN sekunder:
- Kode PIN utama (`58293647`) > dompet tanpa passphrase.
- Kode PIN sekunder (`71425839`) > dompet dengan passphrase.

Sekarang kamu bisa impor set kunci publik kamu ke Sparrow Wallet untuk mengelola dompetmu. Di Sparrow, dompet ini bakal muncul sebagai dompet yang berbeda dari dompet awal kamu yang nggak pakai passphrase.

Buka Sparrow Wallet. Pastikan perangkat lunak terhubung ke node, kemudian klik pada tab "*File*" dan pilih "*New Wallet*".

![PASSPHRASE BIP39](assets/notext/26.webp)

Pilih nama untuk dompet kamu yang dilindungi oleh passphrase. Untuk contoh ini, aku memilih nama yang secara eksplisit menyertakan istilah "*passphrase*". Namun, kalau kamu lebih suka menjaga kerahasiaan dompet ini di komputer milikmu, kamu bisa memilih nama yang kurang sugestif.

![PASSPHRASE BIP39](assets/notext/27.webp)

Pilih tipe skrip untuk dompetmu. Aku sarankan kamu untuk memilih "*Taproot*" atau, jika tidak tersedia, "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/28.webp)

Hubungkan Ledger kamu ke komputer, lalu klik Connected Hardware Wallet. Pastikan kamu sudah punya passphrase aktif di Ledger dengan membukanya pakai kode PIN sekunder. Kalau belum, restart dulu Ledger kamu dan masuk dengan PIN yang terhubung ke passphrase. Sebelum lanjut ke proses pemindaian, jangan lupa buka aplikasi *Bitcoin* di Ledger kamu.

![PASSPHRASE BIP39](assets/notext/29.webp)

Klik tombol "*Scan...*".

![PASSPHRASE BIP39](assets/notext/30.webp)

Klik pada "*Import Keystore*".

![PASSPHRASE BIP39](assets/notext/31.webp)

Dompet kamu yang dilindungi oleh passphrase sekarang telah dibuat di Sparrow. Untuk mengonfirmasi, klik tombol "*Apply*".

![PASSPHRASE BIP39](assets/notext/32.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini bakal menjaga keamanan data dompet kamu di Sparrow, termasuk kunci publik, alamat, label, dan riwayat transaksi dari akses yang nggak sah.

Aku nyaranin kamu menyimpan kata sandi ini di password manager biar nggak lupa.

![PASSPHRASE BIP39](assets/notext/33.webp)

Sekarang, dompet kamu sudah jadi! Di menu Settings, Sparrow bakal menampilkan Master fingerprint kamu. Ini adalah sidik jari dari kunci induk yang dipakai sebagai dasar turunan dompet kamu. Aku sangat nyaranin kamu buat menyimpan salinan sidik jari ini. Di contohku, nilainya adalah 281ee33a.

![PASSPHRASE BIP39](assets/notext/34.webp)

Ingat apa yang udah kita bahas di bagian sebelumnya: kesalahan sekecil apa pun saat memasukkan passphrase bakal bikin dompet baru yang sepenuhnya berbeda dengan kunci yang juga berbeda. Jadi, setiap kali kamu mau memastikan akses ke dompet yang benar dengan passphrase yang tepat, periksa apakah sidik jari dari kunci induk kamu cocok dengan yang udah kamu catat. Info ini sendiri nggak menimbulkan risiko apa pun terhadap keamanan dana atau privasi kamu.

Sebelum mulai pakai dompet kamu dengan passphrase, aku sangat nyaranin buat melakukan tes pemulihan tanpa risiko. Catat dulu info penting seperti xpub atau sidik jari dari kunci induk kamu, lalu reset Ledger kamu sementara dompetnya masih kosong. Setelah itu, coba pulihkan dompet kamu di Ledger pakai cadangan kertas berisi seedphrase 24 kata dan passphrase. Pastikan hasil yang muncul setelah pemulihan cocok dengan data yang kamu catat sebelumnya. Kalau cocok, berarti cadangan kertas kamu bisa diandalkan.

Selamat! Dompet Bitcoin kamu sekarang sudah diamankan dengan passphrase. Kalau kamu ngerasa tutorial ini bermanfaat, aku bakal sangat menghargai kalau kamu kasih jempol ke atas di bawah ini. Jangan ragu juga buat bagikan artikel ini ke jaringan sosial kamu. Makasih banyak!

Aku juga nyaranin kamu buat cek tutorial lengkap lainnya tentang cara pakai Ledger Flex kamu.

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
