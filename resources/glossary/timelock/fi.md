---
term: TIMELOCK

---
Älykkään sopimuksen alkeisominaisuus, jonka avulla voidaan asettaa aikapohjainen ehto, jonka on täytyttävä, jotta transaktio voidaan lisätä lohkoon. Bitcoinissa on kahdenlaisia aikalukkoja:


- Absoluuttinen aikalukko, joka määrittää tarkan hetken, jota ennen tapahtumaa ei voida sisällyttää lohkoon;
- Suhteellinen aikalukko, joka asettaa viiveen edellisen tapahtuman hyväksymisestä.

Aikalukko voidaan määritellä joko Unix-aikana ilmaistuna päivämääränä tai lohkonumerona. Lopuksi aikalukko voi koskea transaktion tulosta käyttämällä tiettyä op-koodia lukitusskriptissä (`OP_CHECKLOCKTIMEVERIFY` tai `OP_CHECKSEQUENCEVERIFY`) tai koko transaktiota käyttämällä tiettyjä transaktiokenttiä (`nLockTime` tai `nSequence`).