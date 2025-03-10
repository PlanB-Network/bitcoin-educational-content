---
name: Kontribusi - Tutorial Git (lanjutan)
description: Panduan untuk pengguna tingkat lanjut untuk menawarkan tutorial tentang Plan ₿ Network dengan Git
---
![cover](assets/cover.webp)

Sebelum mengikuti tutorial menambahkan tutorial baru ini, Anda harus menyelesaikan beberapa langkah awal. Jika Anda belum melakukannya, silakan lihat tutorial pengantar ini terlebih dahulu, lalu kembali ke sini:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Anda sudah memiliki :


- Pilih tema untuk tutorial Anda;
- Menghubungi tim Plan ₿ Network melalui [Grup Telegram](https://t.me/PlanBNetwork_ContentBuilder) atau paolo@planb.network ;
- Pilih alat kontribusi Anda.

Dalam tutorial untuk pengguna Git yang sudah berpengalaman ini, kami akan meringkas secara singkat langkah-langkah utama dan panduan penting untuk menawarkan tutorial Plan ₿ Network yang baru. Jika Anda tidak terbiasa dengan Git dan GitHub, saya sarankan Anda untuk mengikuti salah satu dari 2 tutorial lain yang lebih terperinci yang akan membawa Anda langkah demi langkah :


- Menengah (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Pemula (antarmuka web)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Alat yang disarankan

Untuk mengedit file Penurunan harga :


- Obsidian** (Gratis, bukan sumber terbuka)
- Tandai Teks** (Gratis, sumber terbuka)
- Zettlr** (Gratis, sumber terbuka)
- Typora** (Perangkat lunak berbayar, ~€15, bukan sumber terbuka)

Untuk Git :


- Git** (Gratis, sumber terbuka)
- GitHub Desktop** (Gratis, sumber terbuka)
- Sourcetree** (Gratis, bukan sumber terbuka)

Untuk mengedit file YAML :


- Kode Visual Studio** (Gratis, sumber terbuka)
- Sublime Text** (Gratis dengan batasan, bukan sumber terbuka)

Untuk membuat diagram dan visual :


- Canva** (Gratis dengan opsi berbayar, bukan sumber terbuka)
- Inkscape** (Gratis, sumber terbuka)
- Penpot** (Gratis, sumber terbuka)

## Alur kerja

### 1 - Konfigurasikan lingkungan lokal Anda


- Anda harus memiliki fork Anda sendiri dari [Paket ₿ Repositori Jaringan di GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sinkronisasi cabang utama (`dev`) dari fork Anda dengan repositori sumber.
- Perbarui klon lokal Anda.

```
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Membuat cabang baru


- Pastikan Anda berada di cabang `dev`.
- Buat cabang baru dengan nama deskriptif (mis. `tuto-green-wallet-loic`).
- Publikasikan cabang ini di fork online Anda.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Tambahkan dokumen tutorial

***Catatan:*** Anda dapat mengotomatiskan langkah 3 dan 4 dengan menggunakan [skrip GUI Python saya] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Jalankan langsung dari foldernya di klon lokal Anda, lalu isi kolom yang diperlukan pada GUI. Untuk informasi lebih lanjut tentang cara menginstal dan menggunakannya, lihat [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Jika Anda lebih suka melakukannya secara manual, ikuti langkah-langkah berikut ini:


- Cari folder yang sesuai di repositori lokal (misal: `tutorial/wallet`).
- Buat direktori yang didedikasikan untuk tutorial dengan nama yang jelas (misal: `green-wallet`). Nama folder ini juga akan menentukan jalur URL tutorial. Nama ini harus menggunakan huruf kecil, tanpa karakter khusus (kecuali tanda penghubung) dan tanpa spasi.
- Tambahkan item-item berikut ke direktori ini:
    - Subfolder bernama `assets` yang berisi file :
        - Dua gambar `.webp`:
            - `logo.webp`: Logo tutorial (format persegi dengan latar belakang). Logo ini harus mewakili perangkat lunak atau alat yang disajikan. Jika tutorial tidak spesifik untuk suatu alat (misalnya: panduan umum untuk membuat frasa mnemonik), Anda dapat memilih visual yang sesuai (misalnya: ikon umum).
            - `cover.webp`: Gambar sampul yang ditampilkan di awal tutorial.
        - Subfolder yang berisi kode bahasa asli tutorial. Sebagai contoh, jika tutorial ditulis dalam bahasa Inggris, subfolder ini harus diberi nama `en'. Tempatkan semua visual tutorial (diagram, gambar, tangkapan layar, dll.) dalam folder ini.
    - File `tutorial.yml` yang berisi metadata (penulis, tag, kategori, tingkat kesulitan, dll.).
    - File Markdown yang berisi tutorial, diberi nama sesuai dengan kode bahasa (misalnya `fr.md`, `en.md`, dll.).

```
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Isi file YAML


- Lengkapi file `tutorial.yml` sebagai berikut:

```
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
```

Berikut ini adalah bidang yang wajib diisi:


- id**: Sebuah UUID (Pengenal Unik Universal) untuk mengidentifikasi tutorial secara unik. Anda dapat membuatnya dengan [alat bantu online] (https://www.uuidgenerator.net/version4). Satu-satunya batasan adalah UUID ini harus acak, agar tidak bertentangan dengan UUID lain di platform;
- project_id** : UUID dari perusahaan atau organisasi di balik alat yang disajikan dalam tutorial [dari daftar proyek] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Sebagai contoh, jika Anda sedang melakukan tutorial mengenai perangkat lunak Green Wallet, Anda dapat menemukan `project_id` ini di file berikut: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Informasi ini ditambahkan dalam file YAML tutorial Anda karena Plan ₿ Network menyimpan database semua perusahaan dan organisasi yang beroperasi dengan Bitcoin atau proyek-proyek terkait. Dengan menambahkan `project_id` dari entitas yang ditautkan ke tutorial Anda, Anda membuat tautan antara dua elemen;
- tag**: 2 atau 3 kata kunci yang relevan terkait dengan konten tutorial, yang dipilih secara eksklusif [dari daftar tag Paket ₿ Jaringan](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- kategori** : Subkategori yang sesuai dengan konten tutorial, sesuai dengan Paket ₿ Struktur jaringan (misalnya untuk dompet: `deskstop`, `perangkat keras`, `seluler`, `cadangan`);
- tingkat** : Tingkat kesulitan tutorial, dari :
    - pemula
    - 'menengah'
    - `advanced`
    - 'ahli'
- profesor**: `kontributor_id` Anda (BIP39 kata) seperti yang ditampilkan di [profil pengajar Anda] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- bahasa_asli** : Bahasa asli tutorial (misalnya `fr`, `en`, dll.) ;
- pengoreksian**: Informasi tentang proses proofreading. Isi bagian pertama, karena mengoreksi tutorial Anda sendiri dianggap sebagai validasi pertama:
    - bahasa**: Mengoreksi kode bahasa (misalnya `fr`, `en`, dsb.).
    - tanggal_kontribusi_terakhir**: Tanggal hari ini.
    - urgensi** : Biarkan kosong.
    - kontributor_id** : ID GitHub Anda.
    - hadiah** : Biarkan kosong.

Untuk detail lebih lanjut mengenai ID guru Anda, silakan lihat tutorial yang sesuai:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
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
```

### 5 - Menulis konten


- Lengkapi properti file Penurunan harga dengan file :
    - Judul (`nama`).
    - Deskripsi singkat (`description`).
- Tambahkan gambar sampul di bagian atas tutorial menggunakan sintaks Markdown (ganti "hijau" dengan nama alat yang ditampilkan):

```
![cover-green](assets/cover.webp)
```


- Tuliskan konten tutorial dalam Markdown :
    - Gunakan judul, daftar, dan paragraf yang terstruktur dengan baik.
    - Menyisipkan visual menggunakan sintaks Markdown :

```
![nom-image](assets/en/001.webp)
```


- Tempatkan diagram dan gambar di subfolder bahasa yang sesuai, di `/assets`.

### 6 - Simpan dan kirimkan tutorial


- Simpan perubahan Anda secara lokal dengan membuat komit dengan pesan deskriptif.
- Dorong perubahan ke fork GitHub Anda.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Setelah selesai, buat Pull Request (PR) di GitHub untuk mengusulkan integrasi modifikasi Anda.
- Tambahkan judul dan deskripsi singkat pada PR. Sebutkan nomor terbitan yang sesuai dalam komentar.

### 7 - Mengoreksi dan menggabungkan


- Tunggu validasi atau umpan balik dari administrator.
- Jika perlu, lakukan koreksi dan dorong komit baru.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Setelah PR digabungkan, Anda dapat menghapus cabang yang sedang bekerja.

## Standar pembuatan konten


- Pemformatan yang didukung pada platform** :
    - Penurunan Harga Klasik: daftar, tautan, gambar, kutipan, cetak tebal, cetak miring, dll.
    - LaTeX (hanya blok, tidak sebaris): dibatasi oleh `$$`.
    - Kode sebaris: Sintaks dengan satu backtick.
    - Blok kode: Sintaks dengan tiga tanda centang, misalnya :

```
print("Hello, Bitcoin!")
```


- Ilustrasi dan diagram** :
    - Semua gambar harus dalam format WebP. Gunakan alat gratis ini untuk mengonversinya jika diperlukan: [ImagesConverter] (https://github.com/LoicPandul/ImagesConverter).
    - Beri nama visual dengan 2 atau 3 digit (misalnya `001.webp`, `002.webp`).
    - Untuk tutorial dompet seluler atau perangkat keras, gunakan mock-up.
    - Gunakan hanya visual yang dibuat sendiri atau bebas royalti.
    - Pastikan mereka relevan dan berkualitas tinggi.
- Piagam grafis** :
    - Font: [Rubik] (https://fonts.google.com/specimen/Rubik).
    - Rencana Warna ₿ Jaringan :
        - Oranye: `#FF5C00`
        - Hitam: `#000000`
        - Putih: `#FFFFFF`

Jika Anda mengalami kesulitan teknis dalam mengirimkan tutorial Anda, jangan ragu untuk meminta bantuan di [grup Telegram khusus untuk kontribusi](https://t.me/PlanBNetwork_ContentBuilder). Terima kasih banyak!