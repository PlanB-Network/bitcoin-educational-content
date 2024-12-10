---
name: VeraCrypt
description: Kuinka helposti salata tallennuslaite?
---
![cover](assets/cover.webp)

Nykyään on tärkeää toteuttaa strategia tiedostojen, kuten henkilökohtaisten dokumenttien, valokuvien tai tärkeiden projektien, saatavuuden, turvallisuuden ja varmuuskopioinnin varmistamiseksi. Näiden tietojen menettäminen voi olla katastrofaalista.

Näiden ongelmien estämiseksi neuvon sinua ylläpitämään useita varmuuskopioita tiedostoistasi eri medioilla. Tietotekniikassa yleisesti käytetty strategia on "3-2-1" varmuuskopiostrategia, joka varmistaa tiedostojesi suojauksen:
- **3** kappaletta tiedostoistasi;
- Tallennettuna ainakin **2** eri tyyppiselle medialle;
- Vähintään **1** kopio säilytetään ulkopuolisessa sijainnissa.

Toisin sanoen on suositeltavaa säilyttää tiedostosi kolmessa eri paikassa, käyttäen eri luonteisia medioita, kuten tietokonettasi, ulkoista kovalevyä, USB-tikkua tai online-tallennuspalvelua. Ja lopuksi, ulkopuolisen kopion säilyttäminen tarkoittaa, että sinulla tulisi olla varmuuskopio tallennettuna kodin tai yrityksen ulkopuolelle. Tämä viimeinen kohta auttaa välttämään tiedostojen täydellisen menetyksen paikallisten katastrofien, kuten tulipalojen tai tulvien, sattuessa. Ulkoinen kopio, kaukana kodistasi tai yrityksestäsi, varmistaa, että tietosi säilyvät riippumatta paikallisista riskeistä.

Tämän 3-2-1 varmuuskopiostrategian helpoksi toteuttamiseksi voit valita online-tallennusratkaisun, synkronoimalla tiedostot tietokoneeltasi pilveen automaattisesti tai säännöllisesti. Näiden online-varmuuskopioratkaisujen joukossa on tietenkin niitä suurilta digitaalisilta yrityksiltä, joita tunnet: Google Drive, Microsoft OneDrive tai Apple iCloud. Nämä eivät kuitenkaan ole parhaita ratkaisuja yksityisyytesi suojaamiseen. Aiemmassa oppaassa esittelin sinulle vaihtoehdon, joka salaa dokumenttisi paremman luottamuksellisuuden saavuttamiseksi: Proton Drive.

https://planb.network/tutorials/others/general/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Noudattamalla tätä paikallisen ja pilven varmuuskopiointistrategiaa hyödyt jo kahdesta eri tyyppisestä mediasta tiedoillesi, joista toinen on ulkopuolinen. 3-2-1 strategian täydentämiseksi sinun tarvitsee vain lisätä ylimääräinen kopio. Neuvoni on yksinkertaisesti säännöllisesti viedä tietosi paikallisesti ja pilvestä fyysiselle medialle, kuten USB-tikulle tai ulkoiselle kovalevylle. Näin, vaikka online-tallennusratkaisusi palvelimet tuhoutuisivat ja tietokoneesi hajoaisi samanaikaisesti, sinulla on silti tämä kolmas kopio ulkoisella medialla, jotta et menetä tietojasi.
![VeraCrypt](assets/notext/01.webp)
Mutta on myös tärkeää miettiä tallennettujen tietojesi turvallisuutta varmistaaksesi, että kukaan muu kuin sinä tai läheisesi eivät pääse niihin käsiksi. Sekä paikalliset että online-tiedot ovat yleensä turvassa. Tietokoneellasi olet todennäköisesti asettanut salasanan, ja nykyaikaisten tietokoneiden kovalevyt ovat usein oletuksena salattuja. Online-tallennustilasi (pilvi) osalta näytin sinulle edellisessä oppaassa, kuinka voit suojata tilisi vahvalla salasanalla ja kaksivaiheisella todennuksella. Kuitenkin kolmannen kopiosi, joka on tallennettu fyysiselle medialle, ainoa turva on sen fyysinen hallussapito. Jos murtovaras onnistuu varastamaan USB-tikkusi tai ulkoisen kovalevysi, hän voisi helposti päästä käsiksi kaikkiin tietoihisi.
![VeraCrypt](assets/notext/02.webp)
Tämän riskin estämiseksi on suositeltavaa salata fyysinen mediasi. Näin ollen kaikki yritykset päästä käsiksi tietoihin vaativat salasanan syöttämisen sisällön salaamiseksi. Ilman tätä salasanaa tietoihin pääsy on mahdotonta, turvaten henkilökohtaiset tiedostosi jopa USB-tikun tai ulkoisen kovalevyn varkauden sattuessa.
![VeraCrypt](assets/notext/03.webp)
Tässä oppaassa näytän sinulle, kuinka voit helposti salata ulkoisen tallennusvälineen käyttäen VeraCryptia, avoimen lähdekoodin työkalua.
## VeraCryptin esittely

VeraCrypt on avoimen lähdekoodin ohjelmisto, joka on saatavilla Windowsille, macOS:lle ja Linuxille. Se mahdollistaa tietojesi salaamisen eri tavoin ja eri välineillä.
![VeraCrypt](assets/notext/04.webp)
Tämä ohjelmisto mahdollistaa salattujen volyymien luomisen ja ylläpidon lennossa, mikä tarkoittaa, että tietosi salataan automaattisesti ennen tallentamista ja puretaan ennen lukemista. Tämä menetelmä varmistaa, että tiedostosi pysyvät suojattuina jopa tallennusvälineesi varkauden sattuessa. VeraCrypt ei ainoastaan salaa tiedostoja, vaan myös tiedostonimet, metatiedot, kansiot ja jopa tallennusvälineesi vapaan tilan.

VeraCryptia voidaan käyttää tiedostojen salaamiseen paikallisesti tai kokonaisten osioiden, mukaan lukien järjestelmälevy, salaamiseen. Sitä voidaan myös käyttää ulkoisen välineen, kuten USB-tikun tai levyn, täydelliseen salaamiseen, kuten tässä oppaassa näemme.

VeraCryptin suuri etu omistuksellisiin ratkaisuihin verrattuna on, että se on täysin avoimen lähdekoodin, mikä tarkoittaa, että sen koodia voi tarkistaa kuka tahansa.

## Kuinka asentaa VeraCrypt?

