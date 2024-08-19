---
term: TRANSAKTIONSGEBÜHREN
---

Transaktionsgebühren stellen eine Summe dar, die darauf abzielt, Miner für ihre Teilnahme am Proof-of-Work-Mechanismus zu entschädigen. Diese Gebühren ermutigen Miner, Transaktionen in die von ihnen erstellten Blöcke aufzunehmen. Sie resultieren aus der Differenz zwischen der Gesamtmenge der Eingänge und der Gesamtmenge der Ausgänge in einer Transaktion:

```text
gebühren = eingänge - ausgänge
```

Sie werden in `sats/vBytes` ausgedrückt, was bedeutet, dass die Gebühren nicht von der Menge der gesendeten Bitcoins abhängen, sondern vom Gewicht der Transaktion. Sie werden vom Sender einer Transaktion frei gewählt und bestimmen dessen Geschwindigkeit der Aufnahme in einen Block durch einen Auktionsmechanismus. Zum Beispiel, sagen wir, ich mache eine Transaktion mit einem Eingang von `100.000 sats`, einem Ausgang von `40.000 sats` und einem weiteren Ausgang von `58.500 sats`. Die Gesamtsumme der Ausgänge beträgt `98.500 sats`. Die dieser Transaktion zugewiesenen Gebühren betragen `1.500 sats`. Der Miner, der meine Transaktion einschließt, kann `1.500 sats` in seiner Coinbase-Transaktion erstellen im Austausch für die `1.500 sats`, die ich in meinen Ausgängen nicht wiedererlangt habe.

Transaktionen mit höheren Gebühren, relativ zu ihrer Größe, werden von Minern als Priorität behandelt, was den Bestätigungsprozess beschleunigen kann. Umgekehrt können Transaktionen mit niedrigeren Gebühren während Zeiten hoher Überlastung verzögert werden. Es ist erwähnenswert, dass Bitcoin-Transaktionsgebühren von der Blocksubvention getrennt sind, die einen zusätzlichen Anreiz für Miner darstellt. Die Blockbelohnung besteht aus neuen Bitcoins, die mit jedem abgebauten Block erstellt werden (Blocksubvention), sowie den gesammelten Transaktionsgebühren. Während die Blocksubvention aufgrund des Gesamtangebotslimits von Bitcoins im Laufe der Zeit abnimmt, werden Transaktionsgebühren weiterhin eine entscheidende Rolle spielen, um Miner zur Teilnahme zu ermutigen.

Auf Protokollebene hindert nichts Benutzer daran, Transaktionen ohne jegliche Gebühren in einem Block einzuschließen. In der Realität ist dieser Typ von gebührenfreien Transaktionen jedoch außergewöhnlich. Standardmäßig leiten Bitcoin-Knoten keine Transaktionen mit Gebühren unter `1 sat/vBytes` weiter. Wenn einige gebührenfreie Transaktionen durchgekommen sind, liegt das daran, dass sie direkt vom gewinnenden Miner integriert wurden, ohne das Netzwerk der Knoten zu durchlaufen. Zum Beispiel beinhaltet die folgende Transaktion keine Gebühren:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

In diesem spezifischen Beispiel war es eine Transaktion, die vom Direktor des F2Pool-Miningpools initiiert wurde. Als regulärer Benutzer liegt die aktuelle untere Grenze daher bei `1 sat/vBytes`.
Es ist auch notwendig, die Grenzen des Löschens zu berücksichtigen. Während Zeiten hoher Überlastung löschen die Mempools der Knoten ihre ausstehenden Transaktionen unterhalb einer bestimmten Schwelle, um ihre zugewiesene RAM-Grenze zu respektieren. Diese Grenze wird vom Benutzer frei gewählt, aber viele lassen den Standardwert von Bitcoin Core bei 300 MB. Sie kann in der `bitcoin.conf`-Datei mit dem Parameter `maxmempool` geändert werden.
> ► *Auf Englisch bezeichnen wir es als "transaction fees".*