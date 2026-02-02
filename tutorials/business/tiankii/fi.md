---
name: Tiankii
description: Lightning-työkalupaketti vähittäiskauppiaille ja kuluttajille
---

![cover](assets/cover.webp)



Bitcoin-ekosysteemissä maksujen hyväksyminen reaaliajassa on edelleen suuri haaste yrityksille ja yksityishenkilöille. Perinteiset ratkaisut edellyttävät usein pitkälle menevää teknistä osaamista, monimutkaista infrastruktuuria ylläpidettäväksi tai edellyttävät, että varat ovat välittäjien hallussa. Tämä tilanne estää Bitcoin:n laajamittaista käyttöönottoa jokapäiväisenä valuuttana, vaikka Lightning Network:n teknologiset edistysaskeleet ovatkin lupaavia.



Vuonna 2021 perustettu salvadorilainen yritys Tiankii vastaa tähän ongelmaan tarjoamalla helppokäyttöisen, modulaarisen Bitcoin-infrastruktuurin. Sen sijaan, että Tiankii pakottaisi ottamaan käyttöön suljetun ekosysteemin, se tarjoaa yhteenliitettyjen työkalujen sarjan, jonka avulla kuka tahansa voi integroida Bitcoin Lightningin liiketoimintaansa uhraamatta varojensa hallintaa.



## Mikä on Tiankii?



### Alkuperä ja filosofia



Tiankii - Nahuatl-termi, joka tarkoittaa "kaikille avointa, kaikille avointa markkinaa" - on El Salvadorin ensimmäinen 100-prosenttisesti Bitcoin-käynnistysyritys. Yrityksen perusti Darvin Otero sen jälkeen, kun Bitcoin hyväksyttiin maan lailliseksi maksuvälineeksi, ja sen tavoitteena on muuttaa Bitcoin arvosäilöstä jokapäiväisissä ostoksissa käytettäväksi valuutaksi. Toisin kuin säilytysalustat, Tiankii noudattaa ei-säilyttävää lähestymistapaa, jossa käyttäjät säilyttävät varojensa hallinnan ja infrastruktuuri toimii vain teknisenä välittäjänä.



### Tekninen arkkitehtuuri



Tiankii on asemoitunut Bitcoin-as-a-Service -infrastruktuurin tarjoajaksi, joka perustuu Lightning Network:ään. Tämä toisen kerroksen teknologia mahdollistaa lähes välittömät maksutapahtumat vähäisin kustannuksin, mikä mahdollistaa mikromaksut ja jokapäiväiset ostokset.



Arkkitehtuuri perustuu kolmeen pilariin:



**Salama-ensimmäinen**: Suositaan järjestelmällisesti Lightning-verkkoa sen nopeuden ja alhaisempien kustannusten vuoksi, mutta säilytetään on-chain-tapahtumatuki suurille summille.



** Avoimet standardit**: LNURL:n käyttö maksupyyntöjen automatisointiin, Lightning Address luettaviin sähköpostitunnuksiin ja Bolt Card yhteentoimiviin NFC-maksuihin.



**wallet-agnostinen modulaarisuus**: Mahdollisuus yhdistää eri Lightning-salkkuja (LNbits, Blink, BlueWallet) tai oma solmu, mikä tarjoaa maksimaalisen joustavuuden vaaditun asiantuntemuksen ja itsenäisyyden tason mukaan.



## Tiankii-ekosysteemin työkalut



### Bitcoin POS - Myymälän sisäinen maksupääte



Sovellus tekee älypuhelimesta tai tabletista Lightning-päätteen. Kauppias syöttää summan paikallisessa valuutassa, ja sovellus luo Lightning QR-koodin tai hyväksyy Bolt-kortin. Tapahtumat hyvitetään välittömästi ilman provisioita, ja käytössä on automaattinen muuntaminen yli 150 valuutassa, juomarahojen hallinta ja myyntihistoria.



### Merchant Dashboard - Yhtenäinen myynnin hallintajärjestelmä



Interface verkkokeskus, joka yhdistää wallet Lightningin, seuraa tapahtumia reaaliajassa, lähettää laskuja ja generate kirjanpitoraportteja. Alusta yhdistää kaikki kanavat: myymälämaksut (POS), verkkomyynti (sähköisen kaupankäynnin lisäosat) tai API integraatiot. Maksut konvergoituvat valittuun wallet:ään.



