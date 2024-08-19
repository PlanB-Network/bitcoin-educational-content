---
term: ANONSETS (ANONYMITÄTSSETS)
---

Anonsets dienen als Indikatoren, um das Datenschutzniveau eines bestimmten UTXO zu bewerten. Genauer gesagt messen sie die Anzahl der ununterscheidbaren UTXOs innerhalb des Sets, das die untersuchte Münze enthält. Da eine Gruppe identischer UTXOs erforderlich ist, werden Anonsets in der Regel innerhalb eines Zyklus von Coinjoins berechnet. Sie erlauben, wo angebracht, die Qualität der Coinjoins zu beurteilen. Ein großes Anonset bedeutet ein erhöhtes Maß an Anonymität, da es schwierig wird, ein spezifisches UTXO innerhalb des Sets zu unterscheiden. Es gibt zwei Arten von Anonsets:
* Das prospektive Anonymitätsset;
* Das retrospektive Anonymitätsset.

Das erste gibt die Größe der Gruppe an, unter der das untersuchte UTXO verborgen ist, wobei das UTXO beim Input bekannt ist. Dieser Indikator ermöglicht es, den Widerstand der Privatsphäre der Münze gegen eine Analyse von der Vergangenheit zur Gegenwart (Input zu Output) zu messen. Auf Englisch wird dieser Indikator als "*forward anonset*," oder "*forward-looking metrics*" bezeichnet.

![](../../dictionnaire/assets/39.png)

Das zweite gibt die Anzahl möglicher Quellen für eine bestimmte Münze an, wobei das UTXO beim Output bekannt ist. Dieser Indikator ermöglicht es, den Widerstand der Privatsphäre der Münze gegen eine Analyse von der Gegenwart zur Vergangenheit (Output zu Input) zu messen. Auf Englisch wird dieser Indikator als "*backward anonset*," oder "*backward-looking metrics*" bezeichnet.

![](../../dictionnaire/assets/40.png)

> ► *Im Französischen wird allgemein akzeptiert, den Begriff „anonset“ zu verwenden. Es könnte jedoch als „ensemble d'anonymat“ oder „potentiel d'anonymat“ übersetzt werden. Sowohl im Englischen als auch im Französischen wird manchmal auch der Begriff „score“ verwendet, um sich auf Anonsets zu beziehen (prospektiver Score und retrospektiver Score).*