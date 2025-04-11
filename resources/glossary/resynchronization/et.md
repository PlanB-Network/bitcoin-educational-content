---
term: RESÜNKRONISEERIMINE

---
Viitab nähtusele, mille puhul plokiahelas toimub selle struktuuri muutmine konkureerivate plokkide olemasolu tõttu samal kõrgusel. See toimub siis, kui osa plokiahelast asendatakse teise ahelaga, millel on suurem kogus kogutud tööd.

Need resünkroniseerimised on osa Bitcoini loomulikust toimimisest, kus erinevad kaevurid võivad leida uusi plokke peaaegu samaaegselt, jagades seega Bitcoini võrgu kaheks. Sellistel juhtudel võib võrk ajutiselt jaguneda konkureerivateks ahelateks. Lõpuks, kui üks neist ahelatest kogub rohkem tööd, loobuvad teised ahelad sõlmedest ja nende plokid muutuvad nn "vananenud plokkideks" või "orvuks jäänud plokkideks" See ühe ahela asendamine teise ahelaga on resünkroniseerimine.

![](../../dictionnaire/assets/9.webp)

Resünkroniseerimisel võib olla mitmesuguseid tagajärgi. Esiteks, kui kasutajal on kinnitatud tehing plokis, mis osutub mahajäetud tehinguks, kuid seda tehingut ei leidu lõppkokkuvõttes kehtivas ahelas, siis muutub tema tehing uuesti kinnitamata tehinguks. Seepärast on soovitatav alati oodata vähemalt 6 kinnitust, et pidada tehingut tõeliselt muutumatuks. Pärast 6 ploki sügavust on resünkroniseerimine nii ebatõenäoline, et selle esinemise tõenäosust võib pidada praktiliselt olematuks.

Lisaks tähendab resünkroniseerimine globaalsel süsteemi tasandil kaevurite arvutusvõimsuse raiskamist. Kui toimub jagunemine, on mõned kaevurid ahelas "A" ja teised ahelas "B". Kui ahel "B" jäetakse lõpuks resünkroniseerimise käigus kõrvale, siis kogu kaevurite poolt selles ahelas kasutatud arvutusvõimsus läheb definitsiooni kohaselt raisku. Kui Bitcoini võrgus on liiga palju resünkroniseerimisi, väheneb seega võrgu üldine turvalisus. See on osaliselt põhjus, miks plokkide suuruse suurendamine või plokkide vahelise intervalli (10 minutit) vähendamine võib olla ohtlik.

> ► * Mõni bitcoin'i kasutaja eelistab kasutada "orphan block", et viidata aegunud plokile. Samuti, kuigi see on anglizism, eelistatakse üldkeeles sageli "reorganiseerimist" või "reorg" "resünktroniseerimisele" *