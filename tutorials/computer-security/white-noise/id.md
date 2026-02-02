---
name: White Noise
description: Aplikasi perpesanan pribadi yang terdesentralisasi berdasarkan protokol Nostr dan MLS
---

![cover](assets/cover.webp)




## Pendahuluan



"Di tengah-tengah kesulitan, ada peluang". Kutipan dari Albert Einstein ini mengingatkan kita bahwa masalah tidaklah pasti, tetapi mengandung benih-benih solusi baru yang inovatif.



Motivasi di balik peluncuran solusi yang kami sajikan dalam tutorial ini mengilustrasikan hal ini dengan sempurna. Ini adalah **White Noise**, yang lahir dari kebutuhan.



Dalam kata-kata pendirinya, Max Hillebrand, yang dilaporkan oleh *Bitcoin Magazine*: "Kami meluncurkan proyek ini karena tidak adanya alternatif lain." Dia menjelaskan bahwa "aplikasi enkripsi yang ada tidak efisien dalam skala besar: menambahkan 100 orang ke dalam sebuah percakapan grup akan sangat memperlambat enkripsi. Sementara itu, platform terdesentralisasi tidak menawarkan pesan pribadi. Akhirnya, jaringan relai terbuka Nostr memungkinkan semua orang untuk menyebarkan ide, tetapi perlindungan pesan langsung masih sangat tidak memadai. Kami menyadari: untuk melindungi kebebasan, kami harus menggabungkan sistem-sistem ini."



## Apa itu White Noise?



White Noise adalah aplikasi perpesanan sumber terbuka yang dikembangkan oleh tim nirlaba. Aplikasi ini mengedepankan keamanan, privasi, dan desentralisasi. Tidak seperti aplikasi konvensional, aplikasi ini tidak memerlukan nomor telepon atau alamat email.


White Noise dibedakan dengan integrasi dua protokol fundamental - Nostr dan MLS - yang membentuk dasar teknisnya.



Nostr (Catatan dan Hal-hal Lain yang Ditransmisikan oleh Relai) adalah protokol sumber terbuka yang terdesentralisasi yang dirancang untuk menolak sensor.  Protokol ini menggunakan relay, pasangan kunci, dan klien.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Dengan white Noise, Anda bahkan dapat memilih pengaturan relai Anda sendiri untuk memaksimalkan privasi.



MLS (Messaging Layer Security), di sisi lain, adalah protokol keamanan yang memungkinkan enkripsi pesan secara end-to-end. Dengan kata lain, pesan hanya dapat diakses pada titik akhir, yaitu pengirim dan penerima pesan. Ini berarti bahwa relay yang terlibat dalam perutean pesan tidak dapat mengakses isinya.



Berikut ini adalah perbandingan singkat antara White Noise dan sejumlah aplikasi perpesanan yang paling terkenal.





| Poin perbandingan           | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Enkripsi E2EE / 1:1         | ✅ Ya         | Opsional   | ✅ Ya             | ✅ Ya    | ✅ Ya     | ✅ Ya              | ✅ Ya   |
| Enkripsi grup E2EE          | ✅ Ya         | ❌ Tidak    | ✅ Ya             | ✅ Ya    | ✅ Ya     | Opsional          | ✅ Ya   |
| Anonimisasi identitas       | ✅ Ya         | Opsional   | ❌ Tidak          | ✅ Ya    | ❌ Tidak  | ❌ Tidak           | ❌ Tidak|
| Server sumber terbuka       | ✅ Ya         | ❌ Tidak    | ❌ Tidak          | ✅ Ya    | ❌ Tidak  | ❌ Tidak           | ✅ Ya   |
| Klien sumber terbuka        | ✅ Ya         | ✅ Ya        | ❌ Tidak          | ✅ Ya    | ❌ Tidak  | ❌ Tidak           | ✅ Ya   |
| Server terdesentralisasi    | ✅ Ya         | ❌ Tidak    | ❌ Tidak          | ✅ Ya    | ❌ Tidak  | ❌ Tidak           | ❌ Tidak|
| Tahun pembuatan             | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Memulai dengan White Noise



### Instalasi White Noise



