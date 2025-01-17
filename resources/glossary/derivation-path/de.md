---
term: ABLEITUNGSPFAD

---
Im Zusammenhang mit hierarchisch-deterministischen (HD) Geldbörsen bezieht sich ein Ableitungspfad auf die Abfolge von Indizes, die zur Ableitung von Unterschlüsseln aus einem Hauptschlüssel verwendet werden. In BIP32 beschrieben, identifiziert dieser Pfad die Baumstruktur für die Ableitung von Unterschlüsseln. Ein Ableitungspfad wird durch eine Reihe von Indizes dargestellt, die durch Schrägstriche getrennt sind, und beginnt immer mit dem Hauptschlüssel (bezeichnet als "m/"). Ein typischer Pfad könnte zum Beispiel `m/84'/0'/0'/0/0` lauten. Jede Ableitungsebene ist mit einer bestimmten Tiefe verbunden:


- m /" bezeichnet den privaten Hauptschlüssel. Er ist einzigartig für eine Brieftasche und kann keine Geschwister in der gleichen Tiefe haben. Der Hauptschlüssel wird direkt vom Seed abgeleitet;
- m / Zweck' /` gibt den Zweck der Ableitung an, der zur Identifizierung der befolgten Norm beiträgt. Dieses Feld ist in BIP43 beschrieben. Hält sich die Brieftasche beispielsweise an den BIP84-Standard (SegWit V0), so lautet der Index "84";
- m / Zweck' / coin-type' /` gibt die Art der Kryptowährung an. Dies ermöglicht eine klare Unterscheidung zwischen Zweigen, die einer Kryptowährung gewidmet sind, und solchen, die einer anderen in einer Multi-Coin-Wallet gewidmet sind. Der Bitcoin gewidmete Index ist `0'`;
- m / Zweck' / Münzart' / Konto' /` gibt die Kontonummer an. Diese Tiefe macht es einfach, eine Brieftasche in verschiedene Konten zu unterscheiden und zu organisieren. Diese Konten werden beginnend mit `0'` nummeriert. Erweiterte Schlüssel (`xpub`, `xprv`...) sind in dieser Tiefe zu finden;
- m / Zweck' / Münzart' / Konto' / Wechselgeld /` gibt den Pfad an. Jedes Konto, wie in Tiefe 3 definiert, hat zwei Pfade in Tiefe 4: eine externe Kette und eine interne Kette (auch "change" genannt). Aus der externen Kette werden Adressen abgeleitet, die für die Öffentlichkeit bestimmt sind, d. h. die Adressen, die uns angeboten werden, wenn wir in unserer Brieftaschensoftware auf "empfangen" klicken. Aus der internen Kette werden Adressen abgeleitet, die nicht für den öffentlichen Austausch bestimmt sind, hauptsächlich Wechselgeldadressen. Die externe Kette wird mit dem Index "0" und die interne Kette mit dem Index "1" gekennzeichnet. Sie werden feststellen, dass wir ab dieser Tiefe keine gehärtete Ableitung mehr durchführen, sondern eine normale Ableitung (es gibt kein Hochkomma). Dank dieses Mechanismus sind wir in der Lage, alle untergeordneten öffentlichen Schlüssel von ihrem "xpub" abzuleiten;
- m / Zweck" / "Münzart" / "Konto" / "Änderung" / "Adressindex" gibt einfach die Nummer der empfangenden Adresse und ihr Schlüsselpaar an, um sie von ihren Geschwistern in der gleichen Tiefe auf dem gleichen Zweig zu unterscheiden. Zum Beispiel hat die erste abgeleitete Adresse den Index `0`, die zweite Adresse den Index `1`, und so weiter...

Wenn meine Empfangsadresse zum Beispiel den Ableitungspfad `m / 86' / 0' / 0' / 0 / 5` hat, können wir folgende Informationen ableiten:


- die Angabe "86" bedeutet, dass wir dem Ableitungsstandard von BIP86 (Taproot / SegWit V1) folgen;
- 0'' bedeutet, dass es sich um eine Bitcoin-Adresse handelt;
- die Zahl "0" zeigt an, dass es sich um das erste Konto der Brieftasche handelt;
- 0" bedeutet, dass es sich um eine externe Adresse handelt;
- 5" bedeutet, dass es sich um die sechste externe Adresse dieses Kontos handelt.

![](../../dictionnaire/assets/18.webp)