---
name: BitBanana
description: Mobil manager for Lightning-noden din
---

![cover](assets/cover.webp)



I denne opplæringen lærer du hvordan du installerer og konfigurerer BitBanana på Android for å kontrollere Lightning-noden din fra smarttelefonen din. Vi ser hvordan du kobler appen til din eksisterende infrastruktur (Umbrel, RaspiBlitz, myNode eller en hvilken som helst LND/Core Lightning-node), foretar Lightning-betalinger, fjernadministrerer kanalene dine, ser rutinginntektene dine og tar sikkerhetskopi av konfigurasjonene dine. Du vil også lære om de beste sikkerhetsrutinene for å beskytte tilgangen til noden din, og hvordan den kan sammenlignes med Zeus, et populært alternativ.



## Vi introduserer BitBanana



BitBanana er en Android-mobilapplikasjon med åpen kildekode som gjør smarttelefonen din om til et komplett dashbord for fjernstyring av Lightning-noden din. I motsetning til Lightning-lommebøker, som har en lokal node på telefonen, har BitBanana en 100 % fjernstyringsfilosofi: appen har ingen satoshi og kobler seg bare til din eksisterende infrastruktur.



Programmet er utviklet av Michael Wünsch under MIT-lisens, og garanterer total åpenhet med null innsamling av personopplysninger og verifiserte reproduserbare builds. BitBanana støtter LND og Core Lightning via standard URI-er (`lndconnect://` og `clngrpc://`), noe som drastisk forenkler den innledende konfigurasjonen. Programmet gjenkjenner også LndHub og Nostr Wallet Connect for brukere uten en personlig node, selv om disse modusene fungerer med begrenset funksjonalitet.



Grensesnittet gir full tilgang til alle nodens kritiske funksjoner: sending og mottak av betalinger (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), administrasjon av Lightning-kanaler (åpning, lukking, gebyrjustering, rebalansering), avansert myntkontroll og administrasjon av vakttårn. BitBanana implementerer også flere robuste sikkerhetslag: biometrisk låsing, stealth-modus, nød-PIN-kode og innebygd Tor-støtte for å anonymisere tilkoblinger.



## Støttede plattformer og installasjon



### Installasjon



BitBanana er eksklusivt tilgjengelig for Android 8.0 eller nyere. Applikasjonen finnes ikke på iOS, og ingen versjon er planlagt. Denne begrensningen forklares av prosjektets historie: BitBanana er den direkte etterfølgeren til Zap Android, opprinnelig utviklet av Michael Wünsch, som bestemte seg for å fortsette sitt arbeid under sitt eget merke. Zap var en familie av separate applikasjoner (Zap Android, Zap iOS, Zap Desktop) utviklet av forskjellige bidragsytere med separate kodebaser. BitBanana forfølger bare Android-grenen.



I tillegg byr iOS-økosystemet på betydelige regulatoriske og tekniske begrensninger for Lightning-applikasjoner som ikke er frihetsberøvende. I 2023 avviste Apple en Zeus-oppdatering på grunn av "lisensbrudd", og i 2024 forlot Phoenix Wallet den amerikanske App Store på grunn av usikkerhet rundt regelverket for leverandører av Lightning-tjenester. Disse hindringene forklarer hvorfor mange Lightning-utviklere foretrekker Android, som tilbyr en mer åpen policy for ikke-frihetsberøvende applikasjoner.



Tre installasjonsmetoder er tilgjengelige for Android: Google Play Store (mer enn 5000 installasjoner, automatiske oppdateringer), F-Droid (reproduserbare builds, verifisering av kildekode) eller manuell APK fra GitHub.



![BitBanana](assets/fr/01.webp)



Den offisielle nettsiden bitbanana.app (til venstre) skryter av "100 % selvforvaltende med NULL datainnsamling". Den sentrale skjermen viser de tre nedlastingsalternativene: F-Droid (anbefalt), Google Play og APK. Skjermbildet til høyre viser varslingstillatelsen for betalingsvarsler.



