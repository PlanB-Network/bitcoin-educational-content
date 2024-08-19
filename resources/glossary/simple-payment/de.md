---
term: EINFACHE ZAHLUNG
---

Transaktionsmuster (oder Modell), das in der Kettenanalyse verwendet wird, gekennzeichnet durch den Verbrauch von einem oder mehreren UTXOs in den Eingaben und die Erzeugung von 2 UTXOs in den Ausgaben. Dieses Modell sieht daher folgendermaßen aus:

![](../../dictionnaire/assets/5.png)

Dieses einfache Zahlungsmodell deutet darauf hin, dass wir wahrscheinlich in Gegenwart einer Sendungs- oder Zahlungstransaktion sind. Der Benutzer hat sein eigenes UTXO in den Eingaben verbraucht, um in den Ausgaben ein Zahlungs-UTXO und ein Wechselgeld-UTXO (Wechselgeld, das an denselben Benutzer zurückgegeben wird) zu befriedigen. Wir wissen daher, dass der beobachtete Benutzer wahrscheinlich nicht mehr im Besitz eines der beiden UTXOs in den Ausgaben ist (das Zahlungs-UTXO), aber sie sind immer noch im Besitz des anderen UTXOs (das Wechselgeld-UTXO).