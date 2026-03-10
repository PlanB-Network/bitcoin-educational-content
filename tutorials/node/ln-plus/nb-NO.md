---
name: Lightning Network+
description: Få gratis innkommende likviditet med kooperative åpninger på Lightning-noden din
---

![cover](assets/cover.webp)



## Innledning



[LN+ (Lightning Network Plus)] (https://lightningnetwork.plus/) er en samfunnsplattform som er utformet for å legge til rette for samarbeid mellom Lightning Network-nodeoperatører. Hovedmålet er å forbedre tilkoblingsmulighetene, likviditeten og desentraliseringen av Lightning-nettverket, uten behov for sentraliserte mellomledd.



Denne opplæringen vil fokusere på **"Swaps"**-tjenesten, som er den mest brukte og strukturerende funksjonen i LN+ i dag. De andre tjenestene som tilbys av plattformen, vil også bli presentert.



## LN+ oversikt



### Hva er Lightning Network Plus?



Lightning Network Plus (LN+) er en fellesskapsplattform for Lightning-nodeoperatører som ønsker å samarbeide direkte og frivillig. Målet er å legge til rette for å skape nyttige, balanserte og bærekraftige Lightning-kanaler, samtidig som man unngår behovet for sentraliserte løsninger eller pålagte knutepunkter.



LN+ er basert på et grunnleggende prinsipp: peer-to-peer-samarbeid, basert på åpenhet, gjensidighet og omdømme.



### LN+-tjenester i korte trekk



LN+ tilbyr flere tjenester som er utformet for å forbedre topologien og likviditeten i Lightning-nettverket, blant annet :





- Swaps**: gjensidig åpning av kanaler mellom operatører (hovedtjeneste).
- Ringer**: sirkulære kanalåpninger mellom flere deltakere.
- Tillitsbaserte swapper**: varianter som i større grad baserer seg på deltakernes tillit og historikk.
- Sosiale funksjoner**: profiler, kommentarer og omdømmesystem.



I resten av denne veiledningen konsentrerer vi oss utelukkende om **Swaps**-tjenesten, som er kjernen i dagens bruk av LN+.



## LN+ "Swaps"-tjeneste



### Definisjon av et LN+-bytte



Et LN+ **bytte** er en frivillig avtale mellom to Lightning-nodeoperatører om gjensidig åpning av Lightning-kanaler med tilsvarende (eller forhåndsavtalt) kapasitet. I motsetning til en konvensjonell unilateral kanalåpning, er byttet basert på **eksplisitt gjensidighet**.



I praksis :





- Du åpner en kanal til partnerens node.
- Partneren din åpner en kanal til noden din.
- Begge parter binder opp en tilsvarende mengde on-chain bitcoins.



### Hva er hensikten med swaps for nodeoperatører?



Swaps-tjenesten tar for seg flere viktige problemer som Lightning-operatører støter på:





- Forbedret tilkobling**: Opprettelse av nyttige toveis kanaler så snart de åpnes.
- Bedre likviditetsstyring**: Hver part har både inngående og utgående kapasitet.
- Redusert risiko for unødvendige kanaler**: Partneren oppfordres til å holde kanalen åpen.
- Større desentralisering**: direkte forbindelser mellom operatørene, uten pålagte knutepunkter.



### For hvilke nodeprofiler er swaps nyttige?



Swaps er spesielt nyttige for :





- Nye noder som raskt ønsker å forbedre rutbarheten sin.
- Mellomledd som ønsker å øke tettheten i kanalgrafen sin.
- Routing-orienterte noder som ønsker å optimalisere topologien sin.



## Koble Lightning-noden til LN+



### Tekniske krav



Før du begynner, trenger du :





- En fungerende Lightning-node (LND, Core Lightning eller Eclair).
- Tilgang til nodens administrasjonsgrensesnitt.
- Tilstrekkelig on-chain-kapasitet til å åpne kanaler.



Gå til nettstedet [Lightning Network](https://lightningnetwork.plus/) Plus og klikk på "Logg inn"-knappen øverst til høyre i grensesnittet.



![capture](assets/fr/03.webp)



### Autentisering ved hjelp av meldingssignatur



For å autentisere deg selv må du signere meldingen ved hjelp av den private nøkkelen til Lightning-noden din. Med ThunderHub er denne operasjonen veldig enkel.



Begynn med å kopiere meldingen som vises av LN+.



![capture](assets/fr/04.webp)



I ThunderHub går du til fanen `Verktøy` og klikker deretter på knappen `Signer` i delen `Meldinger`.



![capture](assets/fr/05.webp)



Lim inn autentiseringsmeldingen fra LN+, og klikk deretter på `Signer`.



![capture](assets/fr/06.webp)



ThunderHub signerer deretter denne meldingen ved hjelp av nodens private nøkkel. Kopier den genererte signaturen.



![capture](assets/fr/07.webp)



Lim inn denne signaturen i det tilsvarende feltet på LN+-nettstedet, og klikk deretter på `Logg på`.



![capture](assets/fr/08.webp)



Du er nå koblet til LN+ med Lightning-noden din. Denne prosessen gjør det mulig for LN+ å verifisere at du er den rettmessige eieren av noden du gjør krav på på plattformen deres.



![capture](assets/fr/09.webp)



Hvis du ønsker det, kan du tilpasse LN+-profilen din, for eksempel ved å legge til en kort biografi.



## Delta i en eksisterende byttehandel



### Tilgang til byttetilbud



For å delta i din første kanalåpning, går du til menyen `Swaps` øverst i grensesnittet. Her finner du alle tilgjengelige bytter, avhengig av nodens egenskaper.



![capture](assets/fr/10.webp)



### Vilkår for kvalifisering



For å bli med i et eksisterende byttetilbud velger du bare den tilsvarende annonsen og registrerer deg. LN+ lar imidlertid bytteskaperen definere visse **kvalifiseringsbetingelser**, for eksempel :





- et minimum antall kanaler som allerede er åpne ;
- minimum total nodekapasitet ;
- visse typer tilkoblinger godtas.



### Nyere noder



Som et resultat av dette, spesielt i de tidlige stadiene av bruken, er det mulig at **få eller ingen tilbud er tilgjengelige** for noden din. Dette er en vanlig situasjon for nye noder eller noder som ennå ikke er tilkoblet.



I mitt tilfelle oppfylte ingen av tilbudene de nødvendige kriteriene, til tross for at det fantes noen åpne kanaler.



## Lag ditt eget byttetilbud



### Når bør du opprette ditt eget bytte?



Når det ikke finnes noe eksisterende tilbud, er det ofte den beste løsningen å opprette ditt eget bytte. Det gir deg også mulighet til å beholde kontrollen over parameterne for byttet.



### Bytt konfigurasjon



Klikk på **Start Liquidity Swap**, og konfigurer deretter tilbudsparametrene dine:





- velg det totale antallet deltakere (3, 4 eller 5);
- angir kapasiteten til kanalene som skal åpnes;
- definere forpliktelsesperioden hvor deltakerne forplikter seg til ikke å stenge kanalene sine;
- angi eventuelle begrensninger som gjelder for deltakerne (minste antall kanaler, minste totale kapasitet, type tilkobling som godtas).



![capture](assets/fr/11.webp)



### Publisering og deltakernes forventninger



Når alle parameterne er lagt inn, klikker du på **Start Liquidity Swap** for å publisere tilbudet ditt. Nå er alt du trenger å gjøre å vente på at andre operatører registrerer seg.



![capture](assets/fr/12.webp)



## Fullføre et bytte



### Effektiv kanalåpning



Nå som alle bytteposisjonene er tatt, kan hver deltaker se fra LN+-grensesnittet hvilken node han må åpne en Lightning-kanal til.



![capture](assets/fr/13.webp)



På din side åpner du kanalen ved å bruke Node-ID-en som er oppgitt av LN+, og respekterer beløpet som er angitt. Denne operasjonen kan utføres via ThunderHub, en annen Lightning node manager eller direkte via nodens grunnleggende grensesnitt.



![capture](assets/fr/14.webp)



Når kanalen er åpnet, vises den i seksjonen for ventende kanaler.



![capture](assets/fr/15.webp)



### Bekreftelse i LN+



Gå deretter tilbake til LN+ for å bekrefte at du har startet kanalåpningen ved å klikke på knappen `Kanalåpning startet`.



![capture](assets/fr/16.webp)



### Slutt på byttet



Når alle deltakerne har åpnet de kanalene de har forpliktet seg til, anses byttet som fullført.



## Omdømme og god kommunikasjonspraksis



### LN+ omdømmesystem



LN+ har et omdømmesystem som er basert på deltakernes meninger etter endt swap. Disse meningene er offentlige og påvirker direkte en operatørs mulighet til å bli med i eller opprette fremtidige bytter.



![capture](assets/fr/17.webp)



### Anbefalt beste praksis



For å bevare et godt omdømme og sikre en smidig gjennomføring av byttene, anbefales det å :





- respektere tidsfrister for åpning av kanaler ;
- kommunisere raskt dersom det oppstår problemer eller forsinkelser;
- bruke kommentarfeltet til å utveksle synspunkter med andre deltakere;
- ikke stenge en kanal før utløpet av forpliktelsesperioden.




![capture](assets/fr/18.webp)



### Hvorfor omdømme er sentralt for LN+



LN+ er basert på en modell for frivillig samarbeid, uten sterke tekniske begrensninger. Omdømme er derfor det viktigste insentivet for å sikre at deltakerne er pålitelige og til å stole på.



## Andre LN+ tjenester



I tillegg til Swaps tilbyr LN+ andre tjenester som er utformet for å forbedre konnektiviteten og koordineringen mellom Lightning-nodeoperatører. Ringer** gjør det mulig for flere deltakere å opprette en sløyfe av kanalåpninger, noe som forsterker redundansen i rutingsstiene og tettheten i Lightning-grafen. Tillitsbaserte bytter** er basert på lignende prinsipper som klassiske bytter, men gir større fleksibilitet til deltakere som allerede har et etablert rykte på plattformen.



LN+ integrerer også sosiale funksjoner som offentlige nodeprofiler, byttekommentarer og et omdømmesystem. Disse verktøyene er ikke tekniske tjenester i seg selv, men spiller en sentral rolle for at plattformen skal fungere smidig, og legger til rette for kommunikasjon, koordinering og tillit mellom operatørene.



## Konklusjon



LN+s Swaps-tjeneste er et effektivt verktøy for å forbedre konnektiviteten, likviditeten og desentraliseringen i Lightning-nettverket. Ved å fremme gjensidige, koordinerte kanalåpninger gjør LN+ det mulig for nodeoperatører å styrke topologien sin, samtidig som de fremmer ansvarlig, desentralisert samarbeid.