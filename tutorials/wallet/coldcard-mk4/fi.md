---
name: COLDCARD Mk4
description: Opas COLDCARD Mk4:n ja Sparrow Wallet:n asettamiseen ja käyttöön
---

![cover-mk4](assets/cover.webp)


**Kiintolaitteet wallet:t** ovat fyysisiä laitteita, jotka on tehty vain Bitcoin:n yksityisen avaimen turvallista säilyttämistä varten. Ne tallentavat yksityiset avaimet offline-tilassa, joten hakkerit eivät pääse niihin käsiksi internetin kautta. Kun taas **ohjelmisto- wallet:tä** käytetään pääasiassa jokapäiväisiin liiketoimiin, **kiinteä wallet:tä** käytetään usein suurempien bitcoin-määrien turvalliseen ja pitkäaikaiseen säilyttämiseen. Kun Bitcoin-tapahtumaa tehdään **hardware wallet:llä**, wallet voi allekirjoittaa tapahtumat laitteen sisällä, joten yksityinen avain ei koskaan altistu internet-yhteydellä varustetuille ympäristöille.


Tässä opetusohjelmassa tutustumme yhteen suosituimmista Coinkiten valmistamista wallet-laitteista, Coldcard Mk4:ään. Katsomme, miten tämä laitteisto-wallet asetetaan ja miten sitä käytetään Bitcoin-tapahtumien suorittamiseen.


## Coldcard Mk4 Yleiskatsaus


Coldcard Mk4 on Coinkiten valmistama Bitcoin-laitteisto wallet. Laite on varustettu näytöllä, numeronäppäimistöllä ja liukukannella. Lisäksi laite tarjoaa useita liitäntä- ja vuorovaikutustapoja, kuten USB-C:n, MicroSD-korttia käyttävän ilmakortin, NFC:n ja virtuaalilevytilan. Mk4 sisältää myös kehittyneitä tietoturvaominaisuuksia, kuten BIP39 passphrase- ja temppu-PIN-tunnukset, jotka antavat käyttäjille paremman hallinnan ja suojan Bitcoin-laitteeseensa.


## Alkuasetukset: PIN-koodi ja kalastelunvastaiset sanat


