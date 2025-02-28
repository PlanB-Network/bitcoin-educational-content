---
term: PENYESUAIAN KESULITAN

---
Penyesuaian tingkat kesulitan adalah sebuah proses periodik yang mendefinisikan ulang target tingkat kesulitan untuk mekanisme pembuktian kerja (mining) pada Bitcoin. Peristiwa ini terjadi setiap 2016 blok (kurang lebih setiap dua minggu). Hal ini berfungsi untuk menambah atau mengurangi faktor kesulitan (disebut juga target kesulitan), tergantung pada seberapa cepat blok 2016 terakhir ditemukan. Penyesuaian ini bertujuan untuk mempertahankan tingkat produksi blok yang stabil dan dapat diprediksi, dengan frekuensi satu blok setiap 10 menit, meskipun ada variasi dalam daya komputasi yang digunakan oleh para penambang. Perubahan tingkat kesulitan selama penyesuaian dibatasi hingga faktor 4. Rumus yang dijalankan oleh node untuk menghitung target baru adalah sebagai berikut:

$$N = A \cdot \left(\frac{T}{1.209.600}\right)$$

&nbsp;

Dimana:


- $N$: Target baru;
- $A$: Target lama dari blok 2016 yang lalu;
- $T$: Total waktu aktual dari blok 2016 terakhir dalam detik;
- $1,209,600$: Target waktu dalam detik untuk menghasilkan 2016 blok dengan interval 10 menit di antara masing-masing blok.

> dalam bahasa Prancis, istilah "reciblage" terkadang juga digunakan untuk merujuk pada penyesuaian. Dalam bahasa Inggris, istilah ini disebut sebagai "Difficulty Adjustment" (Penyesuaian Kesulitan)