---
term: P2SH
---

P2SH steht für *Pay to Script Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. Im Gegensatz zu P2PK- und P2PKH-Skripten, bei denen die Ausgabebedingungen vordefiniert sind, ermöglicht P2SH die Integration von beliebigen Ausgabebedingungen und zusätzlichen Funktionalitäten innerhalb eines Transaktionsskripts.

Technisch gesehen enthält in einer P2SH-Transaktion das `scriptPubKey` den kryptografischen Hash eines `redeemScript`, anstatt explizite Ausgabebedingungen. Dieser Hash wird mittels eines `SHA256`-Hashs erhalten. Beim Senden von Bitcoins an eine P2SH-Adresse wird das zugrundeliegende `redeemScript` nicht offengelegt. Nur sein Hash ist in der Transaktion enthalten. P2SH-Adressen sind in `Base58Check` kodiert und beginnen mit der Zahl `3`. Wenn der Empfänger die erhaltenen Bitcoins ausgeben möchte, muss er ein `redeemScript` bereitstellen, das mit dem Hash im `scriptPubKey` übereinstimmt, zusammen mit den notwendigen Daten, um die Bedingungen dieses `redeemScript` zu erfüllen. Beispielsweise könnte in einem P2SH-Multisignatur-Skript das Skript Signaturen von mehreren privaten Schlüsseln erfordern.

Die Verwendung von P2SH bietet mehr Flexibilität, da sie die Konstruktion von beliebigen Skripten ermöglicht, ohne dass der Sender die Details kennt. P2SH wurde 2012 mit BIP16 eingeführt.