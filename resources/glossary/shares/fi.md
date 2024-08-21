---
termi: SHARES
---

Louhinta-altaiden kontekstissa osuus on indikaattori, jota käytetään yksittäisen louhijan panoksen mittaamiseen altaassa. Tämä mittari toimii perustana laskettaessa palkkiota, jonka allas jakaa kullekin louhijalle. Jokainen osuus vastaa hashia, joka täyttää vaikeustavoitteen, joka on matalampi kuin Bitcoin-verkon vaatimus.

Selittääksemme analogian avulla, kuvittele 20-sivuinen noppa. Bitcoinissa oletetaan, että työn todistamiseen vaaditaan numeron heittämistä, joka on pienempi kuin 3 lohkon vahvistamiseksi (eli saavutetaan tulos 1 tai 2). Nyt kuvittele, että louhinta-altaassa osuuden vaikeustavoite on asetettu 10:een. Näin ollen yksittäiselle louhijalle altaassa jokainen nopanheitto, joka tuottaa numeron alle 10, lasketaan kelvolliseksi osuudeksi. Nämä osuudet sitten siirretään louhijalta altaalle, jotta hän voi vaatia palkkionsa, vaikka ne eivät vastaisikaan kelvollista tulosta Bitcoinin lohkolle.

Jokaisella lasketulla hashilla yksittäinen louhija altaassa voi kohdata kolme erilaista skenaariota:
* Jos hash-arvo on suurempi tai yhtä suuri kuin altaan asettama vaikeustavoite osuudelle, tämä hash on hyödytön. Louhija vaihtaa nonce-arvoaan yrittäessään uutta hashia: `hash > osuus > lohko`.
* Jos hash on pienempi kuin osuuden vaikeustavoite, mutta suurempi tai yhtä suuri kuin Bitcoinin vaikeustavoite, tämä hash muodostaa kelvollisen osuuden, joka ei kuitenkaan riitä lohkon vahvistamiseen. Louhija voi lähettää tämän hashin altaalleen vaatiakseen siihen liittyvää palkkiota: `osuus > hash > lohko`.
* Jos hash on pienempi kuin Bitcoin-verkon vaikeustavoite, sitä pidetään sekä kelvollisena osuutena että kelvollisena lohkona. Louhija lähettää tämän hashin altaalleen, joka kiirehtii lähettämään sen Bitcoin-verkkoon. Tätä hashia pidetään myös kelvollisena osuutena louhijalle: `osuus > lohko > hash`.

![](../../dictionnaire/assets/32.png)

Tätä osuusjärjestelmää käytetään arvioimaan kunkin yksittäisen louhijan tekemää työtä altaassa, ilman että kaikkia louhijan tuottamia hasheja tarvitsee laskea uudelleen, mikä olisi täysin tehotonta altaan kannalta.

Louhinta-altaat säätävät osuuksien vaikeustasoa tasapainottaakseen varmennuskuormaa ja varmistaakseen, että jokainen louhija, olipa hän sitten pieni tai suuri, lähettää osuuksia suunnilleen joka muutaman sekunnin välein. Tämä mahdollistaa kunkin louhijan hashraten tarkan laskennan ja palkkioiden jakamisen valitun korvauslaskentamenetelmän mukaan (PPS, PPLNS, TIDES...).

> ► *Ranskaksi "shares" voidaan kääntää "part" -sanalla.*