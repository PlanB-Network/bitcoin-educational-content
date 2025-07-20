---
name: Misty Breez
description: Lightning Wallet tanpa busur.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez adalah Lightning self-holding Wallet yang dikembangkan oleh Breez berdasarkan Kit Pengembangan Perangkat Lunak mereka dan jaringan **Liquid** yang dikembangkan oleh BlockStream.


Hadir dengan pendekatan yang benar-benar baru untuk beroperasi tanpa node Lightning: potensi **GAME CHANGER** dalam transfer antar-jaringan Bitcoin.


Dalam tutorial ini, kami akan menjelaskan cara kerja portofolio ini dan memberi Anda gambaran yang lengkap.



## Bagaimana cara kerja Misty Breez?



Misty Breez adalah implementasi tanpa node Lightning sebagai backend. Ini telah dikembangkan berdasarkan Breez SDK dan Liquid.



Liquid adalah Layer paralel dengan jaringan Bitcoin, yang menawarkan peningkatan signifikan dalam hal kecepatan dan biaya transaksi. Layer ini memungkinkan Misty Breez untuk tidak menggunakan node Lightning dan sebagai gantinya menggunakan layanan Exchange pihak ketiga seperti **Boltz** untuk memastikan interoperabilitas antara Liquid Network dan Lightning Network. Jangan terburu-buru, kita akan kembali ke sini.



Untuk saat ini, mari kita mulai petualangan kita dengan Misty Breez Wallet.



## Memulai dengan Misty Breez



