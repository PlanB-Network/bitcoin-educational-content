---
term: BYZANTINE GENERALS PROBLEM
---

Problém byl poprvé formulován Leslie Lamportem, Robertem Shostakem a Marshallem Peasem ve specializovaném časopise *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) v červenci 1982. Dnes se používá k ilustraci výzev v rozhodovacích procesech, když distribuovaný systém nemůže důvěřovat žádnému aktérovi.

V této metafoře je skupina byzantských generálů a jejich příslušných armád tábořena kolem města, které si přejí zaútočit nebo obléhat. Generálové jsou geograficky odděleni jeden od druhého a musí komunikovat prostřednictvím poslů, aby koordinovali svou strategii. Nezáleží na tom, zda zaútočí nebo ustoupí, pokud všichni generálové dosáhnou konsensu.

Proto můžeme zvážit následující požadavky:
* Každý generál musí učinit rozhodnutí: zaútočit nebo ustoupit (ano nebo ne);
* Jakmile je rozhodnutí učiněno, nemůže být změněno;
* Všichni generálové musí souhlasit se stejným rozhodnutím a provést jej synchronně.

Navíc generál může komunikovat s jiným pouze prostřednictvím zpráv přenášených kurýrem, které mohou být zpožděny, zničeny, změněny nebo ztraceny. A i když je zpráva úspěšně doručena, jeden nebo více generálů se může (z jakéhokoli důvodu) rozhodnout zradit zavedenou důvěru a poslat podvodnou zprávu, čímž zasévá chaos.

Aplikace dilematu na kontext Bitcoin blockchainu, každý generál reprezentuje uzel v síti, který potřebuje dosáhnout konsensu o stavu systému. Jinými slovy, většina účastníků v distribuované síti musí souhlasit a provést stejnou akci, aby se zabránilo totálnímu selhání. Jediný způsob, jak dosáhnout konsensu v tomto typu distribuovaného systému, je mít alespoň 2/3 uzlů v síti spolehlivých a poctivých. Proto, pokud se většina sítě rozhodne jednat zlomyslně, systém je zranitelný.

> ► *Toto dilema je někdy také nazýváno "Problém spolehlivého vysílání".*