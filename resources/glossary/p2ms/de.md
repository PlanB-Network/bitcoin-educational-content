---
term: P2MS

---
P2MS steht für *Pay to Multisig*, was so viel bedeutet wie "Bezahlen für mehrere Unterschriften". Es handelt sich dabei um ein Standard-Skriptmodell, das verwendet wird, um Ausgabenbedingungen für einen UTXO festzulegen. Es ermöglicht das Sperren von Bitcoins mit mehreren öffentlichen Schlüsseln. Um diese Bitcoins auszugeben, ist eine Signatur mit einer vordefinierten Anzahl von zugehörigen privaten Schlüsseln erforderlich. Zum Beispiel beinhaltet ein "P2MS 2/3" "3" öffentliche Schlüssel mit "3" dazugehörigen geheimen privaten Schlüsseln. Um die mit diesem P2MS-Skript gesperrten Bitcoins auszugeben, ist eine Signatur mit mindestens "2" der "3" privaten Schlüssel erforderlich. Dies ist ein Schwellenwert-Sicherheitssystem.

Dieses Skript wurde 2011 von Gavin Andresen erfunden, als er die Wartung des Haupt-Bitcoin-Clients übernahm. Heute wird P2MS von einigen Anwendungen nur noch am Rande genutzt. Die große Mehrheit der modernen Multisignaturen verwendet andere Skripte wie P2SH oder P2WSH. Im Vergleich zu diesen ist P2MS extrem trivial. Die öffentlichen Schlüssel, aus denen es besteht, werden beim Empfang der Transaktion offengelegt. Die Verwendung eines P2MS ist auch teurer als andere Multisignatur-Skripte.

> ► *P2MS werden oft als "bare-multisig" bezeichnet, was mit "nackte Multisignatur" oder "rohe Multisignatur" übersetzt werden könnte. Anfang 2023 standen P2MS-Skripte im Mittelpunkt einer Kontroverse, weil sie im Rahmen des Stamps-Protokolls missbraucht wurden. Dabei wurde insbesondere auf ihre Auswirkungen auf den UTXO-Satz hingewiesen.*