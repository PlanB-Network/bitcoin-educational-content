---
term: Merkle Tree
---

Merkle Tree 是一種加密累加器。它是一種證明特定資訊在一個較大集合中的屬性的方法。它是一種資料結構，有助於以精簡的格式驗證資訊。在 Bitcoin 系統中，Merkle 樹用於將區塊的交易組合並濃縮為單個 Hash，稱為 Merkle Root（或「*根 Hash*」）。每個交易都會進行散列，然後將相鄰的散列分層散列在一起，直到得到 Merkle Root。


![](../../dictionnaire/assets/1.webp)


此結構可快速驗證特定交易是否包含在指定區塊中，而無需分析所有交易。例如，如果我只有 Merkle Root，我想要驗證 `TX 7` 確實是該樹的一部分，我只需要以下證明：


- `TX 7`；
- `Hash 8`；
- `Hash 5-6`；
- `gw-8 1-2-3-4`.

有了這些資訊，我就能計算出直到 Merkle Root 的中間節點。


![](../../dictionnaire/assets/2.webp)


Merkle Trees 主要用於只保留區塊標頭而不保留交易的輕型節點 (稱為「SPV」)。這種結構也出現在 UTREEXO 通訊協定 (UTREEXO 通訊協定) 和 MAST Taproot (MAST Taproot 通訊協定)，前者允許濃縮 UTXO 節點集，後者則允許濃縮 UTXO 節點集。


> ► *Merkle Tree以1979年設計此結構的密碼學家Ralph Merkle命名。Merkle Tree 也可以稱為「Hash 樹」。在法語中，它被稱為 "Arbre de Merkle 「或 」arbre de hachage"。