---
name: Green Wallet

description: Oppsett og Brukerveiledning (CC Bistack)
---

![cover](assets/cover.webp)

Hot Mobile Wallet - Nybegynner - Gratis - For å sikre fra 0 til 1 000 €

For å sikre beløp under 1 000 €, er en gratis hot wallet (tilkoblet internettet) perfekt for nybegynnere. Oppsettet er enkelt, og grensesnittet er designet for nybegynnere.

Hvis du vil besøke deres nettside, klikk her (https://blockstream.com/green/)!

## Videoopplæring

![green wallet opplæringsvideo](https://www.youtube.com/watch?v=lONbCS31am4)

## Skriftlig Opplæring

> Denne veiledningen ble produsert og tilhører Bitstack. Bitstack er en bitcoin neo-bank basert i Paris som tillater DCA på bitcoin. Veiledning skrevet av Loic Morel den 15/02/2023. Dette tilhører dem. https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet

![bilde](assets/0.webp)

Hvordan Installere Din Første Bitcoin Wallet? Green Wallet Opplæring

Hvis du ønsker å dra nytte av de mange fordelene med Bitcoin-systemet, inkludert usensurerbarheten og ubeslagleggbarheten av dine midler, må du personlig holde nøklene som gir tilgang til dine bitcoins.

I denne opplæringen vil jeg forklare hvordan du setter opp din første lommebok med Green Wallet. Dette programmet er spesielt egnet for nybegynnerbrukere. Det er veldig enkelt å bruke, selv om du ikke har avansert kunnskap om Bitcoin.

Green Wallet er tilgjengelig på alle typer enheter. I denne opplæringen vil vi se hvordan man bruker den på mobil, men du kan også laste den ned på en datamaskin.

Det første steget er selvfølgelig å laste ned Green Wallet-programvaren eller applikasjonen. Hvis du er på mobil, kan du enkelt laste den ned fra din butikk. Sørg for at du er på den offisielle applikasjonsnedlastingssiden. Her er sidene avhengig av systemet ditt:

> - Google Play Store
>
> - Apple App Store

Hvis du laster ned programvaren på en datamaskin, anbefaler jeg sterkt at du verifiserer autentisiteten og integriteten til binærfilen før du installerer den på maskinen din. Jeg vil forklare hvordan du utfører denne operasjonen i en fremtidig opplæring.

## Velge Applikasjonsinnstillinger

Når du starter applikasjonen, vil du komme til hjemmeskjermen. For øyeblikket har du ingen lommebøker. Senere, hvis du har opprettet flere lommebøker, kan du finne dem her.

Den første handlingen du må ta før du oppretter lommeboken din, er å åpne applikasjonsinnstillingene for å velge de som passer deg best.

![bilde](assets/1.webp)

- "Forbedret Personvern" lar deg deaktivere muligheten til å ta skjermbilder i applikasjonen. Dette alternativet vil også skjule forhåndsvisninger og automatisk sikre applikasjonen når du låser telefonen din. Det er kun tilgjengelig på Android;
- Du kan deretter velge å rute trafikken din gjennom Tor slik at alle tilkoblingene dine er kryptert. Dette senker litt driften av applikasjonen din, men jeg anbefaler å aktivere den for å bevare personvernet ditt;

- "Testnet"-alternativet lar deg opprette lommebøker på Testnet. Dette er et nettverk som fungerer akkurat som Bitcoin-systemet, bortsett fra at bitcoinene som utveksles på det har absolutt ingen verdi. Dette separate Testnet-nettverket er favorisert av brukere eller utviklere som ønsker å teste applikasjoner uten å ta noen økonomisk risiko. Hvis du vil bruke Green Wallet på det ekte Bitcoin-systemet, kan du la dette alternativet være ukrysset;

- "Hjelp Green"-alternativet lar deg overføre konfidensiell informasjon til Blockstream slik at de kan forbedre applikasjonen sin;

- "Personlig Electrum Server"-alternativet lar deg koble din egen eksterne Bitcoin-node for å ha tilgang til nettverksinformasjon og kringkaste transaksjonene dine;
- Alternativet "SPV-verifisering" lar deg laste ned og verifisere bestemt informasjon fra Blockchain selv. Dette reduserer behovet for å stole på Blockstream-noden. Vær oppmerksom på at dette alternativet ikke gir alle garantier som en ekte Bitcoin-node, men hvis du ikke har en, kan det være et godt alternativ å aktivere.
Når du har valgt innstillingene dine, kan du klikke på "Lagre"-knappen og deretter starte applikasjonen på nytt.

## Opprette en Bitcoin-lommebok

Neste steg er å opprette din Bitcoin-lommebok. For å gjøre dette, klikk på:

> - Legg til en lommebok;
> - Ny lommebok;
> - Bitcoin.

![bilde](assets/3.webp)

Alternativet "Gjenopprett en lommebok" lar deg få tilgang til en eksisterende lommebok igjen ved å bruke dens mnemoniske frase. Alternativet "Kun-Visning Lommebok" lar deg importere en utvidet offentlig nøkkel (xpub) for å se bevegelsene til en lommebok uten å kunne bruke midlene dens.

> "Kun-Visning lommeboken er spesielt nyttig hvis du har en maskinvarelommebok. Du kan importere xpub til telefonen din for å opprette mottaksadresser og spore saldoen til lommeboken som er vert på maskinvarelommeboken."
> Nettverksalternativene lar deg koble lommeboken din til forskjellige systemer. "Liquid"-nettverket er en Bitcoin sidekjede. "Testnet"-nettverket er en kopi av Bitcoin-nettverket, men med bitcoins som ikke har noen verdi. Til slutt er "Testnet Liquid"-nettverket tilsvarende Testnet for Liquid-sidekjeden. I denne opplæringen ønsker vi bare å opprette en Bitcoin-lommebok, så vi velger "Bitcoin"-nettverket.

Deretter blir du spurt hvilken type lommebok du ønsker å opprette. Det enkleste alternativet er å opprette en "Single Sig"-lommebok. I dette tilfellet vil hver UTXO (bit av bitcoin) som tilhører oss kun være låst av et enkelt nøkkelpar.

Velg "Single Signature".

Du kan deretter velge å ha en mnemonisk frase på 12 ord eller 24 ord. Denne frasen vil tillate deg å gjenopprette tilgang til lommeboken din fra hvilken som helst kompatibel programvare i tilfelle tap, tyveri eller skade på telefonen din.

En 24-ords frase er sikrere enn en 12-ords frase mot brute force-angrep. Imidlertid er for øyeblikket en 12-ords frase fortsatt tilstrekkelig sikker. I praktiske termer, hvis du velger en 12-ords frase, vil du være rett over den minimumsanbefalte grensen av NIST. Dette betyr at frasen din er sikker i dag, men den kan ikke være det i fremtiden på grunn av fremskritt innen databehandling (med mindre du også bruker en BIP39-passfrase). Som standard anbefaler jeg å velge en 24-ords frase, men det er opp til deg å gjøre ditt eget valg.

![bilde](assets/6.webp)

Programvaren vil deretter gi deg din gjenopprettingsfrase. Du må lagre den ordentlig ved å skrive den ned på et passende fysisk medium. Det anbefales sterkt ikke å beholde denne frasen på noe digitalt medium, selv om det er kryptert. Den bør skrives ned på papir eller metall avhengig av den lagrede verdien.

Denne frasen er av største betydning da den gir tilgang til nøklene til lommeboken din uten noen begrensninger. Hvis du mister den, vil du ikke lenger kunne få tilgang til bitcoinene dine hvis telefonen din slutter å fungere. Hvis denne mnemoniske frasen blir stjålet, kan en angriper irreversibelt stjele alle midlene dine.

Ordene i denne frasen må skrives sammen. Ikke del opp frasen din! I tillegg er det også essensielt å skrive ned hvert ord i den definerte rekkefølgen, sammen med nummeret sitt. En uordnet frase er ubrukelig.

For å lære mer om sikring av gjenopprettingsfrasen, anbefaler jeg sterkt å lese min dedikerte artikkel om dette emnet.

![bilde](assets/7.webp)
Green Wallet ber deg deretter om å bekrefte visse ord fra frasen din for å sikre at du har skrevet dem ned riktig.
![bilde](assets/10.webp)

Du kan deretter velge et navn for lommeboken din for å skille den fra andre hvis du oppretter flere lommebøker senere. På dette stadiet er ikke navnet viktig siden vi vil slette denne lommeboken for å verifisere gyldigheten av den mnemoniske frasen i neste steg.

Du blir også bedt om å sette opp en PIN-kode. Den brukes til å låse tilgangen til lommeboken din. Det er tilrådelig å sette opp et komplekst og tilfeldig passord, spesielt for å beskytte lommeboken din i tilfelle telefonen din blir stjålet.

Denne PIN-koden har ingenting å gjøre med Bitcoin-lommeboken i seg selv. Faktisk, kun med gjenopprettingsfrasen, vil du kunne gjenopprette tilgangen til alle dine bitcoins. PIN-koden blokkerer kun tilgangen til lommeboken din på telefonen din. Derfor er det mye viktigere å sikkerhetskopiere frasen enn å sikkerhetskopiere denne PIN-koden.

Du kan senere legge til en biometrisk låseopsjon for å unngå å måtte angi PIN-koden hver gang du bruker den. Generelt er biometri mye mindre sikker enn selve PIN-koden. Derfor råder jeg som standard mot å implementere denne opplåsningsopsjonen.

Du må angi den valgte PIN-koden en andre gang i Green-applikasjonen for å bekrefte den.

![bilde](assets/12.webp)

Gratulerer! Du har fullført opprettelsen av din Bitcoin-lommebok.

![bilde](assets/14.webp)

Hvis du vil legge til en BIP39-passfrase til denne Bitcoin-lommeboken, må du klikke på de tre prikkene øverst til høyre på skjermen når du angir PIN-koden din for å låse opp lommeboken. Vær forsiktig, jeg råder sterkt mot å bruke en passfrase hvis du ikke forstår de underliggende mekanismene. Du kan miste tilgangen til dine bitcoins.

## Simulering av gjenoppretting av din Bitcoin-lommebok

Før du sender bitcoins til din nye lommebok, er det essensielt å utføre en gjenopprettingstest for å sikre at sikkerhetskopien av den mnemoniske frasen er funksjonell. I praksis vil vi slette lommeboken mens den fortsatt er tom og prøve å gjenopprette den kun ved bruk av gjenopprettingsfrasen, som om vi hadde mistet tilgangen til telefonen vår.

I tillegg til å verifisere gyldigheten av frasen, lar denne praksisen deg også øve på å gjenopprette en Bitcoin-lommebok. Så, hvis du noen gang befinner deg i en nødsituasjon, vil du vite nøyaktig hvilke steg du må ta for å gjenopprette tilgangen til midlene dine.

For å gjøre dette, før du sletter lommeboken din, må du hente en referanseinformasjon som vil tillate deg å gjenkjenne den senere. Derfor vil du kopiere de siste 8 tegnene av den første adressen som blir foreslått til deg.
For å få tilgang til denne informasjonen, klikk på "Motta"-knappen. Lommeboken vil vise en adresse. Skriv ned de siste 8 tegnene av adressen på et separat stykke papir. Dette tilsvarer adressens kontrollsum.

For eksempel, på min lommebok, ville de 8 tegnene å merke seg være: JTbP4482.

![bilde](assets/16.webp)

Når du har notert denne informasjonen, kan du slette lommeboken din. Fra lommebokens hjemmeskjerm, klikk på innstillingsikonet, deretter klikk på "Koble fra".

> "Jeg vil understreke nok en gang at denne operasjonen må gjøres med en tom lommebok, før du sender noen bitcoins til den. Ellers risikerer du å miste dem."

![bilde](assets/19.webp)

Du vil da bli tatt til lommebokens opplåsingsskjerm. Klikk på de tre prikkene i øverste høyre hjørne av skjermen, deretter klikk på "Slett Lommebok", og bekreft.

![bilde](assets/21.webp)
Du er nå på hjemskjermen til Green Wallet-applikasjonen, og det er ingen lommebøker tilgjengelige. Du er for øyeblikket i samme situasjon som om du hadde mistet eller ødelagt telefonen din og prøvde å gjenopprette lommeboken din kun fra den mnemoniske frasen.

Nå klikker du på "Legg til lommebok", deretter "Gjenopprett lommebok", og til slutt "Bitcoin".

![bilde](assets/23.webp)

Programvaren spør oss deretter om vi ønsker å gjenopprette fra en QR-kode eller fra en mnemonisk frase. I vårt tilfelle er det en frase.

Deretter blir vi bedt om å angi gjenopprettingsfrasen. Dette er frasen vi skrev ned da vi opprettet lommeboken. Hvis du bruker en 24-ords frase, husk å klikke på den lille "24"-boksen.

Når alle ordene er angitt, hvis programvaren forteller deg at det er en feil, betyr det at sjekksummen for frasen din er feil. I dette tilfellet betyr det at papirkopien av din mnemoniske frase er ugyldig. Du må starte denne opplæringen på nytt fra begynnelsen og sørge for å skrive ned frasen korrekt når den blir gitt til deg.

Ellers kan du klikke på "Fortsett".

![bilde](assets/26.webp)

Programvaren vil indikere "Lommebok ikke funnet". Dette er helt normalt siden vi for øyeblikket ikke har sendt noen bitcoins til den. Derfor kan den ikke oppdage noen transaksjoner på blokkjeden som er assosiert med denne lommeboken.

Klikk på "Manuell gjenoppretting" nederst på skjermen, deretter klikk på "Enkel signatur".

![bilde](assets/28.webp)

Til slutt vil du bli bedt om å navngi denne lommeboken og tildele den en PIN-kode. Du kan gi den samme navnet og PIN-koden som den opprinnelige lommeboken.
Som en påminnelse, denne PIN-koden tjener kun til å låse opp lommeboken i denne applikasjonen og på denne spesifikke telefonen. I motsetning til den mnemoniske frasen, tillater den deg ikke å regenerere lommeboken din på en annen programvare eller maskinvare.
![bilde](assets/30.webp)

Når PIN-koden er validert, vil du bli tatt tilbake til hjemmesiden til lommeboken din. Det er på tide å sjekke om din gjenopprettingsfrase er funksjonell ved å observere den første avledede adressen. For å gjøre dette, klikk på "Motta" for å få tilgang til den første adressen.

Hvis de siste 8 tegnene er nøyaktig de samme som de du noterte som vitner på papiret ditt før du slettet lommeboken, så er frasen din gyldig. I mitt tilfelle kan vi se at sjekksummen av min første adresse faktisk er lik den tidligere noterte verdien: JTbP4482.

![bilde](assets/32.webp)

Jeg vet at denne verifiseringspraksisen er kjedelig, men den er absolutt nødvendig for å sikre riktig sikkerhet for din Bitcoin-lommebok. Jeg anbefaler sterkt at du utvikler denne vanen når du oppretter en lommebok, enten det er på programvare eller maskinvare.

Med Green Wallet brukte jeg den første adressen for å utføre denne prosessen. Du kan imidlertid også ta en utvidet offentlig nøkkel (xpub/zpub) eller hovedfingeravtrykket til den private nøkkelen som vitneinformasjon.

## Bruke Green Wallet Bitcoin Wallet

Når lommeboken din er satt opp og verifisert, kan du begynne å bruke den.

For å komme i gang, anbefaler jeg å tilpasse innstillingene for lommeboken din. For å gjøre dette, klikk på innstillingsikonet i øvre høyre hjørne av skjermen.

- Alternativet "Vist enhet" lar deg tilpasse enheten som brukes i lommeboken din. Hvis du har en liten mengde midler, kan det være relevant å vise lommeboken din i sats i stedet for bitcoins. Satoshi (sat) tilsvarer en hundredel milliondel av en bitcoin: 1 BTC = 100 000 000 sats.
- Alternativet "Standard Gebyrbeløp" lar deg tilpasse gebyrene som er tildelt transaksjonene dine som standard. Jo høyere gebyrer per vbyte (virtuell byte), desto raskere vil transaksjonene dine bli bekreftet. Du kan senere endre denne gebyrsatsen for hver transaksjon basert på trengselen i Bitcoin-nettverket.
- Alternativet "Biometrisk Tilkobling" lar deg låse opp lommeboken din med fingeravtrykket ditt i stedet for PIN-koden. Generelt sett råder jeg mot å aktivere dette alternativet. Biometri er mye mindre sikker enn PIN-koden.

![bilde](assets/34.webp)
Som standard tildeler Green Wallet deg en BIP49 "Nested SegWit"-konto med P2SH (Pay to Script Hash)-adresser. For noen år siden var bruk av denne typen konto relevant fordi ikke alle støttet native SegWit-adresser ennå. I dag støtter flertallet av Bitcoin-relaterte tjenester SegWit, så det er ikke lenger noen grunn til å bruke en "Nested SegWit"-konto.

Vi vil nå opprette en ny BIP84 "Native SegWit"-konto for å dra nytte av alle dens fordeler, og også for å ha P2WPKH (Pay to Witness Public Key Hash)-adresser. For å gjøre dette, klikk på din "Legacy SegWit-konto" og deretter på "Legg til en ny konto", og til slutt på "SegWit-konto". Du kan deretter gi denne kontoen et navn hvis du ønsker det.

![bilde](assets/36.webp)

I fremtiden, hvis du trenger å opprette nye kontoer på denne lommeboken, anbefaler jeg å velge SegWit V0 BIP84-kontoer som standard, eller SegWit V1 BIP86 (når tilgjengelig).

På hjemmesiden til lommeboken din kan du se dine forskjellige kontoer, inkludert din nye SegWit-konto.

Videre er driften av Green Wallet-applikasjonen veldig enkel. For å motta bitcoins i lommeboken din, klikk på "Motta"-knappen. Lommeboken viser en mottaksadresse. En adresse lar deg motta bitcoins i lommeboken din. Du kan enten kopiere den i tekstformat for å sende den til betaleren din, eller skanne QR-koden med en annen Bitcoin-lommebok for å betale adressen.

![bilde](assets/38.webp)

Denne typen adresse indikerer ikke for betaleren hvilket beløp de skal sende deg. Du kan også opprette en adresse som automatisk vil be om et valgt beløp fra betaleren. For å gjøre dette, klikk på "Flere alternativer" og angi ønsket beløp.

Siden du bruker en SegWit V0 BIP84-konto, bør adressen din starte med prefikset "bc1q". I mitt eksempel bruker jeg en Testnet-lommebok, så prefikset er litt annerledes enn ditt.

En mottaksadresse bør ikke brukes flere ganger. Dette er en dårlig praksis som utgjør risikoer for personvernet ditt. Som standard vil Green-lommeboken generere en ny adresse for deg når du klikker på "Motta" og den forrige allerede har blitt brukt. Du kan også klikke på ikonet med den roterende pilen for å be om en ny blank adresse knyttet til lommeboken din.

> "Tips: Når du kopierer og limer inn en mottaksadresse, trenger du ikke å verifisere at hver karakter av adressen er korrekt. Faktisk inkluderer adresser en sjekksum for å oppdage en liten skrivefeil. Det er bare nødvendig å sjekke de første og siste tegnene på adressen for å sikre dens gyldighet."
> På skjermbildene nedenfor kan du se at jeg sendte 0,02 btc til adressen min. Transaksjonen vises på Green, først som "ubekreftet" mens den venter på å bli inkludert i blokkjeden av en gruvearbeider. Når transaksjonen har mottatt flere bekreftelser, har du vellykket mottatt dine bitcoins i din egen lommebok.

![bilde](assets/40.webp)
Hvis du ønsker å sende bitcoins, må du hente mottaksadressen du ønsker å sende midlene til og klikke på "Send"-knappen. På neste side må du angi destinasjonsadressen. Du kan enten skrive den inn manuelt eller skanne en QR-kode ved å klikke på det tilsvarende ikonet. Deretter velger du transaksjonsbeløpet. Du kan enten angi et beløp i bitcoins eller et beløp i amerikanske dollar ved å klikke på den hvite dobbeltpilen.
![bilde](assets/43.webp)

I midten av skjermen kan du velge gebyrsatsen som er tildelt denne transaksjonen. Du kan enten følge applikasjonens anbefalinger eller tilpasse dine gebyrer. Jo høyere gebyrer du setter sammenlignet med andre transaksjoner som venter på bekreftelse, jo raskere vil transaksjonen din bli inkludert, og motsatt.

Klikk på "Neste". Du vil da komme til en skjerm som gir deg detaljene om transaksjonen din. Du kan verifisere at den angitte adressen er korrekt, at beløpet tilsvarer det du ønsker å sende, og at gebyrene er korrekte.

For å signere transaksjonen og kringkaste den til Bitcoin-nettverket, skyv den grønne knappen nederst på skjermen til høyre.

![bilde](assets/46.webp)

Transaksjonen din vises nå på dashbordet til din Bitcoin-lommebok.

## Konklusjon

Gratulerer! Du har nå din egen selvforvaltede Bitcoin-lommebok. Dine bitcoins tilhører virkelig deg.

Denne Green Wallet fra Blockstream er en utmerket løsning for nybegynnere med en liten mengde bitcoins. Som du har sett, er den veldig enkel å bruke. Det er imidlertid fortsatt en hot wallet. Hvis du har betydelige mengder bitcoins, anbefaler jeg å bruke en hardware wallet.

Når du har lært å mestre Green Wallet og forstå mekanismene som spiller inn, kan du utforske mer omfattende løsninger som Samourai Wallet eller Sparrow Wallet.
For å konkludere, minner jeg deg nok en gang om at du absolutt må ta vare på sikkerhetskopien av din gjenopprettingsfrase. Den gir direkte og ubegrenset tilgang til dine bitcoins. Hvis du mister den, vil du ikke lenger kunne gjenopprette dine bitcoins hvis telefonen din er tapt, ødelagt eller stjålet. Alle som har tilgang til denne frasen kan stjele dine bitcoins, og det vil ikke være noen måte å gjenopprette dem på.

> Denne guiden ble produsert og tilhører Bitstack. Bitstack er en bitcoin neo-bank basert i Paris som tillater DCA på bitcoin. Guide skrevet av Loic Morel den 15.02.2023. Dette tilhører dem. [Lenke til den originale artikkelen](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet)