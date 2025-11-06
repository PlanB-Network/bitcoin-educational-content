---
name: Cashu.me
description: Cashu.me opas ecashin käyttöön
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Tässä on BTC Sessionsin video-opas, joka opastaa sinua Cashu.me Bitcoin Wallet:n käyttöönotossa ja käytössä, sillä sen avulla pääset käsiksi yksinkertaisiin, halpoihin ja yksityisiin Bitcoin-tapahtumiin - ilman sovelluskauppaa!*


Tässä opetusohjelmassa tutustumme Cashu.me:hen, selainpohjaiseen Wallet:een, joka mahdollistaa yksityiset Bitcoin-maksut Chaumian ecashia käyttäen. Ennen kuin sukellamme sisään, tutustutaan lyhyesti ecashiin ja sen toimintaan.


## Johdanto ecashiin


Kuvittele, että digitaalinen käteinen toimii aivan kuten fyysiset setelit taskussasi - se on yksityistä, välitöntä ja käyttökelpoista ilman välikäsiä. Juuri tämän ecash mahdollistaa: digitaalinen maksutapa, joka tuo fyysisen käteisen yksityisyyden takaisin digitaaliseen maailmaan. Toisin kuin onchain-Bitcoin, joka tallentaa jokaisen maksutapahtuman julkiselle Ledger:lle, joka on kaikkien nähtävissä, ecash luo yksityisiä rahakkeita, jotka edustavat todellista Bitcoin-arvoa ja pitävät kulutustottumuksesi luottamuksellisina.


Ajattele, että ecash on digitaalinen haltijaväline, joka on tallennettu laitteeseesi - jos pidät sitä hallussasi, omistat sen, aivan kuten fyysisen käteisenkin. Näitä rahakkeita laskevat liikkeelle luotettavat palvelut, joita kutsutaan nimellä `Mints` ja jotka pitävät hallussaan taustalla olevia Bitcoin-varantoja. Kun käytät ecashia, et lähetä transaktioitasi koko verkkoon. Sen sijaan vaihdat yksityisiä tokeneita suoraan muiden kanssa, mikä luo maksukokemuksen, joka tuntuu enemmän käteisen antamiselta kuin perinteiseltä digitaaliselta maksulta.


Cashu on ilmainen ja avoimen lähdekoodin Chaumian ecash-protokolla, joka on rakennettu Bitcoin:lle. Teknologia perustuu David Chaumin uraauurtavaan 1980-luvun kryptografiatutkimukseen, jossa käytetään "sokeita allekirjoituksia" yksityisyyden varmistamiseksi. Kun vastaanotat ecash-tunnuksia, rahapaja allekirjoittaa ne tietämättä, mihin ne seuraavaksi käytetään - tämä on ratkaiseva ominaisuus, joka estää transaktioiden jäljittämisen. Tärkeää on, että ecash ei korvaa Bitcoin:aa, vaan täydentää sitä ratkaisemalla joitakin Bitcoin-arkkitehtuurin vaatimuksiin liittyviä kriittisiä kysymyksiä. Se tarjoaa fyysisen käteisen tarjoaman yksityisyyden (joka puuttuu Bitcoin:n läpinäkyvästä Ledger:stä) ja mahdollistaa välittömät mikrotransaktiot ilman Blockchain-maksuja tai vahvistusviiveitä.


Ecash integroituu saumattomasti Lightning Network:een. Lightningin avulla voit tallettaa Bitcoin:n rahapajalle (muuntamalla Bitcoin:n arvon ecash-tunnuksiksi) ja nostaa sen myöhemmin (muuntamalla tunnukset takaisin Lightning-saldoksi). Yhdessä ne muodostavat tehokkaan yhdistelmän: Bitcoin tarjoaa turvallisen selvityksen Layer, Lightning mahdollistaa nopeat maksutapahtumat ja verkon yhteentoimivuuden, ja ecash lisää yksityisyyden Layer, joka saa digitaaliset maksut tuntumaan jälleen todella yksityisiltä.


## Cashu.me


Cashu.me on "progressiivinen verkkosovellus (PWA)", joka toteuttaa Cashu-protokollan - Bitcoin:lle suunnitellun Chaumian ecashin erityisen toteutuksen. PWA:na se toimii suoraan selaimessasi ilman asennusta sovelluskaupoista, vaikka voitkin `asentaa` sen laitteeseesi helpommin käytettäväksi. Tämä verkkopohjainen lähestymistapa takaa laajan yhteensopivuuden eri käyttöjärjestelmien välillä ja ylläpitää turvallisuutta kryptografisten protokollien avulla eikä alustarajoitusten avulla.


## 🎉 Tärkeimmät ominaisuudet


Tutustutaan ominaisuuksiin ja tutkitaan, mitä Cashu.me tarjoaa:



