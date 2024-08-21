---
term: SHARES
---

Dalam konteks kolam penambangan, sebuah *share* adalah indikator yang digunakan untuk mengukur kontribusi penambang individu dalam kolam tersebut. Ukuran ini berfungsi sebagai dasar untuk menghitung hadiah yang didistribusikan kembali oleh kolam kepada setiap penambang. Setiap *share* sesuai dengan hash yang memenuhi target kesulitan lebih rendah daripada jaringan Bitcoin.

Untuk menjelaskan dengan analogi, bayangkan sebuah dadu ber-20 sisi. Di Bitcoin, anggaplah bahwa bukti kerja memerlukan pengguliran angka lebih rendah dari 3 untuk memvalidasi sebuah blok (yaitu, mencapai hasil 1 atau 2). Sekarang, bayangkan bahwa dalam sebuah kolam penambangan, target kesulitan untuk sebuah *share* ditetapkan pada 10. Jadi, untuk penambang individu dalam kolam, setiap lemparan dadu yang menghasilkan angka lebih rendah dari 10 dihitung sebagai *share* yang valid. *Share-share* ini kemudian ditransmisikan ke kolam oleh penambang, untuk mengklaim hadiah mereka, meskipun mereka tidak sesuai dengan hasil yang valid untuk sebuah blok di Bitcoin.

Untuk setiap hash yang dihitung, penambang individu dalam sebuah kolam dapat menghadapi tiga skenario berbeda:
* Jika nilai hash lebih besar dari atau sama dengan target kesulitan kolam yang ditetapkan untuk sebuah *share*, maka hash ini tidak berguna. Penambang kemudian mengubah nonce mereka untuk mencoba hash baru: `hash > share > block`.
* Jika hash lebih rendah dari target kesulitan *share*, tetapi lebih besar dari atau sama dengan target kesulitan Bitcoin, maka hash ini merupakan *share* yang valid, namun tidak cukup untuk memvalidasi sebuah blok. Penambang dapat mengirim hash ini ke kolam mereka untuk mengklaim hadiah yang terkait dengan *share*: `share > hash > block`.
* Jika hash lebih rendah dari target kesulitan jaringan Bitcoin, ini dianggap sebagai *share* yang valid dan juga blok yang valid. Penambang mentransmisikan hash ini ke kolam mereka, yang segera menyiarkannya di jaringan Bitcoin. Hash ini juga dihitung sebagai *share* yang valid untuk penambang: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Sistem *share* ini digunakan untuk memperkirakan pekerjaan yang dilakukan oleh setiap penambang individu dalam sebuah kolam, tanpa harus menghitung ulang semua hash yang dihasilkan oleh penambang, yang akan sangat tidak efisien bagi kolam.

Kolam penambangan menyesuaikan kesulitan *share* untuk menyeimbangkan beban verifikasi dan memastikan bahwa setiap penambang, baik kecil maupun besar, mengirimkan *share* kira-kira setiap beberapa detik. Ini memungkinkan perhitungan yang akurat dari hashrate setiap penambang dan distribusi hadiah sesuai dengan metode perhitungan kompensasi yang dipilih (PPS, PPLNS, TIDES...).

> ► *Dalam bahasa Prancis, "shares" dapat diterjemahkan sebagai "part".*