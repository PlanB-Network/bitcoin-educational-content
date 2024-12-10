---
name: PlanB Professor
description: Bagaimana cara menambahkan profil profesor Anda di Jaringan PlanB?
---
![cover](assets/cover.webp)

Misi dari PlanB adalah untuk menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin, dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, yang memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform. Kontribusi dapat mengambil berbagai bentuk: mengoreksi dan memeriksa teks yang ada, memproduksi kursus pelatihan, menerjemahkan ke dalam bahasa lain, memperbarui informasi, atau membuat tutorial baru yang belum tersedia di situs kami.

Jika Anda ingin menambahkan tutorial lengkap baru atau kursus di Jaringan PlanB, Anda perlu membuat profil profesor Anda. Ini akan memungkinkan Anda untuk mendapatkan kredit yang tepat untuk konten yang Anda produksi di situs web.
![tutorial](assets/1.webp)
Jika Anda sebelumnya telah berkontribusi ke Jaringan PlanB, kemungkinan Anda sudah memiliki ID kontributor. Anda dapat menemukannya di folder profesor Anda yang dapat diakses [melalui halaman ini](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Jika ini kasusnya, Anda dapat melewatkan tutorial ini dan mulai berkontribusi langsung.
![tutorial](assets/2.webp)

Mari kita temukan bersama bagaimana menambahkan profesor baru dalam tutorial ini!

## Prasyarat

**Perangkat lunak yang diperlukan untuk mengikuti tutorial saya:**
- [GitHub Desktop](https://desktop.github.com/)
- Sebuah editor kode ([VSC](https://code.visualstudio.com/) atau [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Prasyarat sebelum memulai tutorial:**
- Memiliki [akun GitHub](https://github.com/signup).
- Memiliki fork dari [repositori sumber Jaringan PlanB](https://github.com/PlanB-Network/bitcoin-educational-content).

**Jika Anda membutuhkan bantuan untuk mendapatkan prasyarat ini, tutorial lain saya akan memandu Anda:**
- **[Memahami Git dan GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
- **[Membuat Akun GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[Menyiapkan Lingkungan Kerja Anda](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**

## Bagaimana cara membuat profil profesor baru?

- Buka browser Anda dan navigasikan ke halaman fork Anda dari repositori PlanB. URL fork Anda seharusnya terlihat seperti: `https://github.com/[username]/bitcoin-educational-content`
![tutorial](assets/4.webp)
- Pastikan Anda berada di cabang utama `dev` kemudian klik tombol `Sync fork`. Jika fork Anda tidak terbaru, GitHub akan menawarkan untuk memperbarui cabang Anda. Lanjutkan dengan sinkronisasi ini.

- Jika, di sisi lain, cabang Anda sudah terbaru, GitHub akan memberi tahu Anda:
![tutorial](assets/5.webp)- Buka GitHub Desktop dan pastikan fork Anda benar-benar dipilih di sudut kiri atas jendela:
![tutorial](assets/6.webp)
- Klik tombol `Fetch origin`.

- Jika repositori lokal Anda sudah terbaru, GitHub Desktop tidak akan menyarankan tindakan lebih lanjut. Jika tidak, opsi `Pull origin` akan muncul. Klik tombol ini untuk memperbarui repositori lokal Anda:
![tutorial](assets/7.webp)
- Pastikan Anda berada di cabang utama `dev`:
![tutorial](assets/8.webp)
- Klik pada cabang ini, kemudian klik tombol `New Branch`:
![tutorial](assets/9.webp)
- Pastikan cabang baru berbasis pada repositori sumber, yaitu `PlanB-Network/bitcoin-educational-content`.
- Beri nama cabang Anda dengan cara yang membuat judulnya jelas tentang tujuannya, gunakan tanda hubung untuk memisahkan setiap kata. Karena cabang ini dimaksudkan untuk menambahkan profil profesor, sebuah contoh nama bisa menjadi: `add-professor-[nama-anda]`. Setelah memasukkan nama, klik pada `Create branch` untuk mengonfirmasi pembuatannya:
![tutorial](assets/10.webp)
- Sekarang klik tombol `Publish branch` untuk menyimpan cabang kerja baru Anda ke fork online Anda di GitHub:
![tutorial](assets/11.webp)
- Pada titik ini, di GitHub Desktop, Anda seharusnya berada pada cabang baru Anda. Ini berarti bahwa semua modifikasi yang dibuat secara lokal di komputer Anda akan secara eksklusif dicatat pada cabang spesifik ini. Juga, selama cabang ini tetap dipilih di GitHub Desktop, file yang terlihat secara lokal di mesin Anda sesuai dengan file dari cabang ini (`add-professor-nama-anda`), dan bukan file dari cabang utama (`dev`):
![tutorial](assets/12.webp)
- Untuk menambahkan profil profesor Anda, buka penjelajah file Anda dan navigasikan ke repositori lokal Anda, di folder `professors`. Anda akan menemukannya di bawah jalur: `\GitHub\bitcoin-educational-content\professors`.

- Di dalam folder ini, buat folder baru yang dinamai dengan nama atau pseudonim Anda. Pastikan tidak ada spasi dalam nama folder. Jadi, jika nama Anda adalah "Loic Pandul" dan tidak ada profesor lain yang memiliki nama ini, folder yang akan dibuat bernama `loic-pandul`:
![tutorial](assets/13.webp)
- Untuk memudahkan, Anda sudah bisa menyalin dan menempelkan semua dokumen dari profesor lain ke dalam folder Anda sendiri. Kami kemudian akan melanjutkan untuk memodifikasi dokumen-dokumen ini agar disesuaikan dengan profil Anda:
![tutorial](assets/14.webp)
- Mulailah dengan menavigasi ke folder `assets`. Hapus gambar profil profesor yang sebelumnya Anda salin, dan gantilah dengan gambar profil Anda sendiri. Sangat penting bahwa gambar ini dalam format `.webp` dan dinamai `profile`, sehingga memberikan nama file lengkap `profile.webp`. Sadarilah, gambar ini akan dipublikasikan di Internet dan dapat diakses oleh semua orang: ![tutorial](assets/15.webp)
- Selanjutnya, buka file `professor.yml` dengan editor kode Anda (VSC atau Sublime Text, misalnya). Anda akan sampai pada file yang disalin dari profesor yang ada:
![tutorial](assets/16.webp)
- Anda kemudian harus memperbarui informasi yang ada dengan milik Anda sendiri:
	- **name:** tuliskan nama atau pseudonim Anda;
	- **links:** tunjukkan akun Anda di jejaring sosial seperti Twitter dan Nostr, serta URL dari situs web pribadi Anda (opsional);
	- **affiliation:** sebutkan nama perusahaan yang mempekerjakan Anda (opsional);
	- **tags:** tentukan area spesialisasi Anda dari daftar berikut, dengan mengetahui bahwa Anda dapat menambahkan tema Anda sendiri. Namun, pastikan untuk membatasi jumlah tag menjadi maksimal 4 untuk memastikan UI yang baik:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** berikan alamat Lightning Anda untuk donasi agar pembaca tutorial masa depan Anda dapat mengirimkan beberapa sats kepada Anda (opsional);
	- **company:** jika Anda memiliki satu, tunjukkan nama perusahaan Anda (opsional). Anda kemudian harus memperbarui informasi yang ada dengan milik Anda sendiri:
![tutorial](assets/17.webp)- Anda juga harus memodifikasi `contributor-id`. Pengenal ini digunakan untuk mengenali Anda di situs web, tetapi tidak dipublikasikan di luar GitHub. Anda bebas memilih kombinasi dua kata, merujuk ke [daftar bahasa Inggris dari 2048 kata dari BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Jangan lupa untuk memasukkan tanda hubung antara dua kata yang dipilih. Sebagai contoh, di sini, saya memilih `crazy-cactus`:
![tutorial](assets/18.webp)
- Setelah Anda selesai memodifikasi dokumen `professor.yml`, klik pada `File > Save` untuk menyimpan file Anda. Anda kemudian dapat keluar dari editor kode Anda:
![tutorial](assets/19.webp)
- Di dalam folder professor Anda, Anda dapat menghapus dokumen yang ditulis dalam bahasa yang tidak berkaitan dengan Anda, yang awalnya disalin dari professor lain. Pertahankan hanya file yang sesuai dengan bahasa ibu Anda. Sebagai contoh, dalam kasus saya, saya hanya menyimpan file `fr.yml`, karena bahasa saya adalah Prancis: ![tutorial](assets/20.webp)
- Klik dua kali pada file ini untuk membukanya dengan editor kode Anda.

- Di dalam file ini, Anda memiliki kesempatan untuk menulis biografi lengkap Anda di bawah bagian `bio` dan ringkasan atau judul singkat di bawah `short_bio`:
![tutorial](assets/21.webp)
- Setelah menyimpan dokumen `fr.yml` Anda, Anda perlu membuat salinan dari file ini untuk masing-masing delapan bahasa berikut:
    - Jerman (DE);
    - Inggris (EN);
    - Prancis (FR);
    - Spanyol (ES);
    - Italia (IT);
    - Portugis (PT);
    - Jepang (JA);
    - Vietnam (VI).

- Lanjutkan untuk menyalin dan menempel file asli Anda, kemudian terjemahkan setiap dokumen ke dalam bahasa yang sesuai. Jika Anda mahir dalam bahasa tersebut, Anda dapat melakukan terjemahan secara manual. Jika tidak, jangan ragu untuk menggunakan alat terjemahan otomatis atau chatbot:
![tutorial](assets/22.webp)
- Jika Anda mau, juga dimungkinkan untuk hanya menyimpan biografi dalam bahasa ibu Anda; kami kemudian akan menangani terjemahan setelah pengajuan Pull Request Anda.

- Folder professor Anda seharusnya terlihat seperti ini:
![tutorial](assets/23.webp)
```plaintext
first-name-last-name/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Sekarang kembali ke GitHub Desktop.
- Di sisi kiri jendela Anda, Anda seharusnya dapat melihat semua modifikasi yang dibuat pada dokumen, spesifik untuk cabang Anda. Pastikan modifikasi-modifikasi ini benar:
![tutorial](assets/24.webp)
- Jika modifikasi tampak benar bagi Anda, tambahkan judul untuk commit Anda. Commit adalah penyimpanan dari modifikasi yang dibuat pada cabang, disertai dengan pesan deskriptif, yang memungkinkan untuk mengikuti evolusi proyek dari waktu ke waktu.
- Setelah judul dimasukkan, tekan tombol biru `Commit to [cabang Anda]` untuk memvalidasi modifikasi ini:
![tutorial](assets/25.webp)
- Kemudian klik pada tombol `Push origin`. Ini akan mengirim commit Anda ke fork Anda:
![tutorial](assets/26.webp)
- Jika Anda telah menyelesaikan modifikasi untuk cabang ini, klik sekarang pada tombol `Preview Pull Request`:
![tutorial](assets/27.webp)
- Anda dapat memeriksa satu kali lagi bahwa modifikasi Anda sudah benar, kemudian klik tombol `Create pull request`: ![tutorial](assets/28.webp) - Anda akan secara otomatis dialihkan ke browser Anda di GitHub ke halaman persiapan Pull Request. Pull Request adalah permintaan yang dibuat untuk mengintegrasikan perubahan dari cabang Anda ke cabang utama dari repositori PlanB Network, yang memungkinkan untuk tinjauan dan diskusi perubahan sebelum penggabungannya: ![tutorial](assets/29.webp)
- Di halaman persiapan ini, tentukan judul yang secara singkat merangkum modifikasi yang ingin Anda gabungkan dengan repositori sumber.
- Tambahkan komentar singkat yang mendeskripsikan perubahan tersebut.
- Setelah menyelesaikan langkah-langkah ini, klik tombol hijau `Create pull request` untuk mengonfirmasi permintaan penggabungan: ![tutorial](assets/30.webp)
- PR Anda kemudian akan terlihat di tab `Pull Request` dari repositori utama PlanB Network. Yang harus Anda lakukan sekarang adalah menunggu sampai seorang administrator menghubungi Anda untuk mengonfirmasi penggabungan kontribusi Anda atau untuk meminta modifikasi tambahan: ![tutorial](assets/31.webp)
- Setelah penggabungan PR Anda dengan cabang utama, disarankan untuk menghapus cabang kerja Anda (`add-professor-your-name`) untuk menjaga sejarah yang bersih di fork Anda. GitHub akan secara otomatis menawarkan Anda opsi ini di halaman PR Anda: ![tutorial](assets/32.webp)
- Di perangkat lunak GitHub Desktop, Anda dapat beralih kembali ke cabang utama dari fork Anda (`dev`): ![tutorial](assets/8.webp)
- Jika Anda ingin melakukan modifikasi pada profil Anda setelah sudah mengirimkan PR Anda, prosedurnya tergantung pada status saat ini dari PR Anda:
	- Jika PR Anda masih terbuka dan belum digabungkan, lakukan modifikasi secara lokal sambil tetap berada di cabang yang sama. Setelah modifikasi selesai, gunakan tombol `Push origin` untuk menambahkan commit baru ke PR Anda yang masih terbuka;
	- Dalam kasus di mana PR Anda sudah digabungkan dengan cabang utama, Anda perlu memulai proses dari awal dengan membuat cabang baru, kemudian mengirimkan PR baru. Pastikan repositori lokal Anda disinkronkan dengan repositori sumber PlanB Network sebelum melanjutkan.
