---
term: ATURAN STANDARDISASI
---

Aturan standardisasi adalah aturan yang diadopsi secara individu oleh setiap node Bitcoin, selain dari aturan konsensus, untuk mendefinisikan struktur transaksi yang belum dikonfirmasi yang diterimanya ke dalam mempoolnya dan disiarkan ke peer-nya. Aturan-aturan ini oleh karena itu dikonfigurasi dan dieksekusi secara lokal oleh setiap node dan dapat bervariasi dari satu node ke node lainnya. Aturan-aturan ini berlaku secara eksklusif untuk transaksi yang belum dikonfirmasi. Oleh karena itu, sebuah node hanya akan menerima transaksi yang dianggap non-standar jika sudah termasuk dalam blok yang valid.

Diketahui bahwa mayoritas node meninggalkan konfigurasi default seperti yang ditetapkan dalam Bitcoin Core, dengan demikian menciptakan keseragaman aturan standardisasi di seluruh jaringan. Transaksi yang, meskipun sesuai dengan aturan konsensus, tidak mematuhi aturan standardisasi ini, akan mengalami kesulitan untuk disiarkan di seluruh jaringan. Namun, masih bisa dimasukkan dalam blok yang valid jika mencapai seorang penambang. Dalam prakteknya, transaksi-transaksi ini, yang disebut sebagai "non-standar," seringkali ditransmisikan langsung ke penambang melalui sarana eksternal di luar jaringan peer-to-peer Bitcoin. Ini seringkali menjadi satu-satunya cara untuk mengonfirmasi jenis transaksi ini.

Sebagai contoh, transaksi yang tidak mengalokasikan biaya sama sekali adalah valid menurut aturan konsensus dan non-standar karena kebijakan default dari Bitcoin Core untuk parameter `minRelayTxFee` adalah `0.00001` (dalam BTC/kB).

> ► *Istilah "aturan mempool" juga terkadang digunakan untuk merujuk pada aturan standardisasi.*