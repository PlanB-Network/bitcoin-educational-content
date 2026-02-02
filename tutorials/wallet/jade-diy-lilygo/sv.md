---
name: Jade DIY
description: Förvandla ett utvecklingskort för 15 USD till en fullt fungerande Bitcoin-hårdvara wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Nybörjarbygge


**Målgrupp:** Nyfikna byggare med liten eller ingen erfarenhet av inbyggda system.


**Varaktighet:** 2 timmar (flexibel)


**Utfall:** I slutet kommer eleverna att:



- Känna igen säkerhetsmodellen för DIY-hårdvaruplånböcker jämfört med kommersiella enheter.
- Montera en mikrokontrollerbaserad signeringsenhet.
- Flasha firmware med öppen källkod och verifiera byggkontrollsumman.
- Signera och sända en mainnet-transaktion med hjälp av sin nya enhet.


---

## Sammanfattning


Denna 2-timmars workshop lär nybörjare att bygga en funktionell Bitcoin-hårdvara wallet genom att flasha Jade-firmware med öppen källkod på ett LilyGO T-Display-kort för 15 USD. Eleverna förvandlar generisk utvecklingshårdvara till en signeringsenhet som kan jämföras med kommersiella plånböcker som kostar 150 $, och lär sig grundläggande säkerhet genom praktisk erfarenhet snarare än enbart teori.


### Filosofi


Att bygga din egen signeringsenhet handlar inte bara om att spara pengar - det handlar om att förstå tekniken som skyddar din Bitcoin. Denna workshop omfattar "säkerhet genom förståelse" över black-box-förtroende. Genom att köpa komponenter, flasha firmware med öppen källkod och generera entropi själva minskar deltagarna risken i leveranskedjan samtidigt som de lär sig att utvärdera säkerhetsanspråk kritiskt. Målet är informerad autonomi: eleverna ska förstå både kraften och begränsningarna i sin DIY-enhet jämfört med härdade kommersiella alternativ.


---

## Grundläggande om konceptet (15 min)


### Vad är egenvårdnad och varför är det viktigt?


Bitcoin skapades för att ta bort behovet av betrodda tredje parter, som banker och företag, från vårt penningsystem. Istället för att använda tillit använder bitcoin matematik, fysik och kryptografi för att ge vem som helst makten att äga och kontrollera sina pengar utan att behöva någons tillstånd.


Det fungerar så att bitcoin finns i en global digital huvudbok som kallas blockkedjan, även kallad bitcoin timechain, som är en offentlig och transparent huvudbok som drivs av datorer, istället för en centraliserad huvudbok som ett bankkonto.


Det som är viktigt att förstå är att för att flytta bitcoin från en plats till en annan måste du signera transaktionen med en så kallad privat nyckel. Tänk på det som att låsa upp ett valv med ett lösenord och flytta bitcoin till någon annans valv. Bitcoin ger dig makten att själv hålla i nycklarna till valvet, istället för att förlita dig på att en bank flyttar dina pengar åt dig.


Med stor makt kommer stort ansvar, tappa bort nycklarna och dina pengar är borta för alltid. På så sätt kan du tänka på nycklarna till valvet som själva pengarna. Även om nycklar inte är samma sak som bitcoin är de mekanismen för att flytta dina pengar och är därför extremt viktiga att skydda. Det är därför vi säger "inte dina nycklar, inte dina mynt".


Termen self-custody kan låta förvirrande, men allt det innebär är att du har dina egna privata nycklar och kontrollerar dina egna bitcoin. Om du inte har den nyckeln litar du på att någon annan håller den åt dig. Om dina bitcoin finns i en ETF eller på en börs (Mt. Gox, FTX, Coinbase, Binance etc.) äger du inte bitcoin, du äger ett anspråk på bitcoin. Detta medför alla typer av risker, som att börser hackas och förlorar dina bitcoin eller att företag lånar ut dina pengar och bara ger dig en bråkdel i reserv. Dessutom skulle betrodda tredje parter ha full kontroll över dina pengar och kunna begränsa eller frysa uttag.


![image](assets/fr/01.webp)


