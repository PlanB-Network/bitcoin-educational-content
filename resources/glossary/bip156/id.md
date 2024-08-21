---
term: BIP156
---

Proposal, yang dikenal sebagai Dandelion, bertujuan untuk meningkatkan privasi routing transaksi dalam jaringan Bitcoin untuk melawan deanonymization. Dalam operasi standar Bitcoin, transaksi langsung disiarkan ke beberapa node. Jika pengamat dapat melihat setiap transaksi yang diteruskan oleh setiap node di jaringan, mereka mungkin mengasumsikan bahwa node pertama yang mengirim transaksi juga merupakan node asal dari transaksi tersebut, dan oleh karena itu berasal dari operator node tersebut. Fenomena ini berpotensi memungkinkan pengamat untuk menghubungkan transaksi, yang biasanya anonim, dengan alamat IP.

Tujuan dari BIP156 adalah untuk mengatasi masalah ini. Untuk melakukan ini, ia memperkenalkan fase tambahan dalam penyiaran untuk mempertahankan anonimitas sebelum propagasi publik. Dengan demikian, Dandelion pertama menggunakan fase "batang" di mana transaksi dikirim melalui jalur acak dari node, sebelum disiarkan ke seluruh jaringan dalam fase "bulu". Batang dan bulu adalah referensi ke perilaku propagasi transaksi melalui jaringan, menyerupai bentuk dandelion (*a dandelion* dalam bahasa Inggris).

Metode routing ini menyamarkan jejak yang mengarah kembali ke node sumber, membuatnya sulit untuk melacak transaksi melalui jaringan kembali ke asalnya. Dandelion dengan demikian meningkatkan privasi dengan membatasi kemampuan musuh untuk deanonymize jaringan. Metode ini menjadi lebih efektif ketika transaksi melintasi selama fase "batang" sebuah node yang mengenkripsi komunikasi jaringannya, seperti dengan Tor atau *P2P Transport V2*. BIP156 belum ditambahkan ke Bitcoin Core.

![](../../dictionnaire/assets/36.png)