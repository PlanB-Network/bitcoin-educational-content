---
term: COINJOIN

---
Coinjoin ist eine Technik, die dazu dient, die Rückverfolgbarkeit von Bitcoins zu umgehen. Sie beruht auf einer kollaborativen Transaktion mit einer spezifischen Struktur gleichen Namens: der Coinjoin-Transaktion. Coinjoin-Transaktionen tragen dazu bei, den Schutz der Privatsphäre von Bitcoin-Nutzern zu verbessern, indem sie es externen Beobachtern erschweren, Transaktionen zu analysieren. Diese Struktur ermöglicht es, mehrere Münzen in einer einzigen Transaktion zu mischen, was es schwierig macht, die Verbindungen zwischen Eingangs- und Ausgangsadressen zu bestimmen.

Die allgemeine Funktionsweise von coinjoin ist wie folgt: Verschiedene Nutzer, die sich vermischen möchten, zahlen einen Betrag als Input für eine Transaktion ein. Diese Eingaben werden als verschiedene Ausgaben desselben Betrags ausgegeben. Am Ende der Transaktion ist es unmöglich festzustellen, welcher Output zu welchem Nutzer gehört. Es gibt technisch gesehen keine Verbindung zwischen den Ein- und Ausgängen der Coinjoin-Transaktion. Die Verbindung zwischen jedem Nutzer und jedem UTXO ist unterbrochen, genauso wie die Historie der einzelnen Münzen.

![](../../dictionnaire/assets/4.webp)

Um Coinjoin zu ermöglichen, ohne dass ein Nutzer zu irgendeinem Zeitpunkt die Kontrolle über sein Geld verliert, wird die Transaktion zunächst von einem Koordinator erstellt und dann an jeden Nutzer übermittelt. Jeder unterschreibt die Transaktion auf seiner Seite, nachdem er sich vergewissert hat, dass sie ihm passt, und dann werden alle Unterschriften zur Transaktion hinzugefügt. Wenn ein Nutzer oder der Koordinator versucht, die Gelder anderer zu stehlen, indem er die Ausgaben der Coinjoin-Transaktion verändert, sind die Unterschriften ungültig und die Transaktion wird von den Knoten abgelehnt. Wenn die Aufzeichnung des Outputs der Teilnehmer unter Verwendung von Chaum'schen Blindsignaturen erfolgt, um die Verbindung mit dem Input zu vermeiden, wird dies als "Chaumian Coinjoin" bezeichnet.

Dieser Mechanismus erhöht die Vertraulichkeit von Transaktionen, ohne dass Änderungen am Bitcoin-Protokoll erforderlich sind. Spezielle Implementierungen von Coinjoin, wie Whirlpool, JoinMarket oder Wabisabi, bieten Lösungen, um den Koordinationsprozess zwischen den Teilnehmern zu erleichtern und die Effizienz der Coinjoin-Transaktion zu erhöhen. Hier ist ein Beispiel für eine Coinjoin-Transaktion:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Es ist schwierig, mit Sicherheit zu bestimmen, wer zuerst die Idee des Coinjoin auf Bitcoin eingeführt hat und wer die Idee hatte, David Chaums blinde Signaturen in diesem Zusammenhang zu verwenden. Es wird oft angenommen, dass Gregory Maxwell der erste war, der dies in [einer Nachricht auf BitcoinTalk im Jahr 2013] (https://bitcointalk.org/index.php?topic=279249.0) diskutierte:

Verwendung von Chaum-Blindsignaturen: Die Nutzer stellen eine Verbindung her und geben Eingaben ein (und ändern Adressen) sowie eine kryptografisch verblendete Version der Adresse, an die sie ihre privaten Münzen senden möchten; der Server signiert die Token und sendet sie zurück. Der Server signiert die Token und sendet sie zurück. Die Benutzer stellen die Verbindung anonym wieder her, demaskieren ihre Ausgabeadressen und senden sie zurück an den Server. Der Server kann sehen, dass alle Ausgaben von ihm signiert wurden und dass folglich alle Ausgaben von gültigen Teilnehmern stammen. Später melden sich die Teilnehmer erneut an und signieren.

Maxwell, G. (2013, 22. August). *CoinJoin: Bitcoin-Privatsphäre für die reale Welt*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Es gibt jedoch frühere Erwähnungen, sowohl für Chaum-Signaturen im Zusammenhang mit dem Mischen als auch für Coinjoins. [Im Juni 2011 stellt Duncan Townsend auf BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) einen Mixer vor, der Chaum-Signaturen in einer Weise verwendet, die modernen Chaumian Coinjoins recht ähnlich ist. Im selben Thread gibt es [eine Nachricht von hashcoin als Antwort auf Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793), um seinen Mixer zu verbessern. Diese Nachricht zeigt, was Coinjoins am ähnlichsten ist. Ein ähnliches System wird auch in [einer Nachricht von Alex Mizrahi aus dem Jahr 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry) erwähnt, als er die Schöpfer von Tenebrix beriet. Der Begriff "Coinjoin" selbst wurde nicht von Greg Maxwell erfunden, sondern geht auf eine Idee von Peter Todd zurück.

> für den Begriff "Coinjoin" gibt es keine französische Übersetzung. Einige Bitcoiner verwenden auch die Begriffe "mix", "mixing" oder "mixage", um sich auf die Coinjoin-Transaktion zu beziehen. Das Mischen ist vielmehr der Prozess, der dem Coinjoin zugrunde liegt. Außerdem ist es wichtig, das Mischen durch Coinjoin nicht mit dem Mischen durch einen zentralen Akteur zu verwechseln, der die Bitcoins während des Prozesses in Besitz nimmt. Dies hat nichts mit dem Coinjoin zu tun, bei dem der Nutzer während des Prozesses nicht die Kontrolle über seine Bitcoins verliert