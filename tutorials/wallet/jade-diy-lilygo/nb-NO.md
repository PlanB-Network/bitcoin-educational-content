---
name: Jade DIY
description: Gjør om et utviklingskort til 15 dollar til en fullt funksjonell Bitcoin-maskinvare wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Nybegynnerbygg


**Målgruppe:** Nysgjerrige byggere med liten eller ingen erfaring med innebygd teknologi.


**Varighet:** 2 timer (fleksibelt)


**Mål:** Ved slutten av kurset vil studentene:



- Kjenne til sikkerhetsmodellen for DIY-lommebøker kontra kommersielle enheter.
- Sett sammen en mikrokontrollerbasert signeringsenhet.
- Flash åpen kildekode-fastvare og verifiser build-kontrollsummen.
- Signer og send en mainnet-transaksjon ved hjelp av den nye enheten.


---

## Sammendrag


Denne totimers workshopen lærer nybegynnere å bygge en funksjonell Bitcoin-maskinvare wallet ved å flashe Jade-fastvare med åpen kildekode på et LilyGO T-Display-kort til 15 dollar. Studentene forvandler generisk utviklingsmaskinvare til en signeringsenhet som kan sammenlignes med kommersielle lommebøker som koster 150 dollar, og lærer grunnleggende sikkerhet gjennom praktisk erfaring i stedet for teori alene.


### Filosofi


Å bygge din egen signeringsenhet handler ikke bare om å spare penger - det handler også om å forstå teknologien som beskytter Bitcoin. Denne workshopen omfavner "sikkerhet gjennom forståelse" fremfor "black box"-tillit. Ved å kjøpe inn komponenter, flashe fastvare med åpen kildekode og generere entropi selv, reduserer elevene risikoen i leverandørkjeden samtidig som de lærer å vurdere sikkerhetskrav kritisk. Målet er informert autonomi: Elevene skal forstå både styrken og begrensningene ved DIY-enheten sin sammenlignet med herdede kommersielle alternativer.


---

## Grunnleggende om konseptet (15 min)


### Hva er selvforvaring, og hvorfor er det viktig?


Bitcoin ble opprettet for å fjerne behovet for betrodde tredjeparter, som banker og selskaper, fra pengesystemet vårt. I stedet for å bruke tillit bruker bitcoin matematikk, fysikk og kryptografi for å gi hvem som helst muligheten til å eie og kontrollere pengene sine uten å trenge tillatelse fra noen.


Det fungerer slik at bitcoin eksisterer i en global digital hovedbok som kalles blokkjeden, også kjent som bitcoins tidskjede, som er en offentlig og transparent hovedbok som drives av datamaskiner, i stedet for en sentralisert hovedbok som en bankkonto.


Det er viktig å forstå at for å kunne flytte bitcoin fra ett sted til et annet, må du signere transaksjonen med det som kalles en privat nøkkel. Tenk på det som å låse opp et hvelv med et passord, og flytte bitcoinene til noen andres hvelv. Bitcoin gir deg muligheten til å holde nøklene til hvelvet selv, i stedet for å stole på at en bank flytter pengene dine for deg.


Med stor makt følger et stort ansvar. Mister du nøklene, er pengene dine borte for alltid. På denne måten kan du tenke på nøklene til hvelvet som selve pengene. Selv om nøkler ikke er det samme som bitcoin, er de mekanismen for å flytte pengene dine og er derfor ekstremt viktige å beskytte. Det er derfor vi sier "ikke nøklene dine, ikke myntene dine".


Begrepet "self-custody" kan høres forvirrende ut, men det betyr bare at du har dine egne private nøkler og kontroll over dine egne bitcoin. Hvis du ikke har den nøkkelen, overlater du den til noen andre. Hvis bitcoinene dine er i en ETF eller på en børs (Mt. Gox, FTX, Coinbase, Binance osv.), eier du ikke bitcoin, du eier en rettighet til bitcoin. Dette introduserer alle slags risikoer, som at børser blir hacket og mister bitcoinene dine, eller at selskaper låner ut pengene dine og bare gir deg en brøkdel i reserve. I tillegg vil betrodde tredjeparter ha full kontroll over pengene dine og kunne begrense eller fryse uttak.


![image](assets/fr/01.webp)


