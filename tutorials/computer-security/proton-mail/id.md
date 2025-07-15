---
name: Proton Mail
description: Mengatur kotak email yang aman
---
![cover](assets/cover.webp)

Kotak email merupakan elemen sentral dari aktivitas online Anda dan sering kali memainkan peran penting dalam keamanan siber Anda. Apabila penyerang berhasil menyusupi kotak email Anda, mereka akan dengan mudah memperoleh akses ke akun-akun Anda yang lain melalui fungsi "*forgot password* (lupa kata sandi)". Hal ini memungkinkan mereka untuk mengendalikan sosial media, rekening bank, dan layanan online lainnya, sebab saat ini alamat email sering digunakan sebagai pengidentifikasi unik identitas daring Anda. Oleh karena itu, mengamankan kotak email Anda sangat penting untuk melindungi diri dari serangan.

Untuk menjamin keamanan kotak email Anda, penting untuk menerapkan beberapa praktik baik sederhana yang akan kita pelajari dalam tutorial ini yang ditujukan bagi pemula dalam bidang komputer. Selain itu, penting untuk memilih penyedia email yang aman yang menawarkan opsi perlindungan canggih dan kebijakan perlindungan privasi yang kuat. Itulah sebabnya dalam tutorial ini saya merekomendasikan untuk mengenal ProtonMail. Meskipun Anda tidak memilih penyedia ini, praktik-praktik baik yang diberikan di sini dapat diterapkan pada kotak email mana pun untuk meningkatkan keamanannya.

## Mengapa menggunakan ProtonMail?

ProtonMail adalah solusi pesan yang cukup aman berkat beberapa fitur unggulan. Pertama, ProtonMail memastikan enkripsi end-to-end (ujung-ke-ujung) pada email Anda, yang berarti hanya pengirim dan penerima yang dapat membaca isinya. Secara teoretis, bahkan ProtonMail sendiri tidak dapat mengakses email penggunanya. Enkripsi ini diterapkan secara otomatis, sehingga tidak memerlukan keahlian teknis khusus dari pengguna.

Selain itu, ProtonMail mengintegrasikan teknologi canggih untuk melindungi privasi Anda, termasuk pemblokiran sistem pelacakan tertentu dan penyamaran alamat IP Anda. Berbasis di Swiss, perusahaan Proton diuntungkan oleh undang-undang perlindungan data yang ketat yang tidak ditemukan di negara lain. Ditambah lagi, ProtonMail adalah open-source,, yang memungkinkan para ahli independen untuk secara bebas mengaudit kode perangkat lunaknya.

Model bisnis Proton didasarkan pada sistem berlangganan, yang meyakinkan karena menunjukkan bahwa perusahaan didanai tanpa harus mengeksploitasi data penggunanya. Dalam tutorial ini, kita akan menjelajahi cara menggunakan versi gratis ProtonMail, tetapi juga tersedia beberapa tingkat langganan yang menawarkan lebih banyak fitur. Model bisnis ini lebih baik daripada sistem yang sepenuhnya gratis, yang dapat menimbulkan kekhawatiran tentang apakah data pribadi kita digunakan untuk keuntungan. Untungnya, hal ini tampaknya tidak terjadi pada ProtonMail.

## Membuat akun Proton

Kunjungi situs resmi Proton: https://proton.me/
![proton](assets/notext/01.webp)

Klik tombol "*Create an account (Buat akun)*":
![proton](assets/notext/02.webp)

Anda memiliki opsi untuk memilih dari berbagai rencana sesuai dengan kebutuhan Anda. Untuk memulai, Anda dapat memilih akun gratis, yang akan memungkinkan Anda untuk menguji layanan dasar dari ProtonMail. Nanti, jika Anda ingin mengakses fitur tambahan dan perangkat lunak Proton lainnya seperti Kalender, VPN, atau Pengelola Kata Sandi, Anda dapat mempertimbangkan untuk berlangganan rencana berbayar.
![proton](assets/notext/03.webp)

Anda kemudian tiba di halaman pembuatan akun.
![proton](assets/notext/04.webp)

Anda dapat memilih nama domain yang Anda sukai untuk alamat email Anda dengan mengklik panah kecil. Pilihan ini tidak berdampak pada apa yang mengikuti.
![proton](assets/notext/05.webp)

Juga, pilih nama pengguna untuk alamat email Anda.
![proton](assets/notext/06.webp)

