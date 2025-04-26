---
term: CPFP (LAPS MAKSAB VANEMA EEST)

---
Tehingumehhanism, mille eesmärk on kiirendada Bitcoini tehingu kinnitamist, sarnaselt sellega, mida teeb Replace-by-Fee (RBF), kuid vastuvõtja poolelt. Kui tehing, mille tasud on turuga võrreldes liiga madalad, jääb sõlmede mempoolsesse ummikusse ja ei kinnita piisavalt kiiresti, saab saaja teha uue tehingu, kulutades blokeeritud tehingus saadud bitcoinid, kuigi see ei ole veel kinnitatud. See teine tehing eeldab tingimata, et esimene tehing tuleb kaevandada, et seda saaks kinnitada. Seega on kaevandajad sunnitud mõlemad tehingud koos arvestama. Teise tehingu eest makstakse palju rohkem tehingutasusid kui esimese eest, nii et keskmine tasu julgustab kaevandajaid mõlemat tehingut lisama. Laps-tehing (teine) maksab kinni jäänud vanemtehingu (esimene) eest. Seetõttu nimetatakse seda "CPFP"

Seega võimaldab CPFP saajal saada oma raha kiiremini kätte, hoolimata saatja poolt makstavatest madalatest algsetest tasudest, erinevalt RBF-st (*Replace-By-Fee*), mis võimaldab saatjal võtta initsiatiivi oma tehingu kiirendamiseks, suurendades tasusid.