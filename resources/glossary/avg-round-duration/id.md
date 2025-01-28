---
term: AVG. DURASI PUTARAN

---
Durasi putaran rata-rata adalah sebuah indikator yang digunakan untuk memperkirakan waktu yang dibutuhkan oleh sebuah pool penambangan untuk menemukan sebuah blok, berdasarkan tingkat kesulitan jaringan dan hashrate pool tersebut. Hal ini dihitung dengan mengambil jumlah bagian yang diharapkan untuk menemukan sebuah blok dan membaginya dengan hashrate pool. Sebagai contoh, jika sebuah mining pool memiliki 200 penambang, dan masing-masing menghasilkan rata-rata 4 share per detik, maka total daya komputasi dari pool tersebut adalah 800 share per detik:

```text
200 * 4 = 800
```

Dengan asumsi bahwa, rata-rata, dibutuhkan 1 juta keping untuk menemukan sebuah blok yang valid, maka *Avg. Durasi Putaran* adalah 1.250 detik, atau sekitar 21 menit:

```text
1,000,000 / 800 = 1,250
```

Secara praktis, ini berarti bahwa, secara rata-rata, mining pool harus menemukan satu blok setiap 21 menit atau lebih. Indikator ini berfluktuasi dengan perubahan dalam hashrate pool: peningkatan hashrate mengurangi *Avg. Durasi Putaran*, sementara penurunan akan memperpanjangnya. Indikator ini juga akan berfluktuasi dengan setiap penyesuaian berkala dari target tingkat kesulitan Bitcoin (setiap tahun 2016). Ukuran ini tidak memperhitungkan blok yang ditemukan oleh pool lain dan hanya berfokus pada kinerja internal dari pool yang sedang dipelajari.