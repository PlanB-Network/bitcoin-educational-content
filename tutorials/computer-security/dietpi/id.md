---
name: DietPi
description: Sistem operasi ringan yang dioptimalkan untuk mesin yang berkinerja buruk. Dengan preferensi untuk hosting mandiri
---

![cover](assets/cover.webp)



Di kalangan non-teknis, merek-merek seperti `Odroid`, `Raspberry Pi`, `Orange Pi` atau `Radxa`, tidak terlalu dikenal. Namun, kita hanya perlu melihat ke dalam lingkaran teknologi, untuk menemukan bahwa komputer **SBC** - yang dibangun di atas satu motherboard, sering kali berukuran mikroskopis dibandingkan dengan komputer yang biasa digunakan - menjadi sangat diperlukan, sebagai dukungan untuk proyek pribadi apa pun.



Ini adalah komputer yang diproduksi dalam berbagai macam model. Komputer ini lebih disukai menjadi tuan rumah distribusi Linux, yang sering kali diadaptasi agar dapat berjalan dengan lancar pada mesin-mesin yang kurang bertenaga.



*tidak terkecuali *DietPi**: ini adalah sistem operasi berbasis Debian, yang dioptimalkan untuk menjadi seringan mungkin dan membuat SBC dengan kinerja paling rendah sekalipun menjadi sangat cepat. Beralih dari Debian12 Bookworm ke Debian13 Trixie tepat saat tutorial ini ditulis, sekarang juga mendukung SBC berbasis prosesor `RISC-V` open source. DietPi adalah penemuan yang menyenangkan yang layak untuk dipelajari lebih lanjut.



## Kekuatan



Ini bukan "duplikat biasa" dari Debian untuk papan tipe Raspberry yang kecil. DietPi adalah:




- Dioptimalkan untuk kecepatan dan ringan**: sebuah [perbandingan dengan distribusi Debian lainnya untuk SBC](https://dietpi.com/blog/?p=888), DietPi lebih ringan dalam segala hal. Image ISO DietPi memiliki berat kurang dari 1 GB, sejauh ini merupakan yang terkecil di antara image ISO yang didedikasikan untuk model Raspberry atau Orange PI yang lebih lama (misalnya). Permintaan untuk sumber daya RAM dan CPU sangat rendah, sehingga selalu mendapatkan yang terbaik dari papan, bahkan yang lebih tua.
- Otomatisasi dan penginstalasi bawaan**: Serangkaian perintah khusus membantu pengguna memantau sumber daya sistem serta mengotomatiskan tugas-tugas untuk menginstal dan meluncurkan program, memperbarui versi, membuat cadangan, dan memeriksa semua log.
- Komunitas yang kuat dan berorientasi pada eksperimen**: [tutorial](https://dietpi.com/forum/c/community-tutorials/8) dan proyek-proyek dari komunitas DietPi, sangat ideal untuk mendapatkan inspirasi dari perangkat lunak yang dapat Anda instal dengan satu klik, terima kasih kepada DietPi.



**Memeras setiap bagian dari SBC Anda tidak pernah semudah ini**.



## Otomatisasi untuk hosting mandiri


Ingin bereksperimen dengan server Anda sendiri untuk menjalankan solusi jaringan tingkat lanjut, atau alat untuk mengembangkan keahlian Bitcoin Anda? DietPi mungkin merupakan solusi yang Anda cari. Meskipun banyak orang yang tahu cara mengelola infrastruktur mereka sendiri dan menjalankan server yang terkonfigurasi dan terlindungi dengan sempurna, DietPi merupakan langkah yang cocok bagi mereka yang ingin memulai dari awal.



Alih-alih melakukan semua tugas rumit yang dibutuhkan secara manual, DietPi memungkinkan Anda untuk membuatnya dengan `wizard` dan baris perintahnya sendiri. Di sini Anda bisa bereksperimen dengan cloud pribadi Anda sendiri, manajemen perangkat _smart home_, pencadangan otomatis dan crontab, serta solusi yang lebih canggih.



![img](assets/en/01.webp)



## Instalasi



### Unduh



DietPi menawarkan banyak sekali image ISO, untuk membakar sistem operasi ke berbagai perangkat. Beberapa hanya didukung: ISO untuk Raspberry PI5 masih dalam pengujian, misalnya, tetapi Anda pasti bisa menemukan yang cocok untuk papan Anda.



Untuk panduan ini, saya memilih untuk menginstalnya pada thin client, jadi pilihannya adalah _PC/VM_ dan kemudian _Native PC_. Ada dua citra ISO untuk perangkat ini, yang berbeda dalam hal generasi bootloader. Mesin yang digunakan dalam tutorial ini sudah cukup tua, jadi pilihannya jatuh pada versi _BIOS/CSM_. Jika Anda memiliki mesin yang lebih baru, versi yang benar mungkin adalah `UEFI`.



![img](assets/en/02.webp)



Anda akan masuk ke halaman yang berisi `gambar pemasang`, `sha256` dan `Tanda Tangan`.



![img](assets/en/03.webp)



Siapkan direktori di `home` komputer Anda sehari-hari, sehingga Anda dapat mengunduh file yang diperlukan, dengan `wget`.



![img](assets/en/04.webp)



Kunci publik pengembang memerlukan penelitian minimum, tetapi Anda dapat menemukannya di tautan ini: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Periksa isi direktori dengan `ls -la` dan impor kunci MichaIng ke dalam keyring Anda, dengan `gpg --import`.



### Verifikasi dan flash



Terakhir, bagian yang paling saya rekomendasikan: pastikan keaslian sistem operasi yang telah Anda unduh dan akan Anda instal pada SBC Anda.



![img](assets/en/06.webp)



Jika Anda juga mendapatkan hasil `Tanda tangan yang bagus` dan kontrol Hash yang sama dengan perintah sha256sum, Anda dapat melanjutkan untuk mem-flash ISO ke stik USB. Gunakan aplikasi seperti Whale Etcher untuk melakukan ini.



![img](assets/en/07.webp)



## Instalasi DietPi



![img](assets/en/09.webp)



Pindahkan flash drive ke perangkat yang akan menjadi host DietPi dan mulai instalasi sistem operasi Lime Green. Dalam latihan ini, kami menggunakan thin client dengan RAM 16 GB, SSD 128 GB untuk sistem operasi, dan disk data kedua 1 TB. Instalasi membutuhkan waktu kurang dari 30 menit, tetapi jika Anda akan menggunakan Raspberry, misalnya, sumber dayanya mungkin lebih sedikit dan membutuhkan waktu lebih lama. Anda akan diperlihatkan kemajuan selama instalasi.



![img](assets/en/08.webp)



Dirancang untuk Raspberry dan sejenisnya, sifat asli dari DietPi adalah apa yang disebut sebagai instalasi `tanpa kepala`, tanpa lingkungan grafis dan dengan akses `shsh` asli. Dalam panduan ini, Anda akan melihat lingkungan grafis, tepatnya LXDE.



Pada langkah ini, Anda juga akan diminta untuk menentukan peramban web mana yang ingin Anda gunakan secara default, antara Chromium dan Firefox. Keduanya bekerja dengan baik; tidak ada kontraindikasi khusus untuk keduanya, selain preferensi pribadi Anda.



Menjelang akhir, penginstal mungkin akan menanyakan apakah Anda ingin menginstal program apa pun, tetapi di sini **Saya menyarankan Anda untuk tidak melakukan pra-pemuatan apa pun**. Anda harus tahu bahwa setelah langkah ini, Anda akan diminta untuk mengubah kata sandi default dari dua pengguna, untuk alasan keamanan. Yang paling penting, Anda akan diminta untuk mengatur `Global Software Password (GSP), yang akan memastikan akses ke berbagai perangkat lunak secara terkendali. **Jika Anda mengunduh perangkat lunak apa pun selama instalasi OS, tanpa pengaturan `GSP`, perangkat lunak tersebut tidak akan dapat diakses**. Anda harus meng-uninstall dan meng-install ulang setelah mengatur `Global Software Password`: oleh karena itu, **jangan memasukkan apa pun untuk menghindari pekerjaan ganda**. (Ketidaknyamanan ini mungkin saja terjadi, tidak 100% pasti).



Instalasi diakhiri dengan permintaan untuk mengaktifkan DietPi-Survey, layanan pengumpulan data otomatis yang digunakan untuk mendukung pengembangan sistem operasi. Menurut situs webnya, pengumpulan data diaktifkan ketika Anda mengunduh perangkat lunak apa pun dari otomatisasi yang disediakan oleh DietPi, atau ketika Anda meng-upgrade ke rilis berikutnya. Setiap orang memiliki pilihan untuk ikut serta (_Opt IN_) atau tidak ikut serta (_Opt OUT_).



![img](assets/en/23.webp)



Setelah menyelesaikan instalasi dan reboot berikutnya, DietPi akan muncul di layar saat Anda mengaturnya. Untuk tutorial ini, seperti yang telah disebutkan, saya memilih lingkungan grafis `LXDE`. Pada desktop saya menemukan pintasan untuk memulai `htop` dan terminal terbuka.



![img](assets/en/10.webp)



### "Alat" dari sistem operasi



Lupakan sebagian besar program yang Anda gunakan pada distribusi Linux Anda-DietPi sangat optimal, Anda telah meninggalkan beberapa di antaranya. Pada dasarnya Anda harus menginstal banyak perintah secara manual, tetapi jika Anda hanya mencobanya, tahan godaan dan cobalah untuk menguji otomatisasi DietPi.



Ini jelas merupakan terminal yang merupakan alat pertama yang berguna untuk memulai dengan sistem operasi baru Anda, dan terbuka secara otomatis setiap kali Anda menyalakannya.



![img](assets/en/11.webp)



Pada layar terminal, Anda akan menemukan daftar serangkaian perintah yang diawali dengan `dietpi-` yang mewakili [tools](https://dietpi.com/docs/dietpi_tools/) dari sistem operasi ini:




- `dietpi-launcher`: untuk mengakses sistem operasi, pengelola file, dll
- `dietpi-Software`: yang merupakan alat yang dapat digunakan untuk menginstal semua perangkat lunak yang sudah tersedia di dalam paket
- `dietpi-config`: untuk mengakses konfigurasi sistem, bahkan yang paling canggih sekalipun.



![img](assets/en/14.webp)



### Cadangan



Mencadangkan server adalah rutinitas yang harus diantisipasi oleh administrator sistem sejak pertama kali dinyalakan.



Dengan DietPi ada perintah `dietpi-Backup`, yang saya sarankan Anda jelajahi untuk menemukan solusi yang ideal: ini memungkinkan Anda untuk mengatur cadangan reguler, tambahan atau tidak tergantung pada aplikasi yang digunakan, dan semua opsi untuk menyesuaikan rutinitas.



![img](assets/en/22.webp)



Pilih tujuan pencadangan, misalnya disk lain, dengan memulai `dietpi-Drive_Manager` untuk menyambungkan drive tujuan dan menggunakannya untuk fungsi ini.



## Konfigurasi



Menginangi sendiri adalah pengalaman yang disarankan untuk semua orang, baik yang ingin tahu maupun yang antusias. Namun, menarik dan mengonfigurasi sebuah server melibatkan beberapa tantangan teknologi yang tidak sedikit. Di sinilah **kemudahan DietPi** hadir, memungkinkan Anda untuk mengonfigurasi sistem yang disesuaikan dengan kebutuhan Anda dalam beberapa langkah sederhana.



![img](assets/en/24.webp)



Pengaturan dasar dan lanjutan, semua ada di ujung jari Anda dalam satu Interface yang tersedia dengan perintah:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


perangkat lunak sudo dietpi-perangkat lunak


```