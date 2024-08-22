---
term: ELTOO
---

Bitcoinの第二層における一般的なプロトコルで、UTXOの所有権を共同で管理する方法を定義します。Eltooは、Christian Decker、Rusty Russell、およびOlaoluwa Osuntokunによって特に設計され、開始と終了の間のLightningチャネル状態の交渉メカニズムに関連する問題を解決することを目的としています。Eltooアーキテクチャは、線形状態管理システムを導入することで交渉プロセスを簡素化し、確立された罰則ベースのアプローチをより柔軟で罰則の少ない更新方法に置き換えます。このプロトコルは、トランザクションの署名においてすべての入力を無視することを可能にする新しいタイプのSigHashの使用を要求します。このSigHashは当初`SIGHASH_NOINPUT`と呼ばれていましたが、その後`SIGHASH_ANYPREVOUT`（*Any Previous Output*）と呼ばれるようになりました。その実装はBIP118で計画されています。

> ► *Eltooは時々「LN-Symmetry」とも呼ばれます。*