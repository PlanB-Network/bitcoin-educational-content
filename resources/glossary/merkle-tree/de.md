---
term: MERKLE-BAUM

---
Ein Merkle-Baum ist ein kryptographischer Akkumulator. Er ist eine Methode zum Nachweis der Zugehörigkeit einer bestimmten Information zu einer größeren Menge. Es handelt sich um eine Datenstruktur, die die Überprüfung von Informationen in einem kompakten Format erleichtert. Im Bitcoin-System werden Merkle-Bäume verwendet, um die Transaktionen eines Blocks in einem einzigen Hash zu gruppieren und zu verdichten, der Merkle Root (oder "*Root Hash*") genannt wird. Jede Transaktion wird gehasht, dann werden die benachbarten Hashes hierarchisch zusammengehasht, bis die Merkle-Wurzel erreicht ist.

![](../../dictionnaire/assets/1.webp)

Diese Struktur ermöglicht eine schnelle Überprüfung, ob eine bestimmte Transaktion in einem bestimmten Block enthalten ist, ohne dass alle Transaktionen analysiert werden müssen. Wenn ich zum Beispiel nur die Merkle-Wurzel habe und überprüfen möchte, ob "TX 7" tatsächlich Teil des Baums ist, brauche ich nur die folgenden Beweise:


- tX 7";
- `HASH 8`;
- `HASH 5-6`;
- rAUTE 1-2-3-4".

Mit diesen Informationen bin ich in der Lage, die Zwischenknoten bis zur Merkle-Wurzel zu berechnen.

![](../../dictionnaire/assets/2.webp)

Merkle-Bäume werden vor allem für leichte Knoten (so genannte "SPV") verwendet, die nur die Block-Header, nicht aber die Transaktionen aufbewahren. Diese Struktur findet sich auch im UTREEXO-Protokoll, einem Protokoll, das die Verdichtung der UTXO-Knotengruppe ermöglicht, und im MAST Taproot.

> ► *Der Merkle-Baum ist nach Ralph Merkle benannt, einem Kryptographen, der diese Struktur 1979 entworfen hat. Ein Merkle-Baum kann auch als "Hash-Baum" bezeichnet werden. Im Französischen wird er als "Arbre de Merkle" oder "arbre de hachage" bezeichnet.*