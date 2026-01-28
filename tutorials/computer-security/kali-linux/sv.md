---
name: Kali
description: Installera Kali Linux på VirtualBox, som ett startbart USB-minne eller som en dual boot, steg för steg.
---

![cover-kali](assets/cover.webp)



## Inledning



### Varför Kali Linux?



**Kali Linux** är en Linux-distribution som är specialiserad på IT-säkerhet.


Här är anledningen till att vi använder Kali Linux:





- Den är förkonfigurerad med ett brett utbud av pentesting-verktyg (system- och nätverkssäkerhetstester).
- Det är **öppen källkod och gratis**, så du kan använda och modifiera det fritt.
- Den är **tillförlitlig och säker**, perfekt för att lära sig mer om cybersäkerhet.
- Det ger dig möjlighet att lära dig att använda Linux i en testklar miljö.
- Den kan installeras på olika sätt: **VirtualBox**, **bootable USB key**, eller **dual boot**.



## Installation och konfiguration



### 1. Förkunskapskrav



**Utrustning som krävs:**





- 64-bitars processor** (Intel eller AMD).
- minst 8 GB RAM** (4 GB kan vara tillräckligt för en lätt installation eller VM).
- 50 GB ledigt diskutrymme** för att installera Kali Linux.
- Internetanslutning** för nedladdning av ISO-bild och uppdateringar.
- Ett USB-minne på minst 8 GB** för att skapa ett startbart media (om du vill installera Kali på en dator eller testa det på Live USB).



Det är viktigt att säkerhetskopiera dina data innan du installerar på en befintlig dator.



### 2. Nedladdningar





