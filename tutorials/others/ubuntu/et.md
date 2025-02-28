---
name: Ubuntu
description: Täielik juhend Ubuntu installimiseks ja kasutamiseks Windowsi alternatiivina
---
![cover](assets/cover.webp)

## Sissejuhatus

Operatsioonisüsteem (OS) on peamine tarkvara, mis haldab kõiki arvuti ressursse. Alternatiivse operatsioonisüsteemi, nagu Ubuntu, valimine võib pakkuda palju eeliseid turvalisuse, kulude ja privaatsuse osas.

### Miks Ubuntu?


- Tõhustatud turvalisus** : Linuxi distributsioonid on tuntud oma turvalisuse ja töökindluse poolest
- Nullkulu**: Ubuntu ja enamik Linuxi distributsioone on tasuta
- Suur kogukond**: Kasutajate kogukond, kes on valmis aitama foorumite ja õpetuste kaudu
- Eraelu puutumatuse austamine**: Avatud lähtekoodiga süsteem suurema läbipaistvuse tagamiseks
- Lihtsus**: Kasutajasõbralik kasutajaliides ja kasutusmugavus
- Rikkalik ökosüsteem** : Ulatuslik avatud lähtekoodiga tarkvara kataloog
- Regulaarne toetus**: Turvalised uuendused Canonicalilt

## Paigaldamine ja konfigureerimine

### 1. Eeltingimused

**Vajalikud seadmed:**


- Vähemalt 12 GB suurune USB-mälu
- Arvuti, millel on vähemalt 25 GB vaba ruumi

### 2. Lae alla


