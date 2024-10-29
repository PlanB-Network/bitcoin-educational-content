---
name: Menambahkan Podcast ke Jaringan PlanB
description: Bagaimana cara menambahkan podcast baru ke Jaringan PlanB?
---
![podcast](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform.

Apakah Anda ingin menambahkan podcast Bitcoin ke situs Jaringan PlanB dan meningkatkan visibilitas acara Anda, tetapi tidak tahu bagaimana? Tutorial ini untuk Anda!
![podcast](assets/01.webp)
- Pertama, Anda perlu memiliki akun GitHub. Jika Anda tidak tahu cara membuatnya, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/create-github-account).
- Kunjungi [repositori GitHub PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) di bagian `resources/podcasts/`:
![podcast](assets/02.webp)
- Klik tombol `Add file` di kanan atas, kemudian pada `Create new file`:
![podcast](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`:
![podcast](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![podcast](assets/05.webp)
- Buat folder untuk podcast Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama podcast Anda dalam huruf kecil dengan tanda hubung menggantikan spasi. Misalnya, jika acara Anda bernama "Super Podcast Bitcoin", Anda harus menulis `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Untuk memvalidasi pembuatan folder, cukup tambahkan garis miring setelah nama podcast Anda di kotak yang sama, misalnya: `super-podcast-bitcoin/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![podcast](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `podcast.yml`:
![podcast](assets/08.webp)
- Isi file ini dengan informasi tentang podcast Anda menggunakan template ini:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Berikut adalah detail yang harus diisi untuk setiap bidang:

- **`name`**: Indikasikan nama podcast Anda.
- **`host`**: Daftarkan nama atau pseudonim pembicara atau host podcast. Setiap nama harus dipisahkan dengan koma.
- **`language`**: Indikasikan kode bahasa dari bahasa yang digunakan dalam podcast Anda. Misalnya, untuk bahasa Inggris, catat `en`, untuk bahasa Italia `it`...

- **`links`**: Sediakan tautan ke konten Anda. Anda memiliki dua pilihan:
	- `podcast`: tautan ke podcast Anda,
	- `twitter`: tautan ke profil Twitter dari podcast atau organisasi yang memproduksinya,
	- `website`: tautan ke situs web podcast atau organisasi yang memproduksinya.
- **`description`**: Tambahkan paragraf singkat yang mendeskripsikan podcast Anda. Deskripsi harus dalam bahasa yang sama seperti yang ditunjukkan di bidang `language:`.
- **`tags`**: Tambahkan dua tag yang terkait dengan podcast Anda. Contoh:
    - `bitcoin`
    - `teknologi`
    - `ekonomi`
    - `pendidikan`...

- **`contributors`**: Sebutkan ID kontributor Anda jika Anda memilikinya.

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin adalah sesi LANGSUNG teknis yang diadakan sekali seminggu di Twitter untuk mendalami protokol Bitcoin, solusi layer dua, dan semua hal yang mengejutkan. Host kami Lounes, Pantamis, Loïc, dan Sosthene akan menjawab pertanyaan Anda dan menawarkan acara paling teknis tentang Bitcoin di dunia.

tags:
  - bitcoin
  - teknologi
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Setelah Anda selesai melakukan perubahan pada file ini, simpan perubahan tersebut dengan mengklik tombol `Commit changes...`:
![podcast](assets/10.webp)
- Tambahkan judul untuk perubahan Anda, serta deskripsi singkat:
![podcast](assets/11.webp)
- Klik tombol hijau `Propose changes`:
![podcast](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda:
![podcast](assets/13.webp)
- Klik pada gambar profil GitHub Anda di pojok kanan atas, lalu pada `Your Repositories`:
![podcast](assets/14.webp)
- Pilih fork Anda dari repositori PlanB Network:
![podcast](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik pada itu:
![podcast](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda:
![podcast](assets/17.webp)
- Kembali ke folder `resources/podcast/` dan pilih folder podcast yang baru saja Anda buat dalam commit sebelumnya: ![podcast](assets/18.webp)
- Di folder podcast Anda, klik tombol `Add file`, lalu pada `Create new file`:
![podcast](assets/19.webp)
- Beri nama folder baru ini `assets` dan konfirmasi pembuatannya dengan menambahkan garis miring `/` di akhir:
![podcast](assets/20.webp)
- Di folder `assets` ini, buat file bernama `.gitkeep`:
![podcast](assets/21.webp)
- Klik tombol `Commit changes...`:
![podcast](assets/22.webp)
- Biarkan judul commit sebagai default, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, lalu klik `Commit changes`:
![podcast](assets/23.webp)
- Kembali ke folder `assets`:
![podcast](assets/24.webp)
- Klik tombol `Add file`, lalu pada `Upload files`:
![podcast](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepas logo podcast Anda ke area tersebut. Gambar ini akan ditampilkan di situs PlanB Network: ![podcast](assets/26.webp)
- Hati-hati, gambar harus berbentuk persegi, agar sesuai dengan situs web kami dengan baik: ![podcast](assets/27.webp)
- Setelah gambar diunggah, verifikasi bahwa kotak `Commit directly to the patch-1 branch` telah dicentang, kemudian klik pada `Commit changes`: ![podcast](assets/28.webp)
- Hati-hati, gambar Anda harus dinamai `logo` dan harus dalam format `.webp`. Nama file lengkapnya harus: `logo.webp`: ![podcast](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`: ![podcast](assets/30.webp)
- Setelah berada di file, klik pada tiga titik kecil di pojok kanan atas kemudian pada `Delete file`: ![podcast](assets/31.webp)
- Verifikasi bahwa Anda masih berada di cabang kerja yang sama, kemudian klik pada tombol `Commit changes`: ![podcast](assets/32.webp)
- Tambahkan judul dan deskripsi ke commit Anda, kemudian klik pada `Commit changes`: ![podcast](assets/33.webp)
- Kembali ke akar repositori Anda: ![podcast](assets/34.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah mengalami perubahan. Klik pada tombol `Compare & pull request`: ![podcast](assets/35.webp)
- Tambahkan judul dan deskripsi yang jelas ke PR Anda: ![podcast](assets/36.webp)
- Klik pada tombol `Create pull request`: ![podcast](assets/37.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan meninjau dan, jika semuanya sesuai, menggabungkannya ke dalam repositori utama PlanB Network. Anda seharusnya melihat podcast Anda muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti perkembangan PR Anda. Seorang administrator mungkin meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat melihatnya di tab `Pull requests` pada repositori GitHub PlanB Network: ![podcast](assets/38.webp)
Terima kasih banyak atas kontribusi berharga Anda! :)