- Gå till [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Välj den ISO-bild som passar din applikation:
  - Install Image** : för installation på PC.
  - Virtual Image**: för att installera Kali på VirtualBox eller VMware.
- Ladda ner ISO-avbildningen.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Skapa en startbar USB-nyckel



Du kan använda flera verktyg, till exempel Balena Etcher :





- Ladda ner och installera [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Öppna Balena Etcher och välj sedan Kali ISO-imagen.
- Välj USB-nyckel som destinationsmedia.
- Klicka på Flash och vänta tills processen är klar.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Installera och säkra Kali Linux



#### 4.1 Starta från USB-minne





- Stäng av datorn.
- Sätt i USB-minnet (som innehåller Kali Linux).
- Slå på datorn. På nyare datorer bör systemet automatiskt känna igen USB-startnyckeln. Om så inte är fallet kan du starta om genom att hålla BIOS/UEFI-åtkomstknappen intryckt (vanligtvis F2, F12 eller Delete, beroende på märke).
  - I BIOS/UEFI-menyn väljer du ditt USB-minne som startenhet.
  - Spara och starta om.



#### 4.2 Starta installationen



##### Startskärm



När du startar från USB-minnet ska startskärmen för Kali Linux visas. Välj mellan **grafisk installation** och **textinstallation**. I det här exemplet har vi valt grafisk installation.



![capture](assets/fr/06.webp)



Om du använder bilden **Live** kommer du att se ett annat läge, **Live**, som också är standardstartalternativet.



![Mode Live](assets/fr/07.webp)



##### Val av språk



Välj önskat språk för installation och system.



![Sélection de la langue](assets/fr/08.webp)



Vänligen ange ditt geografiska läge.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfiguration av tangentbord



Välj din tangentbordslayout. Ett testfält finns tillgängligt för att kontrollera att tangenterna motsvarar din konfiguration.



![Configuration du clavier](assets/fr/10.webp)



##### Nätverksanslutning



Installationen kommer nu att skanna dina nätverksgränssnitt, söka efter en DHCP-tjänst och sedan uppmana dig att ange ett värdnamn för ditt system. I exemplet nedan har vi angett **"kali"** som värdnamn.



![Configuration réseau](assets/fr/11.webp)



Du kan även ange ett standarddomännamn som systemet ska använda (värden kan hämtas från DHCP eller om det finns ett befintligt operativsystem).



![Choix du type d'installation](assets/fr/12.webp)



##### Användarkonton



Skapa sedan ett användarkonto för systemet (fullständigt namn, användarnamn och ett starkt lösenord).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Tidszon



Välj ditt geografiska område för att ställa in systemtiden.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Typ av partitionering



Installationsprogrammet skannar sedan dina diskar och visar flera alternativ beroende på din konfiguration.



I den här guiden utgår vi från en **blank disk**, vilket ger **fyra möjliga val**.


Vi kommer att välja **Guided - use entire disk**, eftersom vi här utför en engångsinstallation av Kali Linux (single boot). Detta innebär att inget annat operativsystem kommer att behållas och att hela disken kan raderas.



Om disken redan innehåller data kan ytterligare ett alternativ **Guided - use largest contiguous free space** visas.



Med det här alternativet kan du installera Kali Linux utan att radera befintliga data, vilket gör det idealiskt för dual booting med ett annat system.



I vårt fall är disken tom, så det här alternativet visas inte.



![Choix du partitionnement](assets/fr/17.webp)



Välj den disk som ska partitioneras.



![capture](assets/fr/18.webp)



Beroende på dina behov kan du välja att förvara alla filer i en enda partition (standardbeteende) eller ha separata partitioner för en eller flera toppkataloger.



Om du inte är säker på vad du vill kan du välja alternativet **Alla filer i en enda partition**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Du får då en sista möjlighet att kontrollera din diskkonfiguration innan installationsprogrammet gör några oåterkalleliga ändringar. När du har klickat på _Continue_ kommer installationsprogrammet att starta och installationen är nästan klar.



![capture](assets/fr/21.webp)



##### Krypterad LVM



Om det här alternativet aktiverades i föregående steg kommer Kali Linux nu att utföra en säker radering av hårddisken innan du ber om ett LVM-lösenord.



Använd ett starkt lösenord, annars visas en varning om ett svagt passphrase.



##### Fullmaktsinformation



Kali Linux använder repositories för att distribuera applikationer. Du måste ange nödvändig proxyinformation om din miljö använder en sådan.



Om du är **inte säker** på om du ska använda en proxy, **lämna blank**. Om du anger felaktig information kommer du inte att kunna ansluta till arkiven.



![capture](assets/fr/22.webp)



##### Metapeter



Om nätverksåtkomst inte har konfigurerats måste du göra **ytterligare konfigurering** när du uppmanas till det.



Om du använder bilden **Live** kommer nästa steg inte att visas.



Du kan sedan välja de [metapaket](https://www.kali.org/docs/general-use/metapackages/) som du vill installera. Standardalternativen installerar ett standard Kali Linux-system, så du behöver inte ändra något.



![capture](assets/fr/23.webp)



#### Information om uppstart



Bekräfta sedan installationen av GRUB-startladdaren.



![capture](assets/fr/24.webp)



##### Omstart



Klicka slutligen på Continue för att starta om din nya Kali Linux-installation.



![capture](assets/fr/25.webp)



#### 4.3 Uppdatering och konfiguration av Kali Linux efter installationen



Uppdatering av systemet är ett viktigt steg efter en ny installation. Du har två alternativ:



##### Alternativ 1: Via grafiskt användargränssnitt (GUI)



Kali, liksom Debian/Ubuntu, erbjuder en integrerad grafisk uppdateringshanterare.



1. Klicka på **huvudmenyn** (längst upp till vänster eller längst ner beroende på skrivbordet).


2. Öppna **"Software Updater"**.


3. Verktyget kommer att :




    - Kontrollera vilka paket som ska uppdateras.
    - Du kommer att se en lista (med storlekar och versioner).
    - Gör att du kan starta uppdateringen med ett enda klick.


4. Ange ditt administratörslösenord (`sudo`) när du uppmanas till det.


5. Låt den installera och starta om vid behov.



##### Alternativ 2: Via terminal



Öppna en terminal och kör :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Det är inte tillrådligt att använda **root**-kontot för dagligt arbete; skapa en användare som inte är root istället.



Skriv in följande kommandon i terminalen:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Logga ut och logga in igen med den nya användaren.



Låt oss sammanfatta några grundläggande Kali Linux-uppgifter i en tabell.



### Grundläggande uppgifter under Kali Linux




| **Kategori** | **Basuppgift** | **Beskrivning / Syfte** | **Huvudmetod** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Systemnavigering** | Öppna terminalen | Få tillgång till Kalis huvudsakliga kommandorad | Klicka på terminalikonen eller använd `Ctrl + Alt + T` |
| | Bläddra i mappar | Förflytta sig i systemets katalogträd | `cd /sökväg/till/mapp`, `ls` för att lista filer |
| | Skapa / ta bort en mapp | Organisera filer | `mkdir mappnamn`, `rm -r mappnamn` |
| **Filhantering** | Kopiera / flytta en fil | Hantera filer i terminalen | `cp fil destination`, `mv fil destination` |
| | Ta bort en fil | Frigöra diskutrymme | `rm filnamn` |
| | Visa innehållet i en textfil | Läsa en fil snabbt | `cat fil.txt`, `less fil.txt` |
| **Systemhantering** | Uppdatera Kali Linux | Installera de senaste versionerna och säkerhetspatchar | `sudo apt update && sudo apt full-upgrade -y` |
| | Installera programvara | Lägga till ett nytt verktyg eller verktygsprogram | `sudo apt install paketnamn` |
| | Ta bort programvara | Rensa systemet | `sudo apt remove paketnamn` |
| | Rensa onödiga beroenden | Spara diskutrymme | `sudo apt autoremove` |
| **Nätverk och Internet** | Kontrollera nätverksanslutning | Testa internetåtkomst | `ping google.com` |
| | Identifiera IP-adress | Känna till din nätverkskonfiguration | `ip a` eller `ifconfig` |
| | Byta Wi-Fi-nätverk | Ansluta till en annan åtkomstpunkt | Nätverksikon → Välj önskat Wi-Fi |
| **Konton och behörigheter** | Köra ett administratörskommando | Få tillfälliga root-rättigheter | `sudo kommando` |
| | Skapa en ny användare | Lägga till ett lokalt konto | `sudo adduser användarnamn` |
| | Ändra ett lösenord | Säkra ett konto | `passwd` |
| **Utseende och komfort** | Byta bakgrundsbild | Personalisera skrivbordet | Högerklicka på skrivbordet → **Skrivbordsinställningar** |
| | Ändra tema / ikoner | Förbättra läsbarhet och estetik | Inställningar → Utseende / Teman |
| **Kali-verktyg** | Öppna verktygsmenyn | Utforska test- och säkerhetsverktyg | Meny **Applikationer → Kali Linux** |
| | Starta ett verktyg (ex: nmap, wireshark) | Praktisk upptäckt av säkerhetsverktyg | `sudo nmap`, `wireshark`, etc. |
| **Hjälp och dokumentation** | Få hjälp med ett kommando | Förstå ett kommando innan det används | `man kommando` eller `kommando --help` |

## Slutsats



Att installera Kali Linux är bara det första steget i att upptäcka denna kraftfulla miljö som är avsedd för cybersäkerhet. Genom att bemästra grundläggande uppgifter och systemhantering kan alla börja utforska de inbyggda verktygen och förstå hur ett Linux-system fungerar. Kali erbjuder en utmärkt inlärningsplattform, både för att förstärka tekniska färdigheter och för att utveckla en genuin IT-säkerhetskultur.