- Mine [ubuntu.com/download](https://ubuntu.com/download)
- Valige stabiilne versioon (soovitatav on LTS)
- ISO-kujutise allalaadimine

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Looge käivitatav USB-klahv

Saate kasutada mitmeid vahendeid, näiteks Balena Etcher :


- Lae alla ja paigalda [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Avage Balena Etcher, seejärel valige Ubuntu ISO-kujutis
- Valige USB-mäluseadmeks USB-mälu
- Klõpsake Flash ja oodake, kuni protsess on lõppenud

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Ubuntu installimine ja turvamine

**4.1 Käivitamine USB-mälupulgalt** (prantsuse keeles)


- Lülita arvuti välja
- Ühendage USB-mäluseade (mis sisaldab Ubuntut)
- Lülitage arvuti sisse. Uuemate arvutite puhul peaks süsteem automaatselt USB-käivitusvõtme ära tundma. Kui see ei ole nii, taaskäivitage arvuti, hoides all BIOS/UEFI juurdepääsuklahvi (tavaliselt F2, F12 või Delete, olenevalt tootemargiast)
 - Valige BIOS/UEFI menüüst oma USB-klahv kui alglaadimisseade
 - Salvesta ja taaskäivita

**4.2 Installeerimise käivitamine** (prantsuse keeles)

**Start-up ekraan**

USB-mäluseadmest käivitamisel näete seda ekraani, mis võimaldab teil Ubuntut käivitada.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Valik keel

Valige paigaldamise ja süsteemi eelistatud keel.

![Sélection de la langue](assets/fr/07.webp)

**Kättesaadavuse valikud

Konfigureerige vajaduse korral ligipääsetavuse valikud (ekraanilugeja, kõrge kontrastsus jne).

![Options d'accessibilité](assets/fr/08.webp)

**Tahvli konfigureerimine

Valige oma klaviatuuri paigutus. Kontrollimiseks, et klahvid vastaksid teie konfiguratsioonile, on saadaval testväli.

![Configuration du clavier](assets/fr/09.webp)

**Võrguühendus**

Uuenduste allalaadimiseks installimise ajal ühenduge Wi-Fi- või traadiga võrku.

![Configuration réseau](assets/fr/10.webp)

**Tüüpi paigaldus

Valige kas "Proovi Ubuntu" (testimiseks ilma installimiseta) või "Installi Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Installatsioonimeetod

Valige interaktiivne paigaldus.

![Mode d'installation](assets/fr/12.webp)

**Valikatsioonivalik

Valige kas vaikimisi paigaldus või laiendatud valik rakendusi.

![Sélection des applications](assets/fr/13.webp)

**Kolmanda osapoole rakendused

Otsustage, kas paigaldada täiendavaid draivereid ja patenteeritud tarkvara või mitte.

![Installation applications tierces](assets/fr/14.webp)

**Tüüpi partitsioneerimine

Teil on kaks peamist võimalust:


- "Ketta kustutamine ja Ubuntu installimine": kasutab kogu ketast Ubuntu jaoks
- " Käsitsi paigaldamine: luua Windowsiga topeltkäivitus või kohandada oma partitsioone

![Choix du partitionnement](assets/fr/15.webp)

**Kasutajakonto loomine

Määrake oma Ubuntu konto kasutajanimi ja parool.

![Création du compte](assets/fr/16.webp)

**Ajavöönd

Valige oma geograafiline piirkond, et määrata süsteemi kellaaeg.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Installatsiooni kokkuvõte**

Kontrollige kõiki oma valikuid enne lõpliku paigaldamise alustamist. Kui klõpsate nupule "Install", algab protsess.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Ubuntu uuendamine pärast paigaldamist** (prantsuse keeles)

Süsteemi uuendamine on oluline samm pärast uut paigaldamist. Teil on kaks võimalust:

**Võimalus 1: graafilise kasutajaliidese kaudu**


- Otsige rakenduste menüüst "Tarkvara ja uuendused"
- Rakendus otsib automaatselt olemasolevaid uuendusi
- Järgige uuenduste installimiseks ekraanil kuvatavaid juhiseid

**Võimalus 2: Terminali kaudu


- Avage terminal (Ctrl + Alt + T)
- Kirjutage järgmine käsk, et kontrollida saadaolevaid uuendusi:

```bash
sudo apt update
```


- Sisestage oma parool, kui seda küsitakse
- Uuenduste installimiseks sisestage :

```bash
sudo apt upgrade
```


- Kinnitage paigaldamine, sisestades 'Y' ja seejärel Enter

### 5. Põhiülesannete avastamine

**5.1 Internetis surfamine

Vaikimisi leiate Firefoxi sageli käivitamisribalt.

Käivitage Firefox ja alustage sirvimist.

Teisi brausereid (Chrome, Brave jne) saab paigaldada Tarkvarahalduri või .deb-pakettide kaudu.

**5.2 Tekstitöötlus

Ubuntu tuleb koos LibreOffice'i paketiga (Writer tekstitöötluseks).

Selle avamiseks : Tegevused > Otsi "LibreOffice Writer" või klõpsa ikoonil, kui see ilmub ribale.

Saate luua, redigeerida ja salvestada dokumente erinevates vormingutes (sh .docx).

**5.3 Rakenduste paigaldamine

Tarkvarahaldur (nimega "Ubuntu tarkvara"): graafiline kasutajaliides rakenduste otsimiseks ja installimiseks.

Kasutage terminalist käsku :

```bash
sudo apt install nom-du-paquet
```

Näide:

```bash
sudo apt install vlc
```

### 6. Järeldus ja lisaressursid

Nüüd olete valmis Ubuntut igapäevaselt kasutama: turvake oma süsteemi, sirvige, tehke kontoritööd, installige tarkvara ja hoidke oma operatsioonisüsteemi ajakohasena!

Kui soovite oma digitaalse elu turvalisust veelgi suurendada, soovitame vaadata meie krüpteeritud sõnumiteenust, mis sobib suurepäraselt teie privaatsuse kaitsmiseks ja täiendab teie Ubuntu installimist:

https://planb.network/tutorials/others/proton-mail