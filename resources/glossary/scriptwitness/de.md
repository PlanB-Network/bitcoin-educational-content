---
term: SCRIPTWITNESS
---

Ein Element in SegWit-Transaktionseinträgen, das die Signaturen und öffentlichen Schlüssel enthält, die notwendig sind, um die in der Transaktion gesendeten Bitcoins freizuschalten. Ähnlich dem `scriptSig` von Legacy-Transaktionen, wird das `scriptWitness` jedoch nicht an derselben Stelle platziert. Tatsächlich ist es dieser Teil, der als "Zeuge" (`*witness*` auf Englisch) bezeichnet wird, der in eine separate Datenbank verschoben wird, um das Problem der Transaktionsveränderlichkeit zu lösen. Jeder SegWit-Eingang hat sein eigenes `scriptWitness`, und alle `scriptWitness`-Elemente zusammen bilden das `Witness`-Feld der Transaktion.

> ► *Achten Sie darauf, `scriptWitness` nicht mit `witnessScript` zu verwechseln. Während das `scriptWitness` die Zeugendaten für jeden SegWit-Eingang enthält, definiert das `witnessScript` die Ausgabebedingungen eines P2WSH oder P2SH-P2WSH UTXO und stellt ein eigenes Skript dar, ähnlich dem `redeemScript` für einen P2SH-Ausgang.*