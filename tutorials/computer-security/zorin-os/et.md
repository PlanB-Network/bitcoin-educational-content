---
name: Zorin OS
description: Täielik juhend Zorin OS-i paigaldamiseks ja kasutamiseks Windowsi kaasaegse alternatiivina
---

![cover](assets/cover.webp)



## Sissejuhatus



Operatsioonisüsteem (OS) on põhitarkvara, mis võimaldab arvuti toimimist: see haldab riistvara, tarkvara, turvalisust ja kasutajaliidest.


Zorin OS on Linuxi distributsioon, mis on loodud spetsiaalselt selleks, et hõlbustada üleminekut Windowsilt, pakkudes samal ajal avatud lähtekoodiga tarkvara eeliseid: turvalisus, stabiilsus, privaatsus ja jõudlus.



Ubuntu LTS-il põhinev Zorin OS ühendab endas suure tarkvara ühilduvuse ja tuttava, kohandatava kasutajaliidese, mis teeb sellest usaldusväärse ja kättesaadava alternatiivi Windowsile.



## Miks Zorin OS?





- Interface tuttav**: Windowsi sarnane välimus (stardimenüü, tegumiriba)
- Lihtne üleminek**: mõeldud kasutajatele, kes tulevad Windowsist
- Tõhustatud turvalisus**: Linuxi arhitektuur, vähem avatud viirustele
- Eraelu puutumatuse austamine**: ei mingit sekkuvat andmekogumist
- Optimeeritud jõudlus**: töötab hästi tagasihoidlikel masinatel
- Ubuntu LTS** baas: stabiilsus, korrapärased uuendused ja laialdane ühilduvus
- Täiustatud isikupärastamine**: Zorin Appearance'i tööriista abil.



## Paigaldamine ja konfigureerimine



### 1. Eeltingimused



**Vajalikud seadmed:**





- Vähemalt **8 GB suurune USB-mälu** (soovitatav on 12 GB);
- Arvuti, millel on vähemalt **25 GB vaba kettaruumi**
- Internetiühendus (soovitatav).



### 2. Lae alla Zorin OS





- Külastage ametlikku veebisaiti: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Valige **Zorin OS Core** (soovitatav tasuta versioon)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- ISO-kujutise allalaadimine



Zorin OS pakub ka :





- Zorin OS Lite** (vanemad arvutid)
- Zorin OS Pro** (tasuline, täiustatud funktsioonide ja toetusega)



## Käivitatava USB-klahvi loomine



Saate kasutada mitmeid vahendeid, näiteks Balena Etcher :





- Lae alla ja paigalda [Balena Etcher](https://etcher.balena.io/).
- Avage Balena Etcher, seejärel valige Zorini ISO-kujutis.
- Valige USB-mäluseadmeks USB-mälu.
- Klõpsake Flash ja oodake, kuni protsess on lõppenud.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Key bootimine ja BIOSi juurdepääs



Lülitage arvuti, millele soovite Zorin OS-i paigaldada, välja ja ühendage seejärel USB-mäluseade.


Kui arvuti käivitub, sisenege BIOSi (`ESC`, `F9` või `F11`, olenevalt tootemargust) ja valige USB-klahv kui alglaadimisseade, seejärel vajutage `Enter`, et käivitada alglaadimisprotsess.





- Käivitamisel valige **Katseta või paigalda Zorin OS**.



![capture](assets/fr/08.webp)





- Kui teil on NVIDIA graafikakaart, valige **Katsetage või installige Zorin OS (kaasaegsed NVIDIA draiverid)**.
- Palun oodake, kuni faile kontrollitakse.



![capture](assets/fr/09.webp)





- Valige Zorin OS-i paigaldusprogrammis keel **Prantsusmaa** ja seejärel klõpsake nuppu Install **Zorin OS**.



![capture](assets/fr/10.webp)





- Valige klaviatuuri paigutus.



![capture](assets/fr/11.webp)





- Märkige kastid **Laadi uuendused alla Zorin OS-i paigaldamise ajal** ja **Installida kolmanda osapoole tarkvara graafika- ja Wi-Fi riistvara ning täiendavate meediaformaatide jaoks**.



![capture](assets/fr/12.webp)





- Zorin OS-i installimiseks kogu kettale: valige **Ketta kustutamine ja Zorin OS-i installimine**.



![capture](assets/fr/14.webp)



Zorin OS-i paigaldamine koos Windowsiga (dual-boot) :





- Valige **Install Zorin OS Windows Boot Manager** kõrval.



![capture](assets/fr/15.webp)





- Kui te ei ole oma ketast partitsioneerinud, valige kettaruum, mida soovite Zorin OS-i jaoks eraldada, seejärel klõpsake **Install now**.



![capture](assets/fr/16.webp)





- Kinnitage muudatused kettal kaks korda.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Valige geograafiline piirkond **Pariis**.



![capture](assets/fr/18.webp)





- Looge oma kasutajakonto ja andke oma arvutile nimi.



![capture](assets/fr/19.webp)





- Palun oodake, kuni Zorin OS installeerub.



![capture](assets/fr/20.webp)





- Kui paigaldus on lõpule viidud, klõpsake nuppu **Umberakendamine**.



![capture](assets/fr/21.webp)





- Eemaldage USB-installatsiooniklahv ja vajutage Enter.



![capture](assets/fr/22.webp)



## Zorin OS-i avastamine ja kasutamine



### Esimene käivitamine



Arvutit käivitades avaneb GRUB - Linuxi alglaadimishaldur. Vaikimisi on valitud **Zorin OS**; 30 sekundi pärast käivitub see automaatselt.



![capture](assets/fr/23.webp)



Kui olete paigaldanud Zorin OS-i koos Windowsiga kahestardiga, saate Windowsi käivitada, valides **Windows Boot Manager**.



Logi sisse oma kasutajakontoga :



![capture](assets/fr/24.webp)



Esimesel käivitamisel käivitub rakendus **Tervitame Zorin OS-i**, mis aitab teil oma uut operatsioonisüsteemi avastada.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Süsteemi ajakohastamine



Varsti avaneb uuenduste haldur, mis annab teile teada, et uuendused on saadaval. Paigaldage need, klõpsates nupule **Installi nüüd**.



![capture](assets/fr/33.webp)



Saate uuendusi käsitsi kontrollida rakenduses **Software** > Uuendused:



![capture](assets/fr/34.webp)



### Isikupärastamine



Esimene asi, mida Zorin OSis teha, on valida **töökoha paigutus**, mis on teile kõige mugavam. Sa leiad sarnaseid paigutusi nagu Windowsis (ja veelgi enam Pro-versioonis).



Selleks avage **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Seejärel avage **Settings**, et kohandada oma süsteemi:


**Heli - Seaded - Zorin OS



![capture](assets/fr/36.webp)



**Online kontod - Seaded - Zorin OS



![capture](assets/fr/37.webp)



### Rakendused



Rakenduste paigaldamiseks on mitu võimalust:





- Software**, Zorin OS-i rakenduste pood. Rakendused pärinevad mitmest allikast: apt, Flatpak ja Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (käsurealt) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Lisateavet rakenduste paigaldamise kohta Zorin OS-is leiate sellelt leheküljelt: [Install Apps (zorin.com)](https://zorin.com/help/install-apps/).



### Windowsi rakendused



Windowsi rakenduste installimiseks alustage **zorin-windows-app-support** paketi installimisega terminali kaudu:



```bash
sudo apt install zorin-windows-app-support
```



Windowsiga ühilduvate rakenduste ja nende ühilduvustasemete loetelu leiate leheküljelt [Wine Application Database] (https://appdb.winehq.org/). Sealt leiad järgmised märgid, mis vastavad ühilduvuse tasemele (parimast halvimani): Platinum, Gold, Silver, Bronze ja Garbage.



Windowsi .exe või .msi rakenduse installimiseks on teil kaks võimalust:





- Avage **PlayOnLinux** ja klõpsake ühilduvate rakenduste ja mängude sirvimiseks nupule **Install**.



![capture](assets/fr/41.webp)





- Tehke topeltklõps rakenduse **.exe või .msi** failil ja laske paigaldusprogrammil teid juhendada.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Järeldus ja lisaressursid



Zorin OS on kindel ja taskukohane alternatiiv Windowsile, mis ühendab endas lihtsuse, turvalisuse ja privaatsuse.



See võimaldab sujuvat üleminekut Linuxile, ohverdamata seejuures mugavust või tootlikkust.



Oma digitaalse elu täiendavaks kaitsmiseks soovitame kasutada privaatsussõbralikke teenuseid, eriti krüpteeritud suhtlemiseks:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2