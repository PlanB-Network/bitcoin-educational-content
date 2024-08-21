---
term: DANDELION
---

Sebuah proposal yang bertujuan untuk meningkatkan privasi dari routing transaksi dalam jaringan Bitcoin untuk mengatasi deanonymization. Dalam operasi standar Bitcoin, transaksi langsung disiarkan ke beberapa node. Fenomena ini berpotensi memungkinkan pengamat untuk menghubungkan transaksi, yang biasanya anonim, dengan alamat IP. Tujuan dari BIP156 adalah untuk mengatasi masalah ini. Untuk melakukan ini, ia memperkenalkan fase tambahan dalam proses penyiaran untuk mempertahankan anonimitas sebelum propagasi publik. Dengan demikian, Dandelion pertama menggunakan fase "stem" di mana transaksi dikirim melalui jalur acak dari node, sebelum disiarkan ke seluruh jaringan dalam fase "fluff". Stem dan fluff adalah referensi ke perilaku propagasi transaksi melalui jaringan, menyerupai bentuk dari dandelion. Metode routing ini menyamarkan jejak yang mengarah kembali ke node sumber, membuatnya sulit untuk melacak transaksi melalui jaringan kembali ke asalnya.

![](../../dictionnaire/assets/36.png)