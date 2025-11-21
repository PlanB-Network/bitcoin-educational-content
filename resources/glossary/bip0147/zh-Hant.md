---
term: BIP0147
---

SegWit Soft Fork 中包含的提案，旨在解決與 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 操作所消耗的假元素有關的可篡改性向量。由於歷史上的 off-by-one bug (單位移位錯誤)，這兩個操作碼會從堆疊中移除一個超出其基本功能的額外元素。因此，為了避免錯誤，必須在 `scriptSig` 開頭加入一個假值，以滿足移除並繞過錯誤。這個值是不必要的，但它必須存在腳本才會有效。引入 P2MS 標準的 BIP11 建議將 `OP_0` 放在不必要的值中。然而，此標準並未在共識規則層級執行，這意味著任何值都可以放在那裡而不會使交易失效。這就是 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 包含可變性向量的原因。BIP147 引入了一個新的共識規則，命名為 `NULLDUMMY`，要求這個假元素是一個空的位元組陣列 (`OP_0`)。任何其他值都會導致腳本評估立即失敗。這項變更適用於 SegWit 之前的腳本以及 P2WSH 腳本，並且需要 Soft Fork。