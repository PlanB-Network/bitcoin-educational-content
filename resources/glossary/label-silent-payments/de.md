---
term: LABEL (STILLE ZAHLUNGEN)

---
Im Rahmen des Silent-Payments-Protokolls sind Labels ganze Zahlen, die zur Änderung der ursprünglichen statischen Adresse verwendet werden, um viele weitere statische Adressen zu erstellen. Die Verwendung dieser Labels ermöglicht die Trennung von Zahlungen, die über Silent Payments verschickt werden, indem für jeden Verwendungszweck eine andere statische Adresse verwendet wird, ohne dass der operative Aufwand für die Erkennung dieser Zahlungen (Scanning) übermäßig erhöht wird. Bob verwendet eine statische Adresse $B$, die aus zwei öffentlichen Schlüsseln besteht: $B_{\text{scan}}$ für das Scannen und $B_{\text{spend}}$ für das Ausgeben. Der Hash von $b_{\text{scan}}$ und einer ganzen Zahl $m$, skalarmultipliziert mit dem Generatorpunkt $G$, wird zum öffentlichen Ausgabenschlüssel $B_{\text{spend}$ hinzugefügt, um eine Art neuen öffentlichen Ausgabenschlüssel $B_m$ zu erzeugen:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$

Der erste Schlüssel $B_1$ zum Beispiel wird auf diese Weise gewonnen:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Die von Bob veröffentlichte statische Adresse setzt sich nun aus $B_{\text{scan}}$ und $B_m$ zusammen. Die erste statische Adresse mit der Bezeichnung $1$ lautet zum Beispiel:

$$ B = B_{\text{scan}} {\text{ ‖ } B_1 $$

Wir beginnen nur mit dem Label $1$, denn das Label $0$ ist für Änderungen reserviert. Alice, die Bitcoins an die von Bob angegebene statische Adresse senden möchte, wird die eindeutige Zahlungsadresse $P_0$ unter Verwendung des neuen $B_1$ anstelle von $B_{\text{spend}}$ ableiten:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

In Wirklichkeit weiß Alice möglicherweise nicht einmal, dass Bob eine gekennzeichnete Adresse hat, da sie einfach den zweiten Teil der von ihm angegebenen statischen Adresse verwendet, die in diesem Fall den Wert $B_1$ und nicht $B_{\text{spend}}$ hat. Um nach Zahlungen zu suchen, wird Bob auf diese Weise immer den Wert seiner ursprünglichen statischen Adresse mit $B_{\text{spend}}$ verwenden:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Dann subtrahiert er einfach den Wert, den er für $P_0$ gefunden hat, von jeder Ausgabe, eine nach der anderen. Dann prüft er, ob eines der Ergebnisse dieser Subtraktionen mit dem Wert eines der Etiketten übereinstimmt, die er in seiner Brieftasche verwendet. Wenn es z.B. für die Ausgabe Nr. 4 mit der Bezeichnung $1$ übereinstimmt, bedeutet dies, dass es sich bei dieser Ausgabe um eine stille Zahlung handelt, die mit seiner statischen Adresse $B_1$ verbunden ist:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Das funktioniert, weil:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Dank dieser Methode kann Bob eine Vielzahl von statischen Adressen (mit $B_1$, $B_2$, $B_3$...) verwenden, die alle von seiner statischen Basisadresse ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$) abgeleitet sind, um die Verwendungen ordnungsgemäß zu trennen.

Diese Trennung der statischen Adressen ist jedoch nur aus Sicht der Verwaltung der persönlichen Brieftasche gültig, ermöglicht aber keine Trennung der Identitäten. Da sie alle denselben $B_{\text{scan}}$ haben, ist es sehr einfach, alle statischen Adressen miteinander in Verbindung zu bringen und daraus zu schließen, dass sie zu einer einzigen Person gehören.