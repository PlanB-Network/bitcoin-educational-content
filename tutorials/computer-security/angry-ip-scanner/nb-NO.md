---
name: Angry IP Scanner
description: En enkel måte å skanne nettverket ditt på
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten.*



___



## I. Presentasjon



Hvordan skanner du raskt og enkelt et Windows-nettverk etter tilkoblede maskiner? Svaret er Angry IP Scanner. Dette open source-prosjektet lar deg enkelt skanne et nettverk ved hjelp av en brukervennlig grafisk Interface.



Dette verktøyet kan brukes av privatpersoner til å **skanne det lokale nettverket**, men også av IT-profesjonelle til samme formål. Et bevis på at **dette verktøyet er veldig praktisk**, er at det allerede har blitt brukt av **noen nettkriminelle grupper** til å skanne bedriftsnettverk (på samme måte som Nmap). Et godt eksempel er [ransomware-gruppen RansomHub] (https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Det er fortsatt et godt stykke programvare, men som med andre nettverks- og sikkerhetsorienterte verktøy kan det misbrukes.



Her bruker vi det på **Windows 11**, men det er fullt mulig å bruke det på andre versjoner av **Windows**, samt på **Linux** og **macOS**.



**Angry IP** Scanner er mindre omfattende enn Nmap, men er likevel interessant for en rask, grunnleggende nettverksanalyse, ikke minst fordi den er innen rekkevidde for alle. Den **detekterer verter som er koblet til nettverket** og identifiserer **vertsnavn** og **åpne porter**.



Hvis du vil gå videre, kan du se veiledningen om Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Komme i gang med Angry IP Scanner



### A. Last ned og installer Angry IP Scanner



Du kan laste ned den nyeste versjonen av Angry IP Scanner fra programmets offisielle nettsted eller fra GitHub. Vi bruker det sistnevnte alternativet. Klikk på lenken nedenfor og last ned EXE-versjonen: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub] (https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Kjør den kjørbare filen for å fortsette med installasjonen. Det er ikke noe spesielt å gjøre under installasjonen.



![Image](assets/fr/013.webp)



### B. Kjør en innledende nettverksskanning



Ved første gangs oppstart bør du ta deg tid til å lese instruksjonene i vinduet "**Kommen i gang**" for å lære mer om hvordan verktøyet fungerer. Det er forresten flere begreper å ta hensyn til:





- **Feeder**: Modul som genererer lister over IP-adresser som skal skannes, fra et tilfeldig IP-område eller en fil med en liste over IP-adresser.
- **Fetcher**: et sett med moduler for å hente informasjon om verter i nettverket. Det finnes for eksempel hentere for å finne MAC-adresser, skanne porter, finne vertsnavn eller sende HTTP-forespørsler.



![Image](assets/fr/018.webp)



For å skanne et IP-undernett skriver du ganske enkelt inn **start IP Address** og **slutt IP Address** i feltet "**IP-område**" (ellers endrer du typen til høyre). Klikk deretter på "**Start**"-knappen.



![Image](assets/fr/019.webp)



Noen titalls sekunder senere vil resultatet være synlig i programvarens Interface. **For hver IP Address i det analyserte området ser du om Angry IP Scanner har oppdaget en host eller ikke, og det vises også et sammendrag på skjermen som angir antall aktive hosts (i dette tilfellet 6) og antall hosts med åpne porter.**



![Image](assets/fr/020.webp)



Her kan vi se at det finnes en host med navnet "**OPNsense.local.domain**", som er tilknyttet IP Address "**192.168.10.1**" og tilgjengelig på **port 80** og **443** (HTTP og HTTPS). Ved å høyreklikke på verten får du tilgang til flere kommandoer, for eksempel pinging, sporing av rute og åpning av nettleser via denne IP Address.



![Image](assets/fr/012.webp)



### C. Legg til skanneporter



Som standard vil **Angry IP Scanner** skanne tre porter: **80** (HTTP), **443** (HTTPS) og **8080**. Du kan legge til flere porter som skal skannes fra programmets innstillinger. Klikk på menyen "**Verktøy**", og deretter på fanen "**Porter**".



Her kan du endre portlisten via alternativet "**Portvalg**". Du kan **angi spesifikke portnumre atskilt med komma, eller portområder**. Eksempelet nedenfor legger til to porter: **445** (SMB) og **389** (LDAP). Hvis du vil skanne porter fra 1 til 1000, skriver du inn "**1-1000**". Det er ikke spesifisert om portskanninger utføres i TCP, UDP eller begge.



![Image](assets/fr/021.webp)



Hvis du kjører skanningen på nytt, vil du sannsynligvis få ny informasjon. I eksempelet nedenfor forteller Angry IP Scanner meg at port 389 og 445 er åpne på vertene "**SRV-ADDS-01**" og "**SRV-ADDS-02**", takket være den nye konfigurasjonen av porter som skal skannes.



![Image](assets/fr/022.webp)



**Merknad**: Fra menyen "**Scanner**" kan du eksportere skanneresultater til en tekstfil.



Hvis du ønsker å gå videre med skanningen, klikker du på menyen "**Tools**" og deretter på "**Fetchers**". Dette legger til "evner" i skanningen. Velg en fetcher og flytt den til venstre for å aktivere den. Dette vil legge til en ekstra kolonne i skanneresultatet.



![Image](assets/fr/014.webp)



Eksempelet nedenfor viser funksjonene "**NetBIOS info**" og "**Web detection**". Førstnevnte gir tilleggsinformasjon som maskinens MAC Address og domenenavn, mens sistnevnte viser tittelen på websiden (som kan gi en viss indikasjon på hvilken type webserver eller applikasjon det dreier seg om).



![Image](assets/fr/011.webp)



Til slutt kan du i innstillingene også endre metoden som brukes for "**ping**", dvs. for å vurdere om en vert er aktiv eller ikke. Siden noen verter ikke svarer på pinger, kan du prøve andre metoder (UDP-pakke, TCP-portsonde, ARP, UDP + TCP-kombinasjon osv.).



## III. Konklusjon



Enkelt og effektivt: Angry IP Scanner oppdager verter som er koblet til et nettverk, og lar deg konfigurere portskanninger. Den er ikke like fleksibel som Nmap når det gjelder alternativer, og den går ikke like langt, men den er en god start for rask skanning.



Hvis du ønsker å bruke **Nmap** med en grafisk Interface, kan du bruke **Zenmap-applikasjonen** (se oversikten nedenfor).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d