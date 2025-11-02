---
name: BTCPAY SERVER - Sateenvarjo
description: BTCPAY SERVER:n asentaminen ja käyttäminen Umbrelissa Bitcoin:n ja Lightningin hyväksymiseksi
---

![cover](assets/cover.webp)



Bitcoin-ekosysteemissä maksujen hyväksyminen on suuri haaste sekä kauppiaille että yrityksille. Perinteiset ratkaisut, olivatpa ne sitten pankkipalveluja (luottokortit, Stripe, PayPal) tai jopa Bitcoin (BitPay, Coinbase Commerce), edellyttävät välittäjiä, jotka perivät huomattavia maksuja, keräävät arkaluonteisia liiketoimintatietojasi ja voivat BLOCK tai sensuroida tapahtumasi mielensä mukaan. Tämä riippuvuus on vastoin Bitcoin:n perusperiaatteita, joita ovat hajauttaminen, luottamuksellisuus ja taloudellinen itsemääräämisoikeus.



BTCPAY SERVER on kehittymässä avoimen lähdekoodin vastaukseksi tähän ongelmaan. Tämä itse isännöity maksuprosessori tekee omasta Bitcoin-solmusta ammattimaisen infrastruktuurin, jossa ei ole välikäsiä, ylimääräisiä käsittelymaksuja eikä kompromisseja yksityisyydestä. BTCPAY SERVER:n on kehittänyt vuodesta 2017 lähtien maailmanlaajuinen avustajien yhteisö, ja sen avulla voit vastaanottaa Bitcoin- ja Lightning-maksuja suoraan lompakkoihisi ja säilyttää varojen täyden hallinnan koko ajan.



BTCPAY SERVER:n asentaminen vaatii perinteisesti kehittyneitä teknisiä taitoja: Linux-palvelimen konfigurointi, Dockerin hallinta, SSL-sertifikaatin hallinta ja verkkoturvallisuus. Umbrel mullistaa tämän lähestymistavan yhdellä napsautuksella tehtävällä asennuksella, joka on integroitu suoraan Bitcoin- ja LIGHTNING NODE-järjestelmiin. Tämä yksinkertaistaminen tekee siitä, mikä aiemmin oli varattu kokeneille teknikoille, kaikkien ulottuville.



**Tärkeää ymmärtää**: BTCPAY SERVER on Umbrel toimii oletusarvoisesti vain paikallisverkossa. Voit luoda laskuja, hyväksyä Lightning- ja Bitcoin-maksuja ja hallita kirjanpitoa millä tahansa kotiverkkoon liitetyllä laitteella (tietokone, älypuhelin, tabletti). Tämä kokoonpano sopii erinomaisesti henkilökohtaisten palvelujen laskuttamiseen, kasvokkain tapahtuvien maksujen hallintaan tai BTCPAY SERVER:n käyttämiseen paikallisverkosta. Toisaalta, jos haluat integroida BTCPAY SERVER:n verkkokauppaan, joka on julkisesti saatavilla Internetissä, tarvitaan lisäkonfiguraatio, jossa on julkinen näkyvyys (käsittelemme tätä asiaa opetusohjelman lopussa).



Tässä oppaassa käydään läpi BTCPAY SERVER:n täydellinen asennus Umbreliin, Bitcoin:n, Wallet:n ja LIGHTNING NODE:n konfigurointi, laskujen luominen ja maksaminen sekä kirjanpidon raportoinnin hallinta. Saat selville, miten BTCPAY SERVER:aa käytetään tehokkaasti paikallisverkossa, ja sen jälkeen puhumme julkista näyttöä koskevista ratkaisuista, jos haluat integroida sen verkkokauppasivustoon.



## Edellytykset



Tämän ohjeen seuraaminen edellyttää, että Umbrel on asennettu ja konfiguroitu oikein. Jos et ole vielä tehnyt sitä, katso Umbrelin asennusta koskeva ohjeemme.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin core-solmun on oltava täysin synkronoitu Blockchain:n kanssa (100 % Umbrelin Bitcoin-sovelluksessa). Tämä alustava synkronointi kestää yleensä 3 päivästä 2 viikkoon laitteistosta ja Internet-yhteydestä riippuen.



