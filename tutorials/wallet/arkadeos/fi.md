---
name: ArkadeOS
description: Täydellinen opas Arkade-portfolioon ja Ark-protokollaan
---

![cover](assets/cover.webp)



Bitcoin-verkolla on edessään suuri haaste: skaalautuvuus. Vaikka pääkerros (kerros 1) tarjoaa vertaansa vailla olevaa turvallisuutta ja hajautusta, se pystyy käsittelemään vain rajallisen määrän tapahtumia sekunnissa. Lightning Network on noussut lupaavaksi toisen kerroksen (layer 2) ratkaisuksi, joka mahdollistaa nopeat ja edulliset maksut. Lightning asettaa kuitenkin omat rajoituksensa: kanavanhallinta, tarve saada likviditeettiä ja tekninen monimutkaisuus, joka saattaa karkottaa uudet käyttäjät.



Tämä on **Ark**:n tausta, joka on uusi layer 2 -protokolla, joka on suunniteltu tarjoamaan yksinkertaisempi käyttäjäkokemus ilman, että suvereniteetti kärsii. **ArkadeOS** (tai Arkade) on tämän protokollan ensimmäinen merkittävä toteutus, joka tarjoaa seuraavan sukupolven Bitcoin-salkun.



Tämä opetusohjelma opastaa sinut Arkaden maailmaan. Tutustumme siihen, miten Ark-protokolla toimii, miten asennat ja konfiguroit Arkade wallet:n ja miten voit käyttää sitä bitcoinien lähettämiseen ja vastaanottamiseen välittömästi, luottamuksellisesti ja ilman tavanomaisia Lightning Network:n kitkaa.



## Arkin protokollan ymmärtäminen



Ennen kuin pääset tutustumaan Arkaden käyttöön, on olennaista ymmärtää Ark-protokollan keskeiset käsitteet, jotka ohjaavat sitä. Ark ei ole erillinen lohkoketju, vaan Bitcoin:n päällä oleva älykäs koordinointimekanismi.



### VTXO-konsepti


Arkin ytimessä on **VTXO** (Virtual UTXO). VTXO on UTXO, jota ei ole vielä julkaistu Bitcoin-lohkoketjussa: se on olemassa pääketjun (off-chain) ulkopuolella, mutta sen tukena on lohkoketjussa valmiiksi allekirjoitettuja transaktioita.



Toisin kuin keskitetyssä pörssissä oleva saldo, VTXO todella kuuluu sinulle. Sinulla on hallussasi kryptografinen todiste, jonka avulla voit milloin tahansa vaatia vastaavat todelliset bitcoinit lohkoketjuun, vaikka Ark-palvelin katoaisi. VTXO:iden avulla voit siirtää arvoa välittömästi käyttäjien välillä odottamatta lohkovahvistuksia.



### ASP:n (Ark-palveluntarjoajan) asema


Ark-protokolla toimii asiakas-palvelin-mallilla. Palvelimen nimi on **ASP** (Ark Service Provider). ASP:llä on kapellimestarin rooli:




- Se tarjoaa verkolle tarvittavan likviditeetin.
- Se koordinoi käyttäjien välisiä tapahtumia.
- Se järjestää selvityskierroksia lohkoketjussa.



On tärkeää huomata, että ASP on **ei huoltajuutta**. Se ei koskaan pidä hallussaan yksityisiä avaimiasi, eikä se voi varastaa varojasi. Sen rooli on puhtaasti tekninen ja logistinen. Jos ASP sensuroi tapahtumasi tai kaatuu, voit aina palauttaa varasi yksipuolisen poistumismenettelyn kautta.



### Kierrokset ja yksityisyys


Arkissa tapahtuvat maksutapahtumat viimeistellään erissä, joita kutsutaan nimellä **Rounds**. Ajoittain (esim. muutaman sekunnin välein) ASP kerää kaikki vireillä olevat transaktiot ja ankkuroi ne Bitcoin-lohkoketjuun yhdeksi optimoiduksi transaktioksi.


Tällä mekanismilla on kaksi merkittävää etua:




- Skaalautuvuus**: Yksi on-chain-tapahtuma voi validoida tuhansia off-chain-maksuja, mikä alentaa merkittävästi käyttäjien kustannuksia.
- Luottamuksellisuus**: Jokainen kierros toimii **CoinJoin**. Kaikkien osallistujien varat sekoitetaan yhteiseen pooliin ennen kuin ne jaetaan uudelleen uusina VTXO:ina. Tämä katkaisee lähettäjän ja vastaanottajan välisen yhteyden, jolloin ulkopuolisen tarkkailijan on erittäin vaikeaa, ellei mahdotonta, jäljittää maksuja.



## ArkadeOS-esittely



ArkadeOS on konkreettinen sovellus, joka tuo Ark-protokollan suuren yleisön saataville. Se on Ark Labsin kehittämä täydellinen ekosysteemi, joka koostuu portfoliosta (Wallet), palvelimesta (Operator) ja kehittäjätyökaluista.



Loppukäyttäjän kannalta Arkade on tyylikäs ja intuitiivinen wallet (PWA - Progressive Web App). Se kätkee VTXO:iden ja kierrosten kryptografisen monimutkaisuuden tutun käyttöliittymän taakse. Arkaden avulla sinulla on osoite vastaanotettavaksi, painike lähetettäväksi ja tapahtumahistoria, aivan kuten klassisessa wallet:ssä, mutta Arkaden välittömyyden ja luottamuksellisuuden voimalla.



## Asennus ja konfigurointi



Koska Arkade on progressiivinen verkkosovellus, se on erityisen helppo asentaa, eikä siihen välttämättä tarvita perinteisiä sovelluskauppoja.



### Pääsy ja asennus


Voit käyttää Arkadea suoraan millä tahansa nykyaikaisella verkkoselaimella (Chrome, Safari, Brave) tietokoneella tai matkapuhelimella.





- Käy hakemuksen virallisella verkkosivustolla: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Sinua tervehtii joukko esittelynäyttöjä, joissa esitellään Arkaden keskeiset käsitteet: Bitcoin:n uusi ekosysteemi, itsesäilytyksen tärkeys ja erätransaktioiden edut.



![arkade onboarding](assets/fr/02.webp)





- Androidissa (Chrome/Brave)** : Paina selainvalikkoa (kolme pistettä) ja valitse "Asenna sovellus" tai "Lisää aloitusnäyttöön".
- IOS:ssä (Safari)**: Paina jakopainiketta (neliö, jossa on nuoli ylöspäin) ja valitse "Aloitusnäytössä".



Kun Arkade on asennettu, se käynnistyy kuin natiivisovellus, koko ruudun kokoisena ja ilman osoitepalkkia.



### Portfolion luominen


Ensimmäisellä käynnistyskerralla sinua pyydetään määrittämään salkkusi.





- Napsauta **"Create New Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet luodaan välittömästi. Toisin kuin perinteiset Bitcoin-lompakot, **Arkade ei käytä 12- tai 24-sanaisia palautuslauseita**. Sen sijaan Arkade luo automaattisesti **yksityisen avaimen** Nostr (nsec) -muodossa, jota käytetään wallet:n varmuuskopiointiin ja palauttamiseen. Muista tallentaa tämä avain välittömästi (katso seuraava kohta).





- Näyttöön tulee "Uusi wallet on toiminnassa!" -näyttö, joka vahvistaa, että wallet on käyttövalmis. Pääset pääkäyttöliittymään napsauttamalla **"GO TO WALLET "**.



Kun olet wallet:ssä, pääset Arkaden pääkäyttöliittymään. Täältä löydät saldosi, painikkeet varojen lähettämistä ja vastaanottamista varten sekä "Sovellukset"-välilehden, jonka kautta pääset käyttämään integroituja sovelluksia, kuten Boltz (Lightning-pörssi), LendaSat ja LendaSwap (lainauspalvelut) sekä Fuji Money (synteettiset varat).



![wallet interface](assets/fr/04.webp)



### Yhteys ASP:hen


Oletusarvoisesti salkku on määritetty automaattisesti muodostamaan yhteys Arkade Labsin viralliseen ASP. Voit tarkistaa, mihin palvelimeen olet yhteydessä menemällä kohtaan **Asetukset** > **Tietoja**, jossa näet palvelimen osoitteen (tällä hetkellä `https://arkade.computer`).



