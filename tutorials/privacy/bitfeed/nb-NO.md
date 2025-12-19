---
name: Bitfeed
description: Utforsk den viktigste Bitcoin-protokollkjeden.
---

![cover](assets/cover.webp)



Bitfeed er en plattform for visualisering av kjedelaget i Bitcoin-protokollen. Den ble initiert av en av bidragsyterne til Mempool.space-prosjektet og skiller seg hovedsakelig ut for sitt minimalistiske utseende og brukervennlighet.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

I denne veiledningen tar vi en titt på dette verktøyet, som lar deg utforske alle transaksjoner og blokker i nettverket.



## Kom i gang med Bitfeed



Bitfeed er en plattform som fokuserer på tre hovedpunkter:





- Blockchain-konsultasjon**,
- Transaksjonssøk**,
- Visualisering av mempool**.



### Rådføring med blokkjeden



På Bitfeed-hjemmesiden finner du hovedsakelig :





- Søkefeltet: Denne delen er inngangspunktet for blockchain-spørringer. Her kan du søke etter en spesifikk blokk ved hjelp av nummer eller hash. Du kan også søke etter spesifikke transaksjoner og Bitcoin-adresser for å verifisere visse transaksjonsopplysninger i nettverket.



![searchBar](assets/fr/01.webp)



Øverst i venstre hjørne kan du se den nåværende prisen på bitcoin, estimert i amerikanske dollar (USD).



![price](assets/fr/02.webp)



På høyre sidefelt finner du plattformmenyen. Fra denne menyen kan du tilpasse plattformgrensesnittet etter eget ønske, legge til eller fjerne elementer og tilpasse visningsfiltre. Du kan for eksempel vise størrelsen på hver blokk etter verdi eller etter vekt i virtuelle byte (vBytes).



![menu](assets/fr/03.webp)



I midten av siden er den siste blokken som ble utvunnet, med en oversikt over alle transaksjonene som er inkludert i den blokken. Denne delen inneholder informasjon om tidsstempelet, det totale antallet bitcoins som er involvert i blokken, størrelsen på blokken i byte, antall transaksjoner og den gjennomsnittlige transaksjonskostnaden per virtuelle byte i blokken.



![block](assets/fr/04.webp)



Du kan gå tilbake i kanalens historikk ved å søke etter en bestemt blokk i søkefeltet, og se den i henhold til dine kriterier.



Vi ønsker for eksempel å se transaksjonene i blokk `879488`.



![bloc](assets/fr/05.webp)



Den første transaksjonen i denne blokken representerer **coinbase**-transaksjonen som gjør det mulig for utvinneren av denne blokken å tjene mining-belønningen, som bare kan brukes etter at 100 blokker har blitt utvunnet, og som består av de inkluderte transaksjonsgebyrene og blokktilskuddet. Denne transaksjonen er den som gjør det mulig å utstede nye bitcoins i systemet.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Som standard blir transaksjoner i en blokk representert i henhold til to kriterier:




- Størrelsen, som kan variere mellom verdien og vekten (vBytes) ;
- Fargen kan variere mellom alder og forholdet mellom transaksjonsavgifter per virtuelle byte.



![options](assets/fr/07.webp)



Vi kan derfor konkludere med at alle transaksjoner som inngår i samme blokk, har samme antall bekreftelser i blokkjeden. De største kubene representerer transaksjonene som inneholder den høyeste mengden bitcoins.



Denne tolkningen bekreftes ytterligere av menyalternativet **"Info"**, som informerer oss om oversettelsen av fargen og størrelsen på blokkens transaksjoner.



![infos](assets/fr/08.webp)



Du kan også se transaksjonene i en blokk etter virtuelle byte og avgiftsforhold. Denne visningen kan avvike fra den forrige, ettersom bitcoin-verdien som inngår i en transaksjon ikke definerer størrelsen på den.



![visualisation](assets/fr/09.webp)



### Visning av transaksjoner



Du kan søke etter en transaksjon ved hjelp av dens identifikator via søkefeltet. Du kan også klikke på en kube for å se informasjonen knyttet til den aktuelle transaksjonen.



I vårt tilfelle tar vi transaksjonen som opptar den største plassen i blokk `879488`.



![biggest](assets/fr/10.webp)



Du vil se at denne transaksjonen har `42,989`, som representerer forskjellen mellom den siste blokken som ble utvunnet og den valgte blokken vår. Disse bekreftelsene bidrar til å styrke sikkerheten i Bitcoin-nettverket, for for å endre denne transaksjonen på en ondsinnet måte må angriperne ha tilsvarende datakraft til å omskrive hele hovedblokk-kjeden.



Størrelsen på denne transaksjonen er 57 088 vByte, hovedsakelig på grunn av det store antallet UTXO-er som brukes i konstruksjonen (842 oppføringer). Overraskende nok er gebyrforholdet relativt lavt (bare 4 sats/vByte) sammenlignet med det generelle blokkgjennomsnittet på 5,82 sats/vByte.



Transaksjonen som tar opp mest plass, er derfor ikke nødvendigvis den transaksjonen som har høyest transaksjonskostnad.



![transaction](assets/fr/11.webp)



Hvis du følger skalaen i **Info**-menyen, er transaksjonen med den høyeste transaksjonskostnaden den lilla. Dette er transaksjonen [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) med en transaksjonskostnadsratio på `147,49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool-visualisering



Mempool er det virtuelle stedet der Bitcoin-transaksjoner som venter på å bli inkludert i en blokk, er gruppert sammen. Bitfeed gjør det mulig å konsultere [mempool](https://planb.academy/resources/glossary/mempool) for flere Bitcoin-utvinnere, og tilbyr et bredt spekter av transaksjonssporing.



![mempool](assets/fr/13.webp)



I denne delen kan du spore alle gyldige og ennå ubekreftede transaksjoner i Bitcoin-nettverkets hovedkjede.



![unconfirmed](assets/fr/14.webp)



Du har nå en guide til hvordan du bruker Bitfeed-plattformen til å analysere blokker og transaksjoner for å visualisere informasjonen som er tilgjengelig på Bitcoin-nettverkets hovedkjede, samtidig som du drar nytte av et minimalistisk, brukervennlig grensesnitt. Hvis du likte denne veiledningen, anbefaler vi at du tar neste steg: oppdag Lightning Network via Amboss-prosjektet.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017