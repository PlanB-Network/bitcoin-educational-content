---
name: Ashigaru - Ricochet
description: Forstå og bruke Ricochet-transaksjoner
---
![cover ricochet](assets/cover.webp)



> *Et førsteklasses verktøy som gir ekstra historikk til transaksjonen din. Stopper svartelistene og bidrar til å beskytte deg mot urettferdige tredjepartsstengninger av kontoer

## Hva er en Ricochet?



Ricochet er en teknikk som består i å utføre flere fiktive transaksjoner mot seg selv for å simulere en overføring av bitcoin-eierskap. Dette verktøyet skiller seg fra Ashigarus andre transaksjoner (arvet fra Samurai Wallet) ved at det ikke gir prospektiv anonymitet, men snarere en form for retrospektiv anonymitet. Ricochet utvisker faktisk de spesifikke egenskapene som kan svekke fungibiliteten til en Bitcoin-del.



Hvis du for eksempel gjør en coinjoin, vil den delen som kommer ut av miksen, bli identifisert som en slik. Kjedeanalyseverktøy kan oppdage kildene til coinjoin-transaksjoner og tildele en etikett til delene som kommer ut av dem. Coinjoin har som mål å bryte en mynts historiske koblinger, men dens vei gjennom coinjoins kan fortsatt spores. Dette fenomenet kan sammenlignes med kryptering av en tekst: Selv om den opprinnelige teksten ikke er tilgjengelig i klartekst, er det lett å se at den har blitt kryptert.



Merkelappen "coinjoined" kan påvirke fungibiliteten til en UTXO. Regulerte enheter, som utvekslingsplattformer, kan nekte å godta en coinjoined UTXO, eller til og med kreve forklaringer fra eieren, med risiko for å få kontoen din blokkert eller pengene dine frosset. I noen tilfeller kan plattformen til og med rapportere oppførselen din til statlige myndigheter.



Det er her Ricochet-metoden kommer inn i bildet. For å viske ut avtrykket etter en coinjoin, utfører Ricochet fire påfølgende transaksjoner der brukeren overfører pengene sine til seg selv på forskjellige adresser. Etter denne sekvensen av transaksjoner sender Ricochet-verktøyet til slutt bitcoinsene til deres endelige destinasjon, for eksempel en utvekslingsplattform. Målet er å skape avstand mellom den opprinnelige coinjoin-transaksjonen og den endelige utgiftshandlingen. På denne måten vil analyseverktøyene i blokkjeden anta at det sannsynligvis har skjedd en overføring av eierskap etter coinjoin-transaksjonen, og at det derfor ikke er behov for å iverksette tiltak mot utstederen.



![image](assets/fr/01.webp)



I møte med Ricochet-metoden kunne man tenke seg at programvare for kjedeanalyse ville gå dypere enn fire sprett. Disse plattformene står imidlertid overfor et dilemma når de skal optimalisere deteksjonsterskelen. De må fastsette en terskel for hvor mange hopp som skal til for å akseptere at det sannsynligvis har skjedd et eierskifte, og at koblingen til en tidligere coinjoin bør ignoreres. Det er imidlertid risikabelt å fastsette denne terskelen: Hver økning i antall hopp som observeres, øker eksponentielt antallet falske positiver, det vil si personer som feilaktig blir markert som deltakere i en coinjoin, selv om operasjonen i virkeligheten ble utført av noen andre. Dette scenariet utgjør en stor risiko for disse selskapene, ettersom falske positiver fører til misnøye, noe som kan føre til at berørte kunder går til konkurrenten. På lang sikt kan en overambisiøs deteksjonsterskel føre til at en plattform mister flere kunder enn konkurrentene, noe som kan true plattformens levedyktighet. Det er derfor komplisert for disse plattformene å øke antallet observerte bounces, og 4 er ofte et tilstrekkelig antall for å motvirke analysene deres.



