---
name: Ubuntu
description: Komplett guide till installation och användning av Ubuntu som ett alternativ till Windows
---
![cover](assets/cover.webp)


## Inledning


Ett operativsystem (OS) är den huvudsakliga programvaran som hanterar alla datorns resurser. Att välja ett alternativt operativsystem som Ubuntu kan erbjuda många fördelar när det gäller säkerhet, kostnad och integritet.


### Varför Ubuntu?




- Förbättrad säkerhet** : Linux-distributioner är välkända för sin säkerhet och robusthet
- Ingen kostnad**: Ubuntu och de flesta Linux-distributioner är kostnadsfria
- Stor gemenskap**: En grupp användare som är redo att hjälpa till via forum och handledning
- Respekt för den personliga integriteten**: System med öppen källkod för ökad transparens
- Enkelhet**: Användarvänlig Interface och enkel användning
- Rikt ekosystem** : Omfattande katalog med programvara med öppen källkod
- Regelbunden support**: Säkra uppdateringar från Canonical


## Installation och konfiguration


### 1. Förkunskapskrav


**Utrustning som krävs:**




- Ett USB-minne på minst 12 GB
- En dator med minst 25 GB tillgängligt


### 2. Nedladdningar




- Gå till [ubuntu.com/download] (https://ubuntu.com/download)
- Välj den stabila versionen (LTS rekommenderas)
- Ladda ner ISO-bild


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. Skapa en startbar USB-nyckel


Du kan använda flera verktyg, till exempel Balena Etcher :




- Ladda ner och installera [Balena Etcher] (https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Öppna Balena Etcher och välj sedan Ubuntu ISO-avbildningen
- Välj USB-nyckel som destinationsmedia
- Klicka på Flash och vänta på att processen ska slutföras


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Installera och säkra Ubuntu


**4.1 Starta från USB-minne** (på franska)




- Stäng av datorn
- Anslut USB-nyckeln (som innehåller Ubuntu)
- Slå på datorn. På nyare datorer bör systemet automatiskt känna igen USB-startnyckeln. Om så inte är fallet, starta om genom att hålla BIOS/UEFI-åtkomstknappen intryckt (vanligtvis F2, F12 eller Delete, beroende på märke)
 - I BIOS/UEFI-menyn väljer du din USB-nyckel som startenhet
 - Spara och starta om


**4.2 Starta installationen** (på franska)


**Startskärm för uppstart**


När du startar från USB-minnet ser du den här skärmen, där du kan starta Ubuntu.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**Val av språk


Välj önskat språk för installation och system.


![Sélection de la langue](assets/fr/07.webp)


**Alternativ för tillgänglighet


Konfigurera tillgänglighetsalternativ om det behövs (skärmläsare, hög kontrast etc.).


![Options d'accessibilité](assets/fr/08.webp)


**Konfiguration av tangentbord


Välj din tangentbordslayout. Ett testfält finns tillgängligt för att kontrollera att tangenterna motsvarar din konfiguration.


![Configuration du clavier](assets/fr/09.webp)


**Nätverksanslutning**


Anslut till ditt Wi-Fi-nätverk eller trådbundna nätverk för att ladda ner uppdateringar under installationen.


![Configuration réseau](assets/fr/10.webp)


**Typ av installation


Välj mellan "Try Ubuntu" (för att testa utan att installera) eller "Install Ubuntu".


![Choix du type d'installation](assets/fr/11.webp)


**Installationsmetod


Välj interaktiv installation.


![Mode d'installation](assets/fr/12.webp)


**Val av applikation


Välj mellan standardinstallationen eller ett utökat urval av applikationer.


![Sélection des applications](assets/fr/13.webp)


**Applikationer från tredje part


Bestäm om du vill installera ytterligare drivrutiner och proprietär programvara eller inte.


![Installation applications tierces](assets/fr/14.webp)


**Typ av partitionering


Du har två huvudalternativ:




- "Radera hårddisken och installera Ubuntu": använder hela hårddisken för Ubuntu
- "Manuell installation: skapa en dual boot med Windows eller anpassa dina partitioner


![Choix du partitionnement](assets/fr/15.webp)


**Skapande av användarkonto


Ange ditt användarnamn och lösenord för ditt Ubuntu-konto.


![Création du compte](assets/fr/16.webp)


**Tidszon


Välj ditt geografiska område för att ställa in systemtiden.


![Sélection du fuseau horaire](assets/fr/17.webp)


**Sammanfattning av installationen**


Kontrollera alla dina val innan du påbörjar den slutliga installationen. När du klickar på "Installera" börjar processen.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 Uppgradering av Ubuntu efter installation** (på franska)


Uppdatering av systemet är ett viktigt steg efter en ny installation. Du har två alternativ:


**Alternativ 1: Via den grafiska användargränssnittet Interface**




- Sök efter "Programvara och uppdateringar" i applikationsmenyn
- Programmet kommer automatiskt att söka efter tillgängliga uppdateringar
- Följ anvisningarna på skärmen för att installera uppdateringarna


**Alternativ 2: Via terminal




- Öppna terminal (Ctrl + Alt + T)
- Skriv följande kommando för att söka efter tillgängliga uppdateringar:


```bash
sudo apt update
```




- Ange ditt lösenord när du uppmanas att göra det
- För att installera uppdateringar, skriv :


```bash
sudo apt upgrade
```




- Bekräfta installationen genom att skriva "Y" och sedan Enter


### 5. Upptäcka grundläggande uppgifter


**5.1 Surfa på Internet


Som standard hittar du ofta Firefox i startfältet.


Starta Firefox och börja surfa.


Andra webbläsare (Chrome, Brave, etc.) kan installeras via Software Manager eller via .deb-paket.


**5.2 Ordbehandling


Ubuntu levereras med LibreOffice-paketet (Writer för ordbehandling).


Så här öppnar du den : Aktiviteter > Sök efter "LibreOffice Writer" eller klicka på ikonen om den visas i fältet.


Du kan skapa, redigera och spara dokument i en mängd olika format (inklusive .docx).


**5.3 Installera program


Programvaruhanterare (kallas "Ubuntu Software"): grafisk Interface för sökning och installation av program.


Använd kommandot från Terminal :


```bash
sudo apt install nom-du-paquet
```


Exempel:


```bash
sudo apt install vlc
```


### 6. Slutsats och ytterligare resurser


Nu är du redo att använda Ubuntu dagligen: säkra ditt system, surfa, göra kontorsarbete, installera programvara och hålla ditt operativsystem uppdaterat!


För att ta säkerheten i ditt digitala liv ett steg längre rekommenderar vi att du tar en titt på vår krypterade meddelandetjänst, som är perfekt lämpad för att skydda din integritet och kompletterar din Ubuntu-installation:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2