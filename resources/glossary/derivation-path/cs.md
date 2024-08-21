---
term: DERIVATION PATH
---

V kontextu Hierarchických Deterministických (HD) peněženek se termínem derivation path (cesta derivace) rozumí sekvence indexů použitých k odvození dětských klíčů z hlavního klíče. Popisováno v BIP32, tato cesta identifikuje stromovou strukturu pro odvození dětských klíčů. Cesta derivace je reprezentována sérií indexů oddělených lomítky a vždy začíná hlavním klíčem (označeným jako `m/`). Například typická cesta by mohla být `m/84'/0'/0'/0/0`. Každá úroveň derivace je spojena s konkrétní hloubkou:
* `m /` označuje hlavní soukromý klíč. Je unikátní pro peněženku a na stejné hloubce nemůže mít sourozence. Hlavní klíč je odvozen přímo ze seedu;
* `m / purpose' /` označuje účel derivace, který pomáhá identifikovat dodržovaný standard. Toto pole je popsáno v BIP43. Například, pokud peněženka dodržuje standard BIP84 (SegWit V0), index by pak byl `84'`;
* `m / purpose' / coin-type' /` označuje typ kryptoměny. To umožňuje jasně rozlišit větve věnované jedné kryptoměně od těch, které jsou věnované jiné, v peněžence pro více měn. Index věnovaný Bitcoinu je `0'`;
* `m / purpose' / coin-type' / account' /` označuje číslo účtu. Tato hloubka usnadňuje rozlišení a organizaci peněženky do různých účtů. Tyto účty jsou číslovány počínaje `0'`. Na této úrovni hloubky se nacházejí rozšířené klíče (`xpub`, `xprv`...);
* `m / purpose' / coin-type' / account' / change /` označuje cestu. Každý účet definovaný na hloubce 3 má na hloubce 4 dvě cesty: vnější řetězec a vnitřní řetězec (také nazývaný "change"). Vnější řetězec odvozuje adresy určené k veřejnému sdílení, tj. adresy, které nám jsou nabídnuty, když klikneme na "přijmout" v našem softwaru peněženky. Vnitřní řetězec odvozuje adresy, které nejsou určeny k veřejné výměně, především adresy pro vrácení drobných. Vnější řetězec je identifikován indexem `0` a vnitřní řetězec je identifikován indexem `1`. Všimnete si, že od této hloubky již neprovádíme zpevněnou derivaci, ale normální derivaci (není zde apostrof). Díky tomuto mechanismu jsme schopni odvodit všechny dětské veřejné klíče z jejich `xpub`;

* `m / purpose' / coin-type' / account' / change / address-index` jednoduše označuje číslo přijímací adresy a její pár klíčů, aby bylo možné ji odlišit od jejích sourozenců na stejné hloubce na stejné větvi. Například první odvozená adresa má index `0`, druhá adresa má index `1` a tak dále...

Například, pokud má moje přijímací adresa cestu derivace `m / 86' / 0' / 0' / 0 / 5`, můžeme vyvodit následující informace:
* `86'` označuje, že dodržujeme standard derivace BIP86 (Taproot / SegWit V1);
* `0'` označuje, že se jedná o adresu Bitcoinu;
* `0'` označuje, že jsme na prvním účtu peněženky;
* `0` označuje, že se jedná o vnější adresu;
* `5` označuje, že je to šestá vnější adresa tohoto účtu.

![](../../dictionnaire/assets/18.png)