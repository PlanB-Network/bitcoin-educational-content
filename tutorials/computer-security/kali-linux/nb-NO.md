---
name: Kali
description: Installere Kali Linux på VirtualBox, som en oppstartbar USB-pinne eller som en dual boot, trinn for trinn.
---

![cover-kali](assets/cover.webp)



## Innledning



### Hvorfor Kali Linux?



**Kali Linux** er en Linux-distribusjon som er spesialisert på IT-sikkerhet.


Dette er grunnen til at vi bruker Kali Linux:





- Den er forhåndskonfigurert med et bredt spekter av pentesting-verktøy (system- og nettverkssikkerhetstester).
- Det er **åpen kildekode og gratis**, så du kan bruke og modifisere det fritt.
- Den er **pålitelig og sikker**, og ideell for å lære om cybersikkerhet.
- Det gir deg muligheten til å lære å bruke Linux i et testklart miljø.
- Den kan installeres på forskjellige måter: **VirtualBox**, **oppstartbar USB-nøkkel** eller **dual oppstart**.



## Installasjon og konfigurasjon



### 1. Forutsetninger



**Nødvendig utstyr:**





- 64-biters prosessor** (Intel eller AMD).
- minimum 8 GB RAM** (4 GB kan være tilstrekkelig for en lett installasjon eller VM).
- 50 GB ledig diskplass** for å installere Kali Linux.
- Internett-tilkobling** for å laste ned ISO-bilde og oppdateringer.
- En USB-nøkkel på minst 8 GB** for å lage oppstartbare medier (hvis du vil installere Kali på en PC eller teste det på Live USB).



Det er viktig å ta sikkerhetskopi av dataene dine før du installerer på en eksisterende PC.



### 2. Last ned





