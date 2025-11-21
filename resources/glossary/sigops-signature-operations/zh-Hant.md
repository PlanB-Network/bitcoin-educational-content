---
term: 簽章作業
---

指驗證交易所需的數位簽章作業。每個 Bitcoin 交易可能包含多個輸入，每個輸入可能需要一個或多個簽章才能視為有效。這些簽章的驗證是透過使用稱為「sigops」的特定操作碼來完成。具體來說，這包括 `OP_CHECKSIG`、`OP_CHECKSIGVERIFY`、`OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY`。這些作業會對必須驗證這些作業的網路節點造成一定的工作量。為了防止透過人為地增加 sigops 數量來進行 DoS 攻擊，該通訊協定因此對每個區塊允許的 sigops 數量設定了限制，以確保對節點而言，驗證負載仍在可管理的範圍內。這個限制目前設定為每個區塊最多 80,000 個 sigops。節點遵循以下規則進行計數：


在 `scriptPubKey` 中，`OP_CHECKSIG` 和 `OP_CHECKSIGVERIFY` 算作 4 個 sigops。操作碼 `OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 計為 80 sigops。事實上，在計算過程中，當這些操作不是 SegWit 輸入的一部分時，它們會乘以 4 (對於 P2WPKH，sigops 的數目因此會是 1)；


在`redeemscript`中，操作碼`OP_CHECKSIG`和`OP_CHECKSIGVERIFY`也算作4 sigops，`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`如果在`OP_n`之前，則算作`4n`，否則算作80 sigops；


對於 `witnessScript` 而言，`OP_CHECKSIG` 和 `OP_CHECKSIGVERIFY` 值 1 sigop，`OP_CHECKMULTISIG` 和 `OP_CHECKMULTISIGVERIFY` 如果是由 `OP_n` 引進，則計為 `n`，否則為 20 sigops；


在 Taproot 腳本中，sigops 的處理方式與傳統腳本不同。Taproot 並非直接計算每個簽章操作，而是為每個交易輸入引入一個 sigops 預算，這個預算與輸入的大小成正比。這個預算是 50 sigops 加上輸入見證的位元組大小。每個簽章作業會減少 50。如果簽章操作的執行使預算降至零以下，則腳本無效。這種方法允許 Taproot 腳本有更大的靈活性，同時透過直接將 sigops 與輸入的權重相連，保持對與 sigops 相關的潛在濫用的保護。因此，Taproot 指令碼不包括在每區塊 80,000 個 sigops 的限制內。