---
name: Pir
description: Bagaimana cara menginstal dan menggunakan aplikasi di Pears?
---

![cover](assets/cover.webp)



Dalam tutorial ini, kita akan belajar cara menjalankan aplikasi di **Pears**, sebuah teknologi peer-to-peer (P2P) yang dikembangkan oleh **Holepunch** dan didukung oleh **Tether**. Tujuannya sederhana: untuk memungkinkan pendistribusian dan penggunaan aplikasi web tanpa bergantung pada infrastruktur terpusat (tidak ada server, tidak ada host, tidak ada perantara). Dengan kata lain, meskipun penyedia cloud tutup atau suatu negara memblokir sebuah domain, aplikasi tetap hidup di antara rekan-rekan jaringan.



## 1. Apa itu Pir?



Pears adalah lingkungan runtime, alat pengembangan, dan platform penyebaran untuk aplikasi peer-to-peer. Alat sumber terbuka ini memungkinkan untuk membangun, berbagi, dan menjalankan perangkat lunak tanpa server atau infrastruktur, secara langsung di antara para pengguna. Secara konkret, ini berarti bahwa alih-alih meng-host aplikasi di server pusat, setiap pengguna menjadi simpul jaringan, berbagi bagian dari aplikasi dan data dengan rekan-rekan lainnya. Keseluruhan sistem membentuk jaringan terdistribusi, dengan setiap contoh bekerja sama untuk menjaga agar layanan tetap dapat diakses.



![Image](assets/fr/01.webp)



Pendekatan ini didasarkan pada seperangkat batu bata perangkat lunak modular yang dikembangkan oleh Holepunch:




- Hypercore**: log terdistribusi yang menjamin konsistensi dan keamanan data tanpa basis data pusat.
- Hyperbee**: pengindeks di atas Hypercore, untuk pengaturan dan penelusuran data yang efisien.
- Hyperdrive**: sistem file terdistribusi yang digunakan untuk menyimpan dan menyinkronkan file aplikasi di antara sesama.
- Hyperswarm** dan **HyperDHT**: lapisan jaringan yang memungkinkan penemuan dan koneksi antara rekan-rekan di seluruh dunia, tanpa server pusat.
- Secretstream**: protokol enkripsi E2E untuk mengamankan pertukaran antara dua rekan.



Dengan menggabungkan komponen-komponen ini, Pears memungkinkan untuk membuat aplikasi yang otonom, terenkripsi, dan terdistribusi, di mana setiap pengguna secara aktif berpartisipasi dalam jaringan. Arsitektur terdesentralisasi ini menghilangkan biaya infrastruktur, risiko penyensoran, dan SPOF (*Single Point of Failure*).



## 2. Asal mula dan filosofi proyek



Pears dikembangkan oleh Holepunch, sebuah perusahaan yang didirikan oleh Mathias Buus dan Paolo Ardoino (CEO Tether dan CTO Bitfinex), dengan misi memperluas logika peer-to-peer di luar Bitcoin. Ambisi mereka adalah membangun "Internet Peer-to-Peer", di mana setiap aplikasi dapat berjalan tanpa otorisasi, tanpa server, dan tanpa perantara. Holepunch sudah berada di belakang **Keet**, sebuah aplikasi konferensi video dan pesan yang sepenuhnya P2P.



*Tutorial instalasi Pears ini dibagi menjadi beberapa bagian tergantung pada sistem operasi Anda. Langsung saja ke bagian yang sesuai dengan lingkungan Anda untuk mengikuti instruksi yang sesuai :*




- Linux (Debian)** → Bagian **3**
- Windows** → Bagian **4**
- macOS** → Bagian **5**



## 3. Cara menginstal Pears di Linux (Debian)



Menginstal Pir pada sistem Debian relatif mudah, tetapi membutuhkan beberapa prasyarat, yang akan kami jelaskan di bagian ini.



### 3.1. memperbarui sistem



Pertama dan terpenting, penting untuk memastikan sistem Anda sudah diperbarui.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. Instal dependensi



Pears bergantung pada pustaka sistem tertentu, terutama `libatomic1`, yang digunakan oleh Bare JavaScript runtime. Instal dengan perintah berikut:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. Instal Node.js dan npm melalui NVM



Pears didistribusikan melalui *npm*, manajer paket *Node.js*. Meskipun Pears tidak bergantung secara langsung pada *Node.js* untuk berfungsi, namun tetap diperlukan untuk instalasi. Metode yang direkomendasikan untuk menginstal *Node.js* di Linux adalah *NVM* (*Node Version Manager*), yang memungkinkan Anda untuk mengelola beberapa versi Node secara paralel.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Kemudian muat ulang terminal Anda untuk mengaktifkan *NVM*:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Periksa apakah *NVM* telah terinstal:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Kemudian instal versi stabil dari *Node.js* (mis. LTS saat ini):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Periksa instalasi *Node.js* dan *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Menginstal Pir dengan npm



Setelah *npm* tersedia, Anda dapat menginstal Pears CLI secara global pada sistem Anda. Hal ini akan memungkinkan Anda untuk menjalankan perintah `pear` dari direktori manapun.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Inisialisasi Pir



Setelah instalasi, cukup jalankan perintah berikut di terminal Anda:



```bash
pear
```



Saat pertama kali dijalankan, Pears akan terhubung ke jaringan peer-to-peer untuk mengunduh komponen yang diperlukan. Proses ini tidak memerlukan server pusat: file diperoleh secara langsung dari rekan-rekan lainnya.



![Image](assets/fr/10.webp)



Setelah pengunduhan selesai, jalankan perintah lagi untuk memeriksa apakah semuanya berfungsi:



```bash
pear
```



![Image](assets/fr/11.webp)



Jika semuanya sudah terinstal dengan benar, Pears Help akan ditampilkan dengan daftar perintah yang tersedia.



### 3.6. Menguji Pir dengan Keet



Untuk memeriksa apakah Pears sudah beroperasi penuh, Anda bisa meluncurkan aplikasi P2P yang sudah tersedia di jaringan, seperti Keet, perangkat lunak perpesanan dan konferensi video sumber terbuka dari Holepunch.



```bash
pear run pear://keet
```



Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa melalui server pusat. Jika Keet diluncurkan dengan benar, instalasi Pears Anda sudah berfungsi penuh.



![Image](assets/fr/12.webp)



Sistem Linux Anda sekarang siap untuk menjalankan dan menghosting aplikasi peer-to-peer dengan Pears.



## 4. Cara memasang Pears di Windows



Menginstal Pears di Windows sama mudahnya dengan di Linux, tetapi membutuhkan beberapa alat khusus.



*Jika Anda menggunakan Linux, Anda dapat langsung ke langkah 6.*



### 4.1. buka PowerShell dalam mode administrator



Pertama-tama, jalankan PowerShell dengan hak administrator :




- Klik pada menu Start (Mulai);
- Ketik PowerShell ;
- Klik kanan pada "*Windows PowerShell*" ;
- Pilih "*Jalankan sebagai administrator*".



![Image](assets/fr/15.webp)



### 4.2. Unduh NVS



Pears diinstal melalui *npm*, manajer paket *Node.js*. Pada Windows, metode yang direkomendasikan oleh Holepunch adalah menggunakan *NVS* (*Node Version Switcher*), yang lebih stabil daripada *NVM* pada sistem ini.



Di PowerShell, jalankan perintah berikut untuk menginstal versi terbaru *NVS*:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Instal Node.js



Setelah instalasi, mulai ulang PowerShell dan masukkan perintah berikut:



```powershell
nvs
```



Anda akan melihat daftar versi *Node.js* yang tersedia. Pilih yang pertama dengan menekan tombol `a` pada papan ketik Anda.



![Image](assets/fr/17.webp)



*Node.js* telah terinstal.



![Image](assets/fr/18.webp)



### 4.4. Periksa instalasi



Pastikan *Node.js* dan *npm* dapat diakses:



```powershell
node -v
npm -v
```



Kedua perintah tersebut harus mengembalikan nomor versi.



![Image](assets/fr/19.webp)



### 4.5. Menginstal Pir dengan npm



Setelah *Node.js* dan *npm* tersedia, instal *Pears CLI* secara global di sistem Anda:



```powershell
npm install -g pear
```



Ini akan menginstal biner `pear` di direktori global *npm* Anda.



![Image](assets/fr/20.webp)



### 4.6. Periksa dan inisialisasi Pir



Setelah instalasi selesai, jalankan :



```powershell
pear
```



Saat pertama kali diluncurkan, Pears akan secara otomatis mengunduh komponen yang diperlukan dari jaringan peer-to-peer. Proses ini mungkin memerlukan waktu beberapa saat.



![Image](assets/fr/21.webp)



Jika semua berjalan dengan baik, Anda akan melihat layar bantuan CLI Pears dengan daftar sub-perintah yang tersedia (run, seed, info...).



### 4.7. Menguji Pir dengan Keet



Untuk memeriksa apakah Pears sudah beroperasi penuh, Anda bisa meluncurkan aplikasi P2P yang sudah tersedia di jaringan, seperti Keet, perangkat lunak perpesanan dan konferensi video sumber terbuka dari Holepunch.



```bash
pear run pear://keet
```



Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa melalui server pusat. Jika Keet diluncurkan dengan benar, instalasi Pears Anda sudah berfungsi penuh.



![Image](assets/fr/22.webp)



