---
term: DURASI PUTARAN RATA-RATA

---
Durasi putaran rata-rata adalah sebuah indikator yang digunakan untuk memperkirakan waktu yang dibutuhkan oleh sebuah kolam penambangan (_mining pool_) untuk menemukan sebuah blok, berdasarkan tingkat kesulitan jaringan dan _hashrate_ kolam tersebut. Hal ini dihitung dengan mengambil jumlah bagian (_share_) yang diharapkan untuk menemukan sebuah blok dan membaginya dengan _hashrate_ kolam. Sebagai contoh, jika sebuah _mining pool_ memiliki 200 penambang, dan masing-masing menghasilkan rata-rata 4 _share_ per detik, maka total daya komputasi dari pool tersebut adalah 800 _share_ per detik:

```text
200 * 4 = 800
```

Dengan asumsi bahwa, dibutuhkan rata-rata 1 juta _share_ untuk menemukan sebuah blok yang valid, maka *Avg. Durasi Putaran* adalah 1.250 detik, atau sekitar 21 menit:

```text
1,000,000 / 800 = 1,250
```

Secara praktis, hal ini berarti bahwa, secara rata-rata, _mining pool_ harus menemukan satu blok setiap 21 menit atau lebih. Indikator ini berubah dengan perubahan dalam _hashrate_ pool: peningkatan _hashrate_ mengurangi Durasi Putaran Rata-rata, sementara penurunan akan memperpanjangnya. Indikator ini juga akan berfluktuasi dengan setiap penyesuaian berkala dari target tingkat kesulitan Bitcoin (setiap tahun 2016). Ukuran ini tidak memperhitungkan blok yang ditemukan oleh kolam lain dan hanya berfokus pada kinerja internal dari kolam tertentu.
