---
name: passphrase BIP39
description: 瞭解 passphrase 如何運作
---
![cover](assets/cover.webp)


## 什麼是 BIP39 passphrase？


HD 錢包通常由 12 或 24 個字組成的 Mnemonic 詞組產生。這個詞組非常重要，因為它可以在 Wallet 的實體媒介（例如 Hardware Wallet）遺失時恢復 Wallet 的所有金鑰。不過，它也構成了單點故障，因為如果它受到攻擊，攻擊者就可以竊取所有的 bitcoins。


![PASSPHRASE BIP39](assets/notext/01.webp)


這就是 passphrase 的用處。這是一個您可以自由選擇的密碼，在金鑰萃取過程中會加入 Mnemonic 詞組，以加強 Wallet 的安全性。


![PASSPHRASE BIP39](assets/notext/02.webp)


請小心不要將 passphrase 與您 Hardware Wallet 的 PIN 碼或用於解鎖存取您電腦上 Wallet 的密碼混淆。與所有這些 Elements 不同的是，passphrase 在您的 Wallet 金鑰的衍生過程中扮演一個角色。 **這意味著沒有它，您將永遠無法恢復您的比特幣。


passphrase 與 Mnemonic 詞組配合使用，可變更產生金鑰的 seed。因此，即使有人取得您的 12 或 24 字短語，如果沒有 passphrase，他們也無法存取您的資金。 **使用 passphrase 基本上會產生一個新的 Wallet，其中包含不同的金鑰。修改 passphrase（即使是輕微修改）會產生不同的 generate。


## 為什麼要使用 passphrase？


passphrase 是任意的，可以是使用者選擇的任何字元組合。因此，使用 passphrase 有幾個優點。首先，它降低了所有與 Mnemonic 短語洩露有關的風險，因為它需要第二個因素才能存取資金 (入室行竊、進入家中等)。


接下來，它可以被策略性地用來創建一個誘餌 Wallet，以應對物理限制來竊取您的資金，就像臭名昭著的 「*$5 扳手攻擊*」。在這種情況下，我們的想法是在沒有 passphrase 的情況下擁有一個 Wallet，其中只包含少量的比特幣，足以滿足潛在的攻擊者，同時擁有一個隱藏的 Wallet。後者使用相同的 Mnemonic 詞組，但以額外的 passphrase 作保護。


最後，當希望控制 HD Wallet 的 seed 產生的隨機性時，使用 passphrase 會很有趣。


## 如何選擇好的 passphrase？

要使 passphrase 有效，它必須有足夠的長度和隨機性。就像強密碼一樣，我建議選擇一個盡可能長且隨機的 passphrase，其中包含各種字母、數字和符號，讓任何暴力攻擊都無法得逞。


正確保存此 passphrase 也很重要，保存方式與 Mnemonic 短語相同。 **失去它就意味著失去比特幣的存取權**。我強烈建議不要只把它記在腦子裡，因為這會不合理地增加丟失的風險。最理想的做法是把它寫在一個與 Mnemonic 短語分開的實體媒介上 (紙張或金屬)。這個備份顯然必須存放在與您的 Mnemonic 短語不同的地方，以防止兩者同時被洩露。


## 教學


若要在 Ledger 裝置 (Stax、Flex 或 Nano) 上設定 passphrase，您可以參考本教學：


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

在 COLDCARD 上：


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

在 Jade Plus 上：


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

護照上 (第 2 批)：


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

在 Trezor 裝置上（Safe 3、Safe 5 或 Model One）：


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42