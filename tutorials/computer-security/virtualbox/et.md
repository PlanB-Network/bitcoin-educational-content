---
name: VirtualBox
description: VirtualBoxi installimine Windows 11-le ja esimese VM-i loomine
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian Burneli originaalsel sisul, mis on avaldatud veebilehel [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___




## I. Esitlus



Selles õpetuses õpime, kuidas paigaldada VirtualBoxi Windows 11-le, et luua virtuaalmasinaid, kas Windows 10, Windows 11, Windows Server või mõne Linuxi distributsiooni (Debian, Ubuntu, Kali Linux jne) käivitamiseks.



See VirtualBoxi sissejuhatav õpetus aitab teil alustada selle Oracle'i poolt välja töötatud avatud lähtekoodiga virtualiseerimislahendusega, mis on täiesti tasuta. Hiljem pannakse internetti ka teisi õpetusi, mis viivad teid teemasse sügavamalt sisse.



Kui tegemist on tööjaama virtualiseerimisega, kas siis projekti raames testimise eesmärgil või IT-õpingute ajal, on VirtualBox selgelt hea lahendus. See on ka alternatiiv teistele lahendustele, nagu Hyper-V, mis on integreeritud Windows 10 ja Windows 11 (samuti Windows Server) ja VMware Workstation (tasuline) / VMware Workstation Player (isiklikuks kasutamiseks tasuta).



Minu konfiguratsioon: **Kuid VirtualBoxi saab paigaldada nii Windows 10 (või vanemasse versiooni) kui ka Linuxile. Mis puutub virtuaalmasinatesse, siis VirtualBox toetab väga erinevaid süsteeme, sealhulgas Windows (nt Windows 10, Windows 11, Windows Server 2022 jne), Linux (Debian, Rocky Linux, Ubuntu, Fedora jne), BSD (PfSense) ja macOS.



## II. VirtualBoxi allalaadimine Windows 11 jaoks



VirtualBoxi allalaadimiseks Windowsi masinasse paigaldamiseks on ainult üks hea Address: [VirtualBoxi ametlikul veebisaidil](https://www.virtualbox.org/wiki/Downloads) jaotises "**Downloadid**". Kliki lihtsalt "Windows hosts", et alustada selle käivitatava faili allalaadimist, mis on veidi üle 100 MB suurune.



![Image](assets/fr/025.webp)



## III. VirtualBoxi paigaldamine Windows 11-sse



### A. VirtualBoxi paigaldamine



VirtualBoxi** paigaldamine on lihtne ja protsess on kõikide Windowsi versioonide puhul sama. Alustage, käivitades äsja alla laetud VirtualBoxi käivitatav fail, seejärel klõpsake "**Next**".



![Image](assets/fr/026.webp)



See paigaldus on kohandatav, kuid ma soovitan paigaldada kõik funktsioonid: mis on vaikimisi valik. Allpool oleval pildil näete erinevaid Elements, sealhulgas:





- VirtualBoxi USB-tugi**, et võimaldada VirtualBoxil toetada USB-seadmeid
- VirtualBox Bridged Network**, et integreerida võrgu tugi "Bridge" režiimis (virtuaalmasin saab otseühendust kohaliku võrguga)
- VirtualBox Host-Only Network**, et integreerida võrgutugi "Host-Only" režiimis (virtuaalmasin saab selles režiimis suhelda ainult teie Windows 11 füüsilise hostiga ja teiste virtuaalmasinatega)



Jätkamiseks klõpsake "**Järgmine**".



![Image](assets/fr/001.webp)



Klõpsake "**Ja**", pidades silmas, et **võrk katkestatakse hetkeks teie Windows 11 masinas**, samal ajal kui VirtualBox teeb võrgumuudatusi, et toetada erinevaid võrgutüüpe, sealhulgas sillarežiimi.



![Image](assets/fr/002.webp)



Kui olete kinnitanud, algab paigaldus... Ja ilmub teade "**Kas soovite selle seadme tarkvara paigaldada?**". Märkige valik "**Always trust software from Oracle Corporation**" ja klõpsake "**Install**". VirtualBox peab tegelikult installima teie arvutisse mitu draiverit.



![Image](assets/fr/003.webp)



Paigaldamine on nüüd lõpule viidud! Märkige valik "**Start Oracle VM VirtualBox 6.1.34 after installation**" ja klõpsake tarkvara käivitamiseks "**Click**".



![Image](assets/fr/004.webp)



### B. Lisage laienduspakett



Ametlikul VirtualBoxi saidil (vt eelmist linki) saate endiselt alla laadida ametliku laienduspaketi, mis on kättesaadav jaotises "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**", klõpsates lingil "**Kõik toetatud platvormid**". See pakett võimaldab teil lisada VirtualBoxile lisafunktsioone: selle lisamine ei ole kohustuslik, kuid see võib olla kasulik! Näiteks sisaldab see USB 3.0 tuge VM-des, veebikaamera tuge ja ketta krüpteerimist.



Avage VirtualBox, klõpsake menüüs "**Fail**" ja seejärel "**Settings**".



![Image](assets/fr/005.webp)



Klõpsake vasakul pool "**Väljendused**" (1), seejärel paremal pool nuppu "**+**" (2), et **laadida äsja alla laaditud VirtualBoxi** laienduspakett (3).



![Image](assets/fr/006.webp)



Kinnitage, klõpsates nupule "**Installatsioon**".



![Image](assets/fr/007.webp)



Klõpsake "**OK**": ametlik laienduspakett on nüüd teie VirtualBoxi instantsile paigaldatud!



![Image](assets/fr/008.webp)



Liigume edasi meie esimese virtuaalse masina loomise juurde.



## IV. Esimese VirtualBox VM-i loomine



Uue virtuaalmasina loomiseks VirtualBoxis klõpsake lihtsalt nupule "**Uus**", et käivitada VM-i loomise viisard. Kuna see on esimene kord, kui te VirtualBoxi käivitate, siis tahaksin teile anda veel mõned üksikasjad Interface ja teiste nuppude kohta.





- Seaded**: VirtualBoxi üldine konfiguratsioon (VM-i vaikimisi kaust, uuenduste haldamine, keel, NAT-võrgud, laiendused jne)
- Import**: virtuaalse seadme importimine OVF-vormingus
- Eksport**: olemasoleva virtuaalmasina eksportimine OVF-vormingus, et luua virtuaalne seade
- Lisa**: olemasoleva virtuaalmasina lisamine VirtualBoxi inventari, standardses VirtualBoxi formaadis (.vbox) või XML-vormingus



Vasakul asuv jaotis "**Tööriistad**" annab juurdepääsu **täiustatud funktsioonidele, eelkõige virtuaalvõrgu, aga ka VM-i salvestusruumi haldamiseks**. "**Tööriistade**" kirje alla lisatakse hiljem teie virtuaalmasinad.



![Image](assets/fr/009.webp)



### A. VM-i loomise protsess



**Mäletatavasti toetab VirtualBox paljusid operatsioonisüsteeme, sealhulgas Windows, Linux ja BSD. Selles näites kavatsen ma luua virtuaalmasina Windows 11 jaoks. Mitmed väljad tuleb täita:





- Nimi**: virtuaalmasina nimi (see on nimi, mis kuvatakse VirtualBoxis)
- Masina kaust**: kuhu salvestada virtuaalmasinat, teades, et sellesse asukohta luuakse VM-i nimega alamkaust
- Type**: operatsioonisüsteemi tüüp, sõltuvalt sellest, millist operatsioonisüsteemi soovite paigaldada
- Versioon**: süsteemi versioon, mida soovite paigaldada, antud juhul Windows 11, seega "**Windows11_64**"



Jätkamiseks klõpsake "**Järgmine**".



![Image](assets/fr/010.webp)



Sõltuvalt eelmises etapis valitud operatsioonisüsteemist annab **VirtualBox soovitusi virtuaalmasinale eraldatavate ressursside kohta**. Siinkohal räägime RAM-ist, mida soovite VM-le eraldada. Oletame, et see on 4 GB, sest see on tõepoolest soovitatav Windows 11 puhul, kuid kui Sul on ressursid vähe, siis määra selle asemel 2 GB. **Jätka



**Märkus**: virtuaalmasinale eraldatud ressursse saab hiljem muuta.



![Image](assets/fr/011.webp)



Mis puutub virtuaalsesse Hard-ketti, siis alustame nullist, seega peame valima "**Loo virtuaalne Hard-ketas kohe**", et VM-l oleks salvestusruumi operatsioonisüsteemi paigaldamiseks ja andmete salvestamiseks. Vajutage nupule "**Loo**".



![Image](assets/fr/012.webp)



VirtualBox toetab virtuaalsete Hard-ketaste jaoks kolme erinevat formaati, mis on suur erinevus võrreldes teiste lahendustega, nagu VMware ja Hyper-V. Valida saab kolme formaadi vahel:





- VDI**, ametlik VirtualBoxi formaat
- VHD**, mis on ametlik Hyper-V formaat, kuigi tänapäeval kasutatakse sagedamini uut VHDX formaati
- VMDX** on VMware ametlik vorming nii VMware Workstationi kui ka VMware ESXi jaoks



Kui soovite luua virtuaalmasina, mida kasutatakse ainult selles VirtualBoxi instantsis, valige "**VDI**". Teisest küljest, kui virtuaalne Hard ketas on kavas hiljem Hyper-V hostile lisada, võib olla hea mõte alustada VHD-vorminguga, et vältida selle teisendamist. Klõpsake nuppu "**Next**".



![Image](assets/fr/013.webp)



**Virtuaalne ketas võib olla kas dünaamiline või fikseeritud suurusega**. Kui see on dünaamiline, siis kasvab fail, mis esindab **virtuaalset ketast (siinkohal .vdi fail), kui andmeid kirjutatakse kettale**, kuni see saavutab oma maksimaalse suuruse, kuid see ei kahane, kui andmeid kustutatakse. Seevastu kui see on fikseeritud suurusega, **määratakse kogu salvestusruum kohe (ja seega reserveeritakse)**, mis võimaldab veidi suuremat jõudlust, kuid võtab virtuaalse ketta esmakordsel loomisel kauem aega.



Isiklikult pean VirtualBoxiga testitud virtuaalmasinate jaoks "**Dünaamiliselt eraldatud**" režiimi piisavaks.



![Image](assets/fr/014.webp)



**Järgmiseks tuleb määrata virtuaalse ketta suurus**, pidades silmas, et vaikimisi salvestatakse ketas VM-i kataloogi (seda saab selles etapis muuta). Ma olen Windows 11 nõuetele vastamiseks märkinud 64 GB suuruse, kuid ka siin võib määrata väiksema suuruse. Klõpsa "**Create**", et luua VM!



![Image](assets/fr/015.webp)



Praegusel hetkel on VM meie inventari hulgas, see on konfigureeritud, kuid operatsioonisüsteem ei ole paigaldatud. Me peame VM-i konfiguratsiooni enne käivitamist lõpule viima.



### B. ISO-kujutise määramine VirtualBox VM-le



Windows 11 või mis tahes muu süsteemi paigaldamiseks on vaja paigaldusallikaid. Enamasti kasutame operatsioonisüsteemi paigaldamiseks ISO-vormingus plaadikujutist. **Vajalik on laadida Windows 11 ISO image meie VM-i virtuaalsesse DVD-ajamasse



Klõpsake VirtualBoxi inventaristikus VM-l (1), seejärel nupul "**Konfigureerimine**" (2), mis annab juurdepääsu selle virtuaalmasina üldkonfiguratsioonile. Seda menüüd kasutatakse ressursside haldamiseks (nt RAM-i suurendamine, protsessori seadistamine jne). Klõpsake vasakul "**Storage**" (3), DVD-kettal, kus hetkel on kirjas "**Empty**" (4), seejärel klõpsake DVD-kujulisel ikoonil (5) ja "**Choose a disk file**" (**Valige plaadifail**).



![Image](assets/fr/016.webp)



Valige installeeritava operatsioonisüsteemi ISO-pilt ja klõpsake OK. See on see, mida ma saan:



![Image](assets/fr/017.webp)



Jääge VM-i "**Konfigureerimine**" sektsiooni, mul on veel mõned asjad seletada.



### C. VM võrguühendus



Mine vasakul asuvasse jaotisse "**Võrk**". Selles jaotises saate hallata virtuaalse masina võrku: virtuaalsete võrguliideste arvu (kuni 4 VM-i kohta), MAC Address ja võrgule juurdepääsu režiimi (NAT, sillaga juurdepääs, sisevõrk jne). **Kui soovite, et teie virtuaalmasinal oleks juurdepääs Internetile, valige "NAT" või "Bridge Access "**, kuid see teine režiim nõuab, et teie võrgus oleks aktiivne DHCP-server või peate IP Address käsitsi konfigureerima.



Märkus: Ma tulen võrgu osa juurde tagasi üksikasjalikumalt spetsiaalses artiklis.



![Image](assets/fr/018.webp)



### D. Virtuaalsete protsessorite arv



Nagu füüsiline arvuti, vajab ka virtuaalne masin tööks RAM-i, Hard-ketast ja protsessorit. VM-i loomisel võisite märgata, et nõustaja ei sisaldanud protsessori konfiguratsiooni. Seda saab aga igal ajal konfigureerida vahekaardil "**System**", seejärel "**Processor**", kus saab valida virtuaalsete protsessorite arvu.



Märkus: "**Enable VT-x/AMD-v nested**" valik on vajalik nested virtualiseerimiseks.



Minu puhul on virtuaalmasinal 2 virtuaalset protsessorit:



![Image](assets/fr/019.webp)



**Et kõhkle vaatamast ka teisi konfiguratsioonimenüü jaotisi.



### E. Esimene käivitamine ja operatsioonisüsteemi paigaldamine



Virtuaalmasina käivitamiseks valige see lihtsalt inventariast ja vajutage nupule "**Start**". Avaneb teine aken, mis annab VM-st visuaalse ülevaate.



![Image](assets/fr/020.webp)



Oih, ma saan vastiku vea ja mu virtuaalne masin ei käivitu! Viga on "Login failed for virtual machine..." järgmiste üksikasjadega:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Tegelikult on see normaalne, sest **viirualiseerimise funktsioon ei ole minu arvutis lubatud**! Selle probleemi parandamiseks tuleb arvuti taaskäivitada, et pääseda BIOS-i ja lubada virtualiseerimine.



![Image](assets/fr/021.webp)



Ootamata taaskäivitan oma arvuti ja **rõhutan klahvi "SUPPR", et pääseda BIOSi** (klahv võib sõltuvalt masinast erineda ja võib olla näiteks F2) minu ASUSi emaplaadil. Virtualiseerimise aktiveerimiseks peab minu puhul olema sisse lülitatud "SVM Mode". Ka siin võib emaplaadil ja tootjal nimetus muutuda. Otsi funktsiooni, mis viitab **AMD-V** (AMD protsessori puhul) või **Intel VT-x** (Inteli protsessori puhul).



![Image](assets/fr/022.webp)



Kui see on tehtud, salvestage muudatus ja taaskäivitage füüsiline masin... Seekord saab **VirtualBox käivitada virtuaalmasina** ja laadida Windows ISO image'i, et installeerida operatsioonisüsteem! 🙂 !



![Image](assets/fr/023.webp)



Meie Windows 11 füüsilisel hostil, kuhu on paigaldatud VirtualBox, näeme, et Windows 11 virtuaalmasina kaust sisaldab erinevaid faile.





- VBOX** fail (XML-vormingus), mis vastab VM-i konfiguratsioonile (RAM, CPU jne)
- VBOX-PREV** fail on varukoopia eelmisest konfiguratsioonist
- VDI** fail vastab virtuaalsele Hard kettale dünaamilises režiimis, seega on selle suurus praegu ainult 13 GB, samas kui selle maksimaalne suurus on 64 GB
- NVRAM** fail sisaldab virtuaalse masina BIOSi olekut, mis on samaväärne füüsilise masina mittepüsiva mäluga



![Image](assets/fr/024.webp)



## V. Kokkuvõte



**VirtualBox on nüüd meie Windows 11 füüsilisel masinal käivitatud ja töötab! Jääb üle vaid seda ära kasutada ja luua virtuaalmasinad!** Windows 11 installeerimise juurde VirtualBox VM-i tulen tagasi teises artiklis. Windows 10, Windows Serveri või mõne Linuxi distributsiooni (Ubuntu, Debian jne.) puhul lase end lihtsalt juhendada!