Det vanligste bruksområdet for Ricochet oppstår når det er nødvendig å skjule en tidligere deltakelse i en coinjoin på en UTXO som du eier.** Ideelt sett er det best å unngå å overføre bitcoins som har gjennomgått en coinjoin til regulerte enheter. Likevel, i tilfelle du ikke har noe annet alternativ, spesielt i det presserende behovet for å likvidere bitcoins i statlig valuta, tilbyr Ricochet en effektiv løsning.



## Hvordan fungerer Ricochet på Ashigaru?



Ricochet er rett og slett en metode for å sende bitcoins til seg selv, opprinnelig oppfunnet av utviklerne av Samurai Wallet. Det er derfor fullt mulig å simulere en Ricochet manuelt, uten behov for et spesialisert verktøy. For de som ønsker å automatisere prosessen og samtidig nyte et mer polert resultat, representerer Ricochet-verktøyet som er tilgjengelig via Ashigaru-applikasjonen (som er en Samourai fork) en god løsning.



Siden Ashigaru tar betalt for tjenesten, koster en Ricochet 100 000 sats` i serviceavgift, pluss en mining-avgift. Det anbefales derfor å bruke den ved overføringer av betydelige beløp.



Ashigaru-applikasjonen tilbyr to Ricochet-varianter:





- Reinforced Ricochet, eller "forskjøvet levering", som gir fordelen av å spre Ashigarus serviceavgifter over de fem påfølgende transaksjonene. Dette alternativet sikrer også at hver transaksjon sendes på et separat tidspunkt og registreres i en annen blokk, noe som i størst mulig grad etterligner oppførselen ved et eierskifte. Selv om denne metoden er langsommere, er den å foretrekke for dem som ikke har det travelt, ettersom den maksimerer Ricochets effektivitet ved å styrke dens motstand mot kjedeanalyse;





- Den klassiske Ricochet, som er designet for å utføre operasjonen raskt, sender alle transaksjoner i et redusert tidsintervall. Denne metoden gir derfor mindre konfidensialitet og mindre motstand mot analyse enn den forsterkede metoden. Den bør bare brukes til hastesendinger.



## Hvordan lage en Ricochet på Ashigaru?



Det er veldig enkelt å gjøre en ricochet på Ashigaru: bare aktiver det tilsvarende alternativet når du oppretter en send-transaksjon. For å begynne, klikk på `+`-knappen, deretter på `Send`, og velg kontoen du ønsker å sende pengene fra.



![Image](assets/fr/02.webp)



Fyll inn transaksjonsinformasjonen: beløpet som skal sendes og mottakerens endelige adresse etter Ricochet-hoppene. Kryss deretter av for alternativet `Ricochet`.



![Image](assets/fr/03.webp)



Deretter kan du velge mellom de to Ricochet-modusene som er omtalt i teoridelen: enten klassisk Ricochet, der alle transaksjonene er inkludert i samme blokk, eller forskjøvet levering, som forbedrer Ricochet-kvaliteten på bekostning av en lengre forsinkelse.



Når du har gjort ditt valg, trykker du på pilen nederst på skjermen for å bekrefte.



![Image](assets/fr/04.webp)



På neste skjermbilde ser du en fullstendig oversikt over transaksjonen din. Det er også her du kan justere gebyrsatsen for Ricochet-transaksjonene dine i henhold til markedsforholdene. Hvis du er fornøyd med alt, kan du dra i den grønne pilen for å signere og distribuere Ricochet-transaksjoner.



![Image](assets/fr/05.webp)



Vent mens de ulike hoppene kjøres automatisk.



![Image](assets/fr/06.webp)



Transaksjonene dine har blitt sendt.



![Image](assets/fr/07.webp)



Du er nå fullt ut kjent med Ricochet-alternativet som er tilgjengelig i Ashigaru-applikasjonen. For å gå videre, anbefaler jeg at du tar BTC 204-kurset mitt, som vil lære deg i detalj hvordan du kan styrke konfidensialiteten din i kjeden.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c