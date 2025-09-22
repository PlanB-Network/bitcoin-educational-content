---
name: BIP-39 Passphrase Trezor
description: Bagaimana cara menambahkan passphrase ke portofolio Trezor saya?
---
![cover](assets/cover.webp)



passphrase BIP39 merupakan kata sandi opsional yang dikombinasikan dengan frasa Mnemonic, memberikan tambahan keamanan Layer untuk portofolio Bitcoin yang bersifat deterministik dan hirarkis. Dalam tutorial ini, kita akan bersama-sama mengetahui cara mengatur passphrase pada Bitcoin Wallet yang aman di Trezor (Safe 3, Safe 5, dan Model One).



![Image](assets/fr/01.webp)



Sebelum memulai tutorial ini, jika Anda belum terbiasa dengan konsep passphrase, cara kerjanya dan implikasinya terhadap Bitcoin Wallet Anda, saya sangat menyarankan agar Anda membaca artikel teoritis lainnya di mana saya menjelaskan semuanya (ini sangat penting, karena menggunakan passphrase tanpa sepenuhnya memahami cara kerjanya dapat membahayakan bitcoin Anda):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase pada Trezor ditangani dengan cara klasik jika Anda memilih standar BIP39 selama konfigurasi (yang saya sarankan jika Anda tidak memerlukan *Cadangan Multi-Bagi*). Yang istimewa dari Trezor adalah Anda bisa memasukkan passphrase secara langsung ke Hardware Wallet, atau melalui keyboard komputer Anda menggunakan perangkat lunak Trezor Suite. Pilihan kedua ini jauh lebih tidak aman, karena komputer memiliki permukaan serangan yang jauh lebih besar daripada Hardware Wallet. Akan tetapi, mengetik passphrase yang rumit mungkin lebih cepat pada keyboard konvensional dibandingkan dengan Hardware Wallet, yang dapat mendorong penggunaan kata sandi yang kuat. Jadi selalu lebih baik menggunakan passphrase, bahkan jika harus diketik, daripada tidak menggunakannya sama sekali. Namun demikian, penting untuk tetap waspada terhadap peningkatan risiko serangan numerik yang diimplikasikan oleh hal ini.



Opsi-opsi ini tidak tersedia pada semua perangkat lunak manajemen portofolio yang kompatibel dengan Trezor. Sebagai contoh, untuk Model One, passphrase dapat dimasukkan melalui keyboard pada Sparrow Wallet. Untuk Model T, Model Safe 3 dan Model Safe 5, Anda harus menggunakan Trezor Suite atau memasukkan passphrase secara langsung pada Hardware Wallet, karena opsi untuk memasukkan melalui Sparrow telah dinonaktifkan oleh HWI beberapa tahun yang lalu.



![Image](assets/fr/02.webp)



Di Trezor Suite, Anda memiliki dua cara berbeda untuk mengelola permintaan passphrase. Anda dapat mengaktifkan opsi "*passphrase*" di tab "*Perangkat*". Jika diaktifkan, Trezor Suite dan semua perangkat lunak manajemen portofolio lainnya akan secara sistematis meminta Anda untuk memasukkan passphrase setiap kali Anda memulai. Jika anda lebih memilih pendekatan yang lebih bijaksana untuk menggunakan passphrase, anda dapat mempertahankan pengaturan pada "*Standard*". Dalam hal ini, Anda harus mengakses menu Hardware Wallet secara manual di sudut kiri atas, dan klik tombol "*+ passphrase*" setiap kali Anda memulainya.



Sebelum memulai tutorial ini, pastikan Anda sudah menginisialisasi Trezor Anda dan membuat frasa Mnemonic. Jika belum, dan Trezor Anda masih baru, ikuti tutorial khusus model yang tersedia di Plan ₿ Network. Setelah Anda menyelesaikan langkah ini, Anda dapat kembali ke tutorial ini.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Menambahkan passphrase ke Safe 3 atau Safe 5



Setelah Anda membuat Wallet, menyimpan Mnemonic, dan mengatur PIN, Anda akan dibawa ke menu beranda Trezor Suite. Di sudut kiri atas, sebuah jendela akan muncul dan meminta Anda untuk mengaktifkan passphrase BIP39.



![Image](assets/fr/03.webp)



Jika jendela ini tidak muncul, Anda harus mengaktifkan opsi "*passphrase*" secara manual di tab pengaturan "*Device*".



![Image](assets/fr/04.webp)



Jendela ini meminta Anda untuk memasukkan passphrase Anda. Pilih passphrase yang kuat dan segera buat cadangan fisik, pada media seperti kertas atau logam. Dalam contoh ini, saya memilih passphrase: `fH3&kL@9mP#2sD5qR!82`. Ini adalah contoh; namun demikian, saya sarankan Anda memilih passphrase yang sedikit lebih panjang. Antara 30 dan 40 karakter akan ideal (seperti kata sandi yang baik).



tentu saja, Anda tidak boleh membagikan passphrase Anda di Internet, seperti yang saya lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.



