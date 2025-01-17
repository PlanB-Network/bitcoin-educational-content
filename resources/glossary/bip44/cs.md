---
term: BIP44

---
Návrh na zlepšení, který zavádí standardní hierarchickou strukturu odvození pro peněženky HD. BIP44 vychází ze zásad stanovených v BIP32 pro odvozování klíčů a z BIP43 pro používání pole "účel". Zavádí pětiúrovňovou odvozovací strukturu: `m / účel' / typ mince' / účet' / změna / adresa_index`. Zde jsou uvedeny podrobnosti o jednotlivých hloubkách:


- `m /` označuje hlavní soukromý klíč. Je jedinečný pro danou peněženku a nemůže mít sourozence ve stejné hloubce. Hlavní klíč je přímo odvozen od seedu peněženky;
- `m / účel' /` označuje účel odvození, který pomáhá identifikovat sledovanou normu. Toto pole je popsáno v BIP43. Například pokud peněženka následuje standard BIP84 (SegWit V0), index by pak byl `84'`;
- `m / purpose' / coin-type' /` označuje typ kryptoměny. To umožňuje jasně rozlišit pobočky určené pro jednu kryptoměnu a pobočky určené pro jinou kryptoměnu v peněžence s více mincemi. Index určený pro Bitcoin je `0`;
- `m / účel' / typ mince' / účet' /` označuje číslo účtu. Tato hloubka umožňuje snadné rozlišení a organizaci peněženky na různé účty. Tyto účty jsou číslovány od `0`. V této hloubce se nacházejí rozšířené klíče (`xpub`, `xprv`...);
- `m / purpose' / coin-type' / account' / change /` označuje řetězec. Každý účet definovaný v hloubce 3 má v hloubce 4 dva řetězce: vnější řetězec a vnitřní řetězec (nazývaný také "změna"). Externí řetězec odvozuje adresy určené k veřejnému sdělování, tj. adresy, které se nám nabídnou, když v softwaru peněženky klikneme na "přijmout". Interní řetězec odvozuje adresy, které nejsou určeny k veřejné výměně, tj. především adresy změn. Externí řetězec se označuje indexem `0` a interní řetězec indexem `1`. Všimněte si, že od této hloubky již neprovádíme odvození natvrdo, ale normální odvození (není zde apostrof). Právě díky tomuto mechanismu jsme schopni odvodit všechny podřízené veřejné klíče z jejich `xpub`;
- `m / purpose' / coin-type' / account' / change / address-index` jednoduše označuje číslo přijímající adresy a její dvojici klíčů, aby se odlišila od svých sourozenců ve stejné hloubce na stejné větvi. Například první odvozená adresa má index `0`, druhá adresa má index `1` a tak dále...

Pokud má moje přijímací adresa například derivační cestu `m / 86' / 0' / 0' / 0 / 5`, můžeme odvodit následující informace:


- `86'` označuje, že se řídíme odvozovacím standardem BIP86 (Taproot nebo SegWitV1);
- `0'` znamená, že se jedná o adresu Bitcoin;
- `0'` znamená, že se nacházíme na prvním účtu peněženky;
- `0` znamená, že se jedná o externí adresu;
- `5` znamená, že se jedná o šestou externí adresu tohoto účtu.

![](../../dictionnaire/assets/18.webp)