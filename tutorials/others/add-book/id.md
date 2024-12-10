---
name: Menambahkan Buku ke Jaringan PlanB
description: Bagaimana cara menambahkan buku baru ke Jaringan PlanB?
---
![book](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, memungkinkan siapa saja untuk berkontribusi pada pengayaan platform.

**Apakah Anda ingin menambahkan buku terkait Bitcoin di situs Jaringan PlanB dan meningkatkan visibilitas karya Anda, tetapi tidak tahu bagaimana? Tutorial ini untuk Anda!**
![book](assets/01.webp)
- Pertama, Anda perlu memiliki akun GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Kunjungi [repositori GitHub dari PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) di bagian `resources/books/`:
![book](assets/02.webp)
- Klik tombol `Add file` di kanan atas, lalu klik `Create new file`:
![book](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking sebuah repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik tombol `Fork this repository`:
![book](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![book](assets/05.webp)
- Buat folder untuk buku Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama buku Anda dengan huruf kecil dan menggunakan tanda hubung sebagai pengganti spasi. Misalnya, jika buku Anda bernama "*My Bitcoin Book*", Anda harus mencatat `my-bitcoin-book`:
![book](assets/06.webp)
- Untuk memvalidasi pembuatan folder, cukup tambahkan garis miring setelah nama buku Anda di kotak yang sama, misalnya: `my-bitcoin-book/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![book](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `book.yml`:
![book](assets/08.webp)
- Isi file ini dengan informasi tentang buku Anda menggunakan template ini:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Berikut adalah detail yang harus diisi untuk setiap bidang:
- **`author`**: Tuliskan nama penulis buku.
- **`level`**: Tuliskan level yang diperlukan untuk dapat membaca dan memahami buku dengan baik. Pilih level di antara berikut:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Tambahkan dua atau tiga tag yang terkait dengan buku Anda. Misalnya:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Setelah Anda selesai melakukan perubahan pada file ini, simpan perubahan tersebut dengan mengklik tombol `Commit changes...`:
![book](assets/10.webp)
- Tambahkan judul untuk perubahan Anda, serta deskripsi singkat: ![book](assets/11.webp)
- Klik tombol hijau `Propose changes`: ![book](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda: ![book](assets/13.webp)
- Klik pada gambar profil GitHub Anda di pojok kanan atas, kemudian pada `Your Repositories`: ![book](assets/14.webp)
- Pilih fork Anda dari repositori PlanB Network: ![book](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik padanya: ![book](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda: ![book](assets/17.webp)
- Kembali ke folder `resources/books/` dan pilih folder buku Anda yang baru saja Anda buat dalam commit sebelumnya: ![book](assets/18.webp)
- Di dalam folder buku Anda, klik tombol `Add file`, kemudian pada `Create new file`: ![book](assets/19.webp)
- Beri nama folder baru ini `assets` dan konfirmasi pembuatannya dengan menaruh garis miring `/` di akhir: ![book](assets/20.webp)
- Di dalam folder `assets` ini, buat file bernama `.gitkeep`: ![book](assets/21.webp)
- Klik pada tombol `Commit changes...`: ![book](assets/22.webp)
- Biarkan judul commit sebagai default, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik pada `Commit changes`: ![book](assets/23.webp)
- Kembali ke folder `assets`: ![book](assets/24.webp)
- Klik pada tombol `Add file`, kemudian pada `Upload files`: ![book](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepaskan gambar sampul buku Anda ke area tersebut. Gambar ini akan ditampilkan di situs PlanB Network: ![book](assets/26.webp)
- Hati-hati, gambar harus dalam format buku, untuk beradaptasi dengan baik di situs web kami, seperti contoh: ![book](assets/27.webp)
- Setelah gambar diunggah, pastikan kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik pada `Commit changes`: ![book](assets/28.webp)- Harap dicatat, gambar Anda harus dinamai `cover_en` jika sampulnya dalam bahasa Inggris dan harus dalam format `.webp`. Oleh karena itu, nama file lengkap harus `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, dll. Jika Anda ingin menggunakan gambar sampul yang berbeda untuk setiap bahasa, misalnya dalam kasus terjemahan buku, Anda dapat menempatkannya di lokasi yang sama di folder `assets`: ![book](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`: ![book](assets/30.webp)
- Setelah berada di file, klik pada 3 titik kecil di pojok kanan atas kemudian pada `Delete file`: ![book](assets/31.webp)
- Pastikan Anda masih berada di cabang kerja yang sama, kemudian klik pada tombol `Commit changes...`: ![book](assets/32.webp)
- Tambahkan judul dan deskripsi ke commit Anda, kemudian klik pada `Commit changes`: ![book](assets/33.webp)
- Kembali ke folder buku Anda: ![book](assets/34.webp)
- Klik tombol `Add file`, lalu pilih `Create new file`:
![book](assets/35.webp)
- Buat file YAML baru dengan memberi nama sesuai indikator bahasa buku. File ini akan digunakan untuk deskripsi buku. Misalnya, jika saya ingin menulis deskripsi dalam bahasa Inggris, saya akan menamai file ini `en.yml`:
![book](assets/36.webp)
- Isi file YAML ini menggunakan template berikut:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Berikut adalah detail yang harus diisi untuk setiap bidang:
- **`title`**: Indikasikan nama buku dalam tanda kutip.
- **`publication_year`**: Indikasikan tahun buku tersebut diterbitkan.
- **`cover`**: Indikasikan nama file yang sesuai dengan gambar sampul, sesuai dengan bahasa file YAML yang sedang Anda edit. Misalnya, jika Anda sedang mengedit file `en.yml` dan sebelumnya telah menambahkan gambar sampul berbahasa Inggris dengan judul `cover_en.webp`, cukup indikasikan `cover_en.webp` di bidang ini.
- **`description`**: Tambahkan paragraf pendek yang mendeskripsikan buku. Deskripsi harus dalam bahasa yang sama seperti yang diindikasikan dalam judul file YAML.
- **`contributors`**: Tambahkan ID kontributor Anda jika Anda memilikinya.

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
title: "My Bitcoin Book"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Temukan dunia Bitcoin yang revolusioner dengan panduan komprehensif ini yang disesuaikan untuk pemula. My Bitcoin Book mengungkap kompleksitas Bitcoin, menyediakan pengenalan yang jelas dan ringkas tentang bagaimana protokol bekerja. Dari teknologi revolusionernya hingga dampak potensialnya terhadap ekonomi global, buku ini menawarkan wawasan berharga dan pengetahuan praktis. Sempurna bagi mereka yang baru mengenal Bitcoin, buku ini mencakup dasar-dasar, tips keamanan, dan masa depan keuangan digital. Menyelami masa depan uang dan memberdayakan diri Anda dengan pengetahuan untuk dengan percaya diri menavigasi era digital.

contributors:
  - pretty-private

![book](assets/37.webp)
- Klik tombol `Commit changes...`:
![book](assets/38.webp)
- Pastikan kotak `Commit directly to the patch-1 branch` dicentang, tambahkan judul, lalu klik `Commit changes`:
![book](assets/39.webp)
- Folder buku sekarang harus terlihat seperti ini:
![book](assets/40.webp)
- Jika semuanya terlihat baik bagi Anda, kembali ke akar fork Anda:
![book](assets/41.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah dimodifikasi. Klik tombol `Compare & pull request`:
![book](assets/42.webp)
- Tambahkan judul yang jelas dan deskripsi ke PR Anda:
![book](assets/43.webp)
- Klik tombol `Create pull request`:
![book](assets/44.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan meninjau dan, jika semuanya sesuai, menggabungkannya ke dalam repositori utama dari Jaringan PlanB. Anda seharusnya melihat buku Anda muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti perkembangan PR Anda. Seorang administrator mungkin meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat melihatnya di tab `Pull requests` pada repositori GitHub Jaringan PlanB.
Terima kasih banyak atas kontribusi berharga Anda! :)
