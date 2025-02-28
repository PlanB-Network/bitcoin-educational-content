---
term: BIP156

---
Proposal, yang dikenal sebagai Dandelion, yang bertujuan untuk meningkatkan privasi perutean transaksi dalam jaringan Bitcoin untuk melawan deanonimisasi. Dalam operasi standar Bitcoin, transaksi langsung disiarkan ke beberapa node. Jika seorang pengamat dapat melihat setiap transaksi yang disiarkan oleh setiap node dalam jaringan, mereka dapat berasumsi bahwa node pertama yang mengirimkan sebuah transaksi juga merupakan node asal dari transaksi tersebut, dan oleh karena itu transaksi tersebut berasal dari operator node tersebut. Fenomena ini berpotensi memungkinkan pengamat untuk menghubungkan transaksi, yang biasanya anonim, dengan alamat IP.

Tujuan dari BIP156 adalah untuk mengatasi masalah ini. Untuk melakukan ini, ia memperkenalkan fase tambahan dalam siaran untuk menjaga anonimitas sebelum disebarkan ke publik. Dengan demikian, Dandelion pertama-tama menggunakan fase "stem" di mana transaksi dikirim melalui jalur node secara acak, sebelum disiarkan ke seluruh jaringan dalam fase "fluff". Stem dan fluff adalah referensi untuk perilaku penyebaran transaksi melalui jaringan, menyerupai bentuk dandelion (*a dandelion* dalam bahasa Inggris).

Metode perutean ini mengaburkan jejak yang mengarah kembali ke simpul sumber, sehingga sulit untuk melacak transaksi melalui jaringan kembali ke asalnya. Dengan demikian, Dandelion meningkatkan privasi dengan membatasi kemampuan lawan untuk mendeanonimisasi jaringan. Metode ini bahkan lebih efektif ketika transaksi melintasi fase "batang" sebuah node yang mengenkripsi komunikasi jaringannya, seperti dengan Tor atau *P2P Transport V2*. BIP156 belum ditambahkan ke Bitcoin Core.

![](../../dictionnaire/assets/36.webp)