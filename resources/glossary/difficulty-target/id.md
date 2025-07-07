---
term: TARGET KESULITAN

---
Faktor kesulitan, yang juga dikenal sebagai target kesulitan, merupakan sebuah parameter yang digunakan dalam mekanisme konsensus dengan (_Proof-of-Work_, PoW) pada Bitcoin. Target ini mewakili nilai numerik yang menentukan kesulitan bagi para penambang untuk memecahkan masalah kriptografi tertentu, yang disebut _proof-of-work_, ketika membuat blok baru di _blockchain_.

Target kesulitan adalah angka 256-bit (64 byte) yang dapat disesuaikan yang menentukan batas penerimaan untuk _hash header_ blok. Dengan kata lain, agar sebuah blok dapat diterima, hash dari header blok tersebut dengan `SHA256d` (double `SHA256`) harus lebih rendah atau sama dengan target kesulitan. Proses _proof-of-work_ terdiri dari memodifikasi bidang `nonce` pada _header_ blok atau transaksi _coinbase_ sampai _hash_ yang dihasilkan lebih rendah dari nilai target.

Target ini disesuaikan setiap 2016 blok (kira-kira setiap dua minggu), dalam sebuah mekanisme yang disebut "penyesuaian kesulitan". Faktor kesulitan dihitung ulang berdasarkan waktu yang dibutuhkan untuk menambang blok 2016 sebelumnya. Jika total waktu kurang dari dua minggu, tingkat kesulitan akan meningkat dengan menyesuaikan target ke bawah. Jika total waktu lebih dari dua minggu, tingkat kesulitan menurun dengan menyesuaikan target ke atas. Tujuannya adalah untuk mempertahankan waktu penambangan rata-rata 10 menit per blok. Waktu interval antar blok ini membantu mencegah pembagian jaringan Bitcoin, yang mengakibatkan pemborosan daya komputasi. Target kesulitan dapat ditemukan di setiap _header_ blok, di dalam bidang `nBits`. Karena bidang ini direduksi menjadi 32 bit dan target sebenarnya adalah 256 bit, maka target ini dipadatkan menjadi format ilmiah yang kurang tepat.

![](../../dictionnaire/assets/34.webp)

> ► *Target kesulitan terkadang juga disebut "faktor kesulitan", dengan ekstensi, ini dapat dirujuk dengan pengkodeannya di _header_ blok dengan istilah "nBits."*
