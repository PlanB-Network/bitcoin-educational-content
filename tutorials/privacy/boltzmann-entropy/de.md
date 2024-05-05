---
name: Boltzmann Calculator
description: Verstehen Sie das Konzept der Entropie und wie man Boltzmann verwendet
---
![cover](assets/cover.webp)

***WARNUNG:** Nach der Verhaftung der Gründer von Samourai Wallet und der Beschlagnahme ihrer Server am 24. April ist die Website KYCP.org derzeit nicht zugänglich. Das Gitlab, das den Python Boltzmann Calculator Code hostete, wurde ebenfalls beschlagnahmt. Derzeit ist es nicht mehr möglich, dieses Tool herunterzuladen. Es besteht jedoch die Möglichkeit, dass der Code in den kommenden Wochen von anderen neu veröffentlicht wird. In der Zwischenzeit können Sie von diesem Tutorial profitieren, um die Funktionsweise des Boltzmann Calculators zu verstehen. Die von diesem Tool bereitgestellten Indikatoren sind auf jede Bitcoin-Transaktion anwendbar und können auch manuell berechnet werden. Ich werde Ihnen alle notwendigen Berechnungen in diesem Tutorial zur Verfügung stellen. Wenn Sie das Python-Tool bereits auf Ihrem Gerät heruntergeladen haben oder ein RoninDojo verwenden, können Sie das Tool weiterhin nutzen und diesem Tutorial wie gewohnt folgen, es funktioniert immer noch.*

*Wir verfolgen die Entwicklungen in diesem Fall sowie die Entwicklungen bezüglich der zugehörigen Tools genau. Seien Sie versichert, dass wir dieses Tutorial aktualisieren werden, sobald neue Informationen verfügbar sind.*

_Dieses Tutorial wird nur zu Bildungs- und Informationszwecken bereitgestellt. Wir befürworten oder ermutigen die Verwendung dieser Tools zu kriminellen Zwecken nicht. Es liegt in der Verantwortung jedes Benutzers, die Gesetze in seiner Gerichtsbarkeit zu beachten._

---

Der Boltzmann Calculator ist ein Werkzeug zur Analyse einer Bitcoin-Transaktion, indem es deren Entropieniveau zusammen mit anderen fortgeschrittenen Metriken misst. Es bietet Einblicke in die Verbindungen zwischen den Eingaben und Ausgaben einer Transaktion. Diese Indikatoren bieten eine quantifizierte Bewertung der Privatsphäre einer Transaktion und helfen, potenzielle Fehler zu identifizieren.

Dieses Python-Tool wurde von den Teams bei Samourai Wallet und OXT entwickelt, kann aber für jede Bitcoin-Transaktion verwendet werden.

## Wie verwendet man den Boltzmann Calculator?
Um den Boltzmann Calculator zu verwenden, stehen Ihnen zwei Optionen zur Verfügung. Die erste ist, das Python-Tool direkt auf Ihrem Gerät zu installieren. Alternativ können Sie sich für die Website KYCP.org (_Know Your Coin Privacy_) entscheiden, die eine vereinfachte Nutzungsplattform bietet. Für [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2)-Nutzer, beachten Sie, dass dieses Tool bereits in Ihren Knoten integriert ist.

Die Verwendung der KYCP-Seite ist ganz einfach: Geben Sie einfach den Transaktionsidentifikator (TXID), den Sie analysieren möchten, in die Suchleiste ein und drücken Sie `ENTER`.
![KYCP](assets/1.webp)
Dann finden Sie verschiedene Informationen über die Transaktion, einschließlich der Verbindungen zwischen den Eingaben und Ausgaben. Klicken Sie auf `deterministische Verbindungen`.
![KYCP](assets/2.webp)
Sie gelangen auf die Seite, die den Indikatoren des Boltzmann Calculators gewidmet ist.
![KYCP](assets/3.webp)
Für diejenigen, die das Tool direkt von ihrem RoninDojo-Knoten aus verwenden möchten, ist es über `RoninCLI > Samourai Toolkit > Boltzmann Calculator` zugänglich.

Wie bei der KYCP.org-Seite müssen Sie, sobald das Python-Tool installiert ist, einfach den TXID der Transaktion, die Sie analysieren möchten, einfügen.

![KYCP](assets/7.webp)

Drücken Sie dann die `ENTER`-Taste, um die Ergebnisse zu erhalten.

![KYCP](assets/8.webp)

## Was sind die Indikatoren des Boltzmann Calculators?
### Kombinationen / Interpretationen:
Der erste Indikator, den die Software berechnet, ist die Gesamtzahl der möglichen Kombinationen, angegeben unter `nb combinations` oder `interpretations` im Tool.

Unter Berücksichtigung der Werte der in der Transaktion beteiligten UTXOs berechnet dieser Indikator die Anzahl der Wege, auf denen die Eingaben den Ausgaben zugeordnet werden können. Mit anderen Worten, er bestimmt die Anzahl der plausiblen Interpretationen, die eine Transaktion aus der Perspektive eines externen Beobachters, der sie analysiert, hervorrufen kann.
Zum Beispiel präsentiert ein Coinjoin, strukturiert nach dem Whirlpool 5x5-Modell, `1.496` mögliche Kombinationen: ![KYCP](assets/4.webp)
Ein Whirlpool Surge Cycle 8x8-Coinjoin bietet andererseits `9.934.563` mögliche Interpretationen: ![KYCP](assets/5.webp)
Im Gegensatz dazu wird eine traditionellere Transaktion mit 1 Eingabe und 2 Ausgaben nur eine einzige Interpretation präsentieren: ![KYCP](assets/6.webp)

### Entropie:
Der zweite berechnete Indikator ist die Entropie einer Transaktion, bezeichnet mit `Entropy`.
Im allgemeinen Kontext der Kryptographie und Information ist Entropie ein quantitatives Maß für die Unsicherheit oder Unvorhersehbarkeit, die mit einer Datenquelle oder einem zufälligen Prozess verbunden ist. Mit anderen Worten, Entropie ist eine Methode, um zu messen, wie schwierig es ist, Informationen vorherzusagen oder zu erraten.

Im spezifischen Kontext der Kettenanalyse ist Entropie auch der Name eines Indikators, der von der Shannon-Entropie abgeleitet und [von LaurentMT erfunden wurde](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), der mit dem Boltzmann-Tool berechnet wird.

Wenn eine Transaktion eine hohe Anzahl möglicher Kombinationen aufweist, ist es oft relevanter, auf ihre Entropie zu verweisen. Dieser Indikator ermöglicht es, das fehlende Wissen der Analysten über die genaue Konfiguration der Transaktion zu messen. Mit anderen Worten, je höher die Entropie, desto schwieriger wird die Aufgabe für Analysten, Bitcoin-Bewegungen zwischen Eingängen und Ausgängen zu identifizieren.

In der Praxis zeigt die Entropie, ob aus der Perspektive eines externen Beobachters eine Transaktion mehrere mögliche Interpretationen zulässt, basierend allein auf den Beträgen von Eingängen und Ausgängen, ohne andere externe oder interne Muster und Heuristiken zu berücksichtigen. Eine hohe Entropie ist dann gleichbedeutend mit besserer Vertraulichkeit für die Transaktion.

Entropie wird als der binäre Logarithmus der Anzahl möglicher Kombinationen definiert. Hier ist die verwendete Formel:
```bash
E: die Entropie der Transaktion
C: die Anzahl möglicher Kombinationen für die Transaktion

E = log2(C)
```

In der Mathematik entspricht der binäre Logarithmus (Basis-2-Logarithmus) der inversen Operation des Potenzierens von 2. Mit anderen Worten, der binäre Logarithmus von `x` ist der Exponent, zu dem `2` erhoben werden muss, um `x` zu erhalten. Dieser Indikator wird somit in Bits ausgedrückt.

