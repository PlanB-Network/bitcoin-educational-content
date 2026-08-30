---
name: Sparrow Wallet - Multisig
description: Opprett en multisignatur-Wallet på Sparrow
---
![cover](assets/cover.webp)


En multisignatur-Wallet (ofte kalt "*Multisig*") er en Bitcoin-Wallet-struktur som krever flere kryptografiske signaturer, fra forskjellige nøkler, for å godkjenne en transaksjon. I motsetning til en vanlig ("*singlesig*") Wallet, der én enkelt privat nøkkel er tilstrekkelig for å låse opp en UTXO, er Multisig basert på en **m-av-n**-modell: av de _n_ nøklene som er knyttet til Wallet, må _m_ av dem alltid medsignere hver transaksjon.


Denne mekanismen gjør det mulig å dele kontrollen over en Wallet mellom flere enheter eller enheter/apparater. I en 2-av-3-konfigurasjon, for eksempel, genereres tre uavhengige nøkkelsett, men bare to av dem trengs for å frigjøre midler. Denne arkitekturen reduserer risikoen forbundet med kompromittering eller tap av en nøkkel drastisk: en tyv med tilgang til bare én nøkkel kan ikke tømme Wallet, og en bruker som mister én nøkkel, har fortsatt tilgang til midlene sine med de to gjenværende.


![Image](assets/fr/01.webp)


Denne økte sikkerheten kommer imidlertid med økt kompleksitet. Å sette opp en Multisig-Wallet krever at du sikrer flere Mnemonic-fraser (én per signaturfaktor) og utvidede offentlige nøkler ("*xpub*"). Hvis du bruker en Multisig 2-av-3-Wallet, må du for å gjenopprette Wallet enten ha alle tre Mnemonic-frasene, eller minst to av de tre frasene. Men hvis du bare har to av de tre frasene, trenger du også tilgang til de tre *xpub*-ene, uten hvilke det vil være umulig å gjenopprette de offentlige nøklene som trengs for å få tilgang til bitcoinsene de beskytter.


For å oppsummere: for å gjenopprette en Multisig-Wallet må du enten:


- Ha tilgang til alle Mnemonic-frasene knyttet til hver signaturfaktor; eller
- Ha det minste antallet Mnemonic-fraser som kreves av terskelen for å kunne signere, og i tillegg ha tilgang til xpub-ene til alle faktorene for å kunne gjenopprette de nødvendige offentlige nøklene.


![Image](assets/fr/02.webp)


Denne håndteringen av sikkerhetskopier for Multisig-Wallet gjøres enklere av *Output Script Descriptors*, som samler all den offentlige dataen som trengs for å få tilgang til midlene. Denne funksjonen er imidlertid ikke implementert i all programvare for Wallet-administrasjon ennå.


Multisig egner seg spesielt godt for bitcoinere som ønsker forbedret sikkerhet eller kollektiv forvaltning av midler: bedrifter, foreninger, familier eller privatpersoner som eier et betydelig antall bitcoins. Det kan brukes til å opprette desentraliserte styringsordninger, for eksempel for å fordele signeringsmyndighet mellom flere forvaltere eller teammedlemmer.


I denne veiledningen skal vi lære hvordan man oppretter og bruker en klassisk multisignatur-Wallet med **Sparrow Wallet**. Hvis du ønsker å opprette en tilpasset multisignatur-Wallet med tidslåser, anbefaler jeg heller at du bruker Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Forutsetninger


