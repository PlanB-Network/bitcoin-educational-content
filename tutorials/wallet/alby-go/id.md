---
name: Alby

description: Ekstensi browser untuk Bitcoin dan Lightning Network
---

![cover](assets/cover.webp)




Melakukan pembayaran yang semakin mudah dengan bitcoin adalah tantangan yang dihadapi banyak perusahaan di sektor ini. Alby menonjol dari yang lain lewat ekstensi wallet Alby untuk peramban. Ekstensi ini bertujuan menyiapkan kerangka kerja yang lancar dengan secara otomatis mendeteksi alamat dan memungkinkan kamu melakukan pembayaran bitcoin tanpa gesekan. Dalam tutorial ini, kita akan mempelajari ekstensi Alby dan menguji bagaimana ekstensi ini memfasilitasi pembayaran langsung dari browser.





![video](https://youtu.be/nd5fX2vHuDw)




## Perpanjangan Alby



Ekstensi Alby adalah alat yang memungkinkan peramban web kamu berinteraksi dengan mudah dan aman dengan jaringan Bitcoin dan lapisan Lightning Network. Hal ini ditandai oleh tiga aspek:




- Lightning Network wallet: Tautkan node atau akun Alby kamu untuk mengirim dan menerima Bitcoin dengan cepat dan murah melalui lapisan Lightning Network.
- Pembayaran lancar melalui web: Ini menghilangkan kebutuhan untuk memindai kode QR atau berpindah antar aplikasi saat melakukan pembayaran Bitcoin di situs web yang mendukung Lightning. Kamu bisa melakukan transaksi dengan lancar hanya dengan satu klik, atau bahkan tanpa konfirmasi jika kamu sudah menetapkan anggaran.
- Manajer Nostr: Ekstensi ini mengelola kunci Nostr kamu, sehingga memudahkan kamu untuk terhubung dan berinteraksi dengan aplikasi Nostr. Ekstensi ini bertindak sebagai penandatangan yang aman tanpa mengekspos kunci privat kamu ke setiap platform.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Sambungkan ke ekstensi



Dalam tutorial ini, kita akan menggunakan ekstensi Alby di peramban Firefox pada sistem operasi Ubuntu. Namun, ekstensi ini juga tersedia di Windows dan peramban lain seperti Chrome.



Kamu dapat menambahkan ekstensi Alby ke browser kamu dengan mengunjungi toko ekstensi.
 [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) atau toko ekstensi [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Sangat penting untuk memastikan bahwa pembuat ekstensi tersebut adalah akun resmi Alby, guna menghindari segala bentuk pembajakan atau pencurian bitcoin kamu.

Tambahkan ekstensi ke browser kamu dengan mengeklik tombol di sebelah kanan.

Berikan izin yang diperlukan untuk menginstal dan menggunakan ekstensi, lalu sematkan ekstensi ke bilah alat agar mudah diakses.




![pin](assets/fr/03.webp)



Kamu juga harus menentukan kode pembuka kunci (sangat penting), yang akan menjamin akses yang aman ke Lightning wallet dari browser kamu. Kami menyarankan kamu menetapkan kata sandi alfanumerik yang kuat.

ℹ️ Simpan kata sandi ini di tempat yang aman agar kamu dapat mengaksesnya jika lupa, karena kata sandi ini dapat diubah tetapi tidak dapat dipulihkan.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby menunjukkan fleksibilitasnya dengan menawarkan dua pilihan kepada kamu:

- Lanjutkan dengan akun Alby jika kamu ingin menggunakan aplikasi ini sambil tetap mengontrol bitcoin kamu.
- Hubungkan wallet atau Lightning node milikmu sendiri jika kamu sudah memilikinya dan wallet tersebut didukung oleh ekstensi ini.




https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Dalam tutorial ini, kami memilih untuk melanjutkan dengan akun Alby untuk memanfaatkan fitur-fitur ekosistem Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Masuk ke akun Alby Anda, atau buat akun jika Anda belum memilikinya.



![signup](assets/fr/05.webp)



## Melakukan pembayaran pertama



Setelah masuk, kamu bisa mengklik ekstensi Alby di toolbar untuk mengakses portofolio kamu.



![buzzin](assets/fr/06.webp)



Setelah kamu membuat akun Alby, kamu perlu menghubungkannya ke wallet agar bisa membelanjakan satoshi. Untuk menghubungkan bitcoin wallet ke akun Alby kamu, kami menyarankan kamu menggunakan node Alby Hub, yang bisa kamu siapkan di komputer kamu sendiri atau dengan berlangganan paket yang ditawarkan oleh Alby.



![hubplan](assets/fr/13.webp)




Dalam tutorial ini, akun Alby kami didukung oleh instalasi lokal pada mesin kami.

Untuk membuat node Alby kamu sendiri, kami merekomendasikan tutorial Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Node ini memungkinkan kamu membuat portofolio Lightning kustodian mandiri dan mengelola saluran Lightning secara efisien untuk mengirim dan menerima satoshi.



![channels](assets/fr/14.webp)



Buka saluran penerimaan yang menentukan total jumlah satoshi yang dapat kamu terima.



![receivechanal](assets/fr/15.webp)


Buka saluran pengiriman dengan mengunci satoshi pada alamat on-chain Bitcoin. Satoshi yang kamu kunci menentukan total satoshi yang dapat kamu belanjakan.



![spend](assets/fr/16.webp)



Kamu sekarang dapat mengirim dan menerima satoshi melalui ekstensi Alby.



![exchange](assets/fr/08.webp)



Mulai saat ini, ekstensi Alby dapat mendeteksi alamat dan invoice Lightning yang tersedia di halaman web yang kamu kunjungi, lalu menyarankan kamu untuk membayarnya dengan Bitcoin atau Lightning langsung dari ekstensi kamu.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Mengamankan kunci pemulihan dengan kunci utama



Kunci utama yang ditawarkan oleh ekstensi Alby bertindak sebagai lapisan pelindung yang memungkinkan kamu berkomunikasi secara aman dengan lapisan jaringan utama Bitcoin (on-chain), sistem Nostr, serta mengaktifkan koneksi Lightning dengan aplikasi Nostr.




![masterKey](assets/fr/11.webp)



Kunci utama ini berbentuk 12 kata yang mirip dengan seedphrase kamu. Oleh karena itu, kami menyarankan kamu menyimpannya menggunakan metode yang aman agar kunci tersebut dapat diakses kapan saja.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Sekarang kamu dapat merasakan pembayaran Bitcoin dan Lightning tanpa gesekan dengan ekstensi Alby. Jika kamu menikmati tutorial ini, kami merekomendasikan tutorial Alby Hub untuk menyiapkan node Alby kamu sendiri dan mengontrol semua aspek wallet Alby kamu dari antarmuka yang halus dan kuat.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
