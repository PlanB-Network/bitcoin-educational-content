---
name: Menambahkan Rekaman Konferensi
description: Bagaimana cara menambahkan rekaman konferensi di Jaringan PlanB?
---
![conference](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin dalam sebanyak mungkin bahasa. Semua konten yang dipublikasikan di situs ini bersifat open-source dan dihosting di GitHub, memungkinkan siapa saja untuk berkontribusi pada pengayaan platform.

Apakah Anda ingin menambahkan rekaman konferensi Bitcoin Anda di situs Jaringan PlanB dan memberikan visibilitas kepada acara ini, tetapi tidak tahu bagaimana? Tutorial ini untuk Anda!

Namun, jika Anda ingin menambahkan konferensi yang akan berlangsung di masa depan, saya menyarankan Anda untuk [membaca tutorial lain ini](https://planb.network/tutorials/others/contribution/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097) di mana kami menjelaskan cara menambahkan acara baru ke situs.
![conference](assets/01.webp)
- Pertama, Anda perlu memiliki akun di GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Kunjungi [repositori GitHub PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) di bagian `resources/conference/`:
![conference](assets/02.webp)
- Klik tombol `Add file` di kanan atas, lalu pada `Create new file`:
![conference](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, yang memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`:
![conference](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![conference](assets/05.webp)
- Buat folder untuk konferensi Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama konferensi Anda dalam huruf kecil dengan tanda hubung menggantikan spasi. Misalnya, jika konferensi Anda bernama "Paris Bitcoin Conference", Anda harus mencatat `paris-bitcoin-conference`. Juga tambahkan tahun konferensi Anda, misalnya: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- Untuk memvalidasi pembuatan folder, cukup catat garis miring setelah nama Anda di kotak yang sama, misalnya: `paris-bitcoin-conference-2024/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![conference](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `conference.yml`:
![conference](assets/08.webp)
Isi file ini dengan informasi terkait konferensi Anda menggunakan template ini:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)
Jika Anda belum memiliki pengenal "*builder*" untuk organisasi Anda, Anda dapat menambahkannya [dengan mengikuti tutorial lain ini](https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d).
- Setelah Anda selesai melakukan perubahan pada file ini, simpan perubahan tersebut dengan mengklik tombol `Commit changes...`:
![konferensi](assets/10.webp)
- Tambahkan judul untuk perubahan Anda, serta deskripsi singkat:
![konferensi](assets/11.webp)
- Klik tombol hijau `Propose changes`:
![konferensi](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda:
![konferensi](assets/13.webp)
- Klik pada gambar profil GitHub Anda di pojok kanan atas, kemudian pada `Your Repositories`:
![konferensi](assets/14.webp)
- Pilih fork Anda dari repositori PlanB Network:
![konferensi](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik pada itu:
![konferensi](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda:
![konferensi](assets/17.webp)
- Kembali ke folder `resources/conference/` dan pilih folder konferensi Anda yang baru saja Anda buat dalam commit sebelumnya:
![konferensi](assets/18.webp)
- Di folder konferensi Anda, klik tombol `Add file`, kemudian pada `Create new file`:
![konferensi](assets/19.webp)
- Beri nama folder baru ini `assets` dan konfirmasi pembuatannya dengan menempatkan garis miring `/` di akhir:
![konferensi](assets/20.webp)
- Di folder `assets` ini, buat file bernama `.gitkeep`:
![konferensi](assets/21.webp)
- Klik pada tombol `Commit changes...`:
![konferensi](assets/22.webp)
- Biarkan judul commit sebagai default, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik pada `Commit changes`:
![konferensi](assets/23.webp)
- Kembali ke folder `assets`:
![konferensi](assets/24.webp)
- Klik pada tombol `Add file`, kemudian pada `Upload files`:
![konferensi](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepaskan gambar yang mewakili konferensi Anda dan akan ditampilkan di situs PlanB Network: ![konferensi](assets/26.webp)
- Ini bisa berupa logo, thumbnail, atau bahkan poster:
![konferensi](assets/27.webp)
- Setelah gambar diunggah, periksa bahwa kotak `Commit directly to the patch-1 branch` dicentang, kemudian klik pada `Commit changes`:
![konferensi](assets/28.webp)
- Hati-hati, gambar Anda harus dinamai `thumbnail` dan harus dalam format `.webp`. Nama file lengkapnya harus: `thumbnail.webp`:
![konferensi](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`:
![konferensi](assets/30.webp)
- Setelah berada di file, klik pada 3 titik kecil di pojok kanan atas kemudian pada `Delete file`:
![konferensi](assets/31.webp)
- Verifikasi bahwa Anda masih berada di cabang kerja yang sama, kemudian klik pada tombol `Commit changes`:
![konferensi](assets/32.webp)
- Tambahkan judul dan deskripsi ke commit Anda, kemudian klik pada `Commit changes`:
![konferensi](assets/33.webp)
- Kembali ke folder konferensi Anda: ![konferensi](assets/34.webp)
- Klik tombol `Tambah file`, lalu pilih `Buat file baru`:
![konferensi](assets/35.webp)
- Buat file markdown (.md) baru dengan memberi nama file tersebut sesuai dengan indikator bahasa ibu Anda. File ini akan digunakan untuk replay konferensi Anda. Sebagai contoh, jika saya ingin menulis deskripsi konferensi dalam bahasa Inggris, saya akan menamai file ini en.md:
![konferensi](assets/36.webp)
- Isi file markdown ini menggunakan template ini yang dapat Anda sesuaikan dengan konfigurasi konferensi Anda:

```markdown
---
name: Konferensi Bitcoin Paris 2024
description: Konferensi Bitcoin terbesar di Prancis dengan lebih dari 8.000 peserta setiap tahunnya!
--- 

# Panggung Utama

## Jumat pagi

![video](https://youtu.be/XXXXXXXXXXXX)

## Jumat sore

![video](https://youtu.be/XXXXXXXXXXXX)

## Sabtu pagi

![video](https://youtu.be/XXXXXXXXXXXX)

## Sabtu sore

![video](https://youtu.be/XXXXXXXXXXXX)

# Ruang Workshop

## Masa Depan Penambangan Bitcoin: Tantangan dan Inovasi

![video](https://youtu.be/XXXXXXXXXXXX)

Pembicara: Satoshi Nakamoto, Satoshi Nakamoto

## Apakah Privasi Masih Mungkin Di Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Pembicara: Satoshi Nakamoto

## Inti Bitcoin: Menyelami Basis Kode

![video](https://youtu.be/XXXXXXXXXXXX)

Pembicara: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Membangun dan Mengamankan Dompet Bitcoin Dengan Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Pembicara: Satoshi Nakamoto
```

![konferensi](assets/37.webp)
- Di awal dokumen Anda, dalam "front matter," isi bidang `name:` dengan nama konferensi Anda dan tahun replay. Di bidang `description:`, tulis deskripsi singkat acara Anda dalam bahasa file tersebut. Sebagai contoh, untuk file bernama `en.md`, deskripsinya harus dalam bahasa Inggris. Tim PlanB Network akan mengurus penerjemahan deskripsi Anda menggunakan model mereka.
- Judul tingkat pertama, ditandai dengan `#`, digunakan untuk mengorganisir konferensi berdasarkan adegan. Sebagai contoh, `# Panggung Utama` untuk panggung utama dan `# Ruang Workshop` untuk panggung yang didedikasikan untuk workshop.

- Judul tingkat kedua, ditandai dengan ganda `##`, digunakan untuk memisahkan video replay yang berbeda. Jika konferensi difilmkan secara terus-menerus selama setengah hari, sebutkan, misalnya, `## Jumat pagi`. Jika konferensi difilmkan dan disiarkan secara individu, namai konferensi langsung dengan judul tingkat kedua.

- Di bawah setiap judul tingkat kedua, sisipkan tautan ke video replay yang sesuai. Sintaksnya harus: `![video](https://youtu.be/XXXXXXXXXXXX)`, menggantikan `XXXXXXXXXXXX` dengan tautan video yang sebenarnya.

- Jika formatnya memungkinkan (konferensi individu), Anda dapat menambahkan nama-nama pembicara. Untuk melakukan ini, tambahkan bidang `Pembicara:` diikuti oleh nama atau pseudonim pembicara di bawah tautan video. Dalam kasus beberapa pembicara, pisahkan setiap nama dengan koma, seperti ini misalnya: `Pembicara: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Setelah modifikasi Anda pada file ini selesai, simpan dengan mengklik tombol `Commit changes...`:
![konferensi](assets/38.webp)
- Tambahkan judul untuk modifikasi Anda, serta deskripsi singkat:
![konferensi](assets/39.webp)
- Klik pada `Commit changes`: ![konferensi](assets/40.webp)
- Folder konferensi Anda sekarang seharusnya terlihat seperti ini:
![konferensi](assets/41.webp)
- Jika semuanya sesuai dengan kepuasan Anda, kembali ke akar dari fork Anda:
![konferensi](assets/42.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah mengalami modifikasi. Klik pada tombol `Compare & pull request`:
![konferensi](assets/43.webp)
- Tambahkan judul dan deskripsi yang jelas untuk PR Anda:
![konferensi](assets/44.webp)
- Klik pada tombol `Create pull request`:
![konferensi](assets/45.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan meninjau dan, jika semuanya dalam urutan, menggabungkannya ke dalam repositori utama dari Jaringan PlanB. Anda seharusnya melihat rekaman konferensi Anda muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti perkembangan PR Anda. Mungkin saja seorang administrator meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat melihatnya di bawah tab `Pull requests` pada repositori GitHub Jaringan PlanB:
![konferensi](assets/46.webp)

Terima kasih banyak atas kontribusi berharga Anda! :)
