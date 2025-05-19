---
term: NALOG
---

U HD (Hijerarhijski Determinističkim) novčanicima, nalog predstavlja derivaciju Layer na dubini 3 prema BIP32. Svaki nalog je sekvencijalno numerisan počevši od `/0'/` (ojačana derivacija, tako da je u stvarnosti `/2^31/` ili `/2 147 483 648/`). Na ovoj dubini derivacije se nalaze poznati `xpubs`. Danas se obično koristi samo jedan nalog unutar HD Wallet. Međutim, prvobitno su bili zamišljeni da segregiraju različite kategorije upotrebe unutar istog Wallet. Na primer, ako uzmemo standardnu putanju derivacije za eksterni Taproot (P2TR) prijemni Address: `m/86'/0'/0'/0/0`, indeks naloga je drugi `/0'/`.


![](../../dictionnaire/assets/17.webp)