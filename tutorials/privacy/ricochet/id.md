---
name: Ricochet
description: Memahami dan menggunakan transaksi Ricochet
---
![cover ricochet](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, alat Ricochet tidak lagi tersedia. Namun, ada kemungkinan alat ini dapat diaktifkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda hanya dapat melakukan Ricochet secara manual. Bagian teoretis dari artikel ini tetap relevan untuk memahami cara kerjanya dan belajar cara melakukannya secara manual.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

> *"Sebuah alat premium yang menambahkan lompatan ekstra dari riwayat ke transaksi Anda. Mengelabui daftar hitam dan membantu melindungi dari penutupan akun pihak ketiga yang tidak adil."*

## Apa itu Ricochet?
Ricochet adalah teknik yang melibatkan pelaksanaan beberapa transaksi fiktif kepada diri sendiri untuk mensimulasikan transfer kepemilikan bitcoin. Alat ini berbeda dari transaksi Samourai lainnya karena tidak menyediakan anonimitas prospektif, melainkan bentuk anonimitas retrospektif. Ricochet membantu mengaburkan spesifisitas yang dapat mengompromikan fungibilitas sebuah koin Bitcoin.

Sebagai contoh, jika Anda melakukan coinjoin, output koin Anda dari campuran akan diidentifikasi sebagai itu. Alat analisis rantai dapat mendeteksi pola transaksi coinjoin dan memberi label pada koin yang keluar dari mereka. Memang, coinjoin bertujuan untuk memutuskan tautan historis sebuah koin, tetapi perjalanannya melalui coinjoins tetap terdeteksi. Untuk membuat analogi, fenomena ini mirip dengan mengenkripsi teks: meskipun kita tidak dapat mengakses teks asli, mudah diidentifikasi bahwa enkripsi telah diterapkan.

Tepatnya, label "koin output coinjoin" ini dapat mempengaruhi fungibilitas sebuah UTXO. Entitas yang diatur, seperti platform pertukaran, mungkin menolak untuk menerima UTXO yang telah menjalani coinjoin, atau bahkan meminta penjelasan dari pemiliknya, dengan risiko memiliki akun mereka diblokir atau dana dibekukan. Dalam beberapa kasus, platform bahkan mungkin melaporkan perilaku Anda ke otoritas negara.

Di sinilah metode Ricochet berperan. Untuk mengaburkan jejak yang ditinggalkan oleh coinjoin, Ricochet melakukan empat transaksi berturut-turut di mana pengguna mentransfer dana mereka ke diri mereka sendiri di alamat yang berbeda. Setelah rangkaian transaksi ini, alat Ricochet akhirnya merutekan bitcoin ke tujuan akhir mereka, seperti platform pertukaran. Tujuannya adalah untuk menciptakan jarak antara transaksi coinjoin asli dan tindakan pengeluaran akhir. Dengan cara ini, alat analisis rantai akan berpikir bahwa kemungkinan telah terjadi transfer kepemilikan setelah coinjoin, dan oleh karena itu tidak perlu mengambil tindakan terhadap pengirim.
![diagram ricochet](assets/en/1.webp)
Dalam menghadapi metode Ricochet, seseorang bisa membayangkan bahwa perangkat lunak analisis rantai akan memperdalam pemeriksaannya melebihi empat lompatan. Namun, platform ini menghadapi dilema dalam mengoptimalkan ambang batas deteksi. Mereka harus menetapkan batas jumlah lompatan setelah itu mereka mengakui bahwa perubahan kepemilikan kemungkinan telah terjadi dan bahwa kaitan dengan coinjoin sebelumnya harus diabaikan. Namun, menentukan ambang batas ini berisiko: setiap perluasan jumlah lompatan yang diamati secara eksponensial meningkatkan volume positif palsu, yaitu, individu yang salah ditandai sebagai peserta dalam coinjoin, padahal operasi tersebut sebenarnya dilakukan oleh orang lain. Skenario ini menimbulkan risiko besar bagi perusahaan-perusahaan ini, karena positif palsu mengarah pada ketidakpuasan, yang dapat mendorong pelanggan yang terpengaruh menuju kompetisi. Dalam jangka panjang, ambang batas yang terlalu ambisius menyebabkan platform kehilangan lebih banyak pelanggan daripada pesaingnya, yang dapat mengancam kelangsungan hidupnya. Oleh karena itu, rumit bagi platform ini untuk meningkatkan jumlah lompatan yang diamati, dan 4 seringkali merupakan jumlah yang cukup untuk menandingi analisis mereka.
Dengan demikian, **kasus penggunaan paling umum untuk Ricochet muncul ketika perlu untuk menyembunyikan partisipasi sebelumnya dalam coinjoin pada UTXO yang milik Anda**. Idealnya, lebih baik menghindari mentransfer bitcoin yang telah mengalami coinjoin ke entitas yang diatur. Namun, dalam keadaan tidak ada pilihan lain, terutama dalam keadaan mendesak untuk melikuidasi bitcoin menjadi mata uang fiat, Ricochet menawarkan solusi yang efektif.

## Bagaimana Cara Kerja Ricochet di Samourai Wallet?
Ricochet hanyalah metode di mana seseorang mengirim bitcoin kepada diri sendiri. Oleh karena itu, sepenuhnya mungkin untuk secara manual mensimulasikan Ricochet tanpa menggunakan alat khusus. Namun, bagi mereka yang ingin mengotomatiskan proses sambil mendapatkan hasil yang lebih terpolisir, alat Ricochet yang tersedia melalui aplikasi Samourai Wallet adalah solusi yang baik.

Karena layanan ini berbayar di Samourai, Ricochet menimbulkan biaya sebesar `100,000 sats` sebagai biaya layanan, ditambah dengan biaya penambangan. Dengan demikian, penggunaannya lebih direkomendasikan untuk transfer jumlah yang signifikan.

Aplikasi Samourai menawarkan dua varian Ricochet:
- Ricochet yang Diperkuat, atau "pengiriman bertahap," menawarkan keuntungan menyebar biaya layanan Samourai melalui lima transaksi berturut-turut. Opsi ini juga memastikan bahwa setiap transaksi disiarkan pada waktu yang berbeda dan dicatat dalam blok yang berbeda, yang sangat meniru perilaku perubahan kepemilikan. Meskipun lebih lambat, metode ini lebih disukai bagi mereka yang tidak terburu-buru, karena memaksimalkan efisiensi Ricochet dengan meningkatkan resistensinya terhadap analisis rantai.
- Ricochet Klasik, yang dirancang untuk menjalankan operasi dengan cepat dengan menyiarkan semua transaksi dalam interval waktu yang berkurang. Metode ini, oleh karena itu, menawarkan privasi yang lebih rendah dan resistensi yang lebih rendah terhadap analisis dibandingkan dengan metode yang diperkuat. Ini hanya harus dipilih untuk transfer darurat.

## Bagaimana Melakukan Transaksi Ricochet di Samourai Wallet?
Untuk melakukan transaksi Ricochet dari aplikasi Samourai Wallet, ikuti tutorial video kami:
![Tutorial video YouTube Ricochet](https://youtu.be/Gsz0zuVo3N4)

Jika Anda ingin mempelajari transaksi Ricochet yang dilakukan dalam tutorial ini, berikut ini adalah:
- Transaksi Ricochet pertama: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Transaksi Ricochet terakhir: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)
**Sumber Daya Eksternal:**
- https://docs.samourai.io/en/wallet/features/ricochet