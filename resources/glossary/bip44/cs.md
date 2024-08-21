---
term: BIP44
---

Návrh na zlepšení, který zavádí standardní hierarchickou strukturu derivace pro HD peněženky. BIP44 staví na principech stanovených BIP32 pro derivaci klíčů a na BIP43 pro použití pole „účel“. Zavádí pětiúrovňovou strukturu derivace: `m / účel' / typ_měny' / účet' / změna / index_adresy`. Zde jsou podrobnosti každé úrovně:
* `m /` označuje hlavní soukromý klíč. Je jedinečný pro peněženku a na stejné úrovni nemůže mít sourozence. Hlavní klíč je přímo odvozen ze seedu peněženky;
* `m / účel' /` označuje účel derivace, který pomáhá identifikovat dodržovaný standard. Toto pole je popsáno v BIP43. Například, pokud peněženka sleduje standard BIP84 (SegWit V0), index by pak byl `84'`;
* `m / účel' / typ_měny' /` označuje typ kryptoměny. To umožňuje jasnou diferenciaci mezi větvemi věnovanými jedné kryptoměně a těmi věnovanými jiné kryptoměně v peněžence s více měnami. Index věnovaný Bitcoinu je `0'`;
* `m / účel' / typ_měny' / účet' /` označuje číslo účtu. Tato úroveň umožňuje snadnou diferenciaci a organizaci peněženky do různých účtů. Tyto účty jsou číslovány od `0'`. Rozšířené klíče (`xpub`, `xprv`...) se nacházejí na této úrovni;
* `m / účel' / typ_měny' / účet' / změna /` označuje řetězec. Každý účet definovaný v úrovni 3 má na úrovni 4 dva řetězce: vnější řetězec a vnitřní řetězec (také nazývaný „změna“). Vnější řetězec derivuje adresy určené k veřejnému sdělení, tj. adresy, které nám jsou nabídnuty, když klikneme na „přijmout“ v našem softwaru peněženky. Vnitřní řetězec derivuje adresy, které nejsou určeny k veřejné výměně, tj. primárně adresy pro změnu. Vnější řetězec je identifikován indexem `0` a vnitřní řetězec indexem `1`. Všimnete si, že od této úrovně již neprovádíme zpevněnou derivaci, ale normální derivaci (není zde apostrof). Díky tomuto mechanismu jsme schopni odvodit všechny dětské veřejné klíče z jejich `xpub`;
* `m / účel' / typ_měny' / účet' / změna / index_adresy` jednoduše označuje číslo přijímací adresy a její pár klíčů, aby bylo možné ji odlišit od jejích sourozenců na stejné úrovni na stejné větvi. Například první odvozená adresa má index `0`, druhá adresa má index `1` a tak dále...
Například, pokud má moje přijímací adresa cestu derivace `m / 86' / 0' / 0' / 0 / 5`, můžeme vyvodit následující informace:
* `86'` označuje, že sledujeme standard derivace BIP86 (Taproot nebo SegWitV1);
* `0'` označuje, že se jedná o adresu Bitcoinu;
* `0'` označuje, že jsme na prvním účtu peněženky;
* `0` označuje, že se jedná o vnější adresu;
* `5` označuje, že je to šestá vnější adresa tohoto účtu.

![](../../dictionnaire/assets/18.png)