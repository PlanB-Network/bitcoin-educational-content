---
name: Raspberry Pi Zero
description: Kuidas ehitada minimaalne, õhuga eraldatud ja odav arvuti, kasutades Raspberry Pi Zero't ja lisakomplekti.
---
![cover](assets/cover.webp)



Kui te olete Plan ₿ Network lehekülgedel juba mõnda aega käinud, siis olete juba teada saanud, et üks kõige enam propageeritud turvaeeskirju, peaaegu kohustuslik, **on rahaliste vahendite haldamine oma privaatvõtmete offline-salvestamise teel**.



Kui te ei ole seda veel avastanud, leiate kogu selle õpetuse vältel lingid avatud lähtekoodiga allikatele, mille abil saate selle kohta rohkem teada.



Privaatvõtmete offline haldamiseks on seega vaja seadmest, mis on püsivalt võrgust lahti ühendatud, olgu selleks [riistvaraline rahakott](https://planb.network/resources/glossary/hardware-wallet) või airgap-arvuti, mis on pühendatud just sellele funktsioonile.



Kuidas seda teha, kui teil ei ole näiteks võimalik osta riistvara, mis täidab ainult seda ülesannet, kuid te ei taha sellest turvameetmest loobuda?



## Lahendus


Mis oleks, kui ma ütleksin teile, et saate teha õhukese arvuti kujulise offline-seadme, mis on USB-mälupulga suuruse ja kaaluga ning maksab 35 eurot? Kas te ei usuks seda?



Jätka lugemist.



Ma ütlen teile rohkem: lugege kogu aeg läbi. Väljapakutud lahendus on odav, kuid see ei ole just kõige lihtsam. Kõigepealt saate üldise idee, siis otsustate investeerida osa oma ajast isiklikesse uuringutesse ja valite võimalikult rahulikult, kas ja kuidas edasi minna.



## Nõuded


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (ilma igasuguse järelliideta) on alus minimaalse jõudlusega arvuti loomiseks, kuid eelkõige puuduvad sellel Wi-Fi ja Bluetooth kaardid, mis on selle harjutuse eesmärgil hädavajalikud.





- **Maksumus**: umbes 15,00 selle õpetuse kirjutamise ajal (august 2025).
- **Tootmise järjepidevus**: Vaarikas tagab tootmise kuni jaanuarini 2030.



PI Zero ilma Wi-Fi ja Bluetoothita on kahjuks muutunud praktiliselt kättesaamatuks. PI Zero W ja PI Zero 2W alternatiivid on ehk kergemini leitavad. Sellisel juhul saate ühendusfunktsioonid keelata, muutes konfigfaili. Pärast operatsioonisüsteemi paigaldamist peate need elemendid config'ile lisama:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



käesoleva juhendi üks osa näitab teile, kuidas ja kus seda teha. Kui soovite aga tõesti kindel olla, siis leiate veebist mitmeid õpetusi Wi-Fi kiibi eemaldamiseks väikese lõikuriga, mis sobib elektroonikaplaatidega töötamiseks.



**2** Raspberry PI Zero _starter kit_: nagu on tavaks Vaarika maailmas, paljas luud, ilma välise korpuseta. Lisaks tingivad nii väikese tahvli piiratud ressursid välismaailmaga ühendamise võimalusi.



Kui otsustasin jätkata, leidsin [selle komplekti](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) täis lisaseadmeid, et kasutada PI Zero kõiki võimalusi. Tegelikult sisaldab komplekt USB A -> micro USB power Supply, väikest USB-keskust, mini-HDMI -> HDMI adapterit, vaskist jahutusradiaatorit ja alumiiniumist väliskesta. Komplektiga on kaasas ka kruvid ja mutrivõtmed, mida on vaja PI Zero uude korpusesse paigutamiseks.





- **Maksumus**: 19.99 eurot.



**3** See õpetus ei nõua suurte eelarvete kulutamist airgap-arvutile. Te peaksite siiski teadma, et vajate USB-klaviatuuri ja -hiirt (rangelt juhtmega, vältige Bluetoothi) ning monitori. Sõltuvalt teie monitori sisendist, võite vajada mini-HDMI adapterit, mis on PI Zero ainus olemasolev väljund. Lõpuks, vaata Hard, et meil kõigil on kuskil kodus mittejuhtmevaba klaviatuur ja hiir - on aeg Dust neid välja lülitada.



## Täiendav eelarve



**4** Originaalvõimsuse Supply saate Raspberry'st, mis maksab umbes 15,00 eurot.



**5** Mina isiklikult otsustasin, et kasutan starteri komplektis toodud Supply toite, kombineerides seda siiski 3,70 eurot maksva USBA → miniUSB nn `no data` kaabliga.



**6** Micro SD-kaart, millel peab olema vähemalt 32 GB massimälu; kui tööstuslik kvaliteet/tase on parem.



**7** Teil on vaja süsteemi, USB-micro-SD adapterit, nagu see, mida näete pildil. Teie PI Zero operatsioonisüsteem ja selle mälu töötavad tegelikult sellel andmekandjal.



![img](assets/it/06.webp)



## Operatsioonisüsteemi paigaldamine


Enne PI Zero sulgemist soovitan paigaldada operatsioonisüsteemi. Siis saate kohe alguses kontrollida LED-i, mis näitab tööd.



Operatsioonisüsteemi valimiseks ja põletamiseks valisin kõige lihtsama viisi: kasutasin Raspberry `PI Imager` tööriista.



![img](assets/it/01.webp)



Mine [Raspberry Githubi](https://github.com/raspberrypi/rpi-imager/releases), et laadida alla Imageri viimane versioon, valides selle, mis sobib kõige paremini sinu operatsioonisüsteemile (v. 1.9.6 kirjutamise ajal). Märkad, et iga faili kõrval on ka vastava faili räsi. See tuleb meile kasuks kontrollimiseks.



![img](assets/it/02.webp)



Soovitan teil oma isikliku meelerahu huvides kontrollida, millist operatsioonisüsteemi te oma airgap-arvutis kasutate. See annab teile kindluse, et kasutate seaduslikku (mitte pahatahtlikku) versiooni Imagerist ja seega ka Raspi OS-i.



Tehke kontrollimine kohe pärast allalaadimist, kui teie tavaliselt kasutatav masin on ühendatud internetti



Seejärel avage Linuxi terminal ja valmistage allalaadimine ette, luues sellega töötamiseks vajaliku kataloogi `raspios`.



![img](assets/it/19.webp)



Laadige imager oma Linuxi distributsiooni jaoks alla `wget` abil.



![img](assets/it/20.webp)



Lõpuks käivitage faili `sha256sum` käsk ja võrrelge Hash selle Githubis Raspberry poolt pakutava Hash-ga.



![img](assets/it/21.webp)



Või kui teil on Windows, avage Power Shell ja sisestage järgmine käsk:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Saate Hash, mis peab vastama Raspberry Githubis avaldatud Hash-le.



Kui olete allalaadimise kinnitanud, saate Imager'i oma igapäevasesse arvutisse paigaldada ja selle avada. Imager on tööriist, mida vajate operatsioonisüsteemi põletamiseks micro SD-le, mis on PI Zero "süsteemikettaks".



Protsess on äärmiselt lihtne: kõigepealt valige Raspberry seade, mida kavatsete kasutada (seega pöörake tähelepanu Raspi Zero **mudelile**), seejärel operatsioonisüsteemi versioon ja lõpuks micro SD-kaardi paigalduspunkt, kuhu operatsioonisüsteemi flashida.



### Esimene samm



![img](assets/it/03.webp)



### Teine samm



![img](assets/it/07.webp)



**Märkus hästi**: valige `PI OS 32-bit`, mis on ainus, mis töötab koos PI Zero'ga.



### Kolmas samm



![img](assets/it/08.webp)



(Olge väga ettevaatlik ja jätke _Exclude System Drive_ (Süsteemiketta väljajätmine) valikuliseks, et vältida Raspi operatsioonisüsteemi installeerimist oma arvutisse.)



Kui kõik on seadistatud, küsib Imager, kas soovite kasutada kohandatud seadeid. Valige, mida soovite, või klõpsake _No_, et jätkata vaikimisi seadistustega.



![img](assets/it/09.webp)



Kinnitage, et soovite kustutada micro SD sisu



![img](assets/it/10.webp)



Imager hakkab operatsioonisüsteemi mikro SD-le vilkuma, jooksvalt kuvatakse ekraanil jooksva töö edenemisest.



![img](assets/it/11.webp)



Lõpus on automaatne kontroll, ma soovitan teil seda mitte peatada.



![img](assets/it/12.webp)



Lõpuks ilmub ekraanile teade, ja kui kõik õnnestus, näeb see välja nagu pildil kujutatud.



![img](assets/it/13.webp)



Nüüd võid tõesti eemaldada micro SD lugejast ja asetada selle PI Zero pessa. Lülita väike Raspberry sisse ja jälgi LED-i: eeldame, et see on roheline ja vilgub, näidates operatsioonisüsteemi normaalset laadimist, ning seejärel jääb pidevalt põlema. Kui näed muid märke, näiteks kui LED vilgub regulaarselt või on punane, vaata KKK või [toefoorumi lehti](https://forums.raspberrypi.com/).



## Esimene konfiguratsioon


Raspi OS-i esimene käivitamine on tavapärasest veidi aeglasem, sest see peab täitma mitmeid tegelikke paigaldusülesandeid. Aga kui kõik on läinud hästi, siis ilmub tervitusekraan.



![img](assets/it/14.webp)



Geograafilise piirkonna määramiseks, eriti õige klaviatuuri laadimiseks, klõpsake nuppu _Next_. Viimasele pöörake erilist tähelepanu.



![img](assets/it/15.webp)



Vajutage nupule _Next_ ja teil palutakse luua oma kasutaja, märkige oma kasutajatunnused üles ja hoidke need hästi.



![img](assets/it/16.webp)



Nõustaja palub teil valida vaikimisi veebibrauseri, kas Chromium või Firefox; samuti võib ta küsida Wi-Fi-võrgu seadete kohta, kui töötate Zero W või 2W PI-ga. Jätkake ja klõpsake _Skip_.



Mingil hetkel palutakse teil uuendada pardatarkvara ja operatsioonisüsteemi. Valige _Skip_: selle harjutuse jaoks ehitame tegelikult võrguühenduseta masinat, mis peab sellest hetkest alates jääma võrguühenduseta.



Lõpuks võidakse paluda teil lubada `ssh`, kuid keelduge ka sellest sammust, kuna tegemist on Zero airgap IP-ga.



![img](assets/it/17.webp)



Enam ei ole palju muud konfigureerida. Kui olete lõpetanud, taaskäivitage vaarikas, et muudatused jõustuksid.



![img](assets/it/18.webp)



## Uus arvuti Airgap


Pärast taaskäivitamist on teie uus airgap-arvuti valmis. PI Zero näitab teile uut töölauda, millega saate töötada kas graafilise kasutajaliidese või käsurea kaudu.



![img](assets/it/22.webp)



### Esimesed sammud PI Zero W või 2W jaoks


Kui te töötate Raspberry PI Zero W või 2W-seeriaga, siis on teie plaadil olemas Wi-Fi ja Bluetooth kiibid. Esimese seadistamise ajal jätsid te ühenduse seadistamise vahele, seega ei ole PI Zero ühendatud internetti. Nüüd saate need kaks kiipi tarkvara abil püsivalt välja lülitada.



Tegelikult pakub Raspi OS faili `config.txt`, mida saate oma maitse järgi muuta. `config` asub `boot` partitsioonil, kataloogis `firmware` ja seda saab redigeerida ja salvestada `root` õigustega.



Avage terminal vasakul üleval olevast ikoonist ja see muutub `juurtudeks`.(1)



![img](assets/it/23.webp)



(1) Kui Raspi OS ei lasknud teil eelmiste sammude käigus luua `root` parooli, siis soovitan seda teha nüüd, käsuga `passwd`. See, et `root` kasutaja liigub sõltumatult teie isiklikust kasutajast, võib osutuda väga mugavaks taastamisolukordades.



Otsige terminalist faili `config.txt` ja olge valmis seda redaktoriga `nano` muutma.



![img](assets/it/24.webp)



Muutmine tuleks teha kogu `config` allosas, pärast sõnu `[All]`. Just selles punktis lisate õpetuse alguses näidatud `dtoverlay` käsud.



![img](assets/it/25.webp)



Salvestage, sulgege ja käivitage uuesti. Järgmises etapis läheme väikese Vaarika uurimise juurde.



## Mida sellelt seadmelt oodata?


Vaadates [tehnilisi andmeid](https://www.raspberrypi.com/products/raspberry-pi-zero/) Raspberry veebisaidilt, on PI Zero-l ühe tuumaga BCM2835 protsessor ja 512 MB RAM-i, seega ei paista see eriti võimas.



Kuna terminal on kergem, kasutame süsteemi konfiguratsioonide uurimiseks käsurea.



Kui lülitate seadme sisse, näete lühikest vikerkaarevärvilist ekraani, millele järgneb Raspberry tervitussõnum ja vasakus alumises nurgas asuvad käivitamisega seotud tuumasõnumid.



Kui ilmub PI OSi töölaud, avage terminal ja sisestage:



```bash
uname -a
```


See käsk näitab ekraanil hetkel kasutatava tuuma versiooni ja muud teavet.



![img](assets/it/26.webp)



Teavet protsessori ja riistvara kohta saate vaadata ka sisestades:



```bash
lscpu
```



![img](assets/it/27.webp)



Vaata ka `proc/mem/info`.



![img](assets/it/28.webp)



Debiani versiooni ja väljalaske koodnime väljaselgitamiseks:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Kasutage


Kuigi jõudlus tundub piiratud (paberil ja võrreldes tänapäeva masinate võimsusega), on PI Zero võimas, eriti kui terminal.





- Kõigepealt võite minna peamenüüdesse ja saada inspiratsiooni _Add/Remove software_ paneelilt, kust leiate mitmeid utiliite programmeerimiseks ja harjutamiseks. Pea meeles, et seda saab teha ka terminalist, kuid alati `root` õigustega.



![img](assets/it/33.webp)





- Saate selle võrguühenduseta seadme "kasutusele võtta" mitmesuguste konfidentsiaalsete dokumentide salvestamiseks, mis jäävad vajadusel kättesaadavaks, ilma et need kunagi internetti pääseksid.
- Seda konfiguratsiooni saate kasutada generate oma GPG võtmete turvaliseks kasutamiseks.
- Sa võiksid isegi kasutada seda uut "mänguasja" airgap-allkirjaseadmena, [järgides Arman The Parman'i nõuandeid](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Minu teadaolevatest rahakottidest on ainus, mis pakub 32-bitist versiooni, Electrum. Noh: Zero IP nagu me valmistasime seda selles õpetuses, võimaldaks teil hoida privaatseid võtmeid offline seadistatud Wallet airgap, mida me hõlmasime selles õpetuses:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Järeldused


Seadistusel on ilmselt üks suur nõrkus: micro SD on andmekandja, mis võib probleeme tekitada. See on haavatav suure koormuse korral; võib-olla on teil sellega juba kogemusi, kuna kasutate seda koos telefoniga. Pärast kogu tarkvara paigaldamist, mida soovite Zero airgap IP-l kasutada, tehke väärtuslikust micro SD-st hea varukoopia, kasutades selleks teie käsutuses olevat Raspi OS tööriista.



![img](assets/it/34.webp)



Kui teie vajadused kasvavad ja koos nendega ka teie eelarve võimalused, võite uurida teisi Raspberry või sarnaseid lahendusi. Rääkides mälust, pakub näiteks PI 5 võimalust monteerida M2 NVME-ketas, mis on kindlasti vastupidavam kui microSD.



Ärge unustage teha märkmeid ja dokumenteerida iga kommunaaltarkvara paigaldamise sammu, mida kavatsete kasutada võrguühenduseta. **varem või hiljem tuleb välja uuendatud Raspi OS**, mida te kindlasti soovite ära kasutada. Sel hetkel pead sa kõik kustutama ja kõik uuesti tegema (võib-olla uue micro SD-ga 😂).



Harjutus, mida me just tegime, eeldades, et see on ka teie esimene eksperiment, jääb teile kauaks meelde. Alati ei ole võimalik pühenduda riistvara `sisaldatud` operatsioonidele offline, unustamata tähelepanu õhukese masina sisselülitamiseks ja kontrollimiseks aeg-ajalt.



Saite selle siiski tehtud, õnnitlused! Ja te saate seda lahendust soovitada kõigile neile, kes peavad oma eelarvet kokku hoidma.