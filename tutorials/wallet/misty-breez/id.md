---
name: Misty Breez
description: Lightning Wallet tanpa busur.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez adalah Lightning self-custody wallet yang dikembangkan oleh Breez berdasarkan Kit Pengembangan Perangkat Lunak mereka dan jaringan **Liquid** yang dikembangkan oleh Blockstream.


Hadir dengan pendekatan yang benar-benar baru untuk beroperasi tanpa node Lightning: potensi **GAME CHANGER** dalam transfer antarjaringan Bitcoin.


Dalam tutorial ini, kita akan menjelaskan cara kerja wallet ini dan memberi kamu gambaran yang lengkap.



## Bagaimana cara kerja Misty Breez?



Misty Breez adalah implementasi tanpa node Lightning sebagai backend. Ini dikembangkan berdasarkan Breez SDK dan Liquid.



Liquid adalah layer paralel dengan jaringan Bitcoin, yang menawarkan peningkatan signifikan dalam hal kecepatan dan biaya transaksi. Layer ini memungkinkan Misty Breez untuk tidak menggunakan node Lightning dan sebagai gantinya menggunakan layanan exchange pihak ketiga seperti **Boltz** untuk memastikan interoperabilitas antara Liquid Network dan Lightning Network. Jangan terburu-buru, kita akan kembali ke bagian ini.



Untuk saat ini, mari mulai petualangan kita dengan Misty Breez Wallet.




## Memulai dengan Misty Breez