Nehmen wir das Beispiel der Berechnung der Entropie für eine Coinjoin-Transaktion, die nach dem Whirlpool 5x5-Modell strukturiert ist, das, wie zuvor erwähnt, eine Anzahl möglicher Kombinationen von `1.496` bietet:
```bash
C = 1.496
E = log2(1.496)
E = 10,5469 Bits
```
Somit zeigt diese Coinjoin-Transaktion eine Entropie von `10,5469 Bits`, was als sehr zufriedenstellend betrachtet wird. Je höher dieser Wert, desto mehr unterschiedliche Interpretationen lässt die Transaktion zu, wodurch ihr Datenschutzniveau gestärkt wird.
Für eine 8x8-Coinjoin-Transaktion, die `9.934.563` Interpretationen bietet, wäre die Entropie:
```bash
C = 9.934.563
E = log2(9.934.563)
E = 23,244 Bits
```

Nehmen wir ein weiteres Beispiel mit einer konventionelleren Transaktion, die einen Eingang und zwei Ausgänge aufweist: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Im Fall dieser Transaktion ist die einzige mögliche Interpretation: `(In.0) > (Out.0 ; Out.1)`. Folglich wird ihre Entropie auf `0` festgelegt:
```bash
C = 1
E = log2(1)
E = 0 Bits
```

### Effizienz:
Der dritte Indikator, der vom Boltzmann-Rechner bereitgestellt wird, heißt `Wallet Efficiency`. Dieser Indikator bewertet die Effizienz der Transaktion, indem er sie mit der optimalen Transaktion vergleicht, die in einer identischen Konfiguration denkbar ist.
Dies führt uns zur Diskussion des Konzepts der maximalen Entropie, die der höchsten Entropie entspricht, die eine spezifische Transaktionsstruktur theoretisch erreichen könnte. Die Effizienz der Transaktion wird dann berechnet, indem diese maximale Entropie mit der tatsächlichen Entropie der analysierten Transaktion konfrontiert wird.
Die verwendete Formel lautet wie folgt:
```bash
ER: die tatsächliche Entropie der Transaktion ausgedrückt in Bits
EM: die maximal mögliche Entropie für eine gegebene Transaktionsstruktur ausgedrückt in Bits
Ef: die Effizienz der Transaktion in Bits

Ef = ER - EM
```

Zum Beispiel, für eine Whirlpool 5x5 Typ Coinjoin-Struktur, wird die maximale Entropie auf `10.5469` festgelegt:
```bash
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 Bits
```

Dieser Indikator wird auch als Prozentsatz ausgedrückt, seine Formel lautet dann:
```bash
CR: die tatsächliche Anzahl möglicher Kombinationen
CM: die maximale Anzahl möglicher Kombinationen mit derselben Struktur
Ef: die Effizienz ausgedrückt als Prozentsatz

Ef = CR / CM
Ef = 1.496 / 1.496
Ef = 100%
```

Eine Effizienz von `100%` zeigt also an, dass die Transaktion ihr Potenzial für Privatsphäre gemäß ihrer Struktur maximiert.

### Entropiedichte:
Der vierte Indikator ist die Entropiedichte, notiert im Werkzeug `Entropiedichte`. Sie bietet eine Perspektive auf die Entropie in Bezug auf jeden Input oder Output der Transaktion. Dieser Indikator erweist sich als nützlich für die Bewertung und den Vergleich der Effizienz von Transaktionen unterschiedlicher Größe. Um sie zu berechnen, teilt man einfach die Gesamtentropie der Transaktion durch die Gesamtzahl der beteiligten Inputs und Outputs:
```bash
ED: die Entropiedichte ausgedrückt in Bits
E: die Entropie der Transaktion ausgedrückt in Bits
T: die Gesamtzahl der Inputs und Outputs in der Transaktion

ED = E / T
```

Nehmen wir das Beispiel eines Whirlpool 5x5 Coinjoin:
```bash
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 Bits
```

