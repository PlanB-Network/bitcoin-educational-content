---
term: AATOMILISED MITMEPOOLSED MAKSED
---

MPP (*Multi-Path Payments*) täiustatud versioon, kus igal maksefragmendil on eraldi osaline saladus, mis tagab, et tehing arveldatakse aatomiliselt, st kas täies ulatuses või üldse mitte.


MPP-d on Lightningi maksetehnikad, mis võimaldavad tehingu jaotada mitmeks väiksemaks osaks ja suunata seda erinevate marsruutide kaudu. Teisisõnu, iga maksefraktsioon võtab erineva sõlme tee. Sellega välditakse likviidsuspiiranguid ühe kanali marsruudil. Põhiliste MPPde puhul jagab iga maksefraktsioon sama saladust ja seega HTLCdes sama Hash. See võib muuta tehingu jälgitavaks, kui vaatleja viibib mitmel marsruudil, sest ta saab kõik need identsed saladused omavahel siduda. Veelgi enam, kuna saladus on kõigi makseosade jaoks unikaalne, ei ole see aatomne. See tähendab, et mõned makse osad võivad olla edukalt sooritatud, samas kui teised võivad ebaõnnestuda.


AMP-s kasutatakse iga fraktsiooni jaoks unikaalseid osalisi saladusi. Kui kõik fragmendid on saadud, võimaldavad need vastuvõtjal rekonstrueerida algse üldsaladuse ja nõuda täielikku makset. See meetod muudab makse osalise tasumise võimatuks, sest täieliku makse avamiseks on vaja kõigi osaliste saladuste valdamist. See tagab, et makse on täielikult edukas või täielikult ebaõnnestunud (st aatomne). AMP parandab ka konfidentsiaalsust, kuna eri marsruutide vahel ei ole enam nähtavaid seoseid.


Üks AMP-de eelis on see, et need toimivad isegi siis, kui ainult vastuvõtja ja saatja on seda meetodit rakendanud. Vahendussõlmed töötlevad neid makseid tavapäraste tehingutena, kasutades HTLCsid, teadmata, et nad töötlevad suurema makse murdosa.