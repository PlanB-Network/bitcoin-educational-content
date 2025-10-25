---
name: WireGuard
description: Menyiapkan WireGuard VPN pada Debian dan Windows
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*
___

## I. Presentasi

Dalam tutorial ini, kita akan belajar cara mengonfigurasi VPN berbasis WireGuard, sebuah solusi VPN gratis dan open source yang meningkatkan kinerja tanpa mengabaikan keamanan.

WireGuard adalah solusi yang relatif baru, tersedia sebagai rilis stabil sejak Maret 2020, dan mendapat kesempatan untuk diintegrasikan langsung ke dalam **kernel Linux sejak versi 5.6**. Ini tidak mencegahnya untuk diakses dari distribusi Linux yang lebih lama yang menggunakan versi kernel yang berbeda. Dibandingkan dengan solusi seperti OpenVPN dan IPSec, WireGuard lebih sederhana untuk digunakan dan jauh lebih cepat, seperti yang akan kita lihat di akhir artikel ini.

Beberapa poin penting tentang WireGuard:

- Sederhana, ringan, dan sangat efisien!
- Operasi hanya UDP (yang bisa menjadi kelemahan saat melewati firewall tertentu)
- Bekerja pada model peer-to-peer daripada client-server
- Otentikasi melalui pertukaran kunci, dengan prinsip yang sama seperti SSH dengan kunci privat/publik
- Penggunaan beberapa algoritma: enkripsi simetris dengan ChaCha20, otentikasi pesan dengan Poly1305, serta yang lainnya seperti Curve25519, BLAKE2, dan SipHash24
- Mendukung IPv4 dan IPv6
- Multi-platform: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (dan diimplementasikan di ProtonVPN)
- Hanya 4.000 baris kode, dibandingkan dengan ratusan ribu untuk solusi lain

Untuk bagian kriptografi, berbagai algoritma yang digunakan dipilih dengan cermat, diaudit dalam beberapa cara, dan diperiksa oleh peneliti keamanan yang berspesialisasi di bidang ini.

