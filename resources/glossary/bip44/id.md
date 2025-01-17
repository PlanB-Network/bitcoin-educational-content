---
term: BIP44

---
Sebuah proposal untuk perbaikan yang memperkenalkan sebuah struktur derivasi hirarki standar untuk dompet HD. BIP44 dibangun berdasarkan prinsip-prinsip yang ditetapkan oleh BIP32 untuk derivasi kunci dan BIP43 untuk penggunaan bidang "tujuan". Ini memperkenalkan struktur derivasi lima tingkat: `m / tujuan '/ jenis_koin' / akun '/ perubahan / indeks_alamat`. Berikut adalah detail dari setiap kedalaman:


- `m /` mengindikasikan kunci pribadi utama. Kunci ini unik untuk sebuah dompet dan tidak dapat memiliki saudara kandung pada kedalaman yang sama. Kunci utama secara langsung diturunkan dari seed wallet;
- 'm / tujuan' / ` menunjukkan tujuan derivasi yang membantu mengidentifikasi standar yang diikuti. Kolom ini dijelaskan dalam BIP43. Sebagai contoh, jika dompet mengikuti standar BIP84 (SegWit V0), indeksnya adalah `84'`;
- 'm / tujuan' / jenis koin' /` menunjukkan jenis mata uang kripto. Hal ini memungkinkan pembedaan yang jelas antara cabang yang didedikasikan untuk satu mata uang kripto dan cabang yang didedikasikan untuk mata uang kripto lainnya dalam dompet multi-koin. Indeks yang didedikasikan untuk Bitcoin adalah `0`;
- `m / tujuan '/ jenis koin' / akun '/` menunjukkan nomor akun. Kedalaman ini memungkinkan diferensiasi dan pengorganisasian dompet ke dalam akun-akun yang berbeda dengan mudah. Akun-akun ini diberi nomor mulai dari `0`. Kunci yang diperluas (`xpub`, `xprv`...) ditemukan pada kedalaman ini;
- `m / tujuan / jenis koin / akun / perubahan /` menunjukkan rantai. Setiap akun seperti yang didefinisikan pada kedalaman 3 memiliki dua rantai pada kedalaman 4: rantai eksternal dan rantai internal (juga disebut "change"). Rantai eksternal mendapatkan alamat yang ditujukan untuk dikomunikasikan secara publik, yaitu alamat yang ditawarkan kepada kita ketika kita mengklik "terima" pada perangkat lunak dompet kita. Rantai internal mendapatkan alamat yang tidak dimaksudkan untuk dipertukarkan secara publik, yaitu, terutama alamat perubahan. Rantai eksternal diidentifikasi dengan indeks `0` dan rantai internal diidentifikasi dengan indeks `1`. Anda akan melihat bahwa mulai dari kedalaman ini, kita tidak lagi melakukan derivasi yang diperkeras, tetapi derivasi normal (tidak ada apostrof). Berkat mekanisme ini, kita dapat menurunkan semua kunci publik anak dari `xpub`;
- `m / tujuan / jenis-koin / akun / perubahan / indeks-alamat` hanya menunjukkan nomor alamat penerima dan pasangan kuncinya, untuk membedakannya dari saudara-saudaranya pada kedalaman yang sama pada cabang yang sama. Sebagai contoh, alamat turunan pertama memiliki indeks `0`, alamat kedua memiliki indeks `1`, dan seterusnya...

Misalnya, jika alamat penerima saya memiliki jalur turunan `m / 86' / 0' / 0' / 0 / 5`, kita dapat menyimpulkan informasi berikut:


- `86'` mengindikasikan bahwa kami mengikuti standar derivasi BIP86 (Taproot atau SegWitV1);
- '0' menunjukkan bahwa itu adalah alamat Bitcoin;
- '0' menunjukkan bahwa kita berada di akun pertama dompet;
- `0` menunjukkan bahwa itu adalah alamat eksternal;
- `5` menunjukkan bahwa ini adalah alamat eksternal keenam dari akun ini.

![](../../dictionnaire/assets/18.webp)