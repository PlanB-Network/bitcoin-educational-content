---
term: SHA512

---
Singkatan dari "*Secure Hash Algorithm 512 bit*", yang merupakan fungsi _hashing_ kriptografi yang menghasilkan _hash_ 512-bit. Fungsi ini dirancang oleh *National Security Agency* (NSA) pada awal tahun 2000-an. Untuk Bitcoin, fungsi `SHA512` tidak digunakan secara langsung di dalam protokol, tetapi digunakan dalam konteks mendapatkan kunci anak pada tingkat aplikasi, menurut BIP32 dan BIP39. Dalam proses ini, fungsi ini digunakan beberapa kali dalam algoritma `HMAC`, serta dalam fungsi penurunan kunci `PBKDF2`. Fungsi `SHA512` merupakan bagian dari keluarga SHA 2, seperti halnya `SHA256`. Pengoperasiannya juga sangat mirip dengan `SHA256`.
