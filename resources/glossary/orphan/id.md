---
term: ORPHAN

---
Secara teoritis, _orphan block_ mengacu pada blok valid yang diterima oleh node yang belum memperoleh blok induk, yaitu blok sebelumnya dalam rantai. Walaupun valid, blok ini tetap terisolasi secara lokal sebagai _orphan_.

Akan tetapi, dalam penggunaan umum, istilah "_orphan block_" sering kali merujuk kepada sebuah blok tanpa anak: sebuah blok yang valid, tetapi tidak disimpan dalam rantai utama Bitcoin. Hal ini terjadi ketika dua penambang menemukan sebuah blok yang valid pada ketinggian rantai yang sama dalam waktu yang singkat dan mempublikasikan melalui jaringan. Node akhirnya hanya memilih satu blok untuk dimasukkan ke dalam rantai, berdasarkan prinsip rantai dengan akumulasi pekerjaan terbanyak, membuat blok lainnya menjadi "_orphan block_"

![](../../dictionnaire/assets/9.webp)

> ► *Secara pribadi, saya lebih suka menggunakan istilah "orphan block" untuk merujuk blok tanpa induk dan istilah "stale block" untuk menyebut blok yang tidak memiliki anak. Menurut saya ini lebih logis dan mudah dimengerti, meskipun sebagian besar pengguna bitcoin tidak mengikuti penggunaan ini.*