I denne veiledningen skal jeg vise deg hvordan du lager en Multisig med [Sparrow Wallet, programvare for Wallet-administrasjon](https://sparrowwallet.com/download/). Hvis du ikke allerede har installert denne programvaren, gjør du det nå. Hvis du trenger hjelp, har vi også en detaljert veiledning for konfigurering av Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

For å sette opp en multisignatur-Wallet trenger du forskjellige Hardware Wallet. For en Multisig 2-av-3 kan du for eksempel bruke:


- En Trezor Model One;
- Ledger Flex;
- En Passport Core.


![Image](assets/fr/03.webp)


Det er lurt å bruke forskjellige merker av Hardware Wallet i Multisig-konfigurasjonen din. Dette sikrer at hvis en bestemt modell skulle få et alvorlig problem, vil det ikke påvirke den totale sikkerheten til Multisig-en din. Dessuten gir det deg mulighet til å dra nytte av de spesifikke fordelene til hver enhet. I min konfigurasjon, for eksempel:



- Trezor Model One er helt åpen kildekode, noe som gjør det mulig å verifisere seed-genereringen. Siden den ikke har et Secure Element, er den likevel sårbar for fysiske angrep;



- Ledger Flex, derimot, drar nytte av proprietær firmware som ikke kan verifiseres, men har et Secure Element som gir utmerket fysisk beskyttelse;



- Passport Core kombinerer helt åpen kildekode-firmware, et Secure Element og air-gapped QR-kode-utveksling. Den fungerer som en uavhengig tredje signatar som kan verifisere adresser og signere PSBT-er uten en USB-datatilkobling.


Før du konfigurerer Multisig-Wallet din, må du sørge for at hver Hardware Wallet er riktig konfigurert (generering og lagring av Mnemonic, PIN-definisjon). For detaljerte instruksjoner kan du se veiledningene våre for hver Hardware Wallet, for eksempel:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Som vi skal se senere i denne veiledningen, er det også mulig å inkludere en faktor i Multisig-konfigurasjonen din som ikke er knyttet til en Hardware Wallet, men der de private nøklene lagres på PC-en din. Denne metoden er åpenbart mindre sikker enn å utelukkende bruke Hardware Wallet, men den kan være relevant i visse tilfeller. For en Multisig 2-av-3 kan du for eksempel velge to Hardware Wallet og én Software Wallet.

> ⚠️ **Sikkerhetsvarsel for Coldcard MK3:** ikke opprett en ny seed på en MK3 som kjører firmware eldre enn 4.2.0. Seeder som er generert på eldre firmware, må erstattes, og midlene må flyttes. Denne veiledningen bruker derfor Passport Core som sin air-gapped referansesignatar.


## Opprette en Multisig-Wallet


Åpne Sparrow Wallet, klikk på fanen "*File*", og velg deretter "*New Wallet*".


![Image](assets/fr/04.webp)


Gi multisignatur-Walleten et navn, og klikk deretter på "*Create Wallet*" for å bekrefte.


![Image](assets/fr/05.webp)


I nedtrekksmenyen "*Policy Type*" velger du alternativet "*Multi Signature*".


![Image](assets/fr/06.webp)


Øverst til høyre kan du nå angi det totale antallet nøkler i Multisig-en din, samt antallet medsignatarer som kreves for å godkjenne en transaksjon. I mitt eksempel er dette et 2-av-3-oppsett.


![Image](assets/fr/07.webp)


Nederst i vinduet viser Sparrow Wallet tre "*Keystore*". Hver av dem representerer et nøkkelsett. Her bruker jeg tre Hardware Wallet, så hver "*Keystore*" tilsvarer én av dem. Vi skal nå konfigurere dem.


Jeg begynner med Passport Core. I fanen "*Keystore 1*" velger jeg alternativet "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Åpne kontoen du vil bruke, på Passport, og velg deretter "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport viser en animert QR-kode som inneholder informasjon om den offentlige nøkkelen.

Velg "*Scan...*" ved siden av "*Passport*" i Sparrow, og skann den animerte QR-koden med datamaskinens webkamera. Kontroller at fingeravtrykket til hovednøkkelen som vises av Sparrow, samsvarer med det som vises på Passport, og importer deretter Keystore.

Xpub-en for Passport-en din er nå importert. Gjenta samme fremgangsmåte for Ledger Flex og Trezor Model One.


For Ledger Flex velger jeg "*Keystore 2*", og klikker deretter på "*Connected Hardware Wallet*". Sørg for at Ledger er koblet til datamaskinen, låst opp, og at Bitcoin-applikasjonen er åpen.


![Image](assets/fr/15.webp)


Klikk deretter på knappen "*Scan...*".


![Image](assets/fr/16.webp)


Ved siden av navnet på Hardware Wallet klikker du på "*Import Keystore*".


![Image](assets/fr/17.webp)


Den andre signataren er nå riktig registrert i Sparrow Wallet.


![Image](assets/fr/18.webp)


Jeg gjentar nøyaktig samme fremgangsmåte med Trezor One for å fullføre Multisig-konfigurasjonen.


![Image](assets/fr/19.webp)


I min konfigurasjon dekker vi ikke dette tilfellet, men hvis du vil inkludere en signatur via en Software Wallet i Sparrow (Hot Wallet) i Multisig-en din, klikker du bare på knappen "*New or Imported Software Wallet*".


Nå som alle signeringsenhetene dine er importert til Sparrow Wallet, kan du fullføre opprettelsen av Multisig ved å klikke på "*Apply*".


![Image](assets/fr/20.webp)


Velg et sterkt passord for å sikre tilgangen til Sparrow Wallet-en din. Dette passordet beskytter de offentlige nøklene dine, adressene, etikettene og transaksjonshistorikken mot uautorisert tilgang.


Husk å lagre dette passordet på et trygt sted, for eksempel i en passordbehandler, for å unngå å miste det.


![Image](assets/fr/21.webp)


## Sikkerhetskopiere en Multisig-Wallet


Vi skal nå lagre *Output Script Descriptor*-en på et uavhengig medium og beholde flere kopier av den.


*Descriptor*-en inneholder alle xpub-ene i Multisig-Wallet din, samt utledningsstiene som brukes til å generere nøklene. Husk hva vi så i del 1: for å gjenopprette en Multisig-Wallet må du enten ha **alle** Mnemonic-frasene, eller bare det minste antallet som kreves for å nå signaturterskelen. I sistnevnte tilfelle er det imidlertid også avgjørende å ha **xpub-ene** til de manglende signatarene. *Descriptor*-en inneholder alle xpub-ene til Multisig-en din.


Hvis dette ikke er klart, kan du bare huske dette: for å gjenopprette en Multisig trenger du det minste antallet Mnemonic-fraser for hver Hardware Wallet som brukes, avhengig av terskelen (i mitt tilfelle: 2 fraser), samt *Descriptor*-en.


Denne *Descriptor*-en inneholder ingen private nøkler, bare offentlige. Dette betyr at den ikke gir tilgang til midlene. Den er derfor ikke like kritisk som Mnemonic-fraser, som gir full tilgang til bitcoinsene dine. Risikoen ved *Descriptor*-en er utelukkende knyttet til konfidensialitet: i tilfelle kompromittering kan en tredjepart observere alle transaksjonene dine, men vil ikke kunne bruke midlene dine.


Jeg anbefaler på det sterkeste at du lager flere kopier av denne *Descriptor*-en og oppbevarer dem sammen med hver signeringsenhet i Multisig-en din. I mitt tilfelle, for eksempel, skriver jeg ut *Descriptor*-en på papir og oppbevarer én kopi sammen med Passport, én med Trezor og én med Ledger. Jeg lagrer også denne *Descriptor*-en som en PDF-fil på tre USB-pinner, hver oppbevart sammen med én av Hardware Wallet-ene. På denne måten maksimerer jeg sjansene mine for aldri å miste denne *Descriptor*-en, og jeg er sikker på å ha to kopier (én fysisk og én digital) sammen med hver enhet.


Når Multisig-Wallet din er opprettet, gir Sparrow deg automatisk denne *Descriptor*-en. Klikk på knappen "*Save PDF...*" for å lagre den både som tekst og som QR-kode.


![Image](assets/fr/22.webp)


Deretter kan du skrive ut denne PDF-en og kopiere den til USB-pinnene dine.


![Image](assets/fr/23.webp)


Passport bruker multisig-konfigurasjonen som er importert av Sparrow, til å vise og verifisere den relevante nøkkelinformasjonen under QR-paring- og signeringsflyten. Oppbevar *Descriptor*-en uavhengig: den er fortsatt avgjørende for å gjenopprette Wallet hvis én signatar ikke er tilgjengelig.


I tillegg til å lagre *Descriptor*-en må du ikke glemme å være spesielt oppmerksom på å lagre Mnemonic-frasene for hver av signeringsenhetene dine. Hvis du er nybegynner, anbefaler jeg på det sterkeste at du leser denne andre veiledningen for å lære hvordan du lagrer og administrerer dem riktig:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Før du mottar dine første bitcoins på Multisig-en din, **anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Noter deg noe referanseinformasjon, for eksempel den første mottaksadressen, og nullstill deretter Hardware Wallet-ene dine mens Wallet fortsatt er tom. Prøv deretter å gjenopprette Multisig-Wallet din på Hardware Wallet-ene ved hjelp av papirsikkerhetskopiene av Mnemonic-frasen, og deretter på Sparrow ved hjelp av *Descriptor*-en. Kontroller at den første adressen som genereres etter gjenopprettingen, samsvarer med den du opprinnelig noterte deg. Hvis den gjør det, kan du være trygg på at papirsikkerhetskopiene dine er pålitelige.


Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, anbefaler jeg deg å lese denne andre veiledningen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Motta bitcoins på Multisig-en din


Wallet er nå klar til å motta bitcoins. Klikk på fanen "*Receive*" i Sparrow.


![Image](assets/fr/30.webp)


Før du bruker adressen som genereres av Sparrow Wallet, bør du ta deg tid til å kontrollere den direkte på skjermen til Hardware Wallet-ene dine. Dette sikrer at adressen ikke er blitt endret, og at enhetene dine har de private nøklene som trengs for å bruke de tilhørende midlene. Dette bidrar til å beskytte deg mot en rekke angrepsvektorer.


For å gjøre dette klikker du på "*Display Address*" for å vise adressen på Trezor eller Ledger, når den er koblet til med kabel.


![Image](assets/fr/31.webp)


Med Passport velger du multisig-kontoen og velger "*Verify Address*". Skann QR-koden til mottaksadressen som vises av Sparrow. Passport bekrefter på skjermen sin om adressen tilhører multisig-Wallet.


Kontroller at adressen som vises på hver Hardware Wallet, tilsvarer nøyaktig den i Sparrow Wallet. Det er lurt å gjøre dette rett før du deler adressen med betaleren, for å være sikker på integriteten.


Deretter kan du tildele adressen en "*Label*" for å angi opprinnelsen til bitcoinsene som mottas. Dette er en god måte å organisere forvaltningen av UTXO-ene dine på.


![Image](assets/fr/34.webp)


Når dette er bekreftet, kan du bruke adressen til å motta bitcoins.


![Image](assets/fr/35.webp)


## Sende bitcoins med Multisig-en din


Nå som du har mottatt dine første sats på Multisig-Wallet din, kan du også bruke dem! Gå til fanen "*Send*" i Sparrow for å bygge en ny transaksjon.


![Image](assets/fr/36.webp)


Hvis du ønsker å bruke *Coin Control*, det vil si manuelt velge UTXO-ene du vil bruke, går du til fanen "*UTXOs*". Velg UTXO-ene du vil bruke, og klikk deretter på "*Send Selected*". Du blir automatisk videresendt til fanen "*Send*", med UTXO-ene allerede forhåndsutfylt.


![Image](assets/fr/37.webp)


Skriv inn mottaksadressen. Flere adresser kan legges til ved å klikke på "*+ Add*".


![Image](assets/fr/38.webp)


Legg til en "*Label*" for å beskrive formålet med denne transaksjonen, slik at det blir lettere å spore transaksjonene dine.


![Image](assets/fr/39.webp)


Skriv inn beløpet som skal sendes til den valgte adressen.


![Image](assets/fr/40.webp)


Juster gebyrsatsen i henhold til gjeldende nettverksforhold. Se for eksempel på [Mempool.space](https://Mempool.space/) for å velge et passende gebyrnivå.


Etter å ha kontrollert alle transaksjonsparametrene, klikker du på "*Create Transaction*".


![Image](assets/fr/41.webp)


Hvis alt ser bra ut, klikker du på "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Nederst på skjermen ser du at Sparrow venter på 2 signaturer. Dette er normalt: Wallet som brukes her, er en Multisig 2-av-3.


![Image](assets/fr/43.webp)


Jeg begynner å signere med Passport-en min. Klikk på "*Show QR*" i Sparrow for å vise PSBT-en (*Partially Signed Bitcoin Transaction*) som animerte QR-koder. På Passport velger du multisig-kontoen og velger "*Sign with QR Code*", og skanner deretter QR-koden som vises av Sparrow.


På skjermen til Hardware Wallet-en din kontrollerer du nøye transaksjonsparametrene: mottakerens adresse, beløpet som sendes, og gebyrene. Når transaksjonen er bekreftet, godkjenner du den for å fortsette til signering.


Etter at du har godkjent transaksjonen, viser Passport den signerte PSBT-en som animerte QR-koder. Klikk på "*Scan QR*" i Sparrow og skann disse kodene med webkameraet ditt. Passport-signaturen legges deretter til. Jeg bruker nå Ledger for den andre nødvendige signaturen: jeg kobler den til og låser den opp, og klikker deretter på "*Sign*" i Sparrow.


![Image](assets/fr/48.webp)


Klikk på "*Sign*" ved siden av navnet på Hardware Wallet.


![Image](assets/fr/49.webp)


Første gang du bruker Ledger med denne Multisig-en, ber Sparrow deg om å verifisere de utvidede offentlige nøklene (xpub-ene) til medsignatarene. Akkurat som med Passport forhindrer dette trinnet deg fra å signere blindt senere. For å bekrefte denne informasjonen sammenligner du xpub-en som vises på Ledger-skjermen, med dem som er gitt direkte av de andre Hardware Wallet-ene dine.


![Image](assets/fr/50.webp)


Kontroller mottakerens adresse, beløpet som overføres, og transaksjonsgebyret, og signer deretter transaksjonen.


![Image](assets/fr/51.webp)


Trykk på skjermen for å signere.


![Image](assets/fr/52.webp)


Sparrow har nå de to signaturene som trengs for å frigjøre midlene fra Multisig-Wallet. Kontroller transaksjonen én siste gang, og hvis alt ser bra ut, klikker du på "*Broadcast Transaction*" for å kringkaste den over nettverket.


![Image](assets/fr/53.webp)


Du finner denne transaksjonen i fanen "*Transactions*" i Sparrow Wallet.


![Image](assets/fr/54.webp)


Gratulerer, nå vet du hvordan du setter opp og bruker en multisignatur-Wallet i Sparrow. Hvis du fant denne veiledningen nyttig, setter jeg pris på om du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på sosiale medier. Takk for at du deler!


For å gå videre anbefaler jeg deg å lese denne veiledningen om en annen metode for å øke sikkerheten til Bitcoin-Wallet din, passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
</content>
