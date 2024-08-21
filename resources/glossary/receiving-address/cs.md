---
term: PŘIJÍMACÍ ADRESA
---

Informace používané k přijímání bitcoinů. Adresa je obvykle vytvořena hašováním veřejného klíče pomocí `SHA256` a `RIMPEMD160` a přidáním metadat k tomuto souhrnu. Veřejné klíče použité k vytvoření přijímací adresy jsou součástí peněženky uživatele a jsou proto odvozeny z jejich seedu. Například adresy SegWit jsou složeny z následujících informací:
* HRP pro označení "bitcoin": `bc`;
* Oddělovač: `1`;
* Verze SegWit použitá: `q` nebo `p`;
* Payload: souhrn veřejného klíče (nebo přímo veřejný klíč v případě Taproot);
* Kontrolní součet: BCH kód.

Nicméně, přijímací adresa může také reprezentovat něco jiného v závislosti na použitém skriptovém modelu. Například adresy P2SH jsou konstruovány pomocí haše skriptu. Adresy Taproot na druhou stranu obsahují upravený veřejný klíč přímo bez hašování.

Přijímací adresa může být reprezentována ve formě alfanumerického řetězce nebo jako QR kód. Každá adresa může být použita vícekrát, ale toto je vysoce nedoporučovaná praxe. Skutečně, aby byla udržena určitá úroveň soukromí, doporučuje se použít každou Bitcoinovou adresu pouze jednou. Pro každou příchozí platbu do peněženky by měla být generována nová adresa. Adresa je kódována v `Bech32` pro adresy SegWit V0, v `Bech32m` pro adresy SegWit V1 a v `Base58check` pro Legacy adresy. Z technického hlediska přijetí bitcoinu znamená vlastnění soukromého klíče spojeného s veřejným klíčem (a tedy adresou). Když někdo přijme bitcoiny, odesílatel aktualizuje stávající omezení na jejich utrácení, takže nyní může mít tuto moc pouze příjemce.

![](../../dictionnaire/assets/23.png)