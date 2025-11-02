---
name: BTCPAY SERVER - vihmavarju
description: BTCPAY SERVER paigaldamine ja kasutamine Umbrelil, et võtta vastu Bitcoin ja Lightning
---

![cover](assets/cover.webp)



Bitcoin ökosüsteemis on maksete vastuvõtmine suur väljakutse nii kaupmeestele kui ka ettevõtetele. Traditsioonilised lahendused, olgu siis pangandus (krediitkaardid, Stripe, PayPal) või isegi Bitcoin (BitPay, Coinbase Commerce), kehtestavad vahendajaid, kes nõuavad märkimisväärseid tasusid, koguvad teie tundlikke äriandmeid ja võivad BLOCK või tsenseerida teie tehinguid oma äranägemise järgi. Selline sõltuvus on vastuolus Bitcoin detsentraliseerimise, konfidentsiaalsuse ja finantssuveräänsuse aluspõhimõtetega.



BTCPAY SERVER on kujunemas avatud lähtekoodiga vastuseks sellele probleemile. See isehostitav makseprotsessor muudab teie enda Bitcoin-sõlme professionaalseks infrastruktuuriks, ilma vahendajata, ilma täiendavate töötlemistasudeta ja ilma kompromissideta privaatsuse osas. BTCPAY SERVER, mida on alates 2017. aastast arendanud ülemaailmne toetajate kogukond, võimaldab teil vastu võtta Bitcoin ja Lightning makseid otse oma rahakotti, säilitades alati täieliku kontrolli oma rahaliste vahendite üle.



Traditsiooniliselt nõuab BTCPAY SERVER paigaldamine kõrgetasemelisi tehnilisi oskusi: Linuxi serveri konfigureerimine, Dockeri valdamine, SSL-sertifikaatide haldamine ja võrgu turvalisus. Umbrel muudab selle lähenemise revolutsiooniliselt, sest ühe klõpsuga paigaldamine on otse integreeritud teie Bitcoin ja LIGHTNING NODE-i. See lihtsustamine muudab selle, mis varem oli reserveeritud kogenud tehnikutele, kõigile kättesaadavaks.



**Tähtis mõista**: BTCPAY SERVER on Umbrel töötab vaikimisi ainult teie kohalikus võrgus. Saate luua arveid, võtta vastu Lightning ja Bitcoin makseid ning hallata oma raamatupidamist mis tahes seadmest, mis on ühendatud teie koduvõrku (arvuti, nutitelefon, tahvelarvuti). See konfiguratsioon on ideaalne isiklike teenuste arveldamiseks, isiklike maksete haldamiseks või BTCPAY SERVER kasutamiseks kohalikust võrgustikust. Teisest küljest, kui soovite integreerida BTCPAY SERVER veebipoodi, mis on avalikult ligipääsetav internetis, on vaja täiendavat konfiguratsiooni, mis on avalikult kättesaadav (seda teemat käsitleme õpetuse lõpus).



See õpetus viib teid läbi BTCPAY SERVER täieliku paigaldamise Umbrelile, Bitcoin Wallet ja LIGHTNING NODE seadistamise, arvete loomise ja maksmise ning raamatupidamisaruandluse haldamise. Saate teada, kuidas kasutada BTCPAY SERVER tõhusalt oma kohalikus võrgus, ja seejärel räägime lahendustest avalikuks kuvamiseks, kui soovite seda integreerida e-kaubanduse saidiga.



## Eeltingimused



Selle õpetuse jälgimiseks peab Umbrel olema õigesti paigaldatud ja konfigureeritud. Kui te pole seda veel teinud, vaadake meie Umbreli paigaldamise õpetust.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Teie Bitcoin core-sõlm peab olema täielikult sünkroonitud Blockchain-ga (100% Umbreli Bitcoin rakenduses). See esialgne sünkroniseerimine võtab tavaliselt aega 3 päevast kuni 2 nädalani, sõltuvalt teie riistvarast ja internetiühendusest.



