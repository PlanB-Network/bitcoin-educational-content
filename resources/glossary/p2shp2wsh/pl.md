---
term: P2SH-P2WSH
---

P2SH-P2WSH to skrót od *Pay to Script Hash - Pay to Witness Script Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO, znany również jako "zagnieżdżony SegWit".


P2SH-P2WSH został wprowadzony wraz z implementacją SegWit w sierpniu 2017 roku. Ten skrypt opisuje P2WSH opakowany w P2SH. Blokuje on bitcoiny w oparciu o Hash skryptu. Różnica w stosunku do klasycznego P2WSH polega na tym, że skrypt jest opakowany w `redeemscript` klasycznego P2SH.


Skrypt ten został stworzony w momencie uruchomienia SegWit, aby ułatwić jego przyjęcie. Umożliwia on korzystanie z tego nowego standardu, nawet w przypadku usług lub portfeli, które nie są jeszcze natywnie kompatybilne z SegWit. Obecnie korzystanie z tego typu skryptów SegWit nie ma już większego znaczenia, ponieważ większość portfeli wdrożyła natywny SegWit. Adresy P2SH-P2WSH są zapisywane przy użyciu kodowania `Base58Check` i zawsze zaczynają się od `3`, jak każdy P2SH Address.