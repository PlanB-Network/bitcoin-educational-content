---
name: Proton Wallet
description: Installere og bruke Proton Bitcoin-lommeboken
---
![cover](assets/cover.webp)

Proton er et sveitsisk selskap som spesialiserer seg på digitalt personvern, og ble grunnlagt i 2014 av forskere fra CERN. Proton er kjent for sine løsninger med åpen kildekode, og tilbyr en rekke tjenester, inkludert Proton Mail, Proton VPN og Proton Drive.

Proton introduserte nylig Proton Wallet, en åpen kildekode, selvforvaltet Bitcoin-lommebok tilgjengelig som en mobilapp eller nettklient, knyttet til Proton-kontoen din. Lommebokens funksjonalitet er relativt klassisk for øyeblikket, med de essensielle verktøyene som forventes av en god Bitcoin-lommebok, for eksempel RBF (*Replace-By-Fee*), tagging eller muligheten til å legge til en BIP39-passordfrase.

Det spesielle med denne lommeboken er muligheten til å sende bitcoins ved hjelp av mottakerens e-postadresse, som Proton automatisk genererer en tom Bitcoin-adresse knyttet til brukerens lommebok. Proton planlegger å legge til nye funksjoner i fremtiden, inkludert Lightning og coinjoins (sannsynligvis ved hjelp av Whirlpool, som antydet av aktivitet på GitHub-depotet deres).

## Opprett en Proton-konto

For å bruke Proton Wallet trenger du en Proton-konto. Du kan opprette en gratis ved å følge de første trinnene i denne opplæringen dedikert til å opprette en Proton-postkasse (bare delen "*Opprette en Proton-konto*"). Når kontoen din er satt opp, kan du fortsette med resten av denne veiledningen.

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Koble til Proton Wallet

