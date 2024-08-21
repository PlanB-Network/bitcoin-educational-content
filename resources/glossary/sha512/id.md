---
term: SHA512
---

Akronim untuk "*Secure Hash Algorithm 512 bits*". Ini adalah fungsi hash kriptografi yang menghasilkan digest sepanjang 512-bit. Dirancang oleh *National Security Agency* (NSA) pada awal tahun 2000-an. Untuk Bitcoin, fungsi `SHA512` tidak digunakan secara langsung dalam protokol, namun digunakan dalam konteks turunan kunci anak pada tingkat aplikasi, sesuai dengan BIP32 dan BIP39. Dalam proses-proses ini, ia digunakan berulang kali dalam algoritma `HMAC`, serta dalam fungsi derivasi kunci `PBKDF2`. Fungsi `SHA512` merupakan bagian dari keluarga SHA 2, seperti `SHA256`. Operasinya sangat mirip dengan yang terakhir.