---
term: COINBASE (TEHING)

---
Coinbase'i tehing on eriline ja ainulaadne tehing, mis sisaldub igas Bitcoini plokiahela plokis. See kujutab endast ploki esimest tehingut ja selle on loonud kaevandaja, kes on edukalt leidnud töötõendit kinnitava päise (*Proof-of-Work*), st vähem või võrdne sihtmääraga.

Coinbase'i tehingul on peamiselt kaks eesmärki: anda kaevandajale plokihüvitis ja lisada uusi bitcoinide ühikuid ringluses olevale rahavarule. Plokihüvitis, mis on kaevandajate majanduslik stiimul töö tõestamiseks, sisaldab kogunenud tasusid plokis sisalduvate tehingute eest ja kindlaksmääratud kogust uusi loodud bitcoine ex-nihilo (plokisubsiidium). See summa, mis algselt 2009. aastal oli 50 bitcoini ploki kohta, väheneb iga 210 000 ploki järel (umbes iga 4 aasta tagant) poole võrra "pooleks"

Coinbase'i tehing erineb tavalisest tehingust mitmeti. Esiteks ei ole sellel sisendit, mis tähendab, et see ei tarbi ühtegi olemasolevat tehingu väljundit (UTXO). Seejärel sisaldab coinbase'i tehingu allkirjastamisskript (`scriptSig`) tavaliselt suvalist välja, mis võimaldab lisada täiendavaid andmeid, näiteks kohandatud sõnumeid või teavet kaevandamistarkvara versiooni kohta. Lõpuks kohaldatakse coinbase'i tehingu poolt genereeritud bitcoinide suhtes 100 plokki (101 kinnitust) pikkust küpsusperioodi enne nende kulutamist, et vältida ahela reorganiseerimise korral võimalikku olematute bitcoinide kulutamist.

> ► *Tõlge "Coinbase" prantsuse keeles puudub. Seetõttu on lubatud kasutada seda terminit otse.*