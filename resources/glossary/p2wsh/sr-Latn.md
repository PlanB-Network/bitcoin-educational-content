---
term: P2WSH
---

P2WSH označava *Pay to Witness Script Hash*. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. P2WSH je uveden implementacijom SegWit u avgustu 2017.


Ovaj skript je sličan P2SH (*Pay to Public Script Hash*), jer takođe zaključava bitkoine na osnovu Hash skripta. Razlika je u načinu na koji se potpisi i skripte uključuju u transakciju. Da bi se potrošili bitkoini na ovom tipu skripta, primalac mora obezbediti originalni skript, nazvan `witnessScript` (ekvivalentno `redeemscript`), zajedno sa potrebnim potpisima. Ovaj mehanizam omogućava implementaciju sofisticiranijih uslova za trošenje, kao što su multisigs.


U kontekstu P2WSH, informacije o skripti potpisa (`scriptWitness`, ekvivalentno `scriptSig`) su premeštene iz tradicionalne strukture transakcije u poseban odeljak nazvan `Witness`. Ovo premeštanje je karakteristika SegWit (*Segregated Witness*) ažuriranja koje pomaže u sprečavanju promenljivosti potpisa. P2WSH transakcije su generalno manje skupe u smislu naknada u poređenju sa Legacy transakcijama, jer deo u svedoku košta manje.


P2WSH adrese su napisane koristeći `Bech32` kodiranje sa kontrolnim zbirom u obliku BCH koda. Ove adrese uvek počinju sa `bc1q`. P2WSH je verzija 0 SegWit izlaza.