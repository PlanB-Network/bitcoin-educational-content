---
name: Ricochet
description: Verständnis und Verwendung von Ricochet-Transaktionen
---
![cover ricochet](assets/cover.webp)

> *"Ein Premium-Tool, das Ihrer Transaktion zusätzliche Verbindungen zur Geschichte hinzufügt. Umgehen Sie die Schwarzen Listen und schützen Sie sich vor ungerechtfertigten Kontosperrungen durch Dritte."*

## Was ist Ricochet?
Ricochet ist eine Technik, bei der mehrere fiktive Transaktionen an sich selbst durchgeführt werden, um einen Transfer des Bitcoin-Besitzes zu simulieren. Dieses Tool unterscheidet sich von anderen Samourai-Transaktionen, da es keine potenzielle Anonymität bietet, sondern eine Form der retrospektiven Anonymität. Ricochet hilft tatsächlich dabei, die Spezifika zu verwischen, die die Fungibilität einer Bitcoin-Münze gefährden könnten.

Wenn Sie beispielsweise eine Coinjoin-Transaktion durchführen, wird Ihre Ausgabe aus dem Mix als solche identifiziert. Chain-Analyse-Tools können Muster von Coinjoin-Transaktionen erkennen und die daraus resultierenden Münzen kennzeichnen. Coinjoin zielt darauf ab, die historischen Verbindungen einer Münze zu unterbrechen, aber ihr Durchgang durch Coinjoins bleibt erkennbar. Um einen Vergleich anzustellen, ähnelt dieses Phänomen dem Verschlüsseln eines Textes: Obwohl wir nicht auf den ursprünglichen Klartext zugreifen können, ist leicht erkennbar, dass eine Verschlüsselung angewendet wurde.

Genau diese Bezeichnung "Coinjoin-Ausgabemünze" kann die Fungibilität einer UTXO beeinträchtigen. Regulierte Einrichtungen wie Börsenplattformen können eine UTXO, die an einem Coinjoin teilgenommen hat, ablehnen oder sogar Erklärungen von ihrem Besitzer verlangen, mit dem Risiko, dass ihr Konto gesperrt oder ihre Gelder eingefroren werden. In einigen Fällen kann die Plattform sogar Ihr Verhalten den staatlichen Behörden melden.

Hier kommt die Ricochet-Methode ins Spiel. Um den Fußabdruck, der durch einen Coinjoin hinterlassen wird, zu verwischen, führt Ricochet vier aufeinanderfolgende Transaktionen durch, bei denen der Benutzer seine Mittel auf verschiedene Adressen überweist. Nach dieser Sequenz von Transaktionen leitet das Ricochet-Tool schließlich die Bitcoins an ihr endgültiges Ziel, wie z.B. eine Börsenplattform. Das Ziel besteht darin, eine Distanz zwischen der ursprünglichen Coinjoin-Transaktion und der endgültigen Ausgabehandlung zu schaffen. Auf diese Weise werden Chain-Analyse-Tools denken, dass wahrscheinlich nach dem Coinjoin ein Eigentumswechsel stattgefunden hat und es daher nicht erforderlich ist, Maßnahmen gegen den Absender zu ergreifen.
![ricochet diagram](assets/de/1.webp)
Angesichts der Ricochet-Methode könnte man sich vorstellen, dass Chain-Analyse-Software ihre Untersuchungen über vier Sprünge hinaus vertiefen würde. Diese Plattformen stehen jedoch vor einem Dilemma bei der Optimierung der Erkennungsschwelle. Sie müssen eine Grenze für die Anzahl der Sprünge festlegen, nach der sie zugeben, dass wahrscheinlich eine Eigentumsänderung stattgefunden hat und die Verbindung zu einem vorherigen Coinjoin ignoriert werden sollte. Die Bestimmung dieser Schwelle ist jedoch riskant: Jede Erweiterung der beobachteten Anzahl von Sprüngen erhöht exponentiell das Volumen der falsch positiven Ergebnisse, d.h. Personen, die fälschlicherweise als Teilnehmer an einem Coinjoin markiert werden, obwohl die Transaktion tatsächlich von jemand anderem durchgeführt wurde. Dieses Szenario birgt ein erhebliches Risiko für diese Unternehmen, da falsch positive Ergebnisse zu Unzufriedenheit führen können, was betroffene Kunden zur Konkurrenz treiben kann. Langfristig führt eine zu ambitionierte Erkennungsschwelle dazu, dass eine Plattform mehr Kunden verliert als ihre Konkurrenten, was ihre Lebensfähigkeit gefährden könnte. Es ist daher eine Herausforderung für diese Plattformen, die Anzahl der beobachteten Sprünge zu erhöhen, und 4 ist oft eine ausreichende Anzahl, um ihre Analysen zu kontern.

Daher tritt **der häufigste Anwendungsfall für Ricochet auf, wenn es notwendig ist, eine frühere Teilnahme an einem Coinjoin auf einer UTXO zu verschleiern, die Ihnen gehört**. Idealerweise sollte man vermeiden, Bitcoins, die an einem Coinjoin teilgenommen haben, an regulierte Einrichtungen zu übertragen. Falls jedoch keine andere Option besteht, insbesondere in der Dringlichkeit, Bitcoins in Fiat-Währung umzuwandeln, bietet Ricochet eine effektive Lösung.

## Wie funktioniert Ricochet in der Samourai Wallet?
Ricochet ist einfach eine Methode, bei der man Bitcoins an sich selbst sendet. Es ist daher durchaus möglich, ein Ricochet manuell ohne Verwendung eines spezialisierten Tools zu simulieren. Für diejenigen, die den Prozess jedoch automatisieren möchten und von einem polierteren Ergebnis profitieren möchten, ist das Ricochet-Tool, das über die Samourai Wallet-Anwendung verfügbar ist, eine gute Lösung.

Da der Service auf Samourai kostenpflichtig ist, fallen für ein Ricochet eine Gebühr von `100.000 Sats` als Servicegebühr sowie Mining-Gebühren an. Daher wird seine Verwendung eher für Überweisungen von größeren Beträgen empfohlen.

Die Samourai-Anwendung bietet zwei Varianten von Ricochet:
- Das verstärkte Ricochet oder "gestaffelte Lieferung" bietet den Vorteil, die Samourai-Servicegebühren auf fünf aufeinanderfolgende Transaktionen zu verteilen. Diese Option stellt auch sicher, dass jede Transaktion zu einer anderen Zeit gesendet und in einem anderen Block aufgezeichnet wird, was dem Verhalten eines Eigentumswechsels nahekommt. Obwohl langsamer, ist diese Methode für diejenigen bevorzugt, die es nicht eilig haben, da sie die Effizienz von Ricochet maximiert, indem sie seine Widerstandsfähigkeit gegen Chain-Analysen stärkt.
- Das klassische Ricochet, das darauf ausgelegt ist, die Operation schnell auszuführen, indem alle Transaktionen innerhalb eines reduzierten Zeitintervalls gesendet werden. Diese Methode bietet daher weniger Privatsphäre und eine geringere Widerstandsfähigkeit gegenüber Analysen im Vergleich zur verstärkten Methode. Sie sollte nur für dringende Überweisungen bevorzugt werden.

## Wie führt man ein Ricochet in der Samourai Wallet durch?
Um eine Ricochet-Transaktion mit der Samourai Wallet-Anwendung durchzuführen, folgen Sie unserem Video-Tutorial:
![Ricochet YouTube Video-Tutorial](https://youtu.be/Gsz0zuVo3N4)

Wenn Sie die in diesem Tutorial durchgeführten Ricochet-Transaktionen studieren möchten, finden Sie sie hier:
- Die erste Ricochet-Transaktion: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Die letzte Ricochet-Transaktion: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)

**Externe Ressourcen:**
- https://docs.samourai.io/en/wallet/features/ricochet
- https://samouraiwallet.com/ricochet
