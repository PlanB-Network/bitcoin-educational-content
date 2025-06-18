---
term: P2PKH
---

P2PKH 代表 *Pay to Public Key Hash*。它是用於在 UTXO 上建立支出條件的標準腳本模型。它允許將比特幣鎖定在一個公開密鑰的 Hash，也就是接收的 Address 上。此腳本與 Legacy 標準相關，由 Satoshi Nakamoto 在 Bitcoin 的早期版本中引入。


P2PK 在腳本中明確包含公開金鑰，與此不同，P2PKH 使用公開金鑰的加密指紋。此腳本包括公開金鑰的 `SHA256` 的 `RIPEMD160` Hash，並規定要存取資金，收款人必須提供符合此 Hash 的公開金鑰，以及由相關私密金鑰產生的有效數位簽章。P2PKH 位址使用「Base58Check」格式編碼，透過使用校驗和來防止排印錯誤。這些位址總是以數字 `1` 開頭。