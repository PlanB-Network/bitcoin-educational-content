---
name: Zorin OS
description: Komplett guide til installasjon og bruk av Zorin OS som et moderne alternativ til Windows
---

![cover](assets/cover.webp)



## Innledning



Et operativsystem (OS) er den grunnleggende programvaren som gjør at en datamaskin kan fungere: Det håndterer maskinvare, programvare, sikkerhet og brukergrensesnitt.


Zorin OS er en Linux-distribusjon som er utviklet spesielt for å lette overgangen fra Windows, samtidig som den tilbyr fordelene med programvare med åpen kildekode: sikkerhet, stabilitet, personvern og ytelse.



Zorin OS er basert på Ubuntu LTS og kombinerer høy programvarekompatibilitet med et velkjent, tilpassbart grensesnitt, noe som gjør det til et troverdig og tilgjengelig alternativ til Windows.



## Hvorfor Zorin OS?





- Interface kjent**: Windows-lignende utseende (startmeny, oppgavelinje)
- Enkel overgang**: utviklet for brukere som kommer fra Windows
- Forbedret sikkerhet**: Linux-arkitektur, mindre utsatt for virus
- Respekt for personvernet**: ingen inngripende datainnsamling
- Optimalisert ytelse**: fungerer godt på beskjedne maskiner
- Ubuntu LTS**-base: stabilitet, regelmessige oppdateringer og bred kompatibilitet
- Avansert personalisering**: via Zorin Appearance-verktøyet.



## Installasjon og konfigurasjon



### 1. Forutsetninger



**Nødvendig utstyr:**





- En USB-nøkkel på minst **8 GB** (12 GB anbefales);
- En datamaskin med minst **25 GB ledig diskplass**
- Internett-tilkobling (anbefalt).



### 2. Last ned Zorin OS





- Besøk den offisielle nettsiden: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Velg **Zorin OS Core** (anbefalt gratisversjon)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Last ned ISO-bilde



Zorin OS tilbyr også :





- Zorin OS Lite** (eldre datamaskiner)
- Zorin OS Pro** (avgiftsbasert, med avanserte funksjoner og support)



## Opprette en oppstartbar USB-nøkkel



Du kan bruke flere verktøy, for eksempel Balena Etcher :





- Last ned og installer [Balena Etcher] (https://etcher.balena.io/).
- Åpne Balena Etcher, og velg deretter Zorin ISO-bildet.
- Velg USB-nøkkel som målmedium.
- Klikk på Flash og vent til prosessen er ferdig.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Nøkkeloppstart og BIOS-tilgang



Slå av datamaskinen du ønsker å installere Zorin OS på, og koble deretter til USB-nøkkelen.


Når datamaskinen starter, går du inn i BIOS (`ESC`, `F9` eller `F11` avhengig av merke) og velger USB-nøkkelen som oppstartsenhet, og trykker deretter på `Enter` for å starte oppstartsprosessen.





- Ved oppstart velger du **Try or Install Zorin OS**.



![capture](assets/fr/08.webp)





- Hvis du har et NVIDIA-grafikkort, velger du **Try or Install Zorin OS (modern NVIDIA drivers)**.
- Vennligst vent mens filene sjekkes.



![capture](assets/fr/09.webp)





- I installasjonsprogrammet for Zorin OS velger du språket **Fransk** og klikker deretter på Installer **Zorin OS**.



![capture](assets/fr/10.webp)





- Velg tastaturoppsett.



![capture](assets/fr/11.webp)





- Merk av i boksene **Last ned oppdateringer under installasjonen av Zorin OS** og **Installer tredjepartsprogramvare for grafikk- og Wi-Fi-maskinvare og ekstra medieformater**.



![capture](assets/fr/12.webp)





- Hvis du vil installere Zorin OS på hele disken, velger du **Slett disk og installer Zorin OS**.



![capture](assets/fr/14.webp)



Slik installerer du Zorin OS sammen med Windows (dual-boot) :





- Velg **Installer Zorin OS ved siden av Windows Boot Manager**.



![capture](assets/fr/15.webp)





- Hvis du ikke har partisjonert disken, velger du diskplassen du ønsker å tildele Zorin OS, og klikker deretter på **Installer nå**.



![capture](assets/fr/16.webp)





- Bekreft endringene på platen to ganger.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Velg det geografiske området **Paris**.



![capture](assets/fr/18.webp)





- Opprett brukerkontoen din, og gi datamaskinen et navn.



![capture](assets/fr/19.webp)





- Vennligst vent mens Zorin OS installeres.



![capture](assets/fr/20.webp)





- Når installasjonen er fullført, klikker du på **Start på nytt nå**.



![capture](assets/fr/21.webp)





- Fjern USB-installasjonsnøkkelen, og trykk på Enter.



![capture](assets/fr/22.webp)



## Oppdage og bruke Zorin OS



### Første oppstart



Når du starter datamaskinen, kommer du til GRUB - Linux' oppstartsbehandlingsprogram. Som standard er **Zorin OS** valgt; etter 30 sekunder starter det automatisk.



![capture](assets/fr/23.webp)



Hvis du har installert Zorin OS som en dual-boot med Windows, kan du starte opp til Windows ved å velge **Windows Boot Manager**.



Logg inn med brukerkontoen din :



![capture](assets/fr/24.webp)



Ved første oppstart startes programmet **Velkommen til Zorin OS** for å hjelpe deg med å oppdage det nye operativsystemet.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Oppdater systemet



Oppdateringsbehandleren åpnes snart for å informere deg om at oppdateringer er tilgjengelige. Installer dem ved å klikke på knappen **Installer nå**.



![capture](assets/fr/33.webp)



Du kan se etter oppdateringer manuelt i **Software** > Oppdateringer:



![capture](assets/fr/34.webp)



### Personalisering



Det første du må gjøre i Zorin OS, er å velge det **skrivebordslayoutet** du er mest komfortabel med. Du finner layouter som ligner på dem du finner i Windows (og enda mer i Pro-versjonen).



Dette gjør du ved å åpne **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Åpne deretter **Innstillinger** for å tilpasse systemet:


**Lyd - Innstillinger - Zorin OS



![capture](assets/fr/36.webp)



**Online-kontoer - Innstillinger - Zorin OS



![capture](assets/fr/37.webp)



### Bruksområder



Det finnes flere måter å installere programmer på:





- Software**, Zorin OS' applikasjonsbutikk. Applikasjonene kommer fra flere kilder: apt, Flatpak og Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (kommandolinje) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



For mer informasjon om hvordan du installerer applikasjoner i Zorin OS, se denne siden: [Installere apper (zorin.com)] (https://zorin.com/help/install-apps/).



### Windows-applikasjoner



For å installere Windows-applikasjoner starter du med å installere pakken **zorin-windows-app-support** via Terminal :



```bash
sudo apt install zorin-windows-app-support
```



For en liste over kompatible Windows-programmer og deres kompatibilitetsnivåer, se siden [Wine Application Database] (https://appdb.winehq.org/). Der finner du følgende merker, som tilsvarer kompatibilitetsnivået (fra best til dårligst): Platina, Gull, Sølv, Bronse og Søppel.



Du har to alternativer for å installere et Windows .exe- eller .msi-program:





- Åpne **PlayOnLinux** og klikk på **Install**-knappen for å bla gjennom kompatible programmer og spill.



![capture](assets/fr/41.webp)





- Dobbeltklikk på programmets **.exe- eller .msi**-fil, og la installasjonsprogrammet veilede deg.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Konklusjon og tilleggsressurser



Zorin OS er et solid og rimelig alternativ til Windows, som kombinerer enkelhet, sikkerhet og personvern.



Det muliggjør en smidig overgang til Linux, uten at det går på bekostning av komfort eller produktivitet.



For å beskytte det digitale livet ditt ytterligere anbefaler vi at du bruker personvernvennlige tjenester, spesielt for kryptert kommunikasjon:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2