---
name: Mempool
description: Utforsk hele Bitcoin-økosystemet.
---

![cover](assets/cover.webp)



Bitcoin-protokollen er et pseudonymt, desentralisert nettverk som er åpent for konsultasjon. Medlemmer (noder), det vil si datamaskiner med en instans av Bitcoin-programvaren, har ubegrenset tilgang til alle data som publiseres på Bitcoin. I Bitcoins tidlige år var imidlertid ikke protokollen like allment tilgjengelig som den er i dag.


I Bitcoins tidlige dager var det nødvendig å kjøre en Bitcoin-node for å få tilgang til de riktige verktøyene (bitcoin-cli) for å avhøre nettverket fra kommandolinjer.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Det er derfor satt i gang prosjekter for å utvide Bitcoin-fellesskapet og gjøre det mer tilgjengelig for alle som ikke eier en node og/eller ikke har de nødvendige tekniske ferdighetene.



I denne veiledningen skal vi se nærmere på **Mempool.space**-prosjektet, dets funksjoner og innvirkningen det har hatt på Bitcoin-økosystemet.



## Hva er Mempool.space?



**Mempool.space** er en utforsker med åpen kildekode som gir nyttig informasjon om transaksjoner, transaksjonsgebyrer, blokker og utvinnere i de ulike Bitcoin-protokollnettverkene. Den ble lansert i 2020 og gir en betydelig forbedring av brukeropplevelsen gjennom representativ grafikk, jevne animasjoner og oversiktlige grensesnitt.



For å forstå prosjektet er en Mempool (minnepool) et virtuelt rom der alle transaksjoner som venter på bekreftelse i Bitcoin-nettverket, lagres. En Mempool er som et "venterom" der Bitcoin-transaksjoner venter på å bli bekreftet. Hver datamaskin i nettverket (node) har sitt eget venterom, noe som forklarer hvorfor ikke alle transaksjoner er synlige for alle samtidig.



Plattformens viktigste innvirkning på Bitcoin-økosystemet er at den gir deg tilgang til den varierte informasjonen i minneområdene til de fleste nodene som finnes på Bitcoin, uten at du trenger å kjøre en av dem. Mempool.space er et depot for visning av og søk i Bitcoin-protokollnettverk.



Stadig mer utbredt bruk i økosystemet og det faktum at Mempool.space er åpen kildekode, har gjort det mulig å integrere det i flere og flere personlige hostingsystemer. Du kan nå ha din egen forekomst av Mempool.space direkte på din personlige node. Se veiledningen vår om hvordan du konfigurerer Mempool.space på Umbrel-noden din nedenfor.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Grunnleggende om Mempool.space



