---
term: 主鑰匙
---

在 HD (Hierarchical Deterministic) 錢包的情況下，主私密金鑰是由 Wallet 的 seed 衍生出來的唯一私密金鑰。為了取得主密鑰，`HMAC-SHA512`函數會套用到 seed，使用字面上的「*Bitcoin seed*」作為密鑰。此操作的結果會產生 512 位元的輸出，其中前 256 位元構成主金鑰，其餘 256 位元則構成主鏈碼。在 HD Wallet 的樹狀結構中，主密鑰和主鏈碼是衍生所有子私鑰和公鑰的起點。因此，主私人密碼匙的推導深度為 0。


![](../../dictionnaire/assets/19.webp)