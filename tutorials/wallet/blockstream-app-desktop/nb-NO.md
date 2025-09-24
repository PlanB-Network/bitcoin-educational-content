---
name: Blockstream App - Desktop
description: Hvordan bruker du Hardware Wallet med Blockstream-appen på en datamaskin?
---
![cover](assets/cover.webp)



## 1. Innledning



### 1.1 Mål for opplæringen





- Denne veiledningen forklarer hvordan du bruker **Blockstream-appen** på en datamaskin til å administrere en Bitcoin **onchain** Wallet med en **Hardware Wallet**, noe som muliggjør sikre transaksjoner som er registrert på hoved-Blockchain Bitcoin.
- Den dekker installasjon, innledende konfigurasjon, tilkobling av en Hardware Wallet og mottak og sending av bitcoins i kjeden.
- Merk: Andre veiledninger i vedleggene dekker Liquid, Watch-Only og mobilapplikasjonen.



### 1.2 Målgruppe





- **Nybegynnere**: Brukere som ønsker å administrere sine bitcoins med sikker skrivebordsprogramvare og en Hardware Wallet.
- **Brukere på mellomnivå**: Personer som ønsker å forstå hvordan man bruker en Hardware Wallet for transaksjoner i kjeden og personvernalternativer som Tor eller SPV.



### 1.3. Bakgrunn om maskinvarelommebøker





- **Hardware Wallet**, **Cold Wallet**: En fysisk enhet som lagrer private nøkler offline, noe som gir et høyt sikkerhetsnivå mot cyberangrep, i motsetning til **Hot-lommebøker** (programvarelommebøker på tilkoblede enheter).
- **Anbefalt bruk**:
    - Ideell for å sikre store beløp eller langsiktig sparing.
    - Passer for sikkerhetsfokuserte brukere som ønsker å beskytte pengene sine mot risikoen forbundet med tilkoblede enheter.
- **Begrensninger**: Krever programvare som Blockstream App for å vise saldoer, generate-adresser og kringkaste Hardware Wallet-signerte transaksjoner.



## 2. Vi presenterer Blockstream-appen





- **Blockstream App** er en mobilapplikasjon (iOS, Android) og skrivebordsapplikasjon for å administrere Bitcoin-lommebøker og eiendeler på Liquid Network. Den ble kjøpt opp av Blockstream i 2016 og het *GreenAddress*, ble omdøpt til *Blockstream Green* (2019), og heter nå *Blockstream app* (2025).
- **Viktige funksjoner**:
- Onchain-transaksjoner på **Blockchain Bitcoin**.
    - Transaksjoner på **Liquid**-nettverket (Sidechain for raske, konfidensielle utvekslinger).
- **Watch-only**-porteføljer for overvåking av fond uten tilgang til nøkler.
    - Personvernalternativer: tilkobling via **Tor**, tilkobling til en **personlig node** via Electrum, eller **SPV**-verifisering for å redusere avhengigheten av tredjepartsnoder.
    - Funksjoner **Replace-by-fee (RBF)** for å øke hastigheten på ubekreftede transaksjoner.
- **Kompatibilitet**: Integrerer maskinvarelommebøker som **Blockstream Jade**.
- **Interface**: Intuitiv for nybegynnere, med avanserte alternativer for eksperter.
- **Merk**: Denne veiledningen fokuserer på bruk av onchain med en Hardware Wallet på skrivebordsversjonen. Andre veiledninger som finnes som vedlegg, dekker bruk på mobilapplikasjoner, for onchain, Liquid og Watch-Only-funksjoner.



## 3. Installere og konfigurere Blockstream App Desktop



### 3.1. Last ned





