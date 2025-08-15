---
name: BitBox02

description: Pengaturan dan penggunaan BitBox02
---

![cover](assets/cover.webp)

BitBox02 (https://bitbox.swiss/) adalah dompet fisik buatan Swiss yang dirancang khusus untuk mengamankan Bitcoinmu. Beberapa fitur utamanya termasuk cadangan dan pemulihan yang mudah menggunakan kartu microSD, desain minimalis dan diskrit, serta dukungan komprehensif untuk Bitcoin.

![device](assets/1.webp)

Dompet ini menawarkan keamanan terdepan yang dirancang oleh para ahli, dengan desain chip ganda yang mencakup secure chip. Kode sumbernya sepenuhnya open-source dan telah diaudit secara menyeluruh oleh peneliti keamanan. BitBox02 dilengkapi BitBoxApp yang sederhana namun kuat untuk pengelolaan Bitcoin yang aman, mendukung node penuh, dan memastikan komunikasi terenkripsi end-to-end antara aplikasi dan perangkat. Diproduksi di Swiss, BitBox02 telah mendapatkan reputasi positif di kalangan penggunanya.

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

BitBox02 dilengkapi konektor USB-C yang terpasang pada casing-nya. Kalau komputer kamu hanya punya port USB-A, gunakan adaptor yang sudah disertakan di dalam paket.

Sambungkan ke komputer mu dan perangkat akan menyala (jangan lakukan itu sekarang).

Perangkat ini punya sensor di bagian atas dan bawah, dan akan memintamu menyentuh salah satu sisinya untuk mengatur orientasi layar sesuai yang kamu mau.

![image](assets/2.webp)

### Unduh Aplikasi BitBox02

Kunjungi https://shiftcrypto.ch/ dan klik pada tautan "App" di bagian atas untuk menuju ke halaman unduhan:

![image](assets/3.webp)

Klik tombol Unduh biru:

![image](assets/4.webp)

Untuk memverifikasi unduhan (ini menambah kompleksitas, tetapi disarankan, terutama jika kamu menyimpan banyak bitcoin), lihat Lampiran A.

Setelah diunduh, kamu bisa mengekstrak filenya. Di Mac, cukup klik ganda file yang sudah diunduh, lalu ikon aplikasi BitBox akan muncul di folder unduhan kamu. Kamu bisa menyeretnya ke desktop (atau ke lokasi lain) supaya lebih mudah diakses.

Klik ganda Aplikasi untuk menjalankannya (tidak perlu "diinstal").

Di Mac, pengawas komputermu akan memberi Anda peringatan. Abaikan saja dan klik "buka":

![image](assets/5.webp)

Kemudian kamu akan melihat ini:

![image](assets/6.webp)

Lanjutkan dan sambungkan perangkat ke komputer.

Perangkat akan menampilkan kode pasangan. Cek apakah kodenya cocok, lalu sentuh sensor untuk memilih tanda centang. Setelah itu, kembali ke layar, dan tombol lanjutkan akan muncul untuk kamu.

![image](assets/7.webp)
Kamu kemudian akan punya opsi untuk membuat seed baru atau memulihkan seed. Aku akan menunjukkan cara membuat seed baru. (Penting juga untuk mencoba memulihkan seed yang kamu buat, untuk mengetes kualitas cadanganmu sebelum kamu memuat bitcoin apa pun ke dalam dompet.)

![image](assets/8.webp)

Perangkat ini dilengkapi dengan kartu microSD. Silakan masukkan jika kamu belum melakukannya.

![image](assets/9.webp)

Beri nama perangkatmu lalu klik lanjutkan, kemudian konfirmasi di perangkat.

![image](assets/10.webp)

Kamu kemudian akan diminta untuk membuat kata sandi untuk perangkat. Ini bukan bagian dari seed kamu, dan juga bukan passphrase (yang memang bagian dari seed). Kata sandi ini hanya berfungsi untuk mengunci perangkat. Setiap kali kamu menyalakan perangkat, kamu akan diminta memasukkan kata sandi ini. Kamu punya 10 kali percobaan gagal berturut-turut sebelum perangkat menghapus semua memorinya, jadi hati-hati. Animasi di layar akan menunjukkan cara menggunakan kontrol perangkat untuk membuat kata sandi.

![image](assets/11.webp)

Baca layar berikutnya, dan centang setiap kotak, lalu lanjutkan.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

Dan inilah tampilan dompet setelah siap digunakan.

![image](assets/15.webp)

### TUNGGU DULU!!

Cukup aneh, BitBox02 memberi tahu kita bahwa kita sudah siap menggunakan perangkat, tapi belum meminta kita menuliskan kata-kata seed! SATU-SATUNYA cadangan yang kita punya hanyalah file yang tersimpan di kartu microSD. Ini tidak cukup. Media penyimpanan seperti ini tidak akan bertahan selamanya (karena bit rot). Kita perlu membuat cadangan di kertas, lengkap dengan duplikatnya, lalu simpan di brankas (seperti yang dijelaskan di panduan umum penggunaan dompet perangkat keras).

Untuk mendapatkan frasa seed kamu dan menuliskannya, buka tab "manage device" di sebelah kiri, lalu klik "show recovery words"

![image](assets/16.webp)

Kamu kemudian bisa masuk ke tahap konfirmasi, dan perangkat akan menampilkan kata-katanya. Tulis dengan rapi, dan jangan biarkan siapa pun melihat kata-kata tersebut.

![image](assets/17.webp)

Setelah itu, kamu bisa klik tab Bitcoin di sebelah kiri untuk mendapatkan alamat penerimaanmu.

![image](assets/18.webp)

Tampilannya memang satu per satu, tapi setidaknya kamu bisa memilih alamat mana yang mau dipakai dari 20 alamat pertama.

![image](assets/19.webp)

Mengklik tombol biru akan menampilkan alamat lengkap, dan kamu akan diminta memeriksa apakah alamat tersebut sama dengan yang ada di layar perangkat. Ini adalah langkah yang baik untuk memastikan tidak ada malware di komputermu yang menipumu agar mengirim bitcoin ke alamat milik penyerang.

![image](assets/20.webp)

Untuk mengirim bitcoin ke dompet ini, kamu bisa menyalin alamatnya lalu menempelkannya di halaman penarikan dari bursa tempat koinmu berada. Aku sarankan kirim jumlah kecil terlebih dahulu, lalu coba berlatih mengirimnya kembali ke bursa atau ke alamat kedua di dompetmu.

Untuk jumlah yang lebih besar, aku sarankan kamu membuat passphrase (lihat bagian di bawah). Dompet asli (tanpa passphrase) bisa kamu gunakan sebagai dompet umpan, yang sebaiknya berisi jumlah wajar agar terlihat meyakinkan.

### Terhubung ke node

BitBox02 akan otomatis terhubung ke sebuah node. Mari kita lihat ke mana perangkat ini terhubung. Klik tab pengaturan di sebelah kiri, lalu pilih "connect your own full node".

![image](assets/21.webp)
Dan di sini kita bisa lihat kalau perangkat ini terhubung ke node ShiftCrypto. Nggak bagus. Kita sudah membocorkan semua alamat bitcoin kita ke mereka, beserta alamat IP kita (tentu saja bukan seed; mereka bisa melihat alamat dan saldo kita, tapi nggak bisa menggunakannya). Kita bisa memasukkan detail node kita sendiri di halaman ini (di luar cakupan panduan khusus ini), atau memakai perangkat lunak yang lebih baik seperti Sparrow Bitcoin Wallet, Electrum Desktop Wallet, atau Specter Desktop. Aku akan mendemonstrasikan penggunaan Sparrow Bitcoin Wallet nanti di panduan ini.

![image](assets/22.webp)

Tambahkan passphrase

Sekarang, setelah kita mengatur perangkat dengan Aplikasi BitBox02 (dan membocorkan alamat kita — hal yang nggak bisa dihindari dengan dompet perangkat keras ini), kita bisa menambahkan passphrase ke frasa seed kita. Ini akan memungkinkan kita membuat dompet baru dengan seed yang sama, dan ShiftCrypto tidak akan pernah melihat alamat baru kita. Dompet ini nanti akan kita hubungkan hanya ke perangkat lunak milik kita sendiri.

### Aktifkan Passphrase

Sekarang lanjutkan dan aktifkan fitur passphrase (tapi kita belum akan menyetelnya). Buka tab "manage device", lalu klik "enable passphrase" (lingkaran merah di bawah).

![image](assets/23.webp)

Baca melalui langkah-langkahnya...

![image](assets/24.webp)
![image](assets/25.webp)
![image](assets/26.webp)

Sekarang lepaskan perangkat, dan matikan Aplikasi BitBox02

AKHIR dari bagian bitbox02 oleh Parman.

Perangkatmu sekarang sepenuhnya operasional untuk digunakan pada solusi desktop apa pun seperti specter, sparrow dan menggunakan antarmuka bitbox.
