---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normaal gesproken wordt een transactie, zodra je die ondertekent, automatisch uitgezonden naar elk Bitcoin-node op het netwerk. Vervolgens wacht ze om gemined te worden.

Zolang ze echter niet in een blok zit, kan een aanvaller die jouw private key heeft bemachtigd de transactie vervangen en de fondsen stelen. Dit is typisch het geval als je een ColdCard hardware wallet gebruikt.

De Slipstream-tool van het miningbedrijf MARA laat je toe om het uitzenden van de transactie naar het netwerk te omzeilen: ze wordt rechtstreeks (en uitsluitend) naar een miner gestuurd, waardoor ze privé blijft en niet wordt blootgesteld op het netwerk. De transactie zal waarschijnlijk langer duren om gemined te worden, maar ze is beschermd tegen een replacement-aanval.

Hieronder bieden we een tutorial waarmee gebruikers van [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), alsook gebruikers van de [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) wallet, de Slipstream-tool van miner MARA kunnen gebruiken via de pagina [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Waarschuwing**: deze tool is enkel bedoeld voor bepaalde profielen, voornamelijk Liana-wallets, miniscript-wallets en bepaalde types multisig. Wizardsardine **raadt expliciet af** om ze te gebruiken voor wallets waarvan de fondsen al kritiek risico op diefstal lopen, bijvoorbeeld wallets waarvan de herstelzin werd gegenereerd op een ColdCard-apparaat dat getroffen is door de kwetsbaarheid in de random number generator. In die situatie is de race tegen de aanvaller een kwestie van seconden, en een transactie die naar één enkele miner wordt gestuurd doet er veel langer over om bevestigd te worden dan een normaal uitgezonden transactie. Als dit jou aangaat, lees dan eerst onze specifieke tutorial:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Voor Liana-gebruikers

Liana wordt onderhouden door Wizardsardine, de uitgever van de pagina [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), dus het traject is rechtstreeks: je exporteert simpelweg het ondertekende PSBT-bestand in plaats van het uit te zenden.

*Vereiste: heb fondsen op je Liana-wallet.*

### Stap 1: Maak je transactie aan met Liana

Bouw zoals gebruikelijk je transactie op door het bestemmingsadres, de beschrijving en het bedrag toe te voegen (hier het maximaal beschikbare bedrag in de wallet).

Om de fee rate in te stellen:

- selecteer de coins die je wilt uitgeven door op het kleine vakje linksonder te klikken, onder "Coins selection";
- voer vervolgens de fee rate in. Vergeet niet de fees veel hoger in te stellen dan het voorgestelde tarief, zoals beschreven op deze pagina: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klik ten slotte op "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Stap 2: Controleer de details van je transactie

Voordat je op "Sign" klikt, controleer je de details van je transactie; controleer in het bijzonder:

- het verzonden bedrag;
- het aantal satoshi's toegewezen aan transactiekosten;
- maar vooral, het adres waarnaar je de fondsen verzendt (vergeet niet de eerste 5/6 tekens, de laatste 5/6, en 5/6 tekens in het midden van het adres te controleren om "address poisoning"-aanvallen te vermijden).

![Checking the transaction details](assets/fr/02.webp)

### Stap 3: Selecteer de ondertekenende wallets

Selecteer vervolgens de software- en/of hardware wallets waarmee je jouw transactie moet ondertekenen. Een korte herinnering: in het geval van een 2-of-2 multisig wallet heb je 2 van de 2 handtekeningen nodig.

### Stap 4: Exporteer het PSBT-bestand van je transactie

De Bitcoin-transactie is nu ondertekend door de juiste sleutels. Klik niet op "Broadcast", anders wordt ze gedeeld met het hele netwerk en, als je een ColdCard hardware wallet gebruikt, wordt jouw transactie publiekelijk blootgesteld en lopen jouw fondsen risico.

Je kunt nu op "Export" klikken, en vervolgens het PSBT-bestand lokaal op je computer opslaan.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Stap 5: Verzend de transactie naar de miner via outofband.wizardsardine.com

Nu volgen de laatste stappen. Om de transactie naar de miner te verzenden, hoef je enkel het PSBT-bestand te nemen en het te slepen en neer te zetten in het daarvoor bestemde gebied.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

De transactie wordt dan weergegeven zoals hieronder getoond.

![Transaction in the queue](assets/fr/05.webp)

### Stap 6: Verzend de transactie via Slipstream

Ten slotte hoef je enkel op "Send" te klikken zodat de transactie via Slipstream naar MARA wordt verzonden.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Binnen enkele seconden gaat de transactie dan van "Sending" naar "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Al wat rest is de transactie-identificatie (TXID) te kopiëren, en die vervolgens te plakken in [mempool.space](https://mempool.space/) om te zien hoe ze gemined wordt:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Let op: de transactie zal weergegeven worden als "Transaction not found" totdat de miner, MARA, een blok mined en jouw transactie erin opneemt. Dit kan enkele tientallen minuten duren, of zelfs uren, omdat MARA slechts ongeveer 4,5% van de hash rate van het Bitcoin-netwerk bezit. Vanaf 4 augustus 2026 komt dit overeen met ongeveer één gemined blok per 3 uur en 45 minuten.

## Voor gebruikers van andere wallets

Als je [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) niet gebruikt maar toch de tool wilt gebruiken, hier is een tutorial met een 2-of-2 multisig wallet. Hiervoor gebruiken we de [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) software wallet.

*Vereiste: heb fondsen op je Sparrow-wallet.*

### Stap 1: Maak je transactie aan

Maak met [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) de transactie aan op je multisig wallet. Vergeet niet de fees veel hoger in te stellen dan het voorgestelde tarief, zoals beschreven op deze pagina: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klik vervolgens, eenmaal aangemaakt, op "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Stap 2: Finaliseer je transactie

Om je transactie te finaliseren, moet je ze nu ondertekenen. Klik hiervoor op "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Stap 3: Onderteken je transactie met je verschillende sleutels

Nu is het tijd om de transactie te ondertekenen. Onderteken ze hiervoor simpelweg met de software- of hardware wallet(s) die je gebruikt.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Stap 4: Download de ondertekende transactie, en zend ze niet uit naar het netwerk

De Bitcoin-transactie is nu ondertekend door beide sleutels van onze 2-of-2 multisig. Klik niet op "Broadcast Transaction", anders wordt ze gedeeld met het hele netwerk en, als je een ColdCard hardware wallet gebruikt, wordt jouw transactie publiekelijk blootgesteld en lopen jouw fondsen risico.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Stap 5: Toon het script van de ondertekende transactie, of download het PSBT-bestand

Om de ondertekende Bitcoin-transactie weer te geven, klik je nu op "View Final Transaction". Je kunt dan het script van de ondertekende Bitcoin-transactie kopiëren:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Als je het transactiebestand wilt downloaden, kun je ofwel:

- klikken op "File", dan "Save transaction…";
- of klikken op de netwerkverbindingsknop rechtsonder (gele knop), en vervolgens op "Save Final Transaction" klikken.

De transactie wordt dan lokaal op je computer opgeslagen.

![Saving the final transaction locally](assets/fr/14.webp)

### Stap 6: Verzend de transactie naar de miner via outofband.wizardsardine.com

Nu volgen de laatste stappen. Om de transactie naar de miner te verzenden, hoef je enkel:

- naar [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) te gaan;
- het script van de ondertekende transactie dat je in de vorige stap hebt gekopieerd te plakken, en vervolgens hieronder op "ADD TO QUEUE" te klikken;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- of het bestand te nemen en te slepen en neer te zetten in het daarvoor bestemde gebied.

![Dropping the transaction file on the tool](assets/fr/16.webp)

De transactie wordt dan weergegeven zoals hieronder getoond.

![Transaction in the queue](assets/fr/17.webp)

Als een melding je vertelt dat het totale inputbedrag aan satoshi's van je transactie onbekend is (en dat, als gevolg daarvan, het aantal satoshi's voor de fees niet kan worden berekend), moet je enkel het totale inputbedrag aan satoshi's handmatig invoeren. Om dit te vinden, klik je gewoon op de weergave van je transactie in Sparrow, in het midden van het diagram:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Voer vervolgens dat bedrag (15.904 sats in ons voorbeeld) in bij de tool [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Controleer ten slotte of de fee rate correct is.

### Stap 7: Verzend de transactie via Slipstream

Ten slotte hoef je enkel op "Send" te klikken zodat de transactie via Slipstream naar MARA wordt verzonden.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Binnen enkele seconden gaat de transactie dan van "Sending" naar "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Al wat rest is de transactie-identificatie (TXID) te kopiëren, en die vervolgens te plakken in [mempool.space](https://mempool.space/) om te zien hoe ze gemined wordt:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Let op: de transactie zal weergegeven worden als "Transaction not found" totdat de miner, MARA, een blok mined en jouw transactie erin opneemt. Dit kan enkele tientallen minuten duren, of zelfs uren, omdat MARA slechts ongeveer 4,5% van de hash rate van het Bitcoin-netwerk bezit. Vanaf 4 augustus 2026 komt dit overeen met ongeveer één gemined blok per 3 uur en 45 minuten.
