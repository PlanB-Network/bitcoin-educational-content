---
term: SETTINGS.JSON

---
File yang digunakan di Bitcoin Core untuk menyimpan pengaturan antarmuka pengguna grafis (GUI). File ini menyimpan informasi mengenai konfigurasi pengguna, seperti contohnya dompet yang terbuka. Ketika Bitcoin Core dimulai ulang, file ini memungkinkan pembukaan kembali wallet yang aktif secara otomatis sebelum aplikasi ditutup. Jika sebuah wallet ditutup melalui GUI, maka wallet tersebut juga akan dihapus dari file ini, dan oleh karena itu, wallet tersebut tidak akan dibuka kembali secara otomatis saat aplikasi dijalankan kembali.