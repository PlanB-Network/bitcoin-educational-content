---
term: CHECKSUM
---

Ein Checksum ist ein berechneter Wert aus einem Datensatz, der verwendet wird, um die Integrität und Gültigkeit dieser Daten während ihrer Übertragung oder Speicherung zu überprüfen. Checksum-Algorithmen sind darauf ausgelegt, zufällige Fehler oder unbeabsichtigte Veränderungen der Daten, wie Übertragungsfehler oder Dateikorruptionen, zu erkennen. Es existieren verschiedene Arten von Checksum-Algorithmen, wie Paritätsprüfungen, modulare Checksums, kryptografische Hashfunktionen oder BCH-Codes (*Bose, Ray-Chaudhuri und Hocquenghem*).

Bei Bitcoin werden Checksums auf Anwendungsebene verwendet, um die Integrität von Empfangsadressen sicherzustellen. Eine Checksum wird aus dem Payload einer Benutzeradresse berechnet und dann dieser Adresse hinzugefügt, um mögliche Fehler bei ihrer Eingabe zu erkennen. Eine Checksum ist auch in Wiederherstellungsphrasen (Mnemonic) vorhanden.

> ► *Die englische Übersetzung von "somme de contrôle" ist "checksum". Es ist allgemein akzeptiert, den Begriff "checksum" direkt auf Deutsch zu verwenden.*