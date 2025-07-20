---
term: P2WPKH
---

P2WPKH označava *Pay to Witness Public Key Hash*. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. P2WPKH je uveden implementacijom SegWit u avgustu 2017.


Ovaj skript je sličan P2PKH (*Pay to Public Key Hash*), jer takođe zaključava bitkoine na osnovu Hash javnog ključa, odnosno, primaoca Address. Razlika je u načinu na koji su potpisi i skripte uključeni u transakciju. U slučaju P2WPKH, informacija o skripti potpisa (`scriptSig`) se premješta iz tradicionalne strukture transakcije u poseban odeljak nazvan `Witness`. Ovaj potez je karakteristika SegWit (*Segregated Witness*) ažuriranja koje pomaže u sprečavanju promenljivosti potpisa. P2WPKH transakcije su generalno manje skupe u smislu naknada u poređenju sa Legacy transakcijama, jer deo u witness-u košta manje.


Adrese P2WPKH su napisane koristeći `Bech32` kodiranje sa kontrolnim zbirom u obliku BCH koda. Ove adrese uvek počinju sa `bc1q`. P2WPKH je verzija 0 SegWit izlaza.