---
name: DietPi
description: Kerge operatsioonisüsteem, mis on optimeeritud vähese jõudlusega masinatele. Eelistades isehostitavat
---

![cover](assets/cover.webp)



Mitte-tehnilistes ringkondades on sellised kaubamärgid nagu `Odroid`, `Raspberry Pi`, `Orange Pi` või `Radxa` vähe tuntud. Kuid piisab, kui vaadata tehnikaringkondadesse, et leida, et **SBC** arvutid - mis on ehitatud ühele emaplaadile ja on sageli mikroskoopilise suurusega võrreldes üldkasutatavate arvutitega - on muutunud asendamatuks toeks mis tahes isiklikule projektile.



Need on arvutid, mida toodetakse mitmesuguseid mudeleid. Eelistatavalt kasutavad nad Linuxi distributsioone, mis on sageli kohandatud nii, et need jooksevad sujuvalt nendel väheste võimsustega masinatel.



**DietPi ei ole erand**: see on Debianil põhinev operatsioonisüsteem, mis on optimeeritud nii kergeks kui võimalik ja teeb isegi kõige vähem võimekama `SBC` väga kiireks. Üleminek Debian12 Bookwormilt Debian13 Trixie'le just siis, kui see õpetus kirjutati, toetab see nüüd ka avatud lähtekoodiga `RISC-V` protsessoril põhinevaid SBCsid. DietPi on meeldiv avastus, mis väärib edasist uurimist.



## Tugevused



See ei ole Debian'i "tavaline duplikaat" väikestele Raspberry-tüüpi plaatidele. DietPi on:




