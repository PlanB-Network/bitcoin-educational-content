---
term: AVG. ROUND DURATION
---

Durasi rata-rata putaran adalah indikator yang digunakan untuk memperkirakan waktu yang dibutuhkan sebuah kolam penambangan untuk menemukan sebuah blok, berdasarkan kesulitan jaringan dan hashrate kolam tersebut. Ini dihitung dengan mengambil jumlah saham yang diharapkan untuk menemukan sebuah blok dan membaginya dengan hashrate kolam. Sebagai contoh, jika sebuah kolam penambangan memiliki 200 penambang, dan masing-masing menghasilkan rata-rata 4 saham per detik, maka total kekuatan komputasi kolam adalah 800 saham per detik:

```text
200 * 4 = 800
```

Dengan asumsi bahwa, rata-rata, dibutuhkan 1 juta saham untuk menemukan sebuah blok yang valid, maka *Avg. Round Duration* kolam tersebut akan menjadi 1.250 detik, atau sekitar 21 menit:

```text
1,000,000 / 800 = 1,250
```

Dalam praktiknya, ini berarti bahwa, rata-rata, kolam penambangan seharusnya menemukan sebuah blok setiap 21 menit atau sekitar itu. Indikator ini berfluktuasi dengan perubahan hashrate kolam: peningkatan dalam hashrate mengurangi *Avg. Round Duration*, sementara penurunan memperpanjangnya. Ini juga akan berfluktuasi dengan setiap penyesuaian periodik dari target kesulitan Bitcoin (setiap 2016 blok). Ukuran ini tidak memperhitungkan blok yang ditemukan oleh kolam lain dan hanya fokus pada kinerja internal dari kolam yang sedang diteliti.