---
term: BIP44

---
Ein Verbesserungsvorschlag, der eine standardmäßige hierarchische Ableitungsstruktur für HD-Wallets einführt. BIP44 baut auf den Grundsätzen von BIP32 für die Schlüsselableitung und auf BIP43 für die Verwendung des Feldes "Zweck" auf. Es führt eine fünfstufige Ableitungsstruktur ein: `m / Zweck' / coin_type' / account' / change / address_index`. Hier sind die Einzelheiten der einzelnen Ebenen:


- m /" bezeichnet den privaten Hauptschlüssel. Er ist einzigartig für eine Brieftasche und kann keine Geschwister in der gleichen Tiefe haben. Der Hauptschlüssel wird direkt vom Seed der Wallet abgeleitet;
- m / Zweck' /` gibt den Zweck der Ableitung an, der zur Identifizierung der befolgten Norm beiträgt. Dieses Feld ist in BIP43 beschrieben. Wenn die Brieftasche beispielsweise dem Standard BIP84 (SegWit V0) folgt, lautet der Index "84";
- m / Zweck' / coin-type' /` gibt die Art der Kryptowährung an. Dies ermöglicht eine klare Unterscheidung zwischen Zweigen, die einer Kryptowährung gewidmet sind, und solchen, die einer anderen Kryptowährung in einer Multi-Coin-Wallet gewidmet sind. Der Bitcoin gewidmete Index ist `0'`;
- m / Zweck' / Münzart' / Konto' /` gibt die Kontonummer an. Diese Tiefe ermöglicht eine einfache Unterscheidung und Organisation einer Brieftasche in verschiedene Konten. Diese Konten werden beginnend mit `0'` nummeriert. Erweiterte Schlüssel (`xpub`, `xprv`...) befinden sich in dieser Tiefe;
- m / Zweck' / Münzart' / Konto' / Wechselgeld /` bezeichnet die Kette. Jedes Konto, wie in Tiefe 3 definiert, hat zwei Ketten in Tiefe 4: eine externe Kette und eine interne Kette (auch "change" genannt). Aus der externen Kette werden Adressen abgeleitet, die für die öffentliche Kommunikation bestimmt sind, d. h. die Adressen, die uns angeboten werden, wenn wir in unserer Brieftaschensoftware auf "Empfangen" klicken. Aus der internen Kette werden Adressen abgeleitet, die nicht für den öffentlichen Austausch bestimmt sind, d. h. in erster Linie Wechseladressen. Die externe Kette wird mit dem Index "0" und die interne Kette mit dem Index "1" gekennzeichnet. Sie werden feststellen, dass wir ab dieser Tiefe keine gehärtete Ableitung mehr durchführen, sondern eine normale Ableitung (es gibt kein Hochkomma). Dank dieses Mechanismus sind wir in der Lage, alle untergeordneten öffentlichen Schlüssel von ihrem "xpub" abzuleiten;
- m / Zweck" / "Münzart" / "Konto" / "Änderung" / "Adressindex" gibt einfach die Nummer der empfangenden Adresse und ihr Schlüsselpaar an, um sie von ihren Geschwistern in der gleichen Tiefe auf dem gleichen Zweig zu unterscheiden. Zum Beispiel hat die erste abgeleitete Adresse den Index `0`, die zweite Adresse den Index `1`, und so weiter...

Wenn meine Empfangsadresse zum Beispiel den Ableitungspfad `m / 86' / 0' / 0' / 0 / 5` hat, können wir folgende Informationen ableiten:


- 86" zeigt an, dass wir dem Ableitungsstandard von BIP86 (Taproot oder SegWitV1) folgen;
- 0'' bedeutet, dass es sich um eine Bitcoin-Adresse handelt;
- die Zahl "0" zeigt an, dass es sich um das erste Konto der Brieftasche handelt;
- 0" bedeutet, dass es sich um eine externe Adresse handelt;
- 5" bedeutet, dass es sich um die sechste externe Adresse dieses Kontos handelt.

![](../../dictionnaire/assets/18.webp)