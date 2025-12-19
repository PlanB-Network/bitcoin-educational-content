---
name: BTCPay Server - Umbrel
description: BTCPay-palvelimen asentaminen ja käyttäminen Umbrelissa Bitcoin:n ja Lightningin hyväksymiseksi
---

![cover](assets/cover.webp)



Bitcoin-ekosysteemissä maksujen hyväksyminen on suuri haaste sekä kauppiaille että yrityksille. Perinteiset ratkaisut, olivatpa ne sitten pankkipalveluja (luottokortit, Stripe, PayPal) tai jopa Bitcoin:tä (BitPay, Coinbase Commerce), edellyttävät välikäsiä, jotka perivät huomattavia maksuja, keräävät arkaluonteisia liiketoimintatietojasi ja voivat estää tai sensuroida tapahtumasi mielensä mukaan. Tämä riippuvuus on vastoin Bitcoin:n perusperiaatteita, joita ovat hajauttaminen, luottamuksellisuus ja taloudellinen itsemääräämisoikeus.



BTCPay Server on kehittymässä avoimen lähdekoodin ratkaisuksi tähän ongelmaan. Tämä itse isännöity maksuprosessori tekee omasta Bitcoin-solmusta ammattimaisen infrastruktuurin, jossa ei ole välikäsiä, ylimääräisiä käsittelymaksuja eikä kompromisseja yksityisyydestä. BTCPay Server on kehitetty vuodesta 2017 lähtien maailmanlaajuisen avustajien yhteisön toimesta, ja sen avulla voit vastaanottaa Bitcoin- ja Lightning-maksuja suoraan lompakkoihisi ja säilyttää varojen täyden hallinnan koko ajan.



Perinteisesti BTCPay Serverin asentaminen vaatii kehittyneitä teknisiä taitoja: Linux-palvelimen konfigurointi, Dockerin hallinta, SSL-varmenteiden hallinta ja verkkoturvallisuus. Umbrel mullistaa tämän lähestymistavan yhden napsautuksen asennuksella, joka on integroitu suoraan Bitcoin- ja Lightning-solmuun. Tämä yksinkertaistaminen tekee siitä, mikä aiemmin oli varattu kokeneille teknikoille, kaikkien ulottuville.



**Tärkeää ymmärtää**: BTCPay Server on Umbrel toimii oletusarvoisesti vain paikallisessa verkossa. Voit luoda laskuja, hyväksyä Lightning- ja Bitcoin-maksuja ja hallita kirjanpitoa millä tahansa kotiverkkoon liitetyllä laitteella (tietokone, älypuhelin, tabletti). Tämä kokoonpano sopii erinomaisesti henkilökohtaisten palvelujen laskuttamiseen, kasvokkain tapahtuvien maksujen hallintaan tai BTCPay Serverin käyttämiseen paikallisverkosta. Toisaalta, jos haluat integroida BTCPay Serverin verkkokauppaan, joka on julkisesti saatavilla Internetissä, tarvitaan lisäkonfiguraatio, jossa on julkinen näkyvyys (käsittelemme tätä asiaa opetusohjelman lopussa).



Tässä oppaassa käydään läpi BTCPay Serverin täydellinen asennus Umbreliin, Bitcoin wallet- ja Lightning-solmun konfigurointi, laskujen luominen ja maksaminen sekä kirjanpidon raportoinnin hallinta. Saat selville, miten voit käyttää BTCPay Serveriä tehokkaasti paikallisverkossa, ja sitten tarkastelemme ratkaisuja julkiseen näyttöön, jos haluat integroida sen verkkokauppasivustoon.



## Edellytykset



Tämän ohjeen seuraaminen edellyttää, että Umbrel on asennettu ja konfiguroitu oikein. Jos et ole vielä tehnyt sitä, katso Umbrelin asennusta koskeva ohjeemme.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin Core -solmun on oltava täysin synkronoitu lohkoketjun kanssa (100 % Umbrelin Bitcoin-sovelluksessa). Tämä alustava synkronointi kestää yleensä kolmesta päivästä kahteen viikkoon riippuen laitteistostasi ja Internet-yhteydestäsi.



Jotta voit hyväksyä Lightning-pikamaksuja, sinun on myös asennettava LND (Lightning Network Daemon) Umbreliin. Katso ohje LND:n asentamisesta ja konfiguroinnista Umbreliin, jos haluat ottaa tämän ominaisuuden käyttöön.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Varaa vähintään 50 Gt vapaata levytilaa BTCPay-palvelimelle, sen tietokannoille ja Lightning-tiedoille. Vakaa Internet-yhteys Ethernet-kaapelin kautta on erittäin suositeltava yhteyden katkeamisen välttämiseksi.



## BTCPay-palvelimen asentaminen Umbreliin



Siirry Umbrelin käyttöliittymästä (`umbrel.local`) App Storeen ja etsi "BTCPay Server" Bitcoin-kategoriasta.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Napsauta Asenna. Umbrel tarkistaa automaattisesti, että Bitcoin Core ja LND on asennettu, ja aloittaa sitten käyttöönoton (2-5 minuuttia).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kun olet asentanut sovelluksen, avaa se. Sinun on luotava järjestelmänvalvojan tili vahvoilla tunnuksilla.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kun tilisi on luotu, BTCPay-palvelin pyytää sinua välittömästi perustamaan ensimmäisen kauppasi. Valitse yrityksen nimi ja valitse viitevaluutta (EUR, USD tai BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Pääsy BTCPay-palvelimelle paikallisessa verkossa osoitteessa



BTCPay-palvelinta voi käyttää mistä tahansa lähiverkon laitteesta (WiFi tai Ethernet). Pääset selaimellasi osoitteeseen :



```url
http://umbrel.local
```



Tai suoraan osoitteeseen :



```url
http://umbrel.local:3003
```



**Etäkäyttö Tailscalen avulla**: Käytä Tailscalea päästäksesi käsiksi BTCPay-palvelimeen mistä päin maailmaa tahansa. Tämän suojatun VPN:n avulla voit muodostaa yhteyden Umbreliin ikään kuin olisit paikallisverkossa. Katso Tailscalen käyttöä Umbrelissa käsittelevä opetusohjelmamme.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin-salkun määrittäminen



Jotta voit hyväksyä maksuja, sinun on määritettävä Bitcoin wallet. BTCPay Server näyttää konfigurointivaihtoehdot kojelaudassa.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Jos haluat määrittää wallet Bitcoin:n, siirry kohtaan "Lompakot" > "Bitcoin".



Sinulla on kaksi vaihtoehtoa: voit luoda uuden salkun suoraan BTCPayssä tai tuoda olemassa olevan salkun. Tuontia varten on käytettävissä useita menetelmiä:




- Kytke laitteisto wallet** (suositellaan): Tuo julkiset avaimesi Vault-sovelluksen kautta
- Tuo wallet-tiedosto** (suositellaan): Lataa portfoliostasi viety tiedosto
- Syötä laajennettu julkinen avain**: Syötä XPub/YPub/ZPub manuaalisesti
- Skannaa wallet QR-koodi** : Skannaa QR-koodi BlueWalletista, Cobo Vaultista, Passportista tai Specter DIY:stä
- Syötä wallet seed** (ei suositella) : Syötä 12- tai 24-sanainen palautuslauseke



![Options de création de portefeuille](assets/fr/06.webp)



Tässä ohjeessa luomme uuden Hot wallet:n: yksityinen avain tallennetaan siis Umbrel-palvelimellemme. Tässä tapauksessa suosittelemme, että siirrät varat säännöllisesti kylmään wallet:een, jotta vältät suurten määrien tallentamisen palvelimelle.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Kun BTCPay-palvelin on määritetty, se vahvistaa, että wallet on valmis hyväksymään on-chain-maksuja.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivoi Lightning Network



Jos haluat hyväksyä Lightning-pikamaksuja, valitse Lompakot > Lightning. Koska LND-solmusi on jo käytössä Umbrelissa, klikkaa "Tallenna"-painiketta vahvistaaksesi yhteyden BTCPay-palvelimesi ja Lightning-solmusi välillä.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Laskujen luominen ja maksaminen



Siirry BTCPay Server -käyttöliittymässä kohtaan Laskut > Luo Invoice. Anna summa, lisää valinnainen kuvaus ja napsauta Luo.



![Création d'une nouvelle facture](assets/fr/10.webp)



Voit sitten klikata "Checkout"-painiketta näyttääksesi laskun. Tämän jälkeen BTCPay luo laskun, jossa on yhtenäinen QR-koodi (BIP21), joka sisältää Bitcoin-osoitteen ja Lightning-laskun.



![Détails de la facture générée](assets/fr/11.webp)



Asiakas voi skannata QR-koodin millä tahansa yhteensopivalla wallet:llä.



![Page de paiement avec QR code](assets/fr/12.webp)



Kun lasku on maksettu, siitä tulee "maksettu" muutamassa sekunnissa Lightningin avulla.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Maksujen hallinta ja seuranta



"Raportointi"-osion "Laskut"-välilehdeltä löydät täydellisen historian laskuistasi päivämäärineen, summineen, tiloineen ja maksutapoineen. Voit viedä sen tarvittaessa.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Myymälän konfigurointi



BTCPay Serverin avulla voit hallita useita myymälöitä eri parametreilla. Jokainen myymälä edustaa erillistä liiketoimintayksikköä: verkkokauppaa, fyysistä myyntipistettä tai palvelulaskutusta.



Kaupan asetuksissa on useita tärkeitä osioita:



![Paramètres du magasin](assets/fr/15.webp)





- Yleiset asetukset**: Kaupan nimi, viitevaluutta (BTC, EUR, USD), laskun päättymisaika (oletus 15 minuuttia), vaadittujen lohkoketjuvahvistusten määrä
- Hinnat**: Valuuttakurssilähteiden ja fiat/Bitcoin-muunnosten konfigurointi
- Kassan ulkonäkö**: Mukauta kassasivujen ulkonäköä (logo, värit, henkilökohtaiset viestit)
- Sähköpostiasetukset**: Sähköposti-ilmoitusten määrittäminen vastaanotetuista maksuista
- Access Tokens**: API-tunnusten hallinta sähköisen kaupankäynnin integraatioita varten (WooCommerce, Shopify jne.)
- Käyttäjät**: Hallitse käyttäjien pääsyä myymälään eritasoisilla käyttöoikeuksilla (Omistaja, Vieras)
- Verkkokoukut**: Webhook-konfigurointi reaaliaikaista synkronointia varten kirjanpito- tai ERP-järjestelmän kanssa



BTCPay Server tarjoaa myös Plugins-osion, jonka avulla voit laajentaa toiminnallisuutta sähköisen kaupankäynnin integraatioilla, myyntipistejärjestelmillä ja lisätyökaluilla.



![Gestion des plugins](assets/fr/16.webp)



## Paikallisen käytön edut ja rajoitukset



**BTCPay-palvelimen edut Umbreliin verrattuna** :




- Täydellinen suvereniteetti: yksityisten avainten ja varojen yksinomainen hallinta, kukaan kolmas osapuoli ei voi jäädyttää tai sensuroida maksujasi
- Huomattavat säästöt: vain Bitcoin:n verkkokustannukset (muutama sentti Lightningilla) vs. 2-3 % perinteisillä prosessoreilla
- Maksimaalinen luottamuksellisuus: ei rekisteröintiä, henkilöllisyyden tarkistamista tai tietojen jakamista kolmansien osapuolten kanssa
- Avoimen lähdekoodin arkkitehtuuri takaa avoimuuden, tarkastettavuuden ja kestävyyden laajan kehittäjäyhteisön avulla
- Helppo asennus Umbrelin kautta, eikä teknisiä taitoja tarvita



**Tärkeitä rajoituksia** :




- Vain lähiverkko**: BTCPay Server on Umbrel on käytettävissä vain kotiverkossasi. Täydellinen henkilökohtaiseen laskutukseen, freelance-palveluihin tai pieniin fyysisiin yrityksiin, mutta ei sovellu julkisesti saatavilla oleviin verkkokauppoihin.
- Täysi tekninen vastuu: solmujen ylläpito, säännölliset varmuuskopiot, yhteyksien seuranta
- Salaman likviditeetin hallinta: kanavien avaaminen ja hallinnointi riittävällä saapuvalla kapasiteetilla
- Tuki rajoittuu yhteisön dokumentaatioon ja foorumeihin, mikä edellyttää enemmän itsenäisyyttä kuin kaupallisella asiakaspalveluosastolla



Tämä paikallisen verkon rajoitus on suurin este BTCPay Serverin integroimiselle verkkokauppaan, jossa asiakkaiden on voitava käyttää maksusivuja mistä tahansa Internetissä.



## Parhaat käytännöt ja turvallisuus



Aktivoi automaattiset Umbrelin varmuuskopiot ja tallenna kopio ulkoiselle tietovälineelle (USB-tikku, kiintolevy, salattu pilvi). Säilytä Bitcoin-siemeniä (palautuslauseita) turvallisessa, fyysisesti erillisessä paikassa. Varmuuskopioi LND:n channel.backup-tiedosto Lightningin palautusta varten.



Seuraa säännöllisesti Bitcoin Core -synkronointia, Lightning-kanavia ja BTCPay-palvelimen vastetta. Yksinkertainen viikoittainen testi: generate ja maksa lasku muutamasta satoshista. Pidä Umbrel ajan tasalla (tietoturvakorjaukset, parannukset). Tee varmuuskopio ennen suuria päivityksiä. Ammattikäyttöön harkitse ulkoista valvontaa (UptimeRobot) sähköposti-/SMS-ilmoituksin.



## BTCPay-palvelimen paljastaminen julkisesti verkkokaupassa



Jos haluat integroida BTCPay-palvelimen verkkokauppaan (WooCommerce, Shopify jne.), asiakkaidesi on voitava käyttää maksusivuja mistä tahansa, ei vain paikallisverkostasi.



**Ratkaisu: Nginx Proxy Manager**



Voit asettaa BTCPay-palvelimen julkisesti näkyville Nginx Proxy Managerin avulla (saatavilla Umbrel App Storesta). Tämä ratkaisu vaatii :




- Verkkotunnus (klassinen tai ilmainen DuckDNS:n, No-IP:n tai Afraid.org:n kautta)
- Porttien välittämisen määrittäminen (portit 80 ja 443) reitittimessäsi
- Nginx Proxy Managerin asennus, joka hallinnoi automaattisesti SSL-varmenteita



Tämä kokoonpano altistaa palvelimesi Internetille ja vaatii erityistä varovaisuutta (vahvat salasanat, 2FA, säännölliset päivitykset). Valmistelemme oman oppaan, jossa kerrotaan yksityiskohtaisesti tästä täydellisestä menettelystä.



## Päätelmä



BTCPay Server on Umbrel yhdistää Bitcoin-solmun tehon ja Umbrelin yksinkertaisuuden luodakseen itse isännöidyn ammattimaisen maksuinfrastruktuurin, joka on kaikkien saatavilla. Tämä taloudellinen suvereniteetti tuo mukanaan ylläpitovastuun, mutta Umbrel yksinkertaistaa huomattavasti operatiivista taakkaa verrattuna hyötyihin: käsittelymaksujen poistaminen, yksityisyytesi suojaaminen, sensuurin vastustaminen ja varojen täydellinen hallinta.



Lähiverkon käyttö kattaa jo nyt monenlaisia sovelluksia: freelance-palvelujen laskutus, henkilökohtaiset maksut, pienet fyysiset kaupat tai yksinkertaisesti Bitcoin:n ja Lightningin oppiminen ja kokeileminen valvotussa ympäristössä. Sähköisen kaupankäynnin tarpeisiin, jotka edellyttävät julkista näkyvyyttä, on olemassa Nginx Proxy Manager -ratkaisu, mutta se vaatii teknistä lisäkonfigurointia, josta kerromme tarkemmin erillisessä opetusohjelmassa.



BTCPay Server on Umbrel tarjoaa täydellisen taloudellisen riippumattomuuden riippumatta siitä, onko sinulla yritys, nuori projekti tai pelkkä kokeilu, BTCPay Server on Umbrel. Polku alkaa ensimmäisestä kaupastasi, ensimmäisestä laskustasi, ensimmäisestä maksusta, joka vastaanotetaan suoraan suvereeniin infrastruktuuriin.



## Resurssit



### Viralliset asiakirjat




- [BTCPay-palvelimen virallinen verkkosivusto](https://btcpayserver.org)
- [Täydellinen BTCPay-palvelimen dokumentaatio](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale documentation](https://tailscale.com/kb)


### Yhteisö ja tuki




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Foorumin sateenvarjo](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)