### Bitcoin kosketukseton kortti (Bolt-kortti)



NFC Bolt -kortti on Tiankiin merkittävä innovaatio Bitcoin:n demokratisoimiseksi suurelle yleisölle. Se toimii kuin kontaktiton pankkikortti, ja sen avulla voit maksaa Bitcoin Lightning -ostokset yksinkertaisesti napauttamalla yhteensopivaa päätelaitetta.



Toisin kuin perinteiset säilytysratkaisut, tämä kortti noudattaa avointa standardia, joka takaa yhteentoimivuuden. Käyttäjät voivat liittää sen omaan wallet:een IBI-sovelluksen kautta, jolloin he säilyttävät yksityiset avaimensa ja voivat valvoa täysin siihen liittyviä varoja. Maksu kestää vain sekunnin, eikä älypuhelinta tarvitse ottaa esiin eikä maksuhetkellä tarvitse olla aktiivista internet-yhteyttä.



Tämä ratkaisu on erityisen osallistava älypuhelimia tuntemattomille ihmisille, ja se tarjoaa helppokäyttöisen portin Bitcoin-talouteen.



### IBI-sovellus - Interface yksittäinen Bitcoin



IBI-sovellus (Individual Bitcoin Interface) on tarkoitettu henkilöille, jotka haluavat käyttää Bitcoin Lightningia päivittäin. Sen tärkein etu on henkilökohtaisen Address Lightning -tunnuksen luominen, joka on sähköpostimuodossa luettava maksutunnus (esimerkki: alice@ibi.me).



Tämä tunniste yksinkertaistaa huomattavasti maksujen vastaanottamista: generate:n ei tarvitse laatia uutta laskua jokaista tapahtumaa varten, vaan lähettäjä voi yksinkertaisesti syöttää Lightning-osoitteen. Käyttöliittymän avulla voit myös hallinnoida Bolt -korttiasi (aktivointi, deaktivointi, käyttörajat), yhdistää erilaisia Lightning-lompakoita ja suorittaa maksuja skannaamalla QR-koodeja.



### Sähköisen kaupankäynnin liitännäiset



Käyttövalmiit integraatiot WooCommerce, Shopify ja Cloudbeds. Asennetaan muutamassa minuutissa lisätäksesi Bitcoin Lightning kassalle. Edut: nollaprovisiot (vs. 2-3 % luottokortit), välitön selvitys, maailmanlaajuinen pääsy, takaisinkirjausten poistaminen. Maksut saapuvat suoraan kauppiaan yhdistettyyn wallet:een.



### Bitcoin API ja kehittäjätyökalut



Tiankii SDK mahdollistaa Bitcoin Lightningin integroinnin olemassa oleviin sovelluksiin ilman oman solmun ylläpitoa. API hoitaa laskujen luomisen, maksujen tarkistamisen ja massapostitukset Google Cloudissa isännöidyn vankan infrastruktuurin avulla. Command Center täydentää tarjontaa organisaatioille, joilla on Address Lightning mukautetuilla verkkotunnuksilla, massamaksuilla sekä NFC-päätteiden ja -korttien keskitetyllä hallinnalla.



## Asennus ja ensimmäiset vaiheet



### Olennaiset edellytykset



Tiankiin käyttäminen ei vaadi monimutkaisia teknisiä edellytyksiä. Sovellukset toimivat verkkoselaimen kautta älypuhelimella, tabletilla tai tietokoneella. Sovelluksen asentamista ei tarvita: tarvitset vain Internet-yhteyden ja tuoreen selaimen IBI:n tai Merchant Dashboardin käyttöä varten.



**Peruskäyttäjille (IBI-sovellus)**: wallet Lightningia ei tarvita. Kun luot tilisi, Tiankii määrittää automaattisesti toimivan Address Lightningin [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html) kautta, joka on nodeless-toteutus, joka käyttää Liquid-verkkoa taustalla. Voit heti vastaanottaa ja lähettää maksuja ilman teknisiä määrityksiä. Tämä ratkaisu yksinkertaistaa huomattavasti aloittelijoiden pääsyä, mutta on samalla itsesäätöinen.



