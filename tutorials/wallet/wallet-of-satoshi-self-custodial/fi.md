---
name: Wallet of Satoshi - Omahuoltajuus
description: Selvitä, miten Wallet of Satoshi-portfolion itsesäilytystila määritetään
---

![cover](assets/cover.webp)



***Ei avaimiasi, ei kolikkojasi* on enemmän kuin sanonta, se on Bitcoin:n perusperiaate, mikä tarkoittaa, että jos et hallitse **yksityisavaimia**, joilla bitcoinisi avataan, et oikeastaan omista niitä.



Monet käyttäjät aloittavat yleensä **custodial wallet:lla** ja siirtyvät sitten **self-custodial wallet:een**, jossa he hallitsevat yksityisiä avaimiaan itse.


Tässä oppaassa emme esittelekään sinulle uutta wallet:n itsehuoltajuusjärjestelmää. Sen sijaan esittelemme sinulle ***Wallet of Satoshi*** wallet:n uuden ominaisuuden: **itseohjautuva tila**.



Tämän uuden integraation tavoitteena on antaa käyttäjille mahdollisuus säilyttää yksityisten avaintensa hallinta ja hyötyä samalla yksinkertaisuudesta ja sujuvasta käyttökokemuksesta.



Ennen kuin menemme asian ytimeen, tarkastellaan hetki Wallet of Satoshi:n (WoS) tarjoamaa erityistä itsehallintatilaa.



## Omahuoltajuuden erityispiirre



WoS:n itsesäilytystilan yksinkertaisuus ja sujuvuus poistaa Lightning-kanavien avaamisen, solmujen hallinnoinnin... Mutta miten tämä on mahdollista?



Wallet of Satoshi:n itsesäilytystila saa virtansa **Sparkista**. Tämä on Layer 2 -ratkaisu Bitcoin:lle, jonka on luonut Lightspark ja jossa käytetään **statechains**-teknologiaa.



Tämän vuoksi et suorita tapahtumia suoraan Lightning Network:llä. LN-verkon ja **Sparkin** välinen vuorovaikutus tapahtuu **atomisten vaihtojen** kautta.



Esimerkiksi Bob haluaa maksaa Lightning-laskun WoSin avulla. Hän siirtää satoshi:nsa, mutta taustalla ne ohjataan Sparkissa toimivalle **Spark-palveluntarjoajalle (SSP)**, joka puolestaan suorittaa maksun Lightning-verkossa.



Alice puolestaan haluaa saada varoja suoraan WoS-salkustaan. Tässä tapauksessa **SSP** vastaanottaa sats:n LN:n kautta ja hyvittää välittömästi Alice:n salkkua.



On siis tärkeää huomata, että WoS:n yksinkertaisuuden ja sujuvuuden hyödyntäminen edellyttää, että olet riippuvainen Sparkin palvelimista. Turvallisuuden kannalta, jos SSP:stä tulee pahantahtoinen tai se ei ole käytettävissä, sinulla on kuitenkin **unilateral exit** -mekanismi, turvatoimenpide, jonka avulla voit saada rahasi takaisin Bitcoin on-chain:llä (vaikka tämä voi olla hidasta ja kallista) , mikä takaa yksityisen Lightning-solmun kokemukseen verrattavissa olevan omatoimisen kokemuksen.



Kun otat kaikki nämä parametrit huomioon, voit päättää, kuinka paljon sats:tä haluat säilyttää WoS-omavarastossasi.



Jos olet uusi Wallet of Satoshi-käyttäjä, sinun on luonnollisesti ladattava wallet-mobiilisovellus. Jos kuitenkin käytät sitä jo ja haluat tietää, miten **itsehallintatilaa** käytetään, siirry suoraan tämän ohjeen kohtaan **itsehallintatilan konfigurointi**.



## Wallet of Satoshi:n käytön aloittaminen



Mene sovelluskauppaan ja lataa WoS.



![screen](assets/fr/03.webp)



Avaa sovellus, kun lataus on valmis, ja paina **Start**.



![screen](assets/fr/04.webp)



Sinut ohjataan sovelluksen pääkäyttöliittymään. Itse asiassa, kun käytät WoSia ensimmäistä kertaa, salkku on jo toiminnassa ja avautuu järjestelmällisesti oletusarvoisesti säilytystilassa.



