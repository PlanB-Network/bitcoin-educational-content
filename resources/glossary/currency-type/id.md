---
term: TIPE MATA UANG
---

Dalam konteks dompet deterministik dan hierarkis (HD), tipe mata uang (*coin type* dalam Bahasa Inggris) adalah tingkat derivasi yang memungkinkan untuk membedakan cabang-cabang dompet berdasarkan berbagai mata uang kripto yang digunakan. Lapisan derivasi ini, yang didefinisikan oleh BIP 44, berada pada kedalaman 2 dari struktur derivasi, mengikuti kunci utama dan tujuannya. Sebagai contoh, untuk Bitcoin, indeks yang ditetapkan adalah `0x80000000`, dicatat sebagai `/0'/` dalam jalur derivasi. Ini berarti bahwa semua alamat dan akun yang berasal dari jalur ini terkait dengan Bitcoin. Lapisan derivasi ini memungkinkan pemisahan yang jelas dari aset-aset berbeda dalam dompet multi-mata uang. Berikut adalah indeks yang digunakan untuk berbagai mata uang kripto:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)