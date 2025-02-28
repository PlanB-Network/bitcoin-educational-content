---
term: ESIALGNE PLOKKIDE ALLALAADIMINE (IBD)

---
Viitab protsessile, mille käigus sõlmpunkt laeb alla ja kontrollib plokiahelat Genesis'i plokist ning sünkroonib teiste sõlmedega Bitcoini võrgus. IBD tuleb läbi viia uue täieliku sõlme käivitamisel. Selle esialgse sünkroniseerimise alguses ei ole sõlmel teavet varasemate tehingute kohta. Seetõttu laeb ta iga ploki alla teistest võrgu sõlmedest, kontrollib selle kehtivust ja lisab selle seejärel oma plokiahela kohalikku versiooni. Tasub märkida, et IBD võib olla pikk ja ressursimahukas, kuna plokiahela ja UTXO kogumi suurus kasvab. Selle täitmise kiirus sõltub sõlme majutava arvuti arvutusvõimekusest, selle RAM-mälu mahust, mäluseadme kiirusest ja ribalaiusest. Kui teil on võimas internetiühendus ja sõlme majutatakse uusimal MacBookil, millel on palju RAM-i, võtab IBD vaid paar tundi, et anda teile aimu. Seevastu kui kasutate mikroarvutit, näiteks Raspberry Pi, võib IBD toiming võtta aega nädal või rohkemgi.

> ► *Fransi keeles on üldtunnustatud, et see viitab otseselt IBD-le. Mõnikord kasutatakse tõlget "synchronisation initiale" või "téléchargement initial des blocs "*