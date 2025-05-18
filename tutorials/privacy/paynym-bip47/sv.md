---
name: BIP47 - PayNym

description: Hur PayNyms fungerar
---
***VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april kan applikationen inte längre användas av användare som inte har en egen Dojo. BIP47 är fortfarande användbart på Sparrow Wallet för alla användare och **på Samourai Wallet endast för användare som har en Dojo**.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> "Han är för stor", sa de alla, och kalkonhanen, som hade fötts med sporrar och trodde att han var en kejsare, svällde upp som ett skepp med alla segel hissade och marscherade rakt fram till honom i stort raseri med ögon röda som eld. Den stackars lilla ankungen visste inte om han skulle stå på sig eller springa sin väg och var mycket olycklig eftersom han föraktades av alla ankorna på gården.

![BIP47, the ugly duckling illustration](assets/1.webp)


En av de viktigaste frågorna för Bitcoin-protokollet är återanvändning av Address. Nätverkets transparens och distribution gör att denna praxis är farlig för användarnas integritet. För att undvika problem relaterade till detta rekommenderas att man använder en ny tom mottagande Address för varje ny inkommande betalning till en Wallet, vilket kan vara komplicerat att uppnå i vissa fall.


Denna kompromiss är lika gammal som vitboken. Satoshi varnade oss redan för denna risk i sitt arbete som publicerades i slutet av 2008:


> Som en extra brandvägg bör ett nytt nyckelpar användas för varje transaktion för att förhindra att de kopplas till en gemensam ägare.

Det finns många lösningar för att ta emot flera betalningar utan Address-återanvändning. Var och en av dem har sina kompromisser och nackdelar. Bland alla dessa lösningar finns [BIP47] (https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki), ett förslag som utvecklats av Justus Ranvier och publicerades 2015, som gör det möjligt att generera återanvändbara betalningskoder. Målet är att göra det möjligt att göra flera transaktioner till samma person utan att återanvända en Address.


Inledningsvis möttes detta förslag med förakt av en del av communityn och det lades aldrig till i Bitcoin Core. Vissa programvaror valde dock fortfarande att implementera det på egen hand. Till exempel utvecklade Samourai Wallet sin egen implementering av BIP47: PayNym. Idag finns den här implementationen tillgänglig på Samourai Wallet för smartphones, samt på [Sparrow Wallet] (https://sparrowwallet.com/) för PC.


Med tiden har Samourai programmerat nya funktioner som är direkt relaterade till PayNym. Nu finns det ett helt ekosystem av verktyg tillgängliga för att optimera användarnas integritet baserat på PayNym och BIP47.

I den här artikeln kommer du att upptäcka principen för BIP47 och PayNym, mekanismerna för dessa protokoll och de praktiska tillämpningar som följer av dem. Jag kommer bara att Address den första versionen av BIP47, som för närvarande används för PayNym, men versionerna 2, 3 och 4 fungerar praktiskt taget på samma sätt.


**Notera** att den enda större skillnaden finns i aviseringstransaktionen:


- Version 1 använder en enkel Address med OP_RETURN för avisering,
- I version 2 används ett Multisig-skript (bloom-Multisig) med OP_RETURN,
- I version 3 och 4 används helt enkelt ett Multisig-skript (cfilter-Multisig).


De mekanismer som diskuteras i den här artikeln, inklusive de kryptografiska metoder som studerats, är därför tillämpliga på alla fyra versionerna. Hittills har PayNym-implementeringen på Samourai Wallet och Sparrow använt den första versionen av BIP47.


## Sammanfattning:


1- Problemet med återanvändning av Address.


2- Principerna för BIP47 och PayNym.


3- Handledning: Använda PayNym.



- Bygga en BIP47-transaktion med Samourai Wallet.
- Bygga en BIP47-transaktion med Sparrow Wallet.


4- BIP47:s funktionssätt.



- Den återanvändbara betalningskoden.
- Den kryptografiska metoden: Diffie-Hellman-nyckel Exchange etablerad på elliptiska kurvor (ECDH).
- Meddelandetransaktionen.
- Uppbyggnad av meddelandetransaktionen.
- Mottagande av meddelandetransaktionen.
- Betalningstransaktionen BIP47.
- Mottagande av BIP47-betalningen och härledning av den privata nyckeln.
- Återbetalning av BIP47-betalningen.


5- Härledda användningsområden för PayNym.


6- Min personliga åsikt om BIP47.


## Problemet med återanvändning av Address.


En mottagande Address används för att ta emot bitcoins. Den genereras från en publik nyckel genom att hasha den och tillämpa ett specifikt format. Det gör det möjligt att skapa ett nytt utgiftsvillkor för ett mynt för att ändra dess ägare.


För att lära dig mer om hur du genererar en mottagande Address rekommenderar jag att du läser den sista delen av den här artikeln: ** Bitcoin Wallet - utdrag från** [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).


Dessutom har du förmodligen redan hört från en kunnig bitcoiner att mottagningsadresser är för engångsbruk, och att du bör generate en ny för varje ny inkommande betalning till din Wallet. Okej, men varför?


I grund och botten äventyrar Address-återanvändning inte direkt dina medel. Användningen av kryptografi på elliptiska kurvor gör att du kan bevisa för nätverket att du har en privat nyckel utan att avslöja den nyckeln. Därför kan du låsa flera olika UTXO:er (Unspent Transaction Outputs) på samma Address och spendera dem vid olika tidpunkter. Om du inte avslöjar den privata nyckeln som är kopplad till den Address kan ingen komma åt dina medel. Problemet med återanvändning av Address är mer relaterat till integritet.


Som nämndes i inledningen innebär Bitcoin-nätverkets transparens och distribution att alla användare med tillgång till en nod kan följa transaktionerna i betalningssystemet. Som ett resultat kan de se de olika saldona för adresser. Satoshi Nakamoto nämnde sedan möjligheten att generera nya nyckelpar, och därmed nya adresser, för varje ny inkommande betalning till en Wallet. Målet skulle vara att ha en extra brandvägg i händelse av en association mellan användarens identitet och ett av deras nyckelpar.


Idag, när det finns kedjeanalysföretag och utvecklingen av KYC (Know Your Customer), är användningen av tomma adresser inte längre en extra brandvägg, utan en skyldighet för alla som bryr sig ens lite om sin integritet.


Strävan efter integritet är inte en komfort eller en fantasi hos Maximalist Bitcoiners. Det är en specifik parameter som direkt påverkar din personliga säkerhet och säkerheten för dina medel. För att hjälpa dig att förstå detta är här ett mycket konkret exempel:



- Bob köper Bitcoin genom Dollar Cost Averaging (DCA), vilket innebär att han förvärvar en liten mängd Bitcoin med jämna mellanrum för att beräkna genomsnittet av sitt ingångspris. Bob skickar systematiskt de köpta medlen till samma mottagande Address. Han köper 0,01 Bitcoin varje vecka och skickar det till samma Address. Efter två år har Bob samlat på sig en hel Bitcoin på denna Address.
- Bagaren på hörnet accepterar betalningar med Bitcoin. Bob är glad över att kunna spendera Bitcoin och går för att köpa sin baguette i satoshis. För att betala använder han de medel som är låsta med hans Address. Hans bagare vet nu att han äger en Bitcoin. Detta betydande belopp kan väcka avund och Bob riskerar potentiellt en fysisk attack i framtiden.


Address återanvändning gör att en observatör kan göra en obestridlig koppling mellan dina olika UTXO:er och ibland mellan din identitet och hela din Wallet.

Det är därför som de flesta Bitcoin Wallet-program automatiskt genererar en ny mottagande Address när du klickar på knappen "Receive". För vanliga användare är det inte ett stort besvär att vänja sig vid att använda nya adresser. Men för en online-verksamhet, en Exchange eller en donationskampanj kan denna begränsning snabbt bli ohanterlig.

Det finns många lösningar för dessa organisationer. Var och en av dem har sina fördelar och nackdelar, men hittills, och som vi kommer att se senare, sticker BIP47 verkligen ut från de andra.


Denna fråga om Address återanvändning är långt ifrån försumbar i Bitcoin. Som du kan se i diagrammet nedan från webbplatsen oxt.me är den totala återanvändningsgraden för Address av Bitcoin-användare för närvarande 52%:

Graf från OXT.me som visar utvecklingen av den totala återanvändningsgraden för Address i Bitcoin-nätverket.


![image](assets/2.webp)

_Credit: OXT_


Majoriteten av dessa återanvändningar kommer från börser, som av effektivitets- och bekvämlighetsskäl återanvänder samma Address många gånger. Hittills skulle BIP47 vara den bästa lösningen för att stävja detta fenomen bland börserna. Detta skulle bidra till att minska den totala återanvändningsgraden av Address utan att orsaka för mycket friktion för dessa enheter.


Denna globala åtgärd över hela nätverket är särskilt relevant i detta fall. Återanvändning av Address är inte bara ett problem för den person som ägnar sig åt detta, utan även för alla som gör affärer med dem. Förlusten av integritet på Bitcoin fungerar som ett virus som sprids från användare till användare. Genom att studera ett globalt mått på alla nätverkstransaktioner kan vi förstå omfattningen av detta fenomen.


## Principerna för BIP47 och PayNym.


BIP47 syftar till att tillhandahålla ett enkelt sätt att ta emot flera betalningar utan Address återanvändning. Dess funktion baseras på användningen av en återanvändbar betalningskod.


På så sätt kan flera avsändare skicka flera betalningar till en enda återanvändbar betalningskod för en annan användare, utan att mottagaren behöver tillhandahålla en ny tom Address för varje ny transaktion.


En användare kan fritt dela sin betalningskod (på sociala nätverk, på sin webbplats ...) utan risk för integritetsförlust, till skillnad från en vanlig mottagare av Address eller en offentlig nyckel.

För att genomföra en Exchange måste båda användarna ha en Bitcoin Wallet med en BIP47-implementering, t.ex. PayNym på Samourai Wallet eller Sparrow Wallet. Genom att koppla ihop de två användarnas betalkoder upprättas en hemlig kanal mellan dem. För att denna kanal ska kunna upprättas måste avsändaren göra en transaktion på Bitcoin Blockchain: meddelandetransaktionen (jag förklarar mer om detta senare).


Sambandet mellan de två användarnas betalkoder genererar delade hemligheter som i sig generate ett stort antal unika Bitcoin-mottagaradresser (exakt 2^32). I verkligheten skickas således inte betalningen med BIP47 till betalningskoden, utan till helt normala adresser som härrör från de inblandade parternas betalningskoder.


Betalningskoden fungerar som en virtuell identifierare, härledd från Wallet seed. I HD Wallet härledningsstruktur finns betalkoden på djup 3, på Wallet kontonivå.


![image](assets/3.webp)


Dess härledningsändamål anges som 47' (0x8000002F) med hänvisning till BIP47. Exempelvis skulle en härledningsväg för en återanvändbar betalkod vara: ** m/47'/0'/0'/**


För att ge dig en uppfattning om hur en betalningskod ser ut, här är min: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Den kan också kodas som en QR-kod för att underlätta kommunikationen:


![image](assets/4.webp)


När det gäller PayNym Bots, de robotar du ser på Twitter, är de helt enkelt visuella representationer av din betalningskod, skapade av Samourai Wallet. De genereras med hjälp av en Hash-funktion, vilket gör dem nästan unika. Här är min med dess identifierare: **+throbbingpond8B1**


![image](assets/5.webp)


Dessa botar har inte någon egentlig teknisk nytta. Istället underlättar de interaktionen mellan användare genom att skapa en virtuell visuell identitet.


För användaren är processen att göra en BIP47-betalning med PayNym-implementeringen extremt enkel. Låt oss föreställa oss att Alice vill skicka betalningar till Bob:


1. Bob delar med sig av sin QR-kod eller direkt sin återanvändbara betalkod. Han kan placera den på sin webbplats, på sina olika offentliga sociala nätverk eller skicka den till Alice via något annat kommunikationsmedel.

2. Alice öppnar sin Samourai- eller Sparrow-programvara och skannar eller klistrar in Bobs betalkod.

3. Alice länkar sitt PayNym med Bobs ("Follow" på engelska). Denna operation görs off-chain och förblir helt gratis.

4. Alice kopplar ihop sitt PayNym med Bobs ("Connect" på engelska). Denna operation görs "On-Chain". Alice måste betala transaktionsavgifterna Mining samt en fast avgift på 15 000 Sats för tjänsten på Samourai. Serviceavgifterna är undantagna på Sparrow. Detta steg är vad vi kallar aviseringstransaktionen.

5. När meddelandetransaktionen har bekräftats kan Alice skapa en BIP47-betalningstransaktion till Bob. Hennes Wallet kommer automatiskt att generate en ny tom mottagande Address för vilken endast Bob har den privata nyckeln.


Att utföra aviseringstransaktionen, dvs. ansluta sin PayNym, är en obligatorisk förutsättning för att göra BIP47-betalningar. När detta är gjort kan dock avsändaren göra flera betalningar till mottagaren (exakt 2^32) utan att behöva utföra en ny aviseringstransaktion.


Du kanske har lagt märke till att det finns två olika sätt att länka PayNyms till varandra: "follow" och "connect". Anslutningsoperationen ("connecter") motsvarar BIP47-meddelandetransaktionen, som helt enkelt är en Bitcoin-transaktion med viss information som överförs via en OP_RETURN-utgång. På så sätt hjälper den till att upprätta krypterad kommunikation mellan de två användarna för att producera de delade hemligheter som krävs för att generera nya tomma mottagningsadresser.


Å andra sidan möjliggör länkningsoperationen ("follow" eller "relier") en länk på Soroban, ett krypterat kommunikationsprotokoll baserat på Tor, speciellt utvecklat av Samourai-teamen.


För att sammanfatta:



- Att länka två PayNyms ("follow") är helt gratis. Det hjälper till att upprätta off-chain-krypterad kommunikation, särskilt för att använda Samourais samarbetsverktyg för transaktioner (Stowaway eller StonewallX2). Denna operation är specifik för PayNym och beskrivs inte i BIP47.
- Att ansluta två PayNyms medför en kostnad. Detta innebär att utföra aviseringstransaktionen för att initiera anslutningen. Kostnaden består av eventuella serviceavgifter, transaktionsavgifter Mining och 546 Sats som skickas till mottagarens aviserings-Address för att meddela dem om tunnelöppningen. Denna operation är relaterad till BIP47. När den är genomförd kan avsändaren göra flera BIP47-betalningar till mottagaren.


För att kunna koppla ihop två PayNyms måste de redan vara kopplade.


## Handledning: Använda PayNym.


Nu när vi har sett teorin, låt oss studera praktiken tillsammans. Tanken med handledningarna nedan är att länka min PayNym på min Sparrow Wallet med min PayNym på min Samourai Wallet. Den första handledningen visar hur du gör en transaktion med hjälp av den återanvändbara betalkoden från Samourai till Sparrow, och den andra handledningen beskriver samma mekanism från Sparrow till Samourai.


** Notera:** Jag utförde dessa tutorials på Testnet. Det här är inte riktiga bitcoins.


### Bygga en BIP47-transaktion med Samourai Wallet.


För att börja behöver du uppenbarligen Samourai Wallet-applikationen. Du kan ladda ner den direkt från Google Play Store eller med APK-filen som finns på den officiella Samourai-webbplatsen.


När Wallet har initialiserats, om du inte redan har gjort det, begär du ditt PayNym genom att klicka på plusset (+) längst ned till höger och sedan på "PayNym".


Det första steget för att göra en BIP47-betalning är att hämta den återanvändbara betalkoden från vår mottagare. Därefter kommer vi att kunna ansluta till dem och därefter länka:


![video](assets/6.mp4)


När aviseringstransaktionen är bekräftad kan jag skicka flera betalningar till min mottagare. Varje transaktion kommer automatiskt att göras med en ny tom Address som mottagaren har nycklarna till. Mottagaren behöver inte vidta några åtgärder, allt är beräknat på min sida.


Så här gör du en BIP47-transaktion på Samourai Wallet:


![video](assets/7.mp4)


### Bygga en BIP47-transaktion med Sparrow Wallet.


Precis som med Samourai måste du naturligtvis ha Sparrow-programvaran. Detta är tillgängligt på din dator. Du kan ladda ner den från deras [officiella webbplats] (https://sparrowwallet.com/).


Se till att verifiera utvecklarens signatur och integriteten hos den nedladdade programvaran innan du installerar den på din maskin.


Skapa en Wallet och begär ditt PayNym genom att klicka på "Show PayNym" i menyn "Tool" i det övre fältet:


![image](assets/8.webp)


Därefter måste du länka och ansluta ditt PayNym till mottagarens. För att göra detta anger du deras återanvändbara betalkod i fönstret "Find Contact", följer dem och utför sedan meddelandetransaktionen genom att klicka på "Link Contact":


![image](assets/9.webp)


När aviseringstransaktionen är bekräftad kan du skicka betalningar till den återanvändbara betalkoden. Så här gör du för att göra det:


![video](assets/10.mp4)


Nu när vi har kunnat studera den praktiska aspekten av PayNyms implementering av BIP47, låt oss se hur alla dessa mekanismer fungerar och vilka kryptografiska metoder som används.


## Det inre arbetet med BIP47.


För att studera mekanismerna för BIP47 är det viktigt att förstå strukturen för den hierarkiska deterministiska (HD) Wallet, mekanismerna för att härleda barnnyckelpar, liksom principerna för elliptisk kurva kryptografi. Lyckligtvis kan du hitta all nödvändig information för att förstå den här delen på min blogg:



- [Förståelse för härledningsvägarna för en Bitcoin Wallet](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-Bitcoin)



- [The Bitcoin Wallet - utdrag ur e-boken Bitcoin Democratized 2] (https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2)


### Den återanvändbara betalningskoden.


Som förklaras i den andra delen av detta dokument är den återanvändbara betalningskoden placerad på djup tre i HD Wallet. Den är något jämförbar med en xpub, både i sin placering och struktur, liksom i sin roll.


Här är de olika delarna som utgör en betalningskod på 80 byte:



- _Byte 0_: Version. Om du använder den första versionen av BIP47 kommer denna byte att vara lika med 0x01.
- _Byte 1_: Bitfältet. Detta utrymme är reserverat för att ge ytterligare indikationer vid specifik användning. Om du bara använder PayNym kommer denna byte att vara lika med 0x00.
- _Byte 2_: Y-pariteten. Denna byte indikerar 0x02 eller 0x03 beroende på pariteten (jämnt eller udda tal) för värdet på y-koordinaten för vår offentliga nyckel. För mer information om denna metod, läs steg 1 i avsnittet "Address-derivering" i den här artikeln.
- _Från byte 3 till byte 34_: X-värdet. Dessa byte anger x-koordinaten för vår offentliga nyckel. Sammankopplingen av x och y-pariteten ger oss vår komprimerade offentliga nyckel.
- _Från byte 35 till byte 66_: Kedjekoden. Detta utrymme är reserverat för den kedjekod som är kopplad till den ovannämnda offentliga nyckeln.
- _Från byte 67 till byte 79_: Utfyllnad. Detta utrymme är reserverat för eventuella framtida utvecklingar. För version 1 fyller vi det helt enkelt med nollor för att nå 80 byte, vilket är storleken på data för en OP_RETURN-utgång.


Här är den hexadecimala representationen av min återanvändbara betalningskod, som presenterades i föregående avsnitt, med färger som motsvarar de byte som presenteras ovan:

Därefter måste du också lägga till prefixbyten "P" för att snabbt identifiera att vi har att göra med en betalningskod. Denna byte är 0x47.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000**


Slutligen beräknar vi kontrollsumman för denna betalkod med hjälp av HASH256, vilket innebär dubbel hashing med SHA256-funktionen. Vi hämtar de fyra första bytena av denna sammanställning och sammanfogar dem i slutet (i rosa).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4**


Betalningskoden är klar, nu behöver vi bara konvertera den till Base 58:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Som du kan se liknar den här konstruktionen mycket strukturen hos en utökad publik nyckel av typen "xpub".


Under denna process för att erhålla vår betalningskod använde vi en komprimerad publik nyckel och en kedjekod. Dessa två Elements är resultatet av en deterministisk och hierarkisk härledning från Wallet seed, enligt följande härledningsväg: m/47'/0'/0'/


Konkret, för att få den offentliga nyckeln och kedjekoden för den återanvändbara betalningskoden, beräknar vi den privata huvudnyckeln från seed och härleder sedan ett barnpar med index 47 + 2^31 (härdad härledning). Sedan härleder vi ytterligare två barnpar med index 2^31 (härdad härledning).


**Note:** Om du vill lära dig mer om att härleda barnnyckelpar inom en hierarkisk deterministisk Bitcoin Wallet rekommenderar jag att du tar CRYPTO301.


### Den kryptografiska metoden: Elliptisk kurva Diffie-Hellman-nyckel Exchange (ECDH).


Den kryptografiska metod som används i kärnan av BIP47 är ECDH (Elliptic-Curve Diffie-Hellman). Detta protokoll är en variant av den klassiska Diffie-Hellman-nyckeln Exchange.


Diffie-Hellman, i sin första version, är ett nyckelöverenskommelseprotokoll som presenterades 1976 och som gör det möjligt för två parter, var och en med ett par offentliga och privata nycklar, att fastställa en delad hemlighet genom att utbyta information över en osäker kommunikationskanal.


![image](assets/11.webp)


Denna delade hemlighet (den röda nyckeln) kan sedan användas för andra uppgifter. Vanligtvis kan den delade hemligheten användas för att kryptera och dekryptera kommunikation över ett osäkert nätverk:


![image](assets/12.webp)


För att uppnå denna Exchange använder Diffie-Hellman modulär aritmetik för att beräkna den delade hemligheten. Här följer en förenklad förklaring av hur det fungerar:



- Alice och Bob kommer överens om en gemensam färg, i det här fallet gul. Den här färgen är känd av alla. Det är offentlig information.
- Alice väljer en hemlig färg, i det här fallet röd. Hon blandar de två färgerna, vilket resulterar i orange.
- Bob väljer en hemlig färg, i det här fallet blågrön. Han blandar de två färgerna, vilket resulterar i himmelsblått.
- Alice och Bob kan Exchange de färger de fick: orange och himmelsblå. Denna Exchange kan ske över ett osäkert nätverk och kan observeras av angripare.
- Alice blandar den himmelsblå färg som hon fått av Bob med sin hemliga färg (röd). Hon erhåller brun.
- Bob blandar den orangea färg han fått från Alice med sin hemliga färg (blågrön). Han får också brunt.


![image](assets/13.webp)


**Credit:** Ursprunglig idé: A.J. Han VinckVektorversion: FlugaalÖversättning: Dereckson, Public domain, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg


I denna förenkling representerar den bruna färgen den hemlighet som delas mellan Alice och Bob. Man bör föreställa sig att det i verkligheten är omöjligt för angriparen att separera de orange och himmelsblå färgerna för att få fram Alice eller Bobs hemliga färger.


Låt oss nu studera dess faktiska funktion. Vid första anblicken kan Diffie-Hellman verka komplicerad att förstå. I själva verket är funktionsprincipen nästan barnslig. Innan jag beskriver dess mekanismer i detalj ska jag snabbt påminna er om två matematiska begrepp som vi kommer att behöva (och som för övrigt också används i många andra kryptografiska metoder).


1. Ett primtal är ett naturligt tal som bara har två delare: 1 och sig självt. Till exempel är talet 7 ett primtal eftersom det bara kan delas med 1 och 7 (sig självt). Å andra sidan är talet 8 inte ett primtal eftersom det kan delas med 1, 2, 4 och 8. Det har därför inte bara två divisorer, utan fyra hela och positiva divisorer.

2. "Modulo" (benämns "mod" eller "%") är en matematisk operation som gör att två heltal kan returnera resten av den euklidiska divisionen av det första talet med det andra talet. Till exempel är 16 mod 5 lika med 1.


Diffie-Hellman-nyckeln Exchange mellan Alice och Bob fungerar på följande sätt:



- Alice och Bob bestämmer två gemensamma tal: p och g. p är ett primtal. Ju större talet p är, desto säkrare blir Diffie-Hellman. g är en primitiv rot till p. Dessa två tal kan kommuniceras i klartext över ett osäkert nätverk, de är motsvarigheten till den gula färgen i förenklingen ovan. Alice och Bob behöver bara ha exakt samma värden för p och g.
- När parametrarna har valts bestämmer Alice och Bob var för sig ett hemligt slumptal. Det slumptal som Alice får fram kallas a (motsvarar den röda färgen) och det slumptal som Bob får fram kallas b (motsvarar den blågröna färgen). Dessa två tal måste förbli hemliga.
- I stället för att utbyta dessa tal a och b kommer vardera parten att beräkna A (versaler) och B (versaler) så att:


A är lika med g multiplicerat med a modulo p:

**A = g^a % p**


B är lika med g upphöjt till potensen av b modulo p:

**B = g^b % p**



- Dessa nummer A (motsvarande den orange färgen) och B (motsvarande den himmelsblå färgen) kommer att utbytas mellan de två parterna. Exchange kan göras i klartext över ett osäkert nätverk.
- Alice, som nu känner till B, kommer att beräkna värdet på z så att:


z är lika med B multiplicerat med a modulo p:

**z = B^a % p**



- Som en påminnelse, B = g^b % p. Därför:

**z = B^a % p**

**z = (g^b)^a % p**


Enligt reglerna för exponentiering:

**(x^n)^m = x^nm**


Därför..:

**z = g^ba % p**



- Bob, som nu känner till A, kommer också att beräkna värdet av z på följande sätt:


z är lika med A multiplicerat med b modulo p:

**z = A^b % p**


Därför..:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Tack vare modulooperatorns distributivitet hittar Alice och Bob exakt samma värde för z. Detta tal representerar deras delade hemlighet, som motsvarar färgen brun i den tidigare förklaringen. De kan använda denna delade hemlighet för att kryptera kommunikationen mellan dem i ett osäkert nätverk.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


En angripare som har tillgång till p, g, A och B kommer inte att kunna beräkna a, b eller z. För att göra detta krävs att exponentiationen vänds, vilket är omöjligt att göra annat än genom att prova alla möjligheter en efter en eftersom vi arbetar med ett ändligt fält. Detta skulle vara likvärdigt med att beräkna den diskreta logaritmen, som är exponentieringens reciproka i en cyklisk finit grupp.


Därför är Diffie-Hellman säkert så länge vi väljer tillräckligt stora värden för a, b och p. Med parametrar på 2 048 bitar (ett tal med 600 decimaler) skulle det vara opraktiskt att testa alla möjligheter för a och b. Hittills har algoritmen ansetts vara säker med tal av denna storlek.


Det är just här som den största nackdelen med Diffie-Hellman-protokollet ligger. För att vara säker måste algoritmen använda stora tal. Som ett resultat av detta föredras nu ECDH-algoritmen, som är en variant av Diffie-Hellman som använder en algebraisk kurva, särskilt en elliptisk kurva. Detta gör att vi kan arbeta med mycket mindre tal med bibehållen säkerhet och därmed minska de beräknings- och lagringsresurser som krävs.


Den allmänna principen för algoritmen förblir densamma. Men istället för att använda ett slumpmässigt tal a och ett tal A som beräknas från a med hjälp av modulär exponentiering, kommer vi att använda ett par nycklar som är etablerade på en elliptisk kurva. I stället för att förlita sig på modulooperatorns distributivitet använder vi grupplagen för elliptiska kurvor, särskilt associativiteten i denna lag.

Om du inte har någon kunskap om hur privata och publika nycklar fungerar på en elliptisk kurva kommer jag att förklara grunderna i den här metoden i de första sex delarna av den här artikeln.


I korthet är en privat nyckel ett slumptal mellan 1 och n-1 (där n är kurvans ordning) och en publik nyckel är en unik punkt på kurvan som bestäms av den privata nyckeln genom punktaddition och dubblering från generatorpunkten, enligt följande:


**K = k-G**


Där K är den publika nyckeln, k är den privata nyckeln och G är generatorpunkten.


En av egenskaperna hos detta nyckelpar är att det är mycket lätt att bestämma K om man känner till k och G, men det är för närvarande omöjligt att bestämma k om man känner till K och G. Det är en envägsfunktion.


Med andra ord kan du enkelt beräkna den publika nyckeln om du känner till den privata nyckeln, men det är omöjligt att beräkna den privata nyckeln om du känner till den publika nyckeln. Denna säkerhet bygger återigen på att det är omöjligt att beräkna den diskreta logaritmen.


Vi kommer att använda denna egenskap för att anpassa vår Diffie-Hellman-algoritm. Funktionsprincipen för ECDH är således följande:



- Alice och Bob kommer överens om en kryptografiskt säker elliptisk kurva och dess parametrar. Denna information är offentlig.
- Alice genererar ett slumptal ka, som blir hennes privata nyckel. Denna privata nyckel måste förbli hemlig. Hon bestämmer sin offentliga nyckel Ka genom att lägga till och dubbla punkter på den valda elliptiska kurvan.


**Ka = ka-G**



- Bob genererar också ett slumptal kb, som blir hans privata nyckel. Han beräknar den tillhörande offentliga nyckeln Kb.


**Kb = kb-G**



- Alice och Bob Exchange sina publika nycklar Ka och Kb över ett osäkert offentligt nätverk.
- Alice beräknar en punkt (x, y) på kurvan genom att använda sin privata nyckel ka på Bobs offentliga nyckel Kb.


**(x, y) = ka-Kb**



- Bob beräknar en punkt (x, y) på kurvan genom att använda sin privata nyckel kb på Alices offentliga nyckel Ka.


**(x, y) = kb-Ka**



- Alice och Bob får samma punkt på den elliptiska kurvan. Den delade hemligheten kommer att vara x-koordinaten för denna punkt.


De får samma delade hemlighet eftersom:


**(x, y) = ka-Kb = ka-kb-G = kb-ka-G = kb-Ka**


En potentiell angripare som observerar det osäkra offentliga nätverket kan endast få tillgång till varje parts publika nycklar och de valda kurvparametrarna. Som tidigare förklarats kan de privata nycklarna inte fastställas enbart med hjälp av dessa två uppgifter, och angriparen kan därför inte komma åt hemligheten.

ECDH är en algoritm som möjliggör nyckeln Exchange. Den används ofta tillsammans med andra kryptografiska metoder för att definiera ett protokoll. Till exempel används ECDH i kärnan av TLS (Transport Layer Security), ett krypterings- och autentiseringsprotokoll som används för internettransport Layer. TLS använder ECDHE för nyckel Exchange, en variant av ECDH där nycklarna är efemära för att ge beständig konfidentialitet. Utöver ECDHE använder TLS även en autentiseringsalgoritm som ECDSA, en krypteringsalgoritm som AES och en Hash funktion som SHA256.


TLS definierar "s" i "https" och den lilla låsikonen som du ser i din webbläsare i det övre vänstra hörnet, vilket garanterar krypterad kommunikation. Så du använder för närvarande ECDH genom att läsa den här artikeln, och du använder den förmodligen dagligen utan att inse det.


### Transaktionen för anmälan


Som vi upptäckte i föregående avsnitt är ECDH en variant av Diffie-Hellman Exchange som involverar nyckelpar som upprättats på en elliptisk kurva. Lyckligtvis har vi gott om nyckelpar som uppfyller denna standard i våra Bitcoin-plånböcker!


Tanken är att använda nyckelparen från de båda parternas hierarkiskt deterministiska Bitcoin-plånböcker för att upprätta delade och efemära hemligheter mellan dem. Inom BIP47 används istället ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).


ECDHE används inledningsvis i BIP47 för att överföra avsändarens betalkod till mottagaren. Detta är den berömda aviseringstransaktionen. För att BIP47 ska kunna användas måste båda parter (avsändaren som skickar betalningar och mottagaren som tar emot betalningar) känna till varandras betalningskoder. Detta är nödvändigt för att härleda de efemära publika nycklarna och därmed de dedikerade mottagaradresserna.


Innan detta Exchange känner avsändaren logiskt sett redan till mottagarens betalkod eftersom de kan ha fått den off-chain, till exempel från deras webbplats eller sociala medier. Mottagaren känner dock inte nödvändigtvis till avsändarens betalkod. Den måste överföras till dem, annars kommer de inte att kunna härleda sina efemära nycklar och kommer därför inte att kunna veta var deras bitcoins finns och låsa upp sina medel. Den skulle kunna sändas till dem off-chain, med hjälp av ett annat kommunikationssystem, men detta skulle utgöra ett problem om Wallet återfås från seed.

Som jag redan har nämnt härleds BIP47-adresser inte från mottagarens seed (annars skulle det vara bättre att använda en av deras xpubs direkt), utan är resultatet av en beräkning som involverar både mottagarens betalningskod och avsändarens betalningskod. Om mottagaren förlorar sin Wallet och försöker återfå den från sin seed måste de därför nödvändigtvis ha alla betalningskoder för de personer som har skickat bitcoins till dem via BIP47.


Det skulle vara möjligt att använda BIP47 utan denna aviseringstransaktion, men då skulle varje användare behöva säkerhetskopiera sina kollegors betalkoder. Denna situation kommer att förbli ohanterlig tills ett enkelt och motståndskraftigt sätt att skapa, lagra och uppdatera dessa säkerhetskopior hittas. Aviseringstransaktionen är därför nästan obligatorisk i det nuvarande läget.


Förutom att säkerhetskopiera betalningskoder, som namnet antyder, fungerar denna transaktion också som ett meddelande till mottagaren. Den informerar deras klient om att en tunnel just har öppnats.


Innan jag förklarar mer i detalj hur meddelandetransaktionen fungerar rent tekniskt vill jag tala lite om sekretessmodellen. Enligt BIP47:s integritetsmodell är det motiverat att vidta vissa försiktighetsåtgärder när denna första transaktion konstrueras.


Betalkoden i sig utgör inte direkt någon integritetsrisk. Till skillnad från den klassiska Bitcoin-modellen, som gör det möjligt att bryta informationsflödet mellan användarens identitet och transaktioner, särskilt genom att hålla de publika nycklarna anonyma, kan betalkoden direkt kopplas till en identitet. Detta är inte obligatoriskt, men denna länk är inte farlig.


Betalningskoden härleder inte direkt de adresser som används för att ta emot BIP47-betalningar. Adresserna erhålls i stället genom att ECDHE tillämpas mellan underordnade nycklar för båda parternas betalningskoder.


Därför utgör en betalkod i sig inte någon direkt risk för den personliga integriteten eftersom endast meddelandet Address härleds från den. Viss information kan härledas från den, men normalt kan man inte veta vem man gör transaktioner med.


Det är därför viktigt att upprätthålla en strikt åtskillnad mellan användarnas betalningskoder. I detta avseende är kodens första kommunikationssteg ett kritiskt ögonblick för betalningens integritet, men det är ändå obligatoriskt för att protokollet ska fungera korrekt. Om en av betalkoderna kan hämtas av allmänheten (t.ex. från en webbplats) ska den andra koden, dvs. avsändarens kod, inte kopplas till den första.


Låt oss till exempel tänka oss att jag vill göra en donation med BIP47 till en fredlig proteströrelse i Kanada:



- Denna organisation har publicerat sin betalkod direkt på sin webbplats eller på sociala medier.
- Denna kod är därför förknippad med rörelsen.
- Jag hämtar den här betalkoden.
- Innan jag kan skicka en transaktion till dem måste jag se till att de känner till min personliga betalkod, som också är kopplad till min identitet eftersom jag använder den för att ta emot transaktioner från mina sociala nätverk.


Hur kan jag överföra den till dem? Om jag skickar den till dem med hjälp av ett konventionellt kommunikationsmedel kan informationen läcka ut och jag kan identifieras som en person som stöder fredliga rörelser.


Aviseringstransaktionen är förvisso inte den enda lösningen för att i hemlighet överföra avsändarens betalkod, men den uppfyller för närvarande denna roll perfekt genom att tillämpa flera säkerhetslager.


I diagrammet nedan representerar de röda linjerna det ögonblick då informationsflödet måste brytas, och de svarta pilarna representerar de obestridliga kopplingar som kan göras av en extern observatör:


![Privacy model diagram for reusable payment code](assets/15.webp)


I verkligheten är det för den klassiska sekretessmodellen för Bitcoin ofta svårt att helt bryta informationsflödet mellan nyckelparet och användaren, särskilt när man utför fjärrtransaktioner. Till exempel vid en donationskampanj måste mottagaren avslöja en Address eller en offentlig nyckel på sin webbplats eller på sociala medieplattformar. Korrekt användning av BIP47, dvs. med aviseringstransaktionen, löser detta problem genom ECDHE och krypteringen Layer som vi kommer att studera.


Uppenbarligen observeras den klassiska integritetsmodellen i Bitcoin fortfarande på nivån för de efemära offentliga nycklar som härrör från kopplingen av de två betalkoderna. De två modellerna är beroende av varandra. Jag vill här bara betona att till skillnad från den klassiska användningen av en publik nyckel för att ta emot bitcoins kan betalningskoden associeras med en identitet eftersom informationen "Bob gör en transaktion med Alice" bryts vid ett annat tillfälle. Betalningskoden används för generate-betalningsadresser, men genom att endast observera Blockchain är det omöjligt att associera en BIP47-betalningstransaktion med de betalningskoder som används för att göra den.


### Uppbyggnad av anmälningstransaktionen


Låt oss nu se hur denna aviseringstransaktion fungerar. Låt oss tänka oss att Alice vill skicka pengar till Bob med BIP47. I mitt exempel agerar Alice som avsändare och Bob som mottagare. Bob har redan publicerat sin betalningskod på sin webbplats, så Alice känner redan till Bobs betalningskod.


1- Alice beräknar en delad hemlighet med ECDH:



- Hon väljer ett nyckelpar från sin HD Wallet som ligger på en annan filial än hennes betalkod. Observera att detta par inte lätt ska kunna associeras med Alices meddelande Address eller Alices identitet (se föregående avsnitt).
- Alice väljer den privata nyckeln från detta par. Vi kommer att kalla den **a** (gemener).



- Alice hämtar den publika nyckel som är kopplad till Bobs avisering Address. Den här nyckeln är det första barnet som härleds från Bobs betalkod (index 0). Vi kallar denna publika nyckel för "B" (versaler). Den privata nyckel som är kopplad till denna publika nyckel kallas "b" (gemener). "B" bestäms genom punktaddition och dubblering på den elliptiska kurvan från "G" (generatorpunkten) med "b" (den privata nyckeln).

**B = b-G**



- Alice räknar ut en hemlig punkt "S" (versaler) på den elliptiska kurvan genom punktaddition och dubblering och använder sin privata nyckel "a" till Bobs offentliga nyckel "B".

**S = a-B**



- Alice beräknar blindningsfaktorn "f" som ska användas för att kryptera hennes betalningskod. För att göra detta kommer hon att generate ett pseudoslumpmässigt nummer med hjälp av HMAC-SHA512-funktionen. Som andra indata till denna funktion använder hon ett värde som endast Bob kommer att kunna hämta: (x), vilket är x-koordinaten för den tidigare beräknade hemliga punkten. Den första inmatningen är (o), som är den UTXO som förbrukats som en inmatning till denna transaktion (utpunkt).

**f = HMAC-SHA512(o, x)**


2- Alice konverterar sin personliga betalkod till bas 2 (binär).


3- Hon använder denna förblindande faktor som en nyckel för att utföra symmetrisk kryptering på nyttolasten i sin betalningskod. Krypteringsalgoritmen som används är helt enkelt XOR. Den operation som utförs liknar Vernam-krypteringen, även känd som "one-time pad":



- Alice delar först upp sin förblindningsfaktor i två delar: de första 32 bytena kallas "f1" och de sista 32 bytena kallas "f2". Så vi har:

**f = f1 || f2**



- Alice beräknar chiffertexten (x') för x-koordinaten för den offentliga nyckeln (x) för sin betalningskod och beräknar separat chiffertexten (c') för sin kedjekod (c). "f1" och "f2" fungerar som krypteringsnycklar och XOR-operationen används.

**x' = x XOR f1**

**c' = c XOR f2**



- Alice ersätter de faktiska värdena för den offentliga nyckelns abscissa (x) och kedjekoden (c) i sin betalningskod med de krypterade värdena (x') och (c').


Innan vi fortsätter med den tekniska beskrivningen av den här meddelandetransaktionen ska vi ta en stund för att diskutera XOR-operationen. XOR är en bitvis logisk operator baserad på boolesk algebra. Givet två bitoperander returnerar den 1 om motsvarande bitar är olika, och den returnerar 0 om motsvarande bitar är lika. Här är sanningstabellen för XOR baserad på värdena för operanderna D och E:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Till exempel:


**0110 XOR 1110 = 1000**


Eller..:


**010011 XOR 110110 = 100101**


Med ECDH är användningen av XOR som en kryptering Layer särskilt sammanhängande. För det första är krypteringen symmetrisk tack vare denna operatör. Detta gör att mottagaren kan dekryptera betalningskoden med samma nyckel som användes för krypteringen. Krypterings- och dekrypteringsnyckeln beräknas från den delade hemligheten med hjälp av ECDH.


Denna symmetri möjliggörs av XOR-operatorns kommutativitets- och associativitetsegenskaper:



- Övriga egenskaper:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Kommutativitet:

D ⊕ E = E ⊕ D



- Associativitet:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Symmetri:

Om: D ⊕ E = L

Då är D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Dessutom är den här krypteringsmetoden mycket lik Vernam-chiffret (One-Time Pad), den enda krypteringsalgoritm som hittills är känd och som har ovillkorlig (eller absolut) säkerhet. För att Vernam-krypteringen ska ha denna egenskap måste krypteringsnyckeln vara helt slumpmässig, ha samma storlek som meddelandet och bara användas en gång. I den krypteringsmetod som används här för BIP47 är nyckeln verkligen lika stor som meddelandet, och blindfaktorn är exakt lika stor som konkateneringen av x-koordinaten för den offentliga nyckeln med betalningskodkedjekoden. Denna krypteringsnyckel används bara en gång. Den här nyckeln härrör dock inte från en perfekt slumpmässig källa som en HMAC. Den är snarare pseudoslumpmässig. Det är därför inte ett Vernam-chiffer, men metoden är likartad.


Låt oss gå tillbaka till vår konstruktion av meddelandetransaktionen:


4- Alice har för närvarande sin betalningskod med en krypterad nyttolast. Hon kommer att konstruera och sända en transaktion som involverar hennes publika nyckel "A" som indata, en utdata till Bobs meddelande Address och en OP_RETURN-utdata som består av hennes betalningskod med den krypterade nyttolasten. Denna transaktion är aviseringstransaktionen.


OP_RETURN är en Opcode, vilket är ett skript som markerar en Bitcoin transaktionsutdata som ogiltig. Idag används den för att sända eller Anchor information om Bitcoin Blockchain. Den kan lagra upp till 80 byte data som registreras i kedjan och därför är synlig för alla andra användare.


Som vi såg i föregående avsnitt används Diffie-Hellman för att generate dela en hemlighet mellan två användare som kommunicerar över ett osäkert nätverk, vilket kan observeras av angripare. I BIP47 används ECDH för att kommunicera i Bitcoin-nätverket, som till sin natur är ett transparent kommunikationsnätverk som kan observeras av många angripare. Den delade hemligheten som beräknas genom Diffie-Hellman-nyckeln Exchange på den elliptiska kurvan används sedan för att kryptera den hemliga information som ska överföras: avsändarens (Alices) betalkod.


Här är ett diagram hämtat från BIP47 som illustrerar det vi just beskrivit:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Om vi matchar detta diagram med det jag beskrev tidigare:



- "Wallet Priv-Key" på Alices sida motsvarar: a.
- "Child Pub-Key 0" på Bobs sida motsvarar: B.
- "Notification Shared Secret" motsvarar: f.
- "Masked Payment Code" motsvarar den krypterade betalkoden, dvs. med den krypterade nyttolasten: x' och c'.
- "Anmälningstransaktion" är den transaktion som innehåller OP_RETURN.


Låt oss rekapitulera de steg vi just gick igenom för att utföra en aviseringstransaktion:



- Alice hämtar Bobs betalkod och meddelande Address.
- Alice väljer en UTXO som tillhör henne i sin HD Wallet med motsvarande nyckelpar.
- Hon räknar ut en hemlig punkt på den elliptiska kurvan med hjälp av ECDH.
- Hon använder denna hemliga punkt för att beräkna en HMAC, som är den bländande faktorn.
- Hon använder denna förblindande faktor för att kryptera nyttolasten för sin personliga betalkod.
- Hon använder en OP_RETURN-transaktionsutskrift för att överföra den maskerade betalkoden till Bob.


För att bättre förstå dess funktion, särskilt användningen av OP_RETURN, låt oss studera en riktig anmälningstransaktion tillsammans. Jag utförde en transaktion av denna typ på Testnet, som du kan hitta genom att klicka här:


https://Mempool.space/fr/Testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e**


![BIP47 Notification Transaction](assets/17.webp)


Kredit: https://blockstream.info/


Genom att observera denna transaktion kan vi redan se att den har en enda ingång och 4 utgångar:



- Den första utdata är OP_RETURN som innehåller min maskerade betalningskod.
- Den andra utgången från 546 Sats pekar på mottagarens meddelande Address.
- Det tredje utflödet på 15 000 Sats representerar serviceavgiften, eftersom jag använde Samourai Wallet för att konstruera denna transaktion.
- Den fjärde utmatningen på två miljoner Sats representerar förändringen, dvs. den återstående skillnaden från min inmatning som går tillbaka till en annan Address som tillhör mig.


Det mest intressanta att studera är uppenbarligen output 0 med OP_RETURN. Låt oss ta en närmare titt på vad den innehåller:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Kredit: https://blockstream.info/


Vi upptäcker det hexadecimala skriptet för utdata: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000**


I det här manuset kan vi bryta ner flera delar:

Bland opkoderna kan vi känna igen 0x6a som hänvisar till OP_RETURN och 0x4c som hänvisar till OP_PUSHDATA1. Byten som följer efter denna opkod anger storleken på den nyttolast som följer. Den indikerar 0x50, vilket är 80 byte.


Därefter kommer betalningskoden med den krypterade nyttolasten.


Här är min betalkod som används i den här transaktionen:


I bas 58: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU**


I bas 16 (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db**


Om vi jämför min betalkod med OP_RETURN kan vi se att HRP (i brunt) och checksumman (i rosa) inte överförs. Detta är normalt, eftersom denna information är avsedd för människor.

Därefter kan vi känna igen (i Green) versionen (0x01), bitfältet (0x00) och den offentliga nyckelpariteten (0x02). Och i slutet av betalningskoden, de tomma bytena i svart (0x00) som tillåter utfyllnad för att nå totalt 80 byte. Alla dessa metadata överförs i klartext (okrypterade).

Slutligen kan vi konstatera att x-koordinaten för den offentliga nyckeln (i blått) och kedjekoden (i rött) har krypterats. Detta utgör betalningskodens nyttolast.


### Mottagande av meddelandetransaktionen.


Nu när Alice har skickat meddelandetransaktionen till Bob ska vi se hur han tolkar den.


Som en påminnelse måste Bob kunna få tillgång till Alices betalkod. Utan denna information kommer han, som vi kommer att se i nästa avsnitt, inte att kunna härleda de nyckelpar som skapats av Alice, och därför kommer han inte att kunna komma åt sina bitcoins som mottagits med BIP47. För tillfället är Alices betalningskods nyttolast krypterad. Låt oss tillsammans se hur Bob dekrypterar den.


1- Bob övervakar transaktioner som skapar utdata med sitt meddelande Address.

2- När en transaktion har en utdata till sin avisering Address, analyserar Bob den för att se om den innehåller en OP_RETURN-utdata som överensstämmer med BIP47-standarden.

3- Om den första byten i OP_RETURN:s nyttolast är 0x01 börjar Bob söka efter en möjlig delad hemlighet med ECDH:



- Bob väljer den publika nyckeln i transaktionsinmatningen. Det vill säga Alices publika nyckel med namnet "A" med: **A = a-G**
- Bob väljer den privata nyckeln "b" som är kopplad till hans personliga meddelande Address: **b**
- Bob beräknar den hemliga punkten "S" (ECDH:s delade hemlighet) på den elliptiska kurvan genom att lägga till och dubbla punkter och använder sin privata nyckel "b" till Alices offentliga nyckel "A": **S = b-A**
- Bob bestämmer den förblindningsfaktor "f" som gör det möjligt för honom att dekryptera Alices betalningskods nyttolast. På samma sätt som Alice beräknade den tidigare, kommer Bob att hitta "f" genom att tillämpa HMAC-SHA512 på (x) x-koordinatvärdet för den hemliga punkten "S", och på (o) UTXO som förbrukats som input i denna meddelandetransaktion: **f = HMAC-SHA512(o, x)**


4- Bob tolkar uppgifterna i OP_RETURN i meddelandetransaktionen som en betalningskod. Han dekrypterar helt enkelt nyttolasten för denna potentiella betalningskod med hjälp av förblindningsfaktorn "f".



- Bob delar upp förblindningsfaktorn "f" i två delar: de första 32 bytena av "f" blir "f1" och de sista 32 bytena blir "f2".
- Bob dekrypterar det krypterade x-koordinatvärdet (x') för Alices publika nyckel för betalningskoden:


**x = x' XOR f1**



- Bob dekrypterar det krypterade kedjekodsvärdet (c') för Alices betalningskod:


**c = c' XOR f2**


5- Bob kontrollerar om värdet på Alices publika nyckel för betalningskoden ingår i secp256k1-gruppen. Om så är fallet tolkar han det som en giltig betalkod. Annars ignorerar han transaktionen.


Nu när Bob känner till Alices betalningskod kan hon skicka upp till 2^32 betalningar till honom utan att någonsin behöva utföra en sådan här aviseringstransaktion igen.


Varför fungerar det här? Hur kan Bob fastställa samma förblindningsfaktor som Alice och dekryptera hennes betalkod? Låt oss undersöka ECDH-processen mer i detalj baserat på vad vi just beskrev.


För det första har vi att göra med symmetrisk kryptering. Detta innebär att krypteringsnyckeln och dekrypteringsnyckeln har samma värde. I det här fallet är nyckeln i meddelandetransaktionen förblindningsfaktorn (f = f1 || f2). Alice och Bob måste få fram samma värde för f utan att överföra det direkt, eftersom en angripare skulle kunna avlyssna det och dekryptera den hemliga informationen.


Denna blindningsfaktor erhålls genom att tillämpa HMAC-SHA512 på två värden: x-koordinaten för en hemlig punkt och den förbrukade UTXO i transaktionsinmatningen. Bob måste därför ha dessa två uppgifter för att kunna dekryptera Alices betalningskods payload.


För inmatningen UTXO kan Bob helt enkelt hämta den genom att observera meddelandetransaktionen. För den hemliga punkten måste Bob använda ECDH.


Som vi såg i avsnittet om Diffie-Hellman kan Alice och Bob hitta en specifik och hemlig punkt på den elliptiska kurvan genom att utbyta sina respektive publika nycklar och i hemlighet använda sina privata nycklar på den andres publika nyckel. Anmälningstransaktionen bygger på denna mekanism:


Bobs nyckelpar: **B = b-G**


Alices nyckelpar: **A = a-G**


För en hemlig punkt S (x,y): **S = a-B = a-b-G = b-a-G = b-A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Nu när Bob känner till Alices betalningskod kan han upptäcka hennes BIP47-betalningar och härleda de privata nycklar som blockerar de mottagna bitcoins.

![Bob interprets Alice's notification transaction](assets/20.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Om vi jämför det här diagrammet med det jag beskrev för dig tidigare:



- "Wallet Pub-Key" på Alice sida motsvarar: A.
- "Child Priv-Key 0" på Bobs sida motsvarar: b.
- "Notification Shared Secret" motsvarar: f.
- "Masked Payment Code" motsvarar Alices maskerade betalkod, dvs. med den krypterade betalningen: x' och c'.
- "Anmälningstransaktion" är den transaktion som innehåller OP_RETURN.


Låt mig sammanfatta de steg som vi just har sett tillsammans för att ta emot och tolka en aviseringstransaktion:



- Bob övervakar transaktionsutgångar till sitt meddelande Address.
- När han upptäcker en sådan hämtar han den information som finns i OP_RETURN.
- Bob väljer den inmatade publika nyckeln och beräknar en hemlig punkt med hjälp av ECDH.
- Han använder denna hemliga punkt för att beräkna en HMAC, som är den förblindande faktorn.
- Han använder denna förblindande faktor för att dekryptera Alices betalningskod som finns i OP_RETURN.


### Betalningstransaktionen BIP47.


Låt oss nu studera betalningsprocessen med BIP47. För att påminna dig om det aktuella läget i situationen:



- Alice känner till Bobs betalkod, som hon helt enkelt har hämtat från hans webbplats.



- Bob känner till Alices betalkod tack vare meddelandetransaktionen.



- Alice kommer att göra en första betalning till Bob. Hon kan göra många fler på samma sätt.


Innan jag förklarar den här processen för dig tycker jag att det är viktigt att påminna dig om vilka index vi för närvarande arbetar med:


Vi beskriver härledningsvägen för en betalkod på följande sätt: m/47'/0'/0'/.


På nästa djup fördelas indexen enligt följande:



- Det första normala (icke-härdade) barnparet används för generate meddelandet Address som vi diskuterade i föregående avsnitt: m/47'/0'/0'/0/.



- Normala nyckelpar används inom ECDH för generate BIP47 betalningsmottagande adresser, som vi kommer att se i detta avsnitt: m/47'/0'/0'/ från 0 till 2.147.483.647/.



- Härdade barnnyckelpar är efemära betalningskoder: m/47'/0'/0'/ från 0' till 2.147.483.647'/.

Varje gång Alice vill skicka en betalning till Bob får hon en ny unik blank Address, återigen tack vare ECDH-protokollet:


- Alice väljer den första privata nyckeln som härrör från hennes personliga återanvändbara betalningskod: **a**



- Alice väljer den första oanvända publika nyckeln som härrör från Bobs betalkod. Denna publika nyckel kallar vi "B". Den är kopplad till den privata nyckeln "b" som bara Bob känner till.

**B = b-G**



- Alice beräknar en hemlig punkt "S" på den elliptiska kurvan genom att lägga till och fördubbla punkter och använder sin privata nyckel "a" till Bobs offentliga nyckel "B":

**S = a-B**



- Från denna hemliga punkt kommer Alice att beräkna den delade hemligheten "s" (gemener). För att göra detta väljer hon x-koordinaten för den hemliga punkten "S", kallad "Sx", och skickar detta värde till SHA256 Hash-funktionen.

**s = SHA256(Sx)**


Lita inte på någon. Verifiera! Om du vill förstå de grundläggande principerna för en Hash-funktion hittar du det du behöver i den här artikeln. Och om du inte litar på NIST (du har rätt), och du vill kunna förstå i detalj hur SHA256 fungerar, förklarar jag allt i den här artikeln på franska.



- Alice använder denna delade hemlighet "s" för att beräkna en Bitcoin-betalning som tar emot Address. Först kontrollerar hon att "s" ligger inom ordningen för secp256k1-kurvan. Om så inte är fallet ökar hon indexet för Bobs offentliga nyckel för att härleda en annan delad hemlighet.



- För det andra beräknar hon en publik nyckel "K0" genom att lägga till punkterna "B" och "s-G" på den elliptiska kurvan. Med andra ord lägger Alice till den offentliga nyckel som härrör från Bobs betalningskod "B" med en annan punkt som beräknas på den elliptiska kurvan genom att lägga till och dubbla punkter med den delade hemligheten "s" från generatorpunkten för secp256k1-kurvan "G". Denna nya punkt representerar en publik nyckel och vi kallar den "K0":

**K0 = B + s-G**



- Med denna publika nyckel "K0" kan Alice härleda en tom mottagande Address på ett standardiserat sätt (t.ex. SegWit V0 i Bech32).


När Alice har denna mottagande Address "K0" som tillhör Bob, kan hon konstruera en standard Bitcoin-transaktion genom att välja en UTXO som tillhör henne på en annan gren av hennes HD Wallet, och spendera den till Bobs "K0" Address.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki

Om vi jämför det här diagrammet med det jag beskrev för dig tidigare:



- "Child Priv-Key" på Alice sida motsvarar: a.
- "Child Pub-Key 0" på Bobs sida motsvarar: B.
- "Betalningshemlighet 0" motsvarar: s.
- "Payment Pub-Key 0" motsvarar: K0.


Låt mig sammanfatta de steg vi just gick igenom tillsammans för att skicka en BIP47-betalning:



- Alice väljer den först härledda privata nyckeln för barnet från sin personliga betalkod.
- Hon beräknar en hemlig punkt på den elliptiska kurvan med hjälp av ECDH från den första oanvända offentliga nyckeln för barn som härleds från Bobs betalningskod.
- Hon använder denna hemliga punkt för att beräkna en delad hemlighet med SHA256.
- Hon använder den delade hemligheten för att beräkna en ny hemlig punkt på den elliptiska kurvan.
- Hon lägger till denna nya hemliga punkt till Bobs offentliga nyckel.
- Hon får en ny efemär publik nyckel för vilken endast Bob har den tillhörande privata nyckeln.
- Alice kan skicka en vanlig transaktion till Bob med den härledda efemära mottagningen Address.


Om hon vill göra en andra betalning upprepar hon ovanstående steg, men väljer den andra härledda offentliga nyckeln från Bobs betalningskod. Det vill säga nästa oanvända nyckel. Hon kommer då att ha en andra mottagande Address som tillhör Bob, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Hon kan fortsätta på detta sätt och härleda upp till 2^32 tomma adresser som tillhör Bob.


Från ett externt perspektiv, genom att observera Bitcoin Blockchain, är det teoretiskt omöjligt att skilja en BIP47-betalning från en vanlig betalning. Här är ett exempel på en BIP47-betalningstransaktion på Testnet:


https://blockstream.info/Testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Det ser ut som en vanlig transaktion med en inbetalning av pengar, en utbetalning av 210 000 Sats och växel.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Kredit: https://blockstream.info/


### Mottagande av BIP47-betalningen och härledning av den privata nyckeln.


Alice har just gjort sin första betalning till en blank BIP47 Address som ägs av Bob. Låt oss nu se hur Bob tar emot denna betalning. Vi ska också se varför Alice inte har tillgång till den privata nyckeln till den Address som hon just genererade, och hur Bob hämtar denna nyckel för att spendera de bitcoins han just har fått.


Så snart Bob tar emot aviseringstransaktionen från Alice, härleder han BIP47:s publika nyckel "K0" redan innan hon skickar någon betalning till den. Han observerar därför alla betalningar till den associerade Address. Faktum är att han omedelbart härleder flera adresser som han kommer att observera (K0, K1, K2, K3...). Så här härleder han denna publika nyckel "K0":



- Bob väljer den första privata nyckeln för barn som härrör från hans betalkod. Den här privata nyckeln kallas "b". Den är associerad med den publika nyckeln "B" som Alice använde i föregående steg: **b**



- Bob väljer Alices första härledda offentliga nyckel från hennes betalningskod. Den här nyckeln kallas "A". Den är associerad med den privata nyckeln "a" som Alice använde i sina beräkningar och som endast Alice känner till. Bob kan utföra denna process eftersom han känner till Alices betalningskod som överfördes till honom i samband med meddelandetransaktionen.

**A = a-G**



- Bob beräknar den hemliga punkten "S" genom att lägga till och fördubbla punkter på den elliptiska kurvan och använder sin privata nyckel "b" till Alices offentliga nyckel "A". Här använder vi ECDH, som garanterar att denna punkt "S" kommer att vara densamma för både Bob och Alice.

**S = b-A**



- Precis som Alice gjorde isolerar Bob x-koordinaten för denna punkt "S". Vi har döpt detta värde till "Sx". Han skickar detta värde genom SHA256-funktionen för att hitta den delade hemligheten "s" (gemener).

**s = SHA256(Sx)**



- På samma sätt som Alice beräknar Bob punkten "s-G" på den elliptiska kurvan. Sedan lägger han till denna hemliga punkt till sin publika nyckel "B". Han får då en ny punkt på ellipskurvan som han tolkar som en publik nyckel "K0":

**K0 = B + s-G**


När Bob har denna publika nyckel "K0" kan han härleda den tillhörande privata nyckeln för att spendera sina bitcoins. Han är den enda som kan generate detta nummer.



- Bob lägger till sin härledda privata nyckel "b" från sin personliga betalkod. Han är den enda som kan få fram värdet på "b". Sedan lägger han till "b" till den delade hemligheten "s" för att få k0, den privata nyckeln för K0: **k0 = b + s**



- Tack vare grupplagen för den elliptiska kurvan får Bob exakt den privata nyckel som motsvarar den publika nyckel som Alice använder. Så vi har: **K0 = k0-G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Om vi jämför det här diagrammet med det jag beskrev för dig tidigare:



- "Child Priv-Key 0" på Bobs sida motsvarar: b.



- "Child Pub-Key 0" på Alice sida motsvarar: A.



- "Betalningshemlighet 0" motsvarar: s.



- "Payment Pub-Key 0" motsvarar: K0.



- "Payment Priv-Key 0" motsvarar: k0.


Låt mig sammanfatta de steg som vi just har sett tillsammans för att ta emot en BIP47-betalning och beräkna motsvarande privata nyckel:



- Bob väljer den första härledda privata nyckeln för barn från sin personliga betalkod.



- Han beräknar en hemlig punkt på den elliptiska kurvan med hjälp av ECDH från den först härledda offentliga nyckeln för barn från Alices kedjekod.



- Han använder denna hemliga punkt för att beräkna en delad hemlighet med SHA256.



- Han använder denna delade hemlighet för att beräkna en ny hemlig punkt på den elliptiska kurvan.



- Han lägger till denna nya hemliga punkt till sin personliga offentliga nyckel.



- Han får en ny efemär publik nyckel, till vilken Alice skickar sin första betalning.



- Bob beräknar den privata nyckeln som är associerad med denna efemära publika nyckel genom att lägga till sin härledda privata nyckel för barn från sin betalningskod och den delade hemligheten.


Eftersom Alice inte kan få tag på "b", Bobs privata nyckel, kan hon inte heller bestämma k0, den privata nyckel som är kopplad till Bobs BIP47 som tar emot Address.


Schematiskt kan vi beskriva beräkningen av den delade hemligheten "S" på följande sätt:


![Calculation of the shared secret with ECDHE](assets/25.webp)


När den delade hemligheten har hittats med ECDH beräknar Alice och Bob BIP47-betalningens publika nyckel "K0", och Bob beräknar också den tillhörande privata nyckeln "k0":


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### Återbetalning av BIP47-betalningen.


Eftersom Bob känner till Alices återanvändbara betalkod har han redan all information som behövs för att skicka en återbetalning till henne. Han behöver inte kontakta Alice för att be om någon information. Han kommer helt enkelt att meddela henne med en aviseringstransaktion, särskilt så att hon kan återställa sina BIP47-adresser med sin seed, och sedan kan han också skicka henne upp till 2^32 betalningar.

Bob kan sedan återbetala Alice på samma sätt som hon skickade betalningar till honom. Rollerna är ombytta:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Du känner nu till alla detaljer i denna fantastiska lösning som BIP47 representerar.


## Härledda användningar av PayNym.


Genomförandet av denna BIP47 på Samourai Wallet har resulterat i PayNyms, identifierare som beräknas utifrån användarnas betalkoder. Idag går deras användbarhet långt utöver användningen av BIP47.


Samourai-teamet håller gradvis på att utveckla ett helt ekosystem av verktyg och tjänster som baseras på användarens PayNym. Bland dessa finns uppenbarligen alla utgiftsverktyg som gör det möjligt att optimera användarens integritet genom att lägga till entropi till en transaktion och därmed lägga till trovärdig deniabilitet.


Den kombinerade användningen av Soroban, det krypterade kommunikationsnätverket baserat på Tor, och PayNyms har i hög grad optimerat användarupplevelsen vid skapandet av samarbetstransaktioner, samtidigt som en god säkerhetsnivå upprätthålls. Det är således enkelt att genomföra Stowaway (PayJoin) och StonewallX2 transaktioner utan att manuellt genomföra de många utbyten av osignerade transaktioner som krävs för att skapa en sådan samarbetstransaktion.


Till skillnad från användningen av BIP47 räcker det med att koppla PayNyms för att använda dessa verktyg, eftersom dessa samarbetstransaktioner inte kräver någon aviseringstransaktion. Det finns inget behov av att ansluta dem.


Om du vill lära dig mer om samarbetstransaktioner, och mer allmänt om alla utgiftsverktyg i Samourai Wallet, kan du läsa avsnittet "Utgiftsverktyg" i den här artikeln. Du hittar en teknisk förklaring och en detaljerad handledning för varje verktyg.


Utöver dessa samarbeten har det nyligen uppmärksammats att Samourai-teamet arbetar med ett autentiseringsprotokoll kopplat till PayNym: Auth47. Detta verktyg är redan implementerat och tillåter till exempel autentisering med en PayNym på en webbplats som accepterar denna metod. I framtiden tror jag att Auth47, utöver denna möjlighet till autentisering på webben, kommer att vara en del av ett större projekt kring ekosystemet BIP47/PayNym/Samourai. Kanske kommer detta protokoll att användas för att ytterligare optimera användarupplevelsen av Samourai Wallet, särskilt när det gäller användningen av utgiftsverktyg. Det återstår att se...


## Min personliga åsikt om BIP47.


Uppenbarligen är den största nackdelen med BIP47 anmälningstransaktionen. Det leder till att användaren måste spendera avgifter för sin Mining, vilket kan vara irriterande för vissa. Men argumentet om "spam" på Bitcoin Blockchain är absolut oacceptabelt. Alla som betalar avgifterna för sin transaktion måste kunna registrera den på Ledger, oavsett dess syfte. Att hävda något annat är att förespråka censur.


Det är möjligt att det i framtiden kommer att finnas andra billigare lösningar för att förmedla avsändarens betalkod till mottagaren och för mottagaren att lagra den på ett säkert sätt. Men än så länge är aviseringstransaktionen den lösning som innebär minst kompromisser.


Denna nackdel är dock försumbar med tanke på alla fördelar med BIP47. Bland alla befintliga förslag för att lösa problemet med återanvändning av Address framstår det för mig som den bästa lösningen.


Som förklarats tidigare kommer majoriteten av återanvändningen av Address från utbyten. BIP47 är den enda rimliga lösningen som faktiskt löser detta problem vid dess källa. Alla förslag som syftar till att minska antalet återanvändningar av Address bör fokusera på denna aspekt och anpassa lösningen till den huvudsakliga källan till problemet.


När det gäller användbarhet är betalningsförfarandet för BIP47 enkelt, trots att det är ganska komplext i sitt inre. Återanvändbara betalningskoder kan därför lätt tas i bruk, även av ovana användare.


När det gäller integritet är BIP47 mycket intressant. Som jag förklarade i avsnittet om aviseringstransaktionen avslöjar betalningskoden inte någon information om de härledda efemära adresserna. Den bryter därför informationsflödet mellan Bitcoin-transaktionen och mottagarens identifierare, till skillnad från den traditionella användningen av en mottagande Address.


Och framför allt, PayNym-implementeringen av BIP47 fungerar! Den har varit tillgänglig på Samourai Wallet sedan 2016 och på Sparrow Wallet sedan början av det här året. Det är inte ett vetenskapligt projekt, utan en lösning som testades igår och som fungerar fullt ut idag.


Förhoppningsvis kommer dessa återanvändbara betalkoder i framtiden att antas av aktörer i ekosystemet, implementeras i Wallet-programvaran och användas av Bitcoinanvändare.


Alla verkligt positiva lösningar för användarnas integritet måste debatteras, drivas på och försvaras, så att Bitcoin inte blir en lekplats för CA:er och ett övervakningsverktyg för regeringar.

Han tänkte på hur han hade blivit förföljd och förolämpad överallt, och nu hörde han alla säga att han var den vackraste av alla dessa vackra fåglar! Och till och med fläderträdet böjde sina grenar mot honom, och solen spred ett så varmt och välvilligt ljus! Då svällde hans fjädrar, hans smala hals rätades ut och han utbrast av hela sitt hjärta: "Hur kunde jag drömma om så mycket lycka när jag bara var en ful liten ankunge."


## För att gå vidare:



- Förstå och använda CoinJoin på Bitcoin.



- Förståelse för härledningsvägarna för en Bitcoin Wallet.



- Installera och använda din RoninDojo Bitcoin-nod.


### Externa resurser och erkännanden:


Tack till LaurentMT och Théo Pantamis för de många begrepp som de förklarat för mig och som jag använt i denna artikel. Jag hoppas att jag har förmedlat dem på ett korrekt sätt.


Tack till Fanis Michalakis för korrekturläsning av denna text och hans expertråd.



- https://bitcoiner.guide/paynym/
- https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols