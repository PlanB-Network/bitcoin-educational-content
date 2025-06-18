---
name: Sateenvarjo Nostr
description: Nostr-sovellusten määrittäminen ja käyttö Umbrelissa
---

![cover](assets/cover.webp)



## Edellytykset: Sateenvarjon asennus



Umbrel on avoimen lähdekoodin alusta, jonka avulla voit helposti isännöidä Bitcoin-sovelluksia ja muita palveluja omalla henkilökohtaisella palvelimellasi. Se on kokonaisratkaisu, joka yksinkertaistaa huomattavasti Bitcoin-solmujen ja hajautettujen sovellusten itseisännöintiä.



Varmista, että olet asentanut Umbrelin asennusoppaan mukaisesti:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Johdanto Nostriin



**Nostr** on avoin, hajautettu verkkoprotokolla, joka on suunniteltu sosiaaliseen verkostoitumiseen. Sen nimi tulee sanoista _"Notes and Other Stuff Transmitted by Relays"_. Sen avulla kuka tahansa voi julkaista viestejä (muistiinpanoja), joita hallitaan JSON-tapahtumina, ja levittää niitä keskitetyn alustan sijaan relepalvelimien kautta. Jokaisella käyttäjällä on kryptografinen avainpari (yksityinen/julkinen), joka toimii tunnisteena: julkinen avain (npub) tunnistaa käyttäjän, ja yksityinen avain (nsec) mahdollistaa viestien allekirjoittamisen. Tämän hajautetun arkkitehtuurin ansiosta **Nostr on sensuurin kestävä** ja erittäin joustava: voit käyttää useita asiakkaita ja muodostaa yhteyden niin moneen releeseen kuin haluat ilman, että olet riippuvainen yhdestä palvelimesta.



Lyhyesti sanottuna Nostr on hajautettu viestintäprotokolla, jossa **asiakkaat** (käyttäjäsovellukset) lähettävät ja vastaanottavat tapahtumia **relayerien** (palvelimien) kautta. Tämä protokolla on ollut erityisen suosittu Bitcoin-yhteisön keskuudessa vuodesta 2023 lähtien sen hajauttamista ja tietojen riippumattomuutta koskevien arvojen vuoksi.



**Huomautus:** Nostrin käyttöä varten tarvitset yksityisen avaimesi (joka on luotu Nostr-asiakasohjelmalla tai erillisellä laajennuksella). **Älä koskaan jaa yksityistä avaintasi**, koska se antaisi kenelle tahansa mahdollisuuden esiintyä sinuna. Säilytä se turvallisessa paikassa ja käytä turvallisia avaimenhallintatyökaluja (katso vinkki alla).



## Nostrin sateenvarjosovellukset



Umbrel tarjoaa integroitujen sovellusten ekosysteemin, jonka avulla voit hyödyntää Nostria täysimääräisesti henkilökohtaisessa solmussasi. Kerromme yksityiskohtaisesti tärkeimpien Nostriin liittyvien sovellusten käytöstä: **Nostr Relay**, **noStrudel**, **Snort** ja **Nostr Wallet Connect**. Kukin vastaa tiettyyn tarpeeseen: _Nostr Relay_ on **yksityinen relepalvelin**, _noStrudel_ ja _Snort_ ovat **Nostr-asiakkaita** (käyttöliittymiä muistiinpanojen lukemiseen/julkaisemiseen), kun taas _Nostr Wallet Connect_ on työkalu, jolla voit yhdistää **Lightning-salkkusi** Nostriin.



### Nostr Relay - Yksityinen relaysi Umbrelissa



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** on Umbrelin virallinen sovellus, jolla voit käyttää **omaasi Nostr-relayta** solmussasi. Päätavoitteena on saada **yksityinen** ja luotettava rele, joka **varmistaa kaiken Nostr**-toimintasi reaaliajassa. Toisin sanoen, käyttämällä tätä henkilökohtaista relettä julkisten releiden lisäksi, varmistat, että kaikki muistiinpanosi, viestisi ja reaktiosi kopioituvat kotiin, turvassa sensuurilta tai tietojen katoamiselta.



