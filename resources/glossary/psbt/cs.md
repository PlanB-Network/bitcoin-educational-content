---
term: PSBT

---
Akronym pro "částečně podepsanou transakci Bitcoin". Jedná se o specifikaci zavedenou spolu s BIP174 s cílem standardizovat způsob, jakým jsou nedokončené transakce konstruovány v softwaru souvisejícím s Bitcoinem, například v softwaru peněženek. PSBT zapouzdřuje transakci, jejíž vstupy nemusí být plně podepsány. Obsahuje všechny potřebné informace, aby účastník mohl transakci podepsat, aniž by vyžadoval další údaje. PSBT tak může mít tři různé podoby:


- Plně zkonstruovaná transakce, ale ještě nepodepsaná;
- Částečně podepsaná transakce, kdy některé vstupy jsou podepsané, zatímco jiné ještě ne;
- Nebo plně podepsanou transakci Bitcoin, kterou lze převést tak, aby byla připravena k vysílání v síti.

Formát PSBT usnadňuje interoperabilitu mezi různými softwarovými peněženkami a podpisovými zařízeními (hardwarové peněženky). V současné době se používá verze 0 formátu PSBT definovaná v BIP174, ale prostřednictvím BIP370 se navrhuje verze 2.

> ► *Verze 1 PSBT neexistuje. Protože verze 0 byla první verzí, druhá verze se neformálně nazývá verze 2. Ava Chow, která je autorkou BIP370, se proto rozhodla přidělit této nové verzi číslo 2, aby se předešlo záměně.*