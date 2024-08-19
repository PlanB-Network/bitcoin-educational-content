---
term: DERIVATION PATH
---

Im Kontext von Hierarchischen Deterministischen (HD) Wallets bezieht sich ein Derivation Path (Ableitungspfad) auf die Sequenz von Indizes, die verwendet werden, um Kind-Schlüssel von einem Master-Schlüssel abzuleiten. Beschrieben in BIP32, identifiziert dieser Pfad die Baumstruktur für die Ableitung von Kind-Schlüsseln. Ein Ableitungspfad wird durch eine Serie von durch Schrägstriche getrennten Indizes dargestellt und beginnt immer mit dem Master-Schlüssel (gekennzeichnet als `m/`). Zum Beispiel könnte ein typischer Pfad `m/84'/0'/0'/0/0` sein. Jede Ableitungsebene ist mit einer spezifischen Tiefe verbunden:
* `m /` zeigt den Master-Privatschlüssel an. Er ist einzigartig für eine Wallet und kann keine Geschwister auf derselben Tiefe haben. Der Master-Schlüssel wird direkt aus dem Seed abgeleitet;
* `m / purpose' /` zeigt den Ableitungszweck an, der hilft, den gefolgten Standard zu identifizieren. Dieses Feld wird in BIP43 beschrieben. Wenn die Wallet dem BIP84-Standard (SegWit V0) folgt, wäre der Index dann `84'`;
* `m / purpose' / coin-type' /` zeigt den Typ der Kryptowährung an. Dies ermöglicht eine klare Unterscheidung zwischen Zweigen, die einer Kryptowährung gewidmet sind, und solchen, die einer anderen in einer Multi-Coin-Wallet gewidmet sind. Der Bitcoin gewidmete Index ist `0'`;
* `m / purpose' / coin-type' / account' /` zeigt die Kontonummer an. Diese Tiefe erleichtert es, eine Wallet in verschiedene Konten zu differenzieren und zu organisieren. Diese Konten werden ab `0'` nummeriert. Erweiterte Schlüssel (`xpub`, `xprv`...) befinden sich auf dieser Tiefe;
* `m / purpose' / coin-type' / account' / change /` zeigt den Pfad an. Jedes Konto, wie bei Tiefe 3 definiert, hat zwei Pfade auf Tiefe 4: eine externe Kette und eine interne Kette (auch "Wechsel" genannt). Die externe Kette leitet Adressen ab, die öffentlich geteilt werden sollen, das heißt, die Adressen, die uns angeboten werden, wenn wir in unserer Wallet-Software auf "empfangen" klicken. Die interne Kette leitet Adressen ab, die nicht öffentlich ausgetauscht werden sollen, hauptsächlich Wechseladressen. Die externe Kette wird mit dem Index `0` und die interne Kette wird mit dem Index `1` identifiziert. Sie werden bemerken, dass wir ab dieser Tiefe keine gehärtete Ableitung mehr durchführen, sondern eine normale Ableitung (es gibt kein Apostroph). Dank dieses Mechanismus sind wir in der Lage, alle Kind-Öffentlichen-Schlüssel von ihrem `xpub` abzuleiten;

* `m / purpose' / coin-type' / account' / change / address-index` zeigt einfach die Nummer der Empfangsadresse und ihr Schlüsselpaar an, um sie von ihren Geschwistern auf derselben Tiefe am selben Zweig zu unterscheiden. Zum Beispiel hat die erste abgeleitete Adresse den Index `0`, die zweite Adresse hat den Index `1` und so weiter...

Zum Beispiel, wenn meine Empfangsadresse den Ableitungspfad `m / 86' / 0' / 0' / 0 / 5` hat, können wir folgende Informationen ableiten:
* `86'` zeigt an, dass wir dem Ableitungsstandard von BIP86 (Taproot / SegWit V1) folgen;
* `0'` zeigt an, dass es sich um eine Bitcoin-Adresse handelt;
* `0'` zeigt an, dass wir uns im ersten Konto der Wallet befinden;
* `0` zeigt an, dass es sich um eine externe Adresse handelt;
* `5` zeigt an, dass es sich um die sechste externe Adresse dieses Kontos handelt.

![](../../dictionnaire/assets/18.png)