Siirry [viralliselle VeraCryptin verkkosivustolle](https://www.veracrypt.fr/en/Downloads.html) "*Lataukset*" -välilehdelle.
![VeraCrypt](assets/notext/05.webp)
Lataa käyttöjärjestelmällesi sopiva versio. Jos käytät Windowsia, valitse "*EXE-asennusohjelma*".
![VeraCrypt](assets/notext/06.webp)
Valitse käyttöliittymäsi kieli.
![VeraCrypt](assets/notext/07.webp)
Hyväksy lisenssiehdot.
![VeraCrypt](assets/notext/08.webp)
Valitse "*Asenna*".
![VeraCrypt](assets/notext/09.webp)
Lopuksi valitse kansio, johon ohjelmisto asennetaan, ja napsauta "*Asenna*" -painiketta.
![VeraCrypt](assets/notext/10.webp)
Odota asennuksen valmistumista.
![VeraCrypt](assets/notext/11.webp)
Asennus on valmis.
![VeraCrypt](assets/notext/12.webp)
Halutessasi voit lahjoittaa bitcoineja tukeaksesi tämän avoimen lähdekoodin työkalun kehitystä.
![VeraCrypt](assets/notext/13.webp)
## Kuinka salata tallennuslaite VeraCryptilla?

Ensimmäisellä käynnistyskerralla saavut tähän käyttöliittymään:
![VeraCrypt](assets/notext/14.webp)
Salataksesi valitsemasi tallennuslaitteen, aloita yhdistämällä se koneeseesi. Kuten myöhemmin näet, uuden salatun volyymin luominen USB-tikulle tai kovalevylle kestää paljon kauemmin, jos laitteessa on jo tietoja, joita et halua poistaa. Siksi suosittelen käyttämään tyhjää USB-tikkua tai tyhjentämään laitteen etukäteen salatun volyymin luomiseksi, jotta säästät aikaa.

VeraCryptissa napsauta "*Volyymit*" -välilehteä.
![VeraCrypt](assets/notext/15.webp)
Sitten valitse "*Luo uusi volyymi...*" -valikko.
![VeraCrypt](assets/notext/16.webp)
Uudessa ikkunassa, joka avautuu, valitse vaihtoehto "*Salaa ei-järjestelmäosio/-asema*" ja napsauta "*Seuraava*".
![VeraCrypt](assets/notext/17.webp)
Sinun täytyy sitten valita "*Standard VeraCrypt volume*" ja "*Hidden VeraCrypt Volume*" välillä. Ensimmäinen vaihtoehto luo standardin salatun tilavuuden laitteellesi. "*Hidden VeraCrypt Volume*" -vaihtoehto mahdollistaa piilotetun tilavuuden luomisen standardin VeraCrypt-tilavuuden sisälle. Tämä menetelmä mahdollistaa sinun kieltää tämän piilotetun tilavuuden olemassaolon pakotilanteessa. Esimerkiksi, jos joku fyysisesti pakottaa sinut salaamaan laitteesi, voit salata vain standardiosan tyydyttääksesi hyökkääjän, mutta et paljasta piilotettua osaa. Esimerkissäni pysyttelen standarditilavuudessa. ![VeraCrypt](assets/notext/18.webp)
Seuraavalla sivulla, klikkaa "*Select Device...*" -painiketta.
![VeraCrypt](assets/notext/19.webp)
Uusi ikkuna avautuu, jossa voit valita tallennuslaitteesi osion saatavilla olevien levyjen listasta. Normaalisti haluamasi osio on listattu rivillä, joka on otsikoitu "*Removable Disk N*". Valittuasi sopivan osion, klikkaa "*OK*" -painiketta.
![VeraCrypt](assets/notext/20.webp)
Valittu tuki näkyy laatikossa. Voit nyt klikata "*Next*" -painiketta. ![VeraCrypt](assets/notext/21.webp)
Seuraavaksi sinun täytyy valita vaihtoehdoista "*Create encrypted volume and format it*" tai "*Encrypt partition in place*". Kuten aiemmin mainittiin, ensimmäinen vaihtoehto poistaa pysyvästi kaikki tiedot USB-tikultasi tai kovalevyltäsi. Valitse tämä vaihtoehto vain, jos laitteesi on tyhjä; muuten menetät kaikki sen sisältämät tiedot. Jos haluat säilyttää olemassa olevat tiedot, voit väliaikaisesti siirtää ne muualle, valita "*Create encrypted volume and format it*" nopeammalle prosessille, joka poistaa kaiken, tai valita "*Encrypt partition in place*". Tämä viimeinen vaihtoehto mahdollistaa tilavuuden salaamisen poistamatta jo olemassa olevia tietoja, mutta prosessi on paljon pidempi. Tässä esimerkissä, koska USB-tikkuni on tyhjä, valitsen "*Create encrypted volume and format it*", vaihtoehdon, joka poistaa kaiken.
![VeraCrypt](assets/notext/22.webp)
Seuraavaksi sinulla on mahdollisuus valita salausalgoritmi ja hajautusfunktio. Ellei sinulla ole erityistarpeita, suosittelen pitämään oletusvaihtoehdot. Klikkaa "*Next*" jatkaaksesi.
![VeraCrypt](assets/notext/23.webp)
Varmista, että tilavuutesi ilmoitettu koko on oikea, jotta salaat koko käytettävissä olevan tilan USB-tikulla, eikä vain osaa siitä. Kun olet varmistanut, klikkaa "*Next*".
![VeraCrypt](assets/notext/24.webp)
Tässä vaiheessa sinun täytyy asettaa salasana laitteesi salaamiseen ja salaamisen purkamiseen. On tärkeää valita vahva salasana estääksesi hyökkääjää purkamasta sisältöäsi brute force -hyökkäyksillä. Salasanan tulisi olla satunnainen, mahdollisimman pitkä ja sisältää useita merkkityyppejä. Neuvon sinua valitsemaan satunnaisen salasanan, joka on vähintään 20 merkkiä pitkä ja sisältää pieniä kirjaimia, isoja kirjaimia, numeroita ja symboleita.

Neuvon myös tallentamaan salasanasi salasananhallintaohjelmaan. Tämä helpottaa pääsyä ja eliminoi unohtamisen riskin. Erityistapauksessamme salasananhallintaohjelma on suositeltavampi kuin paperinen väline. Todellakin, murron sattuessa, vaikka tallennuslaitteesi saatettaisiin varastaa, salasana hallintaohjelmassa ei ole hyökkääjän löydettävissä, mikä estää pääsyn tietoihin. Toisaalta, jos salasananhallintaohjelmasi on kompromisoitu, fyysinen pääsy laitteeseen on silti tarpeen hyödyntää salasanaa ja päästä käsiksi tietoihin.

Lisätietoja salasanojen hallinnasta, suosittelen tutustumaan tähän toiseen kattavaan opastukseen:
Syötä salasanasi kahteen määrättyyn kenttään ja napsauta sitten "*Seuraava*". ![VeraCrypt](assets/notext/25.webp)
VeraCrypt kysyy sinulta, aiotko tallentaa suurempia kuin 4 GiB tiedostoja salattuun taltioon. Tämä kysymys mahdollistaa ohjelmiston valita sopivimman tiedostojärjestelmän. Yleensä käytetään FAT-järjestelmää, koska se on yhteensopiva useimpien käyttöjärjestelmien kanssa, mutta se asettaa maksimitiedostokoon rajaksi 4 GiB. Jos tarvitset suurempien tiedostojen hallintaa, voit valita exFAT-järjestelmän.
![VeraCrypt](assets/notext/26.webp)
Seuraavaksi pääset sivulle, joka mahdollistaa satunnaisen avaimen luomisen. Tämä avain on tärkeä, sillä sitä käytetään tietojesi salaamiseen ja purkamiseen. Se tallennetaan tietovälineesi tiettyyn osioon, joka on suojattu aiemmin asettamallasi salasanalla. Vahvan salausavaimen luomiseksi VeraCrypt tarvitsee entropiaa. Siksi ohjelmisto pyytää sinua liikuttamaan hiirtäsi satunnaisesti ikkunan yli; näitä liikkeitä käytetään sitten avaimen luomiseen. Jatka hiiren liikuttamista, kunnes entropiamittari on täysin täytetty. Sen jälkeen napsauta "*Alusta*" aloittaaksesi salatun taltion luomisen.
![VeraCrypt](assets/notext/27.webp)
Odota, kunnes alustus on valmis. Tämä voi kestää kauan suurille taltioille.
![VeraCrypt](assets/notext/28.webp)
Saat sitten vahvistuksen.
![VeraCrypt](assets/notext/29.webp)
## Kuinka käyttää salattua asemaa VeraCryptin kanssa?

Toistaiseksi tietovälineesi on salattu, joten et voi avata sitä. Salataksesi sen, siirry VeraCryptiin.
![VeraCrypt](assets/notext/30.webp)
Valitse listasta aseman kirjain. Esimerkiksi minä valitsin "*L:*".
![VeraCrypt](assets/notext/31.webp)
Napsauta "*Valitse laite...*" -painiketta.
![VeraCrypt](assets/notext/32.webp)
Valitse koneesi kaikista levyistä salattu taltio tietovälineelläsi ja napsauta sitten "*OK*" -painiketta.
![VeraCrypt](assets/notext/33.webp)
Näet, että taltiosi on hyvin valittu.
![VeraCrypt](assets/notext/34.webp)
Napsauta "*Liitä*" -painiketta.
![VeraCrypt](assets/notext/35.webp)
Syötä taltion luomisen aikana valitsemasi salasana ja napsauta sitten "*OK*".
![VeraCrypt](assets/notext/36.webp)
Näet, että taltiosi on nyt purettu ja käytettävissä aseman kirjaimella "*L:*".
![VeraCrypt](assets/notext/37.webp)
Päästäksesi siihen, avaa tiedostonhallintasi ja siirry asemaan "*L:*" (tai toiseen kirjaimeen riippuen siitä, minkä valitsit aiemmissa vaiheissa). ![VeraCrypt](assets/notext/38.webp)
Lisättyäsi henkilökohtaisia tiedostoja tietovälineeseen, salataksesi taltion uudelleen, napsauta yksinkertaisesti "*Irrota*" -painiketta.
![VeraCrypt](assets/notext/39.webp)
Taltiosi ei enää näy kirjaimen "*L:*" alla. Se on siis salattu uudelleen.
![VeraCrypt](assets/notext/40.webp)
Voit nyt poistaa tallennusvälineesi.

Onnittelut, sinulla on nyt salattu väline henkilökohtaisten tietojesi turvalliseen säilyttämiseen, mikä täydentää 3-2-1 strategiaasi lisäksi tietokoneesi kopion ja online-tallennusratkaisusi kanssa.
Jos haluat tukea VeraCryptin kehitystä, voit myös lahjoittaa bitcoineja [tällä sivulla](https://www.veracrypt.fr/en/Donation.html).