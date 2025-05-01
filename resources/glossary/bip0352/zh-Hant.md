---
term: BIP0352
---

由 Josibake 和 Ruben Somsen 提出的改進提案，其中介紹了 Silent Payments，這是一種使用靜態 Bitcoin 位址接收付款的方法，不需要 Address 重複使用、互動，而且不同付款之間也沒有可見的 On-Chain 連結。此技術不需要為每筆交易 generate 新的、未使用的收款位址，因此避免了 Bitcoin 中收款人必須提供新的 Address 給付款人的一般互動。


在這個系統中，付款人使用收款人的公開金鑰和自己的私人金鑰，為每筆付款 generate 一個新的 Address。只有收款人使用他們的私人金鑰，才能計算出對應於這個 Address 的私人金鑰。ECDH (*Elliptic-Curve Diffie-Hellman*) 是一種密碼金鑰 Exchange 演算法，用來建立一個共享秘密，然後用來推算出接收的 Address 和私人金鑰（僅限於收款人一方）。收款人必須掃描 Blockchain，並檢查符合無聲付款條件的每筆交易，才能識別出擬用於他們的無聲付款。與使用通知交易建立付款通道的 BIP47 不同，無聲付款省去了這個步驟，節省了一次交易。但是，收款人必須掃描所有可能的交易，以應用 ECDH 來判斷這些交易是否是寄給他們的。