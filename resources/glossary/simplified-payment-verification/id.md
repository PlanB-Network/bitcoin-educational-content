---
term: SIMPLIFIED PAYMENT VERIFICATION

---
Metode yang memungkinkan klien ringan untuk memverifikasi transaksi Bitcoin tanpa mengunduh seluruh _blockchain_. Sebuah node yang menggunakan SPV hanya mengunduh _header_ blok, yang jauh lebih ringan daripada blok lengkap. Ketika perlu memverifikasi transaksi, node SPV meminta bukti Merkle dari node penuh untuk mengonfirmasi bahwa transaksi tersebut termasuk dalam blok tertentu. Pendekatan ini efisien untuk perangkat dengan sumber daya yang terbatas, seperti _smartphone_, akan tetapi pendekatan ini menyiratkan ketergantungan pada node penuh, yang dapat mengurangi keamanan dan meningkatkan kepercayaan yang dibutuhkan.

> ► *Singkatan "SPV" sering digunakan untuk merujuk pada metode ini.*
