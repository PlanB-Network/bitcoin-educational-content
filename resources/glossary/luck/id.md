---
term: KEBERUNTUNGAN

---
Sebuah indikator yang digunakan dalam mining pool untuk mengukur performa pool relatif terhadap ekspektasi teoritisnya. Seperti namanya, indikator ini mengevaluasi keberuntungan pool dalam menemukan blok. Keberuntungan dihitung dengan membandingkan jumlah keping yang secara teoritis dibutuhkan untuk menemukan blok yang valid, berdasarkan tingkat kesulitan Bitcoin saat ini, dengan jumlah keping yang dihasilkan untuk menemukan blok tersebut. Jumlah bagian yang lebih rendah dari yang diharapkan mengindikasikan keberuntungan, sementara jumlah yang lebih tinggi mengindikasikan ketidakberuntungan.

Dengan menghubungkan tingkat kesulitan pada Bitcoin dengan jumlah keping yang diproduksi setiap detik dan tingkat kesulitan setiap keping, pool dapat menghitung jumlah keping yang secara teoritis diperlukan untuk menemukan blok yang valid. Sebagai contoh, misalkan secara teoritis, dibutuhkan 100.000 keping untuk sebuah pool untuk menemukan sebuah blok. Jika pool menghasilkan 200.000 sebelum menemukan sebuah blok, keberuntungannya adalah 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Sebaliknya, jika pool ini menemukan blok yang valid setelah hanya menghasilkan 50.000 saham, maka keberuntungannya adalah 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Luck adalah indikator yang hanya dapat diperbarui setelah sebuah blok ditemukan oleh pool, menjadikannya indikator statis yang diperbarui secara berkala.