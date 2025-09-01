---
name: Elementaarne operatsioonisüsteem
description: Ideaalne asendaja Windowsile ja MacOSile
---

![cover](assets/cover.webp)



Elementary OS on Ubuntu-põhine operatsioonisüsteem, mis on loodud lihtsaks, kiireks ja stabiilseks kasutamiseks paljudes igapäevastes olukordades. See kujutab endast tasakaalustatud Linuxi alternatiivi MacOSile ja Windowsile. Selle sujuv, intuitiivne ja lihtsa graafilise Interface abil on seda lihtne õppida, isegi algajatele. Samuti keskendub see ergonoomikale, turvalisusele ja jõudlusele.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Miks valida Elementary OS





- Lihtsus ja kasutusmugavus**: Elementary OS-i graafiline Interface on MacOs ja Windows'i graafilise Interface vahel. See tuttavlikkus muudab selle hõlpsasti kasutatavaks ka kogenematuile kasutajatele.





- Turvalisus**: Nagu enamik Linuxi distributsioone, on ka Elementary OSil kõrge turvalisuse tase. Regulaarsed uuendused, õiguste haldamine ja tavaliste viiruste puudumine teevad sellest usaldusväärse süsteemi.





- Kiirus**: Elementary OS on kerge distributsioon. See nõuab vähe ressursse, mistõttu on see kiire ja sobib tagasihoidliku konfiguratsiooniga arvutitele.





- Tasuta**: Süsteem on täiesti tasuta. Kuid kui te seda alla laadite, võite teha annetuse, et toetada arendajaid.





- Aktiivne kogukond**: Elementaarse operatsioonisüsteemi ümbritsev kogukond on mitmekesine ja tundlik. Kui teil tekib raskusi, võite kergesti leida abi foorumitest või sotsiaalvõrgustikest.



## Paigaldamine ja konfigureerimine


### Riistvara eeldused



Enne paigaldamise alustamist veenduge, et teil on olemas järgmised seadmed:





- Vähemalt 12 GB suurune **USB-võti**
- RAM** mälu vähemalt 4 GB
- **Hard ketas mahuga 20 GB** või rohkem mugavaks kasutamiseks



## ISO-kujutise allalaadimine



