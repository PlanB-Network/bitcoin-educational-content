---
name: Picocrypt
description: Alat sumber terbuka untuk mengenkripsi data Anda
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan telah dilakukan pada konten asli.*



___



## I. Presentasi



Dalam tutorial ini, kita akan melihat Picocrypt, sebuah perangkat lunak enkripsi yang sederhana, ringan, dan efektif untuk mengenkripsi data dengan tingkat keamanan yang tinggi.



Cocok untuk **mengenkripsi file**, Anda dapat menggunakannya untuk melindungi **data di komputer Anda, di stik USB**, tetapi juga data yang disimpan di Cloud. Sebagai contoh, Anda dapat mengenkripsi data dan menyimpannya di **Microsoft OneDrive, Google Drive, iCloud atau Dropbox**, meskipun untuk tujuan ini, saya lebih memilih perangkat lunak lain yang akan disajikan dalam artikel mendatang.



Anda juga bisa menggunakannya ketika Anda perlu **berbagi data dengan pihak ketiga**: berkat Picocrypt dan kunci dekripsi, mereka bisa mendekripsi data di komputer mereka. Jadi, jika akun atau komputer Anda disusupi, data Anda terlindungi.



Untuk mengikuti proyek Picocrypt, hanya ada satu Address:





- [Picocrypt di GitHub](https://github.com/Picocrypt/Picocrypt)



Benar-benar **gratis dan sumber terbuka**, PicoCrypt tersedia untuk **Windows,** **Linux** dan **macOS**. Pada Windows, Anda bisa menginstalnya pada komputer Anda sendiri atau menggunakan versi portabel.



## II. Picocrypt, perangkat lunak enkripsi sumber terbuka



Perangkat lunak enkripsi Picocrypt** menampilkan dirinya sebagai **alternatif** untuk solusi terkenal lainnya seperti **VeraCrypt** dan **Cryptomator** (**dirancang untuk mengenkripsi data di lingkungan Cloud**), atau **AxCrypt**. Ngomong-ngomong, di GitHub resmi Picocrypt, Anda bisa menemukan perbandingan dengan beberapa pesaing:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Sumber: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt **sangat ringan**, dengan berat hanya **3 MB**, dan tidak perlu diinstal: ini adalah **aplikasi portabel** dengan keuntungan tidak memerlukan hak administrator! Namun, aplikasi ini tidak mengabaikan keamanan, karena mengandalkan **algoritma yang kuat dan dapat diandalkan**:





- Algoritma enkripsi XChaCha20**
- Fungsi pintas tombol **Argon2**



Di atas dan di atas keuntungan yang baru saja disebutkan, yang benar-benar menarik adalah **kemudahan penggunaannya**!



Hanya perlu satu hal: **audit kode**, tetapi itu sudah direncanakan, seperti yang bisa Anda lihat dari tabel perbandingan di atas (baris terakhir). Tetapi karena ini open source, tidak ada yang bisa menghentikan Anda untuk melihat kode sumbernya.



Meskipun dibandingkan dengan BitLocker pada tabel di atas, **menurut saya BitLocker dan Picocrypt ditujukan untuk penggunaan yang berbeda**: BitLocker untuk mengenkripsi sebuah volume lengkap (Windows, misalnya) dan Picocrypt untuk mengenkripsi sebuah struktur pohon atau ruang penyimpanan berjenis "Drive".



## III. Menggunakan Picocrypt



Untuk demonstrasi ini, mesin Windows 11 akan digunakan.



### A. Mengenkripsi data dengan Picocrypt



Pertama-tama, Anda perlu mengunduh Picocrypt.exe dari GitHub resmi ([lihat halaman ini](https://github.com/Picocrypt/Picocrypt/releases)).



Buka aplikasi untuk menampilkan Interface yang minimalis di layar. Untuk mengenkripsi data, baik itu **sebuah file, beberapa file atau sebuah folder**, cukup dengan **seret dan letakkan ke dalam Interface Picocrypt**. Ini akan memilih data yang akan dienkripsi.



![Image](assets/fr/020.webp)



Kemudian, untuk enkripsi data, Anda memiliki akses ke beberapa opsi, termasuk kunci enkripsi. Ini bisa berupa kata sandi yang kuat atau kunci enkripsi dalam bentuk file kunci, atau **keduanya**. Jika kita mengambil contoh kata sandi, Anda memiliki pilihan antara membuat kata sandi Anda sendiri, atau membuat kata sandi dengan Picocrypt.



Kata sandi ini harus kuat, karena dapat digunakan untuk mendekripsi data. Masukkan di bawah "**Password**" dan "**Konfirmasi Kata Sandi**", kemudian klik "**Enkripsi**" untuk mengenkripsi data! Sebelum itu, Anda dapat mengklik tombol "**Change**" di sebelah "**Save output as**" untuk menentukan direktori output.



**Catatan**: untuk menggunakan kunci dalam format file, klik "**Buat**" di sebelah kanan "**Keyfiles**" untuk membuat kunci. Kemudian, pilih dengan mengeklik "**Edit**" dan seret serta jatuhkan file kunci ke area yang sesuai.



![Image](assets/fr/019.webp)



Dua file yang dipilih dienkripsi dan dikelompokkan bersama dalam file "**Encrypted.zip.pcv**", karena **PCV** adalah ekstensi yang digunakan oleh Picocrypt. File ZIP ini tidak dapat dibaca berkat enkripsi. Untuk mencegah file-file yang dipilih dikelompokkan bersama dalam satu file ZIP terenkripsi, Anda perlu mencentang opsi "**Recursively**", sehingga ada banyak file yang dienkripsi sebanyak file yang akan dienkripsi.



Untuk mengakses data kita, kita perlu mendekripsinya menggunakan Picocrypt.



![Image](assets/fr/023.webp)



Sebelum kita membahas tentang dekripsi data, berikut ini beberapa informasi tentang beberapa opsi yang tersedia:





- Mode Paranoid**: menggunakan tingkat keamanan tertinggi yang ditawarkan oleh Picocrypt. Alat ini akan menggunakan beberapa algoritma enkripsi bertingkat (XChaCha20 dan Serpent) dan HMAC-SHA3 sebagai pengganti BLAKE2b untuk autentikasi data.
- Reed-Solomon**: mengimplementasikan kode koreksi kesalahan *Reed-Solomon* untuk memfasilitasi koreksi kesalahan pada data yang rusak. Hal ini memungkinkan Anda untuk mendukung tingkat korupsi sekitar 3% dari file Anda.
- Pisahkan menjadi potongan-potongan** atau **bagi menjadi beberapa bagian**: jika anda mengenkripsi file yang besar, anda dapat meminta Picocrypt untuk membaginya menjadi beberapa bagian. Hal ini dapat membuat file lebih mudah untuk ditransfer.
- Kompres File** atau **Kompres file**: mengompres file untuk mengurangi ukuran file yang dienkripsi.
- File yang dihapus** atau **Fichiers supprimés**: hapus file sumber untuk menyimpan hanya versi terenkripsi



### B. Mendekripsi data dengan Picocrypt



Jika Anda perlu mendekripsi data, itu tidak lebih rumit daripada mengenkripsinya. Cukup buka Picocrypt dan **seret dan letakkan file PCV yang akan didekripsi**. Kemudian masukkan kata sandi dan/atau pilih file kunci sebelum mengklik "**Decrypt**".



![Image](assets/fr/021.webp)



Versi tidak terenkripsi dari arsip ZIP "Encrypted.zip" sekarang memungkinkan saya untuk memulihkan dua file saya dalam teks yang jelas!



![Image](assets/fr/022.webp)



## IV. Kesimpulan



**Anda telah diperingatkan: Picocrypt sangat mudah digunakan, dan berhasil! Meskipun Interface minimalis, ia menggabungkan beberapa opsi yang sangat berguna untuk menyesuaikan enkripsi! Dan karena tersedia dalam versi portabel, Anda bisa membawanya ke mana pun Anda pergi, sehingga Anda bisa mendekripsi data Anda dengan percaya diri**



Pastikan untuk menggunakan kata sandi yang kuat untuk melindungi data, dan jika anda menggunakan file kunci, anda harus ingat untuk mencadangkannya, jika tidak, anda tidak akan dapat mendekripsi kontainer PCV yang dihasilkan oleh Picocrypt. Terakhir, anda harus mengetahui bahwa ada juga [versi CLI](https://github.com/Picocrypt/CLI) (dengan fitur yang lebih sedikit) yang memungkinkan anda untuk menjalankan Picocrypt dari baris perintah: di sini, sekali lagi, Picocrypt membuka pintu ke kemungkinan baru.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5