---
term: passphrase (BIP39)
---

一個可選的密碼，當與恢復短語結合時，可為確定性和分層 Bitcoin 錢包提供額外的 Layer 安全性。HD 錢包通常由 12 或 24 個單詞組成的恢復詞組生成。恢復詞組非常重要，因為它允許在遺失時恢復 Wallet 中的所有金鑰。但是，它構成了單點故障 (SPOF)。如果它受到損害，比特幣就會有風險。這就是 passphrase 的用處。它是一個可選的密碼，由使用者自行選擇，並添加到恢復短語中，以增強 Wallet 的安全性。不要與 PIN 碼或普通密碼混淆，passphrase 在密碼鑰匙的推導過程中扮演一個角色。


它與恢復密碼詞組一起工作，修改產生金鑰的 seed。因此，即使有人取得您的復原短語，如果沒有 passphrase，他們也無法存取您的資金。使用 passphrase 基本上會產生一個新的 Wallet，並擁有不同的金鑰。修改（即使是輕微修改）passphrase 會產生不同的 generate。


passphrase 是任意的，可以是使用者選擇的任何字元組合。使用 passphrase 有幾個優點。首先，它減少了與復原短語洩露相關的風險，因為它需要第二個因素來存取資金。其次，它可以被策略性地用於創建包含少量比特幣的誘餌錢包，以防被實體威脅盜取您的資金。最後，當希望控制 HD Wallet seed 產生的隨機性時，它的使用是很有趣的。passphrase 必須有足夠的複雜性來抵抗暴力攻擊，而且必須可靠地保存。遺失 passphrase 會導致無法存取資金，就像遺失復原短語一樣。


> ► *passphrase有時也被稱為："two-factor seed phrase"、"password"、"seed extension"、"extension word「，甚至 」13th or 25th word"。值得注意的是，Bitcoin 上有兩種密碼短語。最為人熟知的是上述依賴於 BIP-39 的密碼，它允許保護整個 HD Wallet。不過，BIP-38 也指定了一種方法，可以用 passphrase 來保護獨一無二的私密金鑰。第二種 passphrase 目前幾乎已不再使用。