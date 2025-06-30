---
term: SPV (NODE RINGAN)

---
Sebuah node SPV (*Simple Payment Verification*), terkadang disebut "_light node"_, adalah sebuah klien ringan dari sebuah node Bitcoin yang mengizinkan pengguna untuk memvalidasi transaksi tanpa harus menyimpan seluruh _blockchain_. Sebagai gantinya, sebuah node SPV hanya menyimpan _header_ blok dan mendapatkan informasi mengenai transaksi tertentu dengan menanyakan seluruh node jika diperlukan. Prinsip verifikasi ini dimungkinkan oleh struktur transaksi dalam blok Bitcoin, yang diatur dalam akumulator kriptografi (Pohon Merkle).

Pendekatan ini menguntungkan untuk perangkat dengan sumber daya yang terbatas, seperti ponsel. Akan tetapi, node SPV bergantung pada node penuh untuk ketersediaan informasi, yang mengimplikasikan tingkat kepercayaan tambahan dan, akibatnya, keamanan yang lebih rendah dibandingkan dengan node penuh. Node SPV tidak dapat memvalidasi transaksi secara mandiri, akan tetapi mereka dapat memverifikasi apakah sebuah transaksi termasuk dalam sebuah blok dengan melihat bukti-bukti Merkle.
