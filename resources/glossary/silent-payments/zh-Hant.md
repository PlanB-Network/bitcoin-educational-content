---
term: 無聲支付
---

使用靜態 Bitcoin 位址接收付款的方法，無需 Address 重複使用、無需互動，且不同付款與靜態 Address 之間無可見的 On-Chain 連結。此技術不需要為每筆交易 generate 新的、未使用的收款位址，因此避免了 Bitcoin 中收款人必須提供新的 Address 給付款人的一般互動。


使用 Silent Payments 時，付款人使用收款人的公開金鑰 (支出公開金鑰和掃描公開金鑰) 和他們自己的私密金鑰總和，作為每次付款的 generate 新 Address 的輸入。只有收款人使用自己的私密金鑰，才能計算出與這筆付款相對應的私密金鑰 Address。ECDH (*Elliptic-Curve Diffie-Hellman*) 是一種密碼金鑰 Exchange 演算法，用來建立一個共享秘密，然後用來推算出接收的 Address 和私人金鑰 (僅在收款人一方)。收款人必須掃描 Blockchain，並檢查符合通訊協定標準的每筆交易，才能識別出專為他們設計的 Silent Payments。與使用通知交易建立付款管道的 BIP47 不同，Silent Payments 省去了這個步驟，節省了一筆交易。然而，折衷的方法是收款人必須掃描所有可能的交易，以應用 ECDH 來判斷這些交易是否是寄給他們的。


例如，Bob 的靜態 Address $B$ 代表他的掃描公開金鑰和支出公開金鑰的串接：


$$ B = B_{\text{scan}}\text{ ‖ }B_{text{spend}}$$


這些鑰匙簡單來自以下路徑：


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


此靜態 Address 由 Bob 發佈。Alice 擷取它來對 Bob 進行無聲付款。她以這種方式計算 Bob 的付款 Address $P_0$：


$$ P_0 = B_{text{spend}}+ \text{Hash}(\text{inputHash} \cdot a \cdot B_{text{scan}} \text{ ‖ } 0) \cdot G $$


在哪裡？


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


與：


- $B_{\text{scan}}$: Bob 的掃描公開金鑰 (靜態 Address)；
- $B_{text{spend}}$: Bob 的花費公開金鑰 (靜態 Address)；
- $A$:輸入中公開金鑰的總和 (調整)；
- $a$:調整的私密金鑰，也就是在 Alice 的交易中作為輸入消耗的 UTXOs 的 `scriptPubKey` 中使用的所有金鑰對的總和；
- $text{outpoint}_L$：在 Alice 的交易中作為輸入的最小 UTXO（按辭彙編輯）；
- $\text{ ‖ }$：Concatenation (操作數端對端連接的操作)；
- $G$:橢圓曲線 `secp256k1` 的生成點；
- $\text{Hash}$：標記為 `BIP0352/SharedSecret` 的 SHA256 Hash 函式；
- $P_0$:支付給 Bob 的第一個公開金鑰 / 唯一 Address；
- $0$:用於 generate 多個唯一付款位址的整數。


Bob 以這種方式掃描 Blockchain，找到他的 Silent Payment：


$$ P_0 = B_{text{spend}}+ \text{Hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$


與：


- $b_{\text{scan}}$: Bob 的私人掃描金鑰。


如果他發現 $P_0$ 是一個 Address 包含寄給他的 Silent Payment，他會計算 $p_0$，這個私密金鑰允許他花掉 Alice 寄給 $P_0$ 的資金：


$$ p_0 = (b_{text\{spend}}+ text{Hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$


與：


- $b_{text{spend}}$：鮑勃的私人支出密鑰；
- $n$: 橢圓曲線 `secp256k1` 的階數.


除了這個基本版本之外，標籤也可以用來從相同的基本靜態 Address 中 generate 出幾個不同的靜態位址，目的是分開多種用途，而不會不合理地倍增掃描時所需的工作。