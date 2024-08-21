---
term: VALUUTA TÜÜP
---

Deterministlike ja hierarhiliste (HD) rahakottide kontekstis on valuuta tüüp (*coin type* inglise keeles) tuletusstruktuuri tase, mis võimaldab eristada rahakoti harusid erinevate kasutatavate krüptovaluutade põhjal. See tuletuskiht, mille on määratlenud BIP 44, asub tuletusstruktuuri sügavusel 2, järgnedes peamisele võtmele ja eesmärgile. Näiteks Bitcoin'i puhul on määratud indeks `0x80000000`, mida tähistatakse tuletustees kui `/0'/`. See tähendab, et kõik sellelt teelt tuletatud aadressid ja kontod on seotud Bitcoin'iga. See tuletuskiht võimaldab mitme valuutaga rahakotis erinevate varade selget eraldamist. Siin on indeksid, mida kasutatakse erinevate krüptovaluutade jaoks:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)