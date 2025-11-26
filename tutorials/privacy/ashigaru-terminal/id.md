---
name: Terminal Ashigaru
description: Gunakan Ashigaru di desktop untuk membuat koin bersama
---

![cover](assets/cover.webp)



Ashigaru Terminal adalah adaptasi tim Ashigaru dari Sparrow Server, yang mengimplementasikan protokol coinjoin Whirlpool. Perangkat lunak ini merupakan kelanjutan dari pekerjaan yang dimulai oleh Samourai Wallet, khususnya pada Whirlpool GUI, yang prinsip-prinsip dasarnya diadopsi: penjagaan keamanan dan kerahasiaan.



Perangkat lunak ini adalah fork dari Sparrow Server, dimodifikasi dan dioptimalkan untuk integrasi penuh dengan ekosistem Whirlpool, protokol coinjoin ZeroLink yang awalnya dikembangkan oleh tim Samourai.



Ashigaru Terminal beroperasi dari antarmuka TUI yang minimalis dan dapat digunakan di komputer pribadi atau di server khusus. Terminal ini memungkinkan Anda berinteraksi langsung dengan Whirlpool untuk memulai akun "*Tx0*", mengelola akun "*Deposit*", "*Premix*", "*Postmix*", dan "*Badbank*", dan melakukan remix otomatis untuk memperkuat kerahasiaan bagian Anda.



Singkatnya, Ashigaru Terminal akan sangat berguna jika Anda ingin membuat koin bersama menggunakan Whirlpool.



Dalam tutorial pertama ini, saya akan memandu Anda melalui instalasi dan pengoperasian Ashigaru Terminal. Tutorial kedua yang lebih lanjut akan dikhususkan untuk pembuatan koin yang sebenarnya.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Pasang Terminal Ashigaru



