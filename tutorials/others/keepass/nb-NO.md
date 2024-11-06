---
name: KEEPASS
description: Hvordan sette opp en lokal passordbehandler?
---
![cover](assets/cover.webp)

I den digitale tidsalderen trenger vi å håndtere en mengde online kontoer som dekker ulike aspekter av vårt daglige liv, inkludert bankvirksomhet, finansielle plattformer, e-poster, fillagring, helse, administrasjon, sosiale nettverk, videospill, osv.

For å autentisere oss på hver av disse kontoene, bruker vi en identifikator, ofte en e-postadresse, ledsaget av et passord. Faced med umuligheten av å huske et stort antall unike passord, kan man være fristet til å gjenbruke samme passord eller å lett modifisere en felles base for å gjøre det lettere å huske. Imidlertid kompromitterer disse praksisene alvorlig sikkerheten til kontoene dine.

Det første prinsippet å følge for passord er å ikke gjenbruke dem. Hver online konto bør være beskyttet av et unikt og helt distinkt passord. Dette er viktig fordi, hvis en angriper klarer å kompromittere et av passordene dine, vil du ikke at de skal ha tilgang til alle kontoene dine. Å ha et unikt passord for hver konto isolerer potensielle angrep og begrenser deres omfang. For eksempel, hvis du bruker samme passord for en videospillplattform og for e-posten din, og det passordet blir kompromittert via en phishing-side relatert til spillplattformen, kunne angriperen da enkelt få tilgang til e-posten din og ta kontroll over alle dine andre online kontoer.

Det andre essensielle prinsippet er passordets styrke. Et passord anses som sterkt hvis det er vanskelig å brute force, det vil si å gjette gjennom prøving og feiling. Dette betyr at passordene dine må være så tilfeldige som mulig, lange, og inkludere en mangfoldighet av tegn (små bokstaver, store bokstaver, tall og symboler).

Å anvende disse to prinsippene for passordsikkerhet (unikhet og robusthet) kan vise seg vanskelig i hverdagen, ettersom det er nesten umulig å huske et unikt, tilfeldig og sterkt passord for alle våre kontoer. Dette er hvor passordbehandleren kommer inn i bildet.

En passordbehandler genererer og lagrer sterke passord på en sikker måte, og lar deg få tilgang til alle dine online kontoer uten å måtte huske dem individuelt. Du trenger bare å huske ett passord, hovedpassordet, som gir deg tilgang til alle dine lagrede passord i behandleren. Å bruke en passordbehandler forbedrer din online sikkerhet fordi det forhindrer gjenbruk av passord og systematisk genererer tilfeldige passord. Men det forenkler også din daglige bruk av kontoene dine ved å sentralisere tilgangen til din sensitive informasjon.
I denne opplæringen vil vi lære hvordan man setter opp og bruker en lokal passordbehandler for å forbedre din online sikkerhet. Her vil jeg introdusere deg for KeePass. Men, hvis du er nybegynner og ønsker å ha en online passordbehandler som er i stand til å synkronisere på tvers av flere enheter, anbefaler jeg å følge vår opplæring om Bitwarden:
https://planb.network/tutorials/others/bitwarden

---

*Forsiktighet: En passordbehandler er flott for å lagre passord, men **du bør aldri lagre din Bitcoin lommeboks' mnemonic frase i den!** Husk, en mnemonic frase bør eksklusivt lagres i et fysisk format, som et stykke papir eller metall.*

---

## Introduksjon til KeePass

KeePass er en gratis og åpen kildekode passordbehandler, perfekt for de som ønsker en gratis og sikker løsning for lokal forvaltning. Det er programvare som skal installeres på din PC som, uten tillegg av plugins, ikke kommuniserer med internettet. Dette er en radikalt forskjellig tilnærming fra den til Bitwarden, som vi dekket i en tidligere opplæring. Bitwarden, i motsetning til KeePass, tillater synkronisering på tvers av flere enheter og krever dermed lagring av passordene dine på en online server.
Som standard støtter ikke KeePass bruk av nettleserutvidelser som Bitwarden; derfor må du manuelt kopiere og lime inn passordene dine fra programvaren. Selv om dette kan virke som en begrensning, er kopiering og liming av passord i stedet for å bruke autofyll en god praksis for din nettbaserte sikkerhet.
KeePass er designet for å være både lett og enkel å bruke, samtidig som den opprettholder høye sikkerhetsstandarder. Programvaren krypterer databasen din lokalt for optimal beskyttelse av dine legitimasjoner. KeePass er også den eneste passordbehandleren som er validert av ANSSI (den franske cybersikkerhetsmyndigheten).

