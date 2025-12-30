---
name: Matrise
description: En veiledning i hvordan du forstår, konfigurerer og bruker Matrix, den sikre, åpne og desentraliserte kommunikasjonsplattformen.
---

![cover](assets/cover.webp)



## Hva er Matrix?



Matrix er en **desentralisert kommunikasjonsprotokoll** som er utviklet for å muliggjøre utveksling av meldinger, filer og lyd-/videosamtaler mellom brukere og applikasjoner, uten å være avhengig av en sentral bedrift. I motsetning til tradisjonelle meldingsplattformer er Matrix en **åpen infrastruktur**, som kan sammenlignes med e-post: Hvem som helst kan velge en server eller drifte en selv, samtidig som de beholder muligheten til å utveksle med resten av nettverket.



Matrix kjennetegnes av tre grunnleggende prinsipper:



### En protokoll, ikke et program



Matrix er ikke en applikasjon som WhatsApp eller Telegram.


Det er et standardisert språk som mange applikasjoner kan bruke.


Med andre ord gir en lang rekke Element-programvare, FluffyChat, Cinny, Nheko og andre, tilgang til det samme Matrix-nettverket.



Dette garanterer total frihet: endring av bruksområde uten tap av kontakter, mangfold av grensesnitt, uavhengighet av en enkelt leverandør.



![capture](assets/fr/03.webp)



### Et desentralisert, føderert nettverk



Matrix' struktur er basert på **federasjon**, en modell der flere uavhengige servere samarbeider med hverandre.


Hver server (kalt _homeserver_) kan være vert for brukere, chatterom og synkronisere meldinger med andre servere i nettverket.


Dermed :





- ingen enkelt enhet kontrollerer hele systemet;
- en server kan forsvinne uten at det påvirker resten av nettverket;
- hver organisasjon eller enkeltperson kan administrere sin egen plass.



Denne modellen sikrer **høy motstandskraft** og gjenspeiler verdiene i teknologisk suverenitet.



![capture](assets/fr/03.webp)



### Et sikkert, kryptert system



Matrix støtter **end-to-end-kryptering (E2EE)** for private utvekslinger og krypterte grupper.


Meldinger kan bare leses av deltakerne, ikke av mellomliggende servere.


Denne tilnærmingen gjør det mulig å kommunisere uten å eksponere innholdet i utvekslingene for en tredjepart, samtidig som man beholder protokollens åpenhet og muligheten for å hoste sin egen server.



![capture](assets/fr/05.webp)



### Unik interoperabilitet



En av Matrix' største fordeler er at den kan fungere som en **bro mellom ulike kommunikasjonssystemer**. Takket være _broer_ er det mulig å koble sammen :





- Telegram
- WhatsApp
- Signal
- Budbringer
- Slakk
- Uenighet
- IRC, XMPP osv.



Dette gjør det mulig å forene lokalsamfunn som er spredt over flere plattformer, samtidig som man beholder kontrollen over infrastrukturen.



![capture](assets/fr/06.webp)



## Hvordan fungerer Matrix?



Denne delen presenterer den interne strukturen i Matrix-nettverket for å forstå hvordan brukere, servere og applikasjoner samhandler i dette desentraliserte økosystemet. Matrix er basert på tre viktige elementer: _hjemmeservere_, identiteter og _klienter_ som brukes til å kommunisere.



### Servere: hjemmeservere



Matrix kjører på uavhengige servere som kalles _homeservere_.


Hver hjemmeserver administrerer :





- brukerkontoene den er vert for,
- private samtaler og salonger som disse brukerne deltar i,
- synkronisering med andre nettverksservere.



Alle hjemmeservere som er koblet til Matrix-nettverket, utveksler automatisk meldinger og hendelser fra felles stuer. For eksempel





- en bruker som er registrert på server A, kan chatte med en bruker på server B,
- en salong kan være spredt over flere titalls servere,
- ingen har kontroll over en salong eller et samfunn som helhet.



Denne modellen er svært robust og gjør det mulig for hver enkelt organisasjon eller person å administrere sin egen infrastruktur.



### Matriseidentifikatorer



Hver bruker har en unik identifikator, kalt **MXID** (_Matrix ID_), som ser ut som en adresse:



```bash
@nomdutilisateur:serveur.xyz
```



Den består av :





- et brukernavn, innledet med **@**
- navnet på serveren som kontoen ble opprettet på, innledet med **:**



Eksempler:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Denne identifikatoren gjør det mulig å kommunisere med alle andre Matrix-brukere, uavhengig av hvilken server de kommer fra.



### Matriseklienter (applikasjoner)



For å bruke Matrix må du koble deg til et program som heter **klient Matrix**.



De mest kjente er :





- Element (nett, mobil, desktop)
- FluffyChat (mobil)
- Cinny (minimalistisk web/skrivebord)
- Nheko (skrivebord)



Disse applikasjonene er bare grensesnitt for :





- for å vise meldinger,
- sende tekst, bilder eller filer,
- bli med på eller opprette messer,
- foreta lyd-/videosamtaler.



Alle applikasjoner kommuniserer med servere via den samme standardiserte protokollen.



### Rom og private meldinger (DM)



I Matrix foregår utvekslingen i **rom** :





- et rom kan være offentlig eller privat
- den kan romme to personer eller tusenvis
- den kan deles mellom flere servere
- den har en unik identifikator som begynner med **!**



Private meldinger er ganske enkelt chatterom med to deltakere, ofte kalt **DM (Direct Messages)**.



Salongsynkroniseringen foregår i sanntid mellom de deltakende serverne, noe som sikrer en sømløs opplevelse samtidig som desentraliseringen opprettholdes.



## Hvorfor bruke Matrix?



Matrix er ikke bare et alternativ til sentraliserte meldingssystemer: Det er en teknologi som oppfyller reelle behov når det gjelder digital suverenitet, sikkerhet og interoperabilitet. Det er mange grunner til at stadig flere mennesker, bedrifter og institusjoner velger denne protokollen for å kommunisere.



### Få tilbake kontrollen over kommunikasjonen din



De fleste meldingsplattformer opererer etter en sentralisert modell: én enkelt aktør kontrollerer servere, tilgang, data og bruksregler. Denne modellen innebærer total avhengighet av leverandøren.


Matrix har en annen tilnærming.


Hvem som helst kan velge hvor kontoen deres skal ligge, eller til og med distribuere sin egen server. Ingen enhet er i posisjon til å blokkere en bruker, kreve inngripende identifikasjon eller pålegge en policyendring.


Denne arkitekturen gir autonomi tilbake til både enkeltpersoner og organisasjoner. Kommunikasjonen er ikke lenger basert på tillit til et selskap, men på en åpen, dokumentert og verifiserbar protokoll.



### Sikker, kryptert kommunikasjon



Matrix støtter ende-til-ende-kryptering for private samtaler og grupper. Denne mekanismen sikrer at bare deltakerne kan lese meldinger, selv om de går gjennom tredjepartsservere i føderasjonen.



Protokollen bruker Megolm/Olm-algoritmen, som er utviklet spesielt for å gi sterk sikkerhet i distribuerte miljøer med flere enheter.



Dette gjør det mulig å :





- beskytte sensitive samtaler,
- hindre uautorisert tilgang (selv fra vertsserveren),
- opprettholde konfidensialitet på lang sikt.



Kryptering er ikke et alternativ: det er en kjernekomponent i protokollen.



### Ikke lenger avhengig av én enkelt applikasjon



Matrix er ikke et program, men en protokoll.



Dette mangfoldet av kunder garanterer :





- et valg tilpasset individuelle behov,
- muligheten til å bruke Matrix på alle typer enheter,
- ingen avhengighet av en enkelt programvare.



Hvis en kunde er uegnet eller ikke lenger skal opprettholdes, velger du ganske enkelt en annen: kontoen fortsetter å fungere normalt.



### Føderering og sammenkobling av ulike samfunn



Føderasjon gjør det mulig for ulike servere å arbeide sammen, samtidig som de administreres uavhengig av hverandre.


Dermed :





- kan en organisasjon administrere sin egen hjemmeserver,
- enkeltpersoner kan bli med på offentlige servere,
- alle kan kommunisere med hverandre som om de befant seg på samme plattform.



Denne fleksibiliteten gjør det mulig å skape kommunikasjonsrom som er tilpasset ethvert behov: team, foreninger, lokalsamfunn, institusjoner eller open source-prosjekter.



Matrix er spesielt populær i tekniske kretser, aktivistkollektiver, forskningsmiljøer, myndigheter og i økende grad i Bitcoin-miljøer.



### Unik interoperabilitet i meldingslandskapet



En av Matrix' største fordeler er muligheten til å **utvide** børser takket være broer som kan koble sammen :





- WhatsApp
- Telegram
- Signal
- Slakk
- Uenighet
- IRC
- XMPP
- og mange andre plattformer



Matrix blir dermed et samlende lag for kommunikasjon, som samler flere miljøer som er spredt over ulike applikasjoner.



Denne interoperabiliteten reduserer fragmenteringen og forenkler samarbeidet.



### En fri, åpen og bærekraftig protokoll



