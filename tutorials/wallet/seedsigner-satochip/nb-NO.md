---
name: Satochip x SeedSigner
description: Hvordan bruker jeg en Satochip med SeedSigner?
---

![cover](assets/cover.webp)



*Takk til [Crypto Guide] (https://www.youtube.com/@CryptoGuide/) for fork av SeedSigner-fastvaren for smartkortstøtte, som vi vil bruke i denne veiledningen



---

Satochip er en maskinvare i wallet-smartkortformat med et EAL6+-sertifisert sikkerhetselement, en av de høyeste sikkerhetsstandardene. Den er designet og produsert av det belgiske selskapet med samme navn: Satochip.



Satochip har en pris på rundt 25 euro, og skiller seg ut fra konkurrentene ved at den gir valuta for pengene. Takket være den sikre brikken er den motstandsdyktig mot fysiske angrep. I tillegg er kildekoden til appleten helt åpen kildekode, lisensiert under *AGPLv3*.



På den annen side innebærer formatet visse funksjonelle begrensninger. Den største ulempen med Satochip er fraværet av en integrert skjerm: Brukerne må derfor signere transaksjoner i blinde, og kun stole på datamaskinens skjerm.



For å overkomme denne svakheten er det spesielt interessant å bruke den sammen med en SeedSigner. I dette oppsettet foregår kommunikasjonen ikke lenger direkte mellom datamaskinen og Satochip, men via utveksling av QR-koder mellom datamaskinen og SeedSigner. SeedSigneren fungerer da som en tillitsskjerm: Den viser informasjonen som skal signeres, mens selve signeringen utføres av Satochip. I motsetning til konvensjonell bruk av SeedSigner (eller til og med bruk i kombinasjon med Seedkeeper), blir seed aldri lastet inn i SeedSigner. SeedSigner blir dermed Satochips skjerm, noe som eliminerer risikoen forbundet med blind signering.



Hvis vi ser på problemet fra den andre siden, vil bruk av SeedSigner med en Satochip fylle et stort hull i SeedSigner: muligheten til å lagre og bruke seed i en secure element.



Etter min mening gir denne konfigurasjonen flere fordeler sammenlignet med konvensjonelle maskinvarelommebøker:




- Satochip koster rundt 25 euro, og siden appleten er åpen kildekode, kan du installere den selv på et tomt smartkort. Deretter må du legge til kostnadene for SeedSigner-komponentene og utvidelsen for lesing av smartkort: Avhengig av hvor du kjøper denne maskinvaren, bør totalsummen ligge på mellom 70 og 100 euro.
- All programvaren som er involvert i oppsettet, er åpen kildekode: SeedSigner-fastvaren og Satochip-appleten.
- Du drar nytte av et sertifisert sikkerhetselement.
- Konfigurasjonen kan gjøres helt selv, uten bruk av maskinvare som eksplisitt er beregnet for Bitcoin-bruk, noe som kan gi en form for plausibel benektelse og motstand mot visse eksterne trusler (inkludert, avhengig av land, statlig press). Dette er også en interessant løsning hvis tilgangen til kommersielle maskinvarelommebøker er begrenset eller umulig i din region.




## 1. Nødvendige materialer



For å utføre dette oppsettet trenger du følgende elementer:




- Det vanlige utstyret som trengs av en klassisk SeedSigner :
 - en Raspberry Pi Zero med GPIO-pinner,
 - 1.3" Waveshare-skjerm,
 - et kompatibelt kamera,
 - et microSD-kort.



![Image](assets/fr/01.webp)





- SeedSigner-utvidelsessettet, som er tilgjengelig [fra den offisielle Satochip-butikken] (https://satochip.io/product/seedsigner-extension-kit/), lar deg lese og skrive til et smartkort direkte fra SeedSigner. Et annet alternativ er å bruke [en ekstern smartkortleser](https://satochip.io/product/chip-card-reader/), som kan kobles til en Micro-USB-port på Raspberry Pi med en kabel. Jeg har imidlertid ikke testet denne løsningen selv;
- [En Satochip](https://satochip.io/product/satochip/), eller alternativt et [tomt smartkort](https://satochip.io/product/card-for-diy-project/) som du kan installere Satochip-appleten på (utvidelsessettet som selges av Satochip, inneholder allerede et tomt smartkort). Satochips utvidelsessett støtter også formatet [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Du kan altså velge dette formatet hvis du foretrekker det.



![Image](assets/fr/02.webp)



For mer informasjon om utstyret som kreves for å sette sammen en SeedSigner, se del 1 av denne andre veiledningen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Installer fastvare



For å bruke din SeedSigner med en Satochip, må du installere en alternativ fastvare, forskjellig fra den originale SeedSigner, for å støtte smartkortlesing. For dette [anbefaler jeg å bruke fork fra "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Last ned [den nyeste versjonen av bildet](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) som tilsvarer Raspberry Pi-modellen du bruker.



![Image](assets/fr/03.webp)



Hvis du ikke allerede har det, laster du ned programvaren [Balena Etcher] (https://etcher.balena.io/), og gjør deretter følgende:




- Sett microSD-kortet inn i datamaskinen;
- Start Etcher ;
- Velg `.zip`-filen du nettopp har lastet ned;
- Velg microSD-kortet som mål;
- Klikk på `Flash!`.



![Image](assets/fr/04.webp)



Vent til prosessen er fullført: microSD-kortet er nå klart til bruk. Du kan nå gå videre til å montere enheten.



For mer informasjon om installasjon av fastvare og verifisering av programvare (et trinn jeg anbefaler på det sterkeste at du tar), se følgende veiledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montering av smartkortleseren



Begynn med å installere kameraet på Raspberry Pi Zero ved å sette det forsiktig inn i kamerapinnen og låse det med den svarte tappen. Plasser deretter Pi på bunnen av kabinettet, og sørg for at portene er på linje med de tilsvarende åpningene.



![Image](assets/fr/05.webp)



Deretter kobler du smartkortleseren til Raspberry Pi Zeros GPIO-pinner.



![Image](assets/fr/06.webp)



Skyv plastdekselet over smartkortleseren til det er riktig plassert.



![Image](assets/fr/07.webp)



Legg deretter skjermen til GPIO-pinnene i utvidelsen.



![Image](assets/fr/08.webp)



Til slutt setter du microSD-kortet som inneholder fastvaren, inn i sideporten på Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Du kan nå koble til SeedSigner enten via Raspberry Pi Zeros Micro-USB-port eller via USB-C-porten på utvidelsen. Begge alternativene fungerer. Vent noen sekunder på oppstart, så bør du se velkomstskjermen vises.



![Image](assets/fr/10.webp)



For mer informasjon om det første oppsettet av SeedSigner, anbefaler jeg at du leser del 4 av den følgende veiledningen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flash et smartkort med Satochip-appleten (valgfritt)



Hvis du allerede eier en Satochip, kan du hoppe over dette trinnet og gå rett til trinn 4. I dette avsnittet skal vi se på hvordan du installerer Satochip-appleten på et tomt smartkort (gjør det selv-metoden). Appleten er ganske enkelt et lite program som kjører på smartkortet, og som gjør det mulig for oss å styre bestemte funksjoner.



For å komme i gang åpner du menyen `Verktøy > Smartkortverktøy` på SeedSigner.



![Image](assets/fr/11.webp)



Velg deretter `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Sett smartkortet ditt inn i SeedSigner-leseren, med brikken vendt nedover, og velg `Satochip`-appleten.



![Image](assets/fr/13.webp)



Vær tålmodig under installasjonen: prosessen kan ta flere titalls sekunder.



![Image](assets/fr/14.webp)



Når appleten er installert, kan du gå videre til trinn 4.



![Image](assets/fr/15.webp)




## 5. Opprette og lagre seed



### 5.1. Generer seed



Nå som du har fått all maskinvare og programvare til å fungere som den skal, kan du fortsette med å lage din Bitcoin-portefølje. Dette gjør du ved å koble til SeedSigner og deretter generate seed som med en vanlig SeedSigner, enten ved å kaste terningen eller ved å ta et bilde:




- Gå til menyen `Verktøy > Kamera / Terningkast`;
- Følg deretter entropigenereringsprosessen i henhold til den valgte metoden;
- Til slutt tar du en sikkerhetskopi av seed på et fysisk medium og kontrollerer sikkerhetskopien nøye.



![Image](assets/fr/16.webp)



Hvis du vil se detaljene i denne prosedyren, kan du følge del 5 av denne veiledningen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Lagre seed på en Seedkeeper



Når seed er generert, er dette den eneste gangen den befinner seg i SeedSigners RAM. I mitt tilfelle vil jeg lagre den på en [Seedkeeper] (https://satochip.io/product/seedkeeper/), et annet Satochip-produkt som er utviklet for å lagre hemmeligheter. Jeg vil bruke denne enheten som en siste utvei, i tilfelle jeg mister Satochipen min.



Hvilken sikkerhetskopistrategi du velger her, avhenger av dine preferanser, men det er viktig å ha minst én kopi av minnefrasen din, enten på et fysisk medium (papir eller metall) eller, som her, i en Seedkeeper. Du kan også multiplisere antall sikkerhetskopier etter behov. Hvis du vil ha mer informasjon om strategier for sikkerhetskopiering av porteføljer, foreslår jeg at du leser denne veiledningen :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

For å sikkerhetskopiere seed på en Seedkeeper, går du direkte til menyen `Backup Seed`.



![Image](assets/fr/17.webp)



Sett deretter Seedkeeperen inn i smartkortleseren, og velg `Til SeedKeeper`.



![Image](assets/fr/18.webp)



Tast inn PIN-koden din for å låse den opp.



![Image](assets/fr/19.webp)



Velg en "etikett" for å enkelt identifisere de ulike hemmelighetene som er lagret på Seedkeeper. Du kan for eksempel bare beholde wallet-avtrykket eller eksplisitt angi `Seed`. Valget avhenger av dine preferanser og risiko.



![Image](assets/fr/20.webp)



Hvis sikkerhetskopieringsstrategien din utelukkende baserer seg på denne Seedkeeperen, anbefaler jeg på det sterkeste at du kjører en tom gjenopprettingstest nå, og deretter sammenligner fingeravtrykkene for å kontrollere at sikkerhetskopien fungerer.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper PIN-koden bør være så lang og tilfeldig som mulig, for å forhindre forsøk på brute force i tilfelle fysisk kompromittering av kortet. Du bør også ta en sikkerhetskopi av denne PIN-koden, lagret et annet sted enn i Seedkeeper. Uten denne PIN-koden vil du ikke kunne få tilgang til mnemonikken som er lagret i Seedkeeper, og bitcoinsene dine vil gå tapt permanent.



### 5.3. Spar seed på Satochip



Nå som porteføljen din er generert, lagret og verifisert, skal vi overføre den til Satochip. For å gjøre dette må du sørge for at seed er lastet inn i SeedSigners RAM. Gå deretter til `Verktøy > Smartkortverktøy > Satochip-funksjoner`.



![Image](assets/fr/21.webp)



Sett Satochip inn i smartkortleseren, og velg deretter `Initialiser med frø`.



![Image](assets/fr/22.webp)



Enheten ber deg om å taste inn Satochip PIN-koden; ettersom kortet er nytt og ikke er initialisert, finnes det ingen PIN-kode ennå. Skriv inn en hvilken som helst kode for å hoppe over dette trinnet (det er ikke en blokkeringskode).



![Image](assets/fr/23.webp)



SeedSigner oppdager at Satochip ikke har blitt initialisert. Klikk på `Jeg forstår` for å bekrefte.



![Image](assets/fr/24.webp)



Deretter kan du stille inn Satochip PIN-koden, fra 4 til 16 tegn. For å styrke sikkerheten til din wallet bør du velge en lang, tilfeldig kode: Det er den eneste beskyttelsen mot fysisk tilgang til minnefrasen din.



Husk å lagre PIN-koden så snart den er opprettet, enten i en sikker passordbehandler eller på et fysisk medium, avhengig av din personlige strategi. I sistnevnte tilfelle må du sørge for å aldri oppbevare mediet som inneholder PIN-koden på samme sted som Satochip, ellers vil beskyttelsen bli ubrukelig. Det er viktig å ha en sikkerhetskopi: **Uten denne PIN-koden vil du ikke kunne få tilgang til seed, og bitcoinsene dine vil gå tapt for alltid**.



![Image](assets/fr/25.webp)



SeedSigner spør deg deretter om hvilken seed du vil importere til Satochip. Velg den som har et fingeravtrykk som samsvarer med porteføljen du nettopp har opprettet.



![Image](assets/fr/26.webp)



Din seed er nå importert til Satochip.



![Image](assets/fr/27.webp)



Du kan nå slå av SeedSigner.



Hvis du ønsker å bruke en passphrase BIP39 for å forbedre sikkerheten til din wallet, kan du se del 6 av denne veiledningen:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importer wallet til Sparrow



Nå som porteføljen din er oppe og går, importerer vi den offentlige informasjonen ("*keystore*") til Sparrow Wallet eller en annen programvare for porteføljeforvaltning. Denne programvaren vil bli brukt til å opprette, distribuere og spore transaksjonene dine. Den vil imidlertid ikke kunne signere dem, ettersom det kun er Satochip (og eventuelle sikkerhetskopier) som har de private nøklene som trengs for denne operasjonen.



### 6.1 Klargjøring av SeedSigner og Satochip



Sett inn microSD-kortet som inneholder operativsystemet, og slå deretter på SeedSigner. For øyeblikket kan den ikke gjøre noe, siden den ennå ikke kjenner til seed-en din. Du må begynne med å sette Satochip inn i smartkortleseren, siden det er den som inneholder seed-en din.



Gå til menyen Verktøy > Smartkortverktøy > Satochip-funksjoner på startskjermen.



![Image](assets/fr/28.webp)



Klikk deretter på "Eksporter Xpub".



![Image](assets/fr/29.webp)



Velg porteføljetype. I vårt tilfelle er det en enkeltportefølje: velg `Single Sig`.



![Image](assets/fr/30.webp)



Deretter kommer valget av skriptstandard. Velg den nyeste: `Native SegWit`.



![Image](assets/fr/31.webp)



Til slutt velger du `Coordinator`, dvs. programvaren for porteføljeforvaltning du ønsker å bruke. Her bruker vi Sparrow Wallet.



![Image](assets/fr/32.webp)



En advarsel vises: dette er helt normalt. Den utvidede offentlige nøkkelen (`xpub`) lar deg se alle adressene som er avledet fra din seed (på den første kontoen). Den gir deg imidlertid ikke tilgang til midlene dine: avsløring av den ville kompromittere personvernet ditt, men ikke sikkerheten til bitcoinsene dine. Med andre ord lar den deg observere saldoen din, men ikke bruke dem.



Klikk på `Jeg forstår`.



![Image](assets/fr/33.webp)



Skriv deretter inn PIN-koden til Satochip for å låse den opp. Dette er koden du definerte og lagret i trinn 5.



![Image](assets/fr/34.webp)



Til slutt klikker du på "Eksporter Xpub" hvis du er fornøyd med informasjonen som vises.



![Image](assets/fr/35.webp)



SeedSigner genererer deretter xpuben din i form av en dynamisk QR-kode, som inneholder alle dataene du trenger for å administrere porteføljen din i Sparrow Wallet. Du kan justere lysstyrken på skjermen ved hjelp av styrespaken for å gjøre det enklere å skanne QR-koden.



### 6.2 Importere en ny portefølje til Sparrow Wallet



Forsikre deg om at Sparrow Wallet-programvaren er installert på datamaskinen din. Hvis du ikke vet hvordan du laster den ned, sjekker ektheten og installerer den riktig, kan du se hele veiledningen vår om emnet :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Åpne Sparrow Wallet på datamaskinen, og klikk deretter på `Fil → Importer Wallet` i menylinjen.



![Image](assets/fr/36.webp)



Bla ned til `SeedSigner`, og velg deretter `Scan...`. Webkameraet ditt aktiveres: Skann den dynamiske QR-koden som vises på SeedSigner-skjermen.



![Image](assets/fr/37.webp)



Gi porteføljen et navn, og klikk deretter på "Opprett Wallet". Sparrow vil da be deg om å angi et passord for å låse lokal tilgang til denne wallet. Velg et sterkt passord: det beskytter dataene dine i Sparrow (offentlige nøkler, adresser, etiketter og transaksjonshistorikk). Dette passordet er imidlertid ikke nødvendig for å gjenopprette wallet i fremtiden: det er bare minnefrasen din (og eventuelt passphrase) som er nødvendig.



Jeg anbefaler at du lagrer dette passordet i en passordbehandler, slik at du unngår å miste det.



![Image](assets/fr/38.webp)



Nøkkellageret ditt har blitt importert.



![Image](assets/fr/39.webp)



Sjekk nå at `Master-fingeravtrykket` som vises i Sparrow Wallet, stemmer overens med det som tidligere ble funnet på SeedSigner.



SeedSigner vil deretter be deg om å skanne en tilfeldig mottakeradresse fra din Sparrow wallet for å bekrefte gyldigheten av importen.



![Image](assets/fr/40.webp)



Satochip (via SeedSigner) og Sparrow Wallet er nå sikkert koblet sammen. Sparrow fungerer som et komplett administrasjonsgrensesnitt, mens Satochip forblir den eneste enheten som kan signere transaksjonene dine. Du er nå klar til å motta og sende bitcoins i en fullstendig luftgapet konfigurasjon.



![Image](assets/fr/41.webp)



## 7. Mottak og sending av bitcoins



Satochip og Sparrow Wallet er nå konfigurert til å fungere sammen. I denne delen forklarer vi trinn for trinn hvordan du mottar og sender bitcoins i denne modusen.



### 7.1 Motta bitcoins



#### 7.1.1 Generering av en mottaksadresse



Åpne Sparrow Wallet på datamaskinen din og lås opp `Satochip-SeedSigner` wallet ved hjelp av passordet ditt. Kontroller at programvaren er koblet til en server (indikator nederst til høyre). Klikk deretter på `Mottak` i sidefeltet.



![Image](assets/fr/42.webp)



En ny Bitcoin-adresse vises. Du vil finne :




- Adressen i tekstformat (begynner med `bc1q...` hvis du bruker P2WPKH, som i dette eksempelet) ;
- Den tilhørende QR-koden ;
- Et `Label`-felt, nyttig for å spore transaksjonene dine.



Jeg anbefaler på det sterkeste at du legger til en etikett på hver bitcoin-kvittering i din wallet. Dette vil hjelpe deg med å enkelt identifisere opprinnelsen til hver UTXO og bedre administrere personvernet ditt. For å finne ut mer om dette viktige emnet, sjekk ut den dedikerte opplæringen på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

For å legge til en etikett skriver du bare inn et navn i feltet "Etikett", og bekrefter deretter.



For eksempel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Adressen din er nå knyttet til denne etiketten i alle Sparrow-seksjoner.



![Image](assets/fr/43.webp)



#### 7.1.2 Address-verifisering på SeedSigner



Før du formidler mottakeradressen til betaleren, er det viktig å kontrollere at den tilhører din seed. Dette trinnet sikrer at Satochip kan signere transaksjoner som er knyttet til denne adressen. Det forhindrer også potensielle angrep der Sparrow viser en falsk adresse. Husk at Sparrow kjører i et usikkert miljø (datamaskinen din), der angrepsflaten er langt større enn for Satochip, som er helt isolert. Derfor bør du aldri stole blindt på adressene som vises i Sparrow før du har sjekket dem på wallet-maskinvaren din.



I Sparrow kan du klikke på QR-koden til adressen for å forstørre den: Den vises da i fullskjerm.



![Image](assets/fr/44.webp)



Sett Satochip-kortet inn i leseren på SeedSigner, og velg deretter `Scan` fra hovedmenyen. Skann QR-koden som vises på datamaskinen, og velg deretter `Bruk Satochip-kort`.



![Image](assets/fr/45.webp)



Bekreft deretter hvilken type skript som brukes (i dette tilfellet `Native SegWit`), skriv inn Satochip PIN-koden for å låse den opp, og valider `xpub`-informasjonen.



![Image](assets/fr/46.webp)



Hvis den skannede adressen samsvarer med den som er utledet fra din seed, vil SeedSigner vise meldingen: `Address bekreftet`.



![Image](assets/fr/47.webp)



Da kan du være sikker på at adressen tilhører porteføljen din.



#### 7.1.3 Mottak av midler



Du kan nå sende denne adressen i tekstform eller via QR-koden til den personen eller avdelingen som skal sende deg satss. Når transaksjonen er sendt ut i nettverket, vil den vises i fanen `Transaksjoner` i Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Send bitcoins



Å sende bitcoins med Satochip-SeedSigner-konfigurasjonen innebærer tre trinn:




- Opprettelse av transaksjoner i Sparrow ;
- Signering av denne transaksjonen på Satochip, via SeedSigner ;
- Til slutt sendes transaksjonen over nettverket fra Sparrow.



All utveksling mellom de to enhetene skjer utelukkende via QR-koder.



#### 7.2.1 Opprette transaksjonen i Sparrow



I Sparrow Wallet kan du opprette en transaksjon ved å klikke på `Send`-fanen i venstre sidefelt. Jeg foretrekker imidlertid å bruke fanen `UTXO`, som lar deg praktisere *Coin Control*. Denne metoden gir deg nøyaktig kontroll over UTXO-ene som brukes, slik at du kan begrense informasjonen som avsløres under transaksjonene dine.



Velg myntene du vil bruke, i kategorien `UTXO`, og klikk deretter på `Send Selected`.



![Image](assets/fr/49.webp)



Fyll deretter ut transaksjonsfeltene:




- I `Betal til` limer du inn mottakerens adresse eller skanner QR-koden deres ved hjelp av kameraikonet ;
- I `Label` legger du til en etikett for å spore denne utgiften;
- I `Beløp` angir du beløpet som skal sendes;
- Til slutt velger du ladehastighet i henhold til gjeldende nettverksforhold (estimater er tilgjengelige på [mempool.space] (https://mempool.space/)).



Når du har fylt ut alle feltene, går du nøye gjennom informasjonen og klikker deretter på `Opprett transaksjon >>`.



![Image](assets/fr/50.webp)



Kontroller transaksjonsdetaljene en siste gang for å se at de er korrekte, og klikk deretter på "Fullfør transaksjon for signering".



![Image](assets/fr/51.webp)



Transaksjonen er nå klar, men er ennå ikke signert. For å vise [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) som en QR-kode, klikk på `Vis QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Signering av transaksjonen med Satochip



Slå på SeedSigner og sett inn Satochip som vanlig. Fra startskjermen velger du `Scan`, og skanner deretter QR-koden som vises på Sparrow.



![Image](assets/fr/53.webp)



Velg alternativet `Bruk Satochip-kort`.



![Image](assets/fr/54.webp)



Tast inn PIN-koden for å låse opp smartkortet.



![Image](assets/fr/55.webp)



SeedSigner oppdager at dette er en PSBT og viser et sammendrag av transaksjonen:




   - Beløpet som sendes,
   - Destinasjonsadresser,
   - Tilhørende transaksjonskostnader.



Klikk på `Review Details` og gransk all informasjonen direkte på SeedSigner-skjermen. De viktigste punktene å sjekke er beløpene som er sendt, destinasjonsadressene og transaksjonsgebyrene.



![Image](assets/fr/56.webp)



Hvis alt er i orden, velger du `Godkjenn PSBT` for å signere transaksjonen ved hjelp av Satochip.



![Image](assets/fr/57.webp)



Når signaturen er fullført, genererer SeedSigner en ny QR-kode som inneholder den signerte transaksjonen, klar til å skannes av Sparrow.



#### 7.2.3 Kringkasting av transaksjonen fra Sparrow



Nå som transaksjonen er signert og validert, gjenstår det bare å kringkaste den i Bitcoin-nettverket slik at en utvinner kan inkludere den i en blokk. I Sparrow klikker du på `Scan QR`.



![Image](assets/fr/58.webp)



Vis QR-koden som vises på SeedSigner (den som inneholder den signerte transaksjonen) til webkameraet. Sparrow vil da vise alle transaksjonsdetaljene. Kontroller at all informasjonen er korrekt, og klikk deretter på "Broadcast Transaction" for å kringkaste den på Bitcoin-nettverket.



![Image](assets/fr/59.webp)



Transaksjonen din er nå overført til nettverket. Du kan følge med på bekreftelsen i fanen `Transaksjoner` i Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Få tilbake wallet



Som vi har sett i de foregående avsnittene, er det flere måter å sikkerhetskopiere gjenopprettingsfrasen din på, avhengig av sikkerhetsstrategien din, i tillegg til Satochip :




- Bruk av en klassisk *SeedQR* med SeedSigner ;
- Ved å registrere den mnemotekniske frasen på et fysisk medium;
- Eller ved å lagre den på en Seedkeeper, som forklart i avsnitt 5.2.



Uansett er det to hovedsituasjoner der du må gripe inn: tap av Satochip eller tap av SeedSigner. La oss ta en titt på hvordan du skal reagere i hvert av disse scenariene.



### 8.1. Hent wallet med Satochip



Hvis du fortsatt har Satochipen din, men SeedSigneren din er ødelagt eller mistet, er situasjonen ganske enkel å håndtere, siden wallet fortsatt er i Satochipen.



Det beste alternativet er å anbefale de nødvendige komponentene og bygge opp en ny SeedSigner fra bunnen av. Ettersom dette er en "stateless" enhet, spiller det ingen rolle om du bruker den samme eller en annen SeedSigner: så lenge du kan sette inn Satochip-en din, vil alt fungere normalt.



Hvis du ikke ønsker å bygge en ny, kan du også bruke Satochip på den klassiske måten, dvs. direkte fra datamaskinen din, uten å gå gjennom SeedSigner. Denne metoden fungerer perfekt, men den reduserer sikkerheten til din Bitcoin wallet betraktelig: du mister "*air-gapped*"-isolasjonen og må nå signere i blinde, siden SeedSigner fungerte som en betrodd skjerm. Dette kan imidlertid være en midlertidig løsning i en nødsituasjon, eller hvis du ikke har mulighet til å gjenoppbygge en SeedSigner.



For å gjøre dette trenger du en USB-smartkort- eller NFC-leser. Åpne wallet som du ønsker å gjenopprette i Sparrow, gå deretter til fanen "Innstillinger" og klikk på "Erstatt".



![Image](assets/fr/61.webp)



Sett inn Satochip i smartkortleseren som er koblet til datamaskinen, og klikk deretter på `Importer` ved siden av `Satochip`.



![Image](assets/fr/62.webp)



Til slutt skriver du inn PIN-koden til smartkortet for å låse det opp. Deretter får du tilgang til wallet, kan opprette transaksjoner og signere dem direkte ved hjelp av den tilkoblede Satochip-enheten.



### 8.2. Hent porteføljen din med SeedSigner



Det andre, mer delikate scenariet er når du mister tilgangen til Satochipen din som inneholder seed: enten den er ødelagt, mistet, stjålet eller du har glemt PIN-koden. Hvis Satochipen din har blitt stjålet eller forlagt, anbefaler vi på det sterkeste at du umiddelbart overfører bitcoinsene dine til en helt ny wallet, generert med en annen seed, så snart du har fått tilbake tilgangen til pengene dine. Dette sikrer at en potensiell angriper aldri kan få tilgang til dine Satochip.



For å få tilgang til porteføljen din igjen og flytte midlene dine, laster du ganske enkelt seed inn i SeedSigner. Avhengig av hvilket backupmedium du brukte, har du flere alternativer:





- Skriv inn den mnemoniske frasen manuelt i menyen `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skann *SeedQR* ved å klikke på "Skann"-knappen på startsiden.



![Image](assets/fr/64.webp)





- Eller last inn seed fra en Seedkeeper via menyen `Seeds > From SeedKeeper` (dette er metoden jeg bruker i denne veiledningen). Du trenger bare å taste inn Seedkeeper-PIN-koden og velge hemmeligheten som skal brukes som seed på SeedSigner.



![Image](assets/fr/65.webp)



Når seed er lastet inn i SeedSigner, uansett hvilken metode du bruker, vil du kunne signere en eller flere skannetransaksjoner for å flytte bitcoinsene dine til en ny, ukompromittert wallet. For å finne ut hvordan du gjør dette, se del 7.2 av følgende veiledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nå vet du hvordan du kan bruke Satochip til å administrere Bitcoin-porteføljen din på en sikker måte i kombinasjon med SeedSigner.



Hvis dette oppsettet har overbevist deg, ikke nøl med å støtte prosjektene som gjør det mulig:




- Ved å kjøpe utstyret ditt direkte [på Satochips nettsted] (https://satochip.io/shop/);
- Ved å gi [en donasjon til SeedSigner-prosjektet] (https://seedsigner.com/donate/);
- Ved å abonnere på [Crypto Guides YouTube-kanal] (https://www.youtube.com/@CryptoGuide/), som drives av personen som vedlikeholder GitHub-depotet som er vert for den modifiserte fastvaren vi brukte i denne opplæringen.