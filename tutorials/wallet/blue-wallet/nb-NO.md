---
name: Blue Wallet

description: Bitcoin Radikalt enkel og kraftfull portefølje
---
![cover](assets/cover.webp)



Å komme i gang med Bitcoin ser ut til å være en stor utfordring for folk som er skeptiske til hvor enkelt det er å bruke det. Å finne de rette verktøyene for å sikre denne enkelheten blir derfor av avgjørende betydning for bedre adopsjon av Bitcoin som et medium for Exchange og ikke bare som et verdioppbevaringsmiddel.



I denne opplæringen skal vi ta en titt på Blue Wallet, en enkel, men svært effektiv Bitcoin Wallet som lar deg administrere bitcoinsene dine personlig og også opprette forvaltningskooperativer basert på [Multisig] (https://planb.network/resources/glossary/multisig) (ikke bekymre deg, vi kommer tilbake til det).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Kom i gang med Blue Wallet



Blue Wallet er en åpen kildekode, selvforvaltende Bitcoin Wallet som lar deg ta kontroll over bitcoinsene dine. Den er tilgjengelig som en mobilapp på både Android- og iOS-plattformer. I denne veiledningen baserer vi oss på Android-versjonen, men alle prosessene som vil bli utviklet, er like gyldige på iOS.



![download](assets/fr/01.webp)



⚠️ Sørg for å laste ned Blue Wallet Bitcoin Wallet-applikasjonen på en offisiell plattform for å garantere dens autentisitet og beskytte bitcoinsene dine mot mulige lekkasjer og hacking.



Når du har installert den, kan du opprette en ny Wallet og lagre de 12 gjenopprettingsordene, eller importere en eksisterende Bitcoin Wallet. Finn ut hvordan du lager en effektiv sikkerhetskopi av nøkkelordene dine, slik at du ikke mister tilgangen til bitcoinsene dine.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Med Blue Wallet kan du opprette separate, dedikerte Bitcoin-porteføljer. Du kan for eksempel ha en Wallet for sparing og en annen for daglige utgifter, alt i samme program.



![home](assets/fr/02.webp)



## Porteføljetyper



I Blue Wallet finner du to opprinnelige Bitcoin-porteføljetyper.



### Bitcoin-porteføljen



Hvis du er vant til andre Bitcoin-porteføljer som Phoenix eller Aqua, vil du ikke være i utakt på Interface med Blue Wallets Bitcoin-portefølje.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blue Wallets Bitcoin Wallet representerer standard Wallet i Bitcoin-økosystemet. Du kan bruke bitcoins så lenge du er i besittelse av gjenvinningsordene som gir en gyldig signatur på nettverket for å autentisere at du eier bitcoinsene.



For å opprette en Bitcoin-portefølje klikker du på knappen **Legg til nå**, skriver inn navnet på porteføljen din og velger Bitcoin-typen.



![bitcoin-wallet](assets/fr/03.webp)



Når du klikker på Bitcoin Wallet-forhåndsvisningen din, kan du se transaksjonshistorikken din og sende og motta bitcoins.



⚠️ Alle transaksjoner i Bitcoin Wallet er på Bitcoin-protokollens hovedkjede (Mainnet).





- Det er intuitivt å motta bitcoins med Bitcoin Blue Wallet Wallet. Nederst på skjermen klikker du på **Motta**-knappen. Del QR-koden eller din Bitcoin Address med avsenderen din, slik at de kan sende deg bitcoinsene.



Du kan også konfigurere et forhåndsdefinert beløp for å angi hvor mye Bitcoin du ønsker å motta.



![receive-bitcoin](assets/fr/04.webp)





- På **Send**-knappen sender du bitcoins til en Bitcoin Address, angir ønsket beløp og validerer transaksjonen.



![send-bitcoin](assets/fr/05.webp)



Med Blue Wallet kan du konfigurere parametrene til Bitcoin-forsendelsen slik du ønsker.



Du kan derfor velge den transaksjonsavgiftsratioen som passer deg hvis du ønsker at transaksjonen din raskt skal valideres i en Mempool og inkluderes i en blokk av utvinnerne. Avhengig av hvilken ratio du velger, vil utvinnerne prioritere transaksjonen din i større eller mindre grad. Finn ut mer i vår Mempool Space-veiledning.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Med Blue Wallet kan du legge til flere mottakere i én enkelt forsendelse.



Når du legger til Bitcoin Address for din første mottaker, klikker du på **Legg til mottaker** i alternativene, legger til Bitcoin Address og angir deretter beløpet som skal sendes til denne mottakeren, og så videre. Blue Wallet vil sende bitcoins for flere forsendelser basert på din enkeltstående handling.



![add-recipients](assets/fr/07.webp)



Du kan fjerne én eller alle mottakere ved å klikke på henholdsvis **Fjern mottaker** og **Fjern alle mottakere**.



![remove-recipient](assets/fr/08.webp)





- **Oppblåste gebyrer**: Har du foretatt en transaksjon som det tar lang tid å få bekreftet? Ved å aktivere gebyrinflasjon kan du legge til ekstra transaksjonsgebyrer til den ventende transaksjonen for å fremskynde bekreftelsen.



![bumping](assets/fr/09.webp)



### Multisig Portefølje



Multisig (multisignatur) Wallet representerer en Wallet som er opprettet fra grupperingen av et visst antall (minimum 2) Bitcoin-lommebøker. I denne typen Wallet, avhengig av konfigurasjonen og metoden som er valgt, blir det å bruke bitcoins en kollektiv og samarbeidende handling.



I Blue Wallet kan du opprette multisignaturporteføljer for foreningen, familien og bedriften din. I denne delen utforsker vi alle aspekter ved denne spesielle porteføljetypen.



Legg til en ny portefølje, og velg typen **Multisig Vault** for å opprette en portefølje med flere signaturer.



![multisig-vault](assets/fr/10.webp)



Definer m-de-n-konfigurasjonen i multisignaturorganisasjonen din ved å klikke på **Hvelvinnstillinger**.



⚠️ I en m-av-n-konfigurasjon representerer **m** det minste antallet signaturer som kreves for å godkjenne en transaksjon, og **n** antallet porteføljer i organisasjonen.



Sørg for å definere et minimumsantall signaturer (m) for størstedelen av organisasjonen. For eksempel krever en konfigurasjon med 2 av 3 flersignaturer at to lommebøker i organisasjonen signerer transaksjonen før den kan utføres.



det er en stor risiko å definere en m-av-n-konfigurasjon der n er lik m. Når et medlem mister tilgangen til sin Wallet, mister du autorisasjonen til å bruke bitcoins i Wallet.



Her er noen eksempler på optimale konfigurasjoner for å sikre sikkerhet og tilgjengelighet til bitcoins:





- 2-de-3 multisignatur.





- 5-de-7 multisignatur.



![vault-settings](assets/fr/11.webp)



Følg beste praksis ved å velge P2WSH-formatet.



**[P2WSH] (https://planb.network/resources/glossary/p2wsh) eller Pay to Witness Script Hash** er en låsemetode som låser transaksjonens utgående bitcoins (Outputs) til Hash i et tilpasset skript som Blue Wallet setter opp. Den største fordelen med denne typen låsing er at den reduserer størrelsen på transaksjonsdataene og implisitt lar deg betale lavere transaksjonsgebyrer.



Opprett eller importer hver av de **n** porteføljene i konfigurasjonen din. I denne veiledningen bruker vi en konfigurasjon med 2 av 3 multisignaturer. Husk å lagre gjenopprettingsordene for hver portefølje individuelt.



![vault-keys](assets/fr/12.webp)





- Motta bitcoins



På Multisig Wallet-siden finner du transaksjonshistorikken din og knappene Mottak og Send.



Å motta bitcoins i en multisignatur Wallet er den samme prosessen som når du er i en standard Bitcoin Wallet.





- Send **bitcoins**:



Ved å administrere en Wallet med flere signaturer blir det å bruke bitcoins en sammensatt handling, enten det er med andre personer eller en egen Wallet. Den enkle signaturen til din Wallet er ikke lenger tilstrekkelig. Dette gir bitcoinsene dine en Layer av sikkerhet, fordi en ondsinnet person ikke vil være i stand til å bruke disse bitcoinsene når han kommer i besittelse av bare én av dine private nøkler.



I likhet med standard Bitcoin-porteføljen til Blue Wallet kan du definere flere mottakere i alternativet **Legg til mottakere**.



Når du validerer transaksjonen din, trenger du en andre signatur for å godkjenne bruken av bitcoins. Husk at vi er i en 2-de-3 multisignaturkonfigurasjon.



Den andre Wallet-signatøren, hvis han eller hun også er en bruker, kan signere transaksjonen selv om han eller hun ikke er på Internett (ingen Wi-Fi, ingen mobildata) ved å skanne QR-koden til den [delvis signerte transaksjonen] (https://planb.network/resources/glossary/psbt) du nettopp har opprettet.



![mutisig-send](assets/fr/13.webp)





- Gå lenger med **Multi signature**-porteføljen:



Klikk på knappen **Administrer nøkler** på Interface i Wallet med flere signaturer.



Ved å glemme et av gjenopprettingsordene til en av de signerende porteføljene (**Glem denne seed...**), gir du Blue Wallet beskjed om å slette sikkerhetskopien av disse ordene fra minnet. Du vil derfor ha laget en ekstern sikkerhetskopi.



![revoke-key](assets/fr/14.webp)



Ved å utføre denne handlingen beholder du bare den offentlige nøkkelen som er knyttet til disse gjenopprettingsordene.



⚠️ Ved å beholde bare offentlige nøkler (XPUB) kan du legge til et ekstra sikkerhetsnivå i konfigurasjonen med to av tre multisignaturer. Det kan faktisk være skadelig å oppbevare alle gjenopprettingsordene på ett sted når telefonen din er under angrep. Angripere med tilgang til bare én **VAULT** (nøkkelord) som du bruker til å signere transaksjonene dine, vil ikke kunne stjele bitcoinsene dine (minimum 02 signaturer kreves) fordi offentlige nøkler ikke kan brukes til å signere transaksjoner.



## Flere alternativer med Blue Wallet



### Bedre sikkerhet for porteføljetilgang



I Innstillinger kan du under **Sikkerhet** definere bruk av et fingeravtrykk for å utføre en transaksjon, eksportere eller slette Wallet. Dette autentiserer personen som bruker smarttelefonen din.



![biometry](assets/fr/15.webp)



## Aktiver Lightning Network



Lightning Network støttes ikke lenger i Blue Wallet-applikasjonen.



I Innstillinger > **Lightning-innstillinger** kan du manuelt koble til Lightning Wallet når du kjører en Lightning Network Daemon (LND)-node. Installer LND Hub, og koble deretter til Wallet ved å angi koblingen som genereres av Hub.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Du har nå fullført den blå Wallet-turen og er klar til å bruke Bitcoin i all sin enkelhet og kraft. Vi anbefaler at du tar det neste steget og finner ut hvordan du kan akseptere Bitcoin-betalinger i butikkene dine, takket være kraften i Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06