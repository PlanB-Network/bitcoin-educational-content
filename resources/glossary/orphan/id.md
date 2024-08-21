---
term: ORPHAN
---

Secara teoretis, blok yatim (orphan block) merujuk pada blok yang valid yang diterima oleh sebuah node tetapi belum mendapatkan blok induknya, yaitu blok sebelumnya dalam rantai. Meskipun valid, blok ini tetap terisolasi secara lokal sebagai blok yatim.

Namun, dalam penggunaan umum, istilah "blok yatim" sering merujuk pada blok tanpa anak: blok yang valid, tetapi tidak dipertahankan dalam rantai utama Bitcoin. Hal ini terjadi ketika dua penambang menemukan blok yang valid pada tinggi rantai yang sama dalam periode waktu yang singkat dan menyiarkannya melalui jaringan. Node akhirnya hanya memilih satu blok untuk dimasukkan dalam rantai, berdasarkan prinsip rantai dengan pekerjaan terakumulasi terbanyak, membuat yang lainnya menjadi "yatim."

![](../../dictionnaire/assets/9.png)

> ► *Secara pribadi, saya lebih suka menggunakan istilah "blok yatim" untuk berbicara tentang blok tanpa induk dan istilah "blok basi" untuk merujuk pada blok yang tidak memiliki anak. Saya merasa ini lebih logis dan mudah dipahami, meskipun mayoritas pengguna Bitcoin tidak mengikuti penggunaan ini.*