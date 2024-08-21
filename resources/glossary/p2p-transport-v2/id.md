---
term: P2P TRANSPORT V2
---

Versi baru dari protokol transportasi P2P Bitcoin yang menggabungkan enkripsi oportunis untuk meningkatkan privasi dan keamanan komunikasi antar node. Peningkatan ini bertujuan untuk mengatasi beberapa masalah dengan versi dasar dari protokol P2P, terutama dengan membuat data yang ditukar tidak dapat dibedakan oleh pengamat pasif (seperti penyedia layanan internet), sehingga mengurangi risiko sensor dan serangan melalui deteksi pola spesifik dalam paket data.

Enkripsi yang diimplementasikan tidak mencakup autentikasi untuk menghindari penambahan kompleksitas yang tidak perlu dan untuk tidak mengompromikan sifat tanpa izin dari koneksi jaringan. Protokol transportasi P2P baru ini tetap menawarkan keamanan yang lebih baik terhadap serangan pasif dan membuat serangan aktif secara signifikan lebih mahal dan terdeteksi (terutama serangan MITM). Pengenalan aliran data pseudo-acak mempersulit tugas bagi penyerang yang ingin mensensor atau memanipulasi komunikasi.

P2P Transport V2 disertakan sebagai opsi (dinonaktifkan secara default) dalam versi 26.0 dari Bitcoin Core, yang dikerahkan pada Desember 2023. Ini dapat diaktifkan dengan opsi `v2transport=1` dalam file konfigurasi.