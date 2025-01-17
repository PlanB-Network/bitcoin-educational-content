---
term: SCRIPTWITNESS

---
Ein Element in SegWit-Transaktionseinträgen, das die Signaturen und öffentlichen Schlüssel enthält, die zum Entsperren der in der Transaktion gesendeten Bitcoins erforderlich sind. Ähnlich wie das `scriptSig` von Legacy-Transaktionen befindet sich das `scriptWitness` jedoch nicht an der gleichen Stelle. Vielmehr wird dieser Teil, der als "Zeuge" (auf Englisch "witness") bezeichnet wird, in eine separate Datenbank ausgelagert, um das Problem der Fälschbarkeit von Transaktionen zu lösen. Jede SegWit-Eingabe hat ihren eigenen `scriptWitness`, und alle `scriptWitness`-Elemente bilden zusammen das Feld `Witness` der Transaktion.

> achten Sie darauf, `scriptWitness` nicht mit `witnessScript` zu verwechseln. Während `scriptWitness` die Witness-Daten für jede SegWit-Eingabe enthält, definiert das `witnessScript` die Ausgabebedingungen eines P2WSH- oder P2SH-P2WSH-UTXO und stellt ein eigenständiges Skript dar, ähnlich dem `redeemScript` für eine P2SH-Ausgabe