Untuk menginstal Ashigaru Terminal, Anda membutuhkan Tor Browser, karena binari hanya didistribusikan melalui jaringan Tor. Jika Anda belum melakukannya, [instal di komputer Anda] (https://www.torproject.org/download/).



### 1.1. Unduh Terminal Ashigaru



Dari Tor Browser, buka [halaman rilis repositori Git mereka] (http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) untuk mengunduh versi terbaru Ashigaru Terminal untuk sistem operasi Anda.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Unduh 2 file berikut ini untuk sistem operasi Anda:




- Biner (`ashigaru_terminal_v1.0.0_amd64.deb` untuk Debian/Ubuntu, `.dmg` untuk macOS atau `.zip` untuk Windows);
- File hash yang ditandatangani: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Periksa Terminal Ashigaru



Sebelum menjalankan perangkat lunak pada perangkat Anda, Anda perlu memeriksa keaslian dan integritasnya. Ini merupakan langkah penting, karena mencegah Anda menginstal versi palsu yang dapat membahayakan bitcoin atau menginfeksi mesin Anda.



Buka tab browser baru dan buka [Alat verifikasi Keybase](https://keybase.io/verify). Rekatkan isi file `.txt` yang baru saja Anda unduh ke dalam bidang yang tersedia, lalu klik tombol `Verify`.



![Image](assets/fr/02.webp)



Untuk mendiversifikasi sumber verifikasi Anda, Anda juga dapat membandingkan pesan tersebut dengan pesan yang tersedia di situs clearnet [ashigaru.rs](https://ashigaru.rs/download/), di bagian `/download`.



![Image](assets/fr/03.webp)



Jika tanda tangan valid, Keybase akan menampilkan pesan yang mengonfirmasi bahwa file tersebut telah ditandatangani oleh pengembang Ashigaru.



![Image](assets/fr/04.webp)



Anda juga dapat mengklik profil `ashigarudev` yang ditampilkan oleh Keybase dan memeriksa apakah sidik jarinya sama persis dengan sidik jari kunci mereka: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Jika muncul kesalahan pada tahap ini, tanda tangan tidak valid. Dalam kasus ini, **jangan menginstal perangkat lunak yang diunduh**. Mulai lagi dari awal, atau mintalah bantuan komunitas sebelum melanjutkan.



Keybase telah memberikan Anda hash terotentikasi dari aplikasi tersebut. Sekarang kita akan memeriksa apakah hash dari file `.deb`, `.zip`, atau `.dmg` yang telah Anda unduh sesuai dengan yang tervalidasi di Keybase. Untuk melakukan hal ini, buka [HASH FILE ONLINE](https://hash-file.online/).



Klik tombol `BROWSE...` dan pilih file `.deb`, `.zip`, atau `.dmg` yang telah diunduh pada langkah 1.1. Kemudian pilih fungsi hash `SHA-256`, dan klik `HITUNG HASH` untuk meng-generate hash file Anda.



![Image](assets/fr/06.webp)



Situs ini kemudian akan menampilkan hash perangkat lunak. Bandingkan dengan hash yang Anda verifikasi pada Keybase.io. Jika keduanya cocok dengan sempurna, pemeriksaan keaslian dan integritas telah berhasil. Anda kemudian dapat menggunakan perangkat lunak tersebut.



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



Klik kanan pada file `.zip` yang telah Anda unduh dan periksa, lalu pilih `Extract All...` untuk mengekstrak isinya.



Setelah ekstraksi selesai, klik dua kali pada file `Ashigaru-terminal.exe` untuk meluncurkan perangkat lunak.



![Image](assets/fr/08.webp)



## 2. Memulai dengan Terminal Ashigaru



Ashigaru Terminal adalah program TUI (*Text-based User Interface*), yaitu antarmuka minimalis yang berjalan langsung di terminal. Anda berinteraksi dengannya menggunakan menu dan pintasan keyboard, tetapi tanpa lingkungan grafis klasik yang sesungguhnya.



![Image](assets/fr/09.webp)



Sangat mudah digunakan: gunakan tombol panah pada keyboard Anda untuk menavigasi menu, dan tekan tombol `Enter` untuk memvalidasi tindakan atau mengonfirmasi pilihan.



## 3. Menghubungkan node Anda ke Terminal Ashigaru



Secara default, Terminal Ashigaru terhubung ke server Electrum publik. Hal ini jelas menimbulkan risiko dalam hal kerahasiaan dan kedaulatan. Jadi kita akan mengonfigurasinya untuk terhubung langsung ke Electrum Server Anda sendiri.



Untuk melakukannya, buka menu `Preferensi > Server`.



![Image](assets/fr/10.webp)



Klik tombol `< Edit >`.



![Image](assets/fr/11.webp)



Pilih `Private Electrum Server`, lalu klik `<Lanjutkan>`.



![Image](assets/fr/12.webp)



Masukkan URL dan port server Anda. Anda dapat menentukan alamat Tor dalam `.onion`. Kemudian klik `< Test >` untuk memverifikasi koneksi.



![Image](assets/fr/13.webp)



Jika koneksi berhasil, pesan `Sukses` akan muncul, bersama dengan rincian server Anda.



![Image](assets/fr/14.webp)



Jika Anda belum memiliki node Bitcoin, saya sarankan Anda mengikuti kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Dalam kasus saya, untuk tutorial ini, saya akan memutuskan koneksi dari server Electrs saya karena saya sedang mengerjakan testnet. Namun, pengoperasiannya tetap sama persis pada mainnet.*



## 4. Buat portofolio di Terminal Ashigaru



Setelah perangkat lunak dikonfigurasikan dengan benar, kita dapat menambahkan portofolio Bitcoin.



Anda memiliki dua pilihan:




- Anda dapat membuat wallet baru dari awal dan menggunakannya secara eksklusif di Ashigaru Terminal. Dalam hal ini, Anda harus membuka perangkat lunak ini setiap kali Anda ingin berinteraksi dengan wallet Anda;
- Sebagai alternatif, Anda dapat mengimpor Ashigaru wallet yang sudah ada langsung dari ponsel Anda ke Ashigaru Terminal. Kerugian dari metode ini adalah sedikit mengurangi keamanan pengaturan Anda, karena wallet Anda akan terpapar pada dua lingkungan yang berisiko, bukan hanya satu. Di sisi lain, metode ini menawarkan keuntungan karena Anda dapat membiarkan Ashigaru Terminal berjalan terus menerus untuk mencampur koin Anda, sekaligus memungkinkan Anda untuk membelanjakannya dari jarak jauh melalui aplikasi seluler Ashigaru.



Dalam tutorial ini, kita akan memilih metode kedua. Namun, jika Anda lebih suka membuat portofolio yang sama sekali baru, prosedurnya tetap sama: satu-satunya perbedaan adalah pada saat pembuatan, ketika Anda harus menyimpan frasa mnemonik baru dan passphrase baru Anda.



Perhatikan juga bahwa Ashigaru Terminal tidak memungkinkan Anda membelanjakan bitcoin secara langsung. Anda dapat menyinkronkan dompet yang sama di Ashigaru Terminal dan aplikasi Ashigaru (yang akan saya lakukan dalam tutorial ini), atau di Sparrow Wallet.



Jika Anda belum memiliki wallet pada aplikasi Ashigaru, Anda dapat mengikuti tutorial khusus:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Buka menu `Dompet`.



![Image](assets/fr/15.webp)



Kemudian pilih `Buat / pulihkan wallet...`. Opsi `Open Wallet...` memungkinkan Anda mengakses portofolio yang telah disimpan di Ashigaru Terminal di kemudian hari.



![Image](assets/fr/16.webp)



Berikan nama pada portofolio Anda.



![Image](assets/fr/17.webp)



Kemudian pilih tipe portofolio `Hot Wallet`.






![Image](assets/fr/18.webp)



Pada tahap inilah prosedurnya berbeda, tergantung pada pilihan awal Anda:




- Jika Anda ingin membuat portofolio baru dari awal, klik `<Generate New Wallet>`, tentukan passphrase BIP39, lalu simpan frasa mnemonik dan passphrase Anda dengan hati-hati pada media fisik;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Jika Anda ingin menggunakan wallet yang sama dengan aplikasi Ashigaru Anda, masukkan 12 kata dari frasa mnemonik Anda dan passphrase BIP39 Anda langsung ke dalam kolom yang sesuai. Tuliskan kata-kata dalam huruf kecil, utuh, berurutan, dipisahkan oleh spasi, tanpa angka atau karakter tambahan.



Setelah langkah ini selesai, klik `< Next >`.



*Catatan*: Jika Anda tidak dapat mengeklik tombol ini, frasa mnemonik Anda tidak valid. Periksa dengan cermat bahwa tidak ada kata yang salah atau salah eja.



![Image](assets/fr/19.webp)



Anda kemudian perlu mengatur kata sandi. Kata sandi ini akan digunakan untuk membuka kunci Ashigaru Terminal wallet dan melindunginya dari akses fisik yang tidak sah. Kata sandi ini tidak terlibat dalam derivasi kriptografi dari kunci Anda: dengan kata lain, bahkan tanpa kata sandi ini, siapa pun yang memiliki frasa mnemonik dan passphrase akan dapat memulihkan wallet Anda dan mengakses bitcoin Anda.



Pilih kata sandi yang panjang, rumit, dan acak. Simpan salinannya di tempat yang aman: idealnya di media fisik atau di pengelola kata sandi yang aman.



Klik `< OK >` setelah Anda selesai.



![Image](assets/fr/20.webp)



## 5. Menggunakan portofolio



Anda kemudian dapat memilih akun mana yang akan diakses. Untuk saat ini, kami belum memulai campuran apa pun, jadi kami akan mengakses akun `Deposit`.



![Image](assets/fr/21.webp)



Pengoperasiannya pun identik dengan Sparrow, karena Terminal Ashigaru adalah fork dari Server Sparrow. Anda akan menemukan menu yang sama:



![Image](assets/fr/22.webp)





- transaksi": memungkinkan Anda untuk melihat riwayat transaksi yang ditautkan ke akun ini. Dalam kasus saya, beberapa di antaranya sudah muncul, karena saya sudah membuat beberapa dengan aplikasi Ashigaru pada wallet yang sama.



![Image](assets/fr/23.webp)





- receive`: menghasilkan alamat tanda terima kosong yang baru untuk menempatkan satss di akun deposit.



![Image](assets/fr/24.webp)





- addresses`: menampilkan daftar semua alamat Anda, baik yang termasuk dalam rantai internal maupun eksternal akun Anda.



![Image](assets/fr/25.webp)





- `UTXOs`: daftar semua UTXO yang tersedia.



![Image](assets/fr/26.webp)





- `Settings`: memberikan akses ke *descriptor* portofolio Anda. Anda juga dapat berkonsultasi dengan seed Anda, menyesuaikan *Gap Limit* atau mengubah tanggal pembuatan portofolio Anda.



![Image](assets/fr/27.webp)



Sekarang Anda tahu cara menginstal dan menggunakan Ashigaru Terminal. Dalam tutorial berikutnya, kita akan melihat cara melakukan coinjoin dengan perangkat lunak ini dan cara mengelola dana di "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
