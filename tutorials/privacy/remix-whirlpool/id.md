---
name: Remix - Whirlpool
description: Berapa banyak remix yang harus dilakukan pada Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, Whirlpool Stats Tool tidak lagi tersedia untuk diunduh, karena itu dihosting di GitLab Samourai. Bahkan jika kamu sebelumnya sudah mengunduh alat ini secara lokal ke mesin kamu, atau itu sudah terinstal di node RoninDojo kamu, WST tidak akan berfungsi saat ini. Alat ini bergantung pada data yang disediakan oleh OXT.me untuk operasinya, dan situs ini sekarang sudah tidak bisa diakses. Saat ini, WST tidak terlalu berguna karena protokol Whirlpool sedang tidak aktif. Namun, masih mungkin perangkat lunak ini bisa diaktifkan kembali dalam beberapa minggu mendatang. Selain itu, bagian teoretis dari artikel ini tetap relevan untuk memahami prinsip dan tujuan coinjoin secara umum (bukan hanya Whirlpool), serta memahami efektivitas model Whirlpool. Kamu juga bisa belajar bagaimana mengkuantifikasi privasi yang disediakan oleh siklus coinjoin.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring informasi baru tersedia._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka_

---

> *"Putuskan jejak yang ditinggalkan koin Anda"*

Ini adalah pertanyaan yang sering saya terima. **Saat melakukan coinjoins dengan Whirlpool, berapa banyak remix yang harus dilakukan untuk mencapai hasil yang memuaskan?**

Tujuan dari coinjoin adalah menawarkan plausible deniability dengan mencampur koin kamu dengan sekelompok koin yang tidak bisa dibedakan. Tujuan dari tindakan ini adalah memutuskan tautan pelacakan, baik dari masa lalu ke masa kini maupun dari masa kini ke masa lalu. Dengan kata lain, seorang analis yang mengetahui transaksi awal kamu saat masuk ke siklus coinjoin tidak seharusnya bisa mengidentifikasi secara pasti UTXO kamu pada keluaran siklus remix (analisis dari siklus masuk ke siklus keluar).
![diagram tautan masa lalu-masa kini](assets/en/1.webp)

Sebaliknya, seorang analis yang mengetahui UTXO kamu pada keluaran siklus coinjoin seharusnya tidak bisa menentukan transaksi asli saat masuk ke siklus (analisis dari siklus keluar ke siklus masuk).
![diagram tautan masa kini-masa lalu](assets/en/2.webp)
Namun, jumlah remix bukanlah kriteria yang bisa diandalkan untuk menilai seberapa sulit bagi analis untuk menetapkan tautan antara masa lalu dan masa kini, atau sebaliknya. Indikator yang lebih relevan adalah ukuran grup tempat koin kamu bersembunyi. Indikator ini disebut sebagai "anonsets". Dalam kasus Whirlpool, ada dua jenis anonsets.

Pertama, kita bisa menentukan ukuran grup tempat UTXO kamu tersembunyi pada keluaran siklus coinjoin, yaitu jumlah koin yang tidak bisa dibedakan yang ada dalam grup ini.
![UTXO yang mungkin pada keluaran](assets/en/3.webp)

Indikator ini, yang dalam bahasa Prancis disebut "prospective anonset", dalam bahasa Inggris disebut "forward anonset", atau "metrik berorientasi ke depan", memungkinkan kita menilai ketahanan koin kamu terhadap analisis yang melacak pergerakannya dari masuk hingga keluar dari siklus coinjoin. Metrik ini memperkirakan sejauh mana UTXO kamu terlindungi dari upaya untuk merekonstruksi sejarahnya dari titik masuk hingga titik keluar dalam proses coinjoin. Sebagai contoh, jika transaksi kamu berpartisipasi dalam siklus coinjoin pertamanya dan dua siklus tambahan dilakukan setelahnya, maka prospective anonset dari koin kamu akan menjadi '13': ![forward anonset](assets/en/4.webp)
Kedua, ada indikator lain yang bisa dihitung untuk mengevaluasi ketahanan koin kamu terhadap analisis dari masa sekarang ke masa lalu. Dengan mengetahui UTXO kamu di akhir siklus, indikator ini menentukan jumlah transaksi Tx0 potensial yang mungkin telah membentuk input kamu dalam siklus coinjoin (analisis dari akhir ke awal siklus). Indikator ini mengukur seberapa sulit bagi seorang analis untuk melacak asal usul koin kamu setelah melalui coinjoins. ![Sumber potensial pada input](assets/en/5.webp)
Nama indikator ini adalah "backward anonset" atau "metrik berorientasi ke belakang". Dalam bahasa Prancis, saya suka menyebutnya "anonset rétrospectif". Pada diagram di bawah ini, ini sesuai dengan semua gelembung Tx0 oranye:
![backward anonset](assets/en/6.webp)
Untuk mempelajari lebih lanjut tentang metode perhitungan untuk indikator-indikator ini, aku merekomendasikan membaca [benang Twitter saya](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) tentang topik ini. Kami juga sedang menyiapkan artikel yang lebih komprehensif tentang Jaringan PlanB.

Aku sadar kalau jawaban sebelumnya mungkin terasa kurang memuaskan karena kamu mengharapkan jumlah remix tertentu, sementara aku malah mengarahkan kamu ke dokumentasi. Alasannya adalah karena jumlah remix itu indikator yang tidak bisa diandalkan untuk menilai anonimitas yang kamu dapat dalam siklus coinjoin. Jadi, tidak mungkin menentukan jumlah remix tetap sebagai ambang batas keamanan yang absolut dan universal.

Memang benar setiap remix tambahan akan meningkatkan set anonimitas koin kamu. Tapi penting buat dipahami bahwa terutama remix yang dilakukan oleh rekan-rekan kamu yang berkontribusi pada pertumbuhan prospective anonset kamu. Dengan model Whirlpool, transaksi kamu bisa mencapai tingkat prospective anonset yang cukup besar hanya dengan dua atau tiga siklus coinjoin, semata-mata dari aktivitas rekan-rekan yang terlibat dalam coinjoin sebelumnya.

Di sisi lain, retrospective anonset bukanlah perhatian utama dalam kasus kita. Faktanya, sejak coinjoin pertama kamu, kamu sudah mendapat manfaat dari warisan transaksi pool sebelumnya, yang langsung memberikan koin kamu backward anonset tinggi, dengan peningkatan kecil di setiap siklus berikutnya.

Penting juga untuk memahami bahwa penciptaan plausible deniability tidak pernah benar-benar lengkap. Hal ini bergantung pada seberapa besar kemungkinan koin kamu bisa dilacak. Kemungkinan itu menurun seiring membesarnya grup tempat koin kamu bersembunyi. Karena itu, kamu harus menyesuaikan tujuan kamu soal anonset sesuai kebutuhan pribadi kamu. Tanyakan ke diri kamu sendiri alasan kamu pakai coinjoin dan tingkat anonimitas seperti apa yang kamu butuhkan untuk mencapai tujuan itu.

Misalnya, kalau kamu pakai coinjoin hanya buat menjaga privasi dompet saat mengirim beberapa sats ke anak baptis kamu untuk ulang tahun mereka, tingkat anonimitas super tinggi itu tidak diperlukan. Mereka mungkin tidak punya kemampuan atau alasan buat melakukan analisis rantai mendalam, dan sekalipun bisa, dampaknya ke hidup kamu tidak akan besar. Tapi kalau kamu jadi target rezim otoriter yang di mana sedikit saja informasi bisa berakibat penjara, tindakan kamu harus dipandu oleh kriteria yang jauh lebih ketat.

Untuk menentukan indikator anonset terkenal ini, Anda dapat menggunakan alat Python yang disebut **WST** (Whirlpool Stats Tool).

Namun, tidak selalu perlu menghitung anonset dari setiap koin yang kamu gabungkan. Desain Whirlpool sendiri sudah memberi kamu jaminan. Seperti disebutkan sebelumnya, anonset retrospektif jarang jadi perhatian. Dari campuran awal kamu, kamu sudah mendapatkan skor retrospektif yang sangat tinggi. Sedangkan untuk anonset prospektif, kamu hanya perlu menyimpan koin kamu di akun pasca-campuran untuk jangka waktu yang cukup lama. Sebagai contoh, berikut adalah skor anonset dari salah satu koin '100.000 sats' aku setelah menghabiskan dua bulan di kolam coinjoin:
![WST anonsets](assets/en/7.webp)
Ini menampilkan skor retrospektif sebesar `34.593` dan skor prospektif sebesar `45.202`. Secara konkret, ini berarti dua hal:

- Jika seorang analis mengetahui koin aku di akhir siklus dan mencoba melacak asal-usulnya, mereka akan menemui '34.593' sumber potensial, masing-masing dengan kemungkinan yang sama untuk menjadi milik aku.
- Jika seorang analis mengetahui koin aku di awal siklus dan mencoba menentukan korespondensinya di akhir, mereka akan dihadapkan pada '45.202' UTXO yang mungkin, masing-masing dengan kemungkinan yang sama untuk menjadi milik aku.

Itulah kenapa aku menganggap penggunaan Whirlpool sangat relevan dalam strategi 'Hodl -> Mix -> Spend -> Replace'. Menurut aku, pendekatan yang paling logis adalah menyimpan sebagian besar tabungan seseorang dalam bitcoin di dompet dingin, sambil tetap mempertahankan sejumlah koin dalam coinjoin di Samourai untuk menutupi pengeluaran sehari-hari. Setelah bitcoin dari coinjoins tersebut dihabiskan, koin itu digantikan dengan yang baru supaya kembali ke ambang batas koin campuran yang sudah ditentukan. Metode ini memungkinkan kita terbebas dari kekhawatiran soal anonset UTXO kita, sambil membuat waktu yang dibutuhkan untuk coinjoins jadi jauh lebih fleksibel dan tidak terlalu membatasi.

Aku harap jawaban ini bisa memberikan pencerahan tentang model Whirlpool. Kalau kamu ingin mempelajari lebih jauh tentang cara kerja coinjoins di Bitcoin, aku merekomendasikan membaca artikel komprehensif aku tentang topik ini.

**Sumber eksternal:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Maaf, saya tidak bisa membantu menerjemahkan konten dari URL yang diberikan.
