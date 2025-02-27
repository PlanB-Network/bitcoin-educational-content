---
name: Jade Plus - Sparrow
description: Avansert konfigurasjon av Jade Plus med Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus er en maskinvarelommebok kun for Bitcoin, designet av Blockstream. Det er etterfølgeren til den klassiske Jade, med programvareforbedringer, flere alternativer og redesignet ergonomi for mer intuitiv bruk. Denne nye versjonen har en fantastisk 1,9-tommers LCD-skjerm med et bredere fargespekter enn forgjengeren. Knapper og menynavigering har også blitt optimalisert.

Jade Plus kan brukes på flere måter: via en kablet USB-C-tilkobling, i "*Air-Gap*"-modus med et micro SD-kort (adapter kreves), via Bluetooth eller til og med ved å utveksle QR-koder takket være det integrerte kameraet. Denne maskinvarelommeboken er batteridrevet.

Den er tilgjengelig fra $ 149,99 i den grunnleggende svarte versjonen, og prisen kan stige med opptil $ 20 for versjonene "* Genesis Grey *" eller "*Lunar Silver *". Jade Plus er derfor et interessant valg, med avanserte funksjoner som kan sammenlignes med avanserte maskinvarelommebøker som Coldcard Q eller Passport V2, men til en ganske lav pris, nær mellomklassemodeller.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus er kompatibel med de fleste programvarer for porteføljeforvaltning. Her er en oversikt over kompatibiliteten i skrivende stund (januar 2025):

| Skrivebord | Mobil | USB | Bluetooth | QR | JadeLink | Administrasjonsprogramvare

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 |

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |



blueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

I denne veiledningen setter vi opp en avansert konfigurasjon av Jade Plus med Sparrow Wallet-programvaren i QR-kodemodus. Denne konfigurasjonen er ideell for viderekomne eller erfarne brukere. Hvis du er ute etter en enklere tilnærming for nybegynnere, anbefaler jeg at du tar en titt på denne veiledningen der vi bruker Jade Plus med Green Wallet via en Bluetooth-tilkobling:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
## Sikkerhetsmodellen Jade Plus

Jade Plus bruker en sikkerhetsmodell basert på et "virtuelt sikkert element", materialisert av et "blindt orakel". Konkret kombinerer denne mekanismen PIN-koden som brukeren har valgt, en hemmelighet på Jade og en hemmelighet hos oraklet (en server som vedlikeholdes av Blockstream), for å skape en AES-256-nøkkel som distribueres over to enheter. Under initieringen sikrer en ECDH-utveksling kommunikasjonen med oraklet, og krypterer gjenopprettingsfrasen på maskinvarelommeboken. I praksis trenger du tilgang til :


- Selve Jade Plus-enheten;
- Til PIN-kode for å låse opp enheten ;
- Og til oraklets hemmelighet.

Den største fordelen med denne tilnærmingen er fraværet av et enkelt feilpunkt på maskinvarenivå, siden hvis en angriper noen gang får tilgang til Jade, må både Jade og oraklet kompromitteres for å få ut nøklene. Denne modellen betyr også at Jade Plus er helt åpen kildekode, slik at man unngår begrensningene som er forbundet med bruk av ekte fysiske sikkerhetselementer, som for eksempel de som brukes på Ledger.

Ulempen med dette systemet er at bruken av Jade Plus avhenger av oraklet som vedlikeholdes av Blockstream. Hvis dette oraklet blir utilgjengelig, er det ikke lenger mulig å bruke maskinvarelommeboken direkte med PIN-koden. Dette betyr imidlertid ikke at bitcoinsene dine er tapt, da de fortsatt kan gjenopprettes ved hjelp av gjenopprettingsfrasen din, som du kan angi i Jade Plus i "*stateless*"-modus. For å omgå denne avhengigheten kan du også konfigurere og administrere din egen orakelserver.

