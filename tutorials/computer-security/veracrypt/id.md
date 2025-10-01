---
name: VeraCrypt
description: Bagaimana cara mudah mengenkripsi perangkat penyimpanan?
---
![cover](assets/cover.webp)

Saat ini, sangat penting untuk menerapkan strategi guna menjamin aksesibilitas, keamanan, dan pencadangan file Anda, seperti dokumen personal, foto, atau proyek penting. Kehilangan data-data ini dapat berakibat fatal.

Untuk mencegah permasalahan ini, saya menyarankan Anda untuk memelihara beberapa salinan cadangan file Anda pada media yang berbeda. Strategi yang umum digunakan dalam komputasi adalah strategi pencadangan "3-2-1", yang menjamin proteksi file Anda:
- **3** salinan file Anda;
- Disimpan pada setidaknya **2** jenis media yang berbeda;
- Dengan setidaknya **1** salinan disimpan di beda lokasi.

Dengan kata lain, disarankan untuk menyimpan berkas Anda di 3 lokasi berbeda, menggunakan media yang bersifat beragam, seperti komputer Anda, hard drive eksternal, USB stick, atau layanan penyimpanan online. Dan terakhir, memiliki salinan beda lokasi berarti Anda harus menyimpan cadangan di luar rumah atau tempat bisnis Anda. Poin terakhir ini membantu menghindari kerugian total file Anda jika terjadi bencana lokal seperti kebakaran atau banjir. Salinan eksternal, yang jauh dari rumah atau bisnis Anda, memastikan data Anda akan tetap bertahan terlepas dari risiko lokal.

Untuk menerapkan strategi pencadangan 3-2-1 ini dengan mudah, Anda dapat memilih solusi penyimpanan online, dengan menyinkronkan file dari komputer Anda secara otomatis atau berkala dengan file yang ada di cloud Anda. Di antara solusi pencadangan online ini, tentu saja ada yang berasal dari perusahaan digital besar yang Anda kenal: Google Drive, Microsoft OneDrive, atau Apple iCloud. Namun, ini bukan solusi yang terbaik untuk melindungi privasi Anda. Dalam tutorial sebelumnya, saya telah memperkenalkan Anda pada alternatif yang mengenkripsi dokumen Anda untuk privasi yang lebih baik: Proton Drive.

https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Dengan mengadopsi strategi pencadangan lokal dan cloud ini, Anda sudah memiliki 2 jenis media berbeda untuk data Anda, salah satunya yang beda lokasi. Untuk melengkapi strategi 3-2-1, Anda hanya perlu menambahkan salinan tambahan. Yang saya sarankan adalah Anda secara berkala mengekspor data yang ada di lokal dan di cloud Anda ke media fisik, seperti USB stick atau hard drive eksternal. Dengan cara ini, meskipun server solusi penyimpanan online Anda hancur dan komputer Anda rusak secara bersamaan, Anda masih memiliki salinan ketiga ini di media eksternal agar tidak kehilangan data Anda.
![VeraCrypt](assets/notext/01.webp)

Namun, penting juga untuk mempertimbangkan keamanan penyimpanan data Anda guna memastikan tidak ada seorang pun selain Anda atau orang terdekat Anda yang dapat mengaksesnya. Data lokal maupun data online pada umumnya aman. Di komputer Anda, kemungkinan besar Anda telah mengatur kata sandi, dan hard drive komputer modern sering kali terenkripsi secara default. Terkait penyimpanan online Anda (cloud), saya telah menunjukkan dalam tutorial sebelumnya bagaimana mengamankan akun Anda dengan kata sandi yang kuat dan autentikasi dua faktor. Akan tetapi, untuk salinan ketiga Anda yang disimpan pada media fisik, satu-satunya keamanannya adalah kepemilikan fisik. Jika seorang pencuri berhasil mencuri USB stick atau hard drive eksternal Anda, mereka dapat dengan mudah mengakses semua data Anda.
![VeraCrypt](assets/notext/02.webp)

Untuk mencegah risiko ini, disarankan untuk mengenkripsi media fisik Anda. Dengan demikian, setiap upaya untuk mengakses data akan memerlukan memasukkan kata sandi untuk mendekripsi isinya. Tanpa kata sandi ini, mustahil mengakses data, sehingga mengamankan file pribadi Anda bahkan jika USB stick atau hard drive eksternal Anda dicuri.
![VeraCrypt](assets/notext/03.webp)

Dalam tutorial ini, saya akan menunjukkan cara mudah mengenkripsi media penyimpanan eksternal menggunakan VeraCrypt, sebuah alat open source.

## Pengenalan VeraCrypt

VeraCrypt adalah perangkat lunak open source yang tersedia di Windows, macOS, dan Linux, yang memungkinkan Anda mengenkripsi data Anda dengan berbagai cara dan di berbagai media.
![VeraCrypt](assets/notext/04.webp)

Perangkat lunak ini memungkinkan pembuatan dan pemeliharaan volume terenkripsi secara langsung, artinya data Anda secara otomatis dienkripsi sebelum disimpan dan didekripsi sebelum dibaca. Metode ini memastikan bahwa file Anda tetap terlindungi bahkan jika media penyimpanan Anda dicuri. VeraCrypt tidak hanya mengenkripsi file, tetapi juga nama file, metadata, folder, dan bahkan ruang kosong pada media penyimpanan Anda.

VeraCrypt dapat digunakan untuk mengenkripsi file secara lokal atau seluruh volume (area terformat), termasuk volume (area terformat) sistem. Ini juga dapat digunakan untuk mengenkripsi sepenuhnya media eksternal seperti USB stick atau disk seperti yang akan kita lihat dalam tutorial ini.

Keuntungan utama VeraCrypt dibandingkan solusi brand lain adalah bahwa VeraCrypt sepenuhnya open source, yang berarti kodenya dapat diverifikasi oleh siapa saja.

## Bagaimana cara menginstal VeraCrypt?

Kunjungi [situs web resmi VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) di tab "*Downloads / Unduh*".
![VeraCrypt](assets/notext/05.webp)

Unduh versi yang cocok untuk sistem operasi Anda. Jika Anda menggunakan Windows, pilih "*EXE Installer*".
![VeraCrypt](assets/notext/06.webp)

Pilih bahasa untuk tampilan Anda.
![VeraCrypt](assets/notext/07.webp)

Terima syarat-syarat lisensi.
![VeraCrypt](assets/notext/08.webp)

Pilih "*Install*".
![VeraCrypt](assets/notext/09.webp)

Akhirnya, pilih folder tempat perangkat lunak akan diinstal, lalu klik tombol "*Install*".
![VeraCrypt](assets/notext/10.webp)

Tunggu hingga instalasi selesai.
![VeraCrypt](assets/notext/11.webp)

Instalasi selesai.
![VeraCrypt](assets/notext/12.webp)

Jika Anda ingin, Anda dapat berdonasi dalam Bitcoin untuk mendukung pengembangan aplikasi open source ini.
![VeraCrypt](assets/notext/13.webp)

## Bagaimana cara mengenkripsi perangkat penyimpanan dengan VeraCrypt?

Pada peluncuran pertama, Anda akan sampai pada tampilan ini:
![VeraCrypt](assets/notext/14.webp)

Untuk mengenkripsi perangkat penyimpanan pilihan Anda, mulailah dengan menghubungkannya ke mesin Anda. Seperti yang akan Anda lihat nanti, proses membuat volume terenkripsi baru pada USB stick atau hard drive akan memakan waktu lebih lama jika perangkat sudah berisi data yang tidak ingin Anda hapus. Oleh karena itu, saya merekomendasikan menggunakan USB stick kosong atau mengosongkan perangkat sebelumnya untuk membuat volume terenkripsi, agar menghemat waktu.

Untuk mengenkripsi perangkat penyimpanan pilihan Anda, mulailah dengan menghubungkannya ke komputer Anda. Seperti yang akan Anda lihat nanti, proses pembuatan volume terenkripsi baru pada USB stick atau hard drive akan memakan waktu jauh lebih lama jika perangkat tersebut sudah berisi data yang tidak ingin Anda hapus. Oleh karena itu, saya merekomendasikan untuk menggunakan USB stick kosong atau mengosongkan perangkat tersebut terlebih dahulu untuk membuat volume terenkripsi, guna menghemat waktu.

Di VeraCrypt, klik pada tab "*Volumes*".
![VeraCrypt](assets/notext/15.webp)

Kemudian pada menu "*Create New Volume... / Buat volume baru*".
![VeraCrypt](assets/notext/16.webp)

Di tampilan baru yang terbuka, pilih opsi "*Encrypt a non-system partition/drive*" dan klik pada "*Next / lanjut*".
![VeraCrypt](assets/notext/17.webp)

Anda sebelumnya harus memilih antara "*Standard VeraCrypt volume*" dan "*Hidden VeraCrypt Volume*". Opsi pertama akan membuat volume terenkripsi standar pada perangkat Anda. Opsi "*Hidden VeraCrypt Volume*" memungkinkan pembuatan volume (area terformat) tersembunyi di dalam volume (area terformat) VeraCrypt standar. Metode ini memungkinkan Anda untuk meniadakan volume (area terformat) tersembunyi ini dalam kasus pemaksaan. Sebagai contoh, jika seseorang secara fisik memaksa Anda untuk mendekripsi perangkat Anda, Anda dapat mendekripsi hanya bagian standar untuk memenuhi permintaan penyerang tetapi tidak mengungkapkan bagian yang tersembunyi. Dalam contoh ini, saya akan menggunakan volume (area terformat) standar.
![VeraCrypt](assets/notext/18.webp)

Pada halaman berikutnya, klik tombol "*Select Device... / Pilih perangkat*".
![VeraCrypt](assets/notext/19.webp)

Sebuah panel baru akan terbuka, di mana Anda bisa memilih partisi perangkat penyimpanan Anda dari daftar disk yang tersedia di komputer. Biasanya, partisi yang ingin Anda enkripsi akan terdaftar di bawah baris berlabel "Removable Disk N". Setelah memilih partisi yang sesuai, klik tombol "OK".
![VeraCrypt](assets/notext/20.webp)

Partisi yang dipilih muncul di kotak. Anda sekarang dapat klik tombol "*Next / lanjut*".
![VeraCrypt](assets/notext/21.webp)

Selanjutnya, Anda perlu memilih antara opsi "*Create encrypted volume and format it*" atau "*Encrypt partition in place*". Seperti yang disebutkan sebelumnya, opsi pertama akan menghapus secara permanen semua data yang ada di USB stick atau hard drive Anda. Pilih opsi ini hanya jika perangkat Anda kosong; jika tidak, Anda akan kehilangan semua data yang terkandung di dalamnya. Jika Anda ingin mempertahankan data yang sudah ada, Anda bisa memindahkannya sementara ke tempat lain, lalu pilih "*Create encrypted volume and format it*" untuk proses yang lebih cepat (yang akan menghapus semuanya), atau pilih "*Encrypt partition in place*". Opsi terakhir ini memungkinkan Anda mengenkripsi volume tanpa menghapus data yang sudah ada, namun prosesnya akan jauh lebih lama. Untuk contoh ini, karena USB stick saya kosong, saya memilih "*Create encrypted volume and format it*", yaitu opsi yang menghapus semuanya.
![VeraCrypt](assets/notext/22.webp)

Selanjutnya, Anda akan memiliki opsi untuk memilih algoritma enkripsi dan fungsi hash. Kecuali Anda memiliki kebutuhan spesifik, saya menyarankan Anda untuk mempertahankan opsi default. Klik "*Next / lanjut*" untuk melanjutkan.
![VeraCrypt](assets/notext/23.webp)

Pastikan ukuran yang ditunjukkan untuk volume (area terformat) Anda benar, untuk mengenkripsi seluruh ruang yang tersedia pada USB stick, dan bukan hanya sebagian. Setelah diverifikasi, klik "*Next / lanjut*".
![VeraCrypt](assets/notext/24.webp)

Pada tahap ini, Anda perlu menetapkan kata sandi untuk mengenkripsi dan mendekripsi perangkat Anda. Penting untuk memilih kata sandi yang kuat guna mencegah penyerang mendekripsi konten Anda dengan serangan brute force. Kata sandi harus acak, sepanjang mungkin, dan mencakup beberapa jenis karakter. Saya menyarankan Anda untuk memilih kata sandi acak setidaknya 20 karakter yang mencakup huruf kecil, huruf besar, angka, dan simbol.

Saya juga menyarankan Anda untuk menyimpan kata sandi Anda di pengelola kata sandi (password manager). Ini akan mempermudah akses dan menghilangkan risiko lupa. Untuk kasus khusus ini, pengelola kata sandi lebih baik daripada media kertas. Sebab, jika terjadi pembobolan, meskipun perangkat penyimpanan Anda mungkin dicuri, kata sandi di pengelola tidak dapat ditemukan oleh penyerang, yang akan mencegah akses ke data. Sebaliknya, jika pengelola kata sandi Anda dibobol, akses fisik ke perangkat tetap diperlukan untuk memanfaatkan kata sandi dan mengakses data.

