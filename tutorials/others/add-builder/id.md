---
name: Menambahkan Pembangun
description: Bagaimana cara mengusulkan penambahan pembangun baru di Jaringan PlanB?
---
![builder](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin, dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, yang memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform.

Apakah Anda ingin menambahkan "pembangun" Bitcoin baru ke situs Jaringan PlanB dan memberikan visibilitas untuk perusahaan atau perangkat lunak Anda, tetapi tidak tahu bagaimana? Tutorial ini untuk Anda!
![builder](assets/01.webp)
- Pertama, Anda perlu memiliki akun GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/create-github-account).
- Kunjungi [repositori GitHub PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) di bagian `resources/builder/`:
![builder](assets/02.webp)
- Klik tombol `Add file` di kanan atas, lalu pada `Create new file`:
![builder](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking sebuah repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, yang memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`:
![builder](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![builder](assets/05.webp)
- Buat folder untuk perusahaan Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama perusahaan Anda dalam huruf kecil dengan tanda hubung menggantikan spasi. Misalnya, jika perusahaan Anda bernama "Bitcoin Baguette", Anda harus menulis `bitcoin-baguette`:
![builder](assets/06.webp)
- Untuk memvalidasi pembuatan folder, cukup tambahkan garis miring setelah nama Anda di kotak yang sama, misalnya: `bitcoin-baguette/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![builder](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `builder.yml`:
![builder](assets/08.webp)
- Isi file ini dengan informasi tentang perusahaan Anda menggunakan template ini:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Berikut apa yang harus diisi untuk setiap kunci:
- `name`: Nama perusahaan Anda (wajib);
- `address` : Lokasi bisnis Anda (opsional);
- `language` : Negara tempat bisnis Anda beroperasi atau bahasa yang didukung (opsional);
- `links` : Berbagai tautan resmi dari bisnis Anda (opsional);
- `tags` : 2 istilah yang mengkualifikasi bisnis Anda (wajib);
- `category` : Kategori yang paling baik menggambarkan bidang di mana bisnis Anda beroperasi di antara pilihan berikut:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
Sebagai contoh, file YAML Anda bisa terlihat seperti ini:
```yaml
name: Bitcoin Baguette

address_line_1: Paris, Prancis
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - pendidikan

category: pendidikan
```

![builder](assets/09.webp)
- Setelah Anda selesai melakukan perubahan pada file ini, simpan perubahan tersebut dengan mengklik tombol `Commit changes...`:
![builder](assets/10.webp)
- Tambahkan judul untuk perubahan Anda, bersama dengan deskripsi singkat:
![builder](assets/11.webp)
- Klik tombol hijau `Propose changes`:
![builder](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda:
![builder](assets/13.webp)
- Klik pada gambar profil GitHub Anda di pojok kanan atas, lalu pada `Your Repositories`:
![builder](assets/14.webp)
- Pilih fork Anda dari repositori PlanB Network:
![builder](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik pada itu:
![builder](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda (**pastikan Anda berada di cabang yang sama dengan modifikasi sebelumnya, ini penting!**):
![builder](assets/17.webp)
- Kembali ke folder `resources/builders/` dan pilih folder bisnis Anda yang baru saja Anda buat dalam commit sebelumnya:
![builder](assets/18.webp)
- Di folder bisnis Anda, klik tombol `Add file`, lalu pada `Create new file`:
![builder](assets/19.webp)
- Beri nama folder baru ini `assets` dan konfirmasi pembuatannya dengan menaruh garis miring `/` di akhir:
![builder](assets/20.webp)
- Di folder `assets` ini, buat file bernama `.gitkeep`:
![builder](assets/21.webp)
- Klik pada tombol `Commit changes...`:
![builder](assets/22.webp)
- Biarkan judul commit sebagai default, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, lalu klik pada `Commit changes`: ![builder](assets/23.webp)
- Kembali ke folder `assets`:
![builder](assets/24.webp)
- Klik pada tombol `Add file`, lalu pada `Upload files`:
![builder](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepaskan gambar perusahaan atau software Anda ke area tersebut. Gambar ini akan ditampilkan di situs PlanB Network:
![builder](assets/26.webp)
- Bisa jadi logo atau ikon:
![builder](assets/27.webp)
- Setelah gambar diunggah, verifikasi bahwa kotak `Commit directly to the patch-1 branch` dicentang, lalu klik pada `Commit changes`:
![builder](assets/28.webp)
- Hati-hati, gambar Anda harus berbentuk persegi, harus dinamai `logo`, dan harus dalam format `.webp`. Nama file lengkapnya harus: `logo.webp`:
![builder](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`:
![builder](assets/30.webp)- Setelah berada di file tersebut, klik pada tiga titik kecil di pojok kanan atas kemudian klik `Delete file`:
![builder](assets/31.webp)
- Pastikan Anda masih berada di cabang kerja yang sama, kemudian klik tombol `Commit changes`:
![builder](assets/32.webp)
- Tambahkan judul dan deskripsi pada commit Anda, kemudian klik `Commit changes`:
![builder](assets/33.webp)
- Kembali ke folder perusahaan Anda:
![builder](assets/34.webp)
- Klik tombol `Add file`, kemudian klik `Create new file`:
![builder](assets/35.webp)
- Buat file YAML baru dengan menamainya dengan indikator bahasa ibu Anda. File ini akan digunakan untuk deskripsi builder. Sebagai contoh, jika saya ingin menulis deskripsi saya dalam bahasa Inggris, saya akan menamai file ini `en.yml`:
![builder](assets/36.webp)
- Isi file YAML ini menggunakan template ini:
```yaml
description: |
 
contributors:
 - 
```

- Untuk kunci `contributors`, Anda dapat menambahkan identifikasi kontributor Anda ke PlanB Network jika Anda memilikinya. Jika tidak, biarkan bidang ini kosong.
- Untuk kunci `description`, Anda hanya perlu menambahkan paragraf singkat yang mendeskripsikan perusahaan atau perangkat lunak Anda. Deskripsi harus dalam bahasa yang sama dengan nama file. Anda tidak perlu menerjemahkan deskripsi ini ke semua bahasa yang didukung di situs, karena tim PlanB akan melakukannya menggunakan model mereka. Sebagai contoh, inilah tampilan file Anda:
```yaml
description: |
Didirikan pada tahun 2017, Bitcoin Baguette adalah sebuah asosiasi berbasis di Paris yang didedikasikan untuk mengorganisir meetup Bitcoin dan workshop teknis. Kami mengumpulkan para penggemar, ahli, dan pikiran yang penasaran untuk menjelajahi dan mendiskusikan kerumitan teknologi Bitcoin. Acara kami menyediakan platform untuk berbagi pengetahuan, jaringan, dan memperdalam pemahaman tentang cara kerja Bitcoin. Bergabunglah dengan kami di Bitcoin Baguette untuk menjadi bagian dari komunitas Bitcoin Paris dan tetap terupdate dengan kemajuan terbaru di bidang ini.

contributors:
- 
```
![builder](assets/37.webp)
- Klik tombol `Commit changes`:
![builder](assets/38.webp)
- Pastikan kotak `Commit directly to the patch-1 branch` dicentang, tambahkan judul, kemudian klik `Commit changes`:
![builder](assets/39.webp)
- Folder perusahaan Anda sekarang harus terlihat seperti ini:
![builder](assets/40.webp)
- Jika semuanya sesuai dengan kepuasan Anda, kembali ke akar fork Anda:
![builder](assets/41.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah mengalami perubahan. Klik tombol `Compare & pull request`:
![builder](assets/42.webp)
- Tambahkan judul dan deskripsi yang jelas ke PR Anda:
![builder](assets/43.webp)
- Klik tombol `Create pull request`:
![builder](assets/44.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan meninjau dan, jika semuanya sesuai, mengintegrasikannya ke dalam repositori utama PlanB Network. Profil builder Anda akan muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti kemajuan PR Anda. Seorang administrator mungkin meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat mengkonsultasikannya di tab `Pull requests` pada repositori GitHub PlanB Network:
![builder](assets/45.webp)
Terima kasih banyak atas kontribusi berharga Anda! :)