Anda kemudian diminta untuk menetapkan kata sandi. Penting untuk memilih kata sandi yang kuat pada tahap ini, karena itu akan memungkinkan akses ke kotak surat Anda. Kata sandi yang kuat harus sepanjang mungkin, menggunakan berbagai karakter yang luas, dan dipilih secara acak. Pada tahun 2024, rekomendasi minimum untuk kata sandi yang aman adalah 13 karakter termasuk angka, huruf kecil dan huruf besar, serta simbol, asalkan kata sandi tersebut benar-benar acak. Namun, saya merekomendasikan untuk memilih kata sandi setidaknya 20 karakter, termasuk semua jenis karakter yang mungkin, untuk memastikan keamanannya lebih lama.
Penggunaan manajer kata sandi adalah praktik yang sangat baik. Ini tidak hanya memungkinkan Anda untuk menyimpan kata sandi Anda secara aman tanpa harus mengingatnya, tetapi juga dapat menghasilkan kata sandi yang panjang dan acak untuk Anda. Memang benar manusia sangat buruk dalam menciptakan urutan acak, dan kata sandi yang tidak cukup acak dapat rentan terhadap serangan brute force. Saya juga merekomendasikan untuk berkonsultasi dengan tutorial lengkap kami tentang pengaturan manajer kata sandi untuk lebih detail mengenai topik ini:
https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

![proton](assets/notext/07.webp)
Klik tombol "*Create Account*".

![proton](assets/notext/08.webp)

Selesaikan CAPTCHA.
![proton](assets/notext/09.webp)

Pilih nama tampilan. Ini adalah nama yang akan ditampilkan kepada penerima Anda ketika Anda mengirim email. Pilih nama asli Anda atau nama panggilan.
![proton](assets/notext/09.webp)

Proton juga menawarkan Anda opsi untuk menetapkan metode pemulihan akun Anda, baik melalui nomor telepon Anda atau dengan alamat email alternatif. Penting untuk dipahami bahwa opsi ini dapat meningkatkan permukaan serangan pada kotak masuk email Anda. Bagi Anda, ini adalah langkah keamanan tambahan untuk mendapatkan kembali akses ke akun Anda jika Anda lupa kata sandi, tetapi bagi peretas, ini adalah kesempatan ekstra untuk mencoba membobol akun Anda. Anda tidak diwajibkan untuk memilih opsi pemulihan ini, tetapi jika Anda memutuskan untuk tidak melakukannya, pastikan untuk menyimpan salinan kata sandi Anda yang aman. Tanpanya, jika Anda kehilangan kata sandi, Anda akan tidak dapat memulihkan akses ke kotak masuk email Anda.
![proton](assets/notext/11.webp)

## Mengatur Kotak Surat Proton Anda

Selamat, kotak surat Proton Anda sekarang telah dibuat! Mulailah dengan memilih warna untuk tema kotak surat Anda.

![proton](assets/notext/12.webp)

Jika Anda mau, Anda juga dapat mengatur penerusan email Anda dari akun Gmail lama ke akun ProtonMail baru Anda.

![proton](assets/notext/13.webp)

Setelah berada di antarmuka kotak surat Anda, saya menyarankan Anda untuk melihat pengaturan untuk menyesuaikannya. Klik pada ikon roda gigi di sudut kanan atas.

![proton](assets/notext/14.webp)

Kemudian klik tombol "*All settings*".

![proton](assets/notext/15.webp)

Di tab "*Dashboard*", Anda akan menemukan informasi terkait akun Anda. Dengan menggulir ke bawah di bagian ini, Anda memiliki opsi untuk memilih jenis email yang bersedia Anda terima dari Proton. Jika Anda lebih memilih untuk tidak menerima notifikasi promosi atau informatif, Anda dapat memilih untuk tidak memilih semua.

![proton](assets/notext/16.webp)

Di tab "*Upgrade plan*", Anda dapat memilih rencana berbayar dengan fitur baru.

![proton](assets/notext/17.webp)

Di tab "*Recovery*", Anda dapat menambah atau mengubah metode pemulihan Anda.

![proton](assets/notext/18.webp)

Di tab "*Account and password*", Anda dapat mengubah nama pengguna Anda, serta metode untuk mengamankan akun Anda.

![proton](assets/notext/19.webp)

Untuk saat ini, kotak surat Anda hanya diamankan dengan kata sandi. Saya menyarankan Anda setidaknya untuk menambahkan perlindungan otentikasi dua faktor dengan aplikasi. Untuk melakukan ini, klik pada kotak centang.

![proton](assets/notext/20.webp)

Konfirmasi kata sandi Anda.

![proton](assets/notext/21.webp)

Kemudian pindai kode QR menggunakan aplikasi 2FA Anda.

![proton](assets/notext/22.webp)

Untuk informasi lebih lanjut, saya menyarankan Anda untuk melihat tutorial kami tentang cara menggunakan aplikasi 2FA.
Di tab "*Language and time*", Anda dapat mengubah bahasa antarmuka serta zona waktu.
Di tab "*Appearance*", Anda dapat mengubah warna antarmuka Anda.

