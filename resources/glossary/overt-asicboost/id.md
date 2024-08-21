---
term: OVERT ASICBOOST
---

Versi terbuka dan transparan dari AsicBoost. AsicBoost adalah teknik optimisasi algoritmik yang digunakan dalam penambangan Bitcoin. Penambang yang menggunakan versi Overt memanipulasi bidang `nVersion` dari blok kandidat dan menggunakan modifikasi ini sebagai nonce tambahan. Metode ini meninggalkan bidang `Nonce` aktual dari blok tersebut tidak berubah selama setiap upaya hashing, dengan demikian mengurangi perhitungan yang diperlukan untuk setiap SHA256, dengan menjaga beberapa data tetap sama antar upaya. Versi ini dapat dideteksi secara publik dan tidak menyembunyikan modifikasinya dari sisanya jaringan, tidak seperti versi Covert dari AsicBoost.