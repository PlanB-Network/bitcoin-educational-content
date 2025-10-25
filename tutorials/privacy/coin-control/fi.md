---
name: Coin Control
description: Tutustu Coin Controliin, tärkeään työkaluun yksityisyytesi suojaamiseksi Bitcoinissa
---
![cover](assets/cover.webp)


*Tämä opetusmateriaali on tuotu [Officine Bitcoinin oppitunnista](https://officinebitcoin.it/lezioni/coinco/).*



## Johdanto



Bitcoin-protokollan vakaus taataan yksinkertaisten keskeisten käsitteiden avulla. Näistä korostuu läpinäkyvyys: kaikki Bitcoin-tapahtumat ovat julkisia ja kenen tahansa helposti tarkistettavissa. Vaikka tämä ominaisuus on protokollan kulmakivi, koska se estää petoksia ja takaa varojen aitouden, se voi myös muodostaa haasteen luottamuksellisuudelle. **Oletko koskaan miettinyt, voiko tällainen läpinäkyvyys heikentää yksityisyyttäsi?**



Sinun pitäisi. Vaikka Satoshi non-kyc:n kerääminen on melko helppoa, yksityisyytesi on suurimmassa vaarassa heti käyttövaiheessa.



### Mitä tapahtuu, kun käytät UTXO



Bitcoin:n käyttäminen ei ole pelkästään arvon siirtämistä jollekin toiselle.



Kuluttamalla yhden UTXO-varoistasi sinun on itse asiassa täytettävä protokollan avoimuudelle asetetut ehdot, koska sinulla on velvollisuus todistaa, että omistat kyseiset varat. Näin ollen teet itsesi vastuulliseksi :




- paljastaa julkisen avaimesi;
- tuottaa digitaalisen allekirjoituksen.



Kulutusajankohta on siis kaikkein kriittisin: ** Bitcoin:n kuluttaminen on teko, joka on tehtävä tietoisesti ja mahdollisimman hyvin hallitusti**.



## Coin ohjaus



Bitcoin-protokollassa ei ole sellaisia nimikkeitä kuin _tili_ tai _rahayksiköt_. UTXO:n käsite selitetään erinomaisesti seuraavalla kurssilla, jota suosittelen lämpimästi:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoin:n avulla keräät ja myöhemmin kulutat pieniä tai suuria tiliyksiköitä, jotka mitataan Satoshi:ssä ja joita edustavat "käyttämättömät transaktiotulokset", **UTXO**, joita kutsutaan myös "kolikoiksi". Kun käytät UTXO:ita transaktion luomiseen, ne tuhoutuvat kokonaan ja niiden tilalle luodaan muita UTXO:ita.



Ohjelmistolompakot on kehitetty tekemään tämä valinta automaattisesti, käyttämällä "satunnaisesti" valittuja kolikoita ja hyväksymällä tietyt protokollan tarjoamat algoritmit. Ainoa kriteeri, jonka nämä algoritmit täyttävät, on, että ne kattavat kulutukseen tarvittavan määrän.



Ne voivat sekoittaa eri-ikäisiä UTXO:ita tai suosia uusimpia tai "vanhimpia", riippuen kehittäjien valitsemasta algoritmista. Parhaat ohjelmistolompakot aikovat myös jättää käyttäjälle tärkeän valinnan.



Coin Control -käsikirja, jota kutsutaan myös nimellä Coin Selection, on joidenkin ohjelmistolompakoiden ominaisuus, jonka avulla voit **manuaalisesti valita UTXO:t käytettäväksi, kun rakennat tapahtumaa**.



Oletetaan, että meillä on Wallet, jolla on kolme UTXO:ta, jotka ovat vastaavasti 21 000, 42 000 ja 63 000 Satoshi.



![img](assets/en/01.webp)



Jos sinun on käytettävä 24 000 Sats ja annettava algoritmin tehdä automaattinen valinta, hyvä Software Wallet saattaa päättää yhdistää UTXO 1 + UTXO 2 maksaakseen 24 000 Sats- ja Miner-maksut, jolloin jäljelle jäävä määrä menee takaisin aloittavan Wallet:n sisäiseen Address:ään.



![img](assets/en/02.webp)



Liiketoimen jälkeen Wallet:n uusi tilanne, jossa otetaan huomioon vain UTXO:t, voidaan tiivistää seuraavasti.



![img](assets/en/03.webp)



Oikean ohjelmiston ja tietoisuutesi avulla olisit kuitenkin voinut tehdä toisenlaisen, tavallaan oikeamman valinnan. Esimerkiksi valitsemalla vain UTXO2 (42 000 Sats:sta).



![img](assets/en/04.webp)



Kun Wallet:n lopputilanne on UTXO:n tasolla, se näyttää erilaiselta kuin aiemmin.



![img](assets/en/05.webp)



## Miksi manuaalinen coin control?



![img](assets/en/06.webp)



Edellä olevissa kahdessa esimerkissä saldo on itse asiassa sama: 108 280 Sats. Käytettyämme 24 000 Sats, ilman manuaalista valintaa meillä olisi 2 UTXO Wallet:ssä; Coin:n manuaalisella valvonnalla meillä on yhteensä 3 UTXO.



Kysymys, jonka voisimme esittää itsellemme, on seuraava: **miksi tehdä tämä kaikki?** On olemassa, tai voisi olla, useita syitä siihen, miksi emme käyttäneet `UTXO1`:tä **ja ne kaikki muodostavat perustan sille, miksi kulutuksen yhteydessä manuaalisen coin controlin aktivointi on yksi hyvistä käytännöistä, joita tulisi noudattaa**.



Valitsemalla UTXO:t voit suosia joitakin näkökohtia toisten kustannuksella. Valinta riippuu siitä, mitä tavoitteita haluat saavuttaa.



### Yksityisyys



Yksi tärkeimmistä eduista manuaalisessa Coin-valvonnassa on **suurin yksityisyys rahan antajalle**. Otetaan aina esimerkki: 24 000 Satoshi:n menot _ilman manuaalista Coin-valintaa_. Koska Bitcoin:n Blockchain on julkinen tietue, ulkopuolinen tarkkailija voi ilman epäilyksen häivääkään todeta, että tulot `UTXO1 21 000 Sats:sta` ja `UTXO2 42 000 Sats:sta` sekä loput, `UTXO5 38 280 Sats:sta` **kaikki kolme kuuluvat samalle käyttäjälle**.



Jos taas valitset manuaalisesti "UTCOXO2", "UTCOXO1" pysyy täysin varattuna ja odottaa UTXO-sarjassa, että se käytetään sopivampana ajankohtana.



UTXO1 voi olla peräisin KYC-lähteestä, kuten Exchange:ssa tavaroista ja palveluista saadusta maksusta, kun taas muut UTXO:t eivät. UTXO-kyc:n sekoittaminen muihin, luottamuksellisempiin varoihin vaarantaa muiden kuin KYC-varojen anonymiteettiaseman.



**KYC-varat johtaisivat väistämättä maksajan henkilöllisyyden paljastumiseen. Jos se olisi sinun lompakkosi, haluaisitko, että ulkopuolinen tarkkailija voisi jäljittää henkilöllisyytesi niin ehdottomalla varmuudella?**



Yritä sitten ottaa huomioon, että esimerkiksi lompakot, jotka toteuttavat UTXO:iden manuaalisen valinnan, mahdollistavat yhden tai useamman UTXO:n **erottelun**, joka on toiminto, jota voidaan käyttää tällaisissa tilanteissa.



Vaikka olen vakuuttunut siitä, että KYC-varat olisi pidettävä erillisessä Wallet:ssa kuin ilman kyc:tä ostettu Bitcoin, jos tämä on sinun tapauksessasi, joidenkin osoitteiden erottaminen toisistaan on tärkeä apu, jota voisit hyödyntää opettelemalla valitsemaan manuaalisesti kulutustulosi.



### Maksujen säästäminen



Oikean UTXO:n valitseminen menojen tekemiseksi **antaa mahdollisuuden maksujen optimointiin**. Jälleen aloittaen alkuperäisestä esimerkistämme, Software Wallet valitsi kaksi UTXO:ta kattamaan suoritettavan menon. Kaksi UTXO:ta merkitsee kahta verkolle näytettävää allekirjoitusta. Tästä seuraa, että tapahtumalla on suurempi "painoarvo" vBytesin suhteen.



Coin:n manuaalisella ohjauksella voit toisaalta valita vain yhden, joka riittää kattamaan summan, jolloin säästät maksuja vähentämällä tapahtuman "painoa".



Kun maksut ovat korkeat, mutta sinun on pakko käyttää Bitcoin On-Chain (esimerkiksi Lightning Network-kanavan avaamiseen), silloin Coin-ohjaus osoittautuu oikeaksi taloudelliseksi kannustimeksi.



### Jäännösten yhdistäminen



Kun teet maksun ja käytät Bitcoin On-Chain:tä, mahdollisuus saada vaihtorahaa on lähes aina varmaa. Jokainen jäännös on itsessään pieni yksityisyyden menetys, sillä se paljastaa verkolle (ja erityisesti maksun vastaanottajalle) sinun Address:si, joka voidaan yhdistää lähdetietoihisi.



Ottaen huomioon, että paras Wallet HDs generate erityiset osoitteet jäänteitä, voit helposti tunnistaa ne ja "erottaa" kaikki jäänteet eri liiketoimien tehtyjen; kun ne ovat saavuttaneet tietyn määrän, voit valita ne manuaalisesti ja konsolidoida ne tai vaihtaa Lightning Network (suosikkimenetelmäni) ja käsitellä niitä, jotta voit saada takaisin yksityisyyden menettänyt menoja.



### Cold:n Wallet:n menot



Cold Wallet on väline, jolla voidaan kohtuullisesti saavuttaa hyvä turvallisuus, jotta voidaan säilyttää mikä tahansa määrä varoja, joita voidaan pitää sivussa pitkän ajanjakson ajan. Ennakoimattomia tapahtumia voi kuitenkin sattua, joten syntyy tarve päästä käsiksi säästöihin ja vastata joihinkin odottamattomiin menoihin.



En tiedä, kuinka moni voi jakaa lähestymistapani, mutta neuvoni on, että **ei koskaan tee menoja suoraan Cold Wallet, jotta vältät muutosten saamisen samojen osoitteiden välillä**. Opettele valitsemaan manuaalisesti UTXO:t, joita tarvitaan menon kattamiseen, siirrä ne Wallet Hot:een ja valmistele tapahtuma jälkimmäisestä. Mahdolliset vaihtorahat voit sitten lähettää takaisin Cold Wallet Address:een (jos määrä on riittävä), käyttää ne muihin kuluihin tai edelleen erottaa ne toisistaan, kuten äsken näimme.



## Käytännön esittely


Kun olemme esitelleet teknisen esittelyn "miksi", katsotaan, miten Coin:n käsisäätö voidaan toteuttaa käytännössä eri ohjelmistojen, työpöytä- ja mobiiliohjelmistojen avulla. Käytämme aina samaa Wallet BIP39:ää, joka on tuotu kumpaankin valittuun työkaluun, jotta voimme näyttää niiden väliset pienet erot.



## Wallet pöytäkone



### Sparrow



Jos käytät Sparrow:a, avaa Wallet ja valitse vasemmanpuoleisesta valikosta _UTXOs_. Näet luettelon kaikista Wallet:ään liittyvistä UTXO:ista.



Napsauta vain hiirellä jotakin niistä ja valitse sitten _Send Selected_. Sparrow näyttää myös valinnan jälkeen käytettävissä olevan summan suoraan komennon vieressä. Graafisesti Sparrow näyttää valitun UTXO:n korostamalla sen sinisellä.



![img](assets/en/07.webp)



Voit myös valita useamman kuin yhden. Auta itseäsi_CTRL_-näppäimellä, jotta voit valita luettelosta muita kuin vierekkäisiä UTXO:ita.



![img](assets/en/08.webp)



Kun olet valinnut UTXO:n manuaalisesti, voit aloittaa liiketoimen rakentamisen, ja Sparrow näyttää sinulle hyvin graafisesti, miten se muodostuu.



![img](assets/en/09.webp)



#### UTXO:n erottelu



Varojen erottelu tarkoittaa niiden "lukitsemista" Wallet:een siten, että niitä ei voida käyttää tapahtuman syöttötietoina. Sparrow sallii tämän toiminnon, jota käytetään aina _UTXOs_-valikosta: asetat hiiren "lukittavan" UTXO:n päälle ja napsautat hiiren oikeaa painiketta. Tämän toimenpiteen ominaisuuksien joukossa näkyy _Freeze UTXO_. Näin pystyt erottelemaan kolikot Sparrow-lompakoilla.



![img](assets/en/29.webp)



### Electrum



Jos Wallet-työpöytäsi on Electrum, sinun pitäisi tietää, että voit valita UTXO:t manuaalisesti joko _Addresses_-valikosta tai _Coins_-valikosta. Molemmissa valikoissa valinta tapahtuu osoittamalla hiirellä haluttuun UTXO:een ja valitsemalla hiiren oikealla painikkeella napsauttamisen jälkeen _Add to Coin control_.



![img](assets/en/10.webp)



Tälläkin ohjelmistolla voit valita useamman kuin yhden UTXO:n, mikä auttaa näppäimistön_CTRL_-näppäimellä, jos ne eivät ole vierekkäin.



![img](assets/en/11.webp)



Graafisesti Electrum näyttää valinnan korostamalla valitut UTXO:t Green:ssa, kun taas alareunassa näkyy samalla värillä korostettu palkki, joka näyttää käytettävissä olevan tasapainon Coin-säädön jälkeen.



![img](assets/en/12.webp)



Kun olet valinnut lähdön tai lähdöt, voit rakentaa tapahtuman tavalliseen tapaan _Lähetä_-valikosta.



#### UTXO:n erottelu



Electrum tarjoaa tämän toiminnon menemällä _Coins_-valikkoon, jossa valitset tietyn UTXO:n ja valitsemalla sitten _Freeze_ hiiren oikealla napsautuksella. Voit "jäädyttää" Address:n myös ilman varoja _Addresses_-valikosta, tai "Coin:n", jotta et käyttäisi sitä.



![img](assets/en/28.webp)



### Nunchuk



Nunchukin avulla voit valita UTXO:t manuaalisesti päävalikosta, kun se on avattu. Käynnistä Nunchuk ja valitse _View coins_.



![img](assets/en/13.webp)



Tämä avaa ikkunan, joka sisältää kaikki Wallet:n UTXO:t. Voit valita yhden tai useamman aktivoimalla kunkin määrän vieressä olevan valintamerkin. Kun olet tehnyt valintasi, jatka valitsemalla _Create transaction_.



![img](assets/en/14.webp)



Sen jälkeen voit syöttää määränpään Address ja asettaa summan ja maksut.



![img](assets/en/15.webp)



#### UTXO:n erottelu



Täydellisyyden vuoksi mainittakoon, että Nunchuk sallii ominaisuuksiensa joukossa myös yhden (tai useamman) UTXO:n erottamisen, ja se tehdään kahdella eri tavalla. Käynnistä _View coins_ -valikko ja valitse manuaalisesti kolikkoluettelosta. Napsauta sitten oikeassa alareunassa olevaa _More_-valikkoa: näkyviin tulee luettelo vaihtoehdoista, joista voit valita _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Voit myös napsauttaa UTXO:lle varattua kohtaa, jolloin saat näkyviin _kolikon tiedot_ -ikkunan. Täällä komento kyseisen UTXO:n lukitsemista/avoimistamista varten näkyy oikeassa yläkulmassa.



![img](assets/en/41.webp)



### Blockstream-sovellus



Blockstream App -työpöydän, joka tunnettiin aiemmin nimellä Green, avulla voit tehdä Coin-valinnan, kun olet jo aloittanut transaktion rakentamisen. Avaa siis Wallet ja napsauta _Send_.



![img](assets/en/16.webp)



Liitä kohde-Address asianmukaiseen kenttään ja valitse sitten _Manuaalinen Coin-valinta_.



![img](assets/en/17.webp)



Tämä avaa ikkunan, jossa voit valita yhden tai useamman UTXO-kolikon. Alla olevassa esimerkissä olemme valinneet kaksi kolikkoa. Vahvista valintasi napsauttamalla _Vahvista Coin-valinta_.



![img](assets/en/18.webp)



Määritä summa ja maksut ja jatka sitten normaalisti maksutapahtumaa.



![img](assets/en/19.webp)



⚠️ HUOM. Green:n _Coins_-valikossa on _Lock_/_Unlock_-kohtia, jotka ennakoivat UTXO:n erottelun mahdollisuutta. Tämä ominaisuus aktivoituu vain niin sanotuilla Multisig-tileillä; se aktivoituu myös vain valitsemalla UTXO, jonka määrä on hyvin pieni, lähellä Dust:n kynnysarvoa.



## Wallet mobiili



Lompakot voidaan valita myös mobiililaitteista, joiden avulla UTXO:t voidaan valita manuaalisesti. Katsotaanpa ensimmäisenä esimerkkinä Blue Wallet.



### Sininen Wallet



Jos olet tämän Wallet:n käyttäjä, avaa se ja siirry johonkin lompakkoosi liittyviin ohjausnäyttöihin napsauttamalla sitä. Päästäksesi Coin:n valvontaoppaaseen sinun on mentävä kulutusvaiheeseen ja napsautettava sitten _Send_.



![img](assets/en/21.webp)



Valitse seuraavassa näytössä oikeassa yläkulmassa olevilla kolmella pisteellä merkityt valikot. Avautuu pudotusikkuna, jossa on joukko komentoja. Valitse viimeinen: _Coin Control_.



![img](assets/en/22.webp)



Tässä vaiheessa sininen Wallet näyttää kaikki UTXO:t. Määrien lisäksi ne erotetaan toisistaan graafisesti eri väreillä.



![img](assets/en/27.webp)



Valitse UTXO ja valitse sen jälkeen _Use Coin_.



![img](assets/en/23.webp)



Sininen Wallet vie sinut takaisin _Send_-ikkunaan, jossa voit jatkaa tapahtuman luomista. Säädä summa ja maksut, minkä jälkeen valitset _Next_.



![img](assets/en/24.webp)



Tässä vaiheessa voit lopettaa maksutapahtuman, kuten yleensä teet.



#### UTXO:n erottelu



Blue Wallet:n avulla voit myös erottaa UTXO:t toisistaan, jolloin niitä ei voi käyttää, mikä ei ole huono toiminto Wallet:lle mobiililaitteesta. Pääset Coin-ohjaukseen juuri selitetyllä tavalla ja valitset UTXO:n valinnan jälkeen _Freeze_ (jäädytä) _Use Coin_ (käytä kolikkoa) sijasta.



![img](assets/en/26.webp)



### Nunchuk



Nunchukin mobiiliversio tarjoaa käyttäjälle myös mahdollisuuden Coin-ohjaukseen. Jos käytät tätä sovellusta mobiilissa, avaa se ja siirry _Lompakko_-valikkoon. Valitse sieltä _View coins_.



![img](assets/en/30.webp)



Napsauta ikkunassa, jossa UTXO-luettelo tulee näkyviin, _Select_.



![img](assets/en/38.webp)



Kunkin UTXO:n vieressä näkyy valintatoiminto. Kuten työpöytäversiossa, Nunchuk-mobiilissa manuaalinen valinta tehdään ruksaamalla määrän vieressä oleva pieni neliö. Näytöllä näkyy valittujen UTXO:iden määrä ja käytettävissä oleva kokonaismäärä. Kun olet valmis, napsauta vasemmassa alakulmassa olevaa ₿-symbolia, joka on käsky aloittaa tapahtuman rakentaminen.



![img](assets/en/31.webp)



Nyt voit suorittaa maksutapahtuman valitsemalla summan ja napsauttamalla Jatka_.



![img](assets/en/32.webp)



Jatka kuten aina, liitä määränpää Address, kuvaus ja räätälöi maksuasetukset.



#### UTXO:n erottelu



Voit myös erottaa UTXO:t toisistaan liikkuvalla Nunchukilla. Avaa oma kolikkoluetteloikkuna ja valitse nuoli sen UTXO:n vierestä, jonka haluat erottaa.



![img](assets/en/42.webp)



Näet kohdan _Kolikon tiedot_, jossa voit valita _Lukitse tämä kolikko_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper on viimeinen Wallet, jonka näemme tässä oppaassa. Näemme sen toiminnallisuuden sovellettuna Coin:n valvontaan Wallet:n yhden tunnuksen avulla, vaikka tällainen käyttö ei olekaan tämän sovelluksen tarkoitus. Kun olet asentanut Keeperin puhelimeesi, käynnistä se ja avaa Wallet, joka sisältää varoja. Napsauta päänäytön keskellä _View All Coins_.



![img](assets/en/34.webp)



Keeper näyttää yleiskatsauksen UTXO:ista. Pääset valintanäyttöön valitsemalla _Select To Send_.



![img](assets/en/35.webp)



Voit valita kolikoita rastittamalla ne klikkaamalla asianmukaista komentoa. Kun olet valmis, napsauta _Send_.



![img](assets/en/36.webp)



Bitcoin Keeper vie sinut suoraan _Send_-valikkoon, jossa voit rakentaa tapahtuman valittujen UTXO:iden kanssa.



![img](assets/en/37.webp)



## Hardware Wallet



Kukin tässä oppaassa esitetyistä ohjelmistolompakoista voi olla pelkkä Interface-kello jollekin laitteistolompakolle. Se tarkoittaa, että Coin:n ohjaus offline-allekirjoituslaitteelle suoritetaan tähän mennessä nähtyjen vaiheiden avulla.



### Yleiset suositukset



Coin-ohjaus on erittäin tehokas tapa valita transaktiosyötteet. Manuaalinen valinta on vieläkin tehokkaampaa, jos olet merkinnyt Satoshisi lähteen hyvin, kun ostat/vastaanotat varoja. Jos haluat oppia tämän tekniikan hyvin, suosittelen seuraavaa opetusohjelmaa:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Olemme aiemmin puhuneet "jäännösten erottelusta". Jos haluat lukita jäännökset myöhempää käsittelyä varten ja saada takaisin yksityisyyden (swap Layer 2), sinun on huolehdittava siitä, että ne "merkitään" aina, kun saat yhden jäännöksen. Tähän mennessä nähdyistä ohjelmistolompakoista vain Electrum värittää UTXO-jäämät graafisesti, jotta ne näkyisivät yhdellä silmäyksellä. Muut, kuten Sparrow, näyttävät yksittäisen UTXO:n johdannaispolun ketjun (`m/84'/0'/0'/0'/1/11`).



Jotta voit soveltaa tätä tekniikkaa tehokkaasti, muista aina lisätä kuvaus saamastasi muutoksesta: henkilö, jolle lähetit varoja (maksu, opetusohjelma tai muu), tietää muutokseen liittyvän Address:n ja tietää, että se kuuluu sinulle, koska se on peräisin yhdessä tekemästänne tapahtumasta!