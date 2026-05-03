---
name: Lightning Network+
description: Hanki ilmaista tulevaa likviditeettiä Lightning-solmun osuuskunta-avausten avulla
---

![cover](assets/cover.webp)



## Johdanto



[LN+ (Lightning Network Plus)] (https://lightningnetwork.plus/) on yhteisöalusta, joka on suunniteltu helpottamaan Lightning Network-solmujen operaattoreiden välistä yhteistyötä. Sen päätavoitteena on parantaa Lightning-verkon liitettävyyttä, likviditeettiä ja hajauttamista ilman keskitettyjä välittäjiä.



Tässä oppaassa keskitytään **"Swaps "**-palveluun, joka on LN+:n nykyisin käytetyin ja rakenteellisin ominaisuus. Myös muut alustan tarjoamat palvelut esitellään.



## LN+ yleiskatsaus



### Mikä on Lightning Network Plus?



Lightning Network Plus (LN+) on yhteisöalusta Lightning-solmujen operaattoreille, jotka haluavat tehdä yhteistyötä suoraan ja vapaaehtoisesti. Sen tavoitteena on helpottaa hyödyllisten, tasapainoisten ja kestävien Lightning-kanavien luomista välttäen samalla keskitettyjen ratkaisujen tai määrättyjen keskusten tarvetta.



LN+ perustuu perusperiaatteeseen: vertaisyhteistyöhön, joka perustuu avoimuuteen, vastavuoroisuuteen ja maineeseen.



### LN+-palvelut yhdellä silmäyksellä



LN+ tarjoaa useita palveluja, joiden tarkoituksena on parantaa Lightning-verkon topologiaa ja likviditeettiä, kuten :





- Vaihdot**: operaattoreiden välisten kanavien vastavuoroinen avaaminen (pääpalvelu).
- Rengas**: pyöreät kanavien aukot useiden osallistujien välillä.
- Luottamukseen perustuvat swapit**: muunnelmat, jotka perustuvat enemmän osallistujien luottamukseen ja historiaan.
- Sosiaaliset ominaisuudet**: profiilit, kommentit ja mainejärjestelmä.



Tämän ohjeen loppuosassa keskitymme yksinomaan **Swaps**-palveluun, joka on LN+:n nykyisen käytön ydin.



## LN+ "Swaps"-palvelu



### LN+-swapin määritelmä



LN+ **swap** on kahden Lightning-solmun ylläpitäjän vapaaehtoinen sopimus avata vastavuoroisesti kapasiteetiltaan vastaavat (tai ennalta sovitut) Lightning-kanavat. Toisin kuin tavanomainen yksipuolinen kanavien avaaminen, swap perustuu **selvään vastavuoroisuuteen**.



Käytännössä :





- Avaat kanavan kumppanisi solmuun.
- Kumppanisi avaa kanavan solmuun.
- Molemmat osapuolet sitovat samanlaisen määrän on-chain-bittikolikoita.



### Mikä on solmujen operaattoreiden vaihtojen tarkoitus?



Swaps-palvelussa käsitellään useita Lightning-operaattoreiden kohtaamia keskeisiä ongelmia:





- Parempi liitettävyys**: hyödyllisten kaksisuuntaisten kanavien luominen heti, kun ne on avattu.
- Parempi likviditeetin hallinta**: kummallakin osapuolella on sekä saapuvaa että lähtevää kapasiteettia.
- Tarpeettomien kanavien riskin väheneminen**: kumppania kannustetaan pitämään kanava auki.
- Suurempi hajauttaminen**: suorat yhteydet operaattoreiden välillä ilman määrättyjä keskuksia.



### Mille solmuprofiileille vaihtaminen on hyödyllistä?



Vaihdot ovat erityisen hyödyllisiä :





- Uudet solmut, jotka haluavat nopeasti parantaa reitityskykyään.
- Välittäjäoperaattorit, jotka haluavat lisätä kanavagrafiikkansa tiheyttä.
- Reititykseen suuntautuneet solmut, jotka haluavat optimoida topologiansa.



## Liitä Lightning-solmu LN+:aan



### Tekniset vaatimukset



Ennen kuin aloitat, tarvitset :





- Toimiva Lightning-solmu (LND, Core Lightning tai Eclair).
- Pääsy solmun hallintakäyttöliittymään.
- Riittävä on-chain-kapasiteetti kanavien avaamiseksi.



Mene [Lightning Network](https://lightningnetwork.plus/) Plus -sivustolle ja napsauta käyttöliittymän oikeassa yläkulmassa olevaa `Login`-painiketta.



![capture](assets/fr/03.webp)



### Todentaminen viestin allekirjoituksella



Jotta voit todentaa itsesi, sinun on allekirjoitettava toimitettu viesti Lightning-solmun yksityisellä avaimella. ThunderHub:n avulla tämä toiminto on hyvin yksinkertainen.



Aloita kopioimalla LN+:n näyttämä viesti.



![capture](assets/fr/04.webp)



Siirry ThunderHub:ssa välilehdelle "Työkalut" ja napsauta sitten "Viestit"-osion "Allekirjoita"-painiketta.



![capture](assets/fr/05.webp)



Liitä LN+:n antama todennusviesti ja napsauta sitten "Allekirjoita".



![capture](assets/fr/06.webp)



ThunderHub allekirjoittaa tämän viestin solmun yksityisellä avaimella. Kopioi luotu allekirjoitus.



![capture](assets/fr/07.webp)



Liitä tämä allekirjoitus LN+-sivuston vastaavaan kenttään ja napsauta sitten "Kirjaudu sisään".



![capture](assets/fr/08.webp)



Olet nyt yhteydessä LN+:aan Lightning-solmun kanssa. Tämän prosessin avulla LN+ voi tarkistaa, että olet sen solmun laillinen omistaja, jonka olet ilmoittanut heidän alustalleen.



![capture](assets/fr/09.webp)



Voit halutessasi muokata LN+-profiiliasi, esimerkiksi lisäämällä lyhyen elämäkerran.



## Osallistu olemassa olevaan swapiin



### Pääsy vaihtotarjouksiin



Jos haluat osallistua ensimmäiseen kanavan avaamiseen, siirry käyttöliittymän yläosassa olevaan `Swaps`-valikkoon. Täältä löydät kaikki tällä hetkellä saatavilla olevat swapit solmusi ominaisuuksista riippuen.



![capture](assets/fr/10.webp)



### Kelpoisuusehdot



Jos haluat liittyä olemassa olevaan vaihtotarjoukseen, valitse vain vastaava ilmoitus ja rekisteröidy. LN+ sallii kuitenkin swap-tarjouksen laatijan määritellä tietyt **kelpoisuusehdot**, kuten :





- vähimmäismäärä jo avattuja kanavia ;
- solmujen vähimmäiskapasiteetti ;
- tietyntyyppiset yhteydet hyväksytään.



### Viimeisimmät solmut



Tämän vuoksi varsinkin käytön alkuvaiheessa on mahdollista, että solmusi on **vähän tarjouksia tai ei lainkaan tarjouksia**. Tämä on yleinen tilanne uusille solmuille tai solmuille, jotka eivät ole vielä liittyneet.



Minun tapauksessani yksikään tarjous ei täyttänyt vaadittuja kriteerejä, vaikka avoimia kanavia oli muutama.



## Luo oma vaihtotarjouksesi



### Milloin sinun pitäisi luoda oma swap?



Kun olemassa olevaa tarjousta ei ole saatavilla, oman vaihtokaupan luominen on usein paras ratkaisu. Sen avulla voit myös säilyttää swapin parametrien hallinnan.



### Vaihda kokoonpano



Napsauta **Start Liquidity Swap** ja määritä sitten tarjousparametrit:





- valitse osallistujien kokonaismäärä (3, 4 tai 5);
- ilmoittavat avattavien kanavien kapasiteetin;
- määritellä sitoumuskausi, jonka aikana osallistujat sitoutuvat olemaan sulkematta kanaviaan;
- täsmennetään mahdolliset osallistujiin sovellettavat rajoitukset (kanavien vähimmäismäärä, kokonaiskapasiteetin vähimmäismäärä, hyväksytty yhteystyyppi).



![capture](assets/fr/11.webp)



### Julkaiseminen ja osallistujien odotukset



Kun kaikki parametrit on syötetty, napsauta **Aloita Liquidity Swap** julkaistaksesi tarjouksesi. Nyt sinun tarvitsee vain odottaa, että muut operaattorit ilmoittautuvat mukaan.



![capture](assets/fr/12.webp)



## Vaihdon viimeistely



### Tehokas kanavan avautuminen



Nyt kun kaikki vaihtopaikat on otettu, kukin osallistuja näkee LN+-käyttöliittymästä, mihin solmuun hänen on avattava salamakanava.



![capture](assets/fr/13.webp)



Avaa kanava omalla puolellasi LN+:n antamalla solmutunnuksella ja ilmoitettua määrää noudattaen. Tämä toiminto voidaan suorittaa ThunderHub:n, toisen Lightning-solmuhallinnan tai suoraan solmusi perusliittymän kautta.



![capture](assets/fr/14.webp)



Kun kanava on avattu, se ilmestyy odottavat kanavat -osioon.



![capture](assets/fr/15.webp)



### Vahvistus LN+:ssa



Palaa sitten takaisin LN+:een ja vahvista, että olet aloittanut kanavan avaamisen, napsauttamalla "Kanavan avaaminen aloitettu" -painiketta.



![capture](assets/fr/16.webp)



### Vaihdon loppu



Kun kaikki osallistujat ovat avanneet ne kanavat, joihin ne ovat sitoutuneet, swapin katsotaan olevan valmis.



## Maine ja hyvät viestintäkäytännöt



### LN+-mainejärjestelmä



LN+ sisältää mainejärjestelmän, joka perustuu osallistujien vaihtojen päätyttyä jättämiin mielipiteisiin. Nämä mielipiteet ovat julkisia ja vaikuttavat suoraan operaattorin mahdollisuuksiin liittyä tuleviin swappeihin tai luoda niitä.



![capture](assets/fr/17.webp)



### Suositellut parhaat käytännöt



Hyvän maineen säilyttämiseksi ja swappien sujuvan toiminnan varmistamiseksi on suositeltavaa, että :





- noudattaa kanavien avaamisen määräaikoja ;
- viestiä nopeasti ongelman tai viivästyksen sattuessa;
- käytä kommenttiosastoa vaihtaaksesi näkemyksiä muiden osallistujien kanssa;
- ei sulje kanavaa ennen sitoumuskauden päättymistä.




![capture](assets/fr/18.webp)



### Miksi maine on keskeinen tekijä LN+:ssa



LN+ perustuu vapaaehtoisen yhteistyön malliin, jossa ei ole vahvoja teknisiä rajoitteita. Näin ollen maine on tärkein kannustin, jolla varmistetaan osallistujien luotettavuus ja luotettavuus.



## Muut LN+-palvelut



Swap-palvelujen lisäksi LN+ tarjoaa muita palveluja, joiden tarkoituksena on parantaa Lightning-solmujen operaattoreiden välistä yhteenkuuluvuutta ja koordinointia. Rings** mahdollistaa sen, että useat osallistujat voivat luoda kanavien avautumissilmukan, mikä vahvistaa reititysreittien redundanssia ja Lightning-graafin tiheyttä. Luottamukseen perustuvat swapit** perustuvat samankaltaisiin periaatteisiin kuin klassiset swapit, mutta ne tarjoavat enemmän joustavuutta osallistujille, joilla on jo vakiintunut maine alustalla.



LN+ sisältää myös sosiaalisia ominaisuuksia, kuten julkisia solmuprofiileja, kommenttien vaihtoa ja mainejärjestelmää. Nämä välineet eivät ole sinänsä teknisiä palveluja, mutta niillä on keskeinen rooli alustan sujuvassa toiminnassa, sillä ne helpottavat viestintää, koordinointia ja luottamusta toimijoiden välillä.



## Päätelmä



LN+:n Swaps-palvelu on tehokas väline Lightning-verkon yhteyksien, likviditeetin ja hajauttamisen parantamiseen. Edistämällä vastavuoroisia, koordinoituja kanavien avauksia LN+ antaa solmujen operaattoreille mahdollisuuden vahvistaa topologiaansa ja edistää samalla vastuullista, hajautettua yhteistyötä.