Programmet ber om tillatelser: nettverk (node-tilkobling), kamera (QR-koder), NFC (LNURL), bakgrunnstjenester (varsler), biometri (sikkerhet) og WireGuard VPN. Ingen sporere, null datainnsamling. Aktiver passord eller biometrisk låsing for å sikre tilgang.



## Opprinnelig konfigurasjon



### Koble til en LND-node



For å koble BitBanana til LND-noden din (Umbrel, RaspiBlitz, myNode), skaff deg en `lndconnect`-URI eller QR-kode som inneholder adressen, TLS-sertifikatet og autentiseringsmakronen.



I denne veiledningen bruker vi en LND-node via umbrel. For mer informasjon, se vår dedikerte veiledning :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Åpne menyen øverst til høyre i Lightning Node-applikasjonen, og velg "Connect wallet".



![BitBanana](assets/fr/04.webp)



Velg **gRPC (Tor)** for å koble til via Tor (anbefalt). QR-koden og detaljer (Host .onion, Port 10009, Macaroon) vises.



![BitBanana](assets/fr/02.webp)



I BitBanana trykker du på "CONNECT NODE", skanner QR-koden eller limer inn URI-en. Godkjenn kameratilgang, og kontroller deretter .onion-adressen som vises før du bekrefter.



**Core Lightning**-tilkobling



Hvis du bruker Core Lightning (CLN) i stedet for LND, forblir prosessen identisk, med URI-en `clngrpc://` som inneholder de gjensidige TLS-sertifikatene. Core Lightning støtter BOLT12 (tilbud), noe som muliggjør gjenbrukbare fakturaer og gjentatte betalinger som ikke er tilgjengelig på LND.



**Tilkobling uten personlig node (LNbits/hosted)**



Hvis du ikke har en Lightning-node, kan BitBanana koble seg til hostede tjenester via LndHub (protokollen som brukes av BlueWallet og LNbits) eller Nostr Wallet Connect (NWC). Vær oppmerksom på at disse modusene fungerer i depotmodus (tjenesten er vert for midlene dine) med begrenset funksjonalitet. Du kan ikke administrere kanaler eller konfigurere rutingavgifter, og du kan bare sende og motta lynbetalinger.



For mer informasjon om LNbits eller Nostr Wallet Connect, se våre ulike veiledninger:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Daglig bruk



### Interface hoved



Startskjermbildet viser Lightning-saldoen din, og menyen øverst til venstre gir tilgang til følgende seksjoner: Kanaler, Routing, Signering/Verifisering, Noder, Kontakter, Innstillinger, Sikkerhetskopiering. Klokkeikonet (øverst til høyre) åpner transaksjonshistorikken. Knappene "Send" og "Receive" nederst gir deg mulighet til å sende og motta satoshier.



![BitBanana](assets/fr/05.webp)



### Lyn- og on-chain-betalinger



![BitBanana](assets/fr/10.webp)



**Send en betaling:** Trykk på "Send"-knappen fra startskjermen. Betalingsskjermen (til venstre) gir deg mulighet til å lime inn en adresse eller betalingsdata i feltet "Address eller betalingsdata", med en QR-skanner øverst til høyre for skanning av koder. Du kan også velge en kontakt som er lagret i Kontakter for å unngå å måtte skanne hver gang.



BitBanana gjenkjenner intelligent alle betalingsformater: klassiske Lightning-fakturaer (tegnstrenger som begynner med `lnbc`), Lightning Address (e-postformat som `utilisateur@domaine.com`), LNURL-betalingskoder for dynamiske betalinger, LNURL-withdraw for uttak av midler, og til og med Keysend-betalinger direkte til en Lightning-publikumsnøkkel uten en forutgående faktura. Programmet utfører automatisk de nødvendige LNURL-oppløsningene i bakgrunnen.



