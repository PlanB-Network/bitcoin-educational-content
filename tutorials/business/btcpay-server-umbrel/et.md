---
name: BTCPay Server - Umbrel
description: BTCPay serveri paigaldamine ja kasutamine Umbrelil, et aktsepteerida Bitcoin ja Lightning'i
---

![cover](assets/cover.webp)



Bitcoin ökosüsteemis on maksete vastuvõtmine suur väljakutse nii kaupmeestele kui ka ettevõtetele. Traditsioonilised lahendused, olgu siis pangandus (krediitkaardid, Stripe, PayPal) või isegi Bitcoin (BitPay, Coinbase Commerce), kehtestavad vahendajaid, kes nõuavad märkimisväärseid tasusid, koguvad teie tundlikke äriandmeid ja võivad teie tehinguid oma äranägemise järgi blokeerida või tsenseerida. Selline sõltuvus on vastuolus Bitcoin detsentraliseerimise, konfidentsiaalsuse ja finantssuveräänsuse aluspõhimõtetega.



BTCPay Server on kujunemas avatud lähtekoodiga lahenduseks sellele probleemile. See isehostitav makseprotsessor muudab teie enda Bitcoin-sõlme professionaalseks infrastruktuuriks, ilma vahendajata, täiendavate töötlemistasudeta ja privaatsuse osas kompromissideta. BTCPay Server, mida on alates 2017. aastast arendanud ülemaailmne toetajate kogukond, võimaldab teil vastu võtta Bitcoin ja Lightning makseid otse oma rahakotti, säilitades alati täieliku kontrolli oma rahaliste vahendite üle.



Traditsiooniliselt nõuab BTCPay Serveri paigaldamine kõrgetasemelisi tehnilisi oskusi: Linuxi serveri konfigureerimine, Dockeri, SSL-sertifikaadi haldamise ja võrgu turvalisuse valdamine. Umbrel muudab selle lähenemisviisi revolutsiooniliselt, sest ühe klikiga paigaldamine on otse integreeritud teie Bitcoin ja Lightning-sõlmega. See lihtsustamine muudab selle, mis varem oli reserveeritud kogenud tehnikutele, kõigile kättesaadavaks.



**Tähtis mõista**: BTCPay Server on Umbrel töötab vaikimisi ainult teie kohalikus võrgus. Saate luua arveid, võtta vastu Lightning- ja Bitcoin-makseid ning hallata oma raamatupidamist mis tahes seadmest, mis on ühendatud teie koduvõrku (arvuti, nutitelefon, tahvelarvuti). See konfiguratsioon on ideaalne isiklike teenuste arveldamiseks, isiklike maksete haldamiseks või BTCPay Serveri kasutamiseks kohalikust võrgust. Teisest küljest, kui soovite integreerida BTCPay Serveri veebipoodi, mis on avalikult ligipääsetav internetis, on vaja lisakonfiguratsiooni, mis on avalikult kättesaadav (seda teemat käsitleme õpetuse lõpus).



See õpetus viib teid läbi BTCPay Serveri täieliku paigaldamise Umbrelile, Bitcoin wallet ja Lightning-sõlme konfigureerimise, arvete loomise ja maksmise ning raamatupidamisaruannete haldamise. Saate teada, kuidas kasutada BTCPay Serverit tõhusalt oma kohalikus võrgus, ja seejärel vaatame lahendusi avalikuks kuvamiseks, kui soovite seda integreerida e-kaubanduse saidiga.



## Eeltingimused



Selle õpetuse jälgimiseks peab Umbrel olema õigesti paigaldatud ja konfigureeritud. Kui te ei ole seda veel teinud, vaadake meie Umbreli paigaldamise õpetust.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Teie Bitcoin Core-sõlm peab olema täielikult sünkroonitud plokiahela (100% Umbreli Bitcoin rakenduses). See esialgne sünkroniseerimine võtab tavaliselt aega 3 päevast kuni 2 nädalani, sõltuvalt teie riistvarast ja internetiühendusest.



Välkmaksete vastuvõtmiseks peate paigaldama Umbrelile ka LND (Lightning Network Daemon). Kui soovite selle funktsiooni lubada, vaadake meie õpetust LND paigaldamise ja konfigureerimise kohta Umbrelil.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Lubage vähemalt 50 GB vaba kettaruumi BTCPay Serverile, selle andmebaasidele ja Lightning-andmetele. Et vältida katkestusi, on tungivalt soovitatav kasutada stabiilset internetiühendust Ethernet-kaabli kaudu.



## BTCPay serveri paigaldamine Umbrelile



Mine Umbreli kasutajaliidesest (`umbrel.local`) App Store'i ja otsi kategooriast Bitcoin välja "BTCPay Server".



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klõpsake nuppu Install. Umbrel kontrollib automaatselt, kas Bitcoin Core ja LND on paigaldatud, ja alustab seejärel kasutuselevõtmist (2-5 minutit).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Pärast paigaldamist avage rakendus. Peate looma tugevate volitustega administraatori konto.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Kui teie konto on loodud, palub BTCPay Server teil kohe luua oma esimene pood. Valige ärinimi ja valige võrdlusvaluuta (EUR, USD või BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Juurdepääs BTCPay serverile oma kohalikus võrgus



BTCPay Server on kättesaadav mis tahes seadmest teie kohalikus võrgus (WiFi või Ethernet). Juurdepääs brauserist :



```url
http://umbrel.local
```



Või otse :



```url
http://umbrel.local:3003
```



**kaugjuurdepääs koos Tailscale'iga**: BTCPay serverile juurdepääsu saamiseks ükskõik kust maailmas, kasutage Tailscale'i. See turvaline VPN võimaldab teil ühendada oma Umbreliga nagu oleksite oma kohalikus võrgus. Vaadake meie Tailscale'ile pühendatud õpetust Umbrelil.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin portfelli konfigureerimine



Maksete vastuvõtmiseks peate konfigureerima Bitcoin wallet. BTCPay Server kuvab seadistamisvõimalusi armatuurlaual.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



wallet Bitcoin konfigureerimiseks valige "Rahakotid" > "Bitcoin".



Teil on kaks võimalust: luua uus portfell otse BTCPay's või importida olemasolev portfell. Impordiks on saadaval mitu meetodit:




- Ühendage riistvara wallet** (soovitatav): Importige oma avalikud võtmed Vault rakenduse kaudu
- Impordi wallet fail** (soovitatav): Laadige oma portfooliost eksporditud fail üles
- Sisestage laiendatud avalik võti**: Sisestage oma XPub/YPub/ZPub käsitsi
- Skaneeri wallet QR-kood** : Skaneeri QR-koodi BlueWalletist, Cobo Vaultist, Passportist või Specter DIY-st
- Sisestage wallet seed** (ei soovitata) : Sisestage oma 12- või 24-sõnaline taastumisfraas



![Options de création de portefeuille](assets/fr/06.webp)



Selle õpetuse jaoks loome uue Hot wallet: privaatne võti salvestatakse seega meie Umbreli serveris. Sel juhul soovitame tungivalt, et liigutaksite raha regulaarselt külmale wallet-le, et vältida suurte summade säilitamist serveris.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Pärast seadistamist kinnitab BTCPay Server, et teie wallet on valmis on-chain makseid vastu võtma.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiveeri Lightning Network



Lightning-pikamaksete vastuvõtmiseks valige rahakotid > Lightning. Seejärel, kuna teie LND sõlme on Umbrelil juba olemas, klõpsake lihtsalt nupule "Salvesta", et kinnitada ühendus BTCPay serveri ja teie Lightning-sõlme vahel.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Arvete koostamine ja tasumine



BTCPay Serveri kasutajaliideses navigeerige jaotisele Arved > Loo Invoice. Sisestage summa, lisage valikuline kirjeldus ja klõpsake nuppu Create.



![Création d'une nouvelle facture](assets/fr/10.webp)



Seejärel saate arve kuvamiseks klõpsata nupule "Kassasse". BTCPay genereerib seejärel arve ühtse QR-koodiga (BIP21), mis sisaldab Bitcoin aadressi ja Lightning-arve.



![Détails de la facture générée](assets/fr/11.webp)



Teie klient saab QR-koodi skaneerida mis tahes ühilduva wallet-ga.



![Page de paiement avec QR code](assets/fr/12.webp)



Kui arve on tasutud, muutub Lightning'i jaoks arve sekundite jooksul "arveldatuks".



![Confirmation de paiement réussi](assets/fr/13.webp)



## Maksete haldamine ja jälgimine



Jaotises "Aruandlus", vahekaardil "Arved" leiate oma arvete täieliku ajaloo koos kuupäeva, summa, staatuse ja makseviisiga. Vajadusel saate seda eksportida.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Poe konfiguratsioon



BTCPay Server võimaldab teil hallata mitut kauplust erinevate parameetritega. Iga pood esindab eraldi äriüksust: e-kaubanduse pood, füüsiline müügipunkt või teenuse arveldamine.



Poe seadetes on mitu olulist jaotist:



![Paramètres du magasin](assets/fr/15.webp)





- Üldised seaded**: Poe nimi, võrdlusvaluuta (BTC, EUR, USD), arve aegumise aeg (vaikimisi 15 minutit), nõutavate plokiahela kinnituste arv
- Hinnad**: Valuutakursside allikate ja fiat/Bitcoin konverteerimise konfiguratsioon
- Kassast väljanägemine**: Kohandage oma kassalehtede välimust (logo, värvid, isikupärastatud sõnumid)
- E-posti seaded**: Saabunud maksete kohta saadetavate e-posti teatiste konfigureerimine
- Juurdepääsutunnused**: API tokenite haldamine e-kaubanduse integratsioonide jaoks (WooCommerce, Shopify jne.)
- Kasutajad**: Halda kasutajate juurdepääsu kauplusele erinevate õiguste tasemetega (Omanik, Külaline)
- Veebikonks**: Webhookide konfigureerimine reaalajas sünkroniseerimiseks teie raamatupidamis- või ERP-süsteemiga



BTCPay Server pakub ka pluginate sektsiooni, et laiendada funktsionaalsust e-kaubanduse integratsioonide, müügipunktisüsteemide ja lisavahenditega.



![Gestion des plugins](assets/fr/16.webp)



## Kohaliku kasutamise eelised ja piirangud



**BTCPay serveri eelised Umbreli ees** :




- Täielik suveräänsus: ainukontroll isiklike võtmete ja rahaliste vahendite üle, ükski kolmas osapool ei saa teie makseid külmutada ega tsenseerida
- Märkimisväärne kokkuhoid: ainult Bitcoin võrgukulud (paar senti Lightningil) võrreldes 2-3% traditsiooniliste protsessoritega
- Maksimaalne konfidentsiaalsus: ei mingit registreerimist, identiteedi kontrollimist ega andmete jagamist kolmandate osapoolte ettevõtetega
- Avatud lähtekoodiga arhitektuur tagab läbipaistvuse, auditeeritavuse ja jätkusuutlikkuse suure arendajate kogukonna kaudu
- Lihtne paigaldus Umbreli abil, ilma et oleks vaja edasijõudnud tehnilisi oskusi



**Tähtsaid piiranguid** :




- Ainult kohalik võrk**: BTCPay Server on Umbrelil ligipääsetav ainult teie koduvõrgust. Ideaalne näost näkku arveldamiseks, vabakutseliste teenuste või väikeste füüsiliste ettevõtete jaoks, kuid ei sobi avalikult ligipääsetavate veebipoodide jaoks.
- Täielik tehniline vastutus: sõlmede hooldus, korrapärased varukoopiad, ühenduvuse jälgimine
- Välklikviidsuse juhtimine: piisava sissetuleva võimsusega kanalite avamine ja haldamine
- Tugi piirdub kogukonna dokumentatsiooni ja foorumitega, mis nõuab suuremat autonoomiat kui kaubanduslik klienditeenindusosakond



See kohaliku võrgu piirang on peamine takistus BTCPay Serveri integreerimisel e-kaubanduse kauplusesse, kus kliendid peavad olema võimelised pääsema makselehekülgedele ükskõik kust internetist.



## Parimad tavad ja ohutus



Aktiveerige automaatsed Umbreli varukoopiad ja salvestage koopia välisele andmekandjale (USB-pulk, kõvaketas, krüpteeritud pilvepakett). Hoidke oma Bitcoin seemneid (taastamislauseid) turvalises, füüsiliselt eraldatud kohas. Varundage LND kanali.backup faili välk taastamiseks.



Jälgige regulaarselt Bitcoin Core sünkroniseerimist, Lightning-kanaleid ja BTCPay Serveri vastuseid. Lihtne iganädalane test: generate ja makske arve mõne satoshi eest. Hoidke Umbrel ajakohasena (turvaparandused, täiendused). Tehke enne suuremaid uuendusi varukoopiaid. Professionaalseks kasutamiseks kaaluge välist jälgimist (UptimeRobot) koos e-posti/SMS-hoiatustega.



## BTCPay serveri avalikustamine veebipoe jaoks



BTCPay Serveri integreerimiseks veebipõhisesse e-kaubamajja (WooCommerce, Shopify jne) peavad teie kliendid saama ligipääsu makselehekülgedele kõikjalt, mitte ainult teie kohalikust võrgustikust.



**Lahendus: Nginx Proxy Manager**



Saate BTCPay serveri avalikult avaldada, kasutades Nginx Proxy Managerit (saadaval Umbrel App Store'is). See lahendus nõuab :




- Domeeninimi (klassikaline või tasuta DuckDNS, No-IP, Afraid.org kaudu)
- Pordi edastamise (pordid 80 ja 443) seadistamine marsruuteril
- Nginx Proxy Manager'i paigaldamine, mis haldab automaatselt SSL sertifikaate



Selline konfiguratsioon paljastab teie serveri internetile ja nõuab täiendavat valvsust (tugevad paroolid, 2FA, korrapärased uuendused). Valmistame ette spetsiaalse õpetuse, milles kirjeldatakse üksikasjalikult seda täielikku protseduuri.



## Kokkuvõte



BTCPay Server on Umbrel ühendab Bitcoin sõlme võimsuse ja Umbreli lihtsuse, et luua isehostitav professionaalne makseinfrastruktuur, mis on kõigile kättesaadav. Selle finantssuveräänsusega kaasneb hoolduskohustus, kuid Umbrel lihtsustab oluliselt operatiivkoormust võrreldes eelistega: töötlemistasude kaotamine, teie privaatsuse kaitse, tsensuurikindlus ja täielik kontroll teie rahaliste vahendite üle.



Kohaliku võrgu kasutamine hõlmab juba praegu väga erinevaid rakendusi: vabakutseliste teenuste arveldamine, isiklikud maksed, väikesed füüsilised kauplused või lihtsalt Bitcoin ja Lightningiga õppimine ja katsetamine kontrollitud keskkonnas. E-kaubanduse vajaduste jaoks, mis nõuavad avalikku kokkupuudet, on olemas Nginx Proxy Manager'i lahendus, kuid see nõuab täiendavat tehnilist konfigureerimist, mida me kirjeldame üksikasjalikult spetsiaalses õpetuses.



BTCPay Server on Umbrel pakub täielikku finantsautonoomiat, olenemata sellest, kas teil on ettevõte, alustav projekt või lihtsalt eksperimenteerimine. Tee algab teie esimesest poest, esimesest arvest, esimesest maksest, mis laekub otse teie suveräänsesse infrastruktuuri.



## Ressursid



### Ametlikud dokumendid




- [BTCPay ametliku serveri veebisait](https://btcpayserver.org)
- [Täielik BTCPay serveri dokumentatsioon](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale dokumentatsioon](https://tailscale.com/kb)


### Ühendus ja toetus




- [Foorumi BTCPay server](https://chat.btcpayserver.org)
- [Foorumi vihmavarju](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)