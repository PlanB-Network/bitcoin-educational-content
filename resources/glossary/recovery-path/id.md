---
term: RECOVERY PATH

---
Dalam perangkat lunak dompet yang menggunakan _Miniscript_, seperti Liana contohnya, _recovery path_ mengacu pada set kunci yang hanya dapat beroperasi setelah periode tidak aktif yang ditentukan dalam skrip yang mengunci bitcoin (_timelock_). _Recovery path_ hanya dapat digunakan setelah _timelock_ sudah kedaluwarsa, sehingga menawarkan sebuah metode untuk memulihkan dana ketika jalur utama tidak tersedia. Pertimbangkan contoh skrip yang menggabungkan 2 kunci yang berbeda: kunci A, yang mengizinkan pengeluaran bitcoin secara langsung, dan kunci B, yang mengizinkan pengeluaran setelah penundaan yang ditentukan oleh penguncian waktu sebesar 52.560 blok. Dalam contoh ini, kunci A berasal dari jalur utama, sedangkan kunci B berasal dari jalur pemulihan.