Buka [situs web White Noise](https://www.whitenoise.chat/), lalu klik **Unduh**.



![screen](assets/fr/03.webp)



White Noise saat ini hanya tersedia di perangkat seluler.


Pada antarmuka baru yang muncul, tekan :





- tombol **Zapstore** atau **Android APK** jika Anda ingin mengunduhnya di Android;
- pada tombol **iOS TestFlight** jika Anda menggunakan iPhone.



![screen](assets/fr/04.webp)



Untuk keperluan tutorial ini, kita akan melakukan pengunduhan Android.


Jika Anda memilih untuk mengunduh melalui **Zapstore**, Anda akan diarahkan ke sana. Setelah berada di Zapstore, ketik **White Noise** di kolom pencarian. Kemudian lanjutkan untuk mengunduh dengan mengklik **Instal**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Jika Anda memilih untuk mengunduh file APK, Anda akan diarahkan ke repositori GitHub White Noise untuk memilih versi yang tepat untuk ponsel cerdas Anda.



File APK yang tersedia adalah file :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), cocok untuk ponsel terbaru dengan prosesor 64-bit;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) cocok untuk ponsel lama dengan prosesor 32-bit.



Anda juga memiliki file **.sha256**, yang merupakan checksum untuk memverifikasi integritas unduhan.



![screen](assets/fr/07.webp)



Setelah pengunduhan selesai, instal dan buka aplikasi.



![screen](assets/fr/08.webp)



### Penyiapan akun pengguna awal



Untuk koneksi pertama Anda ke White Noise, tekan tombol **Daftar**.



![screen](assets/fr/09.webp)



Selanjutnya, konfigurasikan profil Anda dengan memilih foto profil, nama, dan menambahkan deskripsi singkat tentang diri Anda. Anda tidak perlu mengisi identitas asli Anda (nama dan foto).


Perhatikan bahwa White Noise secara otomatis memilih nama (nama samaran) untuk Anda, yang dapat Anda pertahankan atau ubah. Terakhir, tekan tombol **End**.



![screen](assets/fr/10.webp)



Anda akan diarahkan ke **layar beranda** White Noise, di mana percakapan Anda akan terdaftar. Akun Anda sekarang sudah diatur dan siap digunakan. Anda dapat membagikan profil Anda atau mencari teman untuk memulai obrolan.



![screen](assets/fr/11.webp)




### Menemukan antarmuka White Noise



Pada antarmuka utama, di bagian atas layar, Anda akan melihat :



Di sudut kiri atas, ikon profil adalah gambar mini foto profil Anda, atau huruf pertama dari nama profil Anda. Klik ikon tersebut untuk mengakses pengaturan akun Anda.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Di sudut kanan atas, Anda akan menemukan ikon untuk memulai percakapan baru.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Pengaturan akun pengguna



Tekan ikon profil di sudut kiri atas untuk mengakses pengaturan.



![screen](assets/fr/16.webp)



Di bagian atas antarmuka **Pengaturan**, Anda akan menemukan foto dan nama profil Anda, diikuti dengan kunci publik Anda, yang dapat Anda bagikan menggunakan kode QR di sebelahnya.



![screen](assets/fr/17.webp)



Tepat di bawah, Anda akan menemukan tombol **Ubah akun**, yang memungkinkan Anda terhubung ke profil lain di dalam aplikasi.



![screen](assets/fr/18.webp)



Kemudian, Anda memiliki bagian pertama dengan empat (4) sub-menu, seperti :





- Mengubah profil**



Dalam submenu ini, Anda dapat memodifikasi nama profil, alamat Nostr (NIP-05)... Jangan lupa klik **Save** untuk menyimpan perubahan Anda.



![screen](assets/fr/19.webp)





- Tombol profil** Kunci profil



Di sini Anda memiliki akses ke kunci publik dan pribadi (rahasia) Anda. Seperti yang diingatkan oleh White Noise, kunci pribadi Anda tidak boleh dibocorkan dalam kondisi apa pun.



![screen](assets/fr/20.webp)





- Relai utama



Dalam submenu ini, Anda dapat menambah atau menghapus **relay umum** (relay yang ditetapkan untuk digunakan dalam semua aplikasi Nostr Anda), **relay kotak masuk**, dan **relay paket kunci**.



Untuk melakukannya, ketuk ikon **sampah** di depan relai untuk menghapusnya, atau ketuk ikon **+** (plus) untuk menambahkan relai baru.



![screen](assets/fr/21.webp)