**Myyjille (Merchant Dashboard)** : Olemassa olevan wallet Lightningin liittäminen on pakollista myyntipäätteiden käyttämiseksi ja maksujen vastaanottamiseksi. Tiankii tukee monia ratkaisuja: mobiililompakoita (Blink, Strike), itse isännöityjä ratkaisuja (LNbits, LND/CLN-solmu) tai verkkolompakoita (Alby). Yksityiskohtaiset yhteysoppaat ovat saatavilla tämän ohjeen Resurssit-osiossa.



### Yksityisasiakkaille: IBI App



**Tilin luominen



Mene osoitteeseen accounts.ibi.me ja luo tilisi. Tällä sivulla voit valita kahden tilityypin välillä: "Henkilökohtainen käyttö" yksityiseen käyttöön tai "Yrityskäyttö" kaupalliseen käyttöön. Valitse "Henkilökohtainen käyttö", niin saat käyttöösi työkalut, joilla voit vastaanottaa ja lähettää maksuja Bitcoin:ssä.



![Choix du type de compte](assets/fr/01.webp)



Kun olet valinnut "Henkilökohtainen käyttö", sinut ohjataan automaattisesti osoitteeseen go.ibi.me, jossa voit suorittaa rekisteröinnin loppuun. Tämä voidaan tehdä sähköpostitse, puhelinnumeron avulla tai Google-, Microsoft- tai Twitter-tiliäsi käyttäen. Luomisen jälkeen pääset välittömästi IBI-käyttöliittymään, jossa Lightning Address on jo toiminnassa.



![Création du compte](assets/fr/02.webp)



**Interface main**



IBI-käyttöliittymä näyttää saldosi satosheina ja paikallisena valuuttana (USD). Kolme painiketta mahdollistaa vuorovaikutuksen: "Vastaanota" maksujen vastaanottamiseksi, "Skannaa" QR-koodin skannaamiseksi ja "Lähetä" satoshien lähettämiseksi.



![Interface IBI](assets/fr/03.webp)



**Vastaanottaa maksun**



Jos haluat vastaanottaa satosheja, paina "Vastaanota". Sovellus luo automaattisesti QR-koodin ja näyttää henkilökohtaisen Address Lightning -viestisi (nom@ibi.me -muodossa). Jaa tämä osoite tai QR-koodi lähettäjän kanssa: varat saapuvat välittömästi IBI-tilillesi.



![Réception avec Lightning Address](assets/fr/04.webp)



Kun saldosi on hyvitetty, voit käyttää näitä satosheja maksujen suorittamiseen.



**lähetä maksu**



Jos haluat lähettää satosheja, paina "Lähetä". Voit joko skannata Lightning QR-koodin tai syöttää suoraan Lightning Address -kohteen.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Syötä haluamasi summa satosheina, tarkista vastaava summa paikallisessa valuutassa ja vahvista maksu.



![Confirmation du montant](assets/fr/07.webp)



Onnistumisilmoitus vahvistaa lähetyksen ja sisältää seuraavat tiedot: lähetetty summa, tapahtumamaksu ja vastaanottaja.



![Paiement réussi](assets/fr/08.webp)



**Tilien hallinta



Asetuksissa voit hallita Bitcoin NFC-kortteja (Bolt-kortit). Käyttöliittymän avulla voit aktivoida, poistaa käytöstä tai asettaa korttien käyttörajat.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Kauppiaille: Kauppiaan kojelauta ja POS



**Yritystilin luominen



Mene osoitteeseen accounts.ibi.me ja luo tilisi. Valitse "Yrityskäyttö" päästäksesi käsiksi kauppiastyökaluihin. Tämäntyyppinen tili avaa pääsyn kauppiaan kojelautaan ja myyntipisteiden päätelaitteisiin.



Kun olet valinnut "Yrityskäyttö", sinut ohjataan automaattisesti kauppiaan kojelaudalle (pay.tiankii.com). Sieltä pääset yrityksen hallintakäyttöliittymään, jossa on tulojen seuranta, tapahtumat ja maksutyökalut. Aloittaaksesi maksujen vastaanottamisen sinun on ensin yhdistettävä wallet Lightning -järjestelmäsi napsauttamalla sivun yläreunassa olevaa linkkiä (katso kuvan nuoli).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** -liitäntä