- Optimeeritud kiirusele ja kergusele**: [võrdlus teiste SBC-distributsioonide Debianiga](https://dietpi.com/blog/?p=888), DietPi on kõiges kergem. DietPi ISO image kaalub vähem kui 1 GB, mis on kaugelt kõige väiksem vanematele Raspberry või Orange PI mudelitele (näiteks) pühendatud versioonide seas. Nõudlus RAM ja CPU ressursside järele on väga väike, nii et see saab alati parima tulemuse ka vanematest tahvlitest.
- Sisseehitatud automaatika ja paigaldusprogrammid**: Spetsiaalsete käskude komplekt aitab kasutajatel jälgida süsteemi ressursse ning automatiseerida ülesandeid programmide installimiseks ja käivitamiseks, versioonide uuendamiseks, varukoopiate tegemiseks ja kõigi logide kontrollimiseks.
- Tugev, eksperimenteerimisele orienteeritud kogukond**: [õpetused](https://dietpi.com/forum/c/community-tutorials/8) ja DietPi kogukonna projektid on ideaalsed selleks, et saada inspiratsiooni tarkvarast, mida saate tänu DietPile ühe klõpsuga paigaldada.



**Et ole kunagi varem olnud lihtsam oma SBC-st iga killuke välja pigistada**.



## Automaatsed funktsioonid iseteeninduse jaoks


Kas soovite eksperimenteerida omaenda serveriga, et kasutada täiustatud võrgulahendusi või vahendeid, et arendada oma Bitcoin teadmisi? DietPi võib olla lahendus, mida olete otsinud. Kuigi paljud inimesed teavad, kuidas hallata oma infrastruktuuri ja käivitada täiuslikult konfigureeritud ja kaitstud servereid, on DietPi sobiv samm neile, kes soovivad alustada nullist.



Selle asemel, et käsitsi täita kõiki keerulisi ülesandeid, mida selline ülesanne nõuab, võimaldab DietPi neid ehitada `viisardiga` ja oma käsurea abil. Siin saate katsetada oma isikliku pilve, _smart home_ seadmete haldamise, automatiseeritud varukoopiate ja crontabiga, aga ka edasijõudnute lahendustega.



![img](assets/en/01.webp)



## Paigaldamine



### Lae alla



DietPi pakub lugematul hulgal ISO-kujutisi, et põletada operatsioonisüsteem paljudele erinevatele seadmetele. Mõned on ainult toetatud: näiteks Raspberry PI5 jaoks mõeldud ISO on veel testimisjärgus, kuid kindlasti leiate oma tahvlile sobiva.



Selle juhendi jaoks valisin selle paigaldamise õhukesele kliendile, nii et valik läks _PC/VM_ ja seejärel _Native PC_. Nende seadmete jaoks on olemas kaks ISO-kujutist, mis erinevad alglaaduri genereerimise poolest. Juhendis kasutatud masin on üsna vana, seega läks valik _BIOS/CSM_ versioonile. Kui sul on uuem masin, siis võib õige versioon olla `UEFI`.



![img](assets/en/02.webp)



Sa jõuad lehele, mis sisaldab `installeerija pilti`, `sha256` ja `allkirju`.



![img](assets/en/03.webp)



Valmistage oma igapäevase arvuti `home` kataloog, et saaksite vajalikud failid alla laadida, kasutades `wget`.



![img](assets/en/04.webp)



Arendaja avalik võti nõudis minimaalset uurimistööd, kuid selle leiad siit: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Kontrollige kataloogi sisu käsuga `ls -la` ja importige MichaIng võti oma võtmehoidlasse käsuga `gpg --import`.



### Kontrollimine ja välk



Lõpuks, see osa, mida ma kõige rohkem soovitan: veenduge allalaaditud ja oma SBC-le paigaldatava operatsioonisüsteemi autentsuses.



![img](assets/en/06.webp)



Kui saite ka käsuga sha256sum tulemuse "Hea allkiri" ja sama Hash kontrolli, võite jätkata ISO flashimist USB-pulgale. Kasutage selleks selliseid rakendusi nagu Whale Etcher.



![img](assets/en/07.webp)



## DietPi paigaldamine



![img](assets/en/09.webp)



Viige mälupulk seadmesse, mis hakkab võõrustama DietPi-d, ja alustage lime Green operatsioonisüsteemi paigaldamist. Selles harjutuses kasutame õhukest klienti, millel on 16 GB RAM-i, 128 GB SSD-plaat operatsioonisüsteemi jaoks ja teine 1 TB suurune andmeketas. Paigaldamine võttis vähem kui 30 minutit, kuid kui te kasutate näiteks Raspberry't, võivad ressursid olla väiksemad ja võtta kauem aega. Paigaldamise ajal näidatakse teile selle kulgu.



![img](assets/en/08.webp)



Kuna DietPi on mõeldud Raspberries'ile ja teistele sarnastele seadmetele, siis on selle tegelik olemus nn `headless` paigaldus, ilma graafilise keskkonnata ja `shsh' ligipääsuga. Juhendis näete hoopis graafilist keskkonda, täpsemalt LXDE-d.



Selle sammu ajal palutakse teil ka otsustada, millist veebibrauserit soovite vaikimisi kasutada, kas Chromium või Firefox. Mõlemad töötavad hästi; kummalgi ei ole mingeid erilisi vastunäidustusi, välja arvatud teie isiklik eelistus.



Lõpupoole võib paigaldaja küsida, kas soovite juba mingeid programme installeerida, kuid siin **nõuandan teil mitte midagi ette laadida**. Te peaksite teadma, et pärast seda sammu palutakse teil turvalisuse huvides muuta kahe kasutaja vaikimisi paroole. Kõige olulisem on, et te peate **seadistama `Global Software Password (GSP)`**, mis tagab kontrollitud juurdepääsu erinevatele tarkvaradele. **Kui te laadite alla mis tahes tarkvara operatsioonisüsteemi paigaldamise ajal, jäävad need ilma `GSP` seadistamata praktiliselt kättesaamatuks**. Pärast `Global Software Password` seadistamist peate neid uuesti deinstallima ja uuesti installima: seetõttu **ei pane midagi sisse, et vältida topelt tööd**. (Ebamugavus on tõenäoline, mitte 100% kindel).



Paigaldamine lõpeb palvega aktiveerida DietPi-Survey, mis on automatiseeritud andmekogumise teenus, mida kasutatakse operatsioonisüsteemi arendamise toetamiseks. Veebisaidi kohaselt aktiveeritakse andmekogumine, kui te laadite alla mis tahes tarkvara DietPi pakutavast automatiseerimisest või kui te uuendate järgmise versioonini. Igaühel on võimalus osaleda (_Opt IN_) või loobuda (_Opt OUT_).



![img](assets/en/23.webp)



Pärast paigaldamise lõpetamist ja sellele järgnevat taaskäivitamist ilmub ekraanile DietPi, nagu te seda seadistate. Õpetuse jaoks valisin, nagu mainitud, graafilise keskkonna `LXDE`. Töölaual leidsin otsetee `htop` käivitamiseks ja avatud terminali.



![img](assets/en/10.webp)



### "Tööriistad" operatsioonisüsteemist



Unustage enamik programme, mida te oma Linuxi distributsioonis kasutate - DietPi on nii optimeeritud, et olete üsna paljud neist välja jätnud. Põhimõtteliselt peaksite paljud käsud käsitsi paigaldama, aga kui te alles proovite, siis pidage kiusatusele vastu ja proovige DietPi automaatikaid testida.



See on kindlasti terminal, mis on esimene kasulik vahend uue operatsioonisüsteemiga alustamiseks, ja see avaneb automaatselt iga kord, kui te selle sisse lülitate.



![img](assets/en/11.webp)



Terminaliekraanil on loetletud rida käske, mille ees on `dietpi-`, mis tähistavad selle operatsioonisüsteemi [tööriistad](https://dietpi.com/docs/dietpi_tools/):




- `dietpi-launcher`: juurdepääsuks operatsioonisüsteemile, failihaldurile jne
- `dietpi-Software`: see on tööriist, mille abil saab paigaldada kogu komplektis juba olemasoleva tarkvara
- `dietpi-config`: juurdepääsuks süsteemi konfiguratsioonidele, isegi kõige arenenumatele.



![img](assets/en/14.webp)



### Varukoopia



Serveri varundamine on rutiinne toiming, mida süsteemiadministraator peaks ette nägema alates esimesest käivitamisest.



DietPi puhul on olemas käsk `dietpi-Backup`, mida ma soovitan teil uurida, et leida ideaalne lahendus: see võimaldab teil seadistada regulaarset varundamist, kas inkrementaalset või mitte, sõltuvalt kasutatavatest rakendustest, ja kõiki võimalusi rutiini kohandamiseks.



![img](assets/en/22.webp)



Valige varukoopia sihtkoht, näiteks teine ketas, käivitades `dietpi-Drive_Manager`, et ühendada sihtketas ja kasutada seda selle funktsiooni jaoks.



## Konfiguratsioon



Self-hosting on soovitatav kogemus kõigile, olgu nad siis uudishimulikud või lihtsalt entusiastid. Kuid serveri ülespanek ja seadistamine hõlmab mõningaid mitte väheolulisi tehnoloogilisi väljakutseid. Siinkohal tuleb appi **DietPi** lihtsus, mis võimaldab teil paari lihtsa sammuga konfigureerida teie vajadustele kohandatud süsteemi.



![img](assets/en/24.webp)



Põhi- ja edasijõudnud seaded, mis on kõik teie käeulatuses ühes Interface käsuga saadaval:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-tarkvara


```