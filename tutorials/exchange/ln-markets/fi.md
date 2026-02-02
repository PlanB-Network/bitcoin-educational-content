---
name: LN Markets
description: Bitcoin:n kauppapaikka Lightning Network:ssä
---

![cover](assets/cover.webp)



LN Markets on ensimmäinen aidosti Lightning-natiivinen Bitcoin-kaupankäyntialusta, jonka avulla voit käydä kauppaa vivutetuilla Bitcoin-johdannaisilla suoraan wallet Lightningista ilman KYC:tä, välittömiä selvityksiä ja minimaalista säilytystä. Vuonna 2020 lanseerattu järjestelmä poistaa perinteisten pörssien kitkat: ei henkilöllisyyden todentamista, ei estettyjä talletuksia, ei lohkoketjuvahvistusten odottelua. wallet Lightningista tulee kaupankäyntitilisi.



## Mikä on LN Markets?



LN Markets tarjoaa **Futuurit** (ikuiset sopimukset, joiden vipuvaikutus on jopa 100-kertainen) ja **Optiot** (Call/Put, joiden riski rajoittuu maksettuun palkkioon). Alusta toimii likviditeetin aggregointikerroksena, joka yhdistää useita kauppapaikkoja optimaalista nollaslippage-toteutusta varten. Varasi ovat lukittuna vain aktiivisten positioidesi tarkan keston ajaksi, ei päiviksi tai viikoiksi, kuten perinteisellä säilytystilillä.



### Saatavilla olevat kaupankäyntituotteet



**Futuurit (ikuiset sopimukset)**



Ikuiset sopimukset ovat futuureja, joilla ei ole päättymispäivää, joten voit spekuloida Bitcoin:n hintakehityksellä vipuvaikutuksella. LN Markets tarjoaa kaksi marginaalinhallintamuotoa:



**Eristetty tila**: Jokaisella asennolla on oma marginaali. Ainoastaan kyseiselle positiolle varatut varat ovat vaarassa. Jos positio saavuttaa realisointihinnan, **vain tämä positio realisoidaan**, muut positiosi ja jäljellä oleva saldosi eivät vaikuta. Ihanteellinen tapa rajoittaa tiukasti riskiä kauppaa kohden.



**Cross Mode (Cross Margin)** : Marginaali jaetaan kaikkien avointen positioiden kesken. Tilisi kokonaissaldo toimii kaikkien positioiden vakuutena. Jos jokin positio menee pieleen, järjestelmä käyttää koko käytettävissä olevaa saldoasi välttääkseen realisoinnin. **Riski** : Jos kokonaissaldosi loppuu, kaikki positiosi voidaan likvidoida samanaikaisesti. Suositellaan vain kokeneille kauppiaille, jotka haluavat maksimoida pääoman tehokkuuden.



**Positionhallinta** :





- Pitkä positio**: panostat BTC/USD:n nousuun. Jos hinta nousee, voitat; jos se laskee, häviät. **Esimerkki**: Bitcoin on 100 000 dollaria, avaat pitkän position 10 000 sats:llä ja 10× vipuvaikutuksella. Jos Bitcoin nousee 105 000 dollariin (+5 %), positiosi voittaa 50 % (5 % × 10), eli ~5 000 sats voittoa. Jos Bitcoin laskee 95 000 dollariin (-5 %), häviät 50 % eli ~5 000 sats tappiota.





- Lyhyt positio**: lyöt vetoa BTC/USD:n laskusta. Jos hinta laskee, voitat; jos se nousee, häviät. **Esimerkki**: Bitcoin on 100 000 dollaria, avaat lyhyen position 10 000 sats:lla ja 10-kertaisella vipuvaikutuksella. Jos Bitcoin laskee 95 000 dollariin (-5 %), voitat 50 % eli ~5 000 sats. Jos Bitcoin nousee 105 000 dollariin (+5 %), häviät 50 %.



