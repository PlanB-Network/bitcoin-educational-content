---
name: Mnemonic fras - Tärningsslag
description: Hur man generate din egen återhämtningsfras med tärningar?
---

![cover](assets/cover.webp)


I den här guiden lär du dig hur du manuellt konstruerar en återhämtningsfras för en Bitcoin Wallet med hjälp av tärningskast.


**VARNING:** För att generera en Mnemonic-fras på ett säkert sätt krävs att man inte lämnar några digitala spår under skapandet, vilket är nästan omöjligt. Annars skulle Wallet utgöra en alldeles för stor attackyta, vilket avsevärt ökar risken för att dina bitcoins blir stulna. **Det avråds därför starkt från att överföra pengar till en Wallet som är beroende av en återställningsfras som du själv har genererat Även om du följer denna handledning till punkt och pricka finns det en risk att återställningsfrasen kan äventyras. **Därför bör denna handledning inte användas för att skapa en riktig Wallet.** Att använda en Hardware Wallet för denna uppgift är mycket mindre riskabelt, eftersom den genererar frasen offline, och riktiga kryptografer har övervägt att använda kvalitativa entropikällor.


Denna handledning kan följas för experimentella ändamål endast för skapandet av en fiktiv Wallet, utan avsikt att använda den med riktiga bitcoins. Erfarenheten erbjuder dock två fördelar:



- För det första gör det att du bättre kan förstå mekanismerna i basen av din Bitcoin Wallet;
- För det andra gör det att du vet hur du ska göra det. Jag säger inte att det kommer att vara användbart en dag, men det kanske det blir!


## Vad är en Mnemonic-fras?


En återställningsfras, ibland även kallad "Mnemonic", "seed-fras" eller "hemlig fras", är en sekvens som vanligtvis består av 12 eller 24 ord och som genereras på ett pseudoslumpmässigt sätt från en entropikälla. Den pseudoslumpmässiga sekvensen kompletteras alltid med en kontrollsumma.


Mnemonic-frasen, tillsammans med en valfri passphrase, används för att deterministiskt härleda alla nycklar som är associerade med en HD (Hierarchical Deterministic) Wallet. Detta innebär att det från denna fras är möjligt att deterministiskt generate och återskapa alla privata och offentliga nycklar för Bitcoin Wallet, och följaktligen få tillgång till de medel som är associerade med den.

![mnemonic](assets/notext/1.webp)

Syftet med denna mening är att tillhandahålla ett lättanvänt sätt för säkerhetskopiering och återställning av bitcoins. Det är absolut nödvändigt att förvara Mnemonic-frasen på en trygg och säker plats, eftersom alla som innehar denna fras skulle ha tillgång till medlen i motsvarande Wallet. Om den används i samband med en traditionell Wallet, och utan en valfri passphrase, utgör den ofta en SPOF (Single Point Of Failure).

Vanligtvis ges denna fras till dig direkt när du skapar din Wallet, av programvaran eller Hardware Wallet som används. Det är dock också möjligt att generate denna fras själv och sedan ange den på det valda stödet för att härleda Wallet-nycklarna. Detta är vad vi kommer att lära oss att göra i denna handledning.


## Förberedelse av nödvändigt material


För att skapa din återställningsfras för hand behöver du:



- Ett pappersark;
- En penna eller blyertspenna, gärna i olika färger för att underlätta organiseringen;
- Flera tärningar för att minimera risken för partiskhet i samband med en obalanserad tärning;
- [Listan med 2048 BIP39-ord](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) utskrivet.


Därefter kommer det att bli nödvändigt att använda en dator med en terminal för att beräkna kontrollsumman. Det är just av denna anledning som jag avråder från den manuella genereringen av Mnemonic-frasen. Enligt min mening ökar en dators ingripande, även under de försiktighetsåtgärder som nämns i denna handledning, avsevärt sårbarheten hos en Wallet.


