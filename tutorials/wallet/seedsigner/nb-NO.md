---
name: SeedSigner
description: En Hardware Wallet som er gjør-det-selv, statsløs, rimelig og fullt luftgapet
---

![cover](assets/cover.webp)



SeedSigner er en Hardware Wallet Bitcoin med åpen kildekode som hvem som helst kan bygge selv ved hjelp av billige, allsidige elektroniske komponenter. I motsetning til kommersielle produkter som Ledger, Coldcard eller Trezor, er dette ikke en ferdigprodusert enhet som er klar til bruk: Det er et fellesskapsprosjekt som lar alle lage sin egen enhet og kontrollere hvert trinn.



SeedSigner er designet for å være 100 % ***luftavstengt***: Den kobler seg aldri til Internett, har ikke Wi-Fi eller Bluetooth (i tilfellet Raspberry Pi Zero v1.3) og er aldri koblet til en datamaskin for å Exchange-data. Kommunikasjonen skjer utelukkende via et Exchange-system med QR-kode. Rent konkret viser porteføljeforvaltningsprogramvaren din (for eksempel Sparrow wallet) transaksjonen som skal signeres i form av QR-koder; du skanner dem med SeedSigners kamera, og deretter signerer enheten transaksjonen ved hjelp av de private nøklene dine som er midlertidig lagret i RAM-minnet. Til slutt genererer den QR-koder som inneholder den signerte transaksjonen, som du skanner med programvaren din for å sende den til Bitcoin-nettverket.



![Image](assets/fr/001.webp)



SeedSigner er også ***stateless***. Med andre ord lagrer den ikke seed eller de private nøklene dine permanent, i motsetning til andre maskinvarelommebøker. Hver gang du starter den på nytt, er minnet helt tomt, med mindre du konfigurerer enheten til å lagre innstillingene dine på et microSD-kort. Du må derfor legge inn seed på nytt hver gang du bruker den, og den mest praktiske metoden er å lagre den i form av en QR-kode, som skannes ved oppstart ved hjelp av SeedSigners kamera. Denne driftsmåten reduserer angrepsflaten betraktelig: Selv om en tyv stjeler enheten din, vil han ikke finne noe informasjon på den, siden den alltid er tom som standard.



Et annet alternativ for å lagre seed og bruke den med SeedSigner er å bruke et *SeedKeeper*-smartkort sammen med en kompatibel leser. Dette gir deg en svært robust *secure element* til å lagre din seed, samtidig som du bruker SeedSigner-skjermen til å signere transaksjoner. Men denne spesielle konfigurasjonen er gjenstand for en annen dedikert veiledning. Her skal vi konsentrere oss om den grunnleggende bruken av SeedSigner:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner-prosjektet inntar en viktig plass i Bitcoin-økosystemet, ettersom det tilbyr alle, overalt i verden, muligheten til å dra nytte av avansert sikkerhet for å beskytte sine bitcoins. Den største fordelen ligger i tilgjengeligheten: maskinvaren som kreves kan kjøpes for mindre enn 50 dollar. I tillegg gjør den det mulig for folk som bor i land med restriksjoner, å bygge sin egen Hardware Wallet av standard datakomponenter, som er enkle å finne og mindre underlagt regulatoriske begrensninger.



Men selv utenfor disse spesielle sammenhengene kan SeedSigner være et interessant alternativ for deg: Det er åpen kildekode, fungerer statsløst og airgapped, og reduserer angrepsvektorene knyttet til Supply-kjeden til Hardware Wallet-en din.



## 1. Nødvendig utstyr



For å bygge din SeedSigner trenger du følgende komponenter:





- Raspberry Pi Zero
    - Versjon 1.3 anbefales, da den verken har Wi-Fi eller Bluetooth, noe som sikrer fullstendig isolasjon.
 - W- og v2-versjonene er også kompatible, men de inneholder en Wi-Fi/Bluetooth-brikke. Det anbefales derfor å deaktivere den fysisk ved å fjerne radiomodulen fra kortet. Operasjonen er relativt enkel, men krever presisjon (en fin tang er tilstrekkelig for Zero W, mens en Hot-penn er nødvendig for v2 for å fjerne metallplaten som skjuler modulen). Jeg vil ikke gå inn på detaljene i denne veiledningen, men du finner alle instruksjonene i dette dokumentet: *[Deaktivering av WiFi/Bluetooth via maskinvare] (https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Merk: Noen Raspberry Pi Zero-modeller selges uten forhåndsloddede GPIO-pinner. Du kan enten kjøpe en versjon med integrerte pinner direkte (enkleste løsning), eller kjøpe pinnene separat og lodde dem selv (mer komplisert løsning).
 - Ikke glem å ta med en mikro-USB-strøm Supply.



![Image](assets/fr/002.webp)





- Waveshare 1,3" skjerm (240×240 px)** (på fransk)
    - Det er viktig å velge akkurat denne modellen: det finnes andre lignende skjermer, men med en annen oppløsning. Uten en oppløsning på 240×240 px vil skjermen være ubrukelig.
    - Displayet har tre knapper og en mini-joystick som fungerer som brukerens Interface.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-kompatibelt kamera
    - Alternativ 1: standardkameraet med en bred gullmatte (sjekk kompatibiliteten med huset ditt).
    - Alternativ 2: det mer kompakte "*Zero*"-kameraet, designet spesielt for Pi Zero.



![Image](assets/fr/004.webp)





- MicroSD**-kort
    - Anbefalt kapasitet: mellom 4 og 32 GB.





- Bolig (valgfritt, men anbefalt)** (valgfritt, men anbefalt)** (valgfritt, men anbefalt)** (valgfritt, men anbefalt)** (anbefalt)
    - Beskytter enheten og gjør den enkel å bruke.
    - Den mest populære modellen er "*Orange Pill Case*", som [STL-filer med åpen kildekode er tilgjengelige for 3D-utskrift] (https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Bokser er også tilgjengelige fra [uavhengige forhandlere knyttet til prosjektet] (https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Du kan kjøpe disse komponentene separat, eller du kan velge ferdige pakker som inneholder all nødvendig maskinvare. Selv bestilte jeg pakken min [fra dette franske nettstedet](https://bitcoinbazar.fr/), men du finner også en liste over leverandører for hver region i verden på [SeedSigner-prosjektets maskinvareside](https://seedsigner.com/hardware/). Hvis du foretrekker å kjøpe komponentene enkeltvis, er de tilgjengelige på de største e-handelsplattformene eller i spesialforretninger.



## 2. Klargjøring av programvaren



Når du har samlet maskinvaren din, må du forberede microSD-kortet ved å installere SeedSigner-systemet på det. For å gjøre dette, gå til din vanlige datamaskin og koble til microSD-kortet ditt beregnet på SeedSigner.



### 2.1. Last ned



Gå til [prosjektets offisielle GitHub-repository] (https://github.com/SeedSigner/seedsigner/releases). Last ned den nyeste versjonen av programvaren :




- `.img`-bildet som tilsvarer din Pi-modell.
- Filen `.sha256.txt`.
- Filen `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Før vi starter installasjonen, la oss sjekke programvaren.



### 2.2 Verifisering under Linux og macOS



Start med å importere den offisielle offentlige nøkkelen til SeedSigner-prosjektet direkte fra Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminalen bør fortelle deg at en nøkkel har blitt importert eller oppdatert. Deretter kjører du verifiseringskommandoen på signaturfilen (husk å endre kommandoen i henhold til din versjon, her `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Hvis alt er i orden, skal utdataene vise `God signatur`. Dette betyr at filen `.sha256.txt` er signert med nøkkelen du nettopp har importert, og at signaturen er gyldig. Ignorer advarselen `WARNING: This key is not certified with a trusted signature`: dette er normalt, ettersom det nå er opp til deg å sjekke at nøkkelen som brukes tilhører SeedSigner-prosjektet.



Dette gjør du ved å sammenligne de siste 16 tegnene i fingeravtrykket som vises med de som er tilgjengelige på [Keybase.io/SeedSigner] (https://keybase.io/seedsigner), på deres [offisielle Twitter] (https://twitter.com/SeedSigner/status/1530555252373704707), eller i filen som er publisert på [SeedSigner.com] (https://seedsigner.com/keybase.txt). Hvis disse identifikatorene stemmer nøyaktig overens, kan du være sikker på at nøkkelen faktisk tilhører prosjektet. Hvis du er i tvil, stopp umiddelbart og spør SeedSigner-fellesskapet (Telegram, X, GitHub...) om hjelp.



Når nøkkelen er validert, kan du kontrollere at det nedlastede bildet ikke har blitt endret (husk å endre kommandoen i henhold til din versjon, her `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Under Linux er denne kommandoen innebygd.
- Advarsel: macOS-versjoner før `Big Sur (11)` gjenkjenner ikke `--ignore-missing`-alternativet. I dette tilfellet må du fjerne det og ignorere advarsler om manglende filer.



Det forventede resultatet er en `OK` ved siden av filen `.img`. Dette bekrefter at det opplastede bildet er identisk med det som er publisert av prosjektet, og at det ikke har blitt endret.



### 2.3 Windows-verifisering



På Windows er fremgangsmåten lik, men kommandoene er forskjellige. Start med å installere [Gpg4win] (https://www.gpg4win.org/) og åpne *Kleopatra*-programmet. Importer den offentlige nøkkelen til SeedSigner-prosjektet fra URL-adressen Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Deretter åpner du PowerShell i mappen der de nedlastede filene ligger (`Shift` + høyreklikk > `Åpne PowerShell her`). Kjør følgende kommando for å sjekke manifestsignaturen (husk å endre kommandoen i henhold til din versjon, her `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Hvis alt er i orden, skal utdataene vise `God signatur`. Dette betyr at filen `.sha256.txt` er signert med nøkkelen du nettopp har importert, og at signaturen er gyldig. Ignorer advarselen `WARNING: This key is not certified with a trusted signature`: dette er normalt, ettersom det nå er opp til deg å sjekke at nøkkelen som brukes tilhører SeedSigner-prosjektet.



Dette gjør du ved å sammenligne de siste 16 tegnene i fingeravtrykket som vises med de som er tilgjengelige på [Keybase.io/SeedSigner] (https://keybase.io/seedsigner), på deres [offisielle Twitter] (https://twitter.com/SeedSigner/status/1530555252373704707), eller i filen som er publisert på [SeedSigner.com] (https://seedsigner.com/keybase.txt). Hvis disse identifikatorene stemmer nøyaktig overens, kan du være sikker på at nøkkelen faktisk tilhører prosjektet. Hvis du er i tvil, stopp umiddelbart og spør SeedSigner-fellesskapet (Telegram, X, GitHub...) om hjelp.



Når nøkkelen er validert, må du kontrollere at bildefilen ikke er ødelagt. Dette gjør du ved å bruke følgende kommando i PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Eksempel for en Raspberry Pi Zero 2 (husk å modifisere kommandoen i henhold til din versjon, her `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell beregner deretter Hash SHA256 for bildefilen din. Sammenlign denne Hash med den tilsvarende verdien i `seedsigner.0.8.6.sha256.txt`.




- Hvis de to verdiene er helt identiske, er kontrollen vellykket, og du kan fortsette.
- Hvis de er forskjellige, er filen skadet eller ødelagt. Ikke bruk den, og start nedlastingen på nytt.



![Image](assets/fr/013.webp)



Vellykket verifisering garanterer at `.img`-filen din er både autentisk (signert av SeedSigner) og uendret (umodifisert). Du kan da trygt gå videre til neste trinn.



### 2.4. Flash bildet



Hvis du ikke allerede har det, kan du laste ned programvaren [Balena Etcher] (https://etcher.balena.io/), og deretter :




- Sett microSD-kortet inn i datamaskinen.
- Launch Etcher.
- Velg den nedlastede og verifiserte `.img`-filen.
- Velg microSD-kort som mål.
- Klikk på `Flash!`.



![Image](assets/fr/014.webp)



Vent til prosessen er fullført: microSD-kortet er klart til bruk. Nå er det tid for montering!



## 3. SeedSigner-montering



Når microSD-kortet er klargjort og flashet med SeedSigner-programvaren, kan du fortsette med den endelige monteringen. Ta deg god tid, da enkelte deler er skjøre (spesielt duken, kameraet og GPIO-pinnene).



### 3.1 Klargjøring av huset



Først og fremst må du åpne kabinettet. Kontroller at den er ren og at det ikke er rester av 3D-printingsplast i veien for de innvendige festene. Se etter :




- Kameraplassering (lite sirkulært hull foran).
- Åpningen for skjermen.
- Utskjæringene for mikro-USB-portene og microSD-sporet på Raspberry Pi Zero.



### 3.2 Installasjon av kamera



Finn kamerabåndkontakten på Raspberry Pi Zero: Det er en tynn, svart stripe på siden av kortet, som kan løftes litt for å åpne den. Løft den forsiktig opp, uten å tvinge den: Den skal bare vippe noen millimeter.



![Image](assets/fr/015.webp)



Sett inn kameradekselet. Den brune/kobberfargede delen skal vende nedover. Pass på at det sitter godt fast i kontakten, uten å vri seg.



![Image](assets/fr/016.webp)



Lukk den svarte stangen for å låse duken (du vil kjenne et lite klikk). Kontroller forsiktig at den holder seg på plass og ikke beveger seg.



![Image](assets/fr/017.webp)



Plasser deretter kameramodulen i det aktuelle hullet i huset. Avhengig av modell kan den klikkes direkte på plass, eller det kan være nødvendig med en liten selvklebende stripe for å holde den på plass. Objektivet må være perfekt justert og vendt utover.



### 3.3 Installere Raspberry Pi Zero



Hvis du bruker et deksel, setter du Raspberry Pi Zero-brettet inn i det. Juster portene forsiktig med åpningene som følger med.



Plasser deretter Waveshare-skjermen på toppen av Raspberry Pi Zero. GPIO-pinnene på Pi skal ligge perfekt på linje med hunnkontakten på skjermen. Trykk skjermen sakte på pinnene, med jevnt trykk på hver side for å unngå å bøye dem.



![Image](assets/fr/018.webp)



Hvis du har et etui, kan du fullføre monteringen ved å legge til frontpanelet og styrespaken.



Til slutt setter du microSD-kortet som inneholder den flashede programvaren, inn i Raspberry Pi Zeros kantmonterte spor. Forsikre deg om at det klikker på plass.



### 3.4 Første oppstart



Koble en mikro-USB-strømkabel til den dedikerte porten. Vent i omtrent ett minutt. SeedSigner-logoen skal vises, etterfulgt av startskjermen.



![Image](assets/fr/019.webp)



Til å begynne med må du kontrollere at de ulike komponentene fungerer som de skal ved å gå til menyen `Innstillinger > I/O-test`.



![Image](assets/fr/020.webp)



Test alle knappene og sørg for at de reagerer som de skal. Klikk deretter på knappen `KEY1` for å kontrollere at kameraet fungerer som forventet. Dette vil ta et bilde.



![Image](assets/fr/021.webp)



### 3.5 Justering av kamera



Avhengig av hvordan du har montert SeedSigner, kan det hende at kameraet viser et invertert bilde. For å rette opp dette kan du gå til `Innstillinger > Avansert > Kamerarotasjon` og velge en 180° rotasjon om nødvendig.



![Image](assets/fr/022.webp)



Hvis du har endret kameravinkelen eller ønsker å endre andre innstillinger (for eksempel Interface-språket) på et senere tidspunkt, må du aktivere persistens av innstillinger på microSD-kortet. Ellers vil innstillingene dine gå tilbake til standardinnstillingene hver gang du starter på nytt, ettersom Raspberry Pi Zero ikke har noe vedvarende minne.



Dette gjør du ved å åpne menyen `Innstillinger > Vedvarende innstillinger` og deretter velge `Aktivert`.



![Image](assets/fr/023.webp)



Hvis alt fungerer som det skal, er SeedSigner nå klar til bruk!



## 4. SeedSigner-innstillinger



Før du oppretter din Bitcoin Wallet, la oss konfigurere SeedSigner. Siden den kjører på en Raspberry Pi Zero uten permanent minne, lagres ikke innstillingene automatisk med mindre du lagrer dem på microSD-kortet. Så sørg for at du har aktivert dette alternativet, ellers vil disse innstillingene gå tapt ved omstart (se trinn 3.5).



### 4.1 Tilgang til parametermeny



Start SeedSigner og vent til startskjermen vises. Bruk styrespaken til å navigere til alternativet `Innstillinger`, og bekreft ved å trykke på midtknappen. Du kommer nå til hovedinnstillingsmenyen.



![Image](assets/fr/024.webp)



### 4.2 Valg av programvare for porteføljeforvaltning



Åpne deretter menyen `Coordinator software`.



![Image](assets/fr/025.webp)



Koordinatoren er programvaren for porteføljeforvaltning som SeedSigner kommuniserer med via QR-koder. Denne programvaren installeres enten på datamaskinen eller på smarttelefonen din. Den gjør det mulig for deg å administrere dine bitcoins, men uten å ha tilgang til dine private nøkler. SeedSigner forblir den eneste enheten som kan signere transaksjonene dine.



Den nåværende fastvareversjonen støtter flere programvarepakker: Sparrow, Specter, BlueWallet, Nunchuk og Keeper. I mitt tilfelle bruker jeg **Sparrow wallet**, som jeg anbefaler spesielt for sin enkelhet og rike funksjonalitet.



Hvis du ikke vet hvordan du installerer den, kan du følge denne veiledningen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Velg programvaren du ønsker fra menyen.



![Image](assets/fr/026.webp)



### 4.3 Visning av enheter og beløp



I menyen `Denominasjonsvisning` kan du velge hvilken enhet beløpene skal vises i:




- `BTC`
- mBTC` (milli-Bitcoin, eller 0,001 BTC)
- gW-20 (satoshier, eller 1/100 000 000 BTC)



**Sats** er vanligvis den mest praktiske enheten for små mengder.



![Image](assets/fr/027.webp)



### 4.4 Avanserte innstillinger



Gå nå til menyen `Avansert`. Her finner du flere nyttige alternativer:




- gW-22 network`: skal bare endres hvis du ønsker å bruke SeedSigner på Testnet.
- qR code density`: justerer mengden informasjon i hver QR-kode. Du kan beholde standardverdien, med mindre du synes det er vanskelig å lese når du skanner.
- xpub export: aktiverer eller deaktiverer eksport av den utvidede offentlige nøkkelen (xpub, ppub, zpub) til programvare for porteføljeforvaltning via QR-kode (en funksjon vi kommer til å bruke senere, så la den være aktivert inntil videre).
- `Skripttyper`: definerer skripttypene som er tillatt for å låse bitcoinsene dine. Du trenger ikke å endre denne parameteren, ettersom skripttypen settes direkte til Sparrow. Her gjelder det bare skript som SeedSigner er autorisert til å manipulere.



### 4.5 Valg av språk



Til slutt kan du i menyen `Language` endre språket på Interface slik at det passer dine preferanser.



![Image](assets/fr/028.webp)



## 5. Opprette og lagre seed



seed (eller Mnemonic-frasen) danner grunnlaget for Bitcoin-porteføljen din. Den brukes til å utlede dine private nøkler og adresser, og gir deg tilgang til midlene dine. SeedSigner tilbyr flere metoder for å generere den, som vi skal se nærmere på i denne delen.



Før vi begynner, noen viktige påminnelser:




- Denne frasen gir deg full, ubegrenset tilgang til alle bitcoinsene dine.** Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til din SeedSigner ;
- Vanligvis brukes en 12-ordsfrase for å gjenopprette en Wallet hvis en Hardware Wallet mistes eller blir stjålet. Men siden SeedSigner er en *stateless* enhet, registrerer den aldri din seed. Så dine fysiske sikkerhetskopier er ikke bare sikkerhetskopier, men **den eneste måten å bruke din Wallet** på. Hvis du mister disse sikkerhetskopiene, vil bitcoinsene dine gå tapt permanent. Så sikkerhetskopier dem nøye, på flere medier og på trygge steder;
- Hvis du nettopp har begynt, anbefaler jeg deg på det sterkeste å lese denne veiledningen for å få en detaljert forståelse av risikoen ved å administrere en Mnemonic-frase :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Åpne verktøyet for oppretting av seed



Fra startskjermen til SeedSigner går du til menyen "Verktøy".



![Image](assets/fr/029.webp)



Du vil nå generate din seed. En seed er rett og slett et stort tilfeldig tall. Jo mer tilfeldig det er generert, desto sikrere er det. SeedSigner tilbyr to måter å gjøre dette på:




- kamera": seed genereres fra den visuelle støyen i et fotografi. Du tar et bilde av et tilfeldig miljø (objekt, landskap, ansikt osv.), og pikselvariasjonene brukes til å beregne generate-entropien. Det er en rask metode, men ikke reproduserbar.
- terningkast": Du kaster terninger for å skape den nødvendige entropien. Det er mer tidkrevende, men reproduserbart og dermed verifiserbart. Hvis du velger denne metoden, følger du rådene i denne veiledningen (du trenger ikke å beregne sjekksummen her, det tar SeedSigner seg av):



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Opprette seed med bildet



Hvis du velger fotometoden, klikker du på `Ny seed` (med kameraikonet), tar et bilde og validerer. Velg deretter lengden på setningen (12 eller 24 ord), som vises på skjermen for lagring. De følgende trinnene er identiske med del 5.3.



### 5.3 Skape seed med terninger



I denne veiledningen bruker vi **Terningkast**-metoden. Klikk på `Ny seed` (med terningikonet).



![Image](assets/fr/030.webp)



Velg deretter lengden på Mnemonic-frasen din. 12 ord gir allerede et tilstrekkelig sikkerhetsnivå, så dette er det valget jeg anbefaler.



![Image](assets/fr/031.webp)



Kast terningen, og skriv inn tallene ved hjelp av markøren. Trykk på midtknappen for å bekrefte hver inntasting. Hvis du gjør en feil, kan du gå tilbake. Bruk flere forskjellige terninger for å redusere påvirkningen fra ubalanserte terninger. Sørg for at du ikke blir overvåket under denne operasjonen.



![Image](assets/fr/032.webp)



Når du har lagt inn dine 50 kast, genererer SeedSigner setningen din. **Følg instruksjonene i denne veiledningen nøye hvis du er nybegynner:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Vise og lagre seed



Skriv ordene i Mnemonic-frasen din forsiktig ned på et egnet fysisk underlag (papir eller metall).



![Image](assets/fr/033.webp)



### 5.5 Kontroll av sikkerhetskopien



For å unngå feil i sikkerhetskopien ber SeedSigner deg om å verifisere sikkerhetskopien. Klikk på `Verifiser`.



![Image](assets/fr/034.webp)



Skriv deretter inn det ønskede ordet i henhold til rekkefølgen i setningen. Her må jeg for eksempel velge det tredje ordet i setningen min.



![Image](assets/fr/035.webp)



Hvis du gjør en feil, vil SeedSigner informere deg om det, og du må begynne på nytt og huske å notere Mnemonic-frasen når du får den. Dette verifiseringstrinnet sikrer at sikkerhetskopien er korrekt og fullstendig. Når sikkerhetskopien er validert, vises `Backup Verified` på skjermen.



![Image](assets/fr/036.webp)



For en mer fullstendig restaureringstest, følg denne veiledningen :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Forståelse av konseptet "tilstandsløs enhet



SeedSigner er en enhet uten permanent minne. Det betyr at seed aldri lagres inne i enheten (i motsetning til for eksempel en Ledger, Trezor eller Coldcard). Så snart du slår av strømmen, forsvinner seed helt fra RAM-minnet. Når SeedSigner startes på nytt, går den tilbake til en tom tilstand: Du må gi den seed igjen for å signere transaksjonene dine.



Dette gir viktig beskyttelse. I motsetning til andre maskinvarelommebøker er SeedSigner basert på en Raspberry Pi Zero uten fysisk beskyttelse, inkludert *secure element*. Men siden ingen sensitive data lagres, vil selv en fysisk kompromittert enhet ikke gjøre det mulig for en angriper å hente ut de private nøklene dine eller bruke bitcoinsene dine.



På den annen side innebærer denne arkitekturen et ekstra ansvar: Uten en sikkerhetskopi er pengene dine definitivt tapt. Derfor anbefaler jeg en ** dobbel sikkerhetskopi**. Du har allerede din gjenopprettingsfrase: dette er din viktigste langsiktige sikkerhetskopi, som skal oppbevares på et trygt sted. Nå skal vi lage en kopi av denne frasen i form av **QR-kode**.



Hver gang du bruker SeedSigner, skanner du denne QR-koden med enhetens kamera, slik at den midlertidig laster inn dine seed i minnet mens du signerer transaksjonene dine. Denne andre sikkerhetskopien, som er beregnet på daglig bruk, må også oppbevares med største forsiktighet: Alle som er i besittelse av denne QR-koden, har full tilgang til bitcoinsene dine.


Jeg anbefaler deg også å oppbevare QR-koden og Mnemonic-frasen på to separate steder, slik at du unngår å miste alt i tilfelle en skade.



Et mer avansert og sikkert alternativ er å bruke SeedSigner med en **SeedKeeper**, som lagrer seed i en secure element. For å finne ut mer, se denne veiledningen :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Skriv hovednøkkelens fingeravtrykk



Når verifiseringen er fullført, viser SeedSigner fingeravtrykket til hovednøkkelen til din Wallet. Dette fingeravtrykket identifiserer Wallet og sikrer at du bruker riktig gjenopprettingsfrase i fremtiden. Det avslører ingen informasjon om de private nøklene dine, så du kan trygt lagre det på et digitalt medium. Bare sørg for at du har en tilgjengelig kopi og aldri mister den.



![Image](assets/fr/037.webp)



Det er også på dette stadiet at du kan legge til en **passphrase BIP39** for å forsterke sikkerheten til din Wallet. Dette alternativet kan være verdt det, avhengig av din backup-strategi, men det innebærer også en risiko: Hvis du mister passphrase, vil tilgangen til bitcoinsene dine gå tapt permanent.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Hvis du ennå ikke er kjent med passphrase-konseptet, inviterer jeg deg til å lese denne omfattende veiledningen om emnet:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Lagre seed i QR-format (*SeedQR*)



Med SeedSigner kan du konvertere seed til en QR-kode på papir, kalt *SeedQR*. Denne metoden gjør det enklere å laste inn Wallet på nytt, ettersom du slipper å skrive inn hvert ord manuelt.



For å gjøre dette trenger du en blank QR-kode i papir eller metall som tilsvarer lengden på Mnemonic-frasen din. Hvis du har kjøpt en komplett pakke for din SeedSigner, er malene vanligvis inkludert. Hvis ikke, kan du laste dem ned og skrive dem ut (eller kopiere dem for hånd) her :




- [12-ords format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24 ords format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompakt format 12 ord](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompakt format 24 ord](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Fra seed-skjermen velger du `Backup seed`.



![Image](assets/fr/039.webp)



Velg deretter `Eksporter som SeedQR`.



![Image](assets/fr/040.webp)



Velg deretter ønsket format (normal eller kompakt) i henhold til den tilgjengelige papirmalen.



![Image](assets/fr/041.webp)



Klikk på `Begin` for å starte opprettelsen av *SeedQR*. SeedSigner vil deretter vise en rekke rutenett (A1, A2, B1 osv.), som hver tilsvarer en del av koden.



![Image](assets/fr/042.webp)



Reproduser hver svarte prikk nøye på lagringsarket, og bruk deretter styrespaken til å gå videre til neste BLOCK. Ta deg god tid: En enkel feiljustering kan gjøre QR-koden ubrukelig.



Noen tips:




- Begynn med blyant, slik at du kan rette opp eventuelle feil, og gå deretter tilbake til en fin svart penn når du er ferdig;
- Et sentrert punkt midt i kvadratet er alt du trenger, det er ikke nødvendig å fylle det helt ut.



![Image](assets/fr/043.webp)



Klikk deretter på `Confirm SeedQR`, og skann QR-koden din for å sjekke at den fungerer som den skal.



![Image](assets/fr/044.webp)



Hvis meldingen `Success` vises, er *SeedQR* gyldig: du kan gå videre til neste trinn.



![Image](assets/fr/045.webp)



**Oppbevar dette arket like strengt som gjenopprettingsfrasen din. Hvem som helst som er i besittelse av denne QR-koden kan rekonstruere de private nøklene dine og stjele bitcoinsene dine



Gratulerer, Bitcoin-porteføljen din er nå oppe og går! Vi skal nå importere de offentlige komponentene til **Sparrow wallet** for å administrere den på en enkel måte.



## 6. Importer Wallet til Sparrow



Når SeedSigner er satt opp og seed er korrekt generert og lagret, er neste trinn å koble denne porteføljen til forvaltningsprogramvare som Sparrow wallet. Din seed vil alltid være frakoblet, da kun den offentlige delen av porteføljen din vil bli overført til Sparrow. Dette gjør det mulig for programvaren å vise adressene og transaksjonene dine og opprette nye transaksjoner, uten at du noen gang kan bruke bitcoinsene dine. For å bruke dine bitcoins må din SeedSigner alltid signere transaksjonen som er forberedt av Sparrow.



### 6.1 Klargjøring av SeedSigner



Sett inn microSD-kortet som inneholder operativsystemet, slå på SeedSigner, og last deretter inn seed som du nettopp har opprettet fra QR-koden for sikkerhetskopien din. På startskjermen velger du `Scan`, og skanner deretter din SeedQR med SeedSigner.



![Image](assets/fr/046.webp)



Kontroller at fingeravtrykket på hovednøkkelen stemmer overens med fingeravtrykket på Wallet. Hvis du bruker en passphrase, legger du den inn på dette stadiet.



![Image](assets/fr/047.webp)



Dette tar deg til menyen for porteføljen din, som i mitt tilfelle heter `d4149b27`. Hvis du er tilbake på startskjermen, velger du `Seeds`, og deretter velger du utskriften som svarer til porteføljen din. Klikk deretter på `Export Xpub`.



![Image](assets/fr/048.webp)



Velg porteføljetype. I vårt tilfelle er det en enkeltportefølje: velg `Single Sig`.



![Image](assets/fr/049.webp)



Deretter kommer valget av skriptstandard. Den nyeste og mest økonomiske når det gjelder transaksjonskostnader er `Taproot`. Jeg anbefaler deg derfor å velge denne standarden.



![Image](assets/fr/050.webp)



En advarsel vil vises. Dette er normalt: Med denne utvidede offentlige nøkkelen (`xpub`) kan du se alle adressene som er avledet fra seed (på den første kontoen). Den lar deg ikke bruke pengene dine, men den avslører strukturen i porteføljen din. Hvis den noen gang lekker, er det et problem for personvernet ditt, men ikke for sikkerheten til bitcoinsene dine: den lar deg se dem, men ikke bruke dem.



Klikk på `Jeg forstår` og deretter på `Eksporter Xpub` hvis du er fornøyd med informasjonen som vises.



SeedSigner genererer deretter xpuben din i form av en dynamisk QR-kode som inneholder alle dataene du trenger for å administrere porteføljen din i Sparrow wallet.



![Image](assets/fr/051.webp)



Du kan bruke styrespaken til å justere lysstyrken på skjermen for å gjøre det enklere å skanne QR-koder.



### 6.2 Importere en ny portefølje til Sparrow wallet



Sørg for at du har installert Sparrow wallet-programvaren på datamaskinen din. Hvis du ikke vet hvordan du laster ned, kontrollerer og installerer den riktig, kan du se hele veiledningen vår om emnet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Åpne Sparrow wallet på datamaskinen, og klikk deretter på `Fil → Importer Wallet` i menylinjen.



![Image](assets/fr/052.webp)



Bla ned til `SeedSigner`, og velg deretter `Scan...`. Webkameraet ditt åpnes: Skann den dynamiske QR-koden som vises på SeedSigner-skjermen.



![Image](assets/fr/053.webp)



Gi porteføljen et navn, og klikk deretter på `Opprett Wallet`. Sparrow vil da be deg om å angi et passord for å låse lokal tilgang til denne Wallet. Velg et sterkt passord: det beskytter tilgangen til porteføljedataene dine i Sparrow (offentlige nøkler, adresser, etiketter og transaksjonshistorikk). Dette passordet er ikke nødvendig for å gjenopprette porteføljen på et senere tidspunkt: bare Mnemonic-frasen din (og eventuelt passphrase) er nødvendig for dette formålet.



Jeg anbefaler at du lagrer dette passordet i en passordbehandler for å unngå å miste det.



![Image](assets/fr/054.webp)



Nøkkellageret ditt er nå importert.



![Image](assets/fr/055.webp)



Kontroller deretter at `Master-fingeravtrykket` som vises i Sparrow, stemmer overens med det som tidligere er registrert i SeedSigner.



SeedSigner og Sparrow wallet er nå sikkert koblet sammen. Sparrow fungerer som en komplett administrasjon av Interface, mens SeedSigner forblir den eneste enheten som kan signere transaksjonene dine. Du er nå klar til å motta og sende bitcoins i en fullstendig luftgapet konfigurasjon.



## 7. Motta og sende bitcoins



SeedSigner og Sparrow wallet er nå konfigurert til å fungere sammen. I denne siste delen skal vi se på hvordan du kan motta og sende bitcoins ved hjelp av denne konfigurasjonen.



### 7.1 Motta bitcoins



#### 7.1.1 Generering av et mottak Address



Åpne Sparrow wallet på datamaskinen din og lås opp SeedSigner Wallet med passordet ditt. Kontroller at programvaren er koblet til en server (hakk nederst til høyre). I sidepanelet klikker du på `Mottak`.



![Image](assets/fr/056.webp)



En ny Bitcoin Address vises. Du vil se :




- Teksten Address (begynner med `bc1p...` hvis du bruker P2TR, slik jeg gjør),
- Den tilhørende QR-koden,
- Et `Label`-felt for sporing av transaksjonene dine.



Jeg anbefaler på det sterkeste at du legger til en etikett på hver Bitcoin-kvittering på din Wallet. Dette vil gjøre det enkelt å identifisere opprinnelsen til hver UTXO og forbedre personvernhåndteringen din. Hvis du vil gå dypere inn i dette viktige emnet, kan du sjekke ut den dedikerte opplæringen på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

For å legge til en etikett skriver du bare inn et navn i feltet "Etikett", og bekrefter deretter.



For eksempel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Din Address er nå knyttet til denne etiketten i alle Sparrow-seksjoner.



![Image](assets/fr/057.webp)



#### 7.1.2 Address-verifisering på SeedSigner



Før du deler den mottatte Address, er det svært viktig å kontrollere at den tilhører din seed. Dette trinnet sikrer at SeedSigner vil kunne signere transaksjoner som er knyttet til denne Address. Det beskytter også mot mulige angrep der Sparrow viser en falsk Address. Husk at Sparrow kjører i et usikkert miljø (datamaskinen din), som har en mye større angrepsflate enn SeedSigner, som er helt isolert. Derfor bør du aldri tro blindt på en mottaker Address som vises på Sparrow før du har verifisert den med din Hardware Wallet.



På Sparrow klikker du på QR-koden til Address for å forstørre den: Den vil da vises i fullskjerm.



![Image](assets/fr/058.webp)



På din SeedSigner, fra hovedmenyen, velg `Scan`. Skann QR-koden som vises på dataskjermen, og velg deretter seed som tilsvarer Wallet (i mitt tilfelle fingeravtrykket `d4149b27`).



![Image](assets/fr/059.webp)



Hvis den skannede Address samsvarer med den som er avledet fra din seed, vil SeedSigner-skjermen vise meldingen: `Address bekreftet`.



![Image](assets/fr/060.webp)



Dette bekrefter at Address tilhører din Wallet, og at du trygt kan motta bitcoins fra den.



#### 7.1.3 Mottak av midler



Du kan nå kommunisere denne Address (i form av tekst eller QR-kode) til den personen eller avdelingen som skal sende deg Satss. Når transaksjonen har blitt sendt ut i nettverket, vil den vises i fanen `Transaksjoner` i Sparrow wallet.



![Image](assets/fr/061.webp)



### 7.2 Send bitcoins



Å sende bitcoins med en SeedSigner er en 3-trinns prosess:




- Opprettelse av transaksjoner i Sparrow ;
- Signatur av transaksjonen på SeedSigner ;
- Endelig distribusjon av transaksjonen via Sparrow.



All utveksling mellom de to enhetene skjer utelukkende ved hjelp av QR-koder.



#### 7.2.1 Opprette transaksjonen i Sparrow



I Sparrow wallet kan du klikke på fanen `Send` i venstre sidefelt. Jeg foretrekker imidlertid å bruke fanen `UTXO`, som lar deg praktisere "*Coin Control*". Denne metoden gir deg nøyaktig kontroll over UTXO-ene som brukes, slik at du kan kontrollere informasjonen du avslører under transaksjonen.



Velg myntene du vil bruke, i kategorien `UTXO`, og klikk deretter på `Send Selected`.



![Image](assets/fr/062.webp)



Fyll deretter ut transaksjonsfeltene:




- I `Betal til` limer du inn mottakerens Address eller klikker på kameraikonet for å skanne QR-koden;
- I `Label` legger du til en etikett for å spore denne utgiften;
- I `Beløp` angir du beløpet som skal sendes;
- Til slutt velger du avgiftssats basert på gjeldende markedsforhold (estimater er tilgjengelige på [Mempool.space] (https://Mempool.space/)).



Når feltene er fylt ut, må du kontrollere informasjonen nøye og deretter klikke på `Opprett transaksjon >>`.



![Image](assets/fr/063.webp)



Kontroller transaksjonsdetaljene for å forsikre deg om at alt er riktig, og klikk deretter på "Fullfør transaksjon for signering".



![Image](assets/fr/064.webp)



Transaksjonen er nå klar, men ennå ikke signert. For å vise [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) som en QR-kode, klikk på `Vis QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Signering av transaksjonen med SeedSigner



Slå på din SeedSigner og skann din SeedQR for å få tilgang til porteføljen din, som vanlig. Fra startskjermen velger du `Scan`, og skanner deretter QR-koden som vises på Sparrow.



![Image](assets/fr/066.webp)



Velg deretter seed som passer til porteføljen din.



![Image](assets/fr/067.webp)



SeedSigner oppdager automatisk at dette er en PSBT og viser et sammendrag av transaksjonen:




   - Beløpet som sendes,
   - Utgangsadresser,
   - Tilhørende transaksjonskostnader.



Klikk på `Review Details` og sjekk nøye all informasjon direkte på SeedSigner-skjermen. Det viktigste å sjekke er beløpet som er sendt, mottakerens Address og beløpet på eventuelle gebyrer.



![Image](assets/fr/068.webp)



Hvis alt er i orden, velger du `Godkjenn PSBT` for å signere transaksjonen ved hjelp av de(n) tilsvarende private nøkkelen(e).



![Image](assets/fr/069.webp)



Når den er signert, genererer SeedSigner en ny QR-kode som inneholder den signerte transaksjonen, klar til å skannes av Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Kringkasting av transaksjonen fra Sparrow



Nå som transaksjonen er gyldig, må den kringkastes i Bitcoin-nettverket, slik at den når en Miner som legger den til i en BLOCK.



På Sparrow klikker du på `QR Scan`.



![Image](assets/fr/071.webp)



Vis QR-koden som vises av SeedSigner (den for den signerte transaksjonen) til webkameraet. Sparrow vil dekode signaturen og vise alle transaksjonsdetaljer. Gjør en siste kontroll av at all informasjonen er korrekt, og klikk deretter på Broadcast Transaction for å kringkaste den i Bitcoin-nettverket.



![Image](assets/fr/072.webp)



Transaksjonen din har nå blitt sendt til Bitcoin-nettverket. Du kan følge med på fremdriften i fanen `Transaksjoner` i Sparrow wallet.



![Image](assets/fr/073.webp)



Du har nå lært det grunnleggende om hvordan du bruker SeedSigner. Hvis du ønsker å fordype deg og utforske mer avanserte bruksområder, kan du ta en titt på følgende veiledning:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Du kan også støtte utviklingen av SeedSigner-prosjektet med åpen kildekode ved å gi en donasjon i bitcoins!] (https://seedsigner.com/donate/)**



*Kreditt: Noen av bildene i denne veiledningen kommer fra [det offisielle nettstedet for SeedSigner-prosjektet] (https://seedsigner.com/) og [GitHub repository] (https://github.com/SeedSigner/seedsigner).*