- Chaumian ecash on Lightning**: Käyttää sokeaa allekirjoitusta, joten rahapajat eivät voi jäljittää käyttäjien saldoja tai tapahtumahistoriaa
- Polettien oma säilytys**: Hallitset ecash-merkkivaluuttoja paikallisesti seed-lauseellasi
- seed-lauseen varmuuskopiot**: 12-sanainen palautuslause Wallet:n palauttamista varten
- Mintun itsenäisyys**: Toimii useiden itsenäisten rahapajojen kanssa - et ole sidottu yhteen palveluntarjoajaan
- Välittömät, ilmaiset maksutapahtumat**: Samassa rahapajassa maksut hoituvat sekunneissa ilman maksuja
- Yksityisyyden suojaava arkkitehtuuri**: Rahapajat eivät näe, kuka tekee liiketoimia kenenkin kanssa
- Offline ecash**: Lähetä/vastaanota poletteja paikallisen siirtoprotokollan, kuten NFC:n, QR-koodin, Bluetoothin jne. kautta ilman Internet-yhteyttä
- Tutustu ecash-minttukortteihin Nostr**:n kautta: Löydä ja tarkista luotettavat rahapajat Nostr-protokollan kautta
- Vaihda ecashia minttujen välillä**: Kaikki rahapajat puhuvat Lightningia, mikä tarkoittaa, että voit siirtää arvoa niiden välillä.
- Kauko-ohjaa Wallet:ää Nostr Wallet Connect (NWC)** -ohjelmalla: Yhdistä muihin sovelluksiin, kuten Nostr Clientiin, ja aloita zappaus NWC:n kautta


Kriittinen kompromissi on "luottamus": vaikka hallitset itse rahakkeita, sinun on luotettava siihen, että rahapajat huolehtivat taustalla olevien Bitcoin -varantojen säilytyksestä. Kuten Cashun dokumentaatiossa todetaan:


> ...rahapaja ylläpitää Lightning-infrastruktuuria ja huolehtii satoshien säilyttämisestä rahapajan ecash-käyttäjien puolesta. Käyttäjien on luotettava siihen, että rahapaja hoitaa Redeem-ekashinsa, kun he haluavat vaihtaa Lightningiin.

