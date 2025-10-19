---
name: Kaart ₿ Akadeemia - Pears App
description: Kuidas paigaldada ja kasutada rakendust Plan ₿ Academy Pears?
---

![cover](assets/cover.webp)



Nagu te ilmselt teate, on Plan ₿ Academy suurim Bitcoin-le pühendatud haridusandmebaas, mis koondab kursusi, õpetusi ja tuhandeid avatud litsentsi alusel avaldatud ressursse. Algselt oli Plan ₿ Academy veebileht. Aga mis juhtuks, kui te ei saaks sellele enam normaalselt ligi, näiteks tsensuuri korral?



Selles õpetuses õpime, kuidas käivitada **Plan ₿ Academy** platvormi tõeliselt inkensuurselt tänu **Pearsile**, mis on **Holepunchi** välja töötatud ja **Tetheri** toetatud peer-to-peer (P2P) tehnoloogia.



Pears on tarkvara, mis võimaldab meil kasutada Plan ₿ Academy platvormi ilma tsentraliseeritud veebisaidile toetumata. Selles õpetuses paigaldame Pearsi teie arvutisse, et pääseda Plan ₿ Academy'le ligi Pearsi kaudu.



Pearsi eesmärk on lihtne: teha võimalikuks veebirakenduste levitamine ja kasutamine ilma tsentraliseeritud infrastruktuurile toetumata (ei mingeid servereid, hoste ega vahendajaid). Teisisõnu, isegi kui pilveteenuse pakkuja sulgeb või mõni riik blokeerib domeeni, elab rakendus edasi võrku kuuluvate eakaaslaste seas. Just selline lähenemine võimaldab meie haridusplatvormil Plan ₿ Academy jääda kättesaadavaks kõikjal maailmas, ilma ühegi tõrkepunktita.



---

**TL;DR :**





- Paigaldage pirnid ;





- Käivitage järgmine käsk, et käivitada Plan ₿ Academy rakendus:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Paigalda pirnid



### 1.1 Mis on pirnid?



Pears on peer-to-peer rakenduste jooksutuskeskkond, arendusvahend ja juurutamisplatvorm. See avatud lähtekoodiga tööriist võimaldab tarkvara koostada, jagada ja käivitada ilma serveri või infrastruktuurita, otse kasutajate vahel. Konkreetselt tähendab see, et selle asemel, et majutada rakendust keskserveris, muutub iga kasutaja võrgusõlmeks, mis jagab osa rakendusest ja andmeid teiste eakaaslastega. Kogu süsteem moodustab hajutatud võrgu, kus iga instants teeb koostööd, et teenus oleks kättesaadav.



![Image](assets/fr/01.webp)



See lähenemisviis põhineb Holepunchi poolt välja töötatud modulaarsete tarkvaraplokkide komplektil:




- Hypercore**: hajutatud logi, mis tagab andmete järjepidevuse ja turvalisuse ilma keskse andmebaasita.
- Hyperbee**: Hypercore'i peal olev indekseerija andmete tõhusaks organiseerimiseks ja sirvimiseks.
- Hyperdrive**: hajutatud failisüsteem, mida kasutatakse rakendusfailide salvestamiseks ja sünkroniseerimiseks kolleegide vahel.
- Hyperswarm** ja **HyperDHT**: võrgukihid, mis võimaldavad tuvastada ja ühendada eakaaslasi kogu maailmas ilma keskserverita.
- Secretstream**: E2E-krüpteerimisprotokoll, mis turvab teabevahetust kahe partneri vahel.



Neid komponente kombineerides võimaldab Pears luua autonoomseid, krüpteeritud ja hajutatud rakendusi, kus iga kasutaja osaleb aktiivselt võrgus. Selline detsentraliseeritud arhitektuur välistab infrastruktuurikulud, tsensuuririskid ja SPOFid (*Single Point of Failure*).



