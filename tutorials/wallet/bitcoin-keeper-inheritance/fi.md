---
name: Bitcoin Keeper - Perintösuunnitelma
description: Suunnittele Bitcoin-siirto Bitcoin Keeper:n avulla
---

![cover](assets/cover.webp)



Bitcoin:n omaisuuden siirto on yksi niistä haasteista, joita haltijat aliarvioivat eniten. Toisin kuin pankkitilillä, jossa rahoituslaitos voi siirtää varat laillisille perillisille, Bitcoin on täysin riippuvainen yksityisten avainten hallussapidosta. Täysin laillinen perillinen ei koskaan pääse käsiksi varoihin ilman näitä avaimia, kun taas salaisuudet hallussaan pitävä pahantahtoinen henkilö voi käyttää varat ilman mitään muodollisuuksia.



Tässä toisessa Bitcoin Keeper:n opetusohjelmassa tutustumme kiinteistösuunnitteluun tarkoitettuihin premium-ominaisuuksiin. Sovellus tarjoaa kehittyneitä työkaluja Enhanced Holvien luomiseen, joissa on Miniscriptin ansiosta ajoitetut suojausmekanismit, sekä liitännäisasiakirjoja, joilla opastat läheisiäsi.



Tässä oppaassa oletetaan, että olet jo oppinut Bitcoin Keeper:n perusteet (salkun luominen, klassinen multisig, laitteistonäppäinten lisääminen), kuten ensimmäisessä oppaassa selitetään:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper-tilaussuunnitelmat



Bitcoin Keeper toimii freemium-mallilla, jossa on kolme tilaustasoa, jotka tarjoavat progressiivisia toimintoja. Pääset suunnitelmiin käsiksi siirtymällä **Lisää**-välilehdelle ja napauttamalla sitten nykyistä suunnitelmaasi (oletusarvo on "Pleb") avataksesi **Tilauksen hallinta** -näytön.



