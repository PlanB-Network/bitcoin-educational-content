---
name: BitBox02

description: Pengaturan dan penggunaan BitBox02
---

![cover](assets/cover.webp)

BitBox02 (https://bitbox.swiss/) adalah dompet fisik buatan Swiss yang dirancang khusus untuk mengamankan Bitcoin Anda. Beberapa fitur utamanya termasuk cadangan dan pemulihan yang mudah menggunakan kartu microSD, desain minimalis dan diskrit, serta dukungan komprehensif untuk Bitcoin.

![device](assets/1.webp)

Dompet ini menawarkan keamanan terdepan yang dirancang oleh para ahli, menampilkan desain chip ganda yang mencakup chip aman. Kode sumbernya telah diaudit sepenuhnya oleh peneliti keamanan dan sepenuhnya open-source. BitBox02 dilengkapi dengan BitBoxApp yang sederhana namun kuat, yang menyediakan manajemen Bitcoin yang aman. Mendukung node penuh untuk Bitcoin dan memastikan komunikasi yang dienkripsi dari ujung ke ujung antara aplikasi dan perangkat. Diproduksi di Swiss, BitBox02 telah mendapatkan reputasi positif di antara penggunanya.

![video](https://youtu.be/sB4b2PbYaj0)

> Spesifikasi
>
> - Konektivitas: USB-C
> - Kompatibilitas: Windows 7 dan lebih baru, macOS 10.13 dan lebih baru, Linux, Android
> - Input: Sensor sentuh kapasitif
> - Mikrokontroler: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; Generator nomor acak sejati
> - Chip aman: ATECC608B; Generator nomor acak sejati (NIST SP 800-90A/B/C)
> - Tampilan: OLED putih 128 x 64 px
> - Material: Polikarbonat
> - Ukuran: 54.5 x 25.4 x 9.6 mm termasuk colokan USB-C
> - Berat: Perangkat 12g; dengan kemasan dan aksesori 160g

Unduh lembar data di situs web mereka https://bitbox.swiss/bitbox02/

## Cara Menggunakan Dompet Perangkat Keras BitBox02

### Mengatur BitBox02

BitBox02 memiliki koneksi USB-C yang terpasang pada casing. Jika komputer Anda menggunakan port USB biasa, Anda harus menggunakan adaptor yang disertakan dengan perangkat.

Sambungkan ke komputer Anda dan perangkat akan menyala (jangan lakukan itu sekarang).

Perangkat ini memiliki sensor di atas dan bawah, dan akan meminta Anda untuk menyentuh bagian atas atau bawah untuk mengorientasikan layar sesuai yang Anda inginkan.

![image](assets/2.webp)

### Unduh Aplikasi BitBox02

Kunjungi https://shiftcrypto.ch/ dan klik pada tautan "App" di bagian atas untuk menuju ke halaman unduhan:

![image](assets/3.webp)

Klik tombol Unduh biru:

![image](assets/4.webp)

Untuk memverifikasi unduhan (ini menambah kompleksitas, tetapi disarankan, terutama jika Anda menyimpan banyak bitcoin), lihat Lampiran A.

Setelah unduhan, Anda dapat mengekstrak file. Di Mac, cukup klik ganda file yang diunduh, dan ikon Aplikasi BitBox akan muncul di direktori unduhan Anda. Anda dapat menyeretnya ke desktop (atau di mana saja) untuk akses yang mudah.

Klik ganda Aplikasi untuk menjalankannya (tidak perlu "diinstal").

Di Mac, pengawas komputer Anda akan memberi Anda peringatan. Abaikan saja dan klik "buka":

![image](assets/5.webp)

Anda kemudian akan melihat ini:

![image](assets/6.webp)

Lanjutkan dan sambungkan perangkat ke komputer.

Perangkat akan menampilkan kode pasangan. Periksa apakah mereka cocok, lalu sentuh sensor untuk memilih tanda centang. Kemudian kembali ke layar, tombol lanjutkan akan tersedia untuk Anda.

![image](assets/7.webp)
Anda kemudian akan memiliki opsi untuk membuat seed baru, atau mengembalikan seed. Saya akan menunjukkan cara membuat seed baru (Penting juga untuk mengembalikan seed yang Anda buat untuk menguji kualitas cadangan Anda, sebelum Anda memuat bitcoin apa pun ke dalam dompet).

![image](assets/8.webp)

Perangkat ini dilengkapi dengan kartu microSD. Silakan masukkan jika Anda belum melakukannya.

![image](assets/9.webp)

Namai perangkat Anda dan klik lanjutkan, kemudian konfirmasi di perangkat.

![image](assets/10.webp)

Anda kemudian akan diminta untuk menetapkan kata sandi untuk perangkat. Ini bukan bagian dari seed Anda. Ini juga bukan passphrase (itu bagian dari seed Anda). Ini hanyalah kata sandi untuk mengunci perangkat. Ketika Anda menyalakan perangkat, Anda akan diminta untuk memasukkan kata sandi ini setiap kali. Anda memiliki 10 kegagalan berturut-turut yang diizinkan sebelum perangkat akan menghapus semua memorinya, jadi berhati-hatilah. Animasi di layar akan mengajarkan Anda cara menggunakan kontrol perangkat untuk menetapkan kata sandi.

![image](assets/11.webp)

Baca layar berikutnya, dan centang setiap kotak, lalu lanjutkan.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

Dan inilah tampilan dompet setelah siap digunakan.

![image](assets/15.webp)

### TUNGGU DULU!!

Cukup aneh, tapi BitBox02 memberi tahu kami kami siap menggunakan perangkat, tetapi belum meminta kami untuk menuliskan kata-kata seed! SATU-SATUNYA cadangan yang kami miliki adalah file yang disimpan ke kartu microSD. Ini tidak cukup. Perangkat penyimpanan ini tidak bertahan selamanya (karena "bit rot"). Kami memerlukan cadangan kertas, dan duplikatnya, disimpan di brankas (seperti dijelaskan dalam panduan umum cara menggunakan dompet perangkat keras)

Untuk mendapatkan frasa seed Anda dan menuliskannya, pergi ke tab "manage device" di sebelah kiri, lalu klik "show recover words"

![image](assets/16.webp)

Anda kemudian dapat melalui konfirmasi, dan perangkat akan menampilkan kata-katanya. Tulislah dengan rapi, dan jangan biarkan siapa pun melihat kata-katanya.

![image](assets/17.webp)

Setelah itu, Anda dapat mengklik tab Bitcoin di sebelah kiri untuk mendapatkan alamat penerimaan Anda.

![image](assets/18.webp)

Ini menampilkan satu per satu, tetapi setidaknya memungkinkan Anda memilih alamat mana yang akan digunakan dari 20 pertama:

![image](assets/19.webp)

Mengklik tombol biru akan menampilkan alamat lengkap, dan Anda akan diminta untuk memeriksa apakah alamat cocok dengan tampilan di layar. Ini adalah praktik yang baik untuk mengonfirmasi bahwa tidak ada malware di komputer Anda yang menipu Anda untuk mengirim bitcoin ke alamat penyerang.

![image](assets/20.webp)

Untuk mengirim bitcoin ke dompet ini, Anda dapat menyalin alamat dan menempelkannya ke halaman penarikan dari bursa tempat koin Anda berada. Saya sarankan Anda mengirim jumlah kecil terlebih dahulu, kemudian berlatih menghabiskannya kembali ke bursa atau ke alamat kedua di dompet Anda.

Untuk jumlah yang lebih besar, saya sarankan Anda membuat passphrase (lihat di bawah). Dompet asli (tanpa passphrase) dapat digunakan sebagai dompet umpan Anda (perlu memiliki jumlah yang wajar di dalamnya agar menjadi umpan yang meyakinkan).

### Terhubung ke node

BitBox02 akan secara otomatis terhubung ke sebuah node. Mari kita lihat ke mana ia terhubung. Klik pada tab pengaturan di sebelah kiri, lalu "connect your own full node".

![image](assets/21.webp)
Dan di sini kita dapat melihat itu terhubung ke node shiftcrypto. Tidak bagus. Kita telah mengkhianati semua alamat bitcoin kita kepada mereka, dan alamat IP kita (tentu saja bukan seed; mereka dapat melihat alamat/saldo kita, tetapi tidak dapat menggunakannya). Kita dapat memasukkan detail node kita sendiri di halaman ini (di luar cakupan panduan khusus ini), atau kita dapat menggunakan perangkat lunak yang lebih baik seperti Sparrow Bitcoin Wallet, Electrum Desktop Wallet, atau Specter Desktop. Saya akan mendemonstrasikan Sparrow Bitcoin Wallet nanti dalam panduan.

![image](assets/22.webp)

Tambahkan passphrase

Sekarang setelah kita telah mengatur perangkat dengan Aplikasi BitBox02 (dan mengungkapkan alamat kita, tidak dapat dihindari dengan dompet perangkat keras khusus ini), kita dapat menambahkan passphrase ke frasa seed kita. Ini akan memungkinkan kita untuk membuat dompet baru menggunakan seed yang sama, dan ShiftCrypto tidak akan pernah melihat alamat baru kita. Kita akan menghubungkan dompet ini hanya ke perangkat lunak kita sendiri.

### Aktifkan Passphrase

Lanjutkan sekarang dan "aktifkan" fitur passphrase (tetapi kita belum menyetel passphrase). Pergi ke tab "manage device", dan klik pada "enable passphrase" (lingkaran merah di bawah).

![image](assets/23.webp)

Baca melalui langkah-langkahnya...

![image](assets/24.webp)
![image](assets/25.webp)
![image](assets/26.webp)

Sekarang lepaskan perangkat, dan matikan Aplikasi BitBox02

AKHIR dari bagian bitbox02 oleh Parman.

Perangkat Anda sekarang sepenuhnya operasional untuk digunakan pada solusi desktop apa pun seperti specter, sparrow dan menggunakan antarmuka bitbox.