---
nimi: Nerdminer
kirjeldus: Alusta bitcoinide kaevandamist võimalusega võita peaaegu 0
---

![kaas](assets/cover.webp)

> Seadista oma NerdMiner_v2

Selles juhendis aitame teil läbi teha vajalikud sammud NerdMiner_v2 seadistamiseks, mis on riistvaraseade (ESP-32 S3), mis on pühendatud bitcoinide kaevandamisele.
Ilmselgelt ei saa sellise seadme arvutusvõimsus konkureerida amatöör- või professionaalsete kaevurite ASICutega. Siiski on NerdMiner suurepärane õppevahend, et muuta bitcoinide kaevandamine käegakatsutavaks. Ja kes teab, (palju) õnne korral võite leida ploki ja selle juurde kuuluva preemia. Uudishimulikele vaatame jaotises [Võidu tõenäosuse hinnang](#estimation-de-la-probabilite-de-gain). Võimsuse tarbimise osas kulutab NerdMiner 0.5W; võrdluseks tarbib LED-lamp keskmiselt 20 korda rohkem.

Enne erinevate sammude läbimist loetleme vajaliku varustuse:

- [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- [USB-C toiteallikas](https://amzn.eu/d/gIOot90)
- 3D korpus: kui teil on 3D printer, saate alla laadida [3D faili](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), vastasel juhul võite osta ühe [Silexperience veebipoest](https://silexperience.company.site/NerdMiner_V2-p544379757).
- PC Chrome brauseriga installitud
- internetiühendus
- bitcoin aadress

Samuti võite osta eelmonteeritud NerdMiner komplekti mitmelt edasimüüjalt, nagu:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Esmalt vaatame, kuidas tarkvara ESP-32 S3-le vilkuda, ja seejärel vaatame, kuidas seda taaskäivitada wifi-võrgu muutmiseks. Need sammud on Windowsi kasutajatele, kui kasutate Linuxi OS-i, palun sooritage [eelnevad sammud](#etapes-preliminaires-pour-utilisateurs-linux), et võimaldada teie süsteemil ESP-32 S3 ära tunda.

# NerdMiner_v2 tarkvara paigaldamine

Tarkvara paigaldamine on oluliselt lihtsustatud tänu veebiflasheri kasutamisele.

## 1. samm: Veebiflasheri ettevalmistamine

Esmalt peate minema [online NM2 flasherile](https://bitmaker-hub.github.io/diyflasher/).

Seejärel valige oma ESP-32-le vastav püsivara. Enamasti on see vaikimisi: T-Display S3. Seejärel klõpsake "Flash".

> ⚠️ On oluline, et kasutaksite Chrome brauserit - kuna see võimaldab vaikimisi kasutada flashi ja pääseda juurde teie USB-portidele.

![](assets/webflasher.webp)

## 2. samm: ESP-32 ühendamine

Kui veebiflasher on käivitatud, avaneb hüpikaken, mis näitab brauseri poolt tuvastatud erinevaid USB-porte.
Seejärel saate ühendada oma ESP-32 ja kuvatakse uus port (sel juhul on see ttyACM0 port). Peate selle valima ja klõpsama nupul "ühenda".
![](assets/flasher-port-serial.webp)

Tarkvara laaditakse seejärel teie ESP32-le mõne sekundi jooksul.

![](assets/NM2-sucessfully-installed.webp)

## 3. samm: NerdMineri seadistamine

Teie NerdMineri seadistamine toimub nutitelefoni või arvuti kaudu.
Luba WiFi ja ühenda kohaliku NerdMinerAP võrguga. Kui kasutate nutitelefoni, avaneb seadistusportaal automaatselt. Vastasel juhul sisestage brauseris aadress 192.168.4.1.
Seejärel valige "Seadista WiFi".

Nüüd saate seadistada oma NerdMineri.
Alustage, ühendudes oma WiFi-võrguga, valides oma võrgu nime ja sisestades vastava parooli.

Seejärel saate valida kaevandusbasseini, milles soovite osaleda. Tõepoolest, bitcoinide kaevandamise tööstuses on tavaline ühendada arvutusvõimsus, et suurendada bloki leidmise võimalusi, jagades preemiat proportsionaalselt pakutud hashrate'iga.
NerdMinerite jaoks võite ühenduda ühega neist basseinidest:

| Basseini URL      | Port  | URL                        | Staatus                                 |
| ----------------- | ----- | -------------------------- | --------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Vaikimisi solo ja avatud lähtekoodiga bassein |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Hooldab CHMEX                           |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Hooldab djerfy                          |

Kui olete oma basseini valinud, peate sisestama oma bitcoini aadressi, et saada preemiat juhul (erandkorras), kui blokk leitakse.

Valige ka oma ajavöönd, et NerdMiner saaks õigesti aega kuvada.
Nüüd võite klõpsata "salvesta".

![](assets/wifi-configuration.webp)

Palju õnne, olete nüüd osa Bitcoinide kaevandamise võrgustikust!

## NerdMineri töö

NerdMinerv2 tarkvaral on 3 erinevat ekraani, millele pääsete ligi klõpsates ekraani paremal küljel asuval ülemisel nupul:

- Peaekraan annab juurdepääsu teie NerdMineri statistikale.
- Teine ekraan annab juurdepääsu ajale, teie hashrate'ile, bitcoini hinnale ja bloki kõrgusele.
- Kolmas ekraan annab juurdepääsu globaalse bitcoini kaevandamise võrgustiku statistikale.
  ![](assets/NM2-screens.webp)

Kui soovite oma NerdMineri taaskäivitada, näiteks WiFi-võrgu vahetamiseks, peate vajutama ülemist nuppu 5 sekundit.

Alumise nupu ühekordne vajutamine lülitab teie NerdMineri välja. Kaks korda klõpsates pööratakse ekraani orientatsiooni.

### Eelsammud Linuxi kasutajatele

Siin on sammud, et Chrome tuvastaks teie jadapordi Linuxis.

1. Tuvastage seotud port:

- Ühendage oma ESP-32 arvutiga.
- Avage terminal.
- Sisestage järgmine käsk kõigi portide loetlemiseks:
  - `dmesg | grep tty`
  - või `ls /dev/tty*`
- Veendumaks, et port on õige, võite protseduuri korrata ilma ESP-32 ühendamata.

2. Muutke seotud pordi õigusi:
Vaikimisi võib jadaportidele juurdepääsuks vaja minna root-õigusi, seega teeme need kättesaadavaks, lisades teie kasutaja `dialout` gruppi.
- `sudo usermod -a -G dialout YOUR_USERNAME`, asenda `YOUR_USERNAME` oma kasutajanimega.
  - seejärel logi välja ja uuesti sisse selle kasutajana või taaskäivita süsteem, et tagada grupimuudatuste jõustumine.

Nüüd, kui teie ESP-32 on süsteemi poolt ära tuntud, võite naasta [esimese sammu juurde](#etape-1-preparation-du-webflasher) tarkvara paigaldamiseks.

## Järeldus

Ja ongi kõik! Teie NerdMiner_v2 on nüüd seadistatud ja kasutusvalmis.

Õnnelikku kaevandamist ja edu teie ettevõtmistes!

### Võiduvõimaluse hindamine

Lõbustagem end võiduvõimaluse hindamisega. See hinnang on üldine ja otsib vaid võimaluse suurusjärku.
Bassein, millega NerdMiner saab ühenduda, on ainult "solo mining pool", mis tähendab, et bassein ei ühenda kõikide ühendatud kaevurite hashrate'i, vaid toimib lihtsalt koordinaatorina.
Oletame nüüd, et meie NerdMineril on hashrate umbes 45kH/s.

Teades, et kogu hashrate on umbes 450 EH/s (või 4,5 x 10^20 hashi sekundis), võime arvestada, et järgmise ploki leidmise tõenäosus on 1 100 miljonis miljardis, mis on väga-väga-väga ebatõenäoline. Seega lisaks sellele, et olla hariduslik vahend ja uudishimu objekt, võib NerdMiner toimida ka loteriipiletina bitcoinide kaevandamisel marginaalse elektrikuluga 0,5 W - kuigi nagu me just nägime, on võiduvõimalus naeruväärselt madal. Kuid miks mitte proovida oma õnne?

### Lisainformatsioon

Siin on mõned lingid, kui soovite teemal rohkem lugeda:

- [NerdMiner_v2 projekti leht](http://github.com/BitMaker-hub/NerdMiner_v2)
- [NerdMinerite täielik dokumentatsioon](https://docs.bitwater.ch/nerd-miner-v2/)