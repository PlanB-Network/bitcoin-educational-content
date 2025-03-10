---
name: Kontribusi - Tutorial dengan GitHub Desktop (Menengah)
description: Panduan lengkap untuk mengusulkan tutorial tentang Plan ₿ Network menggunakan GitHub Desktop
---
![cover](assets/cover.webp)

Sebelum mengikuti tutorial tentang cara menambahkan tutorial baru ini, Anda harus sudah menyelesaikan beberapa langkah awal. Jika Anda belum melakukannya, saya mengundang Anda untuk terlebih dahulu membaca tutorial pengantar ini, lalu kembali ke sini:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Anda sudah melakukannya:


- Memilih tema tutorial Anda;
- Menghubungi tim Plan ₿ Network melalui [grup Telegram](https://t.me/PlanBNetwork_ContentBuilder) atau paolo@planb.network;
- Memilih alat kontribusi Anda.

Dalam tutorial ini, kita akan melihat cara menambahkan tutorial Anda di Plan ₿ Network dengan menyiapkan lingkungan lokal Anda dengan GitHub Desktop. Jika Anda sudah mahir menggunakan Git, tutorial yang sangat mendetail ini mungkin tidak diperlukan untuk Anda. Saya lebih menyarankan untuk membaca tutorial lain di mana saya hanya menyajikan panduan utama, tanpa panduan langkah demi langkah yang mendetail:


- Pengguna berpengalaman**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Jika Anda memilih untuk tidak mengatur lingkungan lokal Anda, ikuti tutorial lain yang dirancang untuk pemula, di mana kita membuat perubahan secara langsung melalui antarmuka web GitHub:


- Pemula (antarmuka web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb

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

Anda harus menginstal di komputer Anda:
- Python 3.8 atau yang lebih baru.

Untuk menggunakan skrip, masuk ke folder tempat skrip disimpan. Skrip ini berada di repositori data Plan ₿ Network pada jalur: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Setelah berada di folder, instal dependensi:

```bash
pip install -r requirements.txt
```

Kemudian jalankan perangkat lunak dengan perintah:

```bash
python3 main.py
```

Antarmuka pengguna grafis (GUI) akan terbuka. Pada penggunaan pertama, Anda harus memasukkan semua informasi yang diperlukan, tetapi dalam penggunaan selanjutnya, skrip akan mengingat informasi pribadi Anda, sehingga Anda tidak perlu memasukkannya lagi.

![DATA-CREATOR-PY](assets/fr/37.webp)

Mulailah dengan memasukkan jalur lokal ke folder `/tutorials` dalam repositori yang telah Anda kloning (`.../bitcoin-educational-content/tutorials/`). Anda dapat memasukkannya secara manual atau mengklik tombol "Browse" untuk menjelajah melalui pengelola file Anda.

![DATA-CREATOR-PY](assets/fr/38.webp)

Pilih bahasa yang akan Anda gunakan untuk menulis tutorial Anda.

![DATA-CREATOR-PY](assets/fr/39.webp)

Di kolom "Contributor's GitHub ID", masukkan nama pengguna GitHub Anda.

![DATA-CREATOR-PY](assets/fr/40.webp)

Di kolom "PBN professor's ID", masukkan identitas Anda menggunakan kata-kata dari daftar BIP39, seperti yang muncul di [profil profesor Anda](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![DATA-CREATOR-PY](assets/fr/41.webp)

Jika Anda belum memiliki profil profesor, lihat tutorial ini:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Kemudian klik tombol "New Tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Pilih kategori utama untuk tutorial Anda. Kemudian, pilih subkategori yang sesuai berdasarkan kategori utama yang telah Anda pilih.

![DATA-CREATOR-PY](assets/fr/43.webp)

Tentukan tingkat kesulitan tutorial.

![DATA-CREATOR-PY](assets/fr/44.webp)

Pilih nama direktori yang dibuat khusus untuk tutorial Anda. Nama folder ini harus mencerminkan perangkat lunak yang dibahas dalam tutorial, menggunakan tanda hubung untuk memisahkan kata. Misalnya, folder dapat diberi nama `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` adalah UUID perusahaan atau organisasi di balik alat yang dibahas dalam tutorial, yang tersedia di [daftar proyek](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Misalnya, untuk tutorial tentang Sparrow Wallet, Anda dapat menemukan `project_id` dalam file: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Informasi ini ditambahkan ke file YAML tutorial Anda karena Plan ₿ Network memelihara database perusahaan dan organisasi yang aktif dalam ekosistem Bitcoin atau proyek terkait. Dengan menambahkan `project_id` yang terkait dengan tutorial Anda, Anda membuat tautan antara konten Anda dan entitas terkait.

***Pembaruan:*** Dalam versi terbaru skrip, Anda tidak perlu lagi memasukkan `project_id` secara manual. Fungsi pencarian telah ditambahkan untuk menemukan proyek berdasarkan nama dan mengambil `project_id` yang sesuai secara otomatis. Ketik awal nama proyek di kolom "Project Name" untuk mencarinya, lalu pilih perusahaan yang diinginkan dari menu dropdown. `project_id` akan otomatis terisi di kolom di bawahnya. Anda juga dapat memasukkannya secara manual jika diperlukan.

![DATA-CREATOR-PY](assets/fr/46.webp)

Untuk tag, pilih 2 atau 3 kata kunci yang relevan dengan konten tutorial Anda, yang hanya dipilih dari [daftar tag Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Perangkat lunak ini juga menyediakan fungsi pencarian kata kunci dengan daftar dropdown.

![DATA-CREATOR-PY](assets/fr/47.webp)

Setelah semua informasi dimasukkan dan diverifikasi, klik "Create Tutorial" untuk mengonfirmasi pembuatan file tutorial Anda. Ini akan menghasilkan folder tutorial Anda dan semua file yang diperlukan dalam kategori yang dipilih secara lokal.

![DATA-CREATOR-PY](assets/fr/48.webp)

Anda sekarang dapat melewati subbagian "Tanpa skrip Python saya", serta langkah 3 "Mengisi file YAML", karena skrip telah melakukan tindakan ini secara otomatis untuk Anda. Lanjutkan langsung ke langkah 4 dan mulai menulis tutorial Anda.

Untuk informasi lebih lanjut tentang skrip Python ini, Anda juga dapat membaca [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Tanpa skrip Python saya

Buka pengelola file Anda dan navigasikan ke folder `bitcoin-educational-content`, yang merupakan klon lokal dari repositori Anda. Biasanya, Anda dapat menemukannya di `Documents\GitHub\bitcoin-educational-content`.

Di dalam direktori ini, Anda perlu menemukan subfolder yang sesuai untuk meletakkan tutorial Anda. Struktur folder mencerminkan berbagai bagian dari situs web Plan ₿ Network. Dalam contoh ini, karena kami ingin menambahkan tutorial tentang Sparrow Wallet, navigasikan ke jalur berikut: `bitcoin-educational-content\tutorials\wallet`, yang sesuai dengan bagian `WALLET` di situs web:

![TUTO](assets/fr/12.webp)

Di dalam folder `wallet`, Anda perlu membuat direktori baru yang secara khusus didedikasikan untuk tutorial Anda. Nama folder ini harus menunjukkan perangkat lunak yang dibahas dalam tutorial, pastikan untuk menghubungkan kata-kata dengan tanda hubung. Dalam contoh saya, folder ini akan diberi nama `dompet-pelangi`:

![TUTO](assets/fr/13.webp)

Dalam sub-folder baru yang didedikasikan untuk tutorial Anda, beberapa elemen perlu ditambahkan:


- Buat folder `assets`, yang dimaksudkan untuk menerima semua ilustrasi yang diperlukan untuk tutorial Anda;
- Di dalam folder `assets` ini, Anda perlu membuat sub-folder yang diberi nama sesuai dengan kode bahasa asli tutorial. Sebagai contoh, jika tutorial ditulis dalam bahasa Inggris, sub-folder ini harus diberi nama `en`. Letakkan semua visual tutorial di sana (diagram, gambar, tangkapan layar, dll.).
- File `tutorial.yml` harus dibuat untuk merekam detail yang terkait dengan tutorial Anda;
- Sebuah file format markdown harus dibuat untuk menulis konten aktual dari tutorial Anda. File ini harus diberi judul sesuai dengan kode bahasa penulisan. Sebagai contoh, untuk tutorial yang ditulis dalam bahasa Prancis, file tersebut harus diberi nama `fr.md`.

![TUTO](assets/fr/14.webp)

Sebagai rangkuman, berikut ini hierarki file yang harus dibuat:

```plaintext
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

```yaml
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
````

Berikut ini adalah rincian bidang yang wajib diisi:


- **id**: Sebuah UUID (Pengenal Unik Universal) untuk mengidentifikasi tutorial secara unik. Anda dapat membuatnya dengan [alat bantu online] (https://www.uuidgenerator.net/version4). Satu-satunya persyaratan adalah bahwa UUID ini bersifat acak untuk menghindari konflik dengan UUID lain di platform;
- **project_id**: UUID dari perusahaan atau organisasi di balik alat yang disajikan dalam tutorial [dari daftar proyek] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Sebagai contoh, jika Anda membuat tutorial mengenai perangkat lunak Sparrow Wallet, Anda dapat menemukan `project_id` ini di dalam berkas berikut: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Informasi ini ditambahkan ke file YAML tutorial Anda karena Plan ₿ Network memiliki database semua perusahaan dan organisasi yang beroperasi dengan Bitcoin atau proyek-proyek terkait. Dengan menambahkan `project_id` dari entitas yang terkait dengan tutorial Anda, Anda membuat tautan antara dua elemen;
- **tags**: 2 atau 3 kata kunci yang relevan terkait dengan konten tutorial, yang dipilih secara eksklusif [dari daftar tag Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Sub-kategori yang sesuai dengan konten tutorial, sesuai dengan struktur situs Jaringan Plan ₿ Network (misalnya untuk dompet: `desktop`, `perangkat keras`, `seluler`, `cadangan`);
- **level**: Tingkat kesulitan tutorial, di antara:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: `contributor_id` Anda (BIP39 kata) seperti yang ditampilkan di [profil profesor Anda] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: Bahasa asli tutorial (misalnya `fr`, `en`, dll.);
- **proofreading**: Informasi tentang proses proofreading. Isi bagian pertama, karena mengoreksi tutorial Anda sendiri dianggap sebagai validasi pertama:
    - **language**: Kode bahasa dari proofreading (misalnya `fr`, `en`, dll.).
    - **last_contribution_date**: Tanggal hari ini.
    - **urgency**: Biarkan kosong.
    - **contributor_id**: ID GitHub Anda.
    - **reward**: Biarkan kosong.

Untuk detail lebih lanjut tentang pengenal profesor Anda, lihat tutorial terkait:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Berikut ini adalah contoh file `tutorial.yml` yang sudah selesai untuk tutorial mengenai dompet Blockstream Green:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Judul]
description: [Deskripsi]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```