---
term: BTCPay Server

definition: Prosesor pembayaran sumber terbuka yang memungkinkan penerimaan pembayaran bitcoin tanpa perantara.
---

⚠️ **Peringatan keamanan kritis (7 Agustus 2026):** sebuah kerentanan kritis yang memengaruhi BTCPay Server sedang dieksploitasi secara aktif dan dapat menyebabkan hilangnya dana. Segera perbarui instance Anda ke **version 2.4.2** melalui `Admin Dashboard > Server > Maintenance > Update`, lalu pastikan bagian footer menampilkan `2.4.2`. Jika Anda tidak dapat memperbarui saat itu juga, matikan BTCPay Server Anda. Setelah diperbarui, Anda juga harus benar-benar memperbarui macaroons dan `macaroons.db` Anda, benar-benar memperbarui string autentikasi dari backend Lightning lainnya, dan, jika Anda membuat dompet on-chain panas (hot wallet) di dalam BTCPay Server, pindahkan dana tersebut dan buat ulang dompetnya. Para integrator juga harus memperbarui NBXplorer ke version 2.6.10. Sumber: [Catatan rilis BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server adalah prosesor pembayaran sumber terbuka yang memungkinkan pedagang dan pengguna untuk menerima pembayaran Bitcoin tanpa bergantung pada pihak ketiga untuk pemrosesan transaksi. Diluncurkan pada tahun 2017, BTCPay Server menyediakan solusi terintegrasi pembayaran Bitcoin untuk situs _e-commerce_, dengan fitur-fitur canggih seperti dukungan untuk dompet perangkat keras, alat penagihan dan akuntansi, serta kompatibilitas dengan Jaringan Lightning. Pengembangannya diprakarsai oleh Nicolas Dorier, sebagai tanggapan atas tindakan Bitpay yang menurutnya telah menyesatkan para penggunanya dengan mendorong mereka ke arah adopsi SegWit2x, yang secara keliru dianggap sebagai Bitcoin yang "benar". Penentangan ini dikemas dalam tweet yang sekarang terkenal dari Nicolas Dorier pada bulan Agustus 2017:

> "Ini bohong, kepercayaanku padamu telah hancur, aku akan membuatmu usang".

