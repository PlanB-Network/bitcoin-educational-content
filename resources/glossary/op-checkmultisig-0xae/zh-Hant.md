---
term: op_checkmultisig (0xae)
---

針對多個公開金鑰檢查多個簽章。它接受一系列 `N` 公鑰和 `M` 簽名作為輸入，其中 `M` 可以小於或等於 `N`。`OP_CHECKMULTISIG` 會驗證是否至少有 `M` 個簽章符合 `N` 個公開金鑰中的 `M`。請注意，由於一個歷史性的錯誤， `OP_CHECKMULTISIG` 會從堆疊中移除一個額外的元素。這個元素被稱為 "*dummy element*"。為了避免在 `scriptSig` 中產生錯誤，因此會包含一個 `OP_0`，這是一個無用的元素，以滿足移除並繞過這個 bug。自 BIP147 (於 2017 年與 SegWit 一同推出)，因該 bug 而消耗的無用元素必須是 `OP_0`，腳本才會有效，因為它是一個 malleability 向量。這個操作碼已在 Tapscript 中移除。