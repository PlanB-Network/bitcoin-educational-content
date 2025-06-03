---
term: ELTOO
---

Bitcoin 第二層的一般通訊協定，定義如何共同管理 UTXO 的 Ownership。Eltoo 是由 Christian Decker、Rusty Russell 和 Olaoluwa Osuntokun 所設計，特別是為了解決 Lightning 通道狀態的協商機制相關問題，也就是開啟與關閉之間的協商機制。Eltoo 架構透過引入線性狀態管理系統來簡化協商過程，以更靈活、懲罰性更低的更新方法取代既有的懲罰性方法。此協定需要使用新類型的 SigHash，允許忽略交易簽章中的所有輸入。這種 SigHash 最初稱為 `SIGHASH_NOINPUT`，後來稱為 `SIGHASH_ANYPREVOUT`（*任何先前的輸出*）。它的實作計畫在 BIP118 中。


> ► *Eltoo有時也被稱為「LN-對稱」。