---
name: Fedora
description: Linuxi distributsioon, mis pakub teile tasuta, täielikku ja turvalist tööruumi.
---


![cover](assets/cover.webp)





Fedora on 2003. aastal käivitatud vaba, avatud lähtekoodiga Linuxil põhinev operatsioonisüsteem, mida arendab **Fedora Project** kogukond ja toetab **Red Hat Linux**. See on tuntud oma stabiilsuse, hea jõudluse ja kasutusmugavuse poolest, mistõttu on see suurepärane valik nii algajatele kui ka edasijõudnutele. Süsteem töötab enamikul kaasaegsetel protsessorarhitektuuridel, mistõttu on seda lihtne paigaldada praktiliselt igale arvutile. Fedora on saadaval ka mitmes eelkonfigureeritud versioonis, mida nimetatakse "Fedora Spins" või "Fedora Editions", mis on mõeldud konkreetsete vajaduste jaoks (videomängud, astronoomia, arendus...).



## Fedora Linuxi arhitektuur



Nagu te varem lugesite, on Fedora vaba operatsioonisüsteem, mis põhineb Linuxi kernelil. Linuxi kernel on operatsioonisüsteemi osa, mis suhtleb arvuti riistvaraga ja haldab süsteemi ressursse, näiteks mälu ja töötlusvõimsust.



Fedora Linux sisaldab mitmesuguseid tarkvaravahendeid ja rakendusi, mis on vajalikud operatsioonisüsteemi käivitamiseks Linuxi tuuma peal. Fedora modulaarne ülesehitus tähendab, et see koosneb peamiselt üksikute komponentide kogumikust, mida saab vajaduse korral kergesti lisada, eemaldada või asendada. See võimaldab kujundada operatsioonisüsteemi, kasutades ainult vajalikke ressursse.



Fedora sisaldab ka töölauakeskkonda, mis on Interface, mille kaudu kasutajad täidavad ülesandeid ja pääsevad ligi rakendustele. Fedora vaikimisi töölauakeskkond on GNOME, mis on kasutajasõbralik, kergesti kasutatav ja väga hästi kohandatav töölauakeskkond.



## Miks valida Fedora?



Arvukate Linuxi distributsioonide hulgast paistab Fedora eriti silma:





- Modulaarsus**: Fedora on ühilduv erinevate protsessorarhitektuuridega, mistõttu saab Fedora paigaldada enamikku arvutitest, isegi madala võimsusega, kohandudes ideaalselt teie vajadustele.





- Lihtne, intuitiivne Interface**: Fedora ühendab kaasaegse graafilise Interface ja võimsa käsurea Interface, mis teeb selle kasutamise lihtsaks kõigi profiilide jaoks.





- Tuuma stabiilsus**: Fedora põhineb Red Hatil ja on tuntud oma uuenduste, eriti tuumavärskenduste usaldusväärsuse poolest, mis viiakse läbi ilma suuremate vigadeta tänu suure kogukonna tasuta panusele.





- Kiire ja lihtne paigaldus**: kuna kujutise suurus on vaid 3 GB, on paigaldamine kiire ja lihtne, isegi piiratud ressurssidega masinatel.



## Fedora väljaanded



Sõltuvalt teie profiilist ja kasutamisest pakub Fedora teie vajadustele vastavaid versioone. Peamiselt leiate:





- Fedora Workstation**: See väljaanne on ideaalne isiklikuks ja/või professionaalseks kasutamiseks arvutites ja sellele on paigaldatud üldised utiliidid, nagu brauserid, kontoripakett (tekstiredaktorid) ja meedia taasesitustarkvara.





- Fedora Server**: See väljaanne on pühendatud serveri haldamisele. Fedora Server sisaldab mitmesuguseid vahendeid, mis aitavad teil serverid oma mastaabis kasutusele võtta ja hallata.





- Fedora CoreOS**: Tahad hõlpsasti käivitada ja juurutada pilverakendusi? Fedora CoreOS on väljaanne, mis annab teile vahendid näiteks Dockeri ja Kuberneti abil kujutiste loomiseks ja haldamiseks.



