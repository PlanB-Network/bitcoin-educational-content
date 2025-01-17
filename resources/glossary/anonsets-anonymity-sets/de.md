---
term: ANONSETS (ANONYMITÄTSSETS)

---
Anonsets dienen als Indikatoren zur Bewertung des Datenschutzniveaus eines bestimmten UTXO. Genauer gesagt messen sie die Anzahl der ununterscheidbaren UTXOs innerhalb der Menge, die die untersuchte Münze enthält. Da eine Gruppe identischer UTXOs erforderlich ist, werden Anonsets im Allgemeinen innerhalb eines Zyklus von Coinjoins berechnet. Sie ermöglichen gegebenenfalls eine Beurteilung der Qualität der Coinjoins. Ein großes Anonset bedeutet ein erhöhtes Maß an Anonymität, da es schwierig wird, ein bestimmtes UTXO innerhalb der Menge zu unterscheiden. Es gibt zwei Arten von Anonsets:


- Die voraussichtliche Anonymität;
- Die retrospektive Anonymität.

Die erste zeigt die Größe der Gruppe an, in der der untersuchte UTXO versteckt ist, wobei der UTXO am Eingang bekannt ist. Mit diesem Indikator lässt sich der Widerstand der Privatsphäre der Münze gegen eine Analyse von der Vergangenheit zur Gegenwart (Eingabe zur Ausgabe) messen. Im Englischen heißt dieser Indikator "*forward anonset*" oder "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Der zweite Indikator gibt die Anzahl der möglichen Quellen für eine bestimmte Münze an, wobei der UTXO am Ausgang bekannt ist. Mit diesem Indikator lässt sich der Widerstand der Privatsphäre der Münze gegen eine Analyse von der Gegenwart in die Vergangenheit (Ausgang zu Eingang) messen. Im Englischen heißt dieser Indikator "*backward anonset*" oder "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> im Französischen ist es allgemein üblich, den Begriff "anonset" zu verwenden Er könnte jedoch auch mit "ensemble d'anonymat" oder "potentiel d'anonymat" übersetzt werden Sowohl im Englischen als auch im Französischen wird manchmal auch der Begriff "score" für Anonsets verwendet (prospective score und retrospective score).*