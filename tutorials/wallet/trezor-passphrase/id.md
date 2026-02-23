---
name: BIP-39 Passphrase Trezor
description: Bagaimana cara menambahkan passphrase ke portofolio Trezor saya?
---
![cover](assets/cover.webp)



Passphrase BIP39 adalah kata sandi opsional yang dikombinasikan dengan mnemonic, dan memberi lapisan keamanan tambahan untuk portofolio Bitcoin yang bersifat deterministik dan hierarkis. Dalam tutorial ini, kita akan sama-sama belajar cara mengatur passphrase di Bitcoin wallet yang aman di Trezor (Safe 3, Safe 5, dan Model One).



![Image](assets/fr/01.webp)



Sebelum mulai tutorial ini, kalau kamu belum terbiasa dengan konsep passphrase, cara kerjanya, dan dampaknya ke Bitcoin wallet kamu, aku sangat sarankan kamu baca artikel teoritis lain yang menjelaskan semuanya (ini penting banget, karena pakai passphrase tanpa benar-benar paham bisa berisiko buat bitcoin kamu):

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Passphrase di Trezor ditangani dengan cara klasik kalau kamu pilih standar BIP39 saat konfigurasi (ini yang aku sarankan kalau kamu tidak butuh *Cadangan Multi-Bagi*). Yang unik dari Trezor, kamu bisa memasukkan passphrase langsung ke hardware wallet, atau lewat keyboard komputer menggunakan Trezor Suite. Opsi kedua ini memang lebih tidak aman karena komputer punya permukaan serangan yang lebih luas daripada hardware wallet. Tapi mengetik passphrase yang kompleks biasanya lebih cepat di keyboard biasa dibandingkan di perangkat, dan ini bisa mendorong penggunaan kata sandi yang lebih kuat. Jadi tetap lebih baik pakai passphrase meskipun harus diketik, daripada tidak sama sekali. Namun kamu tetap perlu waspada karena ada peningkatan risiko serangan brute force kalau metode ini dipakai.

Opsi ini tidak selalu tersedia di semua software manajemen portofolio yang kompatibel dengan Trezor. Misalnya, untuk Model One, passphrase bisa dimasukkan lewat keyboard di Sparrow Wallet. Untuk Model T, Model Safe 3, dan Model Safe 5, kamu harus pakai Trezor Suite atau masukkan passphrase langsung di hardware wallet, karena opsi input lewat Sparrow sudah dinonaktifkan oleh HWI beberapa tahun lalu.



![Image](assets/fr/02.webp)



Di Trezor Suite, kamu punya dua cara untuk mengelola permintaan passphrase. Kamu bisa aktifkan opsi "*passphrase*" di tab "*Perangkat*". Kalau diaktifkan, Trezor Suite dan semua software manajemen portofolio lain akan otomatis meminta kamu memasukkan passphrase setiap kali perangkat dihubungkan. Kalau kamu lebih suka pendekatan yang lebih rahasia, kamu bisa biarkan pengaturannya di "*Standard*". Dalam kasus ini, kamu harus masuk ke menu hardware wallet secara manual di sudut kiri atas, lalu klik tombol "*+ passphrase*" setiap kali kamu mau menggunakannya.

Sebelum mulai tutorial ini, pastikan Trezor kamu sudah diinisialisasi dan sudah punya mnemonic. Kalau belum dan perangkat kamu masih baru, ikuti tutorial khusus untuk model tersebut di Plan ₿ Academy. Setelah selesai, kamu bisa kembali ke sini untuk lanjut.



https://planb.academy/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.academy/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Menambahkan passphrase ke Safe 3 atau Safe 5



Setelah kamu membuat wallet, menyimpan mnemonic, dan mengatur PIN, kamu akan diarahkan ke halaman utama Trezor Suite. Di sudut kiri atas, akan muncul jendela yang meminta kamu untuk mengaktifkan passphrase BIP39.


![Image](assets/fr/03.webp)



Jika jendela ini tidak muncul, kamu harus mengaktifkan opsi "*passphrase*" secara manual di tab pengaturan "*Device*".



![Image](assets/fr/04.webp)


Jendela ini meminta kamu memasukkan passphrase. Pilih passphrase yang kuat dan segera buat cadangan fisik, misalnya di kertas atau logam. Dalam contoh ini, aku pakai passphrase: `fH3&kL@9mP#2sD5qR!82`. Ini cuma contoh, tapi aku sarankan kamu pilih passphrase yang lebih panjang. Idealnya antara 30 sampai 40 karakter, seperti kata sandi yang kuat.

Tentu saja, kamu tidak boleh membagikan passphrase kamu di internet, seperti yang aku lakukan di tutorial ini. Contoh wallet ini hanya dipakai di testnet dan akan dihapus di akhir tutorial.

