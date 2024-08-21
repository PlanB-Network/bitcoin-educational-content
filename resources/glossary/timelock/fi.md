---
termi: TIMELOCK
---

Älykkään sopimuksen perusosa, joka mahdollistaa aikaan perustuvan ehdon asettamisen, joka on täytettävä, jotta tapahtuma voidaan lisätä lohkoon. Bitcoinissa on kaksi tyyppiä aikalukoista:
* Absoluuttinen aikalukko, joka määrittää tarkan hetken, ennen jota tapahtumaa ei voida sisällyttää lohkoon;
* Suhteellinen aikalukko, joka asettaa viiveen edellisen tapahtuman hyväksymisestä.
Aikalukko voidaan määritellä joko päivämääränä Unix-ajan ilmaisuna tai lohkonumerona. Lopuksi, aikalukkoa voidaan soveltaa tapahtuman tulosteeseen käyttämällä tiettyä operaatiokoodia lukitusskriptissä (`OP_CHECKLOCKTIMEVERIFY` tai `OP_CHECKSEQUENCEVERIFY`), tai koko tapahtumaan käyttämällä tiettyjä tapahtumakenttiä (`nLockTime` tai `nSequence`).