Matrix-protokollen er helt åpen kildekode og åpent utviklet.


Dette gir flere fordeler:





- en kontinuerlig utvikling av standarden,
- muligheten for hvem som helst til å sjekke koden,
- uavhengighet av kommersielle eller politiske endringer,
- langsiktig motstandskraft.



I motsetning til proprietære meldingssystemer er fremtiden til Matrix ikke avhengig av et enkelt selskap, men av et globalt fellesskap og en åpen standard.



## Hvordan oppretter jeg en Matrix-konto?



Det er enkelt å opprette en Matrix-konto, og det krever ingen tekniske ferdigheter. Brukere kan bli med på en eksisterende server, opprette en innlogging og begynne å chatte umiddelbart. Denne delen beskriver de viktigste trinnene.



### Velg en server (offentlig eller privat)



Matrix er et føderert nettverk: Det finnes en rekke servere (hjemmeservere) som administreres av ulike organisasjoner, lokalsamfunn eller enkeltpersoner. Valget av server bestemmer bare _hvor_ kontoen er lagret, men forhindrer ikke kommunikasjon med hele nettverket.


**To alternativer er tilgjengelige:**



### - Bruk en offentlig server



Dette er den enkleste løsningen.


Eksempler på populære servere:





- _matrix.org_ (den mest kjente)
- _envs.net
- tematiske fellesskapsservere (teknologi, personvern, åpen kildekode ...)



Disse serverne egner seg for nybegynnere som ønsker å registrere seg raskt.



### - Bruk en privat server



Ideell for :





- en organisasjon,
- en familie,
- et prosjekt med åpen kildekode,
- et arbeidsteam,
- eller for suverent, selvdrevet bruk.



I dette tilfellet må noen administrere serveren (Synapse, Dendrite, Conduit...).


Uansett hvilken server du velger, kan brukerne snakke med hverandre takket være føderasjon.



### Opprett en konto trinn for trinn



Ettersom Matrix er en åpen protokoll, kan den brukes av flere programmer.


Som beskrevet ovenfor, tilbyr de ulike grensesnitt og funksjoner avhengig av behov:





- Element**: den mest komplette klienten, tilgjengelig på alle plattformer.
- FluffyChat**: enkel, moderne og ideell for mobiler.
- Nheko**: lett, ergonomisk klient for PC-er.
- SchildiChat**: Element-variant med ergonomiske forbedringer.
- NeoChat**: integrert i KDE-økosystemet.



Valg av klient har ingen innvirkning på kontoen: alle fungerer med alle Matrix-servere.



### Klassiske trinn :





- Åpne den valgte applikasjonen. I vårt tilfelle vil vi gjøre dette med [Element](app.element.io).
- Velg "Opprett en konto".



![cover-kali](assets/fr/10.webp)



For enkelhets skyld kan du opprette en Matrix-konto ved hjelp av **Google, Facebook, Apple, GitHub eller GitLab**. Disse tjenestene vil bare vite at kontoen deres har blitt brukt til å få tilgang til Matrix: dette kalles en **social connection**.



For større konfidensialitet kan du også registrere deg manuelt ved å velge et **brukernavn**, et **passord** og en **e-postadresse**.



Avhengig av hvilken server du velger, kan det være nødvendig med en **captcha**, samt at du godtar **bruksvilkårene**.



Når registreringen er validert, sendes en bekreftelse via e-post.


Bare klikk på lenken for å aktivere kontoen din og få tilgang til webapplikasjonen (Element) for å delta i dine første Matrix-samtaler.



![cover-kali](assets/fr/11.webp)



Du har nå en konto og bruker nettversjonen av Element.



## Legg til din første kontakt



For å kommunisere med noen på Matrix trenger du bare å vite deres fulle identifikator, kalt **Matrix ID**.



Eksempel:



`@alice:matrix.org @bened:monserveur.bj`



### Legg til en kontakt



For å invitere venner til gruppechatten klikker du på `i`-sirkelen øverst i høyre hjørne. Dette åpner panelet til høyre. Klikk på "People" for å vise listen over medlemmer i dette rommet: dere bør være de eneste som er til stede for øyeblikket.



![cover-kali](assets/fr/12.webp)



Klikk på "Inviter til dette rommet" øverst i personlisten, og du får opp en melding der du kan invitere vennene dine til å bli med deg i Matrix. Hvis de allerede er logget inn i Matrix, skriver du inn Matrix-ID-en deres. Hvis de ikke er det, skriver du inn e-postadressen deres, så blir de invitert til å bli med oss.



Det finnes ikke noe "venn"-system: En kontakt er ganske enkelt en person som det er åpnet en samtale med.



