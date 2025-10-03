---
name: Picocrypt
description: Alat sumber terbuka untuk mengenkripsi data Anda
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan telah dilakukan pada konten asli.*
___

## I. Presentasi

Dalam tutorial ini, kita akan melihat Picocrypt, sebuah perangkat lunak enkripsi yang sederhana, ringan, dan efektif untuk mengenkripsi data dengan tingkat keamanan yang tinggi.

Cocok untuk **mengenkripsi file**, Anda dapat menggunakannya untuk melindungi **data di komputer Anda**, **di flash drive USB**, tetapi juga data yang disimpan di Cloud. Misalnya, Anda dapat mengenkripsi data dan menyimpannya di Microsoft OneDrive, Google Drive, iCloud, atau Dropbox, meskipun untuk tujuan ini saya lebih memilih perangkat lunak lain yang akan disajikan dalam artikel mendatang.

Anda juga dapat menggunakannya saat Anda perlu **berbagi data dengan pihak ketiga**: berkat Picocrypt dan kunci dekripsi, mereka akan dapat mendekripsi data di komputer mereka. Jadi, jika akun atau komputer Anda disusupi, data Anda tetap terlindungi.

Untuk mengikuti proyek Picocrypt, hanya ada satu alamat:

- [Picocrypt di GitHub](https://github.com/Picocrypt/Picocrypt)

Benar-benar **gratis dan open source**, PicoCrypt tersedia untuk **Windows,** **Linux** dan **macOS**. Pada Windows, Anda bisa menginstalnya pada komputer Anda sendiri atau menggunakan versi portabel.

## II. Picocrypt, perangkat lunak enkripsi open source

**Perangkat lunak enkripsi Picocrypt** menampilkan dirinya sebagai **alternatif** untuk solusi terkenal lainnya seperti **VeraCrypt** dan **Cryptomator** (**dirancang untuk mengenkripsi data di lingkungan Cloud**), atau **AxCrypt**. Ngomong-ngomong, di GitHub resmi Picocrypt, Anda bisa menemukan perbandingan dengan beberapa pesaing:

|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Gratis         | ✅ Ya                                                                              | ✅ Ya       | ✅ Ya     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Ya                                                                              | ✅ Ya       | ❌ Tidak      | ❌ No       | ✅ Yes       |
| Ukuran         | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Ya       | ❌ Tidak      | ✅ Yes      | ❌ No        |
| Perizinan      | ✅ Tidak ada                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Penggunaan     | ✅ Mudah                                                                             | ❌ Susah      | ✅ Mudah    | ✅ Mudah     | 🟧 Menengah   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Tidak diketahui  | ✅ Scrypt    |
| Intergritas Data | ✅ Selalu                                                                           | ❌ Tidak        | ❌ Tidak      | ❓ Tidak diketahui  | ✅ Selalu    |
| Deniability    | ✅ Ada                                                                        | ✅ Ada | ❌ Tidak      | ❌ Tidak       | ❌ Tidak        |
| Kode Reed-Solomon   | ✅ Ya                                                                              | ❌ Tidak        | ❌ Tidak      | ❌ Tidak       | ❌ Tidak        |
| Kompresi    | ✅ Ya                                                                              | ❌ Tidak        | ✅ Ya     | ✅ Ya      | ❌ Tidak        |
| Sistem Telemetri      | ✅ Tidak ada                                                                             | ✅ Tidak ada      | ✅ Tidak ada    | ❓ Tidak diketahui  | ✅ Tidak ada      |
| Teraudit          | ✅ [Ya](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Ya       | ❌ Tidak      | ❓ Tidak diketahui  | ✅ Ya       |

Sumber: [Github.com](https://github.com/Picocrypt/Picocrypt)

Picocrypt **sangat ringan**, dengan ukuran hanya **3 MB**, dan tidak perlu diinstal: ini adalah **aplikasi portabel** dengan keuntungan tidak memerlukan hak administrator! Namun, aplikasi ini tidak mengabaikan keamanan, karena mengandalkan **algoritma yang kuat dan dapat diandalkan**:

- Algoritma enkripsi **XChaCha20**
- Fungsi Key bypass **Argon2**

Di luar keunggulan yang baru saja disebutkan, yang paling menarik adalah **kemudahan penggunaannya!**

Hanya membutuhkan satu hal: **code audit**, tetapi itu sudah direncanakan, seperti yang Anda lihat dari tabel perbandingan di atas (baris terakhir). Namun, karena ini adalah open source, tidak ada yang menghentikan Anda untuk melihat soruce codenya.

Meskipun dibandingkan dengan BitLocker dalam tabel di atas, **menurut pendapat saya BitLocker dan Picocrypt ditujukan untuk kegunaan yang berbeda**: BitLocker untuk mengenkripsi seluruh volume (misalnya, volume Windows) dan Picocrypt untuk mengenkripsi struktur direktori atau ruang penyimpanan tipe "Drive".

## III. Menggunakan Picocrypt

Untuk demonstrasi ini, menggunakan komputer Windows 11.

### A. Mengenkripsi data dengan Picocrypt

Pertama-tama, Anda perlu mengunduh Picocrypt.exe dari GitHub resmi ([lihat halaman ini](https://github.com/Picocrypt/Picocrypt/releases)).

Buka aplikasi untuk menampilkan Interface yang minimalis di layar. Untuk mengenkripsi data, baik itu **sebuah file, beberapa file atau sebuah folder**, cukup dengan **seret dan letakkan ke dalam Interface Picocrypt**. Ini akan memilih data yang akan dienkripsi.

![Image](assets/fr/020.webp)

Kemudian, untuk enkripsi data, Anda memiliki akses ke beberapa opsi, termasuk kunci enkripsi. Kunci ini bisa berupa kata sandi yang kuat atau kunci enkripsi dalam bentuk file kunci, atau keduanya. Jika kita mengambil contoh kata sandi, Anda memiliki pilihan antara membuat kata sandi Anda sendiri, atau membuat kata sandi dengan Picocrypt.

Kata sandi ini harus kuat, karena dapat digunakan untuk mendekripsi data. Masukkan di bawah "Password" dan "Confirm Password", lalu klik "**Encrypt**" untuk mengenkripsi data! Sebelum itu, Anda dapat mengklik tombol "**Change**" di samping "**Save output as**" untuk menentukan direktori keluaran.

**Catatan**: untuk menggunakan kunci dalam format file, klik "**Create**" di sebelah kanan "**Keyfiles**" untuk membuat kunci. Kemudian, pilih dengan mengeklik "**Edit**" dan drag and drop file kunci ke area yang sesuai.

![Image](assets/fr/019.webp)

Kedua file yang dipilih dienkripsi dan dikelompokkan dalam file "**Encrypted.zip.pcv**", karena **PCV** adalah ekstensi yang digunakan oleh Picocrypt. File ZIP ini tidak dapat dibaca berkat enkripsi. Untuk mencegah file yang dipilih dikelompokkan dalam satu file ZIP terenkripsi, Anda perlu mencentang opsi "**Recursively**", sehingga ada file terenkripsi sebanyak jumlah file yang akan dienkripsi.

Untuk mengakses data kita, kita perlu mendekripsinya menggunakan Picocrypt.

![Image](assets/fr/023.webp)

Sebelum kita berbicara tentang dekripsi data, berikut adalah beberapa informasi tentang beberapa opsi yang tersedia:

- **Paranoid mode**: menggunakan tingkat keamanan tertinggi yang ditawarkan oleh Picocrypt. Aplikasi ini akan menggunakan beberapa algoritma enkripsi berantai (XChaCha20 dan Serpent) dan HMAC-SHA3 alih-alih BLAKE2b untuk otentikasi data.
- **Reed-Solomon**: menerapkan kode koreksi kesalahan Reed-Solomon untuk memfasilitasi koreksi kesalahan pada data yang rusak. Ini memungkinkan Anda untuk mendukung tingkat kerusakan sekitar 3% dari file Anda.
- **Split into chunks**: jika Anda mengenkripsi file besar, Anda dapat meminta Picocrypt untuk membaginya menjadi beberapa bagian. Ini dapat membuat file lebih mudah untuk ditransfer.
- **Compress Files**: mengompres file untuk mengurangi ukuran file terenkripsi.
- **Deleted files**: menghapus file asli untuk hanya menyimpan versi terenkripsi.

### B. Mendekripsi data dengan Picocrypt

Jika Anda perlu mendekripsi data, itu tidak lebih rumit daripada mengenkripsinya. Cukup buka Picocrypt dan **drag and drop file PCV yang akan didekripsi**. Kemudian masukkan kata sandi dan/atau pilih file kunci sebelum mengklik "**Decrypt**".

![Image](assets/fr/021.webp)

Versi tidak terenkripsi dari arsip ZIP "Encrypted.zip" sekarang memungkinkan saya untuk memulihkan kedua file saya dalam teks yang jelas!

![Image](assets/fr/022.webp)

## IV. Kesimpulan

**Anda sudah diperingatkan: Picocrypt sangat mudah digunakan, dan berfungsi! Meskipun Interface-nya minimalis, Picocrypt menggabungkan beberapa opsi yang sangat berguna untuk menyesuaikan enkripsi! Dan karena tersedia dalam versi portabel, Anda dapat membawanya ke mana pun Anda pergi, sehingga Anda dapat mendekripsi data Anda dengan percaya diri.**

Pastikan untuk menggunakan kata sandi yang kuat untuk melindungi data, dan jika Anda menggunakan file kunci, Anda harus ingat untuk mencadangkannya, jika tidak, Anda tidak akan lagi dapat mendekripsi kontainer PCV yang dihasilkan oleh Picocrypt. Terakhir, Anda harus tahu bahwa ada juga [versi CLI](https://github.com/Picocrypt/CLI) (dengan fitur yang lebih sedikit) yang memungkinkan Anda menjalankan Picocrypt dari command line: dan lagi, Picocrypt membuka pintu ke kemungkinan baru.

https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5
