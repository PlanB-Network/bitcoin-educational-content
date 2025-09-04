---
name: Debian
description: Linuxi distributsioon, mis on tuntud oma stabiilsuse, töökindluse ja ühilduvuse poolest.
---

![cover](assets/cover.webp)



Debian on vaba GNU/Linuxi distributsioon, mis on tuntud oma töökindluse ja usaldusväärsuse poolest. Selle Linuxi tuuma ja kõiki pakette on rangelt testitud, et tagada kindel stabiilsus ja kõrge turvalisuse tase. Debian sobib nii serverite kui ka tööjaamade jaoks ning pakub lihtsat kasutuskogemust ja suurt tarkvarakataloogi. Olenemata sellest, kas otsite turvalist süsteemi igapäevaseks kasutamiseks või tootmiskeskkonda, on Debian õige valik.



## Miks valida Debian?





- Tasuta ja avatud**: Debian on täielikult avatud lähtekoodiga, tagades läbipaistvuse ja litsentsitasude puudumise.
- Stabiilsus ja turvalisus**: iga versioon läbib põhjaliku testimisprotsessi, mis teeb Debianist ühe kõige usaldusväärsema ja turvalisema distributsiooni turul.
- Aktiivne kogukond**: suur kogukond ja ulatuslik dokumentatsioon on teile alati toeks, kui seda vajate.
- Kerge ja skaleeritav**: te saate paigaldada Debianiamiant ka tagasihoidlike ressurssidega masinatele, säilitades samal ajal hea jõudluse.
- Laiaulatuslik tarkvarakataloog**: üle 50 000 ametliku paketi on saadaval repositooriumide kaudu.



## Valige Interface graafika



Debian pakub mitmeid töölauakeskkondi, mis sobivad teie vajadustele:





- GNOME**: kaasaegne, intuitiivne Interface, ideaalne algajatele. See pakub sujuvat, lihtsasti kasutatavat graafilist menüüd rakendustele juurdepääsuks.
- XFCE**: kerge ja kiire, ideaalne vähem võimsate masinate jaoks.
- KDE Plasma**: väga hästi kohandatav, Windowsi-taolise välimusega.
- Cinnamon**: lihtne ja elegantne Interface, mis on inspireeritud Windowsist.
- LXDE / LXQt**: ülikerge, sobib vanematele arvutitele.
- MATE**: lihtne ja klassikaline, lähedane vanale GNOME-le.



💡 Mugava ja hõlpsasti haaratava kogemuse saamiseks on **GNOME väga soovitatav**.



## Debiani paigaldamine ja konfigureerimine


### Nõuded riistvarale



Enne paigaldamise alustamist veenduge, et teil on olemas järgmised seadmed:





- USB-võti**: vähemalt 8 GB, et hoida käivitatavat ISO-kujutist.
- Juhusjuurdepääsu mälu (RAM)**: 4 GB sujuvaks paigaldamiseks ja tööks.
- Kettaruum**: vähemalt 15 GB vaba ruumi süsteemi ja uuenduste jaoks.



### Lae alla



Debiani image'i valik sõltub teie protsessori arhitektuurist:





- AMD64**: lae alla "live hybrid" väljaanne [download] nimekirjast (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: hankige DVD-pilt ametlikust [Debian] veebisaidilt (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Muud arhitektuurid**: leidke oma arhitektuurile vastav ISO [siin](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Käivitatava USB-klahvi loomine



Kui olete alla laadinud sobiva ISO-kujutise, jätkake paigalduskandja loomisega:




- Laadige Balena Etcher** [ametlikust veebisaidist](https://etcher.balena.io/) alla, seejärel hankige oma süsteemi jaoks sobiv binaarskeem ja installige see.



![etcher](assets/fr/02.webp)





- Käivitage Etcher**: avage tarkvara ja valige eelnevalt alla laaditud Debian ISO image.
- Valige USB-mäluseade**: määrake oma mäluseade (8 GB+) sihtmärgiks.
- Käivitage flash**: klõpsake **Flash!** ja oodake, kuni protsess on lõppenud.



![flash](assets/fr/03.webp)



Teie USB-mäluseade on nüüd valmis, et alustada Debiani installimist.



## Debiani paigaldamine oma süsteemi



### Käivitamine USB-mäluseadmelt



Installeerimise käivitamiseks USB-mäluseadmelt:




- Lülitage** arvuti täielikult välja.
- Taaskäivitage**, seejärel sisenege BIOS/UEFI-sse, vajutades kohe `ESC`, `F2`, `F11` (või spetsiaalset klahvi, olenevalt teie tootemargist).
- Käivitamismenüüs **valige alglaadimisseadmeks oma USB-mäluseade**.
- Kinnitage** Enter-klahviga, et alustada Debian'i kujutist: see viib teid paigaldusprogrammi tervitusekraanile.



### Paigalduse käivitamine



Algusekraan:



![starting](assets/fr/04.webp)



USB-mälupulgalt käivitamisel pakub Debiani tervitusekraan mitmeid võimalusi:




- Live System**: käivitab Debiani ilma selle installeerimiseta, ideaalne keskkonna testimiseks.
- Start Installer**: alustab paigaldamist otse Hard kettale.
- Täiustatud paigaldusvalikud**: annab teile juurdepääsu kohandatud paigaldusrežiimidele.



Debianiga tutvumiseks reaalajas valige **Live süsteem** ja kinnitage **Enter**. Seejärel saate installimise käivitada, klõpsates live-keskkonnas **Install Debian**.



![system](assets/fr/05.webp)





- Keele valik** (valikuline)



Valige loetelust oma Debiani süsteemi põhikeel, seejärel klõpsake OK.



![language](assets/fr/06.webp)





- Ajavöönd** (GMT)



Valige oma geograafiline tsoon, et määrata automaatselt kuupäev ja kellaaeg.



![timezone](assets/fr/07.webp)





- Klaviatuuri paigutus



Valige oma klaviatuuri keel ja paigutus. Kasutage sisseehitatud testvälja, et kontrollida, kas iga klahv annab oodatud tähemärgi.



![keyboard](assets/fr/08.webp)



### Ketta partitsioneerimine





- Ketta kustutamine**: kui teil on spetsiaalne partitsioon, kustutab see valik kogu selle sisu.
- Manuaalne partitsioneerimine**: valige see valik, et luua, muuta suurust või kustutada partitsioone vastavalt vajadusele.



![disk](assets/fr/09.webp)





- Kasutajakonto loomine



Sisestage oma täisnimi, kontonimi ja tugev parool, et tagada teie seansi turvalisus.



![user](assets/fr/10.webp)





- Parameetrite kokkuvõte**



Kuvatakse teie valikute kokkuvõte: kontrollige iga punkti ja vajadusel minge tagasi, et seda muuta.



![settings](assets/fr/11.webp)





- Paigalduse käivitamine



Klõpsake failide kopeerimise ja süsteemi konfigureerimise alustamiseks nuppu **Install**, seejärel oodake, kuni protsess on lõppenud.



![install](assets/fr/12.webp)





- Restart**



Kui paigaldus on lõpetatud, taaskäivitage arvuti, et rakendada kõik konfiguratsioonid ja pääseda ligi oma uuele Debian-süsteemile.



![restart](assets/fr/13.webp)



Käivitamisel sisestage kasutajanimi ja parool, et pääseda süsteemi.



![login](assets/fr/14.webp)



## Süsteemi uuendamine



Enne süsteemi kasutamise alustamist on oluline seda uuendada. See võimaldab teil saada kasu uusimatest tarkvaraparandustest, ajakohastest repositooriumidest ja mõnel juhul ka operatsioonisüsteemi enda turvaparandustest.



### Võimalus 1: Uuendamine graafilise Interface (GNOME) kaudu



Kui olete paigaldanud Debiani koos GNOME töölauakeskkonnaga, saate uuendusi teha graafiliselt. Selleks avage rakendus **Tarkvara**, seejärel minge vahekaardile **Ajakohastused**. Seejärel klõpsake protsessi alustamiseks nupule **Uusendus ja uuendamine**.



### Võimalus 2: uuendamine terminali kaudu (soovitatav)



See meetod pakub täielikumat kontrolli. See võimaldab teil uuendada repositooriume, tarkvarapakette ja vajaduse korral ka tuuma.




- Avage terminal, kasutades klahvikombinatsiooni `Ctrl + Alt + T`.
- Värskendage olemasolevate pakettide nimekirja järgmise käsuga:



```shell
sudo apt update
```



Sisestage küsimisel oma parool (märkige, et sisestamisel ei kuvata ühtegi märki - see on normaalne).





- Kättesaadavate värskenduste installimiseks:



```shell
sudo apt full-upgrade
```



## Avastage põhiülesanded



### Interneti sirvimine



Debianis on vaikimisi veebibrauseriks **Firefox**. Kui te eelistate mõnda muud brauserit, võite paigaldada mõne teise, tingimusel, et see on Debian'i repositooriumides saadaval (näiteks Chromium, Brave...).



### Tekstitöötlus



**LibreOffice** pakett on Debianis vaikimisi paigaldatud.





- Dokumentide kirjutamiseks kasutage **LibreOffice Writerit**, mis on Microsoft Wordi vaste.
- Tabelarvete puhul on **LibreOffice Calc** alternatiiviks Exceli programmile.
- Lõpuks võimaldab **LibreOffice Impress** luua esitlusi nagu PowerPoint.



## Rakenduste paigaldamine



Rakenduste paigaldamiseks Debianis on kaks võimalust:



### Graafiline meetod:



Rakenduste hõlpsaks otsimiseks ja installimiseks saate kasutada **tarkvara haldurit** (kättesaadav graafilise Interface kaudu).



### Käsurea meetod:



Kui otsitav rakendus ei ilmu graafilises Interface-s või kui eelistate terminali, kasutage järgmist käsku:



```shell
sudo apt install <name>
```



Asendage `<nimi>` paketi nimega. Näiteks `curl` paigaldamiseks:



```shell
sudo apt install curl
```



### Käsitsi allalaaditud paketi paigaldamine:



Kui olete alla laadinud `.deb` faili (Debian pakett), saate selle paigaldada järgmise käsuga:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Teie Debian-süsteem on nüüd paigaldatud ja valmis oma igapäevaste ülesannete täitmiseks.


Tänu **GNOME** töölauakeskkonnale saate juurdepääsu paljudele rakendustele kasutajasõbraliku graafilise Interface kaudu, mis on ideaalne nii algajatele kui ka edasijõudnutele.



Samuti on võimalik töölauakeskkonda vahetada (nt XFCE, KDE jne), ilma et peaks Debianit uuesti installeerima. Selleks kasutage lihtsalt terminali ja installige uus valitud keskkond.



Kui soovite rohkem teada saada Debianist ja üldisemalt GNU/Linuxi distributsioonidest, soovitan teil tutvuda selle kursusega:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1