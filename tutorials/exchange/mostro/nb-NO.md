---
name: Mostro
description: KYC-fri Bitcoin P2P utvekslingsplattform via Lightning og Nostr
---

![cover](assets/cover.webp)



Hvordan kan du kjøpe eller selge bitcoins uten å kompromittere din økonomiske suverenitet? Sentraliserte plattformer pålegger invasive KYC-prosedyrer som eksponerer personopplysningene dine, med mulighet for vilkårlig frysing av kontoer eller statlig overvåking.



**Mostro P2P** tilbyr et desentralisert alternativ som kombinerer Lightning Network, Nostr-protokollen og hold-fakturaer. Den viktigste innovasjonen er et automatisert escrow-system der bitcoinsene dine forblir under din kontroll gjennom hele børsen, noe som eliminerer risikoen for tyveri, børskonkurs eller vilkårlig konfiskering.



## Hva er Mostro P2P?



Mostro P2P er en åpen kildekode Bitcoin utvekslingsprotokoll opprettet av **grunch **, utvikler av den populære Telegram-bot **lnp2pbot ** lansert i 2021. Mens lnp2pbot allerede aktiverte KYC-fri P2P-utveksling via Lightning, presenterte den en stor sårbarhet: **Telegram utgjør et sentralisert feilpunkt** som er utsatt for sensur fra myndigheter.



Mostro representerer den **desentraliserte evolusjonen** av dette konseptet: Ved å erstatte Telegram med **Nostr**-protokollen (et usensurabelt nettverk av distribuerte reléer), eliminerer Mostro denne systemiske risikoen. Protokollen kombinerer Lightning Network for øyeblikkelige transaksjoner, Nostr for sensurresistent kommunikasjon og **hold-fakturaer** for å skape en virkelig ikke-frihetsberøvende automatisert deponering.



### Teknisk arkitektur



Mostro fungerer gjennom tre komponenter:




- Daemon Mostrod**: koordinerer utvekslinger mellom brukere og Lightning Network
- Lightning**-node: oppretter ventende fakturaer (~24 timer kryptografisk sperring)
- Mostro**-kunder: brukergrensesnitt (CLI, mobil, web)



Ordrer publiseres på Nostr som offentlige hendelser (type 38383), mens private handler overføres via ende-til-ende-krypterte meldinger (NIP-59, NIP-44). Hver Mostro-instans definerer sine egne gebyrer (vanligvis mellom 0,3 % og 1 %) og transaksjonsgrenser (fra noen få tusen til flere hundre tusen sats, avhengig av instans).



### Avgjørende fordeler



**Motstandsdyktig mot sensur**: Ingen myndigheter kan stenge Mostro så lenge det finnes Nostr-reléer et eller annet sted i verden. I motsetning til den sårbare lnp2pbot via Telegram, tillater Mostro utveksling som er **sensursikker**.



**Escrow ikke-frihetsberøvende **: Lightning hold-fakturaer låser bitcoinsene dine uten å overføre dem permanent. Midlene dine forblir under din kontroll og returneres automatisk til deg i tilfelle et problem (~ 24 timer).



**Designet for konfidensialitet**: To moduser er tilgjengelige for å dekke dine behov. Omdømmemodus** knytter omdømmet ditt til Nostr-nøkkelen din for å bygge varig tillit. Fullstendig privat modus** gir deg absolutt anonymitet med engangsnøkler.



## Hovedfunksjoner



**Desentralisert kommunikasjon**: Alle bestillinger publiseres på Nostr via kryptografisk signerte hendelser. Private forhandlinger overføres via ende-til-ende-krypterte meldinger, noe som garanterer absolutt konfidensialitet.



**Reputasjonssystem**: 5-stjerners rangering med iterativ beregning som lagres permanent på Nostr. Lar deg gradvis bygge opp et rykte som en pålitelig trader.



**Desentralisert voldgift**: I tilfelle en tvist undersøker en upartisk voldgiftsdommer bevisene og tar en avgjørelse basert på transparente kriterier. Hver tvist genererer en unik token for sporbarhet.



**Fleksibilitet i betaling**: Støtte for mange fiat-valutaer via yadio.ios valutakurstjeneste. Aksepterer SEPA-overføringer, PayPal, Revolut, kontanter og alle metoder som er avtalt mellom partene.



## Mostro-kunder tilgjengelig



Mostro tilbyr to hovedklienter for P2P-sentralene dine.



### Mostro CLI - Kommandolinjeklient



**Mostro CLI** er den mest modne og funksjonelle klienten. Den er skrevet i Rust og tilbyr alle Mostro-funksjonene via et kommandolinjegrensesnitt. Kompatibel med macOS, Linux og Windows.



**Hovedkontroller** :




- `lister over bestillinger`: Viser alle tilgjengelige bestillinger
- `neworder` : Opprett en ny kjøps- eller salgsordre
- `takesell` / `takebuy`: Ta en kjøps- eller salgsordre
- `fiatsent`: Bekreft sending av fiat-betaling
- `release`: Frigjør spærringen og sluttfører utvekslingen
- `getdm`: Vis direkte meldinger
- `rate` : Evaluer motparten din etter en utveksling



Ideell for tekniske brukere, automatisering og miljøer som krever maksimal sikkerhet.



### Mostro Mobile - Applikasjon for smarttelefon



**Mobilappen** i alfaversjon gjør det mulig å handle P2P direkte fra smarttelefonen. Intuitiv grafisk Interface med fanenavigering, ordrevisning, avanserte filtre og integrert chat for å kommunisere med motpartene dine.



Tilgjengelig for ** Android ** (via APK på GitHub), er det det optimale valget for brukere som foretrekker enkelhet og sporadisk mobilhandel.



### Mostro-web - Interface web (under utvikling)



Interface avansert JavaScript-webapplikasjon under aktiv utvikling. Designet for å tilby en komplett brukeropplevelse med omfattende handels- og porteføljeforvaltningsfunksjoner. Tilgang via nettleser uten behov for installasjon.



## Installasjon og konfigurasjon



Denne veiledningen vil veilede deg gjennom installasjon og bruk av de to viktigste Mostro-klientene: CLI og mobilapplikasjonen.



### Viktige forutsetninger



Før du begynner, trenger du :





- En fungerende Lightning Network** wallet med tilstrekkelig likviditet (eller Lightning-kompatibel)
 - Anbefales: Phoenix, Breez, Wallet eller Satoshi...
 - Minimum 1000 satoshis i likviditet for å teste



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- En privat nøkkel fra Nostr** (format `nsec1...`)
 - Opprett en dedikert handelsnøkkel på [nostrkeygen.com] (https://nostrkeygen.com/)
 - Viktig**: Bruk aldri din personlige hovednøkkel Nostr
 - Oppbevar den private nøkkelen på et trygt sted (passordbehandler)





- Valgfritt, men anbefalt**: VPN- eller Tor-tilkobling for å maskere IP-adressen din



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Installasjon av Mostro CLI



#### På macOS



**Trinn 1: Rust-sjekk**



Kontroller at Rust er installert (versjon 1.64+ kreves):



```bash
rustc --version
```



Hvis Rust ikke er installert :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Trinn 2: Kloning av depotet**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Trinn 3: Konfigurasjon**



Kopier og rediger :



```bash
cp .env-sample .env
```



Åpne `.env` og konfigurer innstillingene dine:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Viktig for synkronisering mellom CLI og mobil**: For å få tilgang til de samme ordrene på CLI og i mobilappen, må du bruke **samme Mostro Pubkey** og **samme Nostr-reléer** i begge klientene. Sjekk disse innstillingene i Innstillinger i mobilappen.



![Configuration .env](assets/fr/02.webp)



**Trinn 4: Installasjon**



Kompilere og installere CLI :



```bash
cargo install --path .
```



Kompileringen tar 1-2 minutter. Den kjørbare filen `mostro-cli` vil bli installert i `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Trinn 5: Sjekk**



Kontroller at alt fungerer:



```bash
mostro-cli --help
```



Du bør se den komplette listen over bestillinger.



![Vérification avec --help](assets/fr/04.webp)



#### På Linux (Ubuntu/Debian)



Installasjonen er identisk med macOS, med tillegg av :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Følg deretter trinn 3 og 4 i macOS-delen.



#### På Windows



Installer først Rust via [rustup.rs] (https://rustup.rs/), og bruk deretter PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identisk konfigurasjon: kopier `.env-sample` til `.env` og fyll inn parametrene dine.



### Installere Mostro Mobile



#### På Android



**Trinn 1**: Gå til [GitHub-utgivelsessiden] (https://github.com/MostroP2P/mobile/releases) og last ned filen **app-release.apk** (ca. 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Trinn 2: Når du har lastet ned, åpner du APK-filen fra nedlastningene dine. Android vil be deg om å godkjenne installasjonen fra denne kilden.



![Téléchargement et installation APK](assets/fr/11.webp)



**Trinn 3**: Følg skjermbildene som presenterer funksjonalitetene:




- Handle Bitcoin fritt - ingen KYC** : Handel uten identitetsbekreftelse takket være Nostr
- Personvern som standard**: Velg mellom Omdømme-modus og Fullt personvern-modus
- Sikkerhet i hvert eneste trinn**: Beskyttelse med fakturaer som ikke er frihetsberøvende



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Trinn 4**: Fortsett ombordstigningen for å oppdage :




- Fullstendig kryptert chat**: Ende-til-ende-kryptert kommunikasjon
- Ta et tilbud**: Bla gjennom ordreboken og velg et tilbud
- Finner du ikke det du trenger? Lag din egen tilpassede bestilling



![Suite onboarding](assets/fr/13.webp)



**Trinn 5: Når onboardingen er fullført, genererer appen automatisk et par Nostr-nøkler. Gå til menyen (☰) og deretter **Account** for å lagre dine **Secret Words** (gjenopprettingsfrase). Det er også på dette skjermbildet at du har muligheten til å endre personvernmodus som tidligere nevnt.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Viktig**: Skriv ned gjenopprettingsfrasen din på et trygt sted (passordbehandler, papirsafe).



### Innledende sikkerhetskonfigurasjon



Uansett hvilken plattform du bruker :





- Dedikert nøkkel**: Bruk en egen Nostr-identitet for handel
- Små beløp**: Begynn med mindre enn 10 000 sats for å komme i gang
- Flere releer**: Konfigurer 3-5 geografisk forskjellige releer
- Nettverksbeskyttelse**: Aktiver VPN eller Tor for å skjule IP-adressen din
- Wallet sikker**: Aktiver automatisk låsing av din wallet Lightning



## Brukes med CLI



Denne delen demonstrerer kjøp av bitcoins via Mostro CLI ved å følge et virkelig brukstilfelle.



### Trinn 1: Liste over tilgjengelige bestillinger



Kommandoen `listororders` viser alle aktive bestillinger:



```bash
mostro-cli listorders
```



Du vil se en tabell med detaljer om hver ordre: ID, type (kjøp/salg), beløp, valuta og betalingsmåte.



![Liste des ordres disponibles](assets/fr/05.webp)



I dette eksempelet er en ordre om å selge 5 EUR via Revolut synlig (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Trinn 2: Ta imot bestillingen



For å kjøpe disse bitcoins, ta bestillingen med `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro vil be deg om å oppgi en **Lightning-faktura** for å motta BTC. Det nøyaktige beløpet i satoshis er angitt (her: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Trinn 3: Lever Lynfakturaen din



Generer en Lightning-faktura fra din wallet (Phoenix, Breez osv.) for det nøyaktige beløpet, og send den deretter :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Systemet bekrefter forsendelsen og ber deg vente på at selgeren betaler hold-fakturaen før du aktiverer spærringen.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Trinn 4: Kontakt selgeren



Når escrow er aktivert, kan du bruke `dmtouser` til å be om betalingsinformasjon fra selgeren:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Trinn 5: Hent svaret



Sjekk direktemeldinger for å se svaret fra selgeren:



```bash
mostro-cli getdm
```



Selgeren gir deg sin betalings-ID (her hans Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Trinn 6: Utføre fiat-betalingen



Send betalingen via den avtalte metoden (Revolut i dette eksempelet) til kontaktopplysningene som er oppgitt. **Ta vare på alle støttedokumenter** (skjermbilder, transaksjonsreferanser).



### Trinn 7: Bekreft betalingsforsendelse



Når betalingen er utført, må du varsle Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Trinn 8: Mottak av bitcoins



Så snart selgeren bekrefter mottak av fiat og frigjør sperringen med kommandoen `release`, mottar du øyeblikkelig bitcoinsene dine på Lightning-fakturaen du oppga.



### Trinn 9: Evaluering



Vurder selgeren for å bidra til det desentraliserte omdømmet:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Nyttige kommandoer



**Annullere en bestilling** (før den er tatt) :


```bash
mostro-cli cancel -o <order-id>
```



**Opprett en ny salgsordre** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Åpne en tvist** :


```bash
mostro-cli dispute -o <order-id>
```



## Bruk med mobilapplikasjonen



Denne delen demonstrerer salg av bitcoins via Mostro Mobile ved å følge et virkelig brukstilfelle.



### Interface hoved



Programmet har tre hovedfaner:





- Ordrebok**: Bla gjennom tilgjengelige kjøps- (BUY BTC) og salgsordrer (SELL BTC)
- Mine handler**: Se dine aktive og historiske ordrer
- Chat**: Kommuniser med motpartene dine ved hjelp av tall



![Interface principale](assets/fr/14.webp)



### Anbefalt konfigurasjon



Før du handler, må du konfigurere noen innstillinger via menyen (☰) > **Innstillinger** :





- Lyn Address** (valgfritt): For å motta betalinger direkte
- Reléer**: Legg til flere Nostr-reléer for robusthet (f.eks. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Sjekk den offentlige nøkkelen til Mostro-instansen du bruker



![Paramètres de l'application](assets/fr/16.webp)



**Viktig for synkronisering mellom CLI og mobil**: Hvis du bruker både CLI og mobilappen, må du konfigurere **eksakt de samme Nostr-reléene og Mostro Pubkey** i begge klientene. Uten denne identiske konfigurasjonen vil du ikke se de samme ordrene tilgjengelig på begge grensesnittene. Reléene og Mostro Pubkey som er synlige i Innstillinger (skjermbilde ovenfor) må samsvare med dem i CLI `.env'-filen din.



### Trinn 1: Opprett en salgsordre



Trykk på den grønne **"+"**-knappen nederst til høyre, og velg deretter **SELL** (rød knapp).



![Boutons de création d'ordre](assets/fr/17.webp)



Fyll ut opprettelsesskjemaet :



1. **Valuta**: Velg valutaen du ønsker å motta (EUR, USD osv.)


2. **Beløp** : Angi beløpet i fiat (f.eks. 1 til 3 EUR)


3. **Betalingsmetoder** : Velg metode (f.eks. "Revolut")


4. **Pristype**: Velg "Markedspris"


5. **Premie**: Juster premien (glidebryter fra -10 % til +10 %, anbefalt: 0 % for å selge raskt)



Trykk på **Send** for å publisere bestillingen din.



### Trinn 2: Bekreftelse av publisering



Bestillingen din er nå publisert! Den vil være tilgjengelig i 24 timer. Du kan avbryte den når som helst før en kjøper tar den ved å utføre kommandoen `cancel`.



![Ordre publié](assets/fr/18.webp)



Ordren vises i **Mine handler**-fanen med statusen "Venter" og merket "Opprettet av deg".



### Trinn 3: En innkjøper tar imot bestillingen din



Når en kjøper tar bestillingen din, mottar du et varsel. Se detaljer i **Mine handler**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Viktig instruksjon**: Du må nå **betale hold-fakturaen** som vises for å låse bitcoinsene dine (her 4674 sats for 1-5 EUR) i escrow. Du har **15 minutter maksimalt** ellers vil utvekslingen bli kansellert.



Kopier hold-fakturaen og betal den fra din wallet Lightning (Phoenix, Breez osv.).



### Trinn 4: Kommuniser med kjøperen



Når spærringen er aktivert, trykker du på **KONTAKTER** for å åpne den krypterte chatten med kjøperen.



Kjøperen (her "anonymous-gloriaZhao") vil kontakte deg for å be om betalingsinformasjonen din. Vennligst svar med dine detaljer (Revtag, IBAN, etc.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Trinn 5: Mottak av fiat-betaling



Vent til du mottar fiat-betalingen på Revolut-kontoen din (eller annen avtalt metode). **Sjekk nøye**:




- Det nøyaktige beløpet
- Avsenderen
- Referansen, hvis ønsket



Kjøperen vil informere deg via chat om at han har sendt betalingen. Mostro vil også vise en melding som bekrefter at fiat har blitt sendt til deg.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Trinn 6: Frigjør spærringen



Når du har **bekreftet mottak** av fiat-betalingen på kontoen din, trykker du på den grønne **RELEASE**-knappen og bekrefter at du vil sende satssen til kjøperen.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins overføres umiddelbart til kjøperen via lynfakturaen hans.



### Trinn 7: Evaluer hensynet



Etter utgivelsen trykker du på **RATE** for å rangere kjøperen. Velg mellom 1 og 5 stjerner (her 5/5), og trykk på **Send vurdering**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Utvekslingen er over!



### Kjøp bitcoins med mobilappen



Prosessen for å **kjøpe** bitcoins er lik, men omvendt:



1. Bla gjennom **Orderbok** > **KJØP BTC**-fanen for å se salgsordrer


2. Klikk på en interessant ordre for å se detaljer


3. Trykk **Ta bestilling**


4. Lever Lightning-fakturaen din (generert fra wallet)


5. Vent på at selgeren aktiverer deponeringen


6. Kontakt selgeren via **KONTAKTA** for betalingsdetaljer


7. Send fiat-betaling (oppbevar bevis)


8. Selger frigir sperret konto etter verifisering


9. Motta bitcoins umiddelbart på lynfakturaen din


10. Vurder selgeren (1-5 stjerner)



### Problemhåndtering



**Avbestill en ordre**: I **My Trades** trykker du på ordren din og deretter på **AVBRYT**-knappen (kun tilgjengelig før den er tatt).



**Åpne en tvist**: Hvis det oppstår en uenighet, trykker du på **DISPUTE** i bestillingsdetaljene. Legg ved alle bevis (skjermbilder fra chatten, referanser til banktransaksjoner).



## Fordeler og begrensninger



### Fordeler



**Økonomisk suverenitet**: Bitcoinsene dine forlater aldri din direkte kontroll takket være hold-faktura-mekanismen, noe som eliminerer risikoen for børskonkurs eller piratkopiering.



**Motstandsdyktig mot sensur**: Ingen myndighet kan stenge ned nettverket eller sensurere ordrene dine. Systemet fungerer så lenge Nostr-reléene er i drift.



**Standard anonymitet**: Bare en pseudonym Nostr-nøkkel identifiserer deg, uten KYC eller personopplysninger. Ende-til-ende-kryptert kommunikasjon.



**Fleksibilitet i betaling**: Alle gjensidig aksepterte betalingsmetoder er mulige (overføringer, mobilapper, kontanter, byttehandel).



### Begrensninger



**Tidlig utvikling**: Rudimentære grensesnitt og teknisk læringskurve kreves.



**Begrenset likviditet**: Begrenset antall bestillinger, spesielt for store beløp eller sjeldne valutaer.



**Tekniske krav**: Grunnleggende forståelse av Lightning og Nostr kreves.



**Individuelt ansvar**: Ingen sentralisert støtte i tilfelle problemer, forsiktighet kreves.



## Konklusjon



Mostro P2P representerer et lovende alternativ til sentraliserte børser, og kombinerer Lightning Network, Nostr og automatisert escrow for virkelig desentralisert handel. Til tross for den tidlige utviklingen og begrensede likviditeten tilbyr plattformen allerede økonomisk suverenitet, sensurresistens og anonymitet som standard.



For bitcoinere som foretrekker autonomi og konfidensialitet, er Mostro et levedyktig alternativ som er verdt å utforske. Den desentraliserte arkitekturen garanterer fellesskap snarere enn kommersiell utvikling, noe som baner vei for en fremtid med virkelig frie Bitcoin-børser.



## Ressurser



### Offisiell dokumentasjon




- [Mostros offisielle nettside](https://mostro.network)
- [Teknisk dokumentasjon] (https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Kildekode og utvikling




- [GitHubs hovedlager] (https://github.com/MostroP2P/mostro)
- [Nettklient] (https://github.com/MostroP2P/mostro-web)
- [Kunde CLI](https://github.com/MostroP2P/mostro-cli)



### Fellesskapet




- [Nostr-protokollen] (https://nostr.com)
- [Lightning Network Guides](https://lightning.network)