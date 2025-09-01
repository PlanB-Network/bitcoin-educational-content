---
name: Browser Mullvad
description: Cara menggunakan Peramban Mullvad untuk privasi
---

![cover](assets/cover.webp)



Di dunia di mana pengawasan digital menjadi sangat umum, melindungi privasi online Anda tidak pernah menjadi lebih penting. Perusahaan-perusahaan menggunakan teknik-teknik canggih untuk melacak Anda:





- Cookie pihak ketiga**: file kecil yang disimpan oleh situs eksternal untuk mengikuti Anda dari satu situs ke situs lainnya
- Sidik jari**: mengumpulkan karakteristik unik dari browser dan perangkat Anda (resolusi layar, font yang diinstal, plugin, dll.) untuk mengidentifikasi Anda tanpa cookie
- Skrip pelacakan**: kode JavaScript tak terlihat yang menganalisis perilaku penjelajahan Anda (klik, gulir, waktu yang dihabiskan)
- Analisis IP Address**: lokasi geografis dan identifikasi penyedia layanan Internet Anda



Data ini kemudian digabungkan untuk membuat profil terperinci tentang perilaku online Anda dan menghasilkan uang, seringkali tanpa sepengetahuan Anda. Kenyataan ini menimbulkan pertanyaan mendasar: bagaimana Anda dapat menjelajahi Internet sambil menjaga anonimitas dan kerahasiaan Anda?



Jawabannya sebagian besar terletak pada pilihan peramban web Anda. Alat yang kita gunakan setiap hari untuk mengakses informasi, melakukan pembelian, atau berkomunikasi ini memainkan peran penting dalam melindungi data pribadi kita. Sayangnya, peramban populer seperti Google Chrome (yang menguasai sekitar 65% pasar global) dirancang dengan model bisnis yang didasarkan pada pengumpulan data pengguna secara besar-besaran.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser menonjol karena pemblokiran pelacaknya yang sangat efektif, jauh melampaui peramban konsumen*



Menghadapi tantangan ini, para pemain baru bermunculan dengan filosofi yang berbeda: yaitu menempatkan privasi sebagai inti dari desain mereka. Di antara mereka, Mullvad Browser menonjol sebagai solusi inovatif yang menggabungkan perlindungan privasi terbaik dengan pengalaman penjelajahan yang lancar dan mudah diakses.



Tidak seperti peramban tradisional yang berusaha mempersonalisasi pengalaman Anda dengan mengumpulkan data Anda, Mullvad Browser mengambil pendekatan yang berlawanan: membuat semua penggunanya tampak identik dengan situs web, sehingga membuat pelacakan individual hampir tidak mungkin dilakukan.



Dalam tutorial ini, kita akan bersama-sama mengetahui bagaimana Mullvad Browser dapat mengubah cara Anda menjelajahi Internet, menawarkan perlindungan yang kuat terhadap pengawasan tanpa mengorbankan kemudahan penggunaan.




## Memperkenalkan Browser Mullvad



**Mullvad Browser** adalah peramban web yang berfokus pada privasi yang dikembangkan bekerja sama dengan Tor Project dan didistribusikan secara gratis oleh perusahaan Swedia, Mullvad VPN. Diluncurkan pada bulan April 2023, ia menampilkan dirinya sebagai **"Peramban Tor tanpa jaringan Tor "**, yang dirancang untuk meminimalkan pelacakan online dan sidik jari sambil memungkinkan pengguna untuk menjelajah melalui VPN tepercaya dan bukan jaringan Tor.



Mullvad Browser adalah peramban sumber terbuka gratis yang berbasiskan pada Firefox ESR (versi Mozilla Firefox yang tahan lama) dan dikembangkan oleh para ahli Tor Project. Secara konkret, peramban ini memiliki sebagian besar fitur perlindungan dari Tor Browser, tetapi **tidak merutekan lalu lintas melalui jaringan Tor**. Sebagai gantinya, pengguna dapat (dan harus) menautkannya ke VPN terenkripsi tepercaya untuk menganonimkan IP Address mereka.



Dalam hal pengalaman pengguna, Mullvad Browser menyerupai peramban klasik, menawarkan navigasi yang lancar. Ini tersedia gratis untuk Windows, macOS dan Linux (tidak ada versi seluler). Anda tidak perlu menjadi pelanggan VPN Mullvad untuk menggunakannya; namun, **menggunakan Mullvad Browser tanpa menyembunyikan IP Anda tidak memberikan anonimitas sepenuhnya** - jadi sangat disarankan untuk menggunakannya bersama dengan VPN yang andal.



### Tujuan: privasi dan anti-pelacakan



Peramban Mullvad telah dirancang dengan satu tujuan utama: **melindungi privasi pengguna** secara online dan melawan teknik pelacakan dan pembuatan profil yang umum. Tujuan utamanya meliputi:





- Secara drastis mengurangi pelacakan dan pelacakan iklan** oleh situs web dan biro iklan. Secara default, Mullvad Browser memblokir pelacak pihak ketiga, cookie pelacak, dan skrip sidik jari yang dapat mengidentifikasi Anda.





- Standarisasi sidik jari peramban Anda** untuk **"berbaur dengan kerumunan". Sidik jari seperti "kartu identitas" unik yang dibuat dengan menggabungkan semua karakteristik peramban Anda. Mullvad Browser memastikan bahwa semua penggunanya memiliki "kartu identitas" yang sama persis, sehingga tidak mungkin untuk membedakan mereka secara individual.





- Menawarkan perlindungan langsung tanpa ekstensi tambahan**. Mullvad Browser hadir dalam konfigurasi "siap pakai": pengguna tidak perlu memasang berbagai ekstensi atau mengubah pengaturan apa pun untuk dilindungi.





- Jangan mengorbankan kinerja atau ergonomi** lebih dari yang diperlukan. Dengan tidak adanya perutean Tor, Mullvad Browser menawarkan penjelajahan yang jauh lebih cepat daripada Tor Browser, mendekati kinerja peramban standar yang digabungkan dengan VPN.



### Fitur-fitur utama Browser Mullvad



Mullvad Browser memiliki serangkaian fitur keamanan dan privasi yang terinspirasi langsung oleh Tor Browser:





- Penjelajahan pribadi setiap saat:** Mode penjelajahan pribadi diaktifkan secara default dan tidak dapat dinonaktifkan. **Tidak ada riwayat, cookie, atau cache yang disimpan dari satu sesi ke sesi berikutnya**. Segera setelah Anda menutup Peramban Mullvad, semua data penjelajahan akan dihapus.





- Perlindungan yang ditingkatkan terhadap sidik jari:** Browser menerapkan pengaturan yang ketat untuk menggagalkan sidik jari digital. Ini termasuk:
 - Agen pengguna** dan standarisasi versi browser
 - Zona waktu diatur ke UTC** untuk semua pengguna
 - Letterboxing**: teknik yang secara otomatis menambahkan margin abu-abu di sekitar halaman web untuk menstandarkan ukuran tampilan dan mencegah identifikasi berdasarkan dimensi layar Anda
 - Memblokir API sidik jari**: Teknologi Canvas (gambar 2D), WebGL (grafik 3D), dan AudioContext (pemrosesan audio) dinonaktifkan karena teknologi tersebut dapat mengungkapkan detail unik tentang perangkat keras Anda
 - Font sistem standar** untuk menghindari identifikasi oleh font yang diinstal





- Memblokir pelacak dan iklan:** Mullvad Browser secara asli mengintegrasikan ekstensi **uBlock Origin** (sudah diinstal sebelumnya) dengan daftar perlindungan tambahan untuk memblokir **pelacak pihak ketiga, skrip iklan, dan konten berbahaya lainnya**. Perlindungan ini disertai dengan **Isolasi Pihak Pertama**: teknik yang menyimpan cookie dalam "pot" terpisah untuk setiap situs web, mencegah satu situs membaca cookie yang disimpan oleh situs lain.





- Tombol pengaturan ulang sesi:** Seperti tombol "Identitas Baru" pada Tor Browser, Mullvad Browser menawarkan tombol untuk **menghidupkan ulang peramban dengan cepat dengan sesi baru yang kosong**.