Di tab "*Security and privacy*", Anda memiliki akses ke berbagai opsi keamanan. Beberapa opsi ini hanya tersedia dengan rencana berbayar. Anda juga memiliki opsi untuk menonaktifkan pengumpulan data Anda oleh Proton, yang menggunakan informasi ini untuk diagnostik dan resolusi bug.

Di tab "*Import*", Anda memiliki opsi untuk mengelola migrasi email lama Anda ke akun ProtonMail baru Anda. Jika Anda lebih memilih untuk memulai dengan kotak surat yang sepenuhnya baru, tanpa mengimpor email lama Anda, Anda dapat memilih untuk mengabaikan opsi ini.

Tab "*Get the apps*" memungkinkan Anda untuk mengunduh aplikasi seluler Proton dan perangkat lunak desktop untuk mengelola kotak surat Anda di platform tersebut. Jika Anda mau, Anda dapat terus menggunakan hanya versi web dari kotak surat Anda, yang saat ini Anda gunakan, karena menawarkan fitur yang sama.

Di tab "*Messages and composing*", Anda memiliki berbagai opsi kustomisasi untuk kotak surat Anda.

Di tab "*Email privacy*", Anda dapat memilih opsi mengenai privasi email Anda.

Di tab "*Identity and addresses*", Anda memiliki opsi untuk menyesuaikan tanda tangan email Anda. Jika Anda memiliki akun berbayar, Anda juga dapat membuat beberapa alamat email yang berbeda yang semuanya akan dikelola dari akun yang sama. Ini bisa sangat berguna untuk memisahkan penggunaan Anda yang berbeda.

Di tab "*Folders and labels*", Anda dapat membuat folder dan label untuk mengorganisir kotak surat Anda.

Tab "*Filters*" memungkinkan Anda untuk mengelola filter untuk email yang Anda terima.

Tab "*Forward and auto-reply*" memungkinkan Anda untuk mengelola penerusan dan balasan otomatis untuk email Anda.

Di tab "*Domain names*", Anda memiliki opsi untuk menyiapkan alamat email menggunakan domain Anda sendiri, yang bisa berguna jika Anda memiliki situs web. Untuk penggunaan pribadi, tidak selalu diperlukan untuk menggunakan fitur ini.

Tab "*Encryption and keys*" memungkinkan Anda untuk mengelola opsi enkripsi untuk email Anda. Untuk pengguna pemula, umumnya tidak perlu untuk memodifikasi pengaturan di bagian ini.

Dan akhirnya, tab "*IMAP/SMTP*" menawarkan Anda kemungkinan untuk mengonfigurasi jembatan untuk menggunakan ProtonMail dengan perangkat lunak email seperti Outlook atau Apple Mail.

Untuk kembali ke halaman utama kotak surat Anda, klik tombol "*Inbox*" di kiri atas.

## Menggunakan Kotak Surat ProtonMail Anda

Untuk mengirim email, sangatlah mudah, cukup klik tombol "*New Message*" di kiri atas.

Di bidang "*To*", masukkan alamat email penerima Anda.

Di bidang "*Subject*", masukkan subjek email Anda.

Tulis pesan Anda.
![proton](assets/notext/41.webp)
Akhirnya, klik tombol "*Kirim*" untuk mengirim email Anda.

![proton](assets/notext/42.webp)

Anda kemudian dapat menemukan pesan yang telah Anda kirim di tab "*Terkirim*".

![proton](assets/notext/43.webp)

Tab "*Kotak Masuk*" berisi email yang telah Anda terima.

![proton](assets/notext/44.webp)

Anda dapat membaca email Anda dengan mengkliknya, dan kemudian mengorganisirnya ke dalam folder yang telah Anda buat.

![proton](assets/notext/45.webp)

## Masuk ke Kotak Surat ProtonMail Anda

Seperti yang telah disebutkan sebelumnya, Anda memiliki opsi untuk menggunakan kotak surat ProtonMail Anda baik melalui versi web, dengan mengunduh perangkat lunak desktop, atau melalui aplikasi seluler. Untuk mengunduh perangkat lunaknya, Anda dapat mengunjungi halaman resmi: https://proton.me/mail/download

Jika Anda lebih memilih untuk hanya menggunakan versi web dari ProtonMail, pertimbangkan untuk menambahkan halaman tersebut ke favorit browser Anda untuk akses yang lebih mudah di masa depan dan untuk menghindari upaya phishing.

Untuk mengaksesnya, kunjungi URL berikut: https://account.proton.me/mail

![proton](assets/notext/46.webp)

Masukkan nama pengguna dan kata sandi Anda, kemudian klik tombol "*Masuk*". Jika Anda telah mengaktifkan autentikasi dua faktor (2FA), Anda juga akan diminta untuk memasukkan 6 digit dinamis yang dihasilkan oleh aplikasi Anda.

![proton](assets/notext/47.webp)

Anda akan kembali ke kotak masuk ProtonMail Anda.

![proton](assets/notext/48.webp)