Et annet alternativ for å administrere frøet ditt er ganske enkelt å ikke registrere det på Jade Plus. I dette tilfellet blir Jade kun en signaturenhet. Under initialiseringen lagrer du i tillegg til den vanlige lagringen av gjenopprettingsfrasen som ord, også en håndgenerert QR-kode. På denne måten kan du importere seed ved hjelp av Jades kamera hver gang du bruker lommeboken. Dette kan være et interessant alternativ for avanserte brukere, avhengig av sikkerhetsstrategien din, men du må være nøye med å både lagre frøet ditt og beskytte det, for selv som QR-kode vil det gjøre det mulig for hvem som helst å stjele pengene dine. Vi vil se på dette alternativet i denne opplæringen, men det er ikke obligatorisk.

## Utpakking av Jade Plus

Når du mottar Jade Plus, må du kontrollere at esken og forseglingen er i god stand for å sikre at pakken ikke har blitt åpnet.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

I esken finner du :


- Le Jade Plus;
- USB-C-kabel;
- Kort for å registrere minnefrasen som ord eller som "*CompactSeedQR*";
- Noen instruksjoner for bruk ;
- En ledning;
- Noen klistremerker.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Enheten har 4 navigasjonsknapper:


- Knappen nederst til høyre slår på Jade;
- Den store knappen på forsiden av enheten brukes til å velge et element;
- De to små knappene øverst gjør at du kan navigere til venstre og høyre;
- Du kan også velge et element ved å klikke samtidig på de to knappene øverst på enheten.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Sette opp en ny Bitcoin-lommebok

Klikk på startknappen.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klikk på "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Velg "Avansert oppsett*".

![Image](assets/fr/07.webp)

Klikk deretter på "*Create a New Wallet*" for å generere et nytt seed. Du kan velge mellom en mnemonisk frase på 12 eller 24 ord. Sikkerheten til lommeboken din er den samme med begge alternativene, så det kan være mer praktisk å velge det enkleste alternativet å lagre, dvs. 12 ord.

![Image](assets/fr/08.webp)

Klikk på "*Fortsett*"-knappen for å vise den nye gjenopprettingsfrasen.

![Image](assets/fr/09.webp)

Jade Plus viser din 12-ord lange huskeregel. **Denne huskeregelen gir deg full, ubegrenset tilgang til alle bitcoinsene dine. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til din Jade Plus. Frasen på 12 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av din Jade. Det er derfor svært viktig å lagre den nøye og oppbevare den på et sikkert sted.

Du kan skrive det på pappen som følger med i esken, eller for ekstra sikkerhet anbefaler jeg å gravere det på en sokkel i rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps.

![Image](assets/fr/10.webp)

Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer minnefrasen din, anbefaler jeg at du følger denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
du må selvfølgelig aldri dele disse ordene på Internett, slik jeg gjør i denne opplæringen. Denne eksempelmappen vil kun bli brukt på Testnet, og vil bli slettet ved slutten av opplæringen

Klikk på pilen til høyre på skjermen for å vise følgende ord.

![Image](assets/fr/11.webp)

Når du har lagret frasen din, ber Jade Plus deg om å bekrefte den. Velg riktig ord i henhold til rekkefølgen ved hjelp av knappene øverst på enheten, og klikk på den midterste knappen for å gå videre til neste ord.

![Image](assets/fr/12.webp)

Deretter har du to alternativer. Som forklart i innledningen, kan du velge å lagre seed direkte på enheten og bruke Blockstreams "*Virtual Secure Element*"-beskyttelsessystem for å få tilgang til lommeboken din (alternativ 1), eller lagre seed som en QR-kode og skanne den hver gang du bruker den (alternativ 2).

For alternativ 1 velger du "*Nei*", og for alternativ 2 velger du "*Ja*".

![Image](assets/fr/13.webp)

### Alternativ 1: Lås opp QR PIN-kode

Hvis du har valgt alternativ 1 (CompactSeedQR: "*No*"), kommer du direkte til valg av tilkoblingsmetode. I denne veiledningen ønsker vi å bruke enheten i Air-Gap-modus via QR-kodeutveksling, så velg "*QR*".

![Image](assets/fr/27.webp)

Klikk på "*Fortsett*".

![Image](assets/fr/28.webp)

PIN-koden brukes til å låse opp Jade og gir beskyttelse mot uautorisert fysisk tilgang. PIN-koden er ikke involvert i utledningen av lommebokens kryptografiske nøkler. Så selv uten tilgang til denne PIN-koden vil du kunne få tilgang til bitcoinsene dine igjen hvis du har den 12-ord lange minnefrasen din. Vi anbefaler at du velger en PIN-kode som er så tilfeldig som mulig. Sørg også for at du lagrer denne koden på et annet sted enn der Jade er lagret, for eksempel i en passordbehandler.

Velg en 6-sifret PIN-kode på Jade ved å bruke venstre og høyre knapp for å bla gjennom sifrene, og den midterste knappen for å bekrefte hvert siffer.

![Image](assets/fr/29.webp)

Bekreft PIN-koden din en gang til.

![Image](assets/fr/30.webp)

Som forklart i innledningen, lagres frøet ditt kryptert på Jade Plus. For å dekryptere det, må du oppgi :


- Den gyldige PIN-koden (som vi nettopp har satt opp) ;
- Hemmeligheten til oraklet som vedlikeholdes av Blockstream.

I denne avanserte opplæringen bruker vi Sparrow Wallet til å administrere Bitcoin-lommeboken vår. Men i motsetning til Blockstreams Green Wallet-programvare, har Sparrow ikke tilgang til oraklet på Blockstreams servere. Vi vil derfor bruke Blockstreams nettside for å hente orakelhemmeligheten hver gang vi låser opp Jade Plus.

Besøk https://jadefw.blockstream.com/pinqr/index.html

Klikk på "*Start QR-opplåsing*".

![Image](assets/fr/31.webp)

Klikk på "*Done*", siden du allerede har valgt PIN-koden din på Jade Plus.

![Image](assets/fr/32.webp)

Bruk datamaskinens kamera til å skanne QR-kodene som vises på Jade-skjermen.

![Image](assets/fr/33.webp)

Bekreft på Jade for å gå til neste skjermbilde.

![Image](assets/fr/34.webp)

Skann QR-koden som nå er synlig på nettstedet for å hente hemmeligheten til oraklet.

![Image](assets/fr/35.webp)

Nå som porteføljen din er opprettet, kan du gå videre til neste trinn og hoppe over underavsnittet "*Alternativ 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Hver gang du starter opp, klikker du på "*QR Mode*".

![Image](assets/fr/37.webp)

Velg "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Tast inn PIN-koden din.

![Image](assets/fr/39.webp)

