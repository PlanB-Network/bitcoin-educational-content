---
term: ATURAN STANDARDISASI

---
Aturan standardisasi diadopsi secara individual oleh setiap node Bitcoin, sebagai tambahan dari aturan konsensus, untuk mendefinisikan struktur transaksi yang belum dikonfirmasi yang diterimanya ke dalam mempool dan disiarkan ke rekan-rekannya. Aturan-aturan ini dikonfigurasikan dan dieksekusi secara lokal oleh setiap node dan dapat bervariasi dari satu node ke node lainnya. Aturan-aturan ini berlaku secara eksklusif untuk transaksi yang belum dikonfirmasi. Oleh karena itu, sebuah node hanya akan menerima transaksi yang dianggap tidak standar jika transaksi tersebut sudah termasuk dalam blok yang valid.

Tercatat bahwa mayoritas node meninggalkan konfigurasi default seperti yang ditetapkan dalam Bitcoin Core, sehingga menciptakan keseragaman aturan standardisasi di seluruh jaringan. Sebuah transaksi yang, meskipun sesuai dengan aturan konsensus, tidak mematuhi aturan standarisasi ini, akan mengalami kesulitan untuk disiarkan ke seluruh jaringan. Akan tetapi, transaksi tersebut masih dapat dimasukkan ke dalam blok yang valid jika mencapai penambang. Dalam praktiknya, transaksi-transaksi ini, yang disebut sebagai "non-standar", sering kali dikirim langsung ke penambang melalui sarana eksternal di luar jaringan peer-to-peer Bitcoin. Ini sering kali menjadi satu-satunya cara untuk mengonfirmasi jenis transaksi ini.

Sebagai contoh, transaksi yang tidak mengalokasikan biaya adalah sah menurut aturan konsensus dan tidak standar karena kebijakan default Bitcoin Core untuk parameter `minRelayTxFee` adalah `0.00001` (dalam BTC/kB).

> ► *Istilah "aturan mempool" terkadang juga digunakan untuk merujuk pada aturan standardisasi.*