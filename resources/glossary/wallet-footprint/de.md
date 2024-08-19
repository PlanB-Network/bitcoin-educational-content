---
term: WALLET FOOTPRINT
---

Ein Satz von charakteristischen Merkmalen, die in Transaktionen beobachtet werden können, die vom selben Bitcoin-Wallet durchgeführt wurden. Diese Merkmale können Ähnlichkeiten in der Verwendung von Skripttypen, die Wiederverwendung von Adressen, die Reihenfolge der UTXOs, die Platzierung von Wechselgeldausgängen, das Signalisieren von RBF (*Replace-by-Fee*), die Versionsnummer, das `nSequence`-Feld und das `nLockTime`-Feld umfassen.

Wallet Footprints werden von Analysten verwendet, um die Aktivitäten einer bestimmten Entität auf der Blockchain zu verfolgen, indem wiederkehrende Muster in ihren Transaktionen identifiziert werden. Zum Beispiel schafft ein Benutzer, der systematisch sein Wechselgeld an P2TR-Adressen (`bc1p…`) sendet, einen charakteristischen Footprint, der verwendet werden kann, um seine zukünftigen Transaktionen zu verfolgen.

Wie LaurentMT in Space Kek #19 (ein französischsprachiger Podcast) erklärt, nimmt die Nützlichkeit von Wallet Footprints in der Kettenanalyse mit der Zeit deutlich zu. Tatsächlich betonen die wachsende Anzahl von Skripttypen und die zunehmend schrittweise Einführung dieser neuen Funktionen durch Wallet-Software die Unterschiede. Es ist sogar möglich, die von der verfolgten Entität verwendete Software genau zu identifizieren. Daher ist es wichtig zu verstehen, dass das Studium eines Wallet-Footprints besonders relevant für neuere Transaktionen ist, mehr als für solche, die Anfang der 2010er Jahre initiiert wurden.