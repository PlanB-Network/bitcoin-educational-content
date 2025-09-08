---
name: Elektrum

description: Full Electrum Guide, från 0 till hjälte
---

![cover](assets/cover.webp)


Nedan finner du några beskrivande källor för Electrum:



- [X] (https://twitter.com/ElectrumWallet)
- [Electrums webbplats](https://electrum.org/)
- [Electrum-dokumentation](https://electrum.readthedocs.io/)


Här är vad Rogzy tycker om denna handledning:


> Jag måste säga, när jag kom över den här guiden blev jag chockad. Grattis till Arman the Parman för detta. Det skulle ha varit skamligt att inte vara värd här och översätta det på så många språk som möjligt. Honeslty, tipsar den killen.

Den ursprungliga posten är följande:


![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)


![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)


## Varför Electrum?


Det här är en detaljerad guide om hur man använder Electrum Bitcoin Wallet, med lösningar på alla dess fällor och egenheter - något jag har utvecklat efter flera års användning och undervisning av studenter om Bitcoin-säkerhet/privacy. Electrum är inte den bästa Bitcoin Wallet för den som vill hålla allt så enkelt som möjligt och föredrar att hålla sig på nybörjarnivå. Istället är det för den person som är, eller strävar efter att vara, en "kraftfull" användare.


För den nya Bitcoiner är det utmärkt endast om det sker under överinseende av en erfaren användare som visar dem vägen. Om man lär sig att använda den på egen hand är det säkert om man tar god tid på sig och använder den i en testmiljö med endast ett litet antal Sats till en början. Den här guiden stöder den strävan, men den är också en bra referens för alla andra.


**Varning:** Den här guiden är ganska lång, så försök inte att göra alla beskrivna steg på en dag. Det är lämpligt att ha guiden till hands och göra stadiga framsteg över tiden.


** Notera: ** du kan också titta på följande Electrum full videoguide (se upp så att den inte ersätter den skriftliga handledningen, men det är en integration till den):


![video](https://youtu.be/NNZdbYd8PUQ)


## Ladda ner Electrum


Helst ska du använda en dedikerad Bitcoin-dator för dina Bitcoin-transaktioner (Min guide för detta https://armantheparman.com/mint/) _(finns även på sekretessavsnittet)_. Det är bra att öva med små belopp på en "smutsig" dator när du först lär dig (vem vet hur mycket dold skadlig kod din vanliga dator har samlat på sig genom åren - du vill inte utsätta dina Bitcoin-plånböcker för dem).


Hämta Electrum från https://electrum.org/.


Klicka på fliken Ladda ner längst upp.


Klicka på den nedladdningslänk som motsvarar din dator. Alla Linux- eller Mac-datorer kan använda Python-länken (röd cirkel). En Linux-dator med ett Intel- eller AMD-chip kan använda Appimage (Green-cirkel; detta är som en körbar fil i Windows). En Raspberry Pi-enhet har en ARM-mikroprocessor och kan bara använda Python-versionen (röd cirkel), inte Appimage, även om Pi-datorer kör Linux. Den blå cirkeln är för Windows och den svarta cirkeln är för Mac.


![image](assets/1.webp)


## Verifiering av Electrum


Syftet med att "verifiera" nedladdningen är att se till att inte en enda bit av data har manipulerats. Det hindrar dig från att använda en "hackad" skadlig version av programvaran. Det går bra att hoppa över detta förutsatt att du bara använder den nedladdade kopian för att öva, dvs. inte använder plånböcker som innehåller seriösa pengar. När du sedan är redo att använda Electrum för dina riktiga pengar bör du ta bort din kopia och börja om, den här gången verifiera din nedladdning.


För att göra detta använder vi kryptografiverktyg för offentliga/privata nycklar - gpg, som vi har skrivit en guide om här (https://armantheparman.com/gpg/). Verktyget gpg levereras med alla Linux-operativsystem. För Mac och Windows, se gpg-länken för nedladdningsinstruktioner.


Förutom att ladda ner Electrum-programvaran behöver du för säkerhets skull också den digitala SIGNATUREN för programvaran. Detta är en textsträng (det är faktiskt ett nummer som kodas med text) som utvecklaren har skapat med sin PRIVATA gpg-nyckel. Med hjälp av gpg-programmet kan vi sedan "testa" SIGNATUREN mot hans OFFENTLIGA nyckel (skapad från utvecklarens privata nyckel) som alla har tillgång till, jämfört med nedladdningsfilen.


Med andra ord, med de tre ingångarna (signatur, publik nyckel och datafil) får vi en sann eller falsk utgång för att bekräfta att filen inte har manipulerats.


För att få signaturen, klicka på länken som motsvarar den fil du laddade ner (se färgade pilar):


![image](assets/2.webp)


Om du klickar på länken kan filen automatiskt laddas ner till din nedladdningsmapp eller öppnas i webbläsaren. Om den öppnas i webbläsaren måste du spara filen. Du kan högerklicka och välja "spara som". Beroende på operativsystem eller webbläsare kan det hända att du måste högerklicka på det vita området, inte på texten.


Nedan ser du hur den nedladdade texten ser ut. Du kan se att det finns flera signaturer - dessa är signaturer av olika personer. Du kan verifiera var och en eller någon. Jag ska visa dig hur du verifierar bara utvecklarens.


![image](assets/3.webp)


Därefter måste du få ThomasV:s offentliga nyckel - han är huvudutvecklaren. Du kan få den direkt från honom, hans Keybase-konto, Github eller någon annan, från en nyckelserver eller från Electrums webbplats.


Att hämta den från Electrums webbplats är faktiskt det minst säkra sättet, för om den här webbplatsen är oärlig (just det vi kontrollerar för), varför får vi en publik nyckel från den (den publika nyckeln kan vara falsk)?


För att hålla det enkelt för nu ska jag visa dig hur du får det från webbplatsen ändå, men kom ihåg detta. Här är kopian (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) på GitHub som du kan jämföra den med.


Scrolla ner lite på sidan för att hitta länken till ThomasV:s publika nyckel (röd cirkel nedan). Klicka på den och ladda ner den, eller om den öppnar en text i en webbläsare, högerklicka för att spara.


![image](assets/4.webp)


Du har nu 3 nya filer, förmodligen alla i nedladdningsmappen. Det spelar ingen roll var de finns, men det underlättar processen om du lägger dem i samma mapp.


De tre filerna:


1. Electrum nedladdning

2. Signaturfilen (vanligtvis är det samma filnamn som Electrum-nedladdningen med ett ".asc"-tillägg)

3. ThomasV:s publika nyckel.


Öppna en terminal i Mac eller Linux, eller kommandotolken (CMD) i Windows.


Navigera till katalogen Downloads (eller var du nu placerade de tre filerna). Om du inte har en aning om vad detta innebär kan du lära dig av den här korta videon för Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) och den här för Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Kom ihåg att på Linux-datorer är katalognamn skiftlägeskänsliga.


I terminalen skriver du så här för att importera ThomasV:s publika nyckel till datorns "nyckelring" (nyckelringen är ett abstrakt begrepp - det är faktiskt bara en fil på datorn):


```bash
gpg --import ThomasV.asc
```


Kontrollera att filnamnet stämmer överens med det du har laddat ner. Lägg också märke till att det är ett dubbelt streck inte ett enkelt streck. Observera också att det finns ett mellanslag före och efter "-import". Tryck sedan på <enter>.


Filen bör importeras. Om du får ett felmeddelande ska du kontrollera att du befinner dig i den katalog där filen faktiskt finns. För att kontrollera vilken katalog du befinner dig i (på Mac eller Linux), skriv pwd. För att se vilka filer som finns i den katalog du befinner dig i (på Mac eller Linux), skriv ls. Du bör se textfilen "ThomasV.asc" listad, eventuellt bland andra filer.


Sedan kör vi kommandot för att verifiera signaturen.


```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```


Observera att det finns 4 "Elements" här, var och en åtskilda av ett mellanslag. Jag har fetmarkerat texten alternativt för att hjälpa dig att se. De fyra Elements är:


1. gpg-programmet

2. alternativet -verifiera

3. filnamnet för signaturen

4. filnamnet för programmet


Av intresse är att du ibland kan utelämna det fjärde elementet och datorn gissar vad du menar. Jag är inte säker, men jag tror att det bara fungerar om filnamnen bara skiljer sig åt genom "asc" i slutet.


Kopiera inte bara filnamnen som jag har visat här - se till att de matchar filnamnet på det som du har på ditt system.


Tryck <enter> för att köra kommandot. Du bör se en "bra signatur från ThomasV" för att indikera framgång. Det kommer att bli några fel eftersom vi inte har de publika nycklarna för de andra personernas signaturer som finns i signaturfilen (det här systemet med att kombinera signaturer i en fil kan ändras i senare versioner). Det finns också en varning längst ned som vi kan ignorera (den varnar oss för att vi inte uttryckligen har sagt till datorn att vi litar på ThomasV:s publika nyckel).


Nu har vi en verifierad kopia av Electrum som är säker att använda.


## Löpande elektrum


### Kör Electrum om du använder Python


Om du laddade ner Python-versionen ska du göra så här för att få den att fungera. Du kommer att se detta på nedladdningssidan:


![image](assets/5.webp)


För Linux är det en bra idé att först uppdatera ditt system:


```bash
sudo apt-get update
sudo apt-get upgrade
```


Kopiera den gulmarkerade texten, klistra in den i terminalen och tryck <enter>. Du kommer att bli tillfrågad om ditt lösenord, eventuellt en bekräftelse för att fortsätta, och sedan installeras dessa filer ("dependencies").


Du måste också extrahera den zippade filen till en valfri katalog. Du kan göra detta med den grafiska användaren Interface eller från kommandoraden (rosa markerat kommando) - kom ihåg att filnamnen kan skilja sig åt. (Observera att när vi verifierade nedladdningen i föregående avsnitt var det zip-filen vi verifierade, inte den extraherade katalogen)


Det finns ett alternativ att "installera" med PIP-programmet, men detta är onödigt och lägger till extra steg och installation av filer. Kör bara programmet med hjälp av terminalen för att kringgå allt detta.


Stegen (Linux) är:


1. navigera till den katalog där filerna extraheras

2. typ: ./run_electrum


På en Mac är stegen desamma, men du kan behöva installera Python3 först och använda det här kommandot för att köra:


```bash
python3 ./run_electrum
```


När Electrum är igång kommer terminalfönstret att förbli öppet. Om du stänger det kommer det att avsluta Electrum-programmet. Minimera det bara när du använder Electrum.


### Kör Electrum med Appimage


Det här är lite enklare, men inte lika enkelt som en körbar fil i Windows. Beroende på vilken version av Linux du kör, kan Appimage-filer som standard ha attribut inställda så att exekvering inte tillåts av systemet. Vi måste ändra detta. Om dina Appimages fungerar kan du hoppa över det här steget. Navigera till den plats där filen finns med hjälp av terminalen och kör sedan detta kommando:


```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```


"sudo" ger superanvändarprivilegier; "chmod" är ett kommando för att ändra läget, ändra vem som kan läsa, skriva eller köra; "ug+x" betyder att vi ändrar användaren och gruppen för att tillåta körning.


Justera filnamnet så att det stämmer överens med din version.


Sedan kommer Electrum att köras genom att dubbelklicka på Appimage-ikonen.


### Kör Electrum med Mac


Dubbelklicka bara på den nedladdade filen (det är en "enhet"). Ett fönster kommer att öppnas. Dra Electrum-ikonen i fönstret till skrivbordet, eller var du nu vill ha programmet. Du kan sedan "mata ut" enheten och radera enheten (den nedladdade filen).


För att köra programmet, dubbelklicka bara på det. Du kan få några Mac-specifika "nanny"-fel som måste kringgås.


### Kör Electrum med Windows


Trots att jag hatar Windows mest av allt är det här den enklaste metoden. Dubbelklicka bara på den körbara filen för att köra.


## Börja med en dummy Wallet


När du först laddar Electrum öppnas ett fönster som ser ut så här:


![image](assets/6.webp)


Vi kommer senare att välja din server manuellt, men för tillfället kan du lämna standardinställningen och ansluta automatiskt.


Skapa sedan en dummy Wallet - sätt aldrig in pengar i denna Wallet. Syftet med denna dummy Wallet är att gå igenom programvaran och se till att allt fungerar bra innan du laddar upp din riktiga Wallet. Vi försöker undvika att oavsiktligt ge upp integriteten med en riktig Wallet. Om du bara övar kan den Wallet som du skapar ändå betraktas som en dummy Wallet.


Du kan låta namnet vara "default_wallet" eller ändra det till vad du vill och sedan klicka på "Next". Om du senare har flera plånböcker kan du hitta dem och öppna dem i det här skedet genom att först klicka på "Choose..."


![image](assets/7.webp)


Välj "Standard Wallet" och <Nästa>:


![image](assets/8.webp)


Välj sedan "Jag har redan en seed". Jag vill inte att du ska få för vana att skapa en Electrum seed, eftersom den använder sitt eget protokoll som inte är kompatibelt med andra plånböcker - det är därför vi inte klickar på "ny seed".


![image](assets/9.webp)


Gå till https://iancoleman.io/bip39/ och skapa en dummy seed. Ändra först ordnumret till 12 (vilket är vanligt), klicka sedan på "generate" och kopiera orden i rutan till ditt urklipp.


![image](assets/10.webp)


Klistra sedan in orden i Electrum. Här är ett exempel:


![image](assets/11.webp)


Electrum kommer att leta efter ord som matchar dess eget protokoll. Vi måste kringgå det. Klicka på alternativ, och välj BIP39 seed:


![image](assets/12.webp)


seed blir då giltig. (Innan du gör detta förväntade sig Electrum en Electrum seed så denna seed sågs som ogiltig). Innan du klickar på nästa, lägg märke till texten som säger "Checksum OK". Det är viktigt (för den riktiga Wallet som du kan använda senare) att du ser detta innan du fortsätter, eftersom det bekräftar giltigheten för den seed du lagt in. Varningen längst ner kan ignoreras, det är Electrum-utvecklarens gnäll om BIP39 och deras "FUD'ey"-påståenden om att deras version (som inte är kompatibel med andra plånböcker) är överlägsen.


**En snabb omväg för en viktig varning:** Syftet med kontrollsumman är att se till att du har angett din seed utan skrivfel. Kontrollsumman är den sista delen av seed (det 12:e ordet blir till slut kontrollsumman) som matematiskt bestäms av den första delen av seed (11 ord). Om du skulle skriva något fel i början kommer checksumman inte att matcha matematiskt, och Wallet-programvaran kommer att varna dig med en varning. Detta betyder inte att seed inte kan användas för att skapa en funktionell Bitcoin Wallet. Föreställ dig att du skapar en Wallet med ett skrivfel, laddar Wallet med Bitcoin, sedan en dag kan du behöva återställa Wallet, men när du gör det återskapar du inte skrivfelet - du återställer fel Wallet! Det är ganska farligt att Electrum låter dig fortsätta att skapa en Wallet om din checksumma är ogiltig, så varning, det är ditt ansvar att se till att så sker. Andra plånböcker kommer inte att låta dig fortsätta, vilket är mycket säkrare. Detta är en av de saker jag menar när jag säger att Electrum är bra att använda, när du väl lär dig att använda det ordentligt (Electrum devs bör fixa detta).


Observera att om du vill lägga till en passphrase finns möjligheten att välja det i det här alternativfönstret, högst upp.


När du har klickat på OK kommer du tillbaka till där du skrev seed-frasen. Om du valde ett passphrase-alternativ ska du INTE ange det med seed-orden (uppmaningen om detta kommer härnäst).


Om du inte begärde en passphrase kommer du att se den här skärmen härnäst - fler alternativ för din Wallet-skriptyp och härledningsväg som du kan lära dig mer om här (https://armantheparman.com/public-and-private-keys/), men lämna bara standardvärdena och fortsätt.


![image](assets/13.webp)


**För extra information** Det första alternativet låter dig välja mellan:



- legacy (adresser som börjar med "1"),
- Pay-to-Script-Hash (adresser som börjar med "3"),
- bech32/native SegWit (adresser som börjar med "bc1q").


I skrivande stund har Electrum ännu inte stöd för Taproot (adresser som börjar med "bc1p"). Det andra alternativet i det här fönstret låter dig ändra avledningsstigen. Jag föreslår att du aldrig ändrar detta, särskilt inte innan du förstår vad det innebär. Folk kommer att betona vikten av att skriva ner härledningsvägen så att du kan återställa din Wallet om det behövs, men om du lämnar den som standard kommer du förmodligen att klara dig bra, så få inte panik - men det är fortfarande god praxis att skriva ner härledningsvägen.


Därefter får du möjlighet att lägga till ett LÖSENORD. Detta ska inte förväxlas med "passphrase". Ett lösenord låser filen på din dator. En passphrase är en del av sammansättningen av den privata nyckeln. Eftersom det här är en dummy Wallet kan du lämna lösenordet tomt och fortsätta.


![image](assets/14.webp)


Du kommer att få ett popup-fönster om nya versionsmeddelanden (jag föreslår att du väljer nej). Wallet kommer då att generate sig själv och vara redo att användas (men kom ihåg att denna Wallet är avsedd att raderas, det är bara en dummy Wallet).


![image](assets/15.webp)


Det finns några saker som jag föreslår att du gör för att ställa in programvarumiljön (krävs endast en gång):


### Ändra enheterna till BTC


Gå till toppmenyn, verktyg -> electrum-preferenser, och där under den allmänna fliken hittar du alternativet att ändra "basenheten" till BTC.

Aktivera fliken Adresser och mynt


Gå till toppmenyn, visa och välj "visa adresser". Gå sedan tillbaka till "Visa" och välj "Visa mynt".


### Aktivera Oneserver


Som standard ansluter Electrum till en slumpmässig nod. Den ansluter också till många andra sekundära noder. Jag är inte säker på vilken data som utbyts med dessa sekundära noder, men vi vill inte att det ska hända, av integritetsskäl. Även om du anger en nod, t.ex. din egen nod, kommer dessa många andra noder också att anslutas, och jag är inte säker på vilken information som delas. Oavsett vilket är det lätt att förhindra. Innan jag visar hur du anger din egen nod kommer vi att tvinga Electrum att bara ansluta till en server åt gången.


**Det finns ett sätt att göra detta genom att ange "oneserver" från kommandoraden, men jag rekommenderar inte detta sätt. Jag kommer att visa ett alternativ som jag tror är enklare i det långa loppet, och mer sannolikt att inte låta dig ansluta till andra noder av misstag.


Anledningen till att vi använder en dummy Wallet är att om vi hade laddat vår riktiga Wallet, med vår riktiga Bitcoin, skulle vi oavsiktligt ha anslutit till en slumpmässig nod vid det här laget (även om vi valde "set server manually" i början, ansluter den fortfarande till dessa andra sekundära noder av någon anledning (hej Electrum devs, ni borde fixa detta). Om vår Wallet var privat skulle detta vara en katastrof.


Vi kan inte heller göra de steg som jag kommer att visa dig nedan utan att först ladda upp någon typ av Wallet. (Vi kommer att redigera en konfigurationsfil som bara fylls i och är redo för redigering när en Wallet har laddats).


Stäng nu av Electrum **(VIKTIGT: om du inte gör detta kommer följande ändringar som du gör att raderas)**.


### LINUX/MAC Konfigureringsfil


Öppna terminalen i Linux eller Mac (Windows instruktioner senare):


Du bör automatiskt befinna dig i hemmappen. Därifrån navigerar du till den dolda mappen för Electrum-inställningar (den ligger i en annan mapp än applikationen).


```bash
cd .electrum
```


Lägg märke till punkten före "electrum" som indikerar att det är en dold mapp.


Ett annat sätt att komma dit är att skriva:


```bash
cd ~/.electrum
```


där "~" representerar sökvägen till din hemkatalog. Du kan se den fullständiga sökvägen till din aktuella katalog med kommandot "pwd".


När du är i katalogen ".electrum" skriver du "nano config" och trycker på <enter>.


En textredigerare öppnas (kallas nano) med konfigurationsfilen öppen. Musen fungerar inte mycket här. Använd piltangenterna för att komma till raden där det står:


```json
"oneserver": false,
```


Ändra "false" till "true", och ändra inte syntaxen (ta inte bort kommatecken eller semikolon).


Tryck <ctrl> x, för att avsluta, sedan "y" för att spara, sedan <enter> som bekräftar ändringen utan att redigera filnamnet.


Kör nu Electrum igen. Klicka sedan på cirkeln längst ner till höger, vilket öppnar nätverksinställningarna. Längst upp i fliken Översikt ser du sedan "ansluten till 1 nod" - det betyder att du lyckats.


Precis under det ser du ett textfält och serverns Address finns där. Du är för närvarande ansluten till den slumpmässiga noden. Mer om att ansluta till en nod i nästa avsnitt.


### Konfigurationsfil för Windows


Konfigurationsfilen för Windows är lite svårare att hitta. Katalogen är: `C:/Users/Parman/AppData/Roaming/Electrum`


Självklart måste du ändra "Parman" till ditt eget användarnamn för datorn.


I den mappen hittar du konfigurationsfilen. Öppna den med en textredigerare och redigera raden:


```json
"oneserver": false,
```


Ändra "false" till "true"; ändra inte syntaxen (ta inte bort kommatecken eller semikolon).


Spara sedan filen och avsluta.


## Anslut Electrum till en nod


Därefter vill vi ansluta vår dummy Wallet till en valfri nod. Om du inte är redo att köra en nod kan du göra något av följande:


1. Anslut till en väns personliga nod (kräver Tor)

2. Anslut till en betrodd företagsnod

3. Anslut till en slumpmässig nod (rekommenderas inte).


Förresten, här är instruktioner för att köra din egen nod, och det här är anledningarna till varför du borde göra det. (kolla in tutorials på Node-avsnittet eller i våra kostnadsfria kurser)


### Anslut till en väns nod via Tor (Guide kommer snart.)


### Anslut till en betrodd företagsnod


Det enda skälet till att göra detta är om du måste komma åt Blockchain och inte har din egen nod tillgänglig (eller en väns).


Låt oss ansluta till Bitaroos nod - Vi får veta att de inte samlar in data. De är en Bitcoin Endast Exchange, som drivs av en passionerad Bitcoiner. Att ansluta till dem innebär lite förtroende, men det är bättre än att ansluta till en slumpmässig nod, som kan vara ett övervakningsföretag.


Gå till nätverksinställningarna genom att klicka på cirkeln längst ned till höger i Wallet:s fönster (rött betyder inte ansluten, Green betyder ansluten och blått betyder ansluten via Tor).


![image](assets/16.webp)


När du klickar på cirkelikonen kommer ett popup-fönster att visas: Din Wallet kommer att visa "ansluten till 1 nod" eftersom vi tvingade fram det tidigare.


Avmarkera rutan "välj server automatiskt" och skriv sedan in Bitaroos uppgifter i fältet Server enligt bilden:


![image](assets/17.webp)


Stäng fönstret, och nu bör vi vara anslutna till Bitaroos nod. För att bekräfta bör cirkeln vara Green. Klicka på den igen och kontrollera att serverinformationen inte har ändrats tillbaka till en slumpmässig nod.


### Anslut till din egen nod


Om du har din egen nod är det bra. Om du bara har Bitcoin Core, och inte en Electrum SERVER också, kommer du ännu inte att kunna ansluta en Electrum Wallet till din nod.


**Observera att Electrum Server och Electrum Wallet är olika saker:** servern är programvara som krävs för att Electrum Wallet ska kunna kommunicera Bitcoin Blockchain - jag vet inte varför den utformades på detta sätt - möjligen för hastighet men jag kan ha fel.


Om du kör ett nodprogram som MyNode (som jag rekommenderar att man börjar med), Raspiblitz (rekommenderas när du blir mer avancerad) eller Umbrel (som jag personligen inte rekommenderar ännu eftersom jag har upplevt för många problem) kan du ansluta din Wallet genom att helt enkelt ange IP Address för den dator (Raspberry Pi) som kör noden, plus ett kolon och 50002, som visas på bilden i föregående avsnitt. (Längre ner visar jag hur du hittar din nods IP Address).


Öppna nätverksinställningarna (klicka på Green eller den röda cirkeln längst ner till höger). Avmarkera rutan "välj server automatiskt" och ange sedan din IP Address som jag har gjort, din kommer att vara annorlunda, men kolon och "50002" bör vara desamma.


![image](assets/18.webp)


Stäng fönstret och nu bör vi vara anslutna till din nod. För att bekräfta, klicka på cirkeln igen och kontrollera att serveruppgifterna inte har ändrats tillbaka till en slumpmässig nod.


Ibland, trots att du gör allt rätt, vägrar den till synes att ansluta. Här är några saker du kan prova..



- Uppgradera till en nyare version av Electrum och din nodprogramvara;
- Försök att ta bort cachemappen i katalogen ".electrum";
- Prova att ändra porten från 50002 till 50001 i nätverksinställningarna;
- Använd [den här guiden] (https://armantheparman.com/tor/) för att ansluta med Tor som ett alternativ;
- Installera om Electrum Server på noden.


## Hitta din nods IP Address


En IP Address är inte något som en vanlig användare vanligtvis vet hur man letar upp och använder. Jag har hjälpt många människor att köra en nod och sedan ansluta sina plånböcker till noden - en stötesten verkar ofta vara att hitta dess IP Address.


För MyNode kan du skriva in i ett webbläsarfönster: `mynode.local`


Ibland fungerar inte "mynode.local" (se till att du inte skriver det i ett Google-sökfält. För att tvinga navigeringsfältet att känna igen din text som en Address och inte en sökning, föregå texten med `http://` så här: `http://mynode.local`. Om det inte fungerar kan du prova med ett "s", så här: `https://mynode.local`.


Detta ger åtkomst till enheten och du kan klicka på inställningslänken (se min blå "cirkel" nedan) för att visa den här skärmen var IP Address finns:


![image](assets/19.webp)


Den här sidan laddas och du ser nodens IP (blå "cirkel")


![image](assets/20.webp)


I framtiden kan du sedan skriva 192.168.0.150 eller http://192.168.0.150 i din webbläsare.


För Raspiblitz (när du inte ansluter en skärm) behöver du en annan metod (som fungerar för MyNode också):


Logga in på routerns webbsida - här hittar du IP Address för alla dina anslutna enheter. Routerns webbsida kommer att vara en IP Address som du anger i en webbläsare. Mitt utseende är:


http://192.168.0.1


För att få inloggningsuppgifterna till routern kan du leta efter dem i användarhandboken eller ibland till och med på en klistermärke på själva routern. Leta efter användarnamn och lösenord. Om du inte hittar det kan du prova Användare: "admin" Lösenord: "lösenord"


Om du kan logga in kommer du att se dina anslutna enheter och från deras namn kan det vara tydligt vilken nod du har. IP Address kommer att finnas där.


### Om de två första metoderna misslyckas fungerar den sista, men det är tråkigt:


Först hittar du IP Address för en enhet i ditt nätverk (den aktuella datorn räcker).


På en Mac hittar du den i Nätverksinställningar:


![image](assets/21.webp)


Vi är intresserade av de första 4 Elements (192.168.0), inte det 4:e elementet, "166" som du ser på bilden (ditt kommer att vara annorlunda).


För Linux använder du kommandoraden:


```bash
ifconfig | grep inet
```


Den vertikala linjen är "pipe"-symbolen och du hittar den under <delete>-tangenten. Du kommer att se en del utdata och en IP Address. (Ignorera 127.0.0.1, det är inte det, och ignorera nätmasken)


I Windows öppnar du kommandotolken (cmd) och skriver:


```bash
ipconfig/all
```


och tryck på Enter. IP Address kan hittas i utmatningen.


Det var den enkla biten. Hard-delen är nu att hitta din nods IP Address - vi måste gissa med brute-force. Låt oss till exempel säga att din dators IP Address börjar med 192.168.0.xxx, sedan för din nod, i en webbläsare, försök: `https://192.168.0.2`


Det minsta möjliga talet är 2 (0 betyder vilken enhet som helst, och 1 tillhör routern) och det högsta, tror jag, är 255 (detta råkar vara 11111111 i binär, det största talet som ryms i 1 byte).


En efter en, arbeta dig upp mot 255. Så småningom kommer du att stanna vid rätt nummer som laddar din MyNode-sida (eller RaspiBlitz-sida). Då vet du vilket nummer du ska ange i dina Electrum-nätverksinställningar för att ansluta till din nod.


Det kommer att se ut ungefär så här (se till att du inkluderar kolon och nummer efteråt):


![image](assets/22.webp)


**Anmärkning** Det är bra att veta att dessa IP-adresser är INTERNA i ditt hemnätverk. Ingen utomstående kan se dem och de är inte känsliga. De är ungefär som telefonväxlar i en stor organisation som leder dig till olika telefoner.


## Ta bort dummy Wallet


Nu har vi framgångsrikt anslutit till en och endast en nod. Detta är hur Electrum kommer att laddas som standard från och med nu. Du bör nu ta bort dummy Wallet (Meny: fil -> ta bort), ifall du av misstag skickar pengar till denna osäkra Wallet (Den är osäker eftersom vi inte skapade den på ett säkert sätt).


## Gör en övning Wallet


Efter att ha tagit bort dummy Wallet, börja om och skapa en ny, på samma sätt, bara den här gången, skriv ner seed-orden och håll dem ganska säkra.


Det är en bra idé att lära sig hur Electrum fungerar med denna övning Wallet, utan den besvärliga Hardware Wallet (som behövs för hög säkerhet). Lägg bara en liten mängd Bitcoin i denna Wallet - anta att du kommer att förlora dessa pengar. När du är duktig, lär dig sedan att använda Electrum med en Hardware Wallet.


I den nya Wallet som du har skapat ser du en lista med adresser. De som finns i Green kallas "mottagningsadresser". De är en produkt av 3 saker:



- seed-fras
- passphrase
- Härledningsvägen


Din nya Wallet har en uppsättning mottagningsadresser som matematiskt och reproducerbart kan skapas av vilken Software Wallet som helst som har seed, passphrase och avledningsvägen. Det finns 4,3 miljarder av dem! Fler än du kommer att behöva. Electrum visar dig bara de första 20, och sedan fler när du använder upp de första.


Mer information om privata nycklar för Bitcoin finns i den här guiden.


![image](assets/23.webp)


Detta skiljer sig mycket från vissa andra plånböcker som bara presenterar 1 Address åt gången.


Eftersom du angav frasen seed när du skapade denna Wallet har Electrum den privata nyckeln för var och en av adresserna, och det är möjligt att spendera från dessa adresser.


Observera också att det finns gula adresser, kallade "ändringsadresser" - Dessa är bara en annan uppsättning adresser från en annan matematisk gren (ytterligare 4,3 miljarder av dessa finns). De används av Wallet för att automatiskt skicka överflödiga medel tillbaka till Wallet som förändring. Om du till exempel tar 1,5 Bitcoin och spenderar 0,5 till en handlare, måste de 1,0 som återstår gå någonstans. Din Wallet kommer att spendera den till nästa tomma gula växel Address - annars går den till Miner! För mer information om detta (UTXO:er) se ![denna guide](https://armantheparman.com/UTXO/).


Gå sedan tillbaka till Ian Colmans webbplats för privata nycklar och ange seed (istället för att generera en). Du kommer att se nedan att informationen om den privata och offentliga nyckeln ändras; allt nedan är beroende av sakerna ovan på sidan.


** Kom ihåg:** du bör "aldrig" ange seed för din riktiga Bitcoin Wallet eller en dator, ett skadligt program kan stjäla det. Vi använder bara en övning Wallet, för inlärningsändamål, så det är bra för nu.


Scrolla ner och ändra härledningsvägen till BIP84 (SegWit) för att matcha din Electrum Wallet genom att klicka på fliken BIP84.


![image](assets/24.webp)


Under det ser du kontots utökade privata nyckel och kontots utökade offentliga nyckel:


![image](assets/25.webp)


Gå in på Electrum och jämför att de matchar. Det finns en meny högst upp, Wallet ->information:


![image](assets/26.webp)


Detta dyker upp:


![image](assets/27.webp)


Observera att de två offentliga nycklarna matchar.


Jämför sedan adresserna. Gå tillbaka till Ian Colemans webbplats och bläddra längst ner:


![image](assets/28.webp)


Observera att de stämmer överens med adresserna i Electrum.


Nu ska vi kontrollera ändringsadresserna. Scrolla upp en bit till derivationsvägen och ändra den sista 0:an till en 1:a:


![image](assets/29.webp)


Scrolla nu ner och jämför adresserna med de gula adresserna i Electrum


Varför gjorde vi allt det här?


Vi tog seed-orden och körde dem genom två olika oberoende program för att se till att de gav oss samma information. Detta minskar avsevärt risken för att skum kod lurar inuti och ger oss falska privata eller publika nycklar eller adresser.


Nästa sak att göra är att ta emot ett litet test och spendera det inom Wallet från en Address till en annan.


## Testa Wallet (Lär dig använda den)


Här ska jag visa dig hur du tar emot en UTXO till din Wallet och sedan flyttar den (spenderar den) till en annan Address inom Wallet. Detta är en mycket liten summa som vi inte har något emot att riskera att förlora.


Detta har ett antal syften.



- Det kommer att bevisa att du har makten att spendera mynt i den nya Wallet.
- Den kommer att visa hur man använder Electrum-programvaran för att göra en spend (och vissa funktioner), innan vi lägger till extra komplexitet för säkerheten (med hjälp av en Hardware Wallet eller luftgapad dator)
- Det kommer att förstärka idén om att du har många adresser att välja mellan för att ta emot och spendera inom samma Wallet.


Öppna ditt test Electrum Wallet och klicka på fliken Adresser, högerklicka sedan på den första Address och välj Kopiera -> Address:


![image](assets/30.webp)


Address finns nu i din dators minne.


Gå nu till en Exchange där du har lite Bitcoin, och låt oss ta ut en liten summa till denna Address, säg 50 000 Sats. Jag kommer att använda Coinbase som ett exempel eftersom det är den mest använda Exchange, även om de är en fiende till Bitcoin, och jag äcklas av att logga in på ett gammalt övergivet konto för detta ändamål.


Logga in och klicka på Send/Receive-knappen, som från och med idag finns i det övre högra hörnet på webbsidan.


![image](assets/31.webp)


Jag har såklart inga pengar hos Coinbase, men tänk dig att det finns pengar här och följ med: Klistra in Address från Electrum i fältet "Till" som jag har gjort. Du måste också välja ett belopp (jag föreslår 50 000 Sats eller så). Skriv inte ett "valfritt meddelande" - Coinbase samlar in tillräckligt med data (och säljer den), det finns ingen anledning att hjälpa dem. Slutligen klickar du på "Fortsätt". Efter det vet jag inte vilka andra popup-fönster du kommer att få, du är på egen hand, men metoden är liknande för alla börser.


![image](assets/32.webp)


Beroende på Exchange kan du se Sats i din Wallet omedelbart, eller efter några timmar/dagar.


Observera att Electrum kommer att visa dig mottagna mynt även om de inte har bekräftats på Blockchain. De mynt du har läses från en Bitcoin-nods väntelista, eller "Mempool". När den kommer till ett block kommer du att se pengarna som bekräftade.


Nu när vi har en UTXO i vår Wallet bör vi märka den. Bara vi kan se denna etikett, den har inget att göra med den offentliga Ledger. Alla våra Electrum-etiketter är bara synliga på den dator vi använder. Vi kan faktiskt spara en fil och använda den för att återställa alla våra etiketter till en annan dator som kör samma Wallet.


### Skapa en etikett för en UTXO


Jag behövde en donation till detta test Wallet, tack vare @Sathoarder som gav mig en live UTXO (10 000 Sats), och en annan person (anon) donerade till samma Address (5000 Sats). Observera att det finns 15 000 Sats i det första Address-saldot och totalt 2 transaktioner (kolumnen längst till höger). Längst ner är saldot 10 000 Sats bekräftat, och ytterligare 5 000 Sats är obekräftade (fortfarande i Mempool).


![image](assets/33.webp)


Om vi nu går över till fliken Mynt kan vi se två "mottagna mynt" eller UTXO. De är båda i samma Address.


![image](assets/34.webp)


Om du går tillbaka till fliken Address och dubbelklickar på området "etiketter" bredvid Address kan du skriva in lite text och sedan trycka på <enter> för att spara:


![image](assets/35.webp)


Detta är bra praxis så att du kan hålla reda på var dina mynt kom ifrån, om de är KYC-fria eller inte, och hur mycket varje UTXO kostade dig (om du behöver sälja och beräkna den skatt som din regering har stulit från dig).


Helst bör du undvika att samla flera mynt i samma Address. Om du bestämmer dig för att göra det (gör inte det) kan du märka varje mynt istället för att alla mynt har samma märkning med Address-metoden. Du kan inte gå till fliken "mynt" och redigera etiketterna där (nej, det skulle vara för intuitivt!). Du måste gå till fliken Historik, hitta transaktionen, märka den, och sedan ser du märkningen i myntsektionen. Alla etiketter som du ser i myntsektionen är från Address-etiketterna ELLER historiketiketterna, men alla historiketiketter åsidosätter alla Address-etiketter. Om du vill säkerhetskopiera dina etiketter till en fil kan du exportera dem från menyn högst upp, Wallet->etiketter->export.


Låt oss sedan spendera mynten från den första Address till den andra Address. Högerklicka på den första Address och välj "spendera från" (Detta är faktiskt inte nödvändigt i det här scenariot, men tänk dig att vi har många mynt på många adresser; med hjälp av den här funktionen kan vi tvinga Wallet att bara spendera de mynt vi vill ha. Om vi vill välja flera mynt på flera adresser kan vi välja adresserna genom att klicka med vänster musknapp samtidigt som vi håller ner kommandotangenten, högerklicka och välja "spendera från":


![image](assets/36.webp)


När du har gjort det visas ett Green-fält längst ned i Wallet-fönstret som anger antalet mynt du har valt och den totala summan som finns tillgänglig att spendera.


Du kan också spendera enskilda mynt inom en Address och utesluta andra i samma Address, men detta avråds eftersom du lämnar mynt i en Address som har försvagats kryptografiskt på grund av att ett av mynten spenderas (en annan anledning till att inte lägga flera mynt i en Address, förutom av integritetsskäl, är att med tanke på att du bör spendera dem alla om du spenderar ett, blir detta onödigt dyrt). Så här väljer du ett enda mynt från en delad Address, men gör det inte:


![image](assets/37.webp)


Nu har vi valt ut två mynt som ska spenderas. Därefter bestämmer vi var de ska spenderas. Låt oss skicka dem till den andra Address. Vi måste kopiera Address så här:


![image](assets/38.webp)


Gå sedan till fliken "Skicka" och klistra in den andra Address i fältet "betala till". Du behöver inte lägga till en beskrivning, men det kan du göra senare genom att redigera etiketter. För beloppet väljer du "Max" för att spendera alla mynt vi valde. Klicka sedan på "Pay" och sedan på knappen "advanced" i popup-fönstret som visas.


![image](assets/39.webp)


Klicka alltid på "avancerad" i det här skedet så att vi kan få finkontroll och kontrollera exakt vad som finns i transaktionen. Här är transaktionen:


![image](assets/40.webp)


Vi ser två interna vita lådor/fönster. Det övre är fönstret för inmatning (vilka mynt som spenderas) och det nedre är fönstret för utmatning (vart mynten tar vägen).


Observera att statusen (längst upp till vänster) är "osignerad" för tillfället. "Sänt belopp" är 0 eftersom mynten överförs inom Wallet. Avgiften är 481 Sats. Observera att om det var 480 Sats skulle den sista nollan tappas bort, så här, 0,0000048 och för det trötta ögat kan detta se ut som 48 Sats - var försiktig (något som Electrum devs borde fixa).


Transaktionens storlek avser datastorleken i bytes, inte beloppet för Bitcoin. "Replace by fee" är aktiverat som standard, och det gör att du kan skicka om transaktionen med en högre avgift om det behövs. Med LockTime kan du justera när transaktionen är giltig - jag har inte lekt med det ännu, men avråder från att använda det om du inte förstår vad du gör och har haft lite övning med små belopp.


Längst ner har vi några snygga Mining-avgiftsjusteringsverktyg. Allt du behöver göra för interna överföringar är att ställa in den till den lägsta avgiften på 1 sat/byte. Skriv bara in siffran manuellt i fältet Target fee. För att kontrollera en lämplig avgift för en extern betalning kan du gå till https://Mempool.space för att se hur upptagen Mempool är, och några föreslagna avgifter visas.


![image](assets/41.webp)


Jag har valt 1 sat/byte.


I inmatningsfönstret ser vi två poster. Den första är donationen på 5000 sat. Vi ser till vänster dess transaktion Hash (som vi kan slå upp på Blockchain). Bredvid står det "21" - det betyder att det är utmatning märkt 21 i den transaktionen (det är faktiskt den 22:a utmatningen eftersom den första är märkt noll).


Något att notera här: UTXO:er existerar endast inom en transaktion. För att spendera en UTXO måste vi referera till den och sätta den referensen i ingången till en ny transaktion. Utgångarna blir då nya UTXO:er och den gamla UTXO blir en STXO (utgång för spenderad transaktion).


Den andra raden är donationen på 10 000 sat. Den har en "0" bredvid transaktionen Hash som den kom från eftersom det är den första (och möjligen enda) utmatningen för den transaktionen.


I det nedre fönstret ser vi vår Address. Lägg märke till att summan av ingångarna i Bitcoin inte riktigt matchar summan av utgångarna. Skillnaden går till Miner. Miner tittar på avvikelsen i alla transaktioner i blocket som den försöker bryta och lägger till det antalet till sin belöning. (Mining-avgifter på detta sätt är helt bortkopplade från transaktionskedjan och börjar ett nytt liv).


Om vi justerar Mining-avgiften kommer utgångsvärdet automatiskt att ändras.


**Det är värt att påpeka här:** notera färgen på adresserna i transaktionsfönstret. Kom ihåg att Green-adresserna är listade i din Address-flik. Om en Address är markerad Green (eller gul) i ett transaktionsfönster har Electrum identifierat Address som en av sina egna. Om Address inte har någon markering är det en extern Address (extern till den för närvarande öppna Wallet), och du bör kontrollera den extra noga.


När du har kontrollerat allt i transaktionen och är säker på att du är nöjd med vilka mynt du spenderar och vart mynten går, kan du klicka på "Slutför"


![image](assets/42.webp)


När du har klickat på "finalise" kan du inte längre göra ändringar - om du behöver det måste du stänga det här och börja om från början. Lägg märke till att knappen "finalise" har ändrats till "export" och att nya knappar har dykt upp: "spara", "kombinera", "signera" och "sända". Knappen "broadcast" är grå eftersom transaktionen inte är signerad och därmed ogiltig i det här skedet.


När du klickar på sign, om du har ett lösenord för Wallet, kommer du att uppmanas att ange det, och sedan ändras statusen (uppe till höger) från "Unsigned" till "Signed". Då kommer knappen "Broadcast" att vara tillgänglig.


När du har sänt kan du stänga transaktionsfönstret. Om du går till fliken Address ser du nu att den första Address är tom och att den andra Address har 1 UTXO.


Obs: Du kommer att se alla dessa förändringar redan innan transaktionen har minats till ett block eller "bekräftats". Detta beror på att Electrum uppdaterar saldon/transaktioner baserat på inte bara Blockchain-data, utan även Mempool-data. Inte alla plånböcker gör detta.


Något som bör påpekas är att vi i stället för att sända kan spara transaktionen till senare. Den kan sparas antingen i osignerat eller signerat tillstånd.


Klicka på "export"-knappen (paradoxalt nog ska du INTE klicka på "spara"-knappen), så visas ett antal alternativ. Transaktionen är kodad med text och kan därför sparas på ett antal olika sätt.


![image](assets/43.webp)


Att spara till en QR-kod är mycket intressant. Om du väljer detta kommer en QR att dyka upp:


![image](assets/44.webp)


Du kan sedan ta ett foto av QR-koden. Det finns ett antal saker du kan göra med detta, men låt oss för tillfället bara säga att du laddar tillbaka den i Wallet senare. Du kan stänga Electrum, ladda Wallet igen och gå till menyn Verktyg:


![image](assets/45.webp)


Detta kommer att ladda upp datorns kamera. Du visar sedan kameran bilden av QR-koden i din telefon, och detta kommer att ladda transaktionen tillbaka, exakt som du lämnade den.


Det är inte intuitivt hur man laddar en sparad transaktion, så var särskilt uppmärksam. Att ladda en transaktion är inte ett "verktyg" men alternativet är dolt i verktygsmenyn (en annan sak som Electrum devs borde fixa).


En liknande process är möjlig med en transaktion som sparas som en fil. Prova att öva med båda metoderna inom samma Wallet. Jag ska inte gå igenom det här, men du kan använda den här funktionen för att skicka en transaktion mellan samma Wallet på olika datorer, mellan plånböcker med flera signaturer och till och från hårdvaruplånböcker. Här är några instruktioner.


För att återgå till "spara"-knappen - det här är inte hur man sparar transaktionstexten. Vad detta faktiskt gör är att tala om för Electrum Wallet att känna igen denna transaktion på den lokala datorn som att den har skickats in som en betalning. Om du gör det av misstag kommer du att se transaktionen med en liten datorikon. Du kan högerklicka och ta bort transaktionen - oroa dig inte, du kan inte ta bort Bitcoin på det här sättet. Electrum kommer då att glömma att den här transaktionen någonsin har skett, och kommer att "återbetala" Sats tillbaka och visa Sats på rätt plats där de faktiskt finns.


### Ändra adresser


Ändra adresser är intressant. Du måste förstå UTXO:er för att förstå den här förklaringen. Om du spenderar till en Address ett belopp som är mindre än UTXO, kommer den överblivna Bitcoin att gå till Miner om inte en ändringsutgång anges.


Du kanske har 6,15 Bitcoin UTXO och vill spendera 0,15 Bitcoin för att donera till några demonstranter som förtrycks av den tyranniska "demokratiska" regeringen någonstans i världen. Du skulle då ta de 6,15 Bitcoin (med hjälp av funktionen "spendera från" i Electrum) och lägga dem i en transaktion.


Du klistrar in demonstranternas Address i fältet "betala till", kanske skriver du "EndTheFed & WEF" i fältet "beskrivning", och för beloppet skriver du 0,15 Bitcoin och klickar på "betala" och sedan "avancerad".


På transaktionsskärmen, för inmatningsfönstret, ser du 6,15 Bitcoin UTXO. För utmatningsfönstret ser du en Address som inte har någon markering (detta är demonstranternas Address) med 0,15 Bitcoin bredvid den. Du kommer också att se en gul Address med något mindre än 6,0 Bitcoin. Detta är förändringen Address som automatiskt valts av Wallet från en av dess egna gula förändringsadresser. Syftet med växel-Address är att Wallet ska kunna lägga växelmynt i dem utan att störa tillgängligheten för de mottagningsadresser som du kanske har planer för eller skickat fakturor till. Om de ska användas senare av kunder, till exempel, vill du inte att din Wallet automatiskt ska använda dem och fylla dem. Det är rörigt och dåligt för integriteten.


Observera att när du justerar Mining-avgiften justeras det ändrade utmatningsbeloppet automatiskt, inte betalningsbeloppet.


### Manuell ändring eller betala till många


Det här är en riktigt intressant funktion i Electrum. Du kommer åt det så här.


![image](assets/46.webp)


Du kan sedan ange flera destinationer för det UTXO-saldo som du spenderar, så här:


![image](assets/47.webp)


Klistra in Address, skriv in ett kommatecken, sedan ett mellanslag, sedan beloppet, sedan <enter> och gör sedan om det. ANGE INTE BELOPP I "BELOPP"-fönstren - Electrum fyller i totalsumman här när du skriver in de enskilda beloppen i "Betala till"-fönstret.


Detta gör att du manuellt kan bestämma var förändringen ska gå (t.ex. en specifik Address i din Wallet, eller en annan Wallet), eller så kan du betala många personer samtidigt. Om din totalsumma inte är tillräckligt hög för att matcha storleken på UTXO kommer Electrum ändå att skapa en extra växelutgång åt dig.


Pay to Many-funktionen ger också möjlighet att skapa egna "PayJoins" eller "CoinJoins" - utanför ramen för den här artikeln, men jag har en guide här. (https://armantheparman.com/cj/)


## Plånböcker


Jag vill demonstrera en Watching Only Wallet med hjälp av Electrum. För att göra det måste jag först definiera "Wallet". Det finns två sätt som "Wallet" används på i Bitcoin:



- Typ A, "Wallet" - avser den programvara som visar dina adresser och saldon, t.ex. Electrum, Blue Wallet, Sparrow wallet etc.



- Typ B, "Wallet" - avser den unika samlingen av adresser som är associerade med kombinationen av vår seed_phrase/passphrase/derivation_path. Det finns 8,6 miljarder adresser i varje Wallet (4,3 miljarder mottagaradresser och 4,3 miljarder ändringsadresser). Om du ändrar något i seed-frasen, passphrase eller härledningsvägen får du en oanvänd Wallet med nya, och alla unika, 8,6 miljarder tomma adresser.


Vilken typ som avses när man använder ordet "Wallet" är uppenbart i sammanhanget.


## Att titta på Wallet - en övning


Det är inte helt uppenbart vad en Wallet är till för, men jag ska börja med att förklara vad det är, hur man gör en övning, och sedan återkommer vi till dess syfte senare när jag förklarar mer om hårdvaruplånböcker. (För en djupgående genomgång av hur man använder en Hardware Wallet, och olika specifika märken, se här)


Vi kommer att göra en dummy vanlig Wallet (den här gången lägger vi till lite mer komplexitet med en passphrase), och sedan dess motsvarande tittar Wallet. Om du vill kan du kopiera den jag gjorde exakt, eller skapa din egen - denna Wallet ska kasseras; använd den faktiskt inte. Börja med att generera en seed med 12 ord med hjälp av Ian Colemans webbplats.


Lägg märke till de 12 slumpmässiga orden i skärmdumpen nedan, och att jag har skrivit in en passphrase i fältet passphrase:


passphrase: "Craig Wright är en lögnare och en bedragare och hör hemma i fängelse. Ross Ulbricht bör också släppas från fängelset omedelbart."


passphrase kan vara upp till 100 tecken långt, och bör helst vara entydigt och inte för kort - Det jag har använt är bara för skojs skull - Jag föreslår generellt att man undviker versaler och symboler bara för att minska din stress när du försöker kombinera om du någonsin har haft problem med att komma ihåg din passphrase.


![image](assets/48.webp)


Gå sedan i Electrum till menyn fil->ny/återställ. Skriv ett unikt namn för att skapa en ny Wallet och klicka på "next".


![image](assets/49.webp)


De följande stegen bör du känna till vid det här laget, så jag listar dem utan bilder:



- Standard Wallet
- Jag har redan en seed
- Kopiera och klistra in de 12 orden i rutan, eller skriv in dem manuellt.
- Klicka på alternativ och välj BIP39, och klicka också på passphrase-bocken ("förläng denna seed med anpassade ord")
- Ange din passphrase precis som du gjorde på Ian Coleman-sidan
- Lämna standardskriptets semantik och härledningssökväg
- Inget behov av att lägga till ett lösenord (låser Wallet)


Gå nu tillbaka till Ian Colemans webbplats, ner till avsnittet "derivation path" och klicka på fliken "BIP 84" för att välja samma skriptsemantik som standardvärdena i Electrum (Native SegWit).


![image](assets/50.webp)


De utökade privata och offentliga nycklarna finns precis nedanför, och de ändras när du gör ändringar i härledningsstigen (eller något annat högre upp på sidan).


![image](assets/51.webp)


Du kommer också att se "BIP32 extended private/public"-nycklar - dessa ska ignoreras för tillfället.


Den utökade privata nyckeln för kontot kan användas för att helt regenerera din Wallet. Den utökade offentliga nyckeln för kontot kan dock bara producera en begränsad version av samma Wallet (titta på Wallet) - Om du lägger den här nyckeln i Electrum kommer den fortfarande att producera alla de 8,6 miljarder adresser som seed eller den utökade privata nyckeln skulle ha, men det kommer inte att finnas några privata nycklar tillgängliga för Electrum, så inga utgifter är möjliga. Låt oss göra det nu för att demonstrera poängen:


Kopiera "account extended public key" till urklipp.


Gå sedan till Electrum, lämna den nuvarande Wallet som vi gjorde öppen och gå till fil->ny/återställ. Processen för att göra Wallet är lite annorlunda än tidigare:



- Standard Wallet
- Använd en huvudnyckel
- Klistra in den utökade offentliga nyckeln i rutan och fortsätt
- Du behöver inte ange en passphrase; den är redan en del av den utökade publika nyckeln
- Inget behov av att ange skriptets semantik och härledningsväg
- Inget behov av att lägga till ett lösenord (låser Wallet)


När Wallet laddas bör du märka att exakt samma adresser laddas som tidigare när seed matades in. Du bör också lägga märke till att det längst upp i titelfältet står "tittar på Wallet". Denna Wallet kan visa dig dina adresser och saldon (genom att kontrollera saldon via en nod), men du kan inte SIGNERA transaktioner (eftersom den övervakande Wallet inte har några privata nycklar).


Vad är det då för mening med det?


En anledning, och inte den viktigaste, är att du potentiellt kan observera din Wallet och dess balans på en dator utan att exponera dina privata nycklar för någon skadlig kod på datorn.


En annan är att det är NÖDVÄNDIGT för att göra betalningar om du väljer att hålla dina privata nycklar borta från datorn; jag ska förklara:


**Hårdvaruplånböcker (HWW)** skapades så att en enhet kan hålla dina privata nycklar säkert (låsta med en PIN-kod), aldrig exponera nycklarna för en dator (även när de är anslutna till en dator via en kabel) och själva inte kan ansluta till internet. En sådan enhet kan inte göra transaktioner på egen hand eftersom alla Bitcoin-transaktioner börjar med att referera till en eller flera UTXO på Blockchain (som finns på en nod). En Wallet måste specificera vilken transaction ID UTXO finns i, och vilken utgång av transaktionen som är den som ska spenderas. Först efter att ha specificerat inmatningen kan en ny transaktion överhuvudtaget skapas, än mindre signeras. Hårdvaruplånböcker kan inte skapa transaktioner eftersom de inte har tillgång till några UTXO:er - de är inte anslutna till någonting!


En utökad publik nyckel extraheras vanligtvis från HWW, och adresser visas sedan på en dator - många känner till programvaran Ledger eller Trezor Suite som visar adresser och saldon på sin dator - detta är en Wallet-övervakning. Dessa program kan skapa transaktioner, men de kan inte underteckna. De kan bara få transaktioner signerade av HWW som är anslutna till dem. HWW tar den nyligen genererade transaktionen från den bevakande Wallet, signerar den och skickar sedan tillbaka den till datorn för sändning till en nod. **HWW kan inte sända själv**, det gör den tillhörande bevakande Wallet. På så sätt samarbetar de två plånböckerna (publik nyckel Wallet på datorn och privat nyckel Wallet i HWW) för att generate, signera och sända, samtidigt som de privata nycklarna hålls isolerade och borta från en internetansluten enhet.


## Delvis signerade Bitcoin-transaktioner (PSBT)


Det är möjligt för en transaktion att skapas och sparas i en fil, senare laddas om, signeras, sparas, senare laddas om och slutligen sändas ut - jag säger inte att någon skulle behöva göra detta; det är bara något som är möjligt.


Tänk nu på en 3 av 5 multisignatur Wallet - 5 privata nycklar skapar en Wallet, och 3 behövs för att helt signera en transaktion (se här för att lära dig mer om multisignatur Wallet-nycklar). Det är möjligt att ha 5 olika datorer som var och en har en av de fem privata nycklarna.


Dator 1 kan generate en transaktion och signera den. Den kan sedan spara den i en fil och skicka den via e-post till Dator 2. Dator 2 kan sedan signera och kan eventuellt spara filen i en QR-kod och överföra QR-koden via ett Zoom-samtal till dator 3 på andra sidan jorden. Dator 3 kan fånga QR-koden, ladda in transaktionen i electrum och signera transaktionen. Efter de första två signaturerna var transaktionen en PSBT (Partially Signed Bitcoin Transaction). Efter den tredje signeringen blev transaktionen fullständigt signerad och giltig, redo för sändning.


Mer information om PSBTS finns i den här guiden. (https://armantheparman.com/PSBT/)


## Använda hårdvaruplånböcker med Electrum


Jag har en guide om hur man använder hårdvaruplånböcker i allmänhet, som jag tror skulle vara viktigt för människor som är nya för HWW, att läsa. (https://armantheparman.com/using-hwws/)


Det finns också guider om olika märken av HWW som ansluter till Sparrow Bitcoin Wallet som finns här. (https://armantheparman.com/hwws/)


Detta kommer att bli min första guide som visar hur man använder en Hardware Wallet med Electrum - jag kommer att använda ColdCard Hardware Wallet för att demonstrera. Det här är inte tänkt att vara en detaljerad guide om ColdCard specifikt, den guiden finns här. Jag visar bara Electrum-specifika punkter. (https://armantheparman.com/cc/)


### Anslutning via micro SD-kort (luftgap)


Innan du ansluter din riktiga Wallet via ColdCard hoppas jag att du har gått igenom de tidigare stegen med att ladda en Electrum-dummy Wallet och ställa in nätverksparametrarna.


Sätt sedan i SD-kortet på ColdCard. Jag antar att du redan har skapat din seed. Om du kommer åt Wallet med en passphrase, använd den nu. Scrolla ner och välj menyn Advanced/Tools ->Export Wallet -> Electrum Wallet.


Du kan bläddra ner och läsa meddelandet. Det erbjuder dig alltid att välja "1" för att ange ett kontonummer som inte är noll (något som ingår i härledningsvägen), men om du följde mitt råd har du inte rört vid standardhärledningsvägarna så du vill inte ha ett kontonummer som inte är noll; tryck bara på bocken för att fortsätta.


Välj sedan skriptets semantik. De flesta kommer att välja "Native SegWit".


Det kommer att stå "Electrum Wallet file written" och filnamnet kommer att visas. Gör en mental anteckning om det.


Ta sedan ut micro SD-kortet och sätt in det i datorn med Electrum.


Vissa operativsystem öppnar automatiskt filutforskaren när du sätter i microSD-kortet. Många människor kommer att se den nya filen Wallet och dubbelklicka på den och undra varför den inte fungerar. Det är inte en bra design. Du måste faktiskt ignorera filutforskaren (stänga den) och öppna filen Wallet med hjälp av Electrum:


Öppna Electrum. Om det redan är öppet med någon annan Wallet, välj fil -> ny. Vi letar efter det här fönstret:


![image](assets/52.webp)


Här är tricket, det är inte intuitivt. Klicka på "välj". Navigera sedan i filsystemet på microSD-kortet och hitta filen Wallet och öppna den.


Nu har du öppnat upp dina Hardware Wallet:s motsvarande tittar på Wallet. Snyggt.


### Anslutning via USB-kabeln.


Det här sättet borde vara enklare, men för Linux-datorer är det mycket svårare. Något som kallas "Udev rules" måste uppdateras. Så här gör du (detaljerad guide https://armantheparman.com/gpg-articles/ ), och i korthet:


Det är en god idé att se till att systemet är uppdaterat. Då så:


```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```


...sedan...


```bash
python3 -m pip install ckcc-protocol
```


Om du får ett fel ska du kontrollera att pip är installerat. Du kan kontrollera med (pip -version), och du kan installera det med (sudo apt install pythron3-pip)


Skapa eller ändra den befintliga filen /etc/udev/rules.d/


Så här:


```bash
sudo nano /etc/udev/rules.d
```


En textredigerare kommer att öppnas. Kopiera texten härifrån och klistra in den i filen rules.d, spara och avsluta.


![image](assets/53.webp)


Kör sedan dessa kommandon ett efter ett:


```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```


Om du får meddelandet "group plugdev" finns redan, så är det okej, fortsätt. Efter det andra kommandot får du ingen feedback/svar, fortsätt bara till det tredje kommandot.


Du kan behöva koppla bort och sedan återansluta ColdCard till datorn.


Om du efter allt detta fortfarande inte kan ansluta ColdCard, skulle jag försöka uppdatera den fasta programvaran (guide snart, men för närvarande kan du hitta instruktioner på tillverkarens webbplats).


Skapa sedan en ny Wallet:



- Standard Wallet
- Använd en hårdvaruenhet
- Den kommer att skanna och upptäcka ditt ColdCard. Fortsätt med detta.
- Välj skriptets semantik och härledningsväg
- Bestäm om filen Wallet ska krypteras (rekommenderas)


### Transaktioner med hjälp av ColdCard


När kabeln är ansluten är det enkelt att genomföra transaktioner. Signeringstransaktioner kommer att vara sömlösa.


Om du använder enheten på ett luftburet sätt måste du manuellt skicka den sparade transaktionen mellan enheter med hjälp av microSD-kortet. Det finns några knep.


När du har skapat en transaktion och slutfört den måste du klicka på exportknappen i det nedre vänstra hörnet. Du kommer att se "spara i fil" som motstridigt inte är vad vi vill ha. Du måste faktiskt först gå till det allra sista menyalternativet som säger "för hårdvaruplånböcker", och sedan, från det valet, hitta det andra "spara i fil" och välj det. Spara sedan filen på microSD-kortet, ta ut kortet och sätt in det i ColdCard. Kom ihåg att du kan behöva använda en passphrase för att välja rätt Wallet. På skärmen kommer det att stå redo att signera. Klicka på bocken, inspektera transaktionen och fortsätt genom att bekräfta med bocken. När du är klar tar du ut kortet och sätter tillbaka det i datorn.


Då måste vi öppna transaktionen med hjälp av electrum. Funktionen ligger dold i menyn verktyg -> ladda transaktion. Navigera i filsystemet och hitta filen. Det kommer att finnas tre filer varje gång du signerar. Den ursprungliga sparade filen som Watching Wallet gjorde, och två som ColdCard gjorde (jag vet inte varför den gör det). En kommer att säga "signerad" och en kommer att säga "slutlig". Det är inte intuitivt men den "signerade" är inte användbar, vi måste öppna den "slutliga" transaktionen.


När du har laddat den kan du klicka på "sänd" och betalningen kommer att göras.


## Uppdatering av Electrum och den dolda katalogen ".electrum"


Electrum finns på två ställen på din dator. Det är själva programmet och det är en dold konfigurationsmapp. Den mappen finns på olika ställen beroende på vilket operativsystem du har:


Fönster:


```bash
C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```


Mac:


```bash
/Users/your_user_name_goes_here/.electrum
```


Linux:


```bash
/home/your_user_name_goes_here/.electrum
```


Notera att `.` står före `electrum` i Linux och Mac - det betyder att katalogen är dold. Observera också att den här katalogen bara skapas (automatiskt) när du kör Electrum för första gången. Katalogen innehåller konfigurationsfilen för Electrum och även den katalog som innehåller alla plånböcker som du har sparat.


Om du tar bort Electrum-programmet från din dator kommer den dolda katalogen att finnas kvar, såvida du inte aktivt tar bort den också.


För att uppgradera electrum går du igenom samma procedur som jag beskrev i början för att ladda ner och verifiera. Du kommer då att ha två kopior av programmet på din dator, och du kan köra endera - varje program kommer att komma åt samma dolda electrum-mapp för sin konfiguration och Wallet-åtkomst. Alla saker vi sparade, som basenheten, standardnoden att ansluta till, andra inställningar och tillgång till plånböcker, kommer att finnas kvar eftersom allt detta sparas i den mappen.


### Flytta dina Electrum och plånböcker till en annan dator


För att göra detta kan du kopiera programfilerna till en USB-enhet och även kopiera katalogen .electrum. Sedan kopierar eller flyttar du dem till den nya datorn. Du behöver inte verifiera programmet på nytt. Se till att kopiera katalogen .electrum till standardplatsen (kom ihåg att kopiera den INNAN du kör Electrum för första gången på den datorn, annars kommer en tom standardmapp .electrum att fyllas i och du kan bli förvirrad).


## Etiketter


Som jag förklarade tidigare finns det en etikettkolumn på fliken Address. Du kan dubbelklicka där och skriva in anteckningar för dig själv (det är bara på din dator, inte offentligt, och inte på Blockchain).


![image](assets/54.webp)


När du flyttar din Electrum Wallet till en annan dator kanske du vill undvika att förlora alla dessa anteckningar. Du kan säkerhetskopiera dem till en fil genom att använda menyn Wallet > etiketter > export och sedan använda Wallet > etiketter > import på den nya datorn.


## Tips:


Om du tycker att den här resursen är användbar och du vill stödja det jag gör för Bitcoin kan du donera lite Sats här:


Statisk blixt Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/electrum/