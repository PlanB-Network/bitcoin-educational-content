---
name: BIP-39 Penandatangan Benih Frasa Sandi
description: Bagaimana cara menambahkan passphrase ke portofolio SeedSigner saya?
---

![cover](assets/cover.webp)



passphrase BIP39 adalah sebuah kata sandi opsional yang dikombinasikan dengan frasa mnemonik, memberikan lapisan keamanan tambahan untuk dompet Bitcoin yang bersifat deterministik dan hirarkis. Dalam tutorial ini, kita akan bersama-sama mempelajari cara mengatur passphrase pada Bitcoin wallet yang digunakan dengan SeedSigner.



![Image](assets/fr/01.webp)



## Prasyarat sebelum menambahkan Frasa Sandi



Sebelum memulai tutorial ini, jika Anda belum terbiasa dengan konsep passphrase, cara kerjanya dan implikasinya terhadap Bitcoin wallet Anda, saya sangat menyarankan agar Anda membaca artikel teoritis lainnya di mana saya menjelaskan semuanya (ini sangat penting, karena menggunakan passphrase tanpa sepenuhnya memahami cara kerjanya dapat membahayakan bitcoin Anda):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sebelum memulai tutorial ini, pastikan Anda telah menginisialisasi SeedSigner dan membuat frasa mnemonik. Jika belum, dan SeedSigner Anda masih baru, ikuti tutorial di Plan ₿ Academy. Setelah Anda menyelesaikan langkah ini, Anda dapat kembali ke tutorial ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Bagaimana cara menambahkan passphrase ke SeedSigner?



Menambahkan passphrase ke portofolio Anda yang dikelola melalui SeedSigner akan membuat portofolio yang benar-benar baru, menghasilkan satu set kunci yang sama sekali terpisah. Akibatnya, jika Anda sudah memiliki portofolio yang berisi satss, Anda tidak akan lagi dapat mengaksesnya dengan passphrase, karena passphrase menghasilkan portofolio yang sama sekali berbeda.



Untuk menerapkan passphrase ke SeedSigner Anda, nyalakan perangkat dan pindai SeedQR Anda seperti biasa. SeedSigner kemudian akan menampilkan sidik jari wallet Anda saat ini, sesuai dengan sidik jari **tanpa passphrase**. wallet dengan passphrase akan memiliki sidik jari yang berbeda.



Klik tombol `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Kemudian masukkan passphrase pilihan Anda pada kolom yang tersedia, dengan menggunakan keyboard di layar. Pastikan untuk membuat satu atau beberapa cadangan fisik (kertas atau logam): kehilangan passphrase ini akan mengakibatkan hilangnya akses ke bitcoin Anda secara permanen. **Untuk memulihkan wallet, baik mnemonik maupun passphrase sangat penting ** Jika salah satu hilang, bitcoin Anda akan diblokir secara permanen.



Setelah Anda menyelesaikan entri Anda, validasi dengan menekan tombol `KEY3` di bagian kanan bawah SeedSigner.



![Image](assets/fr/03.webp)



*Dalam contoh ini, saya menggunakan passphrase `pba`. Namun demikian, dalam kasus Anda, pastikan Anda memilih passphrase yang kuat. Untuk mengetahui cara menentukan passphrase yang optimal, silakan baca artikel ini:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner kemudian menampilkan sidik jari baru dari passphrase wallet Anda. Buatlah beberapa salinan sidik jari ini: ini penting ketika menggunakan wallet dengan passphrase, karena ini memungkinkan Anda untuk memeriksa, setiap kali Anda memasuki passphrase, bahwa Anda tidak membuat kesalahan pengetikan dan bahwa Anda mengakses wallet yang benar.



Sebagai contoh, jika dalam kasus saya, saya keliru menuliskan passphrase `Pba` ketika memulai SeedSigner dan bukannya `pba`, perubahan sederhana dari huruf kecil ke huruf besar ini akan menghasilkan pembuatan portofolio yang sama sekali berbeda dengan portofolio yang ingin saya akses.



Sidik jari ini tidak menimbulkan risiko terhadap keamanan atau kerahasiaan wallet Anda. Sidik jari ini tidak mengungkapkan informasi apa pun, baik publik maupun pribadi, tentang kunci Anda. Jadi, tidak seperti mnemonic dan passphrase, Anda dapat menyimpan sidik jari pada media digital. Saya sarankan Anda menyimpan salinannya di beberapa tempat: di selembar kertas, di pengelola kata sandi, dll.



Setelah Anda menyimpan sidik jari Anda, klik `Selesai`.



![Image](assets/fr/04.webp)



Anda kemudian memiliki akses ke semua fungsi portofolio Anda, seperti pada SeedSigner klasik.



![Image](assets/fr/05.webp)



Sekarang Anda dapat mengimpor keystore ke Sparrow Wallet dan menggunakan wallet seperti biasa. Setiap kali Anda memulai ulang, Anda harus memindai SeedQR Anda dan memasukkan kembali passphrase Anda menggunakan keyboard, seperti yang kami lakukan di sini.



Sebelum Anda benar-benar menggunakan wallet dengan passphrase, saya sangat menyarankan agar Anda melakukan tes pemulihan kosong penuh. Hal ini akan memungkinkan Anda untuk mengonfirmasi bahwa cadangan frasa mnemonik dan passphrase Anda valid. Untuk mempelajari cara melakukan pemeriksaan ini, lihat tutorial berikut:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895