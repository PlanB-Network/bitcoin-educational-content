---
term: PŘIJÍMACÍ ADRESA

---
Informace používané k přijímání bitcoinů. Adresa se obvykle vytváří hashováním veřejného klíče pomocí `SHA256` a `RIMPEMD160` a přidáním metadat k tomuto digestu. Veřejné klíče použité ke konstrukci přijímací adresy jsou součástí peněženky uživatele, a proto jsou odvozeny od jeho seedu. Například adresy SegWit se skládají z následujících informací:


- HRP pro označení "bitcoin": `bc`;
- Oddělovač: `1`;
- Použitá verze SegWit: `q` nebo `p`;
- Platební zatížení: digest veřejného klíče (nebo přímo veřejný klíč v případě Taproot);
- Kontrolní součet: kód BCH.

V závislosti na použitém modelu skriptu však může přijímací adresa představovat i něco jiného. Například adresy P2SH jsou konstruovány pomocí hashe skriptu. Naproti tomu adresy Taproot obsahují upravený veřejný klíč přímo bez hashování.

Přijímací adresa může být reprezentována ve formě alfanumerického řetězce nebo jako QR kód. Každá adresa může být použita vícekrát, ale to je velmi nedoporučovaná praxe. V zájmu zachování určité úrovně soukromí se totiž doporučuje používat každou adresu Bitcoin pouze jednou. Pro každou příchozí platbu do vlastní peněženky by měla být vygenerována nová adresa. Adresa je kódována v `Bech32` pro adresy SegWit V0, v `Bech32m` pro adresy SegWit V1 a v `Base58check` pro adresy Legacy. Z technického hlediska znamená přijímání bitcoinů vlastnictví soukromého klíče spojeného s veřejným klíčem (a tedy i adresy). Když někdo obdrží bitcoiny, odesílatel aktualizuje stávající omezení na jejich utrácení, takže tuto pravomoc nyní může mít pouze příjemce.

![](../../dictionnaire/assets/23.webp)