Jotta voit hyväksyä Lightning-pikamaksuja, sinun on myös asennettava LND (Lightning Network Daemon) Umbreliin. Katso ohje LND:n asentamisesta ja konfiguroinnista Umbreliin, jos haluat ottaa tämän ominaisuuden käyttöön.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Varaa vähintään 50 Gt vapaata levytilaa BTCPAY SERVER:lle, sen tietokannoille ja Lightning-tiedoille. Vakaa Internet-yhteys Ethernet-kaapelin kautta on erittäin suositeltava, jotta vältetään yhteyden katkeamiset.



## BTCPAY SERVER:n asentaminen sateenvarjoon



Siirry Umbrel Interface:stä (`umbrel.local`) App Storeen ja etsi "BTCPAY SERVER" Bitcoin-kategoriasta.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Napsauta Asenna. Umbrel tarkistaa automaattisesti, että Bitcoin core ja LND on asennettu, ja aloittaa sitten käyttöönoton (2-5 minuuttia).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kun olet asentanut sovelluksen, avaa se. Sinun on luotava järjestelmänvalvojan tili vahvoilla tunnuksilla.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kun tilisi on luotu, BTCPAY SERVER pyytää sinua välittömästi perustamaan ensimmäisen myymälän. Valitse ammattinimi ja valitse viitevaluutta (EUR, USD tai BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Pääsy BTCPAY SERVER:ään paikallisverkossa



BTCPAY SERVER:een pääsee käsiksi mistä tahansa lähiverkon laitteesta (WiFi tai Ethernet). Pääset selaimellasi osoitteeseen :



```url
http://umbrel.local
```



Tai suoraan osoitteeseen :



```url
http://umbrel.local:3003
```



**Etäkäyttö Tailscalen avulla**: BTCPAY SERVER:een pääsee käsiksi mistä päin maailmaa tahansa Tailscalen avulla. Tämän suojatun VPN:n avulla voit muodostaa yhteyden Umbreliin kuin olisit paikallisverkossa. Katso Tailscalen käyttöä Umbrelissa käsittelevä opetusohjelmamme.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin-salkun määrittäminen



Maksujen vastaanottamista varten sinun on määritettävä Bitcoin Wallet. BTCPAY SERVER näyttää konfigurointivaihtoehdot kojelaudassa.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Jos haluat määrittää Wallet Bitcoin:n, siirry kohtaan "Lompakot" > "Bitcoin".



Sinulla on kaksi vaihtoehtoa: voit luoda uuden salkun suoraan BTCPayssä tai tuoda olemassa olevan salkun. Tuontia varten on käytettävissä useita menetelmiä:




- Kytke Hardware Wallet** (suositellaan): Tuo julkiset avaimesi Holvi-sovelluksen kautta
- Tuo Wallet-tiedosto** (suositellaan): Lataa portfoliostasi viety tiedosto
- Syötä laajennettu julkinen avain**: Syötä XPub/YPub/ZPub manuaalisesti
- Skannaa Wallet QR-koodi** : Skannaa QR-koodi BlueWalletista, Cobo Vaultista, Passportista tai Specter DIY:stä
- Syötä Wallet seed** (ei suositella) : Syötä 12- tai 24-sanainen palautuslauseke



![Options de création de portefeuille](assets/fr/06.webp)



Tässä ohjeessa luomme uuden Hot Wallet:n: yksityinen avain tallennetaan siis Umbrel-palvelimellemme. Tässä tapauksessa suosittelemme, että siirrät varat säännöllisesti Cold Wallet:een, jotta vältät suurten määrien tallentamisen palvelimelle.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Kun BTCPAY SERVER on konfiguroitu, se vahvistaa, että Wallet on valmis hyväksymään On-Chain-maksuja.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivoi Lightning Network



Jos haluat hyväksyä Lightning-pikamaksuja, valitse Lompakot > Lightning. Koska LND-solmusi on jo käytössä Umbrelissa, napsauta "Tallenna"-painiketta vahvistaaksesi yhteyden BTCPAY SERVER:n ja LIGHTNING NODE:n välillä.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Laskujen luominen ja maksaminen



Siirry Interface BTCPAY SERVER:ssa kohtaan Laskut > Luo Invoice. Syötä summa, lisää valinnainen kuvaus ja napsauta Luo.



![Création d'une nouvelle facture](assets/fr/10.webp)



Voit sitten klikata "Checkout"-painiketta näyttääksesi Invoice:n. BTCPay luo sitten Invoice:n, jossa on yhtenäinen QR-koodi (BIP21), joka sisältää Bitcoin Address:n ja Lightning Invoice:n.



![Détails de la facture générée](assets/fr/11.webp)



Asiakas voi skannata QR-koodin millä tahansa yhteensopivalla Wallet:llä.



![Page de paiement avec QR code](assets/fr/12.webp)



Kun maksu on suoritettu, Invoice:stä tulee Lightningin "Settled" muutamassa sekunnissa.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Maksujen hallinta ja seuranta



Raportointi-osiossa, "Laskut"-välilehdellä, löydät laskusi täydellisen historian, jossa on päivämäärä, summa, tila ja maksutapa. Voit viedä sen tarvittaessa.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Myymälän konfigurointi



BTCPAY SERVER:n avulla voit hallita useita myymälöitä eri parametreilla. Jokainen myymälä edustaa erillistä liiketoimintayksikköä: verkkokauppaa, fyysistä myyntipistettä tai palvelulaskutusta.



Kaupan asetuksissa on useita tärkeitä osioita:



![Paramètres du magasin](assets/fr/15.webp)





- Yleiset asetukset**: Invoice:n viimeinen voimassaoloaika (oletus 15 minuuttia), vaadittujen Blockchain-vahvistusten lukumäärä
- Hinnat**: Exchange-kurssilähteiden konfigurointi ja fiat/Bitcoin-muunnokset
- Kassan ulkonäkö**: Mukauta kassasivujen ulkonäköä (logo, värit, henkilökohtaiset viestit)
- Sähköpostiasetukset**: Sähköposti-ilmoitusten määrittäminen vastaanotetuista maksuista
- Access Tokens**: API token hallinta sähköisen kaupankäynnin integraatioita varten (WooCommerce, Shopify jne.)
- Käyttäjät**: Hallitse käyttäjien pääsyä myymälään eritasoisilla käyttöoikeuksilla (Omistaja, Vieras)
- Verkkokoukut**: Webhook-konfigurointi reaaliaikaista synkronointia varten kirjanpito- tai ERP-järjestelmän kanssa



BTCPAY SERVER tarjoaa myös Plugins-osion, jonka avulla voit laajentaa toiminnallisuutta sähköisen kaupankäynnin integraatioilla, myyntipistejärjestelmillä ja lisätyökaluilla.



![Gestion des plugins](assets/fr/16.webp)



## Paikallisen käytön edut ja rajoitukset



**BTCPAY SERVER:n hyödyt sateenvarjossa** :




- Täydellinen suvereniteetti: yksityisten avainten ja varojen yksinomainen hallinta, kukaan kolmas osapuoli ei voi jäädyttää tai sensuroida maksujasi
- Huomattavat säästöt: vain Bitcoin:n verkkokustannukset (muutama sentti Lightningilla) vs. 2-3 % perinteisillä prosessoreilla
- Maksimaalinen luottamuksellisuus: ei rekisteröintiä, henkilöllisyyden tarkistamista tai tietojen jakamista kolmansien osapuolten kanssa
- Avoimen lähdekoodin arkkitehtuuri takaa avoimuuden, tarkastettavuuden ja kestävyyden laajan kehittäjäyhteisön avulla
- Helppo asennus Umbrelin kautta, eikä teknisiä taitoja tarvita



**Tärkeitä rajoituksia** :




- Vain lähiverkko**: BTCPAY SERVER on Umbrel on käytettävissä vain kotiverkostasi. Sopii erinomaisesti kasvokkain tapahtuvaan laskutukseen, freelance-palveluihin tai pieniin fyysisiin yrityksiin, mutta ei sovellu verkkokauppoihin, jotka ovat julkisesti saatavilla Internetissä.
- Täysi tekninen vastuu: solmujen ylläpito, säännölliset varmuuskopiot, yhteyksien seuranta
- Salaman likviditeetin hallinta: kanavien avaaminen ja hallinnointi riittävällä saapuvalla kapasiteetilla
- Tuki rajoittuu yhteisön dokumentaatioon ja foorumeihin, mikä edellyttää enemmän itsenäisyyttä kuin kaupallisella asiakaspalveluosastolla



Tämä lähiverkkorajoitus on suurin este BTCPAY SERVER:n integroimiselle verkkokauppaan, jossa asiakkaiden on voitava käyttää maksusivuja mistä tahansa Internetissä.



## Parhaat käytännöt ja turvallisuus



Aktivoi automaattiset Umbrelin varmuuskopiot ja tallenna kopio ulkoiselle tietovälineelle (USB-tikku, Hard-levy, salattu pilvi). Säilytä Bitcoin-siemeniä (palautuslauseita) turvallisessa, fyysisesti erillisessä paikassa. Tallenna LND-kanava.backup-tiedosto Lightning-palauttamista varten.



Tarkkaile säännöllisesti Bitcoin core:n synkronointia, Lightning-kanavia ja BTCPAY SERVER:n vastetta. Yksinkertainen viikoittainen testi: generate ja maksa lasku muutamasta satoshista. Pidä Umbrel ajan tasalla (tietoturvakorjaukset, parannukset). Tee varmuuskopio ennen suuria päivityksiä. Ammattikäyttöön harkitse ulkoista valvontaa (UptimeRobot) sähköposti-/SMS-ilmoituksin.



## Näytä BTCPAY SERVER julkisesti verkkokaupalle



Jos haluat integroida BTCPAY SERVER:n verkkopohjaiseen verkkokauppaan (WooCommerce, Shopify jne.), asiakkaidesi on voitava käyttää maksusivuja mistä tahansa, ei vain paikallisverkosta.



**Ratkaisu: Nginx Proxy Manager**



Voit julkaista BTCPAY SERVER:n julkisesti käyttämällä Nginx Proxy Manageria (saatavilla Umbrel App Storesta). Tämä ratkaisu vaatii :




- Verkkotunnus (klassinen tai ilmainen DuckDNS:n, No-IP:n tai Afraid.org:n kautta)
- Porttien välittämisen määrittäminen (portit 80 ja 443) reitittimessäsi
- Nginx Proxy Managerin asennus, joka hallinnoi automaattisesti SSL-varmenteita



Tämä kokoonpano altistaa palvelimesi Internetille ja vaatii erityistä tarkkaavaisuutta (vahvat salasanat, 2FA, säännölliset päivitykset). Valmistelemme oman oppaan, jossa kerrotaan yksityiskohtaisesti tästä täydellisestä menettelystä.



## Päätelmä



BTCPAY SERVER on Umbrel yhdistää Bitcoin-solmun tehon ja Umbrelin yksinkertaisuuden, jotta voidaan luoda kaikkien saatavilla oleva itse isännöity ammattimainen maksuinfrastruktuuri. Tämä taloudellinen riippumattomuus tuo mukanaan ylläpitovastuun, mutta Umbrel yksinkertaistaa huomattavasti operatiivista taakkaa verrattuna hyötyihin: käsittelymaksujen poistaminen, yksityisyytesi suojaaminen, sensuurin vastustaminen ja varojen täydellinen hallinta.



Lähiverkon käyttö kattaa jo nyt monenlaisia sovelluksia: freelance-palvelujen laskutus, kasvokkain tapahtuva maksaminen, pienet fyysiset kaupat tai yksinkertaisesti Bitcoin:n ja Lightningin opettelu ja kokeilu valvotussa ympäristössä. Sähköisen kaupankäynnin tarpeisiin, jotka edellyttävät julkista näkyvyyttä, on olemassa Nginx Proxy Manager -ratkaisu, mutta se vaatii teknistä lisäkonfigurointia, josta kerromme tarkemmin erillisessä opetusohjelmassa.



BTCPAY SERVER on Umbrel tarjoaa täydellisen taloudellisen riippumattomuuden riippumatta siitä, onko kyseessä yritys, aloitteleva projekti vai pelkkä kokeilu. Polku alkaa ensimmäisestä kaupasta, ensimmäisestä Invoice:sta, ensimmäisestä maksusta, joka saapuu suoraan suvereeniin infrastruktuuriin.



## Resurssit



### Viralliset asiakirjat




- [BTCPAY SERVER virallinen verkkosivusto](https://btcpayserver.org)
- [Täydellinen BTCPAY SERVER-dokumentaatio](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale documentation](https://tailscale.com/kb)


### Yhteisö ja tuki




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Foorumin sateenvarjo](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)