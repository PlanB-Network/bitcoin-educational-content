---
term: VIN
definition: Igice kigize itunshwa ry'amafaranga rya Bitcoin cyerekana inkomoko y'amafaranga binyuze ku kwerekeza kuri UTXO yakozwe kera.
---

Ikintu kidasanzwe c’isoko rya Bitcoin kigaragaza aho amahera akoreshwa mu guhazwa n’ibiva. Buri `vin` yerekeza ku giciro kitakoreshejwe (UTXO) kivuye mu gucuruza kwa kera. Igikorwa kishobora kubamwo ibintu vyinshi vyinjizwa, kimwe cose kigaragazwa n’uguhuza `txid` (ikimenyetso c’igikorwa c’intango) na `vout` (urutonde rw’ivyo biva muri ico gicuruzwa).


Buri `vin` irimwo amakuru akurikira:


- `txid`: ikimenyetso c'isoko ry'imbere ririmwo igisohoka gikoreshwa hano nk'inyungu;
- `vout`: urutonde rw'ibisohoka mu gucuruza imbere;
- `scriptSig` canke `scriptWitness`: inyandiko yo gufungura itanga amakuru akenewe kugira ngo yuzuze ivyangombwa vyashizweho na `scriptPubKey` y'isoko ry'imbere ry'amahera yaryo ariko arakoreshwa, akenshi mu gutanga umukono w'ibanga;
- `nSequence`: umwanya wihariye ukoreshwa mu kwerekana ingene iyi nkuru ipfungiwe n'igihe, hamwe n'ibindi bihitamwo nka RBF.