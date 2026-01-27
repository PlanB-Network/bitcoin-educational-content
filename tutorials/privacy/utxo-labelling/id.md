---
name: Labelling UTXO
description: Bagaimana cara melabeli UTXO dengan tepat?
---
![cover](assets/cover.webp)

Dalam tutorial ini, kamu akan menemukan segala hal yang perlu kamu ketahui tentang pelabelan UTXO di dompet Bitcoin kamu dan tentang kontrol koin. Kita mulai dengan bagian teoretis untuk benar-benar memahami konsep-konsep ini, sebelum lanjut ke bagian praktis di mana kita menjelajahi cara memakai label secara konkret di perangkat lunak dompet Bitcoin utama.

## Apa itu pelabelan UTXO?
"Pelabelan" adalah teknik yang melibatkan pengaitan anotasi atau label dengan UTXO tertentu di dalam dompet Bitcoin kamu. Anotasi ini disimpan secara lokal oleh perangkat lunak dompet dan tidak pernah dikirim melalui jaringan Bitcoin. Jadi, pelabelan adalah alat untuk manajemen pribadi.

Sebagai contoh, kalau aku menerima UTXO dari transaksi P2P lewat Bisq dengan Charles, aku bisa kasih label 'Bisq P2P Purchase Charles'.

Pelabelan memungkinkan seseorang untuk mengingat asal atau tujuan dari UTXO, yang mempermudah manajemen dana dan mengoptimalkan privasi pengguna. Pelabelan makin relevan ketika dipadukan dengan fungsi "kontrol koin". Kontrol koin adalah opsi yang tersedia di dompet Bitcoin yang bagus, yang memberi kemampuan kepada pengguna untuk secara manual memilih UTXO tertentu mana yang akan dipakai sebagai input saat membuat transaksi.

Memakai dompet dengan kontrol koin, dipasangkan dengan pelabelan UTXO, memungkinkan pengguna untuk dengan tepat membedakan dan memilih UTXO untuk transaksi mereka, sehingga menghindari penggabungan UTXO dari sumber yang berbeda. Praktik ini mengurangi risiko yang terkait dengan Heuristik Kepemilikan Input Bersama (CIOH), yang menyarankan adanya kepemilikan bersama dari input sebuah transaksi, yang bisa mengompromikan privasi pengguna.

Mari balik ke contoh UTXO no-KYC aku dari Bisq; aku ingin menghindari menggabungkannya dengan UTXO yang datang, misalnya, dari platform pertukaran yang diatur yang mengetahui identitasku. Dengan memberi label berbeda pada UTXO no-KYC aku dan pada UTXO KYC aku, aku bisa dengan mudah mengenali UTXO mana yang akan dipakai sebagai input untuk memenuhi pengeluaran, memakai fungsi kontrol koin.

## Bagaimana cara melabeli UTXO Anda dengan tepat?
Tidak ada metode universal untuk pelabelan UTXO yang cocok untuk semua orang. Terserah kamu untuk menentukan sistem pelabelan supaya kamu bisa dengan mudah menemukan jalan di dalam dompet kamu.
Kriteria penting dalam pelabelan adalah sumber dari UTXO. Kamu harus cukup menjelaskan bagaimana koin itu sampai ke dompet kamu. Apakah itu dari platform pertukaran? Pelunasan tagihan oleh klien? Pertukaran peer-to-peer? Atau apakah itu kembalian dari pembelian? Dengan begitu, kamu bisa menentukan:

- `Withdrawal Exchange.com`;
- `Payment Client David`;
- `P2P Purchase Charles`;
- `Change from sofa purchase`.
![labelling](assets/en/1.webp)

Untuk menyempurnakan manajemen UTXO kamu dan mengikuti strategi pemisahan dana kamu di dalam dompet, kamu bisa memperkaya label kamu dengan indikator tambahan yang mencerminkan pemisahan itu. Jika dompet kamu berisi dua kategori UTXO yang tidak ingin kamu campur, kamu bisa memasukkan penanda dalam label kamu untuk dengan jelas membedakan kelompok tersebut.

Penanda pemisahan ini akan bergantung pada kriteria kamu sendiri, seperti perbedaan antara UTXO KYC (mengetahui identitas kamu) dan no-KYC (anonim), atau antara dana profesional dan pribadi. Mengambil contoh label yang disebutkan sebelumnya, ini bisa diterjemahkan sebagai:

- `KYC - Withdrawal Exchange.com`;
- `KYC - Payment Client David`;
- `NO KYC - P2P Purchase Charles`;
- `NO KYC - Change from sofa purchase`.
![pelabelan](assets/en/2.webp) Dalam setiap kasus, ingatlah bahwa pelabelan yang baik adalah pelabelan yang bisa kamu pahami ketika kamu membutuhkannya. Jika dompet Bitcoin kamu terutama ditujukan untuk tabungan, bisa jadi label itu baru akan berguna buat kamu beberapa dekade lagi. Jadi, pastikan label tersebut jelas, tepat, dan lengkap.

Disarankan juga untuk mempertahankan pelabelan sebuah koin sepanjang transaksi. Misalnya, saat konsolidasi UTXO no-KYC, pastikan untuk menandai UTXO yang dihasilkan bukan hanya sebagai 'konsolidasi', tetapi secara spesifik sebagai 'konsolidasi no-KYC' supaya jejak asal koin tetap jelas.

