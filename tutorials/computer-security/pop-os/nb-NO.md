---
name: Pop!_OS
description: Guide til installasjon av Pop!_OS, en Linux-distribusjon
---

![cover](assets/cover.webp)



## Innledning



Pop!OS er et Linux-basert operativsystem utviklet av **System76**, en amerikansk produsent som spesialiserer seg på maskiner for utviklere, designere og avanserte brukere.



Pop!OS er utviklet for å tilby et moderne, stabilt miljø med høy ytelse, og kjennetegnes av en enkel brukeropplevelse, kraftige verktøy og et sterkt fokus på produktivitet.



### Hvem er System76?



System76 er et amerikansk selskap grunnlagt i 2005 og basert i Denver, som spesialiserer seg på produksjon av bærbare, stasjonære og stasjonære datamaskiner og servere som er utviklet spesielt for Linux.



I motsetning til tradisjonelle produsenter utvikler System76 maskiner som er designet for å være åpne, reparerbare og orientert mot programvarefrihet.



System76 lager ikke bare datamaskiner.



Selskapet utvikler også :




- Pop!OS**, et eget Linux-basert operativsystem;
- COSMIC**, det moderne skrivebordsmiljøet med høy ytelse som brukes av Pop!OS ;
- Open Firmware**, en fastvare med åpen kildekode basert på Coreboot ;
- verktøy for utviklere og designere.



Målet er å tilby maskinvare- og programvareintegrasjon av høy kvalitet, som kan sammenlignes med Apples økosystem, men helt åpent og sentrert rundt Linux.



## Et moderne, stabilt og tilgjengelig system



Pop!OS bygger på fundamentet til Ubuntu, noe som gir det utmerket stabilitet, bred maskinvarekompatibilitet og tilgang til et stort programvareøkosystem.


Det elegante grensesnittet, COSMIC-skrivebordet, er utformet for å være flytende, intuitivt og tilpasningsdyktig, selv for nye brukere.



## Et ideelt valg for utviklere, designere og krevende brukere



Pop!OS er spesielt verdsatt av :





- utviklere (forhåndsinstallerte verktøy, avansert flislegging),
- brukere med Nvidia- eller AMD-grafikkort,
- studenter og fagfolk på jakt etter et pålitelig system,
- windows-brukere som ønsker å gjøre en enkel overgang.



Den inkluderer automatisk flislegging, et oversiktlig programvaresenter og integrerte produktivitetsverktøy som gjør den daglige bruken enklere.



## Høydepunkter fra Pop!OS





- Optimalisert ytelse** takket være regelmessige oppdateringer.
- To ISO-versjoner er tilgjengelige**: standard og Nvidia-optimalisert.
- Forbedret sikkerhet** (LUKS-kryptering tilgjengelig ved installasjon).
- Interface COSMIC** ergonomisk og moderne.
- Meget kompatibel** med Ubuntu og Flatpak-programvare.



## Last ned POP!OS på en sikker måte



### 1. Forutsetninger



Før du laster ned og installerer POP!OS, er det noen ting du må gjøre for å forberede installasjonsmiljøet på riktig måte.



### Nødvendig utstyr





- En kompatibel datamaskin**: Intel- eller AMD-prosessor, Intel / AMD / Nvidia GPU.
- Minst 4 GB RAM** (8 GB anbefales for komfortabel bruk).
- minimum 20 GB ledig plass** (40 GB eller mer anbefales).
- En USB-nøkkel på minst 4 GB** for å opprette installasjonsmediet.



### Internett-tilkobling



En stabil forbindelse er nyttig for :





- last ned ISO-bildet,
- installere oppdateringer etter installasjon.



Pop!OS kan kjøres uten tilkobling, men installasjonen går mye smidigere over Internett.



### Sikkerhetskopiering av data



Hvis Pop!OS skal erstatte eller sameksistere med et annet system (Windows, Ubuntu osv.), anbefales det å ta sikkerhetskopi av viktige filer før du går videre.



### Kontroller om det finnes en Nvidia GPU (hvis aktuelt)



For datamaskiner som er utstyrt med et Nvidia-grafikkort, må du laste ned det spesielle ISO-bildet som inneholder Nvidia-driverne.


Denne kontrollen er veldig enkel:





- ved å lese spesifikasjonene for PC-en,
- eller ved å slå opp grafikkortmodellen i systeminnstillingene.



### Last ned fra det offisielle nettstedet



