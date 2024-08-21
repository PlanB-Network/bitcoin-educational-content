---
term: SETTINGS.JSON
---

File yang digunakan dalam Bitcoin Core untuk menyimpan pengaturan dari antarmuka pengguna grafis (GUI). File ini menyimpan informasi tentang konfigurasi pengguna, seperti dompet yang terbuka sebagai contoh. Ketika Bitcoin Core dijalankan kembali, file ini memungkinkan pembukaan otomatis dompet yang aktif sebelum aplikasi ditutup. Jika sebuah dompet ditutup melalui GUI, dompet tersebut juga akan dihapus dari file ini, dan oleh karena itu, dompet tersebut tidak akan dibuka secara otomatis pada saat start berikutnya.