- Gå til [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Velg ISO-bildet for applikasjonen din:
  - Install Image** : for PC-installasjon.
  - Virtual Image**: for å installere Kali på VirtualBox eller VMware.
- Last ned ISO-bildet.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Opprett en oppstartbar USB-nøkkel



Du kan bruke flere verktøy, for eksempel Balena Etcher :





- Last ned og installer [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Åpne Balena Etcher, og velg deretter Kali ISO-bildet.
- Velg USB-nøkkel som målmedium.
- Klikk på Flash og vent til prosessen er ferdig.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Installasjon og sikring av Kali Linux



#### 4.1 Oppstart på USB-nøkkelen





- Slå av datamaskinen.
- Plugg inn USB-nøkkelen (som inneholder Kali Linux).
- Slå på datamaskinen. På nyere PC-er skal systemet automatisk gjenkjenne USB-oppstartsnøkkelen. Hvis dette ikke er tilfelle, kan du starte på nytt ved å holde BIOS/UEFI-tilgangstasten nede (vanligvis F2, F12 eller Delete, avhengig av merke).
  - I BIOS/UEFI-menyen velger du USB-nøkkelen som oppstartsenhet.
  - Lagre og start på nytt.



#### 4.2 Start av installasjonen



##### Oppstartsskjerm



Når du starter opp fra USB-minnepinnen, skal oppstartsskjermen for Kali Linux vises. Velg mellom **grafisk installasjon** og **tekstinstallasjon**. I dette eksemplet har vi valgt grafisk installasjon.



![capture](assets/fr/06.webp)



Hvis du bruker **Live**-bildet, vil du se en annen modus, **Live**, som også er standard oppstartsalternativ.



![Mode Live](assets/fr/07.webp)



##### Valg av språk



Velg ønsket språk for installasjonen og systemet.



![Sélection de la langue](assets/fr/08.webp)



Vennligst spesifiser din geografiske plassering.



![Options d'accessibilité](assets/fr/09.webp)



##### Tastaturkonfigurasjon



Velg tastaturoppsettet ditt. Et testfelt er tilgjengelig for å kontrollere at tastene samsvarer med konfigurasjonen din.



![Configuration du clavier](assets/fr/10.webp)



##### Nettverkstilkobling



Installasjonen vil nå skanne nettverksgrensesnittene dine, søke etter en DHCP-tjeneste og deretter be deg om å oppgi et vertsnavn for systemet ditt. I eksempelet nedenfor har vi angitt **"kali"** som vertsnavn.



![Configuration réseau](assets/fr/11.webp)



Du kan eventuelt angi et standard domenenavn som dette systemet skal bruke (verdier kan hentes fra DHCP eller hvis det finnes et eksisterende operativsystem).



![Choix du type d'installation](assets/fr/12.webp)



##### Brukerkontoer



Deretter oppretter du en brukerkonto for systemet (fullt navn, brukernavn og et sterkt passord).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Tidssone



Velg ditt geografiske område for å stille inn systemtiden.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Partisjoneringstype



Installasjonsprogrammet skanner deretter diskene dine og viser flere alternativer avhengig av konfigurasjonen din.



I denne veiledningen tar vi utgangspunkt i en **blank disk**, noe som gir **fire mulige valg**.


Vi velger **Guided - use entire disk**, siden vi her skal utføre en engangsinstallasjon av Kali Linux (single boot). Dette betyr at ingen andre operativsystemer beholdes, og at hele disken kan slettes.



Hvis disken allerede inneholder data, kan det hende at det vises et ekstra alternativ **Guided - use largest contiguous free space**.



Dette alternativet lar deg installere Kali Linux uten å slette eksisterende data, noe som gjør det ideelt for dobbeltstart med et annet system.



I vårt tilfelle er disken tom, så dette alternativet vises ikke.



![Choix du partitionnement](assets/fr/17.webp)



Velg disken som skal partisjoneres.



![capture](assets/fr/18.webp)



Avhengig av behovene dine kan du velge å oppbevare alle filene dine i én enkelt partisjon (standardinnstilling) eller ha separate partisjoner for én eller flere toppnivåkataloger.



Hvis du ikke er sikker på hva du vil ha, velger du alternativet **Alle filer i én enkelt partisjon**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Du får da en siste mulighet til å kontrollere diskkonfigurasjonen før installasjonsprogrammet gjør irreversible endringer. Når du har klikket på _Continue_, starter installasjonsprogrammet, og installasjonen er nesten fullført.



![capture](assets/fr/21.webp)



##### Kryptert LVM



Hvis dette alternativet ble aktivert i forrige trinn, vil Kali Linux nå utføre en sikker sletting av harddisken før du blir bedt om et LVM-passord.



Bruk et sterkt passord, ellers vises en advarsel om et svakt passphrase-passord.



##### Fullmaktsinformasjon



Kali Linux bruker repositorier til å distribuere applikasjoner. Du må oppgi nødvendig proxy-informasjon hvis miljøet ditt bruker en slik.



Hvis du **ikke er sikker** på om du skal bruke en proxy, kan du **ikke fylle inn noe**. Hvis du oppgir feil informasjon, vil du ikke kunne koble deg til repositoriene.



![capture](assets/fr/22.webp)



##### Metapets



Hvis nettverkstilgang ikke er konfigurert, må du **videre konfigurere** når du blir bedt om det.



Hvis du bruker **Live**-bildet, vises ikke neste trinn.



Deretter kan du velge de [metapakkene](https://www.kali.org/docs/general-use/metapackages/) du ønsker å installere. Standardalternativene vil installere et standard Kali Linux-system, så du trenger ikke å endre noe.



![capture](assets/fr/23.webp)



#### Informasjon om oppstart



Bekreft deretter installasjonen av GRUB-oppstartsinnlasteren.



![capture](assets/fr/24.webp)



##### Start på nytt



Til slutt klikker du på Fortsett for å starte den nye Kali Linux-installasjonen på nytt.



![capture](assets/fr/25.webp)



#### 4.3 Oppdatering og konfigurering av Kali Linux etter installasjon



Oppdatering av systemet er et viktig skritt etter en ny installasjon. Du har to alternativer:



##### Alternativ 1: Via grafisk brukergrensesnitt (GUI)



Kali har, i likhet med Debian/Ubuntu, en integrert grafisk oppdateringshåndtering.



1. Klikk på **hovedmenyen** (øverst til venstre eller nederst, avhengig av skrivebordet ditt).


2. Åpne **"Software Updater"**.


3. Verktøyet vil :




    - Sjekk pakkene som skal oppdateres.
    - Du får opp en liste (med størrelser og versjoner).
    - Gjør at du kan starte oppdateringen med ett enkelt klikk.


4. Skriv inn administratorpassordet ditt (`sudo`) når du blir bedt om det.


5. La den installere og starte på nytt om nødvendig.



##### Alternativ 2: Via terminal



Åpne en terminal og kjør :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Det anbefales ikke å bruke **root**-kontoen til daglig arbeid; opprett i stedet en ikke-root-bruker.



Skriv inn disse kommandoene i terminalen:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Logg ut og logg inn igjen med den nye brukeren.



La oss oppsummere noen grunnleggende Kali Linux-oppgaver i en tabell.



### Grunnleggende oppgaver under Kali Linux




| **Kategori** | **Basisoppgave** | **Beskrivelse / Mål** | **Hovedmetode** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Systemnavigasjon** | Åpne terminalen | Få tilgang til Kalis hovedkommandolinje | Klikk på terminalikonet eller bruk `Ctrl + Alt + T` |
| | Bla gjennom mapper | Bevege seg i systemets mappestruktur | `cd /sti/til/mappe`, `ls` for å liste filer |
| | Opprette / slette en mappe | Organisere filer | `mkdir mappenavn`, `rm -r mappenavn` |
| **Filbehandling** | Kopiere / flytte en fil | Manipulere filer i terminalen | `cp fil destinasjon`, `mv fil destinasjon` |
| | Slette en fil | Frigjøre diskplass | `rm filnavn` |
| | Vise innholdet i en tekstfil | Lese en fil raskt | `cat fil.txt`, `less fil.txt` |
| **Systembehandling** | Oppdatere Kali Linux | Installere de nyeste versjonene og sikkerhetsoppdateringene | `sudo apt update && sudo apt full-upgrade -y` |
| | Installere programvare | Legge til et nytt verktøy eller verktøyprogram | `sudo apt install pakkenavn` |
| | Slette programvare | Rense systemet | `sudo apt remove pakkenavn` |
| | Rense unødvendige avhengigheter | Spar diskplass | `sudo apt autoremove` |
| **Nettverk og internett** | Sjekke nettverkstilkobling | Teste internettilgang | `ping google.com` |
| | Identifisere IP-adresse | Kjenne din nettverkskonfigurasjon | `ip a` eller `ifconfig` |
| | Bytte Wi-Fi-nettverk | Koble til et annet tilgangspunkt | Nettverksikon → Velg ønsket Wi-Fi |
| **Kontoer og tillatelser** | Utføre en administratorkommando | Få midlertidige root-rettigheter | `sudo kommando` |
| | Opprette en ny bruker | Legge til en lokal konto | `sudo adduser brukernavn` |
| | Endre et passord | Sikre en konto | `passwd` |
| **Utseende og komfort** | Bytte bakgrunnsbilde | Personliggjøre skrivebordet | Høyreklikk på skrivebordet → **Skrivebordsinnstillinger** |
| | Endre tema / ikoner | Forbedre lesbarhet og estetikk | Innstillinger → Utseende / Temaer |
| **Kali-verktøy** | Åpne verktøy-menyen | Utforske test- og sikkerhetsverktøy | Meny **Programmer → Kali Linux** |
| | Starte et verktøy (f.eks: nmap, wireshark) | Praktisk oppdagelse av sikkerhetsverktøy | `sudo nmap`, `wireshark`, osv. |
| **Hjelp og dokumentasjon** | Få hjelp til en kommando | Forstå en kommando før bruk | `man kommando` eller `kommando --help` |

## Konklusjon



Installasjonen av Kali Linux er bare første skritt på veien mot å oppdage dette kraftige miljøet som er dedikert til cybersikkerhet. Ved å mestre grunnleggende oppgaver og systemadministrasjon kan alle begynne å utforske de innebygde verktøyene og forstå hvordan et Linux-system fungerer. Kali er en utmerket læringsplattform, både for å styrke tekniske ferdigheter og for å utvikle en genuin kultur for IT-sikkerhet.