Aplikasi seluler Misty Breez tersedia di platform unduhan resmi seperti Google Play Store (di Android) dan Apple Store (di iOS). Anda juga dapat diarahkan ke aplikasi yang tepat dari situs web resmi [Misty Breez](https://breez.technology/misty/).



⚠️ Pastikan kamu tidak tertukar antara Misty Breez dengan Breez Wallet.



⚠️ **PENTING**: Demi keamanan bitcoin kamu, sangat penting untuk mengunduh aplikasi dari platform resmi untuk memastikan keasliannya.



![download-misty-breez](assets/fr/01.webp)



Dalam tutorial ini, kita akan mulai dari perangkat Android. Namun demikian, setiap langkah dan fitur spesifik yang dirinci dalam bagian ini juga berlaku untuk iOS.



Setelah instalasi, Misty Breez memberi kamu pilihan untuk membuat wallet baru atau memulihkan Lightning wallet lama yang memiliki seedphrase.


Dalam tutorial ini, kita memilih untuk membuat wallet baru.




⚠️Misty Breez saat ini sedang dalam tahap pengembangan, jadi kami menyarankanmu untuk memulai dengan jumlah yang wajar.



![create-wallet](assets/fr/02.webp)


### Simpan seedphrase kamu:


Salah satu hal pertama yang harus kamu lakukan saat membuat wallet baru adalah membuat cadangan 12 kata pemulihan.


Berikut beberapa tips tentang cara membuat cadangan seedphrase kamu.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Untuk mencadangkan seedphrase kamu, pilih menu **Preferensi > Keamanan**, lalu opsi **Periksa Seedphrase Cadangan Kamu**.



![backup](assets/fr/03.webp)


Untuk keamanan tambahan, kamu juga dapat **membuat kode PIN** untuk mengautentikasi akses ke wallet kamu.




Temukan mata uang lokal kamu dalam berbagai mata uang yang didukung oleh Misty Breez. Konfigurasikan mata uang kamu dari menu **Preferensi > Mata Uang Fiat**, lalu pilih satu atau beberapa mata uang yang kamu inginkan.




![devises](assets/fr/04.webp)



### Melakukan transaksi pertama kamu


Jika kamu sudah terbiasa dengan wallet Breez, kamu tidak akan kesulitan dengan interface intuitif dari Misty Breez.



Pada menu **Saldo** di interface, klik opsi **Terima** untuk membuat invoice guna menerima bitcoin kamu di wallet.



⚠️ Misty Breez akan meminta kamu untuk mengaktifkan notifikasi aplikasi di pengaturan ponsel agar bisa mendapatkan Lightning Address.



Dengan Misty Breez, kamu dapat:




- Menerima bitcoin di Lightning Network mulai dari **100 satoshi** hingga **25.000.000 satoshi**.
- Menerima bitcoin di jaringan utama Bitcoin mulai dari **25.000 satoshi**.



![transactions](assets/fr/05.webp)



Di sinilah keajaiban Misty Breez dimulai.


Tidak seperti Breez Wallet, yang menyediakan node Lightning dan mengharuskan kamu menanggung sendiri biaya pembukaan dan penutupan channel pembayaran, Misty Breez tidak meminta kamu melakukan apa pun. Seperti yang sudah disebutkan sebelumnya, Misty Breez bahkan tidak bekerja berbasis node Lightning.



Mari kita lihat lebih dekat cara kerjanya di balik layar.



Pada kenyataannya, kamu memiliki wallet Liquid yang terhubung dengan wallet Misty Breez kamu. Secara teknis, kamu akan menangani L-BTC (Liquid Bitcoin) dengan harga tetap yang terhubung ke layanan konversi pihak ketiga berbasis submarine swap yang memungkinkan kamu beroperasi dengan Lightning Network.



Ketika kamu menerima pembayaran di Misty Breez wallet, pengirim akan mengirimkan satoshi yang kemudian melewati layanan konversi seperti Boltz (yang saat ini digunakan oleh Misty Breez), untuk mengonversi satoshi yang dikirim menjadi L-BTC yang akan diterima di Misty Breez wallet kamu (yang terhubung ke Liquid wallet).


Berikut adalah diagram sederhana mengenai proses yang terjadi di balik layar.




![lnswap-in](assets/fr/06.webp)



Klik pada Interface di menu **Saldo**, klik opsi **Kirim** untuk membayar Lightning Invoice.


Masukkan Lightning Invoice, Lightning Address milik penerima kamu atau cukup pindai kode QR pada Invoice untuk melakukan pembayaran.



![send-bitcoins](assets/fr/07.webp)



Di balik layar, kamu menggunakan Liquid wallet yang terhubung dengan Misty Breez wallet untuk mengonversi nilai setara L-BTC menjadi satoshi melalui Boltz, lalu mentransfer satoshi tersebut ke Lightning wallet penerima kamu (di Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Fitur infrastruktur Misty Breez ini memungkinkan pengguna untuk tetap melakukan transaksi bahkan ketika Misty Breez sedang offline.



Untuk pengguna yang lebih berpengalaman, ada juga menu **Preferensi > Pengembang** yang memberi kamu detail tambahan tentang:




- Versi Kit Pengembangan Perangkat Lunak Breez.
- Kunci publik Misty Breez wallet kamu.
- Peminjam, pengenal unik yang berasal dari kunci publik utama.
- Saldo wallet kamu.
- Tip Liquid, untuk mengirim L-BTC dalam jumlah kecil.
- Tip Bitcoin, untuk mengirim Bitcoin dalam jumlah kecil.



Kamu juga dapat melakukan tindakan tertentu, seperti sinkronisasi dengan Liquid Network, mencadangkan kunci kamu, membagikan log aktivitas, dan memilih untuk memindai ulang Liquid Network.




![dev-mode](assets/fr/09.webp)


Selamat! Kamu sekarang sudah punya pemahaman yang baik tentang wallet Misty Breez dan kontribusinya terhadap transaksi antaringan Bitcoin. Jika kamu merasa tutorial ini bermanfaat, berikan jempol Green kepada kami. Kami akan sangat senang mendengarnya dari kamu.



Untuk melangkah lebih jauh, aku juga menyarankan kamu untuk melihat tutorial kami tentang Aqua Wallet, yang bekerja dengan cara yang mirip dengan Misty Breez:


https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125
