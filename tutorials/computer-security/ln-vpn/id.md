---
name: LN VPN

description: Mengatur VPN Anda
---

![image](assets/cover.webp)

LN VPN adalah layanan VPN yang dapat disesuaikan dan hanya menerima pembayaran melalui lightning. Hari ini, saya akan menunjukkan cara menggunakannya dan meninggalkan jejak lebih sedikit saat menjelajahi internet.

Ada banyak penyedia layanan VPN berkualitas, dan kami telah melakukan tinjauan komprehensif dalam artikel ini (hyperlink). Namun, LN VPN menonjol, dan kami tidak ingin melewatkan kesempatan untuk memperkenalkannya kepada Anda.

Sebagian besar penyedia layanan VPN seperti ProtonVPN dan Mullvad menawarkan opsi untuk membayar dengan bitcoin tetapi memerlukan pembuatan akun dan pembelian paket untuk jangka waktu yang lebih panjang atau lebih pendek, yang mungkin tidak sesuai dengan anggaran setiap orang.

LN VPN memungkinkan penggunaan VPN sesuai permintaan untuk sesingkat satu jam, berkat implementasi pembayaran bitcoin melalui jaringan lightning. Pembayaran lightning yang instan dan anonim, membuka dunia kemungkinan untuk mikropembayaran.

> 💡 Panduan ini menjelaskan cara menggunakan LN VPN dari sistem Linux Ubuntu 22.04 LTS.

## Prasyarat: Wireguard

Dalam istilah sederhana, Wireguard digunakan untuk membuat terowongan aman antara komputer Anda dan server jarak jauh yang akan Anda gunakan untuk menjelajahi Internet. Alamat IP dari server ini yang akan muncul sebagai milik Anda selama durasi sewa yang akan Anda kontrak dengan mengikuti panduan ini.

Panduan instalasi Wireguard resmi: https://www.wireguard.com/install/

```
Instalasi Wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Prasyarat: Dompet Bitcoin Lightning

Jika Anda belum memiliki dompet Bitcoin Lightning, tidak perlu khawatir, kami telah membuat panduan yang sangat sederhana untuk Anda di sini. (bagian tutorial LN dapat membantu Anda)

## Langkah 1: Mengontrak Sewa

Dari https://lnvpn.com, Anda perlu memilih negara dari IP keluar terowongan VPN dan durasi. Setelah parameter ini diatur, klik pada Bayar dengan lightning.

![image](assets/1.webp)

Sebuah invoice lightning akan ditampilkan, dan Anda hanya perlu memindainya dengan dompet lightning Anda.

Setelah invoice dibayar, Anda perlu menunggu beberapa detik hingga dua menit untuk pengaturan konfigurasi Wireguard Anda dihasilkan. Jika membutuhkan waktu sedikit lebih lama, jangan panik, kami telah melakukan prosedur ini puluhan kali, dan terkadang memang membutuhkan waktu sedikit lebih lama.
Layar berikutnya akan muncul dan Anda hanya perlu mengklik "Download as File" untuk menerima file konfigurasi Anda, yang akan memiliki nama seperti lnvpn-xx-xx.conf di mana "xx" akan sesuai dengan tanggal saat ini.
![image](assets/2.webp)

## Langkah 2: Mengaktifkan terowongan

Pertama, Anda perlu mengganti nama file konfigurasi yang diperoleh pada langkah sebelumnya agar dapat secara otomatis dikenali oleh Wireguard.

Pergi ke folder unduhan Anda, baik dalam jendela terminal atau dengan penjelajah file, dan ganti nama file lnvpn-xx-xx.conf menjadi wg0.conf seperti ini:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Sekarang! Terowongan diaktifkan!

## Langkah 3: Verifikasi

Gunakan layanan online seperti whatismyip untuk memverifikasi bahwa alamat IP publik Anda sekarang adalah dari VPN yang baru saja Anda aktifkan.

## Langkah 4: Menonaktifkan
Ketika masa sewa Anda berakhir, Anda perlu menonaktifkan koneksi untuk mendapatkan kembali akses ke internet. Anda kemudian dapat mengulangi langkah 1 sampai 3 kapan pun Anda ingin menetapkan sewa dengan LN VPN.
Menonaktifkan terowongan:

```
    $ sudo ip link delete dev wg0
```

Itu dia! Anda sekarang tahu cara menggunakan LN VPN, layanan VPN yang unik!