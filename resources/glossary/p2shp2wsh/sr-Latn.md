---
term: P2SH-P2WSH
---

P2SH-P2WSH označava *Pay to Script Hash - Pay to Witness Script Hash*. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO, takođe poznat kao "Nested SegWit".


P2SH-P2WSH je uveden sa implementacijom SegWit u avgustu 2017. Ovaj skript opisuje P2WSH umotan unutar P2SH. Zaključava bitkoine na osnovu Hash skripta. Razlika u odnosu na klasični P2WSH je što je skript umotan u `redeemscript` klasičnog P2SH.


Ovaj skript je kreiran prilikom lansiranja SegWit kako bi se olakšalo njegovo usvajanje. Omogućava korišćenje ovog novog standarda, čak i sa servisima ili novčanicima koji još nisu nativno kompatibilni sa SegWit. Danas, stoga, više nije veoma relevantno koristiti ove tipove umotanih SegWit skripti, jer je većina novčanika implementirala nativni SegWit. P2SH-P2WSH adrese su napisane koristeći `Base58Check` kodiranje i uvek počinju sa `3`, kao i svaki P2SH Address.