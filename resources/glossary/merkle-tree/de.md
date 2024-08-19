---
term: MERKLE TREE
---

Ein Merkle Tree ist ein kryptografischer Akkumulator. Es handelt sich um eine Methode, um die Mitgliedschaft eines bestimmten Informationsstücks innerhalb einer größeren Menge nachzuweisen. Es ist eine Datenstruktur, die die Überprüfung von Informationen in einem kompakten Format erleichtert. Im Bitcoin-System werden Merkle Trees verwendet, um die Transaktionen eines Blocks zu gruppieren und in einen einzelnen Hash zu kondensieren, der als Merkle Root (oder "*Root Hash*") bezeichnet wird. Jede Transaktion wird gehasht, dann werden die benachbarten Hashes hierarchisch zusammengefasst, bis der Merkle Root erhalten wird.

![](../../dictionnaire/assets/1.png)

Diese Struktur ermöglicht die schnelle Überprüfung, ob eine spezifische Transaktion in einem gegebenen Block enthalten ist, ohne alle Transaktionen analysieren zu müssen. Zum Beispiel, wenn ich nur den Merkle Root habe und verifizieren möchte, dass `TX 7` tatsächlich Teil des Baums ist, würde ich nur die folgenden Beweise benötigen:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Mit diesen Informationen bin ich in der Lage, die Zwischenknoten bis zum Merkle Root zu berechnen.

![](../../dictionnaire/assets/2.png)

Merkle Trees werden insbesondere für Light Nodes (bekannt als "SPV") verwendet, die nur die Blockheader, aber nicht die Transaktionen speichern. Diese Struktur findet sich auch im UTREEXO-Protokoll, einem Protokoll, das das Kondensieren des UTXO-Sets von Knoten ermöglicht, und im MAST Taproot.

> ► *Der Merkle Tree ist nach Ralph Merkle benannt, einem Kryptografen, der diese Struktur 1979 entworfen hat. Ein Merkle Tree kann auch als "Hash-Baum" bezeichnet werden. Auf Französisch wird er als "Arbre de Merkle" oder "arbre de hachage" bezeichnet.*