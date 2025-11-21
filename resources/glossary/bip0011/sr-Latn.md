---
term: BIP0011
---

BIP koji je uveo Gavin Andresen u martu 2012. predlaže standardnu metodu za kreiranje transakcija sa višestrukim potpisima na Bitcoin. Ovaj predlog ima za cilj poboljšanje sigurnosti bitkoina zahtevajući više potpisa za validaciju transakcije. BIP11 uvodi novi tip skripta, nazvan "M-of-N Multisig," gde `M` predstavlja minimalan broj potrebnih potpisa od `N` mogućih javnih ključeva. Ovaj standard koristi `OP_CHECKMULTISIG` opcode, koji već postoji u Bitcoin, ali koji prethodno nije bio usklađen sa pravilima standardizacije čvorova. Iako se ovaj tip skripta više ne koristi često za stvarne Multisig novčanike, u korist P2SH ili P2WSH, njegova upotreba ostaje moguća. Posebno se koristi u meta-protokolima kao što su Stamps. Čvorovi, međutim, mogu odlučiti da ne prosleđuju ove P2MS transakcije sa parametrom `permitbaremultisig=0`.


> ► *Danas je ovaj standard poznat kao "bare-Multisig" ili "P2MS".*