Med selvforvaring fjerner du tillit fra ligningen. Ingen kan fryse pengene dine eller nekte en transaksjon, du kan sende penger over landegrensene, til hvem som helst, når som helst, og du trenger verken bankkonto, ID eller noens godkjenning. Ingen kan stoppe deg, sensurere deg eller stjele fra deg, noe som frigjør bitcoins fulle kraft som frihetspenger. Det er derfor vi sier at med bitcoin kan du være din egen bank.


Bitcoin ble opprettet for å løse problemet med manipulering av tillit og penger, en utvei fra vårt nåværende system, men utgangen fungerer bare hvis du tar nøklene. Det er derfor det er så viktig med selvforvaring.


### Hva er en Wallet?


Begrepet wallet er litt av en misvisende betegnelse og kan derfor være forvirrende. Ja, det stemmer at en bitcoin wallet, i likhet med en fysisk wallet, lagrer verdi. Men hovedforskjellen er at bitcoin-lommebøker faktisk ikke lagrer noen bitcoin.


Bitcoin eksisterer kun som en hovedbokoppføring i den offentlige blokkjeden, eller i de metaforiske hvelvene i cyberspace. Husk at for å flytte bitcoin må du bruke nøklene dine til å låse opp hvelvet og flytte myntene et annet sted, og det er de private nøklene som brukes til å bruke bitcoin. Når du foretar en transaksjon med dine wallet, bruker du egentlig bare nøklene dine til å signere transaksjonen. Det er slik du viser at du eier pengene og har rett til å bruke myntene.


Bitcoin-lommebøker lagrer egentlig bare de private nøklene dine, så det ville vært mer korrekt å kalle dem nøkkelringer.


### Hot vs Cold lommebøker


En hot wallet er en programvareapp på telefonen eller datamaskinen din. Den er koblet til internett, slik at den er enklere å bruke og raskere å signere transaksjoner, men dette betyr også at den er mer utsatt for hackere, skadelig programvare og phishing. Den kalles "hot" fordi den er koblet til Internett, er plugget inn og er slått på. Et eksempel kan være en telefon wallet eller en nettleser wallet.


En kald wallet, eller maskinvare-wallet, er derimot en enhet som oppretter og lagrer nøkkelen din offline. Dette fjerner muligheten for at noen kan hacke pengene dine og er mye tryggere for langsiktig sparing, men det er en enhet som er nødvendig for å signere hver transaksjon og kan være mindre praktisk.


### Hardware Wallet Trusselmodell


Maskinvare-lommebøker finnes for å løse et grunnleggende problem: Hvordan signerer du Bitcoin-transaksjoner uten å eksponere de private nøklene dine for en Internett-tilkoblet datamaskin som kan bli kompromittert av skadelig programvare eller eksterne angripere? Kjernetrusselmodellen tar utgangspunkt i at den bærbare datamaskinen eller telefonen du bruker til daglig, er potensielt fiendtlig. En maskinvare-wallet skaper et isolert miljø der private nøkler aldri forlater enheten, og transaksjonssigneringen skjer i en secure element eller mikrokontroller som kun kommuniserer signaturen tilbake til vertsdatamaskinen, ikke selve nøkkelen. Selv om datamaskinen din er fullstendig kompromittert, kan en angriper ikke stjele Bitcoin uten fysisk tilgang til enheten og PIN-koden din.


Lommebøker med maskinvare introduserer imidlertid sine egne trusler. Du må stole på at produsenten ikke har introdusert bakdører, at leverandørkjeden ikke har blitt tuklet med, og at genereringen av tilfeldige tall virkelig er tilfeldig. Fysiske angripere kan hente ut nøkler gjennom sidekanalangrep eller chipmanipulering, og noen med midlertidig tilgang kan endre enheten din. Når du bygger din egen maskinvare wallet, får du hjelp til å forstå disse avveiningene - du må ta avgjørelser om sikre elementer kontra vanlige mikrokontrollere, hvordan du skal verifisere transaksjoner på en skjerm, og hvordan du skal beskytte deg mot både eksterne og fysiske trusler. Målet er ikke perfekt sikkerhet, men å forstå hvilke trusler du beskytter deg mot, og hvilke som gjenstår.


### Nøkkelbegreper



- Entropi og seed-fraser:** Din wallet er ikke tryggere enn den tilfeldigheten den er født med. Vi blander enhetens tilfeldige tallgenerator med menneskevennlige triks som terningkast, konverterer entropien til en 12- eller 24-ords [BIP39-frase] (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), og forlater rommet med en skriftlig eller metallisk backup du stoler på.
- Hygiene for frøfraser:** Behandle seed som hovednøkler til sparepengene dine. Skriv aldri inn ordene på en telefon eller datamaskin - keyloggere, skjermbilder og sikkerhetskopier i skyen kan lekke dem for alltid. Oppbevar frasen offline, lagre den et sted bare du har tilgang til, og øv deg på å lese den høyt før du drar.
- Sikkert element + mikrokontroller:** Tenk på secure element som hvelvet og mikrokontrolleren som hjernen. secure element beskytter private nøkler med sabotasjemotstand, mens mikrokontrolleren håndterer skjermen, knappene og fastvarelogikken. Merk at maskinvarelommebøkene vi bygger i dag, ikke har en secure element. Det betyr ikke at den er usikker, bare at den har ett beskyttelsesnivå mindre.
- Stole på fastvare:** Fastvare er det usynlige operativsystemet til wallet. Last alltid ned fra merkede utgivelser, sjekk den publiserte hashen, og forstå at reproduserbare builds lar flere personer kompilere den samme koden og komme frem til nøyaktig samme binærfil. Hvis sjekksummen ikke stemmer overens, signerer du ikke.


---

## Hva er det vi bygger?


Vi tar generisk maskinvare, LilyGo T-Display, og flasher Jade SDK-fastvare på den. Jade Plus] (https://blockstream.com/jade/jade-plus/) er en wallet med åpen kildekode, som vanligvis koster 150 dollar:


![image](assets/fr/02.webp)


I dag skal vi i stedet flashe fastvaren deres på en maskinvare til 15 dollar.


### Hva du bør kjøpe


![image](assets/fr/03.webp)



- LilyGO T-Display (16 MB med skall, modell K164)** - [Bestill direkte fra LilyGO] (https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) for ca. $15. Dette ESP32-kortet har skjerm, knapper og USB-grensesnitt som speiler Blockstreams Jade Plus. ESP32-kortet inneholder også Wi-Fi- og Bluetooth-radioer; vi leverer fastvare som holder dem deaktivert, men de former trusselmodellen din fordi ondsinnet kode kan slå dem på igjen.
- USB-C-kabel** - Ta med en datakapabel slik at du kan flashe fastvare og drive kortet direkte fra den bærbare datamaskinen (helt greit for klassebruk).


### Hvorfor bygge din egen Hardware Wallet?



- Spar ca. 135 dollar i forhold til å kjøpe en kommersiell enhet.
- Bygg opp komfort med fastvare som blinker, sikre elementer og wallet-hygiene.
- Start opp flere signeringsenheter for å spre besparelsene på flere lommebøker.
- Reduser risikoen i leverandørkjeden ved å kjøpe inn og montere alle komponenter selv.
- Husk Lopps mantra: Suverenitet og bekvemmelighet står alltid i motsetning til hverandre.


## Fysisk oppsett


### Forbered saken din


Du har to alternativer for å huse LilyGO T-Display-kortet ditt: et 3D-printet etui eller det offisielle LilyGO-kabinettet. Det trykte kabinettet kan du finne og skrive ut fra [denne modellen] (https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Det gir et lett og tilpassbart skall til enheten din.


![image](assets/fr/04.webp)


Alternativt kan du bruke det offisielle LilyGO-etuiet, som har en litt annen passform og finish, og som gir mer robust beskyttelse og et polert utseende.


![image](assets/fr/05.webp)


Vær oppmerksom på at det trykte og det offisielle kabinettet har litt forskjellig design og montering. Uansett hvilket alternativ du velger, må du sørge for at kortet sitter ordentlig på plass i kabinettet for å unngå løse forbindelser eller skader.


### Inspiser styret


Før du fortsetter, må du inspisere LilyGO T-Display-kortet nøye for synlige defekter eller rusk. Kontroller at skjermen, knappene og USB-C-porten er rene og fri for støv eller loddesprut. Håndter kortet med forsiktighet, og vær oppmerksom på elektrostatisk utladning (ESD) ved å jorde deg selv eller bruke en ESD-håndleddsstropp for å forhindre skade på følsomme komponenter.


### Koble til den bærbare datamaskinen


Koble LilyGO-kortet til den bærbare datamaskinen ved hjelp av en USB-C-kabel med datakapasitet. Denne tilkoblingen gir strøm og lar deg flashe fastvaren.


Når du starter opp, ser du følgende skjermbilde:


![image](assets/fr/06.webp)



Når LilyGO er slått på, vil den vise en fargetestskjerm som veksler mellom faste farger. Dette bekrefter at skjermen og kortet fungerer som de skal før du blinker fastvaren.


Når fargetesten er fullført, går skjermen over i en standardtilstand som indikerer at kortet er klart for de neste trinnene i byggeprosessen.


![image](assets/fr/07.webp)


## Den enkle måten eller Hard-måten


Det finnes to hovedmetoder for å flashe fastvaren til wallet-maskinvaren: den enkle måten og den vanskelige måten. Den enkle måten bruker forhåndskonfigurerte verktøy eller nettbaserte flashere som automatisk laster inn fastvaren på enheten din med minimale inndata. Denne metoden er ideell for nybegynnere som vil ha en rask gevinst eller foretrekker å unngå kompleksiteten ved feilsøking og kommandolinjeinteraksjoner. Den forenkler prosessen og får deg raskere i gang, noe som gjør den tilgjengelig for dem som ikke har erfaring med innebygd utvikling eller maskinvarelommebøker.


Den harde måten innebærer derimot manuell bruk av kommandolinjeverktøy for å flashe fastvaren. Denne tilnærmingen krever verifisering av fastvaresignaturer og sjekksummer for å sikre autentisitet og integritet, noe som gir deg en dypere forståelse av flashing-prosessen og hvordan fastvaren samhandler med maskinvaren. Selv om det krever mer innsats og kjennskap til terminalkommandoer, gir det større kontroll, åpenhet og tillit til enhetens sikkerhet.


Hver metode har sine kompromisser: Den enkle metoden ofrer en viss grad av tillit og forståelse for hastighet og bekvemmelighet, mens den vanskelige metoden krever mer tid og tekniske ferdigheter, men belønner deg med fleksibilitet og en sterkere forståelse av den underliggende teknologien. Lærerne bør oppmuntre studentene til å velge den veien som passer best med deres komfortnivå og nysgjerrighet, slik at de får både selvtillit og utforskertrang.


## Den enkle måten


Den enkleste måten å flashe en ESP32 på



- Gå til den offisielle Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Du kan laste ned kildefilen og kjøre nettstedet lokalt, men GitHub er allerede vert for det på [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub serverer HTML, CSS, JavaScript osv. direkte til nettleseren din, slik at du kan flashe enheten uten å installere utviklerverktøy.


![image](assets/fr/09.webp)



- Åpne rullegardinmenyen (standardinnstillingen er sannsynligvis `M5Stack Core2`), og velg utviklingskortet ditt - for denne klassen velger du `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Når du klikker på blits, vil dette vises. For å vite hvilken enhet som er LILYGO, kobler du fra lilygoen og kobler den til igjen. COM-porten som lilygoen er koblet til vil vises og forsvinne. Klikk på COM-porten som Jade er koblet til


![image](assets/fr/11.webp)



- Det er det en fremdriftslinje skal vises, og når den er ferdig, er du klar til å sette den opp


## Sette opp Jade Wallet


Når fastvaren er flashet, er LilyGO T-Display nå en fullt funksjonell Jade-maskinvare wallet. Denne delen vil lede deg gjennom den innledende oppsettprosessen, fra å generere seed-frasen til å koble til enheten med wallet-programvare som Sparrow eller Blockstream Green-mobilappen.


### Første oppstart og enhetsoppsett



- Slå på enheten:** Når LilyGO fortsatt er koblet til den bærbare datamaskinen via USB-C, bør Jade-fastvaren starte opp automatisk. Du vil se Jade-logoen vises på skjermen.



- Gå inn i oppsettmodus:** Enheten viser deg en innledende meny. Bruk de to fysiske knappene på kortet til å navigere:
 - Venstre knapp:** Flytt opp/tilbake
 - Høyre knapp:** Flytt nedover/forover
 - Begge knappene samtidig:** Velg/bekreft



- Velg "Setup":** Naviger til Setup-alternativet, og trykk på begge knappene for å bekrefte. Enheten vil veilede deg gjennom den innledende konfigurasjonsprosessen.


### Opprette din Wallet



- Velg "Start oppsett":** Enheten vil be deg om å starte opprettelsesprosessen for wallet. Bekreft valget ditt.



- Velg "Opprett ny Wallet":** Du får opp to alternativer:
 - Create New Wallet:** Genererer en ny seed-frase (velg denne for workshopen)
 - Gjenopprett Wallet:** Gjenopprett en eksisterende wallet fra en seed-frase (for avanserte brukere)



- Velg "Opprett ny Wallet" og bekreft.



- Generere entropi:** Enheten bruker sin egen tilfeldighetsgenerator til å skape kryptografisk entropi. Denne prosessen tar noen sekunder, ettersom enheten samler inn tilfeldigheter fra flere kilder.


### Ta opp frøfrasen din



- Skriv ned seed-frasen din:** Enheten vil nå vise en 12-ords BIP39 seed-frase, ett ord om gangen. Dette er det mest kritiske trinnet i hele prosessen.


**Viktige sikkerhetsrutiner:**


- Skriv hvert ord tydelig på papir (bruk eventuelt de medfølgende seed-setningskortene)
- Dobbeltsjekk hvert ord mens du skriver det
- Aldri fotografer seed-frasen med telefonen din
- Skriv aldri ordene inn på noen datamaskin eller telefon
- Hold seed-setningen din privat - ikke del skjermen eller vis den til andre



- Bekreft seed-frasen din:** Etter at du har skrevet ned alle 12 ordene, vil enheten be deg om å bekrefte flere ord fra frasen for å sikre at du har registrert dem riktig. Bruk knappene til å velge riktig ord for hver ledetekst.


**Profftips:** Før du går videre, bør du øve deg på å lese seed-frasen høyt for deg selv (stille, slik at andre ikke kan høre). På den måten kan du fange opp eventuelle håndskriftsfeil eller uklarheter.


### Tilkoblingsmetode



- Velg tilkoblingstype:** Jade-fastvaren støtter to tilkoblingsmetoder:
 - USB:** Kablet tilkobling via USB-C-kabel (anbefales for dette verkstedet)
 - Bluetooth:** Trådløs tilkobling til mobile enheter



- Velg **USB** inntil videre, ettersom det er det enkleste alternativet for stasjonær wallet-programvare og ikke introduserer trådløse angrepsvektorer.



- Enhetsnavn:** Jade vil vise en unik identifikator som "Connect Jade A7D924". Denne identifikatoren hjelper deg med å skille mellom flere maskinvarelommebøker hvis du ender opp med å bygge mer enn én. Noter denne identifikatoren hvis du ønsker det.


### Koble til Wallet-programvaren


Du har nå to hovedalternativer for grensesnittet med den nyopprettede maskinvaren wallet: mobilappen Blockstream Green (for bruk på farten) eller Sparrow Wallet (for stasjonær bruk med mer avanserte funksjoner). I denne workshopen fokuserer vi på Sparrow Wallet, ettersom den gir bedre innsyn i de tekniske detaljene i Bitcoin-transaksjoner.


#### Alternativ 1: Blockstream Green Mobile App (Hurtigstart)


Hvis du vil teste enheten raskt med en mobil enhet:



- Last ned **Blockstream Green**-appen fra App Store (iOS) eller Google Play (Android)
- Åpne appen og velg "Koble til Hardware Wallet"
- Velg "Jade" fra listen over støttede enheter
- Koble Jade til telefonen ved hjelp av en USB-C til USB-C-kabel (eller USB-C til Lightning-adapter for iPhone 15+)
- Følg instruksjonene på skjermen for å koble til og opprette din første wallet


**Merknad om Liquid:** Blockstream Green-appen støtter både Bitcoin og Liquid (en Bitcoin-sidekjede). Hvis du bruker Liquid-funksjoner, kan du bli bedt om å "Eksportere hovedblindingsnøkkel" - dette gjør det mulig for appen å se transaksjonsbeløp på Liquid-nettverket, som ellers er konfidensielle. I denne workshopen kan du hoppe over Liquid-funksjoner og fokusere på standard Bitcoin-transaksjoner.


#### Alternativ 2: Sparrow Wallet (anbefalt for verksted)


Sparrow Wallet er et kraftig skrivebordsprogram som gir deg detaljert kontroll over Bitcoin-transaksjonene dine, og som kobles sømløst sammen med Jade-maskinvaren wallet.


**Installasjon:**



- Last ned Sparrow Wallet fra den offisielle nettsiden: [sparrowwallet.com] (https://sparrowwallet.com)
- Verifiser nedlastingssignaturen (se Sparrow-dokumentasjonen for mer informasjon)
- Installer og start applikasjonen


**Koble din Jade til Sparrow:**



- I Sparrow går du til **File → Ny Wallet**
- Gi wallet et navn (f.eks. "My Jade Wallet")
- Klikk på **Koblet Hardware Wallet**
- Sparrow bør automatisk oppdage den tilkoblede Jade-enheten din
- Hvis du blir bedt om det, bekrefter du tilkoblingen på Jade-displayet ved å trykke på begge knappene
- Velg ønsket skripttype:
 - Native Segwit (P2WPKH):** Anbefales for nybegynnere - lavest avgifter, bredest kompatibilitet med moderne lommebøker
 - Nested Segwit (P2SH-P2WPKH):** For kompatibilitet med eldre tjenester
 - Taproot (P2TR):** Mest avansert, gir best personvern og lavest avgifter, men krever avansert wallet-støtte
- Klikk på **Importer nøkkellager** for å fullføre tilkoblingen


**Konfigurering av Sparrows servertilkobling


Før du kan se saldoen din eller kringkaste transaksjoner, må Sparrow koble seg til en Bitcoin-node for å hente blokkjededata. Du har flere alternativer, alle med ulike avveininger mellom bekvemmelighet, personvern og tillit:



- Public Electrum Server (enklest, minst privat):** Kobles til en offentlig server som drives av en tredjepart. Rask å sette opp, men serveren kan se wallet-adressene dine og potensielt koble dem til IP-adressen din. Bra for testing på testnett.
 - I Sparrow går du til **Verktøy → Innstillinger → Server**
 - Velg **Public Server** og velg en server fra listen
 - Klikk på **Test tilkobling** for å bekrefte



- Bitcoin Core eller Knots Node (mest privat, mest arbeid):** Kjør din egen komplette Bitcoin-node. Dette er gullstandarden for personvern og verifisering, ettersom du validerer alle transaksjoner selv og ikke stoler på andres servere. Det krever imidlertid at du laster ned hele blokkjeden (~ 600 GB) og holder noden synkronisert.
 - Installer og synkroniser Bitcoin Core eller Knots
 - I Sparrow går du til **Verktøy → Innstillinger → Server**
 - Velg **Bitcoin Core eller Knots**, og skriv inn tilkoblingsdetaljene for noden din



- Privat Electrum Server (god balanse):** Vær vert for din egen Electrum-server (som Fulcrum eller Electrs) som er koblet til din Bitcoin Core- eller Knots-node. Tilbyr fullt personvern uten at du trenger å kjøre Sparrow på samme maskin som noden din.
 - Sett opp en Electrum-server som peker til Bitcoin Core- eller Knots-noden din
 - I Sparrow går du til **Verktøy → Innstillinger → Server**
 - Velg **Private Electrum**, og skriv inn serverens URL-adresse


For denne workshopen er det helt greit å bruke en **Public Electrum Server** for testnett-transaksjoner. I et produksjonsmiljø med ekte penger bør du vurdere å kjøre din egen node eller bruke en betrodd privat server for maksimalt personvern.


#### Alternativ 3: Blockstream Green Desktop App (hurtigstart)


Blockstream Green er programvaren for å fullføre oppsettet av JadeDIY, og den må være med skrivebordsversjonen



- Last ned den offisielle Blockstream-applikasjonen - dette er lenken til den fra nettstedet deres. Når du er der, klikker du på [Last ned nå] (https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Avhengig av hvor du laster ned, vil filen sannsynligvis ligge i nedlastingsmappen din. Sjekk der, og dobbeltklikk på den kjørbare filen for å installere programvaren.


![image](assets/fr/13.webp)



- Du må kanskje gi administratorrettigheter for å kjøre installasjonsprogrammet. Når du har gjort det, dukker det opp et vindu som skal se ut som på bildet nedenfor - klikk på **Neste**.


![image](assets/fr/14.webp)



- Velg hvor du vil at det installerte programmet skal ligge (sammen med de andre programmene eller et sted som er lett å finne), og klikk deretter på **Neste**.


![image](assets/fr/15.webp)



- Installasjonsprogrammet vil be om et snarveisnavn. Skriv inn et navn eller behold standardnavnet, og klikk deretter på **Neste**.


![image](assets/fr/16.webp)



- Hvis du vil ha en snarvei på skrivebordet, merker du av i boksen, ellers klikker du på **Neste**.


![image](assets/fr/17.webp)



- Til slutt klikker du på **Install** og venter noen minutter på at installasjonen skal fullføres.


![image](assets/fr/18.webp)



- Fremdriftslinjen skal fylles helt til slutten.


![image](assets/fr/19.webp)



- Når den er ferdig, vises en ny side - klikk på **Avslutt**.


![image](assets/fr/20.webp)



- Finn det nylig installerte Blockstream-programmet (eksempelet vises i Start-menyen i Windows 11).


![image](assets/fr/21.webp)



- Når du har funnet den, klikker du for å starte den - en startskjerm bør vises.


### Verifisere oppsettet ditt


Når du er koblet til Sparrow (eller en annen wallet-applikasjon):



- Sjekk adressene dine:** Sparrow vil vise mottakeradresser som er avledet fra seed-frasen din. Du kan bekrefte en adresse på Jade-enheten ved å gå til "Mottak"-fanen i Sparrow og klikke på "Vis Address" - adressen skal vises både på dataskjermen og på Jade-skjermen.



- Generer en mottakeradresse:** Klikk på fanen **Mottak** i Sparrow og kopier den første mottakeradressen i Bitcoin.



- Klar for transaksjoner:** Din maskinvare wallet er nå ferdig konfigurert og klar til å motta og signere Bitcoin-transaksjoner. Gå videre til neste avsnitt for å øve på å signere en testnet-transaksjon.



---

### Sjekkliste for hurtigoppsett



- Jade-fastvaren starter vellykket
- Ny wallet opprettet med 12-ords seed-frase
- Frøfrasen skrives ned tydelig og verifiseres
- USB-tilkoblingsmodus valgt
- Wallet-programvare (Sparrow) installert og tilkoblet
- Servertilkobling konfigurert (offentlig Electrum for mainnet)
- Første mottakeradresse generert og verifisert på enheten



---

**MIT License**


**Opphavsrett (c) 2025 Bitcoin-nettverket NYC**


Det gis herved tillatelse til enhver person som skaffer seg en kopi av denne programvaren og tilhørende dokumentasjonsfiler ("programvaren"), til å handle med programvaren uten begrensninger, inkludert, men ikke begrenset til, retten til å bruke, kopiere, endre, slå sammen, publisere, distribuere, viderelisensiere og/eller selge kopier av programvaren, og til å tillate personer som programvaren leveres til, å gjøre dette, på følgende vilkår:


Ovennevnte opphavsrettserklæring og denne tillatelseserklæringen skal inkluderes i alle kopier eller vesentlige deler av programvaren.


PROGRAMVAREN LEVERES "SOM DEN ER", UTEN NOEN FORM FOR GARANTI, VERKEN UTTRYKKELIG ELLER UNDERFORSTÅTT, INKLUDERT, MEN IKKE BEGRENSET TIL, GARANTIER FOR SALGBARHET, EGNETHET FOR ET BESTEMT FORMÅL OG IKKE-KRENKELSE AV RETTIGHETER. UNDER INGEN OMSTENDIGHETER SKAL FORFATTERNE ELLER OPPHAVSRETTSINNEHAVERNE VÆRE ANSVARLIGE FOR KRAV, SKADER ELLER ANNET ANSVAR, ENTEN DET GJELDER KONTRAKT, ERSTATNINGSANSVAR ELLER ANNET, SOM OPPSTÅR FRA, PÅ GRUNN AV ELLER I FORBINDELSE MED PROGRAMVAREN ELLER BRUK ELLER ANNEN OMGANG MED PROGRAMVAREN.


---