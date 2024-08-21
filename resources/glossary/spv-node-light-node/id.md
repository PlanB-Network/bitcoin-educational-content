---
term: SPV NODE (LIGHT NODE)
---

Sebuah node SPV (*Simple Payment Verification*), yang terkadang disebut "light node," adalah klien ringan dari sebuah node Bitcoin yang memungkinkan pengguna untuk memvalidasi transaksi tanpa harus menyimpan seluruh blockchain. Sebaliknya, sebuah node SPV hanya menyimpan header blok dan memperoleh informasi tentang transaksi tertentu dengan menanyakan kepada full node ketika diperlukan. Prinsip verifikasi ini dimungkinkan oleh struktur transaksi dalam blok Bitcoin, yang disusun dalam sebuah akumulator kriptografis (Merkle Tree).

Pendekatan ini menguntungkan untuk perangkat dengan sumber daya terbatas, seperti ponsel. Namun, node SPV bergantung pada full node untuk ketersediaan informasi, yang mengimplikasikan tingkat kepercayaan tambahan dan, akibatnya, keamanan yang lebih rendah dibandingkan dengan full node. Node SPV tidak dapat memvalidasi transaksi secara mandiri, tetapi mereka dapat memverifikasi apakah sebuah transaksi termasuk dalam sebuah blok dengan berkonsultasi pada bukti Merkle.