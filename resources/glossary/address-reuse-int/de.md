---
term: ADDRESS REUSE (INT)
---

Die Wiederverwendung von Adressen wird als "intern" bezeichnet, wenn sie innerhalb derselben Transaktion sowohl als Eingabe als auch als Ausgabe auftritt. In dieser Konfiguration ist die interne Adresswiederverwendung eine Heuristik der Blockchain-Analyse, die eine plausible Hypothese über das Wechselgeld der Transaktion zulässt. Tatsächlich, wenn es zwei Ausgaben gibt und eine davon dieselbe Empfangsadresse wie die Eingabe verwendet, dann ist es wahrscheinlich, dass die zweite Ausgabe das Eigentum des ursprünglichen Benutzers verlässt. Die Ausgabe mit der wiederverwendeten Adresse stellt wahrscheinlich das Wechselgeld dar.

![](../../dictionnaire/assets/10.png)