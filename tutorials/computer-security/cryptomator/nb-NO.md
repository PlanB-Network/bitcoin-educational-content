---
name: Cryptomator
description: Krypter filene dine i skyen
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten.*



___



## I. Presentasjon



I denne veiledningen bruker vi Cryptomator-programmet til å kryptere data som er lagret i skyen, enten det er på Microsoft OneDrive, Google Drive, Dropbox, Box eller til og med iCloud.



Kryptering av dataene du lagrer på nettbaserte lagringsløsninger som Drive, er den beste måten å beskytte filene dine og personvernet ditt på. Takket være kryptering er du den eneste som kan dekryptere og lese dataene dine, selv om de er lagret på en server i USA eller et annet land rundt om i verden.



I denne demonstrasjonen brukes en Windows 11 22H2-maskin med OneDrive, men fremgangsmåten er identisk på andre versjoner av Windows og andre lagringstjenester. Alt du trenger å gjøre er å installere synkroniseringsklienten og legge til kontoen din. Dette vil gjøre det mulig for Cryptomator å lagre data i hvelvet.



![Image](assets/fr/020.webp)



Cryptomator er et alternativ til andre programmer, særlig Picocrypt, som er presentert i en annen artikkel, og som ser annerledes ut, men er like enkelt å bruke. Cryptomator er også **åpen kildekode**, RGPD-kompatibel og **krypterer data med AES-256 bit-krypteringsalgoritmen**. Picocrypt bruker derimot den raskere XChaCha20-algoritmen (også 256-bit).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomator-applikasjonen er tilgjengelig på **Windows** (exe / msi), **Linux**, **macOS,** men også **Android** og **iOS**. Forresten, alle applikasjoner er gratis, bortsett fra Android-applikasjonen, som du må betale for (14,99 euro).



På maskinen din oppretter **Cryptomator en mappe der det opprettes et safe**. I safen, som kan være lagret på OneDrive, Google Drive eller lignende, vil dataene dine bli kryptert. Så hvis du lagrer alle dataene dine i safen på Drive-lagringsplassen din, vil de være beskyttet (fordi de er kryptert).



**I denne artikkelen brukes nettbaserte lagringstjenester som eksempel, men Cryptomator kan brukes til å kryptere data på en lokal disk, en ekstern disk eller til og med en NAS. Det finnes faktisk ingen begrensninger.**



## II. Installere Cryptomator



For å komme i gang må du **laste ned** og **installere** **Cryptomator**. Når nedlastingen er fullført, er det bare noen få klikk som skal til for å fullføre installasjonen. I likhet med [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), vil Cryptomator basere seg på WinFsp for å **montere en virtuell stasjon på Windows-maskinen din**.





- [Last ned Cryptomator fra det offisielle nettstedet](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Bruke Cryptomator på Windows



### A. Opprett en ny safe



For å opprette en ny safe klikker du på "**Legg til**"-knappen og velger "**Ny safe...**". De eksisterende og kjente safene på denne maskinen vises da i Interface, til venstre. **En safe som er opprettet på maskin A, kan åpnes og endres på maskin B**, forutsatt at den er utstyrt med Cryptomator (og krypteringsnøkkelen er kjent).



![Image](assets/fr/015.webp)



Begynn med å gi hvelvet et navn, f.eks. "**IT-Connect**". Dette vil opprette en katalog med navnet "**IT-Connect**" i OneDrive.



![Image](assets/fr/011.webp)



I neste trinn vil Cryptomator sannsynligvis **detektere "Drive"** som finnes på maskinen din: Google Drive, OneDrive, Dropbox, etc.... Slik at du kan velge leverandør direkte. Jeg prøvde dette på to forskjellige Windows 11-maskiner, med flere stasjoner, og det ble ikke oppdaget. Det er ikke noe problem, bare definer en "**Custom location**" og velg roten til lagringsplassen din. For eksempel: ** C: \ Brukere \ <Brukernavn> \ OneDrive **.



![Image](assets/fr/018.webp)



Deretter kan du justere et alternativ under ekspertinnstillinger.



![Image](assets/fr/021.webp)



Deretter må du definere **et passord som tilsvarer krypteringsnøkkelen**. Med dette passordet kan du **låse opp Cryptomator-skapet** og få tilgang til dataene. **Hvis du mister det, mister du også tilgangen til dataene dine**. Til slutt har du fortsatt muligheten til å **opprette en sikkerhetskopinøkkel** ved å krysse av for alternativet "**Yes, better safe than sorry**", omtrent på samme måte som for [BitLocker]-gjenopprettingsnøkkelen (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Dette anbefales, men ikke lagre denne sikkerhetskopinøkkelen i roten av OneDrive!



Klikk på "**Opprett en safe**".



![Image](assets/fr/019.webp)



Kopier gjenopprettingsnøkkelen og lagre den i din favorittpassordbehandler. Klikk på "**Neste**".



![Image](assets/fr/013.webp)



Nå er den nye bagasjerommet ditt opprettet og klart til bruk!



![Image](assets/fr/014.webp)



### B. Tilgangstall



For å få tilgang til en safe og dens data, enten for å **lese eksisterende data eller legge til nye data**, må du **låse den opp**. Cryptomator viser en liste over kjente safer: IT-Connect-safen vises, så det er bare å velge den og klikke på "**Unlock**".



![Image](assets/fr/016.webp)



Du må oppgi passordet ditt for å låse opp safen. Klikk deretter på "**Frigjør stasjon**".



![Image](assets/fr/022.webp)



**Safen er montert på Windows-maskinen som en virtuell stasjon, og denne stasjonen, som her arver bokstaven E, gir deg tilgang til dataene dine (i klartekst, siden safen er ulåst).**



![Image](assets/fr/017.webp)



På OneDrive-siden kan vi ikke bla gjennom Cryptomator-hvelvet direkte. Vi kan ikke se dataene (verken filnavnene eller innholdet). Dette betyr at du ikke trenger å legge til data i Cryptomator-hvelvet ditt via den vanlige OneDrive-snarveien. **Du må legge til data ved hjelp av Cryptomators virtuelle stasjon.**



![Image](assets/fr/012.webp)



### C. Alternativer for bagasjerommet



Du får tilgang til safe-innstillingene via knappen "**Encrypted volume options**" (når den er låst), og den aktiverer automatisk låsing ved inaktivitet, akkurat som du kan gjøre med passordsafen din. Alternativet "**Unlock encrypted volume on startup**" låser opp stasjonen uten at du trenger å gjøre noe, og monterer den virtuelle stasjonen. Av sikkerhetsgrunner er det best å unngå å aktivere dette alternativet.



Under fanen "**Mounting**" kan du også velge å montere den skrivebeskyttet eller tilordne en bestemt bokstav.



![Image](assets/fr/024.webp)



I tillegg kan du i Cryptomator-innstillingene **aktivere automatisk programoppstart**.



## IV. Konklusjon



Med **Cryptomator** kan du **opprette en kryptert safe** på bare noen få minutter for å beskytte dataene du ønsker å lagre på OneDrive og konsorter. Det er veldig enkelt å bruke når det gjelder å "parre" det med en stasjon: for dette formålet foretrekker jeg det fremfor Picocrypt.