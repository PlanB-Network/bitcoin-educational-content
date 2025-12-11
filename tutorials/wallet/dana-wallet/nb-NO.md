---
name: Dana Wallet
description: Minimalistisk portefølje for stille betalinger (BIP-352)
---

![cover](assets/cover.webp)



Gjenbruk av Bitcoin-adresser er en av de mest direkte truslene mot brukernes konfidensialitet. Når en mottaker deler en enkelt adresse for å motta flere betalinger, kan enhver observatør spore alle tilknyttede transaksjoner og rekonstruere deres økonomiske historie. Dette problemet rammer særlig innholdsskapere, veldedige organisasjoner og aktivister som ønsker å offentliggjøre en donasjonsadresse uten at det går på bekostning av personvernet til giverne eller dem selv.



Dana Wallet svarer på dette problemet med en elegant løsning: Silent Payments. Denne minimalistiske wallet med åpen kildekode, som ble lansert i 2024, genererer en gjenbrukbar statisk adresse samtidig som den garanterer at hver mottatte betaling havner på en egen adresse i blokkjeden. Avsenderen trenger ingen forutgående interaksjon med mottakeren, og ingen eksterne observatører kan koble individuelle transaksjoner sammen. På blokkjeden ser disse betalingene ut som helt vanlige Taproot-transaksjoner.



Dana Wallet er tilgjengelig på Mainnet og Signet, men utviklerne anser det fortsatt som eksperimentelt og anbefaler ikke å sette inn penger du ikke er forberedt på å tape. I denne opplæringen bruker vi Signet-versjonen for å oppdage Silent Payments uten å risikere noen reelle midler.



## Hva er Dana Wallet?



### Filosofi og målsettinger



Dana Wallet har en "SP-først"-tilnærming: wallet genererer utelukkende Silent Payments-adresser, og godtar kun denne typen betaling. Du vil ikke kunne opprette en klassisk Bitcoin-adresse (eldre, SegWit- eller Taproot-standard) med dette programmet. Denne bevisste begrensningen gjør at du kan konsentrere deg fullt og helt om å lære deg BIP-352-protokollen uten å bli distrahert av andre funksjoner. Det oversiktlige grensesnittet er bevisst valgt for å gjøre det enklere å bruke enn å ha en overflod av alternativer, noe som gjør verktøyet tilgjengelig selv for brukere som ikke er kjent med on-chain-konfidensialitet.



Prosjektet er utviklet med åpen kildekode, med Flutter for mobilgrensesnittet og Rust for den interne kryptografiske logikken. Denne arkitekturen kombinerer en flytende brukeropplevelse med optimal ytelse for intensive skanneoperasjoner.



### Hvordan fungerer Silent Payments?



Stille betalinger (BIP-352) er basert på en sofistikert kryptografisk mekanisme som bruker Elliptic Curve Diffie-Hellman-nøkkelen Exchange (ECDH). Mottakeren genererer en statisk adresse (som starter med `sp1...` på mainnet eller `tsp1...` på Signet) som består av to forskjellige offentlige nøkler: en skanne-nøkkel ($B_{scan}$) for å oppdage innkommende betalinger, og en utgiftsnøkkel ($B_{spend}$) for å bruke mottatte midler. Denne separasjonen gjør det mulig å beholde utgiftsnøkkelen på wallet-maskinvaren, mens skannøkkelen brukes på en tilkoblet enhet.



Når en avsender ønsker å foreta en betaling, kombinerer wallet summen av de private inngangsnøklene med mottakerens offentlige skannøkkel for å beregne en delt ECDH-hemmelighet. Denne hemmeligheten genererer en kryptografisk "tweak" som, lagt til mottakerens utgiftsnøkkel, skaper en unik Taproot-adresse for den aktuelle transaksjonen.



Mottakeren kan reprodusere denne beregningen ved hjelp av sin private skannøkkel og de offentlige nøklene som er synlige i transaksjonen (Diffie-Hellman matematisk egenskap). Dermed kan han oppdage og bruke pengene uten noen forutgående interaksjon med avsenderen.



Denne tilnærmingen har flere fordeler:




- Mottakerkonfidensialitet**: hver betaling ender opp på en annen adresse
- Avsenderkonfidensialitet**: ingen vedvarende identifikator som knytter betalinger sammen
- Ingen tredjepartsserver**: protokollen fungerer autonomt
- Transaksjoner som ikke kan skilles fra hverandre**: Stille betalinger ser ut som vanlige Taproot-transaksjoner



Den største ulempen er kostnaden ved skanning: Mottakeren må analysere hver nye Taproot-transaksjon for å oppdage dem som er ment for ham.



Hvis du vil lære mer om den tekniske driften av Silent Payments, anbefaler vi BTC204-kurset om konfidensialitet i Bitcoin, som inneholder et eget kapittel om Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Støttede plattformer



Dana Wallet er tilgjengelig som en Android-applikasjon. APK-en kan lastes ned via det dedikerte F-Droid-depotet som tilbys av utviklerne, via Obtainium eller direkte fra GitHub. For Linux-brukere er det teknisk mulig å kompilere Flutter-applikasjonen for skrivebordet.



Appen er ikke tilgjengelig på iOS eller via de offisielle butikkene (Google Play, App Store), noe som gjenspeiler dens eksperimentelle status og fokus på et teknisk publikum.



## Installasjon



### Viktige forutsetninger



For å installere Dana Wallet på Android trenger du en Android-enhet med alternativet "Ukjente kilder" aktivert i sikkerhetsinnstillingene. Det kreves ingen konto eller registrering.



### Legg til F-Cold depositum



Den anbefalte metoden er å legge til Dana Wallets dedikerte F-Droid repository. Gå til `fdroid.silentpayments.dev` hvor du finner linken til depotet og en QR-kode du kan skanne. Depotet tilbyr for øyeblikket 3 applikasjoner: Mainnet-versjonen, Development og Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Installasjon via F-Droid



Åpne F-Droid-applikasjonen på Android-enheten din, og gå deretter til Innstillinger via ikonet nederst til høyre. Velg "Repositories" for å administrere appkilder. Trykk på "+" -knappen for å legge til et nytt depot, og skann deretter QR-koden eller lim inn lenken `https://fdroid.silentpayments.dev/fdroid/repo`. Når depotet er lagt til, ser du de tre versjonene av Dana Wallet som er tilgjengelige. Velg "Dana Wallet - Bookmark" og trykk på "Install".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Opprinnelig konfigurasjon



### Opprettelse av portefølje



Ved første lansering viser Dana Wallet en velkomstskjerm som introduserer oppdraget: "Send og motta donasjoner uten mellommenn". Trykk på "Start" for å fortsette. På neste skjermbilde presenteres applikasjonens tre hovedfordeler:




- Enkel donasjon**: Begynn å motta donasjoner på få sekunder
- Personvern som standard**: ingen behov for servere eller kompleks infrastruktur
- E-postlignende opplevelse**: send og motta bitcoins like enkelt som en e-post



Du kan velge mellom "Gjenopprett" for å gjenopprette en eksisterende portefølje eller "Opprett ny wallet" for å opprette en ny. Trykk på "Opprett ny wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Programmet genererer deretter en gjenopprettingsfrase, som du bør notere nøye ned på et fysisk medium. Selv for testmidler uten reell verdi bør du ta i bruk gode rutiner for sikkerhetskopiering.



### Interface og parametere



Når porteføljen er opprettet, kommer du til hovedgrensesnittet, som er delt inn i to faner: "Transact" og "Innstillinger".



Fanen **Transact** viser bitcoin-saldoen din (og omregningen til dollar), en liste over nylige transaksjoner og to handlingsknapper: "Betal" for å sende penger, og en mottaksknapp (nedlastingsikon).



Fanen **Innstillinger** tilbyr fire alternativer:




- Vis seed-frase**: viser gjenopprettingsfrasen din for sikker oppbevaring
- Endre fiat-valuta**: endre visningsvaluta (USD som standard)
- Angi backend-URL**: konfigurer Blindbit-serverens URL (se neste avsnitt)
- Wipe wallet**: tørker wallet helt fra enheten



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit-serveren



Dana Wallet bruker en indekseringsserver som heter **Blindbit** for å oppdage dine Stille betalinger. Det er viktig å forstå hvordan den fungerer for å kunne evaluere programmets tillitsmodell.



**Hvorfor trenger vi en server?



For å oppdage en Silent Payment må wallet teoretisk sett skanne alle Taproot-transaksjoner i hver blokk og utføre en kryptografisk beregning (ECDH) for hver enkelt. På en mobiltelefon vil denne operasjonen være for beregnings- og båndbreddeintensiv.



Blindbit-serveren løser dette problemet ved å forhåndsberegne mellomliggende data (kalt "tweaks") for alle Taproot-transaksjoner. wallet laster deretter ned disse tweaks (33 byte per transaksjon) og utfører den endelige beregningen **lokalt** for å sjekke om en betaling tilhører deg.



**Beholdt konfidensialitet**



I motsetning til en vanlig Electrum-server der du avslører adressene dine, vet ikke Blindbit-serveren hvilke betalinger som tilhører deg. Den gir de samme dataene til alle brukere, og det er telefonen din som utfører den endelige verifiseringen. Konfidensialiteten din blir derfor bevart overfor serveren.



**Standardserver



Dana Wallet bruker den offentlige serveren `silentpayments.dev/blindbit/signet` (for Signet) eller `silentpayments.dev/blindbit/mainnet` (for Mainnet). Du kan endre denne URL-en i innstillingene hvis du er vert for din egen server.



**Host din egen Blindbit-server**



For brukere som ønsker total suverenitet, er det mulig å være vert for sin egen Blindbit Oracle-server. Dette krever :




- En komplett Bitcoin Core-node **ikke-aglet** (ikke-pruned)
- Installere Blindbit Oracle (tilgjengelig på GitHub: `setavenger/blindbit-oracle`)
- Ca. 10 GB ekstra diskplass
- Tekniske ferdigheter (Go-kompilering, serverkonfigurasjon)



Det finnes ennå ikke noe ferdigpakket program for Umbrel eller Start9. Installasjonen forblir manuell inntil videre. Dette er et felt i aktiv utvikling, og det kan dukke opp mer tilgjengelige løsninger i fremtiden.



## Daglig bruk



### Mottak av midler



For å motta bitcoins trykker du på mottaksknappen (nedlastingsikonet) fra hovedskjermen. Dana Wallet viser deretter din komplette Silent Payment-adresse i formatet `tsp1q...` på bokmerket. Grensesnittet tilbyr flere alternativer:




- Vis QR-kode**: viser QR-koden til adressen din for enkel skanning
- Del**: Del adressen via telefonens applikasjoner
- Copy**: kopierer adressen til utklippstavlen



Som vist på skjermen kan du dele denne adressen offentlig på sosiale nettverk uten at det går på bekostning av personvernet ditt.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



For å få dine første testmidler på Signet, bruk den dedikerte Silent Payments-kranen som er tilgjengelig på `silentpayments.dev/faucet/signet`. Kopier adressen din `tsp1...`, lim den inn i feltet på kranen, og valider deretter forespørselen. Vent til en blokk blir utvunnet (ca. 10 minutter på Signet).



### Send en betaling



For å sende penger trykker du på "Betal"-knappen fra hovedskjermbildet. Skjermbildet "Velg mottaker(e)" vises med tre alternativer for å angi mottaker:




- Legg inn betalingsinformasjon manuelt
- Lim inn fra utklippstavlen**: lim inn en adresse fra utklippstavlen
- Skann QR-kode**: skann en QR-kode som inneholder adressen



Når mottakerens adresse er validert, kan du i skjermbildet "Angi beløp" angi beløpet som skal sendes i satoshier. Din tilgjengelige saldo vises som referanse. Trykk på "Fortsett til gebyrvalg" for å fortsette.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Det neste skjermbildet viser tre avgiftsnivåer, avhengig av hvor mye det haster:




- Rask** (10-30 minutter): høyere gebyrer for rask bekreftelse
- Normal** (30-60 minutter): moderate kostnader
- Langsom** (1+ time): Minimumsgebyr for ikke-presserende transaksjoner



Etter at du har valgt gebyrnivå, oppsummerer bekreftelsesskjermen "Klar til å sende?" alle detaljene: destinasjonsadresse, beløp, estimert tid og transaksjonsgebyr. Sjekk denne informasjonen nøye, og trykk deretter på "Send" for å sende transaksjonen.



Når transaksjonen er sendt, vises den i historikken din med statusen "Ubekreftet" inntil den blir inkludert i en sperre. Saldoen din oppdateres tilsvarende.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Fordeler og begrensninger



### Høydepunkter





- Pedagogisk**: forenklet grensesnitt med fokus på læring Stille betalinger
- Toveis**: støtter både sending og mottak, i motsetning til andre porteføljer
- Åpen kildekode**: fullstendig reviderbar kode på GitHub
- Dedikert Faucet**: gjør det enklere å skaffe testfinansiering
- Uten konto**: ingen registrering eller personopplysninger kreves



### Begrensninger å ta hensyn til





- Eksperimentell**: urevidert programvare, bruk med forsiktighet på Mainnet
- Begrenset plattform**: hovedsakelig Android, ingen iOS-versjon
- Redusert funksjonalitet**: ingen myntkontroll, ingen underkontoer, ingen Lightning
- Intensiv skanning**: betalingsoppdagelse krever betydelige ressurser



## Beste praksis



### seed sikkerhet



Selv for Signet-tester med verdiløs bakgrunn må du ta gjenopprettingsfrasen din på alvor. Bruk alternativet "Vis seed-frase" i innstillingene for å skrive den ned nøye. Som en god praksis bør du ha helt separate lommebøker for Signet og Mainnet: Bruk aldri en seed som er opprettet for testing på en wallet som er ment å motta ekte midler.



### Advarsel om eksperimentell status



Dana Wallet anses fortsatt som eksperimentell av utviklerne. Som de tydelig sier: "Ikke bruk midler du ikke er villig til å tape". For læringsformål bør du velge Signet-versjonen. Hvis du bruker Mainnet-versjonen, bør du begrense deg til token-beløp.



### Sikkerhetskopiering og gjenoppretting



Gjenoppretting av Silent Payments-midler krever en wallet som er kompatibel med BIP-352-protokollen. En standard wallet kan ikke skanne blokkjeden for å hente dine UTXO Silent Payments. Behold Dana Wallet installert, eller bruk alternativet "Gjenopprett" ved første lansering for å gjenopprette en eksisterende wallet.



## Sammenligning med BIP-47 og PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Silent Payments eliminerer BIP-47-varslingstransaksjonen på bekostning av en dyrere skanning. PayJoin løser et annet problem (inputkorrelasjon) og kan kombineres med Silent Payments.



## Konklusjon



Dana Wallet er et verdifullt pedagogisk verktøy for å lære om Silent Payments i et risikofritt miljø. Den minimalistiske tilnærmingen gjør at du kan forstå de grunnleggende mekanismene i BIP-352-protokollen uten å bli distrahert av sekundære funksjoner. Ved å eksperimentere med Signet får du en praktisk forståelse av denne lovende teknologien for konfidensielle Bitcoin-transaksjoner.



Silent Payments representerer et betydelig skritt fremover i å forene brukervennlighet og respekt for personvernet. Entusiasmen i samfunnet og de første integrasjonene i forskjellige lommebøker (Cake Wallet, BitBox02, BlueWallet for sending) peker mot en fremtid der publisering av en donasjonsadresse ikke lenger vil gå på bekostning av eierens økonomiske personvern.



## Ressurser



### Offisiell dokumentasjon




- Dana Wallet GitHub-arkiv: https://github.com/cygnet3/danawallet
- F-Cold depositum: https://fdroid.silentpayments.dev
- Felles nettsted for Silent Payments: https://silentpayments.xyz
- Spesifikasjon BIP-352: https://bips.dev/352



### Signet testverktøy




- Faucet Stille betalinger: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit-server (selvbetjent)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle