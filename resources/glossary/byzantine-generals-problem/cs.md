---
term: PROBLÉM BYZANTSKÝCH GENERÁLŮ

---
Problém poprvé formulovali Leslie Lamport, Robert Shostak a Marshall Pease v odborném časopise *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) v červenci 1982. Dnes se používá k ilustraci problémů z hlediska rozhodování, když distribuovaný systém nemůže důvěřovat žádnému účastníkovi.

V této metafoře se skupina byzantských generálů a jejich armády utáboří kolem města, které chtějí napadnout nebo obléhat. Generálové jsou od sebe geograficky odděleni a musí spolu komunikovat prostřednictvím posla, aby mohli koordinovat svou strategii. Nezáleží na tom, zda zaútočí, nebo ustoupí, pokud se všichni generálové dohodnou.

Proto můžeme uvažovat o následujících požadavcích:


- Každý generál se musí rozhodnout: zaútočit nebo ustoupit (ano nebo ne);
- Jednou přijaté rozhodnutí nelze změnit;
- Všichni generálové se musí shodnout na stejném rozhodnutí a provést ho synchronně.

Kromě toho může generál komunikovat s jiným generálem pouze prostřednictvím zpráv předávaných kurýrem, které mohou být zpožděny, zničeny, pozměněny nebo ztraceny. A i když je zpráva úspěšně doručena, jeden nebo více generálů se může rozhodnout (z jakéhokoli důvodu) zradit navázanou důvěru a poslat falešnou zprávu, a zasít tak chaos.

Pokud toto dilema aplikujeme na kontext bitcoinového blockchainu, pak každý obecný představuje uzel v síti, který musí dosáhnout konsenzu o stavu systému. Jinými slovy, většina účastníků distribuované sítě se musí shodnout a provést stejnou akci, aby nedošlo k úplnému selhání. Jediným způsobem, jak dosáhnout konsensu v tomto typu distribuovaného systému, je mít alespoň 2/3 uzlů sítě spolehlivých a čestných. Pokud se tedy většina sítě rozhodne jednat nekalým způsobem, je systém zranitelný.

> ► *Toto dilema se někdy nazývá také "problém spolehlivého vysílání".*