---
name: Kontribusi - Tutorial
description: Bagaimana cara mengusulkan tutorial baru di Jaringan PlanB?
---
![cover](assets/cover.webp)

Misi dari PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin, dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, yang menawarkan kesempatan bagi siapa saja untuk berpartisipasi dalam memperkaya platform. Kontribusi dapat mengambil berbagai bentuk: mengoreksi dan memeriksa teks yang ada, menerjemahkan ke dalam bahasa lain, memperbarui informasi, atau membuat tutorial baru yang belum tersedia di situs kami.

Dalam tutorial ini, saya akan menjelaskan cara memodifikasi bagian "Tutorial" dari Jaringan PlanB. Jika Anda ingin menambahkan tutorial baru atau memperbaiki yang sudah ada, artikel ini untuk Anda! Kami akan melihat secara detail bagaimana berkontribusi ke Jaringan PlanB melalui GitHub, sambil menggunakan Obsidian, alat penulisan.

## Prasyarat

Untuk berkontribusi ke Jaringan PlanB, Anda memiliki 3 opsi tergantung pada tingkat pengalaman Anda dengan GitHub:
1. **Pengguna berpengalaman**: Lanjutkan dengan metode biasa Anda dan konsultasikan tutorial ini untuk memahami struktur repositori PlanB, persyaratan khusus, dan alur kerja.
2. **Pemula yang siap belajar**: Saya merekomendasikan untuk menyiapkan lingkungan kerja Anda sendiri. Ikuti tutorial ini serta artikel lain kami yang tercantum di bawah untuk membimbing Anda langkah demi langkah.
3. **Pemula untuk kontribusi kecil**: Untuk tugas yang memerlukan modifikasi lebih sedikit, seperti proofreading atau koreksi, gunakan antarmuka web GitHub langsung tanpa menyiapkan lingkungan lokal yang lengkap.

**Perangkat lunak yang diperlukan untuk mengikuti tutorial saya:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Sebuah editor kode ([VSC](https://code.visualstudio.com/) atau [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Prasyarat sebelum memulai tutorial:**
- Memiliki [akun GitHub](https://github.com/signup).
- Memiliki fork dari [repositori sumber Jaringan PlanB](https://github.com/PlanB-Network/bitcoin-educational-content).
- Memiliki [profil profesor di Jaringan PlanB](https://planb.network/professors) (hanya jika Anda mengusulkan tutorial lengkap).

**Jika Anda memerlukan bantuan untuk mendapatkan prasyarat ini, tutorial lain saya akan membimbing Anda:**
- **[Memahami Git dan GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
- **[Membuat akun GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[Menyiapkan lingkungan kerja Anda](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
- **[Membuat profil profesor](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Jenis konten apa yang ditulis di Jaringan PlanB?
Kami terutama mencari tutorial tentang alat yang terkait dengan Bitcoin atau ekosistemnya. Konten ini dapat diorganisir sekitar enam kategori utama:
- Wallet;
- Node;
- Mining;
- Merchant;
- Exchange;
- Privacy.
![tutorial](assets/2.webp)
Di luar topik khusus yang terkait dengan Bitcoin, PlanB juga mencari kontribusi pada tema yang menyoroti kedaulatan individu, seperti:
- Alat open source;
- Komputasi;
- Kriptografi;
- Energi;
- Matematika;
- Ekonomi;
- DIYs;
- LifeHacking...
Sebagai contoh, saat ini kami memiliki tutorial tentang Tails, Nostr, atau GrapheneOS. Alat-alat ini tidak langsung terkait dengan Bitcoin, tetapi mereka adalah sistem yang dapat menarik minat kami dalam proses kedaulatan di dunia digital. Konten-konten ini dapat diintegrasikan ke dalam sub-kategori dari bagian "Lainnya".

Anda memiliki pilihan antara merancang tutorial dari awal atau mengambil tutorial yang sebelumnya dipublikasikan di situs web Anda (dengan syarat Anda memiliki hak cipta) untuk juga dibagikan di Jaringan PlanB, dengan menambahkan tautan ke artikel asli.

Apa pun pilihan Anda, ingatlah bahwa semua konten yang dipublikasikan di Jaringan PlanB berada di bawah lisensi bebas [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Lisensi ini memungkinkan siapa saja untuk menyalin dan, berpotensi, untuk memodifikasi konten Anda, asalkan sumber asli diberikan kredit yang semestinya.

## Bagaimana cara mengusulkan tutorial di Jaringan PlanB?

Setelah semuanya siap, dan lingkungan lokal Anda sudah diatur dengan baik dengan fork Anda sendiri dari Jaringan PlanB, Anda dapat mulai menambahkan tutorial.

### Membuat cabang baru

- Buka browser Anda dan arahkan ke halaman fork Anda dari repositori PlanB. Ini adalah fork yang telah Anda buat di GitHub. URL fork Anda seharusnya terlihat seperti: `https://github.com/[nama-pengguna-anda]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Pastikan Anda berada di cabang utama `dev` kemudian klik tombol `Sync fork`. Jika fork Anda tidak terbaru, GitHub akan menawarkan untuk memperbarui cabang Anda. Lanjutkan dengan pembaruan ini. Jika, sebaliknya, cabang Anda sudah terbaru, GitHub akan memberi tahu Anda:
![tutorial](assets/4.webp)
- Buka perangkat lunak GitHub Desktop dan pastikan fork Anda benar-benar dipilih di sudut kiri atas jendela:
![tutorial](assets/5.webp)
- Klik tombol `Fetch origin`. Jika repositori lokal Anda sudah terbaru, GitHub Desktop tidak akan menyarankan tindakan lebih lanjut. Jika tidak, opsi `Pull origin` akan muncul. Klik tombol ini untuk memperbarui repositori lokal Anda: ![tutorial](assets/6.webp)
- Pastikan Anda berada di cabang utama `dev`:
![tutorial](assets/7.webp)
- Klik pada cabang ini, kemudian klik tombol `New Branch`:
![tutorial](assets/8.webp)
- Pastikan cabang baru didasarkan pada repositori sumber, yaitu `PlanB-Network/bitcoin-educational-content`.
- Beri nama cabang Anda dengan cara yang jelas tentang tujuannya, menggunakan tanda hubung untuk memisahkan setiap kata. Misalnya, katakanlah tujuan kami adalah menulis tutorial tentang penggunaan perangkat lunak Sparrow Wallet. Dalam kasus ini, cabang kerja yang didedikasikan untuk menulis tutorial ini bisa dinamai: `tuto-sparrow-wallet-loic`. Setelah nama yang sesuai dimasukkan, klik `Create branch` untuk mengonfirmasi pembuatan cabang:
![tutorial](assets/9.webp)
- Sekarang klik tombol `Publish branch` untuk menyimpan cabang kerja baru Anda di fork online Anda di GitHub:
![tutorial](assets/10.webp)
Sekarang, di GitHub Desktop, Anda seharusnya berada di cabang baru Anda. Ini berarti bahwa semua perubahan yang dilakukan secara lokal di komputer Anda akan dicatat secara eksklusif pada cabang spesifik ini. Juga, selama cabang ini tetap dipilih di GitHub Desktop, file yang terlihat secara lokal di mesin Anda sesuai dengan file dari cabang ini (`tuto-sparrow-wallet-loic`), dan bukan dari cabang utama (`dev`).
![tutorial](assets/11.webp)
Untuk setiap artikel baru yang ingin Anda terbitkan, Anda perlu membuat cabang baru dari `dev`. Cabang dalam Git adalah versi paralel dari proyek, yang memungkinkan Anda untuk melakukan perubahan tanpa mempengaruhi cabang utama, sampai pekerjaan siap untuk digabungkan.
### Menambahkan tutorial

Sekarang cabang kerja telah dibuat, saatnya untuk mengintegrasikan tutorial baru Anda.
- Buka manajer file Anda dan navigasikan ke folder `bitcoin-educational-content`, yang mewakili klon lokal dari repositori Anda. Anda seharusnya biasanya menemukannya di bawah `Documents\GitHub\bitcoin-educational-content`. Di dalam direktori ini, akan diperlukan untuk menemukan sub-folder yang tepat untuk menempatkan tutorial Anda. Organisasi folder mencerminkan bagian yang berbeda dari situs web Jaringan PlanB. Dalam contoh kita, karena kami ingin menambahkan tutorial tentang Sparrow Wallet, maka tepat untuk pergi ke jalur berikut: `bitcoin-educational-content\tutorials\wallet` yang sesuai dengan bagian `WALLET` di situs web: ![tutorial](assets/12.webp)
- Di dalam folder `wallet`, Anda perlu membuat direktori baru khusus untuk tutorial Anda. Nama folder ini harus menggambarkan perangkat lunak yang dibahas dalam tutorial, dengan menghubungkan kata-kata dengan tanda hubung. Untuk contoh saya, folder akan berjudul `sparrow-wallet`:
![tutorial](assets/13.webp)
- Di dalam sub-folder baru ini yang didedikasikan untuk tutorial Anda, beberapa elemen perlu ditambahkan:
	- Buat folder `assets`, yang dimaksudkan untuk menerima semua ilustrasi yang diperlukan untuk tutorial Anda;
    - Di dalam folder `assets` ini, Anda perlu membuat 8 sub-folder bernama `fr`, `de`, `en`, `it`, `es`, `ja`, `vi`, dan `pt`, untuk mengklasifikasikan visual sesuai dengan bahasa yang sesuai. Anda juga harus menambahkan sub-folder `notext` untuk visual yang tidak memerlukan terjemahan, seperti tangkapan layar misalnya;
	- File `tutorial.yml` harus dibuat untuk mencatat detail yang berkaitan dengan tutorial Anda;
	- File format markdown harus dibuat untuk menulis konten sebenarnya dari tutorial Anda. File ini harus diberi judul sesuai dengan kode bahasa penulisan. Misalnya, untuk tutorial yang ditulis dalam bahasa Prancis, file tersebut harus disebut `fr.md`.
![tutorial](assets/14.webp)
- Untuk merangkum, berikut adalah hierarki file yang harus dibuat:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (untuk dimodifikasi dengan kategori yang tepat)
        └── sparrow-wallet/ (untuk dimodifikasi dengan nama tutorial)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (untuk dimodifikasi sesuai dengan kode bahasa yang tepat)
```

- Untuk memulai, buka file `tutorial.yml` Anda menggunakan editor kode Anda.
- Isi setiap bidang dengan informasi yang ditentukan di bawah ini:
- **builder**: Masukkan nama perusahaan yang memproduksi perangkat lunak yang Anda buat tutorialnya;
- **tags**: Tentukan serangkaian kata kunci yang erat kaitannya dengan topik artikel Anda, untuk memfasilitasi pencarian dan pengindeksannya;
- **kategori**: Pilih sub-kategori yang sesuai di antara yang tersedia di situs PlanB, berdasarkan isi dari tutorial Anda. Misalnya, untuk tutorial di bagian `WALLET`, opsi yang tersedia adalah `Desktop`, `Hardware`, dan `Mobile`;
- **level**: Indikasikan tingkat kesulitan dari tutorial Anda dengan memilih salah satu dari empat kategori berikut:
    - Pemula (`beginner`),
    - Menengah (`intermediary`),
    - Lanjutan (`advanced`),
    - Ahli (`expert`).
- **professor**: Sertakan ID kontributor Anda sebagaimana muncul di profil professor Anda. Untuk detail lebih lanjut, rujuk ke [tutorial yang sesuai](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (opsional): Jika Anda ingin memberikan kredit ke situs web sumber untuk tutorial yang Anda kembangkan, seperti situs pribadi Anda sendiri, ini adalah tempat Anda dapat menambahkan link yang bersangkutan.
![tutorial](assets/15.webp)
- Setelah Anda selesai memodifikasi file `tutorial.yml` Anda, simpan dokumen Anda dengan mengklik `File > Save`:
![tutorial](assets/16.webp)
- Anda sekarang dapat menutup editor kode Anda.
- Di folder `assets`, Anda harus menambahkan file bernama `logo.webp`, yang akan berfungsi sebagai thumbnail untuk artikel Anda. Gambar ini harus dalam format `.webp` dan harus menghormati dimensi persegi untuk harmonisasi dengan antarmuka pengguna. Anda bebas memilih logo dari perangkat lunak yang dibahas dalam tutorial atau gambar relevan lainnya, asalkan bebas dari hak cipta. Selain itu, tambahkan juga gambar berjudul `cover.webp` di lokasi yang sama. Gambar ini akan ditampilkan di bagian atas tutorial Anda. Pastikan gambar ini, seperti logo, menghormati hak penggunaan dan cocok untuk konteks tutorial Anda:
![tutorial](assets/17.webp)
- Sekarang, Anda dapat membuka file yang akan menjadi host tutorial Anda, dinamai dengan kode bahasa Anda, seperti `fr.md`. Pergi ke Obsidian, di sisi kiri jendela, gulir melalui pohon folder ke folder tutorial Anda dan ke file yang dicari:
![tutorial](assets/18.webp)
- Klik pada file untuk membukanya:
![tutorial](assets/19.webp)
- Kami akan mulai dengan mengisi bagian `Properties` di bagian atas dokumen. Jika bagian ini hilang dari file Anda (jika dokumen sepenuhnya kosong), Anda dapat mereproduksinya dengan menyalinnya dari tutorial lain yang sudah ada: ![tutorial](assets/20.webp)
- Anda juga dapat menambahkannya secara manual dengan cara ini menggunakan editor kode Anda:
```markdown
---
name: [Judul]
description: [Deskripsi]
---
```
![tutorial](assets/21.webp)
- Isi nama tutorial Anda dan deskripsi singkat dari itu:
![tutorial](assets/22.webp)
- Kemudian tambahkan gambar sampul Anda di awal tutorial. Untuk melakukan ini, ketik:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Sintaks ini akan berguna kapanpun menambahkan gambar ke tutorial Anda diperlukan. Tanda seru menunjukkan bahwa ini adalah gambar, dengan teks alternatif (alt) yang ditentukan di antara kurung. Jalur ke gambar diindikasikan di antara tanda kurung:
![tutorial](assets/23.webp)
- Lanjutkan menulis tutorial Anda dengan menulis konten Anda. Ketika Anda ingin mengintegrasikan subjudul, terapkan pemformatan markdown yang sesuai dengan menambahkan prefix teks dengan `##`:
![tutorial](assets/24.webp)

### Bagaimana cara menambahkan diagram ke tutorial?
Subfolder bahasa dalam folder `assets` dimaksudkan untuk mengorganisir diagram dan visual yang akan menemani tutorial Anda. Jika gambar Anda mencakup teks, pastikan untuk menerjemahkannya untuk setiap bahasa yang bersangkutan agar konten Anda dapat diakses oleh audiens internasional. Untuk diagram tanpa teks untuk diterjemahkan atau tangkapan layar, letakkan langsung di subfolder `notext`. ![tutorial](assets/25.webp)
Untuk menamai gambar Anda, cukup letakkan nomor sesuai urutan kemunculan dalam tutorial. Sebagai contoh, namai gambar pertama Anda `1.webp`, kedua `2.webp`, dan seterusnya.

Jika diagram yang sama diterjemahkan ke dalam beberapa bahasa, pertahankan nama file yang sama untuk terjemahan yang berbeda di subfolder bahasa, seperti `en/1.webp`, `fr/1.webp`, `pt/1.webp`, dll.

Anda memiliki opsi untuk menggunakan format gambar yang berbeda seperti `jpeg`, `png`, atau `webp`. Disarankan untuk memilih format `webp` agar gambar tidak terlalu berat. ![tutorial](assets/26.webp)
Untuk memasukkan diagram ke dalam dokumen Anda, gunakan perintah berikut dalam Markdown, pastikan untuk menentukan teks alternatif yang sesuai dan jalur gambar yang benar:
```markdown
![sparrow](assets/notext/1.webp)
```
Tanda seru di awal menunjukkan bahwa itu adalah gambar. Teks alternatif, yang membantu dalam aksesibilitas dan SEO, ditempatkan di antara kurung siku. Akhirnya, jalur ke gambar ditunjukkan di antara tanda kurung: ![tutorial](assets/27.webp)
Jika Anda ingin membuat diagram sendiri, pastikan untuk mengikuti piagam grafis dari PlanB Network untuk memastikan konsistensi visual:
- **Font**: Gunakan [Rubik](https://fonts.google.com/specimen/Rubik);
- **Warna**:
	- Oranye: #FF5C00
	- Hitam: #000000
	- Putih: #FFFFFF

**Sangat penting bahwa semua visual yang diintegrasikan ke dalam tutorial Anda bebas royalti atau mematuhi lisensi file sumber**. Selain itu, semua diagram yang diterbitkan di PlanB Network tersedia di bawah lisensi CC-BY-SA, sama seperti teks.

**-> Tip:** Saat berbagi file secara publik, seperti gambar, penting untuk menghapus metadata yang tidak perlu. Ini bisa berisi informasi sensitif, seperti data lokasi, tanggal pembuatan, atau detail tentang penulis. Untuk melindungi privasi Anda, disarankan untuk menghapus metadata ini. Untuk menyederhanakan operasi ini, Anda dapat menggunakan alat khusus seperti [Exif Cleaner](https://exifcleaner.com/), yang menawarkan kemampuan untuk membersihkan metadata dokumen dengan drag-and-drop yang sederhana.

### Bagaimana cara menyimpan dan mengunggah tutorial?

Setelah Anda selesai menulis tutorial Anda dalam bahasa pilihan Anda, langkah selanjutnya adalah mengirimkan **Pull Request**. Administrator kemudian akan menambahkan terjemahan yang hilang dari tutorial Anda, berkat metode terjemahan otomatis kami.

- Untuk melanjutkan dengan Pull Request, buka perangkat lunak GitHub Desktop.
- Perangkat lunak tersebut seharusnya secara otomatis mendeteksi perubahan yang telah Anda buat secara lokal dibandingkan dengan repositori asli. Sebelum melanjutkan, periksa dengan cermat di sisi kiri antarmuka bahwa perubahan ini persis sesuai dengan yang Anda harapkan: ![tutorial](assets/28.webp)
- Tambahkan judul untuk commit Anda, kemudian klik tombol biru `Commit to [cabang Anda]` untuk memvalidasi perubahan ini: ![tutorial](assets/29.webp)
Commit adalah penyimpanan dari perubahan yang dibuat ke cabang, disertai dengan pesan deskriptif, yang memungkinkan untuk mengikuti evolusi proyek dari waktu ke waktu. Ini merupakan semacam titik pemeriksaan sementara.
- Kemudian klik tombol `Push origin`. Ini akan mengirimkan commit Anda ke fork Anda: ![tutorial](assets/30.webp)- Jika Anda belum menyelesaikan tutorial Anda, Anda dapat kembali ke tutorial tersebut nanti dan membuat commit baru.
- Jika Anda telah menyelesaikan pengeditan untuk cabang ini, sekarang klik tombol `Preview Pull Request`: ![tutorial](assets/31.webp)
- Anda dapat memeriksa satu kali lagi bahwa modifikasi Anda sudah benar, kemudian klik tombol `Create pull request`:
![tutorial](assets/32.webp)
Pull Request adalah permintaan yang dibuat untuk mengintegrasikan perubahan dari cabang Anda ke cabang utama dari repositori PlanB Network, yang memungkinkan untuk tinjauan dan diskusi perubahan sebelum penggabungannya.

- Anda akan secara otomatis dialihkan di browser Anda ke GitHub pada halaman persiapan Pull Request Anda:
![tutorial](assets/33.webp)
- Berikan judul yang secara singkat merangkum modifikasi yang ingin Anda gabungkan dengan repositori sumber.
- Tambahkan komentar singkat yang menggambarkan perubahan tersebut.
- Klik tombol hijau `Create pull request` untuk mengonfirmasi permintaan penggabungan:
![tutorial](assets/34.webp)
PR Anda kemudian akan terlihat di tab `Pull Request` dari repositori utama PlanB Network. Yang harus Anda lakukan sekarang adalah menunggu sampai seorang administrator menghubungi Anda untuk mengonfirmasi penggabungan kontribusi Anda atau untuk meminta modifikasi tambahan.
![tutorial](assets/35.webp)
Setelah penggabungan PR Anda dengan cabang utama, disarankan untuk menghapus cabang kerja Anda (`tuto-sparrow-wallet`) untuk menjaga sejarah yang bersih pada fork Anda. GitHub akan secara otomatis menawarkan Anda opsi ini pada halaman PR Anda:
![tutorial](assets/36.webp)
Pada perangkat lunak GitHub Desktop, Anda dapat beralih kembali ke cabang utama dari fork Anda (`dev`).
![tutorial](assets/7.webp)
Jika Anda ingin melakukan modifikasi pada kontribusi Anda setelah sudah mengirimkan PR Anda, prosedur yang harus diikuti tergantung pada status saat ini dari PR Anda:
- Jika PR Anda masih terbuka dan belum digabungkan, lakukan modifikasi secara lokal sambil tetap berada di cabang yang sama. Setelah modifikasi selesai, gunakan tombol `Push origin` untuk menambahkan commit baru ke PR Anda yang masih terbuka;
- Dalam kasus di mana PR Anda sudah digabungkan dengan cabang utama, Anda perlu melakukan proses dari awal dengan membuat cabang baru, kemudian mengirimkan PR baru. Pastikan repositori lokal Anda disinkronkan dengan repositori sumber PlanB Network sebelum melanjutkan.
