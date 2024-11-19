---
name: Proton Drive
description: Implementering av Sikkerhetskopiering
---
![cover](assets/cover.webp)

I dagens samfunn er det avgjørende å etablere en strategi for å sikre tilgjengeligheten, sikkerheten og sikkerhetskopieringen av dine personlige filer, som dine personlige dokumenter, bilder eller viktige prosjekter. Å miste disse dataene kan være katastrofalt.

For å forhindre disse problemene, anbefaler jeg å opprettholde flere sikkerhetskopier av filene dine på forskjellige medier. En ofte brukt strategi i databehandling er "3-2-1" sikkerhetskopieringsstrategien, som sikrer beskyttelsen av filene dine:
- **3** kopier av filene dine;
- Lagret på minst **2** forskjellige typer medier;
- Med minst **1** kopi oppbevart eksternt.

Med andre ord, det er tilrådelig å lagre filene dine på 3 forskjellige steder, ved å bruke forskjellige typer medier, som din datamaskin, en ekstern harddisk, en USB-stikk eller en nettbasert lagringstjeneste. Og til slutt, å ha en ekstern kopi betyr at du bør ha en sikkerhetskopi lagret utenfor ditt hjem eller bedrift. Dette siste punktet hjelper til med å unngå totalt tap av filene dine i tilfelle lokale katastrofer som branner eller flom. En ekstern kopi, langt fra ditt hjem eller bedrift, sikrer at dataene dine vil overleve uavhengig av lokale risikoer.

For å lette implementeringen av 3-2-1 sikkerhetskopieringsstrategien, kan du bruke en nettbasert lagringstjeneste. Disse løsningene, ofte referert til som "skyen", tilbyr ekstra beskyttelse ved å lagre dataene dine på sikre servere tilgjengelige fra enhver enhet. Uttrykket "sky" refererer simpelthen til lagring av data på eksterne servere.

Mange mennesker bruker lagringsløsningene til store digitale selskaper: Google Drive, Microsoft OneDrive eller Apple iCloud.
![PROTON DRIVE](assets/notext/01.webp)
Disse løsningene er praktiske for daglig bruk og sikrer tilgjengeligheten av dataene dine, men de garanterer ikke konfidensialitet. I denne veiledningen foreslår jeg å oppdage en annen løsning, like enkel å bruke som lagringsverktøyene til Big Tech, men med ekstra tiltak for å beskytte ditt privatliv. Denne løsningen er Proton Drive, det nettbaserte lagringsverktøyet fra det sveitsiske selskapet Proton. Vi vil også se hvordan man enkelt kan implementere en 3-2-1 strategi egnet for daglig bruk.

## Introduksjon til Proton Drive
Proton Drive er en interessant løsning for nettbasert lagring fordi den kombinerer brukervennlighet med sikkerhet for filene dine. I motsetning til tradisjonelle skytjenester fra teknologigiganter, implementerer Proton Drive tiltak for å beskytte ditt privatliv. Den sikrer ende-til-ende-kryptering for alle filene dine, noe som betyr at selv Protons team ikke kan få tilgang til dataene dine. Dessuten er Proton Drive åpen kildekode, noe som tillater uavhengige eksperter å fritt revidere programvarekoden.
![PROTON DRIVE](assets/notext/02.webp)
Protons forretningsmodell er basert på et abonnementssystem, noe som er betryggende da det indikerer at selskapet er finansiert uten nødvendigvis å utnytte brukernes data. I denne veiledningen vil jeg forklare hvordan du bruker den gratis versjonen av Proton Drive, men det finnes også flere abonnementsnivåer som tilbyr flere funksjoner. Denne forretningsmodellen er å foretrekke fremfor et gratis system i stil med Big Tech, noe som kan lede en til å lure på om våre personlige data blir brukt til fortjeneste. Dette ser ikke ut til å være tilfellet med Proton.

Proton Drive tilbyr mye mer enn bare lagringsalternativer; det tillater også deling, redigering og samarbeid om dokumenter på nett med redigeringsverktøy, likt Googles programvaresuite.
Angående [priser](https://proton.me/pricing), tilbyr gratisversjonen opptil 5 GB lagringsplass og inkluderer grunnleggende funksjoner. For å utvide kapasiteten til 200 GB lagringsplass, er et spesifikt abonnement på Proton Drive tilgjengelig for 4 € per måned. Proton Unlimited-pakken tilbyr derimot for 10 € per måned en lagringsplass på opptil 500 GB på Proton Drive, i tillegg til å inkludere alle Protons betalte tjenester, som VPN og passordbehandler, samt ekstra fordeler på gratisverktøy (e-post og kalender). ![PROTON DRIVE](assets/notext/03.webp)
## Hvordan opprette en Proton-konto?

Hvis du ennå ikke har en Proton-konto, må du opprette en. Jeg henviser deg til vår Proton Mail-opplæring der vi forklarer i detalj hvordan du oppretter en gratis Proton-konto og setter den opp:

https://planb.network/tutorials/others/proton-mail
![PROTON DRIVE](assets/notext/04.webp)
## Hvordan sette opp Proton Drive?

Når du er logget inn på din Proton Mail, klikk på ikonet med fire små kvadrater øverst til venstre på skjermen.
![PROTON DRIVE](assets/notext/05.webp)
Deretter klikker du på "*Drive*".
![PROTON DRIVE](assets/notext/06.webp)
Du er nå på din Proton Drive.
![PROTON DRIVE](assets/notext/07.webp)
## Hvordan bruke Proton Drive?
For å legge til filer i din Proton Drive, når du utelukkende bruker webversjonen (vi vil diskutere bruk av den lokale versjonen senere), trenger du bare å dra og slippe dokumentene dine direkte inn i grensesnittet. ![PROTON DRIVE](assets/notext/08.webp) Du kan deretter finne dokumentet ditt på hjemmesiden. ![PROTON DRIVE](assets/notext/09.webp) For å legge til et nytt element, klikk på "*Ny*" knappen øverst til venstre på skjermen. ![PROTON DRIVE](assets/notext/10.webp) Funksjonen "*Last opp fil*" åpner din lokale filutforsker, som lar deg velge og importere nye dokumenter til Proton Drive, akkurat som du ville gjort ved å dra og slippe. ![PROTON DRIVE](assets/notext/11.webp) "*Last opp mappe*" lar deg importere en hel mappe. ![PROTON DRIVE](assets/notext/12.webp) "*Ny mappe*" gjør det mulig for deg å opprette en mappe for bedre å organisere dokumentene dine på Proton Drive. ![PROTON DRIVE](assets/notext/13.webp) Klikk på dette alternativet, tildel et navn til mappen din. ![PROTON DRIVE](assets/notext/14.webp) Deretter vil du finne den direkte på hjemmesiden til Proton Drive. ![PROTON DRIVE](assets/notext/15.webp) Til slutt, "*Nytt dokument*" lar deg opprette et nytt tekst dokument direkte i Proton Drive. ![PROTON DRIVE](assets/notext/16.webp) Ved å klikke på det, åpnes et nytt blankt dokument. ![PROTON DRIVE](assets/notext/17.webp) Du kan skrive på det og redigere det. ![PROTON DRIVE](assets/notext/18.webp) Hvis du klikker på "*Del*" knappen øverst til høyre, kan du dele dokumentet. ![PROTON DRIVE](assets/notext/19.webp) Du trenger bare å skrive inn e-posten til bidragsyteren som du ønsker å gi tilgang til dokumentet, enten i skrivebeskyttet modus eller med redigeringsrettigheter. ![PROTON DRIVE](assets/notext/20.webp) Hvis du går tilbake til din Proton Drive, kan du se at dokumentet har blitt lagret vellykket. ![PROTON DRIVE](assets/notext/21.webp) I fanen "*Delt*" kan du finne dokumentene som du har delt med andre. ![PROTON DRIVE](assets/notext/22.webp) Og i fanen "*Delt med meg*" kan du se dokumentene som andre har delt med deg. ![PROTON DRIVE](assets/notext/23.webp) Til slutt, i fanen "*Søppel*" kan du finne dine nylig slettede dokumenter. ![PROTON DRIVE](assets/notext/24.webp) De fleste innstillinger for din Proton Drive er integrert i din Proton-konto. For detaljerte instruksjoner om å sette opp kontoen din, inviterer jeg deg til å konsultere denne veiledningen:
https://planb.network/tutorials/others/proton-mail

## Hvordan installere Proton Drive programvare?
Proton Drive tilbyr også programvare som muliggjør synkronisering av dine lokale filer med ditt online lagringsområde. Denne funksjonen letter og automatiserer implementeringen av vår 3-2-1 sikkerhetskopistrategi. Med Proton Drive-programvaren får du 2 synkroniserte kopier av filene dine: en på datamaskinen din og den andre på Protons servere, og oppfyller dermed kriteriene for 2 mediatyper og sikkerhetskopi utenfor stedet. Du trenger bare å opprette en tredje kopi, som vi vil sette opp senere.
For å bruke programvaren, klikk på fanen "*Datamaskiner*" på din Proton Drive-konto og velg knappen som tilsvarer ditt operativsystem for å fortsette med nedlastingen.
![PROTON DRIVE](assets/notext/25.webp) Når du har installert, må du logge inn for å låse opp kontoen din, og deretter klikke på "*Logg inn*".
![PROTON DRIVE](assets/notext/26.webp)
Velg de lokale filene du ønsker å synkronisere med din Proton Drive.
![PROTON DRIVE](assets/notext/27.webp)
For eksempel har jeg kun valgt mappen "*Proton Backup*". Deretter klikker du på "*Fortsett*" knappen.
![PROTON DRIVE](assets/notext/28.webp)
Du vil da komme til programvaregrensesnittet, som ligner på webapplikasjonen.
![PROTON DRIVE](assets/notext/29.webp)
Fra nå av vil du ha en mappe med tittelen "*Proton Drive*" lokalt på datamaskinen din, som vil samle alle dokumentene dine lagret på Proton online. Hvis du legger til en fil i denne mappen fra datamaskinen din, vil du automatisk finne den på hjemmesiden til Proton Drive webapplikasjonen, og omvendt. For mappene du valgte å synkronisere under programvareinstallasjonen, kan du også finne dem online ved å gå til "*Datamaskiner*" seksjonen av Proton Drive og deretter velge datamaskinen din.
![PROTON DRIVE](assets/notext/30.webp)
Slik blir alle filene dine sikkerhetskopiert og synkronisert både lokalt på maskinen din og på Proton Drives online servere.

## Hvordan lage en sikkerhetskopi av Proton Drive?

Hvis du har fulgt de foregående trinnene, har du nå 2 distinkte sikkerhetskopi-lokasjoner for dine viktige filer. For å fullføre vår 3-2-1 sikkerhetskopistrategi, trenger vi å legge til en tredje kopi.
Jeg foreslår at du utfører denne ekstra sikkerhetskopien på et eksternt medium, som for eksempel en ekstern harddisk eller en USB-stikk. Avhengig av intensiteten av din bruk, sett en passende frekvens for oppdatering av sikkerhetskopien (ukentlig, månedlig, halvårlig...). Ved hvert valgt intervall, vil du trenge å laste ned hele din Proton Drive for å sikkerhetskopiere dataene på det valgte eksterne mediet. På denne måten, selv i tilfelle tyveri av datamaskinen din og samtidig ødeleggelse av Protons servere, vil du fortsatt opprettholde sikker tilgang til filene dine takket være kopien på USB-stikken.

For å gjøre dette, gå til din Proton Drive.
![PROTON DRIVE](assets/notext/31.webp)
Velg alle filene dine.
![PROTON DRIVE](assets/notext/32.webp)
Deretter klikker du på den lille pilen for å laste dem ned.
![PROTON DRIVE](assets/notext/33.webp)
Vi vil deretter gjenta operasjonen med våre filer synkronisert fra vår datamaskin.
![PROTON DRIVE](assets/notext/34.webp)
Du vil da finne .zip-filer i nedlastingene dine. Koble ganske enkelt det eksterne mediet du foretrekker til datamaskinen din, og overfør deretter disse filene til det.
![PROTON DRIVE](assets/notext/35.webp)
Hvis du er bekymret for at denne USB-stikken kan bli stjålet, vurder å kryptere den med programvare som VeraCrypt (vi vil lage en opplæring om denne programvaren snart).

Gratulerer, du har nå en veldig robust 3-2-1 sikkerhetskopistrategi, som lar deg drastisk redusere risikoen for å miste tilgangen til dine personlige dokumenter, uansett omstendighetene. Ved å velge Proton Drive for dine online sikkerhetskopier, drar du også nytte av ende-til-ende-kryptering, som garanterer beskyttelsen av ditt privatliv.

For å lære mer om å sikre din online tilstedeværelse og unngå hacking, anbefaler jeg også at du konsulterer vår detaljerte opplæring om Bitwarden passordbehandler:

https://planb.network/tutorials/others/bitwarden