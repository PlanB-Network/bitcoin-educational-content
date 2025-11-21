---
term: BIP0137
---

Predlaže standardizovani format za potpisivanje poruka sa Bitcoin privatnim ključevima i njihovim povezanim adresama, kako bi se dokazao Ownership od Address. Ovaj BIP ima za cilj da reši nejasnoće vezane za različite tipove Bitcoin adresa (P2PKH, P2SH, P2WPKH...) prilikom potpisivanja poruke. Uvodi metodu za eksplicitno razlikovanje ovih Address formata putem potpisa. Ovi potpisi su korisni za razne primene kao što su dokazivanje sredstava, revizija i druge upotrebe koje zahtevaju autentifikaciju Address putem njegovog privatnog ključa. BIP322 je od tada uveo novi format potpisa koji omogućava proširenje ovog standarda i generalizaciju za bilo koji tip skripta.