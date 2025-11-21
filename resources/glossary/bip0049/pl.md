---
term: BIP0049
---

BIP49 to informacyjny BIP, który wprowadza metodę derywacji używaną do generate zagnieżdżonych adresów SegWit w HD Wallet. Proponowana ścieżka derywacji jest zgodna ze standardami BIP43 i BIP44, z indeksem `49'` (utwardzona derywacja) na głębokości celu. Na przykład, pierwszy Address konta P2SH-P2WPKH zostałby wyprowadzony ze ścieżki: `m/49'/0'/0'/0/0`. Zagnieżdżone skrypty SegWit zostały wymyślone podczas uruchamiania SegWit, aby ułatwić jego przyjęcie. Pozwalają one na korzystanie z tego nowego standardu, nawet w portfelach, które nie są jeszcze natywnie kompatybilne z SegWit.