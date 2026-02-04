---
term: Indeks blok

definition: Struktur LevelDB dalam Bitcoin Core yang mengatalogkan metadata dan lokasi blok.
---
Sebuah struktur data LevelDB di Bitcoin Core yang membuat katalog metadata tentang semua blok. Setiap entri dalam indeks ini memberikan detail seperti pengenal blok, ketinggiannya dalam _blockchain_, penunjuk ke blok dalam database, dan metadata lainnya. Pengindeksan ini memungkinkan pengguna untuk menemukan blok yang tersimpan dalam memori dengan cepat.