Pearsi arendab ettevõte Holepunch, mille asutasid Mathias Buus ja Paolo Ardoino (Tetheri tegevjuht ja Bitfinexi tehnoloogiajuht) ning mille eesmärk on laiendada peer-to-peer loogikat Bitcoin-st kaugemale. Nende eesmärk on luua "Peer-to-Peer Internet", kus iga rakendus saab töötada ilma autoriseerimata, ilma serverite ja vahendajateta. Holepunch on juba **Keet** taga, mis on täielikult P2P videokonverentsi- ja sõnumsiderakendus.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*See Pearsi paigaldamise õpetus on jagatud mitmesse ossa sõltuvalt teie operatsioonisüsteemist. Mine otse oma keskkonnale vastavasse jaotisse, et järgida asjakohaseid juhiseid :*




- Linux (Debian)** → Osa **1.2.**
- Windows** → Osa **1.3.**
- macOS** → Osa **1.4.**




### 1.2 - Kuidas paigaldada Pears Linuxi (Debian)?



Pearsi paigaldamine Debianisüsteemi on suhteliselt lihtne, kuid nõuab mõningaid eeltingimusi, mida selgitame üksikasjalikult selles jaotises.



#### 1.2.1. Süsteemi uuendamine



Kõigepealt on oluline veenduda, et teie süsteem on ajakohane.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Sõltuvuste paigaldamine



Pears tugineb mitmetele süsteemiraamatukogudele, sealhulgas `libatomic1`, mida kasutab Bare JavaScript runtime. Paigaldage see järgmise käsuga:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Node.js ja npm installimine NVM-i kaudu



Pearsi levitatakse *npm*, *Node.js* paketihalduri kaudu. Kuigi Pears ei sõltu toimimiseks otseselt *Node.jsist*, on see paigaldamiseks vajalik. Soovitatav meetod *Node.js* installimiseks Linuxis on *NVM* (*Node Version Manager*), mis võimaldab hallata mitut Node'i versiooni paralleelselt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Seejärel laadige oma terminal uuesti, et aktiveerida *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Kontrollige, et *NVM* on paigaldatud:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Seejärel installige *Node.js* stabiilne versioon (nt praegune LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Kontrollige *Node.js* ja *npm* installatsioone:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Pearsi paigaldamine npm abil



Kui *npm* on saadaval, saate paigaldada Pears CLI globaalselt oma süsteemi. See võimaldab teil käivitada käsku `pear` mis tahes kataloogist.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Pirnide initsialiseerimine



Pärast paigaldamist käivitage lihtsalt järgmine käsk oma terminalis:



```bash
pear
```



Esimesel käivitamisel ühendab Pears vajaliku komponendi allalaadimiseks peer-to-peer-võrku. See protsess ei nõua keskse serveri olemasolu: failid saadakse otse teistelt eakaaslastelt.



![Image](assets/fr/10.webp)



Kui allalaadimine on lõppenud, käivitage käsk uuesti, et kontrollida, kas kõik toimib:



```bash
pear
```



![Image](assets/fr/11.webp)



Kui kõik on õigesti paigaldatud, kuvatakse Pearsi abi koos kättesaadavate käskude loeteluga.



#### 1.2.6. Pirnide testimine Keetiga



Et kontrollida, kas Pears on täielikult töökorras, võite käivitada P2P rakenduse, mis on juba võrgus olemas, näiteks Keet, Holepunchi avatud lähtekoodiga sõnumi- ja videokonverentsitarkvara.



```bash
pear run pear://keet
```



See käsk laeb Keet-rakenduse otse Pearsi võrgust, ilma et see läbiks keskserverit. Kui Keet käivitub korrektselt, on teie Pearsi paigaldus täielikult toimiv.



![Image](assets/fr/12.webp)



Teie Linux-süsteem on nüüd valmis käivitama ja hostima peer-to-peer rakendusi koos Pearsiga.