Arkaden nykyisessä versiossa (Beta) ASP-palvelinta ei voi muokata manuaalisesti. Sovellus muodostaa automaattisesti yhteyden Arkade Labsin viralliseen ASP-palvelimeen. Tulevaisuudessa käyttäjät voivat ehkä valita eri ASP-palvelimien välillä mieltymystensä mukaan, mutta tämä ominaisuus ei ole vielä käytettävissä.



### Yksityisen avaimen varmuuskopiointi


**Arkade käyttää Nostr (nsec) -muodossa olevaa yksityistä avainta varmuuskopiointi- ja palautusmenetelmänä. Voit varmuuskopioida yksityisen avaimen :





- Siirry päänäytöstä kohtaan **Asetukset**.
- Valitse **"Varmuuskopiointi ja yksityisyys "**.
- Näet **yksityisen avaimesi** näkyvän muodossa `nsec...`. Tämä pitkä merkkijono on ainoa keino palauttaa wallet.
- Paina **"COPY NSEC TO CLIPBOARD "** kopioidaksesi yksityisen avaimesi.
- Säilytä tämä avain turvallisessa paikassa**: kirjoita se paperille, säilytä sitä turvallisessa salasanahallinnassa tai käytä muuta sinulle sopivaa varmuuskopiointimenetelmää.
- Arkade tarjoaa myös vaihtoehdon **"Enable Nostr backups "**. Tämä ominaisuus käyttää Nostr-protokollaa (hajautettu verkko) varmuuskopioidakseen automaattisesti tietyt tiedot wallet:sta salatussa muodossa Nostr-releisiin. Tämä helpottaa synkronointia useiden laitteiden välillä ja helpottaa wallet:n tilan palauttamista.



**Tärkeää**: Nostr-varmistukset ovat vain **mukavuus** ominaisuus. Ne eivät korvaa nsec-avaimen varmuuskopiointia. Nostr-releet eivät takaa tietojen pysyvää tallentamista. Yksityinen nsec-avaimesi on edelleen ainoa taattu keino saada rahasi takaisin.



![backup private key](assets/fr/05.webp)




## Arkaden käyttäminen



Kun olet asentanut wallet:n, olet valmis tutkimaan Arkaden ominaisuuksia. Käyttöliittymä on suunniteltu yhdistämään eri Bitcoin-maksutyypit (On-chain, Lightning, Ark) saumattomasti.



### Varojen vastaanottaminen



Jos haluat rahoittaa salkkusi, paina **"Vastaanota "**. Arkade tarjoaa kolme vastaanottotapaa:





- Ark-maksu**: Jos lähettäjä käyttää myös Arkadea, jaa Ark-osoitteesi välitöntä, luottamuksellista ja lähes ilmaista siirtoa varten.
- Ketjussa oleva talletus (täysihoito)**: Käytä Bitcoin-osoitetta (`bc1p...`) vastaanottaa klassisesta wallet:sta tai vaihdosta. Odota vahvistusta (~10 min), ennen kuin varat muunnetaan VTXOiksi.
- Salamavaihto**: Luo Lightning-lasku ja maksa se ulkoisesta wallet Lightningista. Varat saapuvat välittömästi automaattisen swapin kautta.



![receive amount](assets/fr/06.webp)



Kuittinäytössä näkyvät kaikki käytettävissä olevat vaihtoehdot: QR-koodi, Ark-osoite, Bitcoin (BIP21) -osoite ja Lightning-lasku. Lightning-maksuja varten pidä sovellus auki tapahtuman aikana.



![receive confirmation](assets/fr/07.webp)



### Varojen lähettäminen



Jos haluat lähettää varoja, paina **"Lähetä "** ja liitä vastaanottajan osoite tai skannaa QR-koodi. Arkade tunnistaa automaattisesti vaaditun maksutyypin:





- Ark**-maksu: Ark-osoitteeseen, siirto on välitön, yksityinen ja lähes ilmainen (0 SATS-maksu). Vastaanottajan ei tarvitse olla verkossa.
- Salama** maksu: Skannaa Lightning-lasku (`lnbc...`) ja Arkade suorittaa automaattisesti vaihdon. ASP maksaa laskun puolestasi ja veloittaa Arkade-saldoasi.
- Ketjumaksu**: `bc1q...` tai `bc1p...`), Arkade käynnistää "Collaborative Output", joka sisällytetään seuraavaan on-chain-kierrokseen.