Tärkeä vaihe myyntipisteen aktivoimiseksi: liitä wallet Lightning -järjestelmäsi maksujen vastaanottamista varten. Käyttöliittymä tarjoaa useita liitäntävaihtoehtoja. Huomaa, että jotkin vaihtoehdot (Bitcoin Onchain ja Lightning Network) ovat vielä kehitteillä ja näkyvät käyttöliittymässä harmaina.



![Options de connexion wallet](assets/fr/12.webp)



Tässä ohjeessa käytämme Lightning Address -liitäntää, joka on yhteensopiva Vivon, Blink Wallet:n ja Striken kanssa. Syötä Lightning Address (nom@domaine.com -muoto), esimerkiksi LN Marketsilta, Albyltä tai muulta yhteensopivalta toimittajalta.



![Saisie de la Lightning Address](assets/fr/13.webp)



Kun olet kirjautunut sisään, tilisi on toiminnassa. Voit nyt käyttää kassakonetta tai palata kojelaudalle määrittämään muita asetuksia.



![Connexion réussie](assets/fr/14.webp)



*maksu Linkit** *Maksu Linkit



"Maksutyökalut"-valikosta pääset "Maksupyyntöön", jonka avulla voit luoda ja hallita maksulinkkejä. Tämä toiminto on hyödyllinen, kun haluat luoda henkilökohtaisia maksulinkkejä, jotka lähetetään sähköpostitse tai viestillä: lahjoitukset, yksittäiset maksut, useat maksut tai jopa maksumuurit sisällön suojaamiseksi. Voit luoda erityyppisiä linkkejä yrityksesi tarpeiden mukaan.



![Liens de paiement](assets/fr/15.webp)



**Myyntipäätteen kokoonpano**



Jos haluat hyväksyä myymälämaksuja, avaa "Maksutyökalut"-valikosta "Myyntipääte"-valikko. Tässä osiossa voit luoda ja hallita myyntipäätteitäsi (päätteiden määrä riippuu suunnitelmastasi, katso Freemium vs. Business-suunnitelmat alla). Avaa POS-käyttöliittymä selaimessasi napsauttamalla "Avaa".



![Gestion des terminaux](assets/fr/16.webp)




**Myynnin synnyttäminen**



Kassapäätteessä näkyy numeronäppäimistö myyntisumman syöttämistä varten. Syötä summa paikallisessa valuutassa (esim. 500 sats vastaa 630,74 ARS) ja vahvista painamalla "OK".



![Saisie du montant](assets/fr/17.webp)



Sovellus luo välittömästi Lightning QR-koodin ja Lightning Address -koodin maksua varten. Asiakkaat voivat skannata QR-koodin wallet-kortilla tai käyttää Bolt-korttiaan NFC-päätteellä.



![QR code de paiement](assets/fr/18.webp)



Heti kun maksu on vastaanotettu, näyttöön ilmestyy vahvistusnäyttö, jossa näkyy vastaanotettu summa paikallisena valuuttana ja satosheina. Voit lähettää kuitin sähköpostitse, tulostaa lipun tai aloittaa uuden myynnin välittömästi.



![Paiement encaissé](assets/fr/19.webp)



**Valvonta ja hallinta**



Kaikki tapahtumat kirjataan kauppiaan kojelaudalle. Sinulla on täydellinen seuranta tuloista jaksoittain, myynnin kokonaismäärästä ja yksityiskohtainen historia kirjanpitoa varten.



Asetukset-käyttöliittymässä on useita määritysvälilehtiä. Yleiset asetukset -välilehdellä voit hallita kauppiasprofiilia ja ilmoituksia. "Käyttäjät"-välilehdellä voit lisätä ja hallita tiimisi pääsyä kauppiaan kojelautaan (usean käyttäjän hallinta suunnitelman mukaan). "Kehitystyötila"-välilehdellä pääset käsiksi API-avaimiin kehittyneitä integraatioita varten, kun taas "Tilaus"-välilehdellä voit hallita tilaustasi.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs. Business-suunnitelmat



