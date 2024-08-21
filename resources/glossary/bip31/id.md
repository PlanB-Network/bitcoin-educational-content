---
term: BIP31
---

Proposal yang bertujuan untuk meningkatkan mekanisme manajemen jaringan oleh node-node Bitcoin. Sebelum BIP31, node-node Bitcoin tidak memiliki cara langsung untuk mengetahui apakah rekan-rekannya masih terhubung, beroperasi, dan tidak kelebihan beban. BIP31 memperkenalkan penggunaan pesan `pong`, sebagai respons terhadap pesan `ping`, yang memungkinkan pemeriksaan aktif koneksi antar node.