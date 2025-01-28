---
term: BENIH DNS

---
Titik koneksi awal untuk node Bitcoin baru yang bergabung dengan jaringan. Seeds ini, yang sebenarnya adalah server DNS tertentu, memiliki alamat yang tertanam secara permanen di dalam kode Bitcoin Core. Ketika sebuah node baru dimulai, node tersebut akan menghubungi server-server ini untuk mendapatkan daftar alamat IP secara acak dari node Bitcoin yang aktif. Node baru tersebut kemudian dapat membuat koneksi dengan node-node dalam daftar ini untuk mendapatkan informasi yang dibutuhkan untuk melakukan Initial Block Download (IBD) dan melakukan sinkronisasi dengan rantai yang memiliki akumulasi pekerjaan paling banyak. Pada tahun 2024, berikut ini adalah daftar Bitcoin Core DNS dan individu yang bertanggung jawab atas pemeliharaannya (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-daftar-dari-simpul-p2p.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

DNS seed adalah metode kedua, dalam urutan prioritas, untuk membuat koneksi pada sebuah node Bitcoin. Metode pertama melibatkan penggunaan file peers.dat yang dibuat oleh node itu sendiri. File ini secara alami kosong dalam kasus node baru, kecuali jika pengguna telah memodifikasinya secara manual.

> ► *Catatan, seed DNS tidak boleh disamakan dengan "seed node," yang merupakan cara ketiga untuk membuat koneksi.*