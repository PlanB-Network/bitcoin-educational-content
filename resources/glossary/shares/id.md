---
term: SAHAM

---
Dalam konteks kumpulan penambangan, bagian adalah indikator yang digunakan untuk mengukur kontribusi penambang individu di dalam kumpulan. Ukuran ini berfungsi sebagai dasar untuk menghitung reward yang didistribusikan oleh pool kepada setiap penambang. Setiap share berhubungan dengan hash yang memenuhi target kesulitan yang lebih rendah dari jaringan Bitcoin.

Untuk menjelaskannya dengan sebuah analogi, bayangkan sebuah dadu dengan 20 sisi. Pada Bitcoin, anggaplah bukti kerja membutuhkan angka yang lebih rendah dari 3 untuk memvalidasi sebuah blok (yaitu mencapai hasil 1 atau 2). Sekarang, bayangkan bahwa dalam sebuah pool penambangan, target kesulitan untuk sebuah bagian ditetapkan pada angka 10. Dengan demikian, untuk seorang penambang individu di dalam pool, setiap lemparan dadu yang menghasilkan angka yang lebih rendah dari 10 dianggap sebagai bagian yang valid. Bagian ini kemudian dikirimkan ke pool oleh penambang, untuk mengklaim upah mereka, meskipun tidak sesuai dengan hasil yang valid untuk sebuah blok di Bitcoin.

Untuk setiap hash yang dihitung, seorang penambang individu dalam sebuah pool dapat menemukan tiga skenario yang berbeda:


- Jika nilai hash lebih besar atau sama dengan target tingkat kesulitan yang ditetapkan pool untuk suatu bagian, maka hash ini tidak berguna. Penambang kemudian mengubah nonce mereka untuk mencoba hash yang baru: `hash > share > block`.
- Jika hash lebih rendah dari target tingkat kesulitan pada bagian tersebut, tetapi lebih besar atau sama dengan target tingkat kesulitan Bitcoin, maka hash ini merupakan bagian yang valid, namun tidak cukup untuk memvalidasi blok. Penambang dapat mengirimkan hash ini ke pool mereka untuk mengklaim reward yang terkait dengan share tersebut: `share > hash > block`.
- Jika hash lebih rendah dari target kesulitan jaringan Bitcoin, maka dianggap sebagai bagian yang valid dan blok yang valid. Penambang mengirimkan hash ini ke pool mereka, yang kemudian segera menyiarkannya di jaringan Bitcoin. Hash ini juga dihitung sebagai bagian yang valid untuk penambang: `share > blok > hash`.

![](../../dictionnaire/assets/32.webp)

Sistem pembagian ini digunakan untuk memperkirakan pekerjaan yang dilakukan oleh setiap penambang dalam pool, tanpa harus menghitung ulang semua hash yang dihasilkan oleh penambang secara individual, yang mana hal ini akan sangat tidak efisien untuk pool.

Mining pool menyesuaikan tingkat kesulitan share untuk menyeimbangkan beban verifikasi dan memastikan bahwa setiap penambang, baik yang kecil maupun yang besar, mengirimkan share kira-kira setiap beberapa detik. Hal ini memungkinkan perhitungan yang akurat dari hashrate setiap penambang dan distribusi reward sesuai dengan metode perhitungan kompensasi yang dipilih (PPS, PPLNS, TIDES...).

> ► *Dalam bahasa Prancis, "saham" dapat diterjemahkan sebagai "bagian".*