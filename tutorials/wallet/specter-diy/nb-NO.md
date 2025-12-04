---
name: Specter DIY
description: Installasjonsveiledning for Spectre DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks skriver kode. Vi vet at noen må skrive programvare for å forsvare personvernet, og siden vi ikke kan få personvern med mindre vi alle gjør det, kommer vi til å skrive det.

*Et Cypherpunk-manifest - Eric Hughes - 9. mars 1993*


Ideen med prosjektet er å bygge en maskinvare-wallet fra hyllevare-komponenter.

Selv om vi har et utvidelseskort som plasserer alt i en fin formfaktor og hjelper deg med å unngå lodding, vil vi fortsette å støtte og opprettholde kompatibilitet med standardkomponenter.


![image](assets/fr/01.webp)


Vi ønsker også å holde prosjektet fleksibelt, slik at det kan fungere på et hvilket som helst annet sett med komponenter med minimale endringer. Kanskje du vil lage en maskinvare-wallet på en annen arkitektur (RISC-V?), med et lydmodem som kommunikasjonskanal - det skal du kunne gjøre. Det skal være enkelt å legge til eller endre funksjonalitet i Specter, og vi prøver å abstrahere logiske moduler så mye som mulig.


QR-koder er en standard måte for Specter å kommunisere med verten på. QR-koder er ganske praktiske og lar brukeren ha kontroll over dataoverføringen - hver QR-kode har en svært begrenset kapasitet, og kommunikasjonen skjer i én retning. Og det er luftovervåket - du trenger ikke å koble wallet til datamaskinen på noe tidspunkt.


For lagring av hemmeligheter støtter vi agnostisk modus (wallet glemmer alle hemmeligheter når den slås av), hensynsløs modus (lagrer hemmeligheter i applikasjonsmikrokontrolleren), og secure element-integrering kommer snart.


