---
term: WIEDERVERWENDBARER ZAHLUNGSCODE
---

In BIP47 ist ein wiederverwendbarer Zahlungscode ein statischer Identifikator, der aus einer Bitcoin-Wallet generiert wird und eine Benachrichtigungstransaktion sowie die Ableitung einzigartiger Adressen ermöglicht. Dies vermeidet die Wiederverwendung von Adressen, was zu einem Verlust der Privatsphäre führt, ohne manuell neue, ungenutzte Adressen für jede Zahlung ableiten und übermitteln zu müssen. In BIP47 werden wiederverwendbare Zahlungscodes wie folgt konstruiert:
* Byte 0 entspricht der Version;
* Byte 1 ist ein Bitfeld für das Hinzufügen von Informationen im Falle einer spezifischen Nutzung;
* Byte 2 gibt die Parität des `y` des öffentlichen Schlüssels an;
* Von Byte 3 bis Byte 34 finden Sie den `x`-Wert des öffentlichen Schlüssels;
* Von Byte 35 bis Byte 66 befindet sich der mit dem öffentlichen Schlüssel assoziierte Ketten-Code;
* Von Byte 67 bis Byte 79 gibt es eine Null-Polsterung.

Ein für Menschen lesbarer Teil (HRP) wird in der Regel am Anfang des Zahlungscodes hinzugefügt und ein Prüfsumme am Ende, und dann wird er in base58 kodiert. Die Konstruktion eines Zahlungscodes ist somit recht ähnlich der eines erweiterten Schlüssels. Hier ist mein eigener BIP47-Zahlungscode in base58 als Beispiel:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

In der PayNym-Implementierung von BIP47 können Zahlungscodes auch in Form von Identifikatoren ausgedrückt werden, die mit dem Bild eines Roboters assoziiert sind. Hier ist meiner zum Beispiel:

```text
+throbbingpond8B1
```

Die Verwendung von Zahlungscodes mit der PayNym-Implementierung ist derzeit auf Sparrow Wallet auf dem PC und auf Samourai Wallet auf Mobilgeräten verfügbar.