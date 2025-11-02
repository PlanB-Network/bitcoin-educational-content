---
name: LNbits Server
description: LNbits'i isehostitava serveri paigaldamine ja seadistamine Ubuntu VPSil koos PHOENIXD või Umbreliga
---

![cover](assets/cover.webp)



LNbits on avatud lähtekoodiga Interface veebirakendus, mis muudab mis tahes Lightning backend (LND, Core Lightning, PHOENIXD) täielikuks teenuseplatvormiks. See isehostitav lahendus võimaldab teil hallata mitut Lightningi portfelli eraldi, võtta kasutusele müügipunkte, luua annetussüsteeme või arveldusteenuseid, säilitades samas täieliku kontrolli oma vahendite üle.



See õpetus hõlmab kahte paigaldusviisi: **VPS Ubuntu koos PHOENIXD-ga** (kerge lahendus ilma täieliku Bitcoin-sõlmita) ja **Umbrel** (integreerimine olemasoleva LND-sõlmega). Erinevalt Plan B Networki üldisest LNbits'i juhendist, mis hõlmab kontseptsioone ja laiendusi, keskendub see juhend samm-sammult tehnilistele paigaldusprotseduuridele.



## Mis on LNbits?



LNbits on Pythonis (FastAPI) välja töötatud Lightning-raamatupidamissüsteem, mis ühendub olemasoleva backendiga (LND, Core Lightning, PHOENIXD). Erinevalt traditsioonilistest Lightning-sõlmedest pakub LNbits ligipääsetavat Interface, mis võimaldab hallata mitut eraldatud portfelli oma API võtmetega. Saate luua alamkontod oma pere, töötajate või projektide jaoks, andmata neile juurdepääsu kõigile teie rahalistele vahenditele.



Lahutatud arhitektuur salvestab teavet SQLite'is (vaikimisi) või PostgreSQLis (tootmine), samas kui rahalisi vahendeid haldab endiselt teie Lightning backend. Selline eraldatus tagab teisaldatavuse: saate PHOENIXD-lt LND-le üle minna ilma kasutajaandmeid kaotamata.



## Peamised omadused



LNbits pakub mitmekülgset **täiendussüsteemi**: (müügipunkt), Paywall (sisu rahaks muutmine), Events (piletimüük), LndHub (server BlueWalletile), Bolt Cards (NFC-maksed), Split Payments (automaatne jaotamine) ja User Manager (kasutajate haldamine koos autentimisega).



**Kaardil** kuvatakse reaalajas saldod, tehingute ajalugu ja arveldustööriistad. Igal Wallet-l on unikaalne URL, mis sisaldab selle API võtmeid, mis võimaldab juurdepääsu ilma traditsioonilise sisselogimiseta. Kolmetasandiline API võtmesüsteem** (admin, Invoice, ainult lugemisõigus) pakub granuleeritud kontrolli õiguste üle turvaliste integratsioonide jaoks.



LNbits rakendab algselt **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) ja toetab **Lightning Address**, tagades ühilduvuse kaasaegsete Lightning-rahakottidega ja hõlbustades professionaalsete teenuste kasutuselevõttu.



## Toetatud platvormid



**Ubuntu VPS**: Kerge lahendus ilma täieliku Bitcoin sõlmpunktita. Eeldused: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + domeeninimi vajalik avalikuks kasutamiseks (LNURL teenused).



**Umbrel**: Lihtne paigaldamine App Store'ist. Eeltingimus: toimiv Umbrel-sõlm koos sünkroniseeritud LND ja avatud kanalitega. Automaatne konfiguratsioon.



Allpool on lingid meie Umbrel ja Umbrel LND õpetustele:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Paigaldamine Ubuntu VPS-i koos PHOENIXD-ga



### Samm 1: VPS-serveri turvamine



** Enne mis tahes paigaldamist** peate oma Ubuntu VPS-serveri kindlustama vastavalt reeglitele. See samm on **kriitiline**, et kaitsta oma infrastruktuuri ja Lightning'i vahendeid.



Siin on üksikasjalik juhend, mis aitab teil alustada: **[Ubuntu serveri esmane konfigureerimine - samm-sammult juhend](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)**, autor Daniel P. Costas.



Selles juhendis käsitletakse kasutajate konfigureerimist, turvalist SSH-d, tulemüüri (UFW), fail2bani, automaatseid uuendusi ja häid süsteemi turvalisuse tavasid.



### 2. samm: PHOENIXD paigaldamine



Kui teie server on turvaline, peate PHOENIXD paigaldama ja konfigureerima. Plan B Network pakub täielikku spetsiaalset õpetust, mis hõlmab paigaldamist, seed genereerimist ja systemd teenuse konfigureerimist:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Kui PHOENIXD on käivitatud ja töötab (kontrollige `./Phoenix-CLI getinfo`ga), märkige **HTTP parool** failis `~/.Phoenix/Phoenix.conf` - seda on vaja LNbits'i ühendamiseks PHOENIXD-ga.



### LNbits kasutuselevõtmine



Paigaldage UV ja kloonige LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigureerige PHOENIXD backend:


```bash
cp .env.example .env && nano .env
```



Lisada faili `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testige `uv run lnbits --host 0.0.0.0 --port 5000`, seejärel looge systemd teenus `Wants=PHOENIXD.service`.



## Esialgne seadistamine ja esmakordne kasutamine



### SuperUser aktiveerimine



Aktiveerige Interface administraator failis `.env` :


```
LNBITS_ADMIN_UI=true
```



Käivitage LNbits uuesti (`sudo systemctl restart lnbits`) ja hankige SuperUser ID:


```bash
cat ~/lnbits/data/.super_user
```



Minge administreerimispaneelile `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>`. Menüüs "Server" saate konfigureerida rahastamisallikad, laiendused ja kasutajakontod.



### Turvaline konto loomine



**Tähtis avaliku kokkupuute jaoks**: Kui te eksponeerite oma LNbits'i instantsi avalikul domeeninimel, millele on juurdepääs internetist, on **kriitiline** keelata kasutajakontode tasuta loomine.



Mine SuperUser administreerimise Interface-st "Seaded" ja seejärel jaotisesse "User Management" (kasutajahaldus). Sealt leiate valiku "Allow creation of new users" (uute kasutajate loomise lubamine).



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Publikule suunatud näituse jaoks koos domeeninimega** :




- Sa pead keelama** valiku "Luba uute kasutajate loomine"
- Ilma selle kaitseta võib igaüks Internetis luua konto teie instantsil
- Ründaja võib luua kontosid ja kasutada teie LIGHTNING NODE likviidsust ilma teie teadmata
- Sa pead looma kasutajakontod käsitsi Interface SuperUserist



**Kasutatakse ainult kohalikul tasandil** :




- See valik on vähem kriitiline, kui teie instantsile on juurdepääs ainult lokaalselt (http://localhost:5000)
- Selle võimaluse keelamine on siiski hea üldine ohutustava



Pärast seadistamist saab ainult SuperUser administraator luua uusi kasutajakontosid Interface "Kasutajad" kaudu. Selline lähenemine tagab täieliku kontrolli selle üle, kes saab teie Lightning-infrastruktuurile ligi ja teie vahendeid kasutada.



### Esimese kanali avamine



PHOENIXD haldab kanaleid automaatselt automaatse likviidsuse kaudu. generate välk Invoice ~30,000 Sats LNbitsist ja maksab selle teisest Wallet. PHOENIXD avab automaatselt kanali ACINQ-le. Avamistasu (~20-23k Sats) arvatakse maha, ülejäänud jääk (~7-10k Sats) ilmub pärast On-Chain kinnitust.



Kontrolli staatust käsuga `./Phoenix-CLI getinfo`. Seejärel kaaluge automaatse likviidsuse väljalülitamist (`auto-liquidity=off` failis `Phoenix.conf`), et kontrollida kanalite avanemist.



### Avalik väljapanek ja HTTPS



**Tähtis**: HTTPS kohustuslik avalikuks kuvamiseks (API võtme turvalisus + LNURL ühilduvus). Jäta see samm vahele ainult kohalikuks kasutamiseks.



**Caddy (soovitatav)**: automaatne SSL. `sudo apt install -y caddy`, redigeeri `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Taaskäivitus: `sudo systemctl restart caddy`.



**Nginx** : Rohkem kontrolli. Installige `nginx certbot python3-certbot-nginx`, looge `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktiveeri: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Lisa faili `.env`: `FORWARDED_ALLOW_IPS=*`



## Vihmavarju paigaldamine



### Kasutuselevõtmine App Store'ist



Mine Umbrel App Store'i, otsi "LNbits" ja klõpsa "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel kontrollib automaatselt vajalikke sõltuvusi. LNbits vajab käivitamiseks LIGHTNING NODE (LND). Kui teie LIGHTNING NODE on juba töökorras, klõpsake kinnitamiseks "Install LNbits".



![Dépendances LNbits](assets/fr/02.webp)



Umbrel laeb alla Dockeri kujutise, konfigureerib automaatselt ühendused LND-ga ja käivitab konteineri (2-5 minutit). Installeerimine toimub täielikult taustal.



### SuperUser'i algne konfiguratsioon



Esimesel käivitamisel palub LNbits teil luua SuperUser administraatori konto. Sisestage kasutajanimi ja määrake turvaline parool, et kaitsta juurdepääsu Interface haldussüsteemile.



![Configuration SuperUser](assets/fr/03.webp)



**Tähtis**: Sellel SuperUser-kontol on teie LNbits'i instantsi täielikud õigused. Valige tugev parool ja hoidke seda turvaliselt.



Kui olete konto loonud, jõuate automaatselt Interface peamise haldusala juurde. Umbrel on juba seadistanud LND teie rahastamisallikana - kõik Lightning-maksed lähevad teie olemasolevate kanalite kaudu.



### Juurdepääs Interface administraatorile



Klõpsake vasakpoolses menüüs "Settings", et pääseda kogu halduspaneelile.



![Interface Settings](assets/fr/04.webp)



Jaotises "Rahakottide haldamine" kuvatakse teie konfiguratsiooni põhiteave:




- Rahastamisallikas** : LndBtcRestWallet (otsene ühendus teie LND Umbrel sõlme)
- Sõlme tasakaal** : Teie Lightning-kanalite kogu likviidsus
- LNbits Balance**: LNbits-süsteemi eraldatud vahendid (algselt 0 Sats)



Nüüd saate otse kasutada oma Umbrel-sõlme likviidsust kõigi loodud LNbits'i rahakottide jaoks. Täiendavat konfigureerimist ei ole vaja - LNbits on käivitatud ja töötab.



### Kasutajate haldamine



Üks LNbits'i kõige võimsamaid funktsioone on võimalus luua mitu sõltumatut kasutajat, kellel kõigil on parooliga autentimine ja eraldi rahakotid. Selline arhitektuur võimaldab kasutada ära teie Umbrel-sõlme likviidsust, pakkudes samal ajal täiesti isoleeritud alamkontosid erinevateks kasutusaladeks: äri, perekond, töötajad, projektid jne.



Külgmenüüs klõpsake "Kasutajad", et pääseda kasutajate haldusse. Uue kasutaja lisamiseks klõpsake nupule "LEE KONTO".



![Gestion des utilisateurs](assets/fr/05.webp)



Täitke kasutaja loomise vorm:




- Kasutajanimi**: Kasutajanimi (näiteks: "Satoshi")
- Määrake salasõna**: Aktiveerige see valik, et määrata autentimise parool
- Parool** ja **Parooli kordus**: Määrake selle kasutaja parool



![Création utilisateur satoshi](assets/fr/06.webp)



Valikulised väljad (Nostr Public Key, E-post, eesnimi, perekonnanimi) võib minimaalse konfiguratsiooni jaoks jätta tühjaks. Kinnitamiseks klõpsake "CREATE ACCOUNT".



![Confirmation utilisateur créé](assets/fr/07.webp)



Teie uus kasutaja ilmub nüüd kasutajate loendisse oma unikaalse identifikaatori ja kasutajanimega.



![Liste des utilisateurs](assets/fr/08.webp)



**Tähtis punkt**: Iga kasutaja saab sisse logida täiesti iseseisvalt oma parooliga. SuperUser administraator säilitab täieliku kontrolli Interface haldustööriista kaudu.



### Kasutaja Wallet haldamine



Nüüd, kui kasutaja "Satoshi" on loodud, tuleb talle määrata Wallet Lightning. Klõpsake asjaomase kasutaja Wallet ikoonil (teine ikoon) ja seejärel "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



Dialoogiboksis palutakse teil anda Wallet-le nimi. Sisestage kirjeldav nimi (nt "Wallet Of Satoshi") ja valige kuvatud valuuta (CUC, USD, EUR jne.).



![Création wallet](assets/fr/10.webp)



Klõpsake nuppu "LOODA". LNbits genereerib koheselt selle kasutaja jaoks toimiva Wallet Lightning'i.



![Confirmation wallet créé](assets/fr/11.webp)



Nüüd näete kahte olemasolevat rahakotti: automaatselt loodud vaikimisi Wallet "LNbits Wallet" ja uut "Wallet Of Satoshi". Kasutajakogemuse lihtsustamiseks saate vaikimisi Wallet kustutada, klõpsates kustutamise ikoonil (punane prügikast).



![Wallet final unique](assets/fr/12.webp)



"Satoshi" kasutajal on nüüd üks, selgelt identifitseeritud Wallet. Iga kasutaja Wallet töötab täiesti iseseisvalt, kasutades samal ajal teie aluseks oleva LND sõlme likviidsust.



**Kontseptsioon**: Kõik need rahakotid jagavad teie Umbreli sõlme globaalset likviidsust. Te ei loo iga Wallet jaoks uusi Lightning-kanaleid - LNbits toimib intelligentse raamatupidamisliku Layer-na, mis haldab raha jaotamist teie olemasolevas Lightning-infrastruktuuris. See ongi LNbits'i mitme Wallet süsteemi jõud.



### Kasutaja sisselogimine



Logige SuperUser-kontost välja (ikoon üleval paremal) ja naaske LNbits'i sisselogimislehele. Nüüd saate uue kasutaja volitustega sisse logida.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Sisestage eelnevalt määratud kasutajanimi ("Satoshi") ja parool, seejärel klõpsake nuppu "LOGIN". Kasutaja saab otsese juurdepääsu oma isiklikule Wallet-le, mis on täielikult isoleeritud administreerimise Interface-st.



### Interface Wallet kasutajalt



Kui kasutaja on ühendatud, saab ta Wallet Lightningist juurdepääsu oma Interface-le.



![Interface wallet utilisateur](assets/fr/14.webp)



Interface omadused:




- Praegune saldo**: Kuvatakse Sats ja valitud valuutas (antud näites CUC)
- Peamised tegevused**: "PASTE REQUEST" (kleebi arve maksmiseks), "CREATE Invoice" (generate kviitung), QR ikoon (kiirskaneerimine)
- Tehingute ajalugu** : Täielik nimekiri kõigist maksetest ja kviitungitest
- Parempoolne külgpaneel**: Konfigureerimis- ja juurdepääsuvõimalused



### Wallet mobiilne juurdepääs



Parempoolne külgpaneel pakub eriti praktilist funktsiooni: mobiilne juurdepääs Wallet-le. Avage jaotis "Mobiilne juurdepääs", et tutvuda olemasolevate võimalustega.



![Mobile Access](assets/fr/15.webp)



LNbits pakub mitmeid võimalusi selle Wallet kasutamiseks nutitelefonis:



**Võimalus 1: Ühilduvad mobiilirakendused




- Lae alla **Zeus** või **BlueWallet** App Store'ist või Google Play'st
- Aktiveerige selle Wallet jaoks LNbitsis **LndHub** laiendus
- LndHubi QR-koodi skaneerimine mobiilirakendusega, et ühendada Wallet



**Võimalus 2: Otsene juurdepääs mobiilibrauseri kaudu**




- "Telefoni eksportimine QR-koodiga" kuvatav QR-kood sisaldab Wallet täielikku URL-koodi koos integreeritud autentimisega
- Skaneeri see QR-kood oma nutitelefoniga, et avada Wallet otse oma mobiilibrauseris
- Lisage leht kiireks juurdepääsuks koduekraanile



**Tähtis turvalisus**: See URL sisaldab API võtmeid, mis võimaldavad täieliku juurdepääsu Wallet-le. Ärge kunagi jagage seda avalikult. Käsitlege seda QR-koodi nagu Bitcoin privaatvõtmeid - igaüks, kes seda QR-koodi skaneerib, saab täieliku juurdepääsu Wallet-le.



See mobiilne funktsioon muudab teie LNbits Umbrel'i instantsi tõeliseks Lightning Wallet serveriks teie ja teie sõprade jaoks, säilitades samal ajal täieliku suveräänsuse oma rahaliste vahendite üle tänu oma isehostitud sõlmpunktile.



### Kasutaja juurdepääsu jagamine



Selle mitme kasutaja konfiguratsiooni peamine kasutusviis on **jagada rahakotte oma pere või lähikondadega**. Kui olete loonud kasutaja, kellel on spetsiaalne Wallet (näiteks "Satoshi" meie näites), saate neid sisselogimise andmeid jagada oma pere usaldusväärsete liikmetega.



**Turvalisuse tagamine Umbrelil**: Juurdepääs teie LNbits'i instantsile Umbrelil on loomulikult kaitstud, kuna sellele saab ligi ainult :




- Teie kohalikus võrgus** : Teie majapidamise liikmed, kes on ühendatud samasse WiFi/Ethernet-võrku, saavad instantsile juurdepääsu
- VPN-i** kaudu: Kui kasutate VPN-i, näiteks Tailscale'i, mis on seadistatud teie Umbreli serverisse, saavad volitatud kasutajad turvalise kaugjuurdepääsu



See topelt Layer kaitse (võrgule juurdepääs + kasutaja autentimine) muudab "Uute kasutajate loomise lubamine" valiku Umbrelil vähem kriitiliseks. Ainult need inimesed, kellel on juba juurdepääs teie võrgule või VPNile, saavad Interface sisselogimisele ligi.



**Tüüpiline stsenaarium**: Looge "isa" konto, "ema" konto, "äri" konto jne. Igal pereliikmel on oma eraldiseisev Wallet Lightning, samas saavad nad kasu teie Umbrel-sõlme ühisest likviidsusest. Lihtsalt jagage kasutajanimi ja parool - kasutaja saab seejärel ühenduse luua mis tahes seadmest teie kohalikus võrgus või Tailscale VPN-i kaudu. Lisateavet leiate meie spetsiaalsest Tailscale'i õpetusest:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Tutvu olemasolevate laiendustega



Pöörduge tagasi Interface SuperUserisse ja avage vasakpoolsel paneelil olev menüü "Laiendused", et avastada kogu LNbits'i laienduse ökosüsteem.



![Extensions disponibles](assets/fr/16.webp)



LNbits pakub rikkalikku kataloogi laiendusi, mis muudavad teie instantsi tõeliseks Lightning-teenuste platvormiks:





- Jukebox**: Sats-powered jukebox süsteem (Spotify maksed)
- Tugipiletid**: Tasuline tugisüsteem (saate Satss küsimustele vastamiseks)
- TPoS**: Turvaline, mobiilne müügiterminal jaemüüjatele
- User Manager**: täiustatud kasutajate ja Wallet haldamine (mida me just kasutasime)
- Sündmused**: Ürituse piletite müük ja valideerimine
- LNURLDevices**: Müügipunktide haldamine, sularahaautomaadid, ühendatud lülitid
- SMTP**: Võimaldab kasutajatel saata e-kirju ja teenida Satss
- Boltkaardid**: NFC-kaartide programmeerimine Lightning tap-to-pay maksete tegemiseks
- NostrNip5**: Loo oma domeenidele NIP5-aadressid
- Jagatud maksed**: Maksete automaatne jaotamine mitme rahakoti vahel



Iga laiendus aktiveeritakse selle Interface abil ühe klõpsuga. Laiendused, mis on märgitud "TASUTA", on tasuta, samas kui mõned on saadaval "TASUTA" versioonidena. Uurige kataloogi, et leida need, mis vastavad teie vajadustele - kas äri, perekonna haldamise või Lightning Network võimalustega eksperimenteerimise jaoks.



## Eelised ja piirangud



**Eelised**: Finantssõltumatus (täielik kontroll fondide/võtmete/andmete üle), arhitektuuriline paindlikkus (kadudeta VPS→Full node migratsioon), professionaalne laiendussüsteem, intuitiivne Interface.



**Piirangud** : Tarkvara on beetaversioonis (ettevaatust summade suhtes), turvalisus on administraatori vastutusel, tundlikke API võtmeid sisaldavad URL-d (HTTPS kohustuslik), mitme kasutaja haldamine eeldab hooldusvastutust.



## Parimad tavad



**Backupid**: seed PHOENIXD/credentials LND, LNbits andmebaas, `.env` failid. Automatiseerida iga päev, hoida väljaspool tootmisserverit, krüpteeritud. Taastamist regulaarselt testida.



**Hooldus**: Regulaarselt kontrollida uuendusi (LNbits, Lightning backend, operatsioonisüsteem). Kontrollige alati enne suuremaid uuendusi versioonimärkusi.





- On Umbrel**: App Store teavitab teid automaatselt uutest versioonidest. Sünkroonige laiendused jaotise "Laienduste haldamine" > "Uuenda kõik" kaudu. Kontrollige SQLite'i andmebaasi lisamist Umbreli automaatsetesse varundustesse.
- VPS**: Uuenda käsitsi `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Jälgige süsteemi logisid: `sudo journalctl -u lnbits -f`.



## Kokkuvõte



LNbits isehosting pakub konkreetset teed rahalise sõltumatuse saavutamiseni. VPS+PHOENIXD pakub kerget lahendust kiirete teenuste osutamiseks, Umbrel täielikku integreerimist olemasoleva Bitcoin sõlme. Skaleeritav arhitektuur võimaldab arengut lihtsast mitme kasutaja Wallet-st keeruliste ärikasutusjuhtumiteni.



Isehostimine eeldab vastutust: varundage seemned, kaitske juurdepääsu, alustage tagasihoidlike summadega. Nende ettevaatusabinõude abil saab LNbitsist Lightning-majanduse kindel lahendus, säilitades samal ajal detsentraliseerituse ja autonoomia.



## Ressursid



### Ametlikud dokumendid




- [LNbits Documentation](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Ametlik paigaldusjuhend](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Ühenduse juhendid




- [Ubuntu serveri algne konfiguratsioon](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) Daniel P. Costas (samm-sammult VPS turvalisus)
- [LNbits + PHOENIXD paigaldamine Ubuntu VPSile](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) Daniel P. Costas (täielik juhend)
- [LNbits Server on Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) poolt Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes