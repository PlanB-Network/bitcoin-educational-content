---
term: BIP113

---
Viidi sisse muudatus kõigi ajalukuoperatsioonide (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`) arvutamisel. See täpsustab, et timelockide kehtivuse hindamiseks tuleb neid nüüd võrrelda MTP-ga (*Median Time Past*), mis on viimase 11 ploki ajamärkide mediaan. Varem kasutati ainult eelmise ploki ajatemplit. See meetod muudab süsteemi prognoositavamaks ja takistab kaevurite poolt ajaviitega manipuleerimist. BIP113 võeti kasutusele 4. juulil 2016 soft forki kaudu koos BIP68 ja BIP112ga, mis aktiveeriti esmakordselt BIP9 meetodi abil.