Vipuvoima (jopa 100-kertainen) vahvistaa voittoja ja tappioita suhteellisesti. **Funding rate** -mekanismi (säännölliset maksut 8 tunnin välein) tasapainottaa pitkät ja lyhyet positiot. Voit hallita jopa 100 futuuripositioasi samanaikaisesti.



**Vaihtoehdot**



Optio on kuin **arpajaislippu, jonka voimassaoloaika päättyy**. Maksat preemion lyödessäsi vetoa Bitcoin:n hinnan suunnasta. **Suurin etu**: et voi koskaan menettää enempää kuin maksamasi preemion, eikä realisointi ole mahdollista.





- Call-optio (nouseva veto)**: Vetoa siitä, että Bitcoin nousee toteutushinnan yläpuolelle ennen eräpäivää. Voitat, jos hinta nousee, ja menetät vain preemion verran, jos hinta laskee.





- Myyntioptio (laskeva veto)**: Lyödään vetoa siitä, että Bitcoin laskee toteutushinnan alapuolelle. Voitat, jos hinta laskee, ja menetät vain preemion verran, jos hinta nousee.





- Straddle (volatiliteettipanos)**: Ostat samanaikaisesti osto- ja myyntipaketin. Voitat, jos Bitcoin tekee suuren liikkeen mihin tahansa suuntaan, ja häviät molemmat preemiot, jos hinta pysyy vakaana.



Rajoitus: 50 samanaikaista paikkaa. Ihanteellinen vivutetun kaupankäynnin aloittamiseen ilman pelkoa likvidoinnista.



**sats ↔ sUSD**: Muunna satoshisi välittömästi synteettisiksi dollareiksi (sUSD) suojautuaksesi volatiliteetilta tai päinvastoin saadaksesi takaisin Bitcoin-altistumisen.



## Alustan käyttöoikeus ja tilin luominen



### Siirry osoitteeseen LN Markets



Siirry osoitteeseen [lnmarkets.com](https://lnmarkets.com) ja napsauta "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Luo tilisi



Tervetulonäytössä on useita yhteydenmuodostustapoja:



![Méthodes de connexion](assets/fr/02.webp)



**Vaihtoehdot saatavilla** :


1. **Rekisteröityä Lightning wallet** (suositellaan) : LNURL-auth Phoenix:n, Breez:n, Zeuksen tai BlueWalletin kanssa


2. **Rekisteröidy sähköpostilla**: klassinen tili (rajoittaa Lightning-kokemusta)


3. **Alby** tai **Ledger**: selainlaajennukset



### Yhteys Lightningin kautta (LNURL-auth)



Klikkaa "Rekisteröidy Lightning wallet:lla". Skannaa QR-koodi wallet Lightningilla :



![QR code LNURL-auth](assets/fr/03.webp)



wallet allekirjoittaa automaattisesti salauspyynnön, ja tilisi luodaan välittömästi ilman sähköpostia tai salasanaa. Vahva turvallisuus ja täydellinen anonymiteetti.



### Alkuperäinen konfigurointi



![Configuration post-connexion](assets/fr/04.webp)



**Valittavat parametrit** :




- Käyttäjätunnus**: muokkaa käyttäjätunnuksesi
- Automaattiset nostot**: aktivoi automaattiset nostot wallet:lle kaupan sulkemisen jälkeen
- Kahden tekijän todennus**: parannettu suojaus 2FA:n avulla
- Dokumentaatio**: pääsy virallisiin resursseihin



## Interface-kiertue



LN Markets:n käyttöliittymä on järjestetty useisiin osioihin, joihin pääsee sivuvalikosta:



### Kojelauta



![Dashboard](assets/fr/06.webp)



Näyttää tuloksesi tuotetyypeittäin (Futures Cross, Futures Isolated, Options) sekä tuloslaskelman, vaihdetut volyymit ja henkilökohtaisen Address Lightningin (esim. `pivi@lnmarkets.com`).



### Profiili



![Profil trader](assets/fr/07.webp)



Yksityiskohtaiset tilastot: kauppojen määrä, kauppiaan tyyppi (SCALPER jne.), positioiden mediaanikesto, Long/Short-erittely, voittoprosentti, keskiarvot (määrä, marginaali, vipuvaikutus) ja progressiivinen maksurakenne volyymin mukaan.



### Kaupat



![Historique des trades](assets/fr/08.webp)



Kaupat-välilehdellä näytetään positioiden täydellinen historia, jossa on kaikki tärkeät mittarit: luontipäivämäärä, suunta (pitkä/lyhyt), position koko (määrä), sitoutunut marginaali, tulo- ja lähtöhinta, realisoitunut voitto/tappio (P&L) ja kaupankäyntipalkkiot. Voit suodattaa tuotetyypeittäin (futuurit/optiot) ja viedä tietosi ulkoista analysointia tai kirjanpitoa varten.



### Asetukset



![Paramètres de la plateforme](assets/fr/05.webp)



Asetukset-välilehdellä on kaksi välilehteä: **Tili** ja **Interface**.



**Tili**-välilehti:



Tilinhallinta muokattavilla kentillä :




- Käyttäjätunnus**: vaihda käyttäjätunnuksesi (esim. "pivi") "Päivitä"-painikkeella
- Sähköposti**: lisää/muuta sähköpostiosoitettasi
- Talletuksen Bitcoin-osoite**: Bitcoin-osoite, jota voit käyttää on-chain-varojen tallettamiseen.



**Kolme konfigurointikytkintä** :




- Näytetäänkö tulostaulukoissa**: valitse, näytetäänkö julkisissa tulostaulukoissa vai ei
- Käytä Taproot-osoitteita**: käytä Bitcoin-osoitteita Taproot on-chain-talletuksiin/nostoihin
- Ota automaattiset nostot käyttöön**: aktivoi automaattiset nostot wallet Lightningiin kaupan sulkemisen jälkeen



**Tilin siirtyminen**: Osio, jonka avulla voit siirtää Lightning-tilisi perinteiseen sähköposti/salasanatodennukseen.



**Session hallinta**: "Tyhjennä istunto ja paikalliset tiedot" -painikkeella voit katkaista yhteyden ja puhdistaa selaimen paikalliset tiedot.



**Interface** välilehti:



Mukauta käyttökokemusta seitsemällä säätimellä:




- Ohita toimeksiannon vahvistus**: poista vahvistusikkuna käytöstä ennen kaupan toteuttamista (nopea kaupankäynti)
- Näytä työkaluvihjeet**: näytä työkaluvihjeet, kun viet hiiren hiiren elementtien päälle
- Yksityinen tila (peittää arkaluonteiset tiedot)**: peittää määrät ja arkaluonteiset tiedot käyttöliittymässä (yksityisyydensuojatila)
- Näytä netto-PL profiilissa**: näytä nettovoitto/tappio julkisessa profiilissasi
- Käytä yksikkökuvakkeita**: näytä valuuttayksiköiden kuvakkeet (sats, $)
- Ota ääni-ilmoitukset käyttöön**: aktivoi ääni-ilmoitukset kaupankäyntitapahtumia varten
- Ota työpöytäilmoitukset käyttöön**: aktivoi käyttöjärjestelmän työpöytäilmoitukset



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin ja synteettiset USD-saldot sekä talletusten, nostojen, ristisiirtojen, swapien, rahoituksen ja on chain-osoitteiden hallinnan historia.



### API



![API V3](assets/fr/10.webp)



LN Markets tarjoaa täydellisen API REST (V2 ja V3) täysin automatisoida kaupankäynnin kautta skriptejä tai botteja. Voit luoda API-avaimia, joilla on muokattavissa olevat oikeudet (vain luku, kaupankäynti, nostot) suoraan käyttöliittymästä. Viralliset TypeScript- ja Python SDK:t ovat saatavilla helppoa integrointia varten. Täydellinen API V3 -dokumentaatio on saatavilla osoitteessa [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Varojen ensimmäinen talletus



Klikkaa "Talletus". Käytettävissä on kolme menetelmää:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: skannaa QR-koodi wallet Lightning -laitteellasi


2. **Invoice**: syötä summa ja skannaa sitten Lightning-lasku


3. **On-Chain**: varikko Bitcoin on chain on chain



## Kaupankäynti käytännössä



### Trade Futures Long: vedonlyönti ylöspäin



Napsauta kojelaudalta "Futures" ja sitten "Isolated". Klikkaa **"Osta "** avataksesi pitkän position.



![Interface Futures Long](assets/fr/12.webp)



Klikkaa "Osta"-painikkeen vieressä olevaa **laskuri**-kuvaketta näyttääksesi positiolaskurin:



![Calculateur de position Long](assets/fr/13.webp)



**Konkreettinen esimerkki** :




- Määrä**: $100 (paikan koko)
- Kaupan marginaali**: 12.336 sats (sitoutunut marginaali)
- Vipuvoima**: 7.73× (jokainen 1% BTC:n vaihtelu = 7,73% pääomastasi)
- Osallistumishinta** : $104,863.5
- Likvidaatio**: $92,852 (kriittinen automaattinen selvityshinta)
- Poistumishinta**: $110,000 (voittolaskentaa varten)
- PL** : 4,492 sats (voitto, jos irtautuminen 110,000 dollarilla)



**Skenaariot** :




- Lisäys +4,9 %** (110 000 dollaria) : +4,492 sats voitto (+36.4%)
- Neutraali** (104 863 dollaria) : -185 sats (vain maksut)
- Alas -11,5 %** (92 852 dollaria): täydellinen realisointi (-100 %)



Vahvista kauppa napsauttamalla "Osta"-painiketta. **Kaksi mahdollista tapausta** :





- Jos tililläsi on riittävästi likviditeettiä**: vahvistusikkuna tulee suoraan näkyviin (kuva alla). Napsauta "Kyllä" toteuttaaksesi kaupan välittömästi.



![Confirmation trade Long](assets/fr/14.webp)





- Jos sinulla ei ole tarpeeksi käteistä**: sen sijaan näytetään Lightning QR-koodi. Skannaa se wallet Lightningilla maksaaksesi vaadittu marginaali. Kauppa avautuu automaattisesti maksun saatuasi



### Trade Futures Short: vedonlyönti alaspäin



Napsauta **"Myy "** avataksesi Short-position (voitat, jos hinta laskee). Avaa laskin laskimen kuvakkeella asettaaksesi position:



![Calculateur de position Short](assets/fr/15.webp)



Vahvista napsauttamalla "Myy". Longin osalta **kaksi mahdollista tapausta**:





- Jos sinulla on tarpeeksi käteistä**: suora vahvistustila, klikkaa "Kyllä"
- Jos sinulla ei ole tarpeeksi käteistä**: näyttöön tulee Lightning QR-koodi (kuva alla). Skannaa se wallet Lightningilla maksaaksesi vaadittu marginaali:



![Paiement Lightning pour Short](assets/fr/16.webp)



Kun Lightning-maksu on vastaanotettu, Short-positiosi avautuu automaattisesti. Sen jälkeen voit hallita sitä kaupankäyntiliittymästä.



#### Aseman sulkeminen



Jos haluat sulkea position (pitkän tai lyhyen), napsauta **pientä ristiä hallintaliittymän oikeassa alakulmassa**:



![Interface de clôture](assets/fr/17.webp)



Vahvistusvälilehti tulee näkyviin kaupan sulkemisen vahvistamiseksi:



![Confirmation clôture](assets/fr/18.webp)



Modaalissa näkyy nykyinen tuloslaskelmasi (voitto tai tappio). Sulje se napsauttamalla "Kyllä". Saldo lisätään (voitto) tai vähennetään (tappio) Wallet:sta välittömästi Lightningin kautta.



### Kauppaoptiot Call: ehdollinen osto-oikeus



Optiot tarjoavat **riskin**, joka on rajoitettu maksettuun preemioon, eikä niitä voida realisoida. Call-optio antaa sinulle oikeuden (ei velvollisuutta) ostaa Bitcoin:n toteutushintaan ennen eräpäivää. Toisin kuin futuurit, et voi koskaan menettää sijoitettua preemiota enempää.



Napsauta kojelaudalta "Asetukset" ja valitse sitten "Soitot"-välilehti.



![Interface Options Call](assets/fr/19.webp)



Määritä kauppa seuraavien parametrien avulla:




- Määrä**: $100 (sopimuksen koko)
- Viimeinen voimassaoloaika** : 2025-11-15 (päättymispäivä)
- Lakko**: $96,000 (tavoitehinta)



Muut kentät lasketaan automaattisesti:




- Marginaali**: 1.045 sats (maksettava palkkio, sinun sijoituksesi)
- Kannattavuusraja**: $96,923 (hinta, jolla saat panoksesi takaisin)
- Delta**: 40 (Bitcoin hintaherkkyys)



**Miten lasketaan voittosi?**



Voittosi riippuu Bitcoin:n hinnasta eräpäivänä. Kaava: **(BTC-hinta - Strike) × Contract koko - Maksettu palkkio**.



**Konkreettisia esimerkkejä** :





- Bitcoin hintaan 96 000 dollaria** (nykyhinta) : Sisäinen arvo = 0 dollaria. **Tappio: -1,045 sats** (menetät preemion)





- Bitcoin hintaan 97 000 dollaria**: (97 000 - 96 000) × 0,00105 BTC = 1,05 dollaria. Muunnettuna sats:ksi ≈ 2,175 sats. **Hyöty: 2,175 - 1,045 = +1,130 sats** (+108 % voitto)





- Bitcoin hintaan 98 000 dollaria**: sisäinen arvo = 2 000 dollaria ≈ 3 224 sats. **Voitto: +2 179 sats** (+208 % voitto)





- Bitcoin 100 000 dollarilla**: sisäinen arvo = 4 000 dollaria ≈ 5 263 sats. **Voitto: +4 218 sats** (+403 % voitto)





- Bitcoin alle 96 000 dollaria**: Optio raukeaa arvottomana. ** Rajoitettu tappio: -1,045 sats**, ei mahdollista realisointia



Napsauta "Buy Call". Näyttöön tulee vahvistusvalintaikkuna:



![Confirmation Call option](assets/fr/20.webp)



Vahvista valinta napsauttamalla uudelleen "Buy Call". Vaihtoehto näkyy "Running Options" -valikossa. Erääntyessäsi LN Markets laskee automaattisesti sisäisen arvon ja mukauttaa voittosi/tappioosi.



**Merkintä myyntioptioista** : Toiminta on samanlainen kuin osto-optioissa, mutta päinvastoin. Myyntioptiolla lyöt vetoa siitä, että Bitcoin:n hinta laskee **alas**. Jos Bitcoin laskee alle toteutushinnan, voitat; jos se pysyy sen yläpuolella, menetät vain maksamasi palkkion. Voittojen laskeminen noudattaa samaa logiikkaa: **(Strike - BTC-hinta) × Contract:n koko - maksettu palkkio**.



### Salama-rahaston nosto



Klikkaa "Peruuta":



![Modal de retrait](assets/fr/21.webp)



**Menetelmät** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice-menettely** :


1. Luo Lightning-lasku wallet:stä


2. Kopioi lasku (alkaa kirjaimella `lnbc...`)


3. Liitä se LN Markets-kenttään


4. Vahvista peruuttaminen


5. wallet hyvitetään 1-3 sekunnissa



Ei Lightning-nostopalkkioita, vain minimaaliset reitityskulut (käytännössä <0,1 %).



## Riskit ja parhaat käytännöt



**Pääriskit** :




- Täydellinen likvidointi**: suuri vipuvaikutus voi tuhota 100 % marginaalista muutamassa minuutissa
- Kokeellinen palvelu**: alfa-vaihe, teknologiset epävarmuustekijät
- Vastapuoliriski**: foorumi pysyy yhtenä vastapuolena



**Parhaat käytännöt** :



1. **Pääomanhallinta**: ota käyttöön profiiliisi räätälöity riskienhallintastrategia. Esimerkiksi: kohdista 5 % kokonaisvaroistasi vivutettuun kaupankäyntiin ja riskeeraa enintään 1 % tästä pääomasta per kauppa (esim.: 1 BTC-varat → 5M sats kauppaa varten → 50k sats maksimiriski per positio)



2. **Systemaattinen stop-loss**: määritä stop-lossit tappioiden rajoittamiseksi kauppaa kohden. Esimerkiksi 1 %:n riskisäännöllä jopa 10 peräkkäistä tappiollista kauppaa edustaa vain 10 % kaupankäyntipääomastasi



3. **Aloita pienestä**: testaa ensin muutamalla tuhannella satssilla mekanismien ymmärtämiseksi ennen pääomanhallintastrategian soveltamista



4. **Nosta voittosi säännöllisesti**: turvaa voittosi tärkeimmällä wallet:lläsi, jolloin vain aktiivinen kaupankäyntipääoma jää alustalle



5. **Varo vipuvaikutusta**: vältä vipuvaikutusta >20×, ellet ole täysin tietoinen likvidointiriskeistä



**Kustannukset**: ei Lightning-talletus-/nostopalkkioita, spread ~0,1 % per kauppa (laskee 0,06 %:iin volyymin mukaan).



## Edut ja rajoitukset



**Hyötyjä** :




- Muu kuin valvottava (kokonaisvalvonta ilman kaupankäyntiaikoja)
- KYC-vapaa (anonymiteetti Lightning/Nostr:n kautta)
- Välittömät maksut (talletukset/nostot sekunneissa)
- Nollaslippage-toteutus likviditeetin yhdistämisen avulla
- API julkinen ja Nostr tuki



**Rajoitukset** :




- Palvelu alfa (mahdollinen kehitys)
- Pienempi likviditeetti kuin Binance/Deribit
- Kielletty Yhdysvaltain asukkailta



## Päätelmä



LN Markets on merkittävä kehitysaskel Bitcoin-kaupankäynnissä, sillä se integroi Lightning Network:n natiivisti ja antaa hallinnan takaisin käyttäjille. Se on ainutlaatuinen vaihtoehto perinteisille keskitetyille pörsseille, kun kokeneet bitcoin-asiakkaat haluavat spekuloida vaarantamatta itsemääräämisoikeuttaan.



Alusta kehittyy edelleen, ja kehitteillä on USDT lineaarisia futuureja ja huoltajuuteen perustumatonta kaupankäyntiä Discreet Log Contracts (DLC) -palvelun kautta. Soveltamalla hyviä riskinhallintakäytäntöjä (pienet summat, stop-loss, säännölliset nostot), LN Markets:sta tulee tehokas työkalu Bitcoin:n vipuvaikutuksen tutkimiseen vastuullisesti.



Aloita pienestä, testaa muutamalla tuhannella satssilla ja tutki vähitellen tätä uutta Lightning Network-aluetta. Hyvää suvereenia kaupankäyntiä ⚡️!



## Resurssit





- [LN Markets:n virallinen verkkosivusto](https://lnmarkets.com)
- [Dokumentaatio](https://docs.lnmarkets.com)