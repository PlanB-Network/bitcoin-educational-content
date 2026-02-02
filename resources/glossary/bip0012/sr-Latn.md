---
term: BIP0012
definition: Predlog koji uvodi OP_EVAL opkod za ugnježdene skripte, zamenjen sa BIP16 (P2SH) iz bezbednosnih razloga.
---

Predlog Gavina Andresena za poboljšanje fleksibilnosti i privatnosti Bitcoin transakcijskih skripti. Ovaj BIP predlaže implementaciju novog skriptnog opkoda, nazvanog `OP_EVAL`, koji omogućava evaluaciju skripte sadržane unutar podataka `scriptSig` tokom procesa validacije transakcije. Glavna modifikacija BIP12 je omogućavanje uključivanja jedne skripte unutar druge skripte. Ova tehnika omogućava kreiranje složenijih uslova koji se mogu verifikovati u trenutku trošenja, bez potrebe da se otkriju korisnicima koji šalju bitkoine na korišćeni Address. BIP12 je kasnije zamenjen sigurnijim predlozima, posebno BIP16 (P2SH), koji nudi drugačiji metod za postizanje istih ciljeva kao `OP_EVAL`.