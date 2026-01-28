---
name: Kali
description: Kali Linuxi paigaldamine VirtualBoxi, käivitatava USB-pulga või dual bootina, samm-sammult.
---

![cover-kali](assets/cover.webp)



## Sissejuhatus



### Miks Kali Linux?



**Kali Linux** on IT-turvalisusele spetsialiseerunud Linuxi distributsioon.


Siin on põhjus, miks me kasutame Kali Linuxi:





- See on eelkonfigureeritud paljude pentesti tööriistadega (süsteemi- ja võrguturbe testid).
- See on **avatud lähtekoodiga ja tasuta**, seega saate seda vabalt kasutada ja muuta.
- See on **loetav ja turvaline**, ideaalne küberturvalisuse õppimiseks.
- See võimaldab teil õppida Linuxi kasutamist testimisvalmis keskkonnas.
- Seda saab paigaldada erinevatel viisidel: **VirtualBox**, **käivitatav USB-mälu** või **kaksikstart**.



## Paigaldamine ja konfigureerimine



### 1. Eeltingimused



**Vajalikud seadmed:**





- 64-bitine protsessor** (Intel või AMD).
- vähemalt 8 GB RAM** (4 GB võib olla piisav lihtsa installeerimise või VM-i puhul).
- 50 GB vaba kettaruumi** Kali Linuxi installimiseks.
- Internetiühendus** ISO-kujutise ja uuenduste allalaadimiseks.
- Vähemalt 8 GB suurune USB-ketas** käivitatava meedia loomiseks (kui soovite Kali arvutisse paigaldada või seda Live USB-l testida).



Enne olemasolevasse arvutisse paigaldamist on oluline teha varukoopia oma andmetest.



### 2. Lae alla