![screen](assets/fr/05.webp)



Vaikka et haluaisikaan käyttää WoSia huoltajatilassa, suosittelemme, että määrität sen ensin. Katso tätä ohjetta.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Siirrymme seuraavaksi WoS:n konfigurointiin omavalvonnassa.



## Omavalvontatilan konfigurointi



Napsauta pääkäyttöliittymän oikeassa yläkulmassa olevaa hampurilaisvalikkoa (3-palkkinen kuvake).



![screen](assets/fr/06.webp)



Napsauta sitten avautuvassa valikossa **Open Self Custody Wallet** -alavalikkoa.



![screen](assets/fr/07.webp)



WoS kertoo heti, että *itsepelastustilassa on palautuslause. Lisäksi olet yksin vastuussa varojesi turvallisuudesta*.



![screen](assets/fr/08.webp)



Tarkista "**Ymmärrän**"-painike (1) ja paina sitten **Open Self Custody Wallet** -painiketta (2), joka näkyy kirkkaankeltaisena.



![screen](assets/fr/09.webp)



### Omahoitosalkun luominen



Kun olet napsauttanut **Open Self Custody Wallet** -painiketta, napsauta **Create a New Wallet** -painiketta.



![screen](assets/fr/10.webp)



WoS luo sinulle sitten itsesäilytysportfolion, jälleen samassa sovelluksessa. Voit vaihtaa **huoltajuus** -tilan (saatavilla tietyillä alueilla) ja **itsehuoltajuus** -tilan välillä milloin tahansa.



![screen](assets/fr/11.webp)



Kun se on luotu, sinut ohjataan WoS:n omahuolinnan pääkäyttöliittymään. Huomaat, että WoS-custody-salkun ja WoS-omahallussalkun yleiskatsauksen ja käyttöliittymien välillä ei ole eroja.



### Muistilauseen tallentaminen



Napauta **Keychain + Backup Wallet** -kuvaketta, joka sijaitsee näytön yläosassa Wallet of Satoshi:n nimen ja hampurilaisvalikon välissä.



![screen](assets/fr/12.webp)



WoS tarjoaa kaksi erilaista tapaa tallentaa 12 sanaa (muistisanaa): **Varmuuskopiointi Google Driven kautta** ja **manuaalinen varmuuskopiointi**.



Vaikka suosittelemme manuaalista varmuuskopiointia, joka on turvallisin, näytämme myös, miten voit varmuuskopioida Google Driven kautta.



#### Varmuuskopiointi Google Driven kautta



Napsauta **Google Drive Backup** -painiketta.



![screen](assets/fr/13.webp)



Jos valitset varmuuskopioinnin Google Driven avulla, on suuri riski, että Google-tilisi vaarantuu. Pahansuopa henkilö pääsisi käsiksi tiedostoon, joka sisältää 12 sanaa, ja voisi siten päästä käsiksi wallet:aan.



Salasanan lisääminen 12 sanaa sisältävän tiedoston salaamiseksi on varmasti hyvä tapa lisätä ylimääräinen tietoturvataso.



Aktivoi siis **Salaa salasanalla** -painike lisäasetuksissa.



![screen](assets/fr/14.webp)



Aseta uudessa avautuvassa käyttöliittymässä vahva salasana ja vahvista se sitten uudelleen.



![screen](assets/fr/15.webp)



On tärkeää muistaa, että kun olet valinnut salasanan, et saa unohtaa sitä tai hukata tallennusvälinettä, jolle olet kirjoittanut sen. Jos unohdat tai kadotat sen, et pääse enää koskaan käsiksi 12 sanaan ja siten varoihisi.



Kun olet valinnut salasanasi, valitse Google-tili varmuuskopiointia varten ja myönnä sitten WoS:n edellyttämät käyttöoikeudet.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Odota muutama sekunti. Bingo! Varmuuskopiointi on suoritettu onnistuneesti.



![screen](assets/fr/18.webp)



Sinulla on aina mahdollisuus tehdä ylimääräinen varmuuskopio valitsemalla toinen varmuuskopiointimenetelmä: manuaalinen varmuuskopiointi.


#### Manuaalinen varmuuskopiointi



Jos valitset manuaalisen varmuuskopioinnin, suosittelemme lämpimästi tutustumaan tähän ohjeeseen, jossa esitellään parhaat käytännöt muistikirjalauseen varmuuskopioimiseksi turvallisesti, jotta et menetä pääsyä bitcoineihisi.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Paina **Manuaalinen varmuuskopiointi**-painiketta.



![screen](assets/fr/19.webp)



Seuraavassa käyttöliittymässä WoS muistuttaa sinua muutamista turvatoimista, jotka on otettava huomioon ennen manuaalisen varmuuskopioinnin aloittamista.



Aktivoi **Ymmärrän**-painike ja paina **Seuraava**-painiketta.



![screen](assets/fr/20.webp)



Tämän jälkeen sinulle esitetään 12 sanaa. Tallenna ne ja napsauta sitten **Seuraava**-painiketta.



![screen](assets/fr/21.webp)



Paina tässä uudessa käyttöliittymässä sanoja oikeassa järjestyksessä.



![screen](assets/fr/22.webp)



Napsauta lopuksi **Seuraava**-painiketta. Onnittelut! Varmuuskopiointi on nyt valmis.



![screen](assets/fr/23.webp)



## Omaisuudenhoitosalkun palauttaminen



Kun haluat palauttaa tai palauttaa WoS wallet:n omavalvonnan puhelimen vaihdon jälkeen tai mistä tahansa muusta syystä, noudata seuraavia ohjeita.



Voit avata WoS-salkun napsauttamalla pääkäyttöliittymän oikeassa yläkulmassa olevaa hampurilaisvalikkoa.


Napsauta avautuvassa valikossa **Open Self Custody Wallet** -alavalikkoa.


Paina avautuvassa uudessa käyttöliittymässä **Restore Existing Wallet** -painiketta.



![screen](assets/fr/24.webp)



Valitse palautusmenetelmä ja siirry seuraavaan vaiheeseen.



![screen](assets/fr/25.webp)



### Palauta Google Driven kautta



1. Paina **Palauta Google Drivesta** -painiketta.


2. Valitse Google-tili ja anna WoS:n hakea Google Driveen tallennetut palautustiedot.


3. Syötä sitten salaus-salasanasi (jos olit tietysti määritellyt sen aiemmin) tiedostosta, joka sisältää 12 sanaa.


4. Odota hetki, että palautus tulee voimaan, ja pääset jälleen käyttämään salkkuasi.



### Manuaalinen restaurointi



1. Paina **Palauta manuaalisesti**-painiketta.


2. Kirjoita sitten muistisääntölauseesi 12 sanaa kirjoittamalla kukin sana sen alkunumeron eteen.


3. Odota hetki, että palautus tulee voimaan, ja pääset jälleen käyttämään salkkuasi.




### Bitcoinien siirtäminen WoS:n säilytyspaikan ja WoS:n omahoitopaikan välillä



Kun sinulla on bitcoineja (sats) WoS-custody wallet:ssa ja luot WoS self-custody wallet:n, et menetä varojasi. Mikä parasta, voit siirtää ne omaan omaisuudenhoitosalkkuusi ja päinvastoin.



Tätä varten :


Voit kopioida salaman WoS-omahallintaosoitteesi tai luomasi laskun.



![screen](assets/fr/26.webp)



Avaa nyt huoltajasi wallet ja paina **Envoyer**-painiketta.



Liitä sitten osoite tai lasku. Paina **Envoyer** toisen kerran.



Palaa takaisin omaan salkkuusi ja näet, että olit todellakin saanut varat.



![screen](assets/fr/27.webp)



## Bitcoinien lähettäminen ja vastaanottaminen



Bitcoineja lähetetään ja vastaanotetaan itse säilytystilassa, ja kuten yleiskatsauksessa ja käyttöliittymissä, ne eivät eroa bitcoinien lähettämisestä ja vastaanottamisesta WoS custody wallet:n kautta.



Tutustu Wallet of Satoshi:n käyttöä Plan₿-verkossa käsittelevään perusoppaaseen.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Voit nyt konfiguroida ja käyttää Wallet of Satoshi:ää itse omavalvontatilassa.



Jos löysit tämän opetusohjelman hyödylliseksi, jätä minulle vihreä peukalo alla. Kiitos paljon!