---
term: P2SH-P2WPKH
---

P2SH-P2WPKH označava *Pay to Script Hash - Pay to Witness Public Key Hash*. To je standardni skript model koji se koristi za uspostavljanje uslova trošenja na UTXO, takođe poznat kao "Nested SegWit".


P2SH-P2WPKH je uveden sa implementacijom SegWit u avgustu 2017. Ovaj skript je P2WPKH umotan unutar P2SH. Zaključava bitkoine na osnovu Hash javnog ključa. Razlika od klasičnog P2WPKH je što je skript umotan u `redeemscript` klasičnog P2SH.


Ovaj skript je kreiran prilikom lansiranja SegWit kako bi se olakšalo njegovo usvajanje. Omogućava korišćenje ovog novog standarda, čak i sa servisima ili novčanicima koji još nisu nativno kompatibilni sa SegWit. To je neka vrsta prelaznog skripta ka novom standardu. Danas, stoga, više nije veoma relevantno koristiti ove tipove umotanih SegWit skripti, pošto je većina novčanika implementirala nativni SegWit. P2SH-P2WPKH adrese su napisane koristeći `Base58Check` kodiranje i uvek počinju sa `3`, kao i svaki P2SH Address.


> ► *`P2SH-P2WPKH` se ponekad naziva i `P2WPKH-nested-in-P2SH`.*