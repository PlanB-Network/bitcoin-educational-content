---
name: Watch Tower
description: Memahami dan menggunakan menara pengawas
---

## Bagaimana menara pengawas bekerja?

Sebagai bagian penting dari ekosistem Lightning Network, menara pengawas memberikan tingkat perlindungan tambahan kepada saluran petir pengguna. Tanggung jawab utamanya adalah untuk mengawasi kesehatan saluran dan mengintervensi jika salah satu pihak saluran mencoba menipu pihak lain.

Jadi, bagaimana menara pengawas dapat menentukan jika sebuah saluran telah dikompromikan? Menara pengawas menerima informasi yang dibutuhkan dari klien, salah satu pihak saluran, untuk dapat mengidentifikasi dan merespons setiap pelanggaran dengan tepat. Detail transaksi terbaru, kondisi saluran saat ini, dan informasi yang diperlukan untuk membuat transaksi penalti seringkali termasuk dalam informasi ini. Sebelum mengirimkan data ke menara pengawas, klien mungkin mengenkripsinya untuk melindungi privasi dan kerahasiaan. Ini mencegah menara pengawas dari mendekripsi data yang dienkripsi kecuali jika pelanggaran benar-benar telah terjadi, meskipun data tersebut diterima. Sistem enkripsi ini melindungi privasi klien dan juga mencegah menara pengawas mengakses data pribadi tanpa otorisasi.

## Bagaimana cara menyiapkan Eye of Satoshi Anda sendiri dan mulai berkontribusi

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) adalah menara pengawas Lightning non-custodial yang sesuai dengan [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Ini memiliki dua komponen utama:

1. teos: termasuk CLI dan fungsionalitas inti sisi server dari menara. Dua biner—teosd dan teos-cli—akan diproduksi ketika crate ini dibangun.

2. teos-common: Termasuk fungsionalitas bersama sisi server dan sisi klien (berguna untuk membuat klien).

Untuk menjalankan menara dengan sukses, Anda akan membutuhkan bitcoind yang berjalan sebelum menjalankan menara dengan perintah teosd. Sebelum menjalankan kedua perintah ini Anda perlu menyiapkan file bitcoin.conf Anda. Berikut adalah langkah-langkah tentang cara melakukannya:-

1. Pasang bitcoin core dari sumber atau unduh. Setelah mengunduh, letakkan file bitcoin.conf di direktori pengguna Bitcoin core. Periksa tautan ini untuk informasi lebih lanjut mengenai di mana meletakkan file tersebut karena tergantung pada sistem operasi yang Anda gunakan.

2. Setelah mengidentifikasi tempat di mana file perlu dibuat, tambahkan opsi-opsi ini:-

'''
#RPC
server=1
rpcuser=<nama-pengguna>
rpcpassword=<kata-sandi>

#chain
regtest=1
'''

- server: Untuk permintaan RPC
- rpcuser dan rpcpassword: Klien RPC dapat mengautentikasi dengan server
- regtest: Tidak diperlukan tetapi berguna jika Anda merencanakan untuk pengembangan.

rpcuser dan rpcpassword perlu Anda pilih. Mereka harus ditulis tanpa tanda kutip. Misal:-

'''
rpcuser=aniketh
rpcpassword=strongpassword
'''

Sekarang, jika Anda menjalankan bitcoind, itu seharusnya mulai menjalankan node.

1. Untuk bagian menara, pertama, Anda harus memasang teos dari sumber. Ikuti instruksi yang diberikan di tautan ini.

2. Setelah berhasil memasang teos di sistem Anda dan menjalankan tes, Anda dapat melanjutkan dengan langkah terakhir yaitu menyiapkan file teos.toml di direktori pengguna teos. File perlu ditempatkan dalam folder bernama .teos (perhatikan titiknya) di bawah folder home Anda. Yaitu, misalnya, /home/<nama-pengguna>/.teos untuk Linux. Setelah Anda menemukan tempatnya, buat file teos.toml dan atur opsi-opsi ini sesuai dengan perubahan yang telah kita lakukan pada bitcoind.
#bitcoindbtc_network = "regtest"
btc_rpc_user = <nama-pengguna-anda>
btc_rpc_password = <kata-sandi-anda>

Perhatikan bahwa di sini nama pengguna dan kata sandi perlu ditulis dalam tanda kutip, yaitu, untuk contoh yang sama seperti sebelumnya:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
'''

Setelah Anda melakukan itu, Anda seharusnya sudah siap untuk menjalankan tower. Mengingat kita berjalan di regtest, kemungkinan tidak akan ada blok yang ditambang di jaringan tes bitcoin kita pada kali pertama tower terhubung kepadanya (jika ada, pasti ada yang salah). Tower membangun cache internal dari 100 blok terakhir dari bitcoind, jadi saat berjalan untuk pertama kali kita mungkin mendapatkan kesalahan berikut:

> ERROR [teosd] Tidak cukup blok untuk memulai tower (dibutuhkan: 100). Tambang setidaknya 100 blok lagi

Mengingat kita berjalan di regtest, kita dapat menambang blok dengan mengeluarkan perintah RPC, tanpa perlu menunggu waktu median 10 menit yang biasanya kita lihat di jaringan lain (seperti mainnet atau testnet). Periksa bantuan bitcoin-cli dan cari cara untuk menambang blok. Jika Anda memerlukan bantuan, Anda dapat membaca artikel ini.

![image](assets/2.webp)

Itu dia, Anda telah berhasil menjalankan tower. Selamat. 🎉