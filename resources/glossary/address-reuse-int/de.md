---
term: ADRESSWIEDERVERWENDUNG (INT)

---
Die Wiederverwendung von Adressen wird als "intern" bezeichnet, wenn sie innerhalb ein und derselben Transaktion sowohl als Eingabe als auch als Ausgabe erfolgt. In dieser Konfiguration ist die interne Adresswiederverwendung eine Heuristik der Blockchain-Analyse, die eine plausible Hypothese über die Änderung der Transaktion zulässt. Wenn es nämlich zwei Ausgänge gibt und einer davon dieselbe Empfangsadresse wie der Eingang verwendet, dann ist es wahrscheinlich, dass der zweite Ausgang den Besitz des ursprünglichen Nutzers verlässt. Die Ausgabe mit der wiederverwendeten Adresse stellt wahrscheinlich die Änderung dar.

![](../../dictionnaire/assets/10.webp)