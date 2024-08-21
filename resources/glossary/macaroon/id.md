---
term: MACAROON
---

Sebuah mekanisme autentikasi yang dirancang untuk mengamankan akses ke layanan pada sistem terdistribusi. Macaroon secara khusus digunakan pada Lightning untuk mengautentikasi pengguna ketika mereka mengakses layanan yang didelegasikan. Sebagai contoh, dengan sebuah node Lightning, adalah mungkin untuk menghasilkan sebuah macaroon yang memberi otorisasi untuk eksekusi transaksi dari smartphone Anda melalui node remote Anda. Tidak seperti cookie, macaroon memiliki keuntungan dapat divalidasi secara kriptografis oleh penerbit atau didelegasikan untuk verifikasi.