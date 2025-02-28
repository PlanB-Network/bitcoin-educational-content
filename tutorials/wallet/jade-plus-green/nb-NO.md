---
name: Jade Plus - Grønn
description: Konfigurer enkelt Jade Plus med Green
---
![cover](assets/cover.webp)

Jade Plus er en maskinvarelommebok kun for Bitcoin, designet av Blockstream. Det er etterfølgeren til den klassiske Jade, med programvareforbedringer, flere alternativer og redesignet ergonomi for mer intuitiv bruk. Denne nye versjonen har en fantastisk 1,9-tommers LCD-skjerm med et bredere fargespekter enn forgjengeren. Knapper og menynavigering har også blitt optimalisert.

Jade Plus kan brukes på flere måter: via en kablet USB-C-tilkobling, i "*Air-Gap*"-modus med et micro SD-kort (adapter kreves), via Bluetooth eller til og med ved å utveksle QR-koder takket være det integrerte kameraet. Denne maskinvarelommeboken er batteridrevet.

Den er tilgjengelig fra $ 149,99 i den grunnleggende svarte versjonen, og prisen kan stige med opptil $ 20 for versjonene "* Genesis Grey *" eller "*Lunar Silver *". Jade Plus er derfor et interessant valg, med avanserte funksjoner som kan sammenlignes med avanserte maskinvarelommebøker som Coldcard Q eller Passport V2, men til en ganske lav pris, nær mellomklassemodeller.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus er kompatibel med de fleste programvarer for porteføljeforvaltning. Her er en oversikt over kompatibiliteten i skrivende stund (januar 2025):

| Skrivebord | Mobil | USB | Bluetooth | QR | JadeLink | Administrasjonsprogramvare

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 |

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |



blueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

I denne veiledningen setter vi opp og bruker Jade Plus med Blockstreams mobilapp Green Wallet via en Bluetooth-tilkobling. Dette oppsettet er ideelt for nybegynnere. Hvis du er ute etter en mer avansert tilnærming, anbefaler jeg at du tar en titt på denne veiledningen, der vi bruker Jade Plus med Sparrow Wallet i QR-kodemodus:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## Sikkerhetsmodellen Jade Plus

Jade Plus bruker en sikkerhetsmodell basert på et "virtuelt sikkert element", materialisert av et "blindt orakel". Konkret kombinerer denne mekanismen PIN-koden som brukeren har valgt, en hemmelighet på Jade og en hemmelighet hos oraklet (en server som vedlikeholdes av Blockstream), for å skape en AES-256-nøkkel som distribueres over to enheter. Under initieringen sikrer en ECDH-utveksling kommunikasjonen med oraklet, og krypterer gjenopprettingsfrasen på maskinvarelommeboken. I praksis trenger du tilgang til :


- Til selve Jade Plus-enheten;
- Til PIN-kode for å låse opp enheten ;
- Og til oraklets hemmelighet.

Den største fordelen med denne tilnærmingen er fraværet av et enkelt feilpunkt på maskinvarenivå, siden hvis en angriper noen gang får tilgang til Jade, må både Jade og oraklet kompromitteres for å få ut nøklene. Denne modellen betyr også at Jade Plus er helt åpen kildekode, slik at man unngår begrensningene som er forbundet med bruk av ekte fysiske sikkerhetselementer, som for eksempel de som brukes på Ledger.

Ulempen med dette systemet er at bruken av Jade Plus avhenger av oraklet som vedlikeholdes av Blockstream. Hvis dette oraklet blir utilgjengelig, er det ikke lenger mulig å bruke maskinvarelommeboken direkte med PIN-koden. Dette betyr imidlertid ikke at bitcoinsene dine er tapt, da de fortsatt kan gjenopprettes ved hjelp av gjenopprettingsfrasen din, som du kan angi i Jade Plus i "*stateless*"-modus. For å omgå denne avhengigheten kan du også konfigurere og administrere din egen orakelserver.

## Utpakking av Jade Plus

Når du mottar Jade Plus, må du kontrollere at esken og forseglingen er i god stand for å sikre at pakken ikke har blitt åpnet.

![JADE-PLUS-GREEN](assets/fr/02.webp)

I esken finner du :


- Le Jade Plus;
- USB-C-kabel;
- Kort for å registrere minnefrasen som ord eller som "*CompactSeedQR*";
- Noen instruksjoner for bruk ;
- En ledning;
- Noen klistremerker.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Enheten har 4 navigasjonsknapper:


- Knappen nederst til høyre slår på Jade;
- Den store knappen på forsiden av enheten brukes til å velge et element;
- De to små knappene øverst gjør at du kan navigere til venstre og høyre;
- Du kan også velge et element ved å klikke samtidig på de to knappene øverst på enheten.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Sette opp en ny Bitcoin-lommebok

Klikk på startknappen.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Klikk på "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Velg "Start oppsett". Alternativet "*Advanced Setup*" gjør det samme, men med tilgang til avanserte innstillinger.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Klikk deretter på "*Create a New Wallet*" for å generere et nytt seed.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Klikk på "*Fortsett*"-knappen for å vise den nye gjenopprettingsfrasen.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus viser din 12-ord lange huskeregel. **Denne huskeregelen gir deg full, ubegrenset tilgang til alle bitcoinsene dine. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til din Jade Plus. Frasen på 12 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av din Jade. Det er derfor svært viktig å lagre den nøye og oppbevare den på et sikkert sted.

Du kan skrive det på pappen som følger med i esken, eller for ekstra sikkerhet anbefaler jeg å gravere det på en sokkel i rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer minnefrasen din, anbefaler jeg at du følger denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***Du må selvsagt aldri dele disse ordene på Internett, slik jeg gjør i denne veiledningen. Denne eksempelmappen vil kun bli brukt på Testnet, og vil bli slettet ved slutten av opplæringen

Klikk på pilen til høyre på skjermen for å vise følgende ord.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Når du har lagret frasen din, ber Jade Plus deg om å bekrefte den. Velg riktig ord i henhold til rekkefølgen ved hjelp av knappene øverst på enheten, og klikk på den midterste knappen for å gå videre til neste ord.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Koble Jade Plus til Green Wallet

I denne veiledningen bruker vi Green Wallet-applikasjonen til å administrere lommeboken som ligger på Jade Plus. Denne metoden er spesielt egnet for nybegynnere. Hvis du ønsker å administrere Bitcoin-lommeboken din mer detaljert, kan du også bruke Sparrow Wallet, som vi vil dekke i en egen veiledning:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
For instruksjoner om hvordan du installerer og konfigurerer Blockstream Green-applikasjonen, se første del av denne andre veiledningen:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
Når du er inne på Blockstream Green-applikasjonen, klikker du på knappen "*Konfigurer en ny portefølje*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Velg "*På maskinvarelommebok*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktiver Bluetooth på smarttelefonen din, og klikk deretter på "*Connect your Jade*"-knappen.

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autoriser Green-applikasjonen til å få tilgang til Bluetooth-tilkoblinger.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Programmet leter etter din Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

På Jade Plus klikker du på "*Bluetooth*"-menyen.

![JADE-PLUS-GREEN](assets/fr/18.webp)

Velg enheten din i Green-applikasjonen.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Bekreft sammenkoblingskoden på Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green tilbyr deg en test for å sikre at din Jade er ekte. Klikk på knappen for å gjøre det.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Bekreft på Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Grønt bekrefter at enheten er ekte.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Stille inn PIN-koden

Klikk på knappen "*Fortsett*" for å velge PIN-koden til Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

PIN-koden låser opp Jade. Den er derfor en beskyttelse mot uautorisert fysisk tilgang. PIN-koden er ikke involvert i utledningen av lommebokens kryptografiske nøkler. Så selv uten tilgang til denne PIN-koden vil du kunne få tilgang til bitcoinsene dine igjen hvis du er i besittelse av den mnemoniske frasen på 12 ord. Vi anbefaler at du velger en PIN-kode som er så tilfeldig som mulig. Sørg for å lagre denne koden på et annet sted enn der Jade er lagret (f.eks. i en passordbehandler).

Velg den 6-sifrede PIN-koden på Jade ved å bruke høyre og venstre knapp for å bla gjennom sifrene, og den midterste knappen for å bekrefte inntastingen av et siffer.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Bekreft PIN-koden din en gang til.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Bitcoin-lommeboken din har blitt opprettet.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Opprett en Bitcoin-konto

Du må nå opprette en konto i porteføljen din. Klikk på knappen "*Opprett en konto*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Velg "*Standard*" hvis du ønsker å opprette en klassisk portefølje med én signering.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Hvis du vil ha mer informasjon om "*2FA*"-alternativet, kan du følge denne andre veiledningen:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
Kontoen din er opprettet.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Hvis du ønsker å tilpasse den grønne porteføljen din, klikker du på de tre små prikkene øverst til høyre.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Med alternativet "*Rename*" kan du tilpasse navnet på porteføljen din, noe som er spesielt nyttig hvis du administrerer flere porteføljer i samme program. I menyen "*Unit*" kan du endre grunnenheten for porteføljen din. Du kan for eksempel velge å vise den i satoshier i stedet for bitcoins. Til slutt gir menyen "*Parameters*" deg tilgang til andre alternativer. Her finner du for eksempel den utvidede offentlige nøkkelen din og dens deskriptor, noe som er nyttig hvis du planlegger å sette opp en lommebok kun for klokker fra Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