Med egen förvaring tar du bort förtroendet från ekvationen. Ingen kan frysa dina pengar eller neka en transaktion, du kan skicka pengar över gränser, till vem som helst, när som helst, och du behöver inte ett bankkonto, ett ID eller någons godkännande. Ingen kan stoppa dig, censurera dig eller stjäla från dig, vilket låser upp bitcoins fulla kraft som frihetspengar. Det är därför vi säger att med bitcoin kan du vara din egen bank.


Bitcoin skapades för att lösa problemet med manipulation av förtroende och pengar, en utväg ur vårt nuvarande system, men utgången fungerar bara om du tar nycklarna. Det är därför självförvaring är så viktigt.


### Vad är en Wallet?


Termen wallet är lite av en missvisande benämning och kan därför vara förvirrande. Ja, det är sant att en bitcoin wallet, precis som en fysisk wallet, lagrar värde. Men den största skillnaden är att bitcoinplånböcker faktiskt inte lagrar några bitcoin.


Bitcoin existerar bara som en bokföringspost på den publika blockkedjan, eller i de metaforiska valven i cyberrymden. Kom ihåg att för att flytta bitcoin måste du använda dina nycklar för att låsa upp valvet och flytta mynten någon annanstans, de privata nycklarna är det som används för att spendera bitcoin. När du gör en transaktion med dina wallet använder du egentligen bara dina nycklar för att signera transaktionen. Det är så du visar bevis på att du äger pengarna och har rätt att spendera mynten.


Bitcoin-plånböcker lagrar egentligen bara dina privata nycklar, så det vore mer korrekt att kalla dem nyckelringar.


### Hot vs Cold plånböcker


En hot wallet är en mjukvaruapp på din telefon eller dator. Den är ansluten till internet, så den är lättare att använda och snabbare att signera transaktioner, men det innebär också att den är mer utsatt för hackare, skadlig kod och nätfiske. Den kallas "het" eftersom den är ansluten till internet, är inkopplad och påslagen. Ett exempel skulle kunna vara en telefon wallet eller en webbläsare wallet.


Å andra sidan är en kall wallet, eller hårdvaru-wallet, en enhet som skapar och lagrar din nyckel offline. Detta tar bort möjligheten för någon att hacka dina medel och är mycket säkrare för långsiktiga besparingar, men det är en enhet som behövs för att underteckna varje transaktion och kan vara mindre bekväm.


### Hardware Wallet Hotmodell


Hårdvaruplånböcker finns för att lösa ett grundläggande problem: hur signerar du Bitcoin-transaktioner utan att exponera dina privata nycklar för en internetansluten dator som kan äventyras av skadlig kod eller fjärrangripare? Den grundläggande hotmodellen utgår från att din vanliga bärbara dator eller telefon är potentiellt fientlig. En hårdvaru-wallet skapar en isolerad miljö där privata nycklar aldrig lämnar enheten, och transaktionssignering sker i en secure element eller mikrokontroller som endast kommunicerar signaturen tillbaka till värddatorn, inte själva nyckeln. Även om din dator är helt komprometterad kan en angripare inte stjäla din Bitcoin utan fysisk tillgång till enheten och din PIN-kod.


Hårdvaruplånböcker medför dock sina egna hot. Du måste lita på att tillverkaren inte har infört bakdörrar, att leveranskedjan inte har manipulerats och att slumptalsgenereringen verkligen är slumpmässig. Fysiska angripare kan extrahera nycklar genom sidokanalattacker eller chipmanipulation, och någon med tillfällig åtkomst kan modifiera din enhet. Genom att bygga din egen hårdvara wallet kan du förstå dessa avvägningar - du kommer att fatta beslut om säkra element kontra mikrokontroller för allmänt bruk, hur du verifierar transaktioner på en skärm och hur du skyddar dig mot både fjärrhot och fysiska hot. Målet är inte perfekt säkerhet, utan att förstå vilka hot du skyddar dig mot och vilka som kvarstår.


### Centrala begrepp



