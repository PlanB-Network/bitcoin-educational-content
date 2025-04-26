---
term: ZEUGE DER TRANSAKTION

---
Bezieht sich auf eine Komponente von Bitcoin-Transaktionen, die mit der SegWit-Soft-Fork verschoben wurde, um das Problem der Fälschbarkeit von Transaktionen zu lösen. Der Zeuge enthält die Signaturen und öffentlichen Schlüssel, die notwendig sind, um die in einer Transaktion ausgegebenen Bitcoins zu entsperren. Bei Legacy-Transaktionen entsprach der Zeuge der Summe der `scriptSig` aus allen Eingaben. Bei SegWit-Transaktionen stellt der Zeuge die Summe von "ScriptWitness" für jede Eingabe dar, und dieser Teil der Transaktion wird nun in einen separaten Merkle-Baum innerhalb des Blocks verschoben.

Vor SegWit konnten Signaturen leicht verändert werden, ohne dass sie ungültig wurden, bevor eine Transaktion bestätigt wurde, wodurch sich die Transaktionskennung änderte. Dies erschwerte die Erstellung verschiedener Protokolle, da sich die Kennung einer unbestätigten Transaktion ändern konnte. Durch die Trennung der Zeugen macht SegWit Transaktionen nicht mehr fälschbar, da jede Änderung der Signaturen nicht mehr die Transaktionskennung (TXID), sondern nur noch die Zeugenkennung (WTXID) beeinflusst. Durch diese Trennung wird nicht nur das Problem der Fälschbarkeit gelöst, sondern auch die Kapazität der einzelnen Blöcke erhöht.

> ► *Im Englischen wird "témoin" mit "Zeuge" übersetzt.*