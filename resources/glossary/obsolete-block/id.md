---
term: USANG (BLOK)

---
Mengacu pada sebuah blok tanpa anak: sebuah blok yang valid, tetapi tidak termasuk dalam rantai Bitcoin utama. Hal ini terjadi ketika dua penambang menemukan sebuah blok yang valid pada ketinggian rantai yang sama dalam waktu yang singkat dan menyiarkannya melalui jaringan. Node pada akhirnya hanya memilih satu blok untuk dimasukkan ke dalam rantai, sesuai dengan prinsip rantai dengan akumulasi pekerjaan yang paling banyak, membuat blok yang lain menjadi "usang". Proses yang mengarah pada produksi sebuah blok usang adalah sebagai berikut:


- Dua penambang menemukan sebuah blok yang valid pada ketinggian rantai yang sama dalam interval waktu yang singkat. Kita sebut saja mereka sebagai `Blok A` dan `Blok B`;
- Masing-masing menyiarkan blok mereka ke jaringan node Bitcoin. Setiap node sekarang memiliki 2 blok pada ketinggian yang sama. Oleh karena itu, ada dua rantai yang valid;
- Para penambang terus mencari bukti-bukti kerja untuk blok-blok berikutnya, namun untuk melakukannya, mereka harus memilih hanya satu blok di antara `Blok A` dan `Blok B` yang akan mereka tambang;
- Seorang penambang akhirnya menemukan sebuah blok yang valid di atas `Blok B`. Kita sebut saja sebagai `Block B+1`;
- Mereka menyiarkan `Blok B+1` ke node jaringan;
- Karena node-node tersebut mengikuti rantai terpanjang (dengan akumulasi pekerjaan paling banyak), mereka akan memperkirakan bahwa `Rantai B` adalah rantai yang harus diikuti;
- Mereka akan meninggalkan `Blok A` yang tidak lagi menjadi bagian dari rantai utama. Dengan demikian, blok ini menjadi blok yang sudah tidak terpakai.

![](../../dictionnaire/assets/9.webp)

> dalam bahasa Inggris, ini disebut sebagai "Stale Block". Dalam bahasa Prancis, ini juga bisa disebut "bloc périmé" atau "bloc abandonné". Meskipun saya tidak setuju dengan penggunaan ini, beberapa pengguna bitcoin menggunakan istilah "bloc orphelin" untuk merujuk pada apa yang sebenarnya merupakan blok usang