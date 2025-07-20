---
term: GOSSIP
---

Gossip adalah algoritma terdistribusi _peer-to-peer_ (P2P) untuk menyebarkan informasi secara epidemik ke semua agen jaringan. Untuk Bitcoin, Lightning dan sistem terdistribusi lainnya, protokol ini memungkinkan _Global State_ dari node dipertukarkan dan disinkronkan hanya dalam beberapa siklus. Setiap node menyebarkan informasi ke satu atau lebih tetangga acak atau non-acak, yang pada gilirannya menyebarkan informasi ke tetangga lain, dan seterusnya, sampai keadaan tersinkronisasi secara global tercapai.


Dalam Lightning, gosip adalah protokol komunikasi antar node untuk berbagi informasi tentang keadaan dan topologi jaringan saat ini. Protokol gosip memungkinkan node untuk mengetahui status dinamis dari saluran pembayaran dan node lainnya, untuk memfasilitasi perutean transaksi di seluruh jaringan tanpa memerlukan koneksi langsung di antara semua node.
