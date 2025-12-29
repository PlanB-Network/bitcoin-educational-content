---
name: Pop!_OS
description: Linuxi distributsiooni Pop!_OS paigaldamise juhend
---

![cover](assets/cover.webp)



## Sissejuhatus



Pop!OS on Linuxil põhinev operatsioonisüsteem, mille on välja töötanud **System76**, Ameerika tootja, kes on spetsialiseerunud arendajatele, disaineritele ja edasijõudnutele mõeldud masinatele.



Pop!OS on loodud pakkuma kaasaegset, stabiilset ja suure jõudlusega keskkonda, mida iseloomustavad lihtne kasutuskogemus, võimsad tööriistad ja suur rõhk tootlikkusel.



### Kes on System76?



System76 on 2005. aastal asutatud Ameerika ettevõte, mis asub Denveris ja on spetsialiseerunud spetsiaalselt Linuxi jaoks mõeldud sülearvutite, lauaarvutite ja serverite tootmisele.



Erinevalt traditsioonilistest tootjatest arendab System76 masinaid, mis on kavandatud avatud, parandatavad ja orienteeritud tarkvaravabadusele.



System76 ei tee ainult arvuteid.



Ettevõte arendab ka :




- Pop!OS**, oma Linuxil põhinev operatsioonisüsteem;
- COSMIC**, kaasaegne, suure jõudlusega töölauakeskkond, mida kasutab Pop!OS ;
- Open Firmware**, avatud lähtekoodiga püsivara, mis põhineb Corebootil ;
- tööriistad arendajatele ja disaineritele.



Eesmärk on pakkuda kvaliteetset riist- ja tarkvaraintegratsiooni, mis on võrreldav Apple'i ökosüsteemiga, kuid on täiesti avatud ja keskendub Linuxile.



## Kaasaegne, stabiilne ja juurdepääsetav süsteem



Pop!OS tugineb Ubuntu-le, andes sellele suurepärase stabiilsuse, laiaulatusliku riistvara ühilduvuse ja juurdepääsu suurele tarkvara ökosüsteemile.


See pakub elegantset kasutajaliidest, COSMICi töölauda, mis on loodud nii, et see oleks sujuv, intuitiivne ja kohandatav isegi uute kasutajate jaoks.



## Ideaalne valik arendajatele, disaineritele ja nõudlikele kasutajatele



Pop!OS on eriti hinnatud :





- arendajad (eelinstalleeritud tööriistad, täiustatud plaatimise haldamine),
- nvidia või AMD graafikakaartidega kasutajad,
- üliõpilastele ja spetsialistidele, kes otsivad usaldusväärset süsteemi,
- windowsi kasutajad, kes soovivad teha lihtsat üleminekut.



See sisaldab automaatset plaatimist, selget tarkvarakeskust ja integreeritud tootlikkusvahendeid, mis lihtsustavad igapäevast kasutamist.



## Pop!OS tipphetked





- Optimeeritud jõudlus** tänu regulaarsetele uuendustele.
- Saadaval on kaks ISO-versiooni**: standard ja Nvidia optimeeritud.
- Täiustatud turvalisus** (LUKS krüpteerimine on paigaldamisel saadaval).
- Interface COSMIC** ergonoomiline ja kaasaegne.
- Väga ühilduv** Ubuntu ja Flatpak tarkvaraga.



## POP!OS turvaliselt alla laadida



### 1. Eeltingimused



Enne POP!OSi allalaadimist ja installimist on vaja teha mõned asjad, et paigalduskeskkond õigesti ette valmistada.



### Vajalikud seadmed





- Ühilduv arvuti**: Intel või AMD protsessor, Intel / AMD / Nvidia GPU.
- Vähemalt 4 GB RAM** (mugavaks kasutamiseks soovitatakse 8 GB).
- vähemalt 20 GB vaba ruumi** (soovitatav on 40 GB või rohkem).
- Vähemalt 4 GB suurune USB-mälu** paigalduskandja loomiseks.



