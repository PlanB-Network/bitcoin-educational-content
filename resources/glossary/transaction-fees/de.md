---
term: TRANSAKTIONSGEBÜHREN

---
Transaktionsgebühren sind ein Betrag, der die Miner für ihre Teilnahme am Proof-of-Work-Mechanismus entschädigen soll. Diese Gebühren sind ein Anreiz für die Miner, Transaktionen in die von ihnen erstellten Blöcke aufzunehmen. Sie ergeben sich aus der Differenz zwischen dem Gesamtbetrag der Inputs und dem Gesamtbetrag der Outputs in einer Transaktion:

```text
fees = inputs - outputs
```

Sie werden in "sats/vBytes" ausgedrückt, was bedeutet, dass die Gebühren nicht von der Menge der gesendeten Bitcoins abhängen, sondern vom Gewicht der Transaktion. Sie werden vom Absender einer Transaktion frei gewählt und bestimmen die Geschwindigkeit, mit der sie in einen Block aufgenommen wird, durch einen Auktionsmechanismus. Nehmen wir zum Beispiel an, ich mache eine Transaktion mit einem Input von 100.000 Sats, einem Output von 40.000 Sats und einem weiteren Output von 58.500 Sats. Die Gesamtsumme der Ausgaben beträgt 98.500 sats. Die Gebühren für diese Transaktion betragen 1.500 Sats. Der Miner, der meine Transaktion einbezieht, kann in seiner Coinbase-Transaktion 1.500 Sats erzeugen, im Austausch für die 1.500 Sats, die ich in meinen Outputs nicht zurückgewonnen habe.

Transaktionen mit höheren Gebühren im Verhältnis zu ihrer Größe werden von den Minern vorrangig behandelt, was den Bestätigungsprozess beschleunigen kann. Umgekehrt können Transaktionen mit niedrigeren Gebühren in Zeiten hoher Überlastung verzögert werden. Es ist erwähnenswert, dass sich die Bitcoin-Transaktionsgebühren von der Block-Belohnung unterscheiden, die einen zusätzlichen Anreiz für Miner darstellt. Die Blockbelohnung besteht aus neuen Bitcoins, die mit jedem geminten Block erzeugt werden (Blocksubvention), sowie aus den eingenommenen Transaktionsgebühren. Während die Blocksubvention mit der Zeit abnimmt, weil das Gesamtangebot an Bitcoins begrenzt ist, werden die Transaktionsgebühren weiterhin eine entscheidende Rolle spielen, um die Miner zur Teilnahme zu bewegen.

Auf Protokollebene hindert die Nutzer nichts daran, Transaktionen ohne Gebühren in einen Block aufzunehmen. In der Realität ist diese Art von gebührenfreier Transaktion die Ausnahme. Standardmäßig leiten Bitcoin-Knoten keine Transaktionen weiter, deren Gebühren niedriger sind als "1 sat/vBytes". Wenn einige gebührenfreie Transaktionen weitergegeben wurden, liegt das daran, dass sie direkt von dem gewinnenden Miner integriert wurden, ohne das Netzwerk der Knoten zu durchqueren. Die folgende Transaktion enthält zum Beispiel keine Gebühren:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

In diesem konkreten Beispiel handelte es sich um eine Transaktion, die vom Direktor des F2Pool-Mining-Pools initiiert wurde. Als regulärer Nutzer liegt die aktuelle Untergrenze daher bei "1 sat/vBytes".

Es ist auch notwendig, die Grenzen der Bereinigung zu berücksichtigen. In Zeiten hoher Auslastung bereinigen die Mempools der Nodes ihre ausstehenden Transaktionen unterhalb eines bestimmten Schwellenwerts, um ihr zugewiesenes RAM-Limit einzuhalten. Dieses Limit wird vom Benutzer frei gewählt, aber viele belassen den Standardwert von Bitcoin Core bei 300 MB. Er kann in der Datei `bitcoin.conf` mit dem Parameter `maxmempool` geändert werden.

> ► *Im Englischen sprechen wir von "Transaktionsgebühren".*