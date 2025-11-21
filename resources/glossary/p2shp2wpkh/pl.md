---
term: P2SH-P2WPKH
---

P2SH-P2WPKH oznacza *Pay to Script Hash - Pay to Witness Public Key Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO, znany również jako "zagnieżdżony SegWit".


P2SH-P2WPKH został wprowadzony wraz z implementacją SegWit w sierpniu 2017 roku. Ten skrypt to P2WPKH zawinięty w P2SH. Blokuje on bitcoiny w oparciu o Hash klucza publicznego. Różnica w stosunku do klasycznego P2WPKH polega na tym, że skrypt jest opakowany w `redeemscript` klasycznego P2SH.


Skrypt ten został stworzony w momencie uruchomienia SegWit, aby ułatwić jego przyjęcie. Umożliwia on korzystanie z tego nowego standardu, nawet w przypadku usług lub portfeli, które nie są jeszcze natywnie kompatybilne z SegWit. Jest to rodzaj skryptu przejściowego do nowego standardu. Obecnie korzystanie z tego typu skryptów SegWit nie ma już większego znaczenia, ponieważ większość portfeli wdrożyła natywny SegWit. Adresy P2SH-P2WPKH są zapisywane przy użyciu kodowania `Base58Check` i zawsze zaczynają się od `3`, jak każdy P2SH Address.


> * ``P2SH-P2WPKH`` jest również czasami nazywane ``P2WPKH-nested-in-P2SH``