---
term: INDEX (SCHLÜSSELNUMMER)
---

Im Kontext eines HD-Wallets bezieht es sich auf die sequenzielle Nummer, die einem von einem Elternschlüssel generierten Kinderschlüssel zugewiesen wird. Dieser Index wird in Kombination mit dem Elternschlüssel und dem Eltern-Chain-Code verwendet, um eindeutige Kinderschlüssel deterministisch abzuleiten. Es ermöglicht eine strukturierte Organisation und die reproduzierbare Generierung mehrerer Geschwister-Kinderschlüsselpaare aus demselben Elternschlüssel. Es handelt sich um eine 32-Bit-Ganzzahl, die in der `HMAC-SHA512` Ableitungsfunktion verwendet wird. Diese Nummer unterscheidet also Geschwister-Kinderschlüssel innerhalb eines HD-Wallets.