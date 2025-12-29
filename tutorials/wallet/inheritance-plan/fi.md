---
name: Perintösuunnitelma Bitcoin
description: Miten siirtää bitcoineja rakkaillesi?
---

![cover](assets/cover.webp)



Bitcoinien siirtäminen on suuri tekninen haaste, jonka monet haltijat jättävät huomiotta. Toisin kuin perinteiset pankkitalletukset, joissa rahoituslaitos voi siirtää varat oikeille omistajille, Bitcoin toimii ilman välikäsiä. Läheisesi eivät koskaan pääse käsiksi varoihisi ilman tarvittavia teknisiä tietoja, riippumatta niiden laillisuudesta.



Tämä opetusohjelma opastaa sinua teknisen perintösuunnitelman laatimisessa. Opit, miten on-chain:n automaattisen siirtämisen mekanismit toimivat, miten dokumentoida määritykset ja miten valita oikeat ratkaisut, jotta Bitcoin-perintösi pysyy läheistesi saatavilla.



## Miksi tekninen perintösuunnitelma on välttämätön



Bitcoin perustuu salauksen perusperiaatteeseen: se, jolla on yksityiset avaimet, hallitsee varoja. Tästä määräysvallasta tulee suuri haavoittuvuus, kun haltija katoaa lähettämättä tarvittavia tietoja.



Bitcoin-perintösuunnitelman on täytettävä kaksi näennäisesti ristiriitaista tavoitetta: antaa läheisillesi mahdollisuus käyttää varojasi, kun aika koittaa, ja estää samalla muita saamasta niitä ennenaikaisesti. Tämä herkkä tasapaino perustuu Bitcoin:n omiin ohjelmointiominaisuuksiin.



Tekninen monimutkaisuus lisää vaikeuksia. Perillisesi joutuvat käsittelemään sellaisia käsitteitä kuin palautuslauseita, salkun kuvaajia tai johdannaispolkuja. Ilman riittävää valmistautumista jopa hyvää tarkoittava perillinen voi tehdä peruuttamattomia virheitä.



## Miten on-chain-perintö toimii



Bitcoin käyttää komentosarjakieltään menoehtojen koodaamiseen suoraan tapahtumiin. on-chain-perintö hyödyntää tätä ohjelmoitavuutta luodakseen vaihtoehtoisia palautusreittejä, jotka aktivoituvat automaattisesti.



### Timelocks



Aikalukot ovat Bitcoin:n periytymisen perusmekanismi. Niiden avulla varat voidaan lukita, kunnes tietty aikaehto täyttyy.



**CLTV (CheckLockTimeVerify)**: Tämä absoluuttinen aikalukko tarkistaa, että tietty aika (päivämäärä tai lohkon korkeus) on saavutettu ennen menon hyväksymistä. Esimerkiksi "nämä varat voidaan käyttää vasta lohkon 900000 jälkeen" tai "1. tammikuuta 2026 jälkeen". CLTV:n etuna on se, että se sallii pitkät viiveet (useita vuosia), mutta päivämäärä on kiinteä ja sitä sovelletaan identtisesti kaikkiin salkun UTXO-varoihin. Jos haluat säilyttää varojen hallinnan, sinun on määräajoin luotava uusi salkku, jossa on pidennetty päättymispäivä, ja siirrettävä varat siihen.



**CSV (CheckSequenceVerify)**: Tämä suhteellinen aikalukko tarkistaa, että tietty määrä lohkoja on kulunut UTXO:n luomisesta. Esimerkiksi "nämä varat voidaan käyttää vasta 52560 lohkoa (~1 vuosi) niiden vastaanottamisesta". CSV:n etuna on, että jokaisella UTXO:llä on oma itsenäinen laskurinsa. Joka kerta, kun suoritat tapahtuman, äskettäin luodut UTXO:t nollaavat oman aikarajansa. Tekninen 65535 lohkon (enintään ~15 kuukautta) raja rajoittaa kuitenkin mahdollisia aikarajoja. Tämä lähestymistapa on luonnollisempi jokapäiväisessä käytössä, koska normaali toimintasi siirtää määräaikoja automaattisesti taaksepäin.



### Useita kulutuspolkuja



Perintösalkussa yhdistyvät useat kulutusvaihtoehdot kussakin osoitteessa:





- Pääpolku** : Omistaja voi käyttää varojaan milloin tahansa pääavaimella ilman aikarajoituksia.
- Elvytyspolku(t)**: Yksi tai useampi vaihtoehtoinen avain voi käyttää varoja vasta tietyn ajan kuluttua.



Jokainen omistajan suorittama transaktio "päivittää" UTXO:n ja luo uusia ulostuloja, joiden aikarajat nollataan. Tämä mekanismi varmistaa, että niin kauan kuin omistaja on aktiivinen, palautuspolut eivät koskaan aktivoidu.



### Miniskripti ja Taproot



**Miniscript** on Andrew Poelstran, Pieter Wuillen ja Sanket Kanjalkarin kehittämä strukturoitu kieli, jonka avulla on helppo kirjoittaa ja analysoida monimutkaisia Bitcoin-skriptejä. Sen avulla voit laatia luettavia ja todennettavissa olevia menoehtoja, jotka ovat välttämättömiä perintökonfiguraatioille, joihin liittyy useita avaimia ja aikalukkoja.



**Taproot** (aktivoidaan marraskuussa 2021) parantaa on-chain:n perintöä merkittävästi. Sen puurakenteen (MAST) ansiosta lohkoketjusta paljastuu vain käytetty menoehto. Jos omistaja käyttää varansa normaalisti, perintöehdot pysyvät näkymättömissä. Tämä luottamuksellisuus vähentää myös monimutkaisten polkujen transaktiokustannuksia.



## Kuvaajien ratkaiseva merkitys



Vanhojen salkkujen osalta elvytyslauseke (seed) ei riitä palauttamaan varojen saatavuutta. Kriittiseksi tekijäksi tulee **kuvaaja**.



Kuvaaja on merkkijono, joka kuvaa tyhjentävästi salkun rakenteen: mukana olevat julkiset avaimet, käyttöehdot, derivointireitit ja konfiguroidut aikarajat. Tässä on yksinkertaistettu esimerkki:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Tässä kuvaajassa sanotaan: "Joko pääavain voi käyttää välittömästi tai palautusavain voi käyttää 52560 lohkon jälkeen".



Puretaanpa tämä esimerkki:




- `wsh()` : Witness Script Hash, osoittaa osoitetyypin (P2WSH)
- or_d()`: "or"-ehto oletushaaralla
- pk([sormenjälki/polku]xpub...)`: Julkinen pääavain, sen sormenjälki ja johdannaispolku
- and_v()`: "ja"-ehto, joka yhdistää palautusavaimen ja aikalukon
- "vanhempi(52560)`: 52560 lohkon suhteellinen aikalukko



** Ilman kuvaajaa perillisesi eivät pysty palauttamaan salkkua, vaikka he käyttäisivät kaikkia palautuslauseita.** Vakiosalkku voidaan palauttaa vain seed:sta, koska se noudattaa standardoituja johdannaispolkuja (BIP44, BIP84). Perinteinen salkku sen sijaan käyttää räätälöityjä skriptejä, joita ei voi arvata. Kuvaajan varmuuskopion (tai ohjelmiston viemän konfigurointitiedoston) on oltava perintäsuunnitelmassa olevien palautuslausekkeiden mukana.



## Perintösuunnitelman dokumentaariset osat



Teknisten mekanismien lisäksi tehokas perintösuunnitelma perustuu kolmeen dokumentointipilariin.



### Perintökirje



Tämä henkilökohtainen kirje on suunnitelmasi lähtökohta. Se on kirjoitettu perillisille, ja siinä selitetään asiayhteys ja varotoimet.



Kirjeessä on oltava selkeät turvallisuussäännöt:




- Älä kiirehdi, ota aikaa oppia ennen kuin siirrät varoja
- Älä koskaan ilmoita täydellistä toipumislausetta yhdelle henkilölle
- Älä koskaan kirjoita palautuslausetta tarkistamattomaan ohjelmistoon tai tietokoneeseen
- Varo huijauksia ja pyytämätöntä apua tarjoavia henkilöitä
- Kysy neuvoa vähintään kahdelta luotettavalta henkilöltä ennen päätöksentekoa



Kirjeessä on myös notaarin yhteystiedot ja testamenttisi sijainti. Se ei saa koskaan sisältää palautuslauseita tai salasanoja.



### Luotettavien yhteystietojen hakemisto



Yhdenkään perillisen ei pitäisi kohdata bitcoinin talteenottoa yksin. Tässä hakemistossa luetellaan henkilöitä, jotka voivat tarjota teknistä tai oikeudellista apua.



Kirjoita jokaisesta yhteyshenkilöstä seuraavat tiedot: täydellinen nimi, suhde sinuun, rooli suunnitelmassa, luottamuksen taso, Bitcoin-taidot ja täydelliset yhteystiedot. Perussääntö: perillisten on aina kuultava vähintään kahta eri henkilöä ennen kuin he tekevät tärkeitä päätöksiä.



### Bitcoin omaisuusluettelo



Tässä osiossa kartoitetaan kaikki bitcoinisi ja niiden palauttamiseen tarvittavat tekniset tiedot.



Kunkin salkun osalta dokumentoidaan :




- Portfoliotyyppi**: laitteisto, ohjelmisto, kokoonpano (single-sig, multisig, legacy)
- Laitteen sijainti**: wallet-laitteiston fyysinen sijainti
- Descriptor/konfigurointitiedoston sijainti**: kriittinen edistyneille salkuille
- Elvytyslausekkeen sijainti**: erillään kuvaajasta
- Pääsykoodit**: PIN-koodit ja salasanat tallennetaan
- Konfiguroidut viiveet**: kun palautuspolut aktivoituvat



## Saatavilla olevat tekniset ratkaisut



Useat ohjelmistopaketit toteuttavat on-chain-perintämekanismeja. Jokaisella on omat tekniset ominaisuutensa.



### Liana



Liana on työpöytäohjelmisto (Linux, macOS, Windows), joka käyttää Miniscriptiä portfolioiden luomiseen ajoitetuilla palautuspoluilla. Projektin on kehittänyt Wizardsardine, jonka perustajana on Antoine Poinsot (Bitcoin:n ydintekijä).



**Tekninen arkkitehtuuri**: Liana luo oletusarvoisesti P2WSH-salkkuja (SegWit natiivi), ja Taproot-tuki on saatavilla wallet-laitteiston yhteensopivuudesta riippuen. Arkkitehtuuri perustuu pääpolkuun ja yhteen tai useampaan palautuspolkuun. Luodussa kuvaajassa koodataan kaikki ehdot, ja se on tallennettava.



**Käytetyt aikalukot**: Rajoitettu 65535 lohkoon (~15 kuukautta). Hallinnan säilyttämiseksi sinun on suoritettava päivitystapahtuma ennen aikalukon päättymistä.



**Hardware wallet -integraatio**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY ja muut laitteet ovat yhteensopivia tapahtumien allekirjoittamiseen.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper on mobiilisovellus (iOS, Android), jossa yhdistyvät multisig- ja timelock-sovellukset "Enhanced Vaults" -palvelun avulla. Mobiilikäyttöön perustuva lähestymistapa ja integroitu opastus tekevät siitä helppokäyttöisen myös vähemmän teknisille käyttäjille.



**Tekninen arkkitehtuuri**: Enhanced Vaults käyttää Miniscriptiä luodakseen multisig-konfiguraatioita, joissa lisäavaimet aktivoituvat määriteltyjen viiveiden jälkeen. Perintöavain lisää olemassa olevaa khorumia, kun taas hätäavain voi ohittaa multisigin kokonaan.



**Käytetyt aikalukot**: Bitcoin Keeper käyttää absoluuttisia aikamittareita (CLTV), mikä mahdollistaa yli 15 kuukauden toimitusajat. Aktivointipäivämäärä asetetaan wallet:n luomisessa, ja se koskee kaikkia UTXO:ita. Sovelluksessa on "revaulting"-toiminto, joka hoitaa päivityksen automaattisesti: käyttäjä vain seuraa ohjattuja vaiheita, eikä hänen tarvitse luoda uutta wallet:tä manuaalisesti.



**Lisäominaisuudet**: Canary Wallets avainten vaarantumisen havaitsemiseksi ja päivitysmuistutukset: Integroidut perintöasiakirjat, Canary Wallets avainten vaarantumisen havaitsemiseksi ja päivitysmuistutukset.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Perintö



Heritage on työpöytäsovellus, joka käyttää Taproot-skriptejä perintöehtojen koodaamiseen. Taproot:n käyttö parantaa luottamuksellisuutta, koska käyttämättömät polut pysyvät näkymättömissä lohkoketjussa.



**Tekninen arkkitehtuuri**: Kukin perintöosoite sisältää pääreitin ja vaihtoehtoisia reittejä kullekin perijälle asteittain etenevin aikatauluin. Hierarkkisen rakenteen ansiosta henkilökohtainen varmuuskopio voidaan määritellä 6 kuukauden kuluessa ja perheen perilliset 12-15 kuukauden kuluessa.



**Käyttömuodot**: (ilmainen) tai hallinnoitu palvelu, joka lisää muistutuksia ja ilmoituksia perillisille (0,05 %/vuosi).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Perillisen toipumisprosessi



Elpymisprosessin ymmärtäminen auttaa laatimaan tehokkaan suunnitelman. Seuraavassa on lueteltu tekniset vaiheet, joita perillisen on noudatettava.



### Takaisinperintää koskevat vaatimukset



Perillinen tarvitsee :


1. ** Alkuperäisen portfolion kuvaus- tai konfiguraatiotiedosto** (JSON- tai tekstimuodossa ohjelmistosta riippuen)


2. **Itsen palautuslauseke** (perintöavaimeen liittyvä lauseke, yleensä 12 tai 24 sanaa)


3. **yhteensopiva ohjelmisto** (Liana, Bitcoin Keeper, Heritage tai Sparrow/Specter vakiokuvaajille)


4. **Yhteys Bitcoin**-solmuun aikalukon tilan tarkistamiseksi ja tapahtuman lähettämiseksi



### Elpymisen vaiheet



1. **Asenna ohjelmisto** suojatulle laitteelle ja määritä yhteys Bitcoin-verkkoon (henkilökohtainen solmu tai Electrum-palvelin)


2. **Importoi kuvaaja** salkun rakenteen uudelleenrakentamiseksi. Ohjelmisto generate automaattisesti kaikki käytetyt osoitteet


3. **Palauta perintöavain** palautuslauseesta. Ohjelmisto tarkistaa, että tämä avain vastaa yhtä kuvaajassa sallituista avaimista


4. **Synkronoi salkku** löytääksesi kaikki UTXO:t ja niiden käyttöehdot


5. **Tarkista aikalukon voimassaolon päättyminen**: ohjelmisto ilmoittaa kunkin UTXO:n osalta, onko palautuspolku aktiivinen


6. **Luo talteenottotapahtuma** osoitteeseen, jota perillinen hallitsee yksin (mieluiten uusi yksittäinen wallet)


7. **Allekirjoita ja lähetä** tapahtuma Bitcoin-verkossa



Jos aikarajoitus ei ole vielä päättynyt, perillisen on odotettava. Ohjelmisto näyttää päivämäärän tai lohkon, josta alkaen perintä on mahdollista. Tämän odotusajan aikana varat pysyvät turvassa lohkoketjussa.



### Perijän varalta seurattavat seikat



Perillisen on kiinnitettävä erityistä huomiota :




- Tarkista ladattujen ohjelmistojen aitous** (tarkistussummat, allekirjoitukset)
- Älä koskaan jaa toipumislausettasi** kenenkään apua tarjoavan kanssa
- Kysy neuvoa vähintään kahdelta luotettavalta henkilöltä** ennen kuin aloitat elvytyksen
- Siirtää varat yksinkertaiseen salkkuun**, jota hän hallitsee täysin toipumisen jälkeen



## Parhaat käytännöt



### Tietojen erottaminen



Älä koskaan säilytä kaikkia tietoja yhdessä paikassa. Kuvaaja on erotettava palautuslausekkeista, jotka puolestaan erotetaan PIN-koodeista. Tämä jako vaikeuttaa hyökkääjän pääsyä, mutta lailliset perilliset voivat silti palauttaa tiedot.



### Elvytystestit



Testaa koko palautusprosessi pienellä summalla, ennen kuin talletat huomattavia summia. Varmista, että voit palauttaa salkun kuvaajasta ja palautuslauseista tyhjällä laitteella. Dokumentoi vaiheet perillisiäsi varten.