![Plans d'abonnement](assets/fr/01.webp)



**Pleb-suunnitelma** (ilmainen) tarjoaa pääsyn perusasioihin: rajoittamaton yhden ja usean avaimen lompakoiden luominen, yhteensopivuus kaikkien tärkeimpien laitteistolompakoiden kanssa (Coldcard, Trezor, Ledger, Jade, Tapsigner...), kolikoiden hallinta, merkitseminen ja yhteys henkilökohtaiseen Electrum-palvelimeen. Tämä suunnitelma riittää vakiokäyttöön ja jopa klassisiin multi-sig-kokoonpanoihin.



**Hodler-paketti** (9,99 €/kk, 1 kuukausi ilmaiseksi, jos maksat vuosittain) sisältää kaikki Pleb-ominaisuudet ja lisää salatut varmuuskopiot pilveen (iCloud tai Google Drive), jotta voit palauttaa kassakaappisi millä tahansa laitteella, palvelinavaimen automaattisten kulutuskäytäntöjen ja 2FA:n lisäämiseksi tietyn kynnysarvon ylittävältä osalta sekä Canary-lompakot, jotka havaitsevat luvattoman pääsyn avaimiin.



**Timantti kädet -suunnitelma** (29,99 €/kk, 1 kuukausi ilmaiseksi, jos maksat vuosittain) on täydellinen paketti jäämistösuunnittelua varten. Se sisältää koko Hodler-suunnitelman ja avaa perintöavaimen (lykätty aktivointi), hätäavaimen (hätäavain palautusta varten menetyksen sattuessa), perintösuunnittelutyökalut ja -asiakirjat sekä tukipuhelun Concierge-tiimin kanssa kokoonpanon vahvistamiseksi. Tämä tarjous on tarkoitettu bitcoin-asiakkaille, jotka haluavat siirtää perintönsä usean sukupolven yli.



Tärkeä seikka: luomasi holvit pysyvät käytettävissä, vaikka vaihtaisit takaisin ilmaispakettiin. Määrityksesi perustuvat avoimiin standardeihin (BSMS, Miniscript) ja toimivat tilauksestasi riippumatta.



## Perintöasiakirjat



Kun olet aktivoinut Diamond Hands -tilauksesi, siirry Lisää-välilehdeltä kohtaan **PERINTÖASIAKIRJAT**. Bitcoin Keeper tarjoaa viisi esimerkkidokumenttia perintösuunnitelmasi jäsentämistä varten sekä vinkkejä käsittelevän osion:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: malli, jonka avulla voit kirjata palautuslauseita siististi ja järjestäytyneesti
- Luotetut yhteyshenkilöt**: malli, jossa luetellaan suunnitelmassasi mukana olevien luotettavien henkilöiden yhteystiedot (notaari, asianajaja, perilliset, avaintenvartijat)
- Additional Share Key**: asiakirja, jossa on yksityiskohtaiset tekniset tiedot kustakin avaimesta: PIN-koodi, johdannaispolku, fyysinen sijainti, laitetyyppi ja kaikki muut tiedot, jotka ovat hyödyllisiä avaimen tunnistamisen ja käytön kannalta
- Takaisinperintäohjeet**: vaiheittaiset ohjeet perilliselle tai edunsaajalle varojen takaisinperimiseksi
- Kirje asianajajalle**: esitäytetty kirje, joka voidaan mukauttaa asianajajaa tai notaaria varten



**Perimysvinkkejä** -osiossa annetaan käytännön neuvoja perillisten avainten turvaamisesta ja perintösuunnitelman optimoinnista.



Muokkaa nämä asiakirjat omaan tilanteeseesi sopiviksi ja säilytä ne turvallisessa paikassa erillään itse avaimista.



## Pilvivarmistuksen määrittäminen



Aktivoi pilvivarmistus konfiguraatiotiedostojen suojaamiseksi ennen perintöholvin luomista. Paina Lisää-välilehdellä **Henkilökohtainen pilvivarmistus**.



![Configuration Cloud Backup](assets/fr/03.webp)



Valitse vahva salasana varmuuskopioiden salaamiseen. Tämä salasana suojaa vain wallet:n asetustiedostot (ei yksityisiä avaimia). Vahvista salasana ja paina **Vahvista**. Varmuuskopiot tallennetaan iCloudiin tai Google Driveen laitteestasi riippuen. Käynnistä ensimmäinen varmuuskopio painamalla **Backup Now**.



## Tuo laitteiston avaimet



Esimerkkiämme varten luomme 2-of-3-turvakaapin, jossa on kaksi lisäavainta (Perinnöllisyys ja Hätä). Aloitetaan tuomalla kaikki tarvittavat avaimet **Keys**-välilehdelle.



![Import des clés hardware](assets/fr/04.webp)



Paina **Lisää näppäin** ja valitse sitten **Lisää näppäin laitteistosta** liittääksesi laitteiston wallet. Bitcoin Keeper tukee monia laitteita: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ja Specter Solutions.



Meidän kokoonpanossamme tuomme :




- 2 **korttipainiketta** (MK4SP ja MK4)
- 2 näppäintä **Tapsigner** (Metro ja Genesis)



Jos haluat lisätä Coldcardin, valitse se luettelosta ja noudata näytön ohjeita julkisen avaimen viemiseksi QR-koodin, tiedoston, USB:n tai NFC:n kautta. Lisätietoja Coldcardin tai Tapsigner:n käytöstä on erillisissä opetusohjelmissamme:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Kun kaikki avaimet on tuotu, löydät ne Avaimet-välilehdeltä mukautetuilla nimillä.



## Luo perintö wallet



Siirrytään runkojen luomiseen. Paina **Lompakot**-välilehdellä **Lisää Wallet**, valitse **Bitcoin Wallet** ja sitten **Luo Wallet**.



![Création du wallet](assets/fr/05.webp)



Valitse wallet-tyyppi. Perinteistä suunnitelmaamme varten valitse **2 kolmesta moniavaimesta**. Aktivoi näytön alareunassa **Enhanced Security Options** ja paina sitten **Proceed**.



![Options de sécurité avancées](assets/fr/06.webp)



Tarkennetut suojausasetukset -ponnahdusikkunassa merkitse :




- Perintöavain**: lisäavain, joka lisätään khorumiin tietyn ajan kuluttua
- Hätäavain**: avain, jossa on lykätty täydellinen valvonta varojen palauttamiseksi, jos avain katoaa



Paina **Tallenna muutokset**. Valitse sitten 3 avainta, jotka muodostavat wallet:n, tuoduista avaimista (esim. Seed Key, Coldcard MK4SP ja Tapsigner Metro).



## Erityisten keskeisten määräaikojen asettaminen



Seuraavassa näytössä voit määrittää hätäavaimen ja perintöavaimen. Tässä määritetään näiden erityisavainten aktivointia koskevat viiveet.



![Configuration des délais](assets/fr/07.webp)



Valitse **Hätäavainta** varten laitteistoavain, joka toimii lopullisena varmuuskopiona (tässä Coldcard MK4), ja valitse aktivointiviive (esimerkissämme 2 vuotta). Toisin kuin perintöavain, hätäavain ei lisää päätösvaltaisuutta: sen avulla voit **ohittaa monisignaalin** kokonaan ja voit hallita varoja täysin määräajan umpeutumisen jälkeen. Se on viimeinen keino: jos useita avaimia katoaa tai tuhoutuu, voit palauttaa kaiken tämän yhden avaimen avulla. Siksi sitä on suojattava äärimmäisen tarkasti.



Valitse **PERINTÖAVAIMEN** kohdalla perilliselle tarkoitettu avain (tässä Coldcard MK4SP) ja valitse viive (esimerkissämme 1 vuosi). Kun avainta ei ole liikuteltu yhden vuoden ajan, se **lisätään allekirjoituskantaan**. Käytännössä wallet 2-of-3 muuttuu wallet 2-of-4:ksi, kun tämä aika on kulunut, jolloin perillinen voi osallistua allekirjoitukseen olemassa olevien avainten rinnalla.



### Miten aikakellot toimivat?



Bitcoin Keeper käyttää **absoluuttisia aikalukkoja** (CLTV - CheckLockTimeVerify), jotka Miniscript mahdollistaa. Toisin kuin suhteelliset timelockit (CSV), jotka alkavat, kun kukin UTXO vastaanotetaan, absoluuttiset timelockit toimivat **kiinnitetyllä päättymispäivämäärällä**, joka määritetään wallet:n luomisen yhteydessä.



Konkreettisesti, jos luot wallet:n tänään 1 vuoden perintöavaimella, aktivointipäivä on "tänään + 1 vuosi". Kaikki tähän wallet:ään talletetut varat ovat talletuspäivästä riippumatta käytettävissä perintöavaimella samana päivänä.



Absoluuttisten aikarajojen etuna on, että ne mahdollistavat yli 15 kuukauden toimitusajat (suhteellisten CSV-aikarajojen raja), mikä selittää, miksi Bitcoin Keeper voi tarjota esimerkiksi 2 vuoden vaihtoehtoja.



### Päivitysmekanismi



Estääksesi erikoisavainten aktivoinnin elinaikanasi sinun on "päivitettävä" wallet:si säännöllisesti. Absoluuttisissa aikalukoissa tämä tarkoittaa **luomista wallet:n uudella, tulevaisuuteen siirretyllä voimassaolon päättymispäivämäärällä** ja varojen siirtämistä tähän uuteen wallet:een.



Bitcoin Keeper yksinkertaistaa tätä prosessia integroidulla päivitystoiminnolla. Sovellus hoitaa monimutkaisuuden automaattisesti taustalla: sinun tarvitsee vain seurata opastettuja vaiheita, eikä sinun tarvitse luoda uutta wallet:a manuaalisesti tai siirtää varoja itse. Suunnittele tämä toiminto säännöllisesti hyvissä ajoin ennen määritetyn lyhimmän aikavälin päättymistä. Esimerkiksi 1 vuoden perintöavaimella päivitä 9-10 kuukauden välein, jotta varmuusmarginaali säilyy.



## Tallenna ja vie kokoonpano



Kun wallet on luotu, sovellus muistuttaa sinua tallentamaan asetustiedoston. **Tämä vaihe on kriittinen**: ilman tätä tiedostoa perillisesi eivät pysty palauttamaan wallet multisigiä.



![Export de la configuration](assets/fr/08.webp)



Paina **Backup Wallet Recovery File**. Käytettävissä on useita vientivaihtoehtoja:




- PDF-vienti**: tuottaa täydellisen asiakirjan, joka sisältää kaikki wallet-tiedot
- Näytä QR**: näyttää QR-koodin, jolla voit tuoda kokoonpanon toiseen laitteeseen
- Airdrop / Tiedoston vienti**: vie tiedoston jakamisvaihtoehtojen kautta
- NFC**: jakaminen NFC:n kautta yhteensopivan laitteen kanssa



Moninkertaista kopiot: yksi notaarin luona, yksi pankin kassakaapissa ja yksi salattu digitaalinen versio. Uusi wallet näkyy nyt Lompakot-välilehdellä tunnisteilla "Moniavain", "2 kolmesta", "Perintöavain" ja "Hätäavain".



## Luo Wallet-kanarialintu



Canary Wallet on varhaisvaroitusjärjestelmä. Ajatus: jokaista wallet:n moniavaimessa käytettyä avainta voidaan käyttää myös erillisessä wallet:n yksittäisavaimessa. Tallettamalla pienen summan tähän wallet-"kanarialle" kaikki luvattomat liikkeet ilmoittavat avaimen vaarantumisesta.



![Canary Wallets](assets/fr/09.webp)



Wallet Canary voidaan määrittää kahdella tavalla. Paina **Lisätietoja** -välilehdellä "Avaimet ja lompakot" -osiossa **Kanarian lompakot**. Näytössä selitetään periaate: jos joku pääsee käsiksi johonkin avaimeesi ja löytää varoja siihen liittyvästä wallet-yksittäisavaimesta, hän yrittää poistaa ne, mikä hälyttää sinut.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Voit määrittää Canaryn myös suoraan avaimesta. Valitse **Näppäimet**-välilehdeltä näppäin (esim. Tapsigner Genesis), paina **Asetukset** (hammasratas) -kuvaketta ja sitten **Canary Wallet**. Liittyvä kanarialintu wallet avautuu, valmiina vastaanottamaan joitakin valvontasatoja.



Talleta pieni summa (muutama tuhat satoshia) jokaiselle kanarialaiselle Wallet:lle. Jos nämä varat siirtyvät ilman suostumustasi, poista välittömästi vaarantunut avain multisig-turvakaapistasi.



## Parhaat käytännöt



**Testaa kokoonpanoasi** pienellä rahasummalla, ennen kuin sijoitat siihen suuren summan. Lähetä muutama tuhat satoshia holviin ja kokeile sitten lähtevää rahankäyttöä tarkistaaksesi, että hallitset allekirjoitusprosessin jokaisella laitteella. Testaa myös konfiguraatiotiedoston tuomista toiseen puhelimeen varmistaaksesi, että varmuuskopiointi toimii.



**Jaa avaimet älykkäästi**. Luovuta avaimet sinetöidyssä kirjekuoressa ja ilmoita PIN-koodi erikseen (esim. toisaalla säilytettävässä palautusohjekirjeessä). Klassisten laitteistolompakoiden osalta säilytä laite luotettavalla kolmannella osapuolella ja seed paperilla tai metallisessa muodossa sinulla tai toisella kolmannella osapuolella. Merkitse kunkin avaimen sormenjälki ja sen nimi konfigurointitiedostoon sekaannusten välttämiseksi.



**Suunnittele säännölliset testit** (paloharjoitukset). Tarkista vuosittain, että voit rakentaa kassakaapin uudelleen varmuuskopioista tyhjällä puhelimella. Testaa Canary-hälytykset tarkistamalla saldot. Simuloi katoamisskenaarioita ("mitä jos menetän Coldcardin?") varmistaaksesi, että jäljellä olevat avainyhdistelmät ovat riittäviä.



**Älä unohda päivitystä**. Jos olet asettanut perintöavaimesi 1 vuodeksi, päivitä se 9-10 kuukauden välein. Tämä on hinta, jonka maksat automaattisesta siirrosta ilman kolmannen osapuolen väliintuloa.



**Pitäkää suunnitelma ajan tasalla**. Kaikki muutokset (avaimen vaihtaminen, perillisten muuttaminen, määräajan muuttaminen) on otettava huomioon kaikissa varmuuskopioissa ja asiakirjoissa. Generoi PDF-tiedostot uudelleen jokaisen muutoksen jälkeen ja jaa uudet versiot uudelleen.



## Rajoitukset ja näkökohdat



Näiden työkalujen tehosta huolimatta on tärkeää tunnistaa niiden rajoitukset, jotta niitä voidaan hallita mahdollisimman tehokkaasti.



Monisignaalisen kassakaapin **monimutkaisuus**, jossa on aikalukot, voi olla riski itsessään: vääränlainen konfigurointi, perillisten väärinkäsitys, kriittisen elementin katoaminen monien komponenttien joukosta. Bitcoin Keeper yksinkertaistaa kokemusta niin paljon kuin mahdollista, mutta se on edelleen tekninen toimenpide. Ota tämä suunnitelma käyttöön vain, jos suojattava määrä oikeuttaa sen. Pienille summille voi riittää yksinkertaisempi suunnitelma.



**Sovellusriippuvuutta** kannattaa miettiä. Vaikka koodi on avointa lähdekoodia ja perustuu avoimiin standardeihin (Miniscript, BSMS), tietyt toiminnot ovat riippuvaisia Keeper-ekosysteemistä. Säilytä kopio sovelluksesta (Android APK tai iOS IPA) ja dokumentoi perillisille lähettämissäsi kirjeissä mahdollisuus käyttää muita Miniscript-yhteensopivia lompakoita (kuten Liana) varojen palauttamiseen.



Luotettavat välittäjät** aiheuttavat inhimillisen riskin. Mitä tapahtuu, jos pahantahtoinen sukulainen käyttää hänelle uskottua avainta ennen määräaikaa? Tai jos asianajaja hukkaa asiakirjasi? Valitse nämä henkilöt huolellisesti, selitä heidän vastuunsa selkeästi ja ota käyttöön suunnitelma B. Canary Wallet, redundantit varmuuskopiot ja multisigin rakenne ovat paras suoja näitä vaaroja vastaan.



## Päätelmä



Bitcoin Keeper tarjoaa Diamond Hands -suunnitelmallaan täydellisen työkalupakin omaisuuden suunnitteluun: Parannetut holvit ajastetuilla avaimilla, liitännäisasiakirjat, Canary-lompakot ja henkilökohtainen tuki.



Kyse on muustakin kuin vain teknisestä kysymyksestä: kyse on omaisuuden arkkitehtuurin suunnittelusta, avainten ja tiedon älykkäästä jakamisesta ja järjestelmän säännöllisestä testaamisesta. Hyvin suunniteltu Bitcoin-perintösuunnitelma muuttaa satoshisi todelliseksi, siirrettäväksi perinnöksi.