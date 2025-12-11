---
name: Pop!_OS
description: Guide till installation av Pop!_OS, en Linux-distribution
---

![cover](assets/cover.webp)



## Inledning



Pop!OS är ett Linux-baserat operativsystem som utvecklats av **System76**, en amerikansk tillverkare som specialiserar sig på maskiner för utvecklare, designers och avancerade användare.



Pop!OS är utformat för att erbjuda en modern, stabil och högpresterande miljö och kännetecknas av en enkel upplevelse, kraftfulla verktyg och ett starkt fokus på produktivitet.



### Vem är System76?



System76 är ett amerikanskt företag grundat 2005 och baserat i Denver som specialiserar sig på tillverkning av bärbara datorer, stationära datorer och servrar som är särskilt utformade för Linux.



Till skillnad från traditionella tillverkare utvecklar System76 maskiner som är utformade för att vara öppna, reparerbara och inriktade på mjukvarufrihet.



System76 tillverkar inte bara datorer.



Företaget utvecklar också :




- Pop!OS**, ett eget Linux-baserat operativsystem;
- COSMIC**, den moderna, högpresterande skrivbordsmiljö som används av Pop!OS ;
- Open Firmware**, en firmware med öppen källkod baserad på Coreboot ;
- verktyg för utvecklare och designers.



Målet är att erbjuda högkvalitativ integration av hårdvara och mjukvara, jämförbar med Apples ekosystem, men helt öppen och centrerad kring Linux.



## Ett modernt, stabilt och tillgängligt system



Pop!OS bygger vidare på Ubuntu och ger det utmärkt stabilitet, bred hårdvarukompatibilitet och tillgång till ett enormt ekosystem av programvara.


Det ger ett elegant gränssnitt, COSMIC-skrivbordet, som är utformat för att vara smidigt, intuitivt och anpassningsbart, även för nya användare.



## Ett perfekt val för utvecklare, designers och krävande användare



Pop!OS är särskilt uppskattat av :





- utvecklare (förinstallerade verktyg, avancerad plattsättningshantering),
- användare med Nvidia- eller AMD-grafikkort,
- studenter och yrkesverksamma som söker ett tillförlitligt system,
- windows-användare som vill göra en enkel övergång.



Den innehåller automatisk plattsättning, ett tydligt programvarucenter och integrerade produktivitetsverktyg som underlättar den dagliga användningen.



## Pop!OS höjdpunkter





- Optimerad prestanda** tack vare regelbundna uppdateringar.
- Två ISO-versioner tillgängliga**: standard och Nvidia-optimerad.
- Förbättrad säkerhet** (LUKS-kryptering tillgänglig vid installation).
- Interface COSMIC** ergonomisk och modern.
- Mycket kompatibel** med Ubuntu och Flatpak-programvaran.



## Ladda ner POP!OS på ett säkert sätt



### 1. Förkunskapskrav



Innan du hämtar och installerar POP!OS finns det några saker du måste göra för att förbereda installationsmiljön på rätt sätt.



### Utrustning som krävs





- En kompatibel dator**: Intel- eller AMD-processor, Intel / AMD / Nvidia GPU.
- Minst 4 GB RAM** (8 GB rekommenderas för bekväm användning).
- minst 20 GB ledigt utrymme** (40 GB eller mer rekommenderas).
- Ett USB-minne på minst 4 GB** för att skapa installationsmediet.



### Internetanslutning



En stabil anslutning är användbar för :





- ladda ner ISO-bilden,
- installera uppdateringar efter installationen.



Pop!OS kan köras utan uppkoppling, men installationen är mycket smidigare via Internet.



### Säkerhetskopiering av data



Om Pop!OS ska ersätta eller samexistera med ett annat system (Windows, Ubuntu, etc.) är det lämpligt att säkerhetskopiera viktiga filer innan du fortsätter.



### Kontrollera om det finns en Nvidia GPU (om tillämpligt)



För datorer som är utrustade med ett Nvidia-grafikkort måste du hämta den speciella ISO-avbildningen som innehåller Nvidia-drivrutinerna.


Denna kontroll är mycket enkel:





- genom att läsa specifikationerna för datorn,
- eller genom att leta upp grafikkortsmodellen i systeminställningarna.



### Ladda ner från den officiella webbplatsen



ISO-bilden för Pop!OS ska laddas ner direkt från den officiella System76-sidan: [system76.com/pop] (https://system76.com/pop/).



På denna sida finns alltid den senaste versionen, anpassad till din maskinvara.



![capture](assets/fr/03.webp)



### Välj version: Standard eller Nvidia, eller Raspberry Pi (ARM64)



Pop!OS finns i tre olika varianter:



### Standardversion



Rekommenderas för datorer som använder :





- intel- eller AMD-processor;
- en integrerad Intel- eller AMD-GPU;
- ett AMD Radeon-grafikkort.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia-version



Rekommenderas för datorer utrustade med Nvidia-grafikkort.


Den här bilden innehåller redan Nvidia-drivrutiner, vilket gör installationen enklare och minskar grafikproblemen.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi-version (ARM64)



För Raspberry Pi 4 och 400 (ARM-processor).


Anpassad till ARM-arkitekturen är detta en specifik version för dessa minidatorer.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Skapa en startbar USB-nyckel



Du kan använda flera verktyg, till exempel Balena Etcher :





- Ladda ner och installera [Balena Etcher] (https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Öppna Balena Etcher och välj sedan ISO-bilden Pop!OS.
- Välj USB-nyckel som destinationsmedia.
- Klicka på Flash och vänta tills processen är klar.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Installera och säkra Pop!OS



### Starta från USB-nyckel





- Stäng av datorn.
- Sätt i USB-stickan (som innehåller Pop!OS).
- Slå på datorn. På nyare datorer bör systemet automatiskt känna igen USB-startnyckeln. Om så inte är fallet kan du starta om genom att hålla BIOS/UEFI-åtkomstknappen intryckt (vanligtvis F2, F12 eller Delete, beroende på märke).
  - I BIOS/UEFI-menyn väljer du ditt USB-minne som startenhet.
  - Spara och starta om.



### Starta installationen



När du har valt ditt startbara USB-minne som startenhet kommer datorn att starta i en Pop!OS Live-miljö.



Välj ditt språk.



![Capture](assets/fr/10.webp)



Välj en plats.



![Capture](assets/fr/11.webp)



Välj ett språk för tangentbordsinmatning.



![Capture](assets/fr/12.webp)



Välj en tangentbordslayout.



![Capture](assets/fr/13.webp)



Välj alternativet `Clean Install` för en standardinstallation. Detta är det bästa alternativet för nya Linux-användare, men var medveten om att det kommer att radera allt innehåll på målenheten. Alternativt kan du välja `Try Demo Mode` för att fortsätta testa Pop!OS i en live-miljö.



![Capture](assets/fr/14.webp)



Välj `Custom (Advanced)` för att komma åt GParted. Med det här verktyget kan du konfigurera avancerade funktioner som dubbelstart, skapa en separat `/home`-partition eller placera `/tmp`-partitionen på en annan enhet.



Klicka på `Erase and Install` för att installera Pop!OS på den valda enheten.



![Capture](assets/fr/15.webp)



### Konfiguration av användarkonto



I nästa del av installationsprogrammet får du hjälp med att skapa ett användarkonto så att du kan logga in på ditt nya operativsystem.



Ange ett fullständigt namn (detta kan innehålla valfri text, stora eller små bokstäver), samt ett användarnamn (som måste vara i små bokstäver) :



![Capture](assets/fr/16.webp)



När kontot har skapats kommer du att bli ombedd att ange ett nytt lösenord.



![Capture](assets/fr/17.webp)



### Fullständig diskkryptering



Kryptering av systemdisken är inte nödvändigt, men det garanterar säkerheten för användardata i händelse av att någon får obehörig fysisk åtkomst till enheten.



Enheten kan krypteras med hjälp av ditt inloggningslösenord genom att markera `Encryption password is the same as user account password`. Du kan också avmarkera den här rutan och välja `Set Password` längst ned. Välj `Don't Encrypt` för att ignorera diskkrypteringsprocessen.



![Capture](assets/fr/18.webp)



Om du har valt knappen "Ange lösenord" visas ytterligare en uppmaning att ange ditt krypteringslösenord.



Fortsätt till nästa steg i installationsprogrammet. Pop!OS kommer nu att påbörja installationen på disken.



![Capture](assets/fr/19.webp)



När installationen är klar startar du om datorn och loggar in för att slutföra konfigurationen av användarkontot.



Om du har ändrat startordningen så att Live-USB-nyckeln prioriteras vid uppstart, stäng av datorn helt och hållet och ta bort installations-USB-nyckeln. Om du är i dual-boot-läge, tryck på lämpliga tangenter för att komma åt konfigurationen och välj den enhet som innehåller Pop!OS-installationen.



![Capture](assets/fr/20.webp)



### NVIDIA-grafik



Om du har installerat från Intel/AMD ISO och ditt system har ett diskret NVIDIA-grafikkort, eller om du har lagt till ett vid ett senare tillfälle, måste du manuellt installera drivrutinerna för ditt kort för att uppnå optimal prestanda. Kör följande kommando i en kommandoterminal för att installera drivrutinen:



```bash
sudo apt install system76-driver-nvidia
```



Du kan också installera NVIDIA-grafikdrivrutiner från Pop!_Shop.



![Capture](assets/fr/20.webp)



## Installation av viktiga verktyg



Pop!OS erbjuder ett brett utbud av programvara via sin Pop!Shop, men många viktiga verktyg kan också installeras via terminalen med `apt` eller `flatpak`. Så här installerar du de viktigaste verktygen för en komplett arbetsmiljö.



### Installation av terminal



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

### Installation via Pop! Shop (grafiskt gränssnitt)





- Öppna **Pop!_Shop** från huvudmenyn.
- Använd sökfältet för att hitta de program du vill ha (t.ex. "Brave").
- Klicka på **Install** för varje applikation.
- Pop!_Shop hanterar automatiskt beroenden och uppdateringar.



## Uppdatering av systemet



### Alternativ 1: Via grafiskt användargränssnitt (GUI)



Pop!OS har en enkel, intuitiv och grafisk uppdateringshanterare.



1. Klicka på **huvudmenyn** (ikonen längst ned till vänster).


2. Öppna **"Pop!_Shop"**.


3. I Pop!_Shop klickar du på fliken **"Uppdateringar"**.


4. Systemet kommer automatiskt att söka efter tillgängliga uppdateringar.


5. Klicka på **"Uppdatera alla"** för att börja installera uppdateringar.


6. Ange ditt lösenord om du blir ombedd att göra det.


7. Låt processen gå klart och starta om den vid behov.



### Alternativ 2: Via terminal



Öppna en terminal och skriv :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Hantering av användare



Vi rekommenderar att du använder ett standardanvändarkonto med sudo-rättigheter för den dagliga driften.



Så här skapar du en ny användare :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Logga ut och logga sedan in igen med den nya användaren.



### Hantering av grafikdrivrutiner





- För Nvidia-kort, kontrollera att de proprietära drivrutinerna är installerade:



```bash
sudo apt install system76-driver-nvidia
```





- För AMD/Intel ingår drivrutiner i allmänhet som standard.



### Aktivera brandvägg (UFW)



Pop!OS blockerar inte nätverkstrafik som standard. Aktivera UFW för att förbättra säkerheten:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Konfigurera automatiska uppdateringar



För att hålla systemet uppdaterat utan manuella ingrepp:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Anpassa utseende och beteende





- Öppna **Systeminställningar** → **Utseende** för att välja ett ljust eller mörkt tema.
- Konfigurera aktiva hörn, animationer och tillägg via COSMIC Manager.
- Justera skrivbordslayouten för att optimera ditt arbetsflöde.



### Konfigurera automatisk säkerhetskopiering



Pop!OS integrerar verktyg som Deja Dup för säkerhetskopiering:





- Starta **Backup** från menyn.
- Välj en extern enhet eller en nätverksplats.
- Schemalägg regelbundna säkerhetskopior.



### Installera användbara GNOME/COSMIC-tillägg



Här är några rekommenderade tillägg för att förbättra användarupplevelsen:





- Dash to Dock**: applikationsfältet alltid synligt.
- GSConnect**: synkronisering med Android.
- Clipboard Indicator**: avancerad hantering av urklipp.



Installera dem via :



```bash
sudo apt install gnome-shell-extensions
```



Aktivera dem sedan i inställningarna.



### Optimering av minnes- och swap-hantering



Kontrollera din swapstatus:



```bash
swapon --show
```



Öka vid behov swap-storleken eller konfigurera en swap-fil :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Lägg till den i filen `/etc/fstab` för automatisk montering.



## Paket- och arkivhantering



### Förstå paketkällor



Pop!OS, baserat på Ubuntu, använder huvudsakligen :





- Officiella Ubuntu**-arkiv: för den mest stabila programvaran.
- System76** repositories: för drivrutiner, firmware och specifika verktyg.
- Flatpak**: tillgång till ett brett utbud av sandboxade applikationer.
- Snap** (tillval): ett annat universellt paketformat.



---

### Lägga till och hantera PPA-repositories



För att installera programvara som uppdateras ofta kan vissa PPA:er (Personal Package Archives) läggas till:



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Slutsats



Pop!OS är en modern och stabil Linux-distribution som passar både nybörjare och avancerade användare.



Tack vare det intuitiva COSMIC-gränssnittet och de integrerade verktygen ger den en smidig och produktiv upplevelse, oavsett om det gäller utveckling, skapande eller daglig användning.



Denna handledning täcker de viktigaste stegen: förberedelser, nedladdning, installation, inledande inställningar och viktiga verktyg.



Utforska gärna Pop!OS ytterligare och anpassa din miljö så att du får ut mesta möjliga av den.