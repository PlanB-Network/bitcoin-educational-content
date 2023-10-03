---
name: BIP47 - PayNym

description: Hur PayNym fungerar
---

# BIP47, den fula ankungen.

> "Den är för stor," sa de alla, och kalkonen som föddes med sporrar och trodde sig vara kejsare svällde upp som ett skepp med alla segel i vinden och gick rakt på honom i stor ilska och röd ända upp till ögonen. Den stackars ankungen visste inte om den skulle stanna eller gå: den var mycket ledsen över att bli förlöjligad av alla ankorna i gården.

![BIP47, den fula ankungen illustration](assets/1.png)

En av de största farorna med Bitcoin-protokollet är återanvändning av adresser. Nätverkets transparens och distribution gör denna praxis farlig för användarens integritet. För att undvika problem relaterade till detta rekommenderas det att använda en ny tom mottagningsadress för varje ny inkommande betalning till en plånbok, vilket kan vara komplicerat i vissa fall.

Denna kompromiss är lika gammal som White Paper. Redan i sin bok som publicerades i slutet av 2008 varnade Satoshi oss för denna risk:

> "Som en extra brandvägg kan ett nytt nyckelpar användas för varje transaktion för att hålla dem obundna till en gemensam ägare."

Det finns många lösningar för att ta emot flera betalningar utan att återanvända adresser. Var och en av dem har sina kompromisser och nackdelar. Bland alla dessa lösningar finns BIP47, ett förslag utvecklat av Justus Ranvier och publicerat 2015 som möjliggör generering av återanvändbara betalningskoder. Målet är att kunna göra flera transaktioner till samma person utan att återanvända en adress.

Från början möttes detta förslag med förakt från en del av gemenskapen, och det har aldrig lagts till i Bitcoin Core. Vissa program har ändå valt att implementera det på egen hand. Således har Samourai Wallet utvecklat sin egen implementation av BIP47: PayNym. Idag är denna implementation naturligtvis tillgänglig på Samourai Wallet för smartphones, men också på Sparrow Wallet för datorer.

Med tiden har Samourai programmerat nya funktioner som är direkt kopplade till PayNym. Nu finns det en hel ekosystem av verktyg som optimerar användarens integritet baserat på PayNym och BIP47.
I den här artikeln kommer du att upptäcka principen för BIP47 och PayNym, mekanismerna för dessa protokoll och de praktiska tillämpningar som följer med dem. Jag kommer bara att behandla den första versionen av BIP47, den som för närvarande används för PayNym, men version 2, 3 och 4 fungerar i stort sett på samma sätt.

> Den enda stora skillnaden finns i notifikationstransaktionen. Version 1 använder en vanlig adress med OP_RETURN för notifikationen, version 2 använder en multisig-skript (bloom-multisig) med OP_RETURN och version 3 och 4 använder helt enkelt en multisig-skript (cfilter-multisig). Mekanismerna som diskuteras i denna artikel, särskilt de studerade kryptografiska metoderna, är därför tillämpliga på alla fyra versioner. För närvarande använder PayNym-implementeringen i Samourai Wallet och Sparrow den första versionen av BIP47.

## Innehållsförteckning:

1- Problem med återanvändning av adresser.

2- Principer för BIP47 och PayNym.

3- Guider: Användning av PayNym.

- Bygga en BIP47-transaktion med Samourai Wallet.

- Bygga en BIP47-transaktion med Sparrow Wallet.

4- Detaljer om BIP47.

- Återanvändbart betalkod.
- Kryptografisk metod: Diffie-Hellman-nyckelutbyte baserat på elliptiska kurvor (ECDH).

- Notifikationstransaktion.
- Konstruktion av notifikationstransaktion.
- Mottagande av notifikationstransaktion.
- BIP47-betalningstransaktion.
- Mottagande av BIP47-betalning och härledning av privat nyckel.
- Återbetalning av BIP47-betalning.

5- Avledade användningar av PayNym.

6- Min personliga åsikt om BIP47.

## Problem med återanvändning av adresser.

En mottagningsadress används för att ta emot bitcoins. Den genereras från en offentlig nyckel genom att hasha den och tillämpa ett specifikt format på den. På så sätt skapar den en ny utgiftsvillkor för en mynt för att ändra ägaren.

