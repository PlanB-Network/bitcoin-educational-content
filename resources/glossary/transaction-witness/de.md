---
term: TRANSACTION WITNESS
---

Bezieht sich auf eine Komponente von Bitcoin-Transaktionen, die mit dem SegWit-Soft-Fork verschoben wurde, um das Problem der Transaktionsveränderlichkeit zu adressieren. Der Zeuge enthält die Signaturen und öffentlichen Schlüssel, die notwendig sind, um die in einer Transaktion ausgegebenen Bitcoins freizuschalten. Bei Legacy-Transaktionen repräsentierte der Zeuge die Summe von `scriptSig` aus allen Eingaben. Bei SegWit-Transaktionen repräsentiert der Zeuge die Summe von `scriptWitness` für jede Eingabe, und dieser Teil der Transaktion wird nun in einen separaten Merkle-Baum innerhalb des Blocks verschoben.

Vor SegWit konnten Signaturen leicht verändert werden, ohne vor der Bestätigung einer Transaktion ungültig zu werden, was den Transaktionsidentifikator änderte. Dies erschwerte den Aufbau verschiedener Protokolle, da eine unbestätigte Transaktion ihren Identifikator ändern konnte. Durch die Trennung der Zeugen macht SegWit Transaktionen nicht veränderlich, da jede Änderung in den Signaturen nicht mehr den Transaktionsidentifikator (TXID) beeinflusst, sondern nur den Zeugenidentifikator (WTXID). Zusätzlich zur Lösung des Veränderlichkeitsproblems ermöglicht diese Trennung eine Erhöhung der Kapazität jedes Blocks.

> ► *Auf Englisch wird "témoin" als "witness" übersetzt.*