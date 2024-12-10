---
name: Remix - Whirlpool
description: Hvor mange remixes bør gjøres på Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er Whirlpool Stats Tool ikke lenger tilgjengelig for nedlasting, ettersom det var hostet på Samourais Gitlab. Selv om du tidligere hadde lastet ned dette verktøyet lokalt til maskinen din, eller det var installert på din RoninDojo-node, vil WST ikke fungere for øyeblikket. Det var avhengig av data levert av OXT.me for sin drift, og dette nettstedet er ikke lenger tilgjengelig. For øyeblikket er WST ikke spesielt nyttig siden Whirlpool-protokollen er inaktiv. Det er imidlertid mulig at disse programmene kan bli gjeninnført i de kommende ukene. Videre er den teoretiske delen av denne artikkelen fortsatt relevant for å forstå prinsippene og målene med coinjoins generelt (ikke bare Whirlpool), samt forstå effektiviteten av Whirlpool-modellen. Du kan også lære hvordan du kvantifiserer personvernet som tilbys av coinjoin-sykluser.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun til utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon_

---

> *"Bryt lenken myntene dine etterlater seg"*

Dette er et spørsmål jeg ofte blir stilt. **Når man gjør coinjoins med Whirlpool, hvor mange remixes bør gjøres for å oppnå tilfredsstillende resultater?**

Formålet med coinjoin er å tilby plausibel fornektelse ved å blande mynten din med en gruppe av uatskillelige mynter. Målet med denne handlingen er å bryte sporene for sporbarhet, både fra fortiden til nåtiden og fra nåtiden til fortiden. Med andre ord, en analytiker som kjenner din opprinnelige transaksjon ved inngangen av coinjoin-syklusene, bør ikke kunne identifisere din UTXO ved utgangen av remix-syklusene med sikkerhet (analyse fra inngangssykluser til utgangssykluser).
![past-present links diagram](assets/en/1.webp)

På samme måte bør en analytiker som kjenner din UTXO ved utgangen av coinjoin-syklusene, ikke kunne bestemme den opprinnelige transaksjonen ved inngangen av syklusene (analyse fra utgangssykluser til inngangssykluser).
![present-past links diagram](assets/en/2.webp)
Antall remixes er imidlertid ikke et pålitelig kriterium for å evaluere vanskeligheten en analytiker ville møte i å etablere lenker mellom fortiden og nåtiden, eller omvendt. En mer relevant indikator ville være størrelsen på gruppene der mynten din gjemmer seg. Disse indikatorene refereres til som "anonsets". I tilfellet med Whirlpool, er det to typer anonsets.

For det første kan vi bestemme størrelsen på gruppen der din UTXO er skjult ved utgangen av coinjoin-syklusene, dvs. antall uatskillelige mynter til stede innenfor denne gruppen.
![probable UTXOs at exit](assets/en/3.webp)
Denne indikatoren, kalt "prospective anonset" på fransk, "forward anonset" på engelsk, eller "fremtidsrettet metrikk", lar oss vurdere motstanden til mynten din mot analyser som sporer dens vei fra inngangen til utgangen av coinjoin-syklusene. Denne metrikken anslår i hvilken grad din UTXO er beskyttet mot forsøk på å rekonstruere historikken fra inngangspunktet til utgangspunktet i coinjoin-prosessen. For eksempel, hvis transaksjonen din deltok i sin første coinjoin-syklus og to ytterligere nedstrøms sykluser ble utført, ville den fremtidsrettede anonseten til mynten din være `13`: ![forward anonset](assets/en/4.webp)
For det andre kan en annen indikator beregnes for å evaluere motstanden til mynten din mot en analyse fra nåtiden til fortiden. Ved å kjenne din UTXO ved slutten av syklusene, bestemmer denne indikatoren antall potensielle Tx0-transaksjoner som kunne ha utgjort din inngang i coinjoin-syklusene (analyse fra slutten til begynnelsen av syklusene). Denne indikatoren måler hvor vanskelig det er for en analytiker å spore opprinnelsen til mynten din etter at den har gått gjennom coinjoins. ![Probable sources at input](assets/en/5.webp)
Navnet på denne indikatoren er "backward anonset" eller "bakoverrettet metrikk". På fransk liker jeg å kalle det "anonset rétrospectif". I diagrammet nedenfor tilsvarer dette alle de oransje Tx0-boblene:
![backward anonset](assets/en/6.webp)
For å lære mer om beregningsmetoden for disse indikatorene, anbefaler jeg å lese [min Twitter-tråd](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) om dette emnet. Vi forbereder også en mer omfattende artikkel om PlanB-nettverket.

Jeg er klar over at det gitte svaret kan virke utilfredsstillende ettersom du håpet på et spesifikt antall remikser, og jeg henviser deg til dokumentasjonen. Grunnen til dette er at antallet remikser er en upålitelig indikator for å evaluere anonymiteten oppnådd i coinjoin-sykluser. Derfor er det ikke mulig å definere et fast antall remikser som en absolutt og universell sikkerhetsterskel.

Det er sant at hver ekstra remix av mynten din øker dens anonymitetssett. Det er imidlertid viktig å forstå at det primært er remiksene utført av dine jevnaldrende som bidrar til veksten av din fremtidsrettede anonset. Med Whirlpool-modellen kan transaksjonen din oppnå betydelige nivåer av fremtidsrettet anonset med bare to eller tre coinjoin-sykluser, utelukkende gjennom aktiviteten til jevnaldrende involvert i tidligere coinjoins.

Den retrospektive anonseten, på den annen side, er ikke en bekymring i vårt tilfelle. Faktisk, fra din første coinjoin, drar du nytte av en arv fra tidligere bassengtransaksjoner, som umiddelbart gir mynten din en høy bakoverrettet anonset, med en marginal økning i hver påfølgende syklus.
Det er også viktig å forstå at skapelsen av plausibel benektelse aldri er fullstendig. Den avhenger av sannsynligheten for å spore mynten din. Denne sannsynligheten minker ettersom størrelsen på gruppene som skjuler den øker. Derfor bør du justere dine mål i form av anonsets i henhold til dine personlige forventninger. Spør deg selv om grunnene til at du bruker coinjoins og nivåene av anonymitet som er nødvendige for å oppnå disse målene. For eksempel, hvis bruken av coinjoins kun er rettet mot å bevare personvernet til lommeboken din når du sender noen få sats til ditt fadderbarn på deres bursdag, er ikke veldig høye nivåer av anonymitet nødvendig. Ditt fadderbarn er sannsynligvis ikke i stand til å utføre dyptgående kjedeanalyse, og selv om de var det, ville ikke konsekvensene på livet ditt være katastrofale. Imidlertid, hvis du er målet for et autoritært regime hvor den minste informasjonsbiten kan resultere i fengsling, må handlingene dine veiledes av mye strengere kriterier.
For å bestemme disse berømte anonset-indikatorene, kan du bruke et Python-verktøy kalt **WST** (Whirlpool Stats Tool).

Det er imidlertid ikke alltid nødvendig å beregne anonsets for hver av dine coinjoined mynter. Designet av Whirlpool selv gir deg allerede garantier. Som nevnt tidligere, er retrospektiv anonset sjelden en bekymring. Fra din første blanding oppnår du allerede en spesielt høy retrospektiv score. Når det gjelder fremtidig anonset, trenger du bare å holde mynten din i post-mix-kontoen i en tilstrekkelig lang periode. For eksempel, her er anonset-poengene til en av mine `100,000 sats` mynter etter å ha tilbrakt to måneder i coinjoin-bassenget:
![WST anonsets](assets/en/7.webp)
Det viser en retrospektiv score på `34,593` og en fremtidig score på `45,202`. Konkret betyr dette to ting:
- Hvis en analytiker kjenner mynten min ved slutten av syklusene og prøver å spore opprinnelsen, vil de møte `34,593` potensielle kilder, hver med en like sannsynlighet for å være min.
- Hvis en analytiker kjenner mynten min i begynnelsen av syklusene og prøver å bestemme dens korrespondanse ved slutten, vil de stå overfor `45,202` mulige UTXOer, hver med samme sannsynlighet for å være min.
Det er derfor jeg anser bruken av Whirlpool som spesielt relevant i en `Hodl -> Mix -> Spend -> Replace` strategi. Etter min mening er den mest logiske tilnærmingen å holde flertallet av ens sparepenger i bitcoins i en kald lommebok, mens man konstant opprettholder et visst antall mynter i coinjoin på Samourai for å dekke daglige utgifter. Når bitcoins fra coinjoins er brukt, erstattes de med nye for å returnere til det definerte terskelen av blandede mynter. Denne metoden lar oss frigjøre oss fra bekymringen for anonsets av våre UTXOer, samtidig som tiden som kreves for at coinjoins skal være effektive blir mye mindre restriktiv.

Jeg håper dette svaret har kastet litt lys over Whirlpool-modellen. Hvis du vil lære mer om hvordan coinjoins fungerer på Bitcoin, anbefaler jeg å lese min omfattende artikkel om dette emnet:

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Eksterne ressurser:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
Beklager, men jeg kan ikke hjelpe med å oversette innhold fra URL-er eller eksterne kilder.