Selles õpetuses võtame Fedora Workstationi väljaande eest vastutuse. Kuid allpool kirjeldatud protsessid on sarnased ka teiste väljaannete puhul.



## Fedora Workstationi paigaldamine ja seadistamine



Fedora Workstationi paigaldamiseks on vaja järgmist riistvara konfiguratsiooni:




- Vähemalt **8 GB suurune USB-mälu** operatsioonisüsteemi käivitamiseks.
- Vähemalt **40 GB vaba ruumi** arvuti Hard kettal.
- 4 GB RAM** sujuvaks kasutuskogemuseks.



### Fedora tööjaama allalaadimine



Saate alla laadida [Fedora Workstation] väljaande (https://fedoraproject.org/fr/workstation/download) Fedora projekti ametlikult veebilehelt. Seejärel valige oma protsessorarhitektuurile vastav versioon (32-bit - 64-bit) ja klõpsake ikoonil **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Looge käivitatav USB-klahv



Fedora installimiseks peate looma käivitatava USB-ketta, kasutades selleks sellist tarkvara nagu [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Kui olete Balena Etcher'i paigaldamise lõpetanud, avage rakendus ja valige alla laetud Fedora Workspace'i ISO-kujutis. Valige oma USB-mäluseadme sihtmälu ja klõpsake nupule **Flash**, et alustada käivitatava võtme loomist.



![boot](assets/fr/05.webp)


### Fedora installimine



Kui olete USB-mäluseadme käivitamise lõpetanud, lülitage arvuti välja.


Lülitage arvuti sisse, seejärel sisenege BIOSi käivitamise ajal, vajutades klahvi `F2`, `F12` või `ESC`, sõltuvalt arvutist.



Valige alglaadimisvalikutes oma USB-mäluseade esmaseks alglaadimisseadmeks. Selle valiku kinnitamisel arvuti taaskäivitub ja käivitab automaatselt USB-mäluseadmel oleva Fedora installeri**.



Kui arvuti on USB-mälupulgalt käivitunud, ilmub **GRUBi ekraan**.



Selles etapis on teil järgmised võimalused:




- Testkandjad**: See valik võimaldab kontrollida USB-pulga terviklikkust ja tagada, et kõik õigeks paigaldamiseks vajalikud sõltuvused on olemas. See on valikuline samm, kuid soovitatav, kui teil on USB-pulga suhtes kahtlusi.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Käivitage Fedora**: See käivitab Fedora "live"-režiimis, ilma installimiseta.



Fedora töölaual (reaalajas) klõpsake **Install Fedora** (või Install on Hard disk), et alustada paigaldusprotsessi. Saate valida, kas paigaldada hiljem ja testida Fedorat ilma installimiseta.



![install-live](assets/fr/08.webp)



Esimene samm on valida Fedora **installeerimiskeel** ja **klaviatuuri paigutus**



![language](assets/fr/10.webp)





- Paigaldusketta valimine:



Valige Hard ketas, millele soovite Fedora installida.



Kui ketas on tühi, kasutab Fedora automaatselt kogu vaba ruumi. Vastasel juhul saate partitsioneerimist kohandada (käsitsi või automaatselt).



![disk](assets/fr/11.webp)





- Krüpteerimine:



Selles etapis soovitab Fedora ketta krüpteerida, et lisada lisaturvalisuse Layer. See tagab, et teie andmeid saab lugeda ainult teie Fedora süsteem.



![chiffrement](assets/fr/12.webp)



Enne installimise käivitamist kuvab Fedora kokkuvõtte teie valikutest. Fedora installimise alustamiseks kinnitage ja klõpsake nupule install.



![resume](assets/fr/13.webp)



Paigaldamise ajal kopeerib Fedora faile ja konfigureerib süsteemi. Kui see on lõpetatud, käivitub arvuti automaatselt uuesti.



![installation](assets/fr/14.webp)



### Põhikonfiguratsioon


Esimesel kasutamisel peate viimistlema mõned seaded:




- Vajaduse korral muutke süsteemi keelt.



![language](assets/fr/15.webp)





- Valige oma eelistustele vastav klaviatuuri paigutus.



![keyboard](assets/fr/16.webp)





- Valige oma ajavöönd, sisestades otsinguribale oma linna nime, seejärel klõpsake vastaval soovitusel.



![timezone](assets/fr/17.webp)





 - Lubage või keelake juurdepääsu oma positsioonile rakenduste jaoks, mis seda vajavad, samuti automaatne veateadete saatmine.



![location](assets/fr/18.webp)





- Otsustage, kas soovite lubada kolmanda osapoole tarkvarahoidlaid.



![logs](assets/fr/19.webp)





- Sisestage oma täisnimi ja määrake oma konto kasutajanimi.



![name](assets/fr/20.webp)





- Looge oma seansi jaoks turvaline salasõna: võimalikult pikk (vähemalt 20 tähemärki), võimalikult juhuslik ja erinevate tähemärkidega (väiketähed, suurtähed, numbrid ja sümbolid). Ärge unustage oma salasõna salvestada.



![mdp](assets/fr/21.webp)



Kui kõik need sammud on lõpetatud, käivitage Fedora ja alustage selle kasutamist kohe, ilma edasise taaskäivitamiseta.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Kui teie paigaldus on lõpule viidud, saate oma Interface kodus konsulteerida mõne eelinstalleeritud utiliidi abil.



![install-now](assets/fr/09.webp)



## Avastage põhiülesanded



### Interneti sirvimine


Fedora vaikimisi brauser on **Firefox**. Seda on lihtne kasutada ja see sobib enamiku vajaduste rahuldamiseks.


Kui eelistate mõnda muud brauserit, saate selle installida **tarkvara haldurist** või **terminali** kaudu.


### Tekstitöötlus


Fedora sisaldab vaikimisi kontoripaketti **LibreOffice**, mis pakub mitmeid kasulikke vahendeid:




- Writer** tekstitöötluseks.
- Calc** tabelite jaoks.
- Impress** esitluste loomiseks.


## Rakenduste paigaldamine


Uute rakenduste paigaldamiseks saate kasutada Fedora **tarkvara haldurit** (nimega _Tarkvara_), mis muudab paigaldamise lihtsaks ja visuaalseks.  Siiski on **terminali** kasutamine sageli kiirem ja täpsem.



Enne mis tahes tarkvara paigaldamist ärge unustage alati **repositooriume** uuendada, et veenduda, et teil on juurdepääs uusimatele versioonidele.



Seejärel kasutage soovitud rakenduse installimise käivitamiseks järgmist käsku:


sudo dnf install tarkvara_nimi`


## Operatsioonisüsteemi uuendamine


Pärast paigaldamist on oluline uuendada Fedorat, et kasutada ära viimaseid turvaparandusi ja tarkvarauuendusi.


### Võimalus 1: Interface graafiku kaudu




- Avage Fedora **Settings**, seejärel minge jaotisse **System**.
- Klõpsake **Tarkvara uuendamine**.
- Alustage uuenduste allalaadimist ja oodake, kuni protsess on lõppenud.



Pärast uuenduste paigaldamist võib olla vajalik **taaskäivitus**.


### Võimalus 2: Terminali kaudu




- Avage terminal ja alustage **repositooriumide** uuendamisega, et veenduda, et teil on olemas uusimad versioonid:



```shell
sudo dnf check-update
```





- Seejärel uuendage kogu paigaldatud tarkvara järgmise käsuga:



```shell
sudo dnf upgrade
```



Nüüd on teie Fedora süsteem ajakohane ja valmis kõigi igapäevaste ülesannete täitmiseks. Avastage meie õpetus Linux Minti, teise Linuxi distributsiooni kohta ja kuidas luua terve ja turvaline keskkond oma Bitcoin tehingute jaoks.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5