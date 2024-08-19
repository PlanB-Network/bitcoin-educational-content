---
term: EMPFANGSADRESSE
---

Informationen, die verwendet werden, um Bitcoins zu empfangen. Eine Adresse wird normalerweise konstruiert, indem ein öffentlicher Schlüssel mit `SHA256` und `RIMPEMD160` gehasht und Metadaten zu diesem Digest hinzugefügt werden. Die öffentlichen Schlüssel, die zur Konstruktion einer Empfangsadresse verwendet werden, sind Teil der Wallet des Benutzers und werden daher von deren Seed abgeleitet. Zum Beispiel werden SegWit-Adressen aus den folgenden Informationen zusammengesetzt:
* Ein HRP, um "bitcoin" zu bezeichnen: `bc`;
* Ein Separator: `1`;
* Die verwendete Version von SegWit: `q` oder `p`;
* Die Nutzlast: der Digest des öffentlichen Schlüssels (oder direkt der öffentliche Schlüssel im Falle von Taproot);
* Die Prüfsumme: ein BCH-Code.

Eine Empfangsadresse kann jedoch auch etwas anderes darstellen, abhängig vom verwendeten Skriptmodell. Zum Beispiel werden P2SH-Adressen unter Verwendung des Hashs des Skripts konstruiert. Taproot-Adressen enthalten andererseits den modifizierten öffentlichen Schlüssel direkt ohne ihn zu hashen.

Eine Empfangsadresse kann in Form einer alphanumerischen Zeichenkette oder als QR-Code dargestellt werden. Jede Adresse kann mehrmals verwendet werden, aber dies ist eine stark abgeratene Praxis. Tatsächlich wird empfohlen, jede Bitcoin-Adresse nur einmal zu verwenden, um ein gewisses Maß an Privatsphäre zu wahren. Für jede eingehende Zahlung an eine Wallet sollte eine neue Adresse generiert werden. Eine Adresse wird für SegWit V0-Adressen in `Bech32`, für SegWit V1-Adressen in `Bech32m` und für Legacy-Adressen in `Base58check` kodiert. Aus technischer Sicht bedeutet das Empfangen von Bitcoins, den privaten Schlüssel zu besitzen, der mit einem öffentlichen Schlüssel (und somit einer Adresse) verbunden ist. Wenn jemand Bitcoins erhält, aktualisiert der Sender die bestehende Einschränkung für ihre Ausgaben, so dass jetzt nur noch der Empfänger diese Macht hat.

![](../../dictionnaire/assets/23.png)