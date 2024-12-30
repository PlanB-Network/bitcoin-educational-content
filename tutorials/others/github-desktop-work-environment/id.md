---
name: GitHub Desktop
description: Bagaimana cara menyiapkan lingkungan kerja lokal Anda?
---
![github](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, yang memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform. Kontribusi dapat mengambil berbagai bentuk: mengoreksi dan memeriksa teks yang ada, menerjemahkan ke dalam bahasa lain, memperbarui informasi, atau membuat tutorial baru yang belum tersedia di situs kami.

Jika Anda ingin berkontribusi ke Jaringan PlanB, Anda perlu menggunakan GitHub untuk mengusulkan perubahan. Untuk melakukan ini, Anda memiliki dua pilihan:
- **Berkontribusi langsung melalui antarmuka web GitHub**: Ini adalah metode paling sederhana. Jika Anda pemula atau jika Anda berencana untuk membuat hanya beberapa kontribusi kecil, opsi ini mungkin yang terbaik untuk Anda;
- **Berkontribusi secara lokal menggunakan Git**: Metode ini lebih cocok jika Anda berencana untuk membuat kontribusi reguler atau signifikan ke Jaringan PlanB. Meskipun menyiapkan lingkungan Git lokal Anda di komputer mungkin tampak kompleks pada awalnya, pendekatan ini lebih efisien dalam jangka panjang. Ini memungkinkan pengelolaan perubahan yang lebih fleksibel. Jika Anda baru dalam hal ini, jangan khawatir, **kami menjelaskan seluruh proses penyiapan lingkungan Anda dalam tutorial ini** (janji, Anda tidak perlu mengetik baris perintah apa pun ^^).

Jika Anda tidak tahu apa itu GitHub, atau jika Anda ingin mempelajari lebih lanjut tentang istilah teknis terkait Git dan GitHub, saya sarankan Anda [membaca artikel pengantar kami untuk membiasakan diri dengan konsep-konsep ini](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb).

- Untuk memulai, Anda tentu saja memerlukan akun GitHub. Jika Anda sudah memiliki satu, Anda dapat masuk, jika tidak, Anda dapat menggunakan [tutorial kami untuk membuat yang baru](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).

## Langkah 1: Instal GitHub Desktop

- Kunjungi https://desktop.github.com/ untuk mengunduh perangkat lunak GitHub Desktop. Perangkat lunak ini memungkinkan Anda untuk berinteraksi dengan mudah dengan GitHub, tanpa harus menggunakan terminal:
![github-desktop](assets/1.webp)
- Ketika Anda pertama kali meluncurkan perangkat lunak, Anda akan diminta untuk menghubungkan akun GitHub Anda. Untuk melakukan ini, klik pada `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- Sebuah halaman otentikasi akan terbuka di browser Anda. Masukkan alamat email dan kata sandi yang dipilih saat membuat akun Anda, kemudian klik pada tombol `Sign in`:
![github-desktop](assets/3.webp)
- Klik pada `Authorize desktop` untuk mengonfirmasi koneksi antara akun Anda dan perangkat lunak:
![github-desktop](assets/4.webp)
- Anda akan secara otomatis dialihkan ke perangkat lunak GitHub Desktop. Klik pada `Finish`: ![github-desktop](assets/5.webp)
- Jika Anda baru saja membuat akun GitHub Anda, Anda akan dialihkan ke halaman yang menunjukkan bahwa Anda belum membuat repositori apa pun. Pada titik ini, sisihkan perangkat lunak GitHub Desktop; kita akan kembali ke sana nanti: ![github-desktop](assets/6.webp)

## Langkah 2: Instal Obsidian

Mari beralih ke menginstal perangkat lunak penulisan. Di sini, Anda memiliki beberapa pilihan. Anda akan memerlukan perangkat lunak yang mendukung pengeditan file Markdown, karena Jaringan PlanB menggunakan format ini untuk file teks di repositorinya.
Ada banyak perangkat lunak yang khusus dirancang untuk mengedit file Markdown, seperti Typora, yang dirancang khusus untuk menulis. Meskipun tidak ideal, juga dimungkinkan untuk memilih editor kode, seperti Visual Studio Code (VSC) atau Sublime Text. Namun, sebagai penulis, saya lebih memilih menggunakan perangkat lunak Obsidian. Mari kita lihat bersama bagaimana cara menginstal dan memulai dengannya.
- Kunjungi https://obsidian.md/download dan unduh perangkat lunaknya: ![github-desktop](assets/7.webp)
- Instal Obsidian, jalankan perangkat lunaknya, pilih bahasa Anda, dan kemudian klik pada `Quick Start`: ![github-desktop](assets/8.webp)
- Anda akan sampai pada perangkat lunak Obsidian. Untuk saat ini, Anda tidak memiliki file yang terbuka: ![github-desktop](assets/9.webp)

## Langkah 3: Fork repositori PlanB Network

- Kunjungi repositori data PlanB Network di alamat berikut: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Dari halaman ini, klik tombol `Fork` di pojok kanan atas jendela: ![github-desktop](assets/11.webp)
- Di menu pembuatan, Anda dapat membiarkan pengaturan default. Pastikan kotak `Copy the dev branch only` dicentang, kemudian klik tombol `Create fork`: ![github-desktop](assets/12.webp)
- Anda kemudian akan sampai pada fork Anda sendiri dari repositori PlanB Network: ![github-desktop](assets/13.webp)
Fork ini merupakan repositori terpisah dari aslinya, meskipun saat ini berisi data yang sama. Anda sekarang akan bekerja pada repositori baru ini.

Dengan cara ini, kita telah membuat salinan dari repositori sumber PlanB Network. Fork Anda (salinannya) dan repositori asli sekarang akan berkembang secara independen satu sama lain. Di repositori asli, kontributor lain mungkin menambahkan data baru, sementara Anda, di fork Anda, akan melanjutkan dengan modifikasi Anda sendiri.
Untuk menjaga konsistensi antara kedua repositori ini, akan diperlukan untuk menyinkronkannya secara berkala sehingga mereka mengambil informasi yang sama. Untuk mengirim perubahan Anda ke repositori sumber, Anda akan menggunakan yang disebut **Pull Request**. Dan untuk mengintegrasikan perubahan dari repositori sumber ke dalam fork Anda, Anda akan menggunakan perintah **Sync fork** yang tersedia di antarmuka web GitHub.
![github-desktop](assets/14.webp)

## Langkah 4: Clone fork

- Kembali ke perangkat lunak GitHub Desktop. Pada saat ini, fork Anda seharusnya muncul di bagian `Your repositories`. Jika Anda tidak segera melihatnya, gunakan tombol panah ganda untuk menyegarkan daftar. Ketika fork Anda muncul, klik padanya untuk memilihnya:
![github-desktop](assets/15.webp)
- Kemudian klik pada tombol biru: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Pertahankan jalur default. Untuk mengonfirmasi, klik pada tombol biru `Clone`:
![github-desktop](assets/17.webp)
- Tunggu sementara GitHub Desktop mengkloning fork Anda secara lokal:
![github-desktop](assets/18.webp)
- Setelah mengkloning repositori, perangkat lunak menawarkan Anda dua pilihan. Anda harus memilih yang pertama: `To contribute to the parent project`. Pilihan ini akan memungkinkan Anda untuk menyajikan pekerjaan Anda di masa depan sebagai kontribusi untuk proyek induk (`PlanB-Network/bitcoin-educational-content`), dan bukan hanya sebagai modifikasi dari fork pribadi Anda (`[username]/bitcoin-educational-content`). Setelah opsi dipilih, klik pada `Continue`: ![github-desktop](assets/19.webp)
- GitHub Desktop Anda sekarang telah dikonfigurasi dengan benar. Sekarang, Anda dapat meninggalkan perangkat lunak terbuka di latar belakang untuk mengikuti modifikasi yang akan kami lakukan.
![github-desktop](assets/20.webp)
Apa yang telah kita capai pada tahap ini adalah pembuatan salinan lokal dari repositori Anda, yang dihosting di GitHub. Sebagai pengingat, repositori ini adalah fork dari repositori sumber dari PlanB Network. Anda akan dapat membuat modifikasi pada salinan lokal ini, seperti menambahkan tutorial, terjemahan, atau koreksi. Setelah modifikasi ini dibuat, Anda akan menggunakan perintah **Push origin** untuk mengirim modifikasi lokal Anda ke fork yang dihosting di GitHub.

Anda juga dapat mengambil modifikasi dari fork, misalnya, selama sinkronisasi dengan repositori PlanB Network. Untuk ini, Anda akan menggunakan perintah **Fetch origin** untuk mengunduh modifikasi ke salinan lokal Anda (klon Anda), dan kemudian perintah **Pull origin** untuk menggabungkannya dengan pekerjaan Anda. Ini memungkinkan Anda untuk tetap up to date dengan perkembangan terbaru dari proyek sambil berkontribusi secara efektif.

![github-desktop](assets/21.webp)
## Langkah 5: Buat vault baru di Obsidian

- Buka perangkat lunak Obsidian dan klik pada ikon vault kecil di bagian bawah kiri jendela:
![github-desktop](assets/22.webp)
- Klik pada tombol `Open` untuk membuka folder yang ada sebagai vault: ![github-desktop](assets/23.webp)
- Penjelajah file Anda akan terbuka. Anda perlu menemukan dan memilih folder yang berjudul `GitHub`, yang seharusnya berada di direktori `Documents` di antara file Anda. Jalur ini sesuai dengan yang Anda tetapkan selama langkah 4. Setelah memilih folder, konfirmasikan seleksinya. Pembuatan vault Anda di Obsidian kemudian akan diluncurkan pada halaman baru dari perangkat lunak:

![github-desktop](assets/24.webp)
-> **Perhatian**, penting untuk tidak memilih folder `bitcoin-educational-content` saat membuat vault baru di Obsidian. Sebagai gantinya, pilih folder induk, `GitHub`. Jika Anda memilih folder `bitcoin-educational-content`, folder konfigurasi `.obsidian`, yang berisi pengaturan Obsidian lokal Anda, akan secara otomatis terintegrasi ke dalam repositori. Kita ingin menghindari ini, karena tidak perlu untuk mentransfer konfigurasi Obsidian Anda ke repositori PlanB Network. Alternatifnya adalah menambahkan folder `.obsidian` ke file `.gitignore`, tetapi metode ini juga akan memodifikasi file `.gitignore` dari repositori sumber, yang tidak diinginkan.

- Di sisi kiri jendela, Anda dapat melihat pohon file dengan repositori GitHub Anda yang telah dikloning secara lokal.
- Dengan mengklik pada panah di samping nama folder, Anda dapat memperluasnya untuk mengakses subfolder dari repositori dan dokumen-dokumen mereka:
![github-desktop](assets/25.webp)
- Jangan lupa untuk mengatur Obsidian ke mode gelap: "Cahaya menarik bug" ;)

## Langkah 6: Pasang Editor Kode
Sebagian besar modifikasi Anda akan berada pada file dalam format Markdown (`.md`). Untuk mengedit dokumen ini, Anda dapat menggunakan Obsidian, perangkat lunak yang telah kita bahas sebelumnya. Namun, PlanB Network menggunakan format file lain, dan Anda akan perlu memodifikasi beberapa di antaranya.

Misalnya, saat membuat tutorial baru, Anda akan perlu membuat file YAML (`.yml`) untuk memasukkan tag untuk tutorial Anda, judulnya, dan ID pengajar Anda. Obsidian tidak menawarkan kemungkinan untuk memodifikasi jenis file ini, sehingga Anda akan memerlukan editor kode.

Untuk ini, beberapa pilihan tersedia untuk Anda. Meskipun notepad standar komputer Anda dapat digunakan untuk modifikasi ini, solusi ini tidak ideal untuk pekerjaan yang rapi. Saya merekomendasikan memilih perangkat lunak yang dirancang khusus untuk tujuan ini, seperti [VS Code](https://code.visualstudio.com/download) atau [Sublime Text](https://www.sublimetext.com/download). Sublime Text, yang terutama ringan, akan lebih dari cukup untuk kebutuhan kita.
- Pasang salah satu dari program perangkat lunak ini, dan simpan untuk modifikasi masa depan Anda. ![github-desktop](assets/26.webp)
Selamat! Lingkungan kerja Anda sekarang telah disiapkan untuk berkontribusi pada PlanB Network. Anda sekarang dapat menjelajahi [tutorial spesifik kami yang lain](https://planb.network/tutorials/others) untuk setiap jenis kontribusi (penerjemahan, proofreading, penulisan...).
