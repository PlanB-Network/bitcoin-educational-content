---
name: Braiins Mini Miner
description: Tee louhinnasta helppoa kotona.
---
![cover](assets/cover.webp)

## Johdanto

Mini Miner braiins BMM 100 on Braiins-louhintapoolin kehittämä tuote. Tämä laite on tyylikkäästi muotoiltu ja erittäin hiljainen. Se tuottaa 1,1 Th/s laskentatehoa ja kuluttaa noin 40 wattia. Toisin kuin monet muut laitteet, se ei ole avoimen lähdekoodin tuote, mutta sen asentaminen on todella helppoa – se onnistuu vain muutamalla klikkauksella! Mini Miner BMM 100 on ensimmäinen julkaistu versio. Nyt on tuotannossa versio 2, nimeltään BMM 101, joka eroaa ensimmäisestä suuremman näytön ja Wi-Fi-tuen ansiosta, mutta asennusmenettelyt pysyvät samoina.

Lisätietoja löydät täydellisestä oppaasta suoraan [valmistajan sivuilta](https://braiins.com/hardware/mini-Miner-bmm-100).

## Yleiskatsaus BMM 100:aan

Laite näyttää suorakulmaiselta laatikolta, jossa on näyttö etupuolella.

![image](assets/en/01.webp)

Yläosassa on tuuletin.

![image](assets/en/02.webp)

Takapuolella on: virtaliitäntä, paikka SD-kortille (voi olla tarpeen päivityksiä varten), pieni painike `IP REPORT`, jonka avulla saa tietoonsa Mini Minerin IP-osoitteen. Tätä osoitetta tarvitaan laitteen hallintapaneeliin pääsyä varten. Kun painiketta painaa, IP-osoite näkyy näytöllä noin 5 sekunnin ajan, jonka jälkeen se katoaa ja alkuperäinen näyttö palautuu. Jos asetuksia täytyy muuttaa, painiketta voi painaa uudelleen ja IP-osoite ilmestyy takaisin näytölle. Listaa jatkaen löydämme Ethernet-portin sekä laitteen nollauspainikkeen, jota varten tarvitaan nuppi tai neula; painiketta on pidettävä painettuna 10 sekunnin ajan, jotta kaikki Mini Minerin asetukset palautuvat oletuksiin. Lopuksi löytyy kaksi merkkivaloa, vihreä ja punainen, jotka ilmaisevat louhijan tilan.

![image](assets/en/03.webp)

## Mini Minerin yhdistäminen

Laite on liitettävä internetiin Ethernet-kaapelilla; huomaa, että uudessa versiossa (BMM 101) tämä ei enää ole välttämätöntä. Tässä Mini Miner -mallissa on kuitenkin ensin yhdistettävä laite internetlinjaan ja sen jälkeen virtalähteeseen: laite käynnistyy automaattisesti ja näyttää IP-osoitteen näytöllä.

## Konfigurointi

Avaa selain ja kirjoita Mini Minerin näytöllä näkyvä IP-osoite hakupalkkiin. Muistutan, että laitteen löytämiseksi verkosta on oltava paikallisessa verkossa, eli käytössä olevan tietokoneen on oltava yhdistettynä samaan verkkoon kuin Mini Miner. Kun IP-osoite on syötetty ja Enter-painiketta painettu, näytölle ilmestyy Mini Minerin käyttöjärjestelmän (Braiins OS) kirjautumissivu.

![image](assets/en/06.webp)

Kirjautumista varten käyttäjätunnus on `root`, ja salasanan voi jättää tyhjäksi. Klikkaa kirjautumista ja Mini Minerin hallintapaneeli ilmestyy näkyviin.

![image](assets/en/07.webp)

## Yleiset asetukset

Siirry kohtaan System.

![image](assets/en/24.webp)

Asetuksista löytyy yleisiä vaihtoehtoja, kuten teema (vaalea tai tumma), kieli, aikavyöhyke ja salasanan vaihto.

![image](assets/en/25.webp)

Jos valitsemme kohdan "Mini Miner Screen", löydämme laitteen näyttöön liittyvät asetukset. Voimme päättää, näytetäänkö kellonaika, Bitcoinin hinta vai laitteen tilatiedot, kuten hashrate, lämpötila, kulutettu teho ja niin edelleen. Tässä voit itse valita, mitä haluat näytöllä näkyvän. Lisäksi voimme muuttaa näytön kirkkautta, ottaa yötilan käyttöön ja valita 12- tai 24-tuntisen aikamuodon.

![image](assets/en/26.webp)

Kun muutokset on tehty, napsauta `Save Changes`, ja näet muutokset laitteen näytöllä.

![image](assets/en/27.webp)

## Yhteys louhintapooliin

Laite ei ole vielä toimintakunnossa, sillä se on liitettävä pooliin louhinnan aloittamiseksi. Siirry kohtaan "Configuration".

![image](assets/en/08.webp)

Ensimmäinen vaihtoehto on `Pools`.

![image](assets/en/09.webp)

Tässä kohdassa meidän on päätettävä, mitä poolia käytetään. Tässä oppaassa esitellään kaksi vaihtoehtoa. Ensimmäinen on yhdistäminen Braiins-louhintapooliin, jota myös ammattimaiset louhijat käyttävät, kuten näet tästä oppaasta:

https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Toinen vaihtoehto on yhdistäminen solo-louhintapooliin, kuten Public Pool. Seuraa tätä ohjetta:

https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins pool

Yhdistääksemme tähän pooliin meidän täytyy luoda tili. Tämä pooli suorittaa myös maksuja Lightning Networkin kautta, joten voimme vastaanottaa muutamia satseja päivässä. Tätä varten on määritettävä Lightning-osoite palkkioiden vastaanottamista varten. Jos et tiedä, kuinka tili luodaan Braiins-poolissa tai kuinka Lightning-osoite määritetään, voit seurata tätä ohjetta:

https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Kun tämä on tehty, olemme Braiins-poolin hallintapaneelissa. Meidän on ilmoitettava poolille, että haluamme yhdistää yhden louhijoistamme. Näytön vasemmasta reunasta löydät useita valintoja. Valitse "workers".

![image](assets/en/04.webp)

Klikkaa sitten oikeassa reunassa olevaa violettia painiketta "Connect workers".

![image](assets/en/05.webp)

Tämän jälkeen avautuu ikkuna, jossa on tarvittavat tiedot Mini Minerin liittämiseksi pooliin. Ainoa muutos, jonka voimme tehdä, on valita Stratum V2. Lisätietoa Stratum v2:sta löydät tästä [sanastosta](https://planb.academy/en/resources/glossary/stratum-v2).

![image](assets/en/10.webp)

Nyt meidän täytyy kopioida tämä merkkijono, joka alkaa stratumv2:lla. Klikkaa pientä "kopioi"-symbolia ja siirry sitten takaisin Mini Minerin hallintapaneeliin kohtaan Configuration → Pools. Klikkaa "add new pool".

![image](assets/en/11.webp)

Liitä kopioitu merkkijono Pool URL -kenttään.

![image](assets/en/12.webp)

Seuraavaksi lisätään käyttäjätunnus ja salasana. Palaa poolin hallintapaneeliin. Siellä näkyvät myös userID ja salasana. UserID on käyttäjätunnuksesi, jonka annoit tiliä luodessasi, sekä louhijan nimi, jonka haluat lisätä. Voit itse päättää, annatko nimen laitteelle, jonka yhdistät pooliin. Tämä on valinnaista, mutta suositeltavaa – jos liität useita laitteita, niiden tunnistaminen helpottuu. Jos et halua antaa mitään nimeä, voit jättää kenttään `workerName`.

![image](assets/en/13.webp)

Seuraavaksi siirrymme Mini Mineriin ja syötämme käyttäjätunnuksen. Tässä tapauksessa syötän "finalstepbitcoin", joka on oma userID:ni, pisteellä erotettuna laitteen nimellä. Tämä on nimi, jonka päätin antaa laitteelle. Jos et halua nimetä sitä, kirjoita vain käyttäjätunnus piste `workername`. Esimerkissäni se olisi finalstepbitcoin.workername. Kun käyttäjätunnus on syötetty, voit valita salasanan ja kirjoittaa sen tyhjään kenttään. Voit käyttää esimerkiksi `anithing123`, kuten myös poolin näytöllä näkyy. Tämä tarkoittaa yksinkertaisesti sitä, että voit valita minkä tahansa salasanan.

Kun kaikki tiedot on syötetty, paina oikealla olevaa tallenna-painiketta (levykkeen muotoinen kuvake). Näin poolin tiedot on konfiguroitu Mini Mineriin.

![image](assets/en/14.webp)

Seuraavaksi palaa poolin hallintapaneeliin ja napsauta "Connected! Go back."

![image](assets/en/15.webp)

Olemme yhdistäneet Mini Minerin Braiins-pooliin! Nyt näet sen työntekijöiden listassa. Jos se ei ilmesty heti, päivitä sivu ja odota hetki. Kun se näkyy listassa, varmista että sen tilana on "OK" ja vihreä valintamerkki.

![image](assets/en/17.webp)

Jos palaat takaisin hallintapaneeliin, sinun pitäisi alkaa nähdä liikettä kaaviossa sekä laitteen hashrate. Tämä tarkoittaa, että pool vastaanottaa työtämme ja louhinta on toiminnassa.

![image](assets/en/16.webp)

### Public Pool

Tämän poolin kautta voi kokeilla onneaan ja louhia solo-tilassa poolin kautta. Tässä tapauksessa emme saa säännöllisiä palkkioita, mutta onnistumisen sattuessa saamme koko lohkopalkkion. Yhdistymme siis Public Pooliin, joka on täysin avoimen lähdekoodin louhintapooli. Avaa uusi selainikkuna ja siirry osoitteeseen [web.public-pool.io](https://web.public-pool.io/#/).

![image](assets/en/18.webp)

Sieltä löytyy sivu, jossa on kaikki tarvittavat tiedot. Kopioimme sieltä stratum-osoitteen.

![image](assets/en/19.webp)

Palaamme Mini Minerin hallintapaneeliin, menemme kohtaan configuration → pools, klikkaamme "add new pool" (sama prosessi kuin aiemmin) ja liitämme stratum-osoitteen Pool URL -kenttään.

![image](assets/en/20.webp)

Seuraavaksi palaamme poolin sivulle ja huomaamme, että käyttäjätunnukseksi on syötettävä Bitcoin-osoite, johon palkkio maksetaan, jos onnistumme louhimaan lohkon. Sen jälkeen piste ja laitteen nimi, kuten aiemmin Braiins Poolin kanssa. Salasanan voimme päättää itse.

![image](assets/en/21.webp)

Palaamme Mini Mineriin ja liitämme käyttäjätunnuskenttään Bitcoin-osoitteen, pisteen ja laitteen nimen. Tässä esimerkissä käytän `miniminer`. Salasanaksi laitan `test`, mutta voit itse syöttää haluamasi.

![image](assets/en/22.webp)

Tallennamme asetukset ja poistamme Braiins-poolin käytöstä.

![image](assets/en/23.webp)

Hyvä! Olemme nyt louhimassa Public Poolissa!

![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)
