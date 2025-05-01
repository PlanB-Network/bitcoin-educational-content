---
term: op_checklocktimeverify (0xb1)
---

使交易無效，除非符合所有這些條件：


- 堆疊不是空的；
- 堆疊頂端的值大於或等於 `0`；
- 在 `nLockTime` 欄位和堆疊頂端的值 (即時或區塊號碼) 之間，時間鎖的類型是相同的；
- 輸入的 `nSequence` 欄位不等於 `0xffffffffffff`；
- 堆疊頂端的值大於或等於交易的 `nLockTime` 欄位的值。


如果其中任何一個條件不成立，就無法滿足包含 `OP_CHECKLOCKTIMEVERIFY` 的指令碼。如果所有這些條件都成立，那麼 `OP_CHECKLOCKTIMEVERIFY` 就會像 `OP_NOP` 一樣，意即它不會對腳本執行任何動作。就好像它消失了一樣。因此，`OP_CHECKLOCKTIMEVERIFY` 會對 UTXO 與包含它的腳本的使用時間施加時間限制。它可以以 Unix 時間日期或區塊號碼的形式來做。為了做到這一點，它限制了使用它的交易的 `nLockTime` 欄位的可能值，而這個 `nLockTime` 欄位本身也限制了交易何時可以包含在區塊中。


> ► *這個 opcode 是 `OP_NOP` 的替代品。它被放在 `OP_NOP2` 上。它的縮寫通常是 "CLTV"。注意， `OP_CLTV`不該與交易的 `nLockTime` 欄位混淆。前者使用後者，但它們的性質和作用是不同的。