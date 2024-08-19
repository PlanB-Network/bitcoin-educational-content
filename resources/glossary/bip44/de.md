---
term: BIP44
---

Ein Verbesserungsvorschlag, der eine standardisierte hierarchische Ableitungsstruktur für HD-Wallets einführt. BIP44 baut auf den von BIP32 für die Schlüsselableitung festgelegten Prinzipien und auf BIP43 für die Verwendung des „Zweck“-Feldes auf. Es führt eine fünfstufige Ableitungsstruktur ein: `m / purpose' / coin_type' / account' / change / address_index`. Hier sind die Details jeder Ebene:
* `m /` zeigt den Master-Privatschlüssel an. Er ist einzigartig für ein Wallet und kann keine Geschwister auf derselben Ebene haben. Der Master-Schlüssel wird direkt aus dem Seed des Wallets abgeleitet;
* `m / purpose' /` gibt den Ableitungszweck an, der hilft, den verfolgten Standard zu identifizieren. Dieses Feld wird in BIP43 beschrieben. Wenn das Wallet beispielsweise dem BIP84 (SegWit V0) Standard folgt, wäre der Index dann `84'`;
* `m / purpose' / coin-type' /` gibt den Typ der Kryptowährung an. Dies ermöglicht eine klare Unterscheidung zwischen Zweigen, die einer Kryptowährung gewidmet sind, und solchen, die einer anderen Kryptowährung in einem Multi-Coin-Wallet gewidmet sind. Der Bitcoin gewidmete Index ist `0'`;
* `m / purpose' / coin-type' / account' /` gibt die Kontonummer an. Diese Ebene ermöglicht eine einfache Unterscheidung und Organisation eines Wallets in verschiedene Konten. Diese Konten werden beginnend mit `0'` nummeriert. Erweiterte Schlüssel (`xpub`, `xprv`...) befinden sich auf dieser Ebene;
* `m / purpose' / coin-type' / account' / change /` gibt die Kette an. Jedes in Tiefe 3 definierte Konto hat zwei Ketten in Tiefe 4: eine externe Kette und eine interne Kette (auch „Wechsel“ genannt). Die externe Kette leitet Adressen ab, die öffentlich kommuniziert werden sollen, d.h., die Adressen, die uns angeboten werden, wenn wir in unserer Wallet-Software auf „Empfangen“ klicken. Die interne Kette leitet Adressen ab, die nicht öffentlich ausgetauscht werden sollen, d.h. hauptsächlich Wechseladressen. Die externe Kette wird mit dem Index `0` und die interne Kette wird mit dem Index `1` identifiziert. Sie werden bemerken, dass wir ab dieser Tiefe keine gehärtete Ableitung mehr durchführen, sondern eine normale Ableitung (es gibt kein Apostroph). Dank dieses Mechanismus sind wir in der Lage, alle Kind-Öffentlichen Schlüssel aus ihrem `xpub` abzuleiten;
* `m / purpose' / coin-type' / account' / change / address-index` gibt einfach die Nummer der Empfangsadresse und ihres Schlüsselpaares an, um sie von ihren Geschwistern auf derselben Ebene am selben Zweig zu unterscheiden. Zum Beispiel hat die erste abgeleitete Adresse den Index `0`, die zweite Adresse hat den Index `1` und so weiter...
Zum Beispiel, wenn meine Empfangsadresse den Ableitungspfad `m / 86' / 0' / 0' / 0 / 5` hat, können wir folgende Informationen ableiten:
* `86'` zeigt an, dass wir dem Ableitungsstandard von BIP86 (Taproot oder SegWitV1) folgen;
* `0'` zeigt an, dass es sich um eine Bitcoin-Adresse handelt;
* `0'` zeigt an, dass wir uns im ersten Konto des Wallets befinden;
* `0` zeigt an, dass es sich um eine externe Adresse handelt;
* `5` zeigt an, dass es sich um die sechste externe Adresse dieses Kontos handelt.

![](../../dictionnaire/assets/18.png)