Sistem Windows Anda sekarang siap untuk menjalankan dan meng-host aplikasi peer-to-peer dengan Pears.



## 5. Bagaimana cara menginstal Pears di macOS?



Menginstal Pears di macOS mirip dengan menginstalnya di Linux, tetapi memerlukan beberapa penyesuaian khusus untuk lingkungan Apple. Mari kita pelajari langkah-langkah ini bersama-sama.



*Jika Anda menggunakan Linux atau Windows dan telah menginstal Pears, Anda dapat langsung melanjutkan ke **langkah 6**.*



### 5.1. Periksa persyaratan sistem



Sebelum menginstal, pastikan bahwa *Xcode Command Line Tools* ada di sistem Anda. Paket ini menyediakan alat kompilasi yang diperlukan untuk _Node.js_ dan dependensinya.



Untuk melakukannya, buka terminal dengan pintasan keyboard `Cmd + Spasi`, lalu ketik `Terminal` dan tekan tombol `Enter`. Anda kemudian dapat memasukkan perintah ini di terminal untuk meluncurkan instalasi:



```bash
xcode-select --install
```



Jika alat ini sudah terinstal di sistem Anda, macOS akan memberi tahu Anda.



### 5.2. Instal NVM



Pears didistribusikan melalui *npm*, manajer paket *Node.js*. Meskipun Pears tidak bergantung secara langsung pada *Node.js* untuk berfungsi, namun tetap diperlukan untuk instalasi. Metode yang direkomendasikan untuk menginstal *Node.js* di macOS adalah *NVM* (*Node Version Manager*), yang memungkinkan Anda untuk mengelola beberapa versi Node secara paralel.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Kemudian muat ulang terminal Anda untuk mengaktifkan *NVM*:



```bash
source ~/.zshrc
```



Jika Anda menggunakan *bash* dan bukan *zsh*, jalankan :



```bash
source ~/.bashrc
```



Kemudian periksa apakah *NVM* sudah terinstal:



```bash
nvm --version
```



Terminal akan mengembalikan versi *NVM* yang terinstal pada sistem Anda.



### 5.3. Instal Node.js dan npm



Kemudian instal versi stabil dari *Node.js* (mis. LTS saat ini):



```bash
nvm install --lts
```



Setelah penginstalan selesai, periksa versi yang diinstal:



```bash
node -v
npm -v
```



Kedua perintah tersebut harus mengembalikan nomor versi.



### 5.4 Menginstal Pir dengan npm



Setelah *npm* tersedia, Anda dapat menginstal Pears CLI secara global pada sistem Anda. Hal ini akan memungkinkan Anda untuk menjalankan perintah `pear` dari direktori manapun.



```bash
npm install -g pear
```



### 5.5. Inisialisasi Pir



Setelah instalasi, cukup jalankan perintah berikut di terminal Anda:



```bash
pear
```



Saat pertama kali dijalankan, Pears akan terhubung ke jaringan peer-to-peer untuk mengunduh komponen yang diperlukan. Proses ini tidak memerlukan server pusat: file diperoleh secara langsung dari rekan-rekan lainnya.



Setelah pengunduhan selesai, jalankan perintah lagi untuk memeriksa apakah semuanya berfungsi:



```bash
pear
```



Jika semuanya sudah terinstal dengan benar, Pears Help akan ditampilkan dengan daftar perintah yang tersedia.



### 5.6. Menguji Pir dengan Keet



Untuk memeriksa apakah Pears sudah beroperasi penuh, Anda bisa meluncurkan aplikasi P2P yang sudah tersedia di jaringan, seperti Keet, perangkat lunak perpesanan dan konferensi video sumber terbuka dari Holepunch.



```bash
pear run pear://keet
```



Perintah ini memuat aplikasi Keet secara langsung dari jaringan Pears, tanpa melalui server pusat. Jika Keet diluncurkan dengan benar, instalasi Pears Anda sudah berfungsi penuh.



Sistem macOS Anda sekarang siap untuk menjalankan dan menghosting aplikasi peer-to-peer dengan Pears.



## 6. Bagaimana cara menggunakan aplikasi di Pears?



Setelah Pears aktif dan berjalan, Anda dapat menjalankan aplikasi pilihan Anda secara langsung dengan perintah berikut:



```bash
pear run pear://[KEY]
```



Cukup ganti `[KEY]` dengan kunci aplikasi yang ingin Anda gunakan.



![Image](assets/fr/13.webp)



Untuk mempelajari cara menjalankan platform Plan ₿ Academy kami di Pears, lihat tutorial komprehensif ini:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Dan untuk mengetahui cara menggunakan aplikasi perpesanan Keet yang baru saja Anda luncurkan di Pears, lihat tutorial ini:



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b