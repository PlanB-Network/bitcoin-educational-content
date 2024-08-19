---
term: KONSOLIDIERUNG
---

Eine spezifische Transaktion, bei der mehrere kleine UTXOs zu einem Eingang zusammengeführt werden, um als Ausgang ein einzelnes, größeres UTXO zu bilden. Diese Operation ist eine Transaktion, die an die eigene Wallet gerichtet ist. Das Ziel der Konsolidierung besteht darin, Zeiträume mit niedrigen Gebühren im Bitcoin-Netzwerk zu nutzen, um mehrere kleine UTXOs zu einem größeren Wert zusammenzuführen. Dadurch werden obligatorische Ausgaben im Falle von Gebührenerhöhungen antizipiert, was Einsparungen bei zukünftigen Transaktionsgebühren ermöglicht.

Tatsächlich sind Transaktionen mit vielen Eingängen schwerer und folglich teurer. Über die Einsparungen bei Transaktionsgebühren hinaus ist die Konsolidierung auch eine Form der langfristigen Planung. Wenn Ihre Wallet sehr kleine UTXOs enthält, können diese unbrauchbar werden, wenn das Bitcoin-Netzwerk in eine längere Periode hoher Gebühren eintritt. Wenn Sie beispielsweise ein UTXO von 10.000 Sats ausgeben müssen, aber die minimalen Mining-Gebühren 15.000 Sats betragen, würden die Kosten den Wert des UTXO selbst übersteigen. Diese kleinen UTXOs werden dann ökonomisch irrational zu verwenden und bleiben unbrauchbar, solange die Gebühren nicht sinken. Diese UTXOs werden üblicherweise als "Staub" bezeichnet. Indem Sie regelmäßig Ihre kleinen UTXOs konsolidieren, reduzieren Sie dieses mit Gebührenerhöhungen verbundene Risiko.

Es ist jedoch wichtig zu beachten, dass Konsolidierungstransaktionen bei einer Kettenanalyse erkennbar sind. Eine solche Transaktion deutet auf eine Common Input Ownership Heuristic (CIOH) hin, was bedeutet, dass die Eingänge der Konsolidierungstransaktion einer einzigen Entität gehören. Dies kann Auswirkungen auf die Privatsphäre des Benutzers haben.

![](../../dictionnaire/assets/7.png)