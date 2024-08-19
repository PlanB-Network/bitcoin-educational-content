---
term: LABEL (STILLE ZAHLUNGEN)
---

Innerhalb des Protokolls für Stille Zahlungen sind Labels ganze Zahlen, die verwendet werden, um die ursprüngliche statische Adresse zu modifizieren, um viele andere statische Adressen zu erstellen. Die Verwendung dieser Labels ermöglicht die Trennung von Zahlungen, die über Stille Zahlungen gesendet werden, indem für jeden Verwendungszweck unterschiedliche statische Adressen eingesetzt werden, ohne die operationelle Belastung für die Erkennung dieser Zahlungen (Scannen) übermäßig zu erhöhen. Bob verwendet eine statische Adresse $B$, die aus zwei öffentlichen Schlüsseln besteht: $B_{\text{scan}}$ zum Scannen und $B_{\text{spend}}$ zum Ausgeben. Der Hash von $b_{\text{scan}}$ und einer ganzen Zahl $m$, skalar-multipliziert mit dem Generatorpunkt $G$, wird zum Ausgabe-öffentlichen Schlüssel $B_{\text{spend}}$ hinzugefügt, um eine Art neuen Ausgabe-öffentlichen Schlüssel $B_m$ zu erstellen:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Zum Beispiel wird der erste Schlüssel $B_1$ auf diese Weise erhalten:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Die von Bob veröffentlichte statische Adresse wird nun aus $B_{\text{scan}}$ und $B_m$ bestehen. Zum Beispiel wird die erste statische Adresse mit dem Label $1$ sein:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Wir beginnen nur ab Label $1$, weil Label $0$ für Wechselgeld reserviert ist. Alice, die Bitcoins an die von Bob bereitgestellte statische Adresse mit Label senden möchte, wird die einzigartige Zahlungsadresse $P_0$ unter Verwendung des neuen $B_1$ anstelle von $B_{\text{spend}}$ ableiten:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

In Wirklichkeit weiß Alice vielleicht gar nicht, dass Bob eine adressierte Adresse hat, da sie einfach den zweiten Teil der statischen Adresse verwendet, die er bereitgestellt hat, was in diesem Fall der Wert $B_1$ anstelle von $B_{\text{spend}}$ ist. Um nach Zahlungen zu suchen, wird Bob immer den Wert seiner ursprünglichen statischen Adresse mit $B_{\text{spend}}$ auf diese Weise verwenden:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Dann wird er einfach den Wert, den er für $P_0$ findet, von jedem Ausgang nacheinander abziehen. Er überprüft dann, ob eines der Ergebnisse dieser Subtraktionen dem Wert eines der Labels entspricht, die er in seiner Wallet verwendet. Wenn es übereinstimmt, zum Beispiel für Ausgang #4 mit dem Label $1$, bedeutet dies, dass dieser Ausgang eine Stille Zahlung ist, die mit seiner statischen Adresse mit dem Label $B_1$ verbunden ist:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Dies funktioniert, weil:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Dank dieser Methode kann Bob eine Vielzahl von statischen Adressen (mit $B_1$, $B_2$, $B_3$...), die alle von seiner Basis-statischen Adresse ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$) abgeleitet sind, verwenden, um die Verwendungen ordnungsgemäß zu trennen.

Diese Trennung von statischen Adressen ist jedoch nur aus der Perspektive der persönlichen Wallet-Verwaltung gültig, erlaubt aber keine Trennung von Identitäten. Da sie alle dasselbe $B_{\text{scan}}$ haben, ist es sehr einfach, alle statischen Adressen zusammenzufassen und zu folgern, dass sie zu einer einzigen Entität gehören.