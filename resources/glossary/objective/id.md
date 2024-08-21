---
term: OBJEKTIF
---

Dalam dompet deterministik dan hierarkis (HD), objektif (atau _tujuan_ dalam bahasa Inggris), yang didefinisikan oleh BIP43, mewakili tingkat derivasi tertentu. Indeks ini, yang terletak pada kedalaman pertama dari pohon derivasi (`m / purpose' /`), mengidentifikasi standar derivasi yang diadopsi oleh dompet, untuk memfasilitasi kompatibilitas antara berbagai perangkat lunak manajemen dompet. Sebagai contoh, dalam kasus alamat SegWit (BIP84), objektifnya dicatat sebagai `/84'/`. Metode ini memungkinkan organisasi kunci yang efisien di antara berbagai jenis alamat dalam dompet HD yang sama. Indeks standar yang digunakan adalah:
* Untuk P2PKH: `44'`;
* Untuk P2WPKH-nested-in-P2SH: `49'`;
* Untuk P2WPKH: `84'`;
* Untuk P2TR: `86'`.

![](../../dictionnaire/assets/20.png)