---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalt, när du signerar en transaktion, sänds den automatiskt ut (broadcastas) till alla Bitcoin-noder i nätverket. Den väntar sedan på att bli minad.

Men så länge den inte finns i ett block kan en angripare som har fått tag på din privata nyckel ersätta den och stjäla pengarna. Detta är typiskt fallet om du använder en ColdCard-hårdvaruplånbok.

Verktyget Slipstream från gruvbolaget MARA låter dig kringgå att sända ut transaktionen till nätverket: den skickas direkt (och enbart) till en gruvarbetare, vilket håller den privat och undviker att exponera den på nätverket. Transaktionen kommer förmodligen att ta längre tid att minas, men den kommer att vara skyddad mot en ersättningsattack.

Nedan erbjuder vi en handledning som låter användare av [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), samt användare av plånboken [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), använda gruvbolaget MARA:s Slipstream-verktyg via sidan [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Varning**: detta verktyg är bara avsett för vissa profiler, huvudsakligen Liana-plånböcker, miniscript-plånböcker och vissa typer av multisig. Wizardsardine **avråder uttryckligen** från att använda det för plånböcker vars medel redan löper akut risk att stjälas, till exempel de vars återställningsfras genererades på en ColdCard-enhet som drabbats av sårbarheten i slumptalsgeneratorn. I den situationen handlar kapplöpningen mot angriparen om sekunder, och en transaktion som skickas till en enda gruvarbetare tar betydligt längre tid att bekräftas än en normalt utsänd transaktion. Om detta berör dig, läs vår dedikerade handledning först:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## För Liana-användare

Liana underhålls av Wizardsardine, utgivaren av sidan [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), så vägen är direkt: du exporterar helt enkelt den signerade PSBT-filen istället för att sända ut den.

*Förutsättning: ha medel på din Liana-plånbok.*

### Steg 1: Skapa din transaktion med Liana

Bygg som vanligt din transaktion genom att lägga till destinationsadressen, beskrivningen och beloppet (här det maximalt tillgängliga i plånboken).

För att ställa in avgiftsnivån:

- välj de mynt du vill spendera genom att klicka på den lilla rutan längst ner till vänster, under "Coins selection";
- ange sedan avgiftsnivån. Kom ihåg att sätta avgifterna betydligt högre än den föreslagna nivån, som beskrivs på denna sida: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klicka slutligen på "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Steg 2: Kontrollera dina transaktionsdetaljer

Innan du klickar på "Sign", kontrollera dina transaktionsdetaljer; särskilt:

- det skickade beloppet;
- antalet satoshis avsatta för transaktionsavgifter;
- men framför allt, adressen du skickar medlen till (kom ihåg att kontrollera de första 5/6 tecknen, de sista 5/6, och 5/6 tecken i mitten av adressen för att undvika "address poisoning"-attacker).

![Checking the transaction details](assets/fr/02.webp)

### Steg 3: Välj signeringsplånböckerna

Välj därefter de mjukvaru- och/eller hårdvaruplånböcker du behöver för att signera din transaktion med. En snabb påminnelse: i fallet med en 2-av-2 multisig-plånbok behöver du 2 signaturer av 2.

### Steg 4: Exportera din transaktions PSBT-fil

Bitcoin-transaktionen är nu signerad av de lämpliga nycklarna. Klicka inte på "Broadcast", annars kommer den att delas med hela nätverket och, om du använder en ColdCard-hårdvaruplånbok, kommer din transaktion att exponeras offentligt och dina medel att riskeras.

Du kan nu klicka på "Export" och sedan spara PSBT-filen lokalt på din dator.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Steg 5: Skicka transaktionen till gruvarbetaren via outofband.wizardsardine.com

Nu till de sista stegen. För att skicka transaktionen till gruvarbetaren behöver du bara ta PSBT-filen och dra och släppa den i det avsedda området.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

Transaktionen visas sedan som nedan.

![Transaction in the queue](assets/fr/05.webp)

### Steg 6: Skicka transaktionen via Slipstream

Slutligen behöver du bara klicka på "Send" så att transaktionen skickas till MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Inom några sekunder går transaktionen sedan från "Sending" till "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Allt som återstår är att kopiera transaktionsidentifieraren (TXID) och sedan klistra in den på [mempool.space](https://mempool.space/) för att kunna följa den bli minad:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Observera: transaktionen kommer att visas som "Transaction not found" tills gruvarbetaren MARA minar ett block och inkluderar din transaktion i det. Detta kan ta flera tiotals minuter, eller till och med timmar, eftersom MARA endast innehar omkring 4,5 % av Bitcoin-nätverkets hashkraft. Från och med den 4 augusti 2026 motsvarar detta ungefär ett minat block var 3 timme och 45 minuter.

## För användare av andra plånböcker

Om du inte använder [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) men ändå vill använda verktyget, här är en handledning som använder en 2-av-2 multisig-plånbok. För att göra detta använder vi mjukvaruplånboken [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Förutsättning: ha medel på din Sparrow-plånbok.*

### Steg 1: Skapa din transaktion

Med [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), skapa transaktionen på din multisig-plånbok. Kom ihåg att sätta avgifterna betydligt högre än den föreslagna nivån, som beskrivs på denna sida: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

När den skapats, klicka på "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Steg 2: Slutför din transaktion

För att slutföra din transaktion behöver du nu signera den. För att göra detta, klicka på "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Steg 3: Signera din transaktion med dina olika nycklar

Nu är det dags att signera transaktionen. För att göra detta, signera helt enkelt med den eller de mjukvaru- eller hårdvaruplånböcker du använder.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Steg 4: Ladda ner den signerade transaktionen, och sänd inte ut den till nätverket

Bitcoin-transaktionen är nu signerad av båda nycklarna i vår 2-av-2 multisig. Klicka inte på "Broadcast Transaction", annars kommer den att delas med hela nätverket och, om du använder en ColdCard-hårdvaruplånbok, kommer din transaktion att exponeras offentligt och dina medel att riskeras.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Steg 5: Visa det signerade transaktionsskriptet, eller ladda ner PSBT-filen

För att visa den signerade Bitcoin-transaktionen, klicka nu på "View Final Transaction". Du kan sedan kopiera det signerade Bitcoin-transaktionsskriptet:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Om du vill ladda ner transaktionsfilen kan du antingen:

- klicka på "File", sedan "Save transaction…";
- eller klicka på nätverksanslutningsknappen längst ner till höger (gul knapp), sedan klicka på "Save Final Transaction".

Transaktionen sparas sedan lokalt på din dator.

![Saving the final transaction locally](assets/fr/14.webp)

### Steg 6: Skicka transaktionen till gruvarbetaren via outofband.wizardsardine.com

Nu till de sista stegen. För att skicka transaktionen till gruvarbetaren behöver du bara:

- gå till [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- klistra in det signerade transaktionsskriptet som kopierades i föregående steg, och klicka sedan på "ADD TO QUEUE" nedan;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- eller ta filen och dra och släpp den i det avsedda området.

![Dropping the transaction file on the tool](assets/fr/16.webp)

Transaktionen visas sedan som nedan.

![Transaction in the queue](assets/fr/17.webp)

Om ett meddelande talar om för dig att det totala inmatningsbeloppet av satoshis i din transaktion är okänt (och att antalet satoshis för avgifterna som ett resultat inte kan beräknas), behöver du bara ange det totala inmatningsbeloppet av satoshis manuellt. För att hitta det, klicka bara på visningen av din transaktion i Sparrow, i mitten av diagrammet:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Ange sedan det beloppet (15 904 sats i vårt exempel) i verktyget [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Kontrollera slutligen att avgiftsnivån är korrekt.

### Steg 7: Skicka transaktionen via Slipstream

Slutligen behöver du bara klicka på "Send" så att transaktionen skickas till MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Inom några sekunder går transaktionen sedan från "Sending" till "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Allt som återstår är att kopiera transaktionsidentifieraren (TXID) och sedan klistra in den på [mempool.space](https://mempool.space/) för att kunna följa den bli minad:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Observera: transaktionen kommer att visas som "Transaction not found" tills gruvarbetaren MARA minar ett block och inkluderar din transaktion i det. Detta kan ta flera tiotals minuter, eller till och med timmar, eftersom MARA endast innehar omkring 4,5 % av Bitcoin-nätverkets hashkraft. Från och med den 4 augusti 2026 motsvarar detta ungefär ett minat block var 3 timme och 45 minuter.
