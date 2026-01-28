---
term: Töötlemata tehing

definition: Bitcoini tehing selle täielikul binaarsel kujul, valmis võrgus edastamiseks.
---
Bitcoini tehing, mis on üles ehitatud ja allkirjastatud, mis eksisteerib binaarsel kujul. Toortehing (*raw TX*) on tehingu lõplik esitus, vahetult enne selle edastamist võrgus. See tehing sisaldab kogu vajalikku teavet, mis on vajalik selle lisamiseks plokki:


- Versioon;
- Lipp;
- Sisendid;
- Väljundid;
- Lukuaeg;
- Tunnistaja.

See, mida nimetatakse "*toore tehinguks*", kujutab endast töötlemata andmeid, mis läbivad kaks korda SHA256 hash-funktsiooni, et genereerida tehingu TXID. Neid andmeid kasutatakse seejärel ploki Merkle-puus, et integreerida tehing plokiahelasse.