Tarkista tiedot "Allekirjoita maksutapahtuma" -näytöltä ja vahvista sitten painamalla **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Nykyinen rajoitus (Beta)**: VTXO:ta, jotka on luotu alle 24 tuntia sitten, ei voi käyttää on-chain-lähdöissä. Jos havaitset virheen, odota, kunnes VTXO:t ovat "kypsiä".



**on-chain:n lähdön luottamuksellisuus**: Ark output transaction on mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Havaitsemme hajautetun syötteen neljään eri lähtöön, kuten CoinJoin:ssa. Ulkopuolisen tarkkailijan on mahdotonta määrittää, mikä määrä kuuluu millekin käyttäjälle.



![transaction ark mempool](assets/fr/11.webp)



## Lisäominaisuudet



### VTXO:n voimassaolon päättymisen hallinta


Ark-protokollan teknisenä ominaisuutena on, että VTXO:lla on **rajoitettu käyttöikä**. Tämä aikarajoitus on protokollan suunnittelun luontainen piirre. Vanhentumisaika on määritettävissä kullakin ASP-palvelimella; Arkade Labsin virallisella ASP-palvelimella tämä aika on noin **4 viikkoa (≈30 päivää)**.



**Tämän rajoituksen ansiosta Ark-palvelin voi tehokkaasti hallita likviditeettiä ja siivota VTXO:t inaktiivisilta käyttäjiltä. Vanhentumisen jälkeen Ark-palvelin voi teknisesti vaatia VTXO-puussa jäljellä olevat varat.



**Jotta VTXO:t pysyvät aktiivisina, ne on "päivitettävä" ennen niiden vanhentumista. Päivittäminen tarkoittaa osallistumista uuteen "kierrokseen", jossa vanhentumassa olevat VTXO:t vaihdetaan uusiin VTXO:ihin, joilla on uusi täysi voimassaoloaika (≈ 30 päivää Arkade Labs ASP:ssä).



Arkade-salkku hallitsee tätä prosessia automaattisesti: sovellus valvoo jatkuvasti VTXO:iden tilaa ja päivittää ne automaattisesti muutamaa päivää ennen niiden vanhentumista. Kunhan avaat sovelluksen säännöllisesti (vähintään kerran viikossa), VTXO:t pysyvät automaattisesti aktiivisina.



**Jos et avaa salkkuasi yli 4 viikkoon, VTXO:t vanhenevat. Et kuitenkaan menetä varojasi: sinulla on mahdollisuus saada ne takaisin **epäselvällä irtautumisella** (ks. seuraava kohta). Tämä menettely on kalliimpi ja hitaampi, mutta sillä varmistetaan, että varasi ovat edelleen käytettävissä.



Tarve avata sovellus säännöllisesti tekee Arkadesta **"Hot Wallet"**, joka on suunniteltu päivittäiseen rahankäyttöön, ei kassakaappiin pitkän aikavälin säästämiseen. Jos haluat säilyttää bitcoineja käyttämättä niitä pitkiä aikoja, suosi kylmää wallet-laitteistoa.



**Tarkista VTXO:iden tila**: Asetukset** > **Lisäasetukset**: Voit seurata VTXO:iden tilaa kohdassa **Asetukset** > **Lisäasetukset**. Katso "Seuraava uusiminen" nähdäksesi, milloin seuraava automaattinen uusiminen tapahtuu, ja "Virtuaalikolikot" nähdäksesi yksityiskohtaisen luettelon kaikista VTXO:eistasi ja niiden päättymispäivästä.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (yksipuolinen poistuminen)



Yksipuolinen poistuminen on Ark-protokollan **perusluonteinen kryptografinen takuu**, joka takaa, että saat rahasi takaisin, vaikka ASP katoaisi, sensuroisi tapahtumasi tai kieltäytyisi yhteistyöstä. Teknisesti ottaen VTXO:t ovat **esimerkittyjä Bitcoin-tapahtumia**, jotka omistat. Ehdottomassa hätätilanteessa voit lähettää nämä transaktiot Bitcoin-lohkoketjuun ja saada rahasi takaisin ilman kenenkään lupaa.



