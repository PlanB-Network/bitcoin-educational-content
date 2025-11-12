---
name: Rencanakan ₿ Akademi - Aplikasi Pir
description: Bagaimana cara menginstal dan menggunakan aplikasi Plan ₿ Academy di Pears?
---

![cover](assets/cover.webp)


Anda mungkin sudah mengetahui bahwa Plan ₿ Academy adalah basis data pendidikan terbesar yang didedikasikan untuk Bitcoin, yang menyatukan kursus, tutorial, dan ribuan sumber daya sumber terbuka. Awalnya, Plan ₿ Academy adalah sebuah situs web. Namun, apa yang akan terjadi jika Anda tidak dapat mengaksesnya secara normal, misalnya jika terjadi penyensoran?


Dalam tutorial ini, kita akan belajar bagaimana menjalankan platform **Plan ₿ Academy** dengan cara yang benar-benar tahan sensor menggunakan **Pears**, sebuah teknologi peer-to-peer (P2P) yang dikembangkan oleh **Holepunch** dan didukung oleh **Tether**.


Pears adalah perangkat lunak yang memungkinkan kita menjalankan platform Plan ₿ Academy tanpa bergantung pada situs web terpusat. Dalam tutorial ini, kita akan menginstal Pears di komputer Anda untuk mengakses Plan ₿ Academy melalui Pears.


Tujuan Pears sederhana: untuk memungkinkan pendistribusian dan penggunaan aplikasi web tanpa bergantung pada infrastruktur terpusat (tidak ada server, tidak ada host, tidak ada perantara). Dengan kata lain, meskipun penyedia layanan cloud ditutup atau suatu negara memblokir sebuah domain, aplikasi akan terus hidup di antara rekan-rekan jaringan. Pendekatan ini memungkinkan platform pendidikan kami, Plan ₿ Academy, tetap dapat diakses di seluruh dunia, tanpa ada satu pun titik kegagalan.


---

**TL; DR:**



- Pasang Pir;



- Jalankan perintah berikut untuk meluncurkan aplikasi Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Apa itu Pir?


Pears sekaligus merupakan lingkungan runtime, alat pengembangan, dan platform penyebaran untuk aplikasi peer-to-peer. Alat sumber terbuka ini memungkinkan Anda untuk membangun, berbagi, dan menjalankan perangkat lunak tanpa server atau infrastruktur, secara langsung di antara para pengguna. Secara praktis, ini berarti bahwa alih-alih meng-host aplikasi di server pusat, setiap pengguna menjadi simpul dalam jaringan: mereka berbagi bagian dari aplikasi dan data dengan rekan-rekan lainnya. Keseluruhan sistem membentuk jaringan terdistribusi di mana setiap contoh bekerja sama untuk menjaga agar layanan tetap dapat diakses.


![Image](assets/fr/01.webp)


Pendekatan ini didasarkan pada seperangkat komponen perangkat lunak modular yang dikembangkan oleh Holepunch:



- Hypercore**: log terdistribusi yang memastikan konsistensi dan keamanan data tanpa basis data pusat.
- Hyperbee**: indeks yang dibangun di atas Hypercore yang memungkinkan data diatur dan ditanyakan secara efisien.
- Hyperdrive**: sistem file terdistribusi yang digunakan untuk menyimpan dan menyinkronkan file aplikasi di antara rekan-rekan.
- Hyperswarm** dan **HyperDHT**: lapisan jaringan yang memungkinkan penemuan rekan dan koneksi di seluruh dunia tanpa server pusat.
- Secretstream**: protokol enkripsi ujung ke ujung yang mengamankan komunikasi antara rekan-rekan.


Dengan menggabungkan komponen-komponen ini, Pears memungkinkan pembuatan aplikasi yang otonom, terenkripsi, dan terdistribusi, di mana setiap pengguna secara aktif berpartisipasi dalam jaringan. Arsitektur terdesentralisasi ini menghilangkan biaya infrastruktur, risiko penyensoran, dan SPOF (*Single Points of Failure*).


