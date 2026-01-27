---
name: KaleidoSwap
description: Avancerad guide till RGB tillgångshandel på Lightning Network med KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap är en sofistikerad skrivbordsapplikation med öppen källkod som överbryggar klyftan mellan RGB-protokollet och Lightning Network. Den fungerar som ett omfattande gränssnitt för att hantera RGB Lightning Nodes, interagera med RGB Lightning Service Providers (LSP) via LSPS1-specifikationen och utföra atomära byten av RGB-tillgångar.


KaleidoSwap är en lösning utan förvaring och ger användarna möjlighet att behålla full kontroll över sina nycklar och data. Genom att utnyttja valideringsparadigmet på klientsidan i RGB möjliggör det privata och skalbara smarta kontrakt ovanpå Bitcoin. Denna handledning dyker in i de avancerade funktionerna i KaleidoSwap och guidar dig genom svårigheterna med "färgad" UTXO-hantering, kanallikviditet för specifika tillgångar och taker-maker-handelsmodellen, vilket säkerställer att du kan utnyttja detta kraftfulla decentraliserade utbytesprotokoll fullt ut.


## Installation


KaleidoSwap tillhandahåller förbyggda binärfiler för de flesta operativsystem, men för avancerade användare kan du bygga från källkod för att säkerställa att du kör den senaste koden med dina specifika konfigurationer.


### Ladda ner Binaries


Du kan hämta den senaste versionen för ditt operativsystem från [den officiella webbplatsen](https://kaleidoswap.com/) eller [GitHubs sida för versioner](https://github.com/kaleidoswap/desktop-app/releases).


### Installationsmetoder


1.  **Windows**: Ladda ner installationsprogrammet `.exe` och kör det.

2.  **macOS**: Ladda ner filen `.dmg`, öppna den och dra KaleidoSwap till din applikationsmapp.

3.  **Linux**: Ladda ner filen `.AppImage` eller `.deb` och installera/köra den.



## Alternativ för nodinställning


När du först startar KaleidoSwap kommer du att presenteras med **Connection Screen**. Detta är det första steget i konfigurationen av din miljö.


![Node Selection Screen](assets/en/01.webp)


Du måste välja hur du vill ansluta till RGB Lightning Network. Detta val påverkar din nivå av kontroll och integritet.


### Alternativ 1: Lokal nod (rekommenderas för egen förvaring)


**För fullständig kontroll och integritet**, kör en nod direkt på din maskin, se fördelarna nedan:


- Självförvaltande**: Du håller i nycklarna. Ingen tredje part kan frysa dina pengar eller censurera dina transaktioner.
- Sekretess**: Dina data stannar på din enhet.
- Oberoende**: Inget beroende av externa tjänsteleverantörer.


Om du väljer **Local Node** kommer du till inställningsfönstret där du kan skapa en ny wallet eller återställa en befintlig.


![Local Node Setup Screen](assets/en/02.webp)


### Alternativ 2: Fjärrstyrd nod


Anslut till en fjärransluten RGB Lightning Node (självhostad på en VPS eller hos en hostad leverantör).


- Fördelar**: Ingen lokal resursanvändning, tillgänglighet 24/7.
- Avvägning**: Kräver att man litar på värden eller hanterar en fjärrserver.


![Remote Node Setup Screen](assets/en/03.webp)


**Vi rekommenderar starkt att du kör din egen nod - antingen lokalt (alternativ 1) eller genom att själv vara värd för en fjärrnod - för att fullt ut utnyttja de censurresistenta egenskaperna hos Bitcoin och RGB.


## Skapa en Wallet


KaleidoSwap hanterar både Bitcoin och RGB tillgångar. Skapandeprocessen för wallet initierar en keystore som säkrar dina on-chain-medel och dina Lightning-kanaltillstånd.


Här är den detaljerade processen:

1. Öppna KaleidoSwap och välj **Local Node**.

2. Klicka på **Create New Wallet**.

3. **Kontoinställning**: Ange ett **Kontonamn** och välj **Nätverk** (t.ex. Bitcoin Mainnet, Testnet, Signet).

4. **Avancerad konfiguration** (valfritt): Om du är en avancerad användare kan du konfigurera anpassade RPC-slutpunkter, indexerings-URL:er eller proxyinställningar under "Avancerade inställningar".

5. Klicka på **Fortsätt**.

6. **Lösenord**: Ange ett starkt lösenord för att kryptera filen wallet lokalt.

7. **Återställningsfras**: Skriv ner din seed-fras och förvara den på ett säkert sätt.


    - Kritiskt**: Denna fras behövs för att återställa dina on-chain-medel och nodidentitet.
    - Varning**: **Lightning channel states kan inte återställas helt från enbart seed**. Du måste också upprätthålla statiska kanalbackuper (SCB) för att återställa medel som är låsta i kanaler.


![Wallet Creation Screen](assets/en/04.webp)



## Översikt över instrumentpanelen


När din wallet har skapats kommer du att skickas till huvudpanelen **Dashboard**.


![KaleidoSwap Dashboard](assets/en/05.webp)


obs: Skärmdumpen ovan visar en wallet som redan har finansierats och har aktiva kanaler. En ny wallet kommer att visa nollsaldon och inga aktiva kanaler förrän du finansierar den


## Finansiering av din Wallet


För att operera med RGB tillgångar måste du finansiera din wallet. KaleidoSwap stöder insättning av både Bitcoin- och RGB-tillgångar via on-chain-transaktioner eller Lightning Network.


### Deponering av Bitcoin


1. Klicka på **Deposit** i menyn Quick Actions.

2. Välj **BTC** från tillgångslistan.


![Select BTC Asset](assets/en/06.webp)


3. Välj din insättningsmetod: **On-chain** eller **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- På kedjan**: Skanna QR-koden eller kopiera adressen för att skicka Bitcoin från en annan wallet.
- Blixten**: Generera en faktura på önskat belopp.


![BTC On-chain Deposit](assets/en/08.webp)


### Deponering av RGB-tillgångar och färgade UTXO:er


För att få RGB-tillgångar (som USDT) behöver du specifika UTXO:er som är tillgängliga för att "färgas" (tilldelas en tillgång).


1. Klicka på **Deposit** och välj RGB-tillgången (t.ex. USDT). **Viktigt**: Om detta är **första gången** din nod tar emot denna specifika tillgång, **lämna fältet för tillgångens ID tomt**. Om du anger ett ID för en okänd tillgång kommer noden att returnera ett felmeddelande eftersom den inte känner igen den ännu.

2. Välj **On-chain** eller **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Mottagningssätt i kedjan: Vittne kontra förblindad


När du tar emot RGB-tillgångar on-chain har du två sekretesslägen:



- Blinded Receive (rekommenderas för sekretess)**: Du tillhandahåller en "blinded" UTXO till avsändaren. Du ber avsändaren att skicka tillgångar till en befintlig UTXO som du äger, men du fördunklar den faktiska UTXO-identifieraren. Detta ger bättre sekretess.
- Vittnet tar emot**: Du tillhandahåller en standard Bitcoin-adress. Du ber avsändaren att skapa en *ny* UTXO åt dig genom att skicka tillgångarna till den adressen. Detta gör att RGB-tillgångarna kan kopplas direkt till den nya UTXO som skapats av transaktionen.


#### Blixtinsättning


För Lightning-insättningar behöver du bara generate en faktura. RGB-tillgången kommer att dirigeras till dig via dina öppna kanaler.


![USDT Lightning Invoice](assets/en/10.webp)



## Öppna kanaler med RGB-tillgångar


För att dirigera RGB tillgångar över Lightning Network behöver du en kanal med tillräcklig likviditet och tillgångsallokering. Det enklaste sättet att komma igång är att **Köpa en kanal** från en LSP (Lightning Service Provider).


### Köpa en kanal från Kaleido LSP


1. Gå till fliken **Channels**. Du kommer att se alternativ för att "Öppna kanal" (manuell) eller "Köpa kanal" (LSP).

2. Klicka på **Köpkanal**.


![Channels Dashboard](assets/en/11.webp)


3. ** Anslut till LSP**: Appen kommer att ansluta till Kaleidos standard-LSP. Denna leverantör erbjuder inkommande likviditet och stöder RGB asset routing.


![Connect to LSP](assets/en/12.webp)


4. **Konfigurera kanal**:


    - Kapacitet**: Välj den totala Bitcoin-kapaciteten för kanalen.
    - RGB Allokering**: Välj den RGB-tillgång (t.ex. USDT) som du vill kunna ta emot eller skicka. LSP:n kommer att se till att kanalen är konfigurerad för att stödja denna tillgång.


![Configure Channel](assets/en/13.webp)



    - RGB Tilldelning**: Välj den RGB-tillgång (t.ex. USDT) som du vill kunna ta emot eller skicka. LSP:n kommer att se till att kanalen är konfigurerad för att stödja denna tillgång.


![RGB Allocation](assets/en/14.webp)


5.  **Betalning**: Du måste betala en avgift till LSP:n för att öppna kanalen och tillhandahålla likviditet. Du kan betala med hjälp av **Lightning** eller **On-chain** Bitcoin. Betalningen kan göras från din interna KaleidoSwap wallet eller en extern wallet.


![Complete Payment](assets/en/15.webp)


6. När betalningen har bekräftats kommer LSP att initiera transaktionen för kanalöppning. Du kommer att se en **Order Completed** skärm.


![Order Completed](assets/en/16.webp)


7. Efter bekräftelse på blockkedjan kommer din kanal att vara aktiv och redo för RGB-överföringar.



## Handel: Taker-Maker-modellen


KaleidoSwaps handelsmotor fungerar enligt en **Taker-Maker-modell**. Du kan byta tillgångar manuellt med en kollega eller använda en Market Maker (LSP).


### Byte med en marknadsgarant (LSP)


Detta är det vanligaste sättet att handla. Du agerar som **Taker** och utför order mot den tillgängliga likviditeten som tillhandahålls av LSP (**Maker**).


1. Navigera till fliken **Trade** och välj **Market Maker**.

2. **Ange belopp**: Ange det belopp i Bitcoin som du vill skicka (eller den tillgång du vill ta emot). Gränssnittet kommer att visa den beräknade växelkursen och avgifterna.


![Market Maker Swap](assets/en/17.webp)


3. ** Bekräfta bytet**: Granska detaljerna, inklusive växelkursen och det exakta beloppet du kommer att få. Klicka på **Bekräfta bytet**.


![Confirm Swap](assets/en/18.webp)


4. **Bearbetning**: Bytet utförs atomiskt på Lightning Network. Du kommer att se en statusskärm som indikerar att bytet väntar.


![Swap Pending](assets/en/19.webp)


5. **Framgång**: När HTLC:erna har avräknats är swappen slutförd och tillgångarna finns i din kanal.


![Swap Success](assets/en/20.webp)



## Utvecklare API


För utvecklare som bygger på KaleidoSwap, exponerar applikationen en API som stöder:



- RGB LSPS1**: För automatiserade likviditetstjänster.
- Swap API**: För programmatisk handel och market making.
- WebSocket**: För prenumerationer på marknadsdata i realtid.


Se [API Documentation](https://docs.kaleidoswap.com/api/introduction) för fullständiga slutpunkter och specifikationer.


## Slutsats


KaleidoSwap ger dig möjlighet att utnyttja integriteten och skalbarheten hos RGB-tillgångar på Lightning Network. Genom att förstå färgade UTXO:er och allokering av kanaltillgångar kan du fullt ut utnyttja detta kraftfulla decentraliserade utbytesprotokoll.