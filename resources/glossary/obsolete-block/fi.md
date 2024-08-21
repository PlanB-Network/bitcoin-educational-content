---
termi: VANHENTUNUT (LOHKO)
---

Viittaa lohkoon ilman lapsia: kelvollinen lohko, mutta jätetty pois pääasiallisesta Bitcoin-ketjusta. Tämä tapahtuu, kun kaksi louhijaa löytää kelvollisen lohkon samalla ketjun korkeudella lyhyen ajan sisällä ja lähettää sen verkkoon. Solmut valitsevat lopulta vain yhden lohkon sisällytettäväksi ketjuun, perustuen eniten kumulatiivista työtä sisältävän ketjun periaatteeseen, tehden toisesta "vanhentuneen". Vanhentuneen lohkon tuottava prosessi on seuraavanlainen:
* Kaksi louhijaa löytää kelvollisen lohkon samalla ketjun korkeudella lyhyen aikavälin sisällä. Kutsutaan niitä `Lohko A` ja `Lohko B`;
* Kumpikin lähettää lohkonsa Bitcoin-solmuverkkoon. Jokaisella solmulla on nyt 2 lohkoa samalla korkeudella. Näin ollen on olemassa kaksi kelvollista ketjua;
* Louhijat jatkavat työn todistusten etsimistä seuraaville lohkoille, mutta tehdäkseen niin, heidän on välttämättä valittava vain yksi lohko `Lohko A` ja `Lohko B` väliltä, jolla he louhivat;
* Louhija löytää lopulta kelvollisen lohkon `Lohko B`n yläpuolelta. Kutsutaan sitä `Lohko B+1`;
* He lähettävät `Lohko B+1`n verkon solmuille;
* Koska solmut seuraavat pisintä ketjua (jossa on eniten kumulatiivista työtä), ne arvioivat, että `Ketju B` on seurattava;
* Ne hylkäävät `Lohko A`n, joka ei enää ole osa pääketjua. Siitä on siten tullut vanhentunut lohko.

![](../../dictionnaire/assets/9.png)

> ► *Englanniksi tätä kutsutaan "Stale Block"ksi. Ranskaksi sitä voidaan myös kutsua "bloc périmé" tai "bloc abandonné". Vaikka en olekaan samaa mieltä tästä käytöstä, jotkut bitcoinistit käyttävät termiä "bloc orphelin" viitatakseen siihen, mikä itse asiassa on vanhentunut lohko.*