ISO-bildet av Pop!OS kan lastes ned direkte fra den offisielle System76-siden: [system76.com/pop] (https://system76.com/pop/).



Denne siden tilbyr alltid den nyeste versjonen, tilpasset din maskinvare.



![capture](assets/fr/03.webp)



### Velg versjon: Standard eller Nvidia, eller Raspberry Pi (ARM64)



Pop!OS er tilgjengelig i tre varianter:



### Standardversjon



Anbefales for datamaskiner som bruker :





- intel- eller AMD-prosessor;
- en integrert Intel- eller AMD-GPU;
- et AMD Radeon-grafikkort.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia-versjon



Anbefales for datamaskiner utstyrt med Nvidia-grafikkort.


Dette bildet inneholder allerede Nvidia-drivere, noe som gjør installasjonen enklere og reduserer grafikkproblemer.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi-versjon (ARM64)



For Raspberry Pi 4 og 400 (ARM-prosessor).


Denne versjonen er tilpasset ARM-arkitekturen, og er en spesifikk versjon for disse minidatamaskinene.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Opprett en oppstartbar USB-nøkkel



Du kan bruke flere verktøy, for eksempel Balena Etcher :





- Last ned og installer [Balena Etcher] (https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Åpne Balena Etcher, og velg deretter Pop!OS ISO-bildet.
- Velg USB-nøkkel som målmedium.
- Klikk på Flash og vent til prosessen er ferdig.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Installere og sikre Pop!OS



### Oppstart fra USB-nøkkel





- Slå av datamaskinen.
- Koble til USB-nøkkelen (som inneholder Pop!OS).
- Slå på datamaskinen. På nyere PC-er skal systemet automatisk gjenkjenne USB-oppstartsnøkkelen. Hvis dette ikke er tilfelle, kan du starte på nytt ved å holde BIOS/UEFI-tilgangstasten nede (vanligvis F2, F12 eller Delete, avhengig av merke).
  - I BIOS/UEFI-menyen velger du USB-nøkkelen som oppstartsenhet.
  - Lagre og start på nytt.



### Starter installasjonen



Når du har valgt den oppstartbare USB-nøkkelen som oppstartsenhet, starter datamaskinen opp i et Pop!OS Live-miljø.



Velg språk.



![Capture](assets/fr/10.webp)



Velg et sted.



![Capture](assets/fr/11.webp)



Velg et språk for tastaturinndata.



![Capture](assets/fr/12.webp)



Velg et tastaturoppsett.



![Capture](assets/fr/13.webp)



Velg alternativet `Clean Install` for en standardinstallasjon. Dette er det beste alternativet for nye Linux-brukere, men vær oppmerksom på at det vil slette alt innholdet på målstasjonen. Alternativt kan du velge `Try Demo Mode` for å fortsette å teste Pop!OS i et live-miljø.



![Capture](assets/fr/14.webp)



Velg `Custom (Advanced)` for å få tilgang til GParted. Med dette verktøyet kan du konfigurere avanserte funksjoner, for eksempel dobbel oppstart, opprette en separat `/home`-partisjon eller plassere `/tmp`-partisjonen på en annen stasjon.



Klikk på "Slett og installer" for å installere Pop!OS på den valgte stasjonen.



![Capture](assets/fr/15.webp)



### Konfigurasjon av brukerkonto



I neste del av installasjonsprogrammet får du veiledning i hvordan du oppretter en brukerkonto slik at du kan logge på det nye operativsystemet.



Oppgi et fullt navn (dette kan inneholde hvilken som helst tekst du ønsker, store eller små bokstaver), samt et brukernavn (som må skrives med små bokstaver) :



![Capture](assets/fr/16.webp)



Når kontoen er opprettet, blir du bedt om å angi et nytt passord.



![Capture](assets/fr/17.webp)



### Fullstendig diskkryptering



Kryptering av systemdisken er ikke nødvendig, men det garanterer sikkerheten til brukerdata i tilfelle noen skulle få uautorisert fysisk tilgang til enheten.



Stasjonen kan krypteres ved hjelp av innloggingspassordet ditt ved å krysse av for `Krypteringspassordet er det samme som brukerkontopassordet`. Du kan også fjerne merket i denne boksen og velge `Set Password` nederst. Velg `Don't Encrypt` for å ignorere diskkrypteringsprosessen.



![Capture](assets/fr/18.webp)



Hvis du har valgt knappen `Set Password`, vil du se en ekstra melding om å angi krypteringspassordet ditt.



Gå videre til neste trinn i installasjonsprogrammet. Pop!OS vil nå begynne installasjonen på disken.



![Capture](assets/fr/19.webp)



Når installasjonen er fullført, starter du datamaskinen på nytt og logger inn for å fullføre konfigurasjonen av brukerkontoen.



Hvis du har endret oppstartsrekkefølgen slik at Live USB-nøkkelen prioriteres ved oppstart, må du slå datamaskinen helt av og fjerne USB-nøkkelen for installasjon. Hvis du er i dual-boot-modus, trykker du på de riktige tastene for å få tilgang til konfigurasjonen og velge stasjonen som inneholder Pop!OS-installasjonen.



![Capture](assets/fr/20.webp)



### NVIDIA-grafikk



Hvis du har installert fra Intel/AMD ISO og systemet ditt har et diskret NVIDIA-grafikkort, eller hvis du har lagt til et på et senere tidspunkt, må du installere driverne for kortet manuelt for å oppnå optimal ytelse. Kjør følgende kommando i en kommandoterminal for å installere driveren:



```bash
sudo apt install system76-driver-nvidia
```



Du kan også installere NVIDIA-grafikkdrivere fra Pop!_Shop.



![Capture](assets/fr/20.webp)



## Installere viktige verktøy



Pop!OS tilbyr et bredt utvalg av programvare via Pop!Shop, men mange viktige verktøy kan også installeres via terminalen med `apt` eller `flatpak`. Slik installerer du de viktigste verktøyene for å få et komplett arbeidsmiljø.



### Installasjon av terminaler



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

### Installasjon via Pop! Shop (grafisk grensesnitt)





- Åpne **Pop!_Shop** fra hovedmenyen.
- Bruk søkefeltet til å finne de programmene du ønsker (for eksempel "Brave").
- Klikk på **Installer** for hvert program.
- Pop!_Shop håndterer avhengigheter og oppdateringer automatisk.



## Oppdatering av systemet



### Alternativ 1: Via grafisk brukergrensesnitt (GUI)



Pop!OS har en enkel, intuitiv grafisk oppdateringsbehandling.



1. Klikk på **hovedmenyen** (ikonet nederst til venstre).


2. Åpne **"Pop!_Shop"**.


3. I Pop!_Shop klikker du på fanen **"Oppdateringer"**.


4. Systemet vil automatisk se etter tilgjengelige oppdateringer.


5. Klikk på **"Oppdater alle"** for å begynne å installere oppdateringer.


6. Skriv inn passordet ditt hvis du blir bedt om det.


7. La prosessen fullføres, og start deretter på nytt om nødvendig.



### Alternativ 2: Via terminal



Åpne en terminal og skriv inn :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Brukeradministrasjon



Vi anbefaler at du bruker en standard brukerkonto med sudo-rettigheter for den daglige driften.



Slik oppretter du en ny bruker :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Logg ut, og logg deretter inn igjen med denne nye brukeren.



### Håndtering av grafikkdrivere





- For Nvidia-kort må du kontrollere at de proprietære driverne er installert:



```bash
sudo apt install system76-driver-nvidia
```





- For AMD/Intel er drivere vanligvis inkludert som standard.



### Aktiver brannmur (UFW)



Pop!OS blokkerer ikke nettverkstrafikk som standard. Aktiver UFW for å forbedre sikkerheten:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Konfigurere automatiske oppdateringer



For å holde systemet oppdatert uten manuell inngripen:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Tilpass utseende og oppførsel





- Åpne **Systeminnstillinger** → **Utseende** for å velge et lyst eller mørkt tema.
- Konfigurer aktive hjørner, animasjoner og utvidelser via COSMIC Manager.
- Juster skrivebordslayouten for å optimalisere arbeidsflyten.



### Konfigurere automatisk sikkerhetskopiering



Pop!OS integrerer verktøy som Deja Dup for sikkerhetskopiering:





- Start **Backup** fra menyen.
- Velg en ekstern stasjon eller en nettverksplassering.
- Planlegg regelmessige sikkerhetskopier.



### Installere nyttige GNOME/COSMIC-utvidelser



Her er noen anbefalte utvidelser for å forbedre brukeropplevelsen:





- Strek til Dock**: applikasjonslinjen er alltid synlig.
- GSConnect**: synkronisering med Android.
- Utklippstavleindikator**: avansert utklippstavlehåndtering.



Installer dem via :



```bash
sudo apt install gnome-shell-extensions
```



Aktiver dem deretter i innstillingene.



### Optimalisering av minne- og swap-styring



Sjekk byttestatusen din:



```bash
swapon --show
```



Om nødvendig kan du øke swap-størrelsen eller konfigurere en swap-fil :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Legg den til i filen `/etc/fstab` for automatisk montering.



## Håndtering av pakker og repositorier



### Forståelse av pakkekilder



Pop!OS, som er basert på Ubuntu, bruker hovedsakelig :





- Offisielle Ubuntu**-arkiver: for den mest stabile programvaren.
- System76**-lagre: for drivere, fastvare og spesifikke verktøy.
- Flatpak**: tilgang til et bredt spekter av sandkasseapplikasjoner.
- Snap** (valgfritt): et annet universelt pakkeformat.



---

### Legg til og administrer PPA-repositorier



For å installere programvare som oppdateres ofte, kan du legge til visse PPA-er (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Konklusjon



Pop!OS er en moderne, stabil Linux-distribusjon som passer for både nybegynnere og avanserte brukere.



Takket være det intuitive COSMIC-grensesnittet og de integrerte verktøyene gir det en flytende og produktiv opplevelse, enten det gjelder utvikling, nyskaping eller daglig bruk.



Denne veiledningen tar for seg de viktigste trinnene: forberedelse, nedlasting, installasjon, innledende innstillinger og viktige verktøy.



Utforsk gjerne Pop!OS videre og tilpass miljøet ditt for å få mest mulig ut av det.