En av de viktigste fordelene med KeePass er dets fleksibilitet. Det kan brukes på mange forskjellige måter, som på en USB-stick uten behov for installasjon på en datamaskin. Videre, takket være sitt [plugin-miljø](https://keepass.info/plugins.html), kan KeePass tilpasses for å møte mer spesifikke behov.
![KEEPASS](assets/notext/01.webp)
## Hvordan laste ned KeePass?

Installasjonsprosessen for KeePass varierer avhengig av operativsystemet du bruker. For Windows- eller Linux-brukere er installasjonen relativt grei. Men, hvis du er på macOS, er et ekstra trinn nødvendig på grunn av KeePass sin utvikling på .NET-plattformen, som ikke direkte støttes av macOS. Derfor må du konfigurere et kompatibelt miljø for å tillate KeePass å kjøre på Apple-enheter.

For Debian/Ubuntu-brukere, åpne terminalen og skriv inn følgende kommandoer:

```bash
sudo apt-get update
sudo apt-get install keepass2
```

For Fedora:

```bash
sudo dnf install keepass
```

For Arch Linux:

```bash
sudo pacman -S keepass
```

Hvis du er på en Windows-datamaskin, gå til [den offisielle KeePass-nedlastingssiden](https://keepass.info/download.html), og last ned den nyeste versjonen av installasjonsprogrammet:
![KEEPASS](assets/notext/02.webp)
Klikk på den nedlastede filen for å kjøre den, og følg instruksjonene i oppsettveiviseren for å fullføre installasjonen (se neste avsnitt).

For macOS-brukere er installasjonen litt mer kompleks. Hvis du ønsker å bruke den originale versjonen av KeePass som på Windows, følg instruksjonene nedenfor. Ellers kan du velge [KeePassXC](https://keepassxc.org/), en alternativ versjon kompatibel med macOS, som tilbyr et litt annerledes grensesnitt.

For å bruke KeePass, trenger du et kjøretidsmiljø for .NET-applikasjoner. Jeg anbefaler å installere Mono for dette. Gå til [den offisielle Mono-siden](https://www.mono-project.com/download/stable/#download-mac) i "*macOS*" seksjonen, og klikk på lenken for å laste ned installasjonspakken (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Åpne den nedlastede `.pkg`-filen og følg instruksjonene for å installere Mono på din Mac.
![KEEPASS](assets/notext/04.webp)
Deretter, gå til den offisielle KeePass-nettsiden og last ned den nyeste portable versjonen i `.zip`-format.
![KEEPASS](assets/notext/05.webp)
Etter å ha lastet ned `.zip`-filen, dobbeltklikk for å pakke den ut. Du vil få en mappe som inneholder flere filer, inkludert `KeePass.exe`. Åpne en terminal, naviger til KeePass-mappen (erstatt `xx` med versjonsnummeret):

```bash
cd ~/Downloads/KeePass-2.xx
```

Og til slutt, kjør KeePass med Mono:

```bash
mono KeePass.exe
```

## Hvordan installere KeePass?

Ved første oppstart, kan du velge grensesnittspråket.
![KEEPASS](assets/notext/06.webp)
Godta vilkårene for lisensen. ![KEEPASS](assets/notext/07.webp)
Velg mappen der KeePass skal installeres.
![KEEPASS](assets/notext/08.webp)
Du kan eventuelt endre hvilke komponenter av applikasjonen som installeres. Hvis du har nok plass, kan du enkelt velge "*Full installasjon*".
![KEEPASS](assets/notext/09.webp)
Og til slutt kan du velge å legge til en snarvei på skrivebordet ditt.
![KEEPASS](assets/notext/10.webp)
Klikk på "*Installer*" knappen.
![KEEPASS](assets/notext/11.webp)
Vent under installasjonen, deretter klikker du på "*Fullfør*" knappen.
![KEEPASS](assets/notext/12.webp)
## Hvordan konfigurere KeePass?

Du kommer nå til KeePass-grensesnittet ditt.
![KEEPASS](assets/notext/13.webp)For å opprette din første database, klikk på "*Fil*" fanen.
![KEEPASS](assets/notext/14.webp)
Deretter på "*Ny*" menyen.
![KEEPASS](assets/notext/15.webp)
Programvaren vil opprette en ny database hvor passordene dine vil bli lagret. Du må velge plasseringen for denne mappen. Velg en plassering som er lett tilgjengelig.
![KEEPASS](assets/notext/16.webp)
Etterpå bør du tenke på å regelmessig ta sikkerhetskopi av denne mappen for å unngå å miste legitimasjonen din i tilfelle tap, skade eller tyveri av datamaskinen din. For eksempel kan du kopiere databasen til en USB-stikk hver uke. Filen som inneholder databasen din heter `Database.kdbx` (dokumentet er kryptert med ditt hovedpassord). For flere råd om beste praksis for sikkerhetskopiering, anbefaler jeg også å konsultere denne andre opplæringen:

https://planb.network/tutorials/others/proton-drive

Neste kommer valget av ditt hovedpassord.
![KEEPASS](assets/notext/17.webp)
Som vi så i introduksjonen, er dette passordet veldig viktig, da det gir deg tilgang til alle dine andre lagrede passord i databasen. Dette passordet vil bli brukt til å kryptere `Database.kdbx` databasen. Det presenterer to hovedrisikoer: tap og kompromittering. Hvis du mister tilgangen til dette passordet, vil du ikke lenger kunne få tilgang til alle legitimasjonene dine. Hvis passordet ditt blir stjålet, i tillegg til den krypterte databasen, vil angriperen kunne få tilgang til alle kontoene dine.

For å minimere risikoen for tap, anbefaler jeg å lage en fysisk sikkerhetskopi av hovedpassordet ditt på papir og lagre det på et sikkert sted. Om mulig, forsegl denne sikkerhetskopien i en sikker konvolutt for å regelmessig sikre at ingen andre har hatt tilgang til den.

For å forhindre kompromittering av hovedpassordet ditt, må det være ekstremt robust. Det bør være så langt som mulig, bruke et bredt utvalg av tegn, og velges tilfeldig. I 2024 er de minimumsanbefalingene for et sikkert passord 13 tegn inkludert tall, små og store bokstaver, samt symboler, forutsatt at passordet er virkelig tilfeldig. Jeg anbefaler imidlertid å velge et passord på minst 20 tegn, inkludert alle mulige typer tegn, for å sikre dets sikkerhet over lengre tid.

Skriv inn ditt hovedpassord i det dedikerte feltet og bekreft det i det følgende feltet, deretter klikker du på "*OK*".
![KEEPASS](assets/notext/18.webp)
Navngi databasen din og legg til en beskrivelse om nødvendig. Dette kan hjelpe deg med å skille mellom forskjellige databaser hvis du oppretter flere, for eksempel en for personlig bruk og en annen for profesjonell bruk.
![KEEPASS](assets/notext/19.webp)
For andre innstillinger anbefaler jeg å beholde standardalternativene. Deretter klikker du på "*OK*" knappen.
![KEEPASS](assets/notext/20.webp)KeePass tilbyr deretter å skrive ut et nødskjema.
![KEEPASS](assets/notext/21.webp)
På dette skjemaet vil du finne plasseringen av databasen din i filene dine, et område for å manuelt skrive ned ditt hovedpassord, samt instruksjoner for å få tilgang til det. Dette skjemaet bør overlates til pålitelige personer, ettersom det muliggjør gjenoppretting av tilgang til legitimasjonene dine i tilfelle et problem.

Men, siden dette skjemaet gir tilgang til passordene dine ved å avsløre ditt hovedpassord, må det brukes med forsiktighet. Det anbefales å oppbevare det i et forseglet konvolutt som et minimum, noe som muliggjør periodiske sjekker for å sikre at det ikke har blitt konsultert. Du er ikke forpliktet til å bruke dette skjemaet og kan vurdere andre sikkerhetskopieringsmetoder for dine kjære.
![KEEPASS](assets/notext/22.webp)
Du kan deretter få tilgang til din passordbehandler.
![KEEPASS](assets/notext/23.webp)
Før du begynner å lagre legitimasjonene dine, anbefaler jeg å endre innstillingene for passordgenerering. For å gjøre dette, gå til fanen "*Tools*" og velg "*Generate Password...*".
![KEEPASS](assets/notext/24.webp)
Her råder jeg deg til å øke lengden på de genererte passordene til 40 tegn. Nå som du har en passordbehandler til å huske dem for deg, er det ingen grunn til å spare på antall tegn. Dessuten trenger du ikke å skrive ned passordene for hånd, siden du kan kopiere og lime dem inn. Så, det gjør ingen forskjell for deg å ha veldig lange passord på 40 tegn, men deres sikkerhet er sterkt forbedret. Jeg råder deg til å gjøre dette, og også til å krysse av for spesialtegn.
![KEEPASS](assets/notext/25.webp)
Bekreft ved å klikke på det lille lagre-ikonet.
![KEEPASS](assets/notext/26.webp)
Legg til et navn på din passordprofil.
![KEEPASS](assets/notext/27.webp)
## Hvordan sikre kontoene dine med KeePass?

For å registrere en ny legitimasjon i din KeePass-behandler, klikk bare på nøkkelikonet med den grønne pilen.
![KEEPASS](assets/notext/28.webp)
I genererings- og lagringsvinduet, klikk på det lille nøkkelikonet og velg din 40-tegns passordprofil.
![KEEPASS](assets/notext/29.webp)
Skriv inn brukernavnet for denne kontoen samt en tittel for å enkelt finne den i databasen din. ![KEEPASS](assets/notext/30.webp) Det er også mulig å legge til en URL hvis du ønsker å bruke snarveier senere, og om nødvendig, et notat. ![KEEPASS](assets/notext/31.webp) Hvis alt er til din tilfredshet, klikk på "*OK*" for å lagre passordet. ![KEEPASS](assets/notext/32.webp) Du kan finne passordet ditt på hjemmesiden til din KeePass-manager. ![KEEPASS](assets/notext/33.webp) For å kopiere et passord, dobbeltklikk på det. Det vil forbli i utklippstavlen din i 12 sekunder, slik at du kan lime det inn på nettstedet under ditt neste innlogging. ![KEEPASS](assets/notext/34.webp) Hvis du ønsker å forlenge varigheten passordet forblir i utklippstavlen, klikk på fanen "*Verktøy*", deretter på "*Alternativer...*". ![KEEPASS](assets/notext/35.webp) Under fanen "*Sikkerhet*", juster varigheten ved å endre antall sekunder i boksen "*Clipboard auto-clear time*". Deretter klikker du på "*OK*" for å lagre endringene dine. ![KEEPASS](assets/notext/36.webp) På venstre side av grensesnittet ditt, vil du legge merke til at det er flere mapper for å organisere passordene dine. ![KEEPASS](assets/notext/37.webp) Du har muligheten til å slette standardmappene eller legge til nye ved å høyreklikke og velge "*Legg til gruppe...*". ![KEEPASS](assets/notext/38.webp) Velg et navn for den nye mappen og velg et ikon. Du kan også importere dine egne ikoner i `.ico`-format. Deretter klikker du på "*OK*" knappen for å fullføre opprettelsen av mappen. ![KEEPASS](assets/notext/39.webp) Mappen din vises på venstre side. ![KEEPASS](assets/notext/40.webp) For å legge til et passord i en mappe, dra det ganske enkelt fra databasen til ønsket mappe. ![KEEPASS](assets/notext/41.webp) Denne funksjonen hjelper deg med å organisere passordbehandleren din og finne legitimasjonen din lettere.
En annen metode for å finne et passord er å bruke søkefunksjonen. Skriv tittelen på identifikatoren du ønsker å finne i søkefeltet øverst i grensesnittet, og du vil direkte få tilgang til det. ![KEEPASS](assets/notext/42.webp) Vær oppmerksom, da KeePass fungerer litt som et tekstbehandlingsdokument. Før du lukker applikasjonen, hvis du har lagt til nye elementer i manageren din, husk å lagre databasen. Du kan gjøre dette ved å klikke på lagre-ikonet eller ved å bruke tastatursnarveien `Ctrl+S`. ![KEEPASS](assets/notext/43.webp)
Hvis du lar KeePass være åpen i bakgrunnen, vil programvaren ikke lukke seg som standard. Men, hvis du lukker KeePass eller slår av datamaskinen din, må du skrive inn hovedpassordet ditt for å dekryptere databasen din når du åpner programvaren på nytt. ![KEEPASS](assets/notext/44.webp)
Det dekker de grunnleggende funksjonene til KeePass. Selvfølgelig, denne opplæringen rettet mot nybegynnere har bare skrapt overflaten av de mange alternativene som er tilgjengelige med denne programvaren. Det er en mengde ytterligere funksjoner å utforske, for ikke å nevne [alle plugin-modulene utviklet av fellesskapet](https://keepass.info/plugins.html) som kan utvide funksjonaliteten til KeePass ytterligere.

Hvis du er interessert i å lære hvordan du drastisk kan forbedre sikkerheten til dine online kontoer for å unngå hacking med 2FA, anbefaler jeg også å sjekke ut denne andre opplæringen:

https://planb.network/tutorials/others/authy