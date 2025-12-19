---
name: DietPi
description: Lettvektsoperativsystem optimalisert for maskiner med lav ytelse. Med en preferanse for selvhosting
---

![cover](assets/cover.webp)



I ikke-tekniske kretser er merker som "Android", "Raspberry Pi", "Orange Pi" eller "Radxa" lite kjent. Men det er bare å ta en titt i teknologikretser for å oppdage at **SBC**-datamaskiner - bygget på ett enkelt hovedkort, ofte mikroskopiske i størrelse sammenlignet med vanlige datamaskiner - er blitt uunnværlige som støtte for ethvert personlig prosjekt.



Dette er datamaskiner som produseres i en lang rekke modeller. De er fortrinnsvis vertskap for Linux-distribusjoner, som ofte er tilpasset for å kjøre problemfritt på disse underdrevne maskinene.



**DietPi er ikke noe unntak**: Det er et Debian-basert operativsystem som er optimalisert for å være så lett som mulig og gjøre selv de minst effektive `SBC`ene svært raske. Det ble byttet fra Debian12 Bookworm til Debian13 Trixie akkurat da denne veiledningen ble skrevet, og støtter nå også `RISC-V`-prosessorbaserte SBC-er med åpen kildekode. DietPi er en hyggelig oppdagelse som fortjener å bli studert nærmere.



## Styrker



Dette er ikke den "vanlige kopien" av Debian for små kort av typen Raspberry. DietPi er det:




