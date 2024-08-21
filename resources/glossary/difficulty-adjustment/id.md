---
term: PENYESUAIAN KESULITAN
---

Penyesuaian kesulitan adalah proses periodik yang mendefinisikan ulang target kesulitan untuk mekanisme proof of work (penambangan) pada Bitcoin. Peristiwa ini terjadi setiap 2016 blok (sekitar setiap dua minggu). Ini bertujuan untuk meningkatkan atau menurunkan faktor kesulitan (juga disebut target kesulitan), tergantung pada seberapa cepat 2016 blok terakhir ditemukan. Penyesuaian bertujuan untuk menjaga tingkat produksi blok yang stabil dan dapat diprediksi, dengan frekuensi satu blok setiap 10 menit, meskipun terdapat variasi dalam kekuatan komputasi yang dikerahkan oleh para penambang. Perubahan dalam kesulitan selama penyesuaian dibatasi hingga faktor 4. Rumus yang dijalankan oleh node untuk menghitung target baru adalah sebagai berikut:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Dimana:
* $N$: Target baru;
* $A$: Target lama dari 2016 blok terakhir;
* $T$: Total waktu aktual dari 2016 blok terakhir dalam detik;
* $1,209,600$: Waktu target dalam detik untuk memproduksi 2016 blok dengan interval 10 menit antar setiap blok.

> ► *Dalam bahasa Prancis, istilah "reciblage" terkadang juga digunakan untuk merujuk pada penyesuaian. Dalam bahasa Inggris, ini disebut sebagai "Difficulty Adjustment".*