**Asennus:** Asenna _Nostr Relay_ Umbrel App Storesta (kategoria _Social_). Kun sovellus on käynnistetty, se toimii taustalla (docker service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Näet sen Interface-verkon Umbrelin kautta: se antaa perustiedot ja ennen kaikkea releesi URL-osoitteen (oikealla ylhäällä), joka sinun on kopioitava myöhempää käyttöä varten. Saatavilla on myös synkronointipainike (maapallokuvake).



**Hyödyntääksesi sateenvarjoreleesi :



**Lisää rele Nostr-asiakasohjelmaan:** Lisää aiemmin kopioimasi yksityisen releen URL-osoite asiakassovellukseesi (esim. Damus iOS:ssä, Amethyst Androidissa, Snort tai noStrudel Umbrelissa jne.). Oletusarvoisesti Umbrelin rele kuuntelee porttia **4848**. Jos käytät sitä lähiverkossa, URL-osoite on seuraavanlainen: `ws://umbrel.local:4848` (tai käytä Umbrelin paikallista IP-osoitetta).



Jos käytät Tailscalea (ks. alla), voit jopa käyttää MagicDNS:n DNS-alasanaa (yleensä `umbrel` tai automaattisesti luotua nimeä) käyttääksesi sitä mistä tahansa, aina portissa 4848.



Jos haluat mieluummin Torin, hanki Umbrelin .onion Address ja käytä sitä portilla 4848 Tor-yhteensopivan selaimen tai asiakkaan kautta (katso Tor-osio)



Kun URL-osoite on lisätty Nostr-asiakkaasi relekonfiguraatioon, muodosta yhteys tähän relekeskukseen. Sinun pitäisi nähdä asiakasohjelmassasi, että Umbrel-rele on yhdistetty (yleensä merkkinä on Green-piste tai vastaava).



**Synkronoi historia (valinnainen)**: Nostr Relayn Interface-verkossa Umbrelissa, napsauta **globe** 🌐 -kuvaketta (sivun yläosassa). Tämä toiminto pakottaa Umbrel-releesi muodostamaan yhteyden muihin releisiisi (jotka on määritetty asiakasohjelmassasi), jotta voit **importoida vanhat julkiset** aktiviteettisi. Tämä tarkoittaa sitä, että julkisten releiden kautta julkaisemasi tai lukemasi aiemmat muistiinpanot ladataan ja tallennetaan myös yksityiseen releeseesi. Odota, että synkronointi tapahtuu.



**Käytä Nostria tavalliseen tapaan:** Tästä lähtien kaikki uusi toiminta (julkaistut muistiinpanot, reaktiot, salatut yksityisviestit jne.), jonka teet Nostrissa, välitetään tavalliseen tapaan julkisiin releisiin **ja samanaikaisesti Umbrel-releeseesi**. Jos Nostr-asiakasohjelmasi on oikein konfiguroitu, se lähettää jokaisen tapahtuman kaikkiin releisiin (myös sinun releeseesi). Yksityinen releesi toimii reaaliaikaisena varmuuskopiona. Jopa siinä tapauksessa, että yhteys katkeaa tilapäisesti, asiakkaasi voivat synkronoida puuttuvat tiedot myöhemmin uudelleen tämän releen ansiosta. näin saat Nostr-tietojesi täydellisen hallinnan



Umbrelin _Nostr Relay_ perustuu avoimen lähdekoodin **nostr-rs-relay**-projektiin (Rust-protokollan toteutus). Se tukee koko Nostr-protokollaa ja lukuisia vakiomuotoisia NIP:iä (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33 jne.), mikä takaa mahdollisimman suuren yhteensopivuuden asiakkaiden kanssa.



### noStrudel - Nostr-asiakas tutkimusmatkailijoille



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** on tehokäyttäjälle suunnattu Nostr-verkkoasiakasohjelma, joka on ihanteellinen Nostr-verkon yksityiskohtaiseen ymmärtämiseen ja tutkimiseen. Se on eräänlainen hiekkalaatikko tapahtumien ja releiden tarkasteluun sekä protokollan lisäominaisuuksien kokeilemiseen. Interface on englanninkielinen ja suhteellisen tekninen, joten se sopii erinomaisesti kokeneille käyttäjille, jotka ovat uteliaita Nostrin sisäisestä toiminnasta.



**Asennus:** Asenna _noStrudel_ Umbrel App Storesta (kategoria _Sosiaalinen_). Kun se on käynnistetty, sitä voi käyttää selaimen kautta Umbrelin Address:ssä (esim. `http://umbrel.local` tai sen .onion/Tailscalen kautta, ks. kohta Ulkoinen käyttö).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Releiden konfigurointi:** Kun avaat noStrudelin, näet oikeassa yläkulmassa "Setup Relays" -painikkeen. Napsauta sitä konfiguroidaksesi releet.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Liitä tälle sivulle aiemmin kopioimasi Umbrel-releen URL-osoite. Voit lisätä myös muita sovelluksen oletusarvoisesti ehdottamia releitä. Kun olet määrittänyt releesi, klikkaa vasemmassa alareunassa olevaa "Kirjaudu sisään" jatkaaksesi.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Yhteys:** noStrudel tarjoaa useita yhteysvaihtoehtoja. Meidän tapauksessamme valitsemme "Yksityinen avain" ja liitämme aiemmin luodun Nostrin yksityisen avaimen. Jos sinulla ei vielä ole avainta, voit asentaa [Nostr Connect]-laajennuksen (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) luodaksesi ja/tai tallentaaksesi Nostr-avaimesi ja kommunikoidaksesi näin turvallisemmin eri Nostr-sovellusten kanssa.



![Interface principale de noStrudel](assets/fr/07.webp)



Kun yhteys on muodostettu, voit käyttää noStrudelia muistiinpanojesi jakamiseen Nostrin kautta. Interface antaa sinulle pääsyn :





- Täydellinen Nostr-kojelauta, jossa on muistiinpanojen aikajana, ilmoitukset, viestinvälitys, profiilihaku
- Relehallinta ja yhteyden tila
- Edistyneet työkalut tapahtumien ja niiden JSON-sisällön tutkimiseen
- Aikajanasuodattimien ja PIN-koodien konfigurointivaihtoehdot



**Vinkki:** _noStrudel_-ohjelmassa voit asettaa _aikataulusuodattimia_ tai testata erilaisia _NIP:iä (Nostr Implementation Possibilities)_. Tarkista esimerkiksi tuki NIP-05:lle (hajautetut tunnisteet) tai uudemmille ominaisuuksille. Tämä tekee _noStrudelista_ erinomaisen työkalun kokeilemiseen kontrolloidussa ympäristössä.



### Snort - Moderni Nostr-asiakas Umbrelissa



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** on toinen Umbrelissa saatavilla oleva Nostr-verkkopalveluasiakas, joka tarjoaa modernin, nopean ja selkeän **Interface**:n vuorovaikutukseen hajautetun sosiaalisen verkoston kanssa. Toisin kuin noStrudel, joka on suunnattu tehokäyttäjille, _Snort_ pyrkii helppokäyttöisyyteen toiminnallisuudesta tinkimättä. Se on rakennettu Reactilla, ja se tarjoaa siistin UX:n, joka muistuttaa klassisia sosiaalisia verkostoja, joten se sopii jokapäiväiseen käyttöön.



**Asennus:** Asenna _Snort_ Umbrel App Storesta (kategoria _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Kun avaat Snortin, näet vasemmassa alakulmassa "Rekisteröidy"-painikkeen.



![Options de connexion dans Snort](assets/fr/10.webp)



Voit joko rekisteröityä tai muodostaa yhteyden olemassa olevaan tiliin (kuten teemme tässä ohjeessa).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort tarjoaa useita yhteysmenetelmiä. Voit käyttää aiemmin asennettua Nostr Connect -laajennusta tai muita käytettävissä olevia menetelmiä. Kun yhteys on muodostettu, voit käyttää sovellusta täysimääräisesti.



_Snort_:n Interface tarjoaa :





- **Postit/Keskustelut/Globaali** -näyttö, jolla voit navigoida muistiinpanojesi, keskusteluketjujen tai globaalin syötteen välillä
- Välilehdet **Ilmoitukset**, **Viestit** (DM), **Haku**, **Profiili** jne. varten.
- **+**- tai _Write_-painike uuden muistion julkaisemiseksi
- **Tilausten (seuranta)** ja **luetteloiden** hallinnointi
- Releiden hallintavalikko releiden lisäämiseksi/poistamiseksi ja niiden saatavuuden seuraamiseksi



**Suositeltu relekonfiguraatio:** Lisätäksesi Umbrel-releen, siirry kohtaan Asetukset - Releet. Kirjoita releesi URL-osoite (`ws://umbrel:4848` tai muu URL-osoite konfiguraatiostasi riippuen) Snortin releiden luetteloon. Näin Snort julkaisee muistiinpanosi yksityisessä releessäsi julkisten lisäksi.



### Nostr Wallet Connect - Yhdistä Lightning Wallet Nostriin



**Nostr Wallet Connect (NWC)** on sovellus, joka **liittää Umbrel (Lightning)**-solmun yhteensopiviin Nostr-sovelluksiin Lightning-maksujen suorittamiseksi (esimerkiksi lähettämällä _zapseja_, mikromaksuja sisällön "tykkäämisestä"). Tässä opetusohjelmassa tarkastelemme, miten noStrudel liitetään Lightning-solmuun maksujen suorittamiseksi suoraan Interface:stä.



**Asennus ja konfigurointi:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Asenna _Nostr Wallet Connect_ Umbrelin Alby-kaupasta.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Klikkaa noStrudelissa profiiliasi oikeassa yläkulmassa ja sitten "hallinnoi" -painiketta.



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Napsauta "Lightning" ja sitten "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Valitse käytettävissä olevista yhteysvaihtoehdoista "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Napsauta "Connect", jolloin sinut ohjataan automaattisesti Umbrel Nostr Wallet Connect -istuntoon.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Nostr Wallet Connect -sivulla voit :




   - Määrittele enimmäisbudjettisi
   - Validoi valtuutukset
   - Aseta yhteyden päättymisaika


Viimeistele napsauttamalla "Yhdistä".



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Sinut ohjataan noStrudeliin ja saat vahvistusviestin: voit nyt zapata koko maailman Wallet/LND-solmusta!



NWC:n ansiosta **Lightning-maksut Nostrin kautta** (zapit palkitsemisviesteihin, _Value for Value_ -maksut jne.) alkavat **omasta solmusta**. Sinun ei enää tarvitse reitittää maksutapahtumia ulkoisten palveluiden kautta tai skannata QR-koodia puhelimellasi joka kerta. Käyttäjäkokemus paranee huomattavasti, mutta pysyy samalla _ei-vartijapainotteisena_ ja yksityisyydensuojaa kunnioittavana.



Jos haluat tietää, miten oma Lightning-solmu perustetaan Umbreliin, suosittelen tutustumaan tähän toiseen kattavaan opetusohjelmaan:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Kehittynyt konfigurointi ja turvallisuus



Umbrelin ja Nostrin käyttäminen yhdessä edistyneellä tasolla edellyttää erityistä huomiota **turvallisuuteen** ja **yhteyksiin**. Seuraavassa on muutamia vinkkejä siitä, miten voit suojata konfiguraatiosi ja käyttää sitä optimaalisesti, missä tahansa oletkin.



### Turvallinen ulkoinen pääsy: Tor ja Tailscale



Turvallisuussyistä Umbreliin pääsee oletusarvoisesti käsiksi vain lähiverkossa (ja Torin kautta). Jos haluat olla vuorovaikutuksessa Nostrin kanssa muualla kuin kotonasi, sinulla on kaksi ensisijaista ratkaisua: **Tor** (anonyymi pääsy sipuliverkon kautta) ja **Tailscale** (yksityinen VPN-verkko).





- Pääsy Torin kautta:** Umbrel määrittää automaattisesti **Tor-palvelun (.onion)** Interface-verkkoa ja -sovelluksia varten. Tämä tarkoittaa, että voit käyttää Interface Umbrelia (mukaan lukien _noStrudel_ tai _Snort_) mistä tahansa Tor-selaimen avulla paljastamatta julkista IP-osoitettasi. _Torin avulla voit käyttää Umbrel-palveluitasi lähiverkkosi ulkopuolelta paljastamatta laitettasi Internetille ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)). _ Käyttääksesi tätä vaihtoehtoa, siirry Umbrelin asetuksiin ja hae Umbrelisi .onion-URL-osoite (tai skannaa annettu QR-koodi). Käy Tor-selaimella tätä .onion Address: saat saman Interface:n kuin paikallisesti. Sen jälkeen voit käyttää Nostr-sovelluksiasi aivan kuten kotona.


