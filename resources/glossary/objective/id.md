---
term: TUJUAN

---
Pada dompet deterministik dan hirarkis (HD), tujuan (atau _purpose_ dalam bahasa Inggris), yang didefinisikan oleh BIP43, merepresentasikan tingkat derivasi tertentu. Indeks ini, yang terletak pada kedalaman pertama dari pohon derivasi (`m/tujuan'/`), mengidentifikasi standar derivasi yang diadopsi oleh dompet, untuk memfasilitasi kompatibilitas antara perangkat lunak manajemen dompet yang berbeda. Sebagai contoh, dalam kasus alamat SegWit (BIP84), tujuan dicatat sebagai `/84'/`. Metode ini memungkinkan pengaturan kunci yang efisien di antara berbagai jenis alamat yang berbeda di dalam dompet HD yang sama. Indeks standar yang digunakan adalah:


- Untuk P2PKH: `44'`;
- Untuk P2WPKH yang bersarang di P2SH: `49'`;
- Untuk P2WPKH: `84'`;
- Untuk P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)