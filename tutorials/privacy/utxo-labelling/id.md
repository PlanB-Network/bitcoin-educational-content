---
name: Pelabelan UTXO
description: Bagaimana cara melabeli UTXO Anda dengan tepat?
---
![cover](assets/cover.webp)

Dalam tutorial ini, Anda akan menemukan segala hal yang perlu Anda ketahui tentang pelabelan UTXO di dompet Bitcoin Anda dan tentang kontrol koin. Kami memulai dengan bagian teoretis untuk sepenuhnya memahami konsep-konsep ini, sebelum beralih ke bagian praktis di mana kami menjelajahi cara menggunakan label secara konkret dalam perangkat lunak dompet Bitcoin utama.

## Apa itu pelabelan UTXO?
"Pelabelan" adalah teknik yang melibatkan pengaitan anotasi atau label dengan UTXO spesifik dalam dompet Bitcoin. Anotasi ini disimpan secara lokal oleh perangkat lunak dompet dan tidak pernah ditransmisikan melalui jaringan Bitcoin. Dengan demikian, pelabelan adalah alat untuk manajemen pribadi.

Sebagai contoh, jika saya menerima UTXO dari transaksi P2P melalui Bisq dengan Charles, saya bisa menetapkannya label `Bisq P2P Purchase Charles`.

Pelabelan memungkinkan seseorang untuk mengingat asal atau tujuan yang dimaksudkan dari UTXO, yang menyederhanakan manajemen dana dan mengoptimalkan privasi pengguna. Pelabelan menjadi lebih relevan ketika dikombinasikan dengan fungsi "kontrol koin". Kontrol koin adalah opsi yang tersedia di dompet Bitcoin yang baik, yang memberikan kemampuan kepada pengguna untuk secara manual memilih UTXO spesifik mana yang akan digunakan sebagai input saat membuat transaksi.

Menggunakan dompet dengan kontrol koin, dipasangkan dengan pelabelan UTXO, memungkinkan pengguna untuk secara tepat membedakan dan memilih UTXO untuk transaksi mereka, sehingga menghindari penggabungan UTXO dari sumber yang berbeda. Praktik ini mengurangi risiko yang terkait dengan Heuristik Kepemilikan Input Bersama (CIOH), yang menyarankan kepemilikan bersama dari input sebuah transaksi, yang dapat mengompromikan privasi pengguna.

Mari kita kembali ke contoh UTXO no-KYC saya dari Bisq; saya ingin menghindari menggabungkannya dengan UTXO yang datang, katakanlah, dari platform pertukaran yang diatur yang mengetahui identitas saya. Dengan menempatkan label yang berbeda pada UTXO no-KYC saya dan pada UTXO KYC saya, saya akan dapat dengan mudah mengidentifikasi UTXO mana yang akan dikonsumsi sebagai input untuk memenuhi pengeluaran, menggunakan fungsi kontrol koin.

## Bagaimana cara melabeli UTXO Anda dengan tepat?
Tidak ada metode universal untuk pelabelan UTXO yang cocok untuk semua orang. Terserah Anda untuk menentukan sistem pelabelan sehingga Anda dapat dengan mudah menemukan jalan Anda di sekitar dompet Anda.
Kriteria penting dalam pelabelan adalah sumber dari UTXO. Anda harus cukup menunjukkan bagaimana koin ini tiba di dompet Anda. Apakah itu dari platform pertukaran? Penyelesaian tagihan oleh klien? Pertukaran peer-to-peer? Atau apakah itu mewakili kembalian dari pembelian? Dengan demikian, Anda bisa menentukan:
- `Withdrawal Exchange.com`;
- `Payment Client David`;
- `P2P Purchase Charles`;
- `Change from sofa purchase`.
![labelling](assets/en/1.webp)
Untuk menyempurnakan manajemen UTXO Anda dan mematuhi strategi segregasi dana Anda dalam dompet, Anda bisa memperkaya label Anda dengan indikator tambahan yang mencerminkan pemisahan ini. Jika dompet Anda berisi dua kategori UTXO yang tidak ingin Anda campur, Anda bisa mengintegrasikan penanda dalam label Anda untuk dengan jelas membedakan kelompok-kelompok ini.

Penanda pemisahan ini akan bergantung pada kriteria Anda sendiri, seperti perbedaan antara UTXO KYC (mengetahui identitas Anda) dan no-KYC (anonim), atau antara dana profesional dan pribadi. Mengambil contoh label yang disebutkan sebelumnya, ini bisa diterjemahkan sebagai:
- `KYC - Withdrawal Exchange.com`;
- `KYC - Payment Client David`;
- `NO KYC - P2P Purchase Charles`;
- `NO KYC - Change from sofa purchase`.
![pelabelan](assets/en/2.webp)Dalam setiap kasus, ingatlah bahwa pelabelan yang baik adalah pelabelan yang dapat Anda pahami ketika Anda membutuhkannya. Jika dompet Bitcoin Anda terutama ditujukan untuk tabungan, mungkin label tersebut hanya akan berguna bagi Anda dalam beberapa dekade. Oleh karena itu, pastikan mereka jelas, tepat, dan komprehensif.

Disarankan juga untuk mempertahankan pelabelan sebuah koin sepanjang transaksi. Misalnya, selama konsolidasi UTXO tanpa-KYC, pastikan untuk menandai UTXO yang dihasilkan tidak hanya sebagai `konsolidasi`, tetapi secara spesifik sebagai `konsolidasi tanpa-KYC` untuk menjaga jejak asal koin yang jelas.

Akhirnya, tidak wajib untuk menaruh tanggal pada label. Kebanyakan perangkat lunak dompet sudah menampilkan tanggal transaksi, dan selalu mungkin untuk mengambil informasi ini di block explorer menggunakan TXID-nya.

## Tutorial: Pelabelan di Specter Desktop

Hubungkan dan buka dompet Anda di Specter Desktop, kemudian pilih tab `Alamat`.

![pelabelan](assets/notext/3.webp)
Di sini, Anda akan melihat daftar semua alamat Anda, serta bitcoin apa saja yang terkunci di dalamnya. Secara default, alamat diidentifikasi oleh indeksnya di bawah kolom `Label`. Untuk mengubah label, cukup klik pada label tersebut, masukkan label yang diinginkan, dan kemudian konfirmasi dengan mengklik ikon biru.
![pelabelan](assets/notext/4.webp)

Label Anda kemudian akan muncul dalam daftar alamat Anda.

![pelabelan](assets/notext/5.webp)

Anda juga dapat menetapkan label terlebih dahulu, saat Anda berbagi alamat penerima Anda dengan pengirim. Untuk melakukan ini, dengan mengakses tab `Terima`, catat label Anda di kolom yang disediakan.

![pelabelan](assets/notext/6.webp)

## Tutorial: Pelabelan di Electrum

Di Dompet Electrum, setelah masuk ke dompet Anda, klik pada transaksi yang ingin Anda beri label dari tab `Riwayat`.

![pelabelan](assets/notext/7.webp)

Sebuah jendela baru terbuka. Klik pada kotak `Deskripsi` dan ketik label Anda.

![pelabelan](assets/notext/8.webp)

Setelah label dimasukkan, Anda dapat menutup jendela ini.

![pelabelan](assets/notext/9.webp)

Label Anda telah berhasil disimpan. Anda dapat menemukannya di bawah tab `Deskripsi`.

![pelabelan](assets/notext/10.webp)

Di tab `Koin`, dari mana Anda dapat melakukan kontrol koin, label Anda ditemukan di kolom `Label`.

![pelabelan](assets/notext/11.webp)

## Tutorial: Pelabelan di Green Wallet

Di aplikasi Green Wallet, akses dompet Anda dan pilih transaksi yang ingin Anda beri label. Kemudian, klik pada ikon pensil kecil untuk mencatat label Anda.

![pelabelan](assets/notext/12.webp)

Ketik label Anda, lalu klik tombol `Simpan` hijau.

![pelabelan](assets/notext/13.webp)

Anda akan dapat menemukan label Anda baik dalam detail transaksi Anda maupun di dashboard dompet Anda.

![pelabelan](assets/notext/14.webp)

## Tutorial: Pelabelan di Samourai Wallet

Di Samourai Wallet, ada beberapa metode yang memungkinkan Anda untuk memberikan label pada transaksi. Untuk yang pertama, mulailah dengan membuka dompet Anda dan pilih transaksi yang ingin Anda tambahkan label. Kemudian tekan tombol `Tambah`, yang terletak di sebelah kotak `Catatan`.

![pelabelan](assets/notext/15.webp)
Ketik label Anda dan konfirmasi dengan mengklik tombol biru `Add`.
![labelling](assets/notext/16.webp)

Anda akan menemukan label Anda dalam detail transaksi Anda, tetapi juga di dashboard dompet Anda.

![labelling](assets/notext/17.webp)
Untuk metode kedua, klik pada tiga titik kecil di pojok kanan atas layar, kemudian pada menu `Show Unspent Transaction Outputs`.
![labelling](assets/notext/18.webp)

Di sini, Anda akan menemukan daftar lengkap semua UTXO yang ada di dompet Anda. Daftar yang ditampilkan berkaitan dengan akun deposit saya, namun, operasi ini dapat direplikasi untuk akun Whirlpool dengan menavigasi dari menu khusus.

Kemudian klik pada UTXO yang ingin Anda labeli, diikuti dengan tombol `Add`.

![labelling](assets/notext/19.webp)

Ketik label Anda dan konfirmasi dengan mengklik tombol biru `Add`. Anda kemudian akan menemukan label Anda baik dalam detail transaksi Anda maupun di dashboard dompet Anda.

![labelling](assets/notext/20.webp)

## Tutorial: Pelabelan di Sparrow Wallet

Dengan perangkat lunak Sparrow Wallet, dimungkinkan untuk menetapkan label dengan beberapa cara. Metode paling sederhana adalah menambahkan label di muka, saat mengkomunikasikan alamat penerima kepada pengirim. Untuk melakukan ini, dalam menu `Receive`, klik pada kolom `Label` dan masukkan label pilihan Anda. Ini akan dipertahankan dan dapat diakses di seluruh perangkat lunak segera setelah bitcoin diterima di alamat tersebut.

![labelling](assets/notext/21.webp)

Jika Anda lupa memberi label pada alamat Anda saat penerimaan, masih dimungkinkan untuk menambahkan satu nanti melalui menu `Transactions`. Cukup klik pada transaksi Anda dalam kolom `Label`, kemudian masukkan label yang diinginkan.

![labelling](assets/notext/22.webp)

Anda juga memiliki opsi untuk menambahkan atau memodifikasi label Anda dari menu `Addresses`.

![labelling](assets/notext/23.webp)

Akhirnya, Anda dapat melihat label Anda di menu `UTXOs`. Sparrow Wallet secara otomatis menambahkan dalam tanda kurung di belakang label Anda sifat dari output, yang membantu untuk membedakan UTXO yang dihasilkan dari perubahan dari yang diterima secara langsung.

![labelling](assets/notext/24.webp)