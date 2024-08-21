---
term: TOORE TEHING
---

Bitcoin'i tehing, mis on koostatud ja allkirjastatud, eksisteerides oma binaarsel kujul. Toore tehing (*raw TX*) on tehingu lõplik esitusviis, just enne selle levitamist võrgus. See tehing sisaldab kõiki vajalikke andmeid selle blokki lisamiseks:
* Versioon;
* Lipp;
* Sisendid;
* Väljundid;
* Lukustusaeg;
* Tunnistaja.

Mida nimetatakse "*tooreks tehinguks*" esindab toorandmeid, mis läbivad SHA256 räsifunktsiooni kaks korda, et genereerida tehingu TXID. Neid andmeid kasutatakse seejärel bloki Merkle'i puus, et integreerida tehing plokiahelasse.

> ► *Seda kontseptsiooni nimetatakse mõnikord ka "Serialiseeritud Tehinguks". Prantsuse keeles võiksid need terminid vastavalt tõlkida kui "transaction brute" ja "transaction sérialisée".*