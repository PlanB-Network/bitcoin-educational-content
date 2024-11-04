---
name: BitBox02

description: Sette opp og bruke en BitBox02
---

![cover](assets/cover.webp)

BitBox02 (https://bitbox.swiss/) er en sveitsiskprodusert fysisk lommebok spesielt designet for å sikre dine Bitcoins. Noen av dens nøkkelfunksjoner inkluderer enkel sikkerhetskopi og gjenoppretting ved hjelp av et microSD-kort, et minimalistisk og diskret design, og omfattende støtte for Bitcoin.

![device](assets/1.webp)

Den tilbyr toppmoderne sikkerhet utviklet av eksperter, med et dobbeltbrikke-design som inkluderer en sikkerhetsbrikke. Kildekoden har blitt fullstendig revidert av sikkerhetsforskere og er helt åpen kildekode. BitBox02 kommer med en enkel, men kraftig BitBoxApp, som gir sikker håndtering av dine Bitcoins. Den støtter full node for Bitcoin og sikrer ende-til-ende kryptert kommunikasjon mellom appen og enheten. Produsert i Sveits, har BitBox02 oppnådd et positivt rykte blant brukerne.

![video](https://youtu.be/sB4b2PbYaj0)

> Spesifikasjoner
>
> - Tilkobling: USB-C
> - Kompatibilitet: Windows 7 og nyere, macOS 10.13 og nyere, Linux, Android
> - Inndata: Kapasitive berøringssensorer
> - Mikrokontroller: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; Ekte tilfeldig tallgenerator
> - Sikkerhetsbrikke: ATECC608B; Ekte tilfeldig tallgenerator (NIST SP 800-90A/B/C)
> - Skjerm: 128 x 64 px hvit OLED
> - Materiale: Polykarbonat
> - Størrelse: 54.5 x 25.4 x 9.6 mm inkludert USB-C plugg
> - Vekt: Enhet 12g; med emballasje og tilbehør 160g

Last ned datablad på deres nettside https://bitbox.swiss/bitbox02/

## Hvordan bruke BitBox02 Hardware Wallet

### Sette opp BitBox02

BitBox02 har en USB-C-tilkobling festet til skallet. Hvis datamaskinen din bruker den vanlige USB-porten, må du bruke adapteren som følger med enheten.

Koble den til datamaskinen din, og enheten vil slå seg på (ikke gjør det ennå).

Den har sensorer over og under, og den vil be deg om å berøre toppen eller bunnen for å orientere skjermen slik du ønsker.

![image](assets/2.webp)

### Last ned BitBox02 Appen

Besøk https://shiftcrypto.ch/ og klikk på "App"-lenken øverst for å komme til nedlastingssiden:

![image](assets/3.webp)

Klikk på den blå Last ned-knappen:

![image](assets/4.webp)

For å verifisere nedlastingen (det legger til kompleksitet, men anbefales, spesielt hvis du lagrer mye bitcoin), se Appendiks A.

Etter nedlastingen kan du pakke ut filen. På en Mac, bare dobbeltklikk på den nedlastede filen, og et BitBox App-ikon vil dukke opp i nedlastingsmappen din. Du kan dra den til skrivebordet ditt (eller hvor som helst) for enkel tilgang.

Dobbeltklikk på appen for å kjøre den (den blir ikke "installert").

På Mac vil datamaskinens barnepike gi deg en advarsel. Bare ignorer den og klikk "åpne":

![image](assets/5.webp)

Du vil da se dette:

![image](assets/6.webp)

Gå videre og koble enheten til datamaskinen.

Den vil vise deg en paringskode. Sjekk at de stemmer overens, og berør deretter sensoren for å velge hake-tegnet. Deretter tilbake til skjermen, vil fortsett-knappen bli tilgjengelig for deg.

![image](assets/7.webp)
Du vil deretter ha muligheten til å opprette en ny seed, eller gjenopprette en seed. Jeg vil demonstrere hvordan man oppretter en ny seed (Det er også viktig å gjenopprette seeden du opprettet for å teste kvaliteten på sikkerhetskopien din, før du laster noen bitcoin på lommeboken).

![bilde](assets/8.webp)

Enheten kom med et microSD-kort. Gå videre og sett det inn hvis du ikke har gjort det.

![bilde](assets/9.webp)

Navngi enheten din og klikk fortsett, deretter bekreft på enheten.

![bilde](assets/10.webp)

Du vil deretter bli bedt om å sette et passord for enheten. Dette er ikke en del av din seed. Det er heller ikke en passfrase (det er en del av din seed). Det er rett og slett et passord for å låse enheten. Når du slår på enheten, vil du bli bedt om å angi dette passordet hver gang. Du har 10 påfølgende feil tillatt før enheten vil slette seg selv for all minne, så vær forsiktig. Animasjonen på skjermen vil lære deg hvordan du bruker enhetens kontroller for å sette passordet.

![bilde](assets/11.webp)

Les neste skjerm, og kryss av hver boks, deretter fortsett.

![bilde](assets/12.webp)
![bilde](assets/13.webp)
![bilde](assets/14.webp)

Og slik ser lommeboken ut når den er klar til bruk.

![bilde](assets/15.webp)

### IKKE SÅ FORT!!

Det er ganske merkelig, men BitBox02 forteller oss at vi er klare til å bruke enheten, men den har ikke bedt oss om å skrive ned seed-ordene! Den ENESTE sikkerhetskopien vi har er filen lagret på microSD-kortet. Dette er utilstrekkelig. Disse lagringsenhetene varer ikke evig (på grunn av "bit rot"). Vi trenger en papirbackup, og duplikater, oppbevart i et sikkerhetsskap (som forklart i den generelle veiledningen for hvordan bruke hardware-lommebøker)

For å få vår seed-frase og skrive den ned, gå til "manage device"-fanen på venstre side, og deretter klikk "show recover words"

![bilde](assets/16.webp)

Du kan deretter gå gjennom bekreftelsen, og enheten vil presentere deg ordene. Skriv dem ned pent, og aldri la noen se ordene.

![bilde](assets/17.webp)

Etter det kan du klikke på Bitcoin-fanen på venstre side for å få dine mottaksadresser.

![bilde](assets/18.webp)

Den viser en om gangen, men i det minste lar den deg velge hvilken adresse du vil bruke fra de første 20:

![bilde](assets/19.webp)

Å klikke på den blå knappen vil vise hele adressen, og du vil bli bedt om å sjekke at adressen stemmer overens med visningen på skjermen. Dette er god praksis for å bekrefte at ingen skadelig programvare på datamaskinen din lurer deg til å sende bitcoin til en angripers adresse.

![bilde](assets/20.webp)

For å sende bitcoin til denne lommeboken, kan du kopiere adressen og lime den inn på uttakssiden til børsen der myntene dine er. Jeg anbefaler at du sender en liten testmengde først, deretter øve på å bruke den enten tilbake til børsen eller til den andre adressen i lommeboken din.

For større beløp, foreslår jeg at du oppretter en passfrase (se nedenfor). Den opprinnelige lommeboken (uten passfrase) kan brukes som din lokkedue-lommebok (den må ha en rimelig mengde der for å være en troverdig lokkedue).

### Koble til en node

BitBox02 vil automatisk koble til en node. La oss se hvor den kobler til. Klikk på innstillingsfanen på venstre side, og deretter "connect your own full node".

![bilde](assets/21.webp)
Og her kan vi se at den kobler seg til shiftcrypto sin node. Ikke bra. Vi har avslørt alle våre bitcoin-adresser for dem, samt vår IP-adresse (ikke frøet selvfølgelig; de kan se våre adresser/saldoer, men kan ikke bruke dem). Vi kan legge inn detaljene for vår egen node på denne siden (utover omfanget av denne spesifikke guiden), eller vi kan bruke bedre programvare som Sparrow Bitcoin Wallet, Electrum Desktop Wallet, eller Specter Desktop. Jeg vil demonstrere Sparrow Bitcoin Wallet senere i guiden.
![bilde](assets/22.webp)

Legg til en passfrase

Nå som vi har satt opp enheten med BitBox02 App (og avslørt våre adresser, uunngåelig med denne spesifikke maskinvarelommeboken), kan vi legge til en passfrase til vår seed-frase. Dette vil tillate oss å opprette en ny lommebok ved hjelp av samme seed, og ShiftCrypto vil aldri se våre nye adresser. Vi vil kun koble denne lommeboken til vår egen programvare.

### Aktiver Passfrase

Gå videre nå og "aktiver" passfrase-funksjonen (men vi setter ikke en passfrase ennå). Gå til "manage device"-fanen, og klikk på "enable passphrase" (rød sirkel nedenfor).

![bilde](assets/23.webp)

Les gjennom stegene…

![bilde](assets/24.webp)
![bilde](assets/25.webp)
![bilde](assets/26.webp)

Koble nå fra enheten, og slå av BitBox02 App

SLUTT på bitbox02-seksjonen av Parman.

Din enhet er nå fullt operativ for å bli brukt på enhver skrivebordsløsning som specter, sparrow og ved å bruke bitbox-grensesnittet.