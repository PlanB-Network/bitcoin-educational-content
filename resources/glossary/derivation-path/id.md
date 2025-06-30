---
term: JALUR DERIVASI

---
Dalam konteks dompet _Hierarchical Deterministic_ (HD), sebuah jalur derivasi mengacu pada urutan indeks yang digunakan untuk derivasi kunci anak dari kunci _master_. Dijelaskan dalam BIP32, jalur ini mengidentifikasi struktur pohon untuk menurunkan anak kunci. Jalur derivasi diwakili oleh serangkaian indeks yang dipisahkan oleh garis miring, dan selalu dimulai dengan kunci utama (dilambangkan sebagai `m/`). Sebagai contoh, sebuah jalur yang umum adalah `m/84'/0'/0'/0/0`. Setiap tingkat derivasi dikaitkan dengan kedalaman tertentu:


- `m /` mengindikasikan kunci pribadi utama. Kunci ini unik untuk sebuah dompet dan tidak dapat memiliki "saudara" pada kedalaman yang sama. Kunci utama diturunkan langsung dari _seed_;
- `m / tujuan' / ` menunjukkan tujuan derivasi yang membantu mengidentifikasi standar yang diikuti. Kolom ini dijelaskan dalam BIP43. Sebagai contoh, jika dompet mengikuti standar BIP84 (SegWit V0), indeksnya adalah `84'`;
- `m / tujuan' / jenis koin' /` menunjukkan jenis mata uang kripto. Hal ini memungkinkan pembedaan yang jelas antara cabang yang didedikasikan untuk satu mata uang kripto dan cabang yang didedikasikan untuk mata uang kripto lainnya di dalam dompet multi-koin. Indeks untuk Bitcoin adalah `0`;
- `m / tujuan '/ jenis koin' / indeks akun '/` menunjukkan nomor indeks akun. Kedalaman ini memudahkan untuk membedakan dan mengatur dompet ke dalam akun-akun yang berbeda. Akun-akun ini diberi nomor mulai dari `0`. Kunci yang _extended_ (`xpub`, `xprv`...) ditemukan pada tingkat kedalaman ini;
- `m / tujuan / jenis koin / indeks akun / kembalian /` menunjukkan jalurnya. Setiap akun seperti yang didefinisikan pada kedalaman 3 memiliki dua jalur pada kedalaman 4: rantai eksternal dan rantai internal (juga disebut "_change_" atau kembalian). Rantai eksternal mendapatkan alamat yang ditujukan untuk dibagikan secara publik, yaitu alamat yang ditawarkan kepada kita ketika kita mengklik "terima" pada perangkat lunak dompet kita. Rantai internal mendapatkan alamat yang tidak dimaksudkan untuk dipertukarkan secara publik, terutama alamat kembalian. Rantai eksternal diidentifikasi dengan indeks `0` dan rantai internal diidentifikasi dengan indeks `1`. Anda akan melihat bahwa mulai dari kedalaman ini, kita tidak lagi melakukan _hardened derivation_, tetapi derivasi normal (tidak ada apostrof). Berkat mekanisme ini, kita dapat menurunkan semua kunci publik anak dari `xpub`;
- `m / tujuan / jenis-koin / indeks akun / kembalian / indeks-alamat` hanya menunjukkan nomor alamat penerima dan pasangan kuncinya, untuk membedakannya dari kunci-kunci saudaranya pada kedalaman yang sama pada cabang yang sama. Sebagai contoh, alamat turunan pertama memiliki indeks `0`, alamat kedua memiliki indeks `1`, dan seterusnya...

Sebagai contoh, jika alamat penerima saya memiliki jalur turunan `m / 86' / 0' / 0' / 0 / 5`, kita dapat menyimpulkan informasi berikut:


- `86'` menunjukkan bahwa kami mengikuti standar derivasi BIP86 (Taproot / SegWit V1);
- `0` menunjukkan bahwa itu adalah alamat Bitcoin;
- `0` menunjukkan bahwa kita berada di akun pertama dompet;
- `0` menunjukkan bahwa itu adalah alamat eksternal;
- `5` menunjukkan bahwa ini adalah alamat eksternal keenam dari akun ini.

![](../../dictionnaire/assets/18.webp)