- Entropi och seed-fraser:** Din wallet är bara lika säker som den slumpmässighet som föder den. Vi kommer att blanda enhetens slumptalsgenerator med människovänliga knep som tärningskast, konvertera entropin till en 12- eller 24-ords [BIP39-fras](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) och lämna rummet med en skriftlig eller metallisk backup som du litar på.
- Fröfrashygien:** Behandla seed som huvudnycklar till dina besparingar. Skriv aldrig in orden i en telefon eller dator - keyloggers, skärmdumpar och molnbackuper kan läcka dem för alltid. Håll frasen offline, förvara den på en plats som bara du har tillgång till och öva på att läsa upp den högt innan du åker.
- Secure element + microcontroller:** Tänk på secure element som valvet och microcontrollern som hjärnan. secure element skyddar privata nycklar med manipuleringsskydd, medan mikrokontrollern hanterar skärmen, knapparna och logiken i den inbyggda programvaran. Observera att de hårdvaruplånböcker som vi bygger idag inte har någon secure element. Det betyder inte att den är osäker, bara att den har en skyddsnivå mindre.
- Lita på firmware:** Firmware är det osynliga operativsystemet i wallet. Ladda alltid ner från taggade utgåvor, kontrollera den publicerade hashen och förstå att reproducerbara builds låter flera personer kompilera samma kod och komma fram till exakt samma binärfil. Om kontrollsumman inte matchar signerar du inte.


---

## Vad är det vi bygger?


Vi tar generisk hårdvara, LilyGo T-Display, och flashar Jade SDK-firmware på den. [Jade Plus](https://blockstream.com/jade/jade-plus/) är en wallet med öppen källkod som vanligtvis kostar 150 dollar:


![image](assets/fr/02.webp)


Idag ska vi flasha deras firmware till en 15-dollars hårdvara istället.


### Vad du ska köpa


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB med skal, modell K164)** - [Beställ direkt från LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) för ca $15. Detta ESP32-kort ger displayen, knapparna och USB-gränssnittet som speglar Blockstreams Jade Plus. Den inbyggda ESP32 innehåller också Wi-Fi- och Bluetooth-radio; vi skickar firmware som håller dem inaktiverade, men de formar din hotmodell eftersom skadlig kod kan slå på dem igen.
- USB-C-kabel** - Ta med en datakapabel kabel så att du kan flasha firmware och strömförsörja kortet direkt från din bärbara dator (helt okej för användning i klassrummet).


### Varför bygga din egen Hardware Wallet?



- Spara cirka 135 USD jämfört med att köpa en kommersiell enhet.
- Skapa trygghet med firmware-flashing, säkra element och wallet-hygien.
- Starta upp ytterligare signeringsenheter för att sprida besparingarna över flera plånböcker.
- Minska risken i leveranskedjan genom att köpa in och montera varje komponent själv.
- Tänk på Lopps mantra: suveränitet och bekvämlighet står alltid i motsatsförhållande till varandra.


## Fysisk uppsättning


### Förbered ditt ärende