**Nostr-rele Torin kautta:** Jos haluat, että asiakkaasi (tai valtuutetut ystäväsi) voivat käyttää Nostr-releetäsi Torin kautta, se on mahdollista. Umbrel ei tarjoa releen .onion Address:tä suoraan, mutta koska se toimii portissa 4848, voit joko :





    - Käytä UI Umbrelin .onion Address:ta ja määritä asiakkaasi ottamaan yhteys tämän Interface:n kautta (käytännöllisesti katsoen mahdotonta WebSocketille),





    - Tai** paljasta portti 4848 erillisenä sipulipalveluna. Tämä vaatii Umbrelin Tor-konfiguraation muokkaamista (varattu SSH:n hallitseville edistyneille käyttäjille). Vaihtoehtoisesti voit harkita **Tor-tunnelia** toisella palvelimella, joka ohjaa Umbreliin: henkilökohtaiseen käyttöön on kuitenkin helpointa käyttää Tailscalea.





- Pääsy Tailscalen kautta:** [Tailscale](https://tailscale.com/) on mesh-VPN-ratkaisu, joka luo virtuaalisen yksityisverkon laitteidesi ja Umbrelin välille. Etu: se toimii kuin olisit lähiverkossa, mutta Internetin kautta, salattuna ja ilman monimutkaisia asetuksia. **Tailscale määrittää Umbrel-laitteellesi kiinteän IP-osoitteen ja yksityisen verkkotunnuksen verkon sijainnista riippumatta ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. Käytännössä, kun olet asentanut Tailscalen Umbreliin (Umbrel App Storesta, kategoria _Networking_) **ja** laitteisiisi (matkapuhelin, PC...), voit tavoittaa Umbrelin Address:n kuten `100.x.y.z` (Tailscalen IP) tai nimen kuten `umbrel.tailnet123.ts.net` kautta.


nostr_:n osalta Tailscale on erittäin hyödyllinen: jos kännykkäsi, jossa Tailscale on aktiivinen, voi muodostaa yhteyden osoitteeseen `ws://umbrel:4848` (MagicDNS:n ansiosta) tai suoraan Tailscalen IP-osoitteeseen ja porttiin 4848 käyttääksesi relettä. Asiakkaat, kuten Damus tai Amethyst, näkevät Umbrelisi ikään kuin se olisi samassa lähiverkossa. **Vinkki:** Ota **MagicDNS** -vaihtoehto käyttöön Tailscale-ohjelmassa, jotta voit käyttää isäntänimeä `umbrel` sen sijaan, että muistaisit IP-osoitteen. Tämä takaa sujuvan yhteyden releeseesi myös silloin, kun olet liikkeellä ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Lisäksi Tailscalen avulla voit käyttää Interface Umbrelia (ja siten _noStrudel/Snort_-verkkoasiakkaita) yksinkertaisen selaimen kautta käyttämällä yksityistä IP-osoitetta tai määritettyä verkkotunnusta. Tor-selainta ei tarvita, ja tiedonsiirtonopeudet ovat yleensä paremmat kuin Tor-verkon kautta.




**Huomaa: Tor ja Tailscale eivät sulje toisiaan pois. Voit pitää Torin aktiivisena anonymisoitua käyttöä tai tiettyjä palveluja varten ja käyttää Tailscalea päivittäin sen yksinkertaisuuden vuoksi. Kummassakaan tapauksessa sinun ei tarvitse avata porttia reitittimessäsi, mikä vahvistaa turvallisuutta.



### Nostr-releen suojaaminen (suositellut käytännöt)



Jos isännöit Nostr-releetä Umbrelissa, erityisesti edistyneessä kontekstissa, muista noudattaa muutamia hyviä käytäntöjä:





- Yksityinen tai rajoitettu rele:** Oletusarvoisesti Umbrel-releesi on yksityinen (ei julkisesti ilmoitettu), ja jos käytät sitä vain Tailscalen tai lähiverkkosi kautta, se pysyy vieraiden ulottumattomissa. **Pitäkää linkki luottamuksellisena ** Älä lähetä sitä julkisiin Nostr-verkkoihin, ellet halua vapaaehtoisesti isännöidä muita käyttäjiä, mikä on aivan toinen asia (moderointi, kaistanleveys jne.). Henkilökohtaisessa käytössä suosittelemme rajoittamaan pääsyn itsellesi ja tarvittaessa muutamalle luotettavalle ystävälle ja perheelle.





- Whitelist / Auth**: NIP-42**-todennusmekanismia sekä julkisten avainten _valkoluetteloita_. Ottamalla nämä vaihtoehdot käyttöön voit rajoittaa relettäsi niin, että se **hyväksyy vain tietyillä avaimilla (omillasi)** allekirjoitettuja tapahtumia tai että asiakkaiden on todennettava itsensä julkaistakseen. tämän asettaminen vaatii releen `config.toml`-konfigurointitiedoston muokkaamista Umbrelissa (SSH:n kautta Docker-säiliössä). _ Se on edistynyt manipulointi, mutta voit esimerkiksi listata sallitut mainokset (`pubkey_whitelist`). Näin vaikka joku löytäisi releesi, hän ei voi julkaista siellä mitään, jos hän ei ole listalla.





- Päivitykset ja ylläpito:** Pidä Umbrel ja _Nostr Relay_ -sovellus ajan tasalla. Päivitykset voivat sisältää suorituskykyparannuksia (esim. parempi roskapostin käsittely) ja tietoturvakorjauksia. Tarkista Umbrelissa App Storesta säännöllisesti _Nostr Relay_ -sovelluksen päivitykset ja käytä niitä tarvittaessa.





- Seuranta ja rajoitukset:** Pidä silmällä, miten relettäsi käytetään. Jos avaat sen muille, pidä silmällä Umbrelisi kuormitusta (CPU/RAM-tallennus), sillä releeseen voi nopeasti kertyä paljon dataa. nostr-rs-relay tarjoaa konfiguroitavissa olevat **nopeus- ja tallennusrajat** (`rajat` konfiguraatiossa, esim. tapahtumien määrä sekunnissa, tapahtumien maksimikoko, vanhojen tapahtumien tyhjennys...). Yksityisessä käytössä sinun ei luultavasti tarvitse koskea näihin, mutta ole tietoinen, että nämä parametrit ovat olemassa, jos tarvitset niitä ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Nostr-avainten suojaaminen:** Tämä kohta on jo mainittu, mutta se on ratkaisevan tärkeä: älä koskaan syötä Nostr-avainta Interface:ään, johon et täysin luota. Käytä sen sijaan selainlaajennuksia tai ulkoisia laitteita (kuten erillisissä puhelimissa olevia Nostr- _signaattoreita_) arkaluontoisten toimintojen allekirjoittamiseen. Umbrelissa verkko-ohjelmasi, kuten _Snort_ ja _noStrudel_, voivat toimia NIP-07:n kautta tietämättä salaista avaintasi. Hyödynnä tätä mahdollisuutta yhdistää mukavuus ja turvallisuus.




Kun noudatat näitä vinkkejä, Umbrel-solmun ja Nostrin integroinnista tulee sekä tehokas **että** turvallinen. Sinulla on täydellinen ympäristö: Bitcoin-solmu Lightning-maksuja varten, yksityinen Nostr-rele tietojen riippumattomuutta varten ja suorituskykyiset Nostr-verkkoasiakkaat, joiden avulla voit navigoida tässä uudessa hajautetussa sosiaalisessa verkostossa. Nauti Nostrin tutkimisesta Umbrelin kanssa!