---
term: TRANSPORTASI P2P V2

---
Versi baru dari protokol transport P2P Bitcoin yang menggabungkan enkripsi oportunistik untuk meningkatkan privasi dan keamanan komunikasi antar node. Peningkatan ini bertujuan untuk mengatasi beberapa masalah dengan versi dasar protokol P2P, terutama dengan membuat data yang dipertukarkan tidak dapat dibedakan oleh pengamat pasif (seperti penyedia layanan internet), sehingga mengurangi risiko penyensoran dan serangan melalui pendeteksian pola tertentu dalam paket data.

Enkripsi yang diimplementasikan tidak menyertakan autentikasi untuk menghindari penambahan kompleksitas yang tidak perlu dan untuk tidak mengorbankan sifat tanpa izin dari koneksi jaringan. Protokol transport P2P yang baru ini menawarkan keamanan yang lebih baik terhadap serangan pasif dan membuat serangan aktif secara signifikan lebih mahal dan dapat dideteksi (terutama serangan MITM). Pengenalan aliran data acak semu mempersulit tugas penyerang yang ingin menyensor atau memanipulasi komunikasi.

P2P Transport V2 disertakan sebagai opsi (dinonaktifkan secara default) pada versi 26.0 Bitcoin Core, yang digunakan pada bulan Desember 2023. Opsi ini dapat diaktifkan dengan opsi `v2transport=1` di file konfigurasi.