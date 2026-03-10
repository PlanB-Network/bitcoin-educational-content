---
name: Zorin OS
description: Komplett guide till installation och användning av Zorin OS som ett modernt alternativ till Windows
---

![cover](assets/cover.webp)



## Inledning



Ett operativsystem (OS) är den grundläggande programvara som gör att en dator kan fungera: det hanterar hårdvara, mjukvara, säkerhet och användargränssnitt.


Zorin OS är en Linux-distribution som är särskilt utformad för att underlätta övergången från Windows, samtidigt som den erbjuder fördelarna med programvara med öppen källkod: säkerhet, stabilitet, integritet och prestanda.



Zorin OS är baserat på Ubuntu LTS och kombinerar hög programvarukompatibilitet med ett välbekant och anpassningsbart gränssnitt, vilket gör det till ett trovärdigt och tillgängligt alternativ till Windows.



## Varför Zorin OS?





- Interface bekant**: Windows-liknande utseende (startmeny, aktivitetsfält)
- Enkel övergång**: utformad för användare som kommer från Windows
- Förbättrad säkerhet**: Linux-arkitektur, mindre utsatt för virus
- Respekt för privatlivet**: ingen påträngande datainsamling
- Optimerad prestanda**: fungerar bra på mindre maskiner
- Ubuntu LTS** bas: stabilitet, regelbundna uppdateringar och bred kompatibilitet
- Avancerad personalisering**: via Zorin Appearance tool.



## Installation och konfiguration



### 1. Förkunskapskrav



**Utrustning som krävs:**





- Ett USB-minne på minst **8 GB** (12 GB rekommenderas);
- En dator med minst **25 GB ledigt diskutrymme**
- Internetanslutning (rekommenderas).



### 2. Ladda ner Zorin OS





- Besök den officiella webbplatsen: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Välj **Zorin OS Core** (gratisversionen rekommenderas)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Ladda ner ISO-bild



Zorin OS erbjuder också :





- Zorin OS Lite** (äldre datorer)
- Zorin OS Pro** (avgiftsbaserat, med avancerade funktioner och support)



## Skapa ett startbart USB-minne



Du kan använda flera verktyg, till exempel Balena Etcher :





- Ladda ner och installera [Balena Etcher] (https://etcher.balena.io/).
- Öppna Balena Etcher och välj sedan Zorin ISO-imagen.
- Välj USB-nyckel som destinationsmedia.
- Klicka på Flash och vänta tills processen är klar.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Nyckel för uppstart och BIOS-åtkomst



Stäng av den dator som du vill installera Zorin OS på och anslut sedan USB-nyckeln.


När datorn startar går du in i BIOS (`ESC`, `F9` eller `F11` beroende på fabrikat) och väljer USB-nyckeln som startenhet och trycker sedan på `Enter` för att starta startprocessen.





- Vid start, välj **Testa eller installera Zorin OS**.



![capture](assets/fr/08.webp)





- Om du har ett NVIDIA-grafikkort väljer du **Testa eller installera Zorin OS (moderna NVIDIA-drivrutiner)**.
- Vänligen vänta medan filerna kontrolleras.



![capture](assets/fr/09.webp)





- I installationsprogrammet för Zorin OS väljer du språket **Franska** och klickar sedan på Installera **Zorin OS**.



![capture](assets/fr/10.webp)





- Välj tangentbordslayout.



![capture](assets/fr/11.webp)





- Markera rutorna **Hämta uppdateringar under installationen av Zorin OS** och **Installera programvara från tredje part för grafik- och Wi-Fi-hårdvara och ytterligare medieformat**.



![capture](assets/fr/12.webp)





- För att installera Zorin OS på hela disken: välj **Erase disk and install Zorin OS**.



![capture](assets/fr/14.webp)



För att installera Zorin OS tillsammans med Windows (dual-boot) :





- Välj **Installera Zorin OS bredvid Windows Boot Manager**.



![capture](assets/fr/15.webp)





- Om du inte har partitionerat din disk, välj det diskutrymme som du vill tilldela Zorin OS och klicka sedan på **Installera nu**.



![capture](assets/fr/16.webp)





- Bekräfta ändringarna på skivan två gånger.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Välj det geografiska området **Paris**.



![capture](assets/fr/18.webp)





- Skapa ditt användarkonto och ge din dator ett namn.



![capture](assets/fr/19.webp)





- Vänligen vänta medan Zorin OS installeras.



![capture](assets/fr/20.webp)





- När installationen är klar klickar du på **Restart Now**.



![capture](assets/fr/21.webp)





- Ta bort USB-installationsnyckeln och tryck på Enter.



![capture](assets/fr/22.webp)



## Upptäcka och använda Zorin OS



### Första uppstarten



När du startar din dator kommer du till GRUB - Linux boot manager. Som standard är **Zorin OS** valt; efter 30 sekunder startar det automatiskt.



![capture](assets/fr/23.webp)



Om du har installerat Zorin OS som en dual-boot med Windows, kan du starta upp till Windows genom att välja **Windows Boot Manager**.



Logga in med ditt användarkonto :



![capture](assets/fr/24.webp)



Vid första uppstarten startas programmet **Welcome to Zorin OS** som hjälper dig att upptäcka ditt nya operativsystem.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Uppdatera systemet



Uppdateringshanteraren kommer snart att öppnas för att meddela att uppdateringar finns tillgängliga. Installera dem genom att klicka på knappen **Installera nu**.



![capture](assets/fr/33.webp)



Du kan manuellt kontrollera om det finns uppdateringar i programmet **Software** > Uppdateringar:



![capture](assets/fr/34.webp)



### Anpassning



Det första du ska göra i Zorin OS är att välja den **skrivbordslayout** du är mest bekväm med. Du kommer att hitta layouter som liknar dem som finns i Windows (och ännu mer med Pro-versionen).



För att göra detta, öppna **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Öppna sedan **Settings** för att anpassa ditt system:


**Ljud - Inställningar - Zorin OS



![capture](assets/fr/36.webp)



**Online-konton - Inställningar - Zorin OS



![capture](assets/fr/37.webp)



### Tillämpningar



Det finns flera sätt att installera program:





- Software**, Zorin OS applikationsbutik. Programmen kommer från flera källor: apt, Flatpak och Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** installera (kommandoraden) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



För mer information om hur du installerar program i Zorin OS, se denna sida: [Installera appar (zorin.com)](https://zorin.com/help/install-apps/).



### Windows-applikationer



För att installera Windows-applikationer börjar du med att installera paketet **zorin-windows-app-support** via Terminal :



```bash
sudo apt install zorin-windows-app-support
```



En lista över kompatibla Windows-program och deras kompatibilitetsnivåer finns på sidan [Wine Application Database] (https://appdb.winehq.org/). Där hittar du följande märken, som motsvarar kompatibilitetsnivån (från bäst till sämst): Platina, Guld, Silver, Brons och Skräp.



Om du vill installera en Windows .exe- eller .msi-applikation har du två alternativ:





- Öppna **PlayOnLinux** och klicka på knappen **Install** för att bläddra bland kompatibla program och spel.



![capture](assets/fr/41.webp)





- Dubbelklicka på programmets fil **.exe eller .msi** och låt installationsprogrammet guida dig.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Slutsats och ytterligare resurser



Zorin OS är ett gediget och prisvärt alternativ till Windows, som kombinerar enkelhet, säkerhet och integritet.



Det möjliggör en smidig övergång till Linux, utan att göra avkall på komfort eller produktivitet.



För att ytterligare skydda ditt digitala liv rekommenderar vi att du använder integritetsvänliga tjänster, särskilt för krypterad kommunikation:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2