För en experimentell metod som rör en "fiktiv Wallet" är det möjligt att använda din vanliga dator och dess terminal. Men för en mer rigorös metod som syftar till att begränsa riskerna för att kompromissa med din fras, skulle idealet vara att använda en dator som är frånkopplad från internet (helst utan en wifi-komponent eller RJ45-kabelanslutning), utrustad med ett minimum av kringutrustning (som alla bör anslutas med kabel för att undvika Bluetooth), och framför allt, som körs på en Linux-distribution med minnesförlust som [Tails] (https://tails.boum.org/index.fr.html), startad från ett flyttbart medium.


![mnemonic](assets/notext/2.webp)


I ett verkligt sammanhang skulle det vara avgörande att säkerställa sekretessen på din arbetsplats genom att välja en plats som är avskild från nyfikna blickar, utan persontrafik och utan kameror (webbkameror, telefoner ...).

Det rekommenderas att använda ett stort antal tärningar för att minska den inverkan som en eventuellt obalanserad tärning har på entropin. Innan tärningarna används rekommenderas att de kontrolleras: detta kan göras genom att testa dem i en skål med saltmättat vatten och låta tärningarna flyta. Kasta sedan varje tärning cirka tjugo gånger i saltvattnet och observera resultatet. Om ett eller två ansikten framstår som oproportionerligt jämfört med de andra, utöka testet med fler kast. Ett jämnt fördelat resultat tyder på att tärningen är tillförlitlig. Men om en eller två sidor regelbundet dominerar bör dessa tärningar läggas åt sidan, eftersom de kan äventyra entropin i din Mnemonic-fras och följaktligen säkerheten för din Wallet.

Under verkliga förhållanden skulle du, efter att ha utfört dessa kontroller, vara redo att generate den nödvändiga entropin. För en experimentell fiktiv Wallet som skapats som en del av denna handledning kan du naturligtvis hoppa över dessa förberedelser.


## Några påminnelser om återhämtningsfrasen


Till att börja med går vi igenom grunderna för att skapa en Mnemonic-fras enligt BIP39. Som tidigare förklarats härrör frasen från pseudoslumpmässig information av en viss storlek, till vilken en kontrollsumma läggs till för att säkerställa dess integritet.


Storleken på denna initiala information, som ofta kallas "entropi", bestäms av antalet ord som du vill få med i återställningsfrasen. De vanligaste formaten är fraser på 12 och 24 ord, vilket ger en entropi på 128 respektive 256 bitar. Här är en tabell som visar de olika entropistorlekarna enligt BIP39:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

Entropi är alltså ett slumpmässigt tal mellan 128 och 256 bitar. I den här handledningen tar vi exemplet med en fras på 12 ord, där entropin är 128 bitar, vilket innebär att vi kommer att generate en slumpmässig sekvens av 128 `0` eller `1`. Detta representerar ett nummer som består av 128 siffror i bas 2 (binärt).

Baserat på denna entropi genereras en kontrollsumma. En kontrollsumma är ett värde som beräknas från en uppsättning data och som används för att verifiera integriteten och giltigheten hos dessa data under överföring eller lagring. Checksummealgoritmer är utformade för att upptäcka oavsiktliga fel eller ändringar i data.

I fallet med vår Mnemonic-fras är kontrollsummans funktion att upptäcka eventuella inmatningsfel när frasen matas in i en Wallet-programvara. En ogiltig kontrollsumma signalerar att det finns ett fel i frasen. Omvänt visar en giltig kontrollsumma att frasen troligen är korrekt.


För att erhålla denna kontrollsumma skickas entropin genom SHA256 Hash-funktionen. Denna operation ger en 256-bitarssekvens som utdata, av vilken endast de första `N` bitarna kommer att behållas, `N` beroende på önskad längd på återställningsfrasen (se tabellen ovan). För en fras med 12 ord behålls således de första 4 bitarna av Hash.

![mnemonic](assets/en/3.webp)

Dessa första 4 bitar, som utgör kontrollsumman, läggs sedan till den ursprungliga entropin. I det här skedet är återställningsfrasen praktiskt taget uppbyggd, men den är fortfarande i binär form. För att omvandla den binära sekvensen till ord i enlighet med BIP39-standarden delar vi först upp sekvensen i 11-bitarssegment.

![mnemonic](assets/notext/4.webp)

Vart och ett av dessa paket representerar ett binärt tal som sedan omvandlas till ett decimaltal (bas 10). Vi lägger till `1` till varje nummer, eftersom man i databehandling börjar räkna från `0`, men BIP39-listan är numrerad från `1`.


![mnemonic](assets/notext/5.webp)


Slutligen anger siffran i decimaltal positionen för motsvarande ord i [listan med 2048 BIP39-ord] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). Allt som återstår är att välja ut dessa ord för att komponera återställningsfrasen för vår Wallet.


![mnemonic](assets/notext/6.webp)


Nu går vi över till att öva! Vi kommer att generate en 12-ords återställningsfras. Denna operation är dock identisk med en 24 ords fras, förutom att det skulle krävas 256 bitars entropi och en 8-bitars kontrollsumma, vilket anges i ekvivalenstabellen i början av detta avsnitt.


## Steg 1: Generering av entropi


Förbered ett pappersark, en penna och en tärning. Till att börja med måste vi generate 128 bitar slumpmässigt, det vill säga en sekvens av 128 "0" och "1" i rad. För att göra detta använder vi tärningar.

![mnemonic](assets/notext/7.webp)


Tärningar har 6 sidor, alla med samma sannolikhet att bli kastade. Vårt mål är dock att producera ett binärt resultat, vilket innebär två möjliga utfall. Därför kommer vi att tilldela värdet "0" till varje kast som landar på ett jämnt tal och "1" för varje udda tal. Som ett resultat kommer vi att utföra 128 kast för att skapa vår 128-bitars entropi. Om tärningen visar `2`, `4` eller `6` skriver vi `0`; för `1`, `3` eller `5` blir det `1`. Varje resultat noteras sekventiellt, från vänster till höger och uppifrån och ner.


För att underlätta följande steg kommer vi att gruppera bitarna i paket om fyra och tre, enligt bilden nedan. Varje rad måste innehålla 11 bitar: 2 paket med 4 bitar och ett paket med 3 bitar.


![mnemonic](assets/notext/8.webp)


Som du kan se i mitt exempel består det tolfte ordet för närvarande av endast 7 bitar. Dessa kommer i nästa steg att kompletteras med checksummans 4 bitar för att bilda de 11 bitarna.


![mnemonic](assets/notext/9.webp)


## Steg 2: Beräkning av kontrollsumman


Detta steg är det mest kritiska i den manuella genereringen av en Mnemonic-fras, eftersom det kräver användning av en dator. Som tidigare nämnts motsvarar kontrollsumman början på SHA256 Hash som genererats från entropin. Även om det är teoretiskt möjligt att beräkna en SHA256 för hand för en inmatning på 128 eller 256 bitar, kan denna uppgift ta en hel vecka. Dessutom skulle eventuella fel i de manuella beräkningarna upptäckas först i slutet av processen, vilket skulle tvinga dig att börja om från början. Därför är det otänkbart att göra detta steg med bara ett pappersark och en penna. En dator är nästan obligatorisk. Om du fortfarande vill lära dig att göra en SHA256 för hand förklarar vi hur du gör det i [CRYPTO301-kursen] (https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).


Av denna anledning avråder jag starkt från att skapa en manuell fras för en faktisk Wallet. Enligt min mening ökar användningen av en dator i detta skede, även med alla nödvändiga försiktighetsåtgärder, orimligt attackytan för Wallet.

För att beräkna kontrollsumman och samtidigt lämna så få spår som möjligt använder vi en Linux-distribution med minnesförlust från en flyttbar enhet med namnet **Tails**. Det här operativsystemet startar från ett USB-minne och arbetar helt och hållet i datorns RAM-minne utan att interagera med Hard-enheten. I teorin lämnar det alltså inga spår på datorn efter att den stängts av. Observera att Tails endast är kompatibelt med processorer av typen x86_64 och inte med processorer av typen ARM.

För att börja, från din vanliga dator, [ladda ner Tails-bilden från dess officiella webbplats] (https://tails.net/install/index.fr.html). Säkerställ att din nedladdning är äkta genom att använda utvecklarens signatur eller det verifieringsverktyg som erbjuds av webbplatsen.

![mnemonic](assets/notext/10.webp)

Först formaterar du ditt USB-minne och installerar sedan Tails med hjälp av ett verktyg som [Balena Etcher] (https://etcher.balena.io/).

![mnemonic](assets/notext/11.webp)

När du har bekräftat att flashningen har lyckats stänger du av datorn. Fortsätt sedan med att koppla bort strömmen Supply och ta bort Hard-enheten från datorns moderkort. Om det finns ett WiFi-kort ska det kopplas bort. På samma sätt ska du ta bort alla RJ45 Ethernet-kablar. För att minimera risken för dataläckage rekommenderas att du kopplar ur din internetbox och stänger av din mobiltelefon. Se dessutom till att koppla bort all överflödig kringutrustning från datorn, t.ex. mikrofon, webbkamera, högtalare eller headset, och kontrollera att övrig kringutrustning endast är ansluten via kabel. Alla dessa steg för att förbereda datorn är inte nödvändiga, men de bidrar helt enkelt till att minska attackytan så mycket som möjligt i ett verkligt sammanhang.


Kontrollera om BIOS är konfigurerat för att tillåta uppstart från en extern enhet. Om inte, ändra denna inställning och starta sedan om datorn. När du har säkrat datormiljön startar du om datorn från USB-minnet med Tails OS.


På välkomstskärmen i Tails väljer du det språk du vill använda och startar sedan systemet genom att klicka på "Starta Tails".


![mnemonic](assets/notext/12.webp)


Klicka på fliken "Program" på skrivbordet.


![mnemonic](assets/notext/13.webp)


Navigera till menyn `Utilities`.


![mnemonic](assets/notext/14.webp)


Och slutligen, klicka på applikationen `Terminal`.


![mnemonic](assets/notext/15.webp)


Du kommer till en ny tom kommandoterminal.


![mnemonic](assets/notext/16.webp)

Skriv kommandot `echo`, följt av din tidigare genererade entropi, och se till att infoga ett mellanslag mellan `echo` och din binära siffersekvens.

![mnemonic](assets/notext/17.webp)


Lägg till ett extra mellanslag och ange sedan följande kommando med hjälp av en _pipe_ (`|`):


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


I exemplet med min entropi ser det totala kommandot ut enligt följande:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


I detta kommando:



- `echo` används för att skicka bitsekvensen;
- `|`, _pipe_, används för att leda utdata från kommandot `echo` till indata för nästa kommando;
- `shasum` initierar en hashingfunktion som tillhör SHA-familjen (_Secure Hash Algorithm_);
- `-a` anger valet av en specifik hashingalgoritm;
- `256` anger att SHA256-algoritmen används;
- `-0` gör att indata tolkas som ett binärt tal.


Efter att du noggrant kontrollerat att din binära sekvens inte innehåller några skrivfel trycker du på `Enter` för att utföra kommandot. Terminalen kommer då att visa SHA256 Hash för din entropi.


![mnemonic](assets/notext/19.webp)


För närvarande uttrycks Hash i hexadecimalt format (bas 16). Till exempel är min:


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


För att slutföra vår Mnemonic-fras behöver vi bara de första 4 bitarna av Hash, som utgör kontrollsumman. I hexadecimalt format representerar varje tecken 4 bitar. Därför behåller vi bara det första tecknet i Hash. För en fras med 24 ord skulle det vara nödvändigt att ta hänsyn till de två första tecknen. I mitt exempel motsvarar detta bokstaven: `a`. Notera noggrant detta tecken någonstans på ditt ark och stäng sedan av datorn.


Nästa steg är att konvertera detta hexadecimala tecken (bas 16) till ett binärt värde (bas 2), eftersom vår fras är uppbyggd i detta format. För att göra detta kan du använda följande konverteringstabell:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

I mitt exempel motsvarar bokstaven "a" det binära talet "1010". Dessa 4 bitar bildar kontrollsumman för vår återställningsfras. Du kan nu lägga till dem till den entropi som redan noterats på ditt pappersark och placera dem i slutet av det sista ordet.


![mnemonic](assets/notext/20.webp)


Din Mnemonic-fras är nu komplett, men den är i binärt format. Nästa steg blir att konvertera den till decimalsystemet så att du sedan kan associera varje siffra med ett motsvarande ord i BIP39-listan.


## Steg 3: Omvandla ord till decimaltal


För att omvandla varje binär rad till ett decimaltal använder vi en metod som underlättar manuell beräkning. För närvarande har du tolv rader på ditt papper, var och en bestående av 11 binära siffror `0` eller `1`. För att fortsätta med omvandlingen till decimaltal ska du tilldela varje första siffra värdet `1024` om den är `1`, annars `0`. För den andra siffran tilldelas värdet `512` om det är `1`, annars `0`, och så vidare till den elfte siffran. Korrespondenserna är följande:



- 1:a bit: `1024`;
- 2:a bit: `512`;
- 3:e bit: `256`;
- 4:e bit: `128`;
- 5:e bit: `64`;
- 6:e bit: `32`;
- 7:e bit: `16`;
- 8:e biten: `8`;
- 9:e bit: `4`;
- 10:e bit: `2`;
- 11:e biten: `1`.


För varje rad lägger vi till de värden som motsvarar siffrorna `1` för att få det decimala talet som motsvarar det binära talet. Låt oss ta exemplet med en binär rad som är lika med:


```plaintext
1010 1101 101
```


Omvandlingen skulle bli enligt följande:

![mnemonic](assets/notext/21.webp)

Resultatet skulle då bli:


```plaintext
1389
```


För varje bit som är lika med `1`, rapportera det tillhörande numret nedan. För varje bit som är lika med `0`, rapportera ingenting.


![mnemonic](assets/notext/22.webp)

Sedan lägger du helt enkelt ihop alla siffror som validerats med "1" för att få det decimaltal som representerar varje binär linje. Till exempel, så här ser det ut för mitt ark:

![mnemonic](assets/notext/23.webp)


## Steg 4: Söka efter orden i Mnemonic-frasen


Med de erhållna decimalsiffrorna kan vi nu hitta motsvarande ord i listan för att komponera Mnemonic-frasen. Numreringen av de 2048 orden i BIP39-listan sträcker sig emellertid från "1" till "2048". Men våra beräknade binära resultat sträcker sig från "0" till "2047". Därför finns det en förskjutning på en enhet som måste korrigeras. För att korrigera denna förskjutning lägger man helt enkelt till `1` till de tolv tidigare beräknade decimaltalen.


![mnemonic](assets/notext/24.webp)


Efter denna justering har du rangordningen för varje ord i listan. Allt som återstår är att identifiera varje ord med dess nummer. Precis som med alla andra steg får du naturligtvis inte använda din dator för att utföra denna konvertering. Se därför till att du har skrivit ut listan i förväg.


[**-> Skriv ut BIP39-listan i A4-format.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Om t.ex. det nummer som härleds från första raden är 1721, kommer motsvarande ord att vara det 1721:a i listan:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

På detta sätt fortsätter vi successivt med de 12 orden för att konstruera vår Mnemonic-fras.


![mnemonic](assets/notext/26.webp)


## Steg 5: Skapa Bitcoin Wallet


Nu återstår bara att importera vår Mnemonic-fras till en Bitcoin Wallet-programvara. Beroende på vad vi föredrar kan detta göras på en stationär programvara för att få en Hot Wallet, eller på en Hardware Wallet för en Cold Wallet.


![mnemonic](assets/notext/27.webp)


Det är först under importen som du kan kontrollera att din checksumma är giltig. Om programvaran visar ett meddelande som "Invalid Checksum" betyder det att ett fel har smugit sig in i din skapelseprocess. I allmänhet beror detta fel antingen på en felberäkning under de manuella konverteringarna och tilläggen, eller på ett skrivfel när du angav din entropi i terminalen på Tails. Det kommer att bli nödvändigt att starta om processen från början för att rätta till dessa fel.


![mnemonic](assets/notext/28.webp)

När du har skapat din Wallet, glöm inte att säkerhetskopiera din återställningsfras på ett fysiskt medium, till exempel papper eller metall, och förstör kalkylbladet som användes under genereringen för att förhindra informationsläckage.


## Specialfall av alternativet tärningsslag på Coldcards


Hårdvaruplånböckerna från Coldcard-familjen erbjuder [en funktion som heter _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), för att generate din Wallet:s återställningsfras med tärningar. Den här metoden är utmärkt eftersom den ger dig direkt kontroll över skapandet av entropi, utan att du behöver använda en extern enhet för att beräkna kontrollsumman som i vår handledning.


Incidenter av Bitcoin-stöld har dock rapporterats nyligen på grund av felaktig användning av denna funktion. Ett alltför begränsat antal tärningskast kan leda till otillräcklig entropi, vilket teoretiskt sett gör det möjligt att brute force Mnemonic-frasen och stjäla de tillhörande bitcoins. För att undvika denna risk rekommenderas det att utföra minst 99 tärningskast på Coldcard, vilket säkerställer tillräcklig entropi.


Den metod för att tolka resultaten som Coldcard föreslår skiljer sig från den som presenteras i den här handledningen. Medan vi i handledningen rekommenderar 128 kast för att uppnå 128 bitars säkerhet, föreslår Coldcard 99 kast för att uppnå 256 bitars säkerhet. I vår metod är det bara två resultat som är möjliga för varje tärningskast: jämnt (`0`) eller udda (`1`). Därför är den entropi som genereras av varje kast lika med `log2(2)`. När det gäller Coldcard, som tar hänsyn till tärningarnas sex möjliga ansikten (från `1` till `6`), är entropin per kast lika med `log2(6)`. Det är därför vi i vår handledning måste utföra fler kast för att uppnå samma entropinivå.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```