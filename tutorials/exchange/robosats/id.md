---
name: Robosats

description: Cara menggunakan Robosats
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) adalah cara mudah untuk bertukar Bitcoin dengan mata uang nasional secara pribadi. Ini menyederhanakan pengalaman peer-to-peer dan menggunakan lightning hold invoices untuk meminimalisir kebutuhan akan penyimpanan dan kepercayaan.

![video](https://youtu.be/XW_wzRz_BDI)

## Panduan

> Panduan ini dari Bitcoin Q&A (https://bitcoiner.guide/robosats/). Seluruh kredit untuknya, dukung dia di sana (https://bitcoiner.guide/contribute); BitcoinQ&A juga merupakan mentor bitcoin. Hubungi dia untuk mentoring!

![image](assets/0.webp)

RoboSats - Pertukaran P2P berbasis Lightning yang sederhana dan pribadi

## Sebelum Anda Mulai

### Hal-hal yang perlu Anda ketahui

| Jargon       | Definisi                                                                                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Identitas perdagangan pribadi Anda yang dihasilkan secara otomatis. Jangan menggunakan robot yang sama lebih dari sekali karena ini dapat mengurangi privasi Anda.                            |
| Token        | Sebuah string karakter acak yang digunakan untuk menghasilkan robot unik Anda.                                                                                                                |
| Maker        | Pengguna yang membuat penawaran untuk membeli atau menjual Bitcoin.                                                                                                                           |
| Taker        | Pengguna yang menerima penawaran pengguna lain untuk membeli atau menjual Bitcoin.                                                                                                            |
| Bond         | Jumlah Bitcoin yang dikunci oleh kedua peer sebagai janji untuk bermain adil dan menyelesaikan bagian mereka dari perdagangan. Bond biasanya 3% dari jumlah perdagangan dan didukung oleh Hodl Invoices. |
| Trade Escrow | Digunakan oleh penjual sebagai metode untuk menahan jumlah Bitcoin perdagangan, lagi-lagi menggunakan Hodl Invoices.                                                                           |
| Fees         | RoboSats membebankan 0,2% dari jumlah perdagangan, yang dibagi antara maker dan taker. Taker membayar 0,175% dan maker membayar 0,025%.                                                       |

## Hal-hal yang perlu Anda miliki

### Dompet Lightning

RoboSats adalah native Lightning, jadi Anda akan membutuhkan Dompet Lightning untuk mendanai bond dan menerima sats yang dibeli sebagai pembeli. Anda harus berhati-hati dalam memilih dompet Anda, karena teknologi yang digunakan untuk membuat RoboSats berfungsi, tidak semua kompatibel.

Jika Anda seorang pengelola node, Zeus adalah pilihan terbaik. Jika Anda tidak memiliki node sendiri, saya sangat merekomendasikan Phoenix, dompet mobile lintas platform dengan pengaturan sederhana dan akses ke Lightning. Phoenix digunakan dalam produksi panduan ini.

### Beberapa Bitcoin

Pembeli dan penjual perlu mendanai bond sebelum perdagangan dapat terjadi. Ini biasanya jumlah yang sangat kecil (~3% dari jumlah perdagangan), tetapi tetap merupakan prasyarat.

Menggunakan RoboSats untuk membeli sats pertama Anda? Mengapa tidak meminjam jumlah kecil yang diperlukan untuk memulai dari seorang teman!? Jika Anda terbang solo, berikut adalah beberapa opsi bagus lainnya untuk mendapatkan beberapa sats noKYC untuk memulai.

### Akses ke RoboSats

Jelas Anda akan membutuhkan akses ke RoboSats! Ada empat cara utama di mana Anda dapat melakukan ini:

1. Melalui Tor Browser (Direkomendasikan!)
2. Melalui web-browser biasa (Tidak direkomendasikan!)
3. Melalui APK Android
4. Klien Anda sendiri

Jika Anda baru mengenal Tor browser, pelajari lebih lanjut dan unduh di [sini](https://www.torproject.org/download/).
Catatan cepat untuk pengguna iOS yang ingin mengakses RoboSats melalui Tor dari ponsel mereka. 'Onion Browser' bukanlah Tor Browser. Sebaliknya, gunakan Orbot + Safari dan Orbot + DuckDuckGo.

## Membeli Bitcoin

Langkah-langkah berikut dilakukan pada Mei 2023 menggunakan versi 0.5.0, diakses melalui browser Tor. Langkah-langkahnya seharusnya identik bagi pengguna yang mengakses RoboSats melalui APK Android.

Saat penulisan ini, RoboSats masih dalam pengembangan aktif, jadi antarmuka mungkin sedikit berubah di masa depan, tetapi langkah dasar yang diperlukan untuk menyelesaikan perdagangan harus tetap sebagian besar tidak berubah.

> Ketika Anda pertama kali memuat RoboSats, Anda akan disambut dengan halaman pendaratan ini. Klik Mulai.

![image](assets/2.webp)

Hasilkan token Anda dan simpan di tempat yang aman seperti aplikasi catatan terenkripsi atau pengelola kata sandi. Token ini dapat digunakan untuk memulihkan ID Robot sementara Anda jika browser atau aplikasi Anda tertutup di tengah perdagangan.

![image](assets/3.webp)

Temui identitas Robot baru Anda, lalu klik Lanjutkan.

![image](assets/4.webp)

Klik Penawaran untuk menjelajahi buku pesanan. Di bagian atas halaman, Anda kemudian dapat menyaring sesuai preferensi Anda. Pastikan untuk mencatat persentase jaminan dan premi di atas rata-rata kurs tukar.

- Pilih Beli
- Pilih mata uang Anda
- Pilih metode pembayaran Anda

![image](assets/5.webp)

> Klik pada penawaran yang ingin Anda ambil. Masukkan jumlah (dalam mata uang fiat pilihan Anda) yang ingin Anda beli dari penjual, lalu periksa kembali detailnya dan klik Ambil Pesanan.

Jika penjual tidak online (ditandai dengan titik merah pada gambar profil mereka), Anda akan melihat peringatan bahwa perdagangan bisa memakan waktu lebih lama dari biasanya. Jika Anda melanjutkan dan penjual tidak melanjutkan tepat waktu, Anda akan dikompensasi 50% dari jumlah jaminan mereka untuk waktu Anda yang terbuang.

![image](assets/6.webp)

Selanjutnya, Anda perlu mengunci jaminan perdagangan Anda dengan membayar faktur di layar. Ini adalah faktur penahanan yang membeku di dompet Anda. Ini hanya akan dikenakan biaya jika Anda gagal menyelesaikan bagian Anda dari perdagangan.

![image](assets/7.webp)

Di Dompet Lightning Anda, pindai kode QR dan bayar faktur.

![image](assets/8.webp)

Selanjutnya, di Dompet Lightning Anda, buat faktur untuk jumlah yang ditunjukkan dan tempelkan ke ruang yang disediakan.

![image](assets/9.webp)

Tunggu penjual untuk mengunci jumlah perdagangan mereka. Ketika ini terjadi, RoboSats akan secara otomatis beralih ke langkah selanjutnya di mana jendela obrolan akan terbuka. Ucapkan Hai dan minta penjual untuk informasi pembayaran fiat mereka. Setelah disediakan, kirim pembayaran melalui metode yang dipilih lalu konfirmasi ini di RoboSats. Semua obrolan di RoboSats dienkripsi PGP yang berarti hanya Anda dan rekan perdagangan Anda yang dapat membaca pesan.

![image](assets/10.webp)

Setelah penjual mengonfirmasi penerimaan pembayaran, RoboSats secara otomatis melepaskan pembayaran menggunakan faktur yang disediakan sebelumnya.

![image](assets/11.webp)

Ketika faktur dibayar, perdagangan selesai dan jaminan Anda dibuka. Anda kemudian akan melihat ringkasan perdagangan.

![image](assets/12.webp)

Periksa Dompet Lightning Anda untuk konfirmasi bahwa sats telah tiba.

![image](assets/13.webp)

## Fitur Tambahan

Selain membeli dan menjual Bitcoin, RoboSats memiliki beberapa fitur lain yang harus Anda ketahui.
Robot Garage
Ingin memiliki beberapa perdagangan yang berlangsung secara bersamaan, tetapi tidak ingin berbagi identitas yang sama di antara mereka? Tidak masalah! Klik pada tab Robot, generate Robot tambahan dan buat atau ambil pesanan Anda berikutnya.
![image](assets/14.webp)

### Membuat Pesanan

Selain mengambil tawaran dari orang lain, Anda dapat membuat tawaran Anda sendiri dan menunggu Robot lain datang kepada Anda.

- Buka halaman Create.
- Tentukan apakah pesanan Anda untuk membeli atau menjual Bitcoin.
- Masukkan jumlah dan mata uang yang ingin Anda Beli/Jual.
- Masukkan metode pembayaran yang Anda bersedia gunakan.
- Masukkan % 'Premium over Market' yang Anda bersedia terima. Perhatikan bahwa ini bisa menjadi angka negatif untuk menawar dengan diskon dibandingkan harga pasar saat ini.
- Klik Create Order.
- Bayar faktur Lightning untuk mengunci Maker Bond Anda.
- Pesanan Anda sekarang aktif. Duduk santai dan tunggu seseorang menerimanya.

![image](assets/15.webp)

### Pembayaran On-chain

RoboSats berfokus pada Lightning, tetapi pembeli memiliki opsi untuk menerima sats mereka ke alamat Bitcoin on-chain. Pembeli dapat memilih opsi ini setelah mengunci bond mereka. Setelah memilih on-chain, pembeli akan melihat ikhtisar biaya. Biaya tambahan untuk layanan ini meliputi:

- Biaya swap yang dikumpulkan oleh RoboSats - Biaya ini dinamis dan berubah tergantung pada seberapa sibuk jaringan Bitcoin.
- Biaya penambangan untuk transaksi pembayaran - Ini dapat dikonfigurasi oleh pembeli.

![image](assets/16.webp)

### P2P Swaps

RoboSats memungkinkan pengguna untuk menukar sats ke dalam atau keluar dari Lightning Wallet mereka. Cukup klik tombol swap di bagian atas halaman penawaran untuk melihat penawaran swap saat ini.

Sebagai pembeli dari penawaran ‘Swap In’, Anda mengirim Bitcoin on-chain ke peer dan menerima sats kembali, dikurangi biaya dan/atau premi yang diiklankan, ke Lightning Wallet Anda. Sebagai pembeli dari penawaran ‘Swap Out’, Anda mengirim sats melalui Lightning dan menerima Bitcoin, dikurangi biaya dan/atau premi, ke alamat on-chain Anda. Pengguna Samourai atau Sparrow Wallet juga dapat memanfaatkan fitur Stowaway untuk menyelesaikan swap.

Penawaran swap RoboSats juga dapat memasukkan alternatif pegged terhadap Bitcoin yang mencakup RBTC, LBTC, dan WBTC. Anda harus sangat berhati-hati jika berinteraksi dengan token ini karena semuanya datang dengan berbagai tradeoff. Pegged Bitcoin bukan Bitcoin!

![image](assets/17.webp)

### Jalankan Klien RoboSats Anda Sendiri

Pelari node Umbrel, Citadel, dan Start9 dapat menginstal klien RoboSats mereka sendiri langsung ke node mereka. Manfaat dari melakukan hal ini terdaftar sebagai:

- Waktu muat yang jauh lebih cepat.
- Lebih aman: Anda mengontrol aplikasi klien RoboSats mana yang Anda jalankan.
- Akses RoboSats dengan aman dari browser/perangkat apa pun. Tidak perlu menggunakan TOR jika Anda berada di jaringan lokal Anda atau menggunakan VPN: backend node Anda menangani torifikasi yang diperlukan untuk anonimisasi.
- Memungkinkan kontrol atas koordinator pasar P2P mana yang Anda hubungkan (default ke robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.webp)

## FAQ

### Bisakah saya ditipu?
Sebagai pembeli, jika Anda telah mengirimkan fiat yang diperlukan untuk bagian Anda dalam perdagangan, tetapi penjual gagal melepaskan sats kepada Anda, maka Anda dapat membuka sengketa. Jika selama proses sengketa ini Anda dapat membuktikan kepada arbitrator RoboSats bahwa Anda memang telah mengirim fiat, dana escrow penjual dan ikatan perdagangan mereka akan dilepaskan kepada Anda. Bagaimana saya bisa membatalkan perdagangan?

Anda dapat membatalkan perdagangan setelah memposting ikatan Anda dengan mengklik tombol Pembatalan Kolaboratif dalam menu perdagangan. Jika rekan perdagangan Anda setuju untuk membatalkan, Anda tidak akan dikenakan biaya. Tetapi jika rekan perdagangan Anda ingin menyelesaikan perdagangan dan Anda tetap membatalkan, Anda akan kehilangan ikatan perdagangan Anda.

### Apakah RoboSats bekerja dengan metode pembayaran ‘X’?

Tidak ada pembatasan pada metode pembayaran di RoboSats. Jika Anda tidak melihat penawaran apa pun dengan metode yang Anda inginkan, buatlah penawaran Anda sendiri menggunakan metode tersebut!

![gambar](assets/19.webp)

### Apa yang dipelajari RoboSats tentang saya ketika saya menggunakannya?

Selama Anda menggunakan RoboSats melalui Tor atau aplikasi Android, tidak ada sama sekali! Pelajari lebih lanjut di sini.

- Tor melindungi privasi jaringan Anda.
- Enkripsi PGP menjaga privasi obrolan perdagangan Anda.
- Tidak adanya akun berarti satu Robot per perdagangan. Ini berarti RoboSats tidak dapat menghubungkan beberapa perdagangan ke satu entitas.

Namun, ada beberapa catatan! Lightning cukup pribadi sebagai pengirim, tetapi tidak sebagai penerima. Jika Anda menerima ke node Lightning Anda sendiri, ID node Anda dibagikan dalam faktur Anda. ID node ini memberi siapa pun yang mengetahuinya titik awal untuk mencoba dan menghubungkan aktivitas on-chain Anda. Hal ini juga berlaku jika pengguna memilih untuk menerima perdagangan mereka melalui pembayaran on-chain.

Untuk mengatasi ini, pengguna dapat memilih untuk menggunakan solusi seperti Proxy Wallet untuk Lightning atau Coinjoin untuk on-chain.

### Federasi

Saat ini ada satu koordinator RoboSats yang dioperasikan oleh tim pengembang RoboSats. Dalam Bitcoin, bentuk sentralisasi apa pun membuatnya menjadi target yang lebih mudah bagi pemerintah atau regulator yang mungkin tidak melihat layanan tertentu dengan baik.

Dengan RoboSats menjadi proyek Open Source, siapa pun dapat mengambil kode dan mulai menjalankan koordinator mereka sendiri. Meskipun ini sedikit mendesentralisasi risiko dari satu target, ini juga memfragmentasi pasar likuiditas yang sudah tipis.

Tim RoboSats menyadari ini dan telah mulai bekerja pada model federasi. Sebagai pengguna akhir, ini seharusnya tidak mengubah alur perdagangan yang ditunjukkan di atas terlalu banyak, tetapi akan ada tampilan atau layar tambahan bagi Anda untuk menambahkan atau menghapus koordinator yang berbeda yang muncul.

AKHIR dari panduan
https://bitcoiner.guide/robosats/