Du har två alternativ för att hysa ditt LilyGO T-Display-kort: ett 3D-utskrivet fodral eller det officiella LilyGO-kabinettet. Det tryckta fodralet kan hittas och skrivas ut från [den här modellen](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Det erbjuder ett lätt och anpassningsbart skal för din enhet.


![image](assets/fr/04.webp)


Alternativt kan du använda det officiella LilyGO-fodralet, som har en något annorlunda passform och finish, vilket ger ett mer robust skydd och ett polerat utseende.


![image](assets/fr/05.webp)


Observera att det tryckta och det officiella fodralet skiljer sig något åt vad gäller design och montering. Oavsett vilket alternativ du väljer ska du se till att kortet sitter ordentligt på plats i höljet för att undvika lösa anslutningar eller skador.


### Inspektera styrelsen


Innan du fortsätter ska du noggrant inspektera ditt LilyGO T-Display-kort för synliga defekter eller skräp. Kontrollera att displayen, knapparna och USB-C-porten är rena och fria från damm eller lödstänk. Hantera kortet med försiktighet och iaktta ESD-säkerhet (elektrostatisk urladdning) genom att jorda dig själv eller använda ett ESD-armband för att förhindra skador på känsliga komponenter.


### Anslut till din bärbara dator


Anslut LilyGO-kortet till din bärbara dator med hjälp av en USB-C-kabel som kan hantera data. Denna anslutning ger ström och gör att du kan flasha den inbyggda programvaran.


Vid uppstart visas följande skärm:


![image](assets/fr/06.webp)



När LilyGO är påslagen kommer den att visa en färgtestskärm som växlar mellan olika färger. Detta bekräftar att displayen och kortet fungerar korrekt innan du blinkar firmware.


När färgtestet är klart kommer skärmen att återgå till ett standardläge, vilket indikerar att kortet är klart för nästa steg i byggprocessen.


![image](assets/fr/07.webp)


## Det enkla sättet eller Hard-sättet


Det finns två huvudmetoder för att flasha firmware till din hårdvara wallet: det enkla sättet och det svåra sättet. Det enkla sättet använder förkonfigurerade verktyg eller webbaserade flashers som automatiskt laddar den fasta programvaran på din enhet med minimal inmatning. Denna metod är idealisk för nybörjare som vill ha en snabb vinst eller föredrar att undvika komplexiteten med felsökning och kommandoradsinteraktioner. Den förenklar processen och gör att du kommer igång snabbare, vilket gör den tillgänglig för dem som är nya inom inbyggd utveckling eller hårdvaruplånböcker.


Den hårda vägen, å andra sidan, innebär att du manuellt använder kommandoradsverktyg för att flasha den fasta programvaran. Detta tillvägagångssätt kräver att du verifierar den fasta programvarans signaturer och kontrollsummor för att säkerställa äkthet och integritet, vilket ger dig en djupare förståelse för flashningsprocessen och hur den fasta programvaran interagerar med maskinvaran. Även om det kräver mer ansträngning och kännedom om terminalkommandon ger det större kontroll, transparens och förtroende för enhetens säkerhet.


Varje metod har sina kompromisser: den enkla vägen offrar en viss grad av förtroende och förståelse för snabbhet och bekvämlighet, medan den svåra vägen kräver mer tid och teknisk skicklighet men belönar dig med flexibilitet och en starkare förståelse för den underliggande tekniken. Instruktörer bör uppmuntra eleverna att välja den väg som bäst stämmer överens med deras komfortnivå och nyfikenhet, vilket främjar både självförtroende och utforskning.


## Det enkla sättet


Det enklaste sättet att flasha en ESP32



- Gå till den officiella Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Du kan ladda ner källfilen och köra webbplatsen lokalt, men GitHub är redan värd för den på [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub serverar HTML, CSS, JavaScript etc. direkt till din webbläsare så att du kan flasha enheten utan att installera utvecklarverktyg.


![image](assets/fr/09.webp)



- Öppna rullgardinsmenyn (den är troligen inställd på `M5Stack Core2`) och välj ditt utvecklingskort - för den här klassen väljer du `LILYGO T-Display`.


![image](assets/fr/10.webp)



- När du klickar på flash kommer detta att visas. För att veta vilken enhet som är LILYGO, koppla ur lilygo och koppla in den igen. COM-porten för lilygo kommer att visas och försvinna. Klicka på den COM-port som Jade är ansluten till


![image](assets/fr/11.webp)



- Det är det en förloppsindikator bör visas och när den är klar är du redo att ställa in den


## Konfigurera Jade Wallet


När den fasta programvaran har flashats är din LilyGO T-Display nu en fullt fungerande Jade-hårdvara wallet. Detta avsnitt kommer att leda dig genom den första installationsprocessen, från att generera din seed-fras till att ansluta enheten med wallet-programvara som Sparrow eller Blockstream Green-mobilappen.


### Initial start och enhetskonfiguration



- Slå på enheten:** Med LilyGO fortfarande ansluten till din bärbara dator via USB-C, bör Jade-firmware starta automatiskt. Du kommer att se Jade-logotypen visas på displayen.



- Enter setup mode:** Enheten visar en inledande meny. Använd de två fysiska knapparna på kortet för att navigera:
 - Vänster knapp:** Flytta upp/back
 - Höger knapp:** Flytta nedåt/framåt
 - Båda knapparna samtidigt:** Välj/bekräfta



- Välj "Setup":** Navigera till alternativet Setup och tryck på båda knapparna för att bekräfta. Enheten kommer att vägleda dig genom den inledande konfigurationsprocessen.


### Skapa din Wallet



- Välj "Begin Setup":** Enheten kommer att uppmana dig att påbörja skapandeprocessen för wallet. Bekräfta ditt val.



- Välj "Skapa ny Wallet":** Du kommer att presenteras med två alternativ:
 - Skapa ny Wallet:** Genererar en ny seed-fras (välj denna för workshopen)
 - Restore Wallet:** Återställ en befintlig wallet från en seed-fras (för avancerade användare)



- Välj "Create New Wallet" och bekräfta.



- Generera entropi:** Enheten använder sin slumptalsgenerator för att skapa kryptografisk entropi. Denna process tar några sekunder eftersom enheten samlar in slumptal från flera källor.


### Spela in din startfras



- Skriv ner din seed-fras:** Enheten kommer nu att visa en 12-ords BIP39 seed-fras, ett ord i taget. Detta är det mest kritiska steget i hela processen.


**Viktiga säkerhetsrutiner:**


- Skriv varje ord tydligt på papper (använd de medföljande seed fraskorten om sådana finns)
- Dubbelkolla varje ord när du skriver det
- Fotografera aldrig seed-frasen med din telefon
- Skriv aldrig in orden i någon dator eller telefon
- Håll din seed-fras privat - dela inte din skärm eller visa den för andra



- Verifiera din seed-fras:** När du har skrivit ner alla 12 orden kommer enheten att be dig att bekräfta flera ord från frasen för att säkerställa att du har spelat in dem korrekt. Använd knapparna för att välja rätt ord för varje fråga.


**Proffstips: ** Innan du går vidare, öva på att läsa din seed-fras högt för dig själv (tyst, så att andra inte kan höra). Detta hjälper till att upptäcka eventuella handstilsfel eller tvetydigheter.


### Anslutningsmetod



- Välj anslutningstyp:** Jade firmware stöder två anslutningsmetoder:
 - USB:** Trådbunden anslutning via USB-C-kabel (rekommenderas för denna workshop)
 - Bluetooth:** Trådlös anslutning till mobila enheter



- Välj **USB** för tillfället, eftersom det är det enklaste alternativet för stationär wallet-programvara och inte introducerar trådlösa attackvektorer.



- Enhetsnamn:** Jade kommer att visa en unik identifierare som "Connect Jade A7D924". Denna identifierare hjälper dig att skilja mellan flera hårdvaruplånböcker om du slutar bygga mer än en. Gör en anteckning om denna identifierare om så önskas.


### Anslutning till Wallet-programvaran


Du har nu två huvudalternativ för gränssnittet mot din nyskapade hårdvara wallet: mobilappen Blockstream Green (för användning på språng) eller Sparrow Wallet (för skrivbordsanvändning med mer avancerade funktioner). I den här workshopen kommer vi att fokusera på Sparrow Wallet, eftersom det ger bättre insyn i de tekniska detaljerna i Bitcoin-transaktioner.


#### Alternativ 1: Blockstream Green mobilapp (snabbstart)


Om du vill testa din enhet snabbt med en mobil enhet:



- Ladda ner **Blockstream Green**-appen från App Store (iOS) eller Google Play (Android)
- Öppna appen och välj "Anslut Hardware Wallet"
- Välj "Jade" från listan över enheter som stöds
- Anslut din Jade till din telefon med en USB-C till USB-C-kabel (eller USB-C till Lightning-adapter för iPhone 15+)
- Följ anvisningarna på skärmen för att ansluta och skapa din första wallet


**Notering om Liquid:** Blockstream Green-appen stöder både Bitcoin och Liquid (en Bitcoin-sidokedja). Om du använder Liquid-funktioner kan du bli ombedd att "Exportera huvudblindnyckel" - detta gör att appen kan se transaktionsbelopp i Liquid-nätverket, som annars är konfidentiella. För den här workshopen kan du hoppa över Liquid-funktioner och fokusera på vanliga Bitcoin-transaktioner.


#### Alternativ 2: Sparrow Wallet (rekommenderas för verkstad)


Sparrow Wallet är ett kraftfullt skrivbordsprogram som ger dig detaljerad kontroll över dina Bitcoin-transaktioner och ansluter sömlöst till din Jade-hårdvara wallet.


**Installation:**



- Ladda ner Sparrow Wallet från den officiella webbplatsen: [sparrowwallet.com](https://sparrowwallet.com)
- Verifiera nedladdningssignaturen (se dokumentationen för Sparrow för mer information)
- Installera och starta programmet


**Ansluter din jade till Sparrow:**



- I Sparrow, gå till **Filer → Ny Wallet**
- Ge din wallet ett namn (t.ex. "My Jade Wallet")
- Klicka på **Ansluter Hardware Wallet**
- Sparrow bör automatiskt upptäcka din inkopplade Jade-enhet
- Om du uppmanas att göra det, bekräfta anslutningen på Jade-displayen genom att trycka på båda knapparna
- Välj önskad typ av skript:
 - Native Segwit (P2WPKH):** Rekommenderas för nybörjare - lägsta avgifter, bredast kompatibilitet med moderna plånböcker
 - Nested Segwit (P2SH-P2WPKH):** För kompatibilitet med äldre tjänster
 - Taproot (P2TR):** Mest avancerad, erbjuder bäst integritet och lägst avgifter, men kräver avancerat stöd för wallet
- Klicka på **Importera nyckelförvaring** för att slutföra anslutningen


**Konfigurera Sparrow:s serveranslutning:**


Innan du kan se ditt saldo eller sända transaktioner måste Sparrow ansluta till en Bitcoin-nod för att hämta blockkedjedata. Du har flera alternativ, vart och ett med olika avvägningar mellan bekvämlighet, integritet och förtroende:



- Public Electrum Server (enklast, minst privat):** Ansluter till en publik server som drivs av en tredje part. Snabb att installera, men servern kan se dina wallet:s adresser och eventuellt koppla dem till din IP-adress. Bra för testning på testnät.
 - I Sparrow går du till **Verktyg → Inställningar → Server**
 - Välj **Public Server** och välj en server från listan
 - Klicka på **Testa anslutning** för att verifiera



- Bitcoin Core eller Knots Node (Mest privat, mest arbete):** Kör din egen fullständiga Bitcoin-nod. Detta är guldstandarden för integritet och verifiering, eftersom du validerar varje transaktion själv och inte litar på någon annans server. Det kräver dock att du laddar ner hela blockkedjan (~ 600 GB) och håller din nod synkroniserad.
 - Installera och synkronisera Bitcoin-kärnor eller knutar
 - I Sparrow går du till **Verktyg → Inställningar → Server**
 - Välj **Bitcoin Core or Knots** och ange anslutningsuppgifterna för din nod



- Private Electrum Server (Good balance):** Hosta din egen Electrum-server (som Fulcrum eller Electrs) ansluten till din Bitcoin Core- eller Knots-nod. Erbjuder full integritet utan att behöva köra Sparrow på samma maskin som din nod.
 - Konfigurera en Electrum-server som pekar på din Bitcoin Core- eller Knots-nod
 - I Sparrow går du till **Verktyg → Inställningar → Server**
 - Välj **Private Electrum** och ange URL:en till din server


För den här workshopen är det helt okej att använda en **Public Electrum Server** för testnet-transaktioner. I en produktionsmiljö med riktiga pengar bör du överväga att köra din egen nod eller använda en betrodd privat server för maximal integritet.


#### Alternativ 3: Blockstream Green Desktop App (snabbstart)


Blockstream Green är programvaran för att slutföra installationen av JadeDIY och den måste vara med skrivbordsversionen



- Hämta den officiella Blockstream-applikationen - det här är länken till den från deras webbplats. När du är där klickar du på [Ladda ner nu](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Beroende på var du hämtar dina filer kommer filen troligen att finnas i mappen Downloads. Kontrollera där och dubbelklicka på den körbara filen för att installera programvaran.


![image](assets/fr/13.webp)



- Du kanske måste ge administratörsrättigheter för att köra installationsprogrammet. När du har gjort det kommer ett fönster att dyka upp som ska se ut som på följande bild - klicka på **Nästa**.


![image](assets/fr/14.webp)



- Välj var du vill att det installerade programmet ska finnas (en plats med dina andra program eller en plats som är lätt att hitta) och klicka sedan på **Nästa**.


![image](assets/fr/15.webp)



- Installationsprogrammet kommer att fråga efter ett genvägsnamn. Ange ett eller behåll standardinställningen och klicka sedan på **Nästa**.


![image](assets/fr/16.webp)



- Om du vill ha en genväg på skrivbordet markerar du rutan, annars klickar du på **Nästa**.


![image](assets/fr/17.webp)



- Klicka slutligen på **Install** och vänta några minuter på att installationen ska slutföras.


![image](assets/fr/18.webp)



- Förloppsindikatorn ska fyllas till slutet.


![image](assets/fr/19.webp)



- När den är klar kommer en ny sida att visas - klicka på **Finish**.


![image](assets/fr/20.webp)



- Hitta ditt nyligen installerade Blockstream-program (exempel visas i Start-menyn i Windows 11).


![image](assets/fr/21.webp)



- När du har hittat den klickar du på för att starta - en startskärm bör visas.


### Verifiera din installation


När du är ansluten till Sparrow (eller en annan wallet-applikation):



- Kontrollera dina adresser:** Sparrow kommer att visa mottagningsadresser som härrör från din seed-fras. Du kan verifiera en adress på din Jade-enhet genom att gå till fliken "Receive" i Sparrow och klicka på "Display Address" - adressen bör visas både på din datorskärm och på Jade-skärmen.



- Skapa en mottagningsadress:** Klicka på fliken **Mottagning** i Sparrow och kopiera din första mottagningsadress från Bitcoin.



- Redo för transaktioner:** Din maskinvara wallet är nu helt konfigurerad och redo att ta emot och signera Bitcoin-transaktioner. Gå vidare till nästa avsnitt för att öva på att signera en testnet-transaktion.



---

### Checklista för snabb installation



- Jade firmware startar framgångsrikt
- Ny wallet skapad med 12-ords seed-fras
- Fröfras nedskriven tydligt och verifierad
- USB anslutningsläge valt
- Wallet-programvara (Sparrow) installerad och ansluten
- Serveranslutning konfigurerad (publik Electrum för mainnet)
- Första mottagningsadressen genererad och verifierad på enheten



---

**MIT-licens**


**Copyright (c) 2025 Bitcoin-nätverket NYC**


Tillstånd beviljas härmed, kostnadsfritt, till varje person som erhåller en kopia av denna programvara och tillhörande dokumentationsfiler ("Programvaran"), att handla med Programvaran utan begränsningar, inklusive utan begränsning rätten att använda, kopiera, modifiera, slå samman, publicera, distribuera, underlicensiera och/eller sälja kopior av Programvaran, och att tillåta personer till vilka Programvaran tillhandahålls att göra det, under förutsättning att följande villkor uppfylls:


Ovanstående meddelande om upphovsrätt och detta meddelande om tillstånd skall ingå i alla kopior eller väsentliga delar av programvaran.


PROGRAMVARAN TILLHANDAHÅLLS "I BEFINTLIGT SKICK", UTAN GARANTIER AV NÅGOT SLAG, UTTRYCKLIGA ELLER UNDERFÖRSTÅDDA, INKLUSIVE MEN INTE BEGRÄNSAT TILL GARANTIER FÖR SÄLJBARHET, LÄMPLIGHET FÖR ETT VISST ÄNDAMÅL OCH ICKE-INTRÅNG. UPPHOVSMÄNNEN ELLER UPPHOVSRÄTTSINNEHAVARNA SKA UNDER INGA OMSTÄNDIGHETER HÅLLAS ANSVARIGA FÖR ANSPRÅK, SKADOR ELLER ANNAT ANSVAR, OAVSETT OM DET RÖR SIG OM AVTAL, SKADESTÅND ELLER ANNAT, SOM UPPSTÅR TILL FÖLJD AV, PÅ GRUND AV ELLER I SAMBAND MED PROGRAMVARAN ELLER ANVÄNDNINGEN AV ELLER ANDRA MELLANHAVANDEN MED PROGRAMVARAN.


---