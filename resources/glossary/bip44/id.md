---
term: BIP44
---

Sebuah usulan untuk perbaikan yang memperkenalkan struktur derivasi hierarkis standar untuk dompet HD. BIP44 membangun prinsip-prinsip yang ditetapkan oleh BIP32 untuk derivasi kunci dan pada BIP43 untuk penggunaan bidang "tujuan". Ini memperkenalkan struktur derivasi lima tingkat: `m / purpose' / coin_type' / account' / change / address_index`. Berikut adalah detail dari setiap kedalaman:
* `m /` menunjukkan kunci privat induk. Ini unik untuk sebuah dompet dan tidak dapat memiliki saudara kandung pada kedalaman yang sama. Kunci induk langsung diturunkan dari benih dompet;
* `m / purpose' /` menunjukkan tujuan derivasi yang membantu mengidentifikasi standar yang diikuti. Bidang ini dijelaskan dalam BIP43. Sebagai contoh, jika dompet mengikuti standar BIP84 (SegWit V0), indeksnya kemudian akan `84'`;
* `m / purpose' / coin-type' /` menunjukkan jenis cryptocurrency. Ini memungkinkan diferensiasi yang jelas antara cabang yang didedikasikan untuk satu cryptocurrency dan cabang yang didedikasikan untuk cryptocurrency lain dalam dompet multi-koin. Indeks yang didedikasikan untuk Bitcoin adalah `0'`;
* `m / purpose' / coin-type' / account' /` menunjukkan nomor akun. Kedalaman ini memungkinkan diferensiasi dan organisasi dompet yang mudah ke dalam akun yang berbeda. Akun-akun ini dinomori mulai dari `0'`. Kunci yang diperluas (`xpub`, `xprv`...) ditemukan pada kedalaman ini;
* `m / purpose' / coin-type' / account' / change /` menunjukkan rantai. Setiap akun seperti yang didefinisikan dalam kedalaman 3 memiliki dua rantai pada kedalaman 4: sebuah rantai eksternal dan sebuah rantai internal (juga disebut “change”). Rantai eksternal menurunkan alamat yang dimaksudkan untuk dikomunikasikan secara publik, yaitu, alamat yang ditawarkan kepada kita ketika kita klik “terima” di perangkat lunak dompet kita. Rantai internal menurunkan alamat yang tidak dimaksudkan untuk ditukar secara publik, yaitu, terutama alamat kembalian. Rantai eksternal diidentifikasi dengan indeks `0` dan rantai internal diidentifikasi dengan indeks `1`. Anda akan menyadari bahwa dari kedalaman ini, kita tidak lagi melakukan derivasi yang diperkuat, tetapi derivasi normal (tidak ada apostrof). Berkat mekanisme ini kita mampu menurunkan semua kunci publik anak dari `xpub` mereka;
* `m / purpose' / coin-type' / account' / change / address-index` hanya menunjukkan nomor alamat penerima dan pasangan kuncinya, untuk membedakannya dari saudara kandungnya pada kedalaman yang sama di cabang yang sama. Sebagai contoh, alamat yang pertama kali diturunkan memiliki indeks `0`, alamat kedua memiliki indeks `1`, dan seterusnya...
Sebagai contoh, jika alamat penerima saya memiliki jalur derivasi `m / 86' / 0' / 0' / 0 / 5`, kita dapat menyimpulkan informasi berikut:
* `86'` menunjukkan bahwa kita mengikuti standar derivasi dari BIP86 (Taproot atau SegWitV1);
* `0'` menunjukkan bahwa itu adalah alamat Bitcoin;
* `0'` menunjukkan bahwa kita berada pada akun pertama dari dompet;
* `0` menunjukkan bahwa itu adalah alamat eksternal;
* `5` menunjukkan bahwa itu adalah alamat eksternal keenam dari akun ini.

![](../../dictionnaire/assets/18.png)