Untuk rekomendasi yang lebih spesifik mengenai cara memilih passphrase, saya mengundang Anda sekali lagi untuk membaca artikel lain ini:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jika Anda ingin memasukkan passphrase melalui keyboard komputer Anda, masukkan di kolom yang tersedia, lalu klik "*Akses passphrase Wallet*".



![Image](assets/fr/05.webp)



Hardware Wallet Anda kemudian akan menampilkan passphrase Anda. Pastikan bahwa cadangan fisik Anda sudah sesuai (kertas atau logam) sebelum mengklik layar untuk melanjutkan.



![Image](assets/fr/06.webp)



Ini akan memberi Anda akses ke portofolio Anda yang dilindungi passphrase.



![Image](assets/fr/07.webp)



Jika anda lebih memilih untuk meningkatkan keamanan dengan memasukkan passphrase anda hanya pada Trezor anda, ketika diminta, klik "*Masukkan passphrase pada Trezor*".



![Image](assets/fr/08.webp)



Keyboard T9 akan muncul di Trezor Anda, memungkinkan Anda untuk memasukkan passphrase. Setelah Anda menyelesaikan entri Anda, klik tanda centang Green untuk menerapkan passphrase ke Wallet Anda.



![Image](assets/fr/09.webp)



Anda kemudian akan memiliki akses ke passphrase yang aman Wallet.



![Image](assets/fr/10.webp)



Untuk menggunakan Sparrow Wallet, prosedurnya serupa, tetapi untuk model T, Safe 3 dan Safe 5, passphrase harus dimasukkan pada Hardware Wallet dan bukan melalui keyboard komputer.



Kapan pun Sparrow Wallet membutuhkan akses ke Trezor Anda, dan passphrase belum diterapkan sejak start-up terakhir, Anda harus memasukinya menggunakan keyboard T9.



![Image](assets/fr/11.webp)



## Menambahkan passphrase ke Model Satu



Pada Model One, penggunaan passphrase BIP39 hampir tidak dapat dipisahkan. Karena perangkat ini tidak menyertakan Secure Element, maka relatif mudah untuk mengekstrak informasi sensitif. Oleh karena itu, perangkat ini tidak tahan terhadap serangan fisik. Namun, karena passphrase tidak disimpan di perangkat setelah dimatikan, menggunakan passphrase yang kuat (tidak mudah dirusak) dapat melindungi Anda dari sebagian besar serangan fisik yang diketahui pada model ini.



Pada Model One, tidak memungkinkan untuk memasukkan passphrase secara langsung pada Hardware Wallet. Anda harus memasukkannya melalui keyboard komputer Anda.



Setelah Anda membuat Wallet, menyimpan Mnemonic, dan mengatur PIN, Anda akan dibawa ke menu beranda Trezor Suite. Di sudut kiri atas, sebuah jendela yang mengundang Anda untuk mengaktifkan passphrase BIP39 akan muncul.



![Image](assets/fr/12.webp)



Jika jendela ini tidak muncul, Anda harus mengaktifkan opsi "*passphrase*" di tab "*Device*" pada pengaturan.



![Image](assets/fr/13.webp)



Jendela ini meminta Anda untuk memasukkan passphrase Anda. Pilih passphrase yang kuat dan segera buat cadangan fisik, pada media seperti kertas atau logam. Dalam contoh ini, saya memilih passphrase: `fH3&kL@9mP#2sD5qR!82`. Ini hanya sebuah contoh; namun demikian, saya sarankan Anda memilih passphrase yang sedikit lebih panjang. Antara 30 dan 40 karakter akan ideal (seperti kata sandi yang baik).



Untuk rekomendasi yang lebih spesifik mengenai cara memilih passphrase, saya mengundang Anda untuk membaca artikel lain ini:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Masukkan passphrase Anda pada kolom yang tersedia, lalu klik tombol "*Akses passphrase Wallet*".



![Image](assets/fr/14.webp)



Hardware Wallet Anda akan menampilkan passphrase Anda. Pastikan bahwa data tersebut cocok dengan cadangan fisik Anda (kertas atau logam), lalu klik tombol sebelah kanan untuk melanjutkan.



![Image](assets/fr/15.webp)



Ini akan membawa Anda ke portofolio Anda yang dilindungi passphrase.



![Image](assets/fr/16.webp)



Untuk menggunakan Sparrow Wallet setelahnya, prosedurnya tetap sama. Setiap kali Sparrow memerlukan akses ke Hardware Wallet Anda, dan passphrase belum dimasukkan sejak perangkat terakhir kali dinyalakan, Anda harus memasukkannya.



![Image](assets/fr/17.webp)



Selamat, Anda sekarang sudah siap untuk menggunakan passphrase BIP39 pada dompet perangkat keras Trezor. Jika Anda ingin meningkatkan keamanan Wallet Anda selangkah lebih maju, lihat tutorial tentang sistem cadangan *Multi-share* Trezor (*Skema Berbagi Rahasia Shamir*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!