---
term: BIP11
---

BIP, eingeführt von Gavin Andresen im März 2012, schlägt eine standardisierte Methode zur Erstellung von Multisignatur-Transaktionen auf Bitcoin vor. Dieser Vorschlag zielt darauf ab, die Sicherheit von Bitcoins zu erhöhen, indem mehrere Signaturen zur Validierung einer Transaktion erforderlich sind. BIP11 führt einen neuen Typ von Skript ein, genannt "M-von-N Multisig", wobei `M` die Mindestanzahl an Signaturen darstellt, die von `N` möglichen öffentlichen Schlüsseln benötigt werden. Dieser Standard nutzt den `OP_CHECKMULTISIG` Opcode, der bereits in Bitcoin existiert, aber zuvor nicht mit den Standardisierungsregeln der Knoten konform war. Obwohl dieser Skripttyp für tatsächliche Multisig-Wallets nicht mehr häufig verwendet wird, zugunsten von P2SH oder P2WSH, bleibt seine Nutzung möglich. Er wird insbesondere in Meta-Protokollen wie Stamps verwendet. Knoten können jedoch wählen, diese P2MS-Transaktionen nicht weiterzuleiten, mit dem Parameter `permitbaremultisig=0`.

> ► *Heutzutage ist dieser Standard als "bare-multisig" oder "P2MS" bekannt.*