---
term: ANONSETS (ANONÜÜMSUSE KOMPLEKTID)

---
Anonsetid on näitajad, mille abil saab hinnata konkreetse UTXO privaatsuse taset. Täpsemalt öeldes mõõdavad nad eristamatute UTXOde arvu kogumis, mis sisaldab uuritavat mündi. Kuna nõutakse identsete UTXOde rühma, arvutatakse anonsetid tavaliselt mündiühenduste tsükli raames. Need võimaldavad vajaduse korral hinnata mündiliitude kvaliteeti. Suur anonset tähendab suuremat anonüümsust, kuna konkreetset UTXOd on kogumis raske eristada. On olemas kahte tüüpi anonsetid:


- Eeldatav anonüümsuse komplekt;
- Retrospektiivne anonüümsuse komplekt.

Esimene näitab selle rühma suurust, mille hulka uuritav UTXO on peidetud, teades UTXOd sisendil. See näitaja võimaldab mõõta müntide privaatsuse vastupidavust analüüsile minevikust tänapäevani (sisendist väljundini). Inglise keeles on selle näitaja nimi "*forward anonset*" või "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Teine näitab antud mündi võimalike allikate arvu, teades UTXO väljundis. See näitaja võimaldab mõõta müntide privaatsuse vastupanu analüüsile praegusest minevikku (väljundist sisendisse). Inglise keeles on selle näitaja nimi "*tagasi anonset*" või "*tagasi vaatlev metrika*"

![](../../dictionnaire/assets/40.webp)

> ► *Fransi keeles on üldtunnustatud kasutada terminit "anonset" Seda võib aga tõlkida ka kui "ensemble d'anonymat" või "potentiel d'anonymat" Nii inglise kui ka prantsuse keeles kasutatakse mõnikord anonüümide kohta ka terminit "score" (prospektiivne skoor ja retrospektiivne skoor).*