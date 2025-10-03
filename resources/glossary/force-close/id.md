---
term: PENUTUPAN PAKSA
---

Mekanisme penutupan saluran Lightning yang tidak kooperatif. Ketika dua pengguna membuka saluran dengan _Multisig_ 2/2, masing-masing dapat menutup saluran secara sepihak dengan mempublikasikan _Commitment Transaction_ terakhir yang telah ditandatangani, untuk memulihkan bitcoin onchain mereka. Hal ini dikenal dengan istilah "_force close_".


Metode ini biasanya digunakan jika salah satu peserta tidak lagi merespons, atau jika penutupan saluran secara kooperatif tidak mungkin dilakukan. Jika penutupan paksa dapat dihindari, itu yang terbaik, karena membutuhkan waktu lebih lama untuk memulihkan dana onchain dan bisa jauh lebih mahal dalam hal biaya.


Dalam _force close_, salah satu dari dua pengguna menyiarkan _Commitment Transaction_, yang mencerminkan status terakhir yang diketahui dari saluran Lightning. Kemudian ada penguncian waktu sebelum bitcoin dapat diambil di dalam _chain_, memberikan waktu kepada pihak lain untuk memverifikasi bahwa transaksi tersebut sesuai dengan status saluran Lightning terbaru. Jika seorang pengguna mencoba menipu dengan menerbitkan _Commitment Transaction_ yang sudah kadaluarsa, pihak lain dapat menggunakan rahasia pencabutan untuk menghukum si penipu dan memulihkan semua dana di dalam saluran.
