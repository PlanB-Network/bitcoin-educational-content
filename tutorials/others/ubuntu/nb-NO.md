---
name: Ubuntu
description: Komplett guide til installasjon og bruk av Ubuntu som et alternativ til Windows
---
![cover](assets/cover.webp)

## Innledning

Et operativsystem (OS) er den viktigste programvaren som administrerer alle datamaskinens ressurser. Å velge et alternativt operativsystem som Ubuntu kan gi mange fordeler når det gjelder sikkerhet, kostnader og personvern.

### Hvorfor Ubuntu?


- Forbedret sikkerhet** : Linux-distribusjoner er kjent for sin sikkerhet og robusthet
- Ingen kostnader**: Ubuntu og de fleste Linux-distribusjoner er gratis
- Stort fellesskap**: Et fellesskap av brukere som står klare til å hjelpe deg via forum og opplæringsprogrammer
- Respekt for personvernet**: Åpen kildekode for større åpenhet
- Enkelhet**: Brukervennlig grensesnitt og enkel bruk
- Rikt økosystem** : Omfattende katalog med programvare med åpen kildekode
- Regelmessig støtte**: Sikre oppdateringer fra Canonical

## Installasjon og konfigurasjon

### 1. Forutsetninger

**Nødvendig utstyr:**


- En USB-nøkkel på minst 12 GB
- En datamaskin med minst 25 GB tilgjengelig

### 2. Last ned


- Gå til [ubuntu.com/download] (https://ubuntu.com/download)
- Velg den stabile versjonen (LTS anbefales)
- Last ned ISO-bilde

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Opprett en oppstartbar USB-nøkkel

Du kan bruke flere verktøy, for eksempel Balena Etcher :


- Last ned og installer [Balena Etcher] (https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Åpne Balena Etcher, og velg deretter Ubuntu ISO-bildet
- Velg USB-nøkkel som målmedium
- Klikk på Flash og vent til prosessen er ferdig

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Installere og sikre Ubuntu

**4.1 Oppstart fra USB-minnepinne** (på fransk)


- Slå av datamaskinen
- Koble til USB-nøkkelen (som inneholder Ubuntu)
- Slå på datamaskinen. På nyere PC-er skal systemet automatisk gjenkjenne USB-oppstartsnøkkelen. Hvis dette ikke er tilfelle, starter du på nytt ved å holde BIOS/UEFI-tilgangstasten nede (vanligvis F2, F12 eller Delete, avhengig av merke)
 - I BIOS/UEFI-menyen velger du USB-nøkkelen som oppstartsenhet
 - Lagre og start på nytt

**4.2 Starte installasjonen** (på fransk)

**Startskjermbilde**

Når du starter opp fra USB-nøkkelen, ser du dette skjermbildet, som lar deg starte Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Valg av språk

Velg ønsket språk for installasjonen og systemet.

![Sélection de la langue](assets/fr/07.webp)

**Tilgjengelighetsalternativer

Konfigurer tilgjengelighetsalternativer om nødvendig (skjermleser, høy kontrast osv.).

![Options d'accessibilité](assets/fr/08.webp)

**Tastaturkonfigurasjon

Velg tastaturoppsettet ditt. Et testfelt er tilgjengelig for å kontrollere at tastene samsvarer med konfigurasjonen din.

![Configuration du clavier](assets/fr/09.webp)

**Nettverkstilkobling**

Koble til Wi-Fi- eller kabelbasert nettverk for å laste ned oppdateringer under installasjonen.

![Configuration réseau](assets/fr/10.webp)

**Type installasjon

Velg mellom "Prøv Ubuntu" (for å teste uten å installere) eller "Installer Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Installasjonsmetode

Velg interaktiv installasjon.

![Mode d'installation](assets/fr/12.webp)

**Valg av applikasjon

Velg mellom standardinstallasjonen eller et utvidet utvalg av programmer.

![Sélection des applications](assets/fr/13.webp)

**Tredjepartsapplikasjoner

Avgjør om du vil installere ekstra drivere og proprietær programvare eller ikke.

![Installation applications tierces](assets/fr/14.webp)

**Type partisjonering

Du har to hovedalternativer:


- "Slett disk og installer Ubuntu": bruker hele disken til Ubuntu
- "Manuell installasjon: Opprett en dual boot med Windows eller tilpass partisjonene dine

![Choix du partitionnement](assets/fr/15.webp)

**Opprettelse av brukerkonto

Angi brukernavn og passord for Ubuntu-kontoen din.

![Création du compte](assets/fr/16.webp)

**Tidssone

Velg ditt geografiske område for å stille inn systemtiden.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Installasjonssammendrag**

Kontroller alle valgene dine før du starter den endelige installasjonen. Når du klikker på "Installer", begynner prosessen.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Oppgradering av Ubuntu etter installasjon** (på fransk)

Oppdatering av systemet er et viktig skritt etter en ny installasjon. Du har to alternativer:

**Alternativ 1: Via det grafiske brukergrensesnittet**


- Søk etter "Programvare og oppdateringer" i applikasjonsmenyen
- Programmet vil automatisk se etter tilgjengelige oppdateringer
- Følg instruksjonene på skjermen for å installere oppdateringene

**Alternativ 2: Via terminal


- Åpne terminal (Ctrl + Alt + T)
- Skriv inn følgende kommando for å se etter tilgjengelige oppdateringer:

```bash
sudo apt update
```


- Skriv inn passordet ditt når du blir bedt om det
- For å installere oppdateringer, skriv inn :

```bash
sudo apt upgrade
```


- Bekreft installasjonen ved å skrive "Y" og deretter Enter

### 5. Oppdage grunnleggende oppgaver

**5.1 Surfe på Internett

Som standard finner du ofte Firefox i oppstartslinjen.

Start Firefox og begynn å surfe.

Andre nettlesere (Chrome, Brave osv.) kan installeres via Software Manager eller via .deb-pakker.

**5.2 Tekstbehandling

Ubuntu leveres med LibreOffice-pakken (Writer for tekstbehandling).

Slik åpner du den: Aktiviteter > Søk etter "LibreOffice Writer", eller klikk på ikonet hvis det vises i linjen.

Du kan opprette, redigere og lagre dokumenter i en rekke ulike formater (inkludert .docx).

**5.3 Installere applikasjoner

Programvarebehandling (kalt "Ubuntu Software"): grafisk grensesnitt for å søke etter og installere programmer.

Fra Terminal bruker du kommandoen :

```bash
sudo apt install nom-du-paquet
```

Eksempel:

```bash
sudo apt install vlc
```

### 6. Konklusjon og tilleggsressurser

Nå er du klar til å bruke Ubuntu til daglig: sikre systemet ditt, surfe, gjøre kontorarbeid, installere programvare og holde operativsystemet oppdatert!

For å ta sikkerheten i ditt digitale liv et skritt videre, anbefaler vi at du tar en titt på vår krypterte meldingstjeneste, som er perfekt egnet til å beskytte personvernet ditt og utfyller din Ubuntu-installasjon:

https://planb.network/tutorials/others/proton-mail