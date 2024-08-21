---
term: BIP113
---

Tutvustas muudatust kõigi ajalukkude toimingute (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`) arvutamises. See sätestab, et ajalukkude kehtivuse hindamiseks tuleb neid nüüd võrrelda MTP-ga (*Median Time Past*, eesti keeles mineviku keskmine aeg), mis on viimase 11 ploki ajatemplite mediaan. Varem kasutati ainult eelmise ploki ajatemplit. See meetod muudab süsteemi ettearvatavamaks ja hoiab ära aja viite manipuleerimise kaevurite poolt. BIP113 tutvustati pehme forki kaudu 4. juulil 2016, koos BIP68 ja BIP112-ga, mis aktiveeriti esmakordselt kasutades BIP9 meetodit.