- Gå til [offisiell nettside] (https://blockstream.com/app/) og klikk på "_Download Now_". Last ned den versjonen som passer til operativsystemet ditt (Windows, macOS, Linux).
- **Merk**: Sørg for å laste ned fra den offisielle kilden for å unngå falsk programvare.



### 3.2. Første konfigurasjon





- **Startskjerm**: Når programmet åpnes første gang, vises et skjermbilde uten en konfigurert Wallet. Opprettede eller importerte porteføljer vil vises her senere.



![image](assets/fr/02.webp)





- **Tilpass innstillingene**: Klikk på innstillingsikonet nederst til venstre, juster alternativene nedenfor, og gå deretter ut av Interface for å fortsette.



![image](assets/fr/03.webp)



#### 3.2.1. Generelle parametere





- Klikk på "**Generelt**" i menyen Innstillinger.
- **Funksjon**: Endre programvarens språk og aktiver eksperimentelle funksjoner ved behov.



![image](assets/fr/04.webp)



#### 3.2.2. Tilkobling via Tor





- Klikk på "**Nettverk**" i menyen Innstillinger.
- **Funksjon**: Rute nettverkstrafikken via **Tor**, et anonymt nettverk som krypterer forbindelsene dine.
- Hvorfor? Skjul din IP Address og beskytt personvernet ditt, ideelt hvis du ikke stoler på nettverket ditt (for eksempel offentlig Wi-Fi).
- **Ulempe**: Kan gjøre programmet tregere på grunn av kryptering.
- **Anbefaling**: Aktiver Tor hvis konfidensialitet er en prioritet, men test tilkoblingshastigheten.



![image](assets/fr/05.webp)



#### 3.2.3. Koble til en personlig node





- I menyen Innstillinger klikker du på "**Tilpassede servere og validering**".
- **Funksjon**: Kobler applikasjonen til din egen **komplette Bitcoin-node** via en **Electrum-server**.
- Hvorfor? Gir total kontroll over Blockchain-data, og eliminerer avhengigheten av Blockstream-servere.
- **Forutsetning**: En konfigurert Bitcoin-node.
- **Anbefaling**: Avanserte brukere som ønsker maksimal suverenitet.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verifisering av SPV





- I menyen Innstillinger klikker du på "**Tilpassede servere og validering**".
- **Funksjon**: Bruker **Simplified Payment Verification (SPV)** som laster ned blokkhoder og verifiserer transaksjonene dine ved hjelp av bevis på inkludering (Merkle), uten å lagre hele Blockchain.
- Hvorfor? Reduserer avhengigheten av Blockstreams standardnode, samtidig som den forblir lett for enhetene.
- **Ulempe**: Mindre sikker enn en Full node, ettersom den er avhengig av tredjepartsnoder for noe informasjon.
- **Anbefaling**: Aktiver SPV hvis du ikke kan bruke en personlig node, men foretrekker en Full node for optimal sikkerhet.



![image](assets/fr/07.webp)



## 4. Koble en Hardware Wallet til Blockstream-appen



### 4.1. Foreløpige betraktninger



#### 4.1.1. For Ledger-brukere





- Blockstream Green støtter bare **Bitcoin Legacy**-applikasjonen på Ledger-enheter (Nano S, Nano X).
- Trinnene du må følge i **Ledger Live** før du kobler til enheten :


1. Gå til **"Innstillinger"** → **"Eksperimentelle funksjoner"** og aktiver **utviklermodus**.


2. Gå til **"My Ledger"** → **"App Catalogue"**, og installer deretter applikasjonen **Bitcoin Legacy**


3. Åpne **Bitcoin Legacy**-applikasjonen på Ledger før du starter Blockstream Green for å opprette forbindelsen.




- **Merk**: Forsikre deg om at Ledger er låst opp med PIN-koden din og at Bitcoin Legacy-applikasjonen er aktiv når du kobler til.



#### 4.1.2 Initialisering av en Hardware Wallet





- Hvis Hardware Wallet (Ledger, Trezor eller Blockstream Jade) aldri har blitt brukt (enten med Blockstream Green eller med annen programvare som Ledger Live), må du først initialisere den. Dette trinnet innebærer at du gjør det i et sikkert miljø, uten kameraer eller observatører:


1. **seed frasegenerering / Mnemonic frase** (12, 18 eller 24 ord): Skriv det nøye ned på et stykke papir.


2. **seed fraseverifisering**: Test Wallet-importen fra de nevnte ordene, f.eks. ved å verifisere den utvidede offentlige nøkkelen. Skal utføres før du sender midler til Wallet og sikrer seed-frasen permanent.


3. **Sikring av seed-frasen**: Oppbevar frasen på et fysisk medium (papir eller metall) og på et trygt sted. Aldri lagre den digitalt (ingen skjermbilder, skyen eller e-post).




- **Viktig**: seed-frasen er din eneste mulighet til å få tilbake pengene dine hvis enheten går tapt eller ikke fungerer som den skal. Hvem som helst med tilgang kan stjele bitcoinsene dine.
- **Ressurser** for sikkerhetskopiering og kontroll av seed-setningen :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfigurasjon for denne opplæringen :





- Vi antar at Hardware Wallet allerede har blitt initialisert med en seed-frase og en PIN-kode for låsing.
- Vi antar at Hardware Wallet aldri har vært koblet til Blockstream App, noe som krever at du oppretter en ny konto. Hvis Hardware Wallet allerede har blitt brukt med Blockstream App, vil kontoen automatisk vises når applikasjonen åpnes.



### 4.2. Start tilkobling





- Fra startskjermen klikker du på "**Setup a New Wallet**", bekrefter vilkårene og betingelsene og klikker på "**Get Started**":



![image](assets/fr/08.webp)





- Velg alternativet "**På Hardware Wallet**":



![image](assets/fr/09.webp)





- Hvis du bruker en **Blockstream Jade**, klikker du på den tilhørende knappen. Ellers velger du "**Koble til en annen maskinvareenhet**":



![image](assets/fr/10.webp)





- Koble Hardware Wallet til datamaskinen via USB, og velg den i Blockstream-appen :



![image](assets/fr/22.webp)





- Vennligst vent mens Blockstream App importerer porteføljeinformasjonen din:



![image](assets/fr/23.webp)



### 4.3. Opprett en konto





- Hvis Hardware Wallet allerede har blitt brukt med Blockstream-appen, vil kontoen din automatisk vises i Interface etter import. Hvis ikke, oppretter du en konto ved å klikke på "**Opprett konto**":



![image](assets/fr/24.webp)





- Velg "**Standard**" for å konfigurere en klassisk Bitcoin-portefølje:



![image](assets/fr/25.webp)





- Når kontoen din er opprettet, kan du få tilgang til hovedporteføljen din i Interface:



![image](assets/fr/26.webp)





## 5. Bruk av Wallet i kjeden med en Hardware Wallet



### 5.1. Motta bitcoins





- Fra hovedskjermbildet for porteføljen klikker du på "**Mottak**" :



![image](assets/fr/27.webp)





- Programmet viser en **blank mottaks-Address**. Ved å bruke en ny Address for hvert mottak forbedrer du konfidensialiteten. Klikk på "**Kopier Address**" for å kopiere Address, eller la avsenderen skanne QR-koden som vises:



![image](assets/fr/12.webp)



**Alternativer** :




- (1) Klikk på pilene for å generate en ny Address knyttet til porteføljen din.
- (2) For å be om et spesifikt beløp klikker du på "**Flere alternativer**" og deretter på "**Begjær beløp**". QR vil bli oppdatert, og Address vil bli erstattet av en Bitcoin betalings URI som f.eks: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Hvis du vil gjenbruke en tidligere Address, klikker du på "**Flere alternativer**" og deretter på "**Liste over adresser**":



![image](assets/fr/14.webp)





- **Verifisering**: Kontroller den delte Address nøye for å unngå feil eller angrep (f.eks. skadelig programvare som endrer utklippstavlen).
- Når transaksjonen er sendt ut i nettverket, vil den vises i Wallet. Vent i 1 til 6 bekreftelser før du anser transaksjonen som uforanderlig.



![image](assets/fr/28.webp)



### 5.2. sende bitcoins





- Fra hovedskjermbildet for porteføljen klikker du på "**Send**".



![image](assets/fr/29.webp)





- Skriv inn **detaljer**:
    - (1) Kontroller at den valgte eiendelen er **Bitcoin** (onchain).
    - (2) Skriv inn **Address til mottakeren** ved å lime den inn eller skanne en QR-kode med webkameraet ditt.
    - (3) Angi **beløpet** som skal sendes (i BTC, satoshier eller andre enheter).




![image](assets/fr/16.webp)





- Velg **transaksjonsgebyrer** (valgfritt) :
 - Velg blant de foreslåtte alternativene (rask, middels, langsom) i henhold til hvor mye det haster, med en estimert bekreftelsestid.
 - For tilpassede kostnader kan du justere antall satoshis per vbyte manuelt. Disse vises på startskjermen. Se også [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Manuelt valg av UTXO-er** (valgfritt): Klikk på "**Manuelt Coin-valg**" for å velge de spesifikke UTXO-ene som skal brukes i transaksjonen.



![image](assets/fr/18.webp)





- **Foreløpig bekreftelse**: Kontroller Address, beløp og gebyrer på oppsummeringsskjermen, og klikk deretter på "**Bekreft transaksjon**". I virkeligheten vil ikke transaksjonen bli frigitt til nettverket før du har signert den med din Hardware Wallet, som alene har de hemmelige nøklene knyttet til adressene som UTXO-er (satoshier) vil bli belastet fra.



![image](assets/fr/19.webp)





- **Endelig kontroll og signatur**: Kontroller at alle transaksjonsparametere er korrekte **på Hardware Wallet**-skjermen, og signer deretter transaksjonen ved hjelp av den. En Address-feil kan føre til irreversibelt tap av midler.





- **Kringkasting**: Når den er signert, kringkaster Blockstream App automatisk transaksjonen på Bitcoin-nettverket.



![image](assets/fr/20.webp)





- **Oppfølging**:
 - Transaksjonen vises på startskjermen til Wallet som "ventende" til den er bekreftet.
 - Så lenge transaksjonen ikke er bekreftet, kan funksjonen **Replace-by-fee (RBF)** brukes til å fremskynde bekreftelsen ved å øke avgiften (se vedlegg).



![image](assets/fr/21.webp)



## Vedlegg



### A1. Andre Blockstream-veiledninger





- Bruk av Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importer og følg en portefølje i "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Bruke Blockstream-appen på mobiltelefoner (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Forklaring av Replace-by-fee (RBF)





- **Definisjon**: Replace-by-fee (RBF) er en funksjon i Bitcoin-nettverket som gjør det mulig for avsenderen å fremskynde bekreftelsen av en **onchain**-transaksjon ved å øke avgiften.
- **Grenser**:
    - RBF er ikke tilgjengelig for Liquid- eller Lightning-transaksjoner.
    - Den første transaksjonen må merkes som RBF-kompatibel, noe Blockstream App gjør automatisk.
- For mer informasjon, se [vår ordliste] (https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Beste praksis





- **Sikre gjenopprettingsfrasen din**:
    - Lagre Hardware Wallets Mnemonic-frasen på et fysisk medium (papir, metall) på et trygt sted.
    - Aldri lagre den digitalt (skyen, e-post, skjermdump).
    - Opplæring : Lagre Mnemonic-frasen din :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Beskytt personvernet ditt**:





    - generate en ny Address for hvert mottak i kjeden.
    - Aktiver **Tor** eller **SPV** for å begrense sporing.
    - Koble til din egen Bitcoin-node via Electrum for maksimal suverenitet.
- **Kontroller alltid leveringsadresser**:





    - Sjekk Address på Hardware Wallet-skjermen før du signerer.
    - Bruk kopier/lim inn eller en QR-kode for å unngå manuelle feil.
- **Optimaliser kostnadene**:





    - Juster avgiftene i henhold til hastegrad og overbelastning i nettverket (se [Mempool.space](https://Mempool.space/)).
    - Bruk Liquid eller Lightning for raske og rimelige transaksjoner som ikke krever sikkerhet i kjeden.
- **Oppdater programvaren**:





    - Hold Blockstream-appen og Hardware Wallet-fastvaren oppdatert med de nyeste funksjonene og sikkerhetsoppdateringene.



### A4. Ytterligere ressurser





- **Offisielle lenker**:
    - [Offisielt nettsted](https://blockstream.com/)
    - [Støtte for Blockstream-appen] (https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentasjon og chat
    - [GitHub] (https://github.com/Blockstream/green_qt)





- **Block Explorers**:
    - Onchain : [Mempool.space] (https://Mempool.space/)
    - Liquid : [Blockstream Info] (https://blockstream.info/Liquid)
    - Lyn : [1ML (Lightning Network)] (https://1ml.com/)





- **Sikring av gjenopprettingsfrasen din:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Ordliste] (https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Ordliste] (https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb