---
name: Ledger Nano S

description: Cara menyiapkan perangkat Ledger Nano S Anda
---

![image](assets/cover.webp)

Dompet fisik dingin – €60 – Pemula – Untuk mengamankan €2.000 hingga €50.000

Ledger adalah solusi Prancis untuk mengamankan bitcoin dengan cara yang sederhana.

Dalam tutorial ini, kami juga membahas bagian passphrase, solusi keamanan lanjutan untuk menyimpan jumlah besar: 20.000€ – 100.000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Menghubungkan Ledger ke Sparrow Bitcoin Wallet (panduan penulisan)

Pastikan Anda telah membaca bagian lainnya "Menggunakan Bitcoin Hardware Wallets" terlebih dahulu. Saya akan melewati beberapa langkah dan lebih fokus pada apa yang spesifik untuk Ledger di sini.

## Menyiapkan perangkat

Ledger dilengkapi dengan kabel USB sendiri. Pastikan Anda menggunakan itu dan bukan sembarang kabel lama. Beberapa kabel USB hanya untuk daya. Yang ini mentransmisikan data DAN daya. Ketika saya menggunakan perangkat dengan kabel USB pengisian ponsel yang tergeletak di sekitar, perangkat gagal terhubung.

Hubungkan ke komputer Anda dan perangkat akan menyala.

![image](assets/1.webp)

Jelajahi opsi-opsinya. Anda akan melihat

1. Atur sebagai perangkat baru
2. Pulihkan dari frasa pemulihan

Pada dasarnya, ini bertanya apakah Anda ingin perangkat membuat seed untuk Anda atau jika Anda sudah memiliki satu yang ingin Anda gunakan. Praktik terbaik adalah membuat seed Anda sendiri, tetapi melakukan itu dengan aman sangat lanjutan, dan di luar cakupan artikel ini. Pilih "Atur sebagai perangkat baru"

Anda kemudian akan diminta untuk memilih PIN. Ini bukan bagian dari seed Bitcoin Anda dan spesifik untuk perangkat ini saja. Ini mengunci perangkat.

Kemudian akan menampilkan kepada Anda 24 kata yang perlu Anda siklus melalui dan tulis.

Anehnya, ketika Anda sampai di akhir, itu mengatakan "tekan kiri untuk memverifikasi kata-kata Anda". Itu tidak menjelaskan bagaimana Anda mengonfirmasi untuk melanjutkan, itu hanya berarti Anda dapat kembali dan melihat kata-kata lagi. Tekan kanan sebagai gantinya, dan konfirmasi dengan menekan kiri dan kanan secara bersamaan.

Bagian selanjutnya sangat menjengkelkan. Ini mencampuradukkan 24 kata dan Anda harus mengonfirmasi setiap satu, dari 1 hingga 24, dengan mengitari semua kata untuk setiap pilihan. Setelah Anda selesai, itu memungkinkan Anda untuk mengonfirmasi dengan tekanan dua tombol dan melanjutkan.

![image](assets/2.webp)

Anda akan melihat di dasbor Anda bahwa Anda memiliki tombol pengaturan, dan tombol tanda tambah yang memungkinkan Anda untuk menginstal aplikasi. Tapi Anda perlu terhubung ke Ledger Live terlebih dahulu. Kami akan melakukannya selanjutnya…

## Unduh Ledger Live

Anda bisa mengunduh Ledger Live dari halaman web mereka, tetapi lebih baik mendapatkannya dari GitHub, di mana kode sumber disimpan.

Google "ledger live GitHub" atau klik tautan ini https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Gulir ke bawah sampai Anda melihat judul, "Downloads"…

![image](assets/4.webp)

Di bagian bawah, Anda akan melihat tautan: Instruksi untuk memverifikasi hash dan tanda tangan dari paket instalasi tersedia di halaman ini. Klik tautan itu.(https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

Di bagian atas, ada pilihan tautan untuk paket perangkat lunak yang Anda butuhkan, tergantung pada sistem operasi Anda. Klik yang sesuai untuk mengunduh.

Selanjutnya, kami ingin memverifikasi hash unduhan, untuk keamanan ekstra.
Ledger mempublikasikan hash dari setiap file yang tersedia di halaman ini. Kita akan meng-hash unduhan dan membandingkan outputnya. Ini perlu identik untuk memastikan file tersebut tidak telah diubah.

Buka terminal pada Mac atau CMD di windows. Ikuti perintah berikut...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Untuk Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Untuk Windows
```

<Enter>

Semoga sudah jelas bahwa perintah dimulai setelah panah. Pastikan, jika artikel ini sudah usang, Anda mengubah nama file dalam perintah sesuai dengan nama file yang Anda unduh. Anda perlu menekan tombol <Enter> setelah setiap perintah. Perintah seperti yang terlihat di sini mungkin tidak muat dalam satu baris di peramban web Anda. Catatan, semuanya diketik dalam satu baris.

Lihat output dari hash dan pastikan itu identik dengan yang dipublikasikan di GitHub.

Idealnya, Anda ingin lebih teliti dan memastikan bahwa hash yang dipublikasikan tidak palsu. Kami melakukan ini dengan tanda tangan gpg, tetapi itu di luar cakupan artikel ini. Jika Anda ingin belajar tentang itu (dan saya sarankan Anda akhirnya melakukannya), maka telusuri artikel ini.

## Terhubung ke Ledger Live

Sebelum Anda menjalankan Ledger Live, membantu privasi sedikit untuk mengaktifkan VPN. Ledger masih akan mendapatkan semua alamat Anda, tetapi mereka tidak akan tahu alamat IP Anda, yang memberikan alamat rumah Anda. Mullvad VPN adalah layanan VPN yang sangat baik dan tidak terlalu mahal (saya tidak beriklan, itu hanya yang saya gunakan).

Instal perangkat lunak ke komputer Anda dan jalankan.

![image](assets/6.webp)

Pilih perangkat Anda, dan pilih "Pertama kali menggunakan..."

![image](assets/7.webp)

Anda kemudian akan dibawa melalui wizard, tetapi kami telah melakukan semua langkah ini sehingga Anda dapat melalui.

![image](assets/8.webp)

Setelah banyak langkah dan kuis, itu akan memeriksa perangkat adalah asli. Anda perlu memastikan Anda terhubung dan memasukkan pin, dan kemudian akan ditanya pada perangkat jika Anda mengizinkan Ledger Live untuk terhubung. Anda harus mengonfirmasi itu, tentu saja.

![image](assets/9.webp)

Ada beberapa iklan shitcoin yang menyamar sebagai "catatan rilis" di pop up berikutnya. Abaikan itu, dan kemudian Anda harus sampai ke layar ini.

![image](assets/10.webp)

Anda harus klik "Tambah akun" untuk mendapatkan Dompet Bitcoin.

![image](assets/11.webp)

Pastikan Anda memilih Bitcoin, dan bukan Bitcoin Cash atau shitcoin lainnya. Ini akan memeriksa perangkat, dan Anda harus mengonfirmasi untuk melanjutkan DI PERANGKAT. Ini akan menghitung alamat selama beberapa menit. Kemudian klik SELESAI.

![image](assets/12.webp)
![image](assets/13.webp)

Bagus. Sekarang Anda memiliki manajer dompet shitcoin yang berisi dompet Bitcoin di komputer Anda. Anda sebenarnya tidak memerlukan ini lagi dan bisa menyingkirkannya. Tujuan sebenarnya adalah untuk mendapatkan Aplikasi Bitcoin di perangkat itu sendiri, dan ini adalah satu-satunya cara, selain melakukan beberapa teknik insinyur perangkat lunak yang ekstrem.

Ingat bahwa sebelumnya, di perangkat, kami memiliki tombol pengaturan dan tombol tanda tambah. Sekarang kami memiliki tombol ekstra - tombol Aplikasi Bitcoin.

Anda dapat mematikan Ledger Live sekarang.

## Tambahkan passphrase
Kini setelah kita memiliki Aplikasi Bitcoin, kita dapat menambahkan passphrase ke seed phrase kita. Kita tidak bisa melakukan itu sebelumnya ketika seed pertama kali dibuat karena pada awalnya, kita tidak memiliki Aplikasi Bitcoin, dan kita perlu terhubung ke Ledger Live untuk mendapatkannya.

Pergi ke menu "settings" di dalam perangkat, kemudian submenu "security". Kemudian pilih passphrase. Anda akan melihat "Advanced feature". Klik tombol kanan, Anda akan melihat "read manual..." dan kemudian setelah klik tombol kanan lagi, Anda akan melihat "back". Tapi itu bukan akhirnya. Secara intuitif, Anda mungkin berpikir itu sudah selesai, tapi klik tombol kanan lagi. Anda akan melihat "set up passphrase".

Anda dapat memutuskan untuk "attach to PIN" atau "Set temporarily". Saya merekomendasikan "attach to the PIN". Dengan cara itu, Anda dapat mengakses dompet yang berbeda tergantung pada PIN yang Anda masukkan ketika pertama kali menyalakan perangkat. Jika Anda "set temporarily", Anda harus memasukkan passphrase setiap kali Anda ingin mengakses dompet tersebut, tapi itu selalu dari PIN default.

Masukkan passphrase dan konfirmasikan.

Ini akan meminta Anda untuk "Current PIN". Ini bukan PIN yang Anda asosiasikan dengan passphrase baru. Ini adalah PIN yang Anda masukkan ketika Anda menyalakan perangkat untuk sesi ini.

Anda sekarang dapat keluar ke menu utama dengan memilih opsi kembali beberapa kali.

## Mengawasi Dompet

Dalam artikel sebelumnya, saya menjelaskan cara mengunduh dan memverifikasi Sparrow wallet, dan cara menghubungkannya ke node Anda sendiri, atau node publik. Anda harus mengikuti panduan ini:

- Pasang Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Pasang Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)

- Hubungkan Sparrow Bitcoin Wallet ke Bitcoin Core (https://armantheparman.com/sparrowcore/)

Sebagai alternatif menggunakan Sparrow Bitcoin Wallet adalah Electrum Desktop Wallet, tapi saya akan melanjutkan menjelaskan Sparrow Bitcoin Wallet karena saya menilai itu yang terbaik untuk kebanyakan orang. Pengguna lanjutan mungkin suka menggunakan Electrum sebagai alternatif.

Kita sekarang akan memuatnya dan menghubungkan Ledger, dengan dompet yang mengandung passphrase. Dompet ini tidak pernah terpapar ke Ledger Live karena dibuat SETELAH kita menghubungkan perangkat ke Ledger Live. Pastikan Anda tidak pernah menghubungkannya ke Ledger Live lagi untuk tidak memaparkan dompet pribadi baru Anda.

Buat Dompet Baru:

![image](assets/14.webp)

Namai dengan sesuatu yang cantik

![image](assets/15.webp)

Perhatikan kotak centang, "Has existing transaction". Jika ini adalah dompet yang telah Anda gunakan sebelumnya, maka centang kotak ini, jika tidak saldo Anda akan salah ditampilkan sebagai nol. Mencentang kotak ini meminta Sparrow untuk memeriksa database Bitcoin Core (blockchain) untuk transaksi sebelumnya. Untuk panduan ini, kita menggunakan dompet baru, jadi Anda dapat meninggalkan kotak tidak dicentang.

![image](assets/16.webp)

Klik pada "Connected Hardware Wallet" dan pastikan perangkat benar-benar terhubung, dinyalakan, PIN dimasukkan, dan Anda telah memasuki Aplikasi Bitcoin.

![image](assets/17.webp)

Klik "Scan" dan kemudian "Import Keystore" di layar berikutnya.

![image](assets/18.webp)

Tidak ada yang perlu diedit di layar berikutnya, Ledger telah mengisinya untuk Anda. Klik "Apply"

![image](assets/19.webp)
Layar berikutnya memungkinkan Anda untuk menambahkan kata sandi. Jangan keliru dengan "frasa sandi"; banyak orang akan melakukannya. Penamaannya tidak beruntung. Kata sandi memungkinkan Anda untuk mengunci dompet ini di komputer Anda. Ini spesifik untuk perangkat lunak ini di komputer ini. Ini bukan bagian dari kunci pribadi Bitcoin Anda.
![image](assets/20.webp)

Setelah jeda, sementara komputer berpikir, Anda akan melihat tombol di sebelah kiri berubah dari abu-abu menjadi biru. Selamat, dompet Anda sekarang siap digunakan. Buat dan kirim transaksi sesuka hati Anda.

![image](assets/21.webp)

## Menerima

Untuk menerima beberapa bitcoin, pergi ke tab Alamat di sebelah kiri dan pilih salah satu alamat untuk menerima. Cukup klik kanan alamat yang Anda inginkan, dan pilih "salin alamat". Kemudian pergi ke bursa tempat uang dikirim dari dan tempelkan di sana. Atau Anda dapat memberikan alamat tersebut kepada pelanggan yang dapat menggunakannya untuk membayar Anda.

Ketika Anda menggunakan dompet untuk pertama kalinya, Anda harus menerima jumlah yang sangat kecil, berlatih mengirimkannya ke alamat lain, baik di dalam dompet atau kembali ke bursa, untuk membuktikan bahwa dompet berfungsi seperti yang diharapkan.

Setelah Anda melakukan itu, Anda harus mencadangkan kata-kata yang Anda tulis. Satu salinan saja tidak cukup. Miliki setidaknya dua salinan kertas (logam lebih baik), dan simpan di dua lokasi yang berbeda dan aman. Ini mengurangi risiko bencana alam menghancurkan HWW dan cadangan kertas Anda dalam satu insiden. Lihat "Menggunakan Dompet Perangkat Keras Bitcoin" untuk diskusi lengkap tentang ini.

## Mengirim

![image](assets/22.webp)

Saat melakukan pembayaran, Anda perlu menempelkan alamat yang Anda bayar di bidang "Bayar ke". Anda sebenarnya tidak bisa meninggalkan Label kosong, itu hanya untuk catatan dompet Anda sendiri, tetapi Sparrow tidak mengizinkannya - cukup masukkan sesuatu (hanya Anda yang akan melihatnya). Masukkan jumlah dan Anda juga dapat secara manual menyesuaikan biaya yang Anda inginkan.

Dompet tidak dapat menandatangani transaksi kecuali HWW terhubung. Itulah tugas HWW - untuk menerima transaksi, menandatanganinya, dan mengembalikannya, sudah ditandatangani. Pastikan saat Anda menandatangani di perangkat, Anda secara visual memeriksa alamat yang Anda bayar sama di perangkat dan di layar komputer, dan faktur yang Anda terima (misalnya Anda mungkin telah menerima email untuk membayar alamat tertentu).

Perhatikan juga jika Anda memilih untuk menggunakan koin yang lebih besar dari jumlah pembayaran, maka sisanya akan dikirim kembali ke salah satu alamat perubahan dompet Anda. Beberapa orang tidak mengetahui hal ini, dan melihat transaksi mereka di blockchain publik, dan berpikir bahwa beberapa bitcoin dikirim ke alamat penyerang, tetapi sebenarnya, itu adalah alamat perubahan mereka sendiri.

## Firmware

Untuk memperbarui firmware, Anda perlu terhubung ke Ledger Live. Jika Anda ingin melakukan ini, Anda harus menghapus perangkat terlebih dahulu, dan pastikan Anda memiliki kata-kata cadangan dan frasa sandi Anda tersedia untuk mengembalikan perangkat. Alasan saya lebih suka menghapus perangkat terlebih dahulu adalah bahwa Anda harus menghubungkan perangkat Anda ke Ledger Live untuk memperbarui firmware, dan saya lebih suka tidak memaparkan dompet baru Anda (yang dengan frasa sandi) ke Ledger Live, sama sekali. Saya hanya tidak percaya Ledger tidak mengekstrak informasi kunci publik saya dari perangkat saat saya terhubung ke Ledger Live. Mereka mengklaim mereka tidak melakukannya, tetapi saya tidak dapat memverifikasi itu sendiri kecuali saya membaca kode, dan memahami perangkat keras internal juga.

## Kesimpulan
Artikel ini menunjukkan kepada Anda cara menggunakan Ledger HWW dengan cara yang lebih aman dan lebih privat daripada yang diiklankan - tetapi artikel ini saja tidak cukup. Seperti yang saya katakan di awal, Anda harus menggabungkannya dengan informasi yang disediakan dalam "Menggunakan Dompet Perangkat Keras Bitcoin". Tips:

Alamat Lightning Statis: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/

Untuk mendalami topik ini lebih lanjut dan memperkuat keamanan dompet Anda di Ledger Nano dengan passphrase BIP39, saya mengundang Anda untuk memeriksa tutorial lengkap ini:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

