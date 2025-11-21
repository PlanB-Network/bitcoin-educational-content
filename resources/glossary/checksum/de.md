---
term: CHECKSUM
---

Die Prüfsumme ist ein Wert, der aus einer Reihe von Daten berechnet wird, um die Integrität und Gültigkeit dieser Daten während der Übertragung oder Speicherung zu überprüfen. Prüfsummenalgorithmen sind so konzipiert, dass sie versehentliche Fehler oder unbeabsichtigte Änderungen von Daten, wie Übertragungsfehler oder Dateibeschädigungen, erkennen. Es gibt verschiedene Arten von Prüfsummenalgorithmen, z. B. Paritätsprüfungen, modulare Prüfsummen, kryptografische Hash-Funktionen oder BCH-Codes (*Bose, Ray-Chaudhuri und Hocquenghem*).


Bei Bitcoin werden auf der Anwendungsebene Prüfsummen verwendet, um die Integrität der Empfangsadressen sicherzustellen. Eine Prüfsumme wird aus der Nutzlast des Address eines Benutzers berechnet und dann zu diesem Address hinzugefügt, um etwaige Fehler in der Eingabe zu erkennen. Eine Prüfsumme ist auch in Wiederherstellungsphrasen (Mnemonics) enthalten.


> es ist allgemein üblich, den englischen Begriff "checksum" direkt im Französischen zu verwenden