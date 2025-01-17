---
name: COLDCARD Q - Avansert
description: Bruke COLDCARD Qs avanserte alternativer
---
![cover](assets/cover.webp)

I en tidligere veiledning gjennomgikk vi den første konfigurasjonen av COLDCARD Q og de grunnleggende funksjonene for nybegynnere. Hvis du nettopp har mottatt COLDCARD Q og ikke har konfigurert det ennå, anbefaler jeg at du starter med den veiledningen før du fortsetter her:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Denne nye veiledningen er dedikert til COLDCARD Qs avanserte alternativer, designet for avanserte og paranoide brukere. COLDCARDs skiller seg faktisk fra andre maskinvarelommebøker ved sine mange avanserte sikkerhetsfunksjoner. Du trenger selvfølgelig ikke å bruke alle disse alternativene. Bare velg de som passer din sikkerhetsstrategi.

**Advarsel**, feil bruk av noen av disse avanserte alternativene kan føre til tap av bitcoins eller ødeleggelse av maskinvarelommeboken din. Jeg anbefaler derfor på det sterkeste at du leser rådene og forklaringene for hvert alternativ nøye.

Før du begynner, må du sørge for at du har tilgang til en fysisk sikkerhetskopi av minnefrasen på 12 eller 24 ord, og sjekke gyldigheten via følgende meny: avansert/Verktøy > Faresone > Frøfunksjoner > Vis frøord.

![CCQ](assets/fr/01.webp)

## BIP39-passordet

Hvis du ikke vet hva en BIP39-passordfrase er, eller hvis det ikke er helt klart for deg hvordan den fungerer, anbefaler jeg på det sterkeste at du tar en titt på denne veiledningen på forhånd, som dekker det teoretiske grunnlaget som trengs for å forstå risikoen forbundet med å bruke en passordfrase :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Husk at når du har satt opp passordfrasen i lommeboken din, vil ikke huskeregelen alene være nok til å få tilgang til bitcoinsene dine igjen. Du trenger både huskeregelen og passordfrasen. I tillegg må du oppgi passordfrasen hver gang du låser opp COLDCARD Q. Dette øker sikkerheten ved å gjøre fysisk tilgang til COLDCARD og kjennskap til PIN-koden utilstrekkelig uten passordfrasen.

På COLDCARDs har du to alternativer for å administrere passordfrasen din:

1. **Klassisk inntasting:** Du taster inn passordfrasen manuelt hver gang du bruker maskinvarelommeboken, akkurat som du gjør med andre maskinvarelommebøker. COLDCARD Q forenkler denne oppgaven med sitt komplette tastatur.

2. **Du kan velge å kryptere passordfrasen og lagre den på et microSD-kort. I så fall må du sette microSD-kortet inn i COLDCARD Q hver gang du bruker det. Vær oppmerksom på at dette microSD-kortet bare fungerer på COLDCARD Q og ikke er en sikkerhetskopi. Det er derfor svært viktig at du også oppbevarer en kopi av passordfrasen din på et fysisk medium, for eksempel papir eller metall.

For å angi passordfrasen for BIP39 går du til menyen "*Passphrase*".

![CCQ](assets/fr/02.webp)

Skriv inn passordfrasen din ved hjelp av tastaturet. Sørg for å velge en sterk passordfrase (lang og tilfeldig), og ta en fysisk sikkerhetskopi.

![CCQ](assets/fr/03.webp)

Når du har angitt passordfrasen, vil COLDCARD Q vise deg hovednøkkelfingeravtrykket til den nye lommeboken som er knyttet til denne passordfrasen. Husk å lagre dette fingeravtrykket. Når du skriver inn passordfrasen på nytt når du bruker enheten i fremtiden, kan du kontrollere at fingeravtrykket som vises, stemmer overens med det du lagret. Denne kontrollen sikrer at du ikke har gjort en feil da du skrev inn passordfrasen.

![CCQ](assets/fr/04.webp)

Du kan nå trykke på "*ENTER*" for å bruke denne passordfrasen til minnefrasen din og aktivere den nye lommeboken. Hvis du foretrekker å lagre denne passordfrasen på et microSD-kort, setter du kortet i riktig spor og trykker på "*1*".

![CCQ](assets/fr/05.webp)

Passordfrasen din er nå brukt. Nøkkelavtrykket vises på startskjermen og øverst på skjermen.

![CCQ](assets/fr/06.webp)

Hver gang du låser opp COLDCARD Q, må du gå til "*Passphrase*"-menyen og skrive inn passordfrasen din på samme måte som ovenfor, for å bruke den på mnemonikken som er lagret i enheten og få tilgang til riktig Bitcoin-lommebok.

![CCQ](assets/fr/07.webp)

Hvis du har lagret passordfrasen på et microSD-kort, setter du det inn i COLDCARD hver gang du bruker det, og åpner menyen "*Passphrase*". COLDCARD vil laste inn passordfrasen direkte fra microSD-kortet, slik at du ikke trenger å skrive den inn manuelt. Klikk på "*Restore Saved*".

![CCQ](assets/fr/08.webp)

Kontroller at lengden og den første bokstaven i den innlastede passordfrasen er riktig.

![CCQ](assets/fr/09.webp)

Bekreft at fingeravtrykket som vises, stemmer overens med lommeboken din, og klikk på "*Restore*".

![CCQ](assets/fr/10.webp)

Husk at bruk av en passordfrase betyr at du må importere et nytt sett med nøkler som er avledet fra kombinasjonen av den mnemoniske frasen og passordfrasen i lommebokadministrasjonsprogramvaren din (som Sparrow Wallet). For å gjøre dette, følg trinnet "*Konfigurer en ny lommebok på Sparrow*" i denne andre veiledningen :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Låser opp alternativer

COLDCARDs drar også nytte av en rekke alternativer for opplåsingsprosessen. La oss finne ut mer om disse avanserte alternativene.

### Lure PIN-koder

En Trick PIN-kode er en sekundær PIN-kode som er forskjellig fra den som ble definert under den første konfigurasjonen av enheten. Denne koden brukes til å utløse bestemte forhåndskonfigurerte handlinger så snart den tastes inn når COLDCARD slås på. Du kan konfigurere flere Trick PIN-koder, hver knyttet til en annen handling. Disse funksjonene gjør at du kan skreddersy COLDCARD til din personlige sikkerhetsstrategi. De er spesielt nyttige i tilfeller av fysisk tvang, for eksempel under et ran (ofte referert til i Bitcoin-miljøet som et "*$5 wrench attack*").

Du aktiverer en Trick PIN-kode og knytter den til en handling ved å gå til menyen `Innstillinger > Påloggingsinnstillinger > Trick PIN-koder`.

![CCQ](assets/fr/11.webp)

Velg "*Legg til nytt triks*".

![CCQ](assets/fr/12.webp)

Angi PIN-koden som skal knyttes til handlingen, og husk å lagre den.

![CCQ](assets/fr/13.webp)

Velg deretter handlingen som skal utføres automatisk hver gang du taster inn denne Trick PIN-koden. Her er listen over handlinger som er tilgjengelige for en PIN-kode:


- "*Brick Self*: Denne handlingen ødelegger begge COLDCARD Q-brikkene hvis Trick PIN-koden tastes inn, noe som gjør enheten helt ubrukelig. Det vil da være umulig å videreselge, gjenbruke eller returnere den til Coinkite. Enheten blir ugjenkallelig foreldet. Denne funksjonen kan brukes i tilfelle ran for å overbevise en overfallsmann om at han aldri vil kunne få tilgang til bitcoinsene dine. **Merk**: Uten en fysisk sikkerhetskopi av minnefrasen og en eventuell passordfrase, vil bitcoinsene dine gå tapt for alltid.

![CCQ](assets/fr/14.webp)


