---
name: Blockstream-appen - kun for Watch-Only
description: Hvordan konfigurerer jeg en Watch-only wallet i Blockstream-appen?
---

![cover](assets/cover.webp)


## 1. Innledning


### 1.1 Målet med opplæringen





- Denne veiledningen forklarer hvordan du konfigurerer og bruker **Watch-Only**-funksjonen i mobilapplikasjonen **Blockstream App** til å overvåke en Bitcoin Wallet uten å få tilgang til dens private nøkler.
- Den dekker installasjon, innledende konfigurasjon, import av en utvidet offentlig nøkkel og bruk av den til å spore saldoer og generate-mottakeradresser.
- Merk: Andre veiledninger, som du finner i vedlegget, dekker Onchain, Liquid og desktop-versjonen.



### 1.2. Målgruppe





- Nybegynnere**: Brukere som ønsker å overvåke en Bitcoin-portefølje (ofte knyttet til en Hardware Wallet) via en intuitiv mobilapplikasjon.
- Brukere på mellomnivå**: Personer som ønsker å administrere skrivebeskyttede porteføljer og samtidig bruke personvernalternativer som Tor eller SPV.
- Hardware Wallet-eiere**: For å sjekke saldoer og generate-adresser uten å koble til enheten.
- Bedrifter og butikker** :
 - Spor transaksjonene dine for regnskapsformål uten å eksponere de private nøklene dine.
 - Verifisere mottatte transaksjoner uten å taste inn privatnøkkelen i nettbaserte betalingssystemer.
 - Gjør det mulig for ansatte å bruke generate til nye mottaksadresser uten å ha tilgang til private nøkler.
- Organisasjoner og crowdfunding**: Vis saldoen på en transparent måte for giverne uten å gi tilgang til midlene.



### 1.3. Introduksjon av Watch-Only



Med en **Watch-Only** Wallet kan du overvåke transaksjonene og saldoen til en Bitcoin Wallet uten å ha tilgang til de private nøklene. I motsetning til en vanlig Wallet lagrer den bare offentlige data, for eksempel den **utvidede **offentlige nøkkelen** (som ga opphav til "**xpub**", deretter "zpub", "ypub" osv.), noe som gjør det mulig å få tak i mottakeradresser og spore transaksjonshistorikk på Blockchain Bitcoin. Fraværet av private nøkler gjør det umulig å utbetale penger fra applikasjonen, noe som garanterer økt sikkerhet.



![image](assets/fr/10.webp)



**Hvorfor bruke en Watch-only wallet?





- Sikkerhet**: Ideell for overvåking av en portefølje som er sikret av en **Hardware Wallet** uten å eksponere private nøkler på en tilkoblet enhet.
- Praktisk**: Lar deg sjekke saldoen og generate nye mottakeradresser uten å koble til Hardware Wallet.
- Konfidensialitet**: Kompatibel med alternativer som **Tor** eller **SPV** for å begrense avhengigheten av tredjepartsservere.
- Bruksområder**: Sporing av midler på farten, generering av adresser for å motta betalinger eller verifisering av transaksjoner uten å risikere private nøkler.



![image](assets/fr/01.webp)



### 1.4. Utvidede offentlige nøkler



En **utvidet offentlig nøkkel** (xpub, ypub, zpub osv.) er et stykke data avledet fra en Bitcoin Wallet som genererer alle underordnede offentlige nøkler og deres tilknyttede mottaksadresser, uten å gi tilgang til de private nøklene.





- Slik fungerer det** : Den utvidede offentlige nøkkelen genereres fra seed-frasen via en deterministisk prosess (BIP-32). Den oppretter et hierarkisk tre av underordnede offentlige nøkler, som hver kan konverteres til en mottatt Address. Ved å bruke samme avledningssti (f.eks. `m/44'/0'/0'`) som den overvåkede Wallet, genererer Watch-only wallet de samme adressene, slik at midler kan spores og nye mottaksadresser kan opprettes.



![image](assets/fr/11.webp)





- Utvidede typer offentlige nøkler
 - xpub**: Brukes for Legacy-porteføljer (adresser som begynner med "1", BIP-44) og Taproot-porteføljer (adresser som begynner med "bc1p", BIP-86).
 - ypub**: Designet for kompatible SegWit-lommebøker (adresser som begynner med "3", BIP-49).
 - zpub**: Tilknyttet opprinnelige SegWit-porteføljer (adresser som begynner med "bc1q", BIP-84).
 - Andre (tpub, upub, vpub osv.)**: Brukes for alternative nettverk (for eksempel Testnet) eller spesifikke standarder. For eksempel er tpub for Testnet-nettverket.





- Forskjell** : Valget mellom xpub, ypub eller zpub avhenger av Address-typen (legacy, SegWit, Taproot eller nested SegWit) og BIP-standarden som brukes av Wallet. Sjekk formatet som kreves av kildeporteføljen din for å sikre kompatibilitet med Blockstream App.





- Sikkerhet og konfidensialitet** : Den utvidede offentlige nøkkelen er ikke sensitiv med tanke på sikkerhet, ettersom den ikke tillater bruk av midler (ingen tilgang til private nøkler). Den er imidlertid sensitiv når det gjelder konfidensialitet, ettersom den avslører alle offentlige adresser og tilhørende transaksjonshistorikk.



**Anbefaling**: Beskytt den utvidede offentlige nøkkelen din som sensitiv informasjon.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet påminnelse





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle navn på en applikasjon som er installert på en smarttelefon, datamaskin eller annen enhet som er koblet til Internett, og som gjør det mulig å administrere og sikre private nøkler fra en Bitcoin Wallet.
- I motsetning til **hardware-lommebøker**, også kjent som **Cold-lommebøker**, som isolerer nøkler offline, opererer programvarelommebøker i et tilkoblet miljø, noe som gjør dem mer sårbare for cyberangrep.





- Anbefalt bruk** :
    - Ideell for håndtering av moderate mengder Bitcoin, spesielt for daglige transaksjoner.
    - Passer for nybegynnere eller brukere med begrensede midler, for hvem en Hardware Wallet kan virke overflødig.





- Begrensninger**: Mindre sikker for oppbevaring av store midler eller langsiktig sparing. I dette tilfellet bør du velge en Hardware Wallet.




## 2. Vi presenterer Blockstream-appen





- Blockstream App** er en mobilapplikasjon (iOS, Android) og skrivebordsapplikasjon for å administrere Bitcoin-porteføljer og eiendeler på Liquid Network. Den ble kjøpt opp av [Blockstream] (https://blockstream.com/) i 2016, og het tidligere *Green Address* og deretter *Blockstream Green*.
- Viktige funksjoner** :
    - Onchain**-transaksjoner på Blockchain Bitcoin.
    - Transaksjoner på **Liquid**-nettverket (Sidechain for raske, konfidensielle utvekslinger).
    - Watch-only**-porteføljer for overvåking av fond uten tilgang til nøkler.
    - Personvernalternativer: tilkobling via **Tor**, tilkobling til en **personlig node** via Electrum, eller **SPV**-verifisering for å redusere avhengigheten av tredjepartsnoder.
    - Funksjoner **Replace-by-fee (RBF)** for å øke hastigheten på ubekreftede transaksjoner.
- Kompatibilitet**: Integrerer maskinvarelommebøker som **Blockstream Jade**.
- Interface**: Intuitiv for nybegynnere, med avanserte alternativer for eksperter.
- Merk**: Denne veiledningen fokuserer på bruk av onchain. Andre veiledninger i vedleggene dekker Onchain, Watch-Only og skrivebordsversjonen.




## 3. Installere og konfigurere Blockstream-appen



### 3.1. Last ned





- For Android** :
    - Last ned [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) fra Google Play Store.
    - Alternativ: Installer via APK-filen som er tilgjengelig på [Blockstreams offisielle GitHub] (https://github.com/Blockstream/green_android).
- For iOS** :
    - Last ned [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) fra App Store.
- Merk**: Sørg for å laste ned fra offisielle kilder for å unngå falske applikasjoner.



### 3.2. Første konfigurasjon





- Startskjerm**: Når programmet åpnes første gang, vises et skjermbilde uten en konfigurert Wallet. Opprettede eller importerte porteføljer vil vises her senere.



![image](assets/fr/02.webp)





- Tilpass innstillingene**: Klikk på "Programinnstillinger", juster alternativene nedenfor, klikk på "Lagre", start programmet på nytt og opprett porteføljen din.



![image](assets/fr/03.webp)



#### 3.2.1. Forbedret personvern (kun Android)





- Funksjon**: Deaktiverer skjermbilder, skjuler forhåndsvisninger av programmer i oppgavebehandling og låser tilgangen når telefonen er låst.
- Hvorfor? Beskytter dataene dine mot uautorisert fysisk tilgang eller skadelig programvare som fanger opp skjermen.



#### 3.2.2. Tilkobling via Tor





- Funksjon**: Rute nettverkstrafikken via **Tor**, et anonymt nettverk som krypterer forbindelsene dine.
- Hvorfor? Skjul IP-en din Address og beskytt personvernet ditt, ideelt hvis du ikke stoler på nettverket ditt (for eksempel offentlig Wi-Fi).
- Ulempe**: Kan gjøre programmet tregere på grunn av kryptering.
- Anbefaling**: Aktiver Tor hvis konfidensialitet er en prioritet, men test tilkoblingshastigheten.



#### 3.2.3. Koble til en personlig node





- Funksjon**: Kobler applikasjonen til din egen **komplette Bitcoin-node** via en **Electrum-server**.
- Hvorfor? Gir total kontroll over Blockchain-data, og eliminerer avhengigheten av Blockstream-servere.
- Forutsetning**: En konfigurert Bitcoin-node.
- Anbefaling**: Avanserte brukere som ønsker maksimal suverenitet.



#### 3.2.4. Verifisering av SPV





- Funksjon**: Bruker **Simplified Payment Verification (SPV)** til å verifisere visse Blockchain-data direkte uten å laste ned hele kjeden.
- Hvorfor? Reduserer avhengigheten av Blockstreams standardnode, samtidig som den forblir lett for mobile enheter.
- Ulempe**: Mindre sikker enn en Full node, ettersom den er avhengig av tredjeparts noder for noe informasjon.
- Anbefaling**: Aktiver SPV hvis du ikke kan bruke en personlig node, men foretrekker en Full node for optimal sikkerhet.





## 4. Opprette en Bitcoin "Watch-only"-portefølje



### 4.1. Gjenopprett utvidet offentlig nøkkel



For å sette opp en Watch-only wallet må du først få tak i den utvidede offentlige nøkkelen (xpub, ypub, zpub osv.) til Wallet som skal overvåkes. Denne informasjonen er vanligvis tilgjengelig i innstillingene eller i delen "Wallet-informasjon" i programvaren eller Hardware Wallet.





- Eksempel med Blockstream-appen: Fra Wallet-startskjermen går du til "Innstillinger", deretter "Wallet Detaljer", og kopierer zpub :



![image](assets/fr/09.webp)





- Alternativ 1: generate en QR-kode som inneholder den utvidede offentlige nøkkelen for skanning i neste trinn.
- Alternativ 2: Bruk en output descriptor hvis Wallet tilbyr det.



### 4.2. Importer Wallet Watch-only





- Advarsel**: Sett opp porteføljen din i et privat miljø, uten kameraer eller observatører.
- Fra startskjermen klikker du på "Opprett en ny portefølje" og deretter på "Kom i gang" :



![image](assets/fr/04.webp)





- Det neste skjermbildet vises:



![image](assets/fr/06.webp)






- (1) **"Oppsett mobil Wallet"** : Opprett en ny Hot Wallet. Se veiledningen "Blockstream App - Onchain" i vedlegget.
- (2) **"Gjenopprett fra sikkerhetskopi"**: Importer en eksisterende portefølje ved hjelp av en Mnemonic-frase (12 eller 24 ord). Forsiktig! Ikke importer frasen fra en Cold Wallet, da den vil bli eksponert på en tilkoblet enhet, noe som ugyldiggjør sikkerheten.
- (3) **"Watch-Only"**: alternativet vi er interessert i for denne veiledningen.





- Velg deretter "**Enkel signatur**" og nettverket "**Bitcoin**":



![image](assets/fr/12.webp)





- Lim inn den utvidede offentlige nøkkelen (xpub, ypub, zpub osv.), skann den tilsvarende QR-koden eller skriv inn en output descriptor. Selv om applikasjonen angir "xpub", er også nøklene ypub, zpub osv. autorisert. Klikk deretter på "Connect":



![image](assets/fr/13.webp)




### 4.3. Bruk av Wallet Watch-only



Når Watch-only wallet er importert, viser den totale saldoen og transaksjonshistorikken for adresser som er avledet fra den utvidede offentlige nøkkelen. Bare transaksjoner i kjeden er synlige (Liquid-transaksjoner ignoreres). Hvis du vil overvåke en Liquid Wallet, gjentar du importen ved å velge "Liquid" i forrige trinn.





- Se saldo og historikk**: Fra startskjermen kan du se total saldo og transaksjonshistorikk i kjeden:



![image](assets/fr/14.webp)





- generate en mottakende Address**: Klikk på "Transact" og deretter på "Receive" for å opprette en ny Address i kjeden. Del den via QR-kode eller kopier for å motta midler:



![image](assets/fr/15.webp)





- Send penger**: Klikk på **"Transact"** og deretter på **"Send"**. Du kan skrive inn :
 - Mottakerens Address.
 - Beløpet for transaksjonen.
 - Transaksjonsgebyrer.



Men siden Watch-only wallet ikke har de private nøklene, kan du ikke sende penger direkte. For å signere transaksjonen må du koble til Hardware Wallet- eller Exchange PSBT-ene dine ved å skanne QR-kodene (et alternativ som for eksempel er tilgjengelig på Coldcard Q).



![image](assets/fr/16.webp)





- Merk**: Kontroller alltid mottakende Address og transaksjonsdetaljer for å unngå feil. Penger som er sendt til feil Address, kan ikke tilbakebetales.




## Vedlegg



### A1. Andre Blockstream App-opplæringer





- Bruke Onchain-nettverket :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Bruk av Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Desktop-versjon :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Utvidede offentlige nøkler





- Ordliste :
 - [Utvidede offentlige nøkler] (https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurs :
 - [Les clés publiques étendues](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/les-cles-etendues-8dcffce1-31bd-5e0b-965b-735f5f9e4602)




### A3. Beste praksis



Følg disse anbefalingene for å bruke **Blockstream App** sikkert og effektivt. De vil hjelpe deg med å beskytte pengene dine, optimalisere transaksjonene dine og bevare konfidensialiteten din i nettverkene **Bitcoin (onchain)**, **Liquid** og **Lightning**.





- Sikre gjenopprettingsfrasen din** :
 - Veiledning: Lagre Mnemonic-frasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Bruk sikker autentisering** :
 - Aktiver en **sterk PIN-kode** eller **biometrisk autentisering** (fingeravtrykk eller ansiktsgjenkjenning) for å beskytte tilgangen til applikasjonen.
 - Del aldri PIN-koden eller biometriske data.





- Beskytt personvernet ditt** :
 - generate en ny Address for hvert mottak i kjeden eller Liquid for å begrense sporing på Blockchain.
 - Aktiver funksjonene "Enhanced Privacy", "Tor" og "SPV".
 - For maksimal konfidensialitet bør du koble Wallet til din egen Bitcoin-node via en Electrum-server i stedet for å bruke den offentlige noden





- Velg det nettverket som passer best til dine behov** :
 - Onchain**: Foretrukket for langsiktig oppbevaring eller transaksjoner av store verdier (gebyrene er ubetydelige i forhold til beløpet).
 - Liquid**: Brukes for raske, rimelige overføringer med forbedret konfidensialitet.
 - Lyn**: Velg øyeblikkelige, rimelige overføringer for små beløp.





- Kontroller alltid leveringsadresser** :
 - Før du sender penger, må du sjekke Address nøye. Midler som sendes til feil Address, er tapt for alltid. Bruk kopier/lim inn eller QR-kodeskanning, aldri kopier/endre en Address for hånd.





- Optimaliser kostnadene** :
 - For transaksjoner i kjeden velger du passende gebyrer (treg, middels, rask) i henhold til hvor mye det haster og hvor overbelastet nettverket er.
 - Bruk Liquid, eller Lightning for små mengder.





- Hold søknaden oppdatert




### A4. Ytterligere ressurser





- Offisielle Blockstream-lenker:**
 - [Offisielt nettsted](https://blockstream.com/)**
 - [Støtte for mobilapplikasjonen] (https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentasjon og chat
 - [GitHub] (https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lyn: **[1ML (Lightning Network)](https://1ml.com/)**





 - Læring og veiledning:** ** **[Plan ₿ Network](https://planb.network/)** :
  - Sikre gjenopprettingsfrasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Ordliste](https://planb.network/fr/resources/glossary/Liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Ordliste](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb