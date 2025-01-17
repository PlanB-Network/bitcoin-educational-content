---
name: Dasar-dasar GitHub
description: Memahami dasar-dasar Git dan GitHub
---

![cover](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tingkat atas tentang Bitcoin, tersedia dalam sebanyak mungkin bahasa. Semua konten yang diterbitkan di situs ini bersifat open-source dan dihosting di GitHub, menawarkan kesempatan kepada siapa saja untuk berkontribusi pada pengayaan platform. Kontribusi dapat berbentuk berbagai cara: mengoreksi dan memeriksa teks yang ada, menerjemahkan ke dalam bahasa lain, memperbarui informasi, atau membuat tutorial baru yang belum tersedia di situs kami.

Jika Anda ingin berkontribusi ke Jaringan PlanB, Anda akan perlu menggunakan Git dan GitHub. Jika alat-alat ini tidak familiar bagi Anda atau jika operasinya terasa samar, jangan panik, artikel ini adalah untuk Anda! Kami akan mengulas bersama dasar-dasar Git dan GitHub, serta jargon teknis terkait, untuk memungkinkan Anda menggunakan alat-alat ini secara efektif setelahnya.

## Apa itu Git?

Git adalah sistem kontrol versi, khusus dirancang untuk mengelola proyek perangkat lunak. Dibuat pada tahun 2005 oleh Linus Torvalds, Git dengan cepat menjadi standar dalam industri pengembangan perangkat lunak untuk kontrol versi. Tapi apa sebenarnya artinya itu?
![git](assets/1.webp)
Pada intinya, Git memungkinkan pengembang untuk melacak perubahan yang dibuat pada kode sumber proyek dari waktu ke waktu. Ini berarti bahwa dengan setiap perubahan dalam kode, Git merekam versi baru dari proyek. Jika terjadi kesalahan atau jika fitur eksperimental tidak berfungsi seperti yang diharapkan, dimungkinkan untuk kembali ke keadaan kode sebelumnya, seperti mesin waktu untuk file.

Salah satu fitur kunci dari Git adalah manajemen cabang. Cabang adalah semacam jalur paralel di mana pengembang dapat bekerja secara independen dari sisa proyek. Ini sangat memudahkan penambahan fitur baru atau koreksi bug tanpa mengganggu kode utama. Setelah modifikasi diuji dan divalidasi, mereka dapat digabungkan dengan cabang utama.

Salah satu kekhasan Git adalah kemampuannya untuk beroperasi secara terdistribusi. Setiap pengembang memiliki salinan lengkap dari proyek di hard drive komputer mereka sendiri, memungkinkan mereka untuk bekerja offline dan menggabungkan perubahan nanti ketika koneksi internet tersedia. Ini mengurangi risiko konflik dan memungkinkan beberapa pengembang untuk bekerja secara simultan pada proyek yang sama tanpa mengganggu satu sama lain.
Awalnya, Git dirancang terutama untuk proyek pengembangan perangkat lunak. Namun, itu juga dapat digunakan untuk mengelola proyek penulisan konten. Alih-alih berkolaborasi pada kode, kita berkolaborasi pada teks. Dan inilah metode yang tepat yang diadopsi oleh Jaringan PlanB untuk mengelola kontennya! Git memfasilitasi kolaborasi dalam penulisan kursus dan tutorial, karena memungkinkan pelacakan perubahan yang tepat, manajemen versi yang efisien, dan juga memungkinkan tinjauan dan peningkatan konten oleh kontributor lain.
## Apa itu GitHub?

GitHub adalah platform manajemen dan hosting kode sumber berdasarkan sistem kontrol versi Git yang baru saja kita bahas. Diluncurkan pada tahun 2008, GitHub dengan cepat mendapatkan popularitas dan telah menjadi referensi penting bagi pengembang di seluruh dunia. Tapi bagaimana GitHub berbeda dari Git, dan mengapa itu sangat penting dalam metode produksi konten kami?
![github](assets/2.webp)
Pertama, penting untuk memahami bahwa GitHub dibangun di atas Git (yang telah kita bahas di bagian sebelumnya). Sementara Git adalah alat yang melacak perubahan kode, GitHub adalah layanan online yang menghosting, berbagi, dan mengelola kode ini.

Bayangkan Git sebagai semacam buku log yang digunakan setiap pengembang di komputer mereka sendiri untuk mencatat semua perubahan dalam proyek mereka. GitHub, di sisi lain, seperti perpustakaan umum di mana semua buku log ini dapat dibagikan, dibandingkan, dan digabungkan.
Perbedaan mendasar antara Git dan GitHub terletak pada fungsi mereka: Git adalah alat yang digunakan secara lokal oleh setiap pengembang untuk mengelola versi kode mereka, sedangkan GitHub adalah platform online yang menyimpan versi tersebut dan memfasilitasi kolaborasi.
GitHub jauh lebih dari sekadar layanan hosting kode. Ini adalah platform kolaborasi yang memungkinkan pengembang untuk bekerja bersama secara efisien. Dan memang, PlanB Network menggunakan platform ini untuk menyimpan tidak hanya semua kode yang menggerakkan situs web, tetapi juga, dan ini yang menarik bagi kita, semua konten (tutorial, pelatihan, sumber daya...).

## Beberapa Istilah Teknis

Di Git dan GitHub, Anda akan menemui perintah dan fitur yang namanya mungkin terdengar kompleks. Di bagian terakhir ini, saya menyediakan definisi sederhana untuk memahami istilah teknis yang mungkin Anda temui saat menggunakan Git dan GitHub:

- **Fetch origin:** Perintah yang mengambil informasi terbaru dan perubahan dari repositori jarak jauh tanpa menggabungkannya dengan pekerjaan lokal Anda. Ini memperbarui repositori lokal Anda dengan cabang dan commit baru yang ada di repositori jarak jauh.

- **Pull origin:** Perintah yang mengambil pembaruan dari repositori jarak jauh dan segera mengintegrasikannya ke dalam cabang lokal Anda untuk menyinkronkannya. Ini menggabungkan langkah fetch dan merge menjadi satu perintah.
- **Sync Fork:** Fitur di GitHub yang memungkinkan Anda untuk memperbarui fork Anda dari suatu proyek dengan perubahan terbaru dari repositori sumber. Ini memastikan bahwa salinan proyek Anda tetap terkini dengan pengembangan utama.
- **Push origin:** Perintah yang digunakan untuk mengirim perubahan lokal Anda ke repositori jarak jauh.

- **Pull Request:** Permintaan yang dikirim oleh kontributor untuk menunjukkan bahwa mereka telah mendorong perubahan ke cabang di repositori jarak jauh dan menginginkan perubahan tersebut untuk ditinjau dan berpotensi digabungkan ke cabang utama repositori.

- **Commit:** Menyimpan perubahan Anda. Commit seperti snapshot instan dari pekerjaan Anda pada momen tertentu, yang memungkinkan untuk menjaga sejarah perubahan. Setiap commit mencakup pesan deskriptif yang menjelaskan apa yang telah dimodifikasi.

- **Branch:** Versi paralel dari repositori, memungkinkan Anda untuk bekerja pada perubahan tanpa mempengaruhi cabang utama (sering disebut "main" atau "master"). Cabang memfasilitasi pengembangan fitur baru dan koreksi bug tanpa risiko mengganggu kode stabil.

- **Merge:** Penggabungan terdiri dari mengintegrasikan perubahan dari satu cabang ke cabang lain. Ini digunakan, misalnya, untuk menambahkan perubahan dari cabang kerja ke cabang utama, yang memungkinkan menambahkan berbagai kontribusi.

- **Fork:** Mem-fork repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, yang memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Fork bisa berjalan sendiri dan menjadi proyek yang berbeda dari aslinya, atau bisa secara teratur disinkronkan dengan proyek asli untuk berkontribusi padanya.

- **Clone:** Mengkloning repositori berarti membuat salinan lokal di komputer Anda, yang memberi Anda akses ke semua file dan sejarahnya. Ini memungkinkan Anda untuk bekerja langsung pada proyek secara lokal.

- **Repository:** Ruang penyimpanan untuk proyek di GitHub. Repositori berisi semua file proyek serta sejarah semua perubahan yang telah dilakukan padanya. Ini adalah dasar penyimpanan dan kolaborasi di GitHub.

- **Issue:** Alat untuk melacak tugas dan bug di GitHub. Issue memungkinkan untuk melaporkan masalah, mengusulkan perbaikan, atau mendiskusikan fitur baru. Setiap issue dapat ditugaskan, dilabeli, dan dikomentari.

Daftar ini jelas tidak lengkap. Ada banyak istilah teknis lain yang spesifik untuk Git dan GitHub. Namun, yang disebutkan di sini adalah yang utama yang akan Anda temui secara sering.
Setelah membaca artikel ini, mungkin beberapa aspek tentang Git dan GitHub masih belum jelas bagi Anda. Saya mendorong Anda untuk mulai menggunakan alat-alat ini sendiri. Praktik seringkali adalah cara terbaik untuk memahami bagaimana mesin bekerja! Dan untuk memulai, Anda dapat menemukan 2 tutorial lainnya:
- **[Buat akun GitHub Anda](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[Menyiapkan Lingkungan Lokal Anda untuk Berkontribusi pada PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**