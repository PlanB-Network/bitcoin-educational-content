---
name: Dojo
description: Avatud lähtekoodiga Bitcoin-sõlm privaatsuse ja autonoomia tagamiseks
---

![cover](assets/cover.webp)



*See õpetus põhineb [ametlikul Ashigaru dokumentatsioonil](https://ashigaru.rs/docs/), mille ma olen üle võtnud ja laiendanud. Olen kõik lõigud selguse parandamiseks ümber kirjutanud, lisanud täiendavaid üksikasjalikke selgitusi, samuti illustratsioone algajatele, et muuta paigaldamine ja kasutamine arusaadavamaks.*



---

Dojo on avatud lähtekoodiga programm, mis on mõeldud teatavate privaatsusele orienteeritud Bitcoin rahakottide taustserveriks, mis põhineb Bitcoin core sõlmpunktil. Ajalooliselt töötati see välja selleks, et töötada koos Samourai Wallet, mobiilse Wallet-ga, mis pakkus täiustatud privaatsusfunktsioone nagu Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet on nüüdseks pärast selle arendajate arreteerimist suletud, kuid selle kogukonna järeltulija, **Ashigaru Wallet**, on selle üle võtnud ja tugineb jätkuvalt Dojole, et pakkuda täielikku kogemust kasutajatele, kes soovivad Bitcoin kasutamisel säilitada kontrolli oma andmete üle.



![Image](assets/fr/01.webp)



Praktiliselt toimib Dojo väravana teie Wallet ja Bitcoin võrgu vahel. Ilma Dojota peaks kergem mobiilne Wallet tegema päringuid kolmandate osapoolte serveritelt, et saada teavet teie UTXOde ja teie ajaloo kohta või edastada teie tehinguid. See tähendab sõltuvust ja tundlike andmete lekkimist kolmanda osapoole serverile (kasutatud aadressid, summad, maksesagedus jne). Dojo puhul majutate seda serverit ise, mis on otse ühendatud teie enda Bitcoin sõlme. Sel viisil läbivad kõik teie portfellipäringud teie kontrollitud infrastruktuuri, ilma vahendajateta, tugevdades teie konfidentsiaalsust ja suveräänsust.



## Dojo loomise nõuded



Dojo serveri seadistamine ei nõua ülivõimsat masinat. Igaüks, kellel on algtasemel arvuti, stabiilne internetiühendus ja võime jätta see pidevalt (24/7) sisse lülitatud, saab luua toimiva Dojo.



### Valige oma masina tüüp



Võite kasutada :




- sülearvuti ;
- lauaarvuti ;
- mini-PC (nt Intel NUC, Lenovo Thincentre Tiny...).



Igal võimalusel on omad eelised ja puudused:




- Hind: remonditud miniarvuti või lauaarvuti on sageli odavam kui uus sülearvuti.
- Ruumala: Mini-PC võtab vähem ruumi.
- Power Supply: sülearvuti eeliseks on aku, mis tähendab, et erinevalt mini-PC-st ei lülitu see voolukatkestuse korral välja.
- Täiustatavus: barbones võimaldab üldjuhul mälu lisada või Hard ketta hõlpsasti välja vahetada.



Lisateabe saamiseks varustuse valiku kohta soovitan teil läbida see kursus:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Soovitatav varustus



Uut masinat ei ole vaja osta. Ümberehitatud arvuti, millel on allpool esitatud spetsifikatsioonid, annab palju parema jõudluse kui üheplaadiline elektroonika (nagu Raspberry Pi).



**Miinimumnõuded:**




- X86-64 arhitektuur (64-bitine protsessor).
- 2 GHz kahetuumaline protsessor või kiirem.
- vähemalt 8 GB RAM.
- 2 TB või rohkem NVMe SSD (Blockchain ja Bitcoin ning vajalike indeksite salvestamiseks).



**Soovitatav operatsioonisüsteem: **




- Debianil põhinev distributsioon, näiteks Ubuntu 24.04 LTS.



**Soovitatav varustus:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- jne.



Dojo serverit on täiesti võimalik kasutada ka muudel riistvarakonfiguratsioonidel. Parima jõudluse saavutamiseks ja probleemide piiramiseks soovitame siiski järgida ülaltoodud soovitusi.



Selles õpetuses kasutan vana ThinkCentre Tiny't, millel on Intel Pentium Dual-Core G4400T protsessor, 8 GB RAM ja 2 TB SSD.



## 1 - Ubuntu installimine



*Kui soovite paigaldada Dojo seadmesse, mis on juba konfigureeritud, võite selle sammu vahele jätta ja minna otse sammu 2 juurde.*



Kui valitud riistvara on ette valmistatud, on aeg paigaldada operatsioonisüsteem. Võite kasutada praktiliselt ükskõik millist Debiani distributsiooni, kuid soovitan valida Ubuntu LTS-versiooni, kuna see sobib meie eesmärkidele suurepäraselt. Järgnevalt on toodud järgitavad sammud:



### 1.1. looge käivitatav USB-mäluseade



Laadige juba töötavast arvutist (teie tavalisest masinast) alla Ubuntu LTS ISO image [ametlikult kodulehelt](https://ubuntu.com/download/desktop) (kirjutamise ajal `24.04`, aga kui on olemas mõni teine).



![Image](assets/fr/02.webp)



Sisestage sellesse arvutisse vähemalt 8 GB suurune USB-mäluseade, seejärel looge käivitatav võti, kasutades sellist tarkvara nagu [Balena Etcher](https://etcher.balena.io/). Valige äsja alla laaditud Ubuntu ISO-kujutis, valige USB-klahv sihtseadmeks ja alustage seejärel loomise protsessi (olge kannatlik, see võib võtta mitu minutit).



![Image](assets/fr/03.webp)



Sisestage käivitatav USB-mälu väljalülitatud arvutisse (see, millel soovite Dojo't käivitada). Käivitage masin ja vajutage kohe klaviatuuril **F12** või **F10** (sõltuvalt mudelist), et pääseda sissejuhatusmenüüsse. Seejärel valige oma USB-klahv arvuti käivitamisjärjekorras prioriteetseks seadmeks.



![Image](assets/fr/04.webp)



### 1.2. paigaldage operatsioonisüsteem



Ilmub Ubuntu avakuva. Valige "Proovige või installige Ubuntu*".



![Image](assets/fr/05.webp)



Seejärel järgige klassikalist Ubuntu paigaldusprotsessi:




- Valige keel.
- Valige klaviatuuri tüüp.
- Kui olete ühendatud RJ45-kaabli kaudu, ei ole vaja Wi-Fi-ühendust konfigureerida.
- Klõpsake "*Install Ubuntu*" ja märgistage valik, et paigaldada kolmanda osapoole tarkvara (Wi-Fi draiverid, multimeediakoodekid jne).
- Kui nõustaja küsib paigalduse tüüpi, valige "*Ketta kustutamine ja Ubuntu installimine*". **Hoiatus**: see toiming kustutab täielikult ketta sisu. Kontrollige hoolikalt, et valitud ketas vastab Dojo jaoks mõeldud NVMe SSD-le.
- Loo lihtne kasutajanimi (nt "*loic*").
- Määrake masinale nimi (nt "*dojo-node*").
- Määrake tugev parool ja hoidke seda turvaliselt.
- Turvalisuse suurendamiseks lülitage sisse valik "*Paluda sisselogimiseks oma salasõna*".
- Märkige oma ajavöönd, seejärel klõpsake "*Install*".
- Oodake, kuni paigaldus on lõpetatud. Kui see on lõpetatud, käivitub süsteem automaatselt uuesti.
- Eemaldage arvuti taaskäivitamisel USB-installatsiooni võti.



Täpsemat teavet Ubuntu installimise protsessi kohta leiate meie spetsiaalsest juhendmaterjalist :



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. süsteemi uuendamine



Pärast esimest käivitamist avage terminal, kasutades klahvikombinatsiooni ***Ctrl + Alt + T***, ja käivitage süsteemi uuendamiseks järgmised käsud:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Kõrvalhoone paigaldamine



Et Dojo saaks korralikult töötada, peavad teie süsteemis olema teatud tarkvaraplokid. Neid kasutatakse tarkvara hoidlate haldamiseks, kommunikatsiooniks, arhiivide dekompressiooniks ja Dojo käivitamiseks Dockeri konteinerite sees. Kõik need toimingud viiakse läbi terminalis.



### 2.1. Ettevalmistus



Järgmine käsk viib teid tagasi oma isiklikku kausta. See on hea tava enne mitmete installatsioonide käivitamist.



```bash
cd ~/
```



Enne mis tahes tarkvara paigaldamist veenduge, et teie masina tarkvara andmebaas on ajakohane. Nii väldite vananenud versioonide paigaldamist.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. paigaldada kommunaalteenused



Süsteemi tuleb lisada mitu vahendit:




- `apt-transport-https`: võimaldab pakette turvaliselt HTTPS-i kaudu alla laadida
- `ca-certificates`: haldab krüpteeritud ühenduste jaoks vajalikke sertifikaate
- `curl`: failide otsimine internetist
- `gnupg-agent`: GPG võtmete haldamiseks
- software-properties-common`: pakub abivahendeid APT repositooriumide manipuleerimiseks
- `unzip`: ZIP-formaadis failide lahtipakkimine



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Paigaldamise ajal võib süsteem küsida teilt kinnitust. Vajutage klahvi "*y*" ja seejärel "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. paigaldage Torsocks



Torsocks võimaldab teatud käske täita Tor-võrgu kaudu, parandades side konfidentsiaalsust.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. paigaldage Docker ja Docker Compose



Dojo töötab Dockeri konteinerite sees. See tähendab, et iga teenus on isoleeritud iseseisvas keskkonnas, mis lihtsustab hooldust ja turvalisust. Selleks tuleb paigaldada Docker ja tööriist Docker Compose, mis võimaldab hallata korraga mitut konteinerit.



#### Dockeri allkirjastamisvõtme lisamine



Docker pakub oma digitaalallkirja võtit. Selle lisamine kinnitab allalaaditud pakettide autentsust.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Lisatud ametlik Dockeri repositoorium



Järgmisena tuleb süsteemile öelda, kust leida ametlikud Dockeri paketid. See käsk lisab teie paketihalduri konfiguratsiooni uue repositooriumi.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Dockeri ja Docker Compose'i paigaldamine



Dockeri põhikomponendid saab nüüd paigaldada.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Kasutaja autoriseerimine



Vaikimisi saavad Dockeri käivitada ainult administraatori õigustega käsud. Suurema mugavuse huvides soovitan lisada oma praeguse kasutaja gruppi "*docker*". See võimaldab teil kasutada Dockerit, ilma et peaksite iga kord sisestama `sudo`.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Ühe kasutaja loomine (valikuline)



Kui soovite oma süsteemi turvalisust parandada, soovitan teil luua eraldi kasutaja ainult Dojo käivitamiseks. Selline eraldamine piirab riske: kui Dojos tekib turvaprobleem, ei ohusta see otseselt teie põhikontot.



### 3.1. kasutajakonto loomine



Järgmine käsk loob uue kasutaja nimega "*dojo*". Sellel kasutajal on kodukataloog `/home/dojo` ja juurdepääs bash-terminalile. Samuti lisatakse ta sudo gruppi, et võimaldada administraatori käskude täitmist.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Parooli määramine



Oluline on määrata sellele kontole tugev parool. Ideaalis peaksite kasutama paroolihaldurit, näiteks Bitwardenit, et generate pikk, Hard-ga ära arvata kombinatsioon.



```bash
sudo passwd dojo
```



Seejärel palub süsteem teil sisestada valitud salasõna ja seejärel kinnitada see teist korda.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Lubage kasutajal kasutada Dockerit



Et kasutaja "*dojo*" saaks käivitada Dojo käivitamiseks vajalikke konteinereid, tuleb ta lisada Dockeri gruppi. Nii ei pea iga käsu ees olema `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Süsteemi taaskäivitamine



Selleks, et grupi muudatused jõustuksid, tuleb masin uuesti käivitada.



```bash
sudo reboot
```



### 3.5. Logi sisse uue kasutajaga



Kui süsteem taaskäivitub, logige sisse ***dojo*** kasutajanime ja varem määratud parooliga. Kõik edasised sammud tuleb sooritada selle spetsiaalse konto kaudu.



## 4. Laadige alla ja kontrollige Dojo



Enne Dojo installimist tuleb kindlasti veenduda, et failid on pärit ametlikult arendajalt ja et neid ei ole muudetud. See samm tugineb PGP ja hashide kasutamisele, et kontrollida failide autentsust ja terviklikkust.



### 4.1. importida arendaja PGP-võti



Laadige arendaja avalik võti alla Tori kaudu ja importige see oma kohalikku võtmehoidjasse. Seda võtit kasutatakse Dojo failidega seotud allkirjade kontrollimiseks.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. lae alla Dojo uusim versioon



Saate välja pakitud arhiivi, mis sisaldab Dojo lähtekoodi. Selles näites on kõige uuem versioon `1.27.0`: muutke käsku vastavalt [uusim versioon siin ametlikus GitHubi repositooriumis](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Laadige alla sõrmejäljed ja allkiri



Arendajad avaldavad faili, milles on loetletud arhiivide digitaalsed sõrmejäljed, samuti nende PGP-võtmega allkirjastatud faili. Laadige need alla, et oma faile kohapeal võrrelda.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Kontrollige PGP allkirja



Kontrollige, et sõrmejälgede fail on allkirjastatud imporditud võtmega.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Õige tulemus näitab kehtivat allkirja võtmega `E53AD419B242822F19E23C6D3033D463D6E544F6` ja sellega seotud Address `dojocoder@pm.me`. Võib ilmuda hoiatus, et võti ei ole sertifitseeritud: võite seda ignoreerida.



Kui aga allkiri on kehtetu, siis lõpetage kohe paigaldusprotsess ja alustage seda uuesti algusest.



![Image](assets/fr/17.webp)



### 4.5. Kontrollige arhiivi terviklikkust



Arvutage allalaaditud faili SHA256-sõrmejälg, seejärel avage sõrmejälgifail, et võrrelda kahte väärtust.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Kui kaks sõrmejälge on identsed, võite olla kindel, et arhiivi ei ole muudetud. Kui need on erinevad, ei lähe edasi ja kustutage failid.



![Image](assets/fr/18.webp)



### 4.6. Väljavõte ja failide korrastamine



Kui kontrollimine on edukalt lõpule viidud, saate arhiivi lahti pakkida ja valmistada ette Dojo paigaldamiseks mõeldud kausta.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Puhastage mittevajalikud failid



Kustutage ajutised failid ja arhiivid, mida enam ei vajata, et hoida keskkond puhtana.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojo konfiguratsioon



Dojo on backend-server, mis koondab mitu teenust, et suhelda teie portfelliga ja hallata Bitcoin sõlme. Selle konfigureerimine võib olla keeruline, kuid projekt pakub lihtsustatud meetodit, mis installib ja konfigureerib automaatselt järgmised komponendid:




- Dojo (peamine API)
- Bitcoin core (täielik Bitcoin sõlm)
- BTC-RPC Explorer (veeb Block explorer)
- Fulcrum Indexer (plokkide ja tehingute kiire indekseerimine)
- Fulcrum Electrumi server on saadaval Tor-võrgus
- Fulcrum Electrum Server on kohalikus võrgus kättesaadav
- Administratsiooni volitused



### 5.1. haldusvolitused



Erinevatele teenustele juurdepääsu tagamiseks on vaja generate mitu unikaalset identifikaatorit:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Need identifikaatorid **peavad olema unikaalsed** (see on väga oluline: te ei tohi kasutada sama salasõna mitme teenuse jaoks), koosneda ainult numbritest, suurtest ja väikestest tähtedest (tähtnumbrilised) ning olla umbes 40 tähemärki pikk, et tagada kõrge turvalisuse tase. Soovitan veel kord tungivalt kasutada paroolihaldurit.



### 5.2. Juurdepääs konfiguratsioonifailidele



Dojo konfiguratsioonifailid asuvad kaustas `conf/`. Liigutage sellesse kataloogi:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core konfiguratsioon



Avage Bitcoin core konfiguratsioonifail nano tekstiredaktoriga:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Sisestage selles failis genereeritud identifikaatorid:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Kasuta "sinu-ID-täheks" ja "sinu-passwort-täheks" omaenda sisselogimisega (tugeva parooliga).***



Samuti saate kohandada Bitcoin core poolt kasutatava vahemälu suurust, et parandada jõudlust (kui teil on palju RAM-i, võite kasutada isegi rohkem):



```
BITCOIND_DB_CACHE=2048
```



Muudatuste salvestamiseks ja redaktori sulgemiseks :




- vajutage `Ctrl + X
- tüüp `y`
- seejärel vajutage "*Enter*"



### 5.4. MySQL konfiguratsioon



Seejärel avage MySQL andmebaasi konfiguratsioon:



```bash
nano docker-mysql.conf.tpl
```



Palun sisestage oma sisselogimisandmed:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Kasuta "sinu-ID-täheks" ja "sinu-passwort-täheks" omaenda sisselogimistega (tugevate, unikaalsete paroolidega).***



Salvesta samamoodi (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Fulcrum indekseerija konfiguratsioon



Avage järgmine fail:



```bash
nano docker-indexer.conf.tpl
```



Lisage parameetrid Fulcrumi aktiveerimiseks ja integreerige see korrektselt Dojosse :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Edasi on 2 võimalust, sõltuvalt teie konfiguratsioonist. Kui Dojo on paigaldatud teie igapäevasest arvutist eraldi asuvasse masinasse (spetsiaalsesse masinasse, serverisse...), siis sisestage selle IP Address oma kohalikus võrgus, näiteks :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Oma masina kohaliku IP Address leidmiseks avage teine terminal ja sisestage järgmine käsk:



```bash
hostname -I
```



Teine võimalus: kui Dojo töötab otse teie igapäevases personaalarvutis, siis jätke konfiguratsioonifailis juba olemasolev vaikeväärtus :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Salvesta ja lahkuge redaktorist (Ctrl + X, y, *Enter*).



### 5.6. Sõlme teenuse konfiguratsioon



Lõpuks avage Dojo põhiteenuse konfiguratsioon:



```bash
nano docker-node.conf.tpl
```



Palun sisestage oma sisselogimisandmed:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Kasuta "sinu-password-here" omaenda kasutajatunnustega (tugevate, unikaalsete paroolidega).***



![Image](assets/fr/26.webp)



Seejärel aktiveerige kohalik indekseerija:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Salvesta ja lahkuge redaktorist (Ctrl + X, y, *Enter*).



### 5.7. Sisselogimise haldamine



Kui seadistamine on lõpetatud, ei ole vaja kõiki loodud identifikaatoreid salvestada. Ainus, mis tuleb tingimata salvestada, on :



```
NODE_ADMIN_KEY
```



See sisselogimine võimaldab teil hiljem sisse logida Dojo hooldusvahendisse. Kõik teised sisselogimised saab eemaldada oma paroolihaldurist või käsitsi kirjutatud märkmetest. Need jäävad kättesaadavaks Dojo konfiguratsioonifailidest, kui teil peaks neid tulevikus vaja olema.



## 6. Dojo paigaldamine



Selles etapis paigaldatakse ja käivitatakse Dojo teie masinasse. Operatsioon käivitab mitu teenust (Bitcoin core, Fulcrumi indekseerija, Dojo backend jne) ja algatab Blockchain Bitcoin täieliku sünkroniseerimise. See võib võtta mitu päeva, sõltuvalt teie riistvarast ja internetiühendusest.



### 6.1. Kontrollige, et Docker töötab korralikult



Enne paigaldamise alustamist veenduge, et Docker on töökorras. Käivitage järgmine käsk:



```bash
docker run hello-world
```



See käsk laeb alla ja käivitab väikese testkonteineri. Kui kõik toimib õigesti, peaksite nägema teate, mis sarnaneb :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Kui seda teadet ei kuvata, alustage masina taaskäivitamisest käsuga :



```bash
sudo reboot
```



Seejärel logige tagasi oma **dojo** kontole ja käivitage testkäsk uuesti. Kui viga püsib, siis ei ole Docker õigesti paigaldatud. Sellisel juhul minge tagasi sammu `2.4.` juurde Dockeri installimisel ja kontrollige hoolikalt iga käsku.



### 6.2. Mine Dojo paigalduskataloogi



Paigaldamiseks vajalikud skriptid asuvad kaustas `my-dojo`. Liigutage sellesse kataloogi:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Kasutage käsku `ls`, et kontrollida, kas fail `dojo.sh` on olemas. See on peamine skript, mis automatiseerib Dojo paigaldamist ja kõigi selle teenuste käivitamist.



![Image](assets/fr/29.webp)



### 6.3. Alustage paigaldamist



Alustage installimist, käivitades :



```bash
./dojo.sh install
```



Kinnitage paigaldus, vajutades "y" ja seejärel "*Enter*".



![Image](assets/fr/30.webp)



See skript on :




- laadida alla ja käivitada vajalikud Dockeri konteinerid,
- initsialiseerida Bitcoin core ja alustada Blockchain sünkroniseerimist,
- käivitage Fulcrumi indekseerija tehingute ja aadresside jälgimiseks,
- aktiveerida Dojo backend ja selle APId.



Sa näed pidevalt logisid, mis jooksevad mööda, värviliste viidetega nagu `bitcoind`, `soroban`, `nodejs` või `fulcrum`. See kerimine näitab, et Dojo on käivitatud ja hakkab erinevaid teenuseid täitma.



![Image](assets/fr/31.webp)



### 6.4. Logi kuvamisest väljumine



Logid ilmuvad reaalajas teie terminalis. Et naasta käsureale, kui Dojo töötab taustal, kirjutage :



```
Ctrl + C
```



Ärge muretsege: logi kuvamise peatamine ei peata teenuseid. Docker jätkab Dojo käivitamist taustal (ilmselgelt ei pea te arvutit peatama, kui soovite, et IBD jätkuks).



### 6.5. Mõistmine *Initial Block Download* (IBD)



Käivitamisel peab Bitcoin core alla laadima ja kontrollima kogu Blockchain alates 2009. aastast. Seda sammu nimetatakse ***Initial Block Download* (IBD)**. See on oluline, sest see võimaldab Dojo-sõlme kontrollida iga Bitcoin plokki ja tehingut iseseisvalt.



Selle sünkroniseerimise kestus sõltub mitmest tegurist:




- teie protsessori võimsus ja olemasoleva RAM-mälu hulk,
- teie ketta kiirust,
- teie võrgusõlme ühendavate eakaaslaste arv ja kvaliteet,
- teie internetiühenduse kiirus.



Praktikas võtab see toiming tavaliselt aega **2-7 päeva**. Selle aja jooksul võite jätta oma masina pidevalt tööle. Mida kauem masin on sisse lülitatud, seda kiiremini toimub sünkroniseerimine. Soovitan teil regulaarselt kontrollida sünkroniseerimise seisu, vaadates Bitcoin core logisid või kasutades Dojo hooldustööriista, kui see on paigaldatud (vt järgmine punkt).



Et süvendada oma teadmisi IBD ja üldisemalt Bitcoin sõlme toimimise ja rolli kohta, soovitan teil vaadata seda kursust:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Sünkroniseerimise jälgimine



Dojo esmakordsel paigaldamisel peate ootama, kuni kaks peamist toimingut on täielikult lõpetatud: Blockchain Bitcoin (*IBD*) täielik allalaadimine ja selle Blockchain indekseerimine Fulcrumi poolt. Sõltuvalt teie ühendusest ja masina võimsusest võib see võtta mitu päeva. Selle aja jooksul saate jälgida protsessi kulgu, et veenduda, et kõik kulgeb tõrgeteta.



Sünkroniseerimise oleku jälgimiseks on kaks võimalust:




- dojo hooldustööriista (või DMT) kasutamine, mis on lihtne, kuid annab IBD ajal vähe üksikasju;
- otsene konsulteerimine Dojo logidega teie masinas, mis on tehnilisem, kuid palju täpsem.



### 7.1. Kontrollige Dojo hooldustööriista (DMT) kaudu



Dojo hooldustööriist on turvaline veebipõhine Interface, mis võimaldab teil jälgida oma tehase seisundit ja teostada teatud toiminguid. See on kõige lihtsam ja kättesaadavam viis IBD töö edenemise jälgimiseks. Esialgses sünkroonimisfaasis võib kuvatav teave olla piiratud. Näiteks DMT ei näita Fulcrumi indekseerimise üksikasjalikku edenemist. Teisalt, kui sünkroniseerimine on lõpule viidud, näitab DMT selgelt :




- kõik tuled Green peal;
- iga teenuse (Node, Indexer, Dojo DB) viimane valideeritud plokk.



Et sellele ligi pääseda, peate teadma oma DMT URL-i ja ühenduma sellega [Tori brauseri kaudu](https://www.torproject.org/download/). Selleks avage terminal ja minge kataloogi `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Seejärel käivitage järgmine käsk:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Seejärel on teil juurdepääs kogu teabele, mis on seotud teie Dojoga ühenduse loomisega Tori kaudu. Meid huvitab siinkohal järgmine URL:



```
Dojo API and Maintenance Tool =
```



DMT-le juurdepääsu saamiseks ükskõik millisest masinast mis tahes võrgus (isegi eemalt) avage Tor Browser ja sisestage see URL, millele järgneb `/admin`. Näiteks kui teie URL on `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, peate sisestama [Tor Browser](https://www.torproject.org/download/) riba:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Palume hoida see Address rangelt konfidentsiaalsena



Seejärel suunatakse teid ümber autentimislehele. DMT-sse logitakse sisse, kasutades varem loodud `NODE_ADMIN_KEY` parooli.



![Image](assets/fr/33.webp)



Kui olete sisse loginud, saate juurdepääsu *Dojo hooldustööriistale*! IBD ajal näete menüüs "*Full node*" teavet "*Viimane plokk*", mis annab teile teada teie Bitcoin sõlme hetkeseisu.



![Image](assets/fr/34.webp)



Ärge unustage, et see Address oleks Tor Browseris järjehoidja, et seda hiljem hõlpsasti üles leida.



Kui teie Dojo on täielikult sünkroonitud, peaksite nägema Green kontrolli ✅ kõigil DMT avalehel olevatel näitajatel.



### 7.2. Kontrollimine Dojo logide kaudu



Teine võimalus IBD edenemise jälgimiseks on vaadata otse masinalogisid. See lähenemisviis pakub palju täpsemat reaalajas jälgimist. Näete, kuidas Bitcoin core edeneb plokkide allalaadimine ja kuidas Fulcrum neid indekseerib.



Ühendage oma Dojo't haldav masin ja avage terminal. Kõik käsud tuleb käivitada kataloogist `my-dojo`. Asetage end sellesse kausta:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core logid



Vaadake Bitcoin core logisid, et jälgida IBD arengut:



```bash
./dojo.sh logs bitcoind
```



Alguses näete plokkide päiste sünkroniseerimise eelset faasi:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Kui see näitaja jõuab 100%-ni, alustab Bitcoin core Blockchain täielikku allalaadimist. Te näete IBD edenemist. Praeguse ploki kõrguse teada saamiseks vaadake väärtust, mis on märgitud `height=`. Võite jälgida ka võtit `progress=`, mis näitab IBD edenemise protsenti.



![Image](assets/fr/36.webp)



Nagu alati, kasutage logide sulgemiseks ja käsureale naasmiseks klahvikombinatsiooni `Ctrl + C`.



#### Fulcrum logid



Kui Bitcoin core on lõpetanud päise eel-sünkroniseerimise, alustab Fulcrum Blockchain indekseerimist jooksvalt. Vaadake selle logisid :



```bash
./dojo.sh logs fulcrum
```



Seejärel näete viimase indekseeritud ploki kõrgust, mis on märgitud pärast `height:`, samuti indekseerimise progressi protsent.



![Image](assets/fr/37.webp)



### 7.3. Fulcrumi andmebaasi rikkumine



Fulcrum on eriti võimas indekseerija, kuid selle paigaldamine võib olla keeruline, mitte ainult selle delikaatse andmebaasi haldamise tõttu. Elektrikatkestuse või masina ootamatu väljalülitamise korral esialgse sünkroniseerimise ajal võib indekseerija andmebaas kahjustada. Seda näete näiteks järgmiste logide puhul:



```bash
fulcrum | The database has been corrupted etc...
```



**Märkus:** Selline viga peaks olema parandatud Fulcrum 2.0 eelseisva versiooniga.



Kui see juhtub teiega, ei mõjuta see bitcoind (teie Bitcoin sõlme): selle IBD jätkab kulgemist Fulcrumist sõltumatult. Kuid te ei saa Fulcrumi kasutada enne, kui olete kustutanud selle vigastatud andmed ja alustanud sünkroniseerimist uuesti algusest. See toimib järgmiselt:



Lõpeta Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Kustutage ainult Fulcrumi konteiner ja maht:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Tavaliselt on nimi `my-dojo_data-fulcrum`, kui see ei ole teie puhul nii, kohandage eelmise käsuga tagastatud nime.



Seejärel taaskäivitage Dojo ja ehitage Fulcrum nullist uuesti üles:



```bash
./dojo.sh upgrade
```



Seejärel saate kontrollida, et Fulcrum töötab korralikult, vaadates logisid:



```bash
docker logs -f fulcrum
```




## 8. Dojo hooldustööriista kasutamine



Kui teie Bitcoin sõlme on sünkroniseeritud kõige Proof of Workga ja Blockchain on Fulcrumi poolt 100% indekseeritud, võite alustada oma Dojo kasutamist.



Teie Dojo pakub laia valikut funktsioone, mida täiustatakse regulaarselt iga uue versiooniga. Minu arvates on 2 kõige olulisemat :




- võimalus ühendada oma Ashigaru Wallet, et kasutada oma sõlme Blockchain andmetega tutvumiseks ja tehingute edastamiseks,
- ja Block explorer, mis annab teile juurdepääsu teabele Blockchain Bitcoin kohta, ilma et teie andmed oleksid avatud välisele instantsile, mida te ei kontrolli.



Uurime, kuidas neid kasutada.


### 8.1. Ühendage Ashigaru oma Dojoga



Ashigaru Wallet ühendamine Dojoga on väga lihtne: kui olete DMT-s, avage menüü "*Paaristamine*". Ilmub QR-kood, mida saate skaneerida otse Ashigaru rakendusega.



![Image](assets/fr/38.webp)



Kui käivitate rakenduse Ashigaru esimest korda pärast Wallet loomist või taastamist, suunatakse teid ümber lehele "*Configure your Dojo server*". Vajutage "*Scan QR*", seejärel skaneerige oma DMT-l kuvatavat QR-koodi.



![Image](assets/fr/39.webp)



Seejärel klõpsake nupule "*Jätka*".



![Image](assets/fr/40.webp)



Nüüd olete ühendatud oma Dojoga.



![Image](assets/fr/41.webp)



### 8.2. Block explorer kasutamine



Dojo installib automaatselt Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), mis kasutab otse teie enda Bitcoin sõlme andmeid. Explorer võimaldab teil pääseda ligi Blockchain ja teie Mempool toorele teabele Interface hõlpsasti mõistetava veebi kaudu. Nii saate näiteks hõlpsasti kontrollida poolelioleva tehingu staatust, vaadata Address saldot või uurida ploki koostist.



Selleks, et sellele ligi pääseda, lihtsalt kutsuge Tor Address oma brauserist üles. Selleks käivitage sama käsk, mida kasutasite oma DMT Address hankimiseks:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Teil on juurdepääs kogu oma Dojo ühendusinfole Tori kaudu. Meid huvitab siinkohal järgmine URL:



```
Block Explorer =
```



Kui olete juba ühendatud oma DMT-ga, leiate selle Address ka menüüst "*Paaride*", mis asub ühenduse JSONi sees:



![Image](assets/fr/43.webp)



Selleks, et pääseda oma brauserile ligi mis tahes masinast mis tahes võrgus (isegi eemalt), avage [Tor Browser](https://www.torproject.org/download/) ja sisestage äsja leitud URL-aadress.



⚠️ **Palume hoida seda Address rangelt konfidentsiaalsena



Seejärel on teil juurdepääs oma Block explorer-le.



![Image](assets/fr/44.webp)



*Pildi krediit: https://ashigaru.rs/.*



Tehingu jälgimiseks sisestage lihtsalt selle txid paremal üleval asuvasse otsinguribale.



![Image](assets/fr/45.webp)



*Pildi krediit: https://ashigaru.rs/.*



Address-ga seotud liikumiste kontrollimiseks toimige samamoodi, sisestades Address otsinguribale.



![Image](assets/fr/46.webp)



*Pildi krediit: https://ashigaru.rs/.*



Üksikasjade kuvamiseks saate sisestada otsinguribale ka ploki Hash või kõrguse.



![Image](assets/fr/47.webp)



*Pildi krediit: https://ashigaru.rs/.*



## 9. Dojo hooldus



### 9.1 Peatage oma Dojo



Ärge kunagi katkestage järsku oma Dojo voolu, sest see võib kahjustada teatud andmebaase, eriti Fulcrumi indekseerija. Kui peate selle siiski välja lülitama, siis lülitage Dojo alati puhtalt välja ja seejärel, kui kõik protseduurid on lõpetatud, lülitage ka masin välja:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Uuenda oma Dojo't



Dojo areneb regulaarselt ja uued versioonid ilmuvad, et parandada vigu, parandada stabiilsust ja lisada funktsioone. Seetõttu on oluline [kontrollida regulaarselt uuendusi](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) ja uuendada oma Dojo't. Protsess on sarnane esialgse paigaldamisega, kuid nõuab teatud failide asendamist uusima kättesaadava versiooniga, säilitades samal ajal oma konfiguratsiooni. Siin on üksikasjalikud sammud, mida tuleb järgida puhta ja turvalise uuenduse tegemiseks:



Dojo praeguse versiooni väljaselgitamiseks käivitage käsk :



```bash
./dojo.sh version
```



Kuigi see samm on vabatahtlik, soovitan alustada operatsioonisüsteemi uuendamisega. See vähendab ühildamatuse ohtu ja tagab, et Dojo poolt kasutatavad sõltuvused on ajakohased:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Mine Dojo kataloogi ja lõpeta praegused teenused:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Seejärel taaskäivitage oma süsteem, et saada puhtaks:



```bash
sudo reboot
```



Dojo on varustatud digitaalselt allkirjastatud failidega. Need PGP-allkirjad tagavad, et failid pärinevad arendajalt ja neid ei ole mingil viisil muudetud. Oluline on neid kontrollida iga kord, kui uuendate Dojo't, nagu te tegite seda ka Dojo esmakordsel paigaldamisel. Alustage arendaja avaliku võtme allalaadimisega Tori kaudu, seejärel importige see :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Pöörduge tagasi oma isiklikku kataloogi:



```bash
cd ~/
```



Laadige Dojo uusim versioon GitHubist alla Tori kaudu. Selles näites on see versioon `1.28.0` (mida ei ole veel olemas selle kirjutamise ajal: see on lihtsalt näide). Ärge unustage asendada fail ja link [soovitud versiooniga](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Laadige alla ka fail, mis sisaldab PGP-sõrmejälgi ja -allkirja (jällegi, ärge unustage, et kohandate käsus versiooni):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Kontrollige, et allalaaditud sõrmejälgifail on allkirjastatud arendaja võtmega:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Õige tulemus peaks kuvama :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Võib ilmuda hoiatus, et võti on sertifitseerimata, kuid see ei ole oluline. Kui aga allkiri on kehtetu või vastab mõnele teisele võtmele, ei lähe edasi ja alustage uuesti, kontrollides linke.



Seejärel arvutage SHA256 sõrmejälg arhiivist ja võrrelge seda ametliku sõrmejälgifailiga :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Kui kaks sõrmejälge sobivad ideaalselt, on arhiiv ehtne ja puutumatu. Kui need erinevad, kustutage failid kohe ja ärge jätkake.



Pakige arhiiv oma kodukataloogis lahti:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Seejärel kopeeri sisu Dojo kataloogi, asendades vana :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



See toiming säilitab teie konfiguratsioonifailid, mis asuvad aadressil `~/dojo-app/docker/my-dojo/conf`, kuid asendab kõik teised failid uuendatud versioonidega.



Keskkonna puhtana hoidmiseks kustutage mittevajalikud failid :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Pöörduge tagasi Dojo skriptide kataloogi ja käivitage käsk update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



See käsk annab Dockerile korralduse ehitada kujutised uute failidega ümber, seejärel taaskäivitatakse automaatselt kõik teenused. Protsessi lõpus kontrollige logisid, et veenduda, et Bitcoin core, Fulcrum ja Dojo töötavad korrektselt:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Kui teenused käivituvad ilma vigadeta ja logid näitavad, et plokke töödeldakse, on teie Dojo nüüd ajakohane ja töökorras.