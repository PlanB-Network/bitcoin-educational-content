---
name: BIP-85
description: Hvordan kan jeg bruke BIP-85 til å generate flere seedphrases fra en hoved-seed?
---
![cover](assets/cover.webp)



## 1. Forståelse av BIP-85



### 1.1 Hva er BIP-85?



BIP-85 er en avansert funksjon som lar deg lage flere **seed sekundærfraser** fra én **seed hovedfrase**.



Hver seed sekundær setning kan brukes til å opprette en helt uavhengig Bitcoin-portefølje. Disse porteføljene kan brukes til en rekke ulike formål: en Hot Wallet på mobilen, en portefølje til en slektning, en egen spareportefølje osv.



Alle seed-underfraser er **matematisk avledet**, men det er **umulig å spore tilbake til seed-hovedfrasen** fra en underfrase. Dette sikrer fullstendig separasjon mellom hver portefølje.



Så lenge du har tilgang til seed-hovedfrasen din (og den tilhørende passphrase hvis du bruker en slik), kan du generere en hvilken som helst seed-sekundærfrase **identisk**, uten å måtte lagre den separat.



### 1.2 Hvorfor bruke BIP-85?



BIP-85 er nyttig hvis du ønsker å :





- Opprett flere uavhengige Bitcoin-porteføljer uten flere sikkerhetskopier
- Administrer midlene dine i henhold til ulike bruksområder (sparing, utgifter, familie, prosjekter)
- Sikring av pårørende ("Uncle Jim"-funksjonen)
- Slett en portefølje uten å miste tilgangen til midlene dine
- Forenkle sikkerheten din: bare én seed-nøkkelfrase for å beskytte



### 1.3 Fordeler i forhold til BIP-32



Med BIP-32 kan en enkelt seed-setning brukes til å generate et komplett hierarki av Bitcoin-kontoer og adresser, ved hjelp av avledningsstier (for eksempel: `m/44'/0'/0'/0'/0/0`). Hver sti kan representere en separat konto, men **alle forblir knyttet til den samme seed-setningen**. Så hvis denne seed-setningen kompromitteres, blir **alle avledede kontoer tilgjengelige**.



Med BIP-85 kan en seed-hovedsetning brukes til å generate flere helt uavhengige seed-sekundærsetninger: **Hvis en av disse sekundære setningene blir kompromittert, vil angriperen aldri kunne gå tilbake til hoved-seed eller få tilgang til de andre porteføljene**.


Dette gjør det mulig å dele opp risikoen:





- Du kan bruke en sekundær seed for Hot Wallet eller midlertidig bruk, og akseptere en høyere eksponering.
- Selv om denne Hot Wallet blir kompromittert, vil de andre midlene dine, som er beskyttet av andre sekundære seeds eller holdes offline, **forbli trygge**.



På den annen side, for både BIP-32 og BIP-85, hvis hoved-seed blir kompromittert, er **alle midler sårbare**. Det er derfor avgjørende å beskytte den med det høyeste sikkerhetsnivået.



![image](assets/fr/02.webp)


## 2. Praktiske bruksområder for BIP-85



Med BIP-85 kan du opprette flere Bitcoin-porteføljer fra én enkelt seed-kjernefrase, hver med sin egen seed-sekundærfrase. Her er fem praktiske bruksområder for å organisere og sikre Bitcoin-midlene dine. Hvert tilfelle forklarer hvorfor det er mer praktisk å bruke BIP-85 enn å administrere flere kontoer med én enkelt seed-frase via BIP-32.



### 2.1 Begrensning av risikoen ved en mindre sikker portefølje





- Scenario**: Du bruker en "Hot Wallet" Wallet (installert på en Internett-tilkoblet enhet) til daglige transaksjoner.
- Løsning BIP-85**: Du oppretter en seed sekundærfrase dedikert til denne porteføljen.
- Fordel i forhold til BIP-32**: Du trenger ikke å importere seeds primære frase til telefonen, noe som reduserer risikoen for hacking. Bare seeds sekundære frase er kompromittert, noe som beskytter de andre lommebøkene dine. Med BIP-32 må du bruke seed-hovedfrasen og en omgåelsesbane, noe som eksponerer alle midlene dine.



### 2.2 Opprett en mappe til et familiemedlem





- Scenario**: Du setter opp en Bitcoin Wallet til noen som står deg nær (f.eks. moren din), samtidig som du kan få den tilbake hvis vedkommende mister den.
- Løsning BIP-85**: Du oppretter en dedikert seed sekundær setning og deler kun denne.
- Fordel i forhold til BIP-32**: Med BIP-32 må du enten dele hovedfrasen din i seed, noe som risikerer alle midlene dine og kompliserer administrasjonen for den du er glad i (håndtering av forgreningsveier), eller opprette en ny seed-frase for å lagre i tillegg til hovedfrasen din i seed.



### 2.3 Tilrettelegging for forvaltning av separate porteføljer





- Scenario**: Du skiller ut bitcoins til ulike formål (f.eks. langsiktig sparing, ikke-KYC-fond).
- Løsning BIP-85**: Du oppretter seed sekundære fraser dedikert til hvert mål.
- Fordel i forhold til BIP-32**: Med BIP-32 deler alle kontoer den samme seed-frasen, noe som kompliserer administrasjonen i tredjepartsporteføljer ved at avledningsstier som `m/44'/0'/0'/0'` må administreres. I tillegg er det ikke mulig å tilordne en separat konto per enhet (f.eks. "sparing på Coldcard", "daglig på mobil", "ferier på Trezor"). BIP-85 tildeler en unik seed sekundærfrase per mål, som er enkel å identifisere og importere separat på hver enhet.



### 2.4 Bruk av en midlertidig Wallet for transaksjoner





- Scenario**: Du trenger en midlertidig portefølje for en engangstransaksjon eller for å bevare konfidensialitet (f.eks. blanding av midler, interaksjon med en Exchange KYC osv.).
- Løsning BIP-85**: Du oppretter en seed sekundær setning, bruker den til transaksjonen og ødelegger den om nødvendig, vel vitende om at den kan regenereres.
- Fordel i forhold til BIP-32**: Med BIP-32 er en midlertidig konto avhengig av seed-hovedsetningen, noe som eksponerer alle midlene dine hvis de blir kompromittert.





## 3. Før du begynner





- Maskinvare** (valgfritt)
 - Coldcard Mk4 eller Q1
 - MicroSD-kort





- Grunnleggende kunnskap
 - Forståelse av Mnemonic-fraser (BIP-39): en liste med 12 til 24 ord for å lagre en mappe.
 - Vet hva en Bitcoin Wallet er: programvare eller enhet for å administrere bitcoins, og hvordan du gjenoppretter den med en Mnemonic-setning.
 - Flere ressurser i vedleggene.





- Kompatibel** programvare
 - Sparrow wallet (datamaskin, for kun overvåking eller avansert styring)
 - Nunchuck (mobil, for multisignaturer)
 - BlueWallet (mobil)
 - ...





- 3.4 Coldcard**-konfigurasjon
 - Initialiser en seed-setning med 24 ord på Coldcard.
 - Valgfritt: Legg til en passphrase for å sikre tilgang til BIP-85-grener.
 - Aktiver nyttige alternativer: NFC (for eksport), deaktiver USB på batteri (sikkerhet).




## 4. Trinn-for-trinn-veiledning



Følg disse trinnene for å opprette, bruke og hente en sekundær Mnemonic med BIP-85 på Coldcard.



### 4.1 generate a seed sekundær setning



Du oppretter en seed sekundærfrase fra seed hovedfrasen din.


Slå på Coldcard og tast inn PIN-koden din.





- 1. Hvis du har brukt en passphrase på din hoved seed:**
 - Gå til `passphrase` på startskjermen.
    - Velg "Legg til ord" og skriv inn passordet ditt.
    - Trykk på `Apply`.
    - Kontroller Wallets identitet: Gå til `Avansert > Vis identitet` for å legge merke til Wallets fingeravtrykk.





- 2. Gå til BIP-85**-menyen
 - Gå til `Avansert > Utlede seed B85` på startskjermen
 - Les advarselen og bekreft.



ColdCard informerer deg om at frøene som genereres, er matematisk avledet fra hoved-seed, men kryptografisk helt uavhengige.


![image](assets/fr/03.webp)





- 3. Velg et format


Velg fraseformatet for seed: 12, 18 eller 24 ord. Kryss av for antall ord som godtas av Wallet som du vil importere seed-frasen til.


