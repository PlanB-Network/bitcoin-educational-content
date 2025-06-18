---
name: Enkel innlogging
description: Identitet beskyttet med alias
---
![cover](assets/cover.webp)

## Innlogging = e-post = tap av personvern


I den digitale verden er det blitt vanlig å ha en konto for alle plattformer man ønsker tilgang til.

Hver av disse tjenestene krever en innlogging, som vanligvis er knyttet til paret _brukernavn_ og _passord_. Brukernavnet er ofte brukerens personlige e-postadresse.


Når man bruker sin personlige e-post Address for hver innlogging, er det lett å forestille seg den første konsekvensen: tap av konfidensialitet, noe som blir stort hvis Address består av _name.surname@serviceemail.com_.


Utviklere av åpen kildekode-verktøy har laget en rekke applikasjonssuiter, nettopp for å få brukerne til å få tilbake litt av personvernet: De vil fortsatt logge inn, men ved hjelp av et alias i stedet for verktøyet som avslører deres private identitet.


Den enkleste av dem jeg personlig har prøvd og fortsatt tester, er [Simple Login] (https://simplelogin.io/).


## Alias


Et e-postalias erstatter ganske enkelt _navn.etternavn_-delen av e-postadressen din Address med et fiktivt navn. For brukeren endres ingenting; alias-tjenesten videresender e-poster til og fra den vanlige Address-en som normalt. Alle kan fortsette å bruke innboksen sin som vanlig, men i stedet for å vise det virkelige navnet sitt, vil den vise en ugjenkjennelig bruker. Denne tjenesten må være effektiv, og så langt har Simple Login vist seg å være nettopp det.


Når du besøker Simple Login-siden for første gang, må du opprette en konto (også her!) ved hjelp av den "offisielle" e-posten Address. Her må du oppgi e-postadressen, et passord og løse en captcha.


![image](assets/it/02.webp)


Enkel innlogging sender en bekreftelsesmelding til den angitte e-posten Address. I stedet for å klikke på bekreftelsesknappen, anbefales det å kopiere lenken og lime den inn i Address-linjen.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Dashbordet for enkel pålogging åpnes umiddelbart, med en kort veiledning for navigering.


![image](assets/it/05.webp)


Det bør bemerkes at Simple Login automatisk aktiverer abonnementet på nyhetsbrevet, som kan deaktiveres fra den aktuelle kommandoen.


![image](assets/it/06.webp)


## Innstillinger


Du kan ta en titt på _Innstillinger_ med en gang for å oppdage funksjonene i tjenesten. Enkel innlogging starter med alle alternativene aktive, inkludert _Premium_, som forblir brukbare i 10 dager. Når prøveperioden er over, har du muligheten til å opprette 10 alias med denne profilen, og du kan koble Proton-e-posten din direkte, ettersom Simple Login har blitt kjøpt opp av den sveitsiske e-postleverandøren.


![image](assets/it/07.webp)


Du kan angi en rekke parametere, eller sjekke om e-posten din allerede har blitt kompromittert når det gjelder personvern.


![image](assets/it/08.webp)


Til slutt kan du eksportere en sikkerhetskopi av profilen din, eller importere en fra en annen leverandør.


![image](assets/it/09.webp)


### Jobb e-post


De som bruker e-post med et personlig domene som jobb-e-post, kan sette opp sitt eget private domene.


![image](assets/it/10.webp)


Fra hovedpanelet, ved å velge _Mailboxes_, er det til og med mulig å legge til andre e-postadresser og også bruke aliasene som vil bli opprettet tilsvarende. I denne opplæringen bestemte jeg meg for eksempel for å opprette profilen med en _gmail.com_-postkasse, og deretter knytte til en _proton.me_ Address.


![image](assets/it/11.webp)


Hvis du legger til en ny Address, spesielt hvis den tilhører Proton-leverandøren, viser den guidede prosedyren muligheten til å gå inn i _sudo_-modus, superbruker. Enkel innlogging vil be om å oppgi passordet til denne postkassen, for å bevise legitim Ownership.


⚠️ **Jeg fraråder deg personlig å gjøre dette**. ⚠️


![image](assets/it/12.webp)


**Det er bedre å få tilgang til e-postboksen -> kopier lenken for bekreftelse og lim den inn i URL-linjen -> og få bekreftelsen uten å avsløre passordet


![image](assets/it/13.webp)


Av de to adressene som legges inn, blir den ene standard og den andre sekundær, men de kan enkelt byttes, og innstillingen er lett å identifisere i dashbordet.


![image](assets/it/14.webp)


Etter å ha lagt til en ekstra e-post Address (valgfritt), la oss se hva vi kan gjøre med Simple Login.


## Opprettelse av alias


I panelet er det første menyalternativet merket _Alias_, og det er her du kan opprette dem. Du har muligheten til å generate aliaser tilfeldig ved å klikke på Random Alias-knappen, som er Green-knappen som vises på neste bilde. Denne funksjonen skaper en unik og spennende e-post Address.


![image](assets/it/24.webp)


Hvis du derimot ønsker å differensiere tjenester ved å gi dem ulike navn, må du velge _Nytt egendefinert alias_. Da kan du gi aliaset navnet på tjenesten du vil ha tilgang til (sosiale medier, tjenesteleverandører, nettbegivenheter, fremmede du har møtt ved en tilfeldighet osv.) Resten håndteres av Simple Login.

For moro skyld (men egentlig ikke, for å være ærlig) bestemte jeg meg for å lage et alias for banken og kalte det `BANK`. Selv om det er sant at banken min vet alt om meg, synes jeg det er morsomt å kommunisere med dem ved hjelp av en e-post Address som er uforståelig for dem. Simple Login genererer faktisk et tilfeldig navn, som er atskilt fra det vi velger med en `.`


Her kan den nye e-posten Address bli:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- og så videre


Man kan velge mer enn ett domene: offentlige domener er tilgjengelige med gratisabonnementet, mens andre, angitt som private (inkludert _@simplelogin.com_), utvider valgmulighetene for brukere som bestemmer seg for å abonnere på et betalingsabonnement.


![image](assets/it/15.webp)


Når det tilfeldige suffikset og domenet er valgt, kan du angi om denne nye (og bisarre) Address skal fungere som et alias for bare én av de personlige e-postboksene, eller for alle. Aliaset blir klart og aktivt etter at du har klikket på _Create_


![image](assets/it/16.webp)


Den nye e-posten Address ble opprettet, og den er nå synlig, klar til å sendes (til banken!) bare ved å kopiere den.


![image](assets/it/18.webp)


Nå kan du fokusere på å opprette et alias for hver tjeneste eller plattform du vil ha tilgang til, og der e-post er en viktig parameter for å opprette en konto.


![image](assets/it/19.webp)


For personvernentusiaster finnes det også en mulighet til å generate en e-post Address basert på UUID-protokollen (ikke på identifiserbare navn), som skaper en unik 128-biters identifikator som ikke kontrolleres av sentraliserte parter. Denne funksjonen, som er nyttig for sensitive kontoer, finner du i menyen _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Som du ser, er dette en e-post Address som krever riktig håndtering.


Hvis du ombestemmer deg og ikke lenger ønsker å bruke et alias, klikker du bare på kommandoen _More_ for hvert enkelt alias og velger _Delete_.


![image](assets/it/23.webp)


## Alias-administrasjon


Det er enkelt å opprette alias, og det er også enkelt å administrere dem, noe som bare krever litt omtanke og disiplin. All trafikk vil faktisk fortsatt gå gjennom e-postinnboksen som vi i begynnelsen har definert som den offisielle innboksen. Varsler og viktig kommunikasjon fra plattformer vil fortsette å ankomme Gmail, Proton eller hva enn e-postleverandøren er.


Resultatet er imidlertid at vi har bevart den viktigste Address som vi, fra det øyeblikket vi oppretter aliasene, står fritt til å bestemme hvem vi skal avsløre det for og hvem ikke.


Et alias fungerer både for mottak og sending: En annen bruker vil faktisk motta svaret fra alias.preoccupy789@8shield.net, hvis dette er pseudonymet som er valgt for den aktuelle mottakeren.


## Fordeler


Alt i alt er det å bruke alias en effektiv måte å beskytte identiteten og personvernet ditt på. E-postadresser samles ofte inn av datameglere og nettsteder for å spore brukervaner og -atferd. Selv om et alias ikke gjør deg helt umulig å spore, er konsekvent bruk av et alias et positivt skritt i retning av å beskytte informasjonen din. I vår "globale digitale landsby", der hacking, datasalg og sikkerhetsbrudd er altfor vanlig, er det dessuten høyst sannsynlig at e-postadressen du bruker til å registrere deg på ulike nettsteder, allerede har blitt kompromittert eller utsatt for angrep.


Et unikt pseudonym, som brukes for hver innlogging, **gjør det umiddelbart mulig for oss å forstå hvilken plattform som sender spam (eller verre) til postkassen vår, fordi e-posten er identifisert av aliaset som er knyttet til den**. Du har ingen anelse om hvor mye spam og phishing som kommer fra såkalte pålitelige kanaler, fordi de er institusjonelle, før du begynner å bruke et alias for banker, et for posttjenester eller et spesifikt for noen obligatoriske offentlige tjenester. Når avsenderen av søppelposten (eller det som verre er) er identifisert, vil du vite at nettstedet har blitt kompromittert, og ta alle forholdsregler for å beskytte alle dataene som er gitt (tenk på kredittkort!) til det spesifikke nettstedet, som kan innse bruddet uker senere.


Når det gjelder Simple Login, har dette verktøyet følgende funksjoner:



- mobilapp (også fra F-Droid) og nettleserutvidelse, for å administrere aliaser i alle situasjoner;
- tofaktorautentisering for hvert nye pseudonym, noe som øker graden av uavhengighet fra selve tjenesten;
- PGP-støtte (for _Premium-brukere);
- enkel oppretting av alle typer alias (egendefinerte, tilfeldige og UUID);
- blant de gratis planene i sektoren, muligheten til å bruke aliaser med flere "offisielle" e-postbokser. Andre konkurrenter begrenser seg til bare én.


## Ulemper


- 10 aliaser er kanskje ikke nok hvis du planlegger å bruke Simple Login i utstrakt grad. I dette tilfellet er det nyttig å kjøpe den rimelige betalingsplanen for å øke antallet tilgjengelige aliaser.
- Det er ikke mulig å opprette et alias med et bestemt navn og domene. Det tilfeldige suffikset som legges til etter et navn valgt av oss, genererer en Address som i beste fall kan beskrives som bisarr. Tradisjonelle sosiale medier nekter vanligvis å gi tilgang til kontoer som er opprettet med denne typen e-postadresser. Nostr fikser dette!
- Hvis du bruker et alias for å sende en melding til noen, er det lett å havne i mottakerens søppelpostmappe. Som et første skritt anbefales det å bruke pseudonymet for å motta, akkurat som når du oppretter en konto, abonnerer på en e-postliste osv.