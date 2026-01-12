---
name: Ashigaru Terminal
description: Gunakan Ashigaru di desktop untuk membuat koin bersama
---

![cover](assets/cover.webp)



Ashigaru Terminal adalah adaptasi tim Ashigaru dari Sparrow Server yang mengimplementasikan protokol coinjoin Whirlpool. Perangkat lunak ini merupakan kelanjutan dari pekerjaan yang dimulai oleh Samourai Wallet, khususnya pada Whirlpool GUI, dengan mengadopsi prinsip-prinsip dasarnya: penjagaan keamanan dan kerahasiaan.

Perangkat lunak ini merupakan fork dari Sparrow Server yang dimodifikasi dan dioptimalkan untuk integrasi penuh dengan ekosistem Whirlpool, yaitu protokol coinjoin ZeroLink yang awalnya dikembangkan oleh tim Samourai.

Ashigaru Terminal beroperasi melalui antarmuka TUI yang minimalis dan dapat digunakan di komputer pribadi maupun di server khusus. Terminal ini memungkinkan kamu berinteraksi langsung dengan Whirlpool untuk memulai akun "Tx0", mengelola akun "*Deposit*", "*Premix*", "*Postmix*", dan "*Badbank*", serta melakukan remix otomatis untuk memperkuat kerahasiaan bagian kamu.

Singkatnya, Ashigaru Terminal akan sangat berguna jika kamu ingin membuat koin bersama menggunakan Whirlpool.

Dalam tutorial pertama ini, aku akan memandu kamu melalui proses instalasi dan pengoperasian Ashigaru Terminal. Tutorial kedua yang lebih lanjut akan dikhususkan untuk proses pembuatan koin yang sebenarnya.


https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Pasang Terminal Ashigaru



