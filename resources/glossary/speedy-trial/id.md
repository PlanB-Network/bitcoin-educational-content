---
term: UJI COBA CEPAT

---
_Speedy trial_ atau uji coba cepat adalah metode aktivasi _soft fork_ yang awalnya dikonsepsualiasi untuk Taproot pada awal tahun 2021 oleh David A. Harding berdasarkan ide dari Russell O'Connor. Prinsipnya adalah menggunakan metode BIP8 dengan parameter `LOT` yang disetel ke `false`, sekaligus mengurangi periode aktivasi menjadi hanya 3 bulan. Periode pemungutan suara yang dipersingkat ini memungkinkan verifikasi persetujuan penambang dengan cepat. Jika ambang batas persetujuan yang diperlukan tercapai selama salah satu periode, s_oft fork_ akan dikunci. _Soft fork_ akan diaktifkan beberapa bulan kemudian, sehingga memberikan penambang waktu yang diperlukan untuk memperbarui perangkat lunak mereka.

Keberhasilan metode ini untuk Taproot, yang telah mendapatkan konsensus yang luas di dalam komunitas Bitcoin, tidak menjamin keefektifannya untuk semua pembaruan. Walaupun metode _Speedy Trial_ memungkinkan aktivasi yang lebih cepat, beberapa pengembang mengungkapkan kekhawatirannya mengenai penggunaannya di masa depan. Mereka khawatir metode ini dapat menyebabkan terjadinya pergantian _soft fork_ yang terlalu cepat, yang berpotensi mengancam stabilitas dan keamanan protokol Bitcoin. Dibandingkan dengan BIP8 dengan parameter `LOT=true`, metode _Speedy Trial_ tidak terlalu mengancam para penambang. Tidak ada UASF yang direncanakan secara otomatis. Metode aktivasi ini belum diformalkan dalam BIP.

> *Istilah "Speedy Trial" dipinjam dari terminologi hukum yang menunjukkan "persidangan yang dipercepat". Hal ini mengacu pada fakta bahwa proposal pengebmbanga dengan cepat dibawa ke hadapan pengadilan para penambang, untuk menentukan niat mereka.*
