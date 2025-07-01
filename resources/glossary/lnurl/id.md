---
term: LNURL
---

Protokol komunikasi yang menetapkan serangkaian fitur yang dirancang untuk menyederhanakan interaksi antara node Lightning dan klien, serta aplikasi pihak ketiga. Protokol ini didasarkan pada HTTP dan memungkinkan tautan dibuat untuk berbagai operasi, seperti permintaan pembayaran, permintaan penarikan, atau fungsi lain yang meningkatkan pengalaman pengguna. Setiap LNURL adalah URL yang dikodekan dalam bech32 dengan awalan `lnurl`, yang, ketika dipindai, memicu serangkaian tindakan otomatis pada dompet Lightning.


Sebagai contoh, LNURL-withdraw (LUD-03) memungkinkan Anda menarik dana dari sebuah layanan dengan memindai kode QR, tanpa harus membuat _invoice_ secara manual. Atau LNURL-auth (LUD-04) memungkinkan Anda terhubung ke layanan _online_ menggunakan kunci privat pada dompet Lightning, bukan kata sandi.
