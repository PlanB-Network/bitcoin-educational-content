---
term: INDEX (SCHLÜSSELNUMMER)

---
Im Zusammenhang mit einer HD-Wallet bezieht er sich auf die fortlaufende Nummer, die einem aus einem Elternschlüssel generierten Kindschlüssel zugeordnet ist. Dieser Index wird in Kombination mit dem übergeordneten Schlüssel und dem übergeordneten Kettencode verwendet, um eindeutige untergeordnete Schlüssel deterministisch abzuleiten. Er ermöglicht eine strukturierte Organisation und die reproduzierbare Erzeugung mehrerer Geschwister-Kind-Schlüsselpaare aus demselben übergeordneten Schlüssel. Es handelt sich um eine 32-Bit-Ganzzahl, die in der Ableitungsfunktion `HMAC-SHA512` verwendet wird. Mit dieser Nummer lassen sich also Geschwisterschlüssel innerhalb einer HD-Brieftasche unterscheiden.