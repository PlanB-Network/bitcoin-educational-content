---
name: Lipa
description: Menyiapkan dan menggunakan dompet seluler Lipa lightning
---
![cover](assets/cover.webp)

Dompet Bitcoin Lightning adalah sebuah aplikasi mobile yang memungkinkan transaksi instan dan berbiaya rendah pada jaringan Lightning Bitcoin. Tidak seperti transaksi pada blockchain utama (on-chain), pembayaran Lightning hampir seketika dan membutuhkan biaya minimal, sehingga sangat cocok untuk pembayaran kecil sehari-hari.

Dompet Lightning, seperti halnya semua dompet ponsel, dianggap sebagai dompet "panas" karena terhubung ke Internet. Oleh karena itu, dompet ini terutama ditujukan untuk mengelola sejumlah kecil uang untuk pengeluaran Anda sehari-hari. Untuk jumlah yang lebih besar, lebih baik menggunakan solusi penyimpanan yang lebih aman seperti dompet perangkat keras.

Jika Anda ingin mempelajari lebih lanjut tentang jaringan Lightning dan memahami cara kerjanya secara teknis, saya sarankan Anda mengikuti kursus ini:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Dalam tutorial ini, kita akan melihat **Lipa**, sebuah dompet Lightning yang sederhana dan efektif yang dikembangkan di Swiss.

## Memperkenalkan Lipa

Lipa adalah dompet Lightning non-kustodian yang dibedakan dari kesederhanaan penggunaannya dan antarmuka yang rapi. Dikembangkan oleh tim Swiss, Lipa menekankan kerahasiaan dan kemudahan penggunaan untuk pemula.

Fitur-fitur utama meliputi:


- Antarmuka pengguna yang intuitif
- Manajemen saluran Petir Otonom
- Dukungan protokol LNURL
- Kemungkinan untuk membeli bitcoin secara langsung di dalam aplikasi

## Menginstalasi dan mengonfigurasi Lipa

Langkah pertama adalah mengunduh aplikasi Lipa. Untuk saat ini, aplikasi ini hanya tersedia di iOS:


- [Untuk Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Versi Android saat ini sedang dikembangkan dan akan segera tersedia.

![Installation de Lipa](assets/fr/01.webp)

Setelah Anda meluncurkan aplikasi, Anda akan tiba di layar beranda, yang menawarkan dua opsi:


- Membuat portofolio baru
- Memulihkan portofolio yang ada dari cadangan

Setelah Anda memilih opsi, aplikasi akan meminta Anda untuk mengaktifkan pemberitahuan. Langkah ini penting, karena notifikasi diperlukan untuk aplikasi :


- Menerima peringatan ketika pembayaran diterima, bahkan ketika aplikasi ditutup
- Dapatkan informasi tentang langkah-langkah yang terlibat dalam membeli bitcoin melalui solusi terintegrasi mereka

Aplikasi ini kemudian menyajikan fungsi utamanya melalui serangkaian layar pengantar:


- Tanda terima pembayaran yang mulus**: Pengguna dapat menerima pembayaran Bitcoin bahkan ketika aplikasi ditutup, menjamin keandalan dan kenyamanan.
- Alamat Lightning non-kustodian**: Lipa sekarang mendukung alamat Lightning non-kustodian, meningkatkan privasi dan keamanan dengan memberikan kontrol penuh kepada pengguna atas bitcoin mereka.
- Kontrol atas data analitik**: Dengan mengutamakan transparansi dan kerahasiaan, pengguna dapat melihat jenis data yang dikumpulkan dan memilih preferensi berbagi.
- Kirim melalui nomor telepon**: Tidak perlu alamat yang rumit - cukup pilih kontak, masukkan jumlahnya, dan kirimkan bitcoin langsung ke nomor telepon mereka.

Aplikasi ini juga mendapat manfaat dari peningkatan berkelanjutan dalam hal stabilitas, keamanan dan keandalan, untuk menjamin pengalaman pengguna yang optimal.

## Navigasi aplikasi

Antarmuka Lipa diatur di sekitar 4 tab utama yang dapat diakses melalui bilah navigasi di bagian bawah layar:

![Navigation principale](assets/fr/02.webp)


- Beranda**: Menampilkan saldo dan riwayat transaksi Anda saat ini
- Pemindai**: Memungkinkan Anda memindai kode QR untuk melakukan pembayaran
- Peta**: Menampilkan peta interaktif bisnis yang menerima Bitcoin di wilayah Anda
- Pengaturan**: Akses ke pengaturan aplikasi, pencadangan, dan preferensi

Menu tambahan dapat diakses dengan menarik layar beranda ke bawah:

![Menu supplémentaire](assets/fr/03.webp)

Isyarat ini mengungkapkan fungsi tambahan, seperti :


- Membeli bitcoin
- Setoran bitcoin on-chain
- Membuat faktur Lightning untuk menerima bitcoin
- Pembayaran faktur kilat

## Simpan portofolio Anda

Untuk mencadangkan dompet Anda, buka tab "Pengaturan" dan pilih "Frasa pemulihan". Lipa menggunakan frasa pemulihan yang sangat penting untuk ditulis dengan hati-hati pada media fisik (kertas, logam). Frasa ini adalah satu-satunya cara untuk memulihkan dana Anda jika ponsel Anda hilang atau dicuri. Untuk memvalidasi cadangan Anda, aplikasi akan meminta Anda untuk mengonfirmasi 3 kata acak dari frasa Anda.

![Backup](assets/fr/04.webp)

Untuk informasi lebih lanjut tentang cara mencadangkan dan mengelola frasa pemulihan Anda dengan benar, saya sangat menyarankan untuk mengikuti tutorial lainnya, terutama jika Anda seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Menerima bitcoin

Untuk menerima bitcoin, Anda memiliki dua opsi. Untuk mengakses opsi-opsi ini, kembali ke layar beranda dan tarik layar ke bawah. Kemudian Anda dapat memilih :


- Pilih "Transfer BTC" untuk menerima bitcoin secara on-chain. Kemudian cukup pindai kode QR dengan dompet Anda yang lain dan selesaikan transaksi.
- Pilih "Request" untuk menerima melalui jaringan Lightning dan masukkan jumlah yang ingin Anda terima.

Dalam kedua kasus tersebut, Anda harus membayar biaya yang setara dengan 0,4% dari jumlah tersebut, atau sekitar 2.500 sat jika aplikasi harus membuka saluran pembayaran baru (yang pasti akan terjadi pada pembayaran pertama).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Kirim bitcoin

Untuk mengirim bitcoin, buka layar beranda, tarik layar ke bawah dan pilih "Bayar". Kemudian cukup dengan :


- masukkan alamat LNURL kilat
- pindai kode QR kilat untuk melakukan pembayaran.

Anda juga dapat membuka tab kedua di bagian bawah layar untuk memindai kode QR secara langsung.

![Envoi de bitcoins](assets/fr/07.webp)

## Beli bitcoin

Lipa menawarkan kemungkinan untuk membeli bitcoin secara langsung dalam aplikasi dengan biaya 1,5%. Untuk melakukan pembelian, buka layar beranda dan tarik ke bawah untuk menampilkan menu. Kemudian pilih "Beli BTC". Tiga layar pengantar akan memandu Anda melalui proses pembelian.

![Menu d'achat](assets/fr/08.webp)

Kemudian masukkan detail bank dari akun yang akan Anda gunakan untuk melakukan pembelian. Pilih mata uang dan masukkan alamat email Anda.

Setelah layar pemuatan, Anda akan menemukan nomor referensi yang akan disertakan dalam transfer yang akan Anda lakukan, serta detail bank untuk penukaran.

![Sélection du montant](assets/fr/09.webp)

Yang harus Anda lakukan adalah menggunakan bank Anda untuk mentransfer jumlah yang diinginkan, mengatur transfer dengan menunjukkan RIB yang sebelumnya diambil dan menunjukkan referensi pada saat transaksi sehingga Lipa dapat mengaitkan pergerakan bank ini dengan dompet Lipa Anda.

![Confirmation d'achat](assets/fr/10.webp)

## Keuntungan dan kerugian

### Manfaat


- Antarmuka yang intuitif
- Biaya layanan yang benar
- Non kustodian
- Solusi pembelian bitcoin terintegrasi
- Integrasi BTCmap
- Dukungan NFC

### Kekurangan


- Tidak mungkin mengirim bitcoin secara berantai
- Pembayaran sedikit lebih lama dari rata-rata

Lipa adalah pilihan yang sangat baik untuk memulai dengan Lightning Network, terutama cocok untuk pengguna yang mencari solusi sederhana untuk pembayaran sehari-hari. Kemudahan penggunaan dan antarmuka yang rapi membuatnya menjadi dompet yang ideal untuk pemula, sekaligus menawarkan fitur-fitur penting untuk penggunaan Lightning sehari-hari.

## Sumber daya


- [Situs web resmi Lipa](https://lipa.swiss/)
- [Dukungan Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)