---
term: WIEDERVERWENDBARER ZAHLUNGSCODE

---
In BIP47 ist ein wiederverwendbarer Zahlungscode ein statischer Bezeichner, der von einer Bitcoin-Wallet generiert wird und eine Benachrichtigungstransaktion und die Ableitung eindeutiger Adressen ermöglicht. Dadurch wird die Wiederverwendung von Adressen vermieden, die zu einem Verlust der Privatsphäre führt, ohne dass für jede Zahlung manuell neue, unbenutzte Adressen abgeleitet und übertragen werden müssen. In BIP47 werden wiederverwendbare Zahlungscodes wie folgt konstruiert:


- Byte 0 entspricht der Version;
- Byte 1 ist ein Bitfeld zum Hinzufügen von Informationen für den Fall einer besonderen Verwendung;
- Byte 2 gibt die Parität des "y" des öffentlichen Schlüssels an;
- Von Byte 3 bis Byte 34 finden Sie den "x"-Wert des öffentlichen Schlüssels;
- Von Byte 35 bis Byte 66 befindet sich der Kettencode, der mit dem öffentlichen Schlüssel verbunden ist;
- Von Byte 67 bis Byte 79 gibt es kein Padding.

Am Anfang des Zahlungscodes wird in der Regel ein vom Menschen lesbarer Teil (Human-Readable Part, HRP) und am Ende eine Prüfsumme angefügt, die dann in base58 verschlüsselt werden. Der Aufbau eines Zahlungscodes ist also dem eines erweiterten Schlüssels recht ähnlich. Hier ist zum Beispiel mein eigener BIP47-Zahlungscode in base58:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

In der PayNym-Implementierung von BIP47 können die Zahlungscodes auch in Form von Identifikatoren ausgedrückt werden, die mit dem Bild eines Roboters verbunden sind. Hier ist meiner, zum Beispiel:

```text
+throbbingpond8B1
```

Die Verwendung von Zahlungscodes mit der PayNym-Implementierung ist derzeit auf Sparrow Wallet auf dem PC und auf Samourai Wallet auf dem Handy verfügbar.