Situs web resmi proyek: [wireguard.com](https://www.wireguard.com/)

Apakah Anda yakin dengan solusi ini setelah membaca pengantar ini? Yang perlu dilakukan hanyalah membaca terus!

## II. Diagram Lab WireGuard

Sebelum saya menyajikan lab saya untuk mengatur WireGuard, Anda harus tahu bahwa Anda dapat membayangkan **menggunakan WireGuard untuk menghubungkan dua infrastruktur jarak jauh**, tetapi juga untuk **menghubungkan klien jarak jauh ke infrastruktur seperti jaringan perusahaan atau jaringan rumah Anda**. Ini sejalan dengan OpenVPN, seperti yang baru-baru ini kita lihat di tutorial "[OpenVPN pada Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".

Jika WireGuard tidak diatur langsung di router atau firewall, seperti yang dapat dibayangkan dengan OpenWRT, Anda perlu mengatur port forwarding agar aliran data mencapai pasangan WireGuard.

![Image](assets/fr/034.webp)

Sekarang saya akan memberi tahu Anda tentang lab saya dan apa yang akan kita siapkan hari ini.

Saya akan menggunakan komputer Debian 11 sebagai server WireGuard dan klien Windows sebagai klien VPN WireGuard. Meskipun agak menyesatkan untuk berbicara tentang hubungan client-server, karena WireGuard bekerja pada model "peer-to-peer". Itu sedikit keliru ketika Anda mencoba mengatur koneksi "client-to-site". Katakanlah saja bahwa saya akan memiliki dua pasangan atau dua titik koneksi WireGuard jika Anda mau: satu di Debian 11 dan yang lainnya di Windows.

Kedua pasangan ini dapat berkomunikasi satu sama lain dalam dua arah, artinya dari komputer Windows saya, saya dapat mengakses LAN jarak jauh dari mesin Debian 11, dan sebaliknya: itu semua tergantung pada konfigurasi terowongan dan firewall dari peer WireGuard.

Dalam contoh ini, saya akan fokus pada kasus berikut: **dari Peer Windows 1 saya yang terhubung ke jaringan rumah saya, saya ingin mengakses jaringan perusahaan saya untuk mengakses server perusahaan melalui saluran VPN WireGuard**. Ini menghasilkan diagram berikut:

![Image](assets/fr/035.webp)

Dalam hal alamat IP, ini memperlihatkan:

- Jaringan rumah: 192.168.1.0/24
- Jaringan perusahaan: 192.168.100.0/24
- Jaringan saluran WireGuard: 192.168.110.0/24
- Alamat IP dari Peer 1 (Windows) di saluran : 192.168.110.2/24
- Alamat IP dari Peer 2 (Debian) di saluran : 192.168.110.121/24

Hanya itu saja yang bisa dilakukan! Mari kita lanjutkan ke konfigurasi!

**Catatan**: secara default, WireGuard beroperasi dalam mode UDP pada **port 51820**.

## III Instalasi dan konfigurasi server WireGuard

Saya akan menggunakan istilah "klien" untuk komputer Windows dan "server" untuk komputer Debian dalam tutorial ini, karena meskipun ini adalah peer-to-peer, namun istilah ini lebih bermakna.

### A. Menginstal WireGuard pada Debian 11

Paket instalasi WireGuard tersedia di repositori resmi Debian 11, jadi yang harus kita lakukan adalah memperbarui cache paket dan menginstalnya:

```
sudo apt-get update
```

```
sudo apt-get install wireguard
```

![Image](assets/fr/022.webp)

Bagian server WireGuard akan diinstal, bersama dengan berbagai aplikasi yang memberikan akses ke perintah yang berguna untuk mengelola konfigurasi.

### B. Memasang Interface WireGuard

Dengan menggunakan **command "wg "**, kita perlu membuat kunci privat dan kunci publik: penting untuk otentikasi antara dua pasangan, yaitu server dan klien (yang juga akan membutuhkan sepasang kunci).

Kita akan membuat kunci privat "**/etc/wireguard/wg-private.key**" dan kunci publik "**/etc/wireguard/wg-public.key**" dengan urutan perintah berikut:

```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```

![Image](assets/fr/023.webp)

Nilai kunci publik akan dikembalikan di konsol. Dalam file konfigurasi WireGuard, kita perlu menambahkan nilai kunci privat kita. Untuk mengambil nilai ini, masukkan perintah di bawah ini dan salin nilainya:

```
sudo cat /etc/wireguard/wg-private.key
```
Saatnya untuk membuat file konfigurasi di "**/etc/wireguard/**". Misalnya, kita dapat menamai file ini "**wg0.conf**", jika kita berpikir bahwa interface jaringan yang terkait dengan WireGuard akan menjadi "wg0", dengan prinsip yang sama seperti "eth0", misalnya.

```
sudo nano /etc/wireguard/wg0.conf
```

Dalam file ini, pertama-tama kita harus menambahkan konten berikut ini (kita akan kembali lagi untuk melengkapinya nanti):

```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```

Bagian `[Interface]` digunakan untuk mendeklarasikan bagian server. Berikut adalah beberapa informasi:

- **Address**: alamat IP dari interface WireGuard di dalam saluran VPN (subnet yang berbeda dari LAN jarak jauh).
- **SaveConfig**: konfigurasi disimpan (dan dilindungi) selama interface aktif.
- **ListenPort**: port pendengaran WireGuard. Dalam hal ini, 51820 adalah port default, tetapi Anda dipersilakan untuk menyesuaikannya.
- **PrivateKey**: nilai kunci privat server kita (wg-private.key).

Simpan file tersebut dan tutup. Dengan perintah "**wg-quick**", kita dapat memulai Interface ini dengan menentukan namanya (wg0, karena file tersebut bernama wg0.conf):

```
sudo wg-quick up wg0
```

Jika Anda mencantumkan alamat IP dari server Debian 11 Anda, Anda akan melihat interface baru bernama "wg0" dengan alamat IP yang ditentukan dalam file konfigurasi:

```
ip a
```

![Image](assets/fr/027.webp)

Dengan semangat yang sama, kita dapat menampilkan konfigurasi Interface "wg0" melalui perintah "wg show":

```
sudo wg show wg0
```

![Image](assets/fr/024.webp)

Terakhir, kita perlu mengaktifkan startup otomatis dari interface wg0 WireGuard kita:

```
sudo systemctl enable wg-quick@wg0.service
```

Untuk saat ini, kita akan mengesampingkan konfigurasi sisi server WireGuard.

### C. Mengaktifkan Penerusan IP

Agar komputer Debian 11 kita dapat **merutekan paket di antara jaringan yang berbeda (seperti router)**, yaitu antara jaringan VPN dan jaringan lokal, kita perlu mengaktifkan [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Secara default, fitur ini dinonaktifkan.

Ubah file konfigurasi ini:

```
sudo nano /etc/sysctl.conf
```

Tambahkan arahan berikut ini ke akhir file dan simpan file :

```
net.ipv4.ip_forward = 1
```

Hanya itu saja yang bisa dilakukan.

### D. Mengaktifkan IP Masquerade

Agar server kita merutekan paket dengan benar dan LAN jarak jauh dapat diakses oleh komputer Windows, kita perlu mengaktifkan IP Masquerade di server Debian kita. Ini semacam aktivasi NAT. Saya akan melakukan konfigurasi ini pada firewall Linux melalui UFW, yang biasa saya gunakan ([tutorial ufw di Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).

Jika Anda belum memiliki UFW dan ingin mengaturnya (Anda juga dapat menggunakan Nftables), mulailah dengan menginstal:

```
sudo apt install ufw
```

Pertama-tama, Anda harus mengaktifkan SSH agar tidak kehilangan kendali atas server jarak jauh (sesuaikan nomor port):

```
sudo ufw allow 22/tcp
```

Port 51820 di UDP juga harus diotorisasi, karena kami menggunakannya untuk WireGuard (sekali lagi, sesuaikan nomor port):

```
sudo ufw allow 51820/udp
```
Selanjutnya, kita akan melanjutkan dengan konfigurasi untuk mengaktifkan IP masquerade. Untuk melakukan ini, kita perlu mengambil nama interface yang terhubung ke jaringan lokal. Jika Anda tidak tahu namanya, jalankan "ip a" untuk melihat nama kartu. Dalam kasus saya, itu adalah kartu "**ens192**".

![Image](assets/fr/036.webp)

Kita akan menggunakan informasi ini. Edit file berikut ini:

```
sudo nano /etc/ufw/before.rules
```

Tambahkan baris-baris ini di akhir file untuk **mengaktifkan IP masquerade pada interface ens192** (sesuaikan nama interface) di dalam string POSTROUTING dari tabel NAT firewall lokal kita:

```
# NAT - IP masquerade
*nat*
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```

Gambar menunjukkan :

![Image](assets/fr/037.webp)

Biarkan file konfigurasi ini tetap terbuka dan lanjutkan ke langkah berikutnya

### E. Konfigurasi firewall Linux untuk WireGuard

Masih di file konfigurasi yang sama, kita akan mendeklarasikan jaringan perusahaan "192.168.100.0/24" sehingga kita dapat menghubunginya. Berikut adalah dua aturan yang perlu ditambahkan (idealnya setelah bagian "*# ok icmp code for FORWARD*" untuk mengelompokkan aturan bersama-sama):

```
# authorize forwarding for the trusted remote network (+ the VPN network)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```

Jika Anda hanya ingin mengotorisasi satu host saja, misalnya "192.168.100.11", itu mudah:

```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```

Sekarang Anda dapat menyimpan file dan menutupnya. Yang tersisa hanyalah mengaktifkan UFW dan restart layanan untuk menerapkan perubahan kita:

```
sudo ufw enable
```

```
sudo systemctl restart ufw
```

Bagian pertama dari konfigurasi server Debian sekarang sudah selesai.

## IV. Klien WireGuard untuk Windows

Klien WireGuard tersedia untuk Windows, macOS, Android, dll... Ini berita bagus. Semua unduhan tersedia di halaman ini:  [WireGuard Client](https://www.wireguard.com/install/). Dalam contoh ini, saya akan menyiapkan klien di Windows. Untuk menyiapkan klien WireGuard di Linux, ikuti prinsip yang sama seperti saat membuat file wg0.conf di mesin Debian (tanpa semua NAT, dll.).

### A. Menginstal klien WireGuard Windows

Setelah Anda mengunduh file yang dapat dieksekusi atau paket MSI, penginstalannya sangat mudah: cukup jalankan penginstal, dan...voila, selesai! 🙂

![Image](assets/fr/038.webp)

### B. Membuat profil WireGuard

Mulailah dengan membuka perangkat lunak untuk membuat saluran baru. Untuk melakukannya, klik panah di sebelah kanan tombol "**Add tunnel**" dan klik tombol "**Add empty tunnel**".

![Image](assets/fr/028.webp)

Window konfigurasi akan terbuka. Setiap kali konfigurasi saluran baru dibuat, WireGuard menghasilkan sepasang kunci privat/publik yang spesifik untuk konfigurasi ini. **Dalam konfigurasi ini, kita perlu mendeklarasikan "peer", yaitu server jarak jauh**:

```
[Interface]
PrivateKey = <la clé privée du PC>
```

Kita perlu melengkapi konfigurasi ini, khususnya untuk mendeklarasikan alamat IP pada interface ini (**Address**), tetapi juga untuk mendeklarasikan server WireGuard jarak jauh melalui blok `[Peer]`. Gambar di bawah ini seharusnya mengingatkan Anda tentang file konfigurasi yang kita buat di sisi server Linux.

Mari kita mulai dengan blok `[Interface]`, menambahkan alamat IP **"192.168.110.2"**; ingat bahwa server memiliki alamat IP "**192.168.110.121**" pada segmen jaringan ini. Ini menghasilkan:

```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```

Selanjutnya, kita perlu mendeklarasikan blok "Peer" dengan tiga properti, yang menghasilkan konfigurasi berikut:

```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```

Dalam gambar :

![Image](assets/fr/029.webp)

**Beberapa penjelasan tentang blok `[Peer]`:**

- **PublicKey**: ini adalah kunci publik dari server WireGuard Debian 11 (Anda dapat memperoleh nilainya dengan perintah "*sudo wg*")
- **AllowedIPs**: ini adalah alamat IP/subnet yang dapat diakses melalui jaringan VPN WireGuard ini, dalam hal ini subnet khusus untuk VPN WireGuard saya (*192.168.110.0/24*) dan LAN jarak jauh saya (*192.168.100.0/24*)
- **Endpoint**: ini adalah IP Address dari hos Debian 11, karena ini adalah titik koneksi WireGuard kami (Anda harus menentukan IP Address publik)

Terakhir, masukkan nama di kolom "**Name**" (tanpa spasi) dan salin lalu tempel kunci publik klien, karena kita akan membutuhkannya untuk mendeklarasikannya di server. Klik "**Register**".

### C. Mendeklarasikan klien di server WireGuard

Saatnya kembali ke server Debian untuk mendeklarasikan "**Peer**", yaitu PC Windows kita, dalam konfigurasi WireGuard. Pertama-tama, kita perlu menghentikan Interface "wg0" untuk memodifikasi konfigurasinya:

```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```

Selanjutnya, modifikasi file konfigurasi yang telah dibuat sebelumnya:

```
sudo nano /etc/wireguard/wg0.conf
```

Pada file ini, setelah blok `[Interface]`, kita perlu mendeklarasikan blok `[Peer]`:

```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```

Blok `[Peer]` ini berisi kunci publik PC Windows 10 (**PublicKey**) dan alamat IP interface PC (**AllowedIPs**): server akan berkomunikasi di dalam saluran WireGuard ini hanya untuk menghubungi klien Windows, oleh karena itu nilainya "**192.168.110.2/32**".

Yang tersisa hanyalah menyimpan file (_CTRL+O lalu Enter lalu CTRL+X melalui Nano_). Luncurkan kembali Interface "wg0":

```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```

Untuk memeriksa apakah deklarasi peer berfungsi, Anda dapat menggunakan perintah ini:

```
sudo wg show
```

Setelah host jarak jauh mengatur koneksi WireGuard, IP Address akan dipindahkan ke nilai "endpoint".

![Image](assets/fr/033.webp)

Terakhir, kita akan mengamankan file konfigurasi untuk membatasi akses root:

```
sudo chmod 600 /etc/wireguard/ -R
```

### D. Koneksi WireGuard Pertama

Sekarang setelah konfigurasi siap, kita dapat memulainya dari PC Windows. Untuk melakukannya, di klien "**WireGuard**", klik tombol "**Activate**": koneksi akan **berubah dari "Off" menjadi "On"**, tetapi itu tidak berarti akan berfungsi. Itu semua tergantung pada apakah konfigurasi Anda benar atau tidak. Ketika koneksi terjalin, kedua komputer kita berkomunikasi melalui Interface WireGuard yang dikonfigurasi di setiap sisi!

![Image](assets/fr/030.webp)

Jika terjadi masalah, ini akan terlihat di tab "**Logbook**". Kedua host akan bertukar paket secara teratur untuk memeriksa status koneksi, oleh karena itu pesan "_Receiving keepalive packet from peer 1_".

![Image](assets/fr/031.webp)

Jika tab "**Journal**" WireGuard menampilkan pesan seperti yang di bawah ini, Anda perlu memeriksa apakah kunci publik yang dideklarasikan di kedua sisi sudah benar.

```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```

Dari PC jarak jauh saya, saya dapat ping alamat IP interface WireGuard saya di sisi server, serta host di LAN jarak jauh saya.

![Image](assets/fr/032.webp)

### E. Kinerja: OpenVPN vs WireGuard

Dari PC jarak jauh saya yang terhubung ke VPN WireGuard, saya berhasil mengakses server file dan mentransfer file melalui [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), untuk melihat tingkat transfer. Dengan WireGuard, saya mendapatkan kecepatan maksimal sekitar 45 Mb/s, yang luar biasa, karena saya menggunakan WiFi.

![Image](assets/fr/025.webp)

Dalam kondisi yang sama, tetapi kali ini melalui koneksi OpenVPN (dalam UDP), dengan operasi yang sama, throughput benar-benar berbeda: sekitar 3 MB/s. Perbedaannya sangat jelas!

![Image](assets/fr/026.webp)

Ini menarik, karena jika, misalnya, Anda beralih dari koneksi WiFi ke koneksi 4G/5G, koneksi ulang akan sangat cepat sehingga interupsi tidak akan terlihat.

### F. Bonus: saluran penuh WireGuard

Dengan konfigurasi saat ini, sebagian lalu lintas mengalir melalui VPN, dan sisanya melalui koneksi Internet klien, termasuk browsing Internet. Jika kita ingin beralih ke **mode full tunnel WireGuard**, agar semuanya melewati saluran VPN, kita perlu membuat beberapa perubahan pada konfigurasi kita....

Pertama, Anda perlu memasang paket "resolvconf" di Debian:

```
sudo apt-get update
sudo apt-get install resolvconf
```

Setelah ini selesai, Anda perlu memodifikasi profil "wg0.conf" pada komputer Debian: hentikan Interface, modifikasi, dan mulai ulang.

```
sudo wg-quick down /etc/wireguard/wg0.conf
```

Selanjutnya, **di blok `[Interface]`, kita menambahkan server DNS yang akan digunakan**. Dalam kasus saya, itu adalah pengendali domain (domain controller) lab saya, tetapi kita juga bisa memasang Bind9 pada komputer Debian untuk memiliki resolver lokal.

```
DNS = 192.168.100.11
```

Simpan file, lalu mulai ulang Interface :

```
sudo wg-quick up /etc/wireguard/wg0.conf
```

Terakhir, dalam konfigurasi saluran pada workstation Windows 10, Anda perlu memodifikasi bagian "AllowedIPs" untuk menunjukkan bahwa semuanya harus melewati saluran. Menggantikan :

```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```

Oleh :

```
AllowedIPs = 0.0.0.0/0
```

Anda dapat melihat bahwa ini juga mengaktifkan opsi "**Kill switch*".

![Image](assets/fr/040.webp)

Akhirnya, saya memanfaatkan saluran penuh ini untuk melakukan uji aliran kecil, yang hasilnya ditunjukkan di bawah ini:

![Image](assets/fr/039.webp)

Konfigurasi WireGuard cukup sederhana dan mudah dimengerti, dan yang terpenting mudah untuk dipelihara.**WireGuard dianggap sebagai masa depan VPN**, jadi sebaiknya kita mengawasinya dengan cermat! Kita juga dapat melihat bahwa manfaatnya signifikan dalam hal kinerja, yang merupakan keuntungan besar untuk WireGuard dibandingkan dengan OpenVPN.

Dokumentasi tambahan:

- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)

**WireGuard VPN Anda sudah aktif dan berjalan! Selamat!**