- "*Wipe Seed*": Denne menyen tilbyr flere handlinger for å slette seed, dvs. tilbakestille COLDCARD uten å ødelegge det. I motsetning til alternativet "*Brick Self*" vil det være mulig å konfigurere enheten på nytt ved hjelp av en sikkerhetskopi av minnefrasen din. Uten denne sikkerhetskopien vil imidlertid bitcoinsene dine gå tapt. Her er de tilgjengelige alternativene:
 - "*Wipe & Reboot* : Fjerner frøet og starter COLDCARD på nytt uten å vise noen informasjon på skjermen.
 - "*Silent Wipe*": Tørker frøet lydløst, og låser opp COLDCARD på en tilfeldig falsk lommebok som om ingenting hadde skjedd.
 - "*Wipe -> Wallet*": Fjerner seed diskret og låser opp COLDCARD på en forhåndskonfigurert sekundær lommebok, utformet som et lokkemiddel. Denne lommeboken kan inneholde en liten del av bitcoin-sparingen din for å tilfredsstille en angriper.
 - "*Say Wiped, Stop*": Sletter frøet og viser meldingen "Frøet er slettet, stopp" på skjermen.

![CCQ](assets/fr/15.webp)


- "*Trygdlommebok*": Med denne handlingen låser Trick PIN-koden opp en lommebok som er avledet fra seed ved hjelp av BIP85. Denne sekundære lommeboken kan brukes som agn for å tilfredsstille en angriper. COLDCARD fungerer som om det var den ekte lommeboken, men uten hoved-PIN-koden (som er forskjellig fra Trick PIN-koden), vil angriperen aldri få tilgang til den ekte lommeboken. Denne strategien er utformet for å få folk til å tro at lommeboken som er knyttet til Trick PIN-koden, er den eneste som finnes.

![CCQ](assets/fr/16.webp)


- "*Nedtelling ved innlogging*": Denne menyen grupperer handlinger med en nedtelling før de utføres. **Noen av dem kan ødelegge enheten din eller føre til tap av bitcoins. Her er de tilgjengelige underhandlingene:
 - "*Wipe & Countdown* : Sletter seed fra minnet på COLDCARD, og starter deretter en nedtelling på én time. Hvis du ikke lagrer mnemonikken eller passordfrasen din, vil bitcoinsene dine gå tapt. Dette alternativet er utformet for å lure en angriper til å tro at enheten vil låses opp ved slutten av nedtellingen, mens den i virkeligheten vil tilbakestilles til fabrikkinnstillingene.
 - "*Nedtelling og murstein*": Starter en nedtelling på én time, og på slutten av nedtellingen ødelegger COLDCARD sine to sikkerhetsbrikker, noe som gjør det permanent ubrukelig. Uten backup vil bitcoinsene dine gå tapt. Denne handlingen er utformet for å lure en angriper, som tror at han venter på en opplåsing, mens enheten i virkeligheten vil selvdestruere.
 - "*Just Countdown* : Utløser en enkel nedtelling på én time, hvoretter COLDCARD starter på nytt uten ytterligere tiltak. Frøet slettes ikke, og enheten forblir intakt. Vær forsiktig så du ikke forveksler denne handlingen med alternativet "*Login Countdown*", som omtales i de følgende avsnittene, og som legger til en nedtelling til hoved-PIN-koden samtidig som det gir tilgang til den virkelige lommeboken.

![CCQ](assets/fr/17.webp)


- "*Look Blank*": Denne handlingen får COLDCARD til å se tomt ut, noe som gir inntrykk av at frøet er slettet. I virkeligheten skjer det ingenting, og frøet forblir intakt. Dette simulerer et ubrukt eller tilbakestilt COLDCARD.

![CCQ](assets/fr/18.webp)


- "*Just Reboot* : Når Trick PIN-koden brukes, starter COLDCARD ganske enkelt på nytt. Ingen andre handlinger utføres.

![CCQ](assets/fr/19.webp)