> För att lära dig mer om generering av en mottagningsadress rekommenderar jag att du läser den sista delen av den här artikeln: Bitcoin-plånboken - utdrag [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Dessutom har du säkert redan hört från en kunnig bitcoinanvändare att mottagningsadresser är engångsadresser och att du därför måste generera en ny adress för varje ny inkommande betalning till din plånbok. Okej, men varför?
I grund och botten innebär återanvändning av adresser inte direkt någon risk för dina pengar. Användningen av kryptografi på elliptiska kurvor gör det möjligt att bevisa för nätverket att du faktiskt äger en privat nyckel utan att avslöja den. Du kan därför låsa flera olika UTXO på samma adress och spendera dem vid olika tillfällen. Om du inte avslöjar den privata nyckeln som är kopplad till denna adress kan ingen komma åt dina pengar. Problemet med återanvändning av adresser handlar snarare om integriteten.

Som nämnts i inledningen gör transparensen och distributionen av Bitcoin-nätverket att vilken användare som helst, förutsatt att de har tillgång till en nod, kan observera transaktionerna i betalningssystemet. På så sätt kan de se de olika saldona på adresserna. Satoshi Nakamoto nämnde då möjligheten att generera nya nyckelpar och därmed nya adresser för varje ny inkommande betalning till en plånbok. Målet skulle vara att ha en extra brandvägg i händelse av en koppling mellan användarens identitet och ett av deras nyckelpar.

Idag, med närvaron av blockkedjeanalysföretag och utvecklingen av KYC, är användningen av tomma adresser inte längre en extra brandvägg, utan ett krav för alla som bryr sig minsta lilla om sin integritet.

Sökandet efter sekretess är inte en bekvämlighet eller en fantasi för maximalistiska bitcoin-användare. Det är en specifik parameter som direkt påverkar din personliga säkerhet och säkerheten för dina pengar. För att förstå detta, här är ett mycket konkret exempel:

- Bob köper bitcoin genom DCA (Dollars Cost Average), vilket innebär att han köper en liten mängd bitcoin med regelbundna intervall för att jämna ut sitt inköpspris. Bob skickar konsekvent de köpta medlen till samma mottagaradress. Han köper 0,01 bitcoin varje vecka och skickar dem till samma adress. Efter två år har Bob samlat en hel bitcoin på denna adress.

- Bagaren på hörnet accepterar betalningar i bitcoin. Glädjande över att kunna spendera bitcoin går Bob och köper sitt bröd i satoshis. För att betala använder han de blockerade medlen med sin adress. Nu vet bagaren att han äger en bitcoin. Denna betydande summa kan väcka avundsjuka och Bob kan potentiellt utsättas för en fysisk attack i framtiden.

Återanvändning av adresser gör det därför möjligt för en observatör att göra en obestridlig koppling mellan dina olika UTXO och ibland mellan din identitet och hela din plånbok.
Det är därför de flesta Bitcoin-plånboksprogram automatiskt genererar en ny mottagningsadress när du klickar på "Ta emot" -knappen. För den vanliga användaren är det inte en stor nackdel att använda nya adresser. Men för en onlinebutik, en börs eller en donationskampanj kan detta hinder snabbt bli ohållbart.
Det finns många lösningar för dessa organisationer. Var och en har sina fördelar och nackdelar, men hittills, som vi kommer att se senare, skiljer sig BIP47 verkligen från de andra.

Detta problem med återanvändning av adresser är inte försumbart inom Bitcoin. Som du kan se på diagrammet nedan från [oxt.me](http://oxt.me/), är den globala återanvändningsgraden för Bitcoin-adresser för närvarande 52%:
Diagram från OXT.me som visar utvecklingen av den globala återanvändningsgraden för adresser på Bitcoin-nätverket.

![image](assets/2.png)

Kredit: https://oxt.me/charts

Majoriteten av denna återanvändning kommer från börser som av effektivitetsskäl återanvänder samma adress många gånger. Hittills skulle BIP47 vara den bästa lösningen för att stoppa detta fenomen hos börser. Det skulle minska den globala återanvändningsgraden av adresser utan att orsaka för mycket friktion för dessa enheter.

Denna globala åtgärd över hela nätverket är särskilt sammanhängande i detta fall. Återanvändning av adresser är inte bara ett problem för personen som utför denna praxis, utan också för alla som gör transaktioner med den. Förlusten av integritet på Bitcoin fungerar som ett virus och sprider sig från användare till användare. Att studera en global åtgärd för alla transaktioner i nätverket gör att vi kan förstå omfattningen av detta fenomen.

## Principer för BIP47 och PayNym.

BIP47 syftar till att erbjuda ett enkelt sätt att ta emot många betalningar utan att återanvända adresser. Dess funktion är baserad på användningen av en återanvändbar betalkod.

På så sätt kan flera avsändare skicka flera betalningar till en enda återanvändbar betalkod från en annan användare, utan att mottagaren behöver skicka en ny tom adress för varje ny transaktion.

En användare kan sedan fritt kommunicera sin betalkod (på sociala nätverk, på sin webbplats...) utan risk för förlust av integritet, till skillnad från en vanlig mottagningsadress eller en offentlig nyckel.
För att genomföra en transaktion måste båda användarna ha en Bitcoin-plånbok med en implementation av BIP47, som PayNym på Samourai Wallet eller Sparrow Wallet. Genom att associera betalningskoderna för de två användarna kan en hemlig kanal etableras mellan dem. För att inrätta denna kanal måste avsändaren genomföra en transaktion på Bitcoin-nätverket: en notifieringstransaktion (jag kommer att förklara mer om det senare).
Genom att associera betalningskoderna för de två användarna genereras delade hemligheter som i sig kan generera ett stort antal unika Bitcoin-mottagaradresser (exakt 2^32). Således skickas betalningen med BIP47 inte till betalningskoden, utan till helt vanliga adresser som härleds från användarnas betalningskoder.

Betalningskoden fungerar därför som en virtuell identifierare, härledd från plånbokens frö. I HD-plånbokens härledningsstruktur finns betalningskoden på nivå 3, på plånbokens kontonivå.

![image](assets/3.png)

Dess härledningsändamål anges som 47' (0x8000002F) med hänvisning till BIP47. Ett exempel på en härledningsväg för en återanvändbar betalningskod är:

> m/47'/0'/0'/

För att du ska kunna föreställa dig hur en betalningskod ser ut, här är min:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Den kan också kodas som en QR-kod för att underlätta kommunikationen:

![image](assets/4.png)

Vad gäller PayNym Bots, de robotar som syns på Twitter, är de bara visuella representationer av din betalningskod, skapade av Samourai Wallet. De skapas med hjälp av en hashfunktion, vilket gör dem nästan unika. Här är min med sin identifierare:

> +throbbingpond8B1

![image](assets/5.png)

Dessa Bots har ingen verklig teknisk användning. Istället underlättar de interaktionen mellan användarna genom att skapa en virtuell visuell identitet.

För användaren är processen för en BIP47-betalning med PayNym-implementeringen extremt enkel. Låt oss säga att Alice vill skicka betalningar till Bob:

1. Bob sprider sin QR-kod, eller direkt sin återanvändbara betalningskod. Han kan placera den på sin webbplats, på olika offentliga sociala medier eller skicka den till Alice via annat kommunikationsmedel.
2. Alice öppnar sin Samourai- eller Sparrow-programvara och skannar eller klistrar in betalningskoden från Bob.
3. Alice kopplar sin PayNym med Bobs ("Follow" på engelska). Denna operation utförs utanför blockkedjan och är helt gratis.

4. Alice kopplar sin PayNym med Bobs ("Connect" på engelska). Denna operation utförs "on chain". Alice måste betala gruvavgifter för transaktionen samt en fast avgift på 15 000 sats för tjänsten på Samourai. Tjänstavgifterna är gratis på Sparrow. Denna steg kallas för anmälningstransaktion.

5. När anmälningstransaktionen har bekräftats kan Alice skapa en BIP47-betalningstransaktion till Bob. Hennes plånbok kommer automatiskt att generera en ny tom mottagningsadress där endast Bob har den privata nyckeln.

Att utföra anmälningstransaktionen, det vill säga att koppla sin PayNym, är ett obligatoriskt förstasteg för att genomföra BIP47-betalningar. Å andra sidan, när detta har gjorts, kan avsändaren genomföra flera betalningar till mottagaren (exakt 2^32), utan att behöva göra en ny anmälningstransaktion.

Ni har sett att det finns två olika operationer för att koppla samman PayNym: att koppla och att ansluta. Anslutningsoperationen ("connecter") motsvarar BIP47-anmälningstransaktionen som helt enkelt är en Bitcoin-transaktion med viss information som överförs genom en OP_RETURN-utgång. På så sätt hjälper den till att etablera en krypterad kommunikation mellan de två användarna för att generera de delade hemligheterna som behövs för att skapa nya tomma mottagningsadresser.

Å andra sidan, kopplingsoperationen ("follow" eller "relier") möjliggör en länkning på Soroban, en krypterad kommunikationsprotokoll baserat på Tor, speciellt utvecklat av Samourai-teamen.

För att sammanfatta:

- Att koppla samman två PayNym ("follow") är helt gratis. Det hjälper till att etablera krypterad "off chain"-kommunikation, särskilt för att använda Samourais samarbetsverktyg för transaktioner (Stowaway eller StonewallX2). Denna operation är specifik för PayNym. Den beskrivs inte i BIP47.

- Att ansluta två PayNym är betalningspliktigt. Det innebär att genomföra anmälningstransaktionen för att starta anslutningen. Kostnaden består av eventuella serviceavgifter, gruvavgifter för transaktionen och 546 sats som skickas till mottagarens anmälningsadress för att informera om öppningen av tunneln. Denna operation är kopplad till BIP47. När den har genomförts kan avsändaren genomföra flera BIP47-betalningar till mottagaren.

För att kunna ansluta två PayNym måste de redan vara kopplade.

## Guider: Användning av PayNym.

Nu när vi har sett teorin, låt oss titta på praktiken tillsammans. Tanken med de följande handledningarna är att koppla min PayNym på min Sparrow-plånbok till min PayNym på min Samourai-plånbok. Den första handledningen visar hur man gör en transaktion med hjälp av återanvändbar betalkod från Samourai till Sparrow, och den andra handledningen beskriver samma mekanism från Sparrow till Samourai.

> Jag utförde dessa handledningar på Testnet. Det är inte riktiga bitcoins.

### Bygga en BIP47-transaktion med Samourai Wallet.

För att börja behöver du självklart Samourai Wallet-appen. Du kan ladda ner den direkt från Google Play Store eller med APK-filen som finns tillgänglig på Samourais officiella webbplats.

När plånboken är initialiserad, om du inte redan har gjort det, begär din PayNym genom att klicka på plus-tecknet (+) längst ned till höger och sedan på "PayNym".

Det första steget för att göra en BIP47-betalning är att hämta mottagarens återanvändbara betalkod. Sedan kan vi ansluta till den och sedan ansluta oss:

![video](assets/6.mp4)

När notifieringstransaktionen har bekräftats kan jag skicka flera betalningar till mottagaren. Varje transaktion görs automatiskt med en ny tom adress där mottagaren har nycklarna. Mottagaren behöver inte göra något, allt beräknas från min sida.

Så här gör du en BIP47-transaktion på Samourai Wallet:

![video](assets/7.mp4)

### Bygga en BIP47-transaktion med Sparrow Wallet.

På samma sätt som för Samourai måste du självklart ha Sparrow-programvaran. Den är tillgänglig på datorn. Du kan ladda ner den från deras [officiella webbplats](https://sparrowwallet.com/).

Se till att kontrollera utvecklarens signatur och integriteten hos den nedladdade programvaran innan du installerar den på din enhet.

Skapa en plånbok och begär din PayNym genom att klicka på "Show PayNym" från "Tool"-menyn i den övre menyraden:

![image](assets/8.png)

Därefter måste du koppla och ansluta din PayNym till mottagarens PayNym. För att göra detta, ange deras återanvändbara betalkod i "Find Contact"-fönstret, följ den och genomför sedan notifieringstransaktionen genom att klicka på "Link Contact":

![image](assets/9.png)

När notifieringstransaktionen har bekräftats kan vi skicka betalningar till den återanvändbara betalkoden. Här är stegen att följa:

![video](assets/10.mp4)

Nu när vi har studerat den praktiska sidan av BIP47 PayNym-implementeringen, låt oss tillsammans se hur dessa mekanismer fungerar och vilka kryptografiska metoder som används.

## BIP47:s mekanismer.

För att studera mekanismerna för BIP47 är det viktigt att förstå strukturen för hierarkisk deterministisk (HD) plånbok, mekanismerna för härledning av barnnyckelpar och principerna för elliptisk kurvkryptografi. Lyckligtvis kan du hitta all nödvändig information för att förstå denna del på min blogg:

- [Förstå härledningsvägar för en Bitcoin-plånbok](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Bitcoin-plånboken - utdrag från e-boken Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Återanvändbar betalkod.

Som förklarat i den andra delen av denna artikel finns den återanvändbara betalkoden på nivå tre i HD-plånboken. Den kan i viss mån liknas vid en xpub, både i placering, struktur och funktion.

Här är de olika delarna som utgör en 80-byte betalkod:

- Byte 0: Versionen. Om den första versionen av BIP47 används kommer detta byte att vara 0x01.

- Byte 1: Bitfältet. Detta utrymme är reserverat för att ge ytterligare information vid specifik användning. Om man bara använder PayNym kommer detta byte att vara 0x00.

- Byte 2: Pariteten för y. Detta byte indikerar 0x02 eller 0x03 beroende på pariteten (jämnt eller udda antal) av värdet för den ordnade y-koordinaten för vår publika nyckel. För mer information om denna praxis, läs steg 1 i avsnittet "adresshärledning" i denna artikel.

- Från byte 3 till byte 34: Värdet för x. Dessa byte indikerar x-koordinaten för vår publika nyckel. Konkatineringen av x och pariteten för y ger oss vår komprimerade publika nyckel.

- Från byte 35 till byte 66: Kedjekoden. Detta utrymme är reserverat för kedjekoden som är associerad med den tidigare nämnda publika nyckeln.

- Från byte 67 till byte 79: Fyllning. Detta utrymme är reserverat för eventuella framtida utvecklingar. För version 1 fyller vi det helt enkelt med nollor för att fylla upp till 80 byte, vilket är storleken på data för en OP_RETURN-utgång.

Här är den hexadecimala representationen av min återanvändbara betalkod, som presenterades i föregående del, med färger som motsvarar ovanstående byte:
Därefter måste vi också lägga till prefixet "P" byte för att snabbt identifiera att det är en betalkod. Detta byte är 0x47.

Slutligen beräknar vi checksumman för denna betalkod med HASH256, det vill säga en dubbel hashning med SHA256-funktionen. Vi tar de fyra första byten av denna hashsumma och lägger till dem i slutet (i rosa).

Betalkoden är klar, nu återstår bara att konvertera den till Base 58:

PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Som ni kan se liknar denna konstruktion starkt strukturen hos en utökad offentlig nyckel av typen "xpub".

Under denna process för att generera vår betalkod har vi använt en komprimerad offentlig nyckel och en kedjekod. Båda dessa element är resultatet av en deterministisk och hierarkisk härledning från plånbokens frö, genom att följa följande härledningsväg: m/47'/0'/0'/
Konkret, för att få den publika nyckeln och kedjekoden för återanvändbar betalningskod, kommer vi att beräkna huvudprivatnyckeln från fröet och sedan härleda ett dotterpar med index 47 + 2^31 (förstärkt härledning). Sedan härleder vi två gånger dotterpar med index 2^31 (förstärkt härledning).

> Om du vill veta mer om härledning av dotternyckelpar inom en deterministisk hierarkisk Bitcoin-plånbok, rekommenderar jag att du tar CRYPTO301.

### Kryptografisk metod: Diffie-Hellman-nyckelutbyte på elliptiska kurvor (ECDH).

Den kryptografiska metoden som används som grund för BIP47 är ECDH (Elliptic-Curve Diffie-Hellman = Diffie-Hellman-nyckelutbyte på elliptiska kurvor). Denna protokoll är en variant av det klassiska Diffie-Hellman-nyckelutbytet.

Diffie-Hellman, i sin första version, är ett nyckelavtalprotokoll som presenterades 1976 och som gör att två personer, med hjälp av två par (publika nycklar och privata nycklar), kan bestämma en delad hemlighet genom att utbyta information över en osäker kommunikationskanal.

![image](assets/11.png)

Denna delade hemlighet (den röda nyckeln) kan sedan användas för att utföra andra uppgifter. Typiskt sett kan denna delade hemlighet användas för att kryptera och dekryptera kommunikation över ett osäkert nätverk:

![image](assets/12.png)

För att lyckas med detta utbyte använder Diffie-Hellman modulär aritmetik för att beräkna den gemensamma hemligheten. Här är en förenklad förklaring av hur det fungerar:

- Alice och Bob bestämmer en gemensam färg, här gul. Denna färg är känd för alla. Det är en offentlig information.

- Alice väljer en hemlig färg, här röd. Hon blandar de två färgerna och får orange.

- Bob väljer en hemlig färg, här blågrön. Han blandar de två färgerna och får ljusblå.

- Alice och Bob kan utbyta de erhållna färgerna: orange och ljusblå. Denna utbyte kan göras över ett osäkert nätverk och observeras av angripare.

- Alice blandar den ljusblå färgen som hon fått från Bob med sin hemliga färg (röd). Hon får brun.

- Bob blandar den orange färgen som han fått från Alice med sin hemliga färg (blågrön). Han får samma bruna färg.

![image](assets/13.png)

> Kredit: Ursprunglig idé: A.J. Han Vinck, Vektorversion: Flugaal, Översättning: Dereckson, Public domain, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg

I denna förklaring representerar den bruna färgen den hemlighet som delas mellan Alice och Bob. Man måste föreställa sig att det i verkligheten är omöjligt för en angripare att separera de orange och ljusblå färgerna för att hitta Alice eller Bobs hemliga färger.

Nu ska vi studera dess faktiska funktion. Vid första anblicken kan Diffie-Hellman verka svårt att förstå. I verkligheten är principen nästan barnsligt enkel. Innan vi går in på detaljerna vill jag snabbt påminna er om två matematiska begrepp som vi kommer att behöva (och som för övrigt också används i många andra krypteringsmetoder).

1. Ett primtal är ett naturligt tal som bara har två delare: 1 och sig självt. Till exempel är siffran 7 ett primtal, eftersom det bara kan delas med 1 och 7 (sig självt). Å andra sidan är siffran 8 inte ett primtal, eftersom det kan delas med 1, 2, 4 och 8. Det har alltså inte bara två delare, utan fyra hela och positiva delare.

2. "Modulo" (noteras "mod" eller "%") är en matematisk operation som mellan två heltal ger resten av den euklidiska divisionen av det första talet med det andra talet. Till exempel är 16 mod 5 lika med 1.

Diffie-Hellman-nyckelutbytet mellan Alice och Bob fungerar på följande sätt:

- Alice och Bob bestämmer två gemensamma tal: p och g. p är ett primtal. Ju större detta tal p är, desto säkrare blir Diffie-Hellman. g är en primitiv rot av p. Dessa två tal kan kommuniceras klartext över ett osäkert nätverk, de motsvarar den gula färgen i förklaringen ovan. Det är bara viktigt att Alice och Bob har exakt samma värden för p och g.

- När parametrarna har valts bestämmer Alice och Bob var för sig ett hemligt slumpmässigt tal. Det slumpmässiga talet som Alice får kallas a (motsvarar den röda färgen) och det slumpmässiga talet som Bob får kallas b (motsvarar den mörkblå färgen). Dessa två tal måste förbli hemliga.

- Istället för att utbyta dessa tal a och b kommer varje part att beräkna A (versal) och B (versal) enligt följande:

> A är lika med g upphöjt till a modulo p:
> A = g^a % p

> B är lika med g upphöjt till b modulo p:
> B = g^b % p

- Dessa tal A (motsvarar den orangea färgen) och B (motsvarar den ljusblåa färgen) kommer att utbytas mellan de två parterna. Utbytet kan ske klartext över ett osäkert nätverk.

- Alice, som nu känner till B, kommer att beräkna värdet av z enligt följande:

> z är lika med B upphöjt till a modulo p:
> z = B^a % p

- Som påminnelse, B = g^b % p. Således har vi:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > Enligt reglerna för beräkningar med exponenter:
  >
  > (x^n)^m = x^nm
  >
  > Således har vi:
  >
  > z = g^ba % p

- Bob, som nu känner till A, kommer också att beräkna värdet av z enligt följande:

> z är lika med A upphöjt till b modulo p:
>
> z = A^b % p
>
> Således har vi:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Tack vare särskilt distributiviteten hos modulo-operatorn hittar Alice och Bob exakt samma värde för z. Detta tal representerar deras gemensamma hemlighet, det vill säga motsvarigheten till brun färg i den tidigare förklaringen. De kan använda denna gemensamma hemlighet för att kryptera kommunikation mellan dem på ett osäkert nätverk.

![Diagram över Diffie-Hellman-protokollets tekniska funktion](assets/14.png)

En angripare som har tillgång till p, g, A och B kommer inte att kunna beräkna a, b eller z. Att göra denna beräkning skulle innebära att man inverterar exponentiering. Detta är omöjligt att göra på annat sätt än att prova alla möjligheter en efter en, eftersom vi arbetar med ett ändligt fält. Det skulle vara att beräkna diskret logaritm, det vill säga den omvända operationen till exponentiering i en ändlig cyklisk grupp.

Så länge vi väljer tillräckligt stora värden för a, b och p är Diffie-Hellman säkert. Typiskt sett skulle det vara omöjligt att testa alla möjligheter för a och b med parametrar på 2 048 bitar (ett tal med 600 siffror i decimalform). Hittills betraktas algoritmen som säker med sådana stora tal.

Det är just på denna nivå som det främsta nackdelen med Diffie-Hellman-protokollet ligger. För att vara säkert måste algoritmen använda stora tal. Som ett resultat föredrar vi idag att använda ECDH-algoritmen, en variant av Diffie-Hellman som använder en algebraisk kurva, och i detta fall en elliptisk kurva. Detta gör att vi kan arbeta med mycket mindre tal samtidigt som vi behåller en jämförbar säkerhet och därmed minska de resurser som krävs för beräkning och lagring.

Den allmänna principen för algoritmen förblir densamma. Men istället för att använda ett slumpmässigt tal a och ett tal A som beräknas från a med modulär exponentiering, kommer vi att använda ett par nycklar som etableras på en elliptisk kurva. Istället för att förlita oss på distributiviteten hos modulo-operatorn kommer vi här att använda grupplagen för elliptiska kurvor, och mer specifikt dess associativitet.
Om du inte har någon kunskap om hur privata och publika nycklar fungerar på en elliptisk kurva, kommer jag att förklara grunderna i denna metod i de sex första delarna av denna artikel.

För att sammanfatta grovt är en privat nyckel ett slumpmässigt tal mellan 1 och n-1 (där n är ordningen på kurvan), och en offentlig nyckel är en unik punkt på kurvan som bestäms genom att addera och dubbla punkter från den genererande punkten med hjälp av den privata nyckeln enligt följande:

> K = k·G

Där K är den offentliga nyckeln, k är den privata nyckeln och G är den genererande punkten.

En av egenskaperna hos detta nyckelpar är att det är mycket enkelt att bestämma K om man känner till k och G, men det är idag omöjligt att bestämma k om man känner till K och G. Det är en enkelriktad funktion.

Med andra ord kan man enkelt beräkna den offentliga nyckeln om man känner till den privata nyckeln, men det är omöjligt att beräkna den privata nyckeln om man känner till den offentliga nyckeln. Denna säkerhet är återigen baserad på den diskreta logaritmens omöjlighet att beräkna.

Vi kommer att använda denna egenskap för att anpassa vår Diffie-Hellman-algoritm. Således är principen för ECDH följande:

- Alice och Bob kommer överens om en kryptografiskt säker elliptisk kurva och dess parametrar. Denna information är offentlig.

- Alice genererar ett slumpmässigt tal ka som kommer att vara hennes privata nyckel. Denna privata nyckel måste förbli hemlig. Hon bestämmer sin offentliga nyckel Ka genom att addera och dubbla punkter på den valda elliptiska kurvan.

> Ka = ka·G

- Bob genererar också ett slumpmässigt tal som kommer att vara hans privata nyckel kb. Och han beräknar den associerade offentliga nyckeln Kb.

> Kb = kb·G

- Alice och Bob utbyter sina offentliga nycklar Ka och Kb på ett osäkert offentligt nätverk.

- Alice beräknar en punkt (x,y) på kurvan genom att tillämpa sin privata nyckel ka från Bobs offentliga nyckel Kb.

> (x,y) = ka·Kb

- Bob beräknar en punkt (x,y) på kurvan genom att tillämpa sin privata nyckel kb från Alices offentliga nyckel Ka.

> (x,y) = kb·Ka

- Alice och Bob får samma punkt på den elliptiska kurvan. Den delade hemligheten kommer att vara x-koordinaten för denna punkt.

De får verkligen samma delade hemlighet eftersom:

> (x,y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

En eventuell angripare som observerar det osäkra offentliga nätverket kan endast få de offentliga nycklarna för var och en och parametrarna för den valda kurvan. Som tidigare förklarat tillåter dessa två ensamma inte att bestämma de privata nycklarna, och därför kan inte angriparen få tillgång till hemligheten.
ECDH är en algoritm som möjliggör en nyckelutbyte. Den används ofta tillsammans med andra kryptografiska metoder för att definiera en protokoll. Till exempel används ECDH i hjärtat av TLS (Transport Layer Security), en krypterings- och autentiseringsprotokoll som används för internettransportlagret. TLS använder ECDHE för nyckelutbyte, en variant av ECDH där nycklarna är temporära för att ge kontinuerlig sekretess. Förutom ECDHE använder TLS också en autentiseringsalgoritm som ECDSA, en krypteringsalgoritm som AES och en hashfunktion som SHA256.
TLS definierar bland annat "s" i "https", samt den lilla låset du ser i din webbläsare uppe till vänster, vilket garanterar att kommunikationen är krypterad. Så du använder ECDH när du läser den här artikeln, och du använder det förmodligen dagligen utan att märka det.

### Meddelandetransaktionen.

Som vi upptäckte i föregående avsnitt är ECDH en variant av Diffie-Hellman-utbytet som innefattar nyckelpar som etableras på en elliptisk kurva. Detta är bra eftersom vi har massor av nyckelpar som följer denna standard i våra Bitcoin-plånböcker!

Idén är att använda nyckelparen från de hierarkiska deterministiska Bitcoin-plånböckerna hos båda parterna för att etablera delade och temporära hemligheter mellan dem. Inom BIP47 används därför ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

ECDHE används först i BIP47 för att överföra betalningskoden från avsändaren till mottagaren. Detta är den berömda meddelandetransaktionen. För att BIP47 ska kunna användas måste båda parterna (avsändaren som skickar betalningar och mottagaren som tar emot betalningar) vara medvetna om den andra partens betalningskod. Detta är nödvändigt för att härleda de temporära publika nycklarna och därmed de dedikerade mottagningsadresserna.

Innan denna utbyte är avsändaren logiskt sett redan medveten om mottagarens betalningskod eftersom den kan ha hämtat den off-chain, till exempel från deras webbplats eller deras sociala nätverk. Å andra sidan är mottagaren inte nödvändigtvis medveten om avsändarens betalningskod. Den måste överföras till mottagaren, annars kan de inte härleda sina temporära nycklar och därmed kommer de inte att kunna veta var deras bitcoins är eller låsa upp sina medel. Det skulle kunna överföras off-chain med ett annat kommunikationssystem, men det skulle vara ett problem om plånboken återställs från fröet.
Faktiskt, som jag redan har nämnt, är BIP47-adresser inte härledda från mottagarens frö (annars skulle det vara bättre att använda en av deras xpub direkt), utan de är resultatet av en beräkning som involverar både betalningskoderna: mottagarens och avsändarens. Därför, om mottagaren förlorar sin plånbok och försöker återställa den från sitt frö, måste de nödvändigtvis ha alla betalningskoder från personer som har skickat bitcoins till dem via BIP47.

Det skulle vara möjligt att använda BIP47 utan denna notifieringstransaktion, men varje användare skulle behöva säkerhetskopiera betalningskoderna för sina kontakter. Denna situation skulle vara svår att hantera tills vi hittar ett enkelt och robust sätt att skapa, lagra och uppdatera dessa säkerhetskopior. Notifieringstransaktionen är därför nästan obligatorisk i den nuvarande situationen.

Förutom att fungera som en säkerhetskopia för betalningskoderna, som namnet antyder, spelar denna transaktion också rollen som en notifiering till mottagaren. Den signalerar till deras klient att en tunnel just har öppnats.

Innan jag förklarar den tekniska funktionen hos notifieringstransaktionen mer detaljerat, vill jag prata lite om sekretessmodellen. BIP47-modellen motiverar vissa försiktighetsåtgärder vid konstruktionen av denna initiala transaktion.

Själva betalningskoden utgör inte direkt en risk för sekretessförlust. Till skillnad från den vanliga Bitcoin-modellen som möjliggör att informationsflödet mellan användarens identitet och transaktioner bryts, särskilt genom att hålla de publika nycklarna anonyma, kan betalningskoden direkt associeras med en identitet. Det är naturligtvis inte ett krav, men denna koppling är inte farlig.

Faktum är att betalningskoden inte direkt härleder de adresser som används för att ta emot BIP47-betalningar. Istället erhålls adresserna genom att tillämpa ECDHE mellan barnnycklar av betalningskoderna från båda parter.

En ensam betalningskod utgör därför inte en direkt risk för sekretessförlust eftersom bara notifieringsadressen härleds från den. Viss information kan utläsas, men normalt sett kommer man inte att kunna veta med vilka du gör transaktioner.

Det är därför viktigt att upprätthålla en strikt separation mellan användarnas betalningskoder. I detta syfte är den inledande kommunikationssteget för koden en kritisk tidpunkt för betalningens sekretess, och ändå nödvändig för protokollets korrekta funktion. Om en av de två betalningskoderna kan hämtas offentligt (till exempel på en webbplats), bör den andra koden, det vill säga avsändarens kod, inte associeras med den första.

Till exempel, låt oss säga att jag vill göra en donation med BIP47 till en fredlig proteströrelse i Kanada:

- Denna organisation har publicerat sin betalkod direkt på sin webbplats eller på sina sociala medier.
- Denna kod är således associerad med rörelsen.

- Jag hämtar denna betalkod.

- Innan jag kan skicka en transaktion till dem måste jag se till att de känner till min personliga betalkod som också är associerad med min identitet eftersom jag använder den för att ta emot transaktioner från mina sociala medier.

Hur kan jag överföra den till dem? Om jag skickar den med en vanlig kommunikationsmetod kan informationen läcka ut och jag kan riskera att bli stämplad som en person som stöder fredliga rörelser.

Transaktionsmeddelandet är visserligen inte den enda lösningen för att hemlighålla avsändarens betalkod, men det fyller för närvarande perfekt den rollen genom att tillämpa flera säkerhetslager.

I schemat nedan representerar de röda linjerna ögonblicket då informationsflödet måste brytas, och de svarta pilarna representerar de oåterkalleliga kopplingarna som kan göras av en extern observatör:

![Schema för sekretessmodell för återanvändbar betalkod](assets/15.png)

I verkligheten är det ofta svårt att helt bryta informationsflödet mellan nyckelparet och användaren i den klassiska sekretessmodellen för Bitcoin, särskilt när man genomför transaktioner på distans. Till exempel, i fallet med en donationskampanj, kommer mottagaren att vara tvungen att avslöja en adress eller en offentlig nyckel på sin webbplats eller sina sociala medier. Rätt användning av BIP47, det vill säga med transaktionsmeddelandet, löser detta genom ECDHE och krypteringslagret som vi kommer att studera.

Självklart observeras den klassiska sekretessmodellen för Bitcoin fortfarande på nivån av de tillfälliga offentliga nycklarna som härleds från sammankopplingen av de två betalkoderna. De två modellerna är ömsesidigt beroende. Jag vill bara belysa här att, till skillnad från den vanliga användningen av en offentlig nyckel för att ta emot bitcoins, kan betalkoden associeras med en identitet eftersom informationen "Bob gör en transaktion med Alice" bryts vid en annan tidpunkt. Betalkoden används för att generera betalningsadresser, men genom att bara observera blockkedjan är det omöjligt att associera en BIP47-betalningstransaktion med de betalkoder som används för att genomföra den.

### Konstruktion av transaktionsmeddelandet.

Nu ska vi se hur detta transaktionsmeddelande fungerar. Låt oss anta att Alice vill skicka pengar till Bob med BIP47. I mitt exempel agerar Alice som avsändare och Bob som mottagare. Den senare har publicerat sin betalkod på sin webbplats. Alice känner redan till Bob's betalkod.

1. Alice beräknar en delad hemlighet med ECDH:

- Hon väljer ett par nycklar från sin HD-plånbok som finns på en annan gren än hennes betalkod. Observera att detta par inte får vara lätt associerat med Alices notifieringsadress eller Alices identitet (se föregående del).
- Alice väljer den privata nyckeln från detta par. Vi kallar den "a" (gemener).

> a

- Alice hämtar den publika nyckeln som är associerad med Bob's notifieringsadress. Denna nyckel är den första härledda dottern från Bob's betalkod (index 0). Vi kallar denna publika nyckel "B" (versaler). Den privata nyckeln som är associerad med denna publika nyckel kallas "b" (gemener). "B" bestäms genom att addera och dubbla punkter på den elliptiska kurvan från "G" (generatorpunkten) med "b" (den privata nyckeln).

> B = b·G

- Alice beräknar en hemlig punkt "S" (versaler) på den elliptiska kurvan genom att addera och dubbla punkter med sin privata nyckel "a" från Bob's publika nyckel "B".

> S = a·B

- Alice beräknar den blinda faktorn "f" som kommer att användas för att kryptera hennes betalkod. För detta kommer hon att generera ett pseudoslumpmässigt tal med HMAC-SHA512-funktionen. Som andra indata till denna funktion använder hon ett värde som bara Bob kommer att kunna hitta: (x), vilket är x-koordinaten för den tidigare beräknade hemliga punkten. Den första indata är (o), som är UTXO:en som används som indata för denna transaktion (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice konverterar sin personliga betalkod till bas 2 (binär).

3. Hon använder denna blinda faktor som nyckel för att utföra symmetrisk kryptering på sin betalkods payload. Den krypteringsalgoritm som används är helt enkelt XOR. Operationen som utförs liknar Vernam-chiffer, även känd som "One-Time Pad":

- Alice delar först upp sin blinda faktor i två delar: de första 32 oktetterna kallas "f1" och de sista 32 oktetterna kallas "f2". Vi har alltså:

> f = f1 || f2

- Alice beräknar kryptot (x') för x-koordinaten för sin betalkods publika nyckel och kryptot (c') för sin kedjekod (c) separat. "f1" och "f2" fungerar som krypteringsnycklar. Operationen som används är XOR.

> x' = x XOR f1
>
> c>' = c XOR f2

- Alice ersätter de verkliga värdena för den publika nyckelns abscissa (x) och kedjekoden (c) i sin betalningskod med de krypterade värdena (x') och (c').

Innan vi fortsätter med den tekniska beskrivningen av denna meddelandetransaktion, låt oss ta en stund och titta närmare på denna XOR-operation. XOR är en bitvis logisk operator baserad på Booles algebra. Med två bitoperander returnerar den 1 om bitarna på samma plats är olika och 0 om bitarna på samma plats är lika. Här är sanningstabellen för XOR baserat på värdena för operanderna D och E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Till exempel:

> 0110 XOR 1110 = 1000

Eller:

> 010011 XOR 110110 = 100101

Med ECDH är användningen av XOR som krypteringslager särskilt sammanhängande. För det första, tack vare denna operator, är krypteringen symmetrisk. Detta gör att mottagaren kan dekryptera betalningskoden med samma nyckel som användes för krypteringen. Krypterings- och dekrypteringsnyckeln beräknas från den delade hemligheten med hjälp av ECDH.

Denna symmetri möjliggörs genom XOR-operatörens egenskaper för kommutativitet och associativitet:

- Andra egenskaper:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Kommutativitet:
  D ⊕ E = E ⊕ D

- Associativitet:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Symmetri:
  Om: D ⊕ E = L
  Då: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
  Därefter liknar denna krypteringsmetod mycket Vernam-chiffret (One-Time Pad), den enda kända krypteringsalgoritmen hittills som har absolut säkerhet. För att Vernam-chiffret ska ha denna egenskap måste krypteringsnyckeln vara helt slumpmässig, vara lika stor som meddelandet och användas endast en gång. I krypteringsmetoden som används här för BIP47 är nyckeln lika stor som meddelandet, blindfaktorn har exakt samma storlek som sammanslagningen av den publika nyckelns abscissa med betalningskodens kedjekod. Denna krypteringsnyckel används bara en gång. Däremot är denna nyckel inte en perfekt slump eftersom den är en HMAC. Den är snarare pseudoslumpmässig. Så det är inte ett Vernam-chiffer, men metoden liknar det.

Låt oss återgå till konstruktionen av notifieringstransaktionen:

4. Alice har nu sin betalningskod med krypterad payload. Hon kommer att konstruera och sprida en transaktion som involverar hennes publika nyckel "A" som input, en output till Bob's notifieringsadress och en OP_RETURN-utgång som består av hennes betalningskod med den krypterade payloaden. Denna transaktion är notifieringstransaktionen.

OP_RETURN är en Opcode, det vill säga ett skript, som markerar en Bitcoin-transaktionsutgång som ogiltig. Idag används den för att sprida eller förankra information på Bitcoin-blockkedjan. Upp till 80 byte data kan lagras där och registreras på kedjan, och därmed synlig för alla andra användare.

Som vi såg i föregående avsnitt används Diffie-Hellman för att generera en delad hemlighet mellan två användare som kommunicerar över ett osäkert nätverk och potentiellt observeras av angripare. I BIP47 används ECDH för att kunna kommunicera på Bitcoin-nätverket, som av naturen är ett transparent kommunikationsnätverk och observeras av många angripare. Den delade hemligheten som beräknas genom Diffie-Hellman-nyckelutbytet på elliptiska kurvan används sedan för att kryptera den hemliga informationen som ska överföras: avsändarens (Alice) betalningskod.

Här är en diagram från BIP47 som illustrerar det vi just beskrivit:

![Diagram Alice skickar sin dolda betalningskod till Bob's notifieringsadress](assets/16.png)

Kredit: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Om vi matchar detta diagram med det jag beskrev tidigare:

- "Wallet Priv-Key" på Alice-sidan motsvarar: a.

- "Child Pub-Key 0" på Bob-sidan motsvarar: B.
- "Notification Shared Secret" motsvarar: f.
- "Masked Payment Code" motsvarar krypterad betalkod: x' och c'.

- "Notification Transaction" är transaktionen som innehåller OP_RETURN.

Jag sammanfattar de steg vi precis har gått igenom för att genomföra en notifikationstransaktion:

- Alice hämtar betalkoden och Bob's notifikationsadress.

- Alice väljer en UTXO som tillhör henne i hennes HD-plånbok med motsvarande nyckelpar.

- Hon beräknar en hemlig punkt på den elliptiska kurvan med hjälp av ECDH.

- Hon använder denna hemliga punkt för att beräkna en HMAC som är den bländningsfaktorn.

- Hon använder denna bländningsfaktor för att kryptera sin personliga betalkods nyttolast.

- Hon använder en OP_RETURN-transaktionsutgång för att överföra den krypterade betalkoden till Bob.

För att förstå mer detaljerat hur det fungerar, och särskilt användningen av OP_RETURN, låt oss titta på en verklig notifikationstransaktion tillsammans. Jag har genomfört en sådan transaktion på Testnet som du kan hitta genom att klicka här:

https://mempool.space/fr/testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

TXID:

> 0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

![Notifikationstransaktion BIP47](assets/17.png)

Kredit: https://blockstream.info/

Genom att observera denna transaktion kan vi redan se att den har en enda input och 4 outputs:

- Den första outputen är OP_RETURN som innehåller min krypterade betalkod.

- Den andra outputen på 546 sats pekar mot min mottagares notifikationsadress.

- Den tredje outputen på 15 000 sats representerar serviceavgifterna, eftersom jag använde Samourai Wallet för att bygga denna transaktion.

- Den fjärde outputen på två miljoner sats representerar växel, det vill säga återstående differens från min input som går till en annan adress som tillhör mig.

Det mest intressanta att studera är naturligtvis output 0 som använder OP_RETURN. Låt oss titta närmare på vad den innehåller:

![OP_RETURN-utgång i notifikationstransaktion BIP47](assets/18.png)

Kredit: https://blockstream.info/

Där upptäcker vi outputens skript i hexadecimalt format:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

I detta skript kan vi analysera flera delar:
6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Opcodes:
6a4c

En byte som indikerar storleken på payloaden (80 byte):
50

Metadata för min klartextbetalningskod:
010002

X-koordinaten för min klartextbetalnings offentliga nyckel:
b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164

Krypterad kedjekod för min klartextbetalning:
927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d8

Fyllnad för att nå 80 byte:
00000000000000000000000000

Bland opcodes kan vi känna igen 0x6a som betecknar OP_RETURN och 0x4c som betecknar OP_PUSHDATA1. Byte efter den senare opcoden indikerar storleken på den efterföljande payloaden. Den indikerar 0x50, vilket motsvarar 80 byte.

Därefter kommer betalningskoden med den krypterade payloaden.

Här är min klartextbetalningskod som används i denna transaktion:

I bas 58:
PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU

I bas 16 (HEX):
4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Om vi jämför min klartextbetalningskod med OP_RETURN kan vi se att HRP (i brunt) och checksumman (i rosa) inte överförs. Det är normalt, denna information är avsedd för människor.
Sedan kan man känna igen (i grönt) versionen (0x01), bitfältet (0x00) och nyckelns offentliga paritet (0x02). Och i slutet av betalkoden finns de tomma byteen i svart (0x00) som används för att fylla ut och nå totalt 80 byte. Alla dessa metadata överförs i klartext (okrypterade).
Slutligen kan man observera att den offentliga nyckelns abscissa (i blått) och kedjekoden (i rött) har krypterats. Detta utgör betalkodens nyttolast.

### Mottagande av transaktionsmeddelandet.

Nu när Alice har skickat transaktionsmeddelandet till Bob, låt oss se hur han tolkar det.

För att påminna, måste Bob kunna komma åt Alice betalkod. Utan denna information, som vi kommer att se i nästa del, kommer han inte att kunna härleda de nyckelpar som skapats av Alice, och därför kommer han inte att kunna komma åt sina bitcoins som mottagits med BIP47. För tillfället är Alice betalkods nyttolast krypterad. Låt oss tillsammans se hur Bob dekrypterar den.

1. Bob övervakar transaktioner som skapar utgångar med hans notifieringsadress.

2. När en transaktion har en utgång på hans notifieringsadress, analyserar Bob den för att se om den innehåller en OP_RETURN-utgång som följer BIP47-standarden.

3. Om det första bytet i OP_RETURN-nyttolasten är 0x01, börjar Bob leta efter en eventuell delad hemlighet med ECDH:

- Bob väljer den offentliga nyckeln i transaktionens ingång. Det vill säga Alice offentliga nyckel som kallas "A" med:

> A = a·G

- Bob väljer den privata nyckeln "b" som är associerad med hans personliga notifieringsadress:

> b

- Bob beräknar den hemliga punkten "S" (delad hemlighet ECDH) på den elliptiska kurvan genom att addera och dubbla punkter genom att tillämpa sin privata nyckel "b" på Alice offentliga nyckel "A":

> S = b·A

- Bob bestämmer den bländningsfaktorn "f" som kommer att användas för att dekryptera Alice betalkods nyttolast. På samma sätt som Alice tidigare beräknade den, kommer Bob att hitta "f" genom att tillämpa HMAC-SHA512 på (x) värdet på den hemliga punktens abscissa "S" och på (o) UTXO som konsumerades som ingång i denna notifieringstransaktion:

> f = HMAC-SHA512(o, x)

4. Bob tolkar OP_RETURN-data i notifieringstransaktionen som en betalkod. Han kommer helt enkelt att dekryptera nyttolasten i denna potentiella betalkod med hjälp av bländningsfaktorn "f":

- Bob delar upp den bländande faktorn "f" i två delar: de första 32 oktetterna av "f" kommer att vara "f1" och de sista 32 oktetterna kommer att vara "f2".
- Bob dekrypterar värdet av den krypterade x-koordinaten (x') från Alice's betalningskod:

> x = x' XOR f1

- Bob dekrypterar värdet av den krypterade kedjekoden (c') från Alice's betalningskod:

> c = c' XOR f2

5. Bob kontrollerar om värdet av Alice's betalningskods publika nyckel verkligen tillhör gruppen secp256k1. Om så är fallet tolkar han det som en giltig betalningskod. Annars ignorerar han transaktionen.

Nu när Bob känner till Alice's betalningskod kan hon skicka upp till 2^32 betalningar till honom utan att någonsin behöva göra en sådan här notifieringstransaktion igen.

Varför fungerar det här? Hur kan Bob bestämma samma bländande faktor som Alice och därmed dekryptera hennes betalningskod? Låt oss titta närmare på ECDH-handlingen i det vi just beskrivit.

För det första har vi att göra med symmetrisk kryptering. Det betyder att krypteringsnyckeln och dekrypteringsnyckeln är samma värde. Den här nyckeln i notifieringstransaktionen är den bländande faktorn (f = f1 || f2). Så Alice och Bob måste få samma värde för f, utan att direkt överföra det eftersom en angripare kan stjäla det och dekryptera den hemliga informationen.

Den här bländande faktorn erhålls genom att tillämpa HMAC-SHA512 på två värden: x-koordinaten för en hemlig punkt och den använda UTXO:n i transaktionen. Så Bob måste ha dessa två uppgifter för att dekryptera Alice's betalningskods nyttolast.

För input-UTXO:n kan Bob enkelt hämta den genom att observera notifieringstransaktionen. För den hemliga punkten måste Bob använda ECDH.

Som vi såg i avsnittet om Diffie-Hellman kan Alice och Bob genom att utbyta sina respektive publika nycklar och hemligt tillämpa sina privata nycklar på den andra personens publika nyckel hitta en specifik och hemlig punkt på den elliptiska kurvan. Notifieringstransaktionen bygger på den här mekanismen:

> Bob's nyckelpar:
>
> B = b·G
>
> Alice's nyckelpar:
>
> A = a·G
>
> För en hemlig punkt S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Schema för att generera en delad hemlighet med ECDHE](assets/19.png)
Nu när Bob känner till Alice betalningskod kommer han att kunna upptäcka hennes BIP47-betalningar och han kommer att kunna härleda de privata nycklarna som låser upp de mottagna bitcoinsen.
![Bob tolkar Alice betalningsmeddelande](assets/20.png)

Kredit: Återanvändbara betalningskoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Om vi matchar detta schema med vad jag tidigare beskrivit för er:

- "Wallet Pub-Key" på Alice sida motsvarar: A.

- "Child Priv-Key 0" på Bob sida motsvarar: b.

- "Notification Shared Secret" motsvarar: f.

- "Masked Payment Code" motsvarar Alice maskerade betalningskod, det vill säga med krypterad payload: x' och c'.

- "Notification Transaction" är transaktionen som innehåller OP_RETURN.

Jag sammanfattar de steg vi precis har gått igenom för att ta emot och tolka en notifikationstransaktion:

- Bob övervakar transaktionsutgångar till sin notifikationsadress.

- När han upptäcker en sådan hämtar han informationen som finns i OP_RETURN.

- Bob väljer den offentliga nyckeln i input och beräknar en hemlig punkt med hjälp av ECDH.

- Han använder denna hemliga punkt för att beräkna en HMAC som är den bländningsfaktorn.

- Han använder denna bländningsfaktor för att dekryptera payloaden i Alice betalningskod som finns i OP_RETURN.

### BIP47-betalningstransaktionen.

Låt oss nu titta närmare på betalningsprocessen med BIP47. För att påminna er om den nuvarande situationen:

- Alice känner till Bob betalningskod som hon enkelt hämtade från hans webbplats.

- Bob känner till Alice betalningskod tack vare notifikationstransaktionen.

- Alice kommer att göra en första betalning till Bob. Hon kan göra många fler på samma sätt.

Innan jag förklarar denna process tror jag att det är viktigt att påminna om vilka index vi för närvarande arbetar med:

Vi beskriver avledningsvägen för en betalningskod på följande sätt: m/47'/0'/0'/.

Nästa nivå fördelar indexen på följande sätt:

- Den första normala (icke förstärkta) barnparet används för att generera notifikationsadressen som vi pratade om i föregående del: m/47'/0'/0'/0/.

- De normala barnnyckelparen används inom ECDH för att generera BIP47-mottagaradresser, som vi kommer att se i den här delen: m/47'/0'/0'/ från 0 till 2 147 483 647/.

- De förstärkta barnnyckelparen är tillfälliga betalningskoder: m/47'/0'/0'/ från 0' till 2 147 483 647'/.
  Varje gång Alice vill skicka en betalning till Bob, genererar hon en ny unik tom adress med hjälp av ECDH-protokollet:

* Alice väljer den första privata nyckeln som härleds från hennes personliga återanvändbara betalkod:

> a

- Alice väljer den första oanvända publika nyckeln som härleds från Bobs betalkod. Denna publika nyckel kallas "B" och är associerad med den privata nyckeln "b" som bara Bob känner till.

> B = b·G

- Alice beräknar en hemlig punkt "S" på den elliptiska kurvan genom att addera och dubbla punkter med sin privata nyckel "a" från Bobs publika nyckel "B":

> S = a·B

- Från denna hemliga punkt beräknar Alice den delade hemligheten "s" (gemener). För att göra detta väljer hon x-koordinaten för den hemliga punkten "S", kallad "Sx", och matar in detta värde i SHA256-hashfunktionen.

> s = SHA256(Sx)

Lita inte. Verifiera! Om du vill förstå grunderna i en hashfunktion hittar du all information i den här artikeln. Och om du inte litar på NIST (du har rätt), och vill förstå SHA256-funktionens funktion i detalj, förklarar jag allt i den här artikeln på franska.

- Alice använder den delade hemligheten "s" för att beräkna en Bitcoin-mottagaradress. Först kontrollerar hon att "s" finns inom ordningen för kurvan secp256k1. Om så inte är fallet ökar hon indexet för Bobs publika nyckel för att härleda en annan delad hemlighet.

- Sedan beräknar hon en publik nyckel "K0" genom att addera punkterna "B" och "s·G" på den elliptiska kurvan. Med andra ord adderar Alice den publika nyckeln som härleds från Bobs betalkod "B" med en annan punkt som beräknas på den elliptiska kurvan genom att addera och dubbla punkter med den delade hemligheten "s" från kurvans generatorpunkt secp256k1 "G". Denna nya punkt representerar en publik nyckel och kallas "K0":

> K0 = B + s·G

- Med denna publika nyckel "K0" kan Alice generera en tom mottagaradress på standardiserat sätt (t.ex. SegWit V0 i Bech32-format).

När Alice har denna mottagaradress "K0" som tillhör Bob kan hon skapa en vanlig Bitcoin-transaktion genom att välja en UTXO som tillhör henne på en annan gren av hennes HD-plånbok och spendera till Bobs adress "K0".

![Alice skickar bitcoins med BIP47 till Bob](assets/21.png)

Kredit: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Om vi matchar denna diagram med det jag tidigare beskrev för er:

- "Child Priv-Key" på Alice-sidan motsvarar: a.

- "Child Pub-Key 0" på Bob-sidan motsvarar: B.

- "Payment Secret 0" motsvarar: s.

- "Payment Pub-Key 0" motsvarar: K0.

Jag sammanfattar de steg vi precis har gått igenom för att skicka en BIP47-betalning:

- Alice väljer den första härledda barnprivatnyckeln från sin personliga betalkod.

- Hon beräknar en hemlig punkt på elliptiska kurvan med hjälp av ECDH från den första oanvända härledda barnpubliknyckeln från Bobs betalkod.

- Hon använder denna hemliga punkt för att beräkna en delad hemlighet med SHA256.

- Hon använder denna delade hemlighet för att beräkna en ny hemlig punkt på elliptiska kurvan.

- Hon adderar denna nya hemliga punkt med Bobs publika nyckel.

- Hon får en ny tillfällig offentlig nyckel som bara Bob har den associerade privata nyckeln till.

- Alice kan skicka en vanlig transaktion till Bob med den härledda tillfälliga mottagningsadressen.

Om hon vill göra en andra betalning kommer hon att upprepa ovanstående steg förutom att hon kommer att välja den andra härledda publika nyckeln från Bobs betalkod. Det vill säga nästa oanvända nyckel. Hon kommer då ha en andra mottagningsadress som tillhör Bob "K1".

![Alice härleder tre BIP47-mottagningsadresser till Bob](assets/22.png)

Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hon kan fortsätta på detta sätt och härleda upp till 2^32 tomma adresser som tillhör Bob.

Från en extern synpunkt, genom att observera Bitcoin-blockkedjan, är det teoretiskt omöjligt att skilja en BIP47-betalning från en vanlig betalning. Här är ett exempel på en BIP47-betalningstransaktion på Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Det liknar en vanlig transaktion med en använd input, en betalningsoutput på 210 000 sats och en växel:

![Bitcoin-betalningstransaktion med BIP47](assets/23.png)

Kredit: https://blockstream.info/

### Mottagande av BIP47-betalning och härledning av privat nyckel.

Alice har precis gjort sin första betalning till en tom BIP47-adress som tillhör Bob. Nu ska vi tillsammans se hur Bob tar emot denna betalning. Vi kommer också att se varför Alice inte har tillgång till den privata nyckeln för den adress hon just har genererat, och hur Bob hittar denna nyckel för att kunna spendera de bitcoins han just har fått.
Så snart Bob tar emot betalningsmeddelandet från Alice härleder han den offentliga BIP47-nyckeln "K0" innan någon betalning har skickats till den. Han övervakar alltså alla betalningar till den associerade adressen. I själva verket härleder han till och med omedelbart flera adresser som han övervakar (K0, K1, K2, K3...). Så här härleder han den offentliga nyckeln "K0":

- Bob väljer den första härledda dotterprivatnyckeln från sin betalningskod. Denna privatnyckel kallas "b". Den är associerad med den offentliga nyckeln "B" som Alice använde i föregående steg:

> b

- Bob väljer den första offentliga nyckeln som härleds från Alice med hjälp av hennes betalningskod. Denna nyckel kallas "A". Den är associerad med den privata nyckeln "a" som Alice använde i sina beräkningar och som bara Alice känner till. Bob kan utföra denna process eftersom han har tillgång till Alice betalningskod som skickades till honom med betalningsmeddelandet.

> A = a·G

- Bob beräknar den hemliga punkten "S" genom att addera och dubbla punkter på den elliptiska kurvan, genom att tillämpa sin privata nyckel "b" på Alice offentliga nyckel "A". Här använder vi ECDH som garanterar att denna punkt "S" kommer att vara densamma för både Bob och Alice.

> S = b·A

- På samma sätt som Alice isolerar Bob abscissen för denna punkt "S". Vi har kallat detta värde "Sx". Han passerar detta värde genom SHA256-funktionen för att hitta den delade hemligheten "s" (gemener).

> s = SHA256(Sx)

- På samma sätt som Alice beräknar Bob punkten "s·G" på den elliptiska kurvan. Sedan adderar han denna hemliga punkt med sin offentliga nyckel "B". Han får då en ny punkt på den elliptiska kurvan som han tolkar som en offentlig nyckel "K0":

> K0 = B + s·G

När Bob har denna offentliga nyckel "K0" kan han härleda den associerade privata nyckeln för att kunna spendera sina bitcoins. Han är den enda som kan generera detta nummer.

- Bob adderar sin härledda dotterprivatnyckel "b" från sin personliga betalningskod. Han är den enda som kan få värdet av "b". Sedan adderar han "b" med den delade hemligheten "s" för att få k0, den privata nyckeln för K0:

> k0 = b + s
> Genom grupplagen för elliptiska kurvor får Bob exakt den privata nyckeln som motsvarar den publika nyckeln som används av Alice. Vi har alltså:
> K0 = k0·G

![Bob genererar sina BIP47-mottagningsadresser](assets/24.png)

Kredit: Återanvändbara betalkoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Om vi matchar detta schema med det jag tidigare beskrev för er:

- "Child Priv-Key 0" på Bob-sidan motsvarar: b.

- "Child Pub-Key 0" på Alice-sidan motsvarar: A.

- "Payment Secret 0" motsvarar: s.

- "Payment Pub-Key 0" motsvarar: K0.

- "Payment Priv-Key 0" motsvarar: k0.

Jag sammanfattar de steg vi precis har gått igenom för att ta emot en BIP47-betalning och beräkna den motsvarande privata nyckeln:

- Bob väljer den första härledda barnprivata nyckeln från sin personliga betalkod.

- Han beräknar en hemlig punkt på elliptiska kurvan med hjälp av ECDH från den första härledda barnpublika nyckeln från Alice kedjekod.

- Han använder denna hemliga punkt för att beräkna en delad hemlighet med SHA256.

- Han använder denna delade hemlighet för att beräkna en ny hemlig punkt på elliptiska kurvan.

- Han adderar denna nya hemliga punkt med sin personliga publika nyckel.

- Han får en ny tillfällig publik nyckel, den som Alice kommer att skicka sin första betalning till.

- Bob beräknar den privata nyckeln som är associerad med denna tillfälliga publika nyckel genom att addera sin härledda barnprivata nyckel från sin betalkod och den delade hemligheten.

Eftersom Alice inte kan få "b", Bobs privata nyckel, kan hon inte bestämma k0, den privata nyckeln som är associerad med Bobs BIP47-mottagningsadress.

Schematiskt kan vi representera beräkningen av den delade hemligheten "S" på följande sätt:

![Beräkning av delad hemlighet med ECDHE](assets/25.png)

När den delade hemligheten har hittats med ECDH, beräknar Alice och Bob BIP47-betalningspubliknyckeln "K0", och Bob beräknar också den associerade privata nyckeln "k0":

![Härledning av BIP47-mottagningsadress från den delade hemligheten](assets/26.png)

### Återbetalning av BIP47-betalningen.

Eftersom Bob känner till Alice återanvändbara betalkod har han redan all nödvändig information för att skicka henne en återbetalning. Han behöver inte kontakta Alice för att be om någon information. Han behöver bara meddela henne med en notifieringstransaktion, särskilt för att hon ska kunna återställa sina BIP47-adresser med sin frö, och sedan kan han också skicka upp till 2^32 betalningar till henne.
Bob kan då återbetala Alice på samma sätt som hon skickade betalningar till honom. Rollerna omvänds:

![Bob skickar en återbetalning till Alice med BIP47](assets/27.png)

Kredit: Återanvändbara betalningskoder för hierarkiska deterministiska plånböcker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nu känner ni till alla delar av denna fantastiska lösning som BIP47 representerar.

## Avledade användningar av PayNym.

Implementeringen av BIP47 i Samourai Wallet har resulterat i PayNym, identifierare som beräknas från användarnas betalningskoder. Idag sträcker sig deras användning långt bortom BIP47.

Samourai-teamet utvecklar gradvis en hel ekosystem av verktyg och tjänster baserade på användarens PayNym. Bland dessa finns naturligtvis alla utgiftsverktyg som optimerar användarens integritet genom att lägga till entropi i en transaktion och därmed lägga till plausible förnekelse.

Den gemensamma användningen av Soroban, det krypterade kommunikationsnätverket baserat på Tor, och PayNym har i hög grad förbättrat användarupplevelsen vid konstruktion av samarbetsprojekt, samtidigt som en god säkerhetsnivå bibehålls. På så sätt kan man enkelt göra Stowaway (PayJoin) och StonewallX2-transaktioner utan att manuellt utföra de många utbytena av osignerade transaktioner som krävs för att genomföra en sådan samarbetsaffär.

Till skillnad från användningen av BIP47, eftersom dessa samarbetsaffärer inte kräver en notifieringstransaktion, räcker det att koppla samman PayNym för att använda dessa verktyg. Det behövs ingen anslutning.

Om du vill veta mer om samarbetsaffärer och mer generellt om alla utgiftsverktyg i Samourai Wallet kan du läsa avsnittet "Utgiftsverktyg" i den här artikeln. Där hittar du en teknisk förklaring och en detaljerad handledning för varje verktyg.

Förutom dessa samarbetsaffärer har vi nyligen sett att Samourai-teamet arbetar på en autentiseringsprotokoll kopplat till PayNym: Auth47. Detta verktyg är redan implementerat och möjliggör till exempel autentisering med hjälp av en PayNym på en webbplats som accepterar denna metod. I framtiden tror jag att utöver denna möjlighet till autentisering på webben kommer Auth47 att ingå i ett större projekt kring BIP47/PayNym/Samourai-ekosystemet. Kanske kommer detta protokoll att användas för att ytterligare förbättra användarupplevelsen av Samourai Wallet, särskilt vid användning av utgiftsverktygen. Det återstår att se...

## Min personliga åsikt om BIP47.

Självklart är den främsta nackdelen med BIP47 transaktionsnotifikationen. Det innebär att användaren måste betala avgifter för att gruvdrift ska ske, vilket kan vara besvärligt för vissa. Å andra sidan är argumentet om "spam" på Bitcoin-blockkedjan helt oacceptabelt. Den som betalar avgifter för sin transaktion bör kunna registrera den i registret, oavsett syfte. Att påstå något annat är att ställa sig på censurens sida.
Det är möjligt att det i framtiden kommer att hittas andra, mindre kostsamma lösningar för att kunna kommunicera betalkoden från avsändaren till mottagaren och för att mottagaren ska kunna lagra den på ett säkert sätt. Men för tillfället är transaktionsnotifikationen den lösning som innebär minst kompromisser.

Denna nackdel är försumbar när man betraktar alla fördelar med BIP47. Bland alla befintliga förslag för att lösa problemet med återanvändning av adresser verkar det enligt mig vara den bästa lösningen.

Som tidigare förklarat kommer majoriteten av återanvändningen av adresser från utbyten. BIP47 är den enda rimliga lösningen som verkligen kan lösa detta problem vid källan. Alla förslag som syftar till att minska antalet återanvändningar av adresser bör fokusera på detta och anpassa lösningen till huvudkällan till problemet.
När det gäller användning är BIP47-betalningsproceduren enkel, även om dess mekanismer är ganska komplexa. Återanvändbara betalkoder kan därför enkelt antas, även av oerfarna användare.
När det gäller integritet är BIP47 mycket intressant. Som jag förklarade i avsnittet om transaktionsnotifikationen avslöjar betalkoden ingen information om de härledda tillfälliga adresserna. Det gör det möjligt att bryta informationsflödet mellan Bitcoin-transaktionen och mottagarens identifierare, till skillnad från användningen av en vanlig mottagningsadress.

Och framför allt fungerar PayNym-implementeringen av BIP47! Den har funnits tillgänglig på Samourai Wallet sedan 2016 och på Sparrow Wallet sedan början av året. Det är inte ett vetenskapligt projekt, utan en lösning som har testats och som fungerar fullt ut idag.
Förhoppningsvis kommer dessa återanvändbara betalkoder i framtiden att antas av aktörerna inom ekosystemet, implementeras i plånboksprogramvara och användas av bitcoin-användare.
Alla verkligt positiva lösningar för användarens integritet måste diskuteras, drivas framåt och försvaras för att Bitcoin inte ska bli CA:s lekplats och regeringarnas övervakningsverktyg.

Han tänkte på hur han hade blivit förföljd och förolämpad överallt, och nu hörde han alla säga att han var den vackraste av alla dessa vackra fåglar! Till och med fläderträdet böjde sina grenar mot honom, och solen spred en så varm och välgörande ljus! Då svällde hans fjädrar, hans långa hals reste sig, och han utropade med hela sitt hjärta: "Hur kunde jag drömma om sådan lycka när jag bara var en ful liten anka?"

## För att gå djupare:

- Förstå och använda CoinJoin på Bitcoin.

- Förstå avledningsvägar för en Bitcoin-plånbok.

- Installera och använda din Bitcoin-nod RoninDojo.

### Externa resurser och tack:

Tack till LaurentMT och Théo Pantamis för de många begreppen de förklarade för mig och som jag använde i den här artikeln. Jag hoppas att jag har kunnat återge dem korrekt.

Tack till Fanis Michalakis för granskningen av denna text och hans expertråd.

    https://bitcoiner.guide/paynym/

    https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

    https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman

    https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques

    https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).

    https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060

    https://ee.stanford.edu/~hellman/publications/24.pdf

    https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols
