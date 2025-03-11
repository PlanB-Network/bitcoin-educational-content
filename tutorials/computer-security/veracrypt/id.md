---
name: VeraCrypt
description: Bagaimana cara mudah mengenkripsi perangkat penyimpanan?
---
![cover](assets/cover.webp)

Saat ini, sangat penting untuk menerapkan strategi guna memastikan aksesibilitas, keamanan, dan pencadangan file Anda, seperti dokumen pribadi, foto, atau proyek penting. Kehilangan data ini bisa menjadi bencana.

Untuk mencegah masalah ini, saya menyarankan Anda untuk memelihara beberapa cadangan file Anda di media yang berbeda. Strategi yang umum digunakan dalam komputasi adalah strategi pencadangan "3-2-1", yang menjamin perlindungan file Anda:
- **3** salinan file Anda;
- Disimpan pada setidaknya **2** jenis media yang berbeda;
- Dengan setidaknya **1** salinan disimpan di luar lokasi.

Dengan kata lain, disarankan untuk menyimpan file Anda di 3 lokasi yang berbeda, menggunakan media yang berbeda sifatnya, seperti komputer Anda, hard drive eksternal, USB stick, atau layanan penyimpanan online. Dan akhirnya, memiliki salinan di luar lokasi berarti Anda harus memiliki cadangan yang disimpan di luar rumah atau bisnis Anda. Poin terakhir ini membantu menghindari kehilangan total file Anda dalam kasus bencana lokal seperti kebakaran atau banjir. Salinan eksternal, yang jauh dari rumah atau bisnis Anda, memastikan bahwa data Anda akan bertahan terlepas dari risiko lokal.

Untuk dengan mudah menerapkan strategi pencadangan 3-2-1 ini, Anda dapat memilih solusi penyimpanan online, dengan menyinkronkan file dari komputer Anda dengan yang ada di cloud Anda secara otomatis atau berkala. Di antara solusi pencadangan online ini, tentu saja ada yang dari perusahaan digital besar yang Anda kenal: Google Drive, Microsoft OneDrive, atau Apple iCloud. Namun, ini bukan solusi terbaik untuk melindungi privasi Anda. Dalam tutorial sebelumnya, saya memperkenalkan Anda pada alternatif yang mengenkripsi dokumen Anda untuk kerahasiaan yang lebih baik: Proton Drive.

https://planb.network/tutorials/others/general/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Dengan mengadopsi strategi pencadangan lokal dan cloud ini, Anda sudah mendapatkan dua jenis media yang berbeda untuk data Anda, salah satunya adalah di luar lokasi. Untuk melengkapi strategi 3-2-1, Anda hanya perlu menambahkan salinan tambahan. Yang saya sarankan adalah secara berkala mengekspor data Anda yang ada secara lokal dan di cloud ke media fisik, seperti USB stick atau hard drive eksternal. Dengan cara ini, bahkan jika server solusi penyimpanan online Anda hancur dan komputer Anda rusak secara bersamaan, Anda masih memiliki salinan ketiga ini pada media eksternal agar tidak kehilangan data Anda.
![VeraCrypt](assets/notext/01.webp)
Namun, juga penting untuk memikirkan tentang keamanan penyimpanan data Anda untuk memastikan bahwa tidak ada orang lain selain Anda atau orang terdekat Anda yang dapat mengaksesnya. Data lokal dan online biasanya aman. Di komputer Anda, Anda mungkin telah mengatur kata sandi, dan hard drive komputer modern seringkali dienkripsi secara default. Mengenai penyimpanan online (cloud) Anda, saya menunjukkan kepada Anda dalam tutorial sebelumnya bagaimana mengamankan akun Anda dengan kata sandi yang kuat dan otentikasi dua faktor. Namun, untuk salinan ketiga Anda yang disimpan di media fisik, satu-satunya keamanan adalah kepemilikan fisiknya. Jika seorang pencuri berhasil mencuri USB stick atau hard drive eksternal Anda, mereka bisa dengan mudah mengakses semua data Anda.
![VeraCrypt](assets/notext/02.webp)
Untuk mencegah risiko ini, disarankan untuk mengenkripsi media fisik Anda. Dengan demikian, setiap upaya untuk mengakses data akan memerlukan memasukkan kata sandi untuk mendekripsi konten. Tanpa kata sandi ini, akan mustahil untuk mengakses data, mengamankan file pribadi Anda bahkan dalam kejadian pencurian USB stick atau hard drive eksternal Anda.
![VeraCrypt](assets/notext/03.webp)
Dalam tutorial ini, saya akan menunjukkan cara mudah mengenkripsi media penyimpanan eksternal menggunakan VeraCrypt, sebuah alat sumber terbuka.
## Pengenalan VeraCrypt

VeraCrypt adalah perangkat lunak sumber terbuka yang tersedia di Windows, macOS, dan Linux, yang memungkinkan Anda mengenkripsi data Anda dengan berbagai cara dan di berbagai media.
![VeraCrypt](assets/notext/04.webp)
Perangkat lunak ini memungkinkan pembuatan dan pemeliharaan volume terenkripsi secara langsung, yang berarti data Anda secara otomatis dienkripsi sebelum disimpan dan didekripsi sebelum dibaca. Metode ini memastikan bahwa file Anda tetap terlindungi bahkan dalam kejadian pencurian media penyimpanan Anda. VeraCrypt tidak hanya mengenkripsi file, tetapi juga nama file, metadata, folder, dan bahkan ruang kosong pada media penyimpanan Anda.

VeraCrypt dapat digunakan untuk mengenkripsi file secara lokal atau seluruh partisi, termasuk disk sistem. Ini juga dapat digunakan untuk sepenuhnya mengenkripsi media eksternal seperti USB stick atau disk seperti yang akan kita lihat dalam tutorial ini.

Keuntungan besar VeraCrypt dibandingkan solusi proprietari adalah bahwa itu sepenuhnya sumber terbuka, yang berarti kodenya dapat diverifikasi oleh siapa saja.

## Bagaimana cara menginstal VeraCrypt?

Kunjungi [situs web resmi VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) di tab "*Downloads*".
![VeraCrypt](assets/notext/05.webp)
Unduh versi yang cocok untuk sistem operasi Anda. Jika Anda menggunakan Windows, pilih "*EXE Installer*".
![VeraCrypt](assets/notext/06.webp)
Pilih bahasa untuk antarmuka Anda.
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
Jika Anda ingin, Anda dapat membuat donasi dalam bitcoin untuk mendukung pengembangan alat sumber terbuka ini.
![VeraCrypt](assets/notext/13.webp)
## Bagaimana cara mengenkripsi perangkat penyimpanan dengan VeraCrypt?

Pada peluncuran pertama, Anda akan sampai pada antarmuka ini:
![VeraCrypt](assets/notext/14.webp)
Untuk mengenkripsi perangkat penyimpanan pilihan Anda, mulailah dengan menghubungkannya ke mesin Anda. Seperti yang akan Anda lihat nanti, proses membuat volume terenkripsi baru pada USB stick atau hard drive akan memakan waktu lebih lama jika perangkat sudah berisi data yang tidak ingin Anda hapus. Oleh karena itu, saya merekomendasikan menggunakan USB stick kosong atau mengosongkan perangkat sebelumnya untuk membuat volume terenkripsi, agar menghemat waktu.

Di VeraCrypt, klik pada tab "*Volumes*".
![VeraCrypt](assets/notext/15.webp)
Kemudian pada menu "*Create New Volume...*".
![VeraCrypt](assets/notext/16.webp)
Di jendela baru yang terbuka, pilih opsi "*Encrypt a non-system partition/drive*" dan klik pada "*Next*".
![VeraCrypt](assets/notext/17.webp)
Anda kemudian harus memilih antara "*Standard VeraCrypt volume*" dan "*Hidden VeraCrypt Volume*". Opsi pertama menciptakan volume terenkripsi standar pada perangkat Anda. Opsi "*Hidden VeraCrypt Volume*" memungkinkan pembuatan volume tersembunyi dalam volume VeraCrypt standar. Metode ini memungkinkan Anda untuk menyangkal keberadaan volume tersembunyi ini dalam kasus paksaan. Sebagai contoh, jika seseorang secara fisik memaksa Anda untuk mendekripsi perangkat Anda, Anda dapat mendekripsi hanya bagian standar untuk memuaskan penyerang tetapi tidak mengungkapkan bagian tersembunyi. Dalam contoh saya, saya akan tetap menggunakan volume standar.
![VeraCrypt](assets/notext/18.webp)
Pada halaman berikutnya, klik tombol "*Select Device...*".
![VeraCrypt](assets/notext/19.webp)
Sebuah jendela baru terbuka di mana Anda dapat memilih partisi dari perangkat penyimpanan Anda dari daftar disk yang tersedia di mesin Anda. Biasanya, partisi yang ingin Anda enkripsi akan terdaftar di bawah baris bertajuk "*Removable Disk N*". Setelah memilih partisi yang sesuai, klik tombol "*OK*".
![VeraCrypt](assets/notext/20.webp)
Dukungan yang dipilih muncul di kotak. Anda sekarang dapat klik tombol "*Next*". ![VeraCrypt](assets/notext/21.webp)
Selanjutnya, Anda perlu memilih antara opsi "*Create encrypted volume and format it*" atau "*Encrypt partition in place*". Seperti disebutkan sebelumnya, opsi pertama akan secara permanen menghapus semua data pada USB stick atau hard drive Anda. Pilih opsi ini hanya jika perangkat Anda kosong; jika tidak, Anda akan kehilangan semua data yang terkandung di dalamnya. Jika Anda ingin menyimpan data yang ada, Anda dapat sementara mentransfernya ke tempat lain, pilih "*Create encrypted volume and format it*" untuk proses yang lebih cepat yang menghapus segalanya, atau pilih "*Encrypt partition in place*". Opsi terakhir ini memungkinkan enkripsi volume tanpa menghapus data yang sudah ada, tetapi prosesnya akan jauh lebih lama. Untuk contoh ini, karena USB stick saya kosong, saya memilih "*Create encrypted volume and format it*", opsi yang menghapus segalanya.
![VeraCrypt](assets/notext/22.webp)
Selanjutnya, Anda akan memiliki opsi untuk memilih algoritma enkripsi dan fungsi hash. Kecuali Anda memiliki kebutuhan spesifik, saya menyarankan Anda untuk mempertahankan opsi default. Klik "*Next*" untuk melanjutkan.
![VeraCrypt](assets/notext/23.webp)
Pastikan ukuran yang ditunjukkan untuk volume Anda benar, untuk mengenkripsi seluruh ruang yang tersedia pada USB stick, dan bukan hanya sebagian. Setelah diverifikasi, klik "*Next*".
![VeraCrypt](assets/notext/24.webp)
Pada tahap ini, Anda perlu menetapkan kata sandi untuk mengenkripsi dan mendekripsi perangkat Anda. Penting untuk memilih kata sandi yang kuat untuk mencegah penyerang mendekripsi konten Anda dengan serangan brute force. Kata sandi harus acak, sepanjang mungkin, dan mencakup beberapa jenis karakter. Saya menyarankan Anda untuk memilih kata sandi acak setidaknya 20 karakter termasuk huruf kecil, huruf besar, angka, dan simbol.

Saya juga menyarankan Anda untuk menyimpan kata sandi Anda dalam manajer kata sandi. Ini memudahkan akses dan menghilangkan risiko lupa. Untuk kasus khusus kita, manajer kata sandi lebih disukai daripada media kertas. Memang, dalam kasus pencurian, meskipun perangkat penyimpanan Anda mungkin dicuri, kata sandi dalam manajer tidak dapat ditemukan oleh penyerang, yang akan mencegah akses ke data. Sebaliknya, jika manajer kata sandi Anda dikompromikan, akses fisik ke perangkat masih diperlukan untuk mengeksploitasi kata sandi dan mengakses data.

Untuk informasi lebih lanjut tentang pengelolaan kata sandi, saya menyarankan Anda untuk menemukan tutorial lengkap lainnya:
Masukkan kata sandi Anda di 2 kolom yang ditentukan, kemudian klik pada "*Next*". ![VeraCrypt](assets/notext/25.webp)
VeraCrypt kemudian akan bertanya apakah Anda berencana untuk menyimpan file yang lebih besar dari 4 GiB dalam volume terenkripsi. Pertanyaan ini memungkinkan perangkat lunak untuk memilih sistem file yang paling cocok. Umumnya, sistem FAT digunakan karena kompatibel dengan sebagian besar sistem operasi, tetapi memberlakukan batas ukuran file maksimum 4 GiB. Jika Anda perlu mengelola file yang lebih besar, Anda dapat memilih sistem exFAT.
![VeraCrypt](assets/notext/26.webp)
Selanjutnya, Anda akan mencapai halaman yang memungkinkan Anda untuk menghasilkan kunci acak. Kunci ini penting, karena akan digunakan untuk mengenkripsi dan mendekripsi data Anda. Kunci ini akan disimpan dalam bagian tertentu dari media Anda, yang sendiri diamankan oleh kata sandi yang Anda tetapkan sebelumnya. Untuk menghasilkan kunci enkripsi yang kuat, VeraCrypt membutuhkan entropi. Itulah mengapa perangkat lunak meminta Anda untuk menggerakkan mouse Anda secara acak di atas jendela; gerakan-gerakan ini kemudian digunakan untuk menghasilkan kunci. Terus gerakkan mouse sampai pengukur entropi sepenuhnya terisi. Kemudian, klik pada "*Format*" untuk mulai membuat volume terenkripsi.
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
Klik pada tombol "*Select Device...*".
![VeraCrypt](assets/notext/32.webp)
Dari daftar semua disk di mesin Anda, pilih volume terenkripsi pada media Anda, kemudian klik pada tombol "*OK*".
![VeraCrypt](assets/notext/33.webp)
Anda dapat melihat bahwa volume Anda telah terpilih dengan baik.
![VeraCrypt](assets/notext/34.webp)
Klik pada tombol "*Mount*".
![VeraCrypt](assets/notext/35.webp)
Masukkan kata sandi yang dipilih selama pembuatan volume, kemudian klik pada "*OK*".
![VeraCrypt](assets/notext/36.webp)
Anda dapat melihat bahwa volume Anda sekarang telah didekripsi dan dapat diakses pada huruf drive "*L:*".
![VeraCrypt](assets/notext/37.webp)
Untuk mengaksesnya, buka penjelajah file Anda dan pergi ke drive "*L:*" (atau huruf lain tergantung pada yang Anda pilih dalam langkah sebelumnya). ![VeraCrypt](assets/notext/38.webp)
Setelah menambahkan file pribadi Anda ke media, untuk mengenkripsi volume lagi, cukup klik pada tombol "*Dismount*".
![VeraCrypt](assets/notext/39.webp)
Volume Anda tidak lagi muncul di bawah huruf "*L:*". Dengan demikian, ia terenkripsi lagi.
![VeraCrypt](assets/notext/40.webp)
Anda sekarang dapat melepas media penyimpanan Anda.

Selamat, Anda sekarang memiliki media terenkripsi untuk menyimpan data pribadi Anda dengan aman, sehingga memiliki strategi lengkap 3-2-1 selain salinan di komputer Anda dan solusi penyimpanan online Anda.
Jika Anda ingin mendukung pengembangan VeraCrypt, Anda juga dapat membuat donasi dalam bitcoin [di halaman ini](https://www.veracrypt.fr/en/Donation.html).