Som nevnt ovenfor er [Mempool.space](https://Mempool.space) en Bitcoin-protokollutforsker som lar deg overvåke transaksjonene dine og spredningen av dem i det valgte Bitcoin-nettverket i sanntid, fra en grafisk Interface.



Mempool.space støtter mange nettverk med Bitcoin-protokoll.


I menylinjen finner du følgende nettverk:




- **Mainnet**: Det viktigste Bitcoin-nettverket der ekte Bitcoin-transaksjoner finner sted.
- **Signet**: Et testnettverk som bruker digitale signaturer til å validere blokker uten å kreve de samme ressursene som hovednettverket.
- **Testnet 3**: Et risikofritt test- og utviklingsnettverk på Bitcoin-protokollen.
- **Testnet 4**: Den nye versjonen av Testnet 3 gir større stabilitet og nye konsensusregler til testmiljøet.



![reseaux](assets/fr/01.webp)



På hjemmesiden, til venstre i Green, ser du de mulige fremtidige blokkene (grupper av transaksjoner) som er klare til å bli validert og integrert (utvunnet) i Bitcoin-nettverket. I gjennomsnitt utvinnes en blokk hvert tiende minutt: Ta vare på denne informasjonen, da den vil komme til nytte senere i utviklingen vår.


I lilla, på høyre side, finner du de siste blokkene som er utvunnet på Bitcoin, og nummeret på den siste blokken som ble utvunnet, representerer den nåværende høyden på nettverket.



![blocs](assets/fr/02.webp)



Avsnittet **Transaksjonsgebyrer** er en estimator for transaksjonsgebyrer. Jo høyere gebyrene som er allokert til transaksjonen din, desto mer sannsynlig er det at transaksjonen din blir lagt til i den neste blokken som er klar til å utvinnes.


Transaksjonsavgifter representerer kostnaden en Miner vil ta fra deg for å sette inn transaksjonen din i en kandidatblokk for Mining. Den er definert av forholdet sat/vB (Satoshi/Virtual Bytes), som representerer antall satoshier du betaler for plassen transaksjonen din vil oppta i kandidatblokken.



⚠️ VIKTIG: I tilfelle Mempool-metning, prioriterer utvinnere transaksjoner som tilbyr det beste forholdet mellom Satoshi/vByte. Jo tyngre (større) transaksjonen din er, desto flere satoshis vil den trenge for å bli inkludert raskt.



![fees-visualizer](assets/fr/03.webp)



Med **Mempool Goggles** kan du visualisere hvor mye plass en transaksjon opptar.



![mempool](assets/fr/04.webp)



En blokk utvinnes omtrent hvert tiende minutt på grunn av vanskelighetsgraden til Proof of Work som utvinnerne må levere for å legge til sin kandidatblokk i kjeden av utvunnede blokker. Denne vanskelighetsgraden varierer hver **2016 blokk**, noe som tilsvarer ca. **2 uker**. Du kan se utviklingen av denne vanskelighetsgraden her.



![difficulty](assets/fr/05.webp)



Når en ny blokk legges til i hovedkjeden, får Miner av den validerte blokken en belønning som består av en fast del (halvert hver 210 000. blokk**, noe som tilsvarer rundt 4 år** under halveringer) og transaksjonsgebyrer.



![halving](assets/fr/06.webp)



## Få tilgang til transaksjonsopplysningene dine



I søkefeltet Mempool.space kan du skrive inn din Bitcoin Address eller din transaction ID for å finne ut mer om historikken din.



![search](assets/fr/07.webp)



På siden med transaksjonsdetaljer finner du generell informasjon om transaksjonen din:




- **Status**: Bekreftet når den er lagt til i en blokk, ubekreftet når den venter i en Mempool.
- **Transaksjonsgebyrer**.
- **Anslått ankomsttid (ETA)**: Den omtrentlige tiden det vil ta før transaksjonen din blir lagt til i en blokk. Den beregnes i henhold til forholdet som utgjør avgiftene knyttet til denne transaksjonen.



![general-txinfo](assets/fr/08.webp)



I delen **Flow** vises en graf over transaksjonskomponentene dine.



Inputs (tidligere UTXO), som brukes til transaksjonen, og outputs som gir mottakerne rett til å bruke bitcoins fra hver output ved å presentere signaturen som kreves for å bruke dem.



![flow](assets/fr/09.webp)



Du finner mer informasjon om adressene som brukes, i avsnittet **Innganger og utganger**.



![address](assets/fr/10.webp)



Oppdag de ulike Bitcoin-transaksjonsordningene for å forbedre konfidensialiteten din.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Gjør transaksjonene dine raskere



I Bitcoin-økosystemet er aspektet ved transaksjonsvalidering av utvinnere uløselig knyttet til transaksjonsgebyrene knyttet til den aktuelle transaksjonen. Utvinnere prioriterer transaksjoner med et høyere gebyrforhold (satoshis/vBytes), noe som kan påvirke gyldigheten av transaksjonen din hvis du ikke betaler rimelige gebyrer som aksepteres av utvinnere. Transaksjonen din vil bli sittende fast i Mempool i påvente av en blokk som aksepterer gebyrforholdet.



Heldigvis finnes det to metoder i Bitcoin-nettverket som gjør det mulig å få bekreftelsen av transaksjonen raskere.





- **RBF** - Erstatning etter gebyr: En metode som lar deg bruke de samme posteringene som transaksjonen med lavt gebyr, men denne gangen ved å øke transaksjonsgebyret for å fremskynde valideringen. Den nye transaksjonen blir validert raskere og inkludert i en blokk, slik at transaksjonen med lav avgift blir ugyldig.



Du kan utføre en gebyrerstatning med porteføljer som godtar denne mekanismen. Se for eksempel vår artikkel om Blue Wallet-porteføljen.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: En tilnærming inspirert av RBF, men på mottakersiden. Når transaksjonen der du er mottaker, blokkeres i en Mempool, har du muligheten til å bruke utgangene (UTXO) fra denne transaksjonen, til tross for at den ennå ikke er bekreftet, ved å allokere flere gebyrer til denne nye transaksjonen, slik at de gjennomsnittlige gebyrene - for transaksjonen der du er mottaker og den initierte transaksjonen - oppmuntrer utvinnere til å inkludere begge transaksjonene i en blokk.



⚠️ Den første transaksjonen må være inkludert i en blokk for at den andre transaksjonen skal kunne bekreftes.



Hvis alle disse begrepene virker litt for tekniske, anbefaler jeg at du [konsulterer ordlisten vår](https://planb.academy/resources/glossary), som inneholder definisjoner av alle faguttrykk knyttet til Bitcoin og økosystemet.



I tillegg til disse metodene lar Mempool.space, takket være forbindelsene med over 80 % av utvinnerne i Bitcoin-nettverket, deg også akselerere alle dine **ubekreftede** transaksjoner, selv de som ikke aktiverer RBF, ved å betale et vederlag til utvinnerne i Exchange for å sette inn den rimelige transaksjonen din i neste blokk som er klar til å bli utvunnet.



Klikk på **Accelerate**-knappen på siden med transaksjonsdetaljer, og fortsett deretter med å betale motparten din til utvinnerne.



![accelerate-section](assets/fr/11.webp)


## Mindreårige



En Miner refererer til en person som administrerer en mine, dvs. en datamaskin som er engasjert i Mining-prosessen, som består i å delta i Proof-of-Work. Miner grupperer de ventende transaksjonene i sin Mempool for å danne en kandidatblokk. Deretter søker den etter en gyldig Hash, mindre enn eller lik målet, for overskriften til denne blokken ved å modifisere de ulike noncesene. Hvis han finner en gyldig Hash, sender han blokken sin til Bitcoin-nettverket og får den tilhørende økonomiske belønningen, som består av blokktilskuddet (opprettelse av nye bitcoins ex-nihilo) og transaksjonsgebyret.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

miners er som "validatorer" som verifiserer og grupperer transaksjoner i blokker. For å legge til en ny blokk i Bitcoin-nettverket må de løse et komplisert matematisk puslespill (Proof-of-Work). Den første Miner som løser gåten, vinner en Bitcoin-belønning (blokktilskudd + avgifter for transaksjoner som er inkludert i blokken).



Vanskelighetsgraden til denne Proof of Work overvåkes, slik at du kan visualisere utviklingen av datakraften som kreves for utvinnere. Du vil finne i avsnittene nedenfor :





- Et estimat av de totale belønningene som gruvearbeiderne høstet under den siste vanskelighetsjusteringen, samt estimater av den neste Halving av blokktilskuddet, som skjer hver 210 000. blokk (ca. 04 år).



![rewards](assets/fr/12.webp)



Denne vanskelighetsgraden justeres hver 2016-blokk (ca. to uker). Den er omvendt proporsjonal med den gjennomsnittlige tiden gruvearbeiderne bruker på Miner hver 2016-blokk.


Når den gjennomsnittlige tiden utvinnerne bruker mindre enn 10 minutter, øker vanskelighetsgraden, noe som viser at det var lettere for utvinnerne å validere Miner-blokker. Når gjennomsnittstiden er over 10 minutter, synker derimot vanskelighetsgraden.



![mining-pool](assets/fr/13.webp)





- Grupper av gruvearbeidere: På grunn av vanskelighetsgraden samarbeider en gruppe utvinnere om å finne Proof of Work på Bitcoin, i det vi kaller en **pool**. Når en blokk utvinnes av gruppen, fordeles belønningen i henhold til prosentandelen av suksess i hver Miners delløsningssøk, dvs. bidraget i datakraft i søket etter Proof-of-Work, eller i henhold til belønningsmetoden som er avtalt i samarbeidet.





![mining](assets/fr/14.webp)



## Lightning Network infrastruktur



Mempool gir ikke bare informasjon om Bitcoins nettverksinfrastruktur (hovedkjeden). Den integrerer også visualiserings- og utforskningsverktøy for Bitcoins Lightning-overlay.



I delen **Lightning** kan du se alle eksisterende forbindelser mellom Lightning-noder.



![network-stats](assets/fr/15.webp)



Denne Interface gir informasjon om :





- Lightning Network-statistikk.



![distribution](assets/fr/16.webp)




⚠️ **VIKTIG**: Kapasiteten til en betalingskanal angir det maksimale beløpet som en node kan sende til en annen node under en Lightning-transaksjon.





- Lynnodene allokeres i henhold til Internett-leverandør (hosting-tjeneste) og eventuelt i henhold til betalingskanalens kapasitet.



![distribution](assets/fr/17.webp)





- Historien om Lightning Networks totale kapasitet.


Du finner også en rangering av disse nodene i henhold til kapasiteten til betalingskanalene deres.



![ranking](assets/fr/18.webp)



## Mer grafikk



Mempool.space er den ideelle plattformen for interaksjon med Bitcoin-protokollnettverk. Grafene gir ikke bare visuelle data som hjelper deg med å bestemme når du skal foreta transaksjoner, men også presise parametere som gjør det mulig å visualisere styrken og helsen til Bitcoin-nettverket og tilhørende lyninfrastrukturer i sanntid.



I **Graphics**-delen kan du se viktige data om Bitcoin-nettverket:




- Utviklingen i Mempool-størrelsen: Du kan observere hvordan størrelsen på Mempool svinger, noe som kan indikere perioder med høy eller lav aktivitet i nettverket.



![graphs](assets/fr/19.webp)






- Utviklingen av transaksjoner og transaksjonsgebyrer i det valgte nettverket: Ved å spore variasjoner i transaksjoner per sekund kan du forutse perioder med overbelastning eller lav aktivitet, og optimalisere transaksjonsgebyrene dine. Denne grafen gir deg et perspektiv på nettverkets kapasitet til å håndtere transaksjonsvolumet.



![graphs](assets/fr/20.webp)



Nå som du har nådd slutten av reisen din på Mempool.space, kan du bli din egen utforsker og spore transaksjonene dine i sanntid. Nedenfor finner du vår artikkel om Bitcoin **Public Pool**-utforskeren.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1