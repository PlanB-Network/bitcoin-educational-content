---
name: Raspberry Pi Zero
description: Cara membangun komputer minimalis, terisolasi, dan berbiaya rendah menggunakan Raspberry Pi Zero dan paket aksesori.
---
![cover](assets/cover.webp)



Jika Anda telah berada di halaman Plan ₿ Network untuk sementara waktu, Anda telah mengetahui bahwa salah satu pengaturan keamanan yang paling dianjurkan, hampir menjadi keharusan, **adalah pengelolaan dana dengan penyimpanan offline kunci pribadi Anda**.



Jika Anda belum menemukannya, di sepanjang tutorial ini Anda akan menemukan tautan ke sumber-sumber sumber daya open source yang dapat Anda gunakan untuk mempelajari lebih lanjut.



Untuk mengelola kunci privat secara offline, diperlukan perangkat yang secara permanen terputus dari jaringan, baik itu [dompet perangkat keras](https://planb.network/resources/glossary/hardware-wallet) atau komputer airgap, yang didedikasikan untuk fungsi khusus ini.



Bagaimana Anda melakukannya jika, misalnya, Anda tidak memiliki kemampuan untuk membeli perangkat keras yang hanya melakukan tugas ini, tetapi Anda tidak ingin melepaskan langkah keamanan ini?



## Solusi


Bagaimana jika saya beritahukan kepada Anda bahwa Anda dapat membuat perangkat offline dalam bentuk komputer airgap yang ukuran dan beratnya sebesar USB flash drive dan harganya 35 euro? Apakah Anda tidak akan mempercayainya?



Lanjutkan membaca.



Saya akan memberi tahu Anda lebih banyak: baca sampai selesai. Solusi yang diusulkan memang murah, tetapi bukan solusi yang paling mudah. Pertama, Anda mendapatkan gambaran umum, kemudian Anda memutuskan untuk menginvestasikan sebagian waktu Anda dalam beberapa penelitian pribadi dan memilih, dengan ketenangan pikiran sebanyak mungkin, apakah dan bagaimana cara melanjutkannya.



## Persyaratan


**1** Sebuah [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (tanpa embel-embel tambahan) adalah dasar untuk membuat komputer dengan kinerja minimal, tetapi yang terpenting tidak memiliki kartu Wi-Fi dan Bluetooth, yang merupakan persyaratan penting untuk tujuan latihan ini.





- Biaya**: sekitar 15.00 pada saat tutorial ini ditulis (Agustus 2025).
- Kontinuitas produksi**: Raspberry menjamin produksi hingga Januari 2030.



PI Zero tanpa Wi-Fi dan Bluetooth, sayangnya hampir tidak tersedia. Anda mungkin dapat menemukan alternatif PI Zero W dan PI Zero 2W dengan lebih mudah. Dalam hal ini, Anda dapat menonaktifkan fungsi koneksi dengan mengubah file konfigurasi. Setelah menginstal sistem operasi, Anda perlu menambahkan item ini ke config:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



bagian dari panduan ini akan menunjukkan kepada Anda bagaimana dan di mana melakukannya. Namun, jika Anda benar-benar ingin memastikannya, Anda dapat menemukan beberapa tutorial di web untuk melepas chip Wi-Fi dengan pemotong kecil, jenis yang cocok untuk mengerjakan papan elektronik.



**2** Sebuah _starter kit_ untuk Raspberry PI Zero: seperti yang biasa dilakukan di dunia Raspberry, tanpa casing eksternal. Selain itu, sumber daya yang terbatas dari papan yang begitu kecil membatasi kemungkinan koneksi dengan dunia luar.



Ketika saya memutuskan untuk melanjutkan, saya menemukan [kit ini] (https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) yang penuh dengan aksesori, untuk memanfaatkan sepenuhnya potensi PI Zero. Bahkan, kit ini berisi USB A -> micro USB power Supply, hub USB kecil, mini-HDMI -> adaptor HDMI, heatsink tembaga, dan casing luar aluminium. Kit ini juga dilengkapi dengan sekrup dan kunci pas yang diperlukan untuk memasang PI Zero di casing baru.





- Biaya**: 19.99 euro.



**3** Tutorial ini tidak mengharuskan Anda untuk menghabiskan anggaran besar untuk komputer airgap. Namun, Anda harus tahu bahwa Anda akan membutuhkan keyboard dan mouse USB (benar-benar berkabel, hindari Bluetooth) dan monitor. Tergantung pada input ke monitor Anda, Anda mungkin memerlukan adaptor dari mini-HDMI, satu-satunya output yang tersedia pada PI Zero. Terakhir, lihatlah Hard untuk mengetahui fakta bahwa kita semua memiliki keyboard dan mouse non-kabel di rumah di suatu tempat-sudah waktunya untuk mematikannya.



## Anggaran Tambahan



**4** Anda bisa mendapatkan daya asli Supply dari Raspberry, dengan harga sekitar 15,00 euro.



**5** Saya secara pribadi memilih untuk menggunakan daya Supply yang disediakan dalam _starter kit_, menggabungkannya dengan kabel USBA → miniUSB yang disebut kabel `tanpa data`, seharga 3,70 euro.



**6** Kartu micro SD, minimal memiliki penyimpanan massal minimal 32 GB; jika kualitas/level industri lebih baik.



**7** Anda akan membutuhkan sebuah sistem, adaptor USB ke micro SD, seperti yang Anda lihat pada gambar. Sistem operasi PI Zero dan memorinya akan bekerja pada media tersebut.



![img](assets/it/06.webp)



## Pemasangan Sistem Operasi


Sebelum menutup PI Zero Anda di dalam casing, saya sarankan Anda menginstal sistem operasi. Anda kemudian akan dapat memeriksa LED yang mengindikasikan pengoperasian, langsung.



Untuk memilih dan membakar sistem operasi, saya memilih cara termudah: menggunakan alat `PI Imager` Raspberry.



![img](assets/it/01.webp)



Pergi ke [Github Raspberry](https://github.com/raspberrypi/rpi-imager/releases) untuk mengunduh rilis terbaru Imager, pilih yang paling sesuai untuk sistem operasi Anda (v. 1.9.6 pada saat penulisan). Anda akan melihat bahwa di samping setiap aset juga ada hash dari file yang bersangkutan. Ini akan berguna untuk verifikasi.



![img](assets/it/02.webp)



Saya sarankan Anda memverifikasi sistem operasi yang akan Anda gunakan pada komputer airgap Anda, demi ketenangan pikiran Anda. Hal ini akan memberi Anda keyakinan bahwa Anda beroperasi dengan versi Imager yang sah (tidak berbahaya) dan, akibatnya, Raspi OS.



Lakukan verifikasi segera setelah mengunduh, dengan mesin yang biasa Anda gunakan terhubung ke Internet



Kemudian buka terminal Linux dan siapkan unduhan, buat direktori `raspios` yang berguna untuk bekerja dengannya.



![img](assets/it/19.webp)



Unduh Imager untuk distribusi Linux Anda dengan `wget`.



![img](assets/it/20.webp)



Terakhir, jalankan perintah file `sha256sum` dan bandingkan Hash dengan yang disediakan oleh Raspberry di Github.



![img](assets/it/21.webp)



Atau, jika Anda menggunakan Windows, buka Power Shell dan ketik perintah berikut:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Anda akan mendapatkan Hash yang harus sesuai dengan yang dipublikasikan di Raspberry Github.



Setelah Anda memverifikasi unduhan, Anda dapat menginstal Imager pada komputer harian Anda dan membukanya. Imager adalah alat yang Anda perlukan untuk membakar sistem operasi ke micro SD, yang akan menjadi "disk sistem" PI Zero.



Prosesnya sangat sederhana: pertama-tama pilihlah perangkat Raspberry yang akan Anda gunakan (jadi perhatikan **model** Raspberry Zero Anda), kemudian versi OS, dan terakhir titik pemasangan kartu micro SD untuk mem-flash OS.



### Langkah Pertama



![img](assets/it/03.webp)



### Langkah Kedua



![img](assets/it/07.webp)



**Perhatikan dengan baik**: pilih `PI OS 32-bit`, satu-satunya yang bekerja dengan PI Zero.



### Langkah Ketiga



![img](assets/it/08.webp)



(Berhati-hatilah untuk tidak memilih _Exclude System Drive_ agar tidak diminta untuk menginstal sistem operasi Raspi pada komputer Anda)



Apabila semuanya sudah diatur, Imager akan menanyakan kepada Anda, apakah Anda ingin menggunakan pengaturan khusus. Pilih yang Anda inginkan, atau klik _No_ untuk melanjutkan dengan opsi default.



![img](assets/it/09.webp)



Konfirmasikan bahwa Anda ingin menghapus isi micro SD



![img](assets/it/10.webp)



Imager mulai mem-flash sistem operasi ke micro SD, dan bilah gulir akan memberi tahu Anda tentang kemajuannya.



![img](assets/it/11.webp)



Pada akhirnya ada verifikasi otomatis, saya sarankan Anda untuk tidak menghentikannya.



![img](assets/it/12.webp)



Akhirnya, sebuah pesan muncul di layar, dan jika semuanya berhasil, maka akan terlihat seperti yang Anda baca dalam gambar.



![img](assets/it/13.webp)



Sekarang Anda benar-benar dapat melepas micro SD dari pembaca dan menempatkannya ke dalam slot PI Zero. Nyalakan Raspberry kecil dan perhatikan LED: kami mengharapkan lampu berwarna hijau dan berkedip, menunjukkan proses pemuatan normal sistem operasi, lalu tetap menyala terus-menerus. Jika Anda melihat tanda lain, misalnya jika LED berkedip dengan frekuensi teratur atau berwarna merah, lihat FAQ atau [halaman forum dukungan](https://forums.raspberrypi.com/).



## Konfigurasi Pertama


Pengaktifan pertama Raspi OS sedikit lebih lambat dari biasanya karena harus melakukan sejumlah tugas instalasi yang sebenarnya. Namun jika semua berjalan dengan baik, Anda akan menemukan layar selamat datang.



![img](assets/it/14.webp)



Klik _Next_ untuk menetapkan wilayah geografis, khususnya untuk memuat keyboard yang benar. Berikan perhatian khusus pada yang terakhir.



![img](assets/it/15.webp)



Klik _Next_ dan Anda akan diminta untuk membuat pengguna Anda, catat kredensial Anda dan simpan dengan baik.



![img](assets/it/16.webp)



Wizard akan meminta Anda untuk memilih browser web default, antara Chromium dan Firefox; wizard juga akan menanyakan tentang pengaturan jaringan Wi-Fi jika Anda menggunakan Zero W atau 2W PI. Lanjutkan dan klik _Lewati_.



Pada titik tertentu Anda akan diminta untuk meng-upgrade perangkat lunak dan sistem operasi yang terpasang. Pilih _Skip_: untuk tujuan latihan ini, kita sebenarnya sedang membangun mesin offline, yang harus tetap offline pada saat ini.



Terakhir, ia mungkin meminta Anda untuk mengaktifkan `ssh`, tetapi tolak langkah ini juga, karena ini adalah IP Zero airgap.



![img](assets/it/17.webp)



Tidak banyak yang perlu dikonfigurasi. Setelah selesai, nyalakan ulang Raspberry agar perubahan diterapkan.



![img](assets/it/18.webp)



## Celah Udara Komputer Baru


Setelah reboot, komputer airgap baru Anda sudah siap. PI Zero menunjukkan desktop baru, yang dapat Anda gunakan melalui GUI atau dari baris perintah.



![img](assets/it/22.webp)



### Langkah Pertama untuk PI Nol W atau 2W


Jika Anda bekerja dengan seri Raspberry PI Zero W atau 2W, papan Anda memiliki chip untuk Wi-Fi dan Bluetooth di dalamnya. Selama penyiapan pertama, Anda melewatkan konfigurasi koneksi, sehingga PI Zero tidak terhubung ke Internet. Sekarang Anda dapat menonaktifkan kedua chip tersebut secara permanen melalui perangkat lunak.



Bahkan, Raspi OS menyediakan file `config.txt` yang dapat Anda edit sesuai dengan keinginan Anda. File `config` terletak pada partisi `boot`, pada direktori `firmware`, dan Anda dapat mengedit dan menyimpannya dengan hak akses `root`.



Buka terminal dari ikon di kiri atas dan terminal akan menjadi `root`.(1)



![img](assets/it/23.webp)



(1) Jika Raspi OS tidak meminta Anda untuk membuat kata sandi `root` pada langkah sebelumnya, saya sarankan Anda untuk membuatnya sekarang, dengan perintah `passwd`. Membuat pengguna `root` bergerak secara independen dari pengguna pribadi Anda akan sangat membantu dalam situasi pemulihan.



Dengan terminal, periksa file `config.txt` dan bersiaplah untuk mengeditnya dengan editor `nano`.



![img](assets/it/24.webp)



Pengeditan harus dilakukan di bagian bawah seluruh `config`, setelah kata `[All]`. Pada titik inilah Anda akan menambahkan perintah `dtoverlay` yang ditunjukkan pada awal tutorial.



![img](assets/it/25.webp)



Simpan, tutup, dan mulai ulang. Pada langkah berikut ini kita akan membahas eksplorasi Raspberry kecil.



## Apa yang Diharapkan dari Perangkat ini?


Melihat [spesifikasi teknis](https://www.raspberrypi.com/products/raspberry-pi-zero/) dari situs Raspberry, PI Zero memiliki prosesor BCM2835 single-core dan RAM 512 MB, sehingga tidak tampak terlalu bertenaga.



Karena terminal lebih ringan, kita akan menggunakan baris perintah untuk menjelajahi konfigurasi sistem.



Ketika Anda menyalakan, Anda akan melihat layar berwarna pelangi singkat, diikuti dengan pesan selamat datang dari Raspberry dan, di sudut kiri bawah, pesan kernel yang terkait dengan booting.



Ketika desktop PI OS muncul, buka terminal dan ketik:



```bash
uname -a
```


Perintah ini akan menampilkan versi kernel yang sedang digunakan pada layar, serta informasi lainnya.



![img](assets/it/26.webp)



Anda juga dapat melihat informasi tentang CPU dan perangkat keras dengan mengetik:



```bash
lscpu
```



![img](assets/it/27.webp)



Dan juga lihat `proc/mem/info`.



![img](assets/it/28.webp)



Untuk mengetahui versi Debian dan nama kode rilis:



"Bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



"Bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Gunakan


Meskipun kinerjanya tampak terbatas (di atas kertas dan dibandingkan dengan kekuatan mesin saat ini), PI Zero memiliki performa yang baik, terutama sebagai terminal.





- Pertama, Anda dapat masuk ke menu utama dan mendapatkan inspirasi dari panel _Add/Remove software_, di mana Anda akan menemukan sejumlah utilitas untuk memprogram dan berlatih. Ingatlah bahwa Anda juga dapat melakukan hal ini dari terminal, tetapi selalu dengan hak akses `root`.



![img](assets/it/33.webp)





- Anda dapat "mengadopsi" perangkat offline ini untuk menyimpan berbagai dokumen rahasia, yang akan tetap dapat diakses saat dibutuhkan, tanpa harus terhubung ke Internet.
- Anda dapat menggunakan konfigurasi ini untuk generate kunci GPG Anda dengan aman.
- Kamu bahkan bisa memanfaatkan "mainan" baru ini sebagai perangkat tanda tangan airgap, [dengan mengikuti saran dari Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Di antara Wallet yang saya ketahui, satu-satunya yang menyediakan rilis 32-bit adalah Electrum. Nah: Zero IP seperti yang kita siapkan dalam tutorial ini akan memungkinkan Anda untuk menyimpan kunci pribadi secara offline yang diatur untuk airgap Wallet yang telah kita bahas dalam tutorial ini:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Kesimpulan


Pengaturan ini mungkin memiliki satu kelemahan besar: micro SD adalah media yang dapat menimbulkan masalah. Ini rentan terhadap penggunaan yang berat; mungkin Anda sudah memiliki pengalaman dengan hal ini, karena menggunakannya dengan ponsel Anda. Setelah menginstal semua perangkat lunak yang ingin Anda gunakan pada Zero airgap IP, buatlah cadangan yang baik untuk micro SD yang berharga, dengan menggunakan alat Raspi OS yang Anda miliki.



![img](assets/it/34.webp)



Seiring dengan bertambahnya kebutuhan Anda, dan juga kemungkinan anggaran Anda, Anda bisa menjelajahi Raspberry lain atau solusi serupa. Berbicara tentang memori, misalnya, PI 5 menawarkan kemungkinan untuk merakit drive NVME M2, yang tentunya lebih kuat daripada microSD.



Jangan lupa untuk mencatat dan mendokumentasikan setiap langkah instalasi perangkat lunak utilitas yang akan Anda gunakan secara offline. **Cepat atau lambat, OS Raspi yang diperbarui akan keluar** yang pasti ingin Anda manfaatkan. Pada saat itu Anda harus menghapus semuanya dan melakukan semuanya lagi (mungkin dengan micro SD baru 😂).



Latihan yang baru saja kita lakukan, dengan asumsi bahwa ini adalah percobaan pertama Anda, Anda akan mengingatnya untuk waktu yang lama. Tidak selalu memungkinkan untuk mencurahkan perangkat keras untuk operasi `tertanam` secara offline, tanpa mengabaikan perhatian pada mesin yang memiliki celah udara untuk dihidupkan dan diperiksa dari waktu ke waktu.



Anda berhasil menyelesaikannya, selamat! Dan Anda akan dapat menyarankan solusi ini kepada semua orang yang perlu menekan anggaran mereka.