![cover-kali](assets/fr/13.webp)



Personen du har invitert, kan enten takke ja eller nei til invitasjonen. Hvis de takker ja, bør du se at de blir med i rommet. Jo flere, jo bedre!



![cover-kali](assets/fr/14.webp)



### Sette opp din egen server



Matrix kommer virkelig til sin rett når den brukes sammen med en personlig server.


Ved å distribuere din egen hjemmeserver kan du :





- opprettholde full kontroll over dataene,
- definere sine egne regler for bruk,
- være vert for flere kontoer (venner, team, fellesskap),
- og sikre maksimal motstandskraft i tilfelle restriksjoner eller sensur.



**Tilgjengelige løsninger:**





- Synapse**: den historiske og mest komplette implementeringen.
- Dendrite**: lettere, kraftigere og designet for fremtidens protokoll.
- Conduit**: en minimalistisk variant som er enkel å distribuere.



**Forkunnskaper:**





- et domenenavn,
- en maskin eller en VPS,
- minimum ferdigheter i systemadministrasjon.



Selv om det krever litt konfigurasjon, blir Matrix et suverent og holdbart verktøy når du administrerer din egen server.



### Bli med på dine første messer



Matrix er i stor grad avhengig av _rom_ (stuer).


Det finnes offentlige, private, kommunale, tekniske, lokale og internasjonale messer.



**Tre måter å bli med i en salong på



1. **Via en invitasjonslenke** (ofte i form av en `matrix.to`-URL).


2. **Søker etter salongnavnet** i applikasjonen.


3. **Ved å skrive inn hele program-ID-en**, f.eks:


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Når du har blitt medlem, oppfører chatterommet seg som en klassisk nyhetsgruppe, med historikk, kryptering, filer, reaksjoner og lyd-/videosamtaler, avhengig av hvilken klient som brukes.



![capture](assets/fr/09.webp)



## Å gå videre



Når du har lært deg det grunnleggende, byr Matrix på en rekke avanserte muligheter. Enten du vil koble til andre meldingssystemer, være vert for din egen server eller organisere et fellesskap, er økosystemet svært innholdsrikt.



### Broer (WhatsApp, Telegram, Signal osv.)



En bro kobler Matrix til andre meldingssystemer.


Med den kan du sende og motta meldinger fra :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Uenighet
- Slakk**
- IRC** (IRC)
- og mange andre



### Hva broer kan gjøre





- Sentraliser alle samtalene dine i Matrix
- Tilby et åpent grensesnitt for samhandling med proprietære tjenester
- Administrer et fellesskap med flere plattformer fra ett sted



Noen broer er offisielle, andre er samfunnsbaserte.


Avhengig av avdelingen kan de kreve :





- en personlig server,
- en ekstra konfigurasjon,
- eller bruk av en eksisterende offentlig bro.



### Bruk av Matrix for en Bitcoin-organisasjon, et lokalsamfunn eller et prosjekt



Matrix er ikke bare et personlig verktøy.


Den kan brukes til å strukturere arbeidsgrupper, organisere lokalsamfunn eller administrere prosjektkommunikasjon.



**Eksempler på bruk:**





- Fellesskap med åpen kildekode
- Bitcoin og Lightning-økosystemprosjekter
- Student- eller utviklergrupper
- Innbyggerorganisasjoner
- Uavhengige medier
- Lokale grupper og foreninger



**Hvorfor er dette interessant?





- 100 % åpen kildekode**-verktøy
- Suveren og desentralisert** kommunikasjon
- Områdene er organisert i **lounger**, **undergrupper**, **private lounger** osv.
- Integrer med Nextcloud, GitLab, Mattermost eller tilpassede roboter
- Finjustert administrasjon av tillatelser og moderering



Matrix blir da en kommunikasjonssøyle for alle strukturer som ønsker å være uavhengige av de store sentraliserte plattformene.



## Konklusjon



Matrix representerer en moderne, åpen og sikker løsning for sanntidskommunikasjon, og tilbyr et desentralisert alternativ til tradisjonelle plattformer. Takket være den fødererte arkitekturen og avanserte krypteringsprotokoller kan brukerne beholde kontrollen over dataene sine, samtidig som de får en flytende og interoperabel opplevelse. Enten det gjelder personlig, profesjonell eller felles bruk, tilbyr Matrix et robust og skalerbart rammeverk for å bygge kommunikasjonsmiljøer som er tilpasset dagens behov.



Hvis du vil vite mer og oppdage alle funksjonene som Matrix tilbyr, kan du lese den offisielle dokumentasjonen som er tilgjengelig her :


[https://matrix.org/docs/](https://matrix.org/docs/)