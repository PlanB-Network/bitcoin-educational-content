---
term: HORODATAGE
---

Penandaan waktu, atau "Timestamp" dalam bahasa Inggris, adalah mekanisme untuk mengaitkan tanda waktu yang tepat dengan suatu peristiwa, data, atau pesan. Dalam konteks umum sistem komputer, penandaan waktu digunakan untuk menentukan urutan kronologis operasi dan untuk memverifikasi integritas data dari waktu ke waktu.


Dalam kasus khusus Bitcoin, stempel waktu digunakan untuk menetapkan kronologi transaksi dan blok. Setiap blok dalam Blockchain berisi Timestamp yang menunjukkan perkiraan waktu pembuatannya. Satoshi Nakamoto bahkan berbicara tentang "server Timestamp", dalam White Paper-nya, untuk menggambarkan apa yang kita sebut sebagai "Blockchain" saat ini. Peran timestamping pada Bitcoin adalah untuk menentukan kronologi transaksi, sehingga, tanpa campur tangan otoritas pusat, dapat ditentukan transaksi mana yang lebih dulu masuk. Mekanisme ini memungkinkan setiap pengguna untuk memverifikasi tidak adanya transaksi di masa lalu, dan dengan demikian mencegah pengguna yang jahat untuk melakukan pengeluaran ganda. Mekanisme ini dibenarkan oleh Satoshi Nakamoto dalam White Paper-nya dengan kalimat yang terkenal: "*Standar ini didasarkan pada waktu Unix, yang mewakili jumlah total detik yang telah berlalu sejak 1 Januari 1970.


> ► *Stempel waktu blok relatif fleksibel pada Bitcoin, karena agar Timestamp dianggap valid, hanya perlu lebih besar dari waktu rata-rata 11 blok sebelumnya (MTP) dan lebih kecil dari median waktu yang dikembalikan oleh node (waktu yang disesuaikan jaringan) ditambah 2 jam