Gå til [nettstedet til Proton Wallet] (https://proton.me/wallet) og klikk på "*Get Proton Wallet*"-knappen.

![Image](assets/fr/01.webp)

Velg abonnementsalternativet "*Gratis*", og klikk deretter på "*Logg inn*".

![Image](assets/fr/02.webp)

Skriv inn e-postadressen og passordet som er knyttet til Proton-kontoen din for å logge på.

![Image](assets/fr/03.webp)

Kontoen din skal nå vises. Klikk på "*Begynn å bruke Proton Wallet nå*".

![Image](assets/fr/04.webp)

## Opprett en Bitcoin-lommebok

Velg standard fiat-valuta for kontoen din, og klikk deretter på "*Opprett ny lommebok*".

![Image](assets/fr/05.webp)

Bitcoin-lommeboken din er nå opprettet. Du kan i teorien begynne å bruke den umiddelbart, men det er veldig viktig å lagre minnepengene dine først. Dette gjør du ved å klikke på "*Secure your wallet*" øverst til høyre i grensesnittet.

![Image](assets/fr/06.webp)

Hvis du ikke allerede har gjort det på Proton, vil du bli bedt om å sette opp en sikkerhetskopi for kontoen din og sikre den ved hjelp av en 2FA-metode. Selv om disse sikkerhetstiltakene gjelder for hele Proton-kontoen din, er de desto mer relevante når Bitcoin-lommeboken din er integrert i den. Jeg anbefaler på det sterkeste at du implementerer dem.

![Image](assets/fr/07.webp)

Hvis du vil lagre minnefrasen din, klikker du på "*Backup this wallet's seed phrase*".

![Image](assets/fr/08.webp)

Skriv inn Proton-passordet ditt.

![Image](assets/fr/09.webp)

Klikk deretter på "*Vis lommebokens seed-frase*" for å vise lommebokens mnemoniske frase.

![Image](assets/fr/10.webp)

Proton Wallet viser din 12-ord lange huskeregel. **Denne huskeregelen gir deg full, ubegrenset tilgang til alle bitcoinsene dine**. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten tilgang til Proton-kontoen din. Frasen på 12 ord kan brukes til å gjenopprette tilgangen til bitcoinsene dine hvis du mister tilgangen til kontoen din. Det er derfor svært viktig å lagre den nøye og oppbevare den på et sikkert sted.

Du kan skrive det på et stykke papir, eller for ekstra sikkerhet anbefaler jeg å gravere det på en sokkel av rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps.

![Image](assets/fr/11.webp)

Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer minnefrasen din, anbefaler jeg at du følger denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

du bør selvfølgelig aldri ta bilde av disse ordene, i motsetning til hva jeg gjør i denne veiledningen

Klikk på "*Done*"-knappen når du har lagret frasen din.

![Image](assets/fr/12.webp)

## Oppdag grensesnittet

Grensesnittet til Proton Wallet er svært intuitivt. Til venstre finner du de forskjellige lommebøkene dine og deres tilknyttede kontoer. "*Primary*"-kontoen er din hovedkonto. Av konfidensialitetshensyn plasseres bitcoins som mottas via Proton-e-postadressen på en egen konto, kalt "*Bitcoin via e-post*".

![Image](assets/fr/13.webp)

For å legge til en ny konto klikker du på "*Legg til konto*".

![Image](assets/fr/14.webp)

For å opprette en ny portefølje klikker du på "*+*"-symbolet ved siden av "*Wallets*".

![Image](assets/fr/15.webp)

Her kan du legge til en BIP39-passordfrase i en ny lommebok.

![Image](assets/fr/16.webp)

Hvis du vil fordype deg i passordfrasen, anbefaler jeg denne veiledningen:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Motta bitcoins

For å motta bitcoins i lommeboken din, velg ønsket konto til venstre i grensesnittet, og klikk deretter på "*Mottak*"-knappen.

![Image](assets/fr/17.webp)

Proton Wallet genererer deretter automatisk en ny, tom adresse.

![Image](assets/fr/18.webp)

Når transaksjonen er fullført, finner du den i delen "*Transaksjoner*". Klikk på "*+Legg til*" for å gi transaksjonen en etikett.

![Image](assets/fr/19.webp)

## Send bitcoins

Nå som du har bitcoins i lommeboken din, kan du sende dem. Velg kontoen du ønsker på venstre side av grensesnittet, og klikk deretter på "*Send*".

![Image](assets/fr/20.webp)

Skriv inn mottakerens Bitcoin-adresse. Du kan skanne en QR-kode ved å klikke på den lille logoen. Hvis du vil sende til en e-postadresse, skriver du den direkte i dette feltet. Når du har skrevet inn Bitcoin-adressen, klikker du på den lille pilen og deretter på "*Bekreft*".

![Image](assets/fr/21.webp)

Angi beløpet som skal sendes, enten i fiat-valuta eller i bitcoins, og klikk deretter på "*Review*".

![Image](assets/fr/22.webp)

Velg transaksjonsgebyr basert på den aktuelle markedssituasjonen.

![Image](assets/fr/23.webp)

Legg til en etikett på transaksjonen, og dobbeltsjekk deretter alle detaljene. Hvis alt er riktig, klikker du på "*Bekreft og send*" for å signere og sende transaksjonen.

![Image](assets/fr/24.webp)

Transaksjonen din vil nå vises i "*Transaksjoner*"-delen av kontoen din i påvente av bekreftelse.

![Image](assets/fr/25.webp)

## Logg inn på applikasjonen

I tillegg til nettklienten er Proton Wallet også tilgjengelig via en mobilapplikasjon. Ved å koble lommeboken til Proton-kontoen din kan du synkronisere lommeboken din mellom nettklienten og mobilappen.

Last ned Proton Wallet fra applikasjonsbutikken din:


- [På App Store] (https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [I Google Play Store] (https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Etter installasjonen klikker du på "*Log in*" og skriver inn e-postadressen og Proton-passordet ditt.

![Image](assets/fr/27.webp)

Du får da tilgang til Bitcoin-lommeboken din, med de samme funksjonene som på nettklienten.

![Image](assets/fr/28.webp)

Gratulerer, du vet nå hvordan du konfigurerer og bruker Proton Wallet. Hvis du synes denne veiledningen var nyttig, vil jeg være takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Takk for at du deler!

For å gå videre, anbefaler jeg denne veiledningen om Jade Plus, Blockstreams nyeste maskinvarelommebok:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
