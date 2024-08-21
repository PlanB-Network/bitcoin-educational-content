---
term: CHAIN CODE
---

Dalam konteks derivasi deterministik hierarkis (HD) dari dompet Bitcoin, chain code adalah nilai garam kriptografi 256-bit yang digunakan untuk menghasilkan kunci anak dari kunci induk, sesuai dengan standar BIP32. Chain code digunakan bersama dengan kunci induk dan indeks anak untuk menghasilkan secara deterministik sepasang kunci baru (kunci privat dan kunci publik) tanpa mengungkapkan kunci induk atau kunci anak yang lain yang telah diturunkan.

Oleh karena itu, terdapat chain code unik untuk setiap pasangan kunci. Chain code diperoleh baik dengan meng-hash benih dompet dan mengambil setengah bagian bit yang kanan. Dalam kasus ini, ini disebut sebagai master chain code, yang terkait dengan master kunci privat. Alternatifnya, dapat diperoleh dengan meng-hash kunci induk dengan chain code induknya dan sebuah indeks, kemudian menyimpan bit-bit yang kanan. Ini kemudian disebut sebagai child chain code.

Tidak mungkin untuk menurunkan kunci tanpa mengetahui chain code yang terkait dengan setiap pasangan induk. Ini memperkenalkan data pseudo-acak ke dalam proses derivasi untuk memastikan bahwa generasi kunci kriptografi tetap tidak dapat diprediksi oleh penyerang sambil tetap deterministik bagi pemegang dompet.

> ► *Dalam bahasa Inggris, "code de chaîne" disebut "chain code", dan "code de chaîne maître" disebut "master chain code".*