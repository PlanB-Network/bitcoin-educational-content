---
term: INDEX (SCHLÜSSEL)
---

Bezieht sich im Zusammenhang mit einem HD-Portfolio auf die fortlaufende Nummer, die einem aus einem übergeordneten Schlüssel erzeugten untergeordneten Schlüssel zugewiesen wird. Dieser Index wird in Kombination mit dem übergeordneten Schlüssel und dem übergeordneten Zeichenfolgencode verwendet, um eindeutige untergeordnete Schlüssel deterministisch abzuleiten. Er ermöglicht eine strukturierte Organisation und reproduzierbare Erzeugung mehrerer Paare von Schwesterschlüsseln aus einem einzigen übergeordneten Schlüssel. Es handelt sich um eine 32-Bit-Ganzzahl, die in der Ableitungsfunktion `HMAC-SHA512` verwendet wird. Diese Zahl kann zur Unterscheidung von Unterschlüsseln innerhalb eines HD-Portfolios verwendet werden.