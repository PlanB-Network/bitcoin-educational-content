---
term: EMPFANGSADRESSE

---
Informationen, die zum Empfang von Bitcoins verwendet werden. Eine Adresse wird in der Regel durch Hashing eines öffentlichen Schlüssels mit `SHA256` und `RIMPEMD160` und Hinzufügen von Metadaten zu diesem Digest erstellt. Die öffentlichen Schlüssel, die verwendet werden, um eine Empfangsadresse zu konstruieren, sind Teil der Brieftasche des Benutzers und werden daher von seinem Seed abgeleitet. SegWit-Adressen setzen sich beispielsweise aus den folgenden Informationen zusammen:


- Ein HRP zur Bezeichnung von "bitcoin": "bc";
- Ein Trennzeichen: "1";
- Die verwendete Version von SegWit: `q` oder `p`;
- Die Nutzlast: der Digest des öffentlichen Schlüssels (oder direkt der öffentliche Schlüssel im Fall von Taproot);
- Die Prüfsumme: ein BCH-Code.

Eine Empfangsadresse kann jedoch auch etwas anderes darstellen, je nach dem verwendeten Skriptmodell. P2SH-Adressen werden zum Beispiel mit dem Hash des Skripts erstellt. Taproot-Adressen hingegen enthalten den geänderten öffentlichen Schlüssel direkt, ohne ihn zu hashen.

Eine Empfangsadresse kann in Form einer alphanumerischen Zeichenfolge oder eines QR-Codes dargestellt werden. Jede Adresse kann mehrfach verwendet werden, wovon jedoch dringend abgeraten wird. Um ein gewisses Maß an Privatsphäre zu wahren, wird empfohlen, jede Bitcoin-Adresse nur einmal zu verwenden. Für jeden Zahlungseingang in die eigene Wallet sollte eine neue Adresse generiert werden. Eine Adresse wird in `Bech32` für SegWit V0 Adressen, in `Bech32m` für SegWit V1 Adressen und in `Base58check` für Legacy Adressen kodiert. Technisch gesehen bedeutet der Erhalt von Bitcoins, dass man den privaten Schlüssel besitzt, der mit einem öffentlichen Schlüssel (und somit einer Adresse) verbunden ist. Wenn jemand Bitcoins erhält, aktualisiert der Absender die bestehende Beschränkung seiner Ausgaben, so dass nur noch der Empfänger über diese Befugnis verfügen kann.

![](../../dictionnaire/assets/23.webp)