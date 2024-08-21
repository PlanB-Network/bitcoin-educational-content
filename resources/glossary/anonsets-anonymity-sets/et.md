---
term: ANONSETS (ANONÜÜMSUSKOMPLEKTID)
---

Anonüümsuskomplektid toimivad indikaatoritena, et hinnata konkreetse UTXO privaatsuse taset. Täpsemalt mõõdavad nad eristamatute UTXOde arvu komplektis, mis sisaldab uuritavat münti. Kuna on vajalik identsete UTXOde grupp, arvutatakse anonüümsuskomplekte tavaliselt mündiühenduste tsüklis. Need võimaldavad vajadusel hinnata mündiühenduste kvaliteeti. Suur anonüümsuskomplekt tähendab suuremat anonüümsuse taset, kuna konkreetse UTXO eristamine komplektis muutub keeruliseks. Anonüümsuskomplektid jagunevad kaheks tüübiks:
* Eeldatav anonüümsuskomplekt;
* Tagasiulatuv anonüümsuskomplekt.

Esimene näitab grupi suurust, mille hulgas uuritav UTXO on peidetud, teades UTXOt sisendis. See näitaja võimaldab mõõta mündi privaatsuse vastupanuvõimet analüüsile minevikust olevikku (sisendist väljundini). Inglise keeles on selle näitaja nimetus “*forward anonset*” ehk “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

Teine näitab võimalike allikate arvu antud mündile, teades UTXOt väljundis. See näitaja võimaldab mõõta mündi privaatsuse vastupanuvõimet analüüsile olevikust minevikku (väljundist sisendini). Inglise keeles on selle näitaja nimetus “*backward anonset*” ehk “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *Prantsuse keeles on üldiselt aktsepteeritud kasutada terminit “anonset”. Siiski võiks seda tõlkida kui “anonüümsuskomplekt” või “anonüümsuse potentsiaal”. Nii inglise kui ka prantsuse keeles kasutatakse mõnikord anonüümsuskomplektide viitamiseks ka terminit “score” (eeldatav skoor ja tagasiulatuv skoor).*