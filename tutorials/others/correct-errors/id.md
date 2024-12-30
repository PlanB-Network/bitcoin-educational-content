---
name: Kontribusi - Koreksi
description: Bagaimana cara mengoreksi kesalahan pada Jaringan PlanB?
---
![cover](assets/cover.webp)

Misi PlanB adalah menyediakan sumber daya pendidikan tentang Bitcoin yang terdepan dalam sebanyak mungkin bahasa. Semua konten yang dipublikasikan di situs ini bersifat open-source dan dihosting di GitHub, yang memungkinkan siapa saja untuk berpartisipasi dalam memperkaya platform. Kontribusi dapat mengambil berbagai bentuk: mengoreksi dan memeriksa teks yang ada, menerjemahkan ke dalam bahasa lain, memperbarui informasi, atau membuat tutorial baru yang belum tersedia di situs kami.

Jika, saat mengkonsultasikan salah satu konten pendidikan kami (tutorial, pelatihan, sumber daya...), Anda mengidentifikasi kesalahan, baik itu kesalahan ejaan, tata bahasa, kesalahan terjemahan kecil dalam bahasa ibu Anda, atau bahkan typo, kami akan sangat berterima kasih jika Anda dapat mengusulkan koreksi cepat sendiri.

Tutorial ini memandu Anda langkah demi langkah melalui proses mengoreksi kesalahan kecil tersebut. Ini adalah tutorial yang ditujukan untuk pemula yang tidak ingin terjun ke dalam kerumitan Git. Namun, jika Anda nyaman dengan Git, berikut adalah ringkasan cepat: Anda hanya perlu melakukan fork [repositori data Jaringan PlanB](https://github.com/PlanB-Network/bitcoin-educational-content), membuat perubahan pada cabang yang didedikasikan, dan mengajukan Pull Request terhadap cabang `dev` dari repositori sumber.

Harap dicatat bahwa jika Anda berencana untuk melakukan tinjauan dan revisi dokumen secara lengkap, terutama untuk terjemahan konten, saya mengundang Anda untuk berkonsultasi [tutorial lebih rinci ini](https://planb.network/tutorials/others/contribution/content-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Di sini, kami hanya fokus pada cara melakukan koreksi cepat untuk kesalahan kecil.

- Pertama, Anda perlu memiliki akun di GitHub. Jika Anda tidak tahu cara membuat akun, kami telah membuat [tutorial terperinci untuk membimbing Anda](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c).
- Kunjungi [repositori GitHub PlanB yang didedikasikan untuk data](https://github.com/PlanB-Network/bitcoin-educational-content):
![typos](assets/01.webp)
- Di sini, Anda akan menemukan semua konten kami yang disusun berdasarkan bagian.
- Jika Anda ingin memodifikasi tutorial, misalnya, pergi ke folder `tutorials`:
![typos](assets/02.webp)
- Anda kemudian akan menemukan kategori tutorial yang berbeda di situs web kami. Misalnya, jika Anda ingin memodifikasi tutorial dalam kategori `Privacy`, klik pada folder yang sesuai:
![typos](assets/03.webp)
- Kemudian pilih folder yang sesuai dengan konten yang ingin Anda koreksi:
![typos](assets/04.webp)
- Di setiap folder konten, Anda akan menemukan data yang tersedia dalam berbagai bahasa. Misalnya, file `en.md` sesuai dengan versi bahasa Inggris dari tutorial, sementara file `fr.md` mewakili versi bahasa Prancis. Pilih file yang sesuai dengan bahasa yang ingin Anda modifikasi: ![typos](assets/05.webp)
- Anda kemudian akan tiba di halaman GitHub dari konten tersebut. Pastikan Anda berada di dokumen yang ingin Anda modifikasi: ![typos](assets/06.webp)
- Klik pada ikon pensil kecil di kiri atas: ![typos](assets/07.webp)
- Jika Anda belum pernah berkontribusi pada konten Jaringan PlanB sebelumnya, Anda perlu membuat fork dari repositori asli. Melakukan fork pada repositori berarti membuat salinan repositori tersebut di akun GitHub Anda sendiri, yang memungkinkan Anda untuk bekerja pada proyek tanpa mempengaruhi repositori asli. Klik pada tombol `Fork this repository`: ![typos](assets/08.webp)
- Anda akan tiba di halaman pengeditan GitHub: ![typos](assets/09.webp)- Lakukan modifikasi teks Anda untuk memperbaiki kesalahan yang telah Anda temukan. Jangan takut, Anda saat ini berada di fork Anda sendiri, jadi ini tidak akan mengubah apa pun di situs PlanB Network untuk saat ini. Sebagai contoh, di sini, mari kita bayangkan bahwa saya memodifikasi kata "entrées" karena memiliki kesalahan penulisan: ![typos](assets/10.webp)
- Setelah koreksi Anda pada dokumen ini selesai, Anda dapat mengklik tombol hijau `Commit Changes...`. Commit adalah seperti snapshot instan dari pekerjaan Anda pada suatu momen tertentu, yang memungkinkan untuk menyimpan riwayat perubahan: ![typos](assets/11.webp)
- Tambahkan judul untuk modifikasi Anda, serta deskripsi singkat: ![typos](assets/12.webp)
- Klik tombol hijau `Propose changes`: ![typos](assets/13.webp)
- Anda akan tiba di halaman yang merangkum semua perubahan Anda: ![typos](assets/14.webp)
- Dengan menggulir ke bawah, Anda dapat melihat modifikasi spesifik yang telah Anda buat: ![typos](assets/15.webp)
- Jika semuanya sesuai dengan Anda dan Anda telah menyelesaikan modifikasi Anda, Anda dapat mengklik tombol hijau `Create Pull Request`: ![typos](assets/16.webp)
- Anda akan tiba di halaman PR. Pull Request adalah permintaan yang dikirim oleh kontributor untuk menunjukkan bahwa mereka telah mendorong modifikasi pada cabang di repositori jarak jauh dan bahwa mereka ingin modifikasi tersebut ditinjau dan berpotensi digabungkan ke cabang utama repositori: ![typos](assets/17.webp)
- Anda dapat menambahkan judul dan deskripsi singkat untuk PR Anda: ![typos](assets/18.webp)
- Jika semuanya terlihat baik bagi Anda, Anda dapat mengklik tombol hijau `Create Pull Request`: ![typos](assets/19.webp)
- Selamat, PR Anda telah dikirim! Anda dapat mengikuti kemajuannya di tab `Pull requests` di [repositori GitHub PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content/pulls) :![typos](assets/20.webp)
Terima kasih banyak atas kontribusi Anda! Jika Anda ingin membuat jenis kontribusi lain ke PlanB Network seperti penulisan konten atau terjemahan, jangan ragu untuk [melihat tutorial lain kami di bagian "Kontribusi"](https://planb.network/tutorials/others).
