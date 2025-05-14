---
name: Trezor Shamir Backup
description: Mnemonic-setninger på Trezor med én eller flere aksjer
---
![cover](assets/cover.webp)



*Bildekreditt: [Trezor.io](https://trezor.io/)*



## Nye alternativer for sikkerhetskopiering på Trezor



Siden 2023 har Trezor tilbudt et nytt sikkerhetskopieringsformat kalt ***Single-share Backup***, som gradvis erstatter den klassiske BIP39-baserte tilnærmingen som finnes på de fleste porteføljer. I motsetning til tradisjonelle Mnemonic-fraser på 12 eller 24 ord, er dette nye formatet basert på en enkelt frase på 20 ord som stammer fra en standard utviklet av SatoshiLabs: **SLIP39**. Målet er å gjøre sikkerhetskopieringen mer robust og lesbar, samtidig som det muliggjør en smidig overgang til en distribuert sikkerhetskopimodell.



Denne distribuerte modellen kalles ***Multi-share Backup***. Den er basert på samme prinsipp, men i stedet for å generere en enkelt Mnemonic-frase, deler den den opp i flere fragmenter kalt ***shares***, som hver for seg er en egen Mnemonic-frase. For å gjenopprette porteføljen må et visst antall av disse *andelene* (definert av en *terskelverdi*) gjenforenes. I en 3-av-5-ordning vil for eksempel 3 *aksjer* av de 5 gjenopprette porteføljen. Vær oppmerksom på at Trezors distribuerte backup-system er forskjellig fra Multisig-lommebøker. For å bruke bitcoins er det kun Hardware Wallet Trezor som kreves. Bare én signatur er nødvendig. Distribusjon gjelder bare på nivået av Mnemonic-frasen, dvs. sikkerhetskopien.



![Image](assets/fr/01.webp)



Dette systemet løser problemet med Mnemonic-frasenes enkeltfeilpunkt uten ulempene forbundet med å administrere en Multisig eller passphrase BIP39. Gjenopprettingsprosessen er ikke lenger basert på én enkelt opplysning, men på flere, med den ekstra fordelen at terskelen gir toleranse for tap.



Brukere som har opprettet en portefølje med *Single-share Backup*, kan når som helst bytte til *Multi-share Backup* uten å måtte migrere porteføljen sin. Mottaksadresser og kontoer forblir identiske. Systemet *Multi-share* påvirker kun sikkerhetskopien, mens resten av porteføljen forblir uendret.



Multi-share Backup* er tilgjengelig på Trezor Model T, Safe 3 og Safe 5. Denne funksjonen støttes ikke av Trezor Model One.



**Viktig merknad:** Trezors *Multi-share*-system er kryptografisk sikkert, ettersom det bruker *Shamirs Secret Sharing*-ordning for distribusjon. Vi fraråder på det sterkeste å bruke et lignende system manuelt, ved å dele en klassisk Mnemonic-frase selv. Det er en dårlig praksis som øker risikoen for tyveri og tap av bitcoins betydelig, så ikke gjør det. En klassisk Mnemonic-frase lagres i sin helhet.



## Shamirs hemmelige deling i SLIP39



Den kryptografiske mekanismen som ligger til grunn for *Multi-share*-sikkerhetskopier på Trezor, er *Shamir's Secret Sharing Scheme* (SSSS). Prinsippet er som følger: Hemmelig informasjon (i dette tilfellet porteføljens seed) omdannes til et matematisk polynom. Deretter beregnes flere punkter i dette polynomet, og hvert av dem blir en andel. Den opprinnelige hemmeligheten rekonstrueres ved hjelp av polynomisk interpolasjon, ved å samle et minimumsantall punkter (terskelen).



Ingen hemmelig informasjon kan utledes fra et antall aksjer under terskelen, noe som garanterer perfekt teoretisk sikkerhet for den hemmelige informasjonen. Med andre ord kan selv en angriper med ubegrenset datakraft ikke gjette seed hvis terskelen ikke er nådd.



SLIP39 bruker denne ordningen for å distribuere seed-porteføljen. Hver andel er en setning på 20 ord, bygget opp fra en liste på 1024 ord (forskjellig fra BIP39-listen).



## Sette opp en sikkerhetskopi med flere delinger på en Trezor



Når du oppretter porteføljen din på Trezor, har du tre ulike alternativer:




- Bruk en klassisk BIP39 Mnemonic-frase med 12 eller 24 ord;
- Bruk en Mnemonic-frase med én deling (SLIP39);
- Konfigurer flere Mnemonic-fraser i Multi-share (SLIP39).



Hvis du velger en Single-share SLIP39 Mnemonic-frase, vil du kunne oppgradere til en Multi-share på et senere tidspunkt uten å måtte tilbakestille porteføljen. Hvis du derimot starter med en klassisk BIP39-portefølje (12- eller 24-ordsfrase), vil du ikke kunne konvertere den direkte til en Multi-share. Du må opprette en ny Multi-share-portefølje fra bunnen av og overføre midlene dine fra den gamle porteføljen til den nye via en eller flere Bitcoin-transaksjoner. Dette er en mer kompleks og kostbar operasjon. Hvis du ønsker å gjøre denne migreringen, anbefaler jeg at du kjøper en ny Hardware Wallet Trezor for å unngå å måtte legge inn seed i et porteføljeprogram.



I denne veiledningen skal vi først se på hvordan du setter opp en Multi-share når du oppretter en portefølje, og deretter skal vi se hvordan du konverterer en Single-share til en Multi-share i en eksisterende portefølje.



Hvis du trenger hjelp med det første oppsettet av enheten din, har vi også en detaljert veiledning for hver Trezor-modell:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### På en ny portefølje



Du har nå fullført den innledende konfigurasjonen av Trezor og er klar til å opprette porteføljen. I Trezor Suite klikker du på knappen "*Opprett ny Wallet*".



![Image](assets/fr/02.webp)



Velg alternativet "*Multi-share Backup*", og klikk deretter på "*Create Wallet*".



![Image](assets/fr/03.webp)



Godta vilkårene for bruk på Trezor og bekreft opprettelsen av porteføljen.



![Image](assets/fr/04.webp)



I Trezor Suite klikker du på "*Fortsett å sikkerhetskopiere*".



![Image](assets/fr/05.webp)



Les instruksjonene nøye, bekreft dem, og klikk deretter på "*Create Wallet backup*".



![Image](assets/fr/06.webp)



Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer Mnemonic-fraser på riktig måte, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

På Trezor velger du det totale antallet aksjer du ønsker å konfigurere. De vanligste konfigurasjonene er 2-de-3 og 3-de-5. I dette eksemplet vil jeg opprette en 2-de-3, så jeg velger 3 delinger. Hver deling vil representere en Mnemonic-frase på 20 ord.



*For Safe 5-brukere vil det stå "*Trykk for å fortsette*" på skjermen, men du må faktisk sveipe opp for å bekrefte



![Image](assets/fr/07.webp)



Bekreft deretter terskelen, dvs. antall aksjer som kreves for å få tilgang til Wallet og bitcoinsene den inneholder.



![Image](assets/fr/08.webp)



Trezor oppretter de ulike aksjene dine (Mnemonic-fraser) ved hjelp av en tilfeldig tallgenerator. Forsikre deg om at du ikke blir overvåket under denne operasjonen. Skriv ned ordene som vises på skjermen, på det fysiske mediet du ønsker. Det er viktig at ordene er nummererte og i rekkefølge.



Jeg anbefaler at du noterer ned hver deling på et separat medium og administrerer lagringen nøye for å unngå at flere er tilgjengelige på samme sted. For en 2-av-3-konfigurasjon som min, kan det for eksempel være et alternativ å oppbevare én del hjemme hos meg, en annen hos en betrodd venn og den siste i en banksafe. Valget av oppbevaringssteder avhenger av din personlige sikkerhetsstrategi.



Øverst på skjermen kan du se hvilken deling du ser på for øyeblikket.



du må selvfølgelig aldri dele disse ordene på Internett, slik jeg gjør i denne veiledningen. Dette eksemplet Wallet vil bare bli brukt på Testnet og vil bli slettet på slutten av opplæringen.**_



![Image](assets/fr/09.webp)



Klikk nederst på skjermen for å gå videre til neste ord. Du kan gå bakover ved å skyve nedover. Når du har skrevet ned alle ordene, holder du fingeren på skjermen for å gå videre til neste del, og gjentar operasjonen.



![Image](assets/fr/10.webp)



På slutten av hvert delingsopptak blir du bedt om å velge ordene i Mnemonic-frasen for å bekrefte at du har skrevet dem ned på riktig måte.



![Image](assets/fr/11.webp)



Og det var det, du har sikkerhetskopiert porteføljen din ved hjelp av Multi-share-alternativet. Du kan nå fortsette med resten av konfigurasjonsinstruksjonene.



### På en eksisterende portefølje av enkeltaksjer



Hvis du allerede har en Trezor Wallet med en single-share-sikkerhetskopi (en SLIP39 Mnemonic-frase, ikke den klassiske BIP39-frasen), og ønsker å forbedre tilgjengeligheten og sikkerheten til Wallet-sikkerhetskopien din, kan du sette opp et multi-share-system uten å måtte overføre bitcoinsene dine.



Dette gjør du ved å koble til og låse opp Hardware Wallet. Gå til Innstillinger i Trezor Suite.



![Image](assets/fr/12.webp)



Gå til fanen "*Enhet*".



![Image](assets/fr/13.webp)



Klikk deretter på "* Opprett sikkerhetskopi med flere delinger*".



![Image](assets/fr/14.webp)



Les instruksjonene, og klikk deretter på "*Create Multi-share Backup*".



![Image](assets/fr/15.webp)



Deretter må du skrive inn din nåværende Mnemonic-frase (single-share) på Trezor-skjermen. Velg antall ord (standard er 20).



![Image](assets/fr/16.webp)



Bruk deretter Trezors tastatur på skjermen til å skrive inn hvert ord i den aktuelle Mnemonic-frasen.



![Image](assets/fr/17.webp)



Deretter kan du velge konfigurasjon for Multi-share Backup ved å følge instruksjonene i forrige avsnitt.



![Image](assets/fr/18.webp)



Når du har opprettet Multi-share Backup, må du bestemme hva du skal gjøre med den opprinnelige Single-share Mnemonic-frasen. Ettersom Bitcoin-porteføljen forblir den samme, vil denne enkeltfrasen alltid gi tilgang til den. Dette avhenger av sikkerhetsstrategien din, men generelt anbefales det å destruere denne frasen for å eliminere dette eneste feilpunktet, som nettopp er målet med Multi-share Backup. Hvis du bestemmer deg for å ødelegge den, må du sørge for at du gjør det på en sikker måte, da **den fremdeles gir tilgang til bitcoins**.



Gratulerer, du er nå oppdatert på bruken av Single-share- og Multi-share-sikkerhetskopier på Trezor-maskinvare-lommebøker. Hvis du ønsker å ta Wallet-sikkerheten et skritt videre, kan du ta en titt på denne veiledningen om BIP39-passordfraser:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Hvis du fant denne opplæringen nyttig, ville jeg være takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!



## Ytterligere ressurser





- [SLIP-0039: Shamirs hemmelighetsdeling for Mnemonic-koder] (https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup på Trezor] (https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamirs hemmelige deling] (https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).