---
name: Remix - Whirlpool
description: Berapa banyak remix yang harus dilakukan pada Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, Whirlpool Stats Tool tidak lagi tersedia untuk diunduh, karena itu dihosting di Gitlab Samourai. Bahkan jika Anda sebelumnya telah mengunduh alat ini secara lokal ke mesin Anda, atau itu diinstal pada node RoninDojo Anda, WST tidak akan berfungsi saat ini. Alat ini bergantung pada data yang disediakan oleh OXT.me untuk operasinya, dan situs ini tidak lagi dapat diakses. Saat ini, WST tidak terlalu berguna karena protokol Whirlpool tidak aktif. Namun, masih mungkin bahwa perangkat lunak ini dapat diaktifkan kembali dalam beberapa minggu mendatang. Selain itu, bagian teoretis dari artikel ini tetap relevan untuk memahami prinsip dan tujuan coinjoins secara umum (bukan hanya Whirlpool), serta memahami efektivitas model Whirlpool. Anda juga dapat belajar bagaimana mengkuantifikasi privasi yang disediakan oleh siklus coinjoin.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring informasi baru tersedia._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka_

---

> *"Putuskan jejak yang ditinggalkan koin Anda"*

Ini adalah pertanyaan yang sering saya terima. **Saat melakukan coinjoins dengan Whirlpool, berapa banyak remix yang harus dilakukan untuk mencapai hasil yang memuaskan?**

Tujuan dari coinjoin adalah untuk menawarkan plausible deniability dengan mencampur koin Anda dengan sekelompok koin yang tidak dapat dibedakan. Tujuan dari tindakan ini adalah untuk memutuskan tautan pelacakan, baik dari masa lalu ke masa kini maupun dari masa kini ke masa lalu. Dengan kata lain, seorang analis yang mengetahui transaksi awal Anda pada masuknya siklus coinjoin tidak seharusnya dapat mengidentifikasi secara definitif UTXO Anda pada keluaran siklus remix (analisis dari siklus masuk ke siklus keluar).
![diagram tautan masa lalu-masa kini](assets/en/1.webp)

Sebaliknya, seorang analis yang mengetahui UTXO Anda pada keluaran siklus coinjoin seharusnya tidak dapat menentukan transaksi asli pada masuknya siklus (analisis dari siklus keluar ke siklus masuk).
![diagram tautan masa kini-masa lalu](assets/en/2.webp)
Namun, jumlah remix bukanlah kriteria yang dapat diandalkan untuk mengevaluasi kesulitan yang akan dihadapi analis dalam menetapkan tautan antara masa lalu dan masa kini, atau sebaliknya. Indikator yang lebih relevan adalah ukuran grup tempat koin Anda bersembunyi. Indikator ini disebut sebagai "anonsets". Dalam kasus Whirlpool, ada dua jenis anonsets.

Pertama, kita dapat menentukan ukuran grup tempat UTXO Anda tersembunyi pada keluaran siklus coinjoin, yaitu, jumlah koin yang tidak dapat dibedakan yang ada dalam grup ini.
![UTXO yang mungkin pada keluaran](assets/en/3.webp)
Indikator ini, yang disebut "prospective anonset" dalam bahasa Prancis, "forward anonset" dalam bahasa Inggris, atau "metrik berorientasi ke depan", memungkinkan kita untuk menilai ketahanan koin Anda terhadap analisis yang melacak jalannya dari masuk hingga keluar dari siklus coinjoin. Metrik ini memperkirakan sejauh mana UTXO Anda dilindungi dari upaya untuk merekonstruksi sejarahnya dari titik masuk hingga titik keluar dalam proses coinjoin. Sebagai contoh, jika transaksi Anda berpartisipasi dalam siklus coinjoin pertamanya dan dua siklus tambahan dilakukan setelahnya, prospective anonset dari koin Anda akan menjadi `13`: ![forward anonset](assets/en/4.webp)
Kedua, indikator lain dapat dihitung untuk mengevaluasi ketahanan koin Anda terhadap analisis dari masa sekarang ke masa lalu. Dengan mengetahui UTXO Anda di akhir siklus, indikator ini menentukan jumlah transaksi Tx0 potensial yang mungkin telah membentuk input Anda dalam siklus coinjoin (analisis dari akhir ke awal siklus). Indikator ini mengukur seberapa sulitnya bagi seorang analis untuk melacak asal usul koin Anda setelah melalui coinjoins. ![Sumber potensial pada input](assets/en/5.webp)
Nama indikator ini adalah "backward anonset" atau "metrik berorientasi ke belakang". Dalam bahasa Prancis, saya suka menyebutnya "anonset rétrospectif". Pada diagram di bawah ini, ini sesuai dengan semua gelembung Tx0 oranye:
![backward anonset](assets/en/6.webp)
Untuk mempelajari lebih lanjut tentang metode perhitungan untuk indikator-indikator ini, saya merekomendasikan membaca [benang Twitter saya](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) tentang topik ini. Kami juga sedang menyiapkan artikel yang lebih komprehensif tentang Jaringan PlanB.

