---
name: Silentium
description: Progressiivinen web wallet hiljaisten maksujen tuella (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin-osoitteiden uudelleenkäyttö on yksi välittömimmistä uhkista käyttäjien luottamuksellisuudelle. Kun vastaanottaja käyttää samaa osoitetta useiden maksujen vastaanottamiseen, kuka tahansa tarkkailija voi jäljittää kaikki siihen liittyvät maksutapahtumat ja rekonstruoida niiden taloushistorian. Tämä ongelma vaikuttaa erityisesti sisällöntuottajiin, hyväntekeväisyysjärjestöihin ja aktivisteihin, jotka haluavat julkisesti näyttää lahjoitusosoitteensa vaarantamatta yksityisyyttään.



Silentium vastaa tähän ongelmaan tyylikkäällä ratkaisulla, jota voi käyttää suoraan selaimesta. Tämä avoimen lähdekoodin progressiivinen verkkosovellus (PWA), jonka Louis Singer lanseerasi toukokuussa 2024, toteuttaa Silent Paymentsin (BIP-352): uudelleenkäytettävän staattisen osoitteen, jossa jokainen maksu päätyy erilliseen lohkoketjuosoitteeseen ilman edeltävää vuorovaikutusta tai havaittavaa linkkiä tapahtumien välillä.



**Tärkeä varoitus**: Silentium on kokeellinen projekti, joka toimii *konseptitodisteena* Silent Paymentsin kevyille lompakoille. Sitä ei tulisi käyttää päivittäisenä wallet:nä tai merkittävien summien tallentamiseen. Kehittäjät toteavat nimenomaisesti:



> Käytä omalla vastuullasi.

Huomaa, että tätä wallet:tä voidaan käyttää testiverkkona tai regtestinä.



## Mikä on Silentium?



### Filosofia ja tavoitteet



Silentium toimii teknisenä demonstraationa hiljaisten maksujen toteuttamisesta kevyessä wallet-selaimessa. Vaikka se tukee myös tavanomaisia Bitcoin-osoitteita, pääpaino on Hiljaisissa maksuissa, jotta käyttäjät voivat kokeilla tätä yksityisyystekniikkaa yksinkertaisella tavalla.



### Miten hiljaiset maksut toimivat?



Hiljaisissa maksuissa (BIP-352) käytetään Elliptic Curve Diffie-Hellman -avainta Exchange (ECDH). Vastaanottaja luo staattisen osoitteen (`sp1...` mainnet:ssä, `tsp1...` testnetissä), joka koostuu kahdesta julkisesta avaimesta: skannausavaimesta maksujen havaitsemiseksi ja käyttöavaimesta niiden käyttämiseksi.



Lähettäjä yhdistää yksityiset syöttöavaimensa vastaanottajan skannausavaimeen laskeakseen jaetun salaisuuden, joka tuottaa kryptografisen "virityksen". Kun tämä "tweak" lisätään menoavaimeen, luodaan jokaiselle tapahtumalle yksilöllinen Taproot-osoite. Vastaanottaja toistaa tämän laskennan yksityisellä skannausavaimellaan havaitakseen ja käyttäessään varat ilman edeltävää vuorovaikutusta.



Edut: parempi luottamuksellisuus lähettäjän ja vastaanottajan kannalta, ei tarvita kolmannen osapuolen palvelinta, maksutapahtumat erottuvat tavanomaisista Taproot-maksuista. Suurin haittapuoli: lohkoketjun intensiivinen skannaus maksujen havaitsemiseksi.



Jos haluat lisätietoja Hiljaisten maksujen teoreettisesta toiminnasta, katso BTC,204-kurssin viimeinen osa Plan ₿ Academy:sta:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Tuetut alustat



Silentium on progressiivinen verkkosovellus (PWA, Progressive Web App), jota voi käyttää millä tahansa nykyaikaisella selaimella (mobiili- tai työpöytäselaimella). Käytä sitä suoraan osoitteessa `app.silentium.dev`, asenna se natiivina sovelluksena selaimen kautta tai ota se käyttöön paikallisesti. Asennus tapahtuu suoraan selaimesta, ilman virallisten kauppojen kautta kulkemista.



## Web-sovelluksen käyttäminen



### Pääsy ja asennus



[Siirry selaimellasi osoitteeseen `https://app.silentium.dev/`](https://app.silentium.dev/). Sovellus latautuu välittömästi ja näyttää aloitusnäytön.



Jos haluat asentaa sen natiivina sovelluksena iOS:ssä, paina jakopainiketta (neliö, jossa on nuoli ylöspäin) ja valitse sitten "Aloitusnäytössä". Androidissa selain tarjoaa yleensä suoraan "Lisää aloitusnäyttöön" -ilmoituksen. Kun Silentium on asennettu, se näkyy omalla kuvakkeellaan ja toimii natiivina sovelluksena, mutta vaatii internet-yhteyden tapahtumien synkronoimiseksi.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Portfolion luominen



Valitse ensimmäisellä käynnistyskerralla "Luo Wallet", jos haluat luoda uuden salkun generate, tai "Palauta Wallet", jos haluat palauttaa olemassa olevan palautuslauseen.



Valitse "Luo Wallet". Sovellus luo 12-sanaisen lauseen, joka sinun on kirjoitettava huolellisesti ylös. Tämä lause on ainoa tapa saada rahasi takaisin. Ota käyttöön hyvät varmuuskopiointikäytännöt myös testnetissä. Paina "Jatka" tallennettuasi lauseen.



Tämän jälkeen sovellus pyytää sinua asettamaan salasanan, jolla suojataan pääsy wallet:ään. Valitse vahva salasana ja vahvista se.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Kun lause on vahvistettu ja salasana asetettu, pääset pääkäyttöliittymään.



### Interface pää- ja parametrit



Pääkäyttöliittymässä näkyy saldosi satosheina (aluksi 0 sats), ja alareunassa on kolme painiketta:




- Sync**: synkronoi wallet:n lohkoketjun kanssa
- Vastaanottaa**: vastaanottaa varoja
- Lähetä**: lähettääksesi bitcoineja



Pääset asetuksiin oikeassa yläkulmassa olevan kuvakkeen kautta (kolme vaakasuoraa palkkia). Asetukset-valikossa on useita vaihtoehtoja:





- Tietoa**: hakutiedot
- Varmuuskopio**: palautuslauseen varmuuskopio
- Explorer**: valitse lohkoketjuetsintä (oletusarvoisesti Mempool) ja Silentiumd-palvelin
- Verkko**: verkon valinta (mainnet/testnet)
- Salasana**: vaihda salasana
- Uudelleenlataus**: wallet:n uudelleenlataaminen
- Nollaus**: täydellinen nollaus
- Teema**: vaihda teema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Osio **Explorer** on erityisen tärkeä: sen avulla voit valita käytettävän lohkoketju-etsimen (oletusarvoisesti Mempool) ja näyttää myös Silentiumd-palvelimen URL-osoitteen (`https://bitcoin.silentium.dev/v1` mainnet:lle). Jos isännöit omaa Silentiumd-palvelinta tai haluat käyttää testnetiä, määritä nämä parametrit tässä.



### Varojen vastaanottaminen



Paina pääkäyttöliittymässä "Vastaanota"-painiketta. Oletusarvoisesti Silentium näyttää Silent Payment -osoitteen ja sen QR-koodin. Osoite alkaa kirjaimella `sp1...` mainnet:ssa tai `tsp1...` testnetissä.



Voit vaihtaa hiljaisen maksun ja klassisen Bitcoin-osoitteen välillä näytön alareunassa olevan "Vaihda klassiseen osoitteeseen" / "Vaihda hiljaiseen osoitteeseen" -painikkeen avulla.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Kun tapahtuma on lähetetty, odota muutama minuutti. Hiljaisten maksujen osalta Silentium etsii automaattisesti lohkoketjusta sinulle tarkoitettuja tapahtumia. Transaktiot näkyvät tilassa "Vahvistamaton" ennen kuin ne vahvistetaan asteittain.



### Lähetä maksu



Paina pääkäyttöliittymästä Lähetä-painiketta. Lähetysnäyttö kysyy sinulta :



1. **Address**: liitä Silent Payment -osoite (`sp1...` tai `tsp1...`) tai klassinen Bitcoin-osoite. Voit skannata osoitteen QR-skannauskuvakkeella.


2. **Määrä**: Kirjoita lähetettävä määrä satosheina. Näytössä on numeronäppäimistö, joka helpottaa syöttämistä. Käytettävissä oleva saldosi näkyy yläreunassa.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Kun olet syöttänyt osoitteen ja summan, jatka painamalla "Jatka". Sovellus pyytää sinua valitsemaan haluamasi maksutason ennen maksutapahtuman vahvistamista.



## wallet:n itseisännöinti



### Miksi itse isännöidä?



Silentiumin paikallinen hosting tarjoaa täydellisen riippumattomuuden, koodin tarkistuksen, kehitysympäristön ja joustavuuden virallisten sivustojen häiriöiden varalta.



### Edellytykset



Node.js (versio 14+), npm tai yarn, Git ja noin 500 Mt levytilaa.



### Paikallinen asennus



Kloonaa arkisto ja asenna :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Käynnistäminen ja käyttö



Käynnistä sovellus kehitystilassa:



```bash
yarn start
```



Siirry selaimessasi osoitteeseen `http://localhost:3000`. Optimoitu tuotantoversio :



```bash
yarn build
```



`build/`:ssä luotuja tiedostoja voidaan käyttää nginxillä, Apachella tai millä tahansa web-palvelimella. Oletusarvoisesti Silentium muodostaa yhteyden julkiseen `bitcoin.silentium.dev`-palvelimeen. Muuta tätä asetusta parametreissa käyttääksesi testnetiä tai omaa palvelintasi.



## Silentiumd-palvelin



### Tehtävä ja toiminta



Silentium käyttää **Silentiumd**-indeksipalvelinta maksujen havaitsemisen optimoimiseksi. Kaikkien Taproot-tapahtumien skannaaminen olisi liian hankalaa selaimelle tai matkapuhelimelle.



Silentiumd laskee välitiedot (tweakit) etukäteen jokaista Taproot-transaktiota varten. wallet lataa nämä viritykset (muutama tavu per tapahtuma) ja suorittaa lopullisen laskennan paikallisesti, jolloin maksun omistajuus tarkistetaan. Palvelin ei koskaan tiedä avaimiasi tai voi tunnistaa transaktioitasi, toisin kuin perinteiset Electrum-palvelimet.



Kompaktit BIP158-suodattimet antavat wallet:n määrittää, mitkä lohkot skannataan paljastamatta osoitteitasi, jolloin luottamuksellisuus säilyy.



### Julkinen palvelin



Vulpem Venturesin sponsoroima julkinen palvelin `bitcoin.silentium.dev` (mainnet) tarjoaa yksinkertaisen ja välittömän kokemuksen. Vaikka luottamuksellisuus säilyy, tämä lähestymistapa edellyttää suhteellista luottamusta kolmannen osapuolen infrastruktuuriin.



### Isännöi omaa Silentiumd-palvelinta



Jos haluat täydellisen itsemääräämisoikeuden, isännöi omaa Silentiumd-palvelinta. Edellytykset: Bitcoin Core, jossa on `txindex=1` ja `blockfilterindex=1`, Go 1.21+, 10-20 GB levytilaa, järjestelmänhallintataitoja.



**Asennus:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Määritä ympäristömuuttujien avulla (katso arkiston `config.md`-tiedostosta lisätietoja). Palvelin indeksoi lohkoketjun ja paljastaa API:n, jota wallet voi kysyä.



Umbrel:lle tai Start9:lle ei ole tällä hetkellä olemassa pakettiratkaisuja, mikä rajoittaa muiden kuin teknisten käyttäjien mahdollisuuksia.



## Edut ja rajoitukset



### Kohokohdat





- Maksimaalinen saavutettavuus**: käyttö millä tahansa selaimella, ei vaadi raskasta asennusta
- Monialustaisuus**: toimii mobiililaitteissa (Android/iOS) ja työpöydällä PWA-teknologian ansiosta
- Yksinkertainen itsepalvelu**: paikallinen asennus mahdollista muutamalla komennolla
- Avoin lähdekoodi**: täysin tarkastettavissa oleva koodi GitHubissa
- Yksityisyyden suojaan keskittyvä**: ei seurantaa, ei analytiikkaa, paikalliset kryptografiset laskutoimitukset
- Erillinen arkkitehtuuri**: wallet (asiakas) ja indeksointipalvelin erotetaan selkeästi toisistaan
- Ilman tiliä**: rekisteröintiä tai henkilötietoja ei tarvita



### Huomioon otettavat rajoitukset





- Kokeellinen hanke**: ainoastaan konseptin todistus, ei tarkoitettu päivittäiseen käyttöön tai tuotantoon
- Ei takuita**: virheiden ja haavoittuvuuksien riski, mahdollinen varojen menetys
- Rajoitettu tuki**: vähän käyttäjädokumentaatiota, pieni yhteisö, ei virallista tukea
- Palvelinriippuvuus**: vaatii toimivan Silentiumd-palvelimen (julkinen tai itse isännöity)
- Intensiivinen skannaus**: Hiljainen maksujen havaitseminen kuluttaa kaistanleveyttä
- Vähennetyt toiminnot**: ei kolikonvalvontaa, ei Lightningia, ei moniosoituksia



## Parhaat käytännöt



### seed turvallisuus



Suhtaudu toipumislausekkeeseen vakavasti myös testnetissä. Kirjoita se muistiin ja säilytä sitä turvallisessa paikassa. Pidä erilliset lompakot testiverkkoa ja mainnet:tä varten: älä koskaan käytä testi-seed:ta wallet:ssä, joka on tarkoitettu oikeille varoille.



### Lähdekoodin todentaminen



Yksi itse isännöinnin eduista on mahdollisuus tarkistaa lähdekoodi ennen sen suorittamista. Jos aiot käyttää Silentiumia oikeilla varoilla, käytä aikaa koodin tarkastamiseen tai pyydä luotettavaa kehittäjää tekemään se. Vertaa myös `app.silentium.dev`-sivustolla käyttöönotetun koodin hash-arvoa GitHub-tietovaraston hash-arvoon aitouden varmistamiseksi.



### Varmuuskopiointi ja palauttaminen



Hiljaisten maksujen varojen takaisinperintä edellyttää wallet:a, joka on yhteensopiva BIP-352-protokollan kanssa. Tavallinen wallet ei voi skannata lohkoketjua UTXO:n hiljaisten maksujen palauttamiseksi. Pidä Silentium asennettuna tai varmista, että sinulla on käytettävissäsi toinen yhteensopiva wallet (kuten Cake Wallet tai muut tulevat toteutukset), jotta voit tarvittaessa palauttaa varasi.



## Päätelmä



Silentium tarjoaa helppokäyttöisen testialustan Silent Paymentsin ymmärtämiseen ilman teknisiä ongelmia. Konseptitodisteena se osoittaa, miten tämä yksityisyysteknologia voidaan integroida wallet-selaimeen säilyttäen samalla itsesäilytyksen. Kokeile testnetissä ja tutustu tähän lupaavaan läpimurtoon on-chain:n yksityisyydensuojassa.



## Resurssit



### Viralliset asiakirjat




- Silentiumin GitHub-arkisto (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub-repository (palvelin): https://github.com/louisinger/silentiumd
- Web-sovellus: https://app.silentium.dev/
- Hiljaiset maksut -yhteisön sivusto: https://silentpayments.xyz
- Eritelmä BIP-352: https://bips.dev/352



### Artikkelit ja resurssit




- Virallinen ilmoitus (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Hiljaiset maksut: https://bitcoinops.org/en/topics/silent-payments/



### Testnet-työkalut




- Testnet hana: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet