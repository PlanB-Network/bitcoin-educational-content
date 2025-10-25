---
name: Sparrow Wallet - Multisig
description: Opprett en portefølje med flere signaturer på Sparrow
---
![cover](assets/cover.webp)



En Wallet med flere signaturer (ofte kalt "*Multisig*") er en Bitcoin Wallet-struktur som krever flere kryptografiske signaturer, fra forskjellige nøkler, for å autorisere en utgift. I motsetning til en konvensjonell ("*singlesig*") Wallet, der en enkelt privat nøkkel er tilstrekkelig for å låse opp en UTXO, er Multisig basert på en **m-av-n**-modell: av de _n_ nøklene som er tilknyttet Wallet, må _m_ nødvendigvis samsignere hver transaksjon.



Denne mekanismen gjør det mulig å dele kontrollen over en portefølje mellom flere enheter eller enheter. I en 2-av-3-konfigurasjon genereres det for eksempel tre uavhengige sett med nøkler, men det trengs bare to for å frigjøre midler. Denne arkitekturen reduserer drastisk risikoen forbundet med kompromittering eller tap av en nøkkel: En tyv som bare har tilgang til én nøkkel, kan ikke tømme Wallet, og en bruker som mister én nøkkel, kan fortsatt få tilgang til midlene sine med de resterende to.



![Image](assets/fr/01.webp)



Denne større sikkerheten kommer imidlertid med større kompleksitet. For å sette opp en Multisig Wallet må du sikre flere Mnemonic-fraser (én per signaturfaktor) og utvidede offentlige nøkler ("*xpub*"). Hvis du bruker en Multisig 2-av-3 Wallet, må du enten ha alle tre Mnemonic-fraser, eller minst to av de tre frasene, for å hente Wallet. Men hvis du bare har to av de tre frasene, må du også ha tilgang til de tre *xpubs*, og uten dem vil det være umulig å hente ut de offentlige nøklene som trengs for å få tilgang til bitcoinsene de beskytter.



For å oppsummere: For å gjenopprette en Multisig-portefølje må du :




- Eller få tilgang til alle Mnemonic-setningene som er knyttet til hver signaturfaktor;
- Enten må du ha det minste antallet Mnemonic-fraser som terskelverdien krever for å kunne signere, og du må også ha tilgang til xpubene til alle faktorene for å kunne hente ut de nødvendige offentlige nøklene.



![Image](assets/fr/02.webp)



Denne håndteringen av Multisig-porteføljesikkerhetskopier gjøres enklere ved hjelp av *Output Script Descriptors*, som samler alle offentlige data som kreves for å få tilgang til fondene. Denne funksjonaliteten er imidlertid ennå ikke implementert i all programvare for porteføljeforvaltning.



Multisig er spesielt godt egnet for bitcoinbrukere som ønsker økt sikkerhet eller kollektiv forvaltning av midler: selskaper, foreninger, familier eller enkeltbrukere som har en betydelig mengde bitcoins. Den kan brukes til å opprette desentraliserte styringsordninger, for eksempel for å fordele signeringsmyndighet mellom flere ledere eller teammedlemmer.



I denne veiledningen lærer vi hvordan du oppretter og bruker en klassisk multisignatur Wallet med **Sparrow Wallet**. Hvis du ønsker å opprette en tilpasset multisignaturportefølje med tidslås, anbefaler jeg at du bruker Liana i stedet:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Forutsetninger



I denne veiledningen skal jeg vise deg hvordan du lager en Multisig med [Sparrow Wallet portfolio management software] (https://sparrowwallet.com/download/). Hvis du ennå ikke har installert denne programvaren, bør du gjøre det nå. Hvis du trenger hjelp, har vi også en detaljert veiledning om hvordan du konfigurerer Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

For å sette opp en Wallet med flere signaturer trenger du forskjellige maskinvarelommebøker. For en Multisig 2-de-3 kan du for eksempel bruke :




- En Trezor Model One;
- Ledger Flex;
- Et Coldcard MK3.



![Image](assets/fr/03.webp)



Det er en god idé å bruke forskjellige Hardware Wallet-merker i Multisig-konfigurasjonen. Dette sikrer at hvis en spesifikk modell støter på et alvorlig problem, vil det ikke påvirke den generelle sikkerheten til Multisig. I tillegg kan du dra nytte av de spesifikke fordelene ved hver enhet. For eksempel, i min konfigurasjon :





- Trezor Model One er helt åpen kildekode, noe som gjør det mulig å verifisere seed-generasjonen. Men siden den ikke er utstyrt med et Secure Element, er den fortsatt sårbar for fysiske angrep;





- Ledger Flex, derimot, har proprietær fastvare som ikke kan verifiseres, men er utstyrt med et Secure Element som gir utmerket fysisk beskyttelse;





- Coldcard er utstyrt med et Secure Element, og koden er søkbar. Det er et interessant valg for vår konfigurasjon, ettersom det tilbyr verifiseringsfunksjoner som ikke er tilgjengelige på andre modeller.



Før du konfigurerer din Multisig Wallet, må du sørge for at hver Hardware Wallet er riktig konfigurert (generering og lagring av Mnemonic, PIN-definisjon). For detaljerte instruksjoner kan du se våre veiledninger for hver Hardware Wallet, for eksempel :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Som vi skal se senere i denne veiledningen, er det også mulig å integrere en faktor i Multisig-konfigurasjonen som ikke er knyttet til en Hardware Wallet, men hvis private nøkler er lagret på PC-en din. Denne metoden er åpenbart mindre sikker enn den eksklusive bruken av maskinvarelommebøker, men den kan være relevant i visse tilfeller. For eksempel kan du for en Multisig 2-de-3 velge to maskinvare-lommebøker og én Software Wallet.



## Opprettelse av en Multisig-portefølje



Åpne Sparrow Wallet, klikk på fanen "*File*", og velg deretter "*New Wallet*".



![Image](assets/fr/04.webp)



Gi multisignaturporteføljen et navn, og klikk deretter på "*Opprett Wallet*" for å bekrefte.



![Image](assets/fr/05.webp)



I rullegardinmenyen "*Policy Type*" velger du alternativet "*Multi Signature*".



![Image](assets/fr/06.webp)



Øverst i høyre hjørne kan du nå definere det totale antallet nøkler i Multisig, samt hvor mange medunderskrivere som kreves for å godkjenne en utgift. I mitt eksempel er dette en 2-av-3-ordning.



![Image](assets/fr/07.webp)



Nederst i vinduet viser Sparrow Wallet tre "*Keystore*". Hver av dem representerer et sett med nøkler. Her bruker jeg tre maskinvareporteføljer, så hver "*Keystore*" tilsvarer en av dem. Nå skal vi konfigurere dem.



Jeg begynner med Coldcard. I fanen "*Keystore 1*" velger jeg alternativet "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Når enheten er låst opp på Coldcard, går jeg til menyen "*Settings*" og deretter til "*Multisig Wallets*".



![Image](assets/fr/09.webp)



I denne menyen kan du administrere Multisig-porteføljene som Coldcard deltar i. Jeg ønsker å opprette en ny, så jeg velger "*Eksporter XPUB*".



![Image](assets/fr/10.webp)



Hvis du bare administrerer én konto, kan du la feltet "*Kontonummer*" være tomt og validere direkte ved å trykke på bekreftelsesknappen.



![Image](assets/fr/11.webp)



Coldcard vil da generate en fil som inneholder xpub-en din, lagret på Micro SD-kortet.



![Image](assets/fr/12.webp)



Sett inn dette Micro SD-kortet i datamaskinen. I Sparrow Wallet klikker du på "*Importer fil...*"-knappen ved siden av "*Coldcard Multisig*", og velger deretter filen som er opprettet av Coldcard på kortet.



![Image](assets/fr/13.webp)



Din xpub har blitt importert. Vi gjentar nå prosedyren med de to andre maskinvarelommebøkene.



![Image](assets/fr/14.webp)



For Ledger Flex velger jeg "*Keystore 2*", og klikker deretter på "*Connected Hardware Wallet*". Kontroller at Ledger er koblet til datamaskinen, ulåst, og at Bitcoin-applikasjonen er åpen.



![Image](assets/fr/15.webp)



Klikk deretter på knappen "*Scan...*".



![Image](assets/fr/16.webp)



Ved siden av navnet på maskinvareporteføljen klikker du på "*Importer Keystore*".



![Image](assets/fr/17.webp)



Den andre signataren er nå korrekt registrert i Sparrow Wallet.



![Image](assets/fr/18.webp)



Jeg gjentar nøyaktig samme prosedyre med Trezor One for å fullføre Multisig-konfigurasjonen.



![Image](assets/fr/19.webp)



I min konfigurasjon dekker vi ikke dette tilfellet, men hvis du vil inkludere en signatur via en Software Wallet i Sparrow (Hot Wallet) i din Multisig, klikker du bare på knappen "*Ny eller importert Software Wallet*".



Nå som alle signaturenhetene dine er importert til Sparrow Wallet, kan du fullføre opprettelsen av Multisig ved å klikke på "*Apply*".



![Image](assets/fr/20.webp)



Velg et sterkt passord for å sikre tilgangen til Sparrow Wallet Wallet. Dette passordet beskytter dine offentlige nøkler, adresser, etiketter og transaksjonshistorikk mot uautorisert tilgang.



Husk å lagre dette passordet på et trygt sted, for eksempel i en passordbehandler, for å unngå å miste det.



![Image](assets/fr/21.webp)



## Sikkerhetskopiering av en Multisig-portefølje



Vi skal nå lagre vår *Output Script Descriptor* på Coldcard (dette gjelder bare brukere som har et Coldcard i Multisig), og fremfor alt skal vi ta en sikkerhetskopi av den på et uavhengig medium.



*Descriptor* inneholder alle xpubene i Multisig-porteføljen din, samt avledningsstiene som ble brukt til å generate-nøklene. Husk hva vi så i del 1: For å gjenopprette en Multisig-portefølje må du enten ha **alle** Mnemonic-frasene, eller bare det minste antallet som kreves for å nå signaturterskelen. I sistnevnte tilfelle er det imidlertid også viktig å ha **xpubene** til de manglende signatarene. *Descriptor* inneholder alle xpubene til Multisig.



Hvis dette ikke er klart, må du bare huske dette: For å hente en Multisig, trenger du minimum antall Mnemonic-fraser for hver Hardware Wallet som brukes, avhengig av terskelen (i mitt tilfelle: 2 fraser), samt *Descriptor*.



Denne *Deskriptoren* inneholder ingen private nøkler, bare offentlige. Dette betyr at den ikke gir tilgang til midlene. Den er derfor ikke like kritisk som Mnemonic-fraser, som gir full tilgang til bitcoinsene dine. Risikoen med *Descriptor* er utelukkende knyttet til konfidensialitet: I tilfelle kompromittering kan en tredjepart observere alle transaksjonene dine, men kan ikke bruke pengene dine.



Jeg anbefaler på det sterkeste at du lager flere kopier av denne *Descriptor*, og oppbevarer dem sammen med hver signeringsenhet på din Multisig. I mitt tilfelle skriver jeg for eksempel ut *Descriptor* på papir og oppbevarer én kopi sammen med Coldcard, en annen sammen med Trezor og en med Ledger. Jeg lagrer også *Descriptor* som en PDF-fil på tre USB-minnepinner, som hver oppbevares sammen med én av maskinvaremappene. På denne måten maksimerer jeg sjansene mine for å aldri miste *Descriptor*, og jeg er sikker på å ha to eksemplarer (ett fysisk og ett digitalt) på hver enhet.



Når Multisig-mappen din er opprettet, gir Sparrow deg automatisk denne *Descriptor*. Klikk på knappen "*Lagre PDF...*" for å lagre den både som tekst og som en QR-kode.



![Image](assets/fr/22.webp)



Deretter kan du skrive ut denne PDF-filen og kopiere den til USB-minnet ditt.



![Image](assets/fr/23.webp)



Vi registrerer også denne *Descriptor* i Coldcard (hvis du bruker en i konfigurasjonen din). Dette vil gjøre det mulig for Coldcard å verifisere at hver transaksjon som signeres senere, samsvarer med den opprinnelige Wallet: riktige xpubs, riktig Address-format, riktig avledningssti ... Uten denne importerte *Descriptor* kan Coldcard ikke bekrefte at Exchange-adresser ikke har blitt kapret eller at PSBT ikke har blitt tuklet med.



Det er dette som gjør Coldcard så interessant i en Multisig: Det tilbyr ekstra kontroller mot visse sofistikerte angrep, som andre maskinvarelommebøker ikke tillater (forutsatt, selvfølgelig, at du bruker det til å signere).



I Sparrow går du til menyen "*Settings*" og klikker deretter på "*Export...*".



![Image](assets/fr/24.webp)



Ved siden av alternativet "*Coldcard Multisig*" klikker du på "*Export File...*" og lagrer tekstfilen på Micro SD-kortet.



![Image](assets/fr/25.webp)



Sett deretter kortet inn i Coldcard. Gå til menyen "*Innstillinger*", deretter "*Multisig lommebøker*", og velg "*Importer fra SD*".



![Image](assets/fr/26.webp)



Velg den aktuelle filen og bekreft importen.



![Image](assets/fr/27.webp)



Klikk på navnet på den nylig importerte Multisig.



![Image](assets/fr/28.webp)



Kontroller Multisig-konfigurasjonsparametrene, og bekreft deretter registreringen.



![Image](assets/fr/29.webp)



Multisig er nå korrekt lagret på Coldcard. Hvis du har flere Coldcards i samme Multisig, gjentar du denne prosedyren for hvert av dem.



I tillegg til å lagre *Descriptor*, må du huske å være spesielt oppmerksom på å lagre Mnemonic-setningene for hver av signaturenhetene dine. Hvis du er nybegynner, anbefaler jeg på det sterkeste at du leser denne andre veiledningen for å lære hvordan du lagrer og håndterer dem på riktig måte:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Før du mottar dine første bitcoins på din Multisig, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Noter litt referanseinformasjon, for eksempel den første mottakende Address, og tilbakestill deretter maskinvarelommebøkene dine mens Wallet fortsatt er tom. Prøv deretter å gjenopprette Multisig Wallet på maskinvare-lommebøkene ved hjelp av Mnemonic-frasepapirsikkerhetskopiene dine, og deretter på Sparrow ved hjelp av *Descriptor*. Sjekk at den første Address som genereres etter gjenopprettingen, stemmer overens med den du opprinnelig skrev ned. Hvis den gjør det, kan du være sikker på at papirsikkerhetskopiene dine er pålitelige.



Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, anbefaler jeg at du leser denne andre veiledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Motta bitcoins på din Multisig



Din Wallet er nå klar til å motta bitcoins. I Sparrow klikker du på fanen "*Mottak*".



![Image](assets/fr/30.webp)



Før du bruker Address generert av Sparrow Wallet, bør du ta deg tid til å sjekke den direkte på skjermen på maskinvarelommebøkene dine. Dette vil sikre at Address ikke har blitt endret, og at enhetene dine har de private nøklene som trengs for å bruke de tilknyttede midlene. Dette bidrar til å beskytte deg mot en rekke angrepsvektorer.



Dette gjør du ved å klikke på "*Display Address*" for å vise Address på Trezor eller Ledger når den er koblet til via kabel.



![Image](assets/fr/31.webp)



Med Coldcard kan denne verifiseringen utføres uten noen interaksjon med Sparrow. Bare åpne "*Address Explorer*"-menyen, og velg deretter din Multisig helt nederst.



![Image](assets/fr/32.webp)



Du vil da se mottaksadressene som genereres av Multisig.



![Image](assets/fr/33.webp)



Kontroller at Address som vises på hver Hardware Wallet, stemmer nøyaktig overens med Wallet i Sparrow Wallet. Det anbefales å gjøre dette rett før du deler Address med betaleren, for å være sikker på at den er korrekt.



Du kan deretter tildele en "*Label*" til denne Address for å angi opprinnelsen til de mottatte bitcoinsene. Dette er en god måte å organisere håndteringen av UTXO-ene dine på.



![Image](assets/fr/34.webp)



Når dette er bekreftet, kan du bruke Address til å motta bitcoins.



![Image](assets/fr/35.webp)



## Sende bitcoins med din Multisig



Nå som du har mottatt dine første Satss på din Multisig Wallet, kan du også bruke dem! I Sparrow går du til "*Send*"-fanen for å opprette en ny transaksjon.



![Image](assets/fr/36.webp)



Hvis du ønsker å bruke *Coin Control*, dvs. manuelt velge UTXO-er du ønsker å bruke, går du til fanen "*UTXOs*". Velg UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir automatisk omdirigert til "*Send*"-fanen, der UTXO-ene allerede er forhåndsutfylt.



![Image](assets/fr/37.webp)



Skriv inn destinasjonen Address. Du kan legge til flere adresser ved å klikke på "*+ Legg til*".



![Image](assets/fr/38.webp)



Legg til en "*Label*" for å beskrive formålet med denne utgiften, slik at det blir enklere å spore transaksjonene.



![Image](assets/fr/39.webp)



Angi beløpet som skal sendes til den valgte Address.



![Image](assets/fr/40.webp)



Juster ladehastigheten i henhold til gjeldende nettverksforhold. Se for eksempel [Mempool.space] (https://Mempool.space/) for å velge et passende ladenivå.



Når du har kontrollert alle transaksjonsparametrene, klikker du på "*Opprett transaksjon*".



![Image](assets/fr/41.webp)



Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Nederst på skjermen ser du at Sparrow venter på to signaturer. Dette er normalt: Wallet som brukes her, er en Multisig 2-de-3.



![Image](assets/fr/43.webp)



Jeg begynner å signere med Coldcard-kortet mitt. For å gjøre dette setter jeg inn et Micro SD-kort i datamaskinen, og klikker deretter på "*Save Transaction*".



![Image](assets/fr/44.webp)



Det finnes tre måter å overføre transaksjonen som skal signeres til Hardware Wallet, og deretter hente den fra Sparrow. Den første er å bruke et Micro SD-kort, som vi skal gjøre her for Coldcard. Den andre er via en kabelforbindelse, som vi vil bruke for den andre signaturen (Ledger og Trezor). Til slutt er det mulig å bruke QR-kodekommunikasjon, for kamerautstyrte enheter som Coldcard Q, Jade Plus eller Passport V2.



Når PSBT (*Partially Signed Bitcoin Transaction*) er lagret på Micro SD-kortet, setter jeg det inn i Coldcard MK3, og velger deretter menyen "*Klar til å signere*".



![Image](assets/fr/45.webp)



På Hardware Wallet-skjermen kontrollerer du nøye transaksjonsparametrene: mottakerens Address, beløpet som er sendt, og gebyrene. Når transaksjonen er bekreftet, validerer du for å gå videre til signering.



![Image](assets/fr/46.webp)



Sett deretter Micro SD-kortet tilbake på datamaskinen, og klikk på "*Load Transaction*" i Sparrow. Velg PSBT signert av Coldcard fra filene dine.



![Image](assets/fr/47.webp)



Du kan se at Coldcard-signaturen er lagt til. Jeg skal nå bruke en annen enhet, i dette tilfellet Ledger, til å utføre den andre signaturen som kreves. Jeg kobler den til, låser den opp og klikker deretter på "*Sign*" på Sparrow.



![Image](assets/fr/48.webp)



Klikk på "*Signer*" ved siden av navnet på din Hardware Wallet.



![Image](assets/fr/49.webp)



Første gang du bruker Ledger med denne Multisig, vil Sparrow be deg om å verifisere de utvidede offentlige nøklene (xpubs) til medsignererne. Som med Coldcard forhindrer dette trinnet at du signerer i blinde senere. For å validere denne informasjonen kan du sammenligne xpub-en som vises på Ledger-skjermen, med de du får direkte fra de andre maskinvarelommebøkene dine.



![Image](assets/fr/50.webp)



Kontroller mottakerens Address, beløpet som overføres og transaksjonsgebyret, og signer deretter transaksjonen.



![Image](assets/fr/51.webp)



Trykk på skjermen for å signere.



![Image](assets/fr/52.webp)



Sparrow har nå de to signaturene som trengs for å frigjøre midlene fra Multisig-porteføljen. Kontroller transaksjonen en siste gang, og hvis alt går bra, klikker du på "*Broadcast Transaction*" for å sende den over nettverket.



![Image](assets/fr/53.webp)



Du finner denne transaksjonen i Sparrow Wallets "*Transaksjoner*"-fane.



![Image](assets/fr/54.webp)



Gratulerer, du vet nå hvordan du setter opp og bruker en multisignatur Wallet på Sparrow. Hvis du synes denne veiledningen var nyttig, vil jeg være takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Takk for at du deler!



Hvis du vil gå videre, anbefaler jeg at du leser denne veiledningen om en annen metode for å øke sikkerheten til din Bitcoin Wallet, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7