### 1.3 - Kuidas paigaldada Pears Windowsis?



Pearsi paigaldamine Windowsis on sama lihtne kui Linuxis, kuid nõuab mõningaid spetsiaalseid tööriistu.



*Kui te kasutate Linuxi ja olete juba paigaldanud Pearsi, võite jätkata otse sammu 2 juurde



#### 1.3.1. Avage PowerShell administraatori režiimis



Kõigepealt käivitage PowerShell administraatori õigustega :




- Klõpsake menüüs Start;
- Tüüp PowerShell ;
- Paremklõpsake paremal nupul "*Windows PowerShell*" ;
- Valige "*Andministraatorina käivitamine*".



![Image](assets/fr/15.webp)



#### 1.3.2. Lae alla NVS



Pears paigaldatakse *npm*, *Node.js* paketihalduri kaudu. Windowsis on Holepunchi soovitatud meetodiks *NVS* (*Node Version Switcher*), mis on selles süsteemis stabiilsem kui *NVM*.



PowerShellis käivitage järgmine käsk, et paigaldada *NVS* uusim versioon :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Node.js installimine



Pärast installimist käivitage PowerShell uuesti ja sisestage järgmine käsk:



```powershell
nvs
```



Te peaksite nägema nimekirja olemasolevatest *Node.js* versioonidest. Valige esimene, vajutades klaviatuuril klahvi `a`.



![Image](assets/fr/17.webp)



*Node.js* on paigaldatud.



![Image](assets/fr/18.webp)



#### 1.3.4. Kontrollida paigaldusi



Veenduge, et *Node.js* ja *npm* on kättesaadavad:



```powershell
node -v
npm -v
```



Mõlemad käsud peavad tagastama versiooni numbri.



![Image](assets/fr/19.webp)



#### 1.3.5. Pearsi paigaldamine npm abil



Kui *Node.js* ja *npm* on saadaval, installige **Pears CLI** globaalselt oma süsteemi:



```powershell
npm install -g pear
```



See installib binaarsüsteemi `pear` teie globaalsesse *npm* kataloogi.



![Image](assets/fr/20.webp)



#### 1.3.6. Kontrollida ja initsialiseerida pirnid



Kui paigaldus on lõpetatud, käivitage :



```powershell
pear
```



Esimesel käivitamisel laeb Pears automaatselt alla vajalikud komponendid võrdõigusvõrgustikust. See protsess võib võtta mõne hetke.



![Image](assets/fr/21.webp)



Kui kõik on läinud hästi, peaksite nägema CLI Pearsi abiekraani koos loeteluga saadaval olevatest alamkäskudest (run, seed, info...).



#### 1.3.7. Pirnide testimine Keetiga



Et kontrollida, kas Pears on täielikult töökorras, võite käivitada võrgus juba olemasoleva P2P rakenduse, näiteks Holepunchi avatud lähtekoodiga sõnumi- ja videokonverentsitarkvara Keet.



```bash
pear run pear://keet
```



See käsk laeb Keet-rakenduse otse Pearsi võrgust, ilma et see läbiks keskserverit. Kui Keet käivitub korrektselt, on teie Pearsi paigaldus täielikult toimiv.



![Image](assets/fr/22.webp)



Teie Windowsi süsteem on nüüd valmis käivitama ja majutama Pearsi abil peer-to-peer rakendusi.



### 1.4. Kuidas paigaldada Pears macOS-i?



Pearsi paigaldamine macOS-i on sarnane Linuxi paigaldamisega, kuid nõuab mõningaid Apple'i keskkonnale omaseid kohandusi. Avastame need sammud koos.



*Kui te kasutate Linuxi või Windowsi ja olete juba paigaldanud Pearsi, võite jätkata otse sammuga 2



#### 1.4.1. Kontrollige süsteeminõudeid



Enne paigaldamist veenduge, et teie süsteemis on olemas *Xcode Command Line Tools*. See pakett pakub vajalikke kompileerimisvahendeid _Node.js_ ja selle sõltuvuste jaoks.



