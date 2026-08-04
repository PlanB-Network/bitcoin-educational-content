---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalt, når du signerer en transaksjon, blir den automatisk kringkastet til hver Bitcoin-node på nettverket. Deretter venter den på å bli minet.

Så lenge den ikke er inkludert i en blokk, kan imidlertid en angriper som har fått tak i din private nøkkel erstatte den og stjele midlene. Dette er typisk tilfellet hvis du bruker en ColdCard maskinvarelommebok.

Slipstream-verktøyet fra gruveselskapet MARA lar deg unngå å kringkaste transaksjonen til nettverket: den sendes direkte (og utelukkende) til en miner, noe som holder den privat og unngår å eksponere den på nettverket. Transaksjonen vil trolig ta lengre tid å bli minet, men den vil være beskyttet mot et erstatningsangrep.

Nedenfor tilbyr vi en veiledning som lar brukere av [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), samt brukere av [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-lommeboken, bruke miner MARAs Slipstream-verktøy via siden [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Advarsel**: dette verktøyet er kun ment for enkelte profiler, hovedsakelig Liana-lommebøker, miniscript-lommebøker og enkelte typer multisig. Wizardsardine **fraråder eksplisitt** å bruke det for lommebøker hvis midler allerede er i kritisk fare for å bli stjålet, for eksempel de hvis gjenopprettingsfrase ble generert på en ColdCard-enhet berørt av sårbarheten i tilfeldigtallsgeneratoren. I den situasjonen er kappløpet mot angriperen et spørsmål om sekunder, og en transaksjon sendt til en enkelt miner tar langt lenger tid å bekrefte enn en normalt kringkastet transaksjon. Hvis dette bekymrer deg, les først vår dedikerte veiledning:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## For Liana-brukere

Liana vedlikeholdes av Wizardsardine, utgiveren av siden [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), så veien er direkte: du eksporterer rett og slett den signerte PSBT-filen i stedet for å kringkaste den.

*Forutsetning: ha midler på din Liana-lommebok.*

### Steg 1: Opprett transaksjonen din med Liana

Som vanlig, bygg transaksjonen din ved å legge til mottakeradressen, beskrivelsen og beløpet (her, det maksimale tilgjengelige i lommeboken).

For å sette gebyrsatsen:

- velg myntene du vil bruke ved å klikke på den lille boksen nederst til venstre, under "Coins selection";
- angi deretter gebyrsatsen. Husk å sette gebyrene mye høyere enn den foreslåtte satsen, som beskrevet på denne siden: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klikk til slutt på "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Steg 2: Sjekk transaksjonsdetaljene dine

Før du klikker "Sign", sjekk transaksjonsdetaljene dine; spesielt:

- beløpet som sendes;
- antall satoshi som er tildelt transaksjonsgebyrer;
- men fremfor alt, adressen du sender midlene til (husk å sjekke de første 5/6 tegnene, de siste 5/6, og 5/6 tegn i midten av adressen for å unngå «address poisoning»-angrep).

![Checking the transaction details](assets/fr/02.webp)

### Steg 3: Velg signeringslommebøkene

Deretter velger du programvare- og/eller maskinvarelommebøkene du trenger for å signere transaksjonen din. En rask påminnelse: for en 2-av-2 multisig-lommebok trenger du 2 av 2 signaturer.

### Steg 4: Eksporter transaksjonens PSBT-fil

Bitcoin-transaksjonen er nå signert med de riktige nøklene. Ikke klikk på "Broadcast", ellers vil den bli delt med hele nettverket, og hvis du bruker en ColdCard maskinvarelommebok, vil transaksjonen din bli offentlig eksponert og midlene dine vil være i fare.

Du kan nå klikke på "Export", og deretter lagre PSBT-filen lokalt på datamaskinen din.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Steg 5: Send transaksjonen til miner via outofband.wizardsardine.com

Nå til de siste stegene. For å sende transaksjonen til miner, trenger du bare å ta PSBT-filen og dra og slippe den inn i det angitte området.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

Transaksjonen vises deretter som vist nedenfor.

![Transaction in the queue](assets/fr/05.webp)

### Steg 6: Send transaksjonen via Slipstream

Til slutt trenger du bare å klikke på "Send" slik at transaksjonen sendes til MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

I løpet av noen sekunder går transaksjonen fra "Sending" til "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Alt som gjenstår er å kopiere transaksjonsidentifikatoren (TXID), og deretter lime den inn i [mempool.space](https://mempool.space/) for å følge med på at den blir minet:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Merk: transaksjonen vil vises som «Transaction not found» helt til miner, MARA, miner en blokk og inkluderer transaksjonen din i den. Dette kan ta flere titalls minutter, eller til og med timer, fordi MARA kun har rundt 4,5 % av Bitcoin-nettverkets hashrate. Per 4. august 2026 tilsvarer dette omtrent én blokk minet hver 3. time og 45. minutt.

## For brukere av andre lommebøker

Hvis du ikke bruker [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) men likevel ønsker å bruke verktøyet, følger her en veiledning med en 2-av-2 multisig-lommebok. For å gjøre dette bruker vi programvarelommeboken [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Forutsetning: ha midler på din Sparrow-lommebok.*

### Steg 1: Opprett transaksjonen din

Med [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), opprett transaksjonen på multisig-lommeboken din. Husk å sette gebyrene mye høyere enn den foreslåtte satsen, som beskrevet på denne siden: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Når den er opprettet, klikk på "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Steg 2: Fullfør transaksjonen din

For å fullføre transaksjonen din, må du nå signere den. For å gjøre dette, klikk på "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Steg 3: Signer transaksjonen din med dine ulike nøkler

Nå er det på tide å signere transaksjonen. For å gjøre dette, signer den rett og slett med programvare- eller maskinvarelommebok(-bøkene) du bruker.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Steg 4: Last ned den signerte transaksjonen, og ikke kringkast den til nettverket

Bitcoin-transaksjonen er nå signert av begge nøklene i vår 2-av-2 multisig. Ikke klikk på "Broadcast Transaction", ellers vil den bli delt med hele nettverket, og hvis du bruker en ColdCard maskinvarelommebok, vil transaksjonen din bli offentlig eksponert og midlene dine vil være i fare.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Steg 5: Vis det signerte transaksjonsskriptet, eller last ned PSBT-filen

For å vise den signerte Bitcoin-transaksjonen, klikk nå på "View Final Transaction". Du kan deretter kopiere det signerte Bitcoin-transaksjonsskriptet:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Hvis du ønsker å laste ned transaksjonsfilen, kan du enten:

- klikke på "File", deretter "Save transaction…";
- eller klikke på nettverkstilkoblingsknappen nederst til høyre (gul knapp), og deretter klikke på "Save Final Transaction".

Transaksjonen vil deretter bli lagret lokalt på datamaskinen din.

![Saving the final transaction locally](assets/fr/14.webp)

### Steg 6: Send transaksjonen til miner via outofband.wizardsardine.com

Nå til de siste stegene. For å sende transaksjonen til miner, trenger du bare å:

- gå til [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- lime inn det signerte transaksjonsskriptet du kopierte i forrige steg, og deretter klikke på "ADD TO QUEUE" nedenfor;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- eller ta filen og dra og slipp den inn i det angitte området.

![Dropping the transaction file on the tool](assets/fr/16.webp)

Transaksjonen vises deretter som vist nedenfor.

![Transaction in the queue](assets/fr/17.webp)

Hvis en melding forteller deg at det totale inngående beløpet i satoshi i transaksjonen din er ukjent (og at, som følge av dette, antall satoshi for gebyrene ikke kan beregnes), trenger du bare å angi det totale inngående beløpet i satoshi manuelt. For å finne det, klikk bare på visningen av transaksjonen din i Sparrow, midt i diagrammet:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Angi deretter det beløpet (15 904 sats i vårt eksempel) i verktøyet [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Til slutt, sjekk at gebyrsatsen er korrekt.

### Steg 7: Send transaksjonen via Slipstream

Til slutt trenger du bare å klikke på "Send" slik at transaksjonen sendes til MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

I løpet av noen sekunder går transaksjonen fra "Sending" til "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Alt som gjenstår er å kopiere transaksjonsidentifikatoren (TXID), og deretter lime den inn i [mempool.space](https://mempool.space/) for å følge med på at den blir minet:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Merk: transaksjonen vil vises som «Transaction not found» helt til miner, MARA, miner en blokk og inkluderer transaksjonen din i den. Dette kan ta flere titalls minutter, eller til og med timer, fordi MARA kun har rundt 4,5 % av Bitcoin-nettverkets hashrate. Per 4. august 2026 tilsvarer dette omtrent én blokk minet hver 3. time og 45. minutt.
