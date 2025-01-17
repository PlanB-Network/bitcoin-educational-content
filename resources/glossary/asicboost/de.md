---
term: ASICBOOST

---
ASICBOOST ist eine 2016 erfundene algorithmische Optimierungsmethode, die die Effizienz des Bitcoin-Minings um etwa 20 % steigern soll, indem sie die Menge der für jeden Hash-Versuch des Headers erforderlichen Berechnungen reduziert. Diese Technik nutzt eine Eigenschaft der für das Mining verwendeten SHA256-Hash-Funktion, die die Daten vor der Verarbeitung in Blöcke unterteilt. ASICBOOST behält einen dieser Blöcke über mehrere Hashing-Versuche hinweg unverändert bei, so dass der Miner nur einen Teil der Arbeit für diesen Block über mehrere Versuche hinweg erledigen muss. Diese gemeinsame Nutzung von Daten ermöglicht die Wiederverwendung von Ergebnissen früherer Berechnungen und verringert so die Gesamtzahl der Berechnungen, die erforderlich sind, um einen gültigen Hash zu finden.

ASICBOOST kann in zwei Formen verwendet werden: Overt ASICBOOST und Covert ASICBOOST. Die verdeckte Form von ASICBOOST ist für jedermann sichtbar, da sie das Feld "nVersion" des Blocks als Nonce verwendet und die echte "Nonce" nicht verändert. Bei der verdeckten Form wird versucht, diese Änderungen durch die Verwendung von Merkle-Bäumen zu verbergen. Diese zweite Methode ist jedoch seit der Einführung von SegWit nicht mehr so effektiv, da der zweite Merkle-Baum die Anzahl der dafür erforderlichen Berechnungen erhöht.

Zusammenfassend lässt sich sagen, dass ASICBOOST es den Minern ermöglicht, nicht bei allen Hashing-Versuchen ein wirklich vollständiges SHA256 durchzuführen, da ein Teil des Ergebnisses unverändert bleibt, was die Arbeit der Miner beschleunigt.