---
name: GnuPG
description: Bagaimana cara memverifikasi integritas dan keaslian perangkat lunak?
---
![cover](assets/cover.webp)

Saat mengunduh perangkat lunak, sangat penting untuk memastikan bahwa perangkat lunak tersebut tidak telah diubah dan memang berasal dari sumber resmi. Hal ini terutama berlaku untuk perangkat lunak yang terkait dengan Bitcoin, seperti perangkat lunak dompet, yang memungkinkan Anda untuk mengamankan kunci yang memberikan akses ke dana Anda. Dalam tutorial ini, kita akan melihat cara memverifikasi integritas dan keaslian perangkat lunak sebelum menginstalnya. Kita akan menggunakan Sparrow Wallet sebagai contoh, sebuah perangkat lunak dompet favorit di kalangan pengguna bitcoin, tetapi prosedurnya akan sama untuk perangkat lunak lainnya.

Memverifikasi integritas melibatkan memastikan bahwa file yang diunduh tidak telah dimodifikasi dengan membandingkan sidik digitalnya (yaitu, hashnya) dengan yang disediakan oleh pengembang resmi. Jika keduanya cocok, itu berarti bahwa file tersebut identik dengan aslinya dan tidak telah rusak atau dimodifikasi oleh penyerang.

Di sisi lain, memverifikasi keaslian memastikan bahwa file tersebut memang berasal dari pengembang resmi dan bukan peniru. Hal ini dilakukan dengan memverifikasi tanda tangan digital. Tanda tangan ini membuktikan bahwa perangkat lunak telah ditandatangani dengan kunci privat pengembang yang sah.

Jika pemeriksaan ini tidak dilakukan, ada risiko menginstal malware yang dapat berisi kode yang dimodifikasi. Kode ini dapat mencuri informasi seperti kunci privat Anda atau memblokir akses ke file Anda. Jenis serangan ini cukup umum, terutama dalam konteks perangkat lunak sumber terbuka di mana versi palsu dapat didistribusikan.

Untuk melakukan verifikasi ini, kita akan menggunakan dua alat: fungsi hashing untuk memverifikasi integritas, dan GnuPG, sebuah alat sumber terbuka yang mengimplementasikan protokol PGP, untuk memverifikasi keaslian.

## Prasyarat

Jika Anda menggunakan **Linux**, GPG sudah terpasang di sebagian besar distribusi. Jika tidak, Anda dapat menginstalnya dengan perintah berikut:

```bash
sudo apt install gnupg
```

Untuk **macOS**, jika Anda belum menginstal manajer paket Homebrew, lakukan dengan perintah berikut:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Kemudian instal GPG dengan perintah ini:

```bash
brew install gnupg
```
Untuk **Windows**, jika Anda tidak memiliki GPG, Anda dapat menginstal perangkat lunak [Gpg4win](https://www.gpg4win.org/).
![GnuPG](assets/notext/01.webp)

## Mengunduh Dokumen

Untuk memulai, kita akan membutuhkan berbagai dokumen. Kunjungi situs resmi [Sparrow Wallet di bagian "*Download*"](https://sparrowwallet.com/download/). Jika Anda ingin memverifikasi perangkat lunak lain, kunjungi situs web perangkat lunak tersebut.

![GnuPG](assets/notext/02.webp)

Anda juga dapat pergi [ke repositori GitHub dari proyek tersebut](https://github.com/sparrowwallet/sparrow/releases).

![GnuPG](assets/notext/03.webp)

Unduh pemasang untuk perangkat lunak yang sesuai dengan sistem operasi Anda.

![GnuPG](assets/notext/04.webp)

Anda juga akan membutuhkan hash file, sering disebut "*SHA256SUMS*" atau "*MANIFEST*".

![GnuPG](assets/notext/05.webp)

Unduh juga tanda tangan PGP dari file tersebut. Ini adalah dokumen dalam format `.asc`.

![GnuPG](assets/notext/06.webp)
Pastikan untuk menempatkan semua file ini dalam folder yang sama untuk langkah-langkah berikutnya.
Akhirnya, Anda akan memerlukan kunci publik pengembang, yang akan kita gunakan untuk memverifikasi tanda tangan PGP. Kunci ini sering tersedia baik di situs web perangkat lunak, di repositori GitHub proyek, terkadang di media sosial pengembang, atau di situs khusus seperti Keybase. Dalam kasus Sparrow Wallet, Anda dapat menemukan kunci publik pengembang Craig Raw [di Keybase](https://keybase.io/craigraw). Untuk mengunduhnya langsung dari terminal, eksekusi perintah:

```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```

![GnuPG](assets/notext/07.webp)

## Memverifikasi Tanda Tangan

Proses memverifikasi tanda tangan sama di **Windows**, **macOS**, dan **Linux**. Biasanya, Anda sudah mengimpor kunci publik pada langkah sebelumnya, tetapi jika belum, lakukan dengan perintah:

```bash
gpg --import [lokasi kunci]
```

Ganti `[lokasi kunci]` dengan lokasi file kunci publik pengembang.

![GnuPG](assets/notext/08.webp)

Verifikasi tanda tangan dengan perintah berikut:

```bash
gpg --verify [file.asc]
```

Ganti `[file.asc]` dengan jalur file tanda tangan. Dalam kasus Sparrow, file ini disebut "*sparrow-2.0.0-manifest.txt.asc*" untuk versi 2.0.0.

![GnuPG](assets/notext/09.webp)

Jika tanda tangan valid, GPG akan mengindikasikan hal ini kepada Anda. Anda kemudian dapat melanjutkan ke langkah selanjutnya, karena ini mengonfirmasi keaslian file.

![GnuPG](assets/notext/10.webp)

## Memverifikasi Hash
Sekarang keaslian perangkat lunak telah dikonfirmasi, juga perlu untuk memverifikasi integritasnya. Kita akan membandingkan hash perangkat lunak dengan hash yang disediakan oleh pengembang. Jika keduanya cocok, ini menjamin bahwa kode perangkat lunak tidak telah diubah.

Di **Windows**, buka terminal dan eksekusi perintah berikut:

```bash
CertUtil -hashfile [lokasi file] SHA256 | findstr /v "hash"
```

Ganti `[lokasi file]` dengan lokasi installer.

![GnuPG](assets/notext/11.webp)

Terminal akan mengembalikan hash dari perangkat lunak yang diunduh.

![GnuPG](assets/notext/12.webp)

Perlu diketahui, untuk beberapa perangkat lunak, mungkin perlu menggunakan fungsi hash yang berbeda dari SHA256. Dalam kasus ini, cukup ganti nama fungsi hash dalam perintah.

Kemudian bandingkan hasilnya dengan nilai yang sesuai dalam file "*sparrow-2.0.0-manifest.txt*".

![GnuPG](assets/notext/13.webp)

Dalam kasus saya, kita melihat bahwa kedua hash cocok dengan sempurna.

Di **macOS** dan **Linux**, proses verifikasi hash otomatis. Tidak perlu untuk secara manual memeriksa kesesuaian antara kedua hash seperti di Windows.

Cukup eksekusi perintah ini di **macOS**:

```bash
shasum --check [nama file] --ignore-missing
```

Ganti `[nama file]` dengan nama installer. Misalnya, untuk Sparrow Wallet:

```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```

Jika hash cocok, Anda seharusnya melihat output berikut:

```bash
Sparrow-2.0.0.dmg: OK
```
Di **Linux**, perintahnya serupa:
```bash
sha256sum --check [nama file] --ignore-missing
```

Dan jika hash cocok, Anda seharusnya melihat keluaran berikut:

```bash
sparrow_2.0.0-1_amd64.deb: OK
```

Anda sekarang dapat yakin bahwa perangkat lunak yang telah Anda unduh adalah asli dan utuh. Anda dapat melanjutkan dengan instalasi pada mesin Anda.

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat menghargai jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan untuk memeriksa tutorial lain tentang VeraCrypt, sebuah perangkat lunak yang memungkinkan Anda untuk mengenkripsi dan mendekripsi perangkat penyimpanan.

https://planb.network/tutorials/others/general/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5