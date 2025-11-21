---
term: BIP0049
---

BIP49 je informativni BIP koji uvodi metodu derivacije korišćenu za generate Ugnježdene SegWit adrese u HD Wallet. Predložena putanja derivacije prati standarde BIP43 i BIP44, sa indeksom `49'` (ojačana derivacija) na dubini cilja. Na primer, prvi Address od P2SH-P2WPKH naloga bi bio izveden iz putanje: `m/49'/0'/0'/0/0`. Ugnježđeni SegWit skripti su izmišljeni prilikom lansiranja SegWit kako bi se olakšalo njegovo usvajanje. Oni omogućavaju korišćenje ovog novog standarda, čak i na novčanicima koji još nisu nativno kompatibilni sa SegWit.