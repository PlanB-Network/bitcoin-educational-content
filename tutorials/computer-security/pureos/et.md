---
name: PureOS
description: Linuxi distributsioon, mis annab teile kontrolli oma digitaalse elu üle.
---

![cover](assets/cover.webp)



Isikuandmete kaitsmine digitaalajastul on iga internetikasutaja jaoks esmatähtis. Ettevõtted, organisatsioonid ja isegi operatsioonisüsteemid on kasulikud teabeallikad teie profiili ja elustiili määratlemisel. Õige operatsioonisüsteemi valimine on esimene samm teie veebipõhise privaatsuse tugevdamisel. Selles õpetuses vaatleme PureOSi, privaatsusele keskendunud Linuxi distributsiooni.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## PureOSiga alustamine



PureOS on Debianil põhinev operatsioonisüsteem, mille on välja töötanud Purism. PureOS sobib nii IT-spetsialistidele kui ka kasutajatele, kes otsivad lihtsat ja kergesti kasutatavat distributsiooni. See on ainulaadne selle poolest, et see on *vaba tarkvara* ja keskendub kasutajate isikuandmete kaitsele, luues raamistiku, mis põhineb Debian'i pakutaval privaatsusel, vabadusel, turvalisusel ja stabiilsusel.



### Miks valida PureOS?





- Lihtne, intuitiivne Interface**: GNOME pakub selget Interface töölauda, mis on loodud nii, et seda oleks lihtne kasutada isegi inimestele, kes ei tunne end käsureaga mugavalt.





- Tasuta**: nagu enamik Linuxi distributsioone, on ka PureOSi kasutamine täiesti tasuta. Siiski on arendajate toetamiseks saadaval igakuine tellimus.





- Turvalisus ja stabiilsus**: PureOSi arhitektuur ja töörežiim muudavad selle väga turvaliseks distributsiooniks, mis tagab andmekaitse ja süsteemi stabiilsuse.





- Dokumentatsioon ja aktiivne kogukond**: PureOSil on selge ja arusaadav dokumentatsioon ning pühendunud ja aktiivne kogukond, mis teeb probleemide lahendamise ja süsteemi samm-sammult õppimise lihtsaks.



## Paigaldamine ja konfigureerimine



PureOS-i paigaldamine ja konfigureerimine arvutisse nõuab järgmisi minimaalseid funktsioone:




- Vähemalt 8 GB suurune USB-mälu süsteemi väljalülitamiseks.
- 4 GB RAM.
- 30 GB vaba ruumi Hard kettal.