**Miten se toimii? Prosessi tapahtuu kahdessa vaiheessa. Ensimmäinen vaihe on **purkaminen**: lähetät peräkkäin VTXO:t muodostavat esisignoidut transaktiot transaktiopuuhun. Sitten **Finalisointi**: kun aikarajat ovat umpeutuneet (yleensä 24 tuntia), keräät bitcoinisi vakio-osoitteesta.



**Tämänhetkinen tilanne Arkadessa**: Arkade: Beta-versiossa ei ole vielä painiketta tai yksinkertaista käyttöliittymää yksipuolista tulostusta varten. Tämä toiminnallisuus edellyttää tällä hetkellä Arkade SDK:n käyttöä ja teknistä osaamista TypeScript-ohjelmoinnista.



**Kaikkakin menettely ei ole käytettävissä napin painalluksella, kryptografinen takuu on olemassa. VTXO:si sisältävät ennalta allekirjoitettuja tapahtumia, jotka kuuluvat laillisesti sinulle. Juuri tämä tekninen takuu tekee Arkista **ei-oikeudellisen** protokollan: jopa pahimmassa tapauksessa rahasi ovat teknisesti palautettavissa. Arkaden tuleviin versioihin lisätään todennäköisesti yksinkertaistettu käyttöliittymä.



## Edut ja rajoitukset



Jotta Arkade saataisiin oikeaan kontekstiin, tehdään yhteenveto sen nykyisistä vahvuuksista ja heikkouksista.



### Kohokohdat




- Käyttäjäkokemus (UX)**: Ei kanavien hallintaa, saapuvaa kapasiteettia tai monimutkaisia kanavien varmuuskopioita kuten Lightningissa. Asenna ja käytä.
- Yksityisyys** : Oletusarvoinen CoinJoin-arkkitehtuuri tarjoaa paljon korkeamman tason anonymiteettiä kuin tavalliset on-chain- tai Lightning-tapahtumat.
- Yhteentoimivuus**: Maksa millä tahansa Bitcoin QR-koodilla (On-chain tai Lightning) yhdestä käyttöliittymästä.



### Rajoitukset




- Nuori protokolla**: Ark on hyvin uusi teknologia. Virheitä voi olla. Arkia ei kannata käyttää sellaisten summien tallentamiseen, joiden häviäminen olisi kriittistä.
- ASP-riippuvuus**: Vaikka järjestelmä ei ole riippuvainen huoltajuudesta, sen sujuvuus riippuu ASP:n saatavuudesta. Jos liitännäispalveluntarjoaja on offline-tilassa, et voi enää tehdä välitöntä liiketoimintaa (voit vain tulostaa on-chain-varojasi).
- Vain Hot Wallet** : Tarve avata sovellus säännöllisesti VTXO:iden päivittämiseksi ei sovellu kylmävarastointiin (Cold Storage).



## Vertailu: Arkade vs Lightning vs Cashu



Jotta ymmärtäisimme paremmin Arkaden asemaa, verrataan sitä kahteen muuhun merkittävään skaalautuvuusratkaisuun.




| Kriteeri | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Malli** | Palvelimen (ASP) koordinoima jaettu UTXO | Maksukanavien P2P-verkko | Pankin (Mint) myöntämät sokeat poletit |
| **Säilytys** | **Ei-säilytyksellinen** (avaimet ovat sinulla) | **Ei-säilytyksellinen** (avaimet ovat sinulla) | **Säilytyksellinen** (Mintillä on varat) |
| **Yksityisyys** | **Korkea** (Natiivi CoinJoin, sokea yleisölle) | **Keskitaso** (Sipulireititys, mutta kanavat näkyvissä) | **Erittäin korkea** (Sokea jopa Mintille) |
| **Skaalautuvuus** | Erinomainen (Massiivinen on-chain batching) | Erinomainen (Loputtomat off-chain transaktiot) | Erinomainen (Yksinkertaiset palvelin-allekirjoitukset) |
| **Kokemus** | Yksinkertainen (lähellä on-chain-lompakkoa) | Monimutkainen (kanavien hallinta, likviditeetti) | Erittäin yksinkertainen (kuin digitaalinen käteinen) |
| **Pääriski** | ASP:n saatavuus & Vanheneminen | Kanavien hallinta & Varmuuskopiot | Luottamus Minttiin (varkausriski) |

