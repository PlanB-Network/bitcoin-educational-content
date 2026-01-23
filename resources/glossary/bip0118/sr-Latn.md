---
term: BIP0118
definition: ANYPREVOUT predlog koji uvodi nove SigHash zastavice koje omogućavaju ponovnu upotrebu potpisa između transakcija, korisno za Eltoo.
---

Predlog za poboljšanje Bitcoin usmeren na uvođenje dva nova SigHash Flag modifikatora: `SIGHASH_ANYPREVOUT` i `SIGHASH_ANYPREVOUTANYSCRIPT`. Ove funkcije proširuju mogućnosti Bitcoin transakcija, posebno u smislu pametnih ugovora i rešenja kao što je Lightning Network. BIP118 bi značajno omogućio korišćenje Eltoo. Glavna prednost `SIGHASH_ANYPREVOUT` je omogućavanje ponovne upotrebe potpisa u više transakcija, što nudi veću fleksibilnost. Konkretno, ovi SigHash-ovi omogućavaju potpis koji ne pokriva nijedan od ulaza transakcije.