Pears dikembangkan oleh Holepunch, sebuah perusahaan yang didirikan oleh Mathias Buus dan Paolo Ardoino (CEO Tether dan CTO Bitfinex), dengan misi memperluas logika peer-to-peer di luar Bitcoin. Ambisi mereka adalah untuk membangun "*Internet of peers*," di mana setiap aplikasi dapat beroperasi tanpa izin, tanpa server, dan tanpa perantara. Holepunch sudah berada di belakang **Keet**, sebuah aplikasi konferensi video dan perpesanan yang sepenuhnya P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Tutorial instalasi Pears ini dibagi menjadi beberapa bagian, tergantung pada sistem operasi Anda. Langsung ke bagian yang sesuai dengan lingkungan Anda untuk mengikuti petunjuk yang sesuai:*



- Linux (Debian)** → Bagian **2**
- Windows** → Bagian **3**
- macOS** → Bagian **4**


## 2. Bagaimana cara menginstal Pears di Linux (Debian)?


Menginstal Pears di Debian relatif sederhana tetapi membutuhkan beberapa prasyarat, yang akan kami jelaskan di bagian ini.


### 2.1. Memperbarui sistem


Sebelum melakukan hal lain, penting untuk memastikan sistem Anda sudah diperbarui.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Menginstal dependensi


Pears bergantung pada beberapa pustaka sistem, termasuk `libatomic1`, yang digunakan oleh mesin runtime Bare JavaScript. Instal dengan perintah berikut:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instal Node.js dan npm melalui NVM


Pears didistribusikan melalui *npm*, manajer paket *Node.js*. Meskipun Pears tidak secara langsung bergantung pada *Node.js* untuk berjalan, namun diperlukan untuk instalasi. Cara yang direkomendasikan untuk menginstal *Node.js* di Linux adalah melalui *NVM* (*Node Version Manager*), yang memungkinkan Anda untuk mengelola beberapa versi Node secara berdampingan.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Kemudian, muat ulang terminal Anda untuk mengaktifkan *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Periksa apakah *NVM* telah terinstal dengan benar:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Selanjutnya, instal versi stabil dari *Node.js* (misalnya, versi LTS saat ini):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Pastikan bahwa *Node.js* dan *npm* telah terinstal dengan benar:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Instal Pir dengan npm


Setelah *npm* tersedia, Anda dapat menginstal Pears CLI secara global pada sistem Anda. Hal ini memungkinkan Anda untuk menjalankan perintah `pear` dari direktori manapun.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inisialisasi Pir


Setelah instalasi, cukup jalankan perintah berikut di terminal Anda:


```bash
pear
```


Saat pertama kali diluncurkan, Pears akan terhubung ke jaringan peer-to-peer untuk mengunduh komponen yang diperlukan. Proses ini tidak bergantung pada server pusat - file-file diambil langsung dari rekan-rekan lainnya.


![Image](assets/fr/10.webp)


Setelah pengunduhan selesai, jalankan perintah sekali lagi untuk mengonfirmasi bahwa semuanya sudah berfungsi:


```bash
pear
```


![Image](assets/fr/11.webp)


Jika semuanya sudah terinstal dengan benar, menu bantuan Pears akan muncul dengan daftar perintah yang tersedia.


### 2.6. Uji Pir dengan Keet


Untuk memverifikasi bahwa Pears telah beroperasi penuh, Anda dapat meluncurkan aplikasi P2P yang tersedia di jaringan, seperti Keet, perangkat lunak pesan dan konferensi video sumber terbuka yang dikembangkan oleh Holepunch.


```bash
pear run pear://keet
```


Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa menggunakan server pusat. Jika Keet diluncurkan dengan benar, itu berarti instalasi Pears Anda berfungsi penuh.


![Image](assets/fr/12.webp)


Sistem Linux Anda sekarang siap untuk menjalankan dan menghosting aplikasi peer-to-peer dengan Pears.


## 3. Cara Memasang Pir di Windows


Menginstal Pears di Windows sama mudahnya dengan di Linux, tetapi membutuhkan beberapa alat khusus.


*Jika Anda menggunakan Linux dan telah menginstal Pears, Anda dapat langsung melompat ke **Langkah 5**.*


### 3.1. Buka PowerShell sebagai Administrator


Pertama, luncurkan PowerShell dengan hak istimewa administrator:



- Klik pada menu Start (Mulai);
- Ketik "PowerShell";
- Klik kanan pada "*Windows PowerShell*";
- Pilih "*Jalankan sebagai administrator*".


![Image](assets/fr/15.webp)


### 3.2. Unduh NVS


Pears diinstal melalui *npm*, manajer paket *Node.js*. Pada Windows, metode yang direkomendasikan oleh Holepunch adalah menggunakan *NVS* (*Node Version Switcher*), yang lebih stabil daripada *NVM* pada sistem ini.


Di PowerShell, jalankan perintah berikut untuk menginstal versi terbaru *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Instal Node.js


Setelah instalasi, mulai ulang PowerShell, lalu masukkan perintah berikut:


```powershell
nvs
```


Anda akan melihat daftar versi *Node.js* yang tersedia. Pilih yang pertama dengan menekan tombol `a` pada papan ketik Anda.


![Image](assets/fr/17.webp)


*Node.js* sekarang sudah terinstal.


![Image](assets/fr/18.webp)


### 3.4. Verifikasi Instalasi


Pastikan *Node.js* dan *npm* dapat diakses:


```powershell
node -v
npm -v
```


Kedua perintah tersebut akan mengembalikan nomor versi.


![Image](assets/fr/19.webp)


### 3.5. Instal Pir dengan npm


Setelah *Node.js* dan *npm* tersedia, instal **Pears CLI** secara global di sistem Anda:


```powershell
npm install -g pear
```


Ini akan menginstal biner `pear` di direktori global *npm* Anda.


![Image](assets/fr/20.webp)


### 3.6. Verifikasi dan Inisialisasi Pir


Setelah instalasi selesai, jalankan:


```powershell
pear
```


Saat pertama kali diluncurkan, Pears akan secara otomatis mengunduh komponen yang diperlukan dari jaringan peer-to-peer. Proses ini mungkin memerlukan waktu beberapa saat.


![Image](assets/fr/21.webp)


Jika semuanya berjalan dengan baik, Anda akan melihat menu bantuan Pears CLI dengan daftar subperintah yang tersedia (run, seed, info...).


### 3.7. Uji Pir dengan Keet


Untuk memverifikasi bahwa Pears telah beroperasi penuh, Anda dapat meluncurkan aplikasi P2P yang tersedia di jaringan, seperti Keet - perangkat lunak perpesanan dan konferensi video sumber terbuka yang dikembangkan oleh Holepunch.


```bash
pear run pear://keet
```


Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa menggunakan server pusat. Jika Keet berhasil diluncurkan, itu berarti instalasi Pears Anda telah berfungsi penuh.


![Image](assets/fr/22.webp)


Sistem Windows Anda sekarang siap untuk menjalankan dan meng-host aplikasi peer-to-peer dengan Pears.


## 4. Cara Memasang Pir di macOS


Menginstal Pears di macOS mirip dengan Linux, tetapi memerlukan beberapa penyesuaian khusus untuk lingkungan Apple. Mari kita bahas langkah-langkah ini bersama-sama.


*Jika Anda menggunakan Linux atau Windows dan telah menginstal Pears, Anda dapat langsung melompat ke **Langkah 5**.*


### 4.1. Periksa Prasyarat Sistem


Sebelum instalasi, pastikan *Xcode Command Line Tools* sudah terinstal di sistem Anda. Paket ini menyediakan alat bantu pembuatan yang diperlukan untuk *Node.js* dan ketergantungannya.


Untuk melakukannya, buka terminal menggunakan pintasan `Cmd + Spasi`, ketik `Terminal`, dan tekan `Enter`. Kemudian, jalankan perintah berikut ini di terminal untuk menginstalnya:


```bash
xcode-select --install
```


Jika alat sudah terinstal di sistem Anda, macOS akan memberi tahu Anda.


### 4.2. Instal NVM


Pears didistribusikan melalui *npm*, manajer paket *Node.js*. Meskipun Pears tidak secara langsung bergantung pada *Node.js* untuk berfungsi, namun diperlukan untuk instalasi. Metode yang direkomendasikan untuk menginstal *Node.js* di macOS adalah *NVM* (*Node Version Manager*), yang memungkinkan Anda untuk mengelola beberapa versi Node secara bersamaan.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Kemudian muat ulang terminal Anda untuk mengaktifkan *NVM*:


```bash
source ~/.zshrc
```


Jika Anda menggunakan *bash* dan bukan *zsh*, jalankan:


```bash
source ~/.bashrc
```


Selanjutnya, periksa apakah *NVM* telah terinstal dengan benar:


```bash
nvm --version
```


Terminal Anda akan menampilkan versi *NVM* yang terinstal.


### 4.3. Instal Node.js dan npm


Selanjutnya, instal versi stabil dari *Node.js* (misalnya, versi LTS saat ini):


```bash
nvm install --lts
```


Setelah penginstalan selesai, verifikasi versi yang diinstal:


```bash
node -v
npm -v
```


Kedua perintah tersebut akan mengembalikan nomor versi.


### 4.4. Instal Pir dengan npm


Setelah *npm* tersedia, Anda dapat menginstal Pears CLI secara global pada sistem Anda. Hal ini akan memungkinkan Anda untuk mengeksekusi perintah `pear` dari direktori manapun.


```bash
npm install -g pear
```


### 4.5. Inisialisasi Pir


Setelah instalasi, cukup jalankan perintah berikut di terminal Anda:


```bash
pear
```


Saat pertama kali diluncurkan, Pears terhubung ke jaringan peer-to-peer untuk mengunduh komponen yang diperlukan. Proses ini tidak memerlukan server pusat - file diambil langsung dari peer lainnya.


Setelah pengunduhan selesai, jalankan kembali perintah untuk memverifikasi bahwa semuanya berfungsi:


```bash
pear
```


Jika semuanya sudah terinstal dengan benar, menu bantuan Pears akan muncul dengan daftar perintah yang tersedia.


### 4.6. Uji Pir dengan Keet


Untuk memverifikasi bahwa Pears telah beroperasi penuh, Anda bisa meluncurkan aplikasi P2P yang sudah tersedia di jaringan, seperti Keet, perangkat lunak perpesanan dan konferensi video sumber terbuka dari Holepunch.


```bash
pear run pear://keet
```


Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa menggunakan server pusat. Jika Keet berhasil diluncurkan, itu berarti instalasi Pears Anda telah berfungsi penuh.


Sistem macOS Anda sekarang siap untuk menjalankan dan menghosting aplikasi peer-to-peer dengan Pears.


## 5. Cara Menggunakan Plan ₿ Academy on Pears


Setelah Pears terinstal dan berjalan, Anda bisa langsung meluncurkan platform **Plan ₿ Academy** melalui jaringan P2P. Cukup jalankan perintah berikut ini di terminal Anda (perintah yang sama dapat digunakan di Linux, Windows, dan macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Setelah pemuatan selesai, Plan ₿ Academy akan terbuka di lingkungan Pears Anda, siap digunakan seperti situs web aslinya - tetapi tanpa ketergantungan pada server pusat.


![Image](assets/fr/14.webp)


## 6. Cara Membuat Rencana Pembibitan ₿ Akademi Pir


Dalam jaringan Pears, untuk *seed* sebuah aplikasi berarti mendistribusikannya ke rekan-rekan lain dari komputer Anda sendiri. Dalam praktiknya, ketika Anda menggunakan seed Plan ₿ Academy, komputer Anda menjadi sumber data yang memungkinkan pengguna lain mengunduh aplikasi tanpa bergantung pada server pusat.


Mekanisme ini memperkuat ketahanan dan ketahanan sensor dari aplikasi kami di jaringan Pears. Semakin banyak peer seed sebuah aplikasi, maka aplikasi tersebut akan semakin tersedia dan terdesentralisasi, bahkan jika beberapa node asli offline.


Untuk membantu mendistribusikan Plan ₿ Academy, cukup jalankan perintah berikut:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Selama perintah ini tetap aktif, perangkat Anda akan berpartisipasi dalam mendistribusikan file aplikasi. Jika Anda menutup terminal, proses berbagi akan berhenti.


Untuk melanjutkan penyemaian setelah memulai ulang, Anda dapat menjalankan perintah di latar belakang atau membuat layanan sistem - misalnya, layanan systemd di Linux, LaunchAgent di macOS, atau tugas terjadwal di Windows. Metode-metode ini memastikan bahwa aplikasi Plan ₿ Academy secara otomatis melanjutkan penyemaian pada saat sistem dimulai.


Terima kasih telah berkontribusi pada distribusi desentralisasi Plan ₿ Academy on Pears dan membantu membuat pendidikan Bitcoin benar-benar tahan sensor!