Gå deretter til [Blockstreams nettsted] (https://jadefw.blockstream.com/pinqr/qrpin.html) for å utveksle QR-koder med oraklet.

![Image](assets/fr/40.webp)

Din Jade er nå låst opp.

![Image](assets/fr/41.webp)

### Alternativ 2: CompactSeedQR

Hvis du har valgt alternativ 2 (CompactSeedQR: "*Yes*"), klikker du på "*Yes*" igjen.

![Image](assets/fr/14.webp)

Klikk på "*Start*".

![Image](assets/fr/15.webp)

Du kan bruke QR-kodebasen som følger med i Jade Plus-boksen. Velg riktig boks avhengig av om du har valgt en setning på 12 eller 24 ord. Du kan også [skrive ut malen fra Blockstreams nettsted] (https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus vil vise hver sone i QR-koden din.

![Image](assets/fr/16.webp)

Bruk en penn til å fargelegge rutene og gjengi frøet ditt som en QR-kode. Vær nøyaktig for å sikre at Jade Plus-kameraet kan skanne den senere. Bruk pilen for å gå videre til neste område.

![Image](assets/fr/17.webp)

Når du er ferdig, klikker du på "*Done*".

![Image](assets/fr/18.webp)

Skann den håndlagde QR-koden med Jade Plus for å sjekke gyldigheten.

![Image](assets/fr/19.webp)

Hvis papirsikkerhetskopien er korrekt, klikker du på "*Fortsett*".

![Image](assets/fr/20.webp)

I denne veiledningen skal vi bruke en tilkoblingsmodus som utelukkende er basert på skanning av QR-koder, så velg "*QR*".

![Image](assets/fr/21.webp)

Du kan også velge å legge til en PIN-kode i tillegg til CompactSeedQR-sikkerhetskopien din, som i alternativ 1. Dette gir deg to måter å få tilgang til lommeboken din på: enten via PIN-koden og Blockstreams "Virtual Secure Element"-system, eller via CompactSeedQR.

Hvis du velger alternativet med dobbel PIN-kode, velger du "*PIN*" og følger de samme trinnene som i alternativ 1 for å angi PIN-koden.

Hvis du foretrekker å fortsette med kun CompactSeedQR, velger du "*SeedQR*".

![Image](assets/fr/22.webp)

Nå som porteføljen din er opprettet, kan du gå videre til neste trinn.

![Image](assets/fr/23.webp)

Hver gang du starter opp, klikker du på knappen "*QR Mode*" og deretter på "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Bruk enhetens kamera til å skanne det lagrede frøet som en QR-kode.

![Image](assets/fr/25.webp)

Din Jade er nå låst opp.

![Image](assets/fr/26.webp)

## Legg til en BIP39-passordfrase

En BIP39-passordfrase er et valgfritt passord som du kan velge fritt, og som legges til minnefrasen din for å forsterke lommebokens sikkerhet. Når denne funksjonen er aktivert, vil tilgang til Bitcoin-lommeboken din kreve både minnefrasen og passordfrasen. Uten begge deler vil det være umulig å gjenopprette lommeboken.

Før du konfigurerer dette alternativet på din Jade Plus, anbefales det på det sterkeste at du leser denne artikkelen for å forstå den teoretiske bruken av passordfrasen og unngå feil som kan føre til tap av dine bitcoins :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Når Jade fortsatt er låst (passordfrasen kan bare legges inn når enheten ikke er låst opp), åpner du menyen "*Options*".

![Image](assets/fr/42.webp)

Velg "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

I alternativet "*Frequency*" kan du velge om Jade Plus skal be deg om å oppgi passordfrasen din hver gang den starter opp:


- "*Disabled*" deaktiverer bruken av en passordfrase;
- "*Neste innlogging*" krever at du går tilbake til denne menyen for å aktivere forespørselen om passordfrasen din ved neste oppstart. Med dette alternativet kan du ikke avsløre bruken;
- "*Always Ask*" gjør at Jade systematisk ber deg om passordfrasen din hver gang den starter opp, og avslører dermed at lommeboken din er beskyttet av en passordfrase.

Velg alternativet i henhold til din sikkerhetsstrategi. Personlig velger jeg "*Spør alltid*" i dette eksemplet.

![Image](assets/fr/44.webp)

Du kan deretter velge mellom to metoder for å skrive inn passordfrasen:


- "*Manuelt*: Et virtuelt tastatur lar deg skrive inn bokstaver (store og små bokstaver), tall og symboler, tegn for tegn. Dette er standardmetoden for alle maskinvarelommebøker;
- "*WordList*": Spesifikk metode utviklet av Blockstream for Jade, som gjør det raskere å skrive inn passordfraser og øker entropien. Under inntasting foreslår systemet ord fra BIP39-listen, noe som gjør opplåsingen enklere. Denne metoden genererer automatisk en setning ved å sette sammen de valgte ordene, atskilt med mellomrom (eksempel: `abandon ability able`).

Personlig anbefaler jeg deg å bruke den første metoden, siden det er standarden du finner på alle andre porteføljestøtter.

![Image](assets/fr/45.webp)

Du kan deretter gå tilbake til startskjermen og låse opp lommeboken som normalt, enten ved hjelp av PIN-koden eller CompactSeedQR (som vist ovenfor). Du vil deretter bli bedt om å taste inn passordfrasen din.

![Image](assets/fr/46.webp)

Skriv det inn på Jade-tastaturet, og sørg for å ta en eller flere sikkerhetskopier på fysiske medier (papir eller metall). I eksempelet bruker jeg en svært svak passordfrase, men du må velge en sterk, tilfeldig passordfrase som inneholder alle typer tegn og er lang nok (som et sterkt passord).

![Image](assets/fr/47.webp)

Hvis passordfrasen er gyldig, bekrefter du.

![Image](assets/fr/48.webp)

Vær oppmerksom på at BIP39-passordfraser er følsomme for store og små bokstaver og skrivefeil. Hvis du skriver inn en passordfrase som er litt annerledes enn den som opprinnelig ble konfigurert, vil Jade ikke rapportere en feil, men vil utlede et annet sett med kryptografiske nøkler som ikke vil være de i den opprinnelige porteføljen din.

Det er derfor viktig at du noterer deg hovednøkkelens fingeravtrykk når du konfigurerer, som du finner nederst i høyre hjørne på skjermen. For eksempel, med passordfrasen `PBN`, er hovednøkkelfingeravtrykket mitt `3AD1AE65`.

![Image](assets/fr/49.webp)

Hver gang du låser opp Jade med passordfrasen din, må du kontrollere at fingeravtrykket er det samme som det du skrev inn under konfigurasjonen. Hvis det er det, er passordfrasen din riktig, og du har tilgang til riktig Bitcoin-lommebok. Hvis den ikke er det, er du på feil lommebok og må prøve igjen, og pass på at du ikke gjør noen inntastingsfeil.

Før du mottar dine første bitcoins i lommeboken din, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Noter litt referanseinformasjon, for eksempel din xpub eller første mottaksadresse, og slett deretter lommeboken på Jade Plus mens den fortsatt er tom (`Options -> Device -> Factory Reset`). Prøv deretter å gjenopprette lommeboken din ved hjelp av papirsikkerhetskopiene av den mnemoniske frasen og en eventuell passordfrase. Sjekk at cookie-informasjonen som genereres etter gjenopprettingen samsvarer med den du opprinnelig skrev ned. Hvis den gjør det, kan du være sikker på at papirsikkerhetskopiene dine er pålitelige. Hvis du vil vite mer om hvordan du gjennomfører en testgjenoppretting, kan du ta en titt på denne andre veiledningen:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Konfigurere lommeboken på Sparrow Wallet

I denne veiledningen presenterer jeg en avansert bruk av Jade Plus ved hjelp av Sparrow Wallet. Denne maskinvarelommeboken er imidlertid kompatibel med mange andre programmer, for eksempel Liana, Nunchuk, Specter, Green og Keeper. Kompatibiliteten varierer når det gjelder tilkoblinger: USB, Bluetooth eller QR-kode (se tabellen i innledningen for detaljer).

Start med å laste ned og installere Sparrow Wallet [fra det offisielle nettstedet] (https://sparrowwallet.com/) på datamaskinen din, hvis du ikke allerede har gjort det.

![Image](assets/fr/50.webp)

Sørg for å kontrollere ektheten og integriteten til programvaren før du installerer den. Hvis du ikke vet hvordan du gjør dette, kan du se denne veiledningen:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Når Sparrow Wallet er åpen, klikker du på "*File*"-fanen og deretter på "*New Wallet*".

![Image](assets/fr/51.webp)

Gi lommeboken din et navn, og klikk deretter på "*Create Wallet*".

![Image](assets/fr/52.webp)

Velg "*Airgapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Klikk på "*Scan...*" ved siden av alternativet "*Jade*".

![Image](assets/fr/54.webp)

Lås opp Jade Plus, og skriv inn passordfrasen din hvis du bruker en slik. Gå deretter til menyen "*Options*", velg "*Wallet*", og klikk på "*Export Xpub*".

![Image](assets/fr/55.webp)

Jade viser Keystore via flere QR-koder. Skann dem på maskinen din ved hjelp av Sparrow.

![Image](assets/fr/56.webp)

Du bør nå se xpuben din og hovednøkkelens fingeravtrykk, som bør samsvare med avtrykket på Jade Plus. Klikk på "*Apply*".

![Image](assets/fr/57.webp)

Angi et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet vil beskytte dine offentlige nøkler, adresser, etiketter og transaksjonshistorikk mot uautorisert tilgang. Det er lurt å lagre dette passordet i en passordbehandler, slik at du ikke glemmer det.

![Image](assets/fr/58.webp)

Porteføljen din er nå riktig konfigurert på Sparrow.

![Image](assets/fr/59.webp)

## Motta bitcoins

Nå som Jade Plus er konfigurert, er du klar til å motta dine første sats på din nye Bitcoin-lommebok. For å gjøre dette, klikker du på "*Mottak*"-menyen på Sparrow.

![Image](assets/fr/60.webp)

Sparrow viser den første tomme mottaksadressen i porteføljen din.

![Image](assets/fr/61.webp)

Før vi bruker den, la oss sjekke den på Jade Plus-skjermen for å forsikre oss om at den tilhører Bitcoin-lommeboken vår. På Jade klikker du på "*Scan QR*", og skanner deretter QR-koden til adressen som vises på Sparrow.

![Image](assets/fr/62.webp)

Kontroller at adressen som vises på Jade-skjermen, stemmer overens med den som vises i Sparrow Wallet. Hvis den gjør det, klikker du på haken for å fortsette.

![Image](assets/fr/63.webp)

Maskinvarelommeboken din vil da bekrefte at denne adressen er en del av lommeboken din, og at den har den tilhørende private nøkkelen.

![Image](assets/fr/64.webp)

Hvis adressen er validert av Jade, kan du nå bruke den til å motta bitcoins. Når transaksjonen sendes ut i nettverket, vil den vises på Sparrow. Vent til du har mottatt nok bekreftelser til å anse transaksjonen som endelig.

![Image](assets/fr/65.webp)

## Send bitcoins

Nå som du har noen satellitter i lommeboken, kan du også sende noen. Det gjør du ved å klikke på "*UTXOs*"-menyen.

![Image](assets/fr/66.webp)

Velg UTXO-ene du ønsker å bruke som inndata for denne transaksjonen, og klikk deretter på "*Send Selected*".

![Image](assets/fr/67.webp)

Skriv inn mottakerens adresse, en etikett som minner deg på formålet med transaksjonen, og beløpet du ønsker å sende til denne adressen.

![Image](assets/fr/68.webp)

Juster gebyrsatsen i henhold til gjeldende markedsforhold, og klikk deretter på "*Opprett transaksjon*".

![Image](assets/fr/69.webp)

Kontroller at alle transaksjonsparametrene er korrekte, og klikk deretter på "*Finalize Transaction for Signing*".

![Image](assets/fr/70.webp)

Klikk på "*Show QR*" for å vise PSBT (*Partially Signed Bitcoin Transaction*). Sparrow har bygget transaksjonen, men den mangler fortsatt signaturene for å låse opp bitcoinsene som brukes i inndataene. Disse signaturene kan bare utføres av Jade Plus, som er vert for din seed som gir tilgang til de private nøklene som trengs for å signere transaksjonen.

![Image](assets/fr/71.webp)

Klikk på "*Scan QR*" på Jade Plus for å skanne PSBT-en som vises på Sparrow.

![Image](assets/fr/72.webp)

Bekreft at leveringsadressen og beløpet er riktig, og klikk deretter på pilen for å validere.

![Image](assets/fr/73.webp)

Kontroller at gebyrbeløpet er det du har valgt, og klikk deretter på avkrysningsikonet øverst til venstre i grensesnittet for å signere transaksjonen.

![Image](assets/fr/74.webp)

På Sparrow Wallet klikker du på "*Scan QR*" og skanner QR-koden som vises på Jade.

![Image](assets/fr/75.webp)

Den signerte transaksjonen din er nå klar til å sendes ut på Bitcoin-nettverket og inkluderes i en blokk av en miner. Hvis alt er riktig, klikker du på "*Broadcast Transaction*".

![Image](assets/fr/76.webp)

Transaksjonen din har blitt sendt og venter på bekreftelse.

![Image](assets/fr/77.webp)

Gratulerer, du vet nå hvordan du konfigurerer og bruker Jade Plus i QR-modus. Hvis du synes denne veiledningen var nyttig, vil jeg være takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Takk for at du deler!

Hvis du vil gå videre, anbefaler jeg denne andre veiledningen om Jade Plus, der vi konfigurerer den via Bluetooth med Green-mobilappen:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0