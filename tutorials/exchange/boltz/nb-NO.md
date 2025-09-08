---
name: Boltz
description: Bytt mellom ulike Bitcoin-lag samtidig som du beholder kontrollen.
---


![cover](assets/cover.webp)



Siden lanseringen i 2009 har Bitcoins peer-to-peer-system for elektroniske kontanter vokst eksponentielt og gitt liv til løsninger som i dag gjør det mulig å bruke systemet umiddelbart i hverdagen, særlig gjennom Lightning Network.



Det gjensto imidlertid et stort problem mellom Bitcoin-protokollagene: flytende interoperabilitet. For å kunne utnytte det fulle potensialet til Bitcoin var det avgjørende å finne en løsning som muliggjorde transaksjoner mellom de ulike lagene i protokollen. Dette behovet førte i 2019 til Boltz, en bro som kobler sammen flere Bitcoin-lag.



## Hva er Boltz?



[Boltz] (https://boltz.Exchange) er en plattform som ikke er underlagt frihetsberøvelse, og som er ideell for alle som ønsker å utføre transaksjoner mellom de ulike lagene i Bitcoin-protokollen:




- on chain**: Bitcoins hovedkjede hvor transaksjoner bekreftes hvert 10. minutt i gjennomsnitt, er transaksjonsgebyrene ofte høye, noe som ikke nødvendigvis oppfyller brukernes behov;
- Lightning Network**: Bitcoin-overlegget for øyeblikkelige betalinger til lave gebyrer, slik at Bitcoin kan brukes til daglige betalinger;
- Liquid Network**: et overlegg for Bitcoin opprettet av Blockstream, som muliggjør rask, Confidential Transactions og bruk av andre Bitcoin-baserte finansielle instrumenter;
- RootStock**: En løsning for utvikling av smartkontrakter basert på Bitcoin-protokollen.



![layers](assets/fr/01.webp)



Interoperabilitet mellom disse ulike lagene er av stor betydning, ettersom det gir brukerne den fleksibiliteten de trenger for å dra full nytte av alt Bitcoin-økosystemet har å tilby.



Boltz bruker atomic swaps. Denne teknologien gjør det mulig å bytte bitcoins mellom to lag (f.eks. BTC på kjeden i Exchange mot BTC på Lightning) direkte mellom to parter, uten behov for tillit og uten behov for et mellomledd. Disse utvekslingene kalles "atomære" fordi de bare kan gi to resultater:




- Enten er Exchange vellykket, og de to deltakerne har i praksis utvekslet sine BTC ;
- Enten mislykkes Exchange, og begge deltakerne drar med sin opprinnelige BTC.



På denne måten beholder du permanent egenbeholdningen av bitcoinsene dine, og Exchange er ikke basert på tillit til motparten: Enten lykkes eller mislykkes Exchange, men ingen av partene kan stjele den andres midler.



En atomisk Exchange fungerer med smartkontrakter [HTLC] (https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). I denne typen Contract er beløpet "låst" i en toveiskanal, og det er innført en tidsbegrensning, slik at hvis transaksjonen ikke fullføres innen en viss tid, går saldoen tilbake til innskyteren. Dette er mekanismen som brukes av Boltz-plattformen.



## Dine første utvekslinger med Boltz



Boltz er en nettplattform som ikke krever noen personlig informasjon fra deg. Boltz har en minimalistisk, flytende Interface som lar deg begynne å handle på mindre enn ett minutt.



![boltz](assets/fr/02.webp)



Når du er på plattformen, kan du opprette atomutvekslinger mellom de ulike lagene i Bitcoin-økosystemet.



![home](assets/fr/03.webp)



Du vil se minimums- og maksimumsantallet satoshier (den minste enheten av Bitcoin) du kan handle via Boltz, inkludert nettverksavgifter og en prosentandel som Boltz tar mellom 0,1 % og 0,5 %.



![fees](assets/fr/04.webp)



Velg deretter Layer som du ønsker å lage en atom-Exchange fra, og velg Layer som du ønsker å motta bitcoins på.



![couches](assets/fr/05.webp)



I denne veiledningen skal vi fokusere på atom Exchange fra hoved Layer til Lightning Network.



Du kan konfigurere baseenheten for sentralene dine ved å velge mellom alternativene :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Når du har fullført de grunnleggende konfigurasjonene, setter du inn beløpet for atom-Exchange, og oppretter deretter en Lightning Invoice for tilsvarende beløp, eller bare setter inn LNURL-en din.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



For å være på den sikre siden bør du sjekke parametrene til din atomic Exchange for å eksportere sikkerhetskopinøklene som er koblet til din Exchange.



Last ned sikkerhetskopinøkkelen på ikonet **Settings** og lagre filen på riktig måte.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Denne filen inneholder de 12 nøkkelordene i porteføljen som er knyttet til atombørsen din.



Klikk deretter på knappen **Opprett atom-Exchange** og fortsett med betalingen av det angitte beløpet.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Når betalingen er utført og bekreftet, vil du automatisk motta det tilsvarende beløpet på din Lightning Wallet.



I **Refund**-menyen finner du Exchange-historikken din for å identifisere den Exchange som du ønsker å få refundert penger på. Du kan også importere en historikk over utvekslinger du har gjort på en annen enhet, for eksempel ved å bruke backupnøkkelfilen som er knyttet til disse utvekslingene.



![refund](assets/fr/11.webp)



I menyen **Historikk** kan du laste ned en mer detaljert historikk over utvekslingene som er knyttet til redningsnøkkelen din, ved å klikke på knappen **Backup**.



![backup](assets/fr/12.webp)



⚠️ Vennligst ikke gi denne filen videre heller, da den inneholder all informasjon knyttet til transaksjonene dine og sikkerhetskopinøkkelen som er knyttet til disse transaksjonene.



Boltz tilbyr deg en høy grad av konfidensialitet takket være tilgang via en `.onion`-kobling på Tor-nettverket. Gjør atomutvekslinger helt anonyme ved å velge menyen **Onion** etter at du har aktivert Tor-surfing i nettleseren din.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nå kjenner du Boltz, en unik Exchange-plattform som muliggjør interoperabilitet mellom de ulike lagene i Bitcoin-økosystemet.