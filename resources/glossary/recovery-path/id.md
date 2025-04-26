---
term: JALUR PEMULIHAN

---
Dalam perangkat lunak dompet yang menggunakan Miniscript, seperti Liana contohnya, jalur pemulihan mengacu pada set kunci yang hanya dapat beroperasi setelah periode tidak aktif yang ditentukan dalam skrip yang mengunci bitcoin (timelock). Jalur pemulihan hanya dapat digunakan setelah timelock kedaluwarsa, sehingga menawarkan sebuah metode untuk memulihkan dana ketika jalur utama tidak tersedia. Pertimbangkan contoh skrip yang menggabungkan 2 kunci yang berbeda: kunci A, yang mengotorisasi pengeluaran bitcoin secara langsung, dan kunci B, yang mengizinkan pengeluaran setelah penundaan yang ditentukan oleh penguncian waktu sebesar 52.560 blok. Dalam contoh ini, kunci A berasal dari jalur utama, sedangkan kunci B berasal dari jalur pemulihan.