Hovedfokuset vårt er multisignaturoppsett med andre maskinvarelommebøker, men wallet kan også fungere som enkeltsignerer. Vi prøver å gjøre den kompatibel med Bitcoin Core der vi kan - PSBT for usignerte transaksjoner, wallet-beskrivelser for import/eksport av multisignaturlommebøker. For å kommunisere med Bitcoin Core på en enklere måte jobber vi også med [Specter Desktop app] (https://github.com/cryptoadvance/specter-desktop) - en liten python flask-server som snakker med din Bitcoin Core node.


Det meste av fastvaren er skrevet i MicroPython, noe som gjør koden enkel å revidere og endre. Vi bruker biblioteket [secp256k1](https://github.com/bitcoin-core/secp256k1) fra Bitcoin Core for elliptiske kurveberegninger og biblioteket [LittlevGL](https://lvgl.io/) for GUI.


## Ansvarsfraskrivelse


Prosjektet har modnet betydelig, slik at sikkerhetsnivået til Spectre-DIY nå kan sammenlignes med kommersielle maskinvarelommebøker på markedet. Vi har implementert en sikker oppstartslaster som verifiserer fastvareoppgraderinger, slik at du kan være sikker på at kun signert fastvare kan lastes opp til enheten etter førstegangsoppsett. I motsetning til kommersielle signeringsenheter må imidlertid bootloaderen installeres manuelt av brukeren, og den er ikke satt opp på fabrikken av enhetsleverandøren. Vær derfor ekstra oppmerksom under den første installasjonen av fastvaren, og sørg for at du verifiserer PGP-signaturer og flasher fastvaren fra en sikker datamaskin.


Hvis noe ikke fungerer, kan du åpne et problem her eller stille et spørsmål i [Telegram-gruppen] (https://t.me/+VEinVSYkW5TUl5Ai).


## Handleliste for Specter-DIY


Her beskriver vi hva du bør kjøpe, og i neste del forklarer vi hvordan du setter det sammen, og gir deg noen tips om kortet - strømbrytere, USB-porter osv.


### Oppdagelsesbrett


Hoveddelen av enheten er utviklerkortet:



- STM32F469I-DISCO-utviklerkort (f.eks. fra [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) eller [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB-kabel
- Standard MicroUSB-kabel for kommunikasjon via USB


Valgfritt, men anbefalt:


- [Waveshare QR-kodeskanner] (https://www.waveshare.com/barcode-scanner-module.htm) med lange pinnehoder som [disse] (https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) eller [disse] (https://www.amazon.com/gp/product/B015KA0RRU/) for å koble skanneren til kortet (4 pinnehoder trengs).


Vi jobber for tiden med et utvidelseskort som inkluderer et smartkortspor, QR-kodeskanner, batteri og et 3d-printet etui, men det inkluderer ikke hoveddelen - oppdagelseskortet som du må bestille separat. På denne måten er angrep på forsyningskjeden fortsatt ikke et problem, ettersom de sikkerhetskritiske komponentene kjøpes fra en tilfeldig elektronikkbutikk.


Du kan begynne å bruke Specter selv uten ekstra komponenter, men du vil kunne kommunisere med den via USB eller det innebygde SD-kortsporet. Hvis du bruker Specter via USB, betyr det at den ikke er luftovervåket, og du mister dermed en viktig sikkerhetsegenskap.


### QR-skanner


For QR-kodeskanner har du flere alternativer.


**Alternativ 1. Anbefalt ** Resonably god skanner fra Waveshare (40 $)


[Waveshare-skanner] (https://www.waveshare.com/barcode-scanner-module.htm) - du må finne en måte å montere den pent på, kanskje bruke en slags Arduino Prototype-skjold og litt ducktape.


Ingen lodding kreves, men hvis du har loddeferdigheter, kan du gjøre wallet mye finere ;)


**Alternativ 2.** Veldig fin skanner fra Mikroe, men ganske dyr (150 $):


[Strekkodeklikk] (https://www.mikroe.com/barcode-click) + [Adapter] (https://www.mikroe.com/arduino-uno-click-shield)


**Alternativ 3: Enhver annen QR-skanner


Du kan finne noen billige skannere i Kina. Kvaliteten er ofte ikke så bra, men du kan ta en sjanse. Kanskje til og med ESPcamera ville gjøre jobben. Du trenger bare å koble til strøm, UART (pinnene D0 og D1) og trigger til D5.


**Alternativ 4: Ingen skanner.


Da kan du bare bruke Specter med USB / SD-kort.


Med mindre du bygger din egen kommunikasjonsmodul som bruker noe annet i stedet for QR-koder - audiomodem, bluetooth eller hva som helst annet. Så snart den kan utløses og sende dataene over seriell, kan du gjøre hva du vil.


### Valgfrie komponenter


Hvis du legger til en liten powerbank eller en batteri- og strømlader/booster, blir wallet helt selvforsynt;)



## Montering av Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Koble til Waveshare strekkodeskanner


wallet-fastvaren konfigurerer skanneren for deg ved første kjøring, slik at det ikke er nødvendig med manuell forhåndskonfigurasjon.


Slik kobler du skanneren til kortet:


![image](assets/fr/02.webp)


For enkelhets skyld kan du kjøpe et Arduino Protype-skjold og lodde og montere alt på det (f.eks. [denne] (https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Strømstyring


På oversiden av kortet er det en jumper som definerer hvor det skal få strøm. Du kan endre jumperens posisjon og velge strømkilde til en av USB-portene eller VIN-pinnen og koble til et eksternt batteri der (bør være 5V).


### Skap for DIY


Ta en titt i mappen [enclosures] (https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Vær kreativ!


Sett sammen din egen Specter-DIY og send oss bildene (lag en pull-forespørsel eller ta kontakt med oss).


Ta en titt på [Galleri] (https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) med spøkelser satt sammen av fellesskapet!




## Installere den kompilerte koden


Med den sikre bootloaderen er den første installasjonen av fastvaren litt annerledes. Oppgraderinger er enklere og krever ikke at du kobler maskinvaren wallet til datamaskinen.


![video](https://youtu.be/eF4cgK_L6T4)


### Blinker innledende fastvare


**Hvis du ikke vil bruke binærfiler fra utgivelsene, kan du se [bootloader documentation] (https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) som forklarer hvordan du kompilerer og konfigurerer den til å bruke dine offentlige nøkler i stedet for våre.



- Hvis du oppgraderer fra versjoner under `1.4.0` eller laster opp fastvaren for første gang, bruker du `initial_firmware_<version>.bin` fra [releases](https://github.com/cryptoadvance/specter-diy/releases)-siden.
 - Verifiser signaturen til filen `sha256.signed.txt` mot [Stepans PGP-nøkkel] (https://stepansnigirev.com/ss-specter-release.asc)
 - Verifiser hashen til `initial_firmware_<version>.bin` mot hashen som er lagret i `sha256.signed.txt`
- Hvis du oppgraderer fra en tom bootloader eller hvis du ser en feilmelding om at fastvaren ikke er gyldig, kan du lese neste avsnitt - Blinke signert Specter-fastvare.
- Kontroller at strømbyttebryteren på oppdagelseskortet står i STLK-posisjon
- Koble oppdagelseskortet til datamaskinen via **miniUSB**-kabelen på toppen av kortet.
    - Kortet skal vises som en flyttbar disk med navnet `DIS_F469NI`.
- Kopier filen `initial_firmware_<version>.bin` til roten av filsystemet `DIS_F469NI`.
- Når kortet er ferdig med å blinke fastvaren, tilbakestiller kortet seg selv og starter på nytt til bootloaderen. Bootloader vil sjekke fastvaren og starte opp i hovedfastvaren. Hvis du ser en feilmelding om at ingen fastvare er funnet - følg oppdateringsinstruksjonene og last opp fastvare via SD-kort.
- Nå kan du sette strømbryteren der du vil ha den, og drive kortet fra powerbanken eller batteriet.


Noen ganger mislykkes det å blinke den opprinnelige fastvaren via copy-paste av `.bin`-filen - ofte på grunn av kabelen, eller hvis du kobler enheten via en USB-hub. I dette tilfellet kan du prøve noen ganger til (fungerer normalt i 2-3 forsøk).


Hvis det mislykkes hele tiden, kan du bruke [stlink] (https://github.com/stlink-org/stlink/releases/latest) open source-verktøy. Installer det og skriv inn i terminalen din: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Det fungerer vanligvis mye mer pålitelig.


### Oppgradering av fastvare



- Last ned `specter_upgrade_<version>.bin` fra [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Kopier denne binærfilen til roten av SD-kortet (FAT-formatert, maks. 32 GB)
 - Sørg for at bare én `specter_upgrade***.bin`-fil ligger i rotkatalogen
- Sett SD-kortet inn i SD-sporet på oppdagelseskortet, og slå på kortet
- Bootloader flasher fastvaren og varsler deg når den er ferdig.
- Start kortet på nytt - du vil se Spectre-DIY-grensesnittet nå, og det vil foreslå at du velger PIN-koden din


Når en ny versjon er ute, er det bare å laste ned `specter_upgrade_<version>.bin` fra utgivelsene, slippe den til SD-kortet og oppgradere enheten akkurat som i forrige trinn. Bootloader vil sørge for at bare signert firmware kan lastes inn på kortet.


### Slik finner du ut fastvareversjonen


Gå til menyen `Enhetsinnstillinger` - der vises versjonsnummeret under tittelen på skjermen.


## Bruk Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Sikkerheten til Specter-DIY


### Maskinvare


Displayet styres av applikasjonens MCU.


Sikker elementintegrasjon er ikke der ennå - for øyeblikket lagres hemmeligheter også på hoved-MCU-en. Men du kan bruke wallet uten å lagre hemmeligheten - du må skrive inn gjenopprettingsfrasen hver gang. Hvorfor huske lange passphrase hvis du kan huske hele huskeregelen?


Enheten bruker ekstern flash til å lagre noen filer (QSPI), men alle brukerfiler signeres av wallet og kontrolleres når de lastes inn.


QR-skannefunksjonaliteten ligger på en separat mikrokontroller, slik at all bildebehandling skjer utenfor den sikkerhetskritiske MCU-enheten. For øyeblikket styres USB og SD-kort fortsatt av hoved-MCU-en, så ikke bruk SD-kort og USB hvis du ønsker å redusere angrepsflaten.


### PIN-beskyttelse (brukerautentisering)


Under den første oppstarten genereres det en unik hemmelighet på hoved-MCU-enheten. Med denne hemmeligheten kan du kontrollere at enheten ikke er erstattet av en ondsinnet enhet - når du taster inn PIN-koden, ser du en liste med ord som forblir de samme så lenge hemmeligheten er der.


PIN-koden din sammen med denne unike hemmeligheten brukes til å generate en dekrypteringsnøkkel for Bitcoin-nøklene dine (hvis du lagrer dem). Så hvis angriperen skulle være i stand til å omgå PIN-skjermen, vil dekrypteringen likevel mislykkes.


Hvis du har låst fastvaren (TODO: legg til instruksjonslenke her), vil det effektivt låse hemmeligheten også, så hvis angriperen blinker en annen firmware til brettet, blir hemmeligheten slettet, og du vil kunne gjenkjenne den når du begynner å skrive inn PIN-koden - ordsekvensen vil være annerledes.


### Generering av gjenopprettingsfrasen


Dette er en av de viktigste delene av wallet - å generate nøkkelen på en sikker måte. For å gjøre dette på en god måte bruker vi flere kilder til entropi:



- TRNG på mikrokontrolleren. Egenutviklet, sertifisert og sannsynligvis bra, men vi stoler ikke på den
- Berøringsskjerm. Hver gang du berører skjermen, måler vi posisjonen og øyeblikket da berøringen skjedde (i mikrokontroller-ticks på 180 MHz).
- Innebygde mikrofoner - ikke ennå. Kortet har to mikrofoner, slik at maskinvaren wallet kan lytte til deg og blande disse dataene inn i entropipoolen.


All denne entropien blir hashet sammen og konvertert til gjenopprettingsfrasen din. Den resulterende entropien er alltid bedre enn noen av de individuelle kildene.


### Logikk på høyt nivå - lommebøker


Specter fungerer som en nøkkellager. Den inneholder private HD-nøkler som kan inngå i lommebøker. Lommebøker defineres av deskriptorene deres. Vi støtter også miniscript.


Hver wallet tilhører et bestemt nettverk. Dette betyr at hvis du har importert en wallet på `testnet`, vil den ikke være tilgjengelig på `mainnet` eller `regtest` - du må bytte til dette nettverket og importere wallet separat.


### Verifisering av transaksjoner


Følgende regler gjelder for transaksjoner som wallet skal signere:



- hvis det finnes blandede inndata fra forskjellige lommebøker, blir brukeren advart ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- endre utganger viser navnet på wallet de sendes til
- for å bruke et multisig- eller miniscript må du først importere wallet ved å legge til wallet-descriptor (via QR, USB eller SD-kort)


## Støtte for deskriptorer


Alle vanlige Bitcoin-beskrivelser fungerer. Bortsett fra det har vi noen få utvidelser:


### Flere forgreninger i deskriptorer


For å spare plass i QR-kodene tillater vi at du legger til deskriptorer med flere grener på én gang. Hvis du vil bruke `wpkh(xpub/0/*)` for mottaksadresser og `wpkh(xpub/1/*)` for endringsadresser, kan du kombinere dem i én enkelt deskriptor: `wpkh(xpub/{0,1}/*)` - wallet vil behandle den første indeksen i `{}`-settdelen som grenen for mottaksadresser og den andre som endringsadresser.


Du kan også angi mer enn to grener, og grenindeksene kan være forskjellige for ulike medunderskrivere, så denne deskriptoren er veldig rar, men helt gyldig:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Her vil wallet bruke skriptet fra `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))` for å motta adressenummer 17.


Det eneste kravet er at antallet indekser i alle settene er det samme (3 i tilfellet ovenfor).


### Standard avledninger


Hvis deskriptoren inneholder offentlige hovednøkler, men ikke inneholder jokertegnavledninger, vil standardavledningen `/{0,1}/*` bli lagt til alle utvidede nøkler i deskriptoren. Hvis minst én av xpubene har en jokertegnavledning, endres ikke beskrivelsen.


Deskriptoren `wpkh(xpub)` blir konvertert til `wpkh(xpub/{0,1}/*)`.


### Miniskript


Specter støtter miniskript, men støtter ikke kompilering fra policy til miniskript (fordi det er altfor dyrt). Vi utfører noen kontroller på miniskriptet, slik at bare `B`-skript er tillatt på toppnivå, og alle argumenter i underminiskript må ha egenskaper i henhold til [spec](http://bitcoin.sipa.be/miniscript/).


Du kan bruke [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) til å generate en deskriptor fra en policy og deretter importere den til wallet.


For eksempel kan en policy "Jeg kan bruke penger nå, eller om 100 dager kan min kone bruke penger" konverteres til wallet på denne måten:


Policy: `eller(9@pk(xpubA),and(older(14400),pk(B)))` (min nøkkel er 9 ganger mer sannsynlig)


Miniskript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))``


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))``


Siden vi her ikke har noen jokertegnavledninger, vil standardavledningene `/{0,1}/*` bli lagt til i xpubene.



---

MIT-lisens


Opphavsrett (c) 2019 cryptoadvance


---