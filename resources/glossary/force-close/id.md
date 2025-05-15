---
term: PENUTUPAN PAKSA
---

Mekanisme penutupan saluran Lightning yang tidak kooperatif. Ketika dua pengguna membuka saluran dengan Multisig 2/2, masing-masing dapat menutup saluran secara sepihak dengan menyiarkan Commitment Transaction terakhir yang telah ditandatangani, untuk memulihkan bitcoin onchain mereka. Hal ini dikenal dengan istilah "force close".


Metode ini biasanya digunakan jika salah satu peserta tidak lagi merespons, atau jika penutupan saluran secara kooperatif tidak mungkin dilakukan. Jika penutupan paksa dapat dihindari, itu yang terbaik, karena membutuhkan waktu lebih lama untuk memulihkan dana onchain dan bisa jauh lebih mahal dalam hal biaya.


Dalam force close, salah satu dari dua pengguna menyiarkan Commitment Transaction, yang mencerminkan status terakhir yang diketahui dari saluran Lightning. Kemudian ada penguncian waktu sebelum bitcoin dapat diambil di dalam chain, memberikan waktu kepada pihak lain untuk memverifikasi bahwa transaksi tersebut sesuai dengan status channel terbaru. Jika seorang pengguna mencoba menipu dengan menerbitkan Commitment Transaction yang sudah kadaluarsa, pihak lain dapat menggunakan rahasia pencabutan untuk menghukum si penipu dan memulihkan semua dana di dalam channel.