![image](assets/fr/04.webp)





- 4. Velg indeks
 - Angi en indeks mellom 0 og 9999.
 - Denne indeksen er avgjørende for å regenerere den sekundære seed på et senere tidspunkt. Oppbevar den nøye med en etikett som f.eks: "Indeks 1 = Wallet mobil", "Indeks 2 = familieprosjekt", "Indeks 4 = testblanding", ...
 - Hvis du mister den, mister du ikke tilgangen til pengene dine, men du må teste kombinasjoner fra 0 til 9999 for å finne dem.


![image](assets/fr/05.webp)





- 5. Noter eller eksporter seed sekundær setning**


ColdCard viser nå en ny seed sekundær setning. Du kan :




 - Den **note manuelt**.
 - Trykk på :
     - 1` for å lagre det på SD-kortet
     - `2` for å **gå inn i "bruk denne seed"**-modus på ColdCard (nyttig for eksport eller signering av en transaksjon)
     - 3` for å vise en **QR-kode** (som skal skannes med en mobilapplikasjon som BlueWallet eller Nunchuck)
     - 4` for å sende den via **NFC**



💡 På dette tidspunktet har du en uavhengig seed-frase, som kan brukes i alle Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Bruke den sekundære seed



Du kan nå bruke denne avledede seed til å opprette en ny portefølje i :




- en mobilapp
- en annen Hardware Wallet
- en Multisig-portefølje



### 4.3 Gjenopprette en tapt seed sekundærfrase



Gjenta prosessen for å hente en sekundær seed når som helst:


1. Start ColdCard på nytt


2. Skriv inn PIN-koden din


3. Skriv inn din passphrase, hvis definert


4. Gå til `Avansert > Avled seed B85`


5. Velg format (12/18/24 ord)


6. Skriv inn samme indeks (f.eks. `1`)


7. Du får nøyaktig den samme sekundære seed




## 5. Grenser, risiko og beste praksis



### 5.1 Avhengighet av seed hovedsetning + passphrase



Bruken av BIP85 er helt avhengig av den 24 ord lange hovedsetningen seed, samt passphrase hvis du har brukt en slik.




- Fra disse to Elements kan alle seed sekundærfraser regenereres.
- Uten en av disse to Elements mister du tilgangen til alle derivatporteføljer.



### 5.2 Risikoer ved konfigurasjon med flere signaturer



Vi fraråder på det sterkeste å bruke sekundære seed-fraser generert fra samme primære seed-frase i en multi-sig-konfigurasjon: Hvis enheten eller den primære seed-frasen blir kompromittert, kan alle multi-sig-nøklene regenereres av en angriper.



### 5.3 Programvarekompatibilitet



Ikke alle applikasjoner støtter direkte BIP85-derivering. Frø generert via BIP85 er imidlertid standard BIP39-frø (12, 18 eller 24 ord), og kan derfor brukes i alle BIP39-kompatible porteføljer.



### 5.4 BIP85-kontoregister



Det anbefales å føre et oppdatert personlig register over seed sekundærfraser.




- Det gjør at du raskt kan finne ut hvilken BIP85-indeks som tilsvarer hvilken portefølje, uten å måtte holde på med seed sekundære fraser.
- Dette registeret bør være minimalistisk, uten noen eksplisitt omtale av Bitcoin, og bør lagres separat fra hoved-seed. Husk å nevne det i arveplanen din.



Registeret kan inneholde :




- bIP85-indeks brukt (tall fra 0 til 9999)
- et bruks- eller referansenavn (f.eks. Hot Wallet, personlige sparepenger, Wallet fra mamma)
- om nødvendig, Wallet-fingeravtrykket for verifisering i ColdCard



### 5.5 Sikkerhetskopiering



Sikkerhetskopier må inneholde :




- den viktigste seed
- gW-76 (hvis brukt)



Må aldri oppbevares sammen:




- hovedstrømmene seed og passphrase
- hovedregisteret seed og BIP85-kontoregisteret



Flere ressurser i vedleggene.




## VEDLEGG



## A.1 Ordliste





- [BEEP] (https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed frase](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Lagre gjenopprettingsfrasen din



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Forståelse av passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Hvordan Bitcoin-porteføljer fungerer



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f