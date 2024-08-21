---
term: DNS SEEDS
---

Titik koneksi awal untuk node Bitcoin baru yang bergabung dengan jaringan. Seed ini, yang sebenarnya adalah server DNS spesifik, memiliki alamat mereka yang secara permanen tertanam dalam kode Bitcoin Core. Ketika sebuah node baru dimulai, node tersebut menghubungi server-server ini untuk mendapatkan daftar acak alamat IP dari node Bitcoin yang diduga aktif. Node baru kemudian dapat menjalin koneksi dengan node-node dalam daftar ini untuk mendapatkan informasi yang diperlukan untuk melakukan Initial Block Download (IBD) dan sinkronisasi dengan rantai yang memiliki pekerjaan terakumulasi terbanyak. Per tahun 2024, berikut adalah daftar DNS seeds Bitcoin Core dan individu yang bertanggung jawab atas pemeliharaannya (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS seeds adalah metode kedua, dalam urutan prioritas, bagi sebuah node Bitcoin untuk menjalin koneksi. Metode pertama melibatkan penggunaan file peers.dat yang dibuat oleh node itu sendiri. File ini secara alami kosong dalam kasus node baru, kecuali pengguna telah memodifikasinya secara manual.

> ► *Catatan, DNS seeds tidak boleh dikacaukan dengan "seed nodes," yang merupakan cara ketiga untuk menjalin koneksi.*