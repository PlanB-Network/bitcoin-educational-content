---
term: YATIM PIATU

---
Secara teoritis, blok anak yatim mengacu pada blok valid yang diterima oleh node yang belum memperoleh blok induk, yaitu blok sebelumnya dalam rantai. Walaupun valid, blok ini tetap terisolasi secara lokal sebagai anak yatim.

Akan tetapi, dalam penggunaan umum, istilah "orphan block" sering kali merujuk kepada sebuah blok tanpa anak: sebuah blok yang valid, tetapi tidak disimpan dalam rantai utama Bitcoin. Hal ini terjadi ketika dua penambang menemukan sebuah blok yang valid pada ketinggian rantai yang sama dalam waktu yang singkat dan menyiarkannya melalui jaringan. Node akhirnya hanya memilih satu blok untuk dimasukkan ke dalam rantai, berdasarkan prinsip rantai dengan akumulasi pekerjaan terbanyak, membuat blok lainnya menjadi "yatim piatu"

![](../../dictionnaire/assets/9.webp)

> ► *Secara pribadi, saya lebih suka menggunakan istilah "blok yatim piatu" untuk membicarakan blok tanpa induk dan istilah "blok basi" untuk menyebut blok yang tidak memiliki anak. Menurut saya ini lebih logis dan mudah dimengerti, meskipun sebagian besar pengguna bitcoin tidak mengikuti penggunaan ini