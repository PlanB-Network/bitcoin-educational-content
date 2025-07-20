---
term: KONSOLIDACIJA
---

Specifična transakcija u kojoj se više malih UTXO-a spajaju u jedan ulaz kako bi se formirao jedan veći UTXO kao izlaz. Ova operacija je transakcija napravljena na sopstveni Wallet. Cilj konsolidacije je da se iskoriste periodi kada su naknade na Bitcoin mreži niske kako bi se spojilo nekoliko malih UTXO-a u jedan veći po vrednosti. Tako se predviđaju obavezni troškovi u slučaju povećanja naknada, omogućavajući uštede na budućim transakcijskim naknadama.


Zaista, transakcije sa mnogo ulaza su teže i, shodno tome, skuplje. Pored ušteda koje se mogu postići na naknadama za transakcije, konsolidacija je takođe oblik dugoročnog planiranja. Ako vaš Wallet sadrži veoma male UTXO-e, oni mogu postati neupotrebljivi ako Bitcoin mreža uđe u produženi period visokih naknada. Na primer, ako trebate potrošiti UTXO od 10,000 Sats, ali minimalne Mining naknade iznose 15,000 Sats, trošak bi premašio vrednost samog UTXO. Ovi mali UTXO-i tada postaju ekonomski neracionalni za korišćenje i ostaju neupotrebljivi sve dok se naknade ne smanje. Ovi UTXO-i se obično nazivaju "Dust." Redovnim konsolidovanjem vaših malih UTXO-a smanjujete ovaj rizik povezan sa povećanjem naknada.


Međutim, važno je napomenuti da su transakcije konsolidacije prepoznatljive tokom analize lanca. Takva transakcija ukazuje na Zajednički Ulaz Ownership Heuristiku (CIOH), što znači da ulazi transakcije konsolidacije pripadaju jednom entitetu. Ovo može imati implikacije u pogledu privatnosti za korisnika.


![](../../dictionnaire/assets/7.webp)