Untuk rekomendasi lebih detail tentang cara memilih passphrase, aku sarankan kamu baca artikel ini:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jika kamu ingin memasukkan passphrase melalui keyboard komputer, masukkan di kolom yang tersedia, lalu klik "*Akses passphrase Wallet*".



![Image](assets/fr/05.webp)



Kemudian Hardware Wallet akan menampilkan passphrase kamu. Pastikan bahwa cadangan fisik kamu sudah sesuai (kertas atau logam) sebelum mengklik layar untuk melanjutkan.



![Image](assets/fr/06.webp)



Ini akan memberi kamu akses ke portofolio kamu yang dilindungi passphrase.



![Image](assets/fr/07.webp)



Kalau kamu lebih memilih meningkatkan keamanan dengan memasukkan passphrase langsung di Trezor saat diminta, klik "*Masukkan passphrase pada Trezor*".


![Image](assets/fr/08.webp)



Keyboard T9 akan muncul di layar Trezor kamu, dan kamu bisa memasukkan passphrase di sana. Setelah selesai mengetik, klik tanda centang hijau untuk menerapkan passphrase ke wallet kamu.


![Image](assets/fr/09.webp)



Kamu kemudian akan memiliki akses ke passphrase yang aman Wallet.



![Image](assets/fr/10.webp)



Untuk pakai Sparrow Wallet, prosesnya hampir sama. Tapi untuk Model T, Safe 3, dan Safe 5, passphrase harus dimasukkan langsung di hardware wallet, bukan lewat keyboard komputer.

Setiap kali Sparrow Wallet butuh akses ke Trezor kamu, dan passphrase belum diterapkan sejak perangkat terakhir dinyalakan, kamu harus memasukkannya lewat keyboard T9 di perangkat.



![Image](assets/fr/11.webp)



## Menambahkan passphrase ke Model One

Di Model One, penggunaan passphrase BIP39 hampir jadi kebutuhan penting. Karena perangkat ini tidak punya Secure Element, relatif lebih mudah mengekstrak data sensitif jika terjadi serangan fisik. Jadi perangkat ini tidak benar-benar tahan terhadap serangan fisik. Tapi karena passphrase tidak disimpan di perangkat setelah dimatikan, memakai passphrase yang kuat dan sulit ditebak bisa melindungi kamu dari sebagian besar serangan fisik yang diketahui pada model ini.

Di Model One, kamu tidak bisa memasukkan passphrase langsung di hardware wallet. Kamu harus memasukkannya lewat keyboard komputer.

Setelah kamu membuat wallet, menyimpan mnemonic, dan mengatur PIN, kamu akan diarahkan ke halaman utama Trezor Suite. Di sudut kiri atas, akan muncul jendela yang mengajak kamu untuk mengaktifkan passphrase BIP39.



![Image](assets/fr/12.webp)



Jika jendela ini tidak muncul, kamu harus mengaktifkan opsi "*passphrase*" di tab "*Device*" pada pengaturan.



![Image](assets/fr/13.webp)


Jendela ini meminta kamu memasukkan passphrase. Pilih passphrase yang kuat dan segera buat cadangan fisik, misalnya di kertas atau logam. Dalam contoh ini, aku pakai passphrase: `fH3&kL@9mP#2sD5qR!82`. Ini cuma contoh, tapi aku sarankan kamu pilih passphrase yang lebih panjang. Idealnya antara 30 sampai 40 karakter, seperti kata sandi yang kuat.

Untuk rekomendasi lebih detail tentang cara memilih passphrase, aku sarankan kamu baca artikel ini:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Masukkan passphrase kamu pada kolom yang tersedia, lalu klik tombol "*Akses passphrase Wallet*".



![Image](assets/fr/14.webp)



Hardware wallet kamu akan menampilkan passphrase yang kamu masukkan. Pastikan datanya cocok dengan cadangan fisik kamu (kertas atau logam), lalu tekan tombol kanan untuk lanjut.


![Image](assets/fr/15.webp)



Ini akan membawa Anda ke portofolio kamu yang dilindungi passphrase.



![Image](assets/fr/16.webp)



Untuk menggunakan Sparrow Wallet setelahnya, prosedurnya tetap sama. Setiap kali Sparrow memerlukan akses ke Hardware Wallet, dan passphrase belum dimasukkan sejak perangkat terakhir kali dinyalakan, kamu harus memasukkannya.



![Image](assets/fr/17.webp)



Selamat, kamu sekarang sudah siap memakai passphrase BIP39 di hardware wallet Trezor. Kalau kamu ingin meningkatkan keamanan wallet kamu ke level berikutnya, kamu bisa lihat tutorial tentang sistem cadangan *Multi-share* Trezor (*Shamir Secret Sharing Scheme*):


https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau kasih jempol hijau di bawah ini. Jangan ragu juga untuk membagikan artikel ini ke jejaring sosial kamu. Terima kasih banyak!