Berechnen wir auch die Entropiedichte für einen Whirlpool 8x8 Coinjoin:
```bash
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Boltzmann-Score:
Das fünfte Informationsstück, das vom Boltzmann-Rechner geliefert wird, ist die Tabelle der Übereinstimmungswahrscheinlichkeiten zwischen den Inputs und Outputs. Diese Tabelle gibt durch den Boltzmann-Score die bedingte Wahrscheinlichkeit an, dass ein spezifischer Input mit einem gegebenen Output in Verbindung steht.

Es handelt sich also um ein quantitatives Maß für die bedingte Wahrscheinlichkeit, dass eine Verbindung zwischen einem Input und einem Output in einer Transaktion auftritt, basierend auf dem Verhältnis der Anzahl günstiger Vorkommnisse dieses Ereignisses zur Gesamtzahl möglicher Vorkommnisse in einer Menge von Interpretationen.

Nehmen wir wieder das Beispiel eines Whirlpool-Coinjoin, würde die Tabelle der bedingten Wahrscheinlichkeiten die Chancen einer Verknüpfung zwischen jedem Input und Output hervorheben und ein quantitatives Maß für die Mehrdeutigkeit der Verbindungen in der Transaktion liefern:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Eingabe 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Eingabe 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Eingabe 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Hier können wir deutlich sehen, dass jede Eingabe die gleiche Chance hat, mit jedem Ausgang assoziiert zu werden, was die Vertraulichkeit der Transaktion erhöht.
Die Berechnung des Boltzmann-Scores erfolgt durch Division der Anzahl der Interpretationen, in denen ein bestimmtes Ereignis auftritt, durch die Gesamtzahl der verfügbaren Interpretationen. Um also den Score zu bestimmen, der Eingabe Nr. 0 mit Ausgang Nr. 3 (`512` Interpretationen) verbindet, wird folgendes Verfahren verwendet:
```bash
Interpretationen (IN.0 > OUT.3) = 512
Gesamtinterpretationen = 1496
Score = 512 / 1496 = 34%
```

Nehmen wir das Beispiel eines Whirlpool 8x8 Coinjoin (Surge-Zyklus), würde die Boltzmann-Tabelle so aussehen:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Jedoch ist die Situation bei einer einfachen Transaktion mit einer einzelnen Eingabe und zwei Ausgängen anders:

| %       | Ausgang 0 | Ausgang 1 |
|---------|-----------|-----------|
| Eingabe 0 | 100%     | 100%     |
Hier wird beobachtet, dass die Wahrscheinlichkeit für jedes Ergebnis, von Eingabe Nr. 0 zu stammen, bei `100%` liegt. Eine niedrigere Wahrscheinlichkeit bedeutet somit eine größere Privatsphäre, indem die direkten Verbindungen zwischen Eingaben und Ausgaben verwässert werden.
### Deterministische Verbindungen:
Das sechste bereitgestellte Informationsstück ist die Anzahl der deterministischen Verbindungen, ergänzt durch das Verhältnis dieser Verbindungen. Dieser Indikator offenbart, wie viele Verbindungen zwischen den Eingaben und Ausgaben in der analysierten Transaktion unbestreitbar sind, mit einer Wahrscheinlichkeit von `100%`. Das Verhältnis bietet andererseits eine Perspektive auf das Gewicht dieser deterministischen Verbindungen innerhalb der gesamten Menge an Transaktionsverbindungen.
Zum Beispiel hat eine Whirlpool-Typ-Coinjoin-Transaktion keine deterministischen Verbindungen und zeigt daher einen Indikator und ein Verhältnis von `0%`. Im Gegensatz dazu ist bei unserer zweiten einfachen untersuchten Transaktion (mit einer Eingabe und zwei Ausgaben) der Indikator auf `2` gesetzt und das Verhältnis erreicht `100%`. Somit signalisiert ein Null-Indikator eine ausgezeichnete Vertraulichkeit aufgrund der Abwesenheit von direkten und unbestreitbaren Verbindungen zwischen Eingaben und Ausgaben.

**Externe Ressourcen:**

- Boltzmann Code auf Samourai
- [Bitcoin-Transaktionen & Privatsphäre (Teil I) von Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin-Transaktionen & Privatsphäre (Teil II) von Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin-Transaktionen & Privatsphäre (Teil III) von Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP-Website
- [Medium-Artikel zur Einführung in das Boltzmann-Skript von Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)