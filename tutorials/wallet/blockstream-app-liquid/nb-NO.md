---
name: Blockstream App - Liquid
description: Slik konfigurerer du Blockstream-appen og bruker Liquid Network
---
![cover](assets/cover.webp)


## 1. Innledning


### 1.1 Mål for opplæringen





- Denne veiledningen forklarer hvordan du bruker mobilapplikasjonen **Blockstream App** til å administrere en **Bitcoin Liquid**-portefølje, dvs. transaksjoner som er registrert direkte på Bitcoin "Liquid"-sidekjeden.
- Den dekker installasjon, innledende konfigurasjon, opprettelse av en Software Wallet og operasjoner for å motta og sende bitcoins på Liquid.
- Merk: Andre veiledninger i vedleggene dekker Onchain, Watch-Only og desktop-versjonen.



### 1.2 Målgruppe





- **Nybegynnere**: Brukere som ønsker å administrere sine bitcoins med en intuitiv mobilapplikasjon som integrerer Liquid Network.
- **Brukere på mellomnivå**: Personer som ønsker å forstå onchain-funksjonalitet og personvernalternativer som Tor eller SPV.



### 1.3 Vi introduserer Liquid



**Liquid** er en **Sidechain** av Bitcoin, utviklet av **[Blockstream](https://blockstream.com/Liquid/)**, designet for å tilby raskere, mer Confidential Transactions og avansert funksjonalitet, samtidig som den forblir koblet til hoved-Blockchain Bitcoin.



En Sidechain er en uavhengig Blockchain som opererer parallelt med Bitcoin, ved hjelp av en mekanisme kjent som **two-way peg**. Dette systemet låser bitcoins på hoved-Blockchain for å skape **Liquid-Bitcoins (L-BTC)**, tokens som sirkulerer på Liquid Network, samtidig som de beholder samme verdi som de opprinnelige bitcoinsene. Midler kan returneres til Blockchain Bitcoin når som helst.



![image](assets/fr/17.webp)






- (1) **Peg-in**: Bitcoins (BTC) låses på hoved-Blockchain av Liquid-føderasjonen. Til gjengjeld utstedes en tilsvarende mengde Liquid-Bitcoins (L-BTC), som sikrer paritet mellom de to kjedene, på Blockchain Liquid og sendes til brukeren.





- (2) **Uavhengige transaksjoner**: Transaksjoner kan kjøres samtidig og uavhengig av hverandre på hoved-Blockchain (BTC) og Sidechain Liquid (L-BTC), avhengig av brukerens behov.





- (3) **Peg-out**: Brukeren sender Liquid-Bitcoins (L-BTC) tilbake til Liquid-føderasjonen. Føderasjonen låser deretter opp en tilsvarende mengde bitcoins (BTC) på hoved-Blockchain og overfører dem til brukeren.



Liquid er avhengig av en **føderasjon** av betrodde deltakere (børser, anerkjente Bitcoin-selskaper) som administrerer blokkvalidering og bilateral forankring. I motsetning til Blockchain Bitcoin, som er desentralisert og avhengig av utvinnere, er Liquid et **føderert** nettverk, noe som betyr at sikkerheten og styringen avhenger av disse deltakerne. Selv om dette innebærer et kompromiss med desentraliseringen, muliggjør det optimalisert ytelse og avansert funksjonalitet.



![image](assets/fr/18.webp)



##### Hvorfor bruke Liquid?





- **Hastighet**: Transaksjoner på Liquid bekreftes på rundt **1 minutt**, sammenlignet med 10 minutter eller mer for transaksjoner i kjeden, takket være blokker som genereres hvert minutt av en føderasjon av validatorer.
- **Forbedret konfidensialitet**: Liquid bruker **Confidential Transactions**, som skjuler beløpet og typen aktiva som overføres, noe som gjør transaksjonene mer private (selv om adressene fortsatt er synlige).
- **Lave gebyrer**: Transaksjoner på Liquid er generelt billigere, noe som gjør dem ideelle for hyppige overføringer eller små beløp.
- **Flere aktiva**: I tillegg til L-BTC-er støtter Liquid utstedelse av andre digitale aktiva, for eksempel stablecoins eller tokens, til bruk i spesifikke applikasjoner.
- **Bruksområder**: Liquid er spesielt godt egnet for plattformovergripende børser, raske betalinger eller applikasjoner som krever smartkontrakter, samtidig som den er knyttet til sikkerheten til Bitcoin.



**Merk: Denne veiledningen fokuserer på bruk av Liquid via Blockstream-appen. For en grundig forståelse av Liquid Network, finner du ressurser i vedlegget.**



### 1.4. Hot Wallet påminnelse





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle navn på en applikasjon som er installert på en smarttelefon, datamaskin eller annen enhet som er koblet til Internett, og som gjør det mulig å administrere og sikre private nøkler fra en Bitcoin Wallet.
- I motsetning til **hardware-lommebøker**, også kjent som **Cold-lommebøker**, som isolerer nøkler offline, opererer programvarelommebøker i et tilkoblet miljø, noe som gjør dem mer sårbare for cyberangrep.





- **Anbefalt bruk**:
    - Ideell for håndtering av moderate mengder Bitcoin, spesielt for daglige transaksjoner.
    - Passer for nybegynnere eller brukere med begrensede midler, for hvem en Hardware Wallet kan virke overflødig.





- **Begrensninger**: Mindre sikker for oppbevaring av store midler eller langsiktig sparing. I dette tilfellet bør du velge en Hardware Wallet.




## 2. Vi presenterer Blockstream-appen





- **Blockstream App** er en mobilapplikasjon (iOS, Android) og skrivebordsapplikasjon for å administrere Bitcoin-lommebøker og eiendeler på Liquid Network. Den ble kjøpt opp av [Blockstream] (https://blockstream.com/) i 2016, og het tidligere *Green Address* og deretter *Blockstream Green*.
- **Viktige funksjoner**:
- Onchain-transaksjoner på **Blockchain Bitcoin**.
    - Transaksjoner på **Liquid**-nettverket (Sidechain for raske, konfidensielle utvekslinger).
- **Watch-only**-porteføljer for overvåking av fond uten tilgang til nøkler.
    - Personvernalternativer: tilkobling via **Tor**, tilkobling til en **personlig node** via Electrum, eller **SPV**-verifisering for å redusere avhengigheten av tredjepartsnoder.
    - Funksjoner **Replace-by-fee (RBF)** for å øke hastigheten på ubekreftede transaksjoner.
- **Kompatibilitet**: Integrerer maskinvarelommebøker som **Blockstream Jade**.
- **Interface**: Intuitiv for nybegynnere, med avanserte alternativer for eksperter.
- **Merk**: Denne veiledningen fokuserer på bruk av onchain. Andre veiledninger i vedleggene dekker Onchain, Watch-Only og skrivebordsversjonen.




## 3. Installere og konfigurere Blockstream-appen



### 3.1. Last ned





- For **Android**:
    - Last ned [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) fra Google Play Store.
    - Alternativ: Installer via APK-filen som er tilgjengelig på [Blockstreams offisielle GitHub] (https://github.com/Blockstream/green_android).
- For **iOS**:
    - Last ned [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) fra App Store.
- **Merk**: Sørg for å laste ned fra offisielle kilder for å unngå falske applikasjoner.



### 3.2. Første konfigurasjon





- **Startskjerm**: Når programmet åpnes første gang, vises et skjermbilde uten en konfigurert Wallet. Opprettede eller importerte porteføljer vil vises her senere.



![image](assets/fr/02.webp)





- **Tilpass innstillingene**: Klikk på "Programinnstillinger", juster alternativene nedenfor, klikk på "Lagre", start programmet på nytt og opprett porteføljen din.



![image](assets/fr/03.webp)



#### 3.2.1. Forbedret personvern (kun Android)





- **Funksjon**: Deaktiverer skjermbilder, skjuler forhåndsvisninger av programmer i oppgavebehandling og låser tilgangen når telefonen er låst.
- Hvorfor? Beskytter dataene dine mot uautorisert fysisk tilgang eller skadelig programvare som fanger opp skjermen.



#### 3.2.2. Tilkobling via Tor





- **Funksjon**: Rute nettverkstrafikken via **Tor**, et anonymt nettverk som krypterer forbindelsene dine.
- Hvorfor? Skjul IP Address og beskytt personvernet ditt, ideelt hvis du ikke stoler på nettverket ditt (for eksempel offentlig Wi-Fi).
- **Ulempe**: Kan gjøre programmet tregere på grunn av kryptering.
- **Anbefaling**: Aktiver Tor hvis konfidensialitet er en prioritet, men test tilkoblingshastigheten.



#### 3.2.3. Koble til en personlig node





- **Funksjon**: Kobler applikasjonen til din egen **komplette Bitcoin-node** via en **Electrum-server**.
- Hvorfor? Gir total kontroll over Blockchain-data, og eliminerer avhengigheten av Blockstream-servere.
- **Forutsetning**: En konfigurert Bitcoin-node.
- **Anbefaling**: Avanserte brukere som ønsker maksimal suverenitet.



#### 3.2.4. Verifisering av SPV





- **Funksjon**: Bruker **Simplified Payment Verification (SPV)** til å verifisere visse Blockchain-data direkte uten å laste ned hele kjeden.
- Hvorfor? Reduserer avhengigheten av Blockstreams standardnode, samtidig som den forblir lett for mobile enheter.
- **Ulempe**: Mindre sikker enn en Full node, ettersom den er avhengig av tredjepartsnoder for noe informasjon.
- **Anbefaling**: Aktiver SPV hvis du ikke kan bruke en personlig node, men foretrekker en Full node for optimal sikkerhet.





## 4. Opprette en Bitcoin onchain-portefølje



### 4.1. Start opprettelse





- **Advarsel**: Sett opp porteføljen din i et privat miljø, uten kameraer eller observatører.
- Fra startskjermen klikker du på "Kom i gang" :



![image](assets/fr/04.webp)





- Hvis du vil administrere en **Cold Wallet** (offline Wallet): klikk på **"Connect Jade"** for å bruke Hardware Wallet Blockstream Jade eller andre kompatible Cold-lommebøker.



![image](assets/fr/05.webp)






- Det neste skjermbildet vises:



![image](assets/fr/06.webp)






- (1) **"Oppsett av mobil Wallet"** : Opprett en ny Hot Wallet (Hot Wallet).
- (2) **"Gjenopprett fra sikkerhetskopi"**: Importer en eksisterende portefølje ved hjelp av en Mnemonic-frase (12 eller 24 ord). Advarsel! Ikke importer frasen fra en Cold Wallet, da den vil bli eksponert på en tilkoblet enhet, noe som ugyldiggjør sikkerheten.
- (3) **"Watch-Only"**: Importer en eksisterende skrivebeskyttet portefølje for å se saldoen (f.eks. for Cold Wallet) uten å eksponere Mnemonic-frasen. Se veiledningen for "Watch Only" i vedlegget.



**I denne veiledningen**: Klikk på **"Oppsett av mobil Wallet"** for å opprette en Hot Wallet.


Wallet opprettes automatisk, og startsiden for Wallet, her kalt "Min Wallet 5", vises:



![image](assets/fr/07.webp)



**Viktig**: Blockstream-appen har forenklet opprettelsen av en Wallet ved å ikke automatisk vise den 12-ord lange seed-frasen. *Selv om porteføljen nå opprettes med ett klikk, risikerer du å miste tilgangen til midlene dine hvis du ikke lagrer seed-frasen*.



### 4.2. Lagre seed frase





- På startskjermen til Wallet klikker du på fanen "Sikkerhet" og deretter på "Sikkerhetskopier" eller "Gjenopprettingsfrase":



![image](assets/fr/08.webp)



seed-frasen på 12 ord vises slik at du kan lagre den.





- Skriv ned gjenopprettingsfrasen din med den største forsiktighet. Skriv den ned på papir eller metall og oppbevar den på et trygt sted (trygt, frakoblet sted). Denne frasen er din eneste mulighet til å få tilgang til bitcoinsene dine i tilfelle du mister enheten din eller sletter applikasjonen.
- Det er også viktig å merke seg at hvem som helst med denne frasen kan stjele alle bitcoinsene dine. Aldri lagre det digitalt:
 - Ingen skjermbilde
 - Ingen sikkerhetskopiering i skyen, e-post eller meldinger
 - Ingen kopiering/liming (risiko for lagring i utklippstavlen)



**! Dette punktet er kritisk**. For mer informasjon om sikkerhetskopiering :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Sjekk seed setning



Før du sender penger til en Address som er knyttet til denne seed-frasen, må du teste sikkerhetskopien av de 12 ordene dine.


For å gjøre dette skriver vi ned en referanse, sletter Wallet, gjenoppretter den med sikkerhetskopien og sjekker at referansen er uendret.





- På startskjermen til Wallet klikker du på fanen "Settings" (Innstillinger) og deretter på "Wallet Details" (Wallet-detaljer), og kopierer zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Merk: En zpub Address kan importeres til Blockstream-applikasjonen for "Watch Only"-funksjonen (se vedlegg).





- Slett applikasjonen, og gjenopprett deretter Wallet via **"Gjenopprett fra sikkerhetskopi"** ved å skrive inn Mnemonic-setningen, og sjekk at zpub er uendret. Hvis ja, er sikkerhetskopien din riktig, og du kan sende penger til Wallet.





- Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, finner du en egen veiledning her :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Sikre tilgang til applikasjonen



Lås tilgangen til applikasjonen med en sterk PIN-kode:




- Fra startskjermen til Wallet går du til **"Sikkerhet"** og klikker deretter på **"PIN"**
- Tast inn og bekreft **en tilfeldig 6-sifret PIN-kode**.



**Biometrisk alternativ**: Tilgjengelig for ekstra bekvemmelighet, men mindre sikkert enn en robust PIN-kode (risiko for uautorisert tilgang, f.eks. fingeravtrykk eller ansiktsskanning under søvn).



**Merknad**: PIN-koden sikrer enheten, men det er bare seed-frasen som kan brukes til å få tilbake penger.





## 5. Bruk av Liquid Wallet



### 5.1. Motta "L-BTC" bitcoins



For å motta Liquid-Bitcoins (L-BTC) er flere alternativer tilgjengelige. Du kan be noen om å sende deg noen direkte ved å dele en Liquid som mottar Address, som er beskrevet nedenfor.



Alternativt kan du Exchange dine bitcoins på kjeden eller via Lightning Network for L-BTC ved hjelp av [en bro som Boltz] (https://boltz.Exchange/): skriv inn din Liquid som mottar Address, foreta betaling som du foretrekker, og motta din L-BTC.





- Fra porteføljens startskjerm klikker du på "**Transact**" og deretter **"Receive"**.



![image](assets/fr/19.webp)





- Som standard viser programmet en tom **kvittering Address, onchain** (SegWit v0-format, som begynner med `bc1q...`). Klikk på "Bitcoin" for å velge **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- **Alternativer**:
 - (1) Klikk på pilene for å velge en annen ny Address knyttet til denne seed-setningen.
    - (2) Du kan også velge en Address blant de som allerede er brukt/vises, ved å klikke på de tre punktene øverst til høyre og deretter på "Liste over adresser"
    - (3) For å be om et spesifikt beløp, klikk på de tre prikkene øverst til høyre, velg "Be om beløp", og skriv inn ønsket beløp. QR-koden oppdateres, og Address erstattes av en Bitcoin-betalings-URI.



![image](assets/fr/21.webp)





- Del Address/URI ved å klikke på "**Del**", kopiere teksten eller skanne QR-koden.
- **Verifisering**: Kontroller Address som deles med mottakeren så langt det er mulig for å unngå feil eller angrep (f.eks. skadelig programvare som endrer utklippstavlen).



### 5.2. sende bitcoins





- Fra porteføljens startskjerm klikker du på "**Transact**" og deretter **"Send"** :



![image](assets/fr/22.webp)





- Skriv inn **detaljer**:
    - (1) Skriv inn **Address til mottakeren** ved å klistre den på eller skanne en QR-kode.
    - (2) Kontroller eiendelene og kontoen som midlene sendes fra.
    - (3) Angi **beløpet** som skal sendes. Du kan velge enhet: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **Sjekk**:
    - Kontroller Address, beløp og kostnader på oppsummeringsskjermen.
    - En Address-feil kan føre til irreversibelt tap av penger. Se opp for skadelig programvare som endrer utklippstavlen.



![image](assets/fr/24.webp)





- **Bekreftelse**: Trykk på "Send"-knappen for å signere og distribuere transaksjonen.
- **Oppfølging**: I Wallet-fanen "Transact" vises transaksjonen som "Unconfirmed", deretter "Confirmed", deretter "Completed":



![image](assets/fr/25.webp)





- Tiden mellom to blokker er 1 minutt på Liquid, så transaksjonen blir raskt bekreftet og fullført.




## Vedlegg



### A1. Andre Blockstream App-opplæringer



Bruk av Onchain-nettverket



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importere og spore en Wallet i "Watch Only"-modus



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Skrivebordsversjon



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Beste praksis



Følg disse anbefalingene for å bruke **Blockstream App** sikkert og effektivt. De vil hjelpe deg med å beskytte pengene dine, optimalisere transaksjonene dine og bevare konfidensialiteten din i nettverkene **Bitcoin (onchain)**, **Liquid** og **Lightning**.





- **Sikre gjenopprettingsfrasen din**:
 - Veiledning: Lagre Mnemonic-frasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Bruk sikker autentisering:
 - Aktiver en **sterk PIN-kode** eller **biometrisk autentisering** (fingeravtrykk eller ansiktsgjenkjenning) for å beskytte tilgangen til applikasjonen.
 - Del aldri PIN-koden eller biometriske data.





- **Beskytt personvernet ditt**:
 - generate en ny Address for hvert mottak i kjeden eller Liquid for å begrense sporing på Blockchain.
 - Aktiver funksjonene "Enhanced Privacy", "Tor" og "SPV".
 - For maksimal konfidensialitet bør du koble Wallet til din egen Bitcoin-node via en Electrum-server i stedet for å bruke den offentlige noden





- Velg det nettverket som passer best til dine behov:
- **Onchain**: Foretrukket for langsiktig oppbevaring eller transaksjoner av store verdier (gebyrene er ubetydelige i forhold til beløpet).
- **Liquid**: Brukes for raske, rimelige overføringer med forbedret konfidensialitet.
- **Lyn**: Velg øyeblikkelige, rimelige overføringer for små beløp.





- **Kontroller alltid leveringsadresser**:
 - Før du sender penger, må du kontrollere Address nøye. Midler som sendes til feil Address er tapt for alltid. Bruk kopier/lim inn eller QR-kodeskanning, og kopier/endr aldri en Address for hånd.





- **Optimaliser kostnadene**:
 - For transaksjoner i kjeden velger du passende gebyrer (treg, middels, rask) i henhold til hvor mye det haster og hvor overbelastet nettverket er.
 - Bruk Liquid eller Lightning for små mengder.





- Hold søknaden oppdatert




### A3. Ytterligere ressurser





- **Offisielle lenker:**
- [Offisielt nettsted](https://blockstream.com/)
- [Støtte for mobilapplikasjonen](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentasjon og chat
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lyn: **[1ML (Lightning Network)](https://1ml.com/)**





- Læring og veiledning:** ** **[Plan ₿ Network](https://planb.network/)** :
 - Sikre gjenopprettingsfrasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Ordliste](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Ordliste](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb