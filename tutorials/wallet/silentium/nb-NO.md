---
name: Silentium
description: Progressiv web wallet med støtte for stille betalinger (BIP-352)
---

![cover](assets/cover.webp)



Gjenbruk av Bitcoin-adresser er en av de mest direkte truslene mot brukernes konfidensialitet. Når en mottaker deler en enkelt adresse for å motta flere betalinger, kan enhver observatør spore alle tilknyttede transaksjoner og rekonstruere deres økonomiske historie. Dette problemet rammer særlig innholdsskapere, veldedige organisasjoner eller aktivister som ønsker å vise en donasjonsadresse offentlig uten at det går på bekostning av personvernet.



Silentium svarer på dette problemet med en elegant løsning som er tilgjengelig direkte fra nettleseren din. Denne progressive webapplikasjonen (PWA) med åpen kildekode, som ble lansert i mai 2024 av Louis Singer, implementerer Silent Payments (BIP-352): en gjenbrukbar statisk adresse der hver betaling havner på en separat blokkjedeadresse, uten forutgående interaksjon eller observerbar kobling mellom transaksjoner.



**Viktig advarsel**: Silentium er et eksperimentelt prosjekt som fungerer som et *proof-of-concept* for Silent Payments' lette lommebøker. Det bør ikke brukes som en daglig wallet eller til lagring av betydelige beløp. Utviklerne oppgir eksplisitt:



> Bruk på eget ansvar.

Merk at denne wallet kan brukes som testnett eller regtest.



## Hva er Silentium?



### Filosofi og målsettinger



Silentium fungerer som en teknisk demonstrasjon for implementering av Silent Payments i en lett wallet-nettleser. Selv om den også støtter konvensjonelle Bitcoin-adresser, ligger hovedvekten på Silent Payments, slik at brukerne kan eksperimentere med denne personvernteknologien på en enkel måte.



### Hvordan fungerer Silent Payments?



Silent Payments (BIP-352) bruker Elliptic Curve Diffie-Hellman-nøkkelen Exchange (ECDH). Mottakeren genererer en statisk adresse (`sp1...` på mainnet, `tsp1...` på testnet) som består av to offentlige nøkler: en skanne-nøkkel for å oppdage betalinger, og en utgiftsnøkkel for å bruke dem.



Avsenderen kombinerer sine private inngangsnøkler med mottakerens skannøkkel for å beregne en delt hemmelighet som genererer en kryptografisk "tweak". Denne "tweaken", som legges til utgiftsnøkkelen, skaper en unik Taproot-adresse for hver transaksjon. Mottakeren reproduserer denne beregningen med sin private skannøkkel for å oppdage og bruke pengene uten noen forutgående interaksjon.



Fordeler: økt konfidensialitet for avsender og mottaker, ingen tredjepartsserver nødvendig, transaksjoner som ikke kan skilles fra konvensjonelle Taproot-betalinger. Største ulempe: intensiv skanning av blokkjeden for å oppdage betalinger.



For å finne ut mer om hvordan Silent Payments fungerer teoretisk, se siste del av BTC,204-kurset på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Støttede plattformer



Silentium er en Progressive Web App (PWA) som er tilgjengelig fra alle moderne nettlesere (mobil eller stasjonær). Du kan bruke den direkte på `app.silentium.dev`, installere den som en egen applikasjon via nettleseren, eller distribuere den lokalt. Installasjonen gjøres direkte fra nettleseren, uten å gå gjennom de offisielle butikkene.



## Bruke webappen



### Tilgang og installasjon



[Gå til `https://app.silentium.dev/` fra nettleseren din](https://app.silentium.dev/). Programmet lastes inn umiddelbart og viser startskjermen.



For å installere den som en egen applikasjon på iOS, trykker du på delingsknappen (firkantet med pil oppover) og velger deretter "På startskjermen". På Android tilbyr nettleseren vanligvis et "Legg til på startskjermen"-varsel direkte. Når Silentium er installert, vises det med et eget ikon og fungerer som en innebygd applikasjon, men krever en internettforbindelse for å synkronisere transaksjoner.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Opprettelse av portefølje



Ved første oppstart velger du "Opprett Wallet" for å opprette en ny generate-portefølje, eller "Gjenopprett Wallet" for å gjenopprette fra en eksisterende gjenopprettingsfrase.



Velg "Opprett Wallet". Programmet genererer en setning på 12 ord som du må skrive ned nøye. Denne frasen er den eneste måten å gjenopprette pengene dine på. Selv på testnettet må du bruke gode sikkerhetskopieringsrutiner. Trykk på "Fortsett" etter at du har lagret frasen.



Programmet ber deg deretter om å angi et passord for å sikre tilgangen til wallet. Velg et sterkt passord, og bekreft det.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Når frasen er bekreftet og passordet er angitt, kommer du til hovedgrensesnittet.



### Interface hoved- og parametere



Hovedgrensesnittet viser saldoen din i satoshier (i utgangspunktet 0 sats), med tre knapper nederst:




- Sync**: synkroniserer wallet med blokkjeden
- Motta**: å motta midler
- Send**: for å sende bitcoins



Gå til Innstillinger via ikonet øverst til høyre (tre horisontale streker). Innstillinger-menyen tilbyr flere alternativer:





- Om**: søknadsinformasjon
- Sikkerhetskopi**: sikkerhetskopi av gjenopprettingsfrasen
- Utforsker**: velg blokkjedeutforsker (Mempool som standard) og Silentiumd-server
- Nettverk**: valg av nettverk (mainnet/testnet)
- Passord**: endre passord
- Reload**: omlasting av wallet
- Reset**: fullstendig tilbakestilling
- Tema**: endre tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Avsnittet **Explorer** er spesielt viktig: her kan du velge hvilken blokkjedeutforsker som skal brukes (Mempool som standard), og du kan også vise URL-en til Silentiumd-serveren (`https://bitcoin.silentium.dev/v1` for mainnet). Hvis du er vert for din egen Silentiumd-server eller ønsker å bruke testnet, er det her du konfigurerer disse parameterne.



### Mottak av midler



Fra hovedgrensesnittet trykker du på "Motta"-knappen. Som standard viser Silentium en Silent Payment-adresse med QR-kode. Adressen starter med `sp1...` på mainnet eller `tsp1...` på testnet.



Du kan bytte mellom Silent Payment og klassiske Bitcoin-adresser ved hjelp av knappen "Bytt til klassisk adresse" / "Bytt til stille adresse" nederst på skjermen.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Når transaksjonen har blitt sendt, må du vente noen minutter. For Silent Payments skanner Silentium automatisk blokkjeden etter transaksjoner som er beregnet på deg. Transaksjoner vises med statusen "Ubekreftet" før de gradvis blir bekreftet.



### Send en betaling



Fra hovedgrensesnittet trykker du på "Send"-knappen. Send-skjermen vil spørre deg om :



1. **Address**: Lim inn en Silent Payment-adresse (`sp1...` eller `tsp1...`) eller en klassisk Bitcoin-adresse. Du kan bruke QR-skanneikonet til å skanne en adresse.


2. **Beløp**: Angi beløpet i satoshier som skal sendes. Et numerisk tastatur vises for enkel inntasting. Den tilgjengelige saldoen vises øverst for referanse.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Når du har lagt inn adressen og beløpet, trykker du på "Fortsett" for å fortsette. Programmet vil be deg om å velge ønsket gebyrnivå før du bekrefter transaksjonen.



## wallet selvhosting



### Hvorfor selv-hosting?



Silentiums lokale hosting tilbyr total suverenitet, kodeverifisering, et utviklingsmiljø og robusthet i møte med feil på det offisielle nettstedet.



### Forutsetninger



Node.js (versjon 14+), npm eller yarn, Git og rundt 500 MB diskplass.



### Lokal installasjon



Klon depotet og installer :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Lansering og bruk



Start programmet i utviklingsmodus:



```bash
yarn start
```



Gå til `http://localhost:3000` i nettleseren din. For en optimalisert produksjonsversjon :



```bash
yarn build
```



Filer som genereres i `build/` kan betjenes med nginx, Apache eller en hvilken som helst webserver. Som standard kobler Silentium seg til den offentlige serveren `bitcoin.silentium.dev`. Endre denne innstillingen i parameterne for å bruke testnet eller din egen server.



## Silentiumd-serveren



### Rolle og drift



Silentium bruker en **Silentiumd**-indekseringsserver for å optimalisere betalingsdeteksjonen. Å skanne alle Taproot-transaksjoner ville vært for tungvint for en nettleser eller mobiltelefon.



Silentiumd forhåndsberegner mellomliggende data (tweaks) for hver Taproot-transaksjon. wallet laster ned disse justeringene (noen få byte per transaksjon) og utfører den endelige beregningen lokalt, og verifiserer eierskapet til betalingen. Serveren kjenner aldri nøklene dine eller kan identifisere transaksjonene dine, i motsetning til konvensjonelle Electrum-servere.



Med kompakte BIP158-filtre kan wallet bestemme hvilke blokker som skal skannes uten å avsløre adressene dine, slik at konfidensialiteten din bevares.



### Offentlig server



Den offentlige serveren `bitcoin.silentium.dev` (mainnet), sponset av Vulpem Ventures, tilbyr en enkel og umiddelbar opplevelse. Selv om konfidensialiteten er ivaretatt, innebærer denne tilnærmingen relativ tillit til tredjeparts infrastruktur.



### Vertskap for din egen Silentiumd-server



For total suverenitet kan du være vert for din egen Silentiumd-server. Forutsetninger: Bitcoin Core ikke-elagged node med `txindex=1` og `blockfilterindex=1`, Go 1.21+, 10-20 GB diskplass, ferdigheter i systemadministrasjon.



**Installasjon:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigurer via miljøvariabler (se arkivets `config.md` for detaljer). Serveren indekserer blokkjeden og eksponerer en API som kan spørres av din wallet.



Det finnes for øyeblikket ingen pakkeløsninger for Umbrel eller Start9, noe som begrenser tilgjengeligheten for ikke-tekniske brukere.



## Fordeler og begrensninger



### Høydepunkter





- Maksimal tilgjengelighet**: kan brukes fra hvilken som helst nettleser, uten behov for tung installasjon
- Multiplattform**: fungerer på mobil (Android/iOS) og datamaskin takket være PWA-teknologi
- Enkel selvhosting**: lokal installasjon mulig med noen få kommandoer
- Åpen kildekode**: fullstendig reviderbar kode på GitHub
- Personvernfokus**: ingen sporing, ingen analyser, lokale kryptografiske beregninger
- Separat arkitektur**: tydelig skille mellom wallet (klient) og indekseringsserver
- Uten konto**: ingen registrering eller personopplysninger kreves



### Begrensninger å ta hensyn til





- Eksperimentelt prosjekt**: kun konseptbevis, ikke ment for daglig bruk eller produksjon
- Ingen garantier**: risiko for feil, sårbarheter, mulig tap av midler
- Begrenset støtte**: lite brukerdokumentasjon, lite fellesskap, ingen offisiell støtte
- Serveravhengighet**: krever en fungerende Silentiumd-server (offentlig eller selvbetjent)
- Intensiv skanning**: Stille betalingsdeteksjon bruker båndbredde
- Redusert funksjonalitet**: ingen myntkontroll, ingen Lightning, ingen multisignaturer



## Beste praksis



### seed sikkerhet



Selv på testnet må du ta gjenopprettingsfrasen din på alvor. Skriv den ned og oppbevar den på et trygt sted. Ha separate lommebøker for testnett og mainnet: Bruk aldri en test-seed på en wallet som er beregnet på ekte midler.



### Verifisering av kildekode



En av fordelene med selvhosting er muligheten til å sjekke kildekoden før du kjører den. Hvis du planlegger å bruke Silentium med ekte penger, bør du ta deg tid til å revidere koden eller få en pålitelig utvikler til å gjøre det. Sammenlign også hashen til koden som er distribuert på `app.silentium.dev` med koden i GitHub-depotet for å sikre autentisitet.



### Sikkerhetskopiering og gjenoppretting



Gjenoppretting av Silent Payments-midler krever en wallet som er kompatibel med BIP-352-protokollen. En standard wallet kan ikke skanne blokkjeden for å hente UTXO Silent Payments. Ha Silentium installert eller sørg for at du har tilgang til en annen kompatibel wallet (for eksempel Cake Wallet eller andre fremtidige implementeringer) for å gjenopprette midlene dine om nødvendig.



## Konklusjon



Silentium gir et tilgjengelig testområde for å forstå Silent Payments uten teknisk friksjon. Som et bevis på konseptet demonstrerer Silentium hvordan denne personvernteknologien kan integreres i en wallet-nettleser samtidig som selvoppbevaringen bevares. Eksperimenter på testnet for å oppdage dette lovende gjennombruddet for on-chain-personvern.



## Ressurser



### Offisiell dokumentasjon




- Silentium GitHub-arkiv (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub-depot (server): https://github.com/louisinger/silentiumd
- Webapplikasjon: https://app.silentium.dev/
- Felles nettsted for Silent Payments: https://silentpayments.xyz
- Spesifikasjon BIP-352: https://bips.dev/352



### Artikler og ressurser




- Offisiell kunngjøring (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Stille betalinger: https://bitcoinops.org/en/topics/silent-payments/



### Testnet-verktøy




- Testnet kran: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet