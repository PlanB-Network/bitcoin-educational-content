---
name: Plaan ₿ Akadeemia - Pears App
description: Kuidas paigaldada ja kasutada rakendust Plan ₿ Academy Pears?
---

![cover](assets/cover.webp)


Ilmselt teate juba, et Plan ₿ Academy on suurim Bitcoin-le pühendatud haridusandmebaas, mis koondab kursusi, õpetusi ja tuhandeid avatud lähtekoodiga ressursse. Algselt oli Plan ₿ Academy veebileht. Aga mis juhtuks, kui te ei saaks sellele enam normaalselt ligi, näiteks tsensuuri korral?


Selles õpetuses õpime, kuidas käivitada **Plan ₿ Academy** platvormi tõeliselt tsensuurikindlalt, kasutades **Pears**, peer-to-peer (P2P) tehnoloogiat, mille on välja töötanud **Holepunch** ja mida toetab **Tether**.


Pears on tarkvara, mis võimaldab meil kasutada Plan ₿ Academy platvormi ilma tsentraliseeritud veebisaidile toetumata. Selles õpetuses paigaldame Pearsi teie arvutisse, et pääseda Plan ₿ Academy'le ligi Pearsi kaudu.


Pearsi eesmärk on lihtne: teha võimalikuks veebirakenduste levitamine ja kasutamine ilma tsentraliseeritud infrastruktuurist sõltumata (ei mingeid servereid, hoste, vahendajaid). Teisisõnu, isegi kui pilveteenuse pakkuja sulgeb või riik blokeerib domeeni, elab rakendus edasi võrgu eakaaslaste seas. Selline lähenemisviis võimaldab meie haridusplatvormil, Plan ₿ Academy'l, jääda kättesaadavaks kogu maailmas, ilma ühegi tõrkepunktita.


---

**TL;DR:**



- Paigaldage pirnid;



- Käivitage järgmine käsk, et käivitada Plan ₿ Academy rakendus:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Mis on pirnid?


Pears on samaaegselt jooksutuskeskkond, arendusvahend ja rakendusplatvorm võrdõiguslikele rakendustele. See avatud lähtekoodiga tööriist võimaldab tarkvara koostada, jagada ja käivitada ilma serverite või infrastruktuurita, otse kasutajate vahel. Praktikas tähendab see, et selle asemel, et majutada rakendust keskserveris, muutub iga kasutaja võrgu sõlmpunktiks: ta jagab osa rakendusest ja andmeid teiste eakaaslastega. Kogu süsteem moodustab hajutatud võrgu, kus iga instants teeb koostööd, et teenus oleks kättesaadav.


![Image](assets/fr/01.webp)


See lähenemisviis põhineb Holepunchi poolt välja töötatud modulaarsete tarkvarakomponentide kogumil:



- Hypercore**: hajutatud logi, mis tagab andmete järjepidevuse ja turvalisuse ilma keskse andmebaasita.
- Hyperbee**: Hypercore'ile ehitatud indeks, mis võimaldab andmeid tõhusalt korraldada ja päringuid teha.
- Hyperdrive**: hajutatud failisüsteem, mida kasutatakse rakendusfailide salvestamiseks ja sünkroniseerimiseks kolleegide vahel.
- Hyperswarm** ja **HyperDHT**: võrgukihid, mis võimaldavad peeride leidmist ja ühendusi kogu maailmas ilma keskserverita.
- Secretstream**: otsast-otsani krüpteerimisprotokoll, mis kindlustab suhtlust partnerite vahel.


Neid komponente kombineerides võimaldab Pears luua autonoomseid, krüpteeritud ja hajutatud rakendusi, kus iga kasutaja osaleb aktiivselt võrgus. Selline detsentraliseeritud arhitektuur välistab infrastruktuurikulud, tsensuuririskid ja SPOFid (*Single Points of Failure*).


Pears on välja töötatud Mathias Buus ja Paolo Ardoino (Tetheri tegevjuht ja Bitfinexi tehnoloogiajuht) asutatud ettevõtte Holepunch poolt, mille eesmärk on laiendada peer-to-peer loogikat Bitcoin-st kaugemale. Nende eesmärk on luua "*peeride internet*", kus iga rakendus saab tegutseda ilma loata, ilma serverite ja vahendajateta. Holepunch on juba **Keet** taga, mis on täielikult P2P videokonverentsi- ja sõnumsiderakendus.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*See Pearsi paigaldamise õpetus on jagatud mitmesse ossa sõltuvalt teie operatsioonisüsteemist. Mine otse sinna, mis vastab sinu keskkonnale, et järgida asjakohaseid juhiseid:*



- Linux (Debian)** → jagu **2**
- Aknad** → jagu **3**
- macOS** → jagu **4**


## 2. Kuidas paigaldada Pears Linuxi (Debian)?


Pearsi paigaldamine Debianile on suhteliselt lihtne, kuid eeldab mõningaid eeltingimusi, mida me käesolevas jaotises üksikasjalikult kirjeldame.


### 2.1. Värskenda süsteemi


Enne kõike muud on oluline veenduda, et teie süsteem on ajakohane.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Paigaldage sõltuvused


Pears tugineb mõnele süsteemiraamatukogule, sealhulgas `libatomic1`, mida kasutab Bare JavaScripti tööajamootor. Paigaldage see järgmise käsuga:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Node.js ja npm paigaldamine NVM-i kaudu


Pearsi levitatakse *npm*, *Node.js* paketihalduri kaudu. Kuigi Pears ei sõltu otseselt *Node.jsist*, on see paigaldamiseks vajalik. Soovitatav viis *Node.js* installimiseks Linuxis on *NVM* (*Node Version Manager*), mis võimaldab hallata mitut Node'i versiooni kõrvuti.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Seejärel laadige terminal uuesti, et aktiveerida *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Kontrollige, et *NVM* on korralikult paigaldatud:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Seejärel installige *Node.js* stabiilne versioon (näiteks praegune LTS-versioon):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Veenduge, et *Node.js* ja *npm* on korralikult paigaldatud:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Paigaldage Pears koos npmiga


Kui *npm* on saadaval, saate globaalselt paigaldada oma süsteemi Pears CLI. See võimaldab teil käivitada käsku `pear` mis tahes kataloogist.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Pirnide initsialiseerimine


Pärast paigaldamist käivitage lihtsalt järgmine käsk oma terminalis:


```bash
pear
```


Esimesel käivitamisel ühendab Pears vajaliku komponendi allalaadimiseks peer-to-peer-võrku. See protsess ei sõltu ühestki keskserverist - failid hangitakse otse teistelt eakaaslastelt.


![Image](assets/fr/10.webp)


Kui allalaadimine on lõppenud, käivitage käsk uuesti, et kinnitada, et kõik toimib:


```bash
pear
```


![Image](assets/fr/11.webp)


Kui kõik on õigesti paigaldatud, ilmub Pearsi abimenüü koos kättesaadavate käskude loeteluga.


### 2.6. Katsepirnid koos Keetiga


Et kontrollida, kas Pears on täielikult töökorras, võite käivitada mõne olemasoleva P2P rakenduse, mis on võrgus saadaval, näiteks Holepunchi poolt välja töötatud avatud lähtekoodiga sõnumi- ja videokonverentsitarkvara Keet.


```bash
pear run pear://keet
```


See käsk laeb Keet-rakenduse otse Pearsi võrgust, ilma keskserverit kasutamata. Kui Keet käivitub korrektselt, tähendab see, et teie Pearsi paigaldus on täielikult toimiv.


![Image](assets/fr/12.webp)


Teie Linux-süsteem on nüüd valmis käivitama ja majutama peer-to-peer rakendusi koos Pearsiga.


## 3. Kuidas paigaldada pirnid Windowsis


Pearsi paigaldamine Windowsis on sama lihtne kui Linuxis, kuid nõuab mõningaid spetsiifilisi tööriistu.


*Kui kasutate Linuxi ja olete juba paigaldanud Pearsi, võite otse edasi minna **Sammu 5**.*


### 3.1. Avage PowerShell administraatorina


Kõigepealt käivitage PowerShell administraatori õigustega:



- Klõpsake menüüs Start;
- Sisestage "PowerShell";
- Klõpsake paremal nupul "*Windows PowerShell*";
- Valige "*Andministraatorina käivitamine*".


![Image](assets/fr/15.webp)


### 3.2. Lae alla NVS


Pears paigaldatakse *npm*, *Node.js* paketihalduri kaudu. Windowsis on Holepunchi soovitatud meetodiks *NVS* (*Node Version Switcher*), mis on selles süsteemis stabiilsem kui *NVM*.


PowerShellis käivitage järgmine käsk, et paigaldada *NVS* uusim versioon:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Paigalda Node.js


Pärast installimist taaskäivitage PowerShell, seejärel sisestage järgmine käsk:


```powershell
nvs
```


Te peaksite nägema nimekirja olemasolevatest *Node.js* versioonidest. Valige esimene, vajutades klaviatuuril klahvi `a`.


![Image](assets/fr/17.webp)


*Node.js* on nüüd paigaldatud.


![Image](assets/fr/18.webp)


### 3.4. Kontrollida paigaldusi


Veenduge, et *Node.js* ja *npm* on kättesaadavad:


```powershell
node -v
npm -v
```


Mõlemad käsud peaksid tagastama versiooni numbri.


![Image](assets/fr/19.webp)


### 3.5. Paigaldage Pears koos npmiga


Kui *Node.js* ja *npm* on saadaval, installige **Pears CLI** globaalselt oma süsteemi:


```powershell
npm install -g pear
```


See installib binaarsüsteemi `pear` teie globaalsesse *npm* kataloogi.


![Image](assets/fr/20.webp)


### 3.6. Kontrollida ja initsialiseerida pirnid


Kui paigaldus on lõpetatud, käivitage:


```powershell
pear
```


Esimesel käivitamisel laeb Pears automaatselt alla vajalikud komponendid võrdõigusvõrgustikust. See protsess võib võtta mõne hetke.


![Image](assets/fr/21.webp)


Kui kõik läks hästi, peaks teil ilmuma Pearsi CLI abimenüü koos kättesaadavate alamkäskude loeteluga (run, seed, info...).


### 3.7. Katsepirnid koos Keetiga


Et kontrollida, kas Pears on täielikult töökorras, võite käivitada olemasoleva P2P rakenduse, mis on võrgus saadaval, näiteks Keet - avatud lähtekoodiga sõnumite ja videokonverentside tarkvara, mille on välja töötanud Holepunch.


```bash
pear run pear://keet
```


See käsk laeb Keet-rakenduse otse Pearsi võrgust, ilma et kasutataks mingit keskserverit. Kui Keet käivitub edukalt, tähendab see, et teie Pearsi paigaldus on täielikult toimiv.


![Image](assets/fr/22.webp)


Teie Windowsi süsteem on nüüd valmis käivitama ja majutama Pearsi abil peer-to-peer rakendusi.


## 4. Kuidas paigaldada pirnid macOS-i


Pearsi paigaldamine macOS-i on sarnane Linuxiga, kuid nõuab mõningaid Apple'i keskkonnale omaseid kohandusi. Käime need sammud koos läbi.


*Kui te kasutate Linuxi või Windowsi ja olete juba paigaldanud Pearsi, võite otse edasi minna **Sammu 5**.*


### 4.1. Kontrollige süsteemi eeldusi


Enne paigaldamist veenduge, et *Xcode'i käsurea tööriistad* on teie süsteemi paigaldatud. See pakett pakub vajalikke ehitustööriistu *Node.js* ja selle sõltuvuste jaoks.


Selleks avage terminal, kasutades klahvikombinatsiooni `Cmd + tühikuklahv`, sisestage `Terminal` ja vajutage `Enter`. Seejärel käivitage terminalis paigaldamiseks järgmine käsk:


```bash
xcode-select --install
```


Kui tööriistad on teie süsteemi juba paigaldatud, teavitab macOS teid sellest.


### 4.2. Paigaldage NVM


Pearsi levitatakse *npm*, *Node.js* paketihalduri kaudu. Kuigi Pears ei sõltu toimimiseks otseselt *Node.jsist*, on see paigaldamiseks vajalik. Soovitatav meetod *Node.js* paigaldamiseks macOS-i on *NVM* (*Node Version Manager*), mis võimaldab hallata mitut Node'i versiooni samaaegselt.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Seejärel laadige terminal uuesti, et aktiveerida *NVM*:


```bash
source ~/.zshrc
```


Kui kasutate *zsh* asemel *bash*, käivitage:


```bash
source ~/.bashrc
```


Seejärel kontrollige, et *NVM* on õigesti paigaldatud:


```bash
nvm --version
```


Teie terminal peaks kuvama installitud *NVM* versiooni.


### 4.3. Paigaldage Node.js ja npm


Seejärel installige *Node.js* stabiilne versioon (näiteks praegune LTS-versioon):


```bash
nvm install --lts
```


Kui paigaldus on lõpetatud, kontrollige paigaldatud versioone:


```bash
node -v
npm -v
```


Mõlemad käsud peaksid tagastama versiooni numbri.


### 4.4. Paigaldage Pears koos npmiga


Kui *npm* on saadaval, saate oma süsteemi globaalselt paigaldada Pears CLI. See võimaldab teil käivitada käsku `pear` mis tahes kataloogist.


```bash
npm install -g pear
```


### 4.5. Pirnide initsialiseerimine


Pärast paigaldamist käivitage lihtsalt järgmine käsk oma terminalis:


```bash
pear
```


Esimesel käivitamisel ühendab Pears vajaliku komponendi allalaadimiseks peer-to-peer-võrku. See protsess ei nõua mingit keskset serverit - failid hangitakse otse teistelt eakaaslastelt.


Kui allalaadimine on lõppenud, käivitage käsk uuesti, et kontrollida, kas kõik toimib:


```bash
pear
```


Kui kõik on õigesti paigaldatud, ilmub Pearsi abimenüü koos kättesaadavate käskude loeteluga.


### 4.6. Katsepirnid koos Keetiga


Et kontrollida, kas Pears on täielikult töökorras, võite käivitada P2P rakenduse, mis on juba võrgus olemas, näiteks Holepunchi avatud lähtekoodiga sõnumite ja videokonverentside tarkvara Keet.


```bash
pear run pear://keet
```


See käsk laeb Keeti rakenduse otse Pearsi võrgust, ilma keskserverit kasutamata. Kui Keet käivitub edukalt, tähendab see, et teie Pearsi paigaldus on täielikult toimiv.


Teie macOS-süsteem on nüüd valmis käivitama ja hostima peer-to-peer-rakendusi koos Pearsiga.


## 5. Kuidas kasutada Plan ₿ Academy't pirnide puhul


Kui Pears on paigaldatud ja töötab, saate käivitada platvormi **Plan ₿ Academy** otse P2P võrgu kaudu. Lihtsalt käivitage oma terminalis järgmine käsk (sama käsk töötab Linuxis, Windowsis ja macOSis):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Kui laadimine on lõpetatud, avaneb Plan ₿ Academy teie Pearsi keskkonnas, mis on valmis kasutamiseks nagu algne veebisait, kuid ilma et see sõltuks keskserverist.


![Image](assets/fr/14.webp)


## 6. Kuidas külviplaani ₿ Akadeemia pirnide kohta ₿ Kuidas külviplaani teha


Pearsi võrgus tähendab *seed* rakenduse ümberjaotamine teistele eakaaslastele oma masinast. Praktikas, kui te seed Plan ₿ Academy, muutub teie arvuti andmeallikaks, mis võimaldab teistel kasutajatel rakendust alla laadida, ilma et nad sõltuksid keskserverist.


See mehhanism tugevdab meie rakenduse vastupidavust ja tsensuurikindlust Pearsi võrgus. Mida rohkem on rakendust seed, seda kättesaadavamaks ja detsentraliseeritumaks see muutub, isegi kui mõni algne sõlmpunkt läheb offline.


Plaani ₿ Akadeemia levitamiseks käivitage lihtsalt järgmine käsk:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Kuni see käsk on aktiivne, osaleb teie seade rakenduse failide levitamises. Kui te sulgete terminali, lõpetatakse jagamisprotsess.


Et jätkata külvamist pärast taaskäivitamist, võite käivitada käsu taustal või luua süsteemiteenuse - näiteks systemd-teenus Linuxis, LaunchAgent macOSis või ajastatud ülesanne Windowsis. Need meetodid tagavad, et Plan ₿ Academy rakendus jätkab külvamist automaatselt süsteemi käivitamisel.


Aitäh, et aitate kaasa Plan ₿ Akadeemia detsentraliseeritud levitamisele Pearsil ja aitate muuta Bitcoin hariduse tõeliselt tsensuurikindlaks!