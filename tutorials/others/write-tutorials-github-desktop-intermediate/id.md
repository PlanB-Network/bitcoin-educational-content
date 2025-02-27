---
name: Kontribusi - Tutorial dengan GitHub Desktop (menengah)
description: Panduan lengkap untuk tutorial Plan ₿ Network dengan GitHub Desktop
---
![cover](assets/cover.webp)

Sebelum mengikuti tutorial menambahkan tutorial baru ini, Anda harus menyelesaikan beberapa langkah awal. Jika Anda belum melakukannya, silakan lihat tutorial pengantar ini terlebih dahulu, lalu kembali ke sini:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Anda sudah memiliki :


- Pilih tema untuk tutorial Anda;
- Menghubungi tim Plan ₿ Network melalui [Grup Telegram](https://t.me/PlanBNetwork_ContentBuilder) atau paolo@planb.network ;
- Pilih alat kontribusi Anda.

Dalam tutorial ini, kita akan melihat cara menambahkan tutorial Anda ke Plan ₿ Network dengan mengonfigurasi lingkungan lokal Anda dengan GitHub Desktop. Jika Anda sudah menguasai Git, tutorial yang sangat mendetail ini mungkin tidak diperlukan untuk Anda. Sebagai gantinya, saya sarankan Anda untuk melihat tutorial lain di mana saya hanya menyajikan panduan umum, tanpa panduan langkah demi langkah yang mendetail:


- Pengguna yang berpengalaman** :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Jika Anda memilih untuk tidak mengonfigurasi lingkungan lokal Anda, ikuti tutorial lain yang dirancang untuk pemula, di mana kami membuat perubahan secara langsung melalui antarmuka web GitHub :


- Pemula (antarmuka web)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Prasyarat

Diperlukan perangkat lunak untuk mengikuti tutorial ini:


- [GitHub Desktop](https://desktop.github.com/);
- Editor file markdown seperti [Obsidian](https://obsidian.md/);
- Editor kode ([VSC] (https://code.visualstudio.com/) atau [Sublime Text] (https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Prasyarat sebelum memulai tutorial :


- Memiliki [akun GitHub](https://github.com/signup);
- Memiliki fork dari [Plan ₿ Repositori sumber jaringan] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Memiliki [profil guru di Plan ₿ Network] (https://planb.network/professors) (hanya jika Anda menawarkan tutorial lengkap).

Jika Anda memerlukan bantuan untuk mendapatkan prasyarat ini, tutorial saya yang lain akan membantu:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Setelah semuanya siap dan lingkungan lokal Anda diatur dengan Plan ₿ Network fork Anda sendiri, Anda dapat mulai menambahkan tutorial.

## 1 - Membuat cabang baru

Buka browser Anda dan arahkan ke halaman fork Anda di repositori Plan ₿ Network. Ini adalah fork yang Anda buat di GitHub. URL fork Anda akan terlihat seperti ini: `https://github.com/[nama pengguna Anda]/konten-pendidikan-bitcoin`:

![TUTO](assets/fr/03.webp)

Pastikan Anda berada di cabang `dev` utama, lalu klik tombol `Sinkronisasi fork`. Jika fork Anda belum diperbarui, GitHub akan meminta Anda untuk memperbarui cabang Anda. Lanjutkan dengan pembaruan ini. Sebaliknya, jika cabang Anda sudah mutakhir, GitHub akan memberi tahu Anda:

![TUTO](assets/fr/04.webp)

Buka GitHub Desktop dan pastikan garpu Anda dipilih dengan benar di sudut kiri atas jendela:

![TUTO](assets/fr/05.webp)

Klik pada tombol `Mengambil asal`. Jika repositori lokal Anda sudah diperbarui, GitHub Desktop tidak akan menyarankan tindakan lebih lanjut. Jika tidak, opsi `Tarik asal` akan muncul. Klik tombol ini untuk memperbarui repositori lokal Anda:

![TUTO](assets/fr/06.webp)

Pastikan Anda berada di cabang utama `dev`:

![TUTO](assets/fr/07.webp)

Klik pada cabang ini, lalu klik tombol `Cabang Baru`:

![TUTO](assets/fr/08.webp)

Pastikan cabang baru didasarkan pada repositori sumber, yaitu `PlanB-Network/bitcoin-educational-content`.

Beri nama cabang Anda sehingga judulnya jelas tentang tujuannya, gunakan tanda hubung untuk memisahkan setiap kata. Sebagai contoh, katakanlah tujuan kita adalah menulis tutorial tentang cara menggunakan Sparrow Wallet. Dalam kasus ini, cabang kerja yang didedikasikan untuk menulis tutorial ini dapat diberi nama: `tuto-sparrow-wallet-loic`. Setelah Anda memasukkan nama yang sesuai, klik `Buat cabang` untuk mengonfirmasi pembuatan cabang:

![TUTO](assets/fr/09.webp)

Sekarang klik tombol `Publish branch` untuk menyimpan cabang kerja baru Anda pada fork online Anda di GitHub :

![TUTO](assets/fr/10.webp)

Sekarang, di GitHub Desktop, Anda seharusnya berada di cabang baru Anda. Ini berarti bahwa setiap perubahan yang Anda buat secara lokal di komputer Anda akan disimpan secara eksklusif di cabang khusus ini. Selain itu, selama cabang ini tetap dipilih di GitHub Desktop, file yang terlihat secara lokal di komputer Anda akan sesuai dengan file dari cabang ini (`tuto-sparrow-wallet-loic`), dan bukan dari cabang utama (`dev`).

![TUTO](assets/fr/11.webp)

Untuk setiap artikel baru yang ingin Anda publikasikan, Anda harus membuat cabang baru dari `dev`. Cabang di Git adalah versi paralel dari proyek, yang memungkinkan Anda untuk membuat perubahan tanpa memengaruhi cabang utama, hingga pekerjaan siap untuk digabungkan.

## 2 - Menambahkan file tutorial

Sekarang setelah cabang kerja telah dibuat, saatnya untuk mengintegrasikan tutorial baru Anda. Anda memiliki dua opsi: menggunakan skrip Python, yang mengotomatiskan pembuatan dokumen yang diperlukan, atau membuat setiap file secara manual. Mari kita lihat langkah-langkah yang harus diikuti untuk setiap opsi.

### Dengan skrip Python saya

Anda perlu menginstal :


- Python 3.8 atau lebih tinggi ;
- Ketergantungan yang diperlukan untuk skrip. Jalankan :

```bash
pip install customtkinter appdirs
````
Pour utiliser le script, rendez-vous dans le dossier où il est stocké. Le script se trouve dans le dépôt de data de Plan ₿ Network sous le chemin : `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.
Une fois dans le dossier, exécutez la commande :
```

python new-tutorial-creation.py

```
Une interface graphique (GUI) va s'ouvrir. La première fois, vous devrez entrer toutes les informations nécessaires, mais lors des utilisations ultérieures du script, vos informations personnelles seront mémorisées, ce qui vous évite de devoir les saisir de nouveau.
![TUTO](assets/fr/37.webp)
Commencez par indiquer le chemin local menant au dossier `/tutorials` sur votre clone du dépôt (`.../bitcoin-educational-content/tutorials/`). Vous pouvez le noter manuellement ou cliquer sur le bouton "Browse" pour naviguer via votre explorateur de fichiers.
![TUTO](assets/fr/38.webp)
Sélectionnez la langue dans laquelle vous rédigerez votre tutoriel.
![TUTO](assets/fr/39.webp)
Choisissez une catégorie principale pour votre tutoriel.
![TUTO](assets/fr/40.webp)
Ensuite, sélectionnez une sous-catégorie appropriée, en fonction de la catégorie principale que vous avez choisie.
![TUTO](assets/fr/41.webp)
Déterminez un niveau de difficulté pour le tutoriel.
![TUTO](assets/fr/42.webp)
Choisissez le nom du répertoire spécialement créé pour votre tutoriel. Le nom de ce dossier devrait refléter le logiciel abordé dans le tutoriel, en utilisant des tirets pour relier les mots. Par exemple, le dossier pourrait s'appeler `red-wallet` :
![TUTO](assets/fr/43.webp)
Le `project_id` est l'UUID de l'entreprise ou de l'organisation derrière l'outil présenté dans le tutoriel, disponible [dans la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, pour un tutoriel sur le logiciel Sparrow Wallet, vous trouverez ce `project_id` dans le fichier : `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Cette information est ajoutée au fichier YAML de votre tutoriel car Plan ₿ Network maintient une base de données des entreprises et organisations actives sur Bitcoin ou des projets connexes. En ajoutant le `project_id` associé à votre tutoriel, vous créez un lien entre votre contenu et l'entité concernée.
***Mise à jour :*** Dans la nouvelle version du script, vous n'avez plus besoin de saisir manuellement le `project_id`. Une fonction de recherche a été ajoutée pour trouver le projet par son nom et récupérer automatiquement le `project_id` correspondant. Tapez le début du nom du projet dans la case "Project name" pour le rechercher, puis sélectionnez l'entreprise souhaitée dans le menu déroulant. Le `project_id` sera automatiquement renseigné dans la case en dessous. Vous avez également la possibilité de le noter manuellement si nécessaire.
![TUTO](assets/fr/44.webp)
Pour les tags, sélectionnez 2 ou 3 mots-clés pertinents en relation avec le contenu de votre tutoriel, en les choisissant exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).
![TUTO](assets/fr/45.webp)
Dans la case "Contributor's GitHub ID", inscrivez votre identifiant GitHub.
![TUTO](assets/fr/46.webp)
Pour la case "PBN professor's ID", saisissez votre identifiant en utilisant les mots de la liste BIP39, tel qu'il apparaît sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).
![TUTO](assets/fr/47.webp)
Pour plus de détails sur votre identifiant de professeur, veuillez consulter le tutoriel suivant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Une fois toutes les informations saisies et vérifiées, cliquez sur "Create Tutorial" pour valider la création des fichiers de votre tutoriel. Cela générera en local le dossier de votre tutoriel et tous les fichiers nécessaires dans le dossier de la catégorie sélectionnée.
![TUTO](assets/fr/48.webp)
Vous pouvez maintenant passer outre la sous-partie "Sans mon script Python", ainsi que l'étape 3 "Remplir le fichier YAML", car le script a déjà effectué ces actions automatiquement pour vous. Passez directement à l'étape 4 et à la rédaction de votre tutoriel.
Pour plus d'informations sur ce script Python, vous pouvez également [consulter son README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).
### Sans mon script Python
Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`.
Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web Plan ₿ Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![TUTO](assets/fr/12.webp)
Au sein du dossier `wallet`, il faut créer un nouveau répertoire spécifiquement dédié à votre tutoriel. Le nom de ce dossier doit évoquer le logiciel traité dans le tutoriel, en veillant à relier les mots par des tirets. Pour mon exemple, le dossier sera intitulé `sparrow-wallet` :
![TUTO](assets/fr/13.webp)
Dans ce nouveau sous-dossier dédié à votre tutoriel, il faut ajouter plusieurs éléments :
- Créez un dossier `assets`, destiné à recevoir toutes les illustrations nécessaires à votre tutoriel ;
- Au sein de ce dossier `assets`, il faut créer un sous-dossier nommé selon le code de langue originale du tutoriel. Par exemple, si le tutoriel est rédigé en anglais, ce sous-dossier doit être nommé `en`. Placez-y tous les visuels du tutoriel (schémas, images, captures d’écran, etc.).
- Un fichier `tutorial.yml` doit être créé pour y consigner les détails relatifs à votre tutoriel ;
- Un fichier en format markdown est à créer pour y rédiger le contenu effectif de votre tutoriel. Ce fichier doit être intitulé selon le code de la langue de rédaction. Par exemple, pour un tutoriel rédigé en français, le fichier devra s'appeler `fr.md`.
![TUTO](assets/fr/14.webp)
Pour résumer, voici la hiérarchie des fichiers à créer :
```

bitcoin-konten-pendidikan/

└── tutorial/

└── dompet/ (ubah ke kategori yang benar)

└── dompet burung pipit/ (modifikasi dengan nama tuto)

├── aset/

│ ├── en/ (ubah ke kode bahasa yang sesuai)

├── tutorial.yml

└── fr.md (akan dimodifikasi sesuai dengan kode bahasa yang sesuai)

```
## 3 - Remplir le fichier YAML
Remplissez le fichier `tutorial.yml` en copiant le modèle suivant :
```

id:

project_id:

tag:

-

-

-

kategori:

tingkat:

kredit:

profesor:

# Mengoreksi metadata

bahasa_asli:

mengoreksi:


  - bahasa:

tanggal_kontribusi_terakhir:

urgensi:

kontributor_id:

-

hadiah:

````

Berikut ini adalah bidang yang wajib diisi:


- id**: Sebuah UUID (Pengenal Unik Universal) untuk mengidentifikasi tutorial secara unik. Anda dapat membuatnya dengan [alat bantu online] (https://www.uuidgenerator.net/version4). Satu-satunya batasan adalah UUID ini harus acak, agar tidak bertentangan dengan UUID lain di platform;
- project_id** : UUID dari perusahaan atau organisasi di balik alat yang disajikan dalam tutorial [dari daftar proyek] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Sebagai contoh, jika Anda sedang melakukan tutorial mengenai perangkat lunak Sparrow Wallet, Anda dapat menemukan `project_id` ini di file berikut: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Informasi ini ditambahkan dalam file YAML tutorial Anda karena Plan ₿ Network menyimpan database semua perusahaan dan organisasi yang beroperasi dengan Bitcoin atau proyek-proyek terkait. Dengan menambahkan `project_id` dari entitas yang ditautkan ke tutorial Anda, Anda membuat tautan antara dua elemen;
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
Berikut ini adalah contoh file `tutorial.yml` yang telah selesai dibuat untuk tutorial mengenai dompet Blockstream Green:

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
```

Setelah Anda selesai mengedit file `tutorial.yml`, simpan dokumen Anda dengan mengklik `File > Save`:

![TUTO](assets/fr/16.webp)

Anda sekarang dapat menutup editor kode Anda.

## 4 - Isi file Penurunan Harga

Sekarang Anda dapat membuka file tutorial Anda, yang diberi nama dengan kode bahasa Anda, misalnya `en.md`. Masuk ke Obsidian, di sisi kiri jendela, dan gulir ke bawah pada pohon folder ke folder tutorial Anda dan file yang diinginkan:

![TUTO](assets/fr/18.webp)

Klik pada file untuk membukanya:

![TUTO](assets/fr/19.webp)

Kita akan mulai dengan mengisi bagian `Properties` di bagian paling atas dokumen.

![TUTO](assets/fr/20.webp)

Tambahkan dan isi blok kode berikut secara manual:

```markdown
---
name: [Titre]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Isi nama tutorial Anda dan deskripsi singkat:

![TUTO](assets/fr/22.webp)

Kemudian, tambahkan jalur ke gambar sampul di awal tutorial Anda. Untuk melakukan ini, perhatikan :

```markdown
![cover-sparrow](assets/cover.webp)
```

Sintaks ini akan sangat berguna ketika Anda perlu menambahkan gambar ke dalam tutorial Anda. Tanda seru menunjukkan gambar, yang teks alternatifnya (alt) ditentukan di antara tanda kurung siku. Jalur ke gambar ditunjukkan di antara tanda kurung:

![TUTO](assets/fr/23.webp)

## 5 - Menambahkan logo dan sampul

Di dalam folder `assets`, Anda perlu menambahkan file bernama `logo.webp`, yang akan berfungsi sebagai gambar mini untuk artikel Anda. Gambar ini harus dalam format `.webp` dan berukuran persegi agar sesuai dengan antarmuka pengguna. Anda bebas memilih logo perangkat lunak yang tercakup dalam tutorial atau gambar lain yang relevan, selama gambar tersebut bebas royalti. Selain itu, tambahkan gambar berjudul `cover.webp` di tempat yang sama. Gambar ini akan ditampilkan di bagian atas tutorial Anda. Pastikan bahwa gambar ini, seperti halnya logo, menghormati hak-hak penggunaan dan sesuai dengan konteks tutorial Anda:

![TUTO](assets/fr/17.webp)

## 6 - Menulis tutorial dan menambahkan visual

Lanjutkan menulis konten tutorial Anda. Bila Anda ingin menyertakan subjudul, terapkan format penurunan nilai yang sesuai dengan mengawali teks dengan `##` :

![TUTO](assets/fr/24.webp)

Subfolder bahasa dalam folder `assets` digunakan untuk menyimpan diagram dan visual yang akan menyertai tutorial Anda. Sedapat mungkin, hindari menyertakan teks dalam gambar agar konten Anda dapat diakses oleh audiens internasional. Tentu saja, perangkat lunak yang disajikan akan berisi teks, tetapi jika Anda menambahkan skema atau indikasi tambahan pada tangkapan layar perangkat lunak, lakukan tanpa teks atau, jika perlu, gunakan bahasa Inggris.

![TUTO](assets/fr/25.webp)

Untuk menamai gambar Anda, cukup gunakan angka yang sesuai dengan urutan kemunculannya dalam tutorial, yang diformat sebagai dua digit (atau tiga digit jika tutorial Anda berisi lebih dari 99 gambar). Contohnya, beri nama gambar pertama Anda `01.webp`, gambar kedua `02.webp`, dan seterusnya.

Gambar Anda harus dalam format `.webp` saja. Jika perlu, Anda dapat menggunakan [perangkat lunak konversi gambar saya] (https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Untuk menyisipkan diagram dalam dokumen Anda, gunakan perintah berikut di Markdown, dengan hati-hati menentukan teks alternatif yang sesuai serta jalur gambar yang benar:

```markdown
![sparrow](assets/fr/01.webp)
```

Tanda seru di awal menunjukkan gambar. Teks alternatif, yang membantu aksesibilitas dan referensi, ditempatkan di antara tanda kurung siku. Terakhir, jalur ke gambar ditunjukkan di antara tanda kurung.

Jika Anda ingin membuat skema Anda sendiri, pastikan untuk mengikuti panduan grafis Plan ₿ Network (Rencana ₿ Jaringan) untuk memastikan konsistensi visual:


- Huruf **: Gunakan [Rubik] (https://fonts.google.com/specimen/Rubik);
- Warna**:
 - Oranye: #FF5C00
 - Hitam: #000000
 - Putih: #FFFFFF

**Sangat penting bahwa semua visual yang diintegrasikan ke dalam tutorial Anda bebas dari hak cipta atau menghormati lisensi file sumber**. Oleh karena itu, semua diagram yang dipublikasikan di Plan ₿ Network tersedia di bawah lisensi CC-BY-SA, dengan cara yang sama seperti teks.

**-> Tips:** Ketika berbagi file di tempat umum, seperti gambar, penting untuk menghapus metadata yang tidak perlu. Metadata ini dapat berisi informasi sensitif, seperti data lokasi, tanggal pembuatan, dan detail pembuat. Untuk melindungi privasi Anda, sebaiknya hapus metadata ini. Untuk menyederhanakan operasi ini, Anda dapat menggunakan alat khusus seperti [Exif Cleaner] (https://exifcleaner.com/), yang memungkinkan Anda untuk membersihkan metadata dokumen dengan hanya menarik dan melepas.

## 7 - Menyimpan dan mengusulkan tutorial

Setelah Anda selesai menulis tutorial Anda dalam bahasa pilihan Anda, langkah selanjutnya adalah mengirimkan **Pull Request**. Administrator kemudian akan menambahkan terjemahan yang kurang ke dalam tutorial Anda, menggunakan metode penerjemahan otomatis kami dengan pengoreksian oleh manusia.

Untuk melakukan Pull Request, buka GitHub Desktop. Perangkat lunak ini akan secara otomatis mendeteksi perubahan apa pun yang telah Anda lakukan secara lokal di cabang Anda ke repositori asli. Sebelum melanjutkan, periksa dengan cermat di sisi kiri antarmuka bahwa perubahan ini sesuai dengan yang Anda harapkan:

![TUTO](assets/fr/28.webp)

Tambahkan judul untuk komit Anda, lalu klik tombol biru `Komit ke [cabang Anda]` untuk memvalidasi perubahan ini:

![TUTO](assets/fr/29.webp)

Komit adalah catatan perubahan yang dibuat pada sebuah cabang, disertai dengan pesan deskriptif, yang memungkinkan Anda untuk melacak evolusi proyek dari waktu ke waktu. Ini adalah semacam pos pemeriksaan perantara.

Kemudian klik pada tombol `Push origin`. Ini akan mengirim komit Anda ke fork Anda:

![TUTO](assets/fr/30.webp)

Jika Anda belum menyelesaikan tutorial Anda, Anda dapat kembali lagi nanti dan membuat komit baru. Jika Anda sudah selesai mengedit cabang ini, klik tombol `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Anda dapat memeriksa untuk terakhir kalinya apakah perubahan Anda sudah benar, lalu klik tombol `Buat permintaan tarik`:

![TUTO](assets/fr/32.webp)

Pull Request adalah permintaan yang dibuat untuk mengintegrasikan perubahan dari cabang Anda ke dalam cabang utama repositori Plan ₿ Network, yang memungkinkan peninjauan dan diskusi perubahan sebelum digabungkan.

Anda akan secara otomatis dialihkan pada peramban Anda ke GitHub di halaman persiapan Pull Request Anda:

![TUTO](assets/fr/33.webp)

Masukkan sebuah judul yang secara singkat meringkas perubahan yang ingin Anda gabungkan dengan repositori sumber. Tambahkan komentar singkat yang menjelaskan perubahan-perubahan ini (jika Anda memiliki nomor isu yang terkait dengan pembuatan tutorial Anda, ingatlah untuk mencatat `Tutup #{nomor isu}` sebagai sebuah komentar), lalu klik tombol hijau `Buat permintaan tarik` untuk mengonfirmasi permintaan penggabungan:

![TUTO](assets/fr/34.webp)

PR Anda kemudian akan terlihat di tab `Tarik Permintaan` pada repositori Rencana ₿ Jaringan utama. Yang harus Anda lakukan sekarang adalah menunggu hingga administrator menghubungi Anda untuk mengonfirmasi bahwa kontribusi Anda telah digabungkan, atau meminta modifikasi lebih lanjut.

![TUTO](assets/fr/35.webp)

Setelah menggabungkan PR Anda dengan cabang utama, kami sarankan untuk menghapus cabang yang sedang bekerja (`tuto-sparrow-wallet`) untuk menjaga riwayat yang bersih di fork Anda. GitHub akan menawarkan opsi ini secara otomatis pada halaman PR Anda:

![TUTO](assets/fr/36.webp)

Di GitHub Desktop, Anda dapat kembali ke cabang utama fork Anda (`dev`).

![TUTO](assets/fr/07.webp)

Jika Anda ingin membuat perubahan pada kontribusi Anda setelah Anda mengirimkan PR Anda, langkah-langkah yang harus diikuti tergantung pada status PR Anda saat ini:


- Jika PR Anda masih terbuka dan belum digabungkan, lakukan perubahan secara lokal, tetap di cabang yang sama. Setelah perubahan selesai, gunakan tombol `Push origin` untuk menambahkan komit baru ke PR yang masih terbuka;
- Jika PR Anda telah digabungkan dengan cabang utama, Anda harus mengulang proses dari awal dengan membuat cabang baru, lalu mengirimkan PR baru. Pastikan repositori lokal Anda disinkronkan dengan repositori Plan ₿ Repositori sumber jaringan sebelum melanjutkan.

Jika Anda mengalami kesulitan teknis dalam mengirimkan tutorial Anda, jangan ragu untuk meminta bantuan di [grup Telegram khusus untuk kontribusi](https://t.me/PlanBNetwork_ContentBuilder). Terima kasih banyak!