For å koble til Jade-enheten igjen etter at du har slått den av, trykker du på av/på-knappen nederst på enheten. Velg enheten din fra startsiden i Green-applikasjonen:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Skriv deretter inn PIN-koden på Jade, og du vil være tilkoblet igjen.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Jade låses opp via Blockstreams "virtuelle sikre element" (se første del av denne veiledningen). Dette krever en Bluetooth-forbindelse med Green-applikasjonen. Hvis du støter på problemer med Bluetooth-tilkoblingen under opplåsingen, kan du prøve å koble fra og koble til de to enhetene på nytt. Hvis problemet vedvarer, kan du likevel låse opp Jade ved å velge alternativet "*QR Scan*" og følge instruksjonene som er tilgjengelige [på Blockstreams nettsted] (https://jadefw.blockstream.com/pinqr/index.html).

Før du mottar dine første bitcoins i lommeboken din, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Noter litt referanseinformasjon, for eksempel din xpub eller første mottaksadresse, og slett deretter lommeboken din i Green-appen og på Jade Plus mens den fortsatt er tom (`Options -> Device -> Factory Reset`). Prøv deretter å gjenopprette lommeboken din ved hjelp av papirsikkerhetskopiene av den mnemoniske frasen. Sjekk at cookie-informasjonen som genereres etter gjenopprettingen samsvarer med den du opprinnelig skrev ned. Hvis den gjør det, kan du være trygg på at papirsikkerhetskopiene dine er pålitelige. Hvis du vil vite mer om hvordan du utfører en testgjenoppretting, kan du lese denne andre veiledningen :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Motta bitcoins

Nå som Bitcoin-lommeboken din er satt opp, er du klar til å motta dine første sats! Bare klikk på "*Motta*"-knappen i Green-applikasjonen.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Green viser en mottaksadresse, men før du bruker den, er det viktig å sjekke den på Jade for å bekrefte at den faktisk tilhører vår portefølje. For å gjøre dette, klikk på knappen "*Verify on device*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Sjekk på Jade at adressen er den samme som på Green, og klikk deretter på knappen for å bekrefte.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Du kan nå dele adressen med betaleren for å motta bitcoins i lommeboken din. Når transaksjonen sendes ut i nettverket, vil den vises i lommeboken din. Vent til du har mottatt nok bekreftelser til å anse transaksjonen som endelig.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Send bitcoins

Med bitcoins i lommeboken din kan du nå også sende bitcoins. Klikk på "*Send*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

På neste side skriver du inn mottakerens adresse. Du kan skrive den inn manuelt eller skanne en QR-kode.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Velg betalingsbeløpet.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Nederst på skjermen kan du velge gebyrsats for denne transaksjonen. Du kan velge om du vil følge programmets anbefalinger eller tilpasse gebyrene selv. Jo høyere gebyret er i forhold til andre ventende transaksjoner, desto raskere vil transaksjonen bli behandlet. For informasjon om gebyrmarkedet, se [Mempool.space] (https://mempool.space/) i delen "*Transaksjonsgebyrer*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klikk på "*Neste*" for å komme til skjermbildet med transaksjonsoversikten. Kontroller at adressen, beløpet og kostnadene er korrekte.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Hvis alt går bra, skyver du den grønne knappen nederst på skjermen til høyre for å signere og kringkaste transaksjonen på Bitcoin-nettverket.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Du blir nå bedt om å bekrefte transaksjonen på Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Kontroller at mottakerens adresse er korrekt. Klikk på haken for å bekrefte.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Kontroller at beløpet er riktig, og bekreft deretter.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Transaksjonen din er signert og sendt fra Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Gratulerer, du vet nå hvordan du konfigurerer og bruker Jade Plus med Blockstream Green-mobilapplikasjonen via Bluetooth-tilkobling. Hvis du synes denne veiledningen var nyttig, vil jeg være takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Takk for at du deler!

For å ta ting et skritt videre, anbefaler jeg denne veiledningen om Jade Plus, der vi konfigurerer den med Sparrow Wallet-programvaren i QR-modus. Du lærer også hvordan du bruker de avanserte innstillingene til maskinvarelommeboken din:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262