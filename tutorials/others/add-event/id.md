---
name: Menambahkan sebuah acara di Jaringan PlanB
description: Bagaimana cara saya menyarankan penambahan acara baru di Jaringan PlanB?
---
![event](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin dalam sebanyak mungkin bahasa. Semua konten yang dipublikasikan di situs ini bersifat open-source dan dihosting di GitHub, menawarkan kesempatan kepada siapa saja untuk berkontribusi dalam pengayaan platform.

Jika Anda ingin menambahkan konferensi Bitcoin ke situs Jaringan PlanB dan meningkatkan visibilitas untuk acara Anda, tetapi tidak tahu bagaimana? Tutorial ini adalah untuk Anda!
![event](assets/01.webp)
- Pertama, Anda perlu memiliki akun di GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/create-github-account).
- Kunjungi [repositori GitHub dari PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) di bagian `resources/conference/`:
![event](assets/02.webp)
- Klik tombol `Add file` di kanan atas, kemudian pada `Create new file`:
![event](assets/03.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Forking sebuah repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`:
![event](assets/04.webp)
- Anda kemudian akan tiba di halaman pengeditan GitHub:
![event](assets/05.webp)
- Buat folder untuk konferensi Anda. Untuk melakukan ini, di kotak `Name your file...`, tulis nama konferensi Anda dalam huruf kecil dengan tanda hubung menggantikan spasi. Misalnya, jika konferensi Anda bernama "Paris Bitcoin Conference", Anda harus mencatat `paris-bitcoin-conference`. Juga tambahkan tahun konferensi Anda, misalnya: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- Untuk memvalidasi pembuatan folder, cukup catat garis miring setelah nama Anda di kotak yang sama, misalnya: `paris-bitcoin-conference-2024/`. Menambahkan garis miring secara otomatis membuat folder daripada file:
![event](assets/07.webp)
- Di dalam folder ini, Anda akan membuat file YAML pertama bernama `events.yml`:
![event](assets/08.webp)
- Isi file ini dengan informasi tentang konferensi Anda menggunakan template ini:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Sebagai contoh, file YAML Anda bisa terlihat seperti ini:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, Prancis
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
deskripsi: Konferensi Bitcoin terbesar di Prancis dengan lebih dari 8.000 peserta setiap tahunnya!
bahasa:
    - fr
    - en
    - es
    - it
tautan:
    situs web: https://paris.bitcoin.fr/conference
    url_replay:
    url_langsung:
tag:
    - Bitcoiner
    - Umum
    - Internasional
```
![event](assets/09.webp)
Jika Anda belum memiliki pengenal "*builder*" untuk organisasi Anda, Anda dapat menambahkannya [dengan mengikuti tutorial lain ini](https://planb.network/tutorials/others/add-builder).

- Setelah Anda selesai melakukan perubahan pada file ini, simpan perubahan tersebut dengan mengklik tombol `Commit changes...`:
![event](assets/10.webp)
- Tambahkan judul untuk perubahan Anda, serta deskripsi singkat:
![event](assets/11.webp)
- Klik tombol hijau `Propose changes`:
![event](assets/12.webp)
- Anda kemudian akan tiba di halaman yang merangkum semua perubahan Anda:
![event](assets/13.webp)
- Klik pada gambar profil GitHub Anda di pojok kanan atas, lalu pada `Your Repositories`:
![event](assets/14.webp)
- Pilih fork Anda dari repositori PlanB Network:
![event](assets/15.webp)
- Anda seharusnya melihat notifikasi di bagian atas jendela dengan cabang baru Anda. Mungkin disebut `patch-1`. Klik pada itu:
![event](assets/16.webp)
- Anda sekarang berada di cabang kerja Anda:
![event](assets/17.webp)
- Kembali ke folder `resources/conference/` dan pilih folder konferensi Anda yang baru saja Anda buat dalam commit sebelumnya:
![event](assets/18.webp)
- Di dalam folder konferensi Anda, klik tombol `Add file`, lalu pada `Create new file`:
![event](assets/19.webp)
- Beri nama folder baru ini `assets` dan konfirmasi pembuatannya dengan menempatkan garis miring `/` di akhir:
![event](assets/20.webp)
- Di dalam folder `assets` ini, buat file bernama `.gitkeep`:
![event](assets/21.webp)
- Klik tombol `Commit changes...`:
![event](assets/22.webp)
- Biarkan judul commit sebagai default, dan pastikan kotak `Commit directly to the patch-1 branch` dicentang, lalu klik `Commit changes`:
![event](assets/23.webp)
- Kembali ke folder `assets`:
![event](assets/24.webp)
- Klik tombol `Add file`, lalu pada `Upload files`: ![event](assets/25.webp)
- Sebuah halaman baru akan terbuka. Seret dan lepas gambar yang mewakili konferensi Anda dan akan ditampilkan di situs PlanB Network:
![event](assets/26.webp)
- Bisa jadi logo, thumbnail, atau bahkan poster:
![event](assets/27.webp)
- Setelah gambar diunggah, periksa bahwa kotak `Commit directly to the patch-1 branch` dicentang, lalu klik `Commit changes`:
![event](assets/28.webp)
- Hati-hati, gambar Anda harus dinamai `thumbnail` dan harus dalam format `.webp`. Nama file lengkapnya harus: `thumbnail.webp`:
![event](assets/29.webp)
- Kembali ke folder `assets` Anda dan klik pada file perantara `.gitkeep`:
![event](assets/30.webp)
- Setelah berada di file tersebut, klik pada 3 titik kecil di pojok kanan atas kemudian pada `Delete file`: ![event](assets/31.webp)
- Verifikasi bahwa Anda masih berada di cabang kerja yang sama, kemudian klik pada tombol `Commit changes`:
![event](assets/32.webp)
- Tambahkan judul dan deskripsi untuk commit Anda, kemudian klik pada `Commit changes`:
![event](assets/33.webp)
- Kembali ke akar repositori Anda:
![event](assets/34.webp)
- Anda seharusnya melihat pesan yang menunjukkan bahwa cabang Anda telah mengalami perubahan. Klik pada tombol `Compare & pull request`:
![event](assets/35.webp)
- Tambahkan judul dan deskripsi yang jelas untuk PR Anda:
![event](assets/36.webp)
- Klik pada tombol `Create pull request`:
![event](assets/37.webp)
Selamat! PR Anda telah berhasil dibuat. Seorang administrator sekarang akan memeriksanya dan, jika semuanya sesuai, menggabungkannya ke dalam repositori utama dari PlanB Network. Anda seharusnya melihat event Anda muncul di situs web beberapa hari kemudian.

Pastikan untuk mengikuti perkembangan PR Anda. Seorang administrator mungkin meninggalkan komentar meminta informasi tambahan. Selama PR Anda belum divalidasi, Anda dapat mengkonsultasikannya di tab `Pull requests` pada repositori GitHub PlanB Network:
![event](assets/38.webp)
Terima kasih banyak atas kontribusi berharga Anda! :)