Tiankii tarjoaa kaksi pakettia Merchant Dashboardiin. **Freemium**-paketti (ilmainen) soveltuu aloittaville yrityksille, joilla on seuraavat rajoitukset: yksi myyntipiste, yksi käyttäjä, kuukausittainen volyymi rajoitettu 1 000 dollariin, eikä pääsyä sähköisen kaupankäynnin liittimiin. **Business**-suunnitelma (0,5 % maksu per tapahtuma) tarjoaa rajattomasti päätelaitteita, rajattomasti käyttäjiä, rajattoman volyymin, pääsyn WooCommerce/Shopify/Cloudbeds-liitännäisiin ja eksklusiiviset WhatsApp-ilmoitukset.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Hyödyt ja rajoitukset



### Kohokohdat



**Huoltajuus**: Säilytät yksityiset avaimesi ja täyden määräysvallan varoistasi. Ei riskiä tilin jäädyttämisestä tai kolmannen osapuolen alustan konkurssista.



**Yksinkertaisuus**: NFC-maksut yksinkertaisella napautuksella, intuitiivinen käyttöliittymä, jossa ei tarvita teknistä asiantuntemusta: Lightning Address sähköpostiosoitteena, NFC-maksut yksinkertaisella napautuksella.



**Täydellinen ekosysteemi**: Työkalut kaikille profiileille (yksityishenkilöt, jälleenmyyjät, kehittäjät) ja modulaariset integraatiot tarpeidesi mukaan.



**ammatillinen vaatimustenmukaisuus**: PCI-DSS-vaatimustenmukaisuus, Salvadorian lainsäädännön noudattaminen.



### Rajoitukset



**Salamointirajoitukset**: Vaatii pysyvän wallet-yhteyden, likviditeetin hallinta suurille volyymeille, riski epäonnistua, jos vastaanottaja on offline-tilassa. Tiankii lieventää näitä näkökohtia integroiduilla LSP:llä.



**SaaS-riippuvuus**: Jos Tiankii ei ole käytettävissä, laskujen luominen on tilapäisesti mahdotonta (varasi pysyvät turvassa).



**Privacy**: Tiankii voi tarkkailla transaktioiden metatietoja (summat, päivämäärät). Vähemmän yksityinen kuin itse isännöity ratkaisu, kuten BTCPay Server.



## Päätelmä



Tiankii havainnollistaa, miten hyvin suunniteltu infrastruktuuri voi poistaa tekniset esteet, jotka estävät Bitcoin:n laajamittaisen käyttöönoton jokapäiväisenä valuuttana. Yhdistämällä Lightning Network:n voiman, vapaamuotoisen lähestymistavan ja helppokäyttöiset työkalut ekosysteemi tarjoaa tasapainoisen polun taloudellisen riippumattomuuden ja helppokäyttöisyyden välille.



Kauppiaille Tiankii tarjoaa tilaisuuden alentaa huomattavasti transaktiokustannuksia ja saada samalla uutta asiakaskuntaa. Kuluttajille Lightning Address ja NFC-kortit tekevät Bitcoin:sta käytännöllisen valuutan ilman teknistä monimutkaisuutta.



Vaikka Bitcoin:n laajamittainen käyttöönotto on edelleen haaste, joka vaatii koulutusta ja aikaa, Tiankiin kaltaiset infrastruktuurit osoittavat, että tekniset välineet ovat jo olemassa. Bitcoin-maksujen yksinkertaistaminen ei ole enää kaukainen visio, vaan todellisuutta, joka on kaikkien halukkaiden ulottuvilla.



## Resurssit



### Viralliset asiakirjat




- [Tiankiin virallinen verkkosivusto](https://tiankii.com)
- [Tiankii Help Center](https://help.tiankii.com)
- [IBI-sovellus](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Komentokeskus](https://cc.ibi.me)



### Wallet liitäntäoppaat




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Yhteisö




- [Lightning Network Plus](https://lightningnetwork.plus) - Salamakoulutusresurssi
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorilainen kiertotalousaloite Bitcoin



### Aiheeseen liittyvät työkalut




- [Blink Wallet](https://blink.sv) - suositellaan Wallet Lightning -yhteensopivuutta
- [LNbits](https://lnbits.com) - Itse isännöity wallet-ratkaisu
- [Standard Bolt Card](https://github.com/boltcard) - NFC-korttien tekniset eritelmät