---
name: Menambahkan Alat Edukasi
description: Bagaimana cara menambahkan materi edukasi baru di Jaringan PlanB?
---
![event](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya edukasi terdepan tentang Bitcoin, dalam sebanyak mungkin bahasa. Semua konten yang dipublikasikan di situs ini bersifat open-source dan dihosting di GitHub, yang memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform.

Lebih dari tutorial dan pelatihan, Jaringan PlanB juga menawarkan perpustakaan konten edukasi tentang Bitcoin yang beragam, dapat diakses oleh semua orang, [di bagian "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Database ini mencakup poster edukasi, meme, poster propaganda humoris, diagram teknis, logo, dan alat lainnya untuk pengguna. Tujuan dari inisiatif ini adalah untuk mendukung individu dan komunitas yang mengajarkan Bitcoin di seluruh dunia dengan menyediakan sumber daya visual yang diperlukan.

Apakah Anda ingin berpartisipasi dalam memperkaya database ini, tetapi tidak tahu bagaimana? Tutorial ini untuk Anda!

*Penting bahwa semua konten yang diintegrasikan ke dalam situs bebas dari hak atau menghormati lisensi file sumber. Juga, semua visual yang dipublikasikan di Jaringan PlanB tersedia di bawah lisensi [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Pertama, Anda perlu memiliki akun di GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/create-github-account).
- Pergi ke [repositori GitHub PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) di bagian `resources/bet/`:
![event](assets/02.webp)
- Klik di kanan atas pada tombol `Add file`, lalu pada `Create new file`:
![event](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking sebuah repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, yang memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`:
![event](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![event](assets/05.webp)
- Buat folder untuk konten Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama konten Anda dengan huruf kecil dan menggunakan tanda hubung sebagai pengganti spasi. Dalam contoh saya, katakanlah saya ingin menambahkan visual PDF dari daftar kata BIP39 sebanyak 2048 kata. Jadi, saya akan menamai folder saya `bip39-wordlist`: ![event](assets/06.webp)
- Untuk mengonfirmasi pembuatan folder, cukup tambahkan garis miring setelah nama di kotak yang sama, misalnya: `bip39-wordlist/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![event](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `bet.yml`:
![event](assets/08.webp)
- Isi file ini dengan informasi terkait konten Anda menggunakan template ini:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`builder`**: Tunjukkan pengenal organisasi Anda di Jaringan PlanB. Jika Anda belum memiliki pengenal "builder" untuk perusahaan Anda, Anda dapat membuatnya [dengan mengikuti tutorial ini](https://planb.network/tutorials/others/add-builder). Jika Anda tidak memilikinya, Anda dapat menggunakan nama Anda, pseudonim Anda, atau nama perusahaan Anda tanpa harus membuat profil builder.
- **`type`**: Pilih jenis konten Anda dari dua opsi berikut:
	- `Educational Content` untuk konten pendidikan.
	- `Visual Content` untuk jenis konten beragam lainnya.

- **`links`**: Sediakan tautan ke konten Anda. Anda memiliki dua opsi:
	- Jika Anda memilih untuk menyimpan konten Anda langsung di GitHub PlanB, Anda perlu menambahkan tautan ke file ini pada langkah berikutnya.
	- Jika konten Anda disimpan di tempat lain, seperti di situs web pribadi Anda, tunjukkan tautan yang sesuai di sini:
	    - `download`: Tautan untuk mengunduh konten Anda.
	    - `view`: Tautan untuk melihat konten Anda (dapat sama dengan tautan unduh). Jika konten Anda tersedia dalam beberapa bahasa, tambahkan tautan untuk setiap bahasa.

- **`tags`**: Tambahkan dua tag yang terkait dengan konten Anda. Contoh:
	- bitcoin
	- teknologi
	- ekonomi
	- pendidikan
	- meme...

- **`contributors`**: Sebutkan pengenal kontributor Anda jika Anda memilikinya.

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- Dalam contoh saya, saya akan meninggalkan tautan kosong untuk sekarang, karena saya akan menambahkan PDF saya langsung di GitHub:
![event](assets/09.webp)
- Setelah modifikasi Anda pada file ini selesai, simpan dengan mengklik tombol `Commit changes...`:
![event](assets/10.webp)
- Tambahkan judul untuk modifikasi Anda, serta deskripsi singkat:
![event](assets/11.webp)
- Klik tombol hijau `Propose changes`:
![event](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda:
![event](assets/13.webp)
- Klik gambar profil GitHub Anda di pojok kanan atas, lalu pada `Your Repositories`:
![event](assets/14.webp)
- Pilih fork Anda dari repositori Jaringan PlanB:
![event](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik pada itu:
![event](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda (**pastikan Anda berada di cabang yang sama dengan modifikasi sebelumnya, ini penting!**):
![event](assets/17.webp)
- Kembali ke folder `resources/bet/` dan pilih folder konten Anda yang baru saja Anda buat dalam commit sebelumnya:
![event](assets/18.webp)
- Di dalam folder konten Anda, klik tombol `Add file`, lalu pada `Create new file`:
![event](assets/19.webp)
- Namai folder baru ini `assets` dan konfirmasi pembuatannya dengan menaruh garis miring `/` di akhir:
![event](assets/20.webp)
- Di dalam folder `assets` ini, buat file bernama `.gitkeep`: ![event](assets/21.webp)
- Klik tombol `Commit changes...`: ![event](assets/22.webp)- Biarkan judul commit seperti bawaan, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik `Commit changes`: ![event](assets/23.webp)
- Kembali ke folder `assets`: ![event](assets/24.webp)
- Klik tombol `Add file`, lalu klik `Upload files`: ![event](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepaskan thumbnail yang mewakili konten Anda ke area tersebut. Gambar ini akan ditampilkan di situs Jaringan PlanB: ![event](assets/26.webp)
- Ini bisa berupa pratinjau, logo, atau ikon: ![event](assets/27.webp)
- Setelah gambar diunggah, pastikan kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik `Commit changes`: ![event](assets/28.webp)
- Hati-hati, gambar Anda harus dinamai `logo` dan harus dalam format `.webp`. Nama file lengkapnya harus: `logo.webp`: ![event](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`: ![event](assets/30.webp)
- Setelah berada di file tersebut, klik pada tiga titik kecil di kanan atas kemudian klik `Delete file`: ![event](assets/31.webp)
- Pastikan Anda masih berada di cabang kerja yang sama, kemudian klik tombol `Commit changes`: ![event](assets/32.webp)
- Tambahkan judul dan deskripsi ke commit Anda, kemudian klik `Commit changes`: ![event](assets/33.webp)
- Kembali ke folder konten Anda: ![event](assets/34.webp)
- Klik tombol `Add file`, lalu klik `Create new file`: ![event](assets/35.webp)
- Buat file YAML baru dengan menamainya dengan indikator bahasa ibu Anda. File ini akan digunakan untuk deskripsi konten. Misalnya, jika saya ingin menulis deskripsi saya dalam bahasa Inggris, saya akan menamai file ini `en.yml`: ![event](assets/36.webp)
- Isi file YAML ini menggunakan template ini:

```yaml
name: 
description: |
  
```

- Untuk kunci `name`, Anda dapat menambahkan nama konten Anda;
- Untuk kunci `description`, Anda hanya perlu menambahkan paragraf singkat yang mendeskripsikan konten Anda. Deskripsi harus dalam bahasa yang sama dengan nama file. Anda tidak perlu menerjemahkan deskripsi ini ke semua bahasa yang didukung di situs, karena tim PlanB akan melakukannya dengan model mereka.
Misalnya, inilah tampilan file Anda:

```yaml
name: BIP39 WORDLIST
description: |
  Daftar lengkap dan bernomor dari 2048 kata bahasa Inggris dari kamus BIP39 yang digunakan untuk mengkodekan frasa mnemonik. Dokumen ini dapat dicetak dalam satu halaman.
```

![event](assets/37.webp)
- Klik tombol `Commit changes...`:
![event](assets/38.webp)
- Pastikan kotak `Commit directly to the patch-1 branch` dicentang, tambahkan judul, kemudian klik `Commit changes`:
![event](assets/39.webp)
- Folder konten Anda sekarang harus terlihat seperti ini:
![event](assets/40.webp)
*Jika Anda lebih memilih untuk tidak menambahkan konten di GitHub dan Anda sudah mencatat link-link tersebut dalam file `bet.yml` pada langkah-langkah sebelumnya, Anda dapat melewatkan bagian ini dan langsung menuju ke bagian pembuatan Pull Request.*
- Kembali ke folder `/assets`:
![event](assets/41.webp)
- Klik tombol `Add file`, lalu klik `Upload files`:
![event](assets/42.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepaskan konten yang ingin Anda bagikan ke area tersebut:
![event](assets/43.webp)
- Sebagai contoh, saya menambahkan file PDF dari daftar BIP39:
![event](assets/44.webp)
- Setelah konten diunggah, pastikan kotak `Commit directly to the patch-1 branch` dicentang, lalu klik `Commit changes`:
![event](assets/45.webp)
- Kembali ke folder `/assets` Anda dan klik file yang baru saja Anda unggah:
![event](assets/46.webp)
- Ambil URL sementara dari file Anda. Sebagai contoh, dalam kasus saya, URL-nya adalah:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Pertahankan hanya bagian terakhir dari URL mulai dari `/resources` ke depan:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Tambahkan ke dasar URL informasi berikut untuk mendapatkan link yang benar:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Apa yang kita lakukan di sini adalah mengantisipasi link masa depan file Anda, setelah proposal Anda digabungkan ke repositori sumber dari Jaringan PlanB.
- Kembali ke file `bet.yml` Anda dan klik ikon pensil: ![event](assets/47.webp)
- Tambahkan link Anda di sana:
![event](assets/48.webp)
- Setelah perubahan Anda selesai, klik tombol `Commit changes...`:
![event](assets/49.webp)
- Tambahkan judul untuk perubahan Anda, serta deskripsi singkat:
![event](assets/50.webp)
- Klik tombol hijau `Commit changes`:
![event](assets/51.webp)

---

- Jika semuanya terlihat baik bagi Anda, kembali ke akar fork Anda:
![event](assets/52.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah dimodifikasi. Klik tombol `Compare & pull request`:
![event](assets/53.webp)
- Tambahkan judul yang jelas dan deskripsi untuk PR Anda:
![event](assets/54.webp)
- Klik tombol `Create pull request`:
![event](assets/55.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan meninjau dan, jika semuanya sesuai, menggabungkannya ke repositori utama dari Jaringan PlanB. Anda seharusnya melihat BET Anda muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti perkembangan PR Anda. Seorang administrator mungkin meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat mengkonsultasikannya di tab Pull requests pada repositori GitHub Jaringan PlanB:
![event](assets/56.webp)
Terima kasih banyak atas kontribusi berharga Anda! :)
