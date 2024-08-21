---
term: OBSOLETE (BLOCK)
---

Merujuk pada blok tanpa anak: sebuah blok yang valid, namun dikecualikan dari rantai utama Bitcoin. Hal ini terjadi ketika dua penambang menemukan blok yang valid pada tinggi rantai yang sama dalam periode waktu yang singkat dan menyiarkannya ke jaringan. Node akhirnya hanya memilih satu blok untuk dimasukkan ke dalam rantai, sesuai dengan prinsip rantai dengan pekerjaan terakumulasi terbanyak, menjadikan yang lainnya "usang". Proses yang mengarah pada produksi blok usang adalah sebagai berikut:
* Dua penambang menemukan blok yang valid pada tinggi rantai yang sama dalam interval waktu yang singkat. Mari kita sebut mereka `Block A` dan `Block B`;
* Masing-masing menyiarkan blok mereka ke jaringan node Bitcoin. Setiap node sekarang memiliki 2 blok pada tinggi yang sama. Oleh karena itu, ada dua rantai yang valid;
* Penambang terus mencari bukti pekerjaan untuk blok-blok berikutnya, tetapi untuk melakukannya, mereka harus memilih hanya satu blok antara `Block A` dan `Block B` di mana mereka akan menambang;
* Seorang penambang akhirnya menemukan blok yang valid di atas `Block B`. Mari kita sebut itu `Block B+1`;
* Mereka menyiarkan `Block B+1` ke node jaringan;
* Karena node mengikuti rantai terpanjang (dengan pekerjaan terakumulasi terbanyak), mereka akan memperkirakan bahwa `Chain B` adalah yang harus diikuti;
* Mereka akan meninggalkan `Block A` yang tidak lagi menjadi bagian dari rantai utama. Blok tersebut kini telah menjadi blok usang.

![](../../dictionnaire/assets/9.png)

> ► *Dalam bahasa Inggris, ini disebut sebagai "Stale Block". Dalam bahasa Prancis, ini juga bisa disebut "bloc périmé" atau "bloc abandonné". Meskipun saya tidak setuju dengan penggunaan ini, beberapa bitcoiner menggunakan istilah "bloc orphelin" untuk merujuk pada apa yang sebenarnya adalah blok usang.*