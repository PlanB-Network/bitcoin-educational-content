---
term: OVERT ASICBOOST
---

Otvorena i transparentna verzija AsicBoosta. AsicBoost je tehnika algoritamske optimizacije koja se koristi u Bitcoin Mining. Rudari koji koriste Overt verziju manipulišu poljem `nVersion` kandidatskog bloka i koriste ovu modifikaciju kao dodatni Nonce. Ova metoda ostavlja stvarno polje `Nonce` bloka nepromenjeno tokom svakog pokušaja heširanja, čime se smanjuju potrebne kalkulacije za svaki SHA256, održavajući neke podatke istim između pokušaja. Ova verzija je javno detektabilna i ne skriva svoje modifikacije od ostatka mreže, za razliku od Covert verzije AsicBoosta.