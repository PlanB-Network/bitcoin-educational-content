---
term: BIP0066
---

Uvedena je standardizacija formata potpisa u transakcijama. Ovaj BIP je predložen kao odgovor na razlike u načinu na koji je OpenSSL obrađivao kodiranje potpisa na različitim sistemima. Ova heterogenost je predstavljala rizik od razdvajanja Blockchain. BIP66 je standardizovao format potpisa za sve transakcije koristeći striktno DER kodiranje (*Distinguished Encoding Rules*). Ova promena je zahtevala Soft Fork. Za svoju aktivaciju, BIP66 je koristio isti mehanizam kao BIP34, zahtevajući da se `nVersion` polje poveća na verziju 3, i odbacujući sve blokove verzije 2 ili niže kada se dostigne prag od 95% Miner. Ovaj prag je pređen na bloku broj 363,725 dana 4. jula 2015. godine.