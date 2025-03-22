---
name: Kontribusi - Tutorial dengan GitHub Desktop (Menengah)
description: Panduan lengkap untuk mengusulkan tutorial tentang Plan ₿ Network menggunakan GitHub Desktop
---
![cover](assets/cover.webp)

Sebelum mengikuti tutorial tentang cara menambahkan tutorial baru ini, Anda harus sudah menyelesaikan beberapa langkah awal. Jika Anda belum melakukannya, saya mengundang Anda untuk terlebih dahulu membaca tutorial pengantar ini, lalu kembali ke sini:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Anda sudah melakukannya:


- Memilih tema tutorial Anda;
- Menghubungi tim Plan ₿ Network melalui [grup Telegram](https://t.me/PlanBNetwork_ContentBuilder) atau paolo@planb.network;
- Memilih alat kontribusi Anda.

Dalam tutorial ini, kita akan melihat cara menambahkan tutorial Anda di Plan ₿ Network dengan menyiapkan lingkungan lokal Anda dengan GitHub Desktop. Jika Anda sudah mahir menggunakan Git, tutorial yang sangat mendetail ini mungkin tidak diperlukan untuk Anda. Saya lebih menyarankan untuk membaca tutorial lain di mana saya hanya menyajikan panduan utama, tanpa panduan langkah demi langkah yang mendetail:


- Pengguna berpengalaman**:

https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Jika Anda memilih untuk tidak mengatur lingkungan lokal Anda, ikuti tutorial lain yang dirancang untuk pemula, di mana kita membuat perubahan secara langsung melalui antarmuka web GitHub:


- Pemula (antarmuka web)**:

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Prasyarat

Diperlukan perangkat lunak untuk mengikuti tutorial ini:


- [GitHub Desktop](https://desktop.github.com/);
- Editor file markdown seperti [Obsidian](https://obsidian.md/);
- Editor kode ([VSC] (https://code.visualstudio.com/) atau [Sublime Text] (https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Prasyarat sebelum memulai tutorial:


- Memiliki [akun GitHub](https://github.com/signup);
- Memiliki fork dari [Plan ₿ Repositori sumber jaringan] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Memiliki [profil profesor di Plan ₿ Network] (https://planb.network/professors) (hanya jika Anda mengajukan tutorial lengkap).

Jika Anda memerlukan bantuan untuk mendapatkan prasyarat ini, tutorial saya yang lain akan membantu Anda:

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Setelah semuanya siap dan lingkungan lokal Anda diatur dengan benar dengan fork Anda sendiri dari Plan ₿ Network, Anda dapat mulai menambahkan tutorial.


## 1 - Membuat cabang baru

Buka peramban Anda dan buka halaman repositori repositori Plan ₿ Network. Ini adalah fork yang telah Anda buat di GitHub. URL fork Anda akan terlihat seperti: `https://github.com/[nama pengguna Anda]/konten-pendidikan-bitcoin`:

![TUTO](assets/fr/03.webp)

Pastikan Anda berada di cabang utama `dev` lalu klik tombol `Sinkronisasi fork`. Jika fork Anda belum diperbarui, GitHub akan menawarkan untuk memperbarui cabang Anda. Lanjutkan dengan pembaruan ini. Sebaliknya, jika cabang Anda sudah mutakhir, GitHub akan memberi tahu Anda:

![TUTO](assets/fr/04.webp)

Buka perangkat lunak GitHub Desktop dan pastikan garpu Anda dipilih dengan benar di sudut kiri atas jendela:

![TUTO](assets/fr/05.webp)

Klik pada tombol `Mengambil asal`. Jika repositori lokal Anda sudah diperbarui, GitHub Desktop tidak akan menyarankan tindakan tambahan apa pun. Jika tidak, opsi `Tarik asal` akan muncul. Klik tombol ini untuk memperbarui repositori lokal Anda:

![TUTO](assets/fr/06.webp)

Verifikasi bahwa Anda memang berada di `dev` cabang utama:

![TUTO](assets/fr/07.webp)

Klik pada cabang ini, lalu klik tombol `Cabang Baru`:

![TUTO](assets/fr/08.webp)

Pastikan bahwa cabang baru didasarkan pada repositori sumber, yaitu `PlanB-Network/bitcoin-educational-content`.

Beri nama cabang Anda sedemikian rupa sehingga judulnya jelas mengenai tujuannya, dengan menggunakan tanda hubung untuk memisahkan setiap kata. Sebagai contoh, katakanlah tujuan kita adalah menulis tutorial tentang penggunaan perangkat lunak Sparrow Wallet. Dalam kasus ini, cabang kerja yang didedikasikan untuk menulis tutorial ini dapat diberi nama: `tuto-sparrow-wallet-loic`. Setelah nama yang sesuai dimasukkan, klik `Buat cabang` untuk mengonfirmasi pembuatan cabang:

![TUTO](assets/fr/09.webp)

Sekarang klik tombol `Publish branch` untuk menyimpan cabang kerja baru Anda ke fork online Anda di GitHub:

![TUTORIAL](assets/fr/10.webp)

Sekarang, di GitHub Desktop, Anda seharusnya berada di cabang baru Anda. Ini berarti bahwa semua perubahan yang dibuat secara lokal di komputer Anda akan disimpan secara eksklusif di cabang khusus ini. Selain itu, selama cabang ini tetap dipilih di GitHub Desktop, file yang terlihat secara lokal di komputer Anda sesuai dengan file dari cabang ini (`tuto-sparrow-wallet-loic`), dan bukan dari cabang utama (`dev`).

![TUTORIAL](assets/fr/11.webp)

Untuk setiap artikel baru yang ingin Anda publikasikan, Anda perlu membuat cabang baru dari `dev`. Cabang di Git adalah versi paralel dari proyek, yang memungkinkan Anda untuk membuat perubahan tanpa memengaruhi cabang utama, hingga pekerjaan siap untuk digabungkan.

## 2 - Menambahkan file tutorial

Setelah cabang kerja dibuat, sekarang saatnya untuk mengintegrasikan tutorial baru Anda. Anda memiliki dua opsi: menggunakan skrip Python, yang mengotomatiskan pembuatan dokumen yang diperlukan, atau secara manual membuat setiap file. Kita akan melihat langkah-langkah yang harus diikuti untuk setiap opsi.

### Dengan skrip Python saya

Anda perlu menginstal pada mesin Anda:


- Python 3.8 atau lebih tinggi.

Untuk menggunakan skrip, arahkan ke folder tempat skrip disimpan. Skrip ini terletak di Rencana ₿ Repositori data jaringan di jalur: `konten-pendidikan-bitcoin/konten-skrip/tutorial-terkait/pencipta-data`.

Setelah berada di dalam folder, instal dependensi:

```
pip install -r requirements.txt
```

Kemudian luncurkan perangkat lunak dengan perintah tersebut:

```
python3 main.py
```

Antarmuka pengguna grafis (GUI) akan terbuka. Pertama kali, Anda harus memasukkan semua informasi yang diperlukan, tetapi pada penggunaan berikutnya, skrip akan mengingat informasi pribadi Anda, sehingga Anda tidak perlu memasukkannya lagi.

![DATA-CREATOR-PY](assets/fr/37.webp)

Mulailah dengan memasukkan jalur lokal ke folder `/tutorials` di repositori kloning Anda (`.../bitcoin-educational-content/tutorials/`). Anda dapat memasukkannya secara manual atau mengklik tombol "Browse" untuk menavigasi menggunakan file explorer Anda.

![DATA-CREATOR-PY](assets/fr/38.webp)

Pilih bahasa yang akan Anda gunakan untuk menulis tutorial.

![DATA-CREATOR-PY](assets/fr/39.webp)

Di bidang "ID GitHub Kontributor", masukkan nama pengguna GitHub Anda.

![DATA-CREATOR-PY](assets/fr/40.webp)

Selanjutnya, Anda perlu mengisi profil profesor Anda. Ada beberapa opsi yang tersedia:
- Masukkan huruf pertama dari nama Anda di kolom "Professor Name". Nama Anda kemudian akan muncul di daftar dropdown "Prof. Suggestions" yang terletak di bawah. Pilih dengan mengkliknya;
- Atau, Anda dapat langsung mengklik daftar dropdown "Prof. Suggestions" dan memilih nama profesor Anda.

Tindakan ini akan secara otomatis mengisi UUID profesor Anda di kolom yang sesuai.


![DATA-CREATOR-PY](assets/fr/41.webp)

Jika Anda belum memiliki profil profesor, lihat tutorial ini:

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Kemudian klik tombol "Tutorial Baru".

![DATA-CREATOR-PY](assets/fr/42.webp)

Pilih kategori utama untuk tutorial Anda. Kemudian, pilih subkategori yang relevan berdasarkan kategori utama yang Anda pilih.

![DATA-CREATOR-PY](assets/fr/43.webp)

Tentukan tingkat kesulitan tutorial.

![DATA-CREATOR-PY](assets/fr/44.webp)

Pilih nama untuk direktori yang dibuat khusus untuk tutorial Anda. Nama folder ini harus mencerminkan perangkat lunak yang dibahas dalam tutorial, dengan menggunakan tanda hubung untuk memisahkan kata-kata. Sebagai contoh, folder ini dapat diberi nama `dompet-merah`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` adalah UUID dari perusahaan atau organisasi di balik alat yang tercakup dalam tutorial, yang tersedia [dalam daftar proyek](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Sebagai contoh, untuk tutorial mengenai Sparrow Wallet, Anda dapat menemukan `project_id` di dalam file: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Informasi ini ditambahkan ke file YAML tutorial Anda karena Plan ₿ Network memiliki database perusahaan dan organisasi yang aktif dalam Bitcoin atau proyek-proyek terkait. Dengan menambahkan `project_id` yang terkait, Anda menautkan konten Anda ke entitas yang relevan.

***Pembaruan:*** Dalam versi baru skrip, Anda tidak perlu lagi memasukkan `project_id` secara manual. Fungsi pencarian telah ditambahkan untuk mencari proyek berdasarkan nama dan secara otomatis mengambil `project_id` yang sesuai. Ketik awal nama proyek di kolom "Nama Proyek" untuk mencarinya, lalu pilih perusahaan yang diinginkan dari menu dropdown. `project_id` akan secara otomatis terisi pada kolom di bawah ini. Anda juga dapat memasukkannya secara manual jika diperlukan.

![DATA-CREATOR-PY](assets/fr/46.webp)

Untuk tag, pilih 2 atau 3 kata kunci yang relevan yang terkait dengan konten tutorial Anda, pilih secara eksklusif dari [Daftar tag Paket ₿ Jaringan] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Perangkat lunak ini juga menyediakan fungsi pencarian kata kunci dengan daftar tarik-turun.

![DATA-CREATOR-PY](assets/fr/47.webp)

Setelah semua informasi dimasukkan dan diverifikasi, klik "Buat Tutorial" untuk mengonfirmasi pembuatan file tutorial Anda. Ini akan membuat folder tutorial Anda dan semua file yang diperlukan dalam kategori yang dipilih secara lokal.

![DATA-CREATOR-PY](assets/fr/48.webp)

Anda sekarang dapat melewati subbagian "Tanpa skrip Python saya" dan juga langkah 3, "Mengisi file YAML," karena skrip telah menyelesaikan tindakan ini untuk Anda. Lanjutkan langsung ke langkah 4 dan mulailah menulis tutorial Anda.

Untuk informasi lebih lanjut tentang skrip Python ini, Anda juga dapat melihat [README] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Tanpa skrip Python saya

Buka manajer file Anda dan arahkan ke folder `bitcoin-educational-content`, yang mewakili klon lokal dari repositori Anda. Anda biasanya dapat menemukannya di bawah `Documents\GitHub\bitcoin-educational-content`.

Di dalam direktori ini, Anda perlu mencari subfolder yang sesuai untuk menempatkan tutorial Anda. Pengaturan folder mencerminkan bagian yang berbeda dari situs web Plan ₿ Network. Dalam contoh kita, karena kita ingin menambahkan tutorial mengenai Sparrow Wallet, kita harus menavigasi ke jalur berikut: `bitcoin-educational-content\tutorials\wallet`, yang sesuai dengan bagian `WALLET` di situs web:

![TUTO](assets/fr/12.webp)

Di dalam folder `wallet`, Anda perlu membuat direktori baru yang secara khusus didedikasikan untuk tutorial Anda. Nama folder ini harus menunjukkan perangkat lunak yang dibahas dalam tutorial, pastikan untuk menghubungkan kata-kata dengan tanda hubung. Dalam contoh saya, folder ini akan diberi nama `dompet-pelangi`:

![TUTO](assets/fr/13.webp)

Dalam sub-folder baru yang didedikasikan untuk tutorial Anda, beberapa elemen perlu ditambahkan:


- Buat folder `assets`, yang dimaksudkan untuk menerima semua ilustrasi yang diperlukan untuk tutorial Anda;
- Di dalam folder `assets` ini, Anda perlu membuat sub-folder yang diberi nama sesuai dengan kode bahasa asli tutorial. Sebagai contoh, jika tutorial ditulis dalam bahasa Inggris, sub-folder ini harus diberi nama `en`. Letakkan semua visual tutorial di sana (diagram, gambar, tangkapan layar, dll.).
- File `tutorial.yml` harus dibuat untuk mencatat detail yang terkait dengan tutorial Anda;
- Sebuah file format markdown harus dibuat untuk menulis konten aktual dari tutorial Anda. File ini harus diberi judul sesuai dengan kode bahasa penulisan. Sebagai contoh, untuk tutorial yang ditulis dalam bahasa Prancis, file tersebut harus diberi nama `fr.md`.

![TUTO](assets/fr/14.webp)

Sebagai rangkuman, berikut ini hierarki file yang harus dibuat:

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Isi file YAML

Isi file `tutorial.yml` dengan menyalin templat berikut:


```
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

professor_id:

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributor_names:
      - 
    reward:
```

Berikut adalah bidang yang wajib diisi:

- **id** : Sebuah UUID (_Universally Unique Identifier_) yang mengidentifikasi tutorial secara unik. Anda dapat membuatnya menggunakan [alat online](https://www.uuidgenerator.net/version4). Satu-satunya persyaratan adalah UUID ini harus acak untuk menghindari konflik dengan UUID lain di platform;

- **project_id** : UUID dari perusahaan atau organisasi yang terkait dengan alat yang dibahas dalam tutorial [dari daftar proyek](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Misalnya, jika Anda membuat tutorial tentang perangkat lunak Green Wallet, Anda dapat menemukan `project_id` dalam file berikut: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Informasi ini ditambahkan ke file YAML tutorial Anda karena Plan ₿ Network mempertahankan basis data dari semua perusahaan dan organisasi yang beroperasi di Bitcoin atau proyek terkait. Dengan menambahkan `project_id` dari entitas yang terkait dengan tutorial Anda, Anda membuat hubungan antara kedua elemen tersebut;

- **tags** : 2 atau 3 kata kunci relevan terkait dengan isi tutorial, dipilih secara eksklusif [dari daftar tag Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category** : Sub-kategori yang sesuai dengan isi tutorial sesuai dengan struktur situs Plan ₿ Network (misalnya untuk dompet: `desktop`, `hardware`, `mobile`, `backup`);

- **level** : Tingkat kesulitan tutorial, dipilih dari:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : `professor_id` Anda (UUID) seperti yang ditampilkan pada [profil profesor Anda](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language** : Bahasa asli dari tutorial (misalnya `fr`, `en`, dll.);

- **proofreading** : Informasi tentang proses pengoreksian. Lengkapi bagian pertama karena mengoreksi tutorial Anda sendiri dihitung sebagai validasi pertama:
    - **language** : Kode bahasa untuk pengoreksian (misalnya `fr`, `en`, dll.).
    - **last_contribution_date** : Tanggal hari ini.
    - **urgency** : 1
    - **contributor_names** : ID GitHub Anda.
    - **reward** : 0

Untuk detail lebih lanjut mengenai ID guru Anda, silakan lihat tutorial yang sesuai:

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency: 1
    contributor_names:
      - LoicPandul
    reward: 0
```

Setelah Anda selesai memodifikasi file `tutorial.yml`, simpan dokumen Anda dengan mengklik `File > Save`:

![TUTO](assets/fr/16.webp)

Anda sekarang dapat menutup editor kode Anda.

## 4 - Isi File Penurunan Harga

Sekarang, Anda dapat membuka file yang akan menjadi tempat tutorial Anda, yang diberi nama dengan kode bahasa Anda, seperti `fr.md`. Masuk ke Obsidian, di sisi kiri jendela, gulir pohon folder sampai Anda menemukan folder tutorial dan file yang Anda cari:

![TUTO](assets/fr/18.webp)

Klik pada file untuk membukanya:

![TUTO](assets/fr/19.webp)

Kita akan mulai dengan mengisi bagian `Properties` di bagian atas dokumen.

![TUTO](assets/fr/20.webp)

Tambahkan dan isi blok kode berikut secara manual:

```
---
name: [Title]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Isi nama tutorial Anda dan deskripsi singkatnya:

![TUTO](assets/fr/22.webp)

Kemudian, tambahkan jalur gambar sampul di awal tutorial Anda. Untuk melakukan ini, perhatikan:

```
![cover-sparrow](assets/cover.webp)
```

Sintaks ini akan berguna ketika Anda perlu menambahkan gambar ke dalam tutorial Anda. Tanda seru menunjukkan bahwa itu adalah gambar, dengan teks alternatif (alt) yang ditentukan di antara tanda kurung. Jalur ke gambar ditunjukkan di antara tanda kurung:

![TUTO](assets/fr/23.webp)

## 5 - Tambahkan Logo dan Sampul

Di dalam folder `assets`, Anda harus menambahkan file bernama `logo.webp`, yang akan berfungsi sebagai gambar mini untuk artikel Anda. Gambar ini harus dalam format `.webp` dan harus memiliki dimensi persegi agar selaras dengan antarmuka pengguna. Anda bebas memilih logo perangkat lunak yang tercakup dalam tutorial atau gambar lain yang relevan, asalkan gambar tersebut bebas dari hak cipta. Selain itu, tambahkan juga gambar berjudul `cover.webp` di tempat yang sama. Gambar ini akan ditampilkan di bagian atas tutorial Anda. Pastikan bahwa gambar ini, seperti halnya logo, menghormati hak penggunaan dan sesuai dengan konteks tutorial Anda:

## 6 - Menulis Tutorial dan Menambahkan Visual

Lanjutkan menulis tutorial Anda dengan menyusun konten Anda. Ketika Anda ingin mengintegrasikan subjudul, terapkan format penurunan harga yang sesuai dengan mengawali teks dengan `##`:

![TUTO](assets/fr/24.webp)

Subfolder bahasa dalam folder `assets` digunakan untuk menyimpan diagram dan visual yang akan menyertai tutorial Anda. Sebisa mungkin, hindari menyertakan teks dalam gambar agar konten Anda dapat diakses oleh audiens internasional. Tentu saja, perangkat lunak yang disajikan akan berisi teks, tetapi jika Anda menambahkan diagram atau indikasi tambahan pada tangkapan layar perangkat lunak, lakukan tanpa teks atau, jika terbukti sangat diperlukan, gunakan bahasa Inggris.

![TUTO](assets/fr/25.webp)

Untuk menamai gambar Anda, cukup gunakan nomor yang sesuai dengan urutan kemunculannya dalam tutorial, yang diformat dengan dua digit (atau tiga digit jika tutorial Anda berisi lebih dari 99 gambar). Contohnya, beri nama gambar pertama Anda `01.webp`, gambar kedua `02.webp`, dan seterusnya.

Gambar Anda harus dalam format `.webp` secara eksklusif. Jika diperlukan, Anda dapat menggunakan [perangkat lunak konversi gambar saya] (https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Untuk menyisipkan diagram ke dalam dokumen Anda, gunakan perintah Markdown berikut ini, pastikan untuk menentukan teks alternatif yang sesuai serta jalur gambar yang benar:

```
![sparrow](assets/fr/01.webp)
```

Tanda seru di awal mengindikasikan bahwa itu adalah gambar. Teks alternatif, yang membantu aksesibilitas dan SEO, ditempatkan di antara tanda kurung. Terakhir, jalur ke gambar ditunjukkan di antara tanda kurung.

Jika Anda ingin membuat diagram Anda sendiri, pastikan untuk mematuhi piagam grafis Plan ₿ Network untuk memastikan konsistensi visual:


- Huruf **: Gunakan [Rubik] (https://fonts.google.com/specimen/Rubik);
- Warna**:
 - Oranye: #FF5C00
 - Hitam: #000000
 - Putih: #FFFFFF

**Sangat penting bahwa semua visual yang diintegrasikan ke dalam tutorial Anda bebas dari hak cipta atau menghormati lisensi file sumbernya**. Selain itu, semua diagram yang dipublikasikan di Plan ₿ Network tersedia di bawah lisensi CC-BY-SA, dengan cara yang sama seperti teks.

**-> Tips:** Ketika berbagi file secara publik, seperti gambar, penting untuk menghapus metadata yang tidak perlu. Metadata ini dapat berisi informasi sensitif, seperti data lokasi, tanggal pembuatan, atau detail tentang pembuatnya. Untuk melindungi privasi Anda, sebaiknya hapus metadata ini. Untuk menyederhanakan proses ini, Anda dapat menggunakan alat khusus seperti [Exif Cleaner] (https://exifcleaner.com/), yang memungkinkan pembersihan metadata dokumen melalui seret dan lepas.

## 7 - Simpan dan Kirimkan Tutorial

Setelah Anda selesai menulis tutorial Anda dalam bahasa pilihan Anda, langkah selanjutnya adalah mengirimkan **Permintaan Penerjemahan**. Administrator kemudian akan menambahkan terjemahan yang kurang dari tutorial Anda, berkat metode penerjemahan otomatis kami dengan tinjauan manusia.

Untuk melanjutkan dengan Pull Request, buka perangkat lunak GitHub Desktop. Perangkat lunak ini akan secara otomatis mendeteksi perubahan yang telah Anda lakukan secara lokal di cabang Anda dibandingkan dengan repositori asli. Sebelum melanjutkan, periksa dengan cermat di sisi kiri antarmuka bahwa perubahan ini sesuai dengan yang Anda harapkan:

![TUTO](assets/fr/28.webp)

Tambahkan judul untuk komit Anda, lalu klik tombol biru `Komit ke [cabang Anda]` untuk memvalidasi perubahan ini:

![TUTO](assets/fr/29.webp)

Komit adalah penyimpanan perubahan yang dibuat pada cabang, disertai dengan pesan deskriptif, yang memungkinkan untuk mengikuti evolusi proyek dari waktu ke waktu. Ini semacam pos pemeriksaan perantara.

Kemudian klik pada tombol `Push origin`. Ini akan mengirim komit Anda ke fork Anda:

![TUTO](assets/fr/30.webp)

Jika Anda belum menyelesaikan tutorial ini, Anda dapat kembali lagi nanti dan membuat komit baru. Jika Anda telah menyelesaikan perubahan Anda untuk cabang ini, klik tombol `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Anda dapat memeriksa untuk terakhir kalinya apakah modifikasi Anda sudah benar, lalu klik tombol `Buat permintaan tarik`:

![TUTO](assets/fr/32.webp)

Pull Request adalah permintaan yang dibuat untuk mengintegrasikan perubahan dari cabang Anda ke cabang utama repositori Plan ₿ Network, yang memungkinkan peninjauan dan diskusi perubahan sebelum penggabungan.

Anda akan secara otomatis diarahkan ke peramban Anda di GitHub ke halaman persiapan Pull Request Anda:

![TUTO](assets/fr/33.webp)

Tunjukkan sebuah judul yang secara singkat meringkas perubahan yang ingin Anda gabungkan dengan repositori sumber. Tambahkan komentar singkat yang menjelaskan perubahan-perubahan ini (jika Anda memiliki nomor isu yang terkait dengan pembuatan tutorial Anda, ingatlah untuk mencatatnya di komentar `Tutup #{nomor isu}`), lalu klik tombol hijau `Buat permintaan tarik` untuk mengonfirmasi permintaan penggabungan:

![TUTO](assets/fr/34.webp)

PR Anda kemudian akan terlihat di tab `Tarik Permintaan` pada repositori Rencana ₿ Jaringan utama. Yang harus Anda lakukan adalah menunggu hingga administrator menghubungi Anda untuk mengonfirmasi penggabungan kontribusi Anda atau meminta modifikasi tambahan.

![TUTO](assets/fr/35.webp)

Setelah PR Anda digabungkan dengan cabang utama, disarankan untuk menghapus cabang yang sedang bekerja (`tuto-sparrow-wallet`) untuk mempertahankan riwayat yang bersih pada fork Anda. GitHub akan secara otomatis menawarkan opsi ini pada halaman PR Anda:

![TUTO](assets/fr/36.webp)

Pada perangkat lunak GitHub Desktop, Anda dapat beralih kembali ke cabang utama fork Anda (`dev`).

![TUTO](assets/fr/07.webp)

Jika Anda ingin membuat perubahan pada kontribusi Anda setelah Anda mengirimkan PR Anda, prosedurnya tergantung pada status PR Anda saat ini:


- Jika PR Anda masih terbuka dan belum digabungkan, lakukan perubahan secara lokal dan tetap berada di cabang yang sama. Setelah modifikasi selesai, gunakan tombol `Push origin` untuk menambahkan komit baru ke PR yang masih terbuka;
- Jika PR Anda telah digabungkan dengan cabang utama, Anda harus memulai proses dari awal dengan membuat cabang baru, lalu mengirimkan PR baru. Pastikan repositori lokal Anda disinkronkan dengan repositori sumber Plan ₿ Network sebelum melanjutkan.

Jika Anda mengalami kesulitan teknis dalam mengirimkan tutorial Anda, jangan ragu untuk meminta bantuan di [grup Telegram khusus untuk kontribusi](https://t.me/PlanBNetwork_ContentBuilder). Terima kasih!