**Arkade** on ihanteellinen kompromissi: Cashun yksinkertaisuus ja luottamuksellisuus, mutta Lightningin suvereenius (ei-hallinnollinen).



## Tuki ja apu



Jos sinulla on ongelmia tai kysymyksiä Arkadea käyttäessäsi, sovellus tarjoaa useita tukivaihtoehtoja:





- Mene kohtaan **Asetukset** > **Tuki**.
- Löydät useita vaihtoehtoja:
  - Asiakastuki**: Hanki apua salkkuusi, ilmoita virheistä tai kysy kysymyksiä.
  - Turvallinen chat**: Keskustelusi ovat turvallisia ja yksityisiä, ja historia säilyy istuntojen välillä.
  - Vikailmoitukset**: Ilmoita kohtaamistasi ongelmista ja niiden toistamiseen tarvittavista toimista.
  - Seuraa edistymistä**: Seuraa jatkuvasti tukilippujasi ja keskustelujasi.



![support](assets/fr/10.webp)



Arkade-tiimi on aktiivinen myös Telegramissa @arkade_os-kanavalla tuen ja integrointimahdollisuuksien osalta.



## Tärkeä huomautus: Sovellus on beta-vaiheessa



**⚠️ Arkade on tällä hetkellä julkisessa beta-versiossa mainnet Bitcoin:ssä**. Vaikka sovellus toimii oikeilla bitcoineilla, on tärkeää noudattaa tiettyjä varotoimenpiteitä.



### Käyttösuositukset




- Käytä pieniä määriä**: Vältä suurten summien tallentamista Arkadeen. Käytä tätä wallet:ää päivittäisiin menoihin ja pidä säästösi kylmässä wallet-laitteistossa.
- Mahdolliset viat ja rajoitukset**: Arkade saattaa sisältää virheitä tai odottamatonta käyttäytymistä, kuten mikä tahansa sovellus, jota kehitetään aktiivisesti. Ilmoita mahdollisista ongelmista integroidun tuen kautta.
- Nopea kehitys** : Sovellusta ja protokollaa parannetaan jatkuvasti. Joitakin ominaisuuksia voidaan muuttaa tai lisätä tulevissa versioissa.



### Nykyiset tunnetut rajoitukset




- 24 tunnin viive VTXO:ssa** : Uusia VTXO:ita ei voi käyttää välittömästi on-chain-lähtöihin.
- ASP unique**: ASP-palvelimen vaihtaminen sovelluksessa ei ole vielä mahdollista.
- Tekninen yksipuolinen tuotos**: Yksinkertaistettua käyttöliittymää yksipuoliselle ulostulolle ei vielä ole (vaatii SDK:n).



Arkade Labsin tiimi työskentelee aktiivisesti näiden rajoitusten lieventämiseksi tulevissa versioissa.



## Päätelmä



ArkadeOS on merkittävä läpimurto Bitcoin-ekosysteemissä. Toteuttamalla Ark-protokollan se osoittaa, että on mahdollista sovittaa yhteen helppokäyttöisyys ja Bitcoin:n perusperiaatteet: älä luota, vaan tarkista.



Vaikka Arkade on vielä lapsenkengissään, se tarjoaa kiehtovan välähdyksen siitä, miltä Bitcoin-maksujen tulevaisuus voisi näyttää: välittömältä, yksityiseltä ja kaikkien ulottuvilla olevalta ilman teknisiä ennakkoedellytyksiä. Se on täydellinen työkalu päivittäisiin menoihisi ja täydentää turvallista säästöratkaisuasi (Cold Wallet).



Kannustamme sinua testaamaan Arkadea pienillä määrillä, jotta voit tutustua tähän uuteen protokollaan itse. Ekosysteemi kehittyy nopeasti, ja Arkade on tämän innovaation eturintamassa.



## Resurssit



Lisätietoja saat virallisista lähteistä:





- Arkade** verkkosivusto: [arkadeos.com](https://arkadeos.com)
- Dokumentaatio**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark**-protokolla: [ark-protocol.org](https://ark-protocol.org)
- Lähdekoodi** : [GitHub Arkade](https://github.com/arkade-os)