Coldcard Mk4:n voi ostaa suoraan [Coinkiten verkkosivustolta] (https://store.coinkite.com/store). Ostajat voivat myös valita maksutavaksi fiat-valuutan tai Bitcoin:n. Lisäksi tarvitset MicroSD-kortin (4 Gt riittää) ja virtalähteen, joka voidaan liittää USB-C-kaapelilla (Coldcard Mk4:ssä on vain USB-C-virransyöttöportti). Huomaa, että koska Mk4-kortissa ei ole sisäänrakennettua akkua, se on käytön aikana aina kytkettävä virtalähteeseen.


Saat Mk4-laitteen väärentämisen estävässä pussissa. Varmista, että pussi ei ole vahingoittunut. Jos huomaat pussissa jotakin ongelmallista, kuten vaurioita tai repeämiä, voit ilmoittaa siitä Coinkite:lle lähettämällä sähköpostia osoitteeseen support@coinkite.com. Lisäksi voit löytää väärentämisen estävästä pussista 12-numeroisen numeron, jota kutsumme Mk4:n pussinumeroksi. Tätä pussinumeroa käytetään myöhemmin todentamaan, että laitetta ei ole peukaloitu kuljetuksen aikana ja että se on peräisin suoraan Coinkiteeltä. Pussinumero tallennetaan turvallisesti Cold-kortin secure element:een OTP (One-Time-Programmable) -flash-muistiin, mikä tarkoittaa, että sitä ei voi muuttaa ohjelmoinnin jälkeen. Kun käynnistät laitteen ensimmäisen kerran, näytöllä näkyvän numeron on vastattava pussissa olevaa numeroa. Näin varmistetaan, että saamasi Mk4 on alkuperäinen tehdaslaite, eikä sitä ole vaihdettu tai muutettu. Vaikka tämä todentaminen vahvistaa laitteen eheyden vain ensimmäisen käynnistyksen yhteydessä, secure element suojaa edelleen yksityiset avaimesi, PIN-koodisi ja passphrase:n, joten Bitcoin:n vaarantaminen on erittäin vaikeaa, jos sitä peukaloidaan. Lisäksi hyvät käytännöt, kuten wallet:een liittyvien tietojen asianmukainen suojaaminen, edistävät itse Cold-kortin yleistä turvallisuutta. Lisätietoja saat tästä [artikkelista] (https://blog.coinkite.com/understanding-mk4-security-model/), jossa käsitellään Coldcardin turvamallia.


Näppäimistössä on 10 numeropainiketta, OK-painike (`✓`) ja peruutuspainike (`✕`). Joitakin numeropainikkeita voidaan käyttää myös navigointiin: `5` navigointiin ylöspäin (`^`), `7` navigointiin vasemmalle (`<`), `8` navigointiin alaspäin `˅` ja `9` navigointiin oikealle (`>`).


![01](assets/en/01.webp)


Jos pakkauksessa ei ole ongelmia, voit avata pussin. Mk4:n mukana toimitetaan wallet-varmuuskopiokortti, johon voidaan tallentaa laitteen PIN-koodia, phishinginestosanoja ja seedphrase:ta koskevat tiedot. Noudata seuraavia ohjeita alustusta varten:


1. Valmistele paperi ja kynä.

2. Kytke Mk4 virtalähteeseen (USB-C-kaapeli) ja aseta MicroSD-kortti.

3. Kun laitteeseen kytketään virta ensimmäisen kerran, näytölle tulee viesti Coldcardin myynti- ja käyttöehdoista. Siirry alaspäin ja jatka painamalla `✓`.

4. Seuraavaksi näyttöön ilmestyy 12-numeroinen numero. Tarkista, että tätä numeroa on verrattu väärentämisen estävässä pussissa olevaan numeroon ja pussin numeron lisäkopioon, joka oli väärentämisen estävässä pussissa, varmistaaksesi, että laitetta ei ole peukaloitu. Jos numerot eivät täsmää, ota välittömästi yhteyttä Coinkite-tukeen ennen jatkamista. Muussa tapauksessa jatka painamalla `✓`.


![02](assets/en/02.webp)


5. Valitse `Valitse PIN-koodi`.

6. Siirry alaspäin lukiessasi ohjeita siirtyäksesi seuraavaan vaiheeseen.


![03](assets/en/03.webp)


7. Luo ja syötä Mk4:ssä PIN-etuliite (2-6 merkkiä pitkä) ja kirjoita se ylös ja jatka painamalla `✓`.

8. Kirjoita ylös kaksi näytöllä näkyvää sanaa. Nämä ovat anti-phishing-sanoja. Jatka painamalla `✓`.


![04](assets/en/04.webp)


9. Luo ja syötä PIN-suffiksi (tai PIN-koodin loppuosa, jonka pituus on 2-6 merkkiä) ja kirjoita se ylös. Jatka painamalla `✓`.

10. Syötä PIN-etuliite uudelleen. Jatka painamalla `✓`.


![05](assets/en/05.webp)


11. Tarkista, ovatko phishingin vastaiset sanat samat kuin vaiheessa 8 kirjoittamasi sanat. Jatka painamalla `✓`.

12. Kirjoita PIN-koodin loppuosa (tai PIN-koodin loppuosa) uudelleen. Jatka painamalla `✓`.


![06](assets/en/06.webp)


13. Mk4:n PIN-koodi ja phishing-sanat on nyt luotu ja tallennettu onnistuneesti laitteeseen.


![07](assets/en/07.webp)


Huomaa, että Mk4 pyytää sinua aina syöttämään PIN-koodin, kun kytket laitteen päälle. Ilman tätä PIN-koodia et voi käyttää Coldcard Mk4:ää. Varmista siis, että luot riittävän varmuuskopion PIN-koodista ja phishing-sanoista.


## Wallet:n määrittäminen


Seuraava vaihe on wallet:n määrittäminen. Voit tehdä tämän kolmella tavalla:


- Uuden wallet:n luominen (vakio)
- Uuden wallet:n luominen nopanheitoilla
- wallet:n tuominen


### Uuden wallet:n luominen (vakio)


Voit luoda uuden wallet:n seuraavasti.


1. Valitse `Uusi Wallet` (tai `Uudet siemen-sanat`) > Valitse `12 sanaa` tai `24 sanaa (oletusarvo)` valintasi mukaan.


![08](assets/en/08.webp)


2. Laite luo 12 tai 24 sanaa seedphrase:ksi valintasi mukaan. Navigoi alaspäin, kun kirjoitat huolellisesti jokaisen sanan oikeassa järjestyksessä. Jatka sitten painamalla `✓`.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Laite pyytää sinua tarkistamaan seedphrase:n kysymällä satunnaisessa järjestyksessä (esimerkiksi "Sana 1 on?`, sitten "Sana 5 on?`, sitten "Sana 12 on?`, ja niin edelleen), ja jokaiseen kysymykseen on kolme sanavaihtoehtoa. Tutustu vaiheen 2 huomautukseen ja valitse sanat oikein (painamalla `1`, `2` tai `3`, riippuen siitä, mikä vastaa oikeaa sanaa), jotta wallet-luomus saadaan valmiiksi.


![09](assets/en/09.webp)


4. Mk4 kysyy sitten, haluatko ottaa NFC/Tap käyttöön vai et. Valitse toistaiseksi `✕` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

5. Lopuksi Mk4:ssä on myös mahdollisuus poistaa USB-portti käytöstä (jota voidaan käyttää ilman ilmatilaa tapahtuvaan tiedonsiirtoon). Valitse toistaiseksi `✓` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

6. Näytöllä näkyy nyt päävalikko, jonka yläreunassa lukee "Ready to Sign". Tämä merkitsee wallet:n luomisprosessin päättymistä.


![10](assets/en/10.webp)


### Uuden wallet:n luominen nopanheitolla


Vaihtoehtoisesti voit myös luoda uuden seedphrase:n entropian avulla. Tee niin, jos et luota Mk4:n juuri luotuun seedphrase:ään.


Coldcard Mk4:ssä toimitaan seuraavasti:


1. Valitse `New Wallet` (tai `New Seed Words`) > Valitse `12 sanan nopanheitto` tai `24 sanan nopanheitto` valintasi mukaan.

2. Sinua pyydetään syöttämään nopanheiton tulokset. Jokainen nopanheitto lisää satunnaisuutta wallet:n luomisprosessiin, mikä varmistaa, että seedphrase luodaan täysin turvallisella ja arvaamattomalla tavalla. Heittojen vähimmäismäärä on 50 12-sanaiselle seedphrase:lle ja 99 24-sanaiselle seedphrase:lle. Paina `✓`, kun olet syöttänyt vähintään 99 nopanheiton arvoa.


![11](assets/en/11.webp)


3. Laite luo 12 tai 24 sanaa seedphrase:ksi valintasi mukaan. Navigoi alaspäin, kun kirjoitat huolellisesti jokaisen sanan oikeassa järjestyksessä. Jatka sitten painamalla `✓`.

4. Laite pyytää sinua tarkistamaan seedphrase:n kysymällä satunnaisessa järjestyksessä (esimerkiksi "Sana 1 on?`, sitten "Sana 5 on?`, sitten "Sana 12 on?`, ja niin edelleen), ja jokaiseen kysymykseen on kolme sanavaihtoehtoa. Katso vaiheen 3 huomautusta ja valitse sanat oikein (painamalla `1`, `2` tai `3`, riippuen siitä, mikä vastaa oikeaa sanaa), jotta wallet-luomus valmistuu.


![12](assets/en/12.webp)


5. Mk4 kysyy sitten, haluatko ottaa NFC/Tap käyttöön vai et. Valitse toistaiseksi `✕` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

6. Lopuksi Mk4:ssä on myös mahdollisuus poistaa USB-portti käytöstä (jota voidaan käyttää ilman ilmatilaa tapahtuvaan tiedonsiirtoon). Valitse toistaiseksi `✓` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

7. Näytöllä näkyy nyt päävalikko, jonka yläreunassa lukee "Ready to Sign". Tämä merkitsee wallet:n luomisprosessin päättymistä.


![13](assets/en/13.webp)


### wallet:n tuonti


Viimeinen vaihtoehto on tuoda wallet. Voit tehdä tämän, jos haluat palauttaa wallet:n jo omistamastasi seedphrase:stä. Voit noudattaa seuraavia ohjeita:


1. Valitse `Import Existing`.

2. Valitse "24 sanaa", "18 sanaa" tai "12 sanaa" seedphrase:n sanamäärän mukaan.


![14](assets/en/14.webp)


3. Coldcard Mk4 kysyy sitten, mitä kukin sana on peräkkäisessä järjestyksessä. Siirry kunkin sanan kohdalla alas- tai ylöspäin, kunnes löydät kunkin sanan kirjoitusalkuisen etuliitteen. Laite kaventaa mahdollisuuksia, kunnes löydät oikean sanan. Toimi samoin muiden sanojen kohdalla.

4. Viimeisen sanan osalta Coldcard Mk4 näyttää vain rajoitetun määrän mahdollisia sanoja. Jos sanoja ei löydy, olet ehkä syöttänyt sanat väärin. Muussa tapauksessa valitse sana, joka vastaa seedphrase-kortissasi olevaa sanaa.


![15](assets/en/15.webp)


5. Mk4 kysyy sitten, haluatko ottaa NFC/Tap käyttöön vai et. Valitse toistaiseksi `✕` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

6. Lopuksi Mk4:ssä on myös mahdollisuus poistaa USB-portti käytöstä (jota voidaan käyttää ilman ilmatilaa tapahtuvaan tiedonsiirtoon). Valitse toistaiseksi `✓` tämän vaihtoehdon kohdalla. Tätä voidaan muuttaa asetuksissa tulevaisuudessa.

7. Näytöllä näkyy nyt päävalikko, jonka yläreunassa lukee "Ready to Sign". Tämä merkitsee wallet:n luomisprosessin päättymistä.


![16](assets/en/16.webp)


Huomaa, että seedphrase on ainoa keino palauttaa wallet. Luo varmuuskopio seedphrase:stä ja säilytä se turvallisessa paikassa. **Ei avaimiasi, ei kolikkojasi**, kuka tahansa, jolla on seedphrase:si, pääsee käsiksi bitcoineihisi!


## passphrase:n asentaminen


Yksi parhaista käytännöistä Bitcoin:ssa on passphrase:n käyttö. passphrase toimii 13. tai 25. sanana seedphrase:n lisäksi. Se eroaa muista siinä, että voit valita minkä tahansa lauseen, kun taas seedphrase valitaan ennalta määrätystä 2048 sanan luettelosta. Oletusarvoisesti, kun olet asettanut wallet:n, aloitat wallet:llä ja tyhjällä passphrase:llä. Jos haluat määrittää muun kuin tyhjän passphrase:n, toimi seuraavasti:


1. Siirry kohtaan `Passphrase`.

2. Siirry alaspäin lukemaan kuvaus passphrase:sta ja jatka sitten painamalla `✓`.

3. Valitse "Muokkaa lausetta".


![17](assets/en/17.webp)


4. Syötä passphrase:


   - Valitse merkkityyppi painamalla `1` (kirjaimet), `2` (numerot) tai `3` (symbolit).
   - Paina `4` vaihtaaksesi pienen ja ison kirjaimen välillä (voidaan käyttää vain kirjaimia syötettäessä).
   - Navigoi käyttämällä `^` tai `˅` valitaksesi passphrase:n merkin.
   - Siirry merkkien välillä käyttämällä `<` tai `>`. Voit myös lisätä välilyöntejä käyttämällä `>`.
   - Paina `✕` poistaaksesi merkit.
   - Paina `✓`, kun olet lopettanut passphrase:n muokkaamisen.

5. Lisäksi muilla vaihtoehdoilla on seuraavat toiminnot:


   - `Add Word` (Lisää sana) tai `Add Numbers` (Lisää numerot) -painikkeilla voit liittää kirjaimia/numeroita parhaillaan muokkaamaasi passphrase:een.
   - Paina `Clear ALL` (Tyhjennä kaikki) nollataksesi parhaillaan muokkaamasi passphrase:n.
   - Palaa päävalikkoon painamalla `CANCEL`.

6. Kirjoita muistiin passphrase varmuuskopioksi.

7. Paina `APPLY`, jotta wallet pääsee käyttämään juuri asettamaasi passphrase:tä.

8. Mk4 näyttää tämän jälkeen 8-merkkisen pääavaimen sormenjäljen. Tätä voidaan pitää wallet:n "tunnisteena". Kirjoita tämä sormenjälki muistiin ja jatka painamalla `✓`.


![18](assets/en/18.webp)


9. Nyt wallet näyttää wallet:n päävalikon ja syöttämäsi passphrase:n.

10. On tärkeää huomata, että wallet ei kerro, että olet syöttänyt väärän passphrase:n, koska jokainen passphrase vastaa omaa wallet:tä, jolla on yksilöllinen identiteetti (pääavaimen sormenjälki). Siksi on hyvä käytäntö syöttää sama passphrase uudelleen ja tarkistaa, että se tuottaa saman wallet:n sormenjäljen, ja varmistaa, että olet syöttänyt sen oikein. Tee tämä suorittamalla vaiheet 11-14.

11. Valitse päävalikosta `Restore Master` ja paina sitten `✓`. Olet nyt takaisin wallet:n päävalikossa, jossa on tyhjä passphrase.


![19](assets/en/19.webp)


12. Siirry uudelleen kohtaan `Passphrase` ja jatka sitten painamalla `✓`.

13. Syötä uudelleen vaiheessa 6 kirjoittamasi passphrase ja paina sitten "APPLY".

14. Tarkista 8-merkkinen pitkä pääavaimen sormenjälki sen sormenjäljen kanssa, jonka olet kirjoittanut ylös vaiheessa 8. Jos molemmat sormenjäljet eivät vastaa toisiaan, olet ehkä kirjoittanut väärät merkit. Voit valita uuden passphrase:n ja toistaa prosessin vaiheesta 1 alkaen. Jos molemmat sormenjäljet täsmäävät, se tarkoittaa, että olet syöttänyt passphrase:n oikein.

15. wallet ja valitsemasi passphrase ovat käyttövalmiita.


## Wallet:n vienti Sparrow:aan


Muiden wallet-laitteistojen tavoin Coldcard Mk4:ää ei voi käyttää yksinään. Se on liitettävä ohjelmistoon wallet, joka toimii liitäntänä. wallet-ohjelmiston avulla voit tarkastella saldoa, luoda tapahtumia ja hallita osoitteita, kun taas Coldcard allekirjoittaa nämä tapahtumat turvallisesti paljastamatta yksityisiä avaimiasi.


Tässä opetusohjelmassa käytämme rajapintana Sparrow Wallet. Menettely wallet:n viemiseksi on seuraava:


1. Varmista, että MicroSD-kortti on asetettu Mk4-laitteeseen.

2. Suorita vaiheet "passphrase:n määrittäminen" wallet:ssa sen passphrase:n kanssa, jonka haluat viedä. Jos haluat viedä wallet:n tyhjän passphrase:n kanssa, voit ohittaa tämän vaiheen.

3. Mene kohtaan `Advanced/Tools` > Valitse `Export Wallet` > Valitse `Generic JSON` > Selaa alaspäin, kun luet ohjeet, ja paina `✓`.


![20](assets/en/20.webp)


4. Mk4 on nyt luonut MicroSD-kortille tiedoston, jonka tiedostomuoto on `.json`.


![21](assets/en/21.webp)


5. Poista MicroSD-kortti Cold-kortista ja aseta se laitteeseen, johon Sparrow Wallet on asennettu.

6. Avaa Sparrow Wallet.

7. Napsauta `File`


![22](assets/en/22.webp)


Napsauta seuraavaksi `New Wallet`


![23](assets/en/23.webp)


Syötä sitten wallet:n nimi


![24](assets/en/24.webp)


Napsauta sen jälkeen `Create Wallet`


![25](assets/en/25.webp)


8. Valitse `Script Type`.


![26](assets/en/26.webp)


9. Valitse Avainsäilö-osiosta `Airapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Etsi Coldcard ja valitse `Import File...`.


![28](assets/en/28.webp)


11. Valitse vaiheessa 4 luotu tiedosto (se, jossa on `.json`-muoto).


![29](assets/en/29.webp)


12. Palaa Mk4:ssä päävalikkoon ja siirry kohtaan `Advanced/Tools` > `View Identity`. Varmista, että Mk4:n näytöllä näkyvä sormenjälki vastaa Sparrow Wallet:ssä olevaa sormenjälkeä (Master-sormenjälki Keystore-osassa)

13. Napsauta oikeassa alakulmassa olevaa Sovelletaan-painiketta.


![30](assets/en/30.webp)


14. Vaihtoehtoisesti voit myös lisätä salasanan viedylle wallet:lle. Tätä salasanaa tarvitaan aina, kun avaat Sparrow Wallet-sovelluksen wallet:n käyttämiseksi. Jos unohdat salasanan tulevaisuudessa, voit yksinkertaisesti toistaa vaiheet 1-13 ja valita uuden salasanan.


![31](assets/en/31.webp)


15. wallet on nyt onnistuneesti viety ja valmis käytettäväksi.


![32](assets/en/32.webp)


## Bitcoinin vastaanottaminen


Seuraavaksi opettelemme, miten vastaanotetaan Bitcoin Mk4:llä. Tämä prosessi on melko yksinkertainen, koska sinun ei tarvitse käyttää itse Mk4-laitetta. Kunhan olet jo vienyt wallet:n Sparrow:een, voit vastaanottaa Bitcoin:n suoraan Sparrow Wallet:n kautta. Seuraa näitä ohjeita vastaanottaaksesi bitcoineja Mk4-laitteella:


1. Avaa Sparrow Wallet.

2. Valitse `Open Wallet` > Valitse wallet-tiedosto, johon haluat vastaanottaa bitcoinia > Anna kyseiseen wallet:een liittyvä salasana.


![33](assets/en/33.webp)


3. Napsauta Sparrow:n käyttöliittymässä käyttöliittymän vasemmalla puolella olevaa Vastaanota-välilehteä.


![34](assets/en/34.webp)


4. Osoite ja QR-koodi näkyvät yläreunassa. Voit kopioida ja liittää osoitteen tai skannata QR-koodin wallet:lla, jota käytät bitcoinien lähettämiseen Sparrow Wallet:een. Voit halutessasi kirjoittaa vastaanottamillesi bitcoineille nimilapun.


![35](assets/en/35.webp)


5. Kun olet lähettänyt bitcoinit, napsauta Sparrow:n käyttöliittymässä käyttöliittymän vasemmalla puolella olevaa `Transaktiot`-välilehteä. Näet transaktiohistorian yläreunassa uuden merkinnän, joka vastaa juuri tekemääsi transaktiota.


![36](assets/en/36.webp)


6. Voit myös siirtyä käyttöliittymän vasemmassa reunassa olevaan `UTXOs`-välilehteen nähdäksesi juuri saamasi bitcoinit.


![37](assets/en/37.webp)


## Bitcoinin lähettäminen


Toisin kuin bitcoinien vastaanottaminen, Coldcard-korttiin liittyvien bitcoinien käyttäminen edellyttää, että käytät Coldcardia tapahtumien allekirjoittamiseen. Bitcoinien lähettäminen Mk4:llä tapahtuu seuraavasti:


1. Aseta MicroSD-kortti laitteeseen, johon Sparrow Wallet on asennettu.

2. Avaa Sparrow Wallet.

3. Valitse `Open Wallet` > Valitse wallet-tiedosto, jota haluat käyttää bitcoinien lähettämiseen > Anna kyseiseen wallet:een liittyvä salasana.


![38](assets/en/38.webp)


4. Napsauta Sparrow:n käyttöliittymässä käyttöliittymän vasemmalla puolella olevaa Lähetä-välilehteä.


![39](assets/en/39.webp)


5. Kirjoita "Pay to" -välilehdelle osoite, johon haluat lähettää bitcoinit.

6. Lisää tapahtumalle etiketti.

7. Kirjoita lähetettävien bitcoinien määrä.

8. Syötä maksu vaihtamalla `Väli` tai syöttämällä numero suoraan `Maksu`-kohtaan.


![40](assets/en/40.webp)


9. Napsauta oikeassa alakulmassa "Luo tapahtuma".


![41](assets/en/41.webp)


10. Näet uuden tapahtumavälilehden, jonka nimi on vaiheessa 6 syöttämäsi nimike. Napsauta "Viimeistele tapahtuma allekirjoitusta varten".


![42](assets/en/42.webp)


11. Napsauta `Tallenna tapahtuma` ja tallenna tapahtuma MicroSD-kortille. Nimeä tiedosto tarvittaessa uudelleen. Tämä vaihe tallentaa tapahtuman PSBT-tiedostona.


![43](assets/en/43.webp)


12. Poista MicroSD-kortti ja aseta se Coldcard Mk4 -korttiin.

13. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

14. Syötä PIN-koodi.

15. Siirry kohtaan `Passphrase` ja syötä passphrase sen wallet:n passphrase, jota haluat käyttää bitcoinien lähettämiseen. Jos haluat käyttää wallet:tä tyhjällä passphrase:llä, ohita tämä vaihe.

16. Varmista, että pääavaimen sormenjälki on sama kuin Sparrow Wallet:ssa. Voit tarkistaa tämän Sparrow Wallet:n käyttöliittymän vasemmanpuoleisella `Settings`-välilehdellä. Jatka sitten painamalla `✓` Mk4:ssäsi. Tämä vie sinut päävalikkoon.

17. Valitse Mk4:n päävalikosta "Valmis allekirjoittamaan". Näytölle tulee viesti "OKAY TO SEND?`. Varmista, että lähetettävien bitcoinien määrä ja vastaanottava osoite ovat oikein. Vahvista painamalla `✓` tai peruuta painamalla `✕`.

18. Jos valittavana on useita PSBT-tiedostoja, Mk4 näyttää viestin "Valitse allekirjoitettava PSBT-tiedosto". Jatka painamalla `✓`. Valitse sitten PSBT-tiedosto, jonka haluat allekirjoittaa, navigoimalla alas- tai ylöspäin. Suorita vaihe 17 kyseiselle tapahtumalle.


![44](assets/en/44.webp)


19. Mk4 näyttää nyt viestin "PSBT Signed" sekä allekirjoitetun PSBT-tiedoston nimen. Jatka painamalla `✓`.

20. Poista MicroSD-kortti Cold-kortista ja aseta se laitteeseen, johon Sparrow Wallet on asennettu.

21. Napsauta Sparrow Wallet:ssä kohtaa `Load Transaction`.


![45](assets/en/45.webp)


22. Valitse tiedosto, jonka nimi on sama kuin vaiheessa 19 luodun tiedoston nimi.


![46](assets/en/46.webp)


23. Napsauta `Broadcast Transaction`.


![47](assets/en/47.webp)


24. Tapahtumasi on lähetetty ja sitä käsitellään parhaillaan. Voit siirtyä `Transaktiot`-välilehdelle nähdäksesi transaktiosi vahvistustilanteen.


![48](assets/en/48.webp)


## Firmware päivitys


### Firmware-version tarkistaminen


Coldcard Mk4:n laiteohjelmiston voi aina päivittää uudempaan versioon. Voit tarkistaa, onko Mk4-laitteesi päivitetty uusimpaan versioon vai ei, suorittamalla seuraavat vaiheet:

1. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

2. Syötä PIN-koodi.

3. Mene kohtaan `Advanced/Tools` > Valitse `Upgrade Firmware` > Valitse `Show Version`.


![49](assets/en/49.webp)


Tarkista Mk4:n näytöllä näkyvä versio [Coinkiten verkkosivustolla](https://coldcard.com/downloads) olevasta versiosta. Jos versio on erilainen, voit päivittää laiteohjelmiston uudempaan versioon.


![50](assets/en/50.webp)


### Laiteohjelmiston päivittäminen


Jos haluat päivittää laiteohjelmiston uusimpaan versioon, toimi seuraavasti:


1. Aseta MicroSD-kortti kannettavaan tietokoneeseen.

2. Mene [Coinkite's website](https://coldcard.com/downloads) ja lataa uusin laiteohjelmisto MicroSD-kortille (punainen painike Mk4-kuvan oikealla puolella, jossa on versionumero).


![51](assets/en/51.webp)


Voit ladata myös muita versioita klikkaamalla `All Files on Mk4` ja valitsemalla haluamasi version. Ladattu tiedosto on `.dfu`-muodossa.


![52](assets/en/52.webp)


3. Poista MicroSD-kortti ja aseta se Mk4-laitteeseen.

4. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

5. Syötä PIN-koodi.

6. Mene kohtaan `Advanced/Tools` > Valitse `Upgrade Firmware` > Valitse `From MicroSD` > Selaa alaspäin, kun luet ohjeet ja paina `✓`.


![53](assets/en/53.webp)


7. Valitse vaiheessa 2 lataamasi .dfu-tiedosto.

8. Coldcard Mk4 näyttää viestin "Asenna tämä uusi laiteohjelmisto?". Selaa alaspäin lukiessasi ohjeita ja paina sitten `✓`.


![54](assets/en/54.webp)


9. Odota, että Mk4 asentaa uuden laiteohjelmiston. Älä katkaise virtalähdettä asennuksen aikana.

10. Kun Mk4 on valmis, se käynnistyy uudelleen. Voit syöttää PIN-koodisi ja suorittaa "Tarkista laiteohjelmistoversio" -vaiheet tarkistaaksesi, onko laiteohjelmisto päivitetty vai ei.


## Lisäominaisuudet


### Vaihda PIN-koodi


Jos haluat vaihtaa kirjautumiskoodin, toimi seuraavasti:


1. Valmistele kynä ja paperi.

2. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

3. Syötä PIN-koodi.

4. Siirry kohtaan "Asetukset" > Valitse "Sisäänkirjautumisasetukset" > Valitse "Vaihda pää-PIN"

5. Siirry alaspäin lukiessasi viestiä ja jatka sitten painamalla `✓`.


![55](assets/en/55.webp)


6. Syötä vanha PIN-koodisi.

7. Syötä uusi PIN-etuliite (2-6 merkkiä pitkä) ja kirjoita se ylös.

8. Mk4 näyttää nyt kaksi uutta anti-phishing-sanaa, kirjoita ne ylös ja jatka sitten painamalla `✓`.

9. Syötä uusi PIN-tunnusloppu (tai PIN-koodin loppuosa, jonka pituus on 2-6 merkkiä) ja kirjoita se ylös.


![56](assets/en/56.webp)


10. Syötä uusi PIN-etuliite uudelleen.

11. Tarkista, vastaavatko phishingin vastaiset sanat vaiheessa 8 kirjoittamiasi sanoja.

12. Kirjoita uusi PIN-koodin loppuosa (tai PIN-koodin loppuosa) uudelleen.


![57](assets/en/57.webp)


13. PIN-koodisi on vaihdettu onnistuneesti.


### Temppujen PIN-koodit - Lisää uusi temppu


Temppu-PIN-koodi on vaihtoehtoinen PIN-koodi, joka eroaa siitä, jota käytit Coldcard Mk4:n käyttöönotossa ensimmäistä kertaa. Kun käynnistät Mk4:n, voit syöttää temppu-PIN-koodin tai -Koodit pää-PIN-koodin sijasta tiettyjen toimintojen käynnistämiseksi. Voit määrittää temppu-PIN-koodin Mk4:ssä seuraavasti:


1. Valmistele kynä ja paperi.

2. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

3. Syötä PIN-koodi.

4. Mene kohtaan "Asetukset" > Valitse "Sisäänkirjautumisasetukset" > Valitse "Temppujen PIN-koodit" > Valitse "Lisää uusi temppu".


![58](assets/en/58.webp)


5. Syötä PIN-koodin etuliite (2-6 merkkiä pitkä) ja kirjoita se ylös.

6. Mk4 näyttää nyt kaksi uutta anti-phishing-sanaa, kirjoita ne ylös ja jatka sitten painamalla `✓`.

7. Syötä temppusi PIN-koodin loppuosa (tai PIN-koodin loppuosa, jonka on oltava 2-6 merkkiä pitkä) ja kirjoita se ylös.


![59](assets/en/59.webp)


8. Siirry alas- tai ylöspäin valitaksesi toiminnon, jonka haluat yhdistää juuri luomaasi temppujen PIN-koodiin. Toimintojen luettelo on seuraava:


    - `Brick Self`, kun se valitaan, Mk4:n sirut tuhoutuvat PIN-koodin syöttämisen jälkeen, jolloin Mk4 on pysyvästi käyttökelvoton.
    - `Wipe Seed`, voit valita seuraavien toimintojen välillä:
      - pyyhi ja käynnistä uudelleen: seed pyyhitään ja Cold-kortti käynnistyy uudelleen PIN-koodin syöttämisen jälkeen.
      - `Silent Wipe`: seed pyyhitään äänettömästi, mutta Cold-kortti käyttäytyy kuin PIN-koodi olisi syötetty väärin.
      - "Pyyhi -> Wallet": seed pyyhitään äänettömästi, ja Cold-kortti vie sinut wallet:een.
    - `Duress Wallet`, kun se on valittuna, Mk4:nne johtaa pakkokäyttöön wallet:ään, kun PIN-koodi on syötetty.
    - `Login Countdown`, voit valita seuraavien toimintojen välillä:
      - "Pyyhi ja laske": seed pyyhitään välittömästi, minkä jälkeen Mk4 alkaa näyttää lähtölaskentaa.
      - `Countdown & Brick`: Lähtölaskenta alkaa, ja Mk4 muurautuu itsestään, kun aika on kulunut.
      - `Just Countdown`: Mk4 aloittaa lähtölaskennan ja käynnistyy uudelleen ajan päätyttyä.
    - kun "Look Blank" on valittu, kun temppu-PIN on syötetty, Cold-kortti käyttäytyy kuin seedphrase olisi pyyhitty, mutta se on itse asiassa edelleen muistissa.
    - `Just Reboot`, kun se on valittuna, Coldcard käynnistyy uudelleen sen jälkeen, kun PIN-koodi on syötetty.
    - `Delta Mode`, Tämä kehittynyt ominaisuus on tarkoitettu kokeneille käyttäjille, ja se on suunniteltu suojaamaan vakavilta uhkilta, kuten sisäpiirin tietämyksen omaavan henkilön suorittamalta pakottamiselta. Kun Delta Mode on aktivoitu, COLDCARD näyttää avaavan aidon wallet:n, jolloin hyökkääjä voi selata ja varmistaa, että se näyttää aidolta. Se kuitenkin salaa estää kaiken tapahtuman allekirjoittamisen, joten bitcoinia ei voi lähettää. Se myös estää pääsyn seed-lauseeseen, ja kaikki yritykset tarkastella sitä poistavat sen kokonaan. Jotta väärennetty wallet näyttäisi vakuuttavammalta, Delta Mode -tilassa käytettävän Trick PIN -koodin on alettava samoilla numeroilla kuin oikean PIN-koodin (joten siinä näkyvät samat anti-phishing-sanat), mutta päätyttävä eri tavalla.
    - `Policy Unlock`, kun se on valittuna, Single Signer Spending Policy (SSSP) poistetaan käytöstä sen jälkeen, kun temppu-PIN on syötetty.
    - "Policy Unlock & Wipe", kun se valitaan, se teeskentelee poistavansa SSSP:n käytöstä, mutta se pyyhkii seedphrase:n samalla.

9. Kun olet valinnut toiminnon, jonka haluat yhdistää temppu PIN-koodin kanssa, vahvista valintasi painamalla `✓`. Temppu-PIN on määritetty onnistuneesti.

10. Asetukset > Sisäänkirjautumisasetukset > Temppu-PINit -kohdassa näet luettelon luomistasi temppu-PINeistä ja niihin liitetyistä toiminnoista. Voit määrittää temppujen PIN-koodit ja niiden kanssa yhdistetyt toiminnot uudelleen. Voit myös piilottaa tai poistaa sen valitsemalla PIN-koodin ja valitsemalla sitten `Piilota temppu` tai `Poista temppu`.


![60](assets/en/60.webp)


### Trick PIN-koodit - Lisää jos väärässä


Vaihtoehtoisesti voit lisätä toiminnon "Lisää jos väärin", joka käynnistyy, kun väärä PIN-koodi on syötetty tietty määrä kertoja. Voit määrittää tämän suorittamalla seuraavat vaiheet:


1. Kytke Mk4-laitteeseen virta kytkemällä se virtalähteeseen.

2. Syötä PIN-koodi.

3. Mene kohtaan "Asetukset" > Valitse "Sisäänkirjautumisasetukset" > Valitse "Trick PIN-koodit" > Valitse "Lisää jos väärä".


![61](assets/en/61.webp)


4. Mk4 näyttää tätä asetusta koskevan viestin. Siirry alaspäin, kun luet selityksen läpi, ja jatka sitten painamalla `✓`.

5. Syötä virheellisten yritysten määrä, joka tarvitaan toimenpiteen käynnistämiseksi. Huomautus: Yritysten enimmäismäärä on `12`. Tämä johtuu siitä, että Mk4 on suunniteltu siten, että kun väärä PIN-koodi syötetään `13` kertaa, laite sulkeutuu, jolloin se on pysyvästi käyttökelvoton. Kun olet syöttänyt numeron, jatka painamalla `✓`.

6. Valitse toiminto navigoimalla ylös tai alas. Käytettävissä olevat toiminnot ovat seuraavat:


   - "Pyyhi, Lopeta": seedphrase pyyhitään ja laite näyttää "Seed is wiped, Stop"
   - pyyhi ja käynnistä uudelleen: seedphrase poistetaan ja laite käynnistyy uudelleen ilman viestiä.
   - `Silent Wipe`: seedphrase pyyhitään hiljaa ja laite käyttäytyy kuin väärän PIN-koodin yritys (ei selvää pyyhintäviestiä).
   - `Brick Self`: Laite on pysyvästi poistettu käytöstä ja näyttää vain "Bricked"
   - "Viimeinen mahdollisuus": seedphrase poistetaan, mutta saat vielä yhden viimeisen PIN-koodiyrityksen; jos syötät väärän PIN-koodin uudelleen, laite sammuu.
   - `Just Reboot`: Laite yksinkertaisesti käynnistyy uudelleen, eikä mikään muu muutu.

Valitse haluamasi toiminto ja jatka painamalla `✓`


![62](assets/en/62.webp)


7. Pääset takaisin hakemistoon `Asetukset > Kirjautumisasetukset > Trick PINs`. `Trick PINs:` -hakemiston alta löydät luettelon temppukoodeista sekä `WRONG PIN`-toiminnon. Voit myös piilottaa tai poistaa sen valitsemalla PIN-koodin ja valitsemalla sitten `Piilota temppu` tai `Poista temppu`.


![63](assets/en/63.webp)



## Päätelmä


Tässä oppaassa on kerrottu, miten Mk4:n asetukset otetaan käyttöön, miten Bitcoin-tapahtumia suoritetaan Mk4:llä ja miten Mk4:n lisäominaisuuksia käytetään. Se tarjoaa turvallisia ja joustavia tapoja säilyttää ja hallita bitcoineja. Sen rakenne varmistaa, että yksityiset avaimet eivät koskaan poistu laitteesta, ja ominaisuudet, kuten passphrase, temppu-PINit ja ilmaan kytketyt transaktiot, antavat käyttäjille täyden hallinnan tietoturva-asetuksistaan. Se voidaan yhdistää Sparrow Wallet:n kanssa, jolloin Bitcoin-tapahtumien luominen, allekirjoittaminen ja hallinnointi on käyttäjäystävällistä yksityisyydestä tai turvallisuudesta tinkimättä.


Jos haluat tutustua muihin toiminnallisuuksiin, voit tutustua dokumentaatioon Coinkiten verkkosivustolla [täällä](https://coldcard.com/docs/). Toivottavasti tästä ohjeesta on hyötyä, kun käytät Coldcard Mk4:ää. Kiitos ja nähdään ensi kerralla!