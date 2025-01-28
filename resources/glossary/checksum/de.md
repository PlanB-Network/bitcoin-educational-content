---
term: CHECKSUM

---
Eine Prüfsumme ist ein aus einem Datensatz berechneter Wert, der dazu dient, die Integrität und Gültigkeit dieser Daten während ihrer Übertragung oder Speicherung zu überprüfen. Prüfsummenalgorithmen sind so konzipiert, dass sie versehentliche Fehler oder unbeabsichtigte Änderungen von Daten, wie Übertragungsfehler oder Dateibeschädigungen, erkennen. Es gibt verschiedene Arten von Prüfsummenalgorithmen, z. B. Paritätsprüfungen, modulare Prüfsummen, kryptografische Hash-Funktionen oder BCH-Codes (*Bose, Ray-Chaudhuri und Hocquenghem*).

In Bitcoin werden Prüfsummen auf der Anwendungsebene verwendet, um die Integrität der empfangenen Adressen sicherzustellen. Eine Prüfsumme wird aus der Nutzlast der Adresse eines Nutzers berechnet und dann zu dieser Adresse hinzugefügt, um mögliche Fehler bei der Eingabe zu erkennen. Eine Prüfsumme ist auch in Wiederherstellungsphrasen (mnemonisch) enthalten.

> ► *Die englische Übersetzung von "somme de contrôle" ist "Prüfsumme". Es ist allgemein üblich, den Begriff "Prüfsumme" direkt im Französischen zu verwenden.*