- Tingkat keamanan yang dapat disesuaikan:** Anda dapat menyesuaikan tingkat keamanan (*Normal*, *Lebih Aman*, *Terbaik*) dalam pengaturan, seperti halnya pada Tor Browser.



## Ekstensi bawaan secara default



Mullvad Browser menyertakan **tiga ekstensi pra-instal** yang merupakan inti dari perlindungan anti-pelacakannya. **Sangat penting untuk tidak menghapus atau mengubah konfigurasinya, karena ini akan membuat Anda unik di antara para pengguna Mullvad Browser:



### *asal *uBlock**


Ekstensi pemblokir iklan dan pelacak ini telah dikonfigurasikan sebelumnya dengan **daftar filter yang dioptimalkan** untuk memblokir:




- Iklan yang mengganggu
- Pelacak pihak ketiga yang mengumpulkan data Anda
- Skrip berbahaya
- Pelacakan perilaku Elements



uBlock Origin di Mullvad Browser menggunakan parameter standar untuk memastikan bahwa semua pengguna memblokir Elements yang sama persis, sehingga menjaga keseragaman jejak digital.



### **Tanpa Naskah**


NoScript berjalan di latar belakang untuk mengelola **tingkat keamanan** peramban. Ini:




- Mengontrol eksekusi JavaScript** sesuai dengan tingkat yang dipilih (Normal/Paling Aman/Paling Aman)
- Menyaring serangan XSS** (Cross-Site Scripting) secara otomatis
- Memblokir konten aktif yang berbahaya** di situs non-HTTPS
- Ikonnya disembunyikan secara default, tetapi dapat ditampilkan melalui "Sesuaikan bilah alat"



### *ekstensi *Mullvad Browser**


Ekstensi khusus Mullvad ini menawarkan fungsi yang berbeda tergantung pada apakah Anda pelanggan VPN Mullvad atau bukan:



#### **Tanpa berlangganan Mullvad VPN:**




- Pemeriksaan koneksi dasar**: menampilkan IP publik Anda saat ini dan beberapa informasi koneksi
- Rekomendasi privasi**: kiat untuk meningkatkan pengaturan keamanan Anda (DNS, hanya HTTPS, mesin pencari)
- Kontrol WebRTC**: aktifkan/nonaktifkan untuk mencegah kebocoran IP Address
- Dapat dihapus tanpa dampak** pada jejak digital Anda jika Anda tidak menggunakan Mullvad VPN



#### **Dengan berlangganan Mullvad VPN:**


Ekstensi ini mengungkapkan potensi penuhnya dengan fitur-fitur canggih:





- Proksi SOCKS5 terintegrasi **: koneksi satu klik ke proksi server VPN Mullvad
 - IP tetap Address**: tidak seperti VPN, yang dapat mengubah IP Address-nya, proxy selalu menjamin output Address yang sama
 - Tombol pemutus otomatis**: jika VPN terputus, lalu lintas peramban segera diblokir
 - Dukungan IPv6**: Konektivitas IPv6 bahkan jika koneksi VPN Anda tidak mengaktifkannya





- Multihop (VPN ganda)**: kemampuan untuk mengubah lokasi proksi untuk membuat terowongan di dalam terowongan
 - Lalu lintas Anda pertama-tama melewati server VPN Anda, lalu "melompat" ke server Mullvad lainnya
 - Gunakan pelokalan yang berbeda hanya untuk browser





- Pemantauan koneksi tingkat lanjut**: pemantauan status VPN Anda secara real-time, server yang tersambung, dan deteksi kebocoran DNS





- Akses ke Mullvad Leta**: mesin pencari pribadi yang diperuntukkan bagi pelanggan (meskipun tidak direkomendasikan oleh Mullvad karena alasan korelasi dengan akun Anda)



Ketiga ekstensi ini bekerja sama untuk menciptakan ekosistem perlindungan yang koheren, di mana setiap pengguna mendapatkan manfaat dari pertahanan yang sama persis tanpa kemungkinan penyesuaian yang akan membahayakan anonimitas kolektif.



## Keuntungan dan kerugian dari Peramban Mullvad



### Manfaat





- Perlindungan privasi yang sangat baik secara default:** Mullvad Browser menerapkan pengaturan privasi yang sangat ketat sejak awal, tanpa perlu konfigurasi manual.





- Performa yang lebih baik daripada Tor Browser:** Dengan tidak adanya perutean bawang, Mullvad Browser **terlihat lebih cepat dan lebih responsif** daripada Tor Browser untuk penjelajahan web klasik.





- Kesederhanaan Interface yang sudah dikenal:** Peramban Mullvad didasarkan pada Interface Firefox. Jika Anda terbiasa dengan Firefox atau bahkan Tor Browser, Anda tidak akan merasa asing.





- Kolaborasi tepercaya dan kode yang diaudit:** Peramban Mullvad mendapat manfaat dari keahlian Proyek Tor, dan semua kode sumber tersedia untuk audit eksternal.



### Kekurangan





- Tidak ada anonimitas jaringan tanpa VPN:** Poin yang paling penting adalah bahwa **Peramban Mullvad tidak menyembunyikan IP Address Anda dengan sendirinya** (seperti semua peramban lain, kecuali Tor Browser). IP Address Anda seperti "Address pos" Anda di Internet: IP Address mengungkapkan lokasi dan ISP Anda. Oleh karena itu, ia **sangat bergantung pada VPN** (jaringan pribadi virtual) untuk menyembunyikan informasi penting ini.





- Tidak ada versi seluler:** Hingga saat ini, Mullvad Browser hanya tersedia di PC (Windows, Mac, Linux).





- Tidak sesuai dengan kebiasaan tertentu:** Mode privat permanen berarti Anda tidak dapat mempertahankan sesi dari satu penggunaan ke penggunaan berikutnya. Tidak mungkin untuk tetap terhubung ke akun web dari satu sesi ke sesi berikutnya.





- Fitur yang dibatasi:** Untuk menjaga keseragaman sidik jari, Mullvad Browser telah **menonaktifkan beberapa fitur** yang ada di Firefox dan tidak dimaksudkan untuk penyesuaian.



## Menginstal Peramban Mullvad



Mullvad Browser tersedia secara gratis untuk Windows, macOS dan Linux. Untuk menginstalnya, kunjungi [situs web resmi Mullvad](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Halaman beranda Browser Mullvad resmi dengan tombol unduh yang disorot.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Pilih sistem operasi Anda pada halaman unduhan Mullvad Browser.*



Klik tombol **"Unduh "** yang sesuai dengan sistem operasi Anda.



Untuk Linux, Anda dapat memilih di antara format yang berbeda tergantung pada distribusi Anda. Setelah pengunduhan selesai:



### Pada Windows


Jalankan file `.exe` yang telah diunduh dan ikuti petunjuk instalasi.



### Di macOS


Buka file `.dmg` yang telah diunduh dan seret aplikasi Mullvad Browser ke dalam folder Aplikasi Anda.



### Di Linux


Ekstrak arsip `.tar.xz` ke dalam direktori pilihan Anda dan jalankan file `start-mullvad-browser.desktop`.



## Konfigurasi dan penggunaan pertama



Saat pertama kali meluncurkan Mullvad Browser, Anda akan melihat Interface yang sangat mirip dengan Tor Browser. Peramban ini telah dikonfigurasi sebelumnya untuk privasi dan tidak memerlukan modifikasi khusus.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Halaman beranda Mullvad Browser dengan ekstensi, ikon sapu hingga generate identitas baru dan menu aplikasi di kanan atas*



**Penting:** Peramban Mullvad tidak menyamarkan IP Address Anda secara default. Untuk perlindungan penuh, kami sangat menyarankan untuk menggunakan VPN secara paralel. Anda dapat menggunakan Mullvad VPN atau layanan VPN tepercaya lainnya.



Browser ini juga menyertakan **DNS-over-HTTPS (DoH)** menggunakan layanan DNS Mullvad: teknologi ini mengenkripsi permintaan DNS Anda (menerjemahkan nama situs menjadi alamat IP) untuk mencegah ISP Anda memantau situs-situs yang Anda kunjungi.



### Pengaturan keamanan



Anda dapat menyesuaikan tingkat keamanan dengan mengeklik **menu aplikasi** (tiga bilah horizontal) di kanan atas, kemudian **"Pengaturan "**, lalu tab **"Privasi & Keamanan "**. Gulir ke bawah ke bagian **"Keamanan "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Pilihan tingkat keamanan: tanda panah menunjukkan jalur dari menu aplikasi ke tab "Privasi & Keamanan" ke opsi keamanan*



Mullvad Browser menawarkan tiga tingkat keamanan:





- Normal** (tingkat default saat ini): Semua fungsi browser dan situs web diaktifkan





- Lebih aman**: Menonaktifkan fungsi situs web yang sering kali berbahaya, yang dapat menyebabkan hilangnya fungsionalitas pada beberapa situs web:
 - JavaScript dinonaktifkan untuk situs non-HTTPS
 - Beberapa jenis huruf dan simbol matematika dinonaktifkan
 - Suara dan video (media HTML5) serta WebGL adalah "klik untuk memutar"





- Paling aman**: Hanya mengizinkan fungsi situs web yang diperlukan untuk situs statis dan layanan dasar:
 - JavaScript dinonaktifkan secara default untuk semua situs
 - Beberapa font, ikon, gambar, dan simbol matematika dinonaktifkan
 - Suara dan video (media HTML5) serta WebGL adalah "klik untuk memutar"



### Tombol sesi baru



Untuk memulai ulang dengan sesi kosong tanpa menutup browser, klik ikon sapu atau gunakan menu aplikasi > **"Sesi baru "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Atur ulang identitas Anda" berfungsi untuk memulai ulang browser dengan sesi yang benar-benar baru*



## Penggunaan sehari-hari



### Navigasi normal



Peramban Mullvad berperilaku seperti peramban klasik untuk penjelajahan sehari-hari. Semua situs web dapat diakses seperti biasa, dengan manfaat tambahan berupa perlindungan yang ditingkatkan terhadap pelacakan.



### Manajemen cookie dan login



Karena mode privat permanen, Anda harus menyambungkan kembali ke akun Anda setiap kali Anda masuk. Ini adalah harga yang harus Anda bayar untuk kerahasiaan maksimum.



### Ekstensi



Peramban Mullvad secara teknis memungkinkan anda untuk memasang ekstensi tambahan dari katalog Firefox, tetapi **penting untuk memahami implikasinya**. Setiap ekstensi yang ditambahkan akan mengubah jejak digital Anda dan membedakan Anda dari pengguna Peramban Mullvad lainnya, yang bertentangan dengan prinsip dasar peramban ini: membuat semua pengguna tampak identik.



Seperti yang dijelaskan Mullvad: *"Terkadang, tidak memiliki pertahanan khusus lebih baik daripada memilikinya. Dengan ingin meningkatkan privasi online, Anda memasang ekstensi yang pada akhirnya membuat Anda semakin terlihat. "*



Jika Anda tetap memilih untuk memasang ekstensi, ketahuilah bahwa Anda membuat sidik jari unik yang bisa digunakan untuk melacak Anda dari satu situs ke situs lainnya. Untuk perlindungan maksimal, sebaiknya tetap menggunakan tiga ekstensi yang sudah diinstal sebelumnya, yang identik untuk semua pengguna.



## Praktik terbaik dengan Browser Mullvad



1. **Selalu gunakan VPN: Peramban Mullvad tidak menyamarkan IP Anda. VPN sangat penting untuk anonimitas sepenuhnya.



2. **Jangan menyesuaikan peramban**: Hindari mengubah pengaturan atau menambahkan ekstensi, karena hal ini dapat membuat Anda mudah dikenali.



3. **Gunakan tombol sesi baru**: Di antara aktivitas yang berbeda, gunakan fungsi reset untuk mempartisi sesi Anda.



4. **Pilih tingkat keamanan yang paling sesuai dengan kebutuhan Anda**:




   - Normal (disarankan)**: Untuk penjelajahan sehari-hari. Sudah menawarkan perlindungan yang sangat baik sekaligus menjaga situs web tetap berfungsi. Ini adalah keseimbangan terbaik untuk 95% pengguna.
   - Lebih aman**: Jika Anda mengunjungi situs yang tidak dikenal atau berpotensi berbahaya, atau untuk perlindungan ekstra pada jaringan Wi-Fi publik. Beberapa situs mungkin tidak berfungsi.
   - Paling aman**: Diperuntukkan bagi situasi berisiko tinggi (jurnalisme investigasi, komunikasi sensitif, lingkungan yang tidak bersahabat). Sebagian besar situs modern akan dibobol, tetapi itulah harga dari keamanan maksimum.



5. **Periksa pembaruan secara teratur**: Selalu perbarui peramban Anda dengan patch keamanan terbaru.



6. **Gunakan mesin pencari yang ramah privasi**: Pilih DuckDuckGo, Startpage, atau Searx daripada Google.



7. **Aktifkan mode hanya HTTPS**: Dalam pengaturan, pastikan bahwa mode "Hanya HTTPS" diaktifkan untuk memaksa koneksi yang aman.



8. **JANGAN ubah pengaturan lanjutan apa pun**: Tidak seperti peramban lain, Peramban Mullvad dirancang agar SEMUA pengguna memiliki konfigurasi yang sama persis. Memodifikasi pengaturan di `about:config` atau mengubah pengaturan uBlock Origin/NoScript akan membuat Anda unik dan sepenuhnya membatalkan anonimitas browser.



## Konfigurasi DNS yang disarankan



Peramban Mullvad secara otomatis mengintegrasikan Mullvad DNS-over-HTTPS. Jika Anda menggunakan Mullvad VPN, ekstensi ini akan merekomendasikan Anda untuk **menonaktifkan Mullvad DoH** karena akan lebih cepat jika menggunakan server DNS server VPN Anda. Jika Anda tidak menggunakan Mullvad VPN, tetap aktifkan Mullvad DoH untuk menghindari pemantauan DNS oleh ISP Anda.



## Kesimpulan



Mullvad Browser merupakan solusi luar biasa bagi mereka yang mencari penjelajahan web yang ramah privasi tanpa kendala kinerja jaringan Tor. Dikombinasikan dengan VPN berkualitas, Mullvad Browser menawarkan proteksi yang tangguh terhadap pelacakan dan pengawasan online.



Meskipun memiliki keterbatasan tertentu (tidak ada versi seluler, sesi non-persisten), Mullvad Browser merupakan alat yang berharga bagi siapa pun yang ingin mendapatkan kembali kendali atas privasi digital mereka. Kemudahan penggunaan dan konfigurasi standarnya menjadikannya pilihan bijak bagi pengguna yang sadar akan privasi, baik pemula maupun yang sudah berpengalaman.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Peramban Mullvad](https://mullvad.net/fr/browser)
- [Halaman unduhan Peramban Mullvad](https://mullvad.net/en/download/browser)
- [Spesifikasi teknis terperinci](https://mullvad.net/en/browser/Hard-facts)
- [Ekstensi Peramban Mullvad](https://mullvad.net/en/help/mullvad-browser-extension)



### Panduan dan penjelasan




- [Mengapa privasi itu penting](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor tanpa Tor: Konsep Peramban Mullvad](https://mullvad.net/en/browser/tor-without-tor)
- [Cara memilih peramban yang ramah privasi](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Memahami sidik jari peramban](https://mullvad.net/en/browser/browser-fingerprinting)



### Dukungan dan bantuan




- [Pusat Bantuan Browser Mullvad](https://mullvad.net/en/help/tag/mullvad-browser)
- [Langkah pertama menuju privasi online](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Sumber daya masyarakat




- [Panduan Peramban Mullvad - Panduan Privasi](https://www.privacyguides.org/en/desktop-browsers/)
- [Diskusi komunitas](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)