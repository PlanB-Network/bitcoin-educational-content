---
name: Wallet of Satoshi - Selvforvaring
description: Finn ut hvordan du konfigurerer selvforvaringsmodus for en Wallet of Satoshi-portefølje
---

![cover](assets/cover.webp)



***Not your keys, not your coins* er mer enn et ordtak, det er et grunnleggende prinsipp i Bitcoin, som betyr at hvis du ikke kontrollerer de **private nøklene** som låser opp bitcoinsene dine, eier du dem egentlig ikke.



Mange brukere starter vanligvis med en **custodial wallet**, og migrerer deretter til en **self-custodial wallet**, der de kontrollerer de private nøklene sine selv.


I denne veiledningen vil vi ikke introdusere deg for en ny wallet med selvforvaring. I stedet skal vi introdusere deg for en ny funksjon i ***Wallet of Satoshi*** wallet: **den selvforvaringsmodusen**.



Målet med den nye integrasjonen er å gjøre det mulig for brukerne å beholde kontrollen over sine private nøkler, samtidig som de får en enkel og smidig brukeropplevelse.



Før vi går til sakens kjerne, la oss ta et øyeblikk til å undersøke den spesielle selvforvaringsmodusen som tilbys av Wallet of Satoshi (WoS).



## Det spesielle med selvforvaringsmodus



WoS' enkle og smidige selvforvaltningsmodus eliminerer kompleksiteten ved å åpne Lightning-kanaler, administrere noder... Men hvordan er dette mulig?



Wallet of Satoshis selvoppbevaringsmodus drives av **Spark**. Dette er en Layer 2-løsning for Bitcoin, laget av Lightspark, ved hjelp av **statechains**-teknologi.



Derfor utfører du ikke transaksjonene dine direkte på Lightning Network. Interaksjoner mellom **LN**-nettverket og **Spark** skjer via **atomiske bytter**.



Bob ønsker for eksempel å betale en Lightning-faktura ved hjelp av WoS. Han overfører sine satoshi, men i bakgrunnen rutes disse til en **Spark Service Provider (SSP)** på Spark, som i sin tur utfører betalingen på Lightning-nettverket.



Alice ønsker derimot å få midler direkte fra WoS-porteføljen sin. I dette tilfellet mottar **SSP** sats via LN og krediterer umiddelbart Alices portefølje.



Så det er viktig å merke seg at for å dra nytte av enkelheten og smidigheten i WoS, må du være avhengig av Sparks servere. Når det gjelder sikkerhet, hvis en SSP blir ondsinnet eller utilgjengelig, har du imidlertid **unilateral exit**-mekanismen, et sikkerhetstiltak som lar deg gjenopprette midlene dine på Bitcoin on-chain (selv om dette kan være tregt og kostbart) , noe som garanterer en selvforvaringsopplevelse som kan sammenlignes med den for en privat Lightning-node.



Når du tar hensyn til alle disse parameterne, kan du bestemme hvor mye sats du ønsker å ha i WoS-selvbevaringen din.



Hvis du er ny i Wallet of Satoshi, må du naturligvis laste ned den mobile wallet-applikasjonen. Hvis du allerede bruker den og ønsker å vite hvordan du bruker **selvforvaringsmodus**, kan du gå direkte til delen **Selvforvaringsmoduskonfigurasjon** i denne veiledningen.



## Kom i gang med Wallet of Satoshi



Gå til applikasjonsbutikken din og last ned WoS.



![screen](assets/fr/03.webp)



Åpne programmet når nedlastingen er fullført, og trykk på **Start**.



![screen](assets/fr/04.webp)



Du vil bli omdirigert til programmets hovedgrensesnitt. Når du åpner WoS for første gang, er porteføljen faktisk allerede funksjonell og åpnes systematisk i depotmodus som standard.



![screen](assets/fr/05.webp)



Selv om du ikke ønsker å bruke WoS i custodial-modus, anbefaler vi at du konfigurerer den først. Se denne veiledningen for å gjøre det.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

La oss gå videre til konfigurasjonen av WoS i egen forvaring.



## Konfigurasjon av selvforvaringsmodus



Klikk på hamburgermenyen (ikonet med tre stolper) øverst til høyre i hovedgrensesnittet.



![screen](assets/fr/06.webp)



Klikk deretter på undermenyen **Åpne Self Custody Wallet** i menyen som vises.



![screen](assets/fr/07.webp)



WoS forteller deg umiddelbart at *selvforvaringsmodus kommer med en gjenopprettingsfrase. Du er også eneansvarlig for sikkerheten til midlene dine*.



![screen](assets/fr/08.webp)



Kryss av for "**Jeg forstår**"-knappen (1), og trykk deretter på **Åpne Self Custody Wallet**-knappen (2), som vises i lysegult.



![screen](assets/fr/09.webp)



### Opprettelse av en portefølje for selvforvalting



Når du har klikket på knappen **Åpne Wallet**, klikker du på knappen **Opprett en ny Wallet**.



![screen](assets/fr/10.webp)



WoS oppretter deretter en portefølje for selvforvaring for deg, igjen i samme applikasjon. Du kan når som helst veksle mellom **forvaltningsmodus** (tilgjengelig i visse regioner) og **selvforvaltningsmodus** når det passer deg.



![screen](assets/fr/11.webp)



Når du har opprettet en WoS-portefølje, blir du omdirigert til WoS' hovedgrensesnitt for selvforvaring. Du vil legge merke til at det ikke er noen forskjeller mellom den generelle oversikten og grensesnittene for en WoS custody-portefølje og en WoS self custody-portefølje.



### Lagre minnefrasen din



Trykk på ikonet **Nøkkelring + Backup Wallet** øverst på skjermen mellom Wallet of Satoshi-navnet og hamburgermenyen.



![screen](assets/fr/12.webp)



WoS tilbyr to forskjellige måter å lagre dine 12 ord (huskeregel) på: **sikkerhetskopiering via Google Disk** og **manuell sikkerhetskopiering**.



Selv om vi anbefaler manuell sikkerhetskopiering, som er det sikreste, viser vi deg også hvordan du tar sikkerhetskopi via Google Disk.



#### Sikkerhetskopiering via Google Disk



Klikk på knappen **Google Drive Backup**.



![screen](assets/fr/13.webp)



Hvis du velger å ta sikkerhetskopi med Google Disk, er det stor risiko for at Google-kontoen din blir kompromittert. En ondsinnet person vil ha tilgang til filen som inneholder de 12 ordene dine, og kan dermed få tilgang til wallet.



Å legge til et passord for å kryptere filen som inneholder de 12 ordene dine, er absolutt en god måte å legge til et ekstra sikkerhetslag på.



Aktiver derfor **Krypter med passord**-knappen i de avanserte alternativene.



![screen](assets/fr/14.webp)



I det nye grensesnittet som vises, angir du et sterkt passord og bekrefter det igjen.



![screen](assets/fr/15.webp)



Det er viktig å huske at når du har valgt et passord, må du ikke glemme det eller miste mediet du har skrevet det på. Hvis du glemmer eller mister det, vil du aldri mer få tilgang til dine 12 ord, og dermed heller ikke til pengene dine.



Når du har valgt passord, velger du en Google-konto for sikkerhetskopien, og gir deretter tilgangene som kreves av WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Vent noen sekunder. Bingo! Sikkerhetskopieringen er fullført.



![screen](assets/fr/18.webp)



Du har alltid muligheten til å ta en ekstra sikkerhetskopi ved å velge den andre sikkerhetskopimetoden: manuell sikkerhetskopiering.


#### Manuell sikkerhetskopiering



