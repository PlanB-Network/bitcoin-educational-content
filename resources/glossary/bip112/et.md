---
term: BIP112

---
Võtab kasutusele opkoodi `OP_CHECKSEQUENCEVERIFY` (CSV) Bitcoini skripti keeles. See operatsioon võimaldab luua tehinguid, mille kehtivus hakkab kehtima alles pärast teatud viivitust võrreldes eelmise tehinguga, mis on määratletud kas plokkide arvus või ajalises kestuses. `OP_CHECKSEQUENCEVERIFY` võrdleb virna tipus olevat väärtust sisendi `nSequence` välja väärtusega. Kui see on suurem ja kõik muud tingimused on täidetud, on skript kehtiv. Seega piirab `OP_CHECKSEQUENCEVERIFY` seda kulutava sisendi `nSequence` välja võimalikke väärtusi ja see `nSequence` väli ise piirab seda, millal seda sisendit sisaldav tehing saab plokki lisada. BIP112 võeti kasutusele 4. juulil 2016 pehme kahvli kaudu koos BIP68 ja BIP113-ga, mis aktiveeriti esmakordselt BIP9 meetodi abil.