- "*Delta-modus*": Denne komplekse handlingen, som er forbeholdt erfarne brukere, er utformet for å motvirke svært sofistikerte tvangsangrep, enten det kommer fra en stat eller en slektning med privilegert informasjon. Når Delta-modus er aktivert, gir COLDCARD tilgang til den virkelige lommeboken, slik at en angriper kan navigere og kontrollere at det er den riktige lommeboken. Transaksjonssignaturer blokkeres imidlertid, noe som forhindrer enhver bitcoinoverføring. I tillegg er tilgangen til minnefrasen deaktivert, og ethvert forsøk på å hente den vil føre til at den slettes. For å øke troverdigheten må Trick PIN-koden som brukes med Delta-modus ha samme prefiks som den ekte PIN-koden (for å vise de samme anti-phishing-ordene), men suffikset må være forskjellig.

![CCQ](assets/fr/20.webp)

Når du har valgt en handling, bekrefter du valget.

![CCQ](assets/fr/21.webp)

Du kan deretter se alle konfigurerte Trick PIN-koder i den dedikerte menyen.

![CCQ](assets/fr/22.webp)

Ved å velge en eksisterende Trick PIN-kode kan du sjekke den tilhørende handlingen. Du kan også skjule den med "*Hide Trick*", slik at den blir usynlig i Trick PIN-menyen. Du kan slette den ved å klikke på "*Delete Trick*", eller du kan endre PIN-koden samtidig som du beholder den tilknyttede handlingen ved å klikke på "*Change PIN*".

![CCQ](assets/fr/23.webp)

Med alternativet "*Add If Wrong*", som er tilgjengelig i menyen "*Trick PIN*", kan du konfigurere en spesifikk handling som utløses automatisk etter et visst antall feilaktige forsøk på å taste inn master-PIN-koden. Antall tillatte forsøk kan stilles inn under konfigurasjonen.

### Scramble-nøkler

Med alternativet Scramble Keys kan du forvrenge sifrene som vises på tastaturknappene når du taster inn PIN-koden. Denne funksjonen beskytter PIN-koden din, selv om den skulle bli overvåket av personer eller kameraer.

Du aktiverer dette alternativet ved å gå til menyen `Innstillinger > Påloggingsinnstillinger > Scramble Keys`.

![CCQ](assets/fr/24.webp)

Velg alternativet "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Når du låser opp COLDCARD Q, vil tastene på tastaturet fra nå av bli tildelt nye numre tilfeldig hver gang du bruker dem.

![CCQ](assets/fr/26.webp)

### Nedtelling for innlogging

Med dette alternativet kan du innføre en systematisk nedtelling hver gang du forsøker å låse opp COLDCARD. Det kan integreres i sikkerhetsstrategien din ved å forsinke tilgangen til enheten i tilfelle tyveri, eller ved å innføre en forsinkelse før du signerer en transaksjon, for eksempel for å beskytte deg selv i tilfelle et ran. Denne nedtellingen gjelder imidlertid for all bruk, inkludert når du bruker COLDCARD på lovlig vis, noe som også forplikter deg til å være tålmodig. Vær forsiktig så du ikke forveksler dette alternativet med "*Just Countdown*"-handlingen, som bare aktiveres når en bestemt Trick PIN-kode brukes.

Du konfigurerer dette alternativet ved å gå til menyen `Innstillinger > Påloggingsinnstillinger > Påloggingsnedtelling`.

![CCQ](assets/fr/27.webp)

Velg nedtellingstid. Hvis du for eksempel velger 1 time, må du vente 1 time for hvert forsøk på å låse opp COLDCARD Q.

![CCQ](assets/fr/28.webp)

Hver gang du låser opp, blir du bedt om å taste inn PIN-koden din.

![CCQ](assets/fr/29.webp)

Vent deretter på tiden som er angitt av nedtellingen.

![CCQ](assets/fr/30.webp)

Når nedtellingen er over, må du taste inn PIN-koden på nytt for å få tilgang til enheten.

![CCQ](assets/fr/31.webp)

### Pålogging til kalkulator

Med dette alternativet kan du skjule COLDCARD som en kalkulator når du låser opp. Du aktiverer denne funksjonen ved å gå til menyen `Innstillinger > Innloggingsinnstillinger > Kalkulatorinnlogging`.

![CCQ](assets/fr/32.webp)

Aktiver alternativet ved å velge det.

![CCQ](assets/fr/33.webp)

Fra nå av vises en fungerende kalkulator med grunnleggende kommandoer hver gang enheten slås på.

![CCQ](assets/fr/34.webp)

Du kan for eksempel beregne SHA256-hashingen av "*Plan B Network*".

![CCQ](assets/fr/35.webp)

For å låse opp COLDCARD fra kalkulatormodus, begynner du med å taste inn PIN-koden din etterfulgt av en bindestrek. Hvis PIN-koden din for eksempel er `00-00` (denne koden er svak og bare et eksempel, så velg en sterk PIN-kode), skriver du inn `00-`. COLDCARD vil da vise dine to anti-phishing-ord.

![CCQ](assets/fr/36.webp)

Skriv deretter inn hele PIN-koden din, atskilt med et mellomrom eller en tankestrek, for eksempel: `00 00`.

![CCQ](assets/fr/37.webp)

COLDCARD går da ut av kalkulatormodus og låses opp som normalt.

## Ødelegge COLDCARD på en ren måte

Hvis du planlegger å kvitte deg med COLDCARD Q, for eksempel fordi du nå bruker en annen maskinvarelommebok, er det viktig å destruere enheten på riktig måte. Dette sikrer at ingen informasjon knyttet til lommeboken din kan gjenopprettes av en tredjepart.

Det finnes tre nivåer av informasjonsødeleggelse, avhengig av dine behov. Før du begynner, må du sørge for at lommeboken din har blitt importert til en annen maskinvarelommebok, at du har tilgang til alle pengene dine og, fremfor alt, at du har din mnemoniske frase og en eventuell passordfrase, som begge er funksjonelle. Uten en sikkerhetskopi av lommeboken vil ødeleggelsen av COLDCARD føre til tap av bitcoins.

Det første nivået av ødeleggelse består av å slette bare frøet. Dette alternativet sletter minnefrasen fra COLDCARDs minne, samtidig som enheten forblir funksjonell. Det er ideelt hvis du ønsker å bruke COLDCARD Q igjen på et senere tidspunkt. For å slette frøet fra minnet, går du til menyen `Avansert/Verktøy > Faresone > Frøfunksjoner > Ødelegg frø`.

![CCQ](assets/fr/38.webp)

Det andre nivået av ødeleggelse består i å deaktivere COLDCARDs to sikkerhetsbrikker permanent via programvaren. Denne handlingen gjør enheten helt ubrukelig. Du vil ikke kunne selge det videre, bruke det på nytt eller returnere det til Coinkite: det vil bli permanent ødelagt. For å fortsette, følg trinnene som er beskrevet i forrige avsnitt angående "*Brick Me*" PIN-koden, og skriv deretter inn denne PIN-koden med vilje når du låser opp COLDCARD.

Det tredje nivået innebærer fysisk ødeleggelse av COLDCARD Qs sikre komponenter. Som tidligere vil dette gjøre enheten ugjenkallelig ubrukelig. For å gjøre dette, bruk et bor til å lage et hull i de to brikkene øverst til høyre på enheten (når den er snudd opp ned), i nærheten av "*SHOOT HERE*"-innskriften.

**Viktige forholdsregler** :


- For å unngå fare for elektrisk støt må du ta ut batteriene fra enheten og koble den fra strømnettet før du håndterer den.
- Vent noen minutter etter at du har slått av enheten før du begynner å bore.
- Bruk isolerte hansker og vernebriller for å ivareta din egen sikkerhet.

![CCQ](assets/fr/39.webp)

Når brikkene er stanset, må du ikke forsøke å koble til COLDCARD Q igjen.

Gratulerer, du er nå oppdatert på COLDCARD Qs avanserte alternativer!

Hvis du fant denne opplæringen nyttig, ville jeg være veldig takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne opplæringen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også denne andre veiledningen, der vi diskuterer bruken av en direkte konkurrent til CCQ, Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a