---
term: DANDELION

---
Sebuah proposal yang bertujuan untuk meningkatkan privasi perutean transaksi dalam jaringan Bitcoin untuk melawan deanonimisasi. Dalam operasi standar Bitcoin, transaksi segera disiarkan ke beberapa node. Fenomena ini berpotensi memungkinkan pengamat untuk menghubungkan transaksi, yang biasanya anonim, dengan alamat IP. Tujuan dari BIP156 adalah untuk mengatasi masalah ini. Untuk melakukan ini, BIP156 memperkenalkan sebuah fase tambahan dalam proses broadcast untuk menjaga anonimitas sebelum disebarkan ke publik. Dengan demikian, Dandelion pertama-tama menggunakan fase "stem" di mana transaksi dikirim melalui jalur node secara acak, sebelum disiarkan ke seluruh jaringan dalam fase "fluff". Stem dan fluff adalah referensi untuk perilaku penyebaran transaksi melalui jaringan, menyerupai bentuk dandelion. Metode perutean ini mengaburkan jejak yang mengarah kembali ke node sumber, sehingga menyulitkan untuk melacak transaksi melalui jaringan kembali ke asalnya.

![](../../dictionnaire/assets/36.webp)