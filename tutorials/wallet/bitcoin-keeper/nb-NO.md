---
name: Bitcoin Keeper
description: Bitcoin mobil wallet for sikkerhet og multi-sig
---

![cover](assets/cover.webp)



Sikker håndtering av bitcoins er en stor utfordring for alle som er bevisste på hva som står på spill når det gjelder økonomisk suverenitet. Det tekniske gapet mellom enkelheten til en mobil wallet og robustheten til en multi-sig-løsning kan virke skremmende for mange brukere. Bitcoin Keeper er posisjonert nettopp i dette skjæringspunktet, og tilbyr en progressiv tilnærming til sikkerhet som følger brukerne etter hvert som de utvikler seg.



Bitcoin Keeper er en mobilapplikasjon med åpen kildekode, utelukkende dedikert til Bitcoin, utviklet av BitHyve-teamet. Ambisjonen er å gjøre avansert porteføljeadministrasjon tilgjengelig, spesielt multisignaturkonfigurasjoner, samtidig som det opprettholdes et intuitivt grensesnitt for nybegynnere. Applikasjonen har slagordet "Secure today, Plan for tomorrow", noe som gjenspeiler filosofien om langsiktig støtte.



I motsetning til generalistiske lommebøker som håndterer flere kryptovalutaer, har Bitcoin Keeper et strengt fokus på Bitcoin. Denne tilnærmingen til kun bitcoin reduserer den potensielle angrepsflaten og forenkler brukeropplevelsen betraktelig. Applikasjonen skiller seg også ut ved å integrere de mest utbredte maskinvarelommebøkene og ha avanserte funksjoner for UTXO-administrasjon.



## Hva er Bitcoin Keeper?



### Filosofi og målsettinger



Bitcoin Keeper ble utviklet for å møte de spesifikke behovene til bitcoinere som ønsker å beholde full kontroll over sine private nøkler. Prosjektet omfavner fullt ut de grunnleggende prinsippene i Bitcoin: åpen og etterprøvbar kildekode, respekt for personvernet og brukersuverenitet. Det kreves ingen registrering eller personlig informasjon for å bruke applikasjonen, og den kan til og med kjøres offline for signeringsoperasjoner.



Det sentrale målet er å tilby et fleksibelt, fremtidsrettet verktøy for lagring av BTC over flere år, og til og med flere generasjoner, takket være arvefunksjonalitet. Applikasjonen gjør det mulig for brukerne å starte med en mobil wallet, og deretter gradvis utvikle seg mot sikrere løsninger med flere signaturer.



### Applikasjonsarkitektur



Bitcoin Keeper organiserer fondsforvaltningen rundt to forskjellige konsepter. **Hot Wallet** er en enkel wallet med én nøkkel som lagres på telefonen, og som er utformet for daglige utgifter og beskjedne beløp. Vaults** er safer med flere signaturer (Multi-Key) som krever flere nøkler for å autorisere en utgift, og som er utformet for sikker langtidslagring.



### Hovedfunksjoner



Bitcoin Keeper støtter nesten alle maskinvarelommebøker på markedet: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport og Coinkites Tapsigner. Integrasjonen skjer via ulike metoder avhengig av enheten: QR-kodeskanning, NFC-tilkobling eller filimport.



Programmet tilbyr også avansert UTXO-administrasjon med transaksjonsmerking, myntkontroll for manuelt valg av inndata ved sending og støtte for PSBT-format for delvis signerte transaksjoner.



## Installasjon og innledende konfigurasjon



Bitcoin Keeper er tilgjengelig gratis på Android via Google Play Store og på iOS via App Store. Utgiveren som er oppført er BitHyve. Før du installerer, må du sørge for at enheten din er fri for skadelig programvare, oppdatert og ikke rotfestet eller jailbreaket.



Ved første oppstart ber programmet deg om å opprette en sikkerhets-PIN-kode. Denne koden beskytter tilgangen til wallet og krypterer sensitive data lokalt. Velg en sterk kode, og lær den utenat. Du kan deretter aktivere biometrisk autentisering (fingeravtrykk eller Face ID) for raskere opplåsing.



![Installation et configuration du PIN](assets/fr/01.webp)



Programmet presenterer deretter flere introduksjonsskjermbilder som forklarer de tre pilarene: Opprettelse av wallet for å sende og motta bitcoins, nøkkeladministrasjon med maskinvare wallet-kompatibilitet, og planlegging av arv for å overføre bitcoins. Trykk på "Kom i gang", og velg deretter "Start ny" for å opprette en ny konfigurasjon.



![Écrans d'introduction](assets/fr/02.webp)



## Oppdage grensesnittet



Bitcoin Keepers grensesnitt er organisert rundt fire hovedfaner som er tilgjengelige fra den nederste navigasjonslinjen:



![Les quatre onglets de l'application](assets/fr/03.webp)



Fanen **Lommebøker** viser lommebøkene dine og saldoen deres. Det er her du får tilgang til lommebøkene dine for å sende og motta bitcoins. Taggene "Hot Wallet" og "Single-Key" eller "Multi-Key" gjør at du raskt kan identifisere typen av hver wallet.



Fanen **Nøkler** sentraliserer administrasjonen av signaturnøklene dine. Her finner du mobilnøkkelen som genereres av applikasjonen, samt alle nøkler som importeres fra maskinvarelommebøker. Det er også her du legger til nye signaturenheter.



Fanen **Concierge** tilbyr støttetjenester: Send inn spørsmål til kundestøtteteamet og kontakt med Bitcoin-rådgivere for personlig hjelp.



Fanen **More** (Flere alternativer) gir tilgang til innstillinger som personlig servertilkobling, sikkerhetskopiering av nøkler, arvedokumenter, skjerminnstillinger og wallet-administrasjon.



## Tilkobling til din egen server



For å styrke konfidensialiteten kan du med Bitcoin Keeper koble applikasjonen til din egen Electrum-server, i stedet for å bruke de offentlige standardserverne.



![Configuration du serveur Electrum](assets/fr/04.webp)



Bla nedover i kategorien Mer for å finne serverinnstillingene. Trykk på "Legg til server" for å konfigurere en ny tilkobling. Du kan velge mellom "Public Server" (forhåndskonfigurerte offentlige servere) og "Private Electrum" (din egen server).



For en privat server angir du URL-adressen (f.eks. umbrel.local for en Umbrel-node) og portnummeret (vanligvis 50001). Aktiver SSL hvis serveren din støtter det. Du kan også skanne en QR-kode for konfigurasjon. Når du har angitt parameterne, trykker du på "Koble til server".



Hvis du ennå ikke har din egen Bitcoin-knute, kan du ta en titt på veiledningen vår om Umbrel, en enkel og rimelig måte å spinne din egen knute på:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Motta bitcoins



Fra Wallets-fanen velger du wallet som du ønsker å motta penger fra ved å trykke på den. wallet-skjermen viser saldoen og tre handlingsknapper: Send Bitcoin, Motta Bitcoin og Vis alle mynter.



![Réception de bitcoins](assets/fr/05.webp)



Trykk på "Mottak Bitcoin". Bitcoin Keeper genererer en ny mottaksadresse i Bech32-format (begynner med bc1...), sammen med QR-koden. Du kan legge til en etikett på denne adressen for å identifisere kilden til midlene. Del adressen med avsenderen ved å vise QR-koden eller kopiere tekstadressen.



Programmet genererer automatisk en ny adresse for hvert mottak, slik at personvernet ditt blir ivaretatt. Bruk "Get New Address" for å få en tom adresse om nødvendig.



## UTXO-ledelse



Bitcoin Keeper gir full oversikt over UTXO (ubrukte transaksjonsutganger) som utgjør saldoen din. Fra en wallet-skjerm trykker du på "Vis alle mynter" for å få tilgang til hjørneadministratoren.



![Gestion des UTXO](assets/fr/06.webp)



Skjermbildet "Administrer mynter" viser hver UTXO enkeltvis med beløp og etikett. I denne visningen kan du spore opprinnelsen til myntene dine og organisere dem. Du kan velge bestemte UTXO-er via "Select to Send" for å sende med myntkontroll, slik at du unngår å blande mynter fra ulike opprinnelser.



## Send bitcoins



For å sende velger du kildeporteføljen og trykker på "Send Bitcoin". Skriv inn destinasjonsadressen (limt inn eller skannet via QR-kode), og legg eventuelt til en etikett for å identifisere mottakeren.



![Envoi de bitcoins](assets/fr/07.webp)



På neste skjermbilde kan du angi beløpet som skal sendes. Grensesnittet viser din tilgjengelige saldo og omregningen til fiat-valuta. Velg ladeprioritet: Lav (økonomi, ~60 minutter), Middels eller Høy (prioritet). Estimerte kostnader i sats/vbyte vises i sanntid. Trykk på "Send" for å fortsette.



![Confirmation et envoi](assets/fr/08.webp)



En oppsummeringsskjerm viser alle detaljene: wallet-kilde, destinasjonsadresse, transaksjonsprioritet, nettverksavgifter, sendt beløp og totalbeløp. Kontroller denne informasjonen nøye, ettersom Bitcoin-transaksjoner er irreversible. Trykk på "Bekreft og send" for å sende transaksjonen.



En bekreftelse med "Send vellykket" vises sammen med en fullstendig oppsummering. Transaksjonen er synlig i historikken "Nylige transaksjoner" med sin egen etikett.



## Lagre nøklene dine



Sikkerhetskopiering av gjenopprettingsnøkkelen er et viktig trinn. Gå til "Sikkerhetskopiering og gjenoppretting" under fanen Mer, og klikk på "Gjenopprettingsnøkkel".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Skjermbildet viser status for sikkerhetskopiene dine. For å bekrefte sikkerhetskopien ber programmet deg om å bekrefte et bestemt ord i frasen din (f.eks. det syvende ordet). Denne bekreftelsen sikrer at du har skrevet ned gjenopprettingsfrasen på riktig måte.



Fra "Innstillinger for gjenopprettingsnøkkel" kan du se hele frasen din via "Vis gjenopprettingsnøkkel" og se signeringsfingeravtrykket til nøkkelen din. Oppbevar 12-ordsfrasen på papir på et trygt sted, beskyttet mot fuktighet og brann. Oppbevar den aldri på en tilkoblet enhet.



## Legg til en ekstern nøkkel (wallet-maskinvare)



En av Bitcoin Keepers største fordeler er integreringen av maskinvarelommebøker. Trykk på "Legg til nøkkel" i fanen Nøkler for å legge til en ny signaturenhet.



![Ajout d'une clé hardware](assets/fr/10.webp)



Velg "Legg til nøkkel fra en maskinvare" for å koble til en wallet-maskinvare. Programmet støtter et bredt spekter av enheter: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner og Specter Solutions.



### Tapsigner-konfigurasjon



Tapsigner er et NFC-kort fra Coinkite som er spesielt egnet for mobil bruk. Hvis du vil lære mer, har vi en egen veiledning :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

For å legge til Tapsigner velger du den fra listen over maskinvarelommebøker.



![Configuration du Tapsigner](assets/fr/11.webp)



Tast først inn den 6-32-sifrede PIN-koden som er trykt på baksiden av kortet (standard på nye kort), eller PIN-koden din hvis den allerede er konfigurert. Trykk på "Fortsett", og før deretter Tapsigner nær baksiden av telefonen når "Klar til å skanne" vises. NFC-kommunikasjon importerer automatisk den offentlige nøkkelen. Du kan deretter legge til en beskrivelse (f.eks. "Métro Card") for å identifisere denne nøkkelen.



## Opprett en multisig-portefølje



Når du har konfigurert nøklene dine, kan du opprette en wallet med flere signaturer som kombinerer flere enheter. Klikk på "Legg til Wallet" i Wallets-fanen.



![Création d'un nouveau wallet](assets/fr/12.webp)



Du har tre alternativer: "Opprett Wallet" for en ny portefølje, "Importer Wallet" for å gjenopprette en eksisterende wallet, eller "Samarbeid Wallet" for et delt hvelv. Velg "Opprett Wallet" og deretter "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Det neste skjermbildet tilbyr ulike konfigurasjoner: "Enkelttast", "2 av 3 multitaster" eller "3 av 5 multitaster". For en tilpasset multi-sig trykker du på "Velg tilpasset oppsett". Velg for eksempel "1 av 2": Det kreves én signatur fra to mulige taster.



Velg deretter nøklene som skal utgjøre ditt Vault. I vårt eksempel kombinerer vi "Mobile Key" (telefonens programvarenøkkel) med "TAPSIGNER" (Metro Card). Denne konfigurasjonen gir redundans: Hvis en av nøklene blir utilgjengelig, kan du alltid bruke pengene dine med den andre.



![Finalisation du wallet multisig](assets/fr/14.webp)



Gi wallet et navn (f.eks. "TestplanB"), legg til en valgfri beskrivelse, og kryss av for de valgte tastene. Trykk på "Opprett din Wallet". En bekreftelsesmelding "Wallet opprettet vellykket" vises, og minner deg på å lagre gjenopprettingsfilen for wallet.



Din nye multisig wallet vises nå i Wallets-fanen med taggen "Multi-key" og indikasjonen "1 av 2".



### Lagre konfigurasjonsfil



**I motsetning til en enkel wallet, der gjenopprettingsfrasen er nok til å gjenopprette tilgangen, krever en wallet multisig også konfigurasjonsfilen som beskriver strukturen til safen (hvilke nøkler som deltar, hvor mange signaturer som kreves). Uten denne filen, selv med alle gjenopprettingsfraser, vil du ikke kunne gjenoppbygge din wallet.



![Export du fichier de configuration](assets/fr/15.webp)



For å eksportere denne filen velger du wallet multisig i Wallets-fanen, og trykker deretter på innstillingsikonet (tannhjulet) øverst i høyre hjørne. I "Wallet-innstillinger" klikker du på "Wallet-konfigurasjonsfil". Flere eksportalternativer er tilgjengelige:





- Eksporter PDF**: genererer et PDF-dokument som inneholder all wallet-informasjon
- Vis QR**: viser en skannbar QR-kode for import av konfigurasjonen til en annen enhet
- Airdrop / File Export**: eksporterer filen via telefonens delingsalternativer
- NFC**: del via NFC med en kompatibel enhet



Oppbevar denne konfigurasjonsfilen separat fra gjenopprettingsfrasene dine, helst på et kryptert eller utskrevet medium. Hvis du mister telefonen, vil denne filen sammen med gjenopprettingsfrasene for hver deltakende nøkkel gjøre det mulig for deg å gjenoppbygge wallet multisig på Bitcoin Keeper eller annen kompatibel programvare.



## Beste praksis



### Organisering av fondet



Strukturer bitcoinsene dine i henhold til hva de skal brukes til: en varm wallet Single-Key for løpende utgifter med begrensede beløp, og en eller flere Vaults Multi-Key for langsiktig sparing. Systematisk UTXO-merking hjelper deg med å holde oversikt over hvor pengene dine kommer fra, noe som er spesielt nyttig for å håndtere konfidensialitet og unngå å blande mynter av ulik opprinnelse.



Hold telefonen sikker: Aktiver den biometriske låsen, utfør systemoppdateringer regelmessig, og vær på vakt når det gjelder installerte programmer. Og hold Bitcoin Keeper oppdatert med sikkerhetsoppdateringer.



### Sikkerhetskopiering



Oppbevar minst to eksemplarer av hver gjenopprettingsfrase på papir, lagret på geografisk adskilte steder. For store summer kan du vurdere gravert, katastrofesikkert metall. Oppbevar aldri disse setningene på en enhet som er koblet til Internett, og fotografer dem aldri.



For multi-sig-hvelv må du også lagre konfigurasjonsfilen (Wallet Recovery File), som inneholder de deltakende offentlige nøklene og hvelvstrukturen. Denne filen, kombinert med nøkkelgjenopprettingsfraser, gjør det mulig å gjenoppbygge wallet på en hvilken som helst kompatibel programvare, for eksempel Sparrow eller Specter.



## Fordeler og begrensninger



### Høydepunkter





- Bitcoin-applikasjonen reduserer kompleksitet og risiko
- Integrert integrering av multisig Vaults med trinnvis veiledning
- Utvidet støtte for maskinvare wallet (Tapsigner, Coldcard, Ledger, Jade osv.)
- Avansert styring av UTXO og myntkontroll
- Kan kobles til en personlig Electrum-server
- Åpen, reviderbar kildekode



### Begrensninger å ta hensyn til





- Interface hovedsakelig på engelsk
- Noen premiumfunksjoner (Cloud Backup, Assisted Server) krever en oppgradering
- Multisig-konfigurasjon krever innledende opplæring



## Konklusjon



Bitcoin Keeper skiller seg ut som en skalerbar løsning for håndtering av bitcoins. Den progressive tilnærmingen, fra den enkle hot wallet til Vaults med flere signaturer, betyr at sikkerheten kan oppgraderes etter hvert som behovene endres. Muligheten til å enkelt integrere maskinvarelommebøker som Tapsigner baner vei for robuste konfigurasjoner uten overdreven kompleksitet.



Den rene bitcoin-orienteringen, den åpne kildekoden og respekten for personvern gjør det til et valg som er i tråd med kjerneverdiene i Bitcoin-økosystemet.



Denne veiledningen dekker de viktigste funksjonene i gratisversjonen av Bitcoin Keeper. Programmet tilbyr også premiumfunksjoner (Cloud Backup, Assisted Server Backup, Canary Wallets) som vil bli gjenstand for en egen veiledning. I en kommende veiledning vil vi også utforske funksjonen Arveplanlegging, som gjør det mulig for deg å forberede overføringen av bitcoins til dine nærmeste, takket være de forbedrede hvelvene og tilhørende dokumenter som er integrert i applikasjonen.



## Ressurser





- Offisiell nettside: [bitcoinkeeper.app] (https://bitcoinkeeper.app)
- Hjelpesenter: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Kildekode: [github.com/bithyve/bitcoin-keeper] (https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper] (https://t.me/BitcoinKeeper)
- Twitter / X: [@bitcoinkeeper_] (https://x.com/bitcoinkeeper_)