- Optimalisert for hastighet og letthet**: en [sammenligning med andre Debian-distribusjoner for SBC](https://dietpi.com/blog/?p=888), DietPi er lettere i alt. DietPi ISO-bildet veier mindre enn 1 GB, og er det desidert minste blant de som er dedikert til eldre modeller av Raspberry eller Orange PI (for eksempel). Etterspørselen etter RAM- og CPU-ressurser er veldig lav, slik at den alltid får det beste ut av brettene, selv eldre.
- Innebygde automatiseringer og installeringsprogrammer**: En rekke dedikerte kommandoer hjelper brukerne med å overvåke systemressursene samt automatisere oppgaver for å installere og starte programmer, oppdatere versjoner, ta sikkerhetskopier og sjekke alle logger.
- Et sterkt, eksperimentorientert fellesskap**: [tutorials] (https://dietpi.com/forum/c/community-tutorials/8) og prosjekter fra DietPi-fellesskapet er ideelle for å bli inspirert av programvare du kan installere med ett klikk, takket være DietPi.



**Det har aldri vært enklere å få ut hver eneste bit av SBC-en**.



## Automatiseringer for selvhosting


Vil du eksperimentere med din egen server for å kjøre avanserte nettverksløsninger, eller verktøy for å utvikle Bitcoin-kompetansen din? DietPi kan være løsningen du har lett etter. Selv om mange kan administrere sin egen infrastruktur og kjøre perfekt konfigurerte og beskyttede servere, er DietPi et passende steg for dem som ønsker å starte helt fra bunnen av.



I stedet for å utføre alle de komplekse oppgavene som en slik oppgave krever manuelt, lar DietPi deg bygge dem med en `veiviser` og en egen kommandolinje. Her kan du eksperimentere med din egen personlige sky, _smart home_-enhetsadministrasjon, automatiserte sikkerhetskopier og crontab, samt mer avanserte løsninger.



![img](assets/en/01.webp)



## Installasjon



### Last ned



DietPi tilbyr et utallige sett med ISO-bilder, slik at du kan brenne operativsystemet til mange forskjellige enheter. Noen støttes bare: ISO-en for Raspberry PI5 er for eksempel fortsatt under testing, men du kan definitivt finne den som passer for ditt kort.



I denne guiden valgte jeg å installere den på en tynn klient, så valget gikk til _PC/VM_ og deretter til _Native PC_. Det finnes to ISO-bilder for disse enhetene, som skiller seg fra hverandre når det gjelder genereringen av bootloaderen. Maskinen som ble brukt i veiledningen er ganske gammel, så valget falt på _BIOS/CSM_-versjonen. Hvis du har en nyere maskin, kan den riktige versjonen være `UEFI`.



![img](assets/en/02.webp)



Du kommer til siden som inneholder `bildet av installasjonsprogrammet`, `sha256` og `Signaturene`.



![img](assets/en/03.webp)



Forbered en katalog i `home` på din daglige datamaskin, slik at du kan laste ned de nødvendige filene med `wget`.



![img](assets/en/04.webp)



Utviklerens offentlige nøkkel krevde et minimum av research, men du finner den på denne lenken: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Sjekk innholdet i katalogen med `ls -la`, og importer MichaIng-nøkkelen til nøkkelringen din med `gpg --import`.



### Verifisering og blits



Til slutt, den delen jeg anbefaler mest: forsikre deg om ektheten til operativsystemet du har lastet ned og skal installere på SBC-en.



![img](assets/en/06.webp)



Hvis du også fikk resultatet `Good signature` og den samme Hash-kontrollen med sha256sum-kommandoen, kan du fortsette å flashe ISO-en til en USB-pinne. Bruk apper som Whale Etcher for å gjøre dette.



![img](assets/en/07.webp)



## Installasjon av DietPi



![img](assets/en/09.webp)



Overfør minnepinnen til enheten som skal være vert for DietPi, og start installasjonen av operativsystemet lime Green. I denne øvelsen bruker vi en tynn klient med 16 GB RAM, en 128 GB SSD for operativsystemet og en annen 1 TB datadisk. Installasjonen tok mindre enn 30 minutter, men hvis du for eksempel bruker en Raspberry, kan ressursene være mindre og ta lengre tid. Du vil bli vist fremdriften under installasjonen.



![img](assets/en/08.webp)



DietPi er designet for Raspberry og lignende, og den egentlige naturen til DietPi er den såkalte `headless`-installasjonen, uten et grafisk miljø og med innfødt `shshsh'-tilgang. I guiden vil du i stedet se et grafisk miljø, nærmere bestemt LXDE.



I dette trinnet blir du også bedt om å velge hvilken nettleser du vil bruke som standard, enten Chromium eller Firefox. Begge fungerer bra, og det er ingen spesielle kontraindikasjoner mot noen av dem, annet enn dine personlige preferanser.



Mot slutten kan installasjonsprogrammet spørre deg om du vil installere noen programmer allerede, men her ** anbefaler jeg at du ikke forhåndsinstallerer noe**. Etter dette trinnet vil du bli bedt om å endre standardpassordene til de to brukerne, av sikkerhetsmessige årsaker. Det viktigste er at du blir bedt om å **innstille det globale programvarepassordet (GSP)`**, som vil sikre tilgang til de ulike programvarene på en kontrollert måte. **Hvis du laster ned programvare under installasjonen av operativsystemet uten at du har angitt GSP, vil de forbli praktisk talt utilgjengelige**. Du må avinstallere og installere dem på nytt etter at du har satt `Global Software Password`: derfor, **ikke legg inn noe for å unngå dobbeltarbeid**. (Ulempen er sannsynlig, ikke 100% sikker).



Installasjonen avsluttes med en forespørsel om å aktivere DietPi-Survey, en automatisert datainnsamlingstjeneste som brukes til å støtte utviklingen av operativsystemet. Ifølge nettstedet aktiveres datainnsamlingen når du laster ned programvare fra automatiseringen som DietPi tilbyr, eller når du oppgraderer til neste versjon. Alle har muligheten til å melde seg på (_Opt IN_) eller av (_Opt OUT_).



![img](assets/en/23.webp)



Etter fullført installasjon og påfølgende omstart dukker DietPi opp på skjermen slik du setter den opp. For opplæringen valgte jeg som nevnt det grafiske miljøet `LXDE`. På skrivebordet fant jeg snarveien for å starte `htop` og den åpne terminalen.



![img](assets/en/10.webp)



### "Verktøy" fra operativsystemet



Glem de fleste programmene du bruker på Linux-distribusjonen din - DietPi er så optimalisert at du har utelatt en hel del. Du må i utgangspunktet installere mange kommandoer manuelt, men hvis du bare prøver det ut, kan du motstå fristelsen og prøve å sette DietPis automatiseringer på prøve.



Det er definitivt terminalen som er det første nyttige verktøyet for å komme i gang med det nye operativsystemet, og den åpnes automatisk hver gang du slår den på.



![img](assets/en/11.webp)



På terminalskjermen finner du en rekke kommandoer innledet med `dietpi-`, som representerer [verktøyene] (https://dietpi.com/docs/dietpi_tools/) i dette operativsystemet:




- `dietpi-launcher`: for å få tilgang til operativsystemet, filbehandling osv
- `dietpi-Software`: som representerer verktøyet som du kan bruke til å installere all programvaren som allerede er tilgjengelig i pakken
- `dietpi-config`: for å få tilgang til systemkonfigurasjoner, selv de mest avanserte.



![img](assets/en/14.webp)



### Sikkerhetskopiering



Sikkerhetskopiering av en server er en rutine som systemadministratoren bør ta høyde for fra første oppstart.



Med DietPi finnes kommandoen `dietpi-Backup`, som jeg anbefaler at du utforsker for å finne den ideelle løsningen: den lar deg sette opp en regelmessig sikkerhetskopi, inkrementell eller ikke, avhengig av hvilke applikasjoner som brukes, og alle alternativene for å tilpasse rutinen.



![img](assets/en/22.webp)



Velg destinasjonen for sikkerhetskopien, for eksempel en annen disk, ved å starte `dietpi-Drive_Manager` for å montere destinasjonsdisken og bruke den til denne funksjonen.



## Konfigurasjon



Selvhosting er en tilrådelig opplevelse for alle, enten de er nysgjerrige eller bare entusiastiske. Å sette opp og konfigurere en server innebærer imidlertid noen ikke ubetydelige teknologiske utfordringer. Det er her **enkelheten til DietPi** kommer inn i bildet, slik at du kan konfigurere et system som er skreddersydd til dine behov i noen få enkle trinn.



![img](assets/en/24.webp)



Grunnleggende og avanserte innstillinger, alt er lett tilgjengelig i den ene Interface som følger med kommandoen:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-programvare


```