Mine ametlikule operatsioonisüsteemi veebisaidile [elementaarne](https://elementary.io/) ja vali summa, millega projekti toetada. See samm on vabatahtlik.


Kui soovite ISO-kujutise tasuta alla laadida, sisestage väljal **"Muu "** 0 ja alustage süsteemi ISO-kujutise allalaadimist.



![0_01](assets/fr/01.webp)



## Käivitatava USB-klahvi loomine



Kui olete ISO-kujutise alla laadinud, peate selle USB-mäluseadmele käivitatavaks tegema, et paigaldamisega jätkata.



Laadige alla tarkvara nagu [Balena Etcher](https://etcher.balena.io/) või mõni sarnane tööriist, seejärel käivitage tarkvara.


Valige eelnevalt alla laetud **Elementaarne OS** ISO-kujutis ja määrake sihtmärgiks oma USB-mälu.



Klõpsake protsessi alustamiseks nupul **flash** ja oodake enne USB-mäluseadme eemaldamist, kuni protsess on lõppenud.



![0_02](assets/fr/02.webp)



## Key bootimine ja BIOSi juurdepääs



Lülitage arvuti, millele soovite Elementary OS-i paigaldada, välja ja ühendage seejärel USB-mälu.


Kui arvuti käivitub, sisenege BIOSi (`ESC`, `F9` või `F11`, olenevalt tootemargust) ja valige USB-klahv kui alglaadimisseade, seejärel vajutage `Enter`, et käivitada alglaadimisprotsess.



## Elementaarse operatsioonisüsteemi paigaldamine



Kui USB-mäluseade on õigesti konfigureeritud, algab paigaldus automaatselt.



### Keele valik



Valige keel, milles soovite süsteemi paigaldada. Võite valida ka piirkondliku variandi.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Klaviatuuri paigutus



Valige oma klaviatuurile vastav paigutus. Välja on ette nähtud, et kontrollida, kas klahvid annavad õiged tähemärgid.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Testrežiim



Elementaarne operatsioonisüsteem võimaldab teil süsteemi enne selle paigaldamist testida. See režiim võimaldab teil uurida Interface, muutmata midagi teie Hard kettal.



### Paigalduse käivitamine





- Klõpsake **"Ketta kustutamine ja paigaldamine "**, et paigaldada otse kogu kettale.
- Klõpsake **"Kohandatud paigaldus "**, kui soovite partitsioone käsitsi hallata.



![0_07](assets/fr/07.webp)



### Plaadi valik



Valige ketas, millele soovitakse paigaldada Elementary OS, ja vajutage nupule Jätka.



![0_08](assets/fr/08.webp)



### Ketta krüpteerimine



Valik võimaldab teil ketta krüpteerida, et **kaitseda oma andmeid**. Selle kaitse aktiveerimiseks peate määrama tugeva parooli. See on siiski vabatahtlik.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Paigalduse käivitamine



Enne paigalduse käivitamist saate lubada täiendavate riistvara draiverite automaatset paigaldamist, sõltuvalt teie masina ühilduvusest.





- Paigaldamise alustamiseks klõpsake nuppu "Erase and install".
- Oodake, kuni protsess on lõppenud.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Restart



Kui olete lõpetanud, klõpsake taaskäivitamiseks nupule **enter** ja eemaldage USB-mälu sobival hetkel, et vältida installimise taaskäivitamist.



![0_13](assets/fr/13.webp)



## Konfiguratsioon pärast paigaldamist



Pärast taaskäivitamist on vaja teha mõned täiendavad sammud.



![0_14](assets/fr/14.webp)



### Keele valik



Kinnitage või muutke süsteemi keelt sisselogimisel.



![0_15](assets/fr/15.webp)



### Klaviatuuri paigutus



Veenduge, et klaviatuuri paigutus on selline, nagu soovite.



![0_16](assets/fr/05.webp)



### Kasutajakonto loomine



Seostage kasutajakonto oma operatsioonisüsteemiga, määrates kasutajanime ja kindlustades seejärel juurdepääsu oma andmetele vähemalt 20 tähemärgilise ja sümbolitest koosneva tähtnumbrilise parooliga.



![0_17](assets/fr/17.webp)



### Esimene ühendus



Esmakordsel sisselogimisel võimaldab Elementary OS teil oma keskkonda mõne põhiseade abil isikupärastada.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Süsteemi uuendamine



Enne pikemaajalist kasutamist on oluline uuendada süsteemi viimaste parandustega.


### Võimalus 1: Uuendamine Interface graafika kaudu



Sisenege **AppCenterisse** ja klõpsake paremas ülemises nurgas oleval uuendamise ikoonil. Oodake, kuni uuendused on loetletud, seejärel klõpsake installimise alustamiseks **"Update All "**.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Võimalus 2: uuendamine terminali kaudu



Uuendust saate teha ka käsurealt terminali kaudu: see on soovitatav võimalus selle täpsuse tõttu.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



Esimeste uuenduste puhul nõuab operatsioonisüsteem teie kasutajaparooli ja kinnitust tarkvarapakettide uuendamiseks, isegi elementaarse tuuma puhul.



## Töökeskkonna konfiguratsioon



Elementaarne operatsioonisüsteem sisaldab ainult olulisi vahendeid. Keskkonna kohandamiseks vastavalt teie vajadustele, eriti kui olete arendaja, soovitame paigaldada lisavahendeid.





- Kasulikke sõltuvusi saab lisada järgmise käsuga (mida tuleb kohandada vastavalt oma vajadustele):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



See käsk installeerib **Git**, **Python 3**, **pip**, **kompilaatoritööriistad**, **wget**, **curl**, **zsh**, **make**, **snapd** ja **vscode**, et valmistada ette põhiline arenduskeskkond.



Elementaarne operatsioonisüsteem on nüüd teie masinas käivitatud ja töötab. Selle lihtsuse, kerguse ja elegantsi filosoofia muudab selle suurepäraseks valikuks nii isiklikuks kui ka professionaalseks kasutamiseks. Saate stabiilse, voolava ja lihtsa süsteemi, mida on võimalik kohandada vastavalt oma eelistustele. Kas arendamiseks, kontorikasutuseks või igapäevaseks sirvimiseks, kõik on olemas, et luua tõhus, intuitiivne ja meeldiv töökeskkond. Vaadake ka meie Fedora õpetust, mis on sama lihtne, töökindel ja modulaarne Linuxi distributsioon.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0