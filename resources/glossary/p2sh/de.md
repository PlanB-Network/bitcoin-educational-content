---
term: P2SH

---
P2SH steht für *Pay to Script Hash*. Es handelt sich dabei um ein Standard-Skriptmodell, das zur Festlegung von Ausgabenbedingungen für einen UTXO verwendet wird. Im Gegensatz zu P2PK- und P2PKH-Skripten, bei denen die Ausgabenbedingungen vordefiniert sind, ermöglicht P2SH die Integration beliebiger Ausgabenbedingungen und zusätzlicher Funktionalitäten in ein Transaktionsskript.

Technisch gesehen enthält der "ScriptPubKey" bei einer P2SH-Transaktion den kryptografischen Hash eines "RedeemScript" und keine expliziten Ausgabebedingungen. Dieser Hash wird mit einem `SHA256`-Hash ermittelt. Beim Senden von Bitcoins an eine P2SH-Adresse wird das zugrundeliegende "RedeemScript" nicht offengelegt. Nur der Hash ist in der Transaktion enthalten. P2SH-Adressen sind in `Base58Check` kodiert und beginnen mit der Zahl `3`. Wenn der Empfänger die erhaltenen Bitcoins ausgeben möchte, muss er ein "DeemScript" angeben, das mit dem Hash im "ScriptPubKey" übereinstimmt, zusammen mit den erforderlichen Daten, um die Bedingungen dieses "DeemScript" zu erfüllen. In einem P2SH-Multisignatur-Skript könnte das Skript zum Beispiel Signaturen von mehreren privaten Schlüsseln erfordern.

Die Verwendung von P2SH bietet mehr Flexibilität, da sie die Erstellung beliebiger Skripte ermöglicht, ohne dass der Absender die Details kennt. P2SH wurde im Jahr 2012 mit BIP16 eingeführt.