Når fakturaen er lastet inn, viser BitBanana alle detaljer: eksakt beløp, estimert rutinggebyr, betalingsbeskrivelse (hvis oppgitt av mottakeren) og fakturaens utløpsdato. Etter bekreftelse dirigeres betalingen via Lightning-kanalene dine. Du kan deretter se ruten som er tatt, steg for steg, og gebyrene som faktisk er betalt, i transaksjonsdetaljene.



**Motta betaling:** Trykk på "Motta"-knappen. En velger (høyre skjerm) lar deg velge mellom Lightning (øyeblikkelig betaling via kanalene dine) og On-Chain. For en Lightning-kvittering skriver du inn ønsket beløp i satoshis (eller lar det stå på 0 for å opprette en faktura uten fast beløp som betaleren skal fylle ut), og legger til en valgfri beskrivelse som skal vises på fakturaen. BitBanana genererer umiddelbart en lynfaktura med QR-kode for skanning. Du kan også kopiere fakturaen som tekst og sende den via e-post. Så snart betalingen er mottatt, får du et push-varsel, og transaksjonen vises umiddelbart i historikken med alle detaljer.



### Kanaler og ruting



![BitBanana](assets/fr/06.webp)



"Kanaler"-delen viser sende-/mottaksfunksjonene dine og lister opp kanalene dine med unike avatarer. Hver kanal viser likviditetsfordelingen mellom lokal og ekstern saldo. Trykk på en kanal for å få fullstendige detaljer og handlinger (stenge, endre rutingavgifter). De tre punktene øverst til høyre gir tilgang til "Rebalance"-alternativet for å rebalansere kanalenes likviditet. "+"-knappen åpner en ny kanal.



Routing-delen (sentralt skjermbilde) viser videresendingsinntekter etter periode (1D, 1W, 1M, 3M, 6M, 1Y) med detaljert videresendingshistorikk for å optimalisere strategien din.



Med Sign/Verify (høyre skjermbilde) kan du kryptografisk signere/verifisere meldinger for å bevise nodekontroll.



### Flere noder og parametere



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: viser nodene dine, med knapper for å legge til manuelt, skanne QR eller veksle mellom noder. Du kan spesielt sette opp forskjellige typer tilkobling til samme node: LAN, VPN eller Tor.



**Administrer kontakter**: lagrer Lightning-kontaktene dine for raske betalinger.



**Innstillinger**: Tilpass valuta, språk, avatarer. Sikkerhets- og personvernseksjonen: App Lock (PIN-kode/biometri), Skjul saldo (stealth-modus), Tor (IP-anonymisering). Konfigurasjon av prisorakler, blokkutforskere, tilpassede avgiftsestimatorer.



## Fordeler og begrensninger



**Høydepunkter:**




- Total mobilitet: styr Lightning-noden din fra hvor som helst
- Full funksjonalitet: betalinger (LNURL, Lightning Address, BOLT 12), kanaladministrasjon, myntkontroll, vakttårn, multi-noder
- Sikkerhet: PIN-kode/biometri, stealth-modus, nød-PIN-kode, innebygd Tor, skjermbildeblokkering
- Gratis, åpen kildekode (MIT), null provisjon, null datainnsamling



**Begrensninger:**




- Krever en aktiv Lightning-node (eller LNbits i depotmodus)
- Ingen iOS-versjon planlagt
- Det er avgjørende å sikre tilgangen til telefonen (macaroon admin = total tilgang til noden)



## Beste praksis



**Sikkerhet:**




- Aktiver PIN-/biometrilås (forhindrer uautorisert tilgang til noden)
- Sett opp en nød-PIN-kode (sletter sensitive data i tilfelle tvang)
- Del aldri innloggings-URI eller makron
- Stealth-modus i fiendtlige miljøer



**Login:**




- VPN-nettverk (Tailscale, ZeroTier): det beste kompromisset mellom hastighet og sikkerhet
- Tor: maksimal konfidensialitet, høyere ventetid
- Clearnet: unngå med mindre det er nødvendig (IP-eksponering, åpne porter)



### Sikkerhetskopiering og gjenoppretting



Til slutt har vi "Backup"-menyen, der du kan lagre konfigurasjonene dine for telefonmigrering eller reinstallasjon.



![BitBanana](assets/fr/08.webp)



**Sikkerhetskopien inneholder IKKE seed- eller kanalsikkerhetskopier (som skal gjøres på noden). Den inneholder: nodekonfigurasjoner (adresser, sertifikater, makroner), etiketter, kontakter, parametere. Gjenopprett-knappen lar deg importere en eksisterende sikkerhetskopi. Bekreftelse kreves før lagring.



![BitBanana](assets/fr/09.webp)



Skriv inn et krypteringspassord (høyre skjermbilde). Systemet åpner filvelgeren (venstre skjermbilde) for å lagre `BitBananaBackup_2025-XX-XX.dat`. Bekreftelse "Sikkerhetskopi opprettet".



**Sikkerhet:** Lagre sikkerhetskopien kryptert (personlig sky, USB, NAS). Del aldri filer eller passord. Test gjenopprettingen regelmessig. Sikkerhetskopien gjenoppretter tilkoblinger, ikke midler.



## BitBanana vs Zeus: Hva er forskjellen?



Hvis du utforsker mobilapper for å administrere en Lightning-node, vil du sannsynligvis støte på Zeus, et populært alternativ til BitBanana. I motsetning til BitBanana, som utelukkende fokuserer på fjernstyring av en eksisterende node, har Zeus en mer omfattende tilnærming og tilbyr to driftsmåter: en Lightning-node innebygd direkte i applikasjonen (innebygd modus med integrert LND) og ekstern tilkobling til en ekstern node, akkurat som BitBanana.



Denne doble funksjonaliteten gjør Zeus spesielt attraktiv for nybegynnere som ønsker å eksperimentere med Lightning uten noen forutgående infrastruktur. Embedded-modus muliggjør umiddelbar oppstart med en komplett mobil node, mens avanserte brukere kan bytte til fjerntilkobling når den personlige noden er konfigurert. Zeus støtter også LND og Core Lightning for ekstern tilkobling, for eksempel BitBanana.



En annen stor fordel med Zeus er tilgjengeligheten på tvers av plattformer (iOS og Android), mens BitBanana forblir utelukkende Android-basert. Zeus har også Olympus LSP-infrastruktur for å legge til rette for mottak av lynbetalinger via just-in-time-kanaler, et Point of Sale-system for forhandlere og integrert swap-funksjonalitet for å administrere likviditet.



BitBanana beholder imidlertid sine spesifikke styrker: et enklere og mer strømlinjeformet grensesnitt, en bedre brukeropplevelse (UX) takket være det eksklusive fokuset på fjernkontroll og en pedagogisk tilnærming med kontekstuelle forklaringer. Zeus tilbyr mer funksjonalitet, men på bekostning av et mer komplekst grensesnitt. Applikasjonen er fortsatt spesielt godt egnet for brukere som ønsker å styre en node utelukkende på avstand, uten vaktmesterfunksjoner.



Hvis du vil vite mer om Zeus, kan du ta en titt på følgende veiledninger:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Konklusjon



BitBanana gjør Android-smarttelefonen din om til et komplett Lightning-dashbord, og tilbyr enestående mobilitet for nodeoperatører. Applikasjonen dekker alle funksjoner: betalinger (alle formater), kanaladministrasjon, myntkontroll, vakttårn, multi-node, med forbedret sikkerhet (PIN/biometri, Tor, Emergency PIN).



BitBanana er helt suverent, og samler ikke inn data og kompromitterer verken konfidensialiteten eller kontrollen over midlene dine. Åpen kildekode (MIT) garanterer åpenhet.



## Ressurser



### Offisiell dokumentasjon




- [BitBananas nettsted](https://bitbanana.app)
- [Fullstendig dokumentasjon](https://docs.bitbanana.app)
- [GitHub-kildekode](https://github.com/michaelWuensch/BitBanana)



### Installasjon




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)