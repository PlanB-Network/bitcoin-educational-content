---
term: MAST
---

Merkelised Alternative Script Tree 的縮寫。一種使用 Merkle Tree 來總結使用者在接收 Address 中選擇的任意數目的花費條件的技術，必須滿足其中一個條件才能花費相關的 bitcoins。Merkle Tree 允許用戶選擇他們想要滿足的條件，而不透露 Blockchain 上其他條件的細節。這有助於降低與這些腳本相關的費用、創建更複雜的條件，並且隨著時間的推移，改善用戶隱私（除了使用 Schnorr 簽名之外）。此概念曾是多項提案的主題，但最終在 2021 年透過 Taproot Soft Fork 加入 Bitcoin。


> ► *最初，"MAST 「代表 」Merklized Abstract Syntax Tree"。在 Taproot 框架內的使用不再與 "Abstract Syntax Tree" 有關。然而，使用者仍繼續使用 MAST 一詞。Anthony Towns 因此建議改變原意，同時保留這個廣泛使用的縮寫為「Merklized Alternative Script Tree」*。