Akhirnya, tidak wajib menaruh tanggal pada label. Kebanyakan perangkat lunak dompet sudah menampilkan tanggal transaksi, dan kamu selalu bisa mengambil informasi ini di block explorer dengan memakai TXID-nya.

## Tutorial: Pelabelan di Specter Desktop

Hubungkan dan buka dompet Anda di Specter Desktop, kemudian pilih tab `Alamat`.

![pelabelan](assets/notext/3.webp)
Di sini, kamu akan melihat daftar semua alamat kamu, serta bitcoin yang terkunci di dalamnya. Secara default, alamat diidentifikasi oleh indeksnya di bawah kolom Label. Untuk mengubah label, cukup klik pada label itu, masukkan 'label' yang kamu inginkan, lalu konfirmasi dengan mengklik ikon biru.
![pelabelan](assets/notext/4.webp)

Label kamu kemudian akan muncul di daftar alamat kamu.

![pelabelan](assets/notext/5.webp)

Kamu juga bisa menetapkan label terlebih dahulu saat kamu berbagi alamat penerima kamu dengan pengirim. Untuk melakukan ini, buka tab 'Terima', lalu isi label kamu di kolom yang disediakan.

![pelabelan](assets/notext/6.webp)

## Tutorial: Pelabelan di Electrum

Di Dompet Electrum, setelah masuk ke dompet kamu, klik pada transaksi yang ingin kamu beri label dari tab `Riwayat`.

![pelabelan](assets/notext/7.webp)

Sebuah jendela baru terbuka. Klik pada kotak `Deskripsi` dan ketik label kamu.

![pelabelan](assets/notext/8.webp)

Setelah label dimasukkan, kamu dapat menutup jendela ini.

![pelabelan](assets/notext/9.webp)

Label kamu telah berhasil disimpan. Kamu dapat menemukannya di bawah tab `Deskripsi`.

![pelabelan](assets/notext/10.webp)

Di tab `Koin`, dari mana kamu dapat melakukan kontrol koin, label kamu ditemukan di kolom `Label`.

![pelabelan](assets/notext/11.webp)

## Tutorial: Pelabelan di Green Wallet

Di aplikasi Green Wallet, buka dompet kamu dan pilih transaksi yang ingin kamu beri label. Setelah itu, klik ikon pensil kecil untuk memasukkan label kamu.

![pelabelan](assets/notext/12.webp)

Ketik label kamu, lalu klik tombol `Simpan` hijau.

![pelabelan](assets/notext/13.webp)

Kamu bisa menemukan label kamu baik di detail transaksi maupun di dashboard dompet kamu.

![pelabelan](assets/notext/14.webp)

## Tutorial: Pelabelan di Samourai Wallet

Di Samourai Wallet, ada beberapa cara yang memungkinkan kamu memberi label pada transaksi. Untuk cara pertama, buka dulu dompet kamu dan pilih transaksi yang ingin kamu tambahkan label. Lalu tekan tombol 'Tambah', yang ada di sebelah kotak 'Catatan'.

![pelabelan](assets/notext/15.webp)
Ketik label kamu dan konfirmasi dengan mengklik tombol biru `Add`.
![labelling](assets/notext/16.webp)

Kamu akan menemukan label dalam detail transaksi kamu, tetapi juga di dashboard dompet kamu.

![labelling](assets/notext/17.webp)
Untuk metode kedua, klik pada tiga titik kecil di pojok kanan atas layar, kemudian pada menu `Show Unspent Transaction Outputs`.
![labelling](assets/notext/18.webp)

Di sini, kamu akan menemukan daftar lengkap semua UTXO yang ada di dompet kamu. Daftar yang ditampilkan berkaitan dengan akun deposit aku, tapi operasi ini bisa direplikasi untuk akun Whirlpool dengan menavigasi lewat menu khusus.

Lalu klik UTXO yang ingin kamu beri label, kemudian tekan tombol 'Add'.

![labelling](assets/notext/19.webp)

Ketik label kamu dan konfirmasi dengan menekan tombol biru 'Add'. Kamu kemudian akan menemukan label kamu baik di detail transaksi maupun di dashboard dompet kamu.

![labelling](assets/notext/20.webp)

## Tutorial: Pelabelan di Sparrow Wallet

Dengan perangkat lunak Sparrow Wallet, kamu bisa menetapkan label dengan beberapa cara. Metode paling sederhana adalah menambahkan label di muka saat kamu mengirimkan alamat penerima ke pengirim. Untuk melakukan ini, di menu 'Receive', klik kolom 'Label' dan masukkan label pilihan kamu. Label ini akan disimpan dan bisa diakses di seluruh perangkat lunak begitu bitcoin diterima di alamat tersebut.

![labelling](assets/notext/21.webp)

Jika kamu lupa memberi label pada alamat kamu saat menerima, kamu tetap bisa menambahkannya nanti lewat menu 'Transactions'. Cukup klik transaksi kamu di kolom 'Label', lalu masukkan label yang kamu inginkan.

![labelling](assets/notext/22.webp)

Kamu juga memiliki opsi untuk menambahkan atau memodifikasi label kamu dari menu `Addresses`.

![labelling](assets/notext/23.webp)

Akhirnya, kamu bisa melihat label kamu di menu 'UTXOs'. Sparrow Wallet secara otomatis menambahkan dalam tanda kurung di belakang label kamu sifat dari output, yang membantu membedakan UTXO yang berasal dari kembalian dan yang diterima secara langsung.

![labelling](assets/notext/24.webp)