Untuk informasi lebih lanjut tentang pengelolaan kata sandi, saya menyarankan Anda untuk melihat tutorial lengkap lainnya berikut ini:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Masukkan kata sandi Anda di 2 kolom yang ditentukan, kemudian klik pada "*Next / lanjut*".
![VeraCrypt](assets/notext/25.webp)

Kemudian, VeraCrypt akan menanyakan apakah Anda berencana menyimpan file yang ukurannya lebih besar dari 4 GiB di volume (area terformat) terenkripsi. Pertanyaan ini bertujuan agar perangkat lunak dapat memilih sistem file yang paling sesuai. Secara umum, sistem FAT digunakan karena kompatibel dengan sebagian besar sistem operasi. Namun, sistem ini memiliki batasan ukuran file maksimum 4 GiB. Jika Anda perlu mengelola file yang lebih besar, Anda bisa memilih sistem exFAT.
![VeraCrypt](assets/notext/26.webp)

Selanjutnya, Anda ada pada halaman yang memungkinkan Anda menghasilkan kunci acak. Kunci ini penting, karena akan digunakan untuk mengenkripsi dan mendekripsi data Anda. Kunci ini akan disimpan di bagian khusus pada media Anda, yang keamanannya sendiri dilindungi oleh kata sandi yang telah Anda tetapkan sebelumnya. Untuk menghasilkan kunci enkripsi yang kuat, VeraCrypt membutuhkan entropi. Itulah mengapa perangkat lunak ini meminta Anda untuk menggerakkan mouse secara acak di atas jendela; gerakan-gerakan ini kemudian digunakan untuk menghasilkan kunci. Lanjutkan menggerakkan mouse hingga pengukur entropi terisi penuh. Setelah itu, klik "_Format_" untuk mulai membuat volume terenkripsi.
![VeraCrypt](assets/notext/27.webp)

Tunggu selama pemformatan dilakukan. Ini bisa memakan waktu lama untuk volume besar.
![VeraCrypt](assets/notext/28.webp)

Anda kemudian akan menerima konfirmasi.
![VeraCrypt](assets/notext/29.webp)

## Bagaimana cara menggunakan drive terenkripsi dengan VeraCrypt?

Untuk saat ini, media Anda terenkripsi dan oleh karena itu Anda tidak dapat membukanya. Untuk mendekripsinya, buka VeraCrypt.
![VeraCrypt](assets/notext/30.webp)

Pilih huruf drive dari daftar. Sebagai contoh, saya memilih "*L:*".
![VeraCrypt](assets/notext/31.webp)

Klik pada tombol "*Select Device... / Pilih perangkat*".
![VeraCrypt](assets/notext/32.webp)

Dari daftar semua disk di komputer Anda, pilih volume terenkripsi pada media Anda, kemudian klik pada tombol "*OK*".
![VeraCrypt](assets/notext/33.webp)

Anda dapat melihat bahwa volume Anda telah terpilih dengan baik.
![VeraCrypt](assets/notext/34.webp)

Klik pada tombol "*Mount / Memasang*".
![VeraCrypt](assets/notext/35.webp)

Masukkan kata sandi yang dipilih selama pembuatan volume, kemudian klik pada "*OK*".
![VeraCrypt](assets/notext/36.webp)

Anda dapat melihat bahwa volume Anda sekarang telah didekripsi dan dapat diakses pada huruf drive "*L:*".
![VeraCrypt](assets/notext/37.webp)

Untuk mengaksesnya, buka penjelajah file Anda dan pergi ke drive "*L:*" (atau huruf lain tergantung pada yang Anda pilih dalam langkah sebelumnya). 
![VeraCrypt](assets/notext/38.webp)

Setelah menambahkan file pribadi Anda ke media, untuk mengenkripsi volume lagi, cukup klik pada tombol "*Dismount / lepaskan*".
![VeraCrypt](assets/notext/39.webp)

Volume Anda tidak lagi muncul di bawah huruf "*L:*". Dengan demikian, Volume terenkripsi lagi.
![VeraCrypt](assets/notext/40.webp)

Anda sekarang dapat melepas media penyimpanan Anda.

Selamat, Anda sekarang memiliki media terenkripsi untuk menyimpan data pribadi Anda dengan aman, sehingga memiliki strategi lengkap 3-2-1 selain salinan di komputer Anda dan penyimpanan online Anda.
Jika Anda ingin mendukung pengembangan VeraCrypt, Anda juga dapat meberikan donasi dalam bitcoin [di halaman ini](https://www.veracrypt.fr/en/Donation.html).