- Memutuskan sambungan**



Klik pada sub-menu ini untuk memutuskan akun Anda dari aplikasi. Namun pastikan Anda telah menyimpan kunci pribadi Anda secara offline, jika tidak, Anda tidak akan dapat masuk lagi nanti.



![screen](assets/fr/22.webp)




Bagian kedua menawarkan sub-menu:





- Pengaturan aplikasi



Di sini Anda dapat menentukan tampilan (tema dan bahasa tampilan) aplikasi, dan bahkan menghapus data jika Anda merasa telah disusupi, atau jika Anda sendiri merasa berisiko.



![screen](assets/fr/23.webp)





- Donasi ke White Noise



Anda dapat mendukung tim di belakang White Noise (organisasi nirlaba) dengan donasi melalui alamat Lightning mereka atau alamat pembayaran diam-diam Bitcoin.



![screen](assets/fr/24.webp)



Terakhir, di bagian paling bawah terdapat **pengaturan pengembang**.



![screen](assets/fr/25.webp)




## Memulai percakapan



Sekarang mari kita lihat cara memulai percakapan. Pada saat artikel ini ditulis, White Noise menawarkan tiga opsi komunikasi. Secara berurutan, kita akan menjelajahi **Private Conversations** (**Chat 1:1**), yaitu antara Anda dan satu orang lain, **Group Conversations** dan **Mengirim File Multimedia**.




### Kucing 1:1



Dari antarmuka utama, untuk menambahkan koresponden baru, klik ikon untuk memulai percakapan baru.


Kemudian pindai kode QR kunci publik (1) atau tempelkan kunci publik (2) koresponden baru Anda ke dalam bilah pencarian untuk menemukannya.



![screen](assets/fr/26.webp)



Kemudian tekan tombol **Mulai percakapan** untuk memulai percakapan dengan koresponden Anda. Anda juga dapat **Mengikuti** koresponden Anda atau mengundangnya ke percakapan grup dengan menekan tombol **Tambahkan ke grup**.



![screen](assets/fr/27.webp)



Pesan pertama Anda kepada koresponden baru mirip dengan permintaan undangan. Permintaan ini harus diterima oleh koresponden Anda sebelum Anda dapat berkomunikasi dengannya. Jika mereka menolak, maka tidak ada percakapan yang bisa dilakukan.



![screen](assets/fr/28.webp)



Terlebih lagi, selama mereka tidak menerima undangan Anda, mereka tidak akan dapat membaca isi pesan awal Anda.



Setelah dia menerima undangan Anda, dia sekarang dapat membalas Anda, dan Anda berdua dapat berkomunikasi dengan lancar dan aman.



![screen](assets/fr/29.webp)



Terlebih lagi, dalam diskusi, Anda memiliki fungsi tambahan.



Anda dapat menekan lama pada pesan tertentu untuk menampilkan opsi, misalnya :




- bereaksi terhadap pesan dengan emoji (1) ;
- membuat **kutipan langsung** untuk membalas pesan dengan menekan **Balas** (2) ;
- salin pesan dengan menekan **Salin** (3).



![screen](assets/fr/30.webp)





- hapus pesan dengan tombol **Hapus** hanya jika pesan tersebut berasal dari Anda.



![screen](assets/fr/31.webp)



Anda dapat mencari di dalam percakapan.



Klik avatar koresponden di bagian atas layar untuk mengakses "informasi percakapan" dan sentuh tombol **Cari dalam percakapan**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Pada bilah pencarian yang muncul, ketik kata yang ingin Anda cari dan luncurkan pencarian. Anda akan melihat kata pencarian Anda disorot dengan huruf **bold**.



![screen](assets/fr/34.webp)




### Percakapan kelompok



Grup percakapan dapat dibuat pada White Noise.



Untuk melakukannya, sentuh ikon pada antarmuka awal percakapan baru, lalu klik **Percakapan grup baru**. Kemudian, pada bilah pencarian, masukkan kunci publik dari anggota pertama yang ingin Anda tambahkan ke grup.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Akhirnya, jika opsi ini tidak berhasil, dari antarmuka **Mulai percakapan baru**, masukkan kunci publik dari anggota pertama yang ingin Anda tambahkan ke grup di bilah pencarian. Anda juga dapat memindai kode QR yang terkait dengan kunci publiknya.



