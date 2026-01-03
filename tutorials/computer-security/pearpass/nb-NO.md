---
name: PearPass
description: Få kontroll over passordene dine med en lokal, nettskyfri passordbehandler som fungerer peer-to-peer
---

![cover](assets/cover.webp)



I en tid der hver enkelt person administrerer dusinvis, til og med hundrevis av nettkontoer, har sikkerheten ved pålogginger blitt et sentralt tema innen IT-sikkerhet. Sosiale nettverk, meldingssystemer, profesjonelle tjenester, finansielle plattformer: Hver av disse tilgangene er avhengig av en hemmelighet, og hvis den blir avslørt, kan det få alvorlige konsekvenser for livet ditt.



Likevel, til tross for økningen i angrep, er dårlige praksiser fortsatt utbredt i befolkningen: svake passord, gjenbrukte passord, passord lagret i klartekst eller omtrent husket. For å løse disse problemene uten å komplisere hverdagen, er løsningen å bruke en passordbehandler.



Det finnes allerede dusinvis av passordbehandlere, og Plan ₿ Academy tilbyr en veiledning for de fleste av dem. Men i denne veiledningen vil jeg introdusere deg for en som skiller seg klart ut fra resten når det gjelder hvordan den fungerer: **PearPass**.



**PearPass er en peer-to-peer passordbehandler, lokal-først og åpen kildekode, utviklet for å gi brukeren full kontroll over sine data.**



![Image](assets/fr/01.webp)



## Hvorfor velge PearPass?



En passordbehandler er et program som genererer, lagrer og organiserer alle passordene dine på en sikker måte. I stedet for å huske eller gjenbruke passord, har du bare én hemmelighet å beskytte: hovedpassordet, som krypterer hele safen din. Denne tilnærmingen gjør det mulig å bruke unike, lange og tilfeldige passord for hver tjeneste, noe som reduserer både risikoen for å glemme og kompromittere passordene, samtidig som det begrenser konsekvensene av en eventuell lekkasje. I dag er det et grunnleggende IT-verktøy som alle bør bruke.



Det finnes to hovedkategorier av passordbehandlere. På den ene siden finnes det lokal programvare, som er veldig sikker siden data aldri lagres på en sentral server, men som ikke er veldig praktisk, siden den ikke lar deg enkelt synkronisere legitimasjonen din mellom flere enheter (datamaskin, smarttelefon, nettbrett...). På den annen side lagrer skybaserte passordadministratorer legitimasjonen din på serverne sine og synkroniserer dem på tvers av alle enhetene dine. Den største fordelen er bekvemmeligheten, men de innebærer et kompromiss når det gjelder sikkerhet, siden passordene dine lagres på infrastrukturer du ikke har kontroll over.



PearPass bryter bevisst med begge modellene. Den plasserer seg mellom lokale administratorer og skyløsninger: Den muliggjør synkronisering av passordene dine, samtidig som den garanterer at de aldri lagres på eksterne servere. Resultatet er at all legitimasjon lagres lokalt på enhetene dine, og synkronisering mellom flere maskiner skjer utelukkende peer-to-peer. Denne arkitekturen eliminerer de enkelte feilkildene som er forbundet med sentraliserte databaser: Det finnes ingen servere som kan kompromitteres, og ingen tredjeparts infrastruktur som kan få tilgang til påloggingsinformasjonen din. Kommunikasjonen mellom enhetene dine er kryptert fra ende til ende, noe som sikrer at bare nøklene du har, gir tilgang til data.



![Image](assets/fr/02.webp)



For å gjøre dette mulig, som navnet antyder, baserer PearPass seg på **Pears**, et peer-to-peer-teknologiøkosystem dedikert til opprettelse og kjøring av serverløse applikasjoner. Pears tilbyr kjøringsmiljøet, distribusjonsmekanismene og nettverkslagene som trengs for å kjøre fullstendig desentraliserte applikasjoner, som kan synkroniseres direkte mellom jevnaldrende, uten noen sentral infrastruktur. Når det gjelder PearPass, sørger Pears for enhetsoppdagelse, kryptert tilkoblingsetablering og synkronisering av passordhvelv mellom maskinene dine. Denne tilnærmingen sikrer at PearPass forblir funksjonell, robust og uavhengig av eksterne myndigheter.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

I tillegg til denne innovative arkitekturen er PearPass helt åpen kildekode, og alle funksjonene er gratis. Programvaren har også blitt uavhengig revidert av Secfault Security. I tillegg til den spesifikke arkitekturen tilbyr PearPass selvfølgelig alle de klassiske funksjonene som forventes av en god passordbehandler, noe vi vil oppdage i løpet av denne veiledningen.



Kort sagt, der tradisjonelle passordadministratorer ber deg om å stole på et selskap og dets servere, har PearPass en suverenitetslogikk: ingen sky, ingen sentraliserte kontoer, ingen mellomledd. Du beholder eksklusiv kontroll over legitimasjonen din, samtidig som du drar nytte av synkronisering mellom enhetene dine.



## Hvordan installerer jeg PearPass?



PearPass er tilgjengelig på alle plattformer: Windows, Linux, macOS, Android, iOS og nettleserutvidelser. Det er ikke nødvendig å installere Pears på maskinen din: PearPass fungerer på egen hånd.



### Installasjon på Windows



På Windows leveres PearPass som et klassisk installasjonsprogram. Gå til [den offisielle nedlastingssiden] (https://pass.pears.com/download), og klikk deretter på knappen `Last ned Windows-installasjonsprogram`.



Når filen er lastet ned, åpner du installasjonsprogrammet og følger trinnene i veiviseren. Programmet kan deretter åpnes fra Start-menyen eller via en snarvei på skrivebordet.



![Image](assets/fr/03.webp)



### Installasjon på macOS



På macOS distribueres PearPass som et diskbilde (`.dmg`). Gå til [den offisielle nedlastingssiden] (https://pass.pears.com/download) og velg den versjonen som tilsvarer Mac-arkitekturen din (Intel eller Apple Silicon). Etter nedlastingen åpner du filen `.dmg` og starter programmet fra mappen `Applications`.



Ved første oppstart vil macOS vise en sikkerhetsmelding som indikerer at applikasjonen kommer fra Internett: Bare bekreft for å fortsette.



### Installasjon på Linux



På Linux er PearPass tilgjengelig i `.AppImage`-format, noe som garanterer bred kompatibilitet med de fleste distribusjoner uten noen spesifikke avhengigheter. Last ned `.AppImage`-filen fra [den offisielle nedlastingssiden] (https://pass.pears.com/download), og start den deretter direkte ved å dobbeltklikke.



Avhengig av miljøet ditt kan det hende du må gjøre filen kjørbar via filegenskaper (høyreklikk) eller med kommandoen `chmod +x`. Når PearPass er autorisert, starter det som et frittstående program.



### Installasjon av nettleserutvidelse



PearPass tilbyr en nettleserutvidelse for automatisk pålogging og rask tilgang til safen din mens du surfer på nettet. Utvidelsen er for øyeblikket tilgjengelig for Google Chrome og kompatible nettlesere. For å installere den, gå til [den offisielle nedlastingssiden] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Når den er lagt til, kan du feste den til verktøylinjen for rask tilgang. For å aktivere utvidelsen må du ha en kobling til PearPass-programmet som er installert lokalt på datamaskinen (vi kommer tilbake til dette senere i veiledningen).



### Installasjon på iOS og Android



På iPhone og Android laster du ganske enkelt ned applikasjonen fra appbutikken din:




- [Google Play Store] (https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store] (https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



I tillegg til disse klassiske installasjonsmetodene er det også mulig å laste ned programvaren direkte fra GitHub-repositorier, for hver :




- [Desktop] (https://github.com/tetherto/pearpass-app-desktop);
- [Mobil] (https://github.com/tetherto/pearpass-app-mobile);
- [Nettleserutvidelse] (https://github.com/tetherto/pearpass-app-browser-extension).



Når PearPass er installert på en eller flere plattformer, kan du gå videre til den første konfigurasjonen. I denne veiledningen starter vi med å konfigurere programvaren på skrivebordet, og deretter synkroniserer vi den med nettleserutvidelsen og mobilapplikasjonen.



## Hvordan oppretter jeg en PearPass-safe?



Når du starter PearPass på datamaskinen din, blir du guidet gjennom to trinn: først angir du hovedpassordet ditt, og deretter oppretter du din første safe.



### Angi hovedpassord



Når programmet startes opp på skrivebordet, klikker du på knappen "Hopp over" og deretter på "Fortsett" for å gå gjennom introduksjonsskjermen og komme til konfigurasjonsfasen for hovedpassordet.



![Image](assets/fr/06.webp)



Det neste viktige steget er å velge hovedpassordet ditt. Som vi så i innledningen, er dette passordet svært viktig, ettersom det gir deg tilgang til alle de andre passordene du har lagret i administratoren. Teknisk sett brukes det til å utlede de kryptografiske nøklene som brukes til å kryptere dataene dine.



Hovedpassordet innebærer to hovedrisikoer: tap og kompromittering. Hvis du mister tilgangen til dette passordet, vil du ikke lenger kunne få tilgang til legitimasjonen din. PearPass lagrer nemlig aldri hovedpassordet ditt: **hvis det går tapt, går legitimasjonen din tapt for godt**. Det finnes ingen gjenopprettingsmekanisme. Omvendt, dersom dette passordet kompromitteres og en angriper får tilgang til en av enhetene dine, vil vedkommende kunne få tilgang til alle kontoene dine.



For å begrense risikoen for tap kan du ta en fysisk sikkerhetskopi av hovedpassordet ditt, for eksempel på papir, og oppbevare den på et sikkert sted. Forsegl gjerne denne sikkerhetskopien i en konvolutt, slik at du med jevne mellomrom kan kontrollere at ingen har hatt tilgang til den. På den annen side må du aldri ta en digital sikkerhetskopi av dette passordet.



For å redusere risikoen for kompromittering må hovedpassordet være sterkt. Det bør være så langt som mulig, inneholde et bredt utvalg av tegn og velges på en helt tilfeldig måte. I 2025 er minimumsanbefalingene minst 13 tegn, inkludert store og små bokstaver, tall og symboler, forutsatt at passordet er tilfeldig. Jeg vil imidlertid anbefale et passord på minst 20 tegn, om ikke mer, med alle typer tegn, for å sikre et mer varig sikkerhetsnivå.



Skriv inn hovedpassordet ditt i feltet, bekreft det en gang til, og klikk deretter på knappen `Fortsett`.



![Image](assets/fr/07.webp)



Du blir deretter omdirigert til innloggingsskjermen: Skriv inn hovedpassordet ditt for å sjekke at alt fungerer som det skal.



![Image](assets/fr/08.webp)



### Opprett din første safe



Når du har logget inn, vil PearPass be deg om å opprette din første safe. En safe er en kryptert beholder der du lagrer passord, ID-er, sikre notater og annen informasjon. Hver safe er isolert og kan identifiseres med et eget navn, slik at du kan organisere dataene dine i henhold til hva du bruker dem til (personlig, profesjonelt, spesifikke prosjekter...).



Klikk på knappen "Opprett et nytt hvelv".



![Image](assets/fr/09.webp)



Velg et navn for hvelvet, og klikk deretter på "Opprett et nytt hvelv" igjen for å fullføre opprettelsen.



![Image](assets/fr/10.webp)



Safen er umiddelbart klar til bruk. Du kan begynne å legge til passord, pålogginger eller sikre notater med en gang.



![Image](assets/fr/11.webp)



## Hvordan legger jeg til en pålogging i PearPass?



Når du har opprettet safen din, kan du begynne å lagre gjenstandene dine i den. PearPass støtter registrering av mange typer gjenstander:




- logge inn på et nettsted eller en tjeneste ;
- identitet: din personlige informasjon for raskt å fylle ut skjemaer, men også for å lagre identitetsdokumenter direkte i PearPass ;
- kredittkort: kredittkortnummeret ditt for raskere betaling når du handler på nettet;
- Wi-Fi: passord for Wi-Fi-nettverkene dine ;
- PassPhrase: hemmelig frase som består av flere ord (advarsel: Jeg fraråder på det sterkeste å bruke den til wallet Bitcoin mnemoniske fraser);
- merk: opprette sikre notater ;
- egendefinert: Med denne funksjonen kan du opprette en egendefinert elementtype, tilpasset dine spesifikke behov.



Start med å åpne PearPass og logg inn med hovedpassordet ditt.



![Image](assets/fr/12.webp)



Velg safen du ønsker å lagre identifikatoren i.



![Image](assets/fr/13.webp)



På startsiden klikker du på knappen for å legge til et nytt element, avhengig av hvilken type informasjon du ønsker å registrere. I mitt tilfelle ønsker jeg å legge til en pålogging for kontoen min på Plan ₿ Academy-nettstedet, så jeg klikker på knappen "Opprett en pålogging".



![Image](assets/fr/14.webp)



Når du har valgt hvilken type vare du ønsker å legge til, får du opp et skjema der du kan legge inn informasjonen som er knyttet til den aktuelle tjenesten. Avhengig av hva du har behov for, kan du legge inn tjenestens navn, innlogging, passord og eventuelt nettadresse og ytterligere merknader.



PearPass har også en passordgenerator, slik at du kan opprette et sterkt passord direkte fra skjemaet. For å bruke den, klikk på ikonet som representerer tre små prikker i `Passord`-feltet, velg ønsket lengde, og klikk deretter på `Insert password`.



Når alle feltene er fylt ut, klikker du på "Lagre"-knappen for å lagre identifikatoren i safen.



![Image](assets/fr/15.webp)



Identifikatoren er nå lagret. Den vises i listen over elementer i den valgte safen, og kan vises ved å klikke på den.



![Image](assets/fr/16.webp)



Du kan enkelt endre et element ved å klikke på det og deretter på "Rediger"-knappen. Du kan også slette det ved å klikke på de tre små prikkene øverst til høyre i grensesnittet, og deretter på "Slett element".



![Image](assets/fr/22.webp)



På mobil forblir logikken den samme, selv om grensesnittet er tilpasset. Etter at du har logget inn, velger du ønsket safe, trykker på `+`-knappen, velger hvilken type vare som skal opprettes, og fyller deretter ut den nødvendige informasjonen.



![Image](assets/fr/17.webp)



## Hvordan organisere PearPass?



Som vi så i de foregående avsnittene, lar PearPass deg opprette flere forskjellige hvelv. Dette gjør det mulig å skille mellom ulike bruksområder og utgjør et første organisasjonsnivå for passordbehandleren din. Fra startsiden kan du enkelt bytte fra ett hvelv til et annet ved å klikke på pilen øverst til venstre i grensesnittet.



![Image](assets/fr/18.webp)



En annen måte å organisere passordene dine på, selv innenfor et hvelv, er å opprette mapper. Dette gjør du ved å klikke på `+`-symbolet ved siden av `Alle mapper` i venstre kolonne i grensesnittet, og deretter skriver du inn navnet på mappen du ønsker å opprette.



![Image](assets/fr/19.webp)



Deretter kan du lagre de identifikatorene du ønsker, enten direkte når du oppretter et element, eller senere ved å klikke på "Rediger". Alt du trenger å gjøre, er å velge ønsket mappe øverst i venstre hjørne av skjemaet.



![Image](assets/fr/20.webp)



Når du har åpnet et element, for eksempel en pålogging, kan du klikke på stjerneikonet øverst til høyre i grensesnittet for å legge det til blant favorittene dine. Favorittene kan raskt finnes i en egen mappe, i tillegg til grunnmappen.



![Image](assets/fr/21.webp)



Til slutt finnes det et søkefelt øverst i grensesnittet, slik at du raskt kan finne det du leter etter, selv om hvelvet ditt inneholder mange identifikatorer.



## Hvordan synkroniserer jeg PearPass på mobilen min?



Nå som du har et fungerende hvelv med elementer lagret på datamaskinen din, vil du sannsynligvis ha tilgang til passordene dine fra smarttelefonen eller en annen enhet. PearPass lar deg synkronisere administratoren din på flere maskiner på en sikker måte ved hjelp av Pears. La oss finne ut hvordan.



Først logger du deg inn i hvelvet på kildemaskinen (for eksempel datamaskinen din) ved hjelp av hovedpassordet ditt. Når du er på startsiden, klikker du på knappen "Legg til en enhet" nederst til høyre i grensesnittet.



![Image](assets/fr/23.webp)



PearPass genererer deretter en invitasjonskobling, også tilgjengelig som en QR-kode, for å synkronisere det valgte hvelvet på den enheten du ønsker.



![Image](assets/fr/24.webp)



Hvis du vil synkronisere på mobilenheten din, må du først installere programmet og deretter starte det. Du blir bedt om å opprette et hovedpassord for din mobile manager. Du kan velge å bruke det samme passordet som på datamaskinen, eller et annet. I alle tilfeller følger du de samme anbefalingene: et sterkt, tilfeldig passord lagret på et fysisk medium.



![Image](assets/fr/25.webp)



Deretter kan du aktivere biometrisk autentisering hvis du ønsker det, slik at du slipper å taste inn hovedpassordet manuelt hver gang du låser opp mobilen.



![Image](assets/fr/26.webp)



Skriv inn hovedpassordet ditt på nytt, og klikk deretter på knappen `Fortsett`.



![Image](assets/fr/27.webp)



Velg alternativet "Last inn et hvelv", klikk deretter på "Skann QR-kode" og skann QR-koden for invitasjonen som vises av PearPass på kildemaskinen (datamaskinen).



![Image](assets/fr/28.webp)



Hvelvene dine på datamaskinen og mobilen er nå synkronisert. Alle ID-er som legges til på den ene enheten, lagres og kopieres sikkert på den andre.



![Image](assets/fr/29.webp)



På mobil kan du også, om du ønsker, aktivere automatisk utfylling av felt. For å gjøre dette, gå til `Settings > Advanced`, og klikk deretter på knappen `Set as Default` i seksjonen `Autofill`.



![Image](assets/fr/30.webp)



## Hvordan synkroniserer jeg PearPass med nettleserutvidelsen?



Det er allerede veldig praktisk å ha en passordadministrator som er synkronisert mellom datamaskinen og smarttelefonen, men det er enda mer praktisk å integrere den direkte i nettleseren din. For å gjøre det, begynner du med å [legge til den offisielle PearPass-utvidelsen i nettleseren] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Fra PearPass-programvaren som er installert på din lokale maskin, går du til `Innstillinger > Avansert`, og aktiverer deretter alternativet `Aktiver nettleserutvidelse`.



![Image](assets/fr/32.webp)



PearPass genererer en token sammenkoblingsfil. Kopier den.



![Image](assets/fr/33.webp)



Åpne deretter PearPass-utvidelsen i nettleseren din, lim inn token-paringen, og klikk på `Verify`-knappen, etterfulgt av `Complete`.



![Image](assets/fr/34.webp)



Passordbehandleren din er nå synkronisert med nettleserutvidelsen.



![Image](assets/fr/35.webp)



Nå kan du enkelt koble deg til ulike nettkontoer.



![Image](assets/fr/36.webp)



Nå vet du hvordan du bruker PearPass passordbehandling. Utover dette verktøyet avhenger den daglige digitale sikkerheten av riktig bruk av passende løsninger. Hvis du ønsker å lære hvordan du setter opp et sikkert, stabilt og effektivt personlig digitalt miljø, inviterer jeg deg til å ta del i opplæringskurset vårt om dette emnet:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1