Välkmaksete vastuvõtmiseks peate paigaldama Umbrelile ka LND (Lightning Network Daemon). Kui soovite selle funktsiooni lubada, vaadake meie õpetust LND paigaldamise ja konfigureerimise kohta Umbrelil.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Jätke BTCPAY SERVER-le, selle andmebaasidele ja Lightning-andmetele vähemalt 50 GB vaba kettaruumi. Et vältida katkestusi, on tungivalt soovitatav kasutada stabiilset internetiühendust Ethernet-kaabli kaudu.



## BTCPAY SERVER paigaldamine vihmavarjule



Umbrel Interface (`umbrel.local`), mine App Store'i ja otsi "BTCPAY SERVER" kategooriast Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klõpsake nuppu Install. Umbrel kontrollib automaatselt, kas Bitcoin core ja LND on paigaldatud, ja alustab seejärel kasutuselevõtmist (2-5 minutit).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Pärast paigaldamist avage rakendus. Peate looma tugevate volitustega administraatori konto.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kui teie konto on loodud, palub BTCPAY SERVER teil kohe luua oma esimene pood. Valige professionaalne nimi ja valige võrdlusvaluuta (EUR, USD või BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Juurdepääs BTCPAY SERVER-le teie kohalikus võrgus



BTCPAY SERVER on kättesaadav mis tahes seadmest teie kohalikus võrgus (WiFi või Ethernet). Juurdepääs brauserist :



```url
http://umbrel.local
```



Või otse :



```url
http://umbrel.local:3003
```



**kaugjuurdepääs koos Tailscale'iga**: Tailscale'i abil saate BTCPAY SERVER-le juurdepääsu ükskõik millisest maailma paigast. See turvaline VPN võimaldab teil oma Umbreliga ühendust võtta nii, nagu oleksite kohalikus võrgus. Vaadake meie Tailscale'ile pühendatud õpetust Umbrelil.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin portfelli konfigureerimine



Maksete vastuvõtmiseks peate konfigureerima Bitcoin Wallet. BTCPAY SERVER kuvab konfigureerimisvalikud armatuurlaual.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Wallet Bitcoin konfigureerimiseks valige "Rahakotid" > "Bitcoin".



Teil on kaks võimalust: luua uus portfell otse BTCPay's või importida olemasolev portfell. Impordiks on saadaval mitu meetodit:




- Ühendage Hardware Wallet** (soovitatav): Importige oma avalikud võtmed Vault rakenduse kaudu
- Impordi Wallet fail** (soovitatav): Laadige portfooliost eksporditud fail üles
- Sisestage laiendatud avalik võti**: Sisestage oma XPub/YPub/ZPub käsitsi
- Skaneeri Wallet QR-kood** : Skaneerige QR-koodi BlueWalletist, Cobo Vaultist, Passportist või Specter DIY-st
- Sisestage Wallet seed** (ei soovitata) : Sisestage oma 12- või 24-sõnaline taastumisfraas



![Options de création de portefeuille](assets/fr/06.webp)



Selle õpetuse jaoks loome uue Hot Wallet: privaatne võti salvestatakse seega meie Umbreli serveris. Sel juhul soovitame tungivalt, et liigutaksite raha regulaarselt Cold Wallet, et vältida suurte summade salvestamist serveris.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Kui BTCPAY SERVER on konfigureeritud, kinnitab Wallet, et teie Wallet on valmis On-Chain makseid vastu võtma.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiveeri Lightning Network



Lightning-pikamaksete vastuvõtmiseks valige rahakotid > Lightning. Seejärel, kuna teie LND-sõlm on Umbrelil juba paigas, klõpsake lihtsalt nupule "Salvesta", et kinnitada ühendus teie BTCPAY SERVER ja LIGHTNING NODE vahel.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Arvete koostamine ja tasumine



Interface BTCPAY SERVER navigeerige jaotisele Arved > Loo Invoice. Sisestage summa, lisage valikuline kirjeldus ja klõpsake nuppu Create.



![Création d'une nouvelle facture](assets/fr/10.webp)



Seejärel saate Invoice kuvamiseks klõpsata nupule "Kassasse". BTCPay genereerib seejärel Invoice ühtse QR-koodiga (BIP21), mis sisaldab Bitcoin Address ja Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Teie klient saab QR-koodi skaneerida mis tahes ühilduva Wallet-ga.



![Page de paiement avec QR code](assets/fr/12.webp)



Kui Invoice on makstud, saab Lightning'i jaoks "arveldatud" mõne sekundiga.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Maksete haldamine ja jälgimine



Jaotises "Aruandlus", vahekaardil "Arved" leiate oma arvete täieliku ajaloo koos kuupäeva, summa, staatuse ja makseviisiga. Vajadusel saate seda eksportida.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Poe konfiguratsioon



BTCPAY SERVER võimaldab teil hallata mitut kauplust erinevate parameetritega. Iga pood esindab eraldi äriüksust: e-kaubanduse pood, füüsiline müügipunkt või teenuse arveldamine.



Poe seadetes on mitu olulist jaotist:



![Paramètres du magasin](assets/fr/15.webp)





- Üldised seaded**: Poe nimi, võrdlusvaluuta (BTC, EUR, USD), Invoice kehtivusaeg (vaikimisi 15 minutit), nõutavate Blockchain kinnituste arv
- Hinnad**: Exchange kursiallikate ja fiat/Bitcoin konverteerimise konfiguratsioon
- Kassa väljanägemine**: Kohandage oma kassalehtede välimust (logo, värvid, isikupärastatud sõnumid)
- E-posti seaded**: Saabunud maksete kohta saadetavate e-posti teatiste konfigureerimine
- Juurdepääsutunnused**: API token haldamine e-kaubanduse integratsioonide jaoks (WooCommerce, Shopify jne)
- Kasutajad**: Halda kasutajate juurdepääsu kauplusele erinevate õiguste tasemetega (Omanik, Külaline)
- Veebikonks**: Webhookide konfigureerimine reaalajas sünkroniseerimiseks teie raamatupidamis- või ERP-süsteemiga



BTCPAY SERVER pakub ka pluginate sektsiooni, et laiendada funktsionaalsust e-kaubanduse integratsioonide, müügipunktisüsteemide ja lisavahenditega.



![Gestion des plugins](assets/fr/16.webp)



## Kohaliku kasutamise eelised ja piirangud



** BTCPAY SERVER eelised vihmavarju puhul** :




- Täielik suveräänsus: ainukontroll isiklike võtmete ja rahaliste vahendite üle, ükski kolmas osapool ei saa teie makseid külmutada ega tsenseerida
- Märkimisväärne kokkuhoid: ainult Bitcoin võrgukulud (paar senti Lightningil) võrreldes 2-3% traditsiooniliste protsessoritega
- Maksimaalne konfidentsiaalsus: ei mingit registreerimist, identiteedi kontrollimist ega andmete jagamist kolmandate osapoolte ettevõtetega
- Avatud lähtekoodiga arhitektuur tagab läbipaistvuse, auditeeritavuse ja jätkusuutlikkuse suure arendajate kogukonna kaudu
- Lihtne paigaldus Umbreli abil, ilma et oleks vaja edasijõudnud tehnilisi oskusi



**Tähtsaid piiranguid** :




- Ainult kohalik võrk**: BTCPAY SERVER on Umbrelil ligipääsetav ainult teie koduvõrgust. Ideaalne näost näkku arveldamiseks, vabakutseliste teenuste või väikeste füüsiliste ettevõtete jaoks, kuid ei sobi veebipoodide jaoks, mis on avalikult ligipääsetavad Internetis.
- Täielik tehniline vastutus: sõlmede hooldus, korrapärased varukoopiad, ühenduvuse jälgimine
- Välklikviidsuse juhtimine: piisava sissetuleva võimsusega kanalite avamine ja haldamine
- Tugi piirdub kogukonna dokumentatsiooni ja foorumitega, mis nõuab suuremat autonoomiat kui kaubanduslik klienditeenindusosakond



See kohtvõrgu piirang on peamine takistus BTCPAY SERVER integreerimisel e-kaubanduspoodi, kus klientidel peab olema võimalik pääseda makselehekülgedele ükskõik kust internetist.



## Parimad tavad ja ohutus



Aktiveerige automaatsed Umbreli varukoopiad ja salvestage koopia välisele andmekandjale (USB-pulk, Hard ketas, krüpteeritud pilv). Hoidke oma Bitcoin seemneid (taastamislauseid) turvalises, füüsiliselt eraldatud kohas. Salvestage LND kanali.backup-faili välk taastamiseks.



Jälgige korrapäraselt Bitcoin core sünkroniseerimist, välgukanaleid ja BTCPAY SERVER reaktsiooni. Lihtne iganädalane test: generate ja maksab arve mõne satelliidi eest. Hoidke Umbrel ajakohasena (turvaparandused, täiendused). Tehke enne suuremaid uuendusi varukoopiaid. Professionaalseks kasutamiseks kaaluge välist jälgimist (UptimeRobot) koos e-posti/SMS-hoiatustega.



## Näita BTCPAY SERVER avalikult veebipoe jaoks



BTCPAY SERVER integreerimiseks veebipõhisesse e-kaubamajja (WooCommerce, Shopify jne) peavad teie kliendid saama makse lehekülgedele ligi kõikjalt, mitte ainult teie kohalikust võrgustikust.



**Lahendus: Nginx Proxy Manager**



BTCPAY SERVER saab avalikustada, kasutades Nginx Proxy Managerit (saadaval Umbrel App Store'is). See lahendus nõuab :




- Domeeninimi (klassikaline või tasuta DuckDNS, No-IP, Afraid.org kaudu)
- Pordi edastamise (pordid 80 ja 443) seadistamine marsruuteril
- Nginx Proxy Manager'i paigaldamine, mis haldab automaatselt SSL sertifikaate



Selline konfiguratsioon paljastab teie serveri internetile ja nõuab täiendavat valvsust (tugevad paroolid, 2FA, korrapärased uuendused). Valmistame ette spetsiaalse õpetuse, milles kirjeldatakse üksikasjalikult seda täielikku protseduuri.



## Kokkuvõte



BTCPAY SERVER on Umbrel ühendab Bitcoin sõlme võimsuse ja Umbreli lihtsuse, et luua kõigile ligipääsetav professionaalsete maksete isehostitav infrastruktuur. Selle finantssuveräänsusega kaasneb hoolduskohustus, kuid Umbrel lihtsustab oluliselt operatiivkoormust võrreldes eelistega: töötlemistasude kaotamine, teie privaatsuse kaitse, tsensuurikindlus ja täielik kontroll teie rahaliste vahendite üle.



Kohaliku võrgu kasutamine hõlmab juba praegu väga erinevaid rakendusi: vabakutseliste teenuste arveldamine, maksed näost-näkku, väikesed füüsilised kauplused või lihtsalt õppimine ja katsetamine Bitcoin ja Lightningiga kontrollitud keskkonnas. E-kaubanduse vajaduste jaoks, mis nõuavad avalikku kokkupuudet, on olemas Nginx Proxy Manager'i lahendus, kuid see nõuab täiendavat tehnilist konfigureerimist, mida me kirjeldame üksikasjalikult spetsiaalses õpetuses.



Olenemata sellest, kas te juhite ettevõtet, alustavat projekti või lihtsalt eksperimenteerite, BTCPAY SERVER on Umbrel pakub täielikku finantsautonoomiat. Tee algab esimesest poest, esimesest Invoice, esimesest maksest, mis laekub otse teie suveräänsesse infrastruktuuri.



## Ressursid



### Ametlikud dokumendid




- [BTCPAY SERVER ametlik kodulehekülg](https://btcpayserver.org)
- [Täielik dokumentatsioon BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale dokumentatsioon](https://tailscale.com/kb)


### Ühendus ja toetus




- [Foorum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Foorumi vihmavarju](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)