Hvis du velger manuell sikkerhetskopiering, anbefaler vi på det sterkeste at du leser denne veiledningen, som tar for seg de beste fremgangsmåtene for å sikkerhetskopiere minnefrasen din på en sikker måte, slik at du ikke mister tilgangen til bitcoinsene dine.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trykk på knappen **Manual Backup**.



![screen](assets/fr/19.webp)



I det følgende grensesnittet minner WoS deg på noen sikkerhetsregler du må ta hensyn til før du fortsetter med den manuelle sikkerhetskopieringen.



Aktiver **Jeg forstår**-knappen, og trykk på **Neste**-knappen.



![screen](assets/fr/20.webp)



Du vil da få opp dine 12 ord. Lagre dem, og klikk deretter på **Neste**-knappen.



![screen](assets/fr/21.webp)



I det nye grensesnittet trykker du på ordene i riktig rekkefølge.



![screen](assets/fr/22.webp)



Til slutt klikker du på knappen **Neste**. Vi gratulerer deg! Sikkerhetskopieringen er nå fullført.



![screen](assets/fr/23.webp)



## Gjenoppretting av portefølje i egenregi



Når du ønsker å gjenopprette eller gjenopprette WoS self-custody wallet etter et telefonbytte eller av andre grunner, kan du følge disse trinnene.



Du åpner WoS-porteføljen ved å klikke på hamburgermenyen øverst til høyre i hovedgrensesnittet.


I menyen som vises, klikker du på undermenyen **Åpne Self Custody Wallet**.


I det nye grensesnittet som vises, trykker du på knappen **Restore Existing Wallet**.



![screen](assets/fr/24.webp)



Velg en gjenopprettingsmetode og fortsett til neste trinn.



![screen](assets/fr/25.webp)



### Gjenopprett via Google Disk



1. Trykk på knappen **Gjenopprett fra Google Disk**.


2. Velg en Google-konto og la WoS hente gjenopprettingsdataene som er lagret på Google Disk.


3. Skriv deretter inn krypteringspassordet ditt (hvis du har definert det tidligere, selvfølgelig) fra filen med de 12 ordene.


4. Vent et øyeblikk før gjenopprettingen trer i kraft, og du vil få tilgang til porteføljen din igjen.



### Manuell restaurering



1. Trykk på knappen **Gjenopprett manuelt**.


2. Skriv deretter inn de 12 ordene i minnefrasen din, og skriv hvert ord foran startnummeret.


3. Vent et øyeblikk før gjenopprettingen trer i kraft, og du vil få tilgang til porteføljen din igjen.




### Overføring av bitcoins mellom WoS-depot og WoS-selvdepot



Når du har bitcoins (sats) i WoS-depotet ditt wallet og oppretter et WoS-selvdepot wallet, vil du ikke miste pengene dine. Enda bedre, du kan overføre dem til din egenbeholdningsportefølje og vice versa.



For å gjøre det :


Du kan kopiere WoS' lynadresse eller en faktura du selv har opprettet.



![screen](assets/fr/26.webp)



Nå åpner du din varetekt wallet og trykker på **Envoyer**-knappen.



Lim deretter inn adressen eller fakturaen. Trykk på **Envoyer** en gang til.



Gå tilbake til din egenbeholdningsportefølje, og du vil se at du faktisk hadde mottatt midlene.



![screen](assets/fr/27.webp)



## Sende og motta bitcoins



Når det gjelder sending og mottak av bitcoins i selvforvaringsmodus, akkurat som den generelle oversikten og grensesnittene, er de ikke forskjellige fra å sende og motta bitcoins via en WoS-depot wallet.



Se den grunnleggende veiledningen om bruk av Wallet of Satoshi på Plan₿ Network.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Du kan nå konfigurere og betjene Wallet of Satoshi selv i selvforvaringsmodus.



Hvis du fant denne opplæringen nyttig, vennligst la meg en grønn tommel nedenfor. Tusen takk skal du ha!