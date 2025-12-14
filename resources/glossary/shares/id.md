---
term: SHARE

---
Dalam konteks _pool_ penambangan, _share_ adalah indikator yang digunakan untuk mengukur kontribusi penambang individu di dalam _pool_. Ukuran ini berfungsi sebagai dasar untuk menghitung _reward_ yang didistribusikan oleh _pool_ kepada setiap penambang. Setiap _share_ berhubungan dengan _hash_ yang memenuhi target kesulitan yang lebih rendah dari jaringan Bitcoin.

Untuk menjelaskannya dengan sebuah analogi, bayangkan sebuah dadu dengan 20 sisi. Pada Bitcoin, anggaplah _proof-of-work_ membutuhkan angka yang lebih rendah dari 3 untuk memvalidasi sebuah blok (Hasil 1 atau 2). Sekarang, bayangkan bahwa dalam sebuah pool penambangan, target kesulitan untuk sebuah bagian ditetapkan pada angka 10. Dengan demikian, untuk seorang penambang individu di dalam _pool_, setiap lemparan dadu yang menghasilkan angka yang lebih rendah dari 10 dianggap sebagai _share_ yang valid. Bagian ini kemudian dikirimkan ke _pool_ oleh penambang, untuk mengklaim upah mereka, meskipun tidak sesuai dengan hasil yang valid untuk sebuah blok di Bitcoin.

Untuk setiap _hash_ yang dihitung, seorang penambang individu dalam sebuah _pool_ dapat menemukan tiga skenario yang berbeda:


- Jika nilai hash lebih besar atau sama dengan target tingkat kesulitan yang ditetapkan _pool_ untuk suatu bagian, maka hash ini tidak berguna. Penambang kemudian mengubah _nonce_ mereka untuk mencoba _hash_ yang baru: `hash > share > block`.
- Jika _hash_ lebih rendah dari target tingkat kesulitan pada bagian tersebut, tetapi lebih besar atau sama dengan target tingkat kesulitan Bitcoin, maka _hash_ ini merupakan _share_ yang valid, namun tidak cukup untuk memvalidasi blok. Penambang dapat mengirimkan _hash_ ini ke _pool_ mereka untuk mengklaim reward yang terkait dengan _share_ tersebut: `share > hash > block`.
- Jika _hash_ lebih rendah dari target kesulitan jaringan Bitcoin, maka dianggap sebagai _share_ yang valid dan blok yang valid. Penambang mengirimkan _hash_ ini ke _pool_ mereka, yang kemudian segera mempublikasikannya di jaringan Bitcoin. _Hash_ ini juga dihitung sebagai _share_ yang valid untuk penambang: `share > blok > hash`.

![](../../dictionnaire/assets/32.webp)

Sistem pembagian ini digunakan untuk memperkirakan pekerjaan yang dilakukan oleh setiap penambang dalam _pool_, tanpa harus menghitung ulang semua _hash_ yang dihasilkan oleh penambang secara individual, yang mana hal ini akan sangat tidak efisien untuk _pool_.

_Mining pool_ menyesuaikan tingkat kesulitan _share_ untuk menyeimbangkan beban verifikasi dan memastikan bahwa setiap penambang, baik yang kecil maupun yang besar, mengirimkan _share_ kira-kira setiap beberapa detik. Hal ini memungkinkan perhitungan yang akurat dari _hashrate_ setiap penambang dan distribusi _reward_ sesuai dengan metode perhitungan kompensasi yang dipilih (PPS, PPLNS, TIDES...).
