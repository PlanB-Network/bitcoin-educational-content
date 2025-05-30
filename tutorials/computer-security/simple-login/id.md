---
name: Login Sederhana
description: Identitas dilindungi dengan alias
---
![cover](assets/cover.webp)

## Login = email = hilangnya privasi


Di dunia digital, sudah menjadi praktik standar untuk memiliki akun untuk setiap platform yang ingin diakses.

Setiap layanan ini memerlukan login, biasanya dikaitkan dengan pasangan _username_ dan _password_. Sering kali, nama pengguna adalah email pribadi pengguna.


Ketika menggunakan email pribadi Address untuk setiap login, mudah untuk membayangkan konsekuensi pertama: hilangnya kerahasiaan, yang menjadi sangat penting jika Address terdiri dari _name.surname@serviceemail.com_.


Para pengembang peralatan sumber terbuka telah menciptakan serangkaian paket aplikasi, yang lahir dengan tepat untuk membuat para pengguna mendapatkan kembali sedikit privasi: mereka masih akan masuk, tetapi menggunakan alias alih-alih alat yang mengungkapkan identitas pribadi mereka.


Yang paling sederhana di antara yang telah saya coba secara pribadi dan masih saya uji adalah [Simple Login] (https://simplelogin.io/).


## Alias


Alias email hanya mengganti bagian _nama.nama_ pada Address email Anda dengan nama fiktif. Bagi pengguna, tidak ada yang berubah; layanan alias meneruskan email ke dan dari Address biasa seperti biasa. Semua orang dapat terus menggunakan kotak masuk mereka seperti biasa, tetapi alih-alih menampilkan nama asli mereka, kotak masuk akan menampilkan pengguna yang tidak dapat dikenali. Layanan ini harus efisien, dan sejauh ini, Simple Login telah terbukti seperti itu.


Ketika mengunjungi situs Simple Login untuk pertama kalinya, Anda harus membuat akun (di sini juga!), menggunakan email "resmi" Address. Di sini, Anda harus memasukkan email, kata sandi, dan memecahkan captcha.


![image](assets/it/02.webp)


Simple Login akan mengirimkan pesan verifikasi ke email yang ditunjukkan pada Address. Daripada mengklik tombol verifikasi, disarankan untuk menyalin tautan dan menempelkannya ke bilah Address.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Dasbor Login Sederhana langsung terbuka, dengan tutorial singkat untuk navigasi.


![image](assets/it/05.webp)


Perlu dicatat bahwa Simple Login secara otomatis mengaktifkan langganan buletin, yang dapat dinonaktifkan dari perintah yang sesuai.


![image](assets/it/06.webp)


## Pengaturan


Anda bisa langsung melihat pada _Pengaturan_ untuk menemukan fitur-fitur layanan ini. Login Sederhana dimulai dengan semua opsi aktif, termasuk yang _Premium_, yang tetap dapat digunakan selama 10 hari. Setelah masa uji coba selesai, Anda akan memiliki kemungkinan untuk membuat 10 alias dengan profil ini dan Anda dapat langsung menautkan email Proton Anda, karena Simple Login telah diakuisisi oleh penyedia email Swiss.


![image](assets/it/07.webp)


Anda bisa mengatur serangkaian parameter, atau memeriksa apakah email Anda telah disusupi dalam hal privasi.


![image](assets/it/08.webp)


Terakhir, Anda bisa mengekspor cadangan profil Anda, atau mengimpornya dari penyedia lain.


![image](assets/it/09.webp)


### Email Kantor


Mereka yang menggunakan email dengan domain pribadi sebagai email kantor dapat mengatur domain pribadi mereka.


![image](assets/it/10.webp)


Dari panel utama, dengan memilih _Mailboxes_, bahkan dimungkinkan untuk menambahkan alamat email lain dan juga menggunakan alias yang akan dibuat. Dalam tutorial ini, sebagai contoh, saya memutuskan untuk membuat profil dengan mailbox _gmail.com_, dan kemudian mengaitkan _proton.me_ Address.


![image](assets/it/11.webp)


Menambahkan Address baru, terutama jika itu milik penyedia Proton, prosedur yang dipandu menunjukkan kemungkinan untuk masuk ke mode _sudo_, pengguna super. Login sederhana akan meminta untuk memasukkan kata sandi kotak surat ini, untuk membuktikan keabsahan Ownership.


⚠️ **Saya pribadi menyarankan agar Anda tidak melakukan hal ini**. ⚠️


![image](assets/it/12.webp)


**Lebih baik mengakses kotak email -> salin tautan untuk verifikasi dan tempelkan di bilah URL -> dan dapatkan verifikasi tanpa mengungkapkan kata sandi.**


![image](assets/it/13.webp)


Dari dua alamat yang dimasukkan, satu alamat menjadi default dan yang lainnya adalah alamat sekunder, tetapi keduanya dapat dengan mudah dialihkan, dan pengaturannya mudah dikenali di dasbor.


![image](assets/it/14.webp)


Setelah menambahkan email kedua Address (opsional), mari kita lihat apa yang dapat kita lakukan dengan Simple Login.


## Pembuatan nama alias


Pada panel, opsi menu pertama diberi label _Alias_, yang merupakan tempat Anda dapat membuatnya. Anda memiliki opsi untuk membuat alias generate secara acak dengan mengeklik tombol Random Alias, yang merupakan tombol Green yang ditunjukkan pada foto berikutnya. Fitur ini menciptakan email Address yang unik dan menarik.


![image](assets/it/24.webp)


Namun, jika Anda ingin membedakan layanan dengan memberikan nama yang berbeda, Anda harus memilih _New Custom Alias_. Dengan demikian, Anda bisa memberikan nama alias sesuai dengan nama layanan yang ingin Anda akses (media sosial, penyedia layanan, acara online, orang asing yang ditemui secara kebetulan, dll.). Selebihnya ditangani oleh Simple Login.

Untuk iseng-iseng (tapi sebenarnya tidak, sejujurnya) saya memutuskan untuk membuat nama samaran untuk bank tersebut dan menamakannya `BANK`. Meskipun benar bahwa bank saya mengetahui segalanya tentang saya, saya merasa lucu berkomunikasi dengan mereka menggunakan email Address yang tidak dapat dimengerti oleh mereka. Simple Login memang menghasilkan nama acak, yang dipisahkan dari nama yang kita pilih dengan tanda `.`


Di sini, email baru Address bisa menjadi:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- dan seterusnya


Seseorang dapat memilih lebih dari satu domain: domain publik tersedia dengan paket gratis, sementara yang lain, yang ditunjukkan sebagai pribadi (termasuk _@simplelogin.com_), memperluas pilihan bagi pengguna yang memutuskan untuk berlangganan paket berbayar.


![image](assets/it/15.webp)


Setelah akhiran acak dan domain telah dipilih, Anda dapat mengatur apakah Address yang baru (dan aneh) ini akan berfungsi sebagai alias hanya untuk salah satu kotak email pribadi, atau untuk semuanya. Alias menjadi siap dan aktif setelah mengklik _Buat_


![image](assets/it/16.webp)


Email baru Address telah dibuat dan sekarang sudah terlihat, siap untuk dikirim (ke bank!) hanya dengan menyalinnya.


![image](assets/it/18.webp)


Pada titik ini, Anda bisa fokus pada pembuatan alias untuk setiap layanan atau platform yang ingin Anda akses dan di mana email diperlukan sebagai parameter penting untuk membuat akun.


![image](assets/it/19.webp)


Bagi para penggemar privasi, ada juga opsi untuk membuat email generate menjadi Address berdasarkan protokol UUID (bukan berdasarkan nama yang dapat diidentifikasi), yang menciptakan pengenal unik 128-bit yang tidak dikendalikan oleh pihak terpusat. Fitur ini, yang berguna untuk akun-akun sensitif, bisa ditemukan di menu _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Seperti yang Anda lihat, ini adalah email Address yang membutuhkan pengelolaan yang tepat.


Jika Anda berubah pikiran dan tidak ingin lagi menggunakan alias, cukup klik pada perintah _Lebih_ pada masing-masing alias dan pilih _Hapus_.


![image](assets/it/23.webp)


## Alias Manajemen


Membuat nama samaran itu sederhana, begitu juga dengan pengelolaannya, yang hanya membutuhkan sedikit perhatian dan disiplin. Semua lalu lintas, pada kenyataannya, masih akan melewati kotak masuk email yang telah kita tetapkan, di awal, sebagai yang resmi. Pemberitahuan dan komunikasi penting dari platform akan terus masuk ke Gmail, Proton, atau apa pun penyedia emailnya.


Hasilnya, bagaimanapun juga, kami telah melestarikan Address utama yang, sejak saat pembuatan alias, kami bebas memutuskan kepada siapa kami akan mengungkapkannya dan siapa yang tidak.


Nama samaran dapat digunakan untuk menerima dan mengirim: pengguna lain akan menerima balasan dari alias.preoccupy789@8shield.net, jika nama samaran yang dipilih adalah nama samaran untuk penerima tersebut.


## Kelebihan


Secara keseluruhan, menggunakan alias adalah cara yang efektif untuk melindungi identitas dan privasi Anda. Alamat email sering kali dikumpulkan oleh pialang data dan situs web untuk melacak kebiasaan dan perilaku pengguna. Meskipun nama samaran tidak membuat Anda sepenuhnya tidak dapat dilacak, namun secara konsisten menggunakan nama samaran merupakan langkah positif untuk melindungi informasi Anda. Selain itu, di "desa digital global" kita, di mana peretasan, penjualan data, dan pelanggaran keamanan adalah hal yang umum terjadi, kemungkinan besar email yang Anda gunakan untuk mendaftar di berbagai situs web telah disusupi atau menjadi target.


Nama samaran yang unik, yang digunakan untuk setiap login, **segera memungkinkan kita untuk memahami platform mana yang mengirimkan spam (atau lebih buruk) ke kotak surat kita, karena email diidentifikasi oleh alias yang terkait dengannya**. Anda tidak tahu berapa banyak spam dan phishing yang berasal dari apa yang disebut saluran yang dapat diandalkan, karena mereka bersifat institusional, sampai Anda mulai menggunakan alias untuk bank, alias untuk layanan pos, atau alias khusus untuk beberapa layanan pemerintah yang wajib. Setelah pengirim spam (atau lebih buruk lagi) teridentifikasi, Anda akan tahu bahwa situs tersebut telah disusupi, mengambil setiap tindakan pencegahan untuk melindungi semua data yang diberikan (pikirkan tentang kartu kredit!) ke situs web tertentu, yang mungkin menyadari pembobolan beberapa minggu kemudian.


Mengenai Login Sederhana, alat ini memiliki fitur-fitur berikut:



- (juga dari F-Droid) dan ekstensi peramban, untuk mengelola alias dalam situasi apa pun;
- autentikasi dua faktor untuk setiap nama samaran baru, yang meningkatkan tingkat kemandirian dari layanan itu sendiri;
- Dukungan PGP (untuk pengguna _Premium);
- pembuatan sederhana dari setiap jenis alias (kustom, acak, dan UUID);
- di antara paket gratis di sektor ini, kemampuan untuk menggunakan alias dengan lebih banyak kotak email "resmi". Pesaing lainnya membatasi hanya satu saja.


## Kekurangan


- 10 alias mungkin tidak cukup jika Anda berencana untuk menggunakan Simple Login secara ekstensif. Dalam hal ini, paket berbayar, yang cukup terjangkau, berguna untuk meningkatkan jumlah kemungkinan alias yang tersedia.
- Tidak mungkin membuat alias dengan nama dan domain tertentu. Akhiran acak, yang ditambahkan setelah nama yang kita pilih, menghasilkan Address yang bisa dibilang aneh. Media sosial tradisional biasanya menolak untuk memberikan akun yang dibuat dengan jenis alamat email ini. Nostr memperbaikinya!
- Jika Anda menggunakan nama samaran untuk mengirim pesan kepada seseorang, pesan tersebut akan mudah masuk ke folder spam penerima. Sebagai langkah pertama, disarankan untuk menggunakan nama samaran untuk menerima, seperti halnya dalam hal membuat akun, berlangganan milis, dll.