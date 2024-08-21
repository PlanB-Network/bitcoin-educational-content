---
term: ALGNE PLOKKIDE ALLALAADIMINE (IBD)
---

Viitab protsessile, mille käigus sõlm laadib alla ja kontrollib plokiahelat alates Genesis-plokist ning sünkroniseerib end Bitcoin'i võrgu teiste sõlmedega. IBD tuleb läbi viia uue täissõlme käivitamisel. Selle esialgse sünkroniseerimise alguses ei oma sõlm teavet varasemate tehingute kohta. Seetõttu laadib see alla iga ploki võrgu teistelt sõlmedelt, kontrollib selle kehtivust ja seejärel lisab selle oma kohalikku plokiahela versiooni. On oluline märkida, et IBD võib olla pikk ja ressursimahukas protsess seoses plokiahela ja UTXO komplekti kasvava suurusega. Selle teostamise kiirus sõltub sõlme majutava arvuti arvutusvõimest, RAM-i mahust, salvestusseadme kiirusest ja ribalaiusest. Et anda teile ettekujutus, kui teil on võimas internetiühendus ja sõlm on majutatud viimase põlvkonna MacBook'ile, millel on palju RAM-i, võtab IBD vaid mõned tunnid. Vastupidisel juhul, kui kasutate mikroarvutit nagu Raspberry Pi, võib IBD võtta nädala või kauem.

> ► *Prantsuse keeles on üldiselt aktsepteeritud viidata otse IBD-le. Mõnikord kasutatav tõlge on "synchronisation initiale" või "téléchargement initial des blocs".*