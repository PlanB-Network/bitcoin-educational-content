---
name: Samourai Wallet - Gjenoppretting
description: Hvordan gjenopprette bitcoins som er fast på Samourai Wallet?
---
![cover](assets/cover.webp)

Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er noen funksjoner i applikasjonen nå inoperative, og brukere som ikke har sin egen Dojo kan ikke lenger formidle transaksjoner.

Etter å ha hjulpet flere brukere med å gjenopprette deres bitcoins de siste dagene, tror jeg at jeg har støtt på de fleste problemene som kan oppstå under restaureringen av en Samourai Wallet. Derfor vil denne veiledningen starte med en situasjonsrapport for å identifisere funksjonalitetene som fortsatt er operative og de som ikke lenger er tilgjengelige innen Samourai Wallet-økosystemet og programvaren påvirket av denne hendelsen. Deretter vil vi gå frem steg for steg for å gjenopprette en Samourai Wallet ved hjelp av Sparrow Wallet-programvaren. Vi vil undersøke alle potensielle hindringer som oppstår under denne prosessen og se løsninger for å løse dem. Til slutt, i den siste delen, vil du oppdage de potensielle risikoene for ditt personvern etter serverbeslagleggelsen.

*En stor takk til [@Louferlou](https://twitter.com/Louferlou), som har hjulpet flere brukere med deres gjenoppretting og delt sine erfaringer med meg, og som også har bidratt til testing for å bestemme hva som fortsatt fungerer.*

## Fungerer Samourai Wallet fortsatt?

Ja, **Samourai Wallet-appen fungerer fortsatt**, men under visse forutsetninger.

For det første er det nødvendig at appen tidligere var installert på din smarttelefon. Google Play Store har fjernet appen, og APK-en var vert på det beslaglagte nettstedet. Derfor er det komplisert å installere Samourai for øyeblikket. Du kan finne APK-er på nettet, men jeg råder mot å laste dem ned med mindre du er sikker på kilden.

Ettersom Samourai Wallet-siden ikke lenger er tilgjengelig på Google Play Store, er det ikke mulig å deaktivere automatiske oppdateringer. Hvis appen returnerer til nedlastingsplattformene, ville det være klokt å **deaktivere automatiske oppdateringer** til mer informasjon er tilgjengelig angående utviklingen av saken.

Hvis Samourai Wallet allerede er installert på din smarttelefon, bør du fortsatt kunne få tilgang til appen. For å bruke lommebokfunksjonaliteten til Samourai, er det essensielt å koble til en Dojo. Tidligere var brukere uten en personlig Dojo avhengige av Samourais servere for å få tilgang til Bitcoin blockchain-informasjon og for å formidle transaksjoner. Med beslagleggelsen av disse serverne, kan ikke appen lenger få tilgang til denne dataen.
Hvis du ikke hadde en tilkoblet Dojo før, men har det nå, kan du sette den opp for å bruke Samourai-appen din igjen. Dette innebærer å sjekke sikkerhetskopiene dine, slette lommeboken (lommeboken, ikke applikasjonen), og gjenopprette lommeboken ved å koble Dojoen din til applikasjonen. For flere detaljer om disse stegene, kan du konsultere [denne veiledningen, i seksjonen "_Forberede din Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
Hvis din Samourai-app allerede var koblet til din egen Dojo, da fungerer lommebokdelen perfekt for deg. Du kan fortsatt se din saldo og formidle transaksjoner. Til tross for alt som skjer, tror jeg Samourai Wallet fortsatt er den beste mobile lommebokprogramvaren for øyeblikket. Personlig planlegger jeg å fortsette å bruke den.
Hovedproblemet du kan støte på er utilgjengeligheten av Whirlpool-kontoer fra appen. Vanligvis prøver Samourai å etablere en forbindelse med din Whirlpool CLI og starte coinjoin-syklusene før du får tilgang til disse kontoene. Men, siden denne forbindelsen ikke lenger er mulig, fortsetter appen å søke på ubestemt tid uten å noen gang gi deg tilgang til Whirlpool-kontoene. I dette tilfellet kan du gjenopprette disse kontoene på en annen lommebokprogramvare mens du kun beholder innskuddskontoen på Samourai.
### Hvilke verktøy er fortsatt tilgjengelige på Samourai?

På den andre siden er noen verktøy enten påvirket av servernedleggelsen eller helt utilgjengelige.

Når det gjelder individuelle utgiftsverktøy, fungerer alt normalt forutsatt, selvfølgelig, at du har din egen Dojo. Normale Stonewall-transaksjoner (og ikke Stonewall x2) fungerer uten problemer.

Kommentarer på Twitter har fremhevet at personvernet som tilbys av en Stonewall-transaksjon nå kan være redusert. Den tilleggsverdien av en Stonewall-transaksjon ligger i det faktum at den er uatskillelig fra en Stonewall x2-transaksjon når det gjelder struktur. Når en analytiker støter på dette spesifikke mønsteret, kan de ikke bestemme om det er en standard Stonewall med en enkelt bruker eller en Stonewall x2 som involverer to brukere. Imidlertid, som vi vil se i de følgende avsnittene, har gjennomføringen av Stonewall x2-transaksjoner blitt mer kompleks på grunn av utilgjengeligheten av Soroban. Noen tror derfor at en analytiker nå kan anta at enhver transaksjon med denne strukturen er en normal Stonewall. Personlig deler jeg ikke denne antagelsen. Selv om Stonewall x2-transaksjoner kan være mindre hyppige (og jeg tror de allerede var det før denne hendelsen), er det faktum at de fortsatt er mulige nok til å ugyldiggjøre en hel analyse basert på antagelsen om at de ikke er det.
**[-> Lær mer om Stonewall-transaksjoner.](https://planb.network/tutorials/privacy/stonewall)**
Når det gjelder Ricochet, har jeg ikke vært i stand til å verifisere om tjenesten fortsatt er operativ, på grunn av at jeg ikke eier en Dojo på Testnet, og jeg foretrekker å ikke risikere å bruke `100 000 sats` mot en lommebok som kunne være kontrollert av myndighetene. Hvis du har hatt muligheten til å teste dette verktøyet nylig, inviterer jeg deg til å kontakte meg slik at vi kan oppdatere denne artikkelen.

Hvis du trenger å bruke Ricochet, vær oppmerksom på at du alltid kan utføre denne operasjonen manuelt med hvilken som helst lommebokprogramvare. For å lære hvordan du manuelt utfører de forskjellige hoppene på riktig måte, anbefaler jeg å konsultere denne andre artikkelen: [**RICOCHET**](https://planb.network/tutorials/privacy/ricochet).

JoinBot-verktøyet er ikke lenger operativt, da det var helt avhengig av deltakelsen fra en lommebok forvaltet av Samourai.

Når det gjelder andre typer samarbeidstransaksjoner, ofte referert til som "cahoots," forblir de mulige, men kun manuelt. Før servernedleggelsen hadde du to alternativer for å utføre Stonewall x2 eller Stowaway (PayJoin) transaksjoner:
- Bruk Soroban-nettverket for automatisk og eksternt å utveksle PSBT-ene;
- Eller utfør disse utvekslingene manuelt ved å skanne flere QR-koder.

Etter flere tester viser det seg at Soroban ikke lenger fungerer. For å utføre disse samarbeidstransaksjonene må datautvekslingen derfor gjøres manuelt. Her er to alternativer for å utføre denne utvekslingen:
- Hvis du fysisk er nær din samarbeidspartner, kan du skanne QR-kodene etter hverandre;
- Hvis du er langt unna din samarbeidspartner, kan dere utveksle PSBT-ene via en ekstern kommunikasjonskanal til applikasjonen. Men vær forsiktig, da dataene som er inneholdt i disse PSBT-ene er sensitive med tanke på personvern. Jeg anbefaler å bruke en kryptert meldingstjeneste for å sikre konfidensialiteten til utvekslingen.
**[-> Lær mer om Stonewall x2-transaksjoner.](https://planb.network/tutorials/privacy/stonewall-x2)**

**[-> Lær mer om Stowaway-transaksjoner.](https://planb.network/tutorials/privacy/payjoin-samourai-wallet)**

Når det gjelder Whirlpool, ser protokollen ikke ut til å fungere lenger, selv for brukere som har sin egen Dojo. Jeg har overvåket min RoninDojo de siste dagene og forsøkt noen grunnleggende manipulasjoner, men Whirlpool CLI har ikke klart å koble til siden servernedleggelsen.

Jeg forblir likevel håpefull om at denne protokollen kan reaktiveres eller kanskje tenkes nytt på en annen måte i de kommende ukene, avhengig av hvordan situasjonen utvikler seg. Denne pausen kan være en mulighet til å utforske nye tilnærminger eller potensielle forbedringer til dette systemet.
### Hvilke eksterne verktøy er fortsatt tilgjengelige?
Når det gjelder andre verktøy relatert til Samourai-miljøet, er noen fortsatt tilgjengelige mens andre ikke er det.

Den gratis kjedeanalyse nettsiden OXT.me er dessverre ikke tilgjengelig for øyeblikket.

Whirlpool Stats Tool er ikke lenger tilgjengelig for nedlasting, da det var vert på Samourais GitLab. Selv om du tidligere hadde lastet ned dette Python-verktøyet lokalt på maskinen din, eller hvis det var installert på din RoninDojo-node, vil WST ikke fungere for øyeblikket. Faktisk var det avhengig av data levert av OXT.me for sin drift, og dette nettstedet er ikke lenger tilgjengelig. For øyeblikket er WST ikke spesielt nyttig siden Whirlpool-protokollen er inaktiv.

Nettstedet KYCP.org er for øyeblikket ikke lenger tilgjengelig.

GitLab som hostet koden for Boltzmann Calculator Python-verktøyet har også blitt beslaglagt. For øyeblikket er det derfor ikke mulig å laste ned dette verktøyet. Men hvis du har en RoninDojo, kan du fortsette å bruke Boltzmann Calculator på samme måte som før.

Når det gjelder RoninDojo, fortsetter denne node-i-boks programvaren å fungere korrekt til tross for utilgjengeligheten av visse spesifikke verktøy som Whirlpool CLI og WST. Den kan fortsatt brukes for annen lommebokprogramvare takket være Fulcrum eller Electrs. Hvis du ønsker å få mer informasjon om RoninDojo eller hvis du har spesifikke spørsmål, oppfordrer jeg deg til å bli med i [deres Telegram-gruppe](https://t.me/RoninDojoNode).

Kildekoden for RoninDojo er imidlertid for øyeblikket ikke lenger tilgjengelig, da den var vert på Samourais GitLab. Det er derfor ikke mulig å manuelt installere den på en Raspberry Pi for øyeblikket.

Når det gjelder programvaren for watch-only lommebok Sentinel, er situasjonen lik den for Samourai-appen. Hvis du har din egen Dojo, kan du fortsette å bruke Sentinel uten problemer. Men hvis du ikke har en Dojo, vil du ikke lenger kunne etablere en forbindelse. I motsetning til Samourai, er Sentinel-nettstedet fortsatt tilgjengelig online. Men vær forsiktig med dette nettstedet og APK-en som tilbys der, da det er uklart hvem som for øyeblikket kontrollerer disse ressursene.

### Er Sparrow Wallet påvirket?
Sparrow Wallet fortsetter å fungere normalt, med unntak av Samourai-verktøy som ikke lenger er tilgjengelige. For øyeblikket er det ikke lenger mulig å utføre coinjoins via Sparrow. På samme måte er verktøy for samarbeidsutgifter ikke lenger tilgjengelige, ettersom Sparrow ikke tilbyr muligheten for manuell utveksling av PSBTs, i motsetning til Samourai. For alle andre funksjoner opererer Sparrow uten problemer. Du kan også bruke denne programvaren til å gjenopprette en Samourai-lommebok om nødvendig.

## Hvordan gjenopprette en Samourai-lommebok?
Som vi har sett i de foregående avsnittene, hvis du eier din egen Dojo, er det ikke nødvendigvis påkrevd å bytte programvare. **Samourai forblir et utmerket valg av hot wallet** for dine daglige utgifter. Imidlertid, hvis du ikke har en Dojo eller hvis du foretrekker å velge en annen programvare, vil jeg forklare den komplette gjenopprettingsprosessen, og detaljere eventuelle potensielle hindringer du kan møte.

I alle tilfeller er det viktig å ta seg tid og sørge for ikke å gjøre noen feil. Husk, det haster ikke, ettersom du holder dine private nøkler, og beslagleggelsen av Samourais servere påvirker ikke dette på noen måte. Uansett hva som skjer, kan de åpenbart ikke få tilgang til dine private nøkler.

### Verifiser passfrasen

For å gjenopprette lommeboken din, må du ha passfrasen din, selv om du velger gjenoppretting via sikkerhetskopifilen. Start med å verifisere gyldigheten av denne passfrasen. Åpne Samourai Wallet-appen din, klikk på Paynym-ikonet øverst til venstre, og velg deretter `Innstillinger`.

![samourai](assets/1.webp)

Deretter klikker du på `Feilsøking` og deretter på `Passfrase/backup test`.

![samourai](assets/2.webp)

Skriv inn passfrasen din og klikk `Ok`. Hvis den er korrekt, vil Samurai bekrefte det. Du har også muligheten til å verifisere sikkerhetskopifilen hvis du planlegger å bruke den senere.

![samourai](assets/3.webp)

Dette trinnet er valgfritt, men anbefales. Det bekrefter at passfrasen er korrekt, og eliminerer en potensiell kilde til problemer senere. Hvis Samourai indikerer at passfrasen er feil på dette stadiet, vil gjenoppretting ikke være mulig. Sørg for at du har skrevet inn passfrasen riktig og sjekk den igjen.

### Alternativ 1: Gjenopprett lommeboken på Sparrow med sikkerhetskopifilen

Siden versjon 1.8.6 av Sparrow Wallet, er det mulig å direkte importere Samourai-lommeboken din ved hjelp av sikkerhetskopitekstfilen med navn `samourai.txt`, som applikasjonen din automatisk genererer. Denne filen inneholder all nødvendig informasjon for å gjenopprette lommeboken din og er kryptert med passfrasen din for sikkerhet.

Hvis du velger dette alternativet, trenger du din oppdaterte `samourai.txt`-fil og passfrasen din. For å generere denne filen på Samourai Wallet, klikk på de tre små prikkene øverst til høyre, og velg deretter `Eksporter lommebokbackup`.

![samourai](assets/4.webp)
Deretter velger du `Eksporter til utklippstavle`. Etter det må du overføre denne filen til PC-en din på en sikker måte. Siden filen er kryptert, men passfrasen alene er tilstrekkelig for å dekryptere den, er det viktig å ta forholdsregler under overføringen. Hvis du velger en direkte overføring som ren tekst, må du opprette en `samourai.txt`-fil på PC-en din og lime inn innholdet fra utklippstavlen i den. Et alternativ ville være å direkte hente `samourai.txt`-filen fra filene som er lagret på telefonen din.
Når du har tilgang til filen på PC-en din, åpner du Sparrow Wallet, klikker på `Fil`-fanen, og velger `Importer lommebok` for å starte importen av lommeboken din.

![samourai](assets/5.webp)
Rull ned til `Samourai Backup`, klikk på `Import File`, og velg deretter din `samourai.txt`-fil.
![samourai](assets/6.webp)

Sparrow vil deretter be deg om et passord for å dekryptere filen. Dette passordet er faktisk din passfrase. Skriv den inn i det tilsvarende feltet og klikk på `Import`.

![samourai](assets/7.webp)

Hvis lommeboken din ikke vises på dette stadiet, er det mulig at du gjorde en feil når du kopierte `samourai.txt`-filen eller når du skrev inn passfrasen. Du kan konsultere feilsøkingsdelen for mer hjelp.

![samourai](assets/8.webp)

For skripttypen, hvis du ikke har konfigurert andre skript i Samourai, bør du normalt bare bruke SegWit V0 (Native SegWit / P2WPKH). Behold dette standard skriptet og klikk på `Import`.

![samourai](assets/9.webp)

Navngi lommeboken din, for eksempel "Samourai Recovery", og klikk deretter på `Create Wallet`.

![samourai](assets/10.webp)

Sparrow vil deretter be deg om å velge et passord. Dette passordet beskytter kun tilgangen til lommeboken din på denne PC-en og har ikke noe å gjøre med avledningen av lommebokens nøkler. Sørg for å velge et sterkt passord, noter det ned for å huske det, og klikk på `Set Password`.

![samourai](assets/11.webp)

Sparrow vil deretter avlede nøklene til lommeboken din og søke etter de tilsvarende transaksjonene.

![samourai](assets/12.webp)

For nå er kun innskuddskontoen din tilgjengelig. Hvis du kun brukte Samourai for denne kontoen, bør du se alle midlene dine. Men, hvis du også brukte Whirlpool, må du avlede `premix`, `postmix`, og `badbank`-kontoene. På Sparrow, klikk enkelt på `Settings`-fanen, deretter på `Add Accounts...`.

![samourai](assets/13.webp)
I vinduet som åpnes, velg `Whirlpool Accounts` fra nedtrekksmenyen, og klikk deretter på `OK`.
![samourai](assets/14.webp)

Du vil da se dine ulike Whirlpool-kontoer dukke opp, og Sparrow vil avlede de nødvendige nøklene for å bruke de tilknyttede bitcoinene.

![samourai](assets/15.webp)

Hvis du bruker en annen programvare enn Sparrow, som Electrum, for å gjenopprette din Samourai-lommebok, her er Whirlpool-konto indeksene for manuell gjenoppretting:
- Innskudd: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Du har nå tilgang til dine bitcoins på Sparrow. Hvis du trenger hjelp med å bruke Sparrow Wallet, kan du også sjekke ut [vår dedikerte opplæring](https://planb.network/tutorials/wallet/sparrow).

Jeg anbefaler også å manuelt importere etikettene du hadde assosiert med dine UTXOer på Samourai. Dette vil tillate deg å utføre effektiv myntkontroll på Sparrow etterpå.

### Alternativ 2: Gjenopprett lommeboken på Sparrow med den mnemoniske frasen

Hvis du ikke ønsker å utføre gjenopprettingen med sikkerhetskopifilen, kan du velge en mer tradisjonell metode ved ganske enkelt å bruke din 12-ords gjenopprettingsfrase og din passfrase. Dette andre alternativet er ofte enklere.
For å starte, sørg for at du har din gjenopprettingsfrase og ditt passord tilgjengelig. Deretter, åpne Sparrow Wallet-programvaren, klikk på `File`-fanen, og velg `Import Wallet` for å begynne importeringen av lommeboken din.
![samourai](assets/16.webp)

Velg `Mnemonic Words (BIP39)` og, i nedtrekksmenyen, klikk på `Use 12 Words`.

![samourai](assets/17.webp)

Skriv inn de 12 ordene fra din gjenopprettingsfrase i riktig rekkefølge.

![samourai](assets/18.webp)

Hvis Sparrow viser en `Invalid Checksum`-melding, indikerer dette at kontrollsummen for gjenopprettingsfrasen ikke er gyldig, noe som sannsynligvis betyr at du gjorde en feil når du tastet inn ordene.

![samourai](assets/19.webp)

Hvis frasen din er korrekt, merk av for `Use Passphrase?`-boksen og skriv inn ditt passord i det dedikerte feltet. Til slutt, hvis alt ser riktig ut, klikk på `Discover Wallet`-knappen.

![samourai](assets/20.webp)

Navngi lommeboken din, for eksempel "Samourai Recovery", og klikk deretter på `Create Wallet`.

![samourai](assets/21.webp)
Sparrow vil deretter be deg om å velge et passord. Dette passordet beskytter kun tilgangen til lommeboken din på denne PC-en og er ikke relatert til utledningen av lommebokens nøkler. Sørg for å velge et sterkt passord, skriv det ned for å huske det, og klikk på `Set Password`.
![samourai](assets/22.webp)

Sparrow vil deretter utlede nøklene for lommeboken din og søke etter tilsvarende transaksjoner.

![samourai](assets/23.webp)

Hvis lommeboken din ikke vises på dette stadiet, er det mulig at du gjorde en feil når du tastet inn passordet eller gjenopprettingsfrasen. Du kan konsultere den dedikerte feilsøkingsseksjonen for mer hjelp.

For nå er kun din innskuddskonto tilgjengelig. Hvis du kun brukte Samourai for denne kontoen, bør du se alle dine midler. Men, hvis du også brukte Whirlpool, må du utlede `premix`, `postmix`, og `badbank`-kontoene. På Sparrow, klikk enkelt på `Settings`-fanen, deretter på `Add Accounts...`.

![samourai](assets/24.webp)

I vinduet som åpnes, velg `Whirlpool Accounts` fra nedtrekkslisten, og klikk deretter på `OK`.

![samourai](assets/25.webp)

Du vil da se dine ulike Whirlpool-kontoer dukke opp, og Sparrow vil utlede de nødvendige nøklene for å bruke de tilknyttede bitcoins.

![samourai](assets/26.webp)

Hvis du bruker en annen programvare som Electrum for å gjenopprette din Samourai-lommebok, her er Whirlpool-konto indeksene for manuell gjenoppretting:
- Innskudd: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Du har nå tilgang til dine bitcoins på Sparrow. Hvis du trenger hjelp med å bruke Sparrow Wallet, kan du også konsultere [vår dedikerte opplæring](https://planb.network/tutorials/wallet/sparrow).

Jeg anbefaler også manuelt å importere etikettene du hadde assosiert med dine UTXOs på Samourai. Dette vil tillate deg å utføre effektiv myntkontroll på Sparrow etterpå.

### Hva er de vanlige problemene som oppstår?
Etter å ha assistert flere personer de siste dagene, tror jeg at jeg har støtt på de fleste problemene som kan forhindre gjenopprettingen av lommeboken din. Hvis du fortsatt ikke kan få tilgang til lommeboken din til tross for de tidligere veiledningene, her er noen ytterligere anbefalinger. Først og fremst, for at gjenopprettingen skal fungere, er det helt essensielt at gjenopprettingsfrasen er korrekt. Hvis du ikke klarer å finne din 12-ords frase, kan du bruke *alternativ 1* for å gjenopprette fra Samourais sikkerhetskopifil. Du kan også få tilgang til gjenopprettingsfrasen din direkte i Samourai Wallet ved å navigere til `Innstillinger`, deretter `Lommebok`, og til slutt velge `Vis 12-ords gjenopprettingsfrase`.

Videre vil en skrivefeil i passfrasen din under gjenoppretting resultere i feil avledede nøkler, som vil forhindre gjenopprettingen av lommeboken din på Sparrow. **Passfrasen må være helt nøyaktig!**

For å løse dette, råder jeg deg først til å sjekke gyldigheten av passfrasen din i Samourai-applikasjonen som beskrevet i "_Verifiser passfrasen_"-delen av denne artikkelen:
1. **Validering i Samourai:** Hvis Samourai bekrefter at passfrasen er korrekt, prøv gjenopprettingen på nytt fra begynnelsen, og sørg for å nøyaktig taste inn passfrasen i Sparrow uten feil;
2. **Feil i Passfrase:** Hvis Samourai indikerer at passfrasen er feil, er det meningsløst å fortsette forsøk på Sparrow. Så lenge den korrekte passfrasen ikke er funnet, er gjenopprettingen av lommeboken din umulig. Hvis du har permanent mistet passfrasen din, hold Samourai-applikasjonen din trygg. Alt du kan gjøre er å håpe at serverne blir startet på nytt slik at du kan gjøre utgifter direkte fra applikasjonen uten å trenge gjenoppretting. **Ikke forsøk å koble til en Dojo i dette tilfellet**, da dette ville innebære å tilbakestille lommeboken din på Samourai, noe som krever tilgang til passfrasen.

Blant andre møtte feil, mange er relatert til nettverkskonfigurasjonen på Sparrow.

Først, sørg for at Sparrow er riktig konfigurert i `mainnet`-modus i stedet for i `testnet`-modus. Faktisk, hvis Sparrow søker etter transaksjonene dine på Testnet, vil den finne ingenting, fordi lommeboken din er på Mainnet. Testnet er en alternativ versjon av Bitcoin, brukt utelukkende for testing og utvikling, og opererer på et separat nettverk fra hovednettverket (Mainnet), med egne blokker og transaksjoner. For å sjekke hvilket nettverk du er på, klikk på `Verktøy`-fanen, deretter på `Start på nytt i`. Hvis `Mainnet`-alternativet vises, da er du ikke på hovednettverket. Velg det for å starte Sparrow på nytt på Mainnet, og begynn deretter gjenopprettingsprosessen din på nytt.

![samourai](assets/27.webp)
Noen har også møtt vanskeligheter med å koble Sparrow til noden sin. Nederst til høyre på Sparrow indikerer en farget bryter om programvaren din er riktig koblet til en Bitcoin-node. For å hente dine Samourai-transaksjoner, er det essensielt at programvaren er godt koblet. Sjekk at bryteren er aktivert, som på bildet mitt nedenfor (gul for en offentlig node, grønn for Bitcoin Core, og blå for en Electrum-server).
![samourai](assets/28.webp)

Hvis bryteren ikke er aktivert, klikk på den for å reaktivere tilkoblingen.

![samourai](assets/29.webp)

Hvis problemet vedvarer, her er noen mulige løsninger:
- Hvis du prøver å koble til din egen Electrum-server (blå) eller din Bitcoin Core (grønn) og Sparrow ikke kan koble til, sjekk tilkoblingsinformasjonen under `Fil > Innstillinger... > Server`;

![samourai](assets/30.webp)
- Hvis tilkoblingsproblemet vedvarer, kan det skyldes en ufullstendig synkronisering av noden din. Sørg for at noden din og indeksereren din er 100% synkronisert. Om nødvendig som en siste utvei, koble fra noden din fra Sparrow og koble til en offentlig node; - Hvis du allerede var koblet til en offentlig node og tilkoblingen mislykkes, prøv å endre noden ved å velge en annen fra rullegardinlisten.

![samourai](assets/31.webp)

Hvis du har lykkes med å gjenopprette lommeboken din, men den virker ufullstendig, kan det være et problem relatert til avledning.

Et problem kan oppstå hvis du brukte din Samourai innskuddskonto med en annen skripttype enn `P2WPKH`. Som standard bruker Samourai denne skripttypen, men hvis du manuelt har endret den, må du også justere dette når du gjenoppretter på Sparrow.

For å avlede grener for andre skripttyper, må du gjenta gjenopprettingsprosessen for hver skripttype som er brukt. For dette, gå til `File > New Wallet` på Sparrow, velg en annen skripttype fra rullegardinlisten, klikk på `New or Imported Software Wallet`, og følg de samme trinnene som i den opprinnelige veiledningen.

![samourai](assets/32.webp)

Et annet avledningsproblem jeg støtte på er relatert til Gap Limit-verdien. Denne verdien forteller Sparrow etter hvor mange tomme adresser den skal slutte å avlede nye adresser. Hvis du etter gjenoppretting merker at noen transaksjoner mangler, kan dette skyldes en for lav Gap Limit. For å løse dette, gå til kontoen som forårsaker problemet, for eksempel postmix-kontoen (hvis flere kontoer er berørt, gjenta denne operasjonen for hver).

![samourai](assets/33.webp)

Klikk på `Settings`-fanen og deretter på `Advanced...`-knappen.
![samourai](assets/34.webp)
Øk gradvis verdien av Gap Limit, for eksempel satte jeg den til `400` her. Deretter klikker du på `Close`-knappen.

![samourai](assets/35.webp)

Klikk på `Apply` for å fullføre. Sparrow vil da avlede et større antall adresser og søke etter midler på dem, noe som bør hjelpe med å gjenopprette alle transaksjonene dine.

![samourai](assets/36.webp)

Det dekker de ulike gjenopprettingsproblemene jeg har støtt på de siste dagene. Hvis du, etter å ha prøvd alle disse løsningene, fortsatt har problemer, inviterer jeg deg til å bli med i [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) for å be om hjelp. Jeg besøker regelmessig denne Discord og ville være glad for å hjelpe hvis jeg har løsningen. Andre bitcoinere vil også kunne dele sine erfaringer og tilby sin assistanse. **Uansett er det avgjørende å holde gjenopprettingsfrasen, sikkerhetskopifilen og passfrasen din konfidensiell**. Ikke del dem med noen, da dette kan tillate dem å stjele dine bitcoins.

Når gjenopprettingen er fullført, har du nå tilgang til dine bitcoins. Det er en god ting, men det er kanskje ikke nok. Faktisk reiser beslagleggelsen av servere nye potensielle risikoer for ditt personvern. I følgende avsnitt vil vi undersøke disse risikoene i detalj og skissere forholdsregler for å beskytte ditt personvern.

## Hva er konsekvensene for personvernet til transaksjonene dine?

### Som en Samourai-bruker uten Dojo

Hvis du brukte Samourai Wallet uten å ha koblet til din egen Dojo, måtte xpubs dine kommuniseres til Samourais servere for at appen skulle fungere. Med beslagleggelsen av disse serverne er det mulig at myndighetene nå har tilgang til disse xpubs.
Dette scenarioet forblir hypotetisk. Vi vet ikke om disse xpubs ble registrert, om eventuell lagring ble ødelagt, om myndighetene har gjenopprettet dem, og om de planlegger å bruke dem for kjedeanalyse. Imidlertid, i en slik situasjon, er det klokt å vurdere det verste scenarioet, der myndighetene har xpubs til brukere som ikke koblet til sin egen Dojo. Til referanse, en xpub er en streng med tegn som inneholder alle nødvendige elementer for å generere barn offentlige nøkler (offentlig nøkkel + kjedekode). Den brukes i hierarkiske deterministiske lommebøker for å generere mottaksadresser og observere transaksjoner på en konto uten å eksponere de tilknyttede private nøklene. Dette tillater, for eksempel, opprettelsen av en "kun-observasjon" lommebok. Imidlertid kan avsløring av xpubs kompromittere brukerens personvern, ettersom de tillater tredjeparter å spore transaksjoner og se saldoene til tilknyttede kontoer.
Alle som kjenner dine xpubs kan dermed se alle mottaksadressene til lommeboken din, de som ble brukt i fortiden, og de som vil bli generert i fremtiden.

For brukere uten en Dojo, har en potensiell lekkasje av dine xpubs to store konsekvenser:
- Coinjoins du kanskje har utført blir ineffektive fra et personvernperspektiv for alle som kjenner dine xpubs, dermed mister myntene dine all anonset;
- Denne personen kan også spore alle mottaksadressene til din Samourai Wallet.

Det er derfor viktig å vurdere det verste scenarioet og å skille lag med denne lommeboken, potensielt kompromittert i form av personvern. For å gjøre dette, opprett en ny lommebok fra bunnen av med en annen programvare, som Sparrow Wallet. Etter å ha verifisert gyldigheten av dine sikkerhetskopier, overfør alle dine midler ved å gjøre transaksjoner. Selv om denne operasjonen ikke bryter sporingssammenhengen til myntene dine, vil det forhindre myndighetene fra å vite med sikkerhet adressene til din nye lommebok.

Under denne overføringsoperasjonen, anbefaler jeg å unngå konsolidering av dine mynter. Hvis vi antar at dine xpubs er kompromittert, vil konsolidering ikke ha noen innvirkning fra synspunktet til personen som har tilgang til disse xpubs, siden ditt personvern allerede er kompromittert med dem. Imidlertid, råder jeg deg til ikke å konsolidere dine mynter for mye hovedsakelig for å beskytte ditt personvern fra andre mennesker. I verste fall, kan kun myndighetene ha tilgang til dine xpubs, men resten av verden vet ikke om dem. Dermed, fra synspunktet til andre, kan konsolidering av dine mynter betydelig skade ditt personvern på grunn av Common Input Ownership Heuristic (CIOH).

Til slutt, for å definitivt bryte sporingen, vurder også å utføre coinjoins fra denne nye lommeboken.
**Advarsel:** Det er ikke nok å bare hente din Samourai lommebok på Sparrow Wallet. Det er nødvendig å opprette en helt ny lommebok med en ny gjenopprettingsfrase hvis du vil unngå å bruke xpubs som kan ha lekket. Hvis du importerer din eksisterende seed til Sparrow, endrer du bare lommebokforvaltningsprogramvaren, men lommeboken forblir den samme.

### Som en bruker av Sparrow eller Samourai med Dojo

Hvis lommeboken din kun er forvaltet på Sparrow Wallet, kunne dine xpubs ikke ha lekket, enten du bruker en offentlig node eller din egen Bitcoin node. På samme måte, hvis du bruker Samourai-appen og alltid har koblet denne appen til din egen Dojo siden opprettelsen av lommeboken din, er dine xpubs også sikre.
Men, hvis du har brukt samme lommebok i en periode **uten din egen Dojo** og deretter med din egen Dojo, er det mulig at Samourai-serverne kan ha hatt tilgang til dine xpubs, og derfor kan myndighetene kjenne dem. Hvis du er i denne spesifikke situasjonen, råder jeg deg til å følge anbefalingene fra forrige avsnitt og vurdere dine xpubs som kompromitterte.
For de som alltid har brukt Sparrow eller Samourai med sin egen Dojo, er hovedrisikoen at anonsettene til myntene dine potensielt kan bli redusert. Anta, i verste fall, at alle brukere uten en Dojo har sine xpubs i hendene på myndighetene, da kan veien til myntene deres gjennom coinjoin-syklusene spores av disse myndighetene.

For å illustrere dette, la oss ta et konkret eksempel. Forestill deg at du deltok i en første syklus av coinjoin, etterfulgt av to ytterligere nedstrøms coinjoin-sykluser. Hvis xpubs til brukere uten en Dojo ikke har lekket, da ville det fremtidige anonsettet til mynten din være 13.

![samourai](assets/37.webp)

Men, hvis vi antar at xpubs har lekket og at du møtte en bruker uten dojo under den innledende coinjoin, og deretter 2 under den første nedstrøms coinjoin, da ville ditt fremtidige anonsett kun være 10 i stedet for 13 fra myndighetenes synspunkt.

![samourai](assets/38.webp)
Dette potensielle fallet i anonsett er komplekst å kvantifisere, da det avhenger av mange faktorer, og hver mynt påvirkes forskjellig. For eksempel, en bruker uten Dojo møtt i de tidlige syklusene påvirker det fremtidige anonsettet mye mer enn en møtt i de senere syklusene. For å gi deg en ide om situasjonen, som forblir hypotetisk, indikerte de siste statistikkene levert av Samourai at mellom 85% og 90% av myntene involvert i coinjoins kom fra brukere med Dojo, Sparrow, eller Bitcoin Keeper, det vil si brukere som, selv i verste fall, ikke ville ha sett sine xpubs lekket.
Selv om disse tallene er vanskelige å verifisere, virker de konsistente for meg av to grunner:
- Sparrow Wallet er mye brukt;
- De fleste node-i-boks-programvare tilbyr Dojo-implementeringer, og disse mainstream-programvarene som Umbrel er veldig populære for tiden.

Dermed må flere aspekter vurderes. Hvis personvernet til myntene dine vis-à-vis myndighetene er ekstremt viktig for deg, ville det være klokt å forberede seg på det verste scenarioet, og det er vanskelig å garantere 100% at dine Whirlpool coinjoin-sykluser ikke kunne spores på grunn av det potensielle lekket av xpubs fra brukere uten Dojo. Selv om denne antagelsen er høyst usannsynlig, er den ikke umulig.

På den annen side, hvis personvernet til myntene dine vis-à-vis myndigheten potensielt i besittelse av disse xpubs ikke er avgjørende for deg, da kan situasjonen vurderes annerledes.

Jeg spesifiserer "vis-à-vis myndigheten" fordi det er viktig å huske på at kun myndigheten som beslagla serverne potensielt er klar over disse xpubs. Hvis målet ditt med å bruke coinjoin var å forhindre at bakeren din kunne følge pengene dine, da er han ikke bedre informert enn før serverbeslaget.
Til slutt er det essensielt å vurdere den opprinnelige anonseten til mynten din, før serverbeslagleggelsen. La oss ta eksempelet med en mynt som hadde nådd en forventet anonset på 40 000; den potensielle reduksjonen i denne anonseten er sannsynligvis ubetydelig. Faktisk, med en allerede veldig høy grunnleggende anonset, er det usannsynlig at tilstedeværelsen av noen få brukere uten Dojo kunne radikalt endre situasjonen. Imidlertid, hvis mynten din hadde en anonset på 40, så kunne denne potensielle lekkasjen alvorlig påvirke dine anonseter og potensielt tillate sporing. Med WST-verktøyet nå ute av tjeneste etter nedleggelsen av OXT.me, kan du bare estimere disse anonsetene. For den retrospektive anonseten, er det ikke så mye å bekymre seg for siden Whirlpool-modellen sikrer at den er veldig høy fra den første coinjoin, takket være arven fra dine jevnaldrende. Det eneste tilfellet hvor dette kunne utgjøre et problem er hvis mynten din ikke har blitt remixet på flere år og den ble blandet i begynnelsen av en pools lansering. Når det gjelder den forventede anonseten, kan du undersøke varigheten mynten din har vært tilgjengelig for coinjoins. Hvis det har vært flere måneder, så har den sannsynligvis en ekstremt høy forventet anonset. Omvendt, hvis den ble lagt til i en pool bare noen timer før serverne ble beslaglagt, så er dens forventede anonset sannsynligvis veldig lav.
[**-> Lær mer om anonseter og deres beregningsmetode.**](https://planb.network/tutorials/privacy/wst-anonsets)

Et annet aspekt å vurdere er effekten av konsolideringer på anonsetene til mynter som har blitt blandet. Gitt at Whirlpool-kontoer ikke lenger er tilgjengelige via Samourai-appen, er det sannsynlig at mange brukere har overført lommeboken sin til annen programvare og forsøkt å ta ut midlene sine fra Whirlpool. Spesielt sist helg, da transaksjonsgebyrene på Bitcoin-nettverket var relativt høye, var det en sterk teknisk og økonomisk insentiv til å konsolidere post-mix mynter. Dette betyr at det er sannsynlig at mange brukere har gjort betydelige konsolideringer.

Problemet med disse post-mix konsolideringene er at de alltid reduserer anonsetene, ikke bare for brukeren som utfører dem, men også for brukerne de møtte under sine coinjoin-sykluser. Selv om jeg ikke har vært i stand til å verifisere eller kvantifisere dette fenomenet nøyaktig, kan de økonomiske insentivene knyttet til transaksjonsgebyrer på den tiden lede oss til å anta at anonsetene potensielt er lavere.

### Som en Sentinel-bruker

Nettverksoperasjonen til watch-only lommebokapplikasjonen Sentinel er lik den til Samourai. For å få tilgang til lommebokinformasjonen din, må applikasjonen overføre xpubs, offentlige nøkler og adresser du har oppgitt til en Dojo. Hvis du alltid har brukt din egen Dojo på Sentinel, er det ingen problem, og du kan fortsette å bruke applikasjonen uten bekymringer. Imidlertid, hvis du var avhengig av Samourais servere for din Sentinel, er det mulig at dine xpubs har blitt eksponert. I dette tilfellet er det tilrådelig å følge samme lommebokbytteprosess som anbefales for Samourai Wallet når den er koblet til Samourais servere.

I det usannsynlige tilfellet at du brukte din Dojo med Samourai, men ikke med Sentinel, ville det være klokere å vurdere at dine xpubs er kompromittert.

## Konklusjon
Takk for at du leste denne artikkelen til slutten. Hvis du mener at det mangler informasjon eller hvis du har forslag, nøl ikke med å kontakte meg for å dele dine tanker. I tillegg, hvis du trenger ytterligere hjelp til å gjenopprette din Samourai Wallet til tross for denne veiledningen, inviterer jeg deg til å bli med i [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) for å be om hjelp. Jeg besøker regelmessig denne Discord og ville være glad for å assistere deg hvis jeg har løsningen. Andre bitcoinere vil også kunne dele sine erfaringer og tilby sin støtte. **Uansett er det essensielt å holde din gjenopprettingsfrase, din sikkerhetskopi-fil, og din passfrase konfidensiell**. Ikke del dem med noen, da dette kunne muliggjøre for dem å stjele dine bitcoins.