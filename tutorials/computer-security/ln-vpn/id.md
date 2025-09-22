---
name: LN VPN

description: Konfigurasikan LN VPN dengan Lightning untuk VPN anonim dan sesuai permintaan
---

![image](assets/cover.webp)

LN VPN adalah layanan VPN yang dapat disesuaikan dan hanya menerima pembayaran melalui Lightning Network. Hari ini, saya akan menunjukkan cara menggunakannya dan meninggalkan jejak yang lebih sedikit saat menjelajahi internet.

Ada banyak penyedia layanan VPN berkualitas, dan kami telah melakukan tinjauan komprehensif dalam artikel ini (hyperlink). Namun, LN VPN menonjol, dan kami tidak ingin melewatkan kesempatan untuk memperkenalkannya kepada Anda.

Sebagian besar penyedia layanan VPN seperti ProtonVPN dan Mullvad menawarkan opsi pembayaran dengan Bitcoin tetapi mensyaratkan pembuatan akun dan pembelian paket untuk jangka waktu yang lebih panjang atau lebih pendek, yang mungkin tidak sesuai dengan anggaran semua orang.

LN VPN memungkinkan penggunaan VPN sesuai kebutuhan, bahkan untuk durasi sesingkat satu jam, berkat implementasi pembayaran Bitcoin melalui Lightning Network. Pembayaran Lightning yang instan dan anonim, membuka dunia kemungkinan untuk pembayaran mikro.

> 💡 **Panduan ini menjelaskan cara menggunakan LN VPN dari sistem Linux Ubuntu 22.04 LTS.**

## Prasyarat: Wireguard

Dalam istilah sederhana, Wireguard digunakan untuk membuat terowongan aman antara komputer Anda dan server jarak jauh yang akan Anda gunakan untuk menjelajahi Internet. Alamat IP dari server ini yang akan muncul sebagai milik Anda selama durasi sewa yang akan Anda kontrak dengan mengikuti panduan ini.

Secara sederhana, WireGuard digunakan untuk menciptakan sambungan aman antara komputer Anda dan server jarak jauh. Melalui sambungan inilah Anda akan menjelajahi internet. Selama durasi sewa yang Anda kontrak dengan mengikuti panduan ini, alamat IP server tersebutlah yang akan muncul sebagai alamat IP Anda.

Panduan instalasi Wireguard resmi: https://www.wireguard.com/install/

```
Instalasi Wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Prasyarat: Dompet Bitcoin Lightning

Jika Anda belum memiliki dompet Bitcoin Lightning, jangan khawatir, kami telah membuat panduan yang sangat sederhana untuk Anda di sini. (bagian tutorial LN dapat membantu Anda)

## Langkah 1: Mengontrak Sewa

Pada https://lnvpn.com, Anda perlu memilih negara dari alamat IP keluar dari sambungan VPN dan durasinya. Setelah parameter ini diatur, klik "Bayar dengan Lightning".
![image](assets/1.webp)

Invoice Lightning akan ditampilkan, dan Anda hanya perlu memindainya dengan dompet Lightning Anda.

Setelah invoice terbayar, Anda perlu menunggu beberapa detik hingga dua menit agar pengaturan konfigurasi Wireguard Anda dihasilkan. Jika memakan waktu sedikit lebih lama, jangan panik; kami telah melakukan prosedur ini puluhan kali, dan terkadang memang membutuhkan waktu sedikit lebih lama.

Berikut adalah teks yang telah diterjemahkan ke dalam bahasa Inggris, dengan mempertahankan tata letak markdown yang sama seperti teks aslinya:

Layar selanjutnya akan muncul dan Anda hanya perlu mengeklik "Download as File" untuk menerima file konfigurasi Anda. Nama file tersebut akan terlihat seperti lnvpn-xx-xx.conf, dengan "xx" merujuk pada tanggal saat ini.
![image](assets/2.webp)

## Langkah 2: Mengaktifkan terowongan

Pertama, Anda perlu mengganti nama file konfigurasi yang Anda dapatkan di langkah sebelumnya agar bisa otomatis dikenali oleh WireGuard.

Buka folder unduhan Anda, baik melalui terminal atau file explorer, lalu ganti nama file lnvpn-xx-xx.conf menjadi wg0.conf. Contohnya seperti ini:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Sekarang! sambungan sudah aktif!

## Langkah 3: Verifikasi

Gunakan layanan online seperti whatismyip untuk memverifikasi bahwa alamat IP publik Anda kini adalah alamat dari VPN yang baru saja Anda aktifkan.

## Langkah 4: Menonaktifkan

Ketika masa sewa Anda habis, Anda perlu memutus koneksi untuk bisa kembali mengakses internet. Setelah itu, Anda bisa mengulangi langkah 1 hingga 3 kapan pun Anda ingin membuat sewa baru dengan LN VPN.

Menonaktifkan sambungan:

```
    $ sudo ip link delete dev wg0
```

Itu dia! Anda sekarang tahu cara menggunakan LN VPN, layanan VPN yang unik!