- Cashun dokumentaatio, [yleiset turvallisuus- ja tietosuojakysymykset](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Tämä tekee ecashista itse Bitcoin:n säilytysratkaisun, vaikka sinulla säilyy täysi määräysvalta rahakkeisiin.


## 1️⃣ Alkuasetukset


① Aloita vierailemalla [Wallet.cashu.me](https://Wallet.cashu.me) selaimessasi. Koska Cashu.me on `PWA`, sinun ei tarvitse ladata sitä sovelluskaupoista, vaan voit yksinkertaisesti avata sivuston suoraan selaimessasi. Helpompaa käyttöä varten voit asentaa sen valinnaisesti laitteesi aloitusnäyttöön.


② Voit asentaa PWA:n napauttamalla selaimen ⋮-valikkopainiketta ja valitsemalla `Lisää aloitusnäyttöön`. Kun olet asentanut, sulje selaimen välilehti ja käynnistä Cashu.me laitteen aloitusnäytöltä. Jatka tervetulonäytössä napauttamalla `Next`.


③ Turvallisuus on kriittinen asia. Säilytä seed-lauseesi turvallisesti salasanahallintaohjelmassa tai, mikä vielä parempaa, kirjoita se paperille. Tämä 12-sanainen palautuslauseke on ainoa keino saada varat takaisin, jos menetät pääsyn tähän laitteeseen. Paljasta seed-lauseesi napauttamalla 👁️ -kuvaketta, kirjoita kaikki 12 sanaa huolellisesti ylös järjestyksessä ja merkitse sitten ruutu, jossa lukee "Olen kirjoittanut sen ylös". Jatka napauttamalla `Seuraava` ja vahvista seuraavassa näytössä olevasta ruudusta, että hyväksyt `ehdot`.


![image](assets/en/01.webp)


Kun olet saanut asennuksen valmiiksi, sinun on muodostettava yhteys `Mint`-järjestelmään. Napauta `ADD MINT` ja sen jälkeen `DISCOVER MINTS` nähdäksesi Nostr-yhteisön suosittelemia minttuja. Lisävarmennusta varten voit tarkastella minttujen luokituksia osoitteessa [bitcoinmints.com](bitcoinmints.com).


Napauta seuraavaksi `Click to browse mints` nähdäksesi koko luettelon. Valitse minttu kopioimalla sen URL-osoite, liittämällä se URL-kenttään ja antamalla sille tunnistettava nimi. Tässä esimerkissä käytämme:


URL: `https://mint.minibits.cash/Bitcoin`

Nimi: `Minibits`


![image](assets/en/02.webp)


Viimeistele prosessi napauttamalla `ADD MINT`. Varmista vahvistusnäytössä, että luotat tämän rahapajan käyttäjään, ja napauta sitten uudelleen `ADD MINT`. Minibits-minttupiste näkyy nyt aloitusnäytössäsi. Kun Wallet on perustettu, sinun on rahoitettava se ennen tapahtumien tekemistä.


![image](assets/en/03.webp)


## 2️⃣ Wallet:n rahoitus


Cashu.me tarjoaa kaksi erillistä tapaa rahoittaa Wallet. Kun napautat aloitusnäytössä kohtaa `Vastaanottaa`, näet vaihtoehdot saada varoja `RAAHA` tai `LIGHTNING` kautta.` Tutustutaanpa molempiin vaihtoehtoihin.


![image](assets/en/04.webp)


### Rahoitus LIGHTNINGin kautta


Ensimmäinen vaihtoehto on rahoittaa Wallet Lightning Invoice:n kautta. "Valitse rahapaja", jos olet lisännyt eri rahapajoja, ja määritä haluamasi summa (Sats). Napauta sitten `LUOTA Invoice.` Nyt saat näkyviin QR-koodin, jonka voit skannata toisella Lightning Wallet:lla tai voit yksinkertaisesti `Kopioida` Invoice:n ja liittää sen toiseen Wallet:aan maksaaksesi ja rahoittaaksesi cashu.me Wallet:n.


![image](assets/en/05.webp)


### Sähköisen rahan vastaanottaminen


Ecash-menetelmän avulla voit vastaanottaa poletteja suoraan toiselta ecash Wallet:ltä. Aloita napauttamalla `Vastaanottaa`-painiketta ja valitsemalla `ECASH`-vaihtoehto. Voit `Paste` tai `Scan` tai käyttää `NFC`:tä lähettääksesi Cashu token:n toisesta Wallet:stä. Jos valitset liittämisen, syötä toisesta Wallet:stä kopioimasi token-merkkijono, `Määrä` ja `Mint` tulevat automaattisesti näkyviin. Suorita tapahtuma loppuun napauttamalla `RECEIVE`, ja Sats ilmestyy Wallet:een. Huomaa, että saldosi on nyt jaettu useammalle kolikolle. Sinulla voi esimerkiksi olla 1 000 Sats Minibits-mintissäsi ja toiset 1 000 Sats Coinos-mintissäsi. Tämä jako eri rahapajojen välillä on tärkeä osa Cashun arkkitehtuuria.


![image](assets/en/06.webp)


### Vaihtaminen minttujen välillä


Jos et enää luota tiettyyn rahapajaan, jonka olet lisännyt, cashu.me tarjoaa mahdollisuuden "vaihtaa" varoja rahapajaan. Siirry mints-välilehdelle ja selaa alaspäin, kunnes näet `Multimint Swaps`. Valitse pudotusvalikosta rahapaikat `FROM` ja `TO` ja anna summa, jonka haluat siirtää. Napauta `SWAP` siirtääksesi rahakkeita minttujen välillä. Tämä toteutetaan Lightning-tapahtuman kautta, joten sinun on jätettävä tilaa mahdollisille Lightning-maksuille. Esimerkissäni 1 sat riitti.


![image](assets/en/07.webp)


## 3️⃣ Varojen lähettäminen


Sats:n lähettämiseen Cashu.me tarjoaa kaksi vaihtoehtoa. Lähettää `ecash` tai `lightning` kautta. Katsotaanpa molempia vaihtoehtoja.


### Lähettäminen Lightningin kautta


Voit lähettää Lightningin kautta seuraavasti:


1. Napauta aloitusnäytössä `SEND` ja valitse `Salama`

2. Sovellus pyytää sinua syöttämään `Lightning Invoice` tai `-Address`. Voit liittää Invoice/Address-koodin suoraan tai käyttää skannauksen QR-koodi-vaihtoehtoa kaapataksesi sen visuaalisesti ja vahvistaa sen sitten "ENTER"-näppäimellä

3. Valitse pudotusvalikosta rahapaja, josta haluat maksaa, ja vahvista napauttamalla "MAKSA". **Huomautus**: kohdassa `Asetukset` -> `Kokeilu` on myös mahdollisuus käyttää `Multinut`, jonka avulla voit maksaa laskuja useista minteistä kerralla.

4. Kun maksu on suoritettu onnistuneesti, näet maksuvahvistuksen ja saldostasi vähennetyn summan.


![image](assets/en/08.webp)


### Lähettäminen ecashin kautta


E-kassan lähettäminen on yhtä yksinkertaista.


1. Napauta `SEND` ja valitse tällä kertaa `ECASH`-vaihtoehto.

2. "Valitse rahapaja" ja syötä "summa", jonka haluat lähettää Sats:na ja vahvista napauttamalla "SEND"

3. Tämä luo "animoidun QR-koodin", jota voit muokata säätämällä nopeus- ja kokoparametreja. Kuka tahansa voi skannata tämän QR-koodin Redeem:ään Sats:ään välittömästi, tai voit napauttaa KOPIOI lähettääksesi token-merkkijonon jollekin toiselle vaihtoehtoisilla kanavilla, kuten Bluetoothilla, NFC:llä tai tavallisella viestillä.

4. Avaan toisen Wallet:n. Liitä leikepöydältä ja valitse `Vastaanota ecash` toisessa Wallet:ssä.


![image](assets/en/09.webp)


## 4️⃣ Lisäominaisuudet


Lähetys- ja vastaanottotoimintojen lisäksi Cashu.me tarjoaa tehokkaita lisäominaisuuksia, jotka parantavat Bitcoin-kokemusta Nostr-ekosysteemissä.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) muuttaa vuorovaikutustapasi Nostr-sovellusten kanssa luomalla saumattoman yhteyden Wallet:n ja sosiaalisten sovellusten välille. Tämän protokollan avulla sovellukset, kuten [Damus](https://damus.io/) tai [Primal](https://primal.net/home), voivat pyytää maksuja suoraan Nostrin releiden kautta ilman, että sinun tarvitsee poistua sovelluksesta.


NWC:n perustaminen Cashu.me:ssä:


1. Mene vasemman yläreunan Hampurilaisvalikosta kohtaan `Asetukset`

2. Siirry kohtaan "NOSTR Wallet CONNECT" ja napauta "Enable" -painiketta

3. Asetat sitten avustuksen, jonka avulla voit määrittää, kuinka paljon sovellukset voivat käyttää Wallet:stä.

4. Kun yhteys on määritetty, voit kopioida yhteysmerkkijonon ja liittää sen mihin tahansa Nostr-asiakasohjelmaan, joka tukee `NWC`:tä, mikä mahdollistaa välittömän zappaus- ja tippitoiminnon.


![image](assets/en/10.webp)


### Lightning Address kautta npub.cash


Cashu.me integroituu [npub.cash]-palveluun (https://npub.cash/) ja tarjoaa sinulle Lightning Address:n, joka toimii saumattomasti Nostr-protokollan kanssa. Täällä voit rekisteröityä ja lunastaa käyttäjätunnuksesi antamalla Nostr `nsec`, joka maksaa 5 000 Sats ja tukee npub.cash-projektia, tai voit käyttää mitä tahansa Nostrin julkista avainta (`npub`) ilman rekisteröitymistä.


Mene ensin kohtaan "Asetukset" ja napauta "Ota käyttöön" Lightning Address npub.cashin kanssa. Tämä generate npub.cash Address käyttää oletusarvoisesti Wallet seed-lauseestasi johdettua `npub`-merkkijonoa.


Vaihtoehtoisesti voit käydä [tällä verkkosivulla](https://npub.cash/username) lunastamassa mukautetun käyttäjätunnuksen käyttämällä omaa Nostr `nsec`-nimeäsi, jolloin saat henkilökohtaisen Lightning Address -tyyppisen Lightning Address:n username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Päätelmät


Cashu.me tarjoaa yksityisiä Bitcoin-maksuja, jotka toimivat kuin fyysinen käteinen - välittömästi ja vertaisvertaisverkossa paljastamatta tapahtumahistoriaasi. Arvostan henkilökohtaisesti sen PWA-arkkitehtuuria, koska se toimii ilman sovelluskaupan rajoituksia. Yhdistämällä Bitcoin:n turvallisuuden, Lightningin nopeuden ja ecashin yksityisyyden Wallet tarjoaa käyttötapauksia, jotka voivat lisätä Bitcoin:n jokapäiväistä käyttöä.


Vaikka sinulla on täysi määräysvalta ecash-tokeneihisi omahallinnan kautta, muista, että rahapajat toimivat luotettuina kolmansina osapuolina, jotka pitävät hallussaan taustalla olevia Bitcoin-reservejä. Mahdollisuus käyttää useita rahapajoja ja vaihtaa niiden välillä tarjoaa joustavuutta ja säilyttää samalla yksityisyys.


NWC:n ja npub.cash-osoitteiden kaltaisten ominaisuuksien ansiosta Cashu.me on houkutteleva Wallet-vaihtoehto sosiaalisille asiakkaille, jotka arvostavat yksityisyyttä ja suvereniteettia enemmän kuin suurten teknologiayhtiöiden poliittisia rajoituksia.


## 📚 Resurssit


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)