### Timelock-huolto



Suunnittele aikarajojen päivittäminen hyvissä ajoin ennen niiden vanhentumista. Jos kyseessä on 12 kuukauden aikarajoitus, suorita tapahtuma 9-10 kuukauden välein. Ohjelmistot tarjoavat yleensä muistutuksia tai automaattisia päivitystoimintoja.



### Suunnitelman päivitys



Bitcoin-kokoonpanosi kehittyy. Jokainen merkittävä muutos (uusi salkku, määräaikojen muuttaminen, perijän lisääminen) on otettava huomioon dokumentaatiossasi. Ota käyttöön vuosittainen tarkistussuunnitelma.



## Lähestymistavan valinta



Valinta eri ratkaisujen välillä riippuu teknisestä profiilistasi ja erityistarpeistasi.



**Liana** sopii työpöytäkäyttäjille, jotka haluavat avoimen lähdekoodin ohjelmistoja, joita he voivat hallita täysin oman solmunsa kautta. Konfigurointi pysyy helposti saatavilla opastetun käyttöliittymän ansiosta. Suhteelliset aikarajat (CSV) yksinkertaistavat ylläpitoa, sillä normaali toimintasi siirtää automaattisesti määräaikoja taaksepäin. Rajoitus: maksimiviive noin 15 kuukautta (65535 lohkoa).



**Bitcoin Keeper** on suunnattu mobiilikäyttäjille, jotka etsivät intuitiivista käyttöliittymää ja integroituja liitännäisasiakirjoja. Sovellus tarjoaa kahdenlaisia erikoisavaimia: perintöavain (joka lisää päätösvaltaisuutta) ja hätäavain (joka ohittaa sen kokonaan). Absoluuttiset timelockit (CLTV) mahdollistavat yli 15 kuukauden läpimenoajat, ja integroitu revaulting-toiminto yksinkertaistaa päivitystä. Diamond Hands -suunnitelma avaa kehittyneet perintöominaisuudet.



**Perimä** on suunnattu teknisille käyttäjille, jotka arvostavat Taproot-luottamuksellisuutta ja hierarkkista periytymistä asteittaisilla viiveillä. Taproot:n puurakenne peittää perintöehdot normaalien tapahtumien aikana ja paljastaa vain palautuksen aikana käytetyn ehdon.



Kaikilla kolmella ratkaisulla on yksi yhteinen piirre: ne edellyttävät säännöllistä päivitystä, jotta palautuspolkujen ennenaikainen aktivointi voidaan estää. Tämä rajoitus on sekä on-chain:n epäluotettavan perinnön hinta että takuu. Suunnittele säännölliset muistutukset ja tee tästä ylläpidosta osa Bitcoin:n hallintarutiineja.



## Päätelmä



Teknisessä Bitcoin-perintösuunnitelmassa yhdistyvät salausmekanismit (timelockit, Miniscript, Taproot) ja tiukka dokumentointi. Kehittyneiden lompakoiden avulla voit lähettää bitcoinisi automaattisesti käyttämättömyyden jälkeen ilman kolmannen osapuolen väliintuloa.



Tärkeimmät perillisille luovutettavat elementit ovat: kuvaaja- tai konfiguraatiotiedosto, palautuslauseke, yksityiskohtaiset palautusohjeet ja pätevien henkilöiden yhteystiedot, jotka voivat auttaa perillisiä.



Aloita valitsemalla profiiliisi sopiva tekninen ratkaisu, testaa sitä pienellä määrällä ja dokumentoi sitten kokonaisuus jäsennellyssä suunnitelmassa. Alkuvaiheen monimutkaisuus takaa, että Bitcoin-varasi siirtyvät eteenpäin täysin luottamuksellisesti.



## Resurssit



### Perintösuunnitelman malli





- [Bitcoin perintösuunnitelman malli (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network dokumentointimalli



### Tekniset viitteet





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Absoluuttisten aikamittareiden määrittely (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Suhteellisten aikarajojen määrittely (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Pieter Wuillen laatima virallinen Miniscript-dokumentaatio



### Ratkaisun viralliset verkkosivustot





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7