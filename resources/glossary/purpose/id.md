---
term: TUJUAN
---

Dalam portofolio deterministik dan hirarkis (HD), tujuan, yang didefinisikan oleh BIP43, mewakili tingkat derivasi tertentu. Indeks ini, yang terletak di kedalaman pertama dari pohon derivasi (`m/tujuan'/`), mengidentifikasi standar derivasi yang diadopsi oleh portofolio, untuk memfasilitasi kompatibilitas antara perangkat lunak manajemen portofolio yang berbeda. Sebagai contoh, dalam kasus alamat SegWit (BIP84), tujuan dicatat sebagai `/84'/`. Metode ini memungkinkan kunci diatur secara efisien di antara berbagai jenis Address yang berbeda dalam satu portofolio HD. Indeks standar yang digunakan adalah :




- Untuk P2PKH: `44'`;
- Untuk P2WPKH yang bersarang di P2SH: `49'` ;
- Untuk P2WPKH: `84'`;
- Untuk P2TR: `86'`.