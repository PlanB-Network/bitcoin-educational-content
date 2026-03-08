---
name: Betjent Bitcoin
description: Valet gir deg en Lightning-node som ikke er i lommen din
---

![cover_valet](assets/cover.webp)



## Innledning


Valet er en lett, selvforvaltende, Bitcoin og Lightning wallet som tilbyr en enkel og praktisk oppstartsprosess for nybegynnere. Den er spesielt skreddersydd for å betjene Bitcoin-samfunn og sirkulære økonomier, spesielt i avsidesliggende områder.


Det er en fork av **Simple Bitcoin Wallet (SBW)**, med en avansert Hosted Lightning-kanalfunksjon kalt **Fiat Channels**, designet for å gjøre det mulig for alle å akseptere Lightning-betalinger uten volatilitetsrisiko.


Valet er for øyeblikket kun tilgjengelig for Android-enheter, og kan lastes ned og installeres fra flere appbutikker med åpen kildekode. Valet er imidlertid **ikke** tilgjengelig i **Google Play Store** på grunn av personvernhensyn for utviklere og KYC-bekymringer.



## Last ned og installer Valet


Valet kan lastes ned som en APK-fil fra Standard Sats' GitHub-side. [Standard Sats] (https://standardsats.github.io/) er selskapet som utviklet Valet.


👉 For å laste ned Valet, besøk Standard Sats [GitHub-siden] (https://github.com/standardsats/valet/releases), og finn den **nyeste** versjonen (dette er ofte den øverste).


👉 Gå til **Assets** og klikk på filen med bare en **.apk**-utvidelse. Nedlastingen starter automatisk.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Når nedlastingen er fullført, går du til enhetens **Filbehandling** > **Nedlastinger**, og velger Valet apk-filen.


![Select_valet_apk](assets/en/002.webp)


👉 Installer den, og i løpet av få sekunder vil appen være klar og vises på startskjermen.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternativt kan du også laste ned Valet fra **F-Droid** app store. Hvis du ikke har F-Droid-appen på enheten din, kan du laste den ned og installere den [her] (https://f-droid.org/en/).


👉 Åpne F-Droid på startskjermen og søk etter **Valet**. Velg det første alternativet med et **lilla og hvitt ikon** blant de to alternativene som vises, og klikk på **Last ned**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Etter nedlasting klikker du på **Installer** og følger instruksjonene på skjermen. Når installasjonen er fullført, kan du starte Valet fra F-Droid ved å klikke på **Åpne**, eller starte den fra enhetens startskjerm.



## Opprette en Bitcoin Wallet


Du kan sette opp en Bitcoin wallet på Valet i to enkle trinn.


👉 Start Valet fra enhetens startskjerm eller fra F-Droid-appen. Et wallet-oppsettskjermbilde vises, med to alternativer: **Opprett ny Wallet** og **Gjenopprett eksisterende Wallet**.


👉 Velg **Opprett ny Wallet**, så opprettes det umiddelbart en ny wallet, og du blir omdirigert til startsiden.


![set_up_a\_new_wallet](assets/en/006.webp)



## Sikkerhetskopier frøfrasen din


👉 På startsiden til wallet klikker du på **Green-kortet** som har påskriften **"Trykk for å lagre wallet-gjenopprettingsfrasen i tilfelle du skulle miste eller bytte ut enheten".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Et sett med 12 engelske ord vises. Skriv dem ned på papir, i rekkefølgen 1 til 12, og oppbevar dem trygt.


![the_seed_phrase](assets/en/008.webp)


### Vær oppmerksom ⚠️:


Vær oppmerksom på følgende elementer:


- Som du allerede vet, er Valet en wallet med selvforvaring, så seed-frasen din er den eneste tilgangen til å gjenopprette Wallet.
- Hvis du noen gang mister seed-frasen din, vil du **aldri** få tilgang til wallet.
- Hvis noen får tak i seed-frasen din, kan de ugjenkallelig stjele alle Bitcoin-ene dine.


Du må derfor skrive ned seed-frasen på 12 ord og oppbevare den på et trygt sted. Du bør aldri ta en skjermdump, lagre den som et utkast i e-posten din eller lagre den på en elektronisk enhet som noen gang har vært koblet til internett.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Mottak og sending av Bitcoin på Valet


Valet er en wallet med selvforvaring med både on-chain- og Lightning Bitcoin-kapasitet. Dette betyr at du kan motta og sende Bitcoin ut av Valet enten via en **On-chain** eller via en **Lightning Network**.


For å kunne motta eller sende Bitcoin gjennom Lightning må du imidlertid sette opp en Lightning-kanal ved å bruke on-chain Bitcoin som Liquidity. Eller du kan kjøpe Lightning-kanallikviditet fra leverandører.



## Generering av en Bitcoin Address i kjeden


For å motta Bitcoin gjennom on-chain må du generere en Bitcoin-adresse.


👉 På startsiden til wallet vil du se et **Orange** og et **Lilla kort**, henholdsvis merket **Bitcoin** og **Lightning**.


👉 Klikk på det oransje kortet merket **Bitcoin**. Du blir omdirigert til et skjermbilde som viser en Bitcoin-adresse.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Du kan **kopiere** adressen og sende den til personen som sender Bitcoin til deg, eller klikke på **del**-knappen for å sende QR-koden til personen via sosiale medier eller andre kommunikasjonskanaler.


👉 Du kan også klikke på **Rediger**-knappen for å angi hvor mange Bitcoin-er som skal sendes til den adressen.


**I likhet med en faktura er redigeringsfunksjonen nyttig i scenarier der du kanskje ønsker å motta et bestemt antall Bitcoin til en adresse på et bestemt tidspunkt, men dette betyr ikke at adressen ikke kan motta høyere eller lavere beløp.


👉Klikk på **Flere nye adresser** for å generere nye tilfeldige adresser.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Du kan også generere en on-chain Bitcoin-adresse ved å klikke på **Mottak**-knappen nederst på wallet-hjemmesiden din. Velg deretter **Mottak til bitcoin-adresse**, og fortsett med samme prosess som ovenfor.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Sende Bitcoin via On-chain


Det er en enkel oppgave å sende ut Bitcoin fra Valet wallet via on-chain.


👉 Nederst på startsiden til wallet klikker du på **Send**-knappen, skriver inn Bitcoin-adressen, eller klikker på **Scan** for å skanne QR-koden til adressen, og deretter klikker du på **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Skriv inn Bitcoin-beløpet du vil sende. Du kan manuelt angi et beløp i Sats eller i Fiat-valuta, eller du kan klikke på **Max** for å bruke hele on-chain-saldoen din.


👉 Du kan også justere gebyrene du vil betale for transaksjonen ved å klikke på den lille grønne boksen merket **gebyr** og deretter skyve den hvite prikken til høyre eller venstre for å henholdsvis øke eller redusere gebyrene. Klikk på **Ok** for å sende transaksjonen.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Sette opp en Lightning Network-kanal


Som nevnt ovenfor er Valet en selvforvaltende Bitcoin og Lightning wallet. For å kunne sende og motta Bitcoin gjennom Lightning-nettverket, må du derfor først sette opp en Lightning-kanal ved å følge disse trinnene:


👉 På startskjermen klikker du på det **Lilla kortet** merket **Lightning**. Du kommer til en side med følgende alternativer:



- Skann node QR
- Kjøp på LNBIG.COM
- Kjøp på BITREFILL.COM
- Be om ny synkronisering av LN-grafen.


Når du velger **Kjøp fra lnbig.com** eller **Kjøp fra bitrefill.com**, blir du omdirigert til nettsidene til disse selskapene, der du kan kjøpe en inngående likviditet med flere kapasiteter. Ignorer det siste alternativet **Forespør LN graf resynkronisering** for nå.


Så vårt valg her er å **Scanne en Node QR**. På dette tidspunktet må du ha bestemt deg for og innhentet **QR-koden** til noden du ønsker å åpne en kanal til. Du kan åpne kanaler til hvilken som helst offentlig node du ønsker. Gå til [1ML] (https://1ml.com/) eller [Amboss] (https://amboss.space/), velg en hvilken som helst offentlig node du ønsker, og skann den tilhørende QR-koden til noden du har valgt.


![channel_opening_options](assets/en/016.webp)


👉 Du vil automatisk bli omdirigert til neste side, hvor du nå må finansiere kanalen din. Igjen, selvforvaltende Lightning-nettverksbruk krever at du bruker Bitcoin-ene dine til å finansiere en kanal. Dette betyr at du må ha Bitcoin i din on-chain wallet som du kan finansiere Lightning-kanalen med. Vennligst se denne artikkelen av [Hacken] (https://hacken.io/discover/lightning-network/) for å lese mer om Lightning-nettverket.


![fund_channel](assets/en/017.webp)


👉 Angi **beløpet** du vil finansiere kanalen med, eller klikk på **Max** for å bruke hele on-chain Bitcoin-saldoen din. Du kan justere **gebyret**, eller la standardinnstillingen for gebyret stå, og klikke på **Ok**.


**Beløpet du finansierer kanalen med, vil være kapasiteten til den nye kanalen (dvs. det totale volumet av Sats som kan overføres til og fra den kanalen)


Det er også viktig at du bruker mer enn **100 000 Sats** som finansieringsbeløp når du åpner en kanal. Dette er fordi mange Lightning-noder krever en kapasitet på minst 100 000 Sats for å åpne en kanal til dem. Så for å unngå prøving og feiling, bruk ganske enkelt beløp som er høyere enn dette.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Når du nå sjekker wallet-hjemmesiden din, vil du se at finansieringsbeløpet ditt nå er flyttet fra **Bitcoin-kortet** til **Lightning-kortet**. I transaksjonshistorikken din vil du se at finansieringstransaksjonen blir behandlet.


![channel_funding_processing](assets/en/020.webp)


👉 Hvis du klikker på Lightning-kortet, vil du se informasjon som viser at Lightning-kanalen din er i ferd med å åpne. Du vil også se **finansieringstransaksjonen for kanalen** på listen over transaksjoner. Vent til finansieringstransaksjonen er bekreftet på blockchain, så er Lightning-kanalen din klar.


![channel_opening](assets/en/021.webp)


👉 Så snart finansieringstransaksjonen er bekreftet, klikker du på **Lightning-kortet** på startsiden din, og du vil se informasjonen om Lightning-kanalen din som følger:



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dette er nodenes IP-adresser. (henholdsvis IPV4 og IPV6)
- KAPASITET:** Dette er det totale volumet av Sats som kan sendes og mottas gjennom denne kanalen
- KAN SENDE:** Dette er mengden Sats du kan sende ut på dette tidspunktet. Du vil legge merke til at det er nesten det samme tallet som **Kapasitet**. Dette er fordi du ikke har sendt ut noen betalinger gjennom kanalen.
- KAN MOTTA:** Dette er antallet Sats du kan motta til denne kanalen for øyeblikket. (Det vil være lite eller ingenting på dette tidspunktet fordi du først må sende ut noen Sats for å skape en innkommende Liquidity for at du skal kunne motta)
- REFUNDABLE:** Dette viser beløpet som blir betalt tilbake til on-chain-adressen din når du stenger kanalen din. Dette kalles også **Kanalens lokale saldo**. Legg merke til at det er litt mindre enn kanalkapasiteten, og dette skyldes at når du stenger en kanal, må du betale et gebyr for å publisere den avsluttende transaksjonen på blockchain, akkurat som du gjorde da du finansierte kanalen. Systemet har derfor trukket fra det antatt laveste beløpet du må betale)
- VALUE IN FLIGHT:** Når noen sender sats til kanalen din, eller når du prøver å sende sats til noen, og transaksjonen av en eller annen grunn blir forsinket, vises det ofte i dette feltet.


![channel_info](assets/en/022.webp)


## Sende Sats gjennom kanalen din


Det er enkelt å sende Sats gjennom Lightning Network.


👉 Nederst på hjemmesiden klikker du på **Send**, og **limer inn** lynfakturaen (du må ha kopiert den) i det angitte feltet, eller klikk på **Scan** for å skanne QR-koden for lynfakturaen.


![click_send_or_scan](assets/en/023.webp)


De fleste lynfakturaer kommer med et forhåndsinnlagt beløp som skal betales. Men i noen få tilfeller kan det være en åpen faktura der du selv må fylle inn beløpet.


👉 Skriv inn beløpet i **Dollars** eller **Sats**, eller klikk på **Max** for å bruke hele saldoen på Lynkanalen din, og klikk deretter på **Ok**. Så snart en god bane er funnet, vil betalingen din bli sendt og fullført i løpet av få sekunder. Følg med på startsiden for å se om betalingen er fullført. Den får en grønn hake når den er fullført.


![enter_the_amount](assets/en/024.webp)


## Mottak av Sats gjennom kanalen din


Mottak av betalinger på Lightning-kanalen din er i stor grad avhengig av om du har en inngående Liquid-likviditet eller ikke. Etter at du har åpnet en kanal, vil du ikke kunne motta betalinger før du i det minste har sendt noen Sats for å **skape inngående likviditet** i den andre enden av kanalforbindelsen. For å bekrefte om du kan motta Sats og hvor mye Sats du kan motta, sjekk **Kan motta**-feltet i kanalinformasjonen din. Dette vil vise deg hvor mange Sats du mottar til enhver tid.


La oss anta at du har sendt ut Sats fra kanalen din, og at du nå har innkommende likviditet og kan motta Sats.


For å motta på Lightning-kanalen må du generere en faktura. I motsetning til Bitcoin on-chain, som bruker adresser, bruker Lightning-nettverket fakturaer. Det finnes to måter å generere en faktura på Valet.


#### ALTERNATIV 1


👉 Nederst på startsiden klikker du på **Mottak** og velger **Mottak til lynfaktura**. Fyll ut beløpet som skal mottas i fakturaen, og klikk på **Ok**. Kopier fakturaen eller del QR-koden med betaleren.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### ALTERNATIV 2


👉 Klikk på det lilla Lightning-kortet på startsiden til wallet. Trykk hvor som helst på kanalen din, og en liste med alternativer vil dukke opp. Velg **Mottak til kanal** og angi beløpet du mottar (enten i Sats eller dollar). Du vil også se hvor mange Sats du kan motta (inngående kapasitet) når du fyller ut fakturaen. Klikk på **Ok** og kopier fakturaen eller del QR-koden med betaleren.


![receive_to_channel](assets/en/028.webp)


**Det første alternativet er et universelt alternativ, noe som betyr at hvis du har mer enn én aktiv kanal og du bruker det første alternativet, vil systemet automatisk velge en av kanalene dine for mottak av Sats.


I dette scenariet er det andre alternativet best å bruke hvis du ønsker å motta Sats til en bestemt kanal.


### Forklaring av kanalens popup-alternativer


Når du trykker på kanalen din, vises følgende valgfelt:


![channel_pop_ups](assets/en/029.webp)


**DEL LIGHTNING CHANNEL DETAILS:** Her kan du dele kanaldetaljer, for eksempel ekstern peer-ID, lokal kanal-ID, finansieringstransaksjon, dato for opprettelse osv.


**SLUTT KANAL TIL WALLET:** Du kan stenge lynkanalen din når du vil. For å stenge kanalen sjekker systemet Bitcoin-saldoen du har på din egen side av kanalen (husk **"Kan sende"**-feltet, også kjent som din lokale saldo), og sender den tilbake til deg. I Valet kan du velge hvor du vil at Bitcoin skal sendes når kanalen er stengt. Så **Lukk kanal til wallet** er ett av to alternativer.


👉 Klikk på dette alternativet, og velg **Bitcoin**. Kanalstengingen starter, og saldoen på kanalen Bitcoin sendes tilbake til wallets on-chain-adresse.


![close_channel_to_wallet](assets/en/030.webp)


**SLUTT KANAL TIL ADDRESS:** Dette er det andre alternativet for å stenge en kanal. Når du velger dette alternativet, blir du bedt om å oppgi en wallet-adresse som Bitcoin-saldoen på kanalen din skal sendes til. Vær oppmerksom på at du i dette alternativet bare kan skanne QR-koden til Bitcoin-adressen du vil stenge kanalen til. For øyeblikket er det ikke mulig å lime inn adressen manuelt.


👉 Klikk på dette alternativet, skann Bitcoin-adressen, og klikk på **Ok**. Kanalstengingen starter, og Lightning Bitcoin-saldoen din blir sendt til adressen du skannet.


![scan_address_and_Ok](assets/en/031.webp)


**MOTTA TIL KANAL:** Dette er det samme som å generere en faktura, men i noen tilfeller kan du ha mer enn én kanal, inkludert Fiat-kanaler (en unik type Lightning-kanal som kan fås i Valet wallet). Så hvis du har flere kanaler åpne, sørger dette alternativet for at du kan motta betaling til en bestemt kanal.


**PÅFYLL FRA ANDRE KANALER:** Dette alternativet er en funksjon som lar deg fylle opp en kanal fra andre eksisterende kanaler. Hvis du for eksempel har to forskjellige Lightning-kanaler (A og B), og Bitcoin-saldoen på kanal A er tom, kan du med dette alternativet enkelt og automatisk fylle opp saldoen på kanal A fra kanal B.


**DIRECT NOT PRIVATE RECEIVE:** Dette er også et alternativ for å generere en faktura for å motta betaling, men når du bruker dette alternativet, betaler avsenderen deg direkte. Det betyr at betalingen ikke går gjennom flere noder før den når deg, slik en vanlig Lightning-betaling gjør. Avsenderen vet altså at det er deg de har betalt, kjenner kanal-ID-en din osv. Dette alternativet kan ofte brukes når du mottar betaling fra en kilde du stoler på, og du ikke trenger å opprettholde personvernet ditt.


## Hostede kanaler og Fiat-kanaler


I likhet med mange andre Bitcoin wallet er Valet en enkel, lett Bitcoin og Lightning wallet. Men den har en unik Lightning-funksjon som skiller den fra de fleste andre Bitcoin wallet. Denne funksjonen kalles **Hosted and Fiat Channels**.


Fiat-kanaler er en type Lightning-implementering som gjør det enkelt å komme inn i og bruke Lightning-nettverket. Det er en depotløsning som tillater full anonymitet, akkurat som med en vanlig Lightning-kanal. Fiat channels-teknologien gjør det også mulig å opprette Bitcoin-derivater i Lightning-nettverket. Med Fiat-kanaler kan selgere for eksempel akseptere betalinger med stabil verdi i Bitcoin uten å bekymre seg for Bitcoins volatilitet.


Den nåværende implementeringen av Fiat-kanaler på Valet gjør det mulig å opprette stabile syntetiske Fiat-valutaer støttet av Sats. Den bruker et vert-klient-forhold der verten er en hvilken som helst Lightning-node som tilbyr denne tjenesten, og klienten er Valet-brukeren. Det er en depotløsning fordi alle Sats befinner seg på vertens side, men fakturagenerering, toruting og preimage-generering skjer fortsatt på klientsiden som i en vanlig Lightning-kanal.


Åpning av en Fiat-kanal tar samme prosess som åpning av en Lightning-kanal. Den eneste vesentlige forskjellen er at klienten (Valet-brukeren) i dette tilfellet ikke trenger å forplikte noen likviditet on-chain for å skape kanalkapasitet. Verten setter kanalens kapasitet og dirigerer alle betalinger for klienten.


👉 For å åpne en Fiat-kanal klikker du på det lilla **Lightning-kortet** på startsiden til wallet. Velg **Scan Node QR** (På dette tidspunktet må du ha identifisert en Host du ønsker å åpne en kanal til, og fått nodens QR. Et eksempel på en Host-node som du kan åpne en Fiat-kanal til, er SATM-noden ved Standard Sats)


**Det er viktig å merke seg at hvem som helst kan være vert. Alt du trenger er å kjøre en Lightning-node med **Fiat channel-plugin** og en **Hedging-tjeneste**. Fiat channels er et åpen kildekode-prosjekt av *Standard Sats*. Les mer om det [her](https://github.com/standardsats/fiat-channels-rfc) og [her](https://standardsats.github.io/).


SATM-noden QR nedenfor:


![SATM_node_QR](assets/en/032.webp)


👉 Når du har skannet noden QR, klikker du på **Forespør USD fiat-kanal** eller **Forespør EUR fiat-kanal** (dette er fiat-denominasjonen Fiat-saldoen din vil bli notert i). Velg USD for øyeblikket, og klikk på **OK**. Kanalen åpnes automatisk, og du kan begynne å motta Sats med en gang. Du skjønner, det er så enkelt!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Gå til startsiden til wallet, og du vil se et **lysegrønt** kort merket **USD**, som er din **Fiat-kanal**.


![fiat_channel_card](assets/en/035.webp)


**Når du mottar Sats på en Fiat-kanal, vil fiat-verdien av Sats du har mottatt være låst som en stabil saldo, mens Sats-volumet flyter med Bitcoin-prisen. Denne løsningen ble hovedsakelig utviklet for selgere som ønsker å akseptere Sats som betaling, men som ikke ønsker å møte volatilitetsutfordringene med Bitcoin. Dette hjelper dem med å opprettholde en stabil verdi til enhver tid, samtidig som de kan gjennomføre transaksjoner i Lightning-nettverket og nyte godt av den globale rekkevidden og det raske oppgjøret til Bitcoin som et byttemiddel på Lightning Network.


Når Fiat-kanalen din opprettes, ser du følgende verdifelt og hva hvert av dem betyr:


![fiat_channel_info](assets/en/036.webp)



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dette er nodenes IP-adresser. (henholdsvis IPV4 og IPV6)
- SERVER RATE:** Dette er Bitcoin-markedsprisen som verten tilbyr tjenestene til deg. Denne vil ofte være litt forskjellig fra den dominerende markedsprisen, fordi en Host kan legge til en liten premie. Det er helt opp til verten å bestemme denne prisen, og den vil derfor også variere fra vert til vert.
- FIAT-BALANCE:** Dette er den låste stabile fiat-verdien for hver sat du mottar på denne kanalen. Husk, som forklart tidligere, at når du mottar Sats på Fiat-kanalen din, blir fiat-verdien av Sats på mottakstidspunktet umiddelbart låst inn som en syntetisk stabil fiat-verdi i dette feltet. Verdien av **Fiat-saldoen** svinger ikke med markedsprisen på Bitcoin. Når du vil foreta betalinger fra denne kanalen, kan du bare sende Sats-ekvivalenten av denne Fiat-saldoen. Så tenk på dette som en digital fiat-valuta støttet av Sats.
- KAPASITET:** Dette er det totale volumet av Sats som kan sendes og mottas gjennom denne kanalen. (Dette stilles også inn av verten. Og i motsetning til en vanlig Lightning-kanal, kan denne kapasiteten justeres av verten etter behov)
- KAN SENDE:** Dette er volumet av Sats du kan sende ut på hvert punkt basert på fiat-saldoen din. Dette er helt forskjellig fra hva du har i en vanlig Lightning-kanal, fordi denne verdien flyter med Bitcoin-prisen. Det du ser her er derfor Sats-verdien av Fiat-saldoen din til enhver tid basert på **Server Rate**.
- CAN RECEIVE:** Dette er antallet Sats du kan motta til denne kanalen for øyeblikket. Etter at du har opprettet kanalen, skal denne verdien være den samme som kanalens kapasitet.
- VALUE IN FLIGHT:** Når noen sender sats til kanalen din, eller når du prøver å sende sats til noen, og transaksjonen av en eller annen grunn blir forsinket, vises det ofte i dette feltet.


Her er viktige ting å merke seg om Fiat-kanaler:



- I motsetning til en vanlig lynkanal kan du umiddelbart begynne å motta Sats når du åpner en fiat-kanal, men du kan ikke sende. Du kan bare sende ut Sats når du har mottatt Sats.
- Til enhver tid er eiendelen som sendes til og fra Sats. *Fiat-saldoen* er bare en syntetisk IOU-representasjon av en Bitcoin-verdi mottatt på et hvilket som helst tidspunkt. Så det er ikke en token-opprettelse eller en ny kryptovaluta.
- Fiat-kanalen er mest nyttig for selgere/bedrifter som er skeptiske til å ta imot Bitcoin-betalinger på grunn av bekymringer for volatilitet. Den kan også være nyttig for bedrifter som ønsker å betale ut lønn til sine ansatte i Bitcoin uten å måtte bære konsekvensene av Bitcoin-volatiliteten, som kan gjøre lønnskapitalen ustabil. Det kan også være nyttig for enkeltpersoner som bor i et område med overveiende bruk av Bitcoin, men som har faste levekostnader.
- Legg merke til at det ikke er noe felt merket som **REFUNDABLE**. Dette er fordi du teknisk sett ikke kan stenge en Fiat-kanal. Du kan bare slutte å bruke en Fiat-kanal ved å tømme saldoen til din vanlige Lightning-kanal.


### Alternativene for popup-vinduer på Fiat Channel forklart


Når du trykker på Fiat Lightning-kanalen din, vises følgende felt:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Med denne funksjonen kan du dele informasjon om Fiat-kanalen din, for eksempel ekstern peer-ID, lokal kanal-ID, dato for opprettelse osv.


**EXPORT CHANNEL STATE:** Med denne funksjonen kan du eksportere statusen til en kanal på et hvilket som helst tidspunkt. Dette er vanligvis nyttig når du skal rette kanalfeil, og en vert kan be deg om å dele dette hvis det er behov for det.


**Som nevnt tidligere kan du teknisk sett ikke stenge en Fiat-kanal, men du kan tømme saldoen i kanalen din til din eksisterende normale Lightning-kanal. Dette flytter automatisk Sat-ekvivalenten av Fiat-saldoen din til den normale lynkanalen din.


**MOTTA TIL KANAL:** Dette er det samme som å generere en faktura, men i noen tilfeller kan en bruker ha mer enn én Fiat-kanal med forskjellige verter, inkludert normale Lightning-kanaler. Så hvis en bruker har flere kanaler åpne, sikrer dette alternativet at de kan motta betaling til en spesifikk kanal.


**PÅFYLL FRA ANDRE KANALER:** Dette alternativet er en funksjon som gjør det mulig for brukeren å fylle på en kanal fra andre eksisterende kanaler. Med dette alternativet kan du altså fylle på Fiat-kanalen din fra en vanlig kanal eller andre Fiat-kanaler du har, på samme måte som du kan tømme.


**DIRECT NOT PRIVATE RECEIVE:** Dette er også et alternativ for å generere en faktura for å motta betaling, men når du bruker dette alternativet, betaler avsenderen deg direkte. Det betyr at betalingen ikke hopper gjennom ulike noder før den når deg. Avsenderen vet altså at det er deg de har betalt, kjenner kanal-ID-en din osv. Dette alternativet kan ofte brukes når du mottar betaling fra en kilde du stoler på, og du ikke trenger å opprettholde personvernet ditt.


## Betjentinnstillinger:


Som alle andre applikasjoner har Valet appinnstillinger som du kan justere etter din egen smak. Du får tilgang til innstillingssiden fra startskjermen.


👉 På startskjermen klikker du på **Gear**-ikonet øverst til høyre på skjermen for å få tilgang til innstillingene. Nedenfor finner du komponentene i innstillingsdelen.


![settings_icon](assets/en/038.webp)


**LOKAL KANALBACKUP ER AKTIVERT:** Hvis denne ellers er **Deaktivert,** bør du aktivere den, fordi dette er den eneste måten du kan gjenopprette de normale Lightning-kanalene dine hvis du avinstallerer og installerer Valet på nytt. Vi forklarer dette senere. Så klikk på denne, og gi Valet tillatelse til **medielagringen**, for det er der sikkerhetskopifilen er lagret.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**HVOR LAGER DU LOKAL BACKUP:** Så lenge du har gitt Valet tillatelse til lagringsplassen din, vil dette feltet automatisk være satt til å lagre lokale sikkerhetskopier i mappen **Downloads**. Men du kan endre det ved å klikke her og velge en hvilken som helst mappe du ønsker.


**MANAGE CHAIN WALLETS** Dette er litt teknisk, og du trenger ikke å bry deg om dette med mindre du er erfaren nok. Standardinnstillingen her er helt fin.


**LEGG TIL MASKINVAREBALLETT:** Du bør heller ikke bry deg om dette, med mindre du har en maskinvare-wallet du ønsker å koble til og overvåke. Med denne innstillingen kan du skanne og koble til din maskinvare-wallet, for eksempel Trezor- eller Cold-kort, og overvåke aktivitetene. Dette er en overvåkingsfunksjon, noe som betyr at du ikke kan utføre transaksjoner på maskinvare-wallet herfra. Du kan bare observere og overvåke wallet-aktiviteter, saldoer osv.


**SET CUSTOM ELECTRUM NODE:** Dette er også teknisk, og med mindre du er kunnskapsrik nok, bør du ikke bry deg om dette. Standardinnstillingen er god nok.


**BITCOIN UNITS:** Dette er hvordan du vil at saldoen din i Bitcoin skal vises. Det første alternativet viser saldoen din i Satoshi-termer, f.eks. 1 000 000 Sats, mens det andre alternativet viser den i BTC-desimaltegn. f.eks. 0,01BTC


**BRUK PIN-AUTHENTISERING** Hvis du merker av i denne boksen, må du sette opp en PIN-kode eller et fingeravtrykk som du må taste inn for å logge inn på wallet og autentisere transaksjoner.


**BRUK TOR-KOBLING:** Hvis du merker av i denne boksen, vil transaksjonene dine bli rutet over Tor-nettverket. Det gir et ekstra lag med personvern, men kan føre til forsinket betalingsgjennomstrømning, spesielt for Lightning-betalinger.


**VIS BIP39 GJENOPPRETTINGSFRASE:** Her kan du få tilgang til din 12-ords seed-frase for sikkerhetskopiering. Så hvis du ikke skrev det ned før, eller du ikke finner hvor du skrev det ned, kan du kopiere det herfra så lenge du fortsatt har tilgang til Wallet.


**BRUKSSTATISTIKK:** Dette viser et sammendrag av alle transaksjonene og aktivitetene dine siden wallet ble opprettet


![usage_stats](assets/en/041.webp)


## Wallet Gjenvinning


Valet er en wallet som ikke er frihetsberøvende, så hvis du mister enheten din eller avinstallerer wallet-appen, må du gjøre en wallet-gjenoppretting for å få tilbake Bitcoin-ene og Lightning-kanalene dine. I begynnelsen av denne veiledningen nevnte vi viktigheten av å skrive ned din **12-ords seed-frase**, fordi det er nøkkelen til å gjenopprette wallet. Det er ingen representanter fra kundeservice som kan hjelpe deg med å komme tilbake til wallet.


Det er to viktige verktøy som trengs for å gjenopprette din Valet wallet, avhengig av om du hadde en aktiv Lightning-kanal eller ikke. For brukere som ikke hadde en aktiv normal Lightning-kanal, er alt de trenger **12-ords seed-frasen**, ved å følge de enkle trinnene nedenfor:


👉 Installer en ny Valet-app, og start/start appen.


👉 Velg **Gjenopprett eksisterende Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Velg **Bare gjenopprettingsfrase**.


![select_recovery_phrase](assets/en/043.webp)


👉 Skriv inn gjenopprettingsfrasen på 12 ord, og klikk på **OK**.


![input_12_words](assets/en/044.webp)


Din wallet vil bli gjenopprettet. I dette tilfellet vil bare on-chain Bitcoin-saldoen din bli gjenopprettet.


Men hvis du hadde en aktiv normal lynkanal og du gjenoppretter wallet med bare gjenopprettingsfrasen, vil lynkanalen din bli tvangsstengt, og all Bitcoin-saldo du har på den, vil automatisk bli sendt til on-chain-saldoen din.


Den andre måten å gjenopprette Valet wallet på, spesielt hvis du hadde en normal Lightning-kanal åpen før du avinstallerte Valet, er å **bruke den lokale sikkerhetskopifilen som er lagret på enheten din, sammen med 12-ords seed-frasen**. Hvis du bruker disse to, vil tilstanden til Lightning-kanalen din bli gjenopprettet, og Lightning-kanalen din vil derfor ikke bli tvangslukket.


Her er trinnene:


👉 Installer en ny Valet-app, og start/start appen.


👉 Velg **Gjenopprett eksisterende Wallet**.


👉 Velg **Backup + gjenopprettingsfrase**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Velg sikkerhetskopifilen fra telefonens filbehandling. (Den er som standard alltid lagret i mappen **Downloads**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Når du har valgt riktig sikkerhetskopifil, vises en melding som bekrefter at det finnes en **"Sikkerhetskopifil"**, og du blir deretter bedt om å skrive inn en seed-frase på 12 ord.


![enter_12_words](assets/en/047.webp)


👉 Skriv inn gjenopprettingsfrasen på 12 ord, og klikk på **OK**. Du vil bli ført til startsiden til wallet.


👉 Vent til Bitcoin-nettverkssynkroniseringen (**SYNC**) og Lightning-nodesynkroniseringen (**LN Sync**) er fullført, og wallet vil bli fullstendig gjenopprettet, inkludert Lightning-kanalene dine.


![LN_sync](assets/en/048.webp)


## Konklusjon


Valet er en spennende wallet-løsning, med funksjoner som gjør den egnet for onboarding av nye brukere. Den har også en Fiat-kanal, en ikke helt ny teknologi som sikrer integrering av fiat-drevne virksomheter på Bitcoin-standarden.


Last ned Valet i dag, og prøv det!!! 🧡