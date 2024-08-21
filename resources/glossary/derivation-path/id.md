---
term: DERIVATION PATH
---

Dalam konteks dompet Hierarchical Deterministic (HD), derivation path merujuk pada urutan indeks yang digunakan untuk menurunkan kunci anak dari kunci induk. Seperti yang dijelaskan dalam BIP32, jalur ini mengidentifikasi struktur pohon untuk menurunkan kunci anak. Derivation path direpresentasikan oleh serangkaian indeks yang dipisahkan oleh garis miring, dan selalu dimulai dengan kunci induk (ditandai sebagai `m/`). Sebagai contoh, jalur tipikal mungkin adalah `m/84'/0'/0'/0/0`. Setiap tingkat penurunan dikaitkan dengan kedalaman spesifik:
* `m /` menunjukkan kunci privat induk. Ini unik untuk sebuah dompet dan tidak dapat memiliki saudara kandung pada kedalaman yang sama. Kunci induk diturunkan langsung dari seed;
* `m / purpose' /` menunjukkan tujuan penurunan yang membantu mengidentifikasi standar yang diikuti. Bidang ini dijelaskan dalam BIP43. Sebagai contoh, jika dompet mengikuti standar BIP84 (SegWit V0), indeksnya kemudian akan `84'`;
* `m / purpose' / coin-type' /` menunjukkan jenis cryptocurrency. Ini memungkinkan untuk diferensiasi yang jelas antara cabang yang didedikasikan untuk satu cryptocurrency dengan yang didedikasikan untuk yang lain dalam dompet multi-koin. Indeks yang didedikasikan untuk Bitcoin adalah `0'`;
* `m / purpose' / coin-type' / account' /` menunjukkan nomor akun. Kedalaman ini memudahkan untuk membedakan dan mengorganisir dompet ke dalam akun yang berbeda. Akun-akun ini dinomori mulai dari `0'`. Kunci terluas (`xpub`, `xprv`...) ditemukan pada kedalaman ini;
* `m / purpose' / coin-type' / account' / change /` menunjukkan jalur. Setiap akun seperti yang didefinisikan pada kedalaman 3 memiliki dua jalur pada kedalaman 4: rantai eksternal dan rantai internal (juga disebut "change"). Rantai eksternal menurunkan alamat yang dimaksudkan untuk dibagikan secara publik, yaitu alamat yang ditawarkan kepada kita ketika kita klik "terima" di perangkat lunak dompet kita. Rantai internal menurunkan alamat yang tidak dimaksudkan untuk ditukar secara publik, terutama alamat kembalian. Rantai eksternal diidentifikasi dengan indeks `0` dan rantai internal diidentifikasi dengan indeks `1`. Anda akan perhatikan bahwa dari kedalaman ini, kita tidak lagi melakukan penurunan yang diperkuat, tetapi penurunan normal (tidak ada apostrof). Berkat mekanisme ini kita dapat menurunkan semua kunci publik anak dari `xpub` mereka;

* `m / purpose' / coin-type' / account' / change / address-index` hanya menunjukkan nomor alamat penerima dan pasangan kuncinya, untuk membedakannya dari saudara kandungnya pada kedalaman yang sama di cabang yang sama. Sebagai contoh, alamat turunan pertama memiliki indeks `0`, alamat kedua memiliki indeks `1`, dan seterusnya...

Sebagai contoh, jika alamat penerima saya memiliki derivation path `m / 86' / 0' / 0' / 0 / 5`, kita dapat menyimpulkan informasi berikut:
* `86'` menunjukkan bahwa kita mengikuti standar penurunan dari BIP86 (Taproot / SegWit V1);
* `0'` menunjukkan bahwa itu adalah alamat Bitcoin;
* `0'` menunjukkan bahwa kita berada pada akun pertama dari dompet;
* `0` menunjukkan bahwa itu adalah alamat eksternal;
* `5` menunjukkan bahwa itu adalah alamat eksternal keenam dari akun ini.

![](../../dictionnaire/assets/18.png)