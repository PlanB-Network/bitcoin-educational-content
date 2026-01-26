---
name: Alby

description: Ekstensi browser untuk Bitcoin dan Lightning Network
---

![cover](assets/cover.webp)




Melakukan pembayaran yang semakin mudah dengan bitcoin adalah tantangan yang dihadapi banyak perusahaan di sektor ini. Alby menonjol dari yang lain dengan ekstensi Alby wallet untuk peramban. Ekstensi ini bertujuan untuk menyiapkan kerangka kerja yang lancar yang secara otomatis mendeteksi alamat dan memungkinkan Anda untuk melakukan pembayaran bitcoin tanpa gesekan. Dalam tutorial ini, kita akan mempelajari ekstensi Alby dan menguji bagaimana ekstensi ini memfasilitasi pembayaran dari browser.




![video](https://youtu.be/nd5fX2vHuDw)




## Perpanjangan Alby



Ekstensi Alby adalah alat yang memungkinkan peramban web Anda berinteraksi dengan mudah dan aman dengan jaringan Bitcoin dan lapisan Lightning Network. Hal ini ditandai dengan tiga aspek:




- Lightning Network wallet: Tautkan node atau akun Alby Anda untuk mengirim dan menerima bitcoin dengan cepat dan murah melalui lapisan Lightning Network.
- Pembayaran lancar melalui Web: Ini menghilangkan kebutuhan untuk memindai kode QR atau beralih di antara aplikasi untuk pembayaran bitcoin di situs web yang mendukung Lightning. Ini memungkinkan transaksi yang lancar dengan satu klik, atau tanpa konfirmasi jika Anda telah menetapkan anggaran.
- Manajer Nostr: Ekstensi ini mengelola kunci Nostr Anda, membuatnya mudah untuk terhubung dan berinteraksi dengan aplikasi Nostr yang bertindak sebagai penandatangan yang aman tanpa mengekspos kunci pribadi Anda ke setiap platform.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Sambungkan ke ekstensi



Dalam tutorial ini, kita akan menggunakan ekstensi Alby di peramban Firefox dalam sistem operasi Ubuntu. Namun, ekstensi ini juga tersedia di Windows dan peramban seperti Chrome.



Anda dapat menambahkan ekstensi Alby ke browser Anda dengan mengunjungi toko ekstensi [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) atau toko ekstensi [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Sangat penting untuk memeriksa bahwa pembuat ekstensi tersebut adalah akun resmi Alby, untuk menghindari segala bentuk pembajakan atau pencurian bitcoin Anda.



Tambahkan ekstensi ke browser Anda dengan mengeklik tombol di sebelah kanan.


Berikan izin yang diperlukan untuk menginstal dan menggunakan ekstensi, lalu sematkan ekstensi ke bilah alat agar mudah diambil.



![pin](assets/fr/03.webp)



Anda juga harus menentukan kode pembuka kunci (sangat penting), yang akan menjamin akses yang aman ke Lightning wallet dari browser Anda. Kami sarankan Anda menetapkan kata sandi alfanumerik yang kuat.



ℹ️ Simpan kata sandi ini di tempat yang aman agar Anda dapat mengaksesnya jika lupa, karena kata sandi ini dapat diubah tetapi tidak dapat diambil kembali.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby menunjukkan kemampuannya beradaptasi dengan menawarkan dua pilihan kepada Anda:




- Lanjutkan dengan akun Alby jika Anda ingin menikmati aplikasi sambil tetap mengontrol bitcoin Anda.
- Hubungkan wallet atau Lightning node Anda sendiri jika Anda sudah memilikinya dan didukung oleh ekstensi.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Dalam tutorial ini, kami memilih untuk melanjutkan dengan akun Alby untuk memanfaatkan fitur-fitur ekosistem Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Masuk ke akun Alby Anda, atau buat akun jika Anda belum memilikinya.



![signup](assets/fr/05.webp)



## Melakukan pembayaran pertama Anda



Setelah masuk, Anda bisa mengklik ekstensi Alby di toolbar untuk mengakses portofolio Anda.



![buzzin](assets/fr/06.webp)



Setelah Anda membuat akun Alby, Anda harus menghubungkannya ke wallet untuk membelanjakan satoshi. Untuk menghubungkan bitcoin wallet ke akun Alby Anda, kami sarankan Anda menggunakan node Alby Hub, yang bisa Anda siapkan di komputer Anda atau berlangganan paket yang ditawarkan oleh Alby.



![hubplan](assets/fr/13.webp)




Dalam tutorial ini, akun Alby kami didukung oleh instalasi lokal pada mesin kami.


Untuk membuat node Alby Anda sendiri, kami merekomendasikan tutorial Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Node ini memungkinkan Anda membuat portofolio Lightning kustodian mandiri dan mengelola saluran Lightning secara efisien untuk mengirim dan menerima satoshi.



![channels](assets/fr/14.webp)



Buka saluran penerimaan yang menentukan jumlah total satoshi yang dapat Anda terima.



![receivechanal](assets/fr/15.webp)



Buka saluran pengiriman dengan memblokir satoshi pada alamat onchain bitcoin. Satoshi yang Anda blokir menentukan total satoshi yang dapat Anda belanjakan.



![spend](assets/fr/16.webp)



Anda sekarang dapat mengirim dan menerima satoshi melalui ekstensi Alby.



![exchange](assets/fr/08.webp)



Mulai saat ini dan seterusnya, ekstensi Alby dapat mendeteksi alamat dan faktur Lightning yang tersedia di halaman web yang Anda kunjungi, dan akan menyarankan agar Anda membayarnya dengan bitcoin atau Lightning langsung dari ekstensi Anda.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Mengamankan kunci pemulihan dengan kunci utama



Kunci utama yang ditawarkan oleh ekstensi Alby bertindak sebagai lapisan pelindung yang memungkinkan Anda untuk berkomunikasi secara aman dengan lapisan jaringan utama Bitcoin (Onchain), sistem Nostr dan memungkinkan Anda untuk mengaktifkan koneksi Lightning dengan aplikasi Nostr.



![masterKey](assets/fr/11.webp)



Kunci utama ini berbentuk 12 kata yang mirip dengan frasa pemulihan Anda. Oleh karena itu, kami menyarankan agar Anda menyimpannya menggunakan metode yang aman untuk memastikan bahwa kunci tersebut dapat diakses kapan saja.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Sekarang Anda dapat merasakan pembayaran bitcoin dan Lightning tanpa gesekan dengan ekstensi Alby. Jika Anda menikmati tutorial ini, kami merekomendasikan tutorial Alby Hub kami untuk menyiapkan node Alby Anda sendiri dan mengontrol semua aspek dompet Alby Anda dari antarmuka yang halus dan kuat.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a