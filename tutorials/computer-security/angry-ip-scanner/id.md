---
name: Angry IP Scanner
description: Cara sederhana untuk memindai jaringan Anda
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## I. Presentasi



Bagaimana Anda memindai jaringan Windows untuk mesin yang terhubung dengan cepat dan mudah? Jawabannya adalah Angry IP Scanner. Proyek sumber terbuka ini memungkinkan Anda memindai jaringan dengan mudah, menggunakan Interface grafis yang mudah digunakan.



Alat ini dapat digunakan oleh perorangan untuk memindai jaringan lokal mereka, tetapi juga oleh para profesional TI untuk tujuan yang sama. Bukti bahwa **alat ini sangat praktis**, alat ini telah digunakan oleh **beberapa kelompok penjahat siber** untuk memindai jaringan perusahaan (dengan cara yang sama seperti Nmap). Contoh yang bagus adalah [kelompok ransomware RansomHub] (https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Ini masih merupakan perangkat lunak yang baik, tetapi seperti halnya perangkat lunak berorientasi jaringan dan keamanan lainnya, penggunaannya dapat disalahgunakan.



Di sini, kita akan menggunakannya pada **Windows 11**, tetapi sangat memungkinkan untuk menggunakannya pada versi **Windows** lainnya, serta pada **Linux** dan **macOS**.



Kurang komprehensif dibandingkan Nmap, **Angry IP** Scanner masih menarik untuk analisis jaringan dasar yang cepat, tetapi juga karena berada dalam jangkauan semua orang. Alat ini akan **mendeteksi host yang terhubung ke jaringan** dan mengidentifikasi **nama host** dan **port yang terbuka**.



Jika Anda ingin melangkah lebih jauh, lihat tutorial tentang Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Memulai dengan Pemindai IP Marah



### A. Unduh dan pasang Pemindai IP Marah



Anda bisa mengunduh versi terbaru Angry IP Scanner dari situs web resmi aplikasi ini atau dari GitHub. Kami akan menggunakan opsi yang terakhir. Klik tautan di bawah ini dan unduh versi EXE-nya: "**ipscan-3.9.1-setup.exe**".





- [Pemindai IP Marah GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Jalankan file yang dapat dieksekusi untuk melanjutkan penginstalan. Tidak ada hal khusus yang harus dilakukan selama instalasi.



![Image](assets/fr/013.webp)



### B. Menjalankan pemindaian jaringan awal



Saat pertama kali diluncurkan, luangkan waktu untuk membaca petunjuk di jendela "**Memulai**" untuk mempelajari lebih lanjut mengenai cara kerja alat ini. Omong-omong, ada beberapa istilah yang perlu dipertimbangkan:





- **Feeder**: modul yang bertanggung jawab untuk menghasilkan daftar alamat IP yang akan dipindai, dari rentang IP acak atau file dengan daftar alamat IP.
- **Fetcher**: sekumpulan modul untuk mengambil informasi tentang host di jaringan. Misalnya, ada fetcher untuk mendeteksi alamat MAC, memindai port, mendeteksi nama host, atau mengirim permintaan HTTP.



![Image](assets/fr/018.webp)



Untuk memindai subnet IP, cukup masukkan **start IP Address** dan **end IP Address** di bidang "**Rentang IP**" (jika tidak, ubah jenisnya di sebelah kanan). Kemudian klik tombol "**Mulai**".



![Image](assets/fr/019.webp)



Beberapa puluh detik kemudian, hasilnya akan terlihat di Interface perangkat lunak. **Untuk setiap IP Address dalam rentang yang dianalisis, Anda akan melihat apakah Angry IP Scanner telah mendeteksi sebuah host atau tidak.** Sebuah ringkasan juga akan muncul di layar, yang menunjukkan jumlah host yang aktif (dalam kasus ini 6) dan jumlah host dengan port yang terbuka.



![Image](assets/fr/020.webp)



Di sini, kita dapat melihat keberadaan host bernama "**OPNsense.local.domain**", yang terkait dengan IP Address "**192.168.10.1**" dan dapat diakses di **port 80** dan **443** (HTTP dan HTTPS). Mengklik kanan pada host akan memberikan akses ke perintah tambahan, seperti ping, melacak rute, dan membuka peramban melalui IP Address ini.



![Image](assets/fr/012.webp)



### C. Menambahkan port pemindaian



Secara default, **Pemindai IP Marah** akan memindai 3 port: **80** (HTTP), **443** (HTTPS) dan **8080**. Anda dapat menambahkan lebih banyak port untuk dipindai dari preferensi aplikasi. Klik pada menu "**Tools**", lalu pada tab "**Ports**".



Di sini, Anda dapat memodifikasi daftar port melalui opsi "**Pemilihan port**". Anda dapat **menunjukkan nomor port tertentu yang dipisahkan dengan koma, atau rentang port**. Contoh di bawah ini menambahkan dua port: **445** (SMB) dan **389** (LDAP). Untuk memindai port dari 1 hingga 1000, masukkan "**1-1000**". Tidak dijelaskan apakah pemindaian port dilakukan dalam TCP, UDP, atau keduanya.



![Image](assets/fr/021.webp)



Jika Anda menjalankan pemindaian lagi, kemungkinan besar Anda akan mendapatkan informasi baru. Pada contoh di bawah ini, Angry IP Scanner memberi tahu saya bahwa port 389 dan 445 terbuka pada host "**SRV-ADDS-01**" dan "**SRV-ADDS-02**", berkat konfigurasi baru port yang akan dipindai.



![Image](assets/fr/022.webp)



**Catatan**: dari menu "**Scanner**", Anda dapat mengekspor hasil pemindaian ke file teks.



Jika Anda ingin melakukan pemindaian lebih lanjut, klik menu "**Tools**", kemudian klik "**Fetchers**". Hal ini akan menambah "kemampuan" pada pemindaian. Cukup pilih fetcher dan geser ke kiri untuk mengaktifkannya. Hal ini akan menambahkan kolom tambahan ke hasil pemindaian.



![Image](assets/fr/014.webp)



Contoh di bawah ini menunjukkan fungsi "**Info NetBIOS**" dan "**Deteksi Web**". Fungsi yang pertama memberikan informasi tambahan seperti MAC Address dan nama domain mesin, sedangkan fungsi yang kedua menampilkan judul halaman web (yang dapat memberikan indikasi jenis server web atau aplikasi).



![Image](assets/fr/011.webp)



Terakhir, dari preferensi, Anda juga dapat mengubah metode yang digunakan untuk "**ping**", yaitu untuk mempertimbangkan apakah sebuah host aktif atau tidak. Karena beberapa host tidak merespons ping, ini memungkinkan Anda untuk mencoba metode lain (paket UDP, probe port TCP, ARP, kombinasi UDP + TCP, dll.).



## III. Kesimpulan



Sederhana dan efektif: Angry IP Scanner mendeteksi host yang terhubung ke jaringan, dan memungkinkan Anda mengonfigurasi pemindaian port. Dari segi opsi, aplikasi ini tidak sefleksibel Nmap, dan tidak menjangkau lebih jauh, tetapi ini merupakan awal yang baik untuk pemindaian cepat.



Jika Anda ingin menggunakan **Nmap** dengan Interface grafis, Anda dapat menggunakan **aplikasi Zenmap** (lihat ikhtisar di bawah).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d