Mine [PureOS ametlikule veebisaidile](https://pureos.net/) ja lae alla operatsioonisüsteemi ISO-kujutis vastavalt oma masina arhitektuurile.



PureOSi installimise käivitamiseks peate looma käivitatava USB-mäluseadme, kasutades flash-tarkvara, näiteks [Balena Etcher](https://www.balena.io/etcher).



Kolme lihtsa sammuga saad USB-pulga, mis on käivitunud PureOSi operatsioonisüsteemiga.





- Ühendage USB-mäluseade ja käivitage allalaaditud Balena tarkvara.
- Seejärel valige PureOS ISO image
- Valige väljundseadmeks USB-mäluseade, seejärel klõpsake nupul **Flash** ja oodake, kuni protsess on lõppenud.



![0_01](assets/fr/01.webp)



Kui USB-mäluseade on käivitunud, taaskäivitage arvuti, millele soovite PureOSi paigaldada.



Käivitamisel pääsete BIOSi, vajutades klahvi `ESC`, `F9` või `F11`, sõltuvalt teie masinast. Valige alglaadimisseadmeks USB-klahv ja vajutage kinnitamiseks klahvi `ENTER`.



### Käivitusekraan



PureOS pakub operatsioonisüsteemi käivitamiseks mitmeid võimalusi. Operatsioonisüsteemi paigaldamise käivitamiseks valige **Test või Install PureOS**.



![0_02](assets/fr/02.webp)



Määrake keel ja klaviatuuri paigutus, mida soovite oma arvutis kasutada.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Lubage või keelake juurdepääs oma **geograafilisele asukohale** rakendustele, et saada teie piirkonnale kohandatud soovitusi.



![0_05](assets/fr/05.webp)



Te saate luua ühenduse oma olemasoleva **NextCloudi** kontoga, et saada andmeid, mis on seotud teises süsteemis kasutatava kontoripaketiga.



![0_06](assets/fr/06.webp)



Õpetus on esitatud, kuid kui soovite selle sammu vahele jätta, võite akna sulgeda.



![0_08](assets/fr/08.webp)



### Paigalduse käivitamine



Klõpsake menüüs **Tegevused** ja uurige süsteemi eelinstalleeritud rakendusi ja tööriistu. Paigaldamise alustamiseks klõpsake **Install PureOS**



![0_09](assets/fr/09.webp)



Seadistage süsteemi keel ja klaviatuuri paigutus vastavalt vajadusele, seejärel konfigureerige Hard ketta partitsioneerimise režiim.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Teil on kaks võimalust oma Hard ketta partitsioneerimiseks:




- Ketta kustutamine**: PureOSi täielikuks paigaldamiseks, kustutades kõik eelnevalt Hard kettal olevad andmed.



![0_14](assets/fr/14.webp)





- Käsitsi partitsioneerimine** oma partituuride loomiseks



⚠️ Kui loote käsitsi osioone oma operatsioonisüsteemi jaoks, veenduge, et eraldate vähemalt 2 GB suuruse partitsiooni PureOSi tööks ja seejärel teise partitsiooni andmete jaoks.



![0_15](assets/fr/15.webp)



Aktiveerige **ketta krüpteerimine**, kui soovite oma andmeid kaitsta. Sisestage tugev ja keeruline parool.



Seostage kasutaja oma operatsioonisüsteemiga, määrates kasutajanime ja vähemalt 20-tähelise tähtnumbrilise parooli, et tugevdada andmete turvalisust.



![0_16](assets/fr/16.webp)



Vaadake tehtud seaded üle ja vajadusel muutke neid.



![0_17](assets/fr/17.webp)



Klõpsake **Install** ja seejärel **Install Now**, et kinnitada, et PureOS on teie arvutisse installeeritud.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Kui paigaldus on lõpetatud, märkige ruut **Umberegistreeri nüüd**, et arvuti uuesti käivitada, seejärel kinnitage:




- Keel.
- Klaviatuuri paigutus.
- Teie NextCloudi konto (valikuline).



![0_25](assets/fr/25.webp)



## Uuendused



Enne PureOSi kasutamise alustamist on oluline oma süsteemi uuendada. See võimaldab teil saada kasu uusimatest funktsioonidest ja turvaparandustest ning tagab suurema stabiilsuse.





- Uuendus Interface graafiku kaudu**:


Avage rakendus **Tarkvara**, seejärel minge vahekaardile **Updates**. Saadaolevad uuendused kuvatakse automaatselt. Klõpsake **Laadi alla** ja seejärel **Installi**, kui allalaadimine on lõppenud.





- Uuendamine terminali kaudu**:


Avage terminal ja sisestage järgmine käsk, et uuendada olemasolevate pakettide nimekirja:



```shell
sudo apt update
```



Sisestage oma parool ja kinnitage. Seejärel installige uuendused:



```shell
sudo apt full-upgrade
```



## PureOS arendamiseks



PureOS ei sisalda vaikimisi kõiki arendamiseks vajalikke vahendeid.


Saate neid kiiresti paigaldada järgmise käsuga:



```shell
sudo apt install build-essential git curl
```



See installib **Git** ja **Curl** kompileerimisvahendid, mis on kasulikud enamikus arenduskeskkondades.



## PureOS keskkond



PureOS paistab silma oma uuendusliku lähenemise poolest tõelisele konvergentsile: üks operatsioonisüsteem tagab sujuva ja tõrgeteta töö erinevates seadmetes, sealhulgas sülearvutites, tahvelarvutites, miniarvutites ja nutitelefonides.



PureOSi rakendused on loodud kohanduvaks: nad kohanduvad automaatselt vastavalt ekraani suurusele ja sisestusrežiimile (puute- või klaviatuur/hiir). Näiteks GNOME veebibrauser kohandab dünaamiliselt oma Interface, et pakkuda optimaalset kasutuskogemust nii mobiil- kui ka lauaarvutites.



PureOS sisaldab ka **LibreOffice** kontoripaketti, mis sisaldab:





- Writer**: täielik tekstiprotsessor dokumentide loomiseks ja redigeerimiseks.
- Calc**: võimas tabelarvutusprogramm andmete ja arvutuste haldamiseks.
- Impress**: vahend professionaalsete esitluste loomiseks.



See tasuta pakett võimaldab teil tõhusalt töötada, ilma et peaksite sõltuma patenteeritud tarkvarast.



PureOS pakub ühtset, turvalist ja paindlikku keskkonda, mis põhineb 100% avatud lähtekoodiga distributsioonil, mis tagab täieliku kontrolli ja range austuse privaatsuse suhtes. Selle tõeline lähenemine hõlbustab eri tüüpi seadmetega, näiteks arvutite, tahvelarvutite ja nutitelefonidega ühilduvate rakenduste loomist, ilma et oleks vaja teha keerulisi kohandusi.



PureOS lihtsustab rakenduste arendamist, testimist ja kasutuselevõttu turvalises keskkonnas, pakkudes ligipääsu olulistele tööriistadele, töökindlatele paketihalduritele ja rikkalikule avatud lähtekoodiga ökosüsteemile. Selle stabiilne arhitektuur ja Commitment konfidentsiaalsus muudavad selle usaldusväärseks platvormiks, mida saab kasutada mitmel otstarbel, sealhulgas Blockchain arendamiseks, kiireks prototüüpimiseks või tootmiskeskkonnaks.



Avastage meie kursus oma turvalisuse tugevdamiseks ja digitaalse privaatsuse kaitsmiseks.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1