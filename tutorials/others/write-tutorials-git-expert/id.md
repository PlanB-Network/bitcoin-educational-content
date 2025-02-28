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

Dalam tutorial untuk pengguna Git yang sudah berpengalaman ini, kami akan meringkas secara singkat langkah-langkah utama dan panduan penting untuk menawarkan tutorial Plan ₿ Network yang baru. Jika Anda tidak terbiasa dengan Git dan GitHub, saya sarankan Anda untuk mengikuti salah satu dari 2 tutorial lain yang lebih terperinci yang akan membawa Anda langkah demi langkah:


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

```bash
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

```bash
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

```bash
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
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tag:


  - dompet
  - perangkat lunak
  - kunci

kategori: Ponsel

tingkat: Pemula

kredit:

profesor: cukup-pribadi

# Mengoreksi metadata

bahasa_asli: fr

mengoreksi:


  - bahasa: fr

last_contribution_date: 2024-11-20

urgensi:

kontributor_id:


      - LoicPandul

hadiah:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Membuat komit dengan pesan deskriptif

git commit -m "Tambahkan tutorial dompet hijau"

# Dorong modifikasi Anda ke garpu Anda

git push asal tuto-dompet-hijau-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Buatlah sebuah komit yang menjelaskan koreksi yang dibuat

git commit -m "Koreksi setelah tinjauan ulang tutorial green-wallet"

# Mendorong koreksi pada garpu Anda

git push asal tuto-dompet-hijau-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Halo, Bitcoin!")

```