Selleks avage terminal klahvikombinatsiooniga `Cmd + tühikuklahv`, seejärel sisestage `Terminal` ja vajutage klahvi `Enter`. Seejärel saate terminali sisestada selle käsu, et käivitada paigaldus:



```bash
xcode-select --install
```



Kui tööriistad on teie süsteemi juba paigaldatud, teavitab macOS teid sellest.



#### 1.4.2. NVM-i paigaldamine



Pearsi levitatakse *npm*, *Node.js* paketihalduri kaudu. Kuigi Pears ei sõltu toimimiseks otseselt *Node.jsist*, on see paigaldamiseks vajalik. Soovitatav meetod *Node.js* paigaldamiseks macOS-i on *NVM* (*Node Version Manager*), mis võimaldab hallata mitut Node'i versiooni paralleelselt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Seejärel laadige oma terminal uuesti, et aktiveerida *NVM* :



```bash
source ~/.zshrc
```



Kui kasutate *bash*, mitte *zsh*, käivitage :



```bash
source ~/.bashrc
```



Seejärel kontrollige, et *NVM* on paigaldatud:



```bash
nvm --version
```



Terminal peaks tagastama teie süsteemi paigaldatud *NVM* versiooni.



#### 1.4.3 Node.js ja npm paigaldamine



Seejärel installige *Node.js* stabiilne versioon (nt praegune LTS):



```bash
nvm install --lts
```



Kui paigaldus on lõpetatud, kontrollige paigaldatud versioone:



```bash
node -v
npm -v
```



Mõlemad käsud peavad tagastama versiooni numbri.



#### 1.4.4 Pearsi paigaldamine npm abil



Kui *npm* on saadaval, saate paigaldada Pears CLI globaalselt oma süsteemi. See võimaldab teil käivitada käsku `pear` mis tahes kataloogist.



```bash
npm install -g pear
```



#### 1.4.5. Pirnide initsialiseerimine



Pärast paigaldamist käivitage lihtsalt järgmine käsk oma terminalis:



```bash
pear
```



Esimesel käivitamisel ühendab Pears vajaliku komponendi allalaadimiseks peer-to-peer-võrku. See protsess ei nõua keskse serveri olemasolu: failid saadakse otse teistelt eakaaslastelt.



Kui allalaadimine on lõppenud, käivitage käsk uuesti, et kontrollida, kas kõik toimib:



```bash
pear
```



Kui kõik on õigesti paigaldatud, kuvatakse Pearsi abi koos kättesaadavate käskude loeteluga.



#### 1.4.6. Pirnide testimine Keetiga



Et kontrollida, kas Pears on täielikult töökorras, võite käivitada võrgus juba olemasoleva P2P rakenduse, näiteks Holepunchi avatud lähtekoodiga sõnumi- ja videokonverentsitarkvara Keet.



```bash
pear run pear://keet
```



See käsk laeb Keet-rakenduse otse Pearsi võrgust, ilma et see läbiks keskserverit. Kui Keet käivitub korrektselt, on teie Pearsi paigaldus täielikult toimiv.



Teie macOS-süsteem on nüüd valmis käivitama ja hostima peer-to-peer-rakendusi koos Pearsiga.



## 2. Kuidas kasutada Plan ₿ Academy't Pirnidel?



Kui Pears on paigaldatud ja töötab, saate **Plan ₿ Academy** platvormi otse P2P võrgu kaudu käivitada. Lihtsalt käivitage oma terminalis järgmine käsk (see on sama käsk Linuxi, Windowsi ja macOSi jaoks):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Pärast üleslaadimist avaneb Plan ₿ Academy teie Pearsi keskkonnas, mis on valmis kasutamiseks nagu algne veebisait, kuid ilma sõltumiseta keskserverist.



![Image](assets/fr/14.webp)