Aplikasi seluler Misty Breez tersedia di platform unduhan resmi seperti Google Play Store (di Android) dan Apple Store (di iOS). Anda juga dapat diarahkan ke aplikasi yang tepat dari situs web resmi [Misty Breez] (https://breez.technology/misty/).



⚠️ Pastikan Anda tidak tertukar antara Misty Breez dengan Breez Wallet.



⚠️ **PENTING**: Demi keamanan bitcoin Anda, sangat penting untuk mengunduh aplikasi dari platform resmi untuk memastikan keasliannya.



![download-misty-breez](assets/fr/01.webp)



Dalam tutorial ini, kita akan mulai dari perangkat Android. Namun demikian, setiap langkah dan fitur spesifik yang dirinci dalam bagian ini juga berlaku untuk iOS.



Setelah instalasi, Misty Breez memberi Anda pilihan untuk membuat Wallet baru atau memulihkan Lightning Wallet lama yang memiliki kata-kata pemulihan.


Dalam tutorial ini, kami memilih untuk membuat portofolio baru.



⚠️Misty Breez saat ini sedang dalam tahap pengembangan, jadi kami menyarankan Anda untuk memulai dengan jumlah yang wajar.



![create-wallet](assets/fr/02.webp)


### Simpan kata-kata pemulihan Anda :


Salah satu hal pertama yang harus Anda lakukan saat membuat portofolio baru adalah membuat cadangan 12 kata pemulihan.


Berikut ini beberapa tips tentang cara membuat cadangan frasa cadangan Anda.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Untuk mencadangkan frasa Anda, pilih menu **Preferensi > Keamanan**, lalu opsi **Periksa Frasa Cadangan Anda**.



![backup](assets/fr/03.webp)


Untuk keamanan tambahan, Anda juga dapat **membuat kode PIN** untuk mengotentikasi akses ke Wallet Anda.




Temukan mata uang lokal Anda dalam berbagai mata uang yang diterima oleh Misty Breez. Konfigurasikan mata uang Anda dari menu **Preferensi > Mata Uang Fiat**, lalu pilih mata uang atau beberapa mata uang yang Anda inginkan.



![devises](assets/fr/04.webp)



### Melakukan transaksi pertama Anda


Jika Anda sudah terbiasa dengan portofolio Breez, Anda tidak akan merasa kesulitan dengan Interface yang intuitif dari Misty Breez.



Pada menu **Saldo** Interface, klik opsi **Terima** untuk membuat faktur guna menerima bitcoin Anda di Wallet.



⚠️ Misty Breez akan meminta Anda untuk mengaktifkan notifikasi untuk aplikasi dalam pengaturan ponsel Anda untuk mendapatkan Lightning Address.



Dengan Misty Breez, Anda dapat :




- Dapatkan bitcoin di Lightning Network mulai dari **100 satoshi** hingga **25.000.000 satoshi**.
- Dapatkan bitcoin di jaringan utama Bitcoin mulai dari **25.000 satoshi**.



![transactions](assets/fr/05.webp)



Di sinilah keajaiban Misty Breez dimulai.


Tidak seperti Breez Wallet, yang menyediakan node Lightning dan meminta Anda untuk menanggung sendiri biaya pembukaan dan penutupan saluran pembayaran, Misty Breez tidak meminta Anda melakukan apa pun. Seperti yang telah disebutkan sebelumnya, Misty Breez bahkan tidak bekerja berdasarkan node Lightning.



Mari kita lihat lebih dekat di balik layar.



Pada kenyataannya, Anda memiliki portofolio Liquid yang terkait dengan portofolio Misty Breez Anda. Logikanya, Anda akan menangani L-BTC (Liquid Bitcoin) dengan harga tetap yang terkait dengan layanan konversi satoshi kapal selam pihak ketiga yang memungkinkan Anda untuk beroperasi dengan Lightning Network.



Ketika Anda menerima pembayaran di Misty Breez Wallet Anda, pengirim akan mengirimkan satoshi yang akan melalui layanan konversi seperti Boltz (saat ini digunakan oleh Misty Breez), untuk mengonversi satoshi yang dikirim menjadi L-BTC yang akan diterima di Misty Breez Wallet Anda (terkait Liquid Wallet).


Berikut ini adalah diagram yang disederhanakan mengenai proses di balik layar.



![lnswap-in](assets/fr/06.webp)



Klik pada Interface di menu **Saldo**, klik opsi **Kirim** untuk membayar Lightning Invoice.


Masukkan Lightning Invoice, Lightning Address milik penerima Anda atau cukup pindai kode QR pada Invoice untuk melakukan pembayaran.



![send-bitcoins](assets/fr/07.webp)



Di belakang layar, Anda mengaktifkan Liquid Wallet yang terkait dengan Misty Breez Wallet Anda untuk mengonversi setara dengan L-BTC ke dalam satoshi melalui Boltz, kemudian mentransfer satoshi ini ke Lightning Wallet penerima Anda (ada di Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Fitur infrastruktur Misty Breez ini memungkinkan pengguna untuk melakukan transaksi bahkan ketika Misty Breez sedang offline.



Untuk yang lebih berpengalaman, ada juga menu **Preferensi > Pengembang** yang memberi Anda sedikit lebih banyak detail tentang :




- Versi Kit Pengembangan Perangkat Lunak Breez.
- Kunci publik Misty Breez Wallet Anda.
- Peminjam, pengenal unik yang berasal dari kunci publik utama.
- Saldo portofolio Anda.
- Tip Liquid, untuk mengirim L-BTC dalam jumlah kecil.
- Tip Bitcoin, untuk mengirim Bitcoin dalam jumlah kecil.



Anda juga dapat melakukan tindakan tertentu, seperti sinkronisasi dengan Liquid Network, mencadangkan kunci Anda, berbagi log aktivitas dan memilih untuk memindai ulang Liquid Network.



![dev-mode](assets/fr/09.webp)


Selamat! Anda sekarang memiliki pemahaman yang baik tentang portofolio Misty Breez dan kontribusinya terhadap transaksi antar jaringan Bitcoin. Jika Anda merasa tutorial ini bermanfaat, berikan jempol Green kepada kami. Kami akan sangat senang mendengarnya dari Anda.



Untuk melangkah lebih jauh, saya juga menyarankan Anda untuk menemukan tutorial kami tentang Aqua Wallet, yang bekerja dengan cara yang mirip dengan Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125