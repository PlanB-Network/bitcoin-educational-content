---
term: Anonsets (Anonymity Sets)

definition: Indikatoren, die den Datenschutzgrad eines UTXO durch Zählung der Anzahl nicht unterscheidbarer UTXOs in einem Satz messen, normalerweise nach coinjoin.
---
Anonsets dienen als Indikatoren zur Bewertung des Vertraulichkeitsgrads eines bestimmten UTXO. Genauer gesagt messen sie die Anzahl ununterscheidbarer UTXOs innerhalb der Menge, die die betrachtete Münze einschließt. Da eine Gruppe identischer UTXOs erforderlich ist, werden Anonsets in der Regel innerhalb eines Coinjoin-Zyklus berechnet. Sie ermöglichen gegebenenfalls eine Beurteilung der Qualität der Coinjoins. Ein großer Anonset bedeutet ein höheres Maß an Anonymität, da es schwierig wird, einen bestimmten UTXO innerhalb der Menge zu unterscheiden.

Es gibt zwei Arten von Anonsets: den Forward-Anonset (forward-looking metrics); und den Backward-Anonset (backward-looking metrics). Der Begriff "*score*" wird mitunter ebenfalls zur Bezeichnung von Anonsets verwendet.

Der erste gibt die Größe der Gruppe an, innerhalb derer sich der betrachtete Ausgangs-UTXO verbirgt, bei bekanntem Eingangs-UTXO. Dieser Indikator ermöglicht es, die Widerstandsfähigkeit der Vertraulichkeit der Münze gegenüber einer Analyse von der Vergangenheit zur Gegenwart (vom Eingang zum Ausgang) zu messen. Der zweite gibt die Anzahl möglicher Quellen für eine gegebene Münze an, bei bekanntem Ausgangs-UTXO. Dieser Indikator ermöglicht es, die Widerstandsfähigkeit der Vertraulichkeit der Münze gegenüber einer Analyse von der Gegenwart zur Vergangenheit (vom Ausgang zum Eingang) zu messen.










