---
term: OP_CHECKSIGVERIFY (0XAD)
definition: Kombinuje OP_CHECKSIG i OP_VERIFY, zaustavljajući skriptu ako je potpis nevažeći.
---

Izvodi istu operaciju kao `OP_CHECKSIG`, ali ako verifikacija potpisa ne uspe, skripta se odmah zaustavlja sa greškom i transakcija je stoga nevažeća. Ako verifikacija uspe, skripta se nastavlja bez dodavanja `1` (tačno) vrednosti na stek. Ukratko, `OP_CHECKSIGVERIFY` izvodi operaciju `OP_CHECKSIG` praćenu `OP_VERIFY`. Ovaj opcode je modifikovan u Tapscript-u da verifikuje Schnorr potpise.