Untuk menginstal Ashigaru Terminal, Anda membutuhkan Tor Browser, karena binari hanya didistribusikan melalui jaringan Tor. Jika Anda belum melakukannya, [instal di komputer Anda](https://www.torproject.org/download/).



### 1.1. Unduh Terminal Ashigaru



Dari Tor Browser, buka [halaman rilis repositori Git mereka](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) untuk mengunduh versi terbaru Ashigaru Terminal untuk sistem operasi Anda.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Unduh 2 file berikut ini untuk sistem operasi kamu:




- Biner (`ashigaru_terminal_v1.0.0_amd64.deb` untuk Debian/Ubuntu, `.dmg` untuk macOS atau `.zip` untuk Windows);
- File hash yang ditandatangani: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Periksa Terminal Ashigaru



Sebelum menjalankan perangkat lunak pada perangkat kamu, kamu perlu memeriksa keaslian dan integritasnya. Ini merupakan langkah penting, karena mencegah kamu menginstal versi palsu yang dapat membahayakan bitcoin atau merusak mesin.



Buka tab browser baru dan buka [Alat verifikasi Keybase](https://keybase.io/verify). Rekatkan isi file `.txt` yang baru saja kamu unduh ke dalam bidang yang tersedia, lalu klik tombol `Verify`.



![Image](assets/fr/02.webp)



Untuk mendiversifikasi sumber verifikasi, kamu juga dapat membandingkan pesan tersebut dengan pesan yang tersedia di situs clearnet [ashigaru.rs](https://ashigaru.rs/download/), di bagian `/download`.



![Image](assets/fr/03.webp)



Jika tanda tangan tersebut valid, Keybase akan menampilkan pesan yang mengonfirmasi bahwa file tersebut telah ditandatangani oleh pengembang Ashigaru.



![Image](assets/fr/04.webp)



Kamu juga dapat mengklik profil `ashigarudev` yang ditampilkan oleh Keybase dan memeriksa apakah sidik jarinya sama persis dengan sidik jari kunci mereka: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Jika muncul kesalahan pada tahap ini, tanda tangan tidak valid. Dalam kasus ini, **jangan menginstal perangkat lunak yang diunduh**. Mulai lagi dari awal, atau mintalah bantuan komunitas sebelum melanjutkan.



Keybase telah memberikan kamu hash terotentikasi dari aplikasi tersebut. Sekarang kita akan memeriksa apakah hash dari file `.deb`, `.zip`, atau `.dmg` yang telah kamu unduh sesuai dengan yang tervalidasi di Keybase. Untuk melakukan hal ini, buka [HASH FILE ONLINE](https://hash-file.online/).



Klik tombol `BROWSE...` dan pilih file `.deb`, `.zip`, atau `.dmg` yang telah diunduh pada langkah 1.1. Kemudian pilih fungsi hash `SHA-256`, dan klik `HITUNG HASH` untuk meng-generate hash file Anda.



![Image](assets/fr/06.webp)



Situs ini kemudian akan menampilkan hash perangkat lunak. Bandingkan dengan hash yang kamu verifikasi pada Keybase.io. Jika keduanya cocok dengan sempurna, pemeriksaan keaslian dan integritas telah berhasil. Kamu kemudian dapat menggunakan perangkat lunak tersebut.



![Image](assets/fr/07.webp)



### 1.3 Peluncuran Terminal Ashigaru





- Debian / Ubuntu



Untuk menginstal perangkat lunak, jalankan perintah :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Ubah urutan sesuai dengan versi yang diunduh.



Kemudian periksa pemasangannya:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Kemudian luncurkan perangkat lunak:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Klik kanan pada file `.zip` yang telah kamu unduh dan periksa, lalu pilih `Extract All...` untuk mengekstrak isinya.



Setelah ekstraksi selesai, klik dua kali pada file `Ashigaru-terminal.exe` untuk meluncurkan perangkat lunak.



![Image](assets/fr/08.webp)



## 2. Memulai dengan Terminal Ashigaru



Ashigaru Terminal adalah program TUI (*Text-based User Interface*), yaitu antarmuka minimalis yang berjalan langsung di terminal. Kamu berinteraksi dengannya menggunakan menu dan pintasan keyboard, tetapi tanpa lingkungan grafis klasik yang sesungguhnya.



![Image](assets/fr/09.webp)



Sangat mudah digunakan: gunakan tombol panah pada keyboard kamu untuk menavigasi menu, dan tekan tombol `Enter` untuk memvalidasi tindakan atau mengonfirmasi pilihan.



## 3. Menghubungkan node Anda ke Terminal Ashigaru



Secara default, Ashigaru Terminal terhubung ke server Electrum publik. Hal ini jelas menimbulkan risiko dalam hal kerahasiaan dan kedaulatan. Jadi kita akan mengonfigurasinya agar terhubung langsung ke Electrum Server milik kamu sendiri.


Untuk melakukannya, buka menu `Preferensi > Server`.



![Image](assets/fr/10.webp)



Klik tombol `< Edit >`.



![Image](assets/fr/11.webp)



Pilih `Private Electrum Server`, lalu klik `<Lanjutkan>`.



![Image](assets/fr/12.webp)



Masukkan URL dan port server kamu. Kamu dapat menentukan alamat Tor dalam `.onion`. Kemudian klik `< Test >` untuk memverifikasi koneksi.



![Image](assets/fr/13.webp)



Jika koneksi berhasil, pesan `Sukses` akan muncul, bersama dengan rincian server kamu.



![Image](assets/fr/14.webp)



Jika kamu belum memiliki node Bitcoin, aku sarankan kamu mengikuti kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Dalam kasus kamu, untuk tutorial ini, aku akan memutuskan koneksi dari server Electrs kamu karena saya sedang mengerjakan testnet. Namun, pengoperasiannya tetap sama persis pada mainnet.*



## 4. Buat portofolio di Terminal Ashigaru



Setelah perangkat lunak dikonfigurasikan dengan benar, kita dapat menambahkan portofolio Bitcoin.



Kamu memiliki dua pilihan:




- Kamu dapat membuat wallet baru dari awal dan menggunakannya secara eksklusif di Ashigaru Terminal. Dalam hal ini, kamu harus membuka perangkat lunak ini setiap kali ingin berinteraksi dengan wallet kamu;

- Sebagai alternatif, kamu dapat mengimpor wallet Ashigaru yang sudah ada langsung dari ponsel kamu ke Ashigaru Terminal. Kekurangan metode ini adalah sedikit mengurangi keamanan pengaturan kamu, karena wallet kamu akan terpapar pada dua lingkungan yang berisiko, bukan hanya satu. Di sisi lain, metode ini menawarkan keuntungan karena kamu dapat membiarkan Ashigaru Terminal berjalan terus menerus untuk mencampur koin kamu, sekaligus memungkinkan kamu membelanjakannya dari jarak jauh melalui aplikasi seluler Ashigaru.

Dalam tutorial ini, kita akan memilih metode kedua. Namun, jika kamu lebih memilih membuat wallet yang benar-benar baru, prosedurnya tetap sama: satu-satunya perbedaan ada pada tahap pembuatan, ketika kamu harus menyimpan seedphrase baru dan passphrase baru kamu.

Perlu juga diperhatikan bahwa Ashigaru Terminal tidak memungkinkan kamu membelanjakan bitcoin secara langsung. Kamu dapat menyinkronkan wallet yang sama di Ashigaru Terminal dan aplikasi Ashigaru (yang akan aku lakukan dalam tutorial ini), atau di Sparrow Wallet.

Jika kamu belum memiliki wallet di aplikasi Ashigaru, kamu dapat mengikuti tutorial khusus berikut:


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Buka menu `Dompet`.



![Image](assets/fr/15.webp)



Kemudian pilih `Buat / pulihkan wallet...`. Opsi `Open Wallet...` memungkinkan Anda mengakses portofolio yang telah disimpan di Ashigaru Terminal di kemudian hari.



![Image](assets/fr/16.webp)



Berikan nama pada portofolio kamu.



![Image](assets/fr/17.webp)



Kemudian pilih tipe portofolio `Hot Wallet`.






![Image](assets/fr/18.webp)



Pada tahap inilah prosedurnya berbeda, tergantung pada pilihan awal kamu:




- Jika kamu ingin membuat portofolio baru dari awal, klik `<Generate New Wallet>`, tentukan passphrase BIP39, lalu simpan frasa mnemonik dan passphrase Anda dengan hati-hati pada media fisik;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Jika kamu ingin menggunakan wallet yang sama dengan aplikasi Ashigaru, masukkan 12 kata dari seedphrase kamu dan passphrase BIP39 kamu langsung ke kolom yang sesuai. Tuliskan kata-kata tersebut dalam huruf kecil, lengkap, berurutan, dipisahkan oleh spasi, tanpa angka atau karakter tambahan.



Setelah langkah ini selesai, klik `< Next >`.



*Catatan*: Jika kamu tidak dapat mengeklik tombol ini, seedphrase kamu tidak valid. Periksa dengan cermat bahwa tidak ada kata yang salah atau salah eja.



![Image](assets/fr/19.webp)



Kamu kemudian perlu mengatur kata sandi. Kata sandi ini akan digunakan untuk membuka kunci wallet Ashigaru Terminal dan melindunginya dari akses fisik yang tidak sah. Kata sandi ini tidak terlibat dalam proses derivasi kriptografi kunci kamu. Dengan kata lain, bahkan tanpa kata sandi ini, siapa pun yang memiliki seedphrase dan passphrase tetap dapat memulihkan wallet kamu dan mengakses bitcoin kamu.

Pilih kata sandi yang panjang, rumit, dan acak. Simpan salinannya di tempat yang aman, idealnya di media fisik atau di pengelola kata sandi yang aman.



Klik `< OK >` setelah kamu selesai.



![Image](assets/fr/20.webp)



## 5. Menggunakan portofolio



Kamu kemudian dapat memilih akun mana yang akan diakses. Untuk saat ini, kami belum memulai campuran apa pun, jadi kami akan mengakses akun `Deposit`.



![Image](assets/fr/21.webp)



Pengoperasiannya pun identik dengan Sparrow, karena Terminal Ashigaru adalah fork dari Server Sparrow. Kamu akan menemukan menu yang sama:



![Image](assets/fr/22.webp)





- transaksi": memungkinkanmu untuk melihat riwayat transaksi yang ditautkan ke akun ini. Dalam kasusku, beberapa di antaranya sudah muncul, karena aku sudah membuat beberapa dengan aplikasi Ashigaru pada wallet yang sama.



![Image](assets/fr/23.webp)





- receive`: menghasilkan alamat tanda terima kosong yang baru untuk menempatkan satss di akun deposit.



![Image](assets/fr/24.webp)





- addresses`: menampilkan daftar semua alamat kamu, baik yang termasuk dalam rantai internal maupun eksternal akun kamu.



![Image](assets/fr/25.webp)





- `UTXOs`: daftar semua UTXO yang tersedia.



![Image](assets/fr/26.webp)





- `Settings`: memberikan akses ke *descriptor* portofolio kamu. Kamu juga dapat melihat seed kamu, menyesuaikan *Gap Limit*, atau mengubah tanggal pembuatan wallet kamu.



![Image](assets/fr/27.webp)



Sekarang kamu sudah tahu cara menginstal dan menggunakan Ashigaru Terminal. Dalam tutorial berikutnya, kita akan melihat cara melakukan coinjoin dengan perangkat lunak ini dan cara mengelola dana di "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