Saya menyadari bahwa jawaban yang diberikan mungkin terasa tidak memuaskan karena Anda berharap untuk mendapatkan jumlah remix tertentu, dan saya mengarahkan Anda ke dokumentasi. Alasannya adalah bahwa jumlah remix merupakan indikator yang tidak dapat diandalkan untuk mengevaluasi anonimitas yang diperoleh dalam siklus coinjoin. Oleh karena itu, tidak mungkin untuk menentukan jumlah remix tetap sebagai ambang batas keamanan yang absolut dan universal.

Memang benar bahwa setiap remix tambahan dari koin Anda meningkatkan set anonimitasnya. Namun, penting untuk memahami bahwa terutama remix yang dilakukan oleh rekan-rekan Anda yang berkontribusi pada pertumbuhan prospective anonset Anda. Dengan model Whirlpool, transaksi Anda dapat mencapai tingkat prospective anonset yang cukup besar hanya dengan dua atau tiga siklus coinjoin, semata-mata melalui aktivitas rekan-rekan yang terlibat dalam coinjoin sebelumnya.

Di sisi lain, retrospective anonset bukanlah perhatian dalam kasus kita. Faktanya, dari coinjoin awal Anda, Anda mendapat manfaat dari warisan transaksi pool sebelumnya, langsung memberikan koin Anda backward anonset yang tinggi, dengan peningkatan marginal di setiap siklus berikutnya.
Juga penting untuk memahami bahwa penciptaan plausible deniability tidak pernah lengkap. Hal ini bergantung pada kemungkinan pelacakan koin Anda. Kemungkinan ini menurun seiring dengan bertambahnya ukuran grup yang menyembunyikannya. Oleh karena itu, Anda harus menyesuaikan tujuan Anda dalam hal anonset sesuai dengan harapan pribadi Anda. Tanyakan pada diri sendiri tentang alasan yang mendorong Anda menggunakan coinjoins dan tingkat anonimitas yang diperlukan untuk mencapai tujuan tersebut. Misalnya, jika penggunaan coinjoins hanya bertujuan untuk menjaga privasi dompet Anda saat mengirim beberapa sats ke anak baptis Anda untuk ulang tahun mereka, tingkat anonimitas yang sangat tinggi tidak diperlukan. Anak baptis Anda mungkin tidak mampu melakukan analisis rantai secara mendalam, dan bahkan jika mereka bisa, dampaknya terhadap hidup Anda tidak akan menjadi bencana. Namun, jika Anda menjadi target rezim otoriter di mana sedikit saja informasi dapat mengakibatkan penjara, tindakan Anda perlu dipandu oleh kriteria yang jauh lebih ketat.

Untuk menentukan indikator anonset terkenal ini, Anda dapat menggunakan alat Python yang disebut **WST** (Whirlpool Stats Tool).

Namun, tidak selalu perlu menghitung anonset dari setiap koin yang Anda gabungkan. Desain Whirlpool sendiri sudah memberikan Anda jaminan. Seperti disebutkan sebelumnya, anonset retrospektif jarang menjadi perhatian. Dari campuran awal Anda, Anda sudah mendapatkan skor retrospektif yang sangat tinggi. Sedangkan untuk anonset prospektif, Anda hanya perlu menyimpan koin Anda di akun pasca-campuran untuk jangka waktu yang cukup lama. Sebagai contoh, berikut adalah skor anonset dari salah satu koin `100.000 sats` saya setelah menghabiskan dua bulan di kolam coinjoin:
![WST anonsets](assets/en/7.webp)
Ini menampilkan skor retrospektif sebesar `34.593` dan skor prospektif sebesar `45.202`. Secara konkret, ini berarti dua hal:
- Jika seorang analis mengetahui koin saya di akhir siklus dan mencoba melacak asal-usulnya, mereka akan menemui `34.593` sumber potensial, masing-masing dengan kemungkinan yang sama untuk menjadi milik saya.
- Jika seorang analis mengetahui koin saya di awal siklus dan mencoba menentukan korespondensinya di akhir, mereka akan dihadapkan pada `45.202` UTXO yang mungkin, masing-masing dengan kemungkinan yang sama untuk menjadi milik saya.
Itulah mengapa saya menganggap penggunaan Whirlpool sangat relevan dalam strategi `Hodl -> Mix -> Spend -> Replace`. Menurut saya, pendekatan yang paling logis adalah menyimpan sebagian besar tabungan seseorang dalam bitcoin di dompet dingin, sambil terus mempertahankan sejumlah koin dalam coinjoin di Samourai untuk menutupi pengeluaran sehari-hari. Setelah bitcoin dari coinjoins tersebut dihabiskan, mereka digantikan dengan yang baru untuk kembali ke ambang batas koin campuran yang ditentukan. Metode ini memungkinkan kita untuk membebaskan diri dari kekhawatiran tentang anonset dari UTXO kita, sambil membuat waktu yang diperlukan untuk coinjoins menjadi efektif jauh lebih tidak restriktif.

Saya harap jawaban ini telah memberikan pencerahan tentang model Whirlpool. Jika Anda ingin mempelajari lebih lanjut tentang cara kerja coinjoins di Bitcoin, saya merekomendasikan membaca [artikel komprehensif saya tentang topik ini](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

**Sumber eksternal:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Maaf, saya tidak bisa membantu menerjemahkan konten dari URL yang diberikan.