- Mine [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Valige oma rakenduse jaoks ISO-kujutis:
  - Install Image** : arvutisse paigaldamiseks.
  - Virtuaalne kujutis**: Kali installimiseks VirtualBoxi või VMware'ile.
- Laadige ISO-kujutis alla.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Looge käivitatav USB-klahv



Saate kasutada mitmeid vahendeid, näiteks Balena Etcher :





- Lae alla ja paigalda [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Avage Balena Etcher, seejärel valige Kali ISO image.
- Valige USB-mäluseadmeks USB-mälu.
- Klõpsake nuppu Flash ja oodake, kuni protsess on lõppenud.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kali Linuxi paigaldamine ja turvamine



#### 4.1 Käivitamine USB-mäluseadmelt





- Lülitage arvuti välja.
- Ühendage USB-mäluseade (mis sisaldab Kali Linuxi).
- Lülitage arvuti sisse. Uuemate arvutite puhul peaks süsteem automaatselt USB-käivitusvõtme ära tundma. Kui see ei ole nii, käivitage seade uuesti, hoides all BIOS/UEFI juurdepääsuklahvi (tavaliselt F2, F12 või Delete, olenevalt tootemargist).
  - Valige BIOS/UEFI menüüs oma USB-mälu kui alglaadimisseade.
  - Salvestage ja taaskäivitage.



#### 4.2 Installeerimise käivitamine



##### Käivitusekraan



USB-mälupulgalt käivitamisel peaks ilmuma Kali Linuxi alglaadimisekraan. Valige **graafiline paigaldus** ja **tekstiinstallatsioon**. Selles näites valisime graafilise installimise.



![capture](assets/fr/06.webp)



Kui kasutate **Live** pilti, näete veel ühte režiimi, **Live**, mis on ka vaikimisi käivitusvõimalus.



![Mode Live](assets/fr/07.webp)



##### Keele valik



Valige paigaldamise ja süsteemi eelistatud keel.



![Sélection de la langue](assets/fr/08.webp)



Palun täpsustage oma geograafiline asukoht.



![Options d'accessibilité](assets/fr/09.webp)



##### Klaviatuuri konfiguratsioon



Valige oma klaviatuuri paigutus. Kontrollimiseks, et klahvid vastaksid teie konfiguratsioonile, on saadaval testväli.



![Configuration du clavier](assets/fr/10.webp)



##### Võrguühendus



Paigaldus otsib nüüd teie võrguliideseid, otsib DHCP-teenust ja palub teil seejärel sisestada oma süsteemi hostinimi. Alljärgnevas näites oleme sisestanud **"kali "** hostinimeks.



![Configuration réseau](assets/fr/11.webp)



Saate valikuliselt anda vaikimisi domeeninime, mida see süsteem kasutab (väärtused saab kätte DHCP-st või kui on olemas juba olemasolev operatsioonisüsteem).



![Choix du type d'installation](assets/fr/12.webp)



##### Kasutajakontod



Seejärel looge süsteemi kasutajakonto (täisnimi, kasutajanimi ja tugev parool).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Ajavöönd



Valige oma geograafiline piirkond, et määrata süsteemi kellaaeg.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Jaotustüüp



Seejärel skaneerib paigaldaja teie kettad ja kuvab sõltuvalt teie konfiguratsioonist mitu võimalust.



Selles juhendis alustame **tühjast kettast**, mis annab **neli võimalikku valikut**.


Me valime **juhendatud - kasutame kogu ketast**, kuna siinkohal teeme Kali Linuxi ühekordset paigaldust (ühekordne käivitamine). See tähendab, et mingit muud operatsioonisüsteemi ei säilitata ja kogu ketas võidakse kustutada.



Kui teie kettal on juba andmeid, võib ilmuda lisavõimalus **Juhend - kasuta suurimat külgnevat vaba ruumi**.



See alternatiiv võimaldab paigaldada Kali Linuxi ilma olemasolevaid andmeid kustutamata, mis teeb selle ideaalseks topeltkäivitamiseks koos teise süsteemiga.



Meie puhul on ketas tühi, nii et see valik ei ilmu.



![Choix du partitionnement](assets/fr/17.webp)



Valige partitsioneeritav ketas.



![capture](assets/fr/18.webp)



Sõltuvalt teie vajadustest võite valida, kas hoida kõiki faile ühes partitsioonis (vaikimisi käitumine) või eraldi partitsioone ühe või mitme tippkataloogi jaoks.



Kui te ei ole kindel, mida soovite, valige valik **Kõik failid ühes partitsioonis**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Seejärel on teil viimane võimalus kontrollida oma ketta konfiguratsiooni, enne kui paigaldusprogramm teeb pöördumatuid muudatusi. Kui olete klõpsanud nuppu _Jaota_, käivitub paigaldusprogramm ja paigaldus on peaaegu lõpetatud.



![capture](assets/fr/21.webp)



##### Krüpteeritud LVM



Kui see valik oli eelmises sammus lubatud, siis teeb Kali Linux nüüd turvalise kõvaketta kustutamise enne, kui ta küsib teilt LVM-i parooli.



Palun kasutage tugevat salasõna, vastasel juhul kuvatakse hoiatus nõrga passphrase kohta.



##### Proxy teave



Kali Linux kasutab rakenduste levitamiseks repositooriume. Te peate sisestama vajalikud proxy andmed, kui teie keskkond seda kasutab.



Kui te **ei ole kindel**, kas kasutada proxy't, **jätke tühjaks**. Vale teabe sisestamine takistab ühendust repositooriumidega.



![capture](assets/fr/22.webp)



##### Metapets



Kui võrgujuurdepääs ei ole konfigureeritud, peate küsimisel **täiendavalt konfigureerima**.



Kui kasutate **Live** pilti, ei kuvata järgmist sammu.



Seejärel saate valida [metapaketid](https://www.kali.org/docs/general-use/metapackages/), mida soovite paigaldada. Vaikimisi valikud installivad standardse Kali Linuxi süsteemi, nii et te ei pea midagi muutma.



![capture](assets/fr/23.webp)



#### Käivitamisega seotud teave



Seejärel kinnitage GRUB-buutimislaaduri paigaldamine.



![capture](assets/fr/24.webp)



##### Restart



Lõpuks klõpsake Continue, et taaskäivitada oma uus Kali Linuxi paigaldus.



![capture](assets/fr/25.webp)



#### 4.3 Kali Linuxi uuendamine ja konfigureerimine pärast paigaldamist



Süsteemi uuendamine on oluline samm pärast uut paigaldamist. Teil on kaks võimalust:



##### Võimalus 1: graafilise kasutajaliidese (GUI) kaudu



Kali, nagu ka Debian/Ubuntu, pakub integreeritud graafilist uuenduste haldurit.



1. Klõpsake **peamenüüs** (vasakul üleval või all, sõltuvalt teie töölauast).


2. Avage **"Tarkvara uuendaja "**.


3. Tööriist :




    - Kontrollige uuendatavaid pakette.
    - Näete nimekirja (koos suuruste ja versioonidega).
    - Võimaldab käivitada uuenduse ühe klõpsuga.


4. Sisestage administraatori parool (`sudo`), kui seda küsitakse.


5. Laske sellel paigaldada ja vajaduse korral taaskäivitada.



##### Võimalus 2: Terminali kaudu



Avage terminal ja käivitage :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Igapäevaseks tööks ei ole soovitatav kasutada **juurdunud** kontot; looge selle asemel mittejuurdunud kasutaja.



Sisestage oma terminalis järgmised käsud:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Logige välja ja logige uuesti sisse uue kasutajaga.



Võtame tabelis kokku mõned põhilised Kali Linuxi ülesanded.



### Põhilised ülesanded Kali Linuxi all




| **Kategooria** | **Põhiülesanne** | **Kirjeldus / Eesmärk** | **Peamine meetod** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Süsteemi navigeerimine** | Terminali avamine | Juurdepääs Kali peamisele käsureale | Klõpsake terminali ikoonil või kasutage `Ctrl + Alt + T` |
| | Kaustade sirvimine | Süsteemi kataloogipuus liikumine | `cd /tee/kaustani`, `ls` failide loetlemiseks |
| | Kausta loomine / kustutamine | Failide organiseerimine | `mkdir kausta_nimi`, `rm -r kausta_nimi` |
| **Failihaldus** | Faili kopeerimine / liigutamine | Failidega manipuleerimine terminalis | `cp fail sihtkoht`, `mv fail sihtkoht` |
| | Faili kustutamine | Kettaruumi vabastamine | `rm faili_nimi` |
| | Tekstifaili sisu kuvamine | Faili kiire lugemine | `cat fail.txt`, `less fail.txt` |
| **Süsteemihaldus** | Kali Linuxi värskendamine | Viimaste versioonide ja turvapaikade installimine | `sudo apt update && sudo apt full-upgrade -y` |
| | Tarkvara installimine | Uue tööriista või utiliidi lisamine | `sudo apt install paketi_nimi` |
| | Tarkvara eemaldamine | Süsteemi puhastamine | `sudo apt remove paketi_nimi` |
| | Mittevajalike sõltuvuste puhastamine | Kettaruumi säästmine | `sudo apt autoremove` |
| **Võrk ja internet** | Võrguühenduse kontrollimine | Interneti-pääsu testimine | `ping google.com` |
| | IP-aadressi tuvastamine | Oma võrgukonfiguratsiooni teadmine | `ip a` või `ifconfig` |
| | Wi-Fi võrgu vahetamine | Teise pääsupunktiga ühenduse loomine | Võrguikoon → Vali soovitud Wi-Fi |
| **Kontod ja õigused** | Administraatori käsu täitmine | Ajutiste juurõiguste saamine | `sudo käsk` |
| | Uue kasutaja loomine | Kohaliku konto lisamine | `sudo adduser kasutajanimi` |
| | Parooli muutmine | Konto turvamine | `passwd` |
| **Välimus ja mugavus** | Taustapildi muutmine | Töölaua isikupärastamine | Paremklõps töölaual → **Töölaua seaded** |
| | Teema / ikoonide muutmine | Loetavuse ja esteetika parandamine | Seaded → Välimus / Teemad |
| **Kali tööriistad** | Tööriistade menüü avamine | Testimis- ja turvatööriistade uurimine | Menüü **Rakendused → Kali Linux** |
| | Tööriista käivitamine (nt: nmap, wireshark) | Turvautiliitide praktiline avastamine | `sudo nmap`, `wireshark` jne. |
| **Abi ja dokumentatsioon** | Abi saamine käsu kohta | Käsu mõistmine enne selle kasutamist | `man käsk` või `käsk --help` |

## Kokkuvõte



Kali Linuxi installimine on vaid esimene samm selle võimsa küberturvalisusele pühendatud keskkonna avastamisel. Põhiülesandeid ja süsteemi haldamist omandades saab igaüks hakata uurima sisseehitatud tööriistu ja mõistma Linuxi süsteemi sisemisi toiminguid. Kali pakub suurepärast õppeplatvormi nii tehniliste oskuste kinnistamiseks kui ka tõelise IT-turbe kultuuri arendamiseks.