---
term: MINISCRIPT

---
Kerangka kerja yang dirancang untuk menyediakan kerangka kerja untuk memprogram skrip dengan aman di Bitcoin. Bahasa asli Bitcoin disebut skrip. Script ini cukup rumit untuk digunakan dalam praktiknya, terutama untuk aplikasi yang canggih dan disesuaikan. Terlebih lagi, sangat sulit untuk memverifikasi batasan-batasan skrip. _Miniscript_ menggunakan bagian dari skrip Bitcoin untuk menyederhanakan pembuatan, analisis, dan verifikasi. Setiap miniscript setara dengan skrip asli. Bahasa kebijakan yang mudah digunakan digunakan, yang kemudian dikompilasi ke dalam _Miniscript_, untuk akhirnya sesuai dengan skrip asli.

![](../../dictionnaire/assets/30.webp)

Dengan demikian, _Miniscript_ memungkinkan para pengembang untuk membuat skrip yang canggih dengan cara yang lebih aman dan dapat diandalkan. Sifat-sifat penting dari _miniscript_ adalah sebagai berikut:


- Ini memungkinkan analisis statis skrip, termasuk kondisi penggunaan yang diizinkan dan biayanya dalam hal sumber daya;
- Hal ini memungkinkan pembuatan skrip yang sesuai dengan konsensus;
- Hal ini memungkinkan untuk menganalisis apakah jalur pengeluaran yang berbeda sesuai dengan aturan standar node;
- Ini menetapkan standar umum, dapat dimengerti dan disusun, untuk semua perangkat lunak dan dompet perangkat keras.

Proyek _Miniscript_ diluncurkan pada tahun 2018 oleh Peter Wuille, Andrew Poelstra, dan Sanket Kanjalkar, melalui perusahaan Blockstream. _Miniscript_ ditambahkan ke dompet Bitcoin Core dalam mode _watch-only_ pada bulan Desember 2022 dengan versi 24.0, dan kemudian sepenuhnya pada bulan Mei 2023 dengan versi 25.0.