Kali ini, alih-alih mengetuk tombol **Mulai percakapan**, klik tombol **Tambahkan ke grup** sebagai gantinya.



![screen](assets/fr/37.webp)



Pada menu pop-up yang muncul, ketuk **Percakapan grup baru**.



![screen](assets/fr/38.webp)



Kemudian tekan **Lanjutkan** (Anda tidak perlu memasukkan kunci publiknya lagi).



![screen](assets/fr/39.webp)



Sebagai pembuat grup, Anda secara otomatis menjadi administratornya. Isi rincian grup, seperti **nama dan deskripsi grup**, lalu klik tombol **Buat grup**.



![screen](assets/fr/40.webp)



Pengguna yang Anda tambahkan sebagai anggota pertama, dan pengguna lain yang Anda tambahkan setelahnya, akan menerima notifikasi yang mengundang mereka untuk bergabung dengan grup. Mereka harus menerima dengan mengeklik **Terima** untuk bergabung dengan grup.



![screen](assets/fr/41.webp)



Anda juga dapat menambahkan anggota baru yang sudah mengobrol dengan Anda ke grup yang sudah ada. Untuk melakukannya, klik avatar koresponden di bagian atas layar untuk mengakses "informasi percakapan" dan ketuk tombol **Tambahkan ke grup**.



![screen](assets/fr/42.webp)



Pada antarmuka baru yang muncul, **centang** grup yang ingin Anda tambahkan, lalu ketuk **Tambahkan ke grup**. Yang perlu dilakukan hanyalah menunggu sampai dia setuju untuk bergabung dengan grup.



![screen](assets/fr/43.webp)



Perhatikan bahwa hanya administrator grup yang dapat memodifikasi informasi grup dan menambahkan atau mengeluarkan anggota. Selain itu, rotasi kunci mencegah anggota yang diblokir untuk mendekripsi pesan di masa mendatang.



Untuk menghapus anggota, dari antarmuka grup utama, ketuk ikon grup di bagian atas untuk mengakses antarmuka informasi grup.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Kemudian klik pada nama anggota dan **Hapus dari grup**. Dari antarmuka ini, Anda juga dapat mengiriminya pesan, mengikutinya, atau menambahkannya ke grup lain.



![screen](assets/fr/46.webp)



### Mengirim file multimedia



Untuk saat ini, hanya foto yang dapat dibagikan di antara pengguna pada White Noise. Baik dalam percakapan pribadi maupun obrolan grup, untuk melakukannya, Anda harus :





- tekan simbol **plus (+)** di sisi kiri kolom input pesan teks.



![screen](assets/fr/47.webp)





- lalu klik pada kotak bertanda **Foto** di bagian bawah untuk mengakses galeri Anda.



![screen](assets/fr/48.webp)





- pilih foto yang akan dikirim.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Poin-poin penting yang perlu diingat



White Noise menawarkan tingkat kerahasiaan yang baik dan keamanan yang unggul. Di sisi lain, ini adalah aplikasi yang sangat baru, tidak terlalu luas dan masih dalam tahap awal. Oleh karena itu, masih terlalu dini untuk menarik kesimpulan aktif apa pun. Ada kemungkinan terjadi beberapa kegagalan fungsi selama penggunaan.



Saat ini, aplikasi ini tidak memiliki fungsi tertentu (tidak ada panggilan audio atau video, tidak ada pengiriman file multimedia audio atau video) dibandingkan dengan aplikasi perpesanan populer.



Namun demikian, White Noise tetap menjadi pilihan yang menarik untuk percakapan di mana kerahasiaan adalah yang terpenting (misalnya dengan keluarga, teman dekat atau aktivis dalam tujuan yang sama), meskipun memerlukan sedikit usaha untuk menginstal (melalui toko aplikasi alternatif atau file APK) dan belajar (menguasai sedikit konsep pasangan kunci, klien dan relay dengan protokol Nostr).



Sekarang Anda sudah tahu cara menggunakan White Noise untuk berkomunikasi secara aman dengan teman dan keluarga Anda. Berikan jempol jika Anda merasa tutorial ini bermanfaat.



Kami merekomendasikan tutorial kami tentang Tox Chat, sebuah aplikasi yang memungkinkan Anda mengobrol tanpa perantara melalui protokol Tox yang terdesentralisasi.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3