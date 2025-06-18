---
term: 輸出腳本描述符
---

輸出腳本描述符，或簡稱描述符，是結構化的表達式，可完整描述輸出腳本 (`scriptPubKey`)，並提供所有必要資訊，以追蹤特定腳本的交易或來自特定腳本的交易。這些描述符透過對所使用位址的結構和類型的標準描述，有助於管理 HD 錢包中的金鑰。


描述符的主要優點在於能夠將還原 Wallet 的所有重要資訊都封裝在單一字串中（除了還原短語之外）。透過儲存描述符與相對應的 Mnemonic 詞組，不僅可以還原私密金鑰，也可以還原 Wallet 的精確結構和相關的腳本參數。事實上，還原 Wallet 不僅需要初始 seed 的知識，還需要特定的索引來推導子金鑰對，以及在 Multisig Wallet 的情況下每個因子的 `xpub`。以前，我們假設這些資訊是所有人都隱含知道的。然而，隨著腳本的多樣化以及更複雜配置的出現，這些資訊可能會變得難以推斷，因而將這些資料變成隱私和 Hard 至強迫資訊。描述符的使用大大簡化了這個過程：只要知道復原短語和相對應的描述符，就能可靠安全地復原一切。


描述符由多個 Elements 組成：


- 腳本功能，如 `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature), 和 `sortedmulti` (Multisignature with sorted keys)；
- 衍生路徑，例如，`[d34db33f/44h/0h/0h]` 表示衍生路徑和特定的主密鑰指紋；
- 各種格式的金鑰，例如十六進位公開金鑰或擴充公開金鑰 (`xpub`)；
- 校驗和，前面加上 Hash，以驗證描述符的完整性。


例如，P2WPKH Wallet 的描述符可以如下所示：


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

在此描述符中，衍生函數 `wpkh` 表示 Pay-to-Witness-Public-Key-Hash 指令碼類型。其後是衍生路徑，其中包含：


- cdeab12f：主鑰匙的指紋；
- `84h`：表示使用 BIP84 目的，擬用於 SegWit v0 位址；
- `0h`：表示它是 Mainnet 上的 BTC 貨幣；
- `0h`：指 Wallet 中使用的特定帳號。


描述符還包括此 Wallet 使用的擴充公開金鑰：


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


接下來，記號 `/<0;1>/*`指定描述符可以從外部 (`0`)和內部 (`1`)鏈 generate 位址，通配符 (`*`)允許以可設定的方式依序衍生多個位址，類似於管理傳統 Wallet 軟體上的「間隙限制」。


最後，`#jy0l7nr4` 代表驗證描述符完整性的校驗和。