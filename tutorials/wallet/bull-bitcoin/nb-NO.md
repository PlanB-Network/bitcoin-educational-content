---
name: Bull Bitcoin Wallet
description: Finn ut hvordan du bruker Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Denne veiledningen tar deg gjennom installasjon, konfigurasjon og bruk av Bull Bitcoin Mobile. Du lærer hvordan du mottar og sender penger på de tre nettverkene: onchain, Liquid og Lightning, og hvordan du overfører Bitcoin fra ett nettverk til et annet. Vedleggene inneholder ressurser og kontakter, bakgrunnsinformasjon og korte forklaringer på tekniske begreper.



## Innledning



**Bull Bitcoin Mobile**, utviklet av **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([opprett konto](https://app.bullbitcoin.com/registration/orangepeel)), er en **selvforvaltende** Bitcoin Wallet, noe som betyr at du har full kontroll over dine private nøkler og dermed dine midler, uten å være avhengig av en tredjepart. Wallet er basert på åpen kildekode og Cypherpunk-filosofien, og kombinerer enkelhet, konfidensialitet og avanserte funksjoner som nettverksbytter og PayJoin-støtte. Den lar deg administrere bitcoins på tre nettverk: **Bitcoin onchain**, **Liquid** og **Lightning**, hvert av dem skreddersydd for spesifikke bruksområder.



### Utviklingskontekst



Wallet er et svar på en stor utfordring: Bitcoin-nettverksavgifter er uegnet for små betalinger, eller for å åpne små selvbetjente Lightning-kanaler. Wallet Bull Bitcoin Mobile tilbyr en selvforvaltende løsning samtidig som den er avhengig av de tre store Bitcoin-nettverkene:





- **Bitcoin-nettverk (onchain)**: Ideell for mellom- til langtidslagring av UTXO-er og transaksjoner av stor verdi, der avgiftene er ubetydelige.
- **Liquid Network**: Utviklet for raske (~2 minutter), mer konfidensielle (skjulte beløp) og rimelige transaksjoner, perfekt for å samle små beløp eller beskytte personvernet ditt.
- **Lightning-nettverk**: Optimalisert for øyeblikkelige, rimelige betalinger, egnet for små og mellomstore daglige transaksjoner.



Med Bull Bitcoin Mobile kan du for eksempel samle små beløp i **Liquid**- eller **Lightning**-porteføljene, og når du har nådd et betydelig beløp, kan du :





- Overføring til onchain-nettverket for sikker lagring på mellomlang eller lang sikt, med forbedret konfidensialitet med Liquid og/eller Lightning oppstrøms, og med onchain-avgifter for en enkelt transaksjon



### Kontinuerlig utvikling



Wallet er i stadig utvikling, så ikke bli overrasket hvis du finner avvik mellom denne veiledningen og din oppdaterte applikasjon.




- Fra og med 19.07.2025 er for eksempel **"Kjøp / Selg / Betal"**-knappene synlige, men nedtonet i applikasjonen, ettersom disse alternativene, som er tilgjengelige på Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel), snart vil bli integrert for en enhetlig opplevelse. Bruken av dem vil forbli helt valgfri. Mange andre utviklinger er i gang eller planlagt: multi-Wallet-administrasjon, passphrase, kompatibilitet med maskinvarelommebøker ...
- På [BullBitcoin GitHub] (https://github.com/orgs/SatoshiPortal/projects/49) kan du sjekke ut aktuelle emner og kommende utvikling. Siden prosjektet er 100 % åpen kildekode og "bygget i offentligheten", kan du også sende oss forslag og eventuelle feil du støter på.




## 1. Forutsetninger



Før du begynner å bruke **Bull Bitcoin Mobile**, må du sørge for at du har følgende elementer:





- **Kompatibel smarttelefon**: En **iOS** (iPhone eller iPad) eller **Android**-enhet
- Internett-tilkobling
- **Sikre sikkerhetskopieringsmedier**: Skriv ned **gjenopprettingsfrasen** (12 ord) på papir eller metall, og oppbevar den på et trygt sted.
- **Grunnleggende kunnskap**: Et minimum av kunnskap om Bitcoin-konsepter (adresser, transaksjoner, gebyrer) er nyttig, selv om denne veiledningen forklarer hvert trinn for nybegynnere.



## 2. Installasjon





- Last ned søknaden:
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Last ned fra applikasjonsbutikken for Android-enheter**
- [GitHub] (https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Last ned APK for Android-enheter direkte**
- [iOS] (https://testflight.apple.com/join/FJbE4JPN) **Last ned via TestFlight for Apple-enheter**
 - Sjekk utviklerens navn (Bull Bitcoin) for å unngå falske applikasjoner.
 - Kontroller at den nedlastede versjonen samsvarer med den siste stabile versjonen som er angitt på GitHub.
 - Bull Bitcoin Mobile er **åpen kildekode**. For å se koden: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Installer applikasjonen




## 3. Opprinnelig konfigurasjon



### 3.1 Start programmet :



Programmet bruker en unik gjenopprettingsfrase på 12 ord for begge porteføljene:




- **sikre Bitcoin Wallet**: For transaksjoner i Bitcoin-nettverket (onchain)
- **Instant Payments' Wallet**: For øyeblikkelige transaksjoner på Liquid- og Lightning-nettverk



Når du åpner den, blir du bedt om å importere en eksisterende gjenopprettingsfrase, eller å opprette en ny Wallet :



![image](assets/fr/02.webp)



### 3.2 Gjenopprettingsfrase :



Hvis du ønsker å gjenbruke en eksisterende Wallet, klikker du på "**Gjenopprett Wallet**" og fyller inn de 12 ordene i gjenopprettingsfrasen din.



Ellers klikker du på "**Opprett ny Wallet**" :




- Skriv ned gjenopprettingsfrasen din med den største forsiktighet. Skriv den ned på papir eller metall, og oppbevar den på et trygt sted (bankboks, frakoblet sted). Denne frasen er din eneste mulighet til å få tilgang til bitcoinsene dine i tilfelle du mister enheten din eller sletter applikasjonen.
- Det er også viktig å merke seg at hvem som helst med denne frasen kan stjele alle bitcoinsene dine. Aldri lagre det digitalt:
 - Ingen skjermbilde
 - Ingen sikkerhetskopiering i skyen, e-post eller meldinger
 - Ingen kopiering/liming (risiko for lagring i utklippstavlen)



**! Dette punktet er kritisk**. For ytterligere hjelp :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Sikring av tilgang :





- Gå til innstillinger, og klikk deretter på **PIN-kode**.
- Sett opp en robust **PIN-kode** for å beskytte tilgangen til applikasjonen.
- Dette trinnet er valgfritt, men anbefales på det sterkeste for å forhindre at noen med tilgang til telefonen din får tilgang til Wallet.



![image](assets/fr/03.webp)



### 3.4 Tilkobling til en personlig node (valgfritt):



Wallet BullBitcoin kobles som standard til Electrum-servere: den første administreres av Bull Bitcoin og en sekundær server fra Blockstream, som begge anses å ikke føre noen logger, noe som reduserer risikoen for sporing.



For større konfidensialitet kan du koble applikasjonen til din egen Bitcoin-node via en Electrum-server (instruksjoner er tilgjengelige på [BullBitcoins GitHub] (https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Mottak av midler



Det er enkelt å motta penger med **Bull Bitcoin Mobile**, og det er skreddersydd til dine behov, enten du bruker :




  - **Bitcoin (onchain)**-nettverket for langsiktig bevaring,
  - **Liquid**-nettverket for raskere og mer Confidential Transactions,
  - **Lightning**-nettverket for øyeblikkelige betalinger med lav verdi.



Programmet genererer automatisk Lightning-mottak eller Invoice-adresser, avhengig av hvilket nettverk som er valgt. Slik går du frem for hvert nettverk.



### 4.1. onchain (Bitcoin-nettverk)



På startskjermen kan du :




- eller velg **Secure Bitcoin Wallet** og klikk deretter på "**Mottak"** :



![image](assets/fr/04.webp)





- eller klikk på "**Mottak"**, og velg deretter nettverket **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Alternativet "Bare kopier eller skann Address" er deaktivert (standard)



![image](assets/fr/06.webp)





- Dette gir tilgang til valgfrie avanserte parametere. Du kan spesifisere :
 - Et **beløp** i BTC, Sats eller fiat.
 - En **personlig merknad** som skal inkluderes i kopien av URI-/QR-koden.
 - Aktivering av **PayJoin** (se vedlegg 3 for mer informasjon), som forbedrer konfidensialiteten ved å kombinere avsender- og mottakeroppføringer.





- **Eksempel på en automatisk generert URI**:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Bruk**: Kopier URI-en for å dele den med avsenderen, eller la ham skanne QR-koden.



#### 4.1.2. Alternativet "Kun kopiere eller skanne Address" er aktivert



![image](assets/fr/07.webp)





- Når alternativet **"Kopier eller skann kun Address"** er aktivert, genererer programmet en enkel Bitcoin Address i SegWit (bech32)-format.





- Eksempel:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Selv om du skriver inn et beløp eller en merknad, vil de ikke bli inkludert i QR-koden eller i kopien av Address





- **Bruk**: Kopier Address for å dele den med avsenderen, eller la ham skanne QR-koden.



#### 4.1.3. Generering av en ny Address





- Hvorfor bruke en ny Address for hver transaksjon? Dette **beskytter personvernet ditt** ved å forhindre at flere betalinger blir knyttet til samme Address, og begrenser mulighetene for sporing på Blockchain.
- Som standard genererer Bull Bitcoin automatisk en ubrukt Address.
 - Du kan tvinge frem opprettelsen av en ny Address ved å klikke på **"Ny Address"** nederst på skjermen.
 - Alle adressene dine er knyttet til seed-frasen din: Uansett hvor mange adresser du bruker, vil porteføljen din vise en enkelt saldo, og kan automatisk konsolidere midler når en forsendelse blir foretatt.





- Tips: Bruk alltid den nye **Address** som leveres av Bull Bitcoin, med mindre du har et spesifikt behov (f.eks. en offentlig Address for å motta donasjoner).



### 4.2. Liquid



På startskjermen kan du :




- eller velg **Sofortbetalinger Wallet** og klikk deretter på **"Mottak"** og deretter **"Liquid"** :



![image](assets/fr/08.webp)





- eller klikk på "**Mottak"**, og velg deretter **Liquid**-nettverket:



![image](assets/fr/09.webp)



Når du er på **"Motta"**-skjermbildet, kopierer du en Liquid Address:





- Ingen beløp eller note. Eksempel:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Eller ved å spesifisere et **beløp** (i BTC, Sats eller fiat) og/eller en **personlig merknad** som skal inkluderes i kopien av URI/QR-koden. Eksempel:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Bruk**: Kopier Address/URI for å dele med avsenderen, eller la ham skanne QR-koden.



### 4.3. Lynnedslag



På startskjermen kan du :




- eller velg **Instantbetalinger Wallet** og klikk deretter på "**Mottak"** :



![image](assets/fr/10.webp)





- eller klikk på "**Mottak"**, og velg deretter nettverket **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Drift, begrensninger og fordeler





- **Mekanisme**: Bull Bitcoin Wallet er en Wallet som gjør det mulig å foreta og motta betalinger via Lightning. Midler som mottas via Lightning lagres i **Liquid**-nettverket (i Wallet Instant Payments) takket være en automatisk swap via **Boltz**. Dette gir deg muligheten til å samhandle med Lightning uten å måtte administrere likviditetskanaler, samtidig som du forblir i egen depot.





- **Grenser:**
- Et **minimumsbeløp** på 100 satoshier (per 19.07.2025) når du generate Invoice.
- Du betaler kostnadene, som trekkes fra beløpet som avsender sender, i motsetning til mottak med Wallet Lightning native, der kun avsender betaler overføringskostnadene i tillegg til beløpet som sendes. Per 19/07/2025 trekkes 47 Sats fra beløpet som sendes.





- **Fordeler**:
- **Selvforvaltende**: Midlene dine forblir under din kontroll, lagret på Liquid Network.
- **Ingen høye avgifter i kjeden**: Lagring på Liquid gjør at du unngår kostbare innskudd i kjeden for å åpne Lightning-kanalen din eller tilføre likviditet. Disse operasjonene kan utføres senere, når beløpet som er akkumulert på Liquid rettferdiggjør avgiftene.





- **Tips:** Hvis avsenderen har Wallet Bull Bitcoin, kan du bruke Liquid Network direkte for å unngå byttegebyr



#### 4.3.2. generate Invoice





- Angi et **beløp** (i BTC, Sats eller fiat)





- Legg til en **personlig merknad** som integreres i Invoice. Hvis avsenderen betaler Invoice, vil din Wallet også inkludere dette i transaksjonsdetaljene.





- **Invoice gyldighet:** Lyn Invoice er gyldig i **12 timer**. Etter denne tiden utløper den og kan ikke lenger betales. En ny Invoice må genereres.





- **Bruk**: Kopier Invoice for å dele den med avsenderen, eller la ham skanne QR-koden.




## 5. Sende midler



### 5.1. Grunnleggende prinsipp



Enten fra hjemmesiden, eller fra lommebøker :



![image](assets/fr/12.webp)



for å åpne sendeskjermen:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** gjør det enkelt å sende penger ved automatisk å oppdage nettverket (Bitcoin, Liquid eller Lightning) basert på Address eller Invoice som er angitt (kopiert eller skannet via QR-kode).



### 5.2. Onchain-overføring (Bitcoin-nettverk)



#### 5.2.1. Send-skjermen



**Aksjon**: Skriv inn eller skann en Bitcoin i kjeden Address





- Hvis beløpet ikke er definert, for eksempel :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Deretter kan du velge på send-skjermen :
 - Beløp i BTC, sat eller fiat. Minimumsbeløp: 546 satoshis den 22/07/2025.
 - En valgfri merknad for å identifisere transaksjonen. Bare synlig for deg, i transaksjonsdetaljene.



![image](assets/fr/14.webp)





- Hvis beløpet allerede er definert, for eksempel :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Du kommer da direkte til bekreftelsesskjermen nedenfor.



#### 5.2.2 Bekreftelsesskjermbilde



Ta deg tid til å sjekke alle parametere, spesielt beløp, destinasjon Address og gebyrer.


Deretter kan du justere parametrene:



![image](assets/fr/15.webp)




- **Avgifter**: Du kan velge :
- Enten vil **utførelseshastigheten** for transaksjonen din, og de tilhørende gebyrene, bli estimert
- Enten gebyrene, i modusen **Absolutte gebyrer** (totale gebyrer i satoshis) eller **Relative gebyrer** (gebyrer per byte), og hastigheten på transaksjonen din vil bli estimert





- **Avanserte innstillinger**:





- **Replace-by-fee (RBF)**: Denne funksjonen er aktivert som standard, og gjør transaksjonen raskere ved at det betales et høyere gebyr (se vedlegg 4 for mer informasjon).





- **Manuelt valg av UTXO**: Hvis midlene dine er lagret på flere forskjellige Wallet-adresser, kan du velge hvilke adresser du vil sende midlene fra. Hvorfor bør du gjøre dette? Med den økende bruken av Bitcoin stiger overføringsgebyrene. Å sende fra flere adresser med små beløp er dyrere enn å sende fra en enkelt Address, men ved å gjøre det nå unngår du å måtte gjøre det senere, når avgiftene blir enda høyere. Dette kalles **konsolidering av UTXO**.



![image](assets/fr/16.webp)





- Sending med **PayJoin**: Hvis funksjonen er aktivert av mottakeren som har oppgitt URI-en, f.eks:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Deretter konfigurerer Bull Bitcoin Mobile sendingen ved å kombinere dine UTXO-er med mottakerens UTXO-er som input, noe som forbedrer konfidensialiteten (se vedlegg 3 for detaljer).



### 5.3. Send til Liquid



#### 5.3.1 Send-skjermen



Nettverket **Liquid** muliggjør raske transaksjoner (~2 minutter takket være én blokk per minutt), mer konfidensielle (maskerte beløp) enn på onchain-nettverket, og med svært lave gebyrer. Midler tas ut fra **Instant Payments Wallet**.



**Handling**: Skriv inn eller skann en Liquid Address





- Hvis beløpet ikke er definert, for eksempel :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Deretter kan du velge på send-skjermen :




- Beløp i BTC, sat eller fiat. Ingen minimum, 1 Satoshi mulig;
- En valgfri merknad for å identifisere transaksjonen. Bare synlig for deg, i transaksjonsdetaljene.



![image](assets/fr/17.webp)





- Hvis beløpet allerede er definert, for eksempel :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Du kommer da direkte til bekreftelsesskjermen nedenfor.



#### 5.3.2 Bekreftelsesskjermbilde



Ta deg tid til å sjekke alle parametrene, spesielt mengden og destinasjonen Address.



![image](assets/fr/18.webp)





- **Gebyrer**: Proporsjonalt med transaksjonens kompleksitet, vanligvis 0,1 sat/vB, dvs. 20-40 satoshis for en enkel transaksjon (33 Sats per 22.07.2025).



### 5.4. Send til Lightning



#### 5.4.1 Send-skjermen



**Lightning**-nettverket muliggjør umiddelbare, rimelige betalinger for små beløp, noe som er ideelt for små daglige transaksjoner.



**Handling**: Skriv inn eller skann en Lightning Invoice





- Hvis du skanner en LN-URL Address som lar deg stille inn hvor mye


Eksempel: `orangepeel@walletofsatoshi.com`.


så kan du velge på send-skjermen :




 - Beløp i BTC, sat eller fiat. Minimumsbeløp på 1000 satoshis den 23/07/2025
 - En valgfri merknad for å identifisere transaksjonen. Den vil bli sendt til mottakeren.



![image](assets/fr/19.webp)





- Hvis du skanner en Lightning Invoice som inneholder en definert mengde


Eksempel:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Du kommer da direkte til bekreftelsesskjermen nedenfor.



Merk: Beløpet må være større enn 21 Sats den 23.07.2025



#### 5.4.2 Drift, begrensninger og fordeler





- **Mekanisme**: Midler trekkes fra **Instant Payments Wallet** (Liquid) og konverteres via en **Liquid → Lightning**-bytteavtale med **Boltz**.





- **Grenser:**
- Et **minimumsbeløp** høyere enn en Wallet Lightning native (se ovenfor)
- **Utgifter** pluss Liquid → Lynbytte via Boltz





- **Fordeler**:
- **Selvforvaltende**: Pengene dine forblir under din kontroll, lagres på Liquid Network og kan overføres via Lightning om nødvendig
- **Ingen høye avgifter i kjeden**: Lagring på Liquid har spart deg for kostbare innskudd i kjeden for å åpne Lightning-kanalen din eller tilføre likviditet. Disse operasjonene kan utføres senere, når beløpet som er akkumulert på Liquid rettferdiggjør avgiftene.





- **Tips:** Hvis mottakeren har Wallet Bull Bitcoin, kan du bruke Liquid Network direkte for å unngå byttekostnader



#### 5.3.3 Bekreftelsesskjermbilde



Ta deg tid til å sjekke alle parametrene, spesielt mengden og destinasjonen Address.



![image](assets/fr/20.webp)




## 6. Se historikk



**Bull Bitcoin Mobile** gjør det enkelt å spore transaksjonene dine i nettverkene **Bitcoin (onchain)**, **Liquid** og **Lightning**. Historikken kan åpnes på to måter, og viser detaljert informasjon for hver type transaksjon. Du kan også sjekke transaksjonene dine ved hjelp av eksterne blokklesere.



### 6.1. Få tilgang til historikk





- Via **startskjermen**:
 - Klikk på **Secure Bitcoin Wallet** for å se **onchain**-transaksjoner, eller på **Instant Payments Wallet** for **Liquid**- og **Lightning**-transaksjoner.
 - Historikken vises rett under porteføljetotalen, filtrert i henhold til hvilken type Wallet som er valgt.



![image](assets/fr/21.webp)





- Via den dedikerte siden:
 - Klikk på **historiesymbolet** (klokkeikon eller lignende) på startskjermen.
 - Få tilgang til en side som viser alle transaksjoner, med filtre etter type handling: **Send**, **Mottak**, **Bytte**, **PayJoin**, **Selg**, **Kjøp** (merk: Selg og Kjøp er under utvikling og er ikke tilgjengelig på nåværende tidspunkt, 20. juli 2025).



![image](assets/fr/22.webp)



### 6.2. Transaksjonsdetaljer



Hver transaksjon viser spesifikk informasjon avhengig av nettverk og type handling (sending eller mottak). Her er detaljene som er tilgjengelige for en **transaksjon i kjeden** :



![image](assets/fr/23.webp)



### 6.3. Kontroll via Block explorer



Listen over utforskere for nettverkene **Bitcoin onchain**, **Liquid** og **Lightning** finnes i vedlegg 4.



For **Lightning** er ikke transaksjoner synlige i offentlige nettlesere. Sjekk detaljer (inkludert Swap ID for Boltz) i applikasjonen.




## 7. Innstillinger



Siden "Innstillinger" kan åpnes direkte fra Bull Bitcoin-applikasjonens startside, og brukes til å konfigurere og administrere ulike aspekter ved porteføljen og brukeropplevelsen.



![image](assets/fr/24.webp)





- **Wallet Sikkerhetskopiering**: Viser porteføljens gjenopprettingsfrase for sikker sikkerhetskopiering. Se avsnitt 3. om oppretting av porteføljer for beste praksis for håndtering og lagring av gjenopprettingsfrasen.





- **Wallet Detaljer**:
- **Pubkey**: Offentlig nøkkel knyttet til Wallet, som brukes til generate Bitcoin-mottaksadresser.
- **Avledningssti**: Avledningsbane som brukes til å generate Wallet adresser fra den private nøkkelen.





- **Electrum-server (Bitcoin-node)**: Sett opp en tilkobling til en tilpasset Bitcoin-node for transaksjoner i kjeden.





- **PIN-kode**: Aktiver og/eller endre sikkerhetskoden for å beskytte tilgangen til applikasjonen og Wallet-funksjonene.





- **Valuta**: Velg om du vil vise beløp i BTC eller Sats, og standard fiat-valuta (dollar, euro osv.).





- **Innstillinger for automatisk bytte**: Med _Auto Swap_-funksjonen kan du automatisere overføringen av BTC fra **Instant Payments Wallet (Liquid)** til din **Bitcoin On-Chain** Wallet, så snart beløpet når en terskel du anser som høy nok til å rettferdiggjøre transaksjonsgebyret.





- **Logger**: Visningsbare aktivitetslogger, som kan deles med teknisk support for å lette feilsøking.





- **Telegram-tilgang for brukerstøtte**: Direkte kobling til den offisielle Telegram-kanalen for brukerstøtte.





- **Github-tilgang**: Lenke til [Bull Bitcoin Github repository] (https://github.com/SatoshiPortal) for å se åpen kildekode eller rapportere problemer.




## VEDLEGG



### A1. Forklaring av PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definisjon** :




- PayJoin, eller **Pay-to-EndPoint (P2EP)**, er en Bitcoin-transaksjonsteknikk som forbedrer konfidensialiteten i **onchain**-nettverket. Den kombinerer avsender- og mottakeroppføringer i én enkelt transaksjon, noe som gjør det vanskeligere å spore beløp og adresser.



**Operasjon:**




- I en PayJoin-transaksjon samarbeider avsender og mottaker via en kompatibel PayJoin-server for å generate en felles transaksjon.
- I stedet for at bare avsenderen bidrar med oppføringer (UTXO), bidrar mottakeren også med en av sine egne UTXO-er. Dette gjør informasjonen på Blockchain uklar: I stedet for én oppføring som tilsvarer det faktiske beløpet, er det nå to oppføringer, og utgangene gjenspeiler ikke direkte beløpet som er utvekslet.
- Den endelige transaksjonen ligner en standard Bitcoin-transaksjon (multi-input/multi-output), men skjuler det faktiske beløpet som sendes og koblingene mellom adressene takket være en steganografisk struktur.



**For bruk i Bull Bitcoin Mobile**




- **Mottak** (Address Supply): PayJoin er aktivert som standard.
- **Send**: Wallet oppdager automatisk en PayJoin URI og konfigurerer transaksjonen deretter, for eksempel:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Fordeler**




- **Forbedret konfidensialitet**: PayJoin opphever antakelsen om at alle oppføringer i en transaksjon tilhører én enkelt enhet. Med PayJoin kommer inndataene fra både avsender og mottaker, noe som bryter med denne antakelsen.
- **Maskering av beløp**: Det faktiske utvekslingsbeløpet vises ikke direkte i utdataene. Det beregnes som differansen mellom mottakerens inngående og utgående UTXO, noe som gjør analysen misvisende.



**Limits**




- PayJoin krever at avsender og mottaker bruker kompatible lommebøker, ellers brukes en standard onchain-transaksjon.
- Transaksjonen er litt mer kompleks (flere innganger og utganger), noe som fører til litt høyere kostnader.
- Selv om den er utformet for å ligne en standardtransaksjon, kan avanserte heuristikker (f.eks. tvetydige utdata, kjente PayJoin-servere) føre til at man mistenker at den brukes, selv om det ikke er helt sikkert.



**Mer info:**




- [Ordliste] (https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Forklaring av Replace-by-fee (RBF)



**Definisjon**: Replace-by-fee (RBF) er en funksjon i Bitcoin-nettverket som gjør det mulig for avsenderen å fremskynde bekreftelsen av en **onchain**-transaksjon ved å godta å betale en høyere avgift.



**Grenser** :




- RBF er ikke tilgjengelig for Liquid eller Lightning-transaksjoner.
- Den første transaksjonen må merkes som RBF-kompatibel når den opprettes, noe Bull Bitcoin Mobile gjør automatisk med mindre den er deaktivert.



**Mer info:**




- [Ordliste] (https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Beste praksis



Følg disse anbefalingene for å bruke **Bull Bitcoin Mobile** sikkert og effektivt. De vil hjelpe deg med å beskytte pengene dine, optimalisere transaksjonene dine og bevare konfidensialiteten din på **Bitcoin (onchain)**, **Liquid** og **Lightning**-nettverkene.





- **Sikre gjenopprettingsfrasen din**:
 - Veiledning: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Bruk sikker autentisering:
 - Aktiver en **sterk PIN-kode** eller **biometrisk autentisering** (fingeravtrykk eller ansiktsgjenkjenning) for å beskytte tilgangen til applikasjonen.
 - Del aldri PIN-koden eller biometriske data.





- **Beskytt personvernet ditt**:
 - generate en ny Address for hvert mottak i kjeden eller Liquid for å begrense sporing på Blockchain.
 - Bruk PayJoin når det er tilgjengelig for å øke konfidensialiteten når det gjelder mengden som sendes videre i kjeden
 - For maksimal konfidensialitet bør du koble Wallet til din egen Bitcoin-node via en Electrum-server i stedet for å bruke den offentlige noden





- Velg det nettverket som passer best til dine behov:
- **Onchain**: Foretrukket for langsiktig oppbevaring eller transaksjoner av store verdier (gebyrene er ubetydelige i forhold til beløpet).
- **Liquid**: Brukes til raske, rimelige overføringer med forbedret konfidensialitet.
- **Lyn**: Velg øyeblikkelige, rimelige overføringer for små beløp. Hvis du er to Wallet Bull Bitcoin-brukere, velger du Liquid for å unngå byttegebyr for Lightning <> Liquid via Boltz.





- **Kontroller alltid leveringsadresser**:
 - Før du sender penger, må du kontrollere Address nøye. Midler som sendes til feil Address, er tapt for alltid. Bruk kopier/lim inn eller QR-kodeskanning, og kopier/endr aldri en Address for hånd.





- **Optimaliser kostnadene**:
 - For transaksjoner i kjeden velger du passende gebyrer (treg, middels, rask) i henhold til hvor mye det haster og hvor overbelastet nettverket er.
 - Bruk Liquid, eller Lightning for små mengder.
 - Aktiver Replace-by-fee (RBF) (se vedlegg 4) for kjedeforsendelser hvis du forventer et behov for raskere bekreftelse.





- Hold søknaden oppdatert




### A4. Ytterligere ressurser





- **Offisielle lenker og support:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : support e-post
- [Bull Bitcoin offisielle nettsted](https://bullbitcoin.com/): **Informasjon om Bull Bitcoin-tjenester, kontooppretting, tilgang til applikasjonen**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Se kode, utvikling og veikart, bidra til utvikling ...**
- [Konto X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- **Telegram-gruppe** for Wallet mobil: gruppechat med support, se siden "Innstillinger".





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lyn: **[1ML (Lightning Network)](https://1ml.com/)**





- Læring og veiledning:** ** **[Plan ₿ Network](https://planb.network/)** :
 - Sikre gjenopprettingsfrasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Ordliste](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Ordliste](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Oversikt over selskapet



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, er den eldste Exchange-plattformen uten depot som utelukkende er dedikert til Bitcoin, grunnlagt i 2013 på Bitcoin-ambassaden i Montreal, Canada. Selskapet ledes av Francis Pouliot, en anerkjent pioner i Bitcoin-økosystemet, og posisjonerer seg som en sentral aktør i arbeidet med å fremme økonomisk suverenitet og brukerautonomi. Selskapets mål er å gjøre det mulig for enkeltpersoner å gjenvinne kontrollen over pengene sine ved å bruke Bitcoin som et verktøy for frihet og betaling, samtidig som de avviser fiat-valutaer og andre kryptovalutaer enn Bitcoin.



![image](assets/fr/26.webp)



[Opprett konto] (https://app.bullbitcoin.com/registration/orangepeel) med 0,25 % rabatt på kjøp og salg av Bitcoin.



#### Verdier og filosofi



Bull Bitcoin skiller seg ut med sine Commitment- til Cypherpunk-prinsipper og Bitcoin-etikk:





- **Eksklusivt fokus på Bitcoin**: Plattformen er tro mot visjonen om en desentralisert, sensurresistent valuta.





- **Ikke-forvalter**: Brukerne beholder full kontroll over sine Bitcoins ved å sende midler til sine egne porteføljer.





- **Konfidensialitet**: Minimert innsamling av personopplysninger, med KYC-frie kjøpsalternativer for transaksjoner under 999 USD. Dataene er beskyttet i samsvar med regelverket (FINTRAC i Canada, AMF i Frankrike).





- **Åpenhet**: Ingen skjulte gebyrer, kostnadene er inkludert i spreaden (forskjellen mellom kjøps- og salgspris).





- **Finansiell suverenitet**: Bull Bitcoin fremmer uavhengighet fra tradisjonelle banksystemer og sentraliserte institusjoner.



#### Viktigste tjenester





- **Fiat-innskudd**: Brukere kan sette inn penger på Bull Bitcoin-kontoen sin med fiat-valuta (CAD, EUR osv.) via bankoverføring eller kontanter/debetkort på utvalgte kanadiske postkontorer.





- **Kjøp av Bitcoin**: Brukere kan kjøpe Bitcoin som sendes direkte til deres ikke-depotportefølje, noe som garanterer total kontroll over midlene deres.





- **Planlagt kjøp av Bitcoin**: Bull Bitcoin tilbyr en automatisert, tilbakevendende kjøpstjeneste (DCA - Dollar Cost Averaging) med jevne mellomrom, som trekker på din tilgjengelige saldo, med direkte overføring av Bitcoins til en brukerkontrollert Wallet, noe som reduserer virkningen av prisvolatilitet.



Merk at et alternativ kalt "AutoBuy" lar deg konvertere fiats så snart de berører Bull Bitcoin-saldoen din, og sende Bitcoins til din egen Wallet. Dette alternativet kan også kombineres med en tilbakevendende bankoverføring som er planlagt med banken din for å foreta en DCA. Dette alternativet automatiserer Bitcoin-akkumuleringen din uten at du noen gang trenger å åpne applikasjonen.






- Kjøp Bitcoin til en fast pris **'Limit Order'**: Lar deg kjøpe Bitcoin til en pris som er spesifisert på forhånd av brukeren, og som automatisk utføres når Bull Bitcoin-indeksens pris når eller faller under den angitte grensen.





- **Selge Bitcoin**: Brukere kan selge sine Bitcoins og motta pengene i fiat-valuta direkte inn på bankkontoen sin via bank- eller SEPA-overføring.





- **Tredjepartsbetalinger**: Bull Bitcoin gjør det mulig for brukere å sende fiat-penger til bankkontoer fra sine Bitcoins, helt transparent for mottakeren.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime er en premiumtjeneste for velstående kunder og bedriftskunder, og tilbyr tilpassede løsninger og premium support. Dette inkluderer tilgang til reduserte gebyrer, en dedikert kontoadministrator og skreddersydde bedriftstjenester. Denne tjenesten er rettet mot institusjoner, profesjonelle tradere og bedriftskunder som ønsker inngående ekspertise og prioritert behandling.





- **Mobil Wallet**: Bull Bitcoin tilbyr en åpen kildekode, selvforvaltende mobil Wallet, tilgjengelig på Android og iOS, som støtter onchain-, Liquid- og Lightning Network-transaksjoner.





- **Pedagogisk støtte**: Gratis veiledninger og personlig veiledning for å hjelpe brukerne med å opprette, sikre og administrere Bitcoin-porteføljene sine, noe som styrker den økonomiske selvstendigheten.



#### Samsvar og sikkerhet





- **Regulatorisk**: Bull Bitcoin er registrert hos FINTRAC (Canada) og AMF (Frankrike) og oppfyller KYC/AML-kravene.





- **Sikkerhet**: Bruk av sikre porteføljer og anbefalinger om offline-lagring. Personopplysninger lagres på Bulls Bitcoin-infrastruktur, som er 100 % selvdrevet og ikke er avhengig av noen tredjepart.