---
term: Address 再利用
---

Address 重複使用是指使用相同的接收 Address 來封鎖多個 UTXO，有時是在幾個不同的交易中。比特幣通常使用對應於唯一 Address 的加密金鑰來鎖定。由於 Blockchain 是公開的，因此很容易看到哪些地址與多少個比特幣相關。在多次支付重複使用相同 Address 的情況下，可以合理地想像所有相關的 UTXO 都屬於同一個實體。因此，Address 重複使用會對使用者的隱私造成問題。它允許在多個交易和 UTXOs 之間建立確定的連結，以及延續 On-Chain 的資金追蹤。Satoshi 中本在他的白皮書中已經提到這個問題：


> "*作為額外的防火牆，每筆交易都可以使用一對新的金鑰，以防止它們被連結到一個共同的所有者。 - Nakamoto, S. (2008).「Bitcoin：點對點電子現金系統」。請參閱 https://Bitcoin.org/Bitcoin.pdf。

為了最低限度地保護隱私，強烈建議每個接收的 Address 只使用一次。對於每筆新付款，宜使用新的 Address generate。對於變更輸出，也應該使用新的 Address。幸運的是，由於有了確定性和分層式錢包，使用多個地址變得非常容易。所有與 Wallet 相關的金鑰對都可以很容易地從 seed 重新產生。這也是為什麼當您點擊「接收」按鈕時，Wallet 軟體總是會產生一個新的、不同的 Address。


> ► *英文稱為「Address Reuse」。