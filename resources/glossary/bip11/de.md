---
term: BIP11

---
BIP, das von Gavin Andresen im März 2012 vorgestellt wurde und eine Standardmethode zur Erstellung von Transaktionen mit mehreren Signaturen in Bitcoin vorschlägt. Dieser Vorschlag zielt darauf ab, die Sicherheit von Bitcoins zu erhöhen, indem mehrere Signaturen zur Validierung einer Transaktion erforderlich sind. BIP11 führt eine neue Art von Skript ein, genannt "M-of-N multisig", wobei `M` die minimale Anzahl der erforderlichen Signaturen von `N` potentiellen öffentlichen Schlüsseln darstellt. Dieser Standard nutzt den Opcode "OP_CHECKMULTISIG", der bereits in Bitcoin existiert, aber bisher nicht mit den Standardisierungsregeln der Nodes konform war. Obwohl diese Art von Skript nicht mehr häufig für echte Multisig-Wallets verwendet wird und P2SH oder P2WSH bevorzugt wird, ist ihre Verwendung weiterhin möglich. Es wird vor allem in Meta-Protokollen wie Stamps verwendet. Die Knoten können sich jedoch dafür entscheiden, diese P2MS-Transaktionen mit dem Parameter `permitbaremultisig=0` nicht weiterzuleiten.

> heutzutage wird dieser Standard als "bare-multisig" oder "P2MS" bezeichnet