### Interneti-ühendus



Stabiilne ühendus on kasulik :





- lae alla ISO-kujutis,
- paigaldada uuendused pärast paigaldamist.



Pop!OS võib töötada ka ilma ühenduseta, kuid installimine on palju sujuvam üle interneti.



### Andmete varundamine



Kui Pop!OS peaks asendama mõne teise süsteemi (Windows, Ubuntu jne) või olema koos sellega, on soovitatav enne jätkamist teha varukoopia tähtsatest failidest.



### Kontrollida Nvidia GPU olemasolu (kui see on kohaldatav)



Nvidia graafikakaardiga varustatud arvutite puhul peate alla laadima spetsiaalse ISO-pildi, mis sisaldab Nvidia draivereid.


See kontroll on väga lihtne:





- konsulteerides arvuti spetsifikatsioonidega,
- või otsides graafikakaardi mudelit süsteemi seadetest.



### Allalaadimine ametlikul veebisaidil



Pop!OS ISO image tuleks alla laadida otse ametlikult System76 lehelt: [system76.com/pop](https://system76.com/pop/).



See lehekülg pakub alati kõige uuemat versiooni, mis on kohandatud teie riistvarale.



![capture](assets/fr/03.webp)



### Vali versioon: Või Nvidia või Raspberry Pi (ARM64)



Pop!OS on saadaval kolmes variandis:



### Standardversioon



Soovitatav arvutitele, mis kasutavad :





- inteli või AMD protsessor;
- integreeritud Inteli või AMD GPU;
- aMD Radeon graafikakaart.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia versioon



Soovitatav Nvidia graafikakaartidega varustatud arvutitele.


See kujutis sisaldab juba Nvidia draivereid, mis lihtsustab paigaldamist ja vähendab graafikaprobleeme.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi versioon (ARM64)



Raspberry Pi 4 ja 400 (ARM-protsessor) jaoks.


See on ARM-arhitektuurile kohandatud spetsiaalne versioon nende miniarvutite jaoks.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Looge käivitatav USB-klahv



Saate kasutada mitmeid vahendeid, näiteks Balena Etcher :





- Lae alla ja paigalda [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Avage Balena Etcher, seejärel valige Pop!OS ISO image.
- Valige USB-mäluseadmeks USB-mälu.
- Klõpsake Flash ja oodake, kuni protsess on lõppenud.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Pop!OS-i paigaldamine ja turvamine



### Käivitamine USB-mäluseadmelt





- Lülitage arvuti välja.
- Ühendage USB-mäluseade (mis sisaldab Pop!OS-i).
- Lülitage arvuti sisse. Uuemate arvutite puhul peaks süsteem automaatselt USB-käivitusvõtme ära tundma. Kui see ei ole nii, käivitage seade uuesti, hoides all BIOS/UEFI juurdepääsuklahvi (tavaliselt F2, F12 või Delete, olenevalt tootemargist).
  - Valige BIOS/UEFI menüüs oma USB-mälu kui alglaadimisseade.
  - Salvestage ja taaskäivitage.



### Paigalduse käivitamine



Kui olete valinud oma käivitatava USB-mäluseadme stardiseadmeks, käivitub arvuti Pop!OS Live keskkonda.



Valige oma keel.



![Capture](assets/fr/10.webp)



Valige asukoht.



![Capture](assets/fr/11.webp)



Valige keel klaviatuuri sisestamiseks.



![Capture](assets/fr/12.webp)



Valige klaviatuuri paigutus.



![Capture](assets/fr/13.webp)



Valige standardse paigalduse jaoks valik `Clean Install` (Puhas paigaldus). See on parim valik uutele Linuxi kasutajatele, kuid pidage meeles, et see kustutab kogu sihtketta sisu. Alternatiivina võite valida `Try Demo Mode`, et jätkata Pop!OS-i testimist live-keskkonnas.



![Capture](assets/fr/14.webp)



GPartedile juurdepääsuks valige `Custom (Advanced)`. See tööriist võimaldab teil konfigureerida täiustatud funktsioone, nagu topeltkäivitamine, eraldi partitsiooni `/home` loomine või partitsiooni `/tmp` paigutamine teisele kettale.



Pop!OS-i paigaldamiseks valitud kettale klõpsake nuppu `Erase and Install`.



![Capture](assets/fr/15.webp)



### Kasutajakonto konfiguratsioon



Paigaldusprogrammi järgmine osa juhendab teid kasutajakonto loomisel, et saaksite uude operatsioonisüsteemi sisse logida.



Sisestage täisnimi (see võib sisaldada mis tahes teksti, mis tahes suur- või väiketähtedega), samuti kasutajanimi (mis peab olema väiketähtedega) :



![Capture](assets/fr/16.webp)



Kui konto on loodud, palutakse teil määrata uus parool.



![Capture](assets/fr/17.webp)



### Täielik ketta krüpteerimine



Süsteemi ketta krüpteerimine ei ole vajalik, kuid see tagab kasutajaandmete turvalisuse juhul, kui keegi saab seadmele volitamata füüsilise juurdepääsu.



Ketta saab krüpteerida oma sisselogimise parooliga, märkides `Krüpteerimise parool on sama mis kasutajakonto parool`. Te võite ka selle ruudukese ära märkida ja valida allosas `Set Password` (määrake salasõna). Valige `Don't Encrypt`, et ignoreerida ketta krüpteerimist.



![Capture](assets/fr/18.webp)



Kui olete valinud nupu `Set Password`, näete täiendavat nõuet määrata oma krüpteerimisparool.



Jätkake paigaldusprogrammi järgmise sammuga. Pop!OS alustab nüüd paigaldamist kettale.



![Capture](assets/fr/19.webp)



Kui paigaldus on lõpetatud, taaskäivitage arvuti ja logige sisse, et lõpetada kasutajakonto konfigureerimine.



Kui olete muutnud käivitamisjärjekorda, et anda prioriteediks Live USB-mälu käivitamisel, lülitage arvuti täielikult välja ja eemaldage installimise USB-mälu. Kui olete kahekäivitusrežiimis, vajutage vastavaid klahve, et pääseda konfiguratsioonile ja valida Pop!OS-i paigaldust sisaldav ketas.



![Capture](assets/fr/20.webp)



### NVIDIA graafika



Kui olete installeerinud Intel/AMD ISO-st ja teie süsteemis on eraldiseisev NVIDIA graafikakaart või kui olete selle hiljem lisanud, peate optimaalse jõudluse saavutamiseks käsitsi installima oma kaardi draiverid. Juhi installimiseks käivitage käsuterminalis järgmine käsk:



```bash
sudo apt install system76-driver-nvidia
```



NVIDIA graafikadraiverid saab paigaldada ka Pop!_Shopist.



![Capture](assets/fr/20.webp)



## Oluliste tööriistade paigaldamine



Pop!OS pakub laia valikut tarkvara oma Pop!Shopi kaudu, kuid paljusid olulisi tööriistu saab paigaldada ka terminali kaudu `apt` või `flatpak` abil. Siin on kirjeldatud, kuidas paigaldada peamised tööriistad täieliku töökeskkonna jaoks.



### Terminali paigaldamine



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Paigaldamine Pop! Shop (graafiline kasutajaliides)





- Avage **Pop!_Shop** peamenüüst.
- Kasutage otsinguriba, et leida soovitud rakendused (näiteks "Brave").
- Klõpsake iga rakenduse puhul **Install**.
- Pop!_Shop haldab sõltuvusi ja uuendusi automaatselt.



## Süsteemi uuendamine



### Võimalus 1: graafilise kasutajaliidese (GUI) kaudu



Pop!OS pakub lihtsat ja intuitiivset graafilist uuenduste haldurit.



1. Klõpsake **peamenüüs** (ikoon all vasakul).


2. Avage **"Pop!_Shop "**.


3. Pop!_Shopis klõpsake vahekaardil **"Uuendused "**.


4. Süsteem kontrollib automaatselt, kas uuendused on saadaval.


5. Uuenduste paigaldamise alustamiseks klõpsake **"Update all "**.


6. Sisestage oma parool, kui seda nõutakse.


7. Laske protsess lõpule viia, seejärel käivitage see vajaduse korral uuesti.



### Võimalus 2: Terminali kaudu



Avage terminal ja sisestage :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Kasutajate haldamine



Soovitame kasutada igapäevasteks toiminguteks standardset kasutajakontot, millel on sudo õigused.



Uue kasutaja loomiseks :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Logige välja ja seejärel logige uuesti sisse selle uue kasutajaga.



### Graafikadraiveri haldamine





- Nvidia kaartide puhul kontrollige, et on paigaldatud patenteeritud draiverid:



```bash
sudo apt install system76-driver-nvidia
```





- AMD/Inteli puhul on draiverid tavaliselt vaikimisi lisatud.



### Aktiveeri tulemüür (UFW)



Pop!OS ei blokeeri võrguliiklust vaikimisi. Turvalisuse suurendamiseks aktiveerige UFW:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Automaatsete värskenduste seadistamine



Süsteemi ajakohasena hoidmine ilma käsitsi sekkumiseta:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Kohandage välimust ja käitumist





- Avage **Süsteemi seaded** → **Esitus**, et valida heledat või tumedat teemat.
- Seadistage aktiivsed nurgad, animatsioonid ja laiendused COSMICi halduri kaudu.
- Reguleerige töölaua paigutust, et optimeerida oma töövoogu.



### Automaatse varundamise seadistamine



Pop!OS integreerib varundamiseks selliseid vahendeid nagu Deja Dup:





- Käivitage menüüst **Backup**.
- Valige väline ketas või võrgukoht.
- Planeeri regulaarsed varundused.



### Kasulike GNOME/COSMICi laienduste paigaldamine



Siin on mõned soovituslikud laiendused, mis parandavad kasutajakogemust:





- Dash to Dock**: rakenduste riba on alati nähtav.
- GSConnect**: sünkroniseerimine Androidiga.
- Lõikeplaadi näitaja**: täiustatud lõikeplaadi haldamine.



Paigaldage need läbi :



```bash
sudo apt install gnome-shell-extensions
```



Seejärel aktiveerige need seadetes.



### Mälu ja andmevahetuse haldamise optimeerimine



Kontrollige oma vahetuse staatust:



```bash
swapon --show
```



Vajaduse korral suurendage swap-faili suurust või konfigureerige swap-faili :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Lisage see faili `/etc/fstab` automaatseks paigaldamiseks.



## Pakettide ja repositooriumide haldamine



### Paketi allikate mõistmine



Pop!OS, mis põhineb Ubuntu-l, kasutab peamiselt :





- Ametlikud Ubuntu** repositooriumid: enamiku stabiilse tarkvara jaoks.
- System76** repositooriumid: draiverite, püsivara ja spetsiifiliste tööriistade jaoks.
- Flatpak**: juurdepääs paljudele liivakastirakendustele.
- Snap** (valikuline): teine universaalne pakendivorming.



---

### PPA repositooriumide lisamine ja haldamine



Sageli uuendatud tarkvara installimiseks saab lisada teatud PPA-d (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Kokkuvõte



Pop!OS on kaasaegne ja stabiilne Linuxi distributsioon, mis sobib nii algajatele kui ka edasijõudnutele.



Tänu intuitiivsele COSMICi kasutajaliidesele ja integreeritud tööriistadele pakub see sujuvat ja produktiivset kasutuskogemust nii arendamiseks, loomiseks kui ka igapäevaseks kasutamiseks.



See õpetus hõlmab peamisi etappe: ettevalmistus, allalaadimine, paigaldamine, algseadistused ja olulised tööriistad.



Uurige Pop!OS-i edasi ja kohandage oma keskkonda, et sellest kõige rohkem kasu saada.