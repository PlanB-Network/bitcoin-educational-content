---
name: Coin Control
description: Bekanta dig med Coin Control, ett nyckelverktyg för att skydda din integritet på Bitcoin
---
![cover](assets/cover.webp)


*Denna handledning är importerad från [en lektion av Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Inledning



Bitcoin-protokollets soliditet garanteras av enkla grundläggande koncept. Bland dessa utmärker sig transparensen: alla Bitcoin-transaktioner är offentliga och lätt verifierbara av vem som helst. Även om denna egenskap är en milstolpe i protokollet, eftersom den förhindrar bedrägerier och garanterar medlens äkthet, kan den också utgöra en utmaning för konfidentialiteten. **Har du någonsin undrat om så mycket transparens kan äventyra din integritet?**



Det borde du göra. Även om det är ganska enkelt att samla Satoshi non-kyc är din integritet mest utsatt precis i utgiftsstadiet.



### Vad händer när du spenderar en UTXO



Att spendera Bitcoin är inte bara att överföra värde till någon annan.



Genom att konsumera en av dina UTXO måste du faktiskt uppfylla de villkor som ställs för protokolltransparens, eftersom du har en skyldighet att bevisa att du äger dessa fonder. Du gör dig därför ansvarig för :




- exponera din publika nyckel;
- skapa en digital signatur.



Tidpunkten för utgifterna är därför den mest kritiska: **att spendera Bitcoin är en handling som ska göras medvetet och med så mycket kontroll som möjligt**.



## Coin Kontroll



I Bitcoin-protokollet existerar inte poster som _konto_ eller _monetära enheter_. Konceptet UTXO förklaras på ett utmärkt sätt i följande kurs, som jag varmt rekommenderar:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Med Bitcoin är det du samlar och senare spenderar små eller stora kontoenheter som mäts i Satoshi, representerade av "outnyttjade transaktionsutgångar", **UTXO**, även kallade "mynt". När du använder UTXO:er för att skapa en transaktion förstörs de helt och hållet och andra UTXO:er skapas i deras ställe.



Programvaruplånböcker utvecklas för att göra detta val automatiskt, med hjälp av "slumpmässigt" valda mynt, genom att anta vissa algoritmer som tillhandahålls av protokollet. Det enda kriteriet som dessa algoritmer uppfyller är att täcka det belopp som behövs för att spendera.



De kan blanda UTXO: er i olika åldrar eller föredra att spendera det nyaste eller "äldsta", beroende på den algoritm som valts av utvecklarna. De bästa mjukvaruplånböckerna, planerar också att lämna användaren med ett viktigt val.



Manualen `Coin Control`, som också kallas `Coin Selection`, är en funktion i vissa mjukvaruplånböcker som gör att du kan **manuellt välja UTXO:er att spendera när du bygger din transaktion**.



Anta att vi har en Wallet med 3 UTXO:er på 21 000, 42 000 respektive 63 000 Satoshi.



![img](assets/en/01.webp)



Om du måste spendera 24 000 Sats och låta en algoritm göra det automatiska urvalet kan en bra Software Wallet välja att kombinera UTXO 1 + UTXO 2 för att betala avgifterna på 24 000 Sats och Miner, vilket skapar en rest som går tillbaka till en intern Address i den startande Wallet.



![img](assets/en/02.webp)



Efter transaktionen kan den nya situationen i Wallet, där endast UTXO räknas, sammanfattas enligt följande.



![img](assets/en/03.webp)



Med rätt programvara och din medvetenhet kunde du dock ha gjort ett annat, på vissa sätt mer korrekt val. Till exempel genom att bara välja UTXO2 (från 42 000 Sats).



![img](assets/en/04.webp)



Med en slutsituation i din Wallet, på nivån UTXO, ser det annorlunda ut än tidigare.



![img](assets/en/05.webp)



## Varför manuell coin control?



![img](assets/en/06.webp)



I de två exemplen ovan är saldot faktiskt detsamma `108 280 Sats`. Efter att ha spenderat 24 000 Sats skulle vi utan manuellt urval ha 2 UTXO i Wallet; med Coin manuell kontroll har vi 3 totalt.



Frågan vi skulle kunna ställa oss är följande: **varför göra allt detta?** Det finns, eller kan finnas, flera anledningar till att vi inte använde `UTXO1` **och alla dessa ligger till grund för varför—vid spendering—aktivering av manuell coin control är en av de goda praxis som bör följas**.



Genom att välja UTXO kan du gynna vissa aspekter framför andra. Valet beror egentligen på vilka mål du vill uppnå.



### Integritet



En av de största fördelarna med manuell Coin-kontroll är **större integritet för den som spenderar**. Låt oss alltid ta vårt exempel: utgifterna för 24 000 Satoshi _utan manuellt Coin-val_. Eftersom Blockchain av Bitcoin är ett offentligt register kan en utomstående observatör utan skuggan av ett tvivel förklara att ingångarna `UTXO1 av 21 000 Sats` och `UTXO2 av 42 000 Sats`, samt resten, `UTXO5 från 38 280 Sats` **alla tre tillhör samma användare**.



Genom att manuellt välja `UTXO2`, å andra sidan, förblir `UTXO1` helt reserverad och sitter i UTXO-uppsättningen och väntar på att användas vid en mer lämplig tidpunkt.



"UTXO1" kan komma från en KYC-källa, till exempel en betalning som mottagits i Exchange för varor och tjänster, medan de andra UTXO:erna inte gör det. Att blanda en UTXO-kyc med andra som är mer konfidentiella äventyrar anonymitetsuppsättningen för icke-kyc-medel.



**KYC-medel skulle oundvikligen leda till att betalarens identitet spåras. Om det var din plånbok, skulle du vilja att en extern observatör kan spåra din identitet med en sådan absolut säkerhet?**



Försök då att tänka på att plånböcker som implementerar manuellt urval av UTXO:er, till exempel, tillåter **segregering av en eller flera UTXO:er**, en funktion som ska användas när sådana situationer uppstår.



Även om jag är övertygad om att KYC-fonder bör förvaras i en separat Wallet än Bitcoin som köpts utan kyc, om detta är ditt fall är segregeringen av några av dina adresser en viktig hjälp, som du kan dra nytta av genom att lära dig att manuellt välja dina utgiftsingångar.



### Besparing på avgifter



Genom att välja rätt UTXO för att göra en utgift **möjliggörs avgiftsoptimering**. Återigen med utgångspunkt från vårt första exempel valde Software Wallet två UTXO:er för att täcka den utgift som skulle göras. Två UTXO:er innebär två signaturer som ska visas för nätverket. Av detta följer att transaktionen har en större "vikt" i termer av vBytes.



Med den manuella kontrollen Coin kan du å andra sidan bara välja en som är tillräcklig för att täcka beloppet, vilket sparar avgifter genom att minska transaktionens "vikt".



I tider när avgifterna är höga, men du tvingas spendera Bitcoin On-Chain (t.ex. för att öppna en Lightning Network-kanal), det är då Coin-kontrollen visar sig vara rätt ekonomiskt incitament att vända sig till.



### Sammanslagning av kvarlevorna



När du gör en betalning och använder Bitcoin On-Chain blir möjligheten att få växel nästan alltid en säkerhet. Varje restbelopp är i sig en liten integritetsförlust, eftersom det avslöjar för nätverket (och särskilt för betalningsmottagaren) en Address som tillhör dig och som kan kopplas till din källinmatning.



Med tanke på att de bästa Wallet HDs generate specialadresserna för resterna, kan du enkelt känna igen dem och "segregera" alla rester av de olika transaktionerna som gjorts; när de har nått ett visst belopp kan du välja dem manuellt och konsolidera dem, eller byta till Lightning Network (min föredragna metod) och bearbeta dem för att återfå den integritet som förlorats i utgifterna.



### Utgifter från en Cold Wallet



Cold Wallet är ett instrument med vilket man rimligen kan få en god grad av säkerhet för att lagra alla belopp för att hålla åt sidan under en lång tidsperiod. Men oförutsedda händelser kan inträffa, så behovet uppstår att få tag på besparingar och möta några oväntade utgifter.



Jag vet inte hur många som kan dela mitt tillvägagångssätt, men mitt råd är att ** aldrig göra utgifterna direkt från Cold Wallet, för att undvika att få förändringen mellan adresserna till samma **. Lär dig att manuellt välja de UTXO: er som behövs för att täcka utgiften, överföra dem till en Wallet Hot och förbereda din transaktion från den senare. Eventuell växel kan du sedan skicka tillbaka till en Cold Wallet Address (om beloppet är tillräckligt), använda för andra utgifter eller fortfarande separera den som vi just har sett.



## Praktisk presentation


Efter den tekniska introduktionen av "varför", låt oss se hur man sätter Coin manuell kontroll i praktiken med olika programvaror, stationära och mobila. Vi kommer alltid att använda samma Wallet BIP39, importerad till vart och ett av de valda verktygen, för att visa dig de små skillnaderna mellan dem.



## Wallet Skrivbord



### Sparrow



Om du använder Sparrow öppnar du din Wallet och väljer _UTXOs_ i menyn till vänster. Du kommer att se en lista över alla UTXO som är kopplade till din Wallet.



Klicka bara med musen på en av dem och välj sedan _Send Selected_. Sparrow visar också den totala summan som är tillgänglig för utgifter efter valet, precis bredvid kommandot. Grafiskt visar Sparrow den valda UTXO genom att markera den i blått.



![img](assets/en/07.webp)



Du kan också välja mer än en. Använd _CTRL_-tangenten för att välja UTXO:er som inte ligger intill varandra i listan.



![img](assets/en/08.webp)



När du har valt UTXO manuellt kan du börja bygga upp transaktionen, och Sparrow visar dig grafiskt hur den är uppbyggd.



![img](assets/en/09.webp)



#### Segregering av UTXO



Att separera medel innebär att "låsa" dem inom Wallet så att de inte kan användas som indata i en transaktion. Sparrow tillåter denna funktion, som alltid nås från _UTXOs_-menyn: du placerar musen över den UTXO som ska "låsas" och klickar på höger musknapp. Bland funktionerna i denna procedur kommer _Freeze UTXO_ att visas. Det är så du kommer att kunna segregera mynt med Sparrow plånböcker.



![img](assets/en/29.webp)



### Elektrum



Om ditt Wallet-skrivbord är Electrum bör du veta att du kan välja UTXO:er manuellt antingen från menyn _Addresses_ eller från menyn _Coins_. I båda menyerna görs urvalet genom att peka med musen på önskad UTXO och välja _Add to Coin control_ efter högerklick.



![img](assets/en/10.webp)



Även med denna programvara kan du välja mer än en UTXO och hjälpa till med _CTRL_-tangenten på tangentbordet om de inte ligger intill varandra.



![img](assets/en/11.webp)



Grafiskt kommer Electrum att visa dig urvalet genom att markera de valda UTXO:erna i Green, medan en stapel visas längst ner, markerad i samma färg, som visar det tillgängliga saldot efter Coin-kontrollen.



![img](assets/en/12.webp)



När du har valt utdata, eller utdata, kan du bygga din transaktion som du brukar göra från _Send_-menyn.



#### Segregering av UTXO



Electrum tillhandahåller denna funktion genom att gå till menyn _Coins_, där du väljer en viss UTXO och sedan väljer _Freeze_ med ett högerklick. Du kan "frysa" Address även utan medel från _Addresses_-menyn, eller "Coin" för att inte spendera den.



![img](assets/en/28.webp)



### Nunchuk



Med Nunchuk kan du manuellt välja UTXO:er från huvudmenyn när den är öppen. Starta Nunchuk och klicka på _Visa mynt_.



![img](assets/en/13.webp)



Detta öppnar fönstret som innehåller alla UTXO:er i din Wallet, där du kan välja en eller flera genom att aktivera kryssmarkeringen bredvid varje belopp. När du har gjort ditt val fortsätter du med _Create transaction_.



![img](assets/en/14.webp)



Därefter kan du ange destinationen Address och ställa in belopp och avgifter.



![img](assets/en/15.webp)



#### Segregering av UTXO



För fullständighetens skull tillåter Nunchuk också bland sina funktioner att segregera en (eller flera) UTXO och gör det på två olika sätt. Gå till menyn _Visa mynt_ och välj manuellt från listan med mynt. Klicka sedan på menyn _More_ längst ner till höger: en lista med alternativ visas, där du kan välja _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Du kan också klicka i utrymmet som är reserverat för UTXO för att komma till fönstret _Coin details_. Här visas kommandot för att låsa/låsa upp UTXO i fråga i det övre högra hörnet.



![img](assets/en/41.webp)



### Blockstream App



Blockstream App desktop, tidigare känd som Green, gör att du kan välja Coin när du redan har börjat bygga transaktionen. Öppna därför din Wallet och klicka på _Send_.



![img](assets/en/16.webp)



Klistra in destinationen Address i lämpligt fält och välj sedan _Manuellt Coin-val_.



![img](assets/en/17.webp)



Då öppnas ett fönster där du kan välja ett eller flera UTXO-mynt. I exemplet nedan har vi valt två mynt. Bekräfta därefter ditt val genom att klicka på _Confirm Coin Selection_.



![img](assets/en/18.webp)



Ange belopp och avgifter och fortsätt sedan normalt med din transaktion.



![img](assets/en/19.webp)



⚠️ N.B. I menyn _Coins_ i Green finns det _Lock_/_Unlock_-objekt som förebådar möjligheten att segregera UTXO. Denna funktion är endast aktiverad i så kallade Multisig-konton; den aktiveras också endast genom att välja UTXO av mycket liten mängd, nära tröskeln för `Dust`.



## Wallet mobil



Plånböcker kan också väljas från mobilen, vilket gör att UTXO kan väljas manuellt. Låt oss se Blue Wallet som det första exemplet.



### Blå Wallet



Om du är användare av denna Wallet, öppna den och klicka för att komma till kontrollskärmarna relaterade till en av dina Wallets. För att komma åt kontrollmanualen för Coin måste du gå in i utgiftsfasen och sedan klicka på _Send_.



![img](assets/en/21.webp)



På nästa skärm väljer du de menyer som indikeras av de tre prickarna i det övre högra hörnet. Ett rullgardinsfönster öppnas med en rad kommandon. Välj det sista: _Coin Control_.



![img](assets/en/22.webp)



Vid denna punkt visar Blue Wallet alla dina UTXO:er. Förutom belopp skiljer de sig åt grafiskt genom olika färger.



![img](assets/en/27.webp)



Välj den UTXO som ska väljas och välj sedan _Use Coin_.



![img](assets/en/23.webp)



Blue Wallet tar dig tillbaka till fönstret _Send_ för att fortsätta bygga upp transaktionen. Justera beloppet och avgifterna, varefter du väljer _Next_.



![img](assets/en/24.webp)



Nu kan du avsluta transaktionen som du brukar göra.



#### Segregering av en UTXO



Blue Wallet låter dig också segregera UTXOs, vilket gör dem otillgängliga för utgifter, vilket inte är en dålig funktion för en Wallet från en mobil enhet. Du kommer åt Coin-kontrollen med den procedur som just förklarats och, efter att ha valt UTXO, väljer du _Freeze_ istället för _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Den mobila versionen av Nunchuk ger också användaren möjlighet att göra Coin-kontroll. Om du använder den här appen från mobilen, öppna den och gå till menyn _Wallet_. Därifrån väljer du _Visa mynt_.



![img](assets/en/30.webp)



Klicka på _Select_ i fönstret där listan med UTXO:er visas.



![img](assets/en/38.webp)



En urvalsfunktion visas bredvid varje UTXO. Precis som i desktopversionen görs manuella val på Nunchuk mobile genom att markera den lilla rutan bredvid beloppet. På skärmen visas antalet UTXO som valts och den totala tillgängliga summan. När du är klar klickar du på symbolen ₿ i det nedre vänstra hörnet, vilket är kommandot för att börja bygga transaktionen.



![img](assets/en/31.webp)



Nu kan du slutföra transaktionen genom att välja belopp och klicka på _Continue_.



![img](assets/en/32.webp)



Fortsätt som vanligt, klistra in en destination Address, beskrivning och anpassa avgiftsinställningarna.



#### Segregering av UTXO



Du kan också segregera UTXO:er med mobil Nunchuk. Öppna fönstret med listan över dedikerade mynt och välj pilen bredvid den UTXO som du vill segregera.



![img](assets/en/42.webp)



Du kommer att se ett utrymme reserverat för _Coin details_, där du kan välja _Lock this coin_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper är den sista Wallet som vi kommer att se i den här guiden. Vi ser dess funktionalitet tillämpas på Coin-kontroll med en Wallet single-sig, även om en sådan användning inte är syftet med just denna app. Efter att ha konfigurerat Keeper på din telefon, starta den och öppna en Wallet som innehåller några medel. I mitten av huvudskärmen klickar du på _Visa alla mynt_.



![img](assets/en/34.webp)



Keeper visar en översikt över UTXO:erna. Klicka på _Select To Send_ för att komma till urvalsskärmen.



![img](assets/en/35.webp)



Du kan välja mynt genom att bocka av dem genom att klicka på rätt kommando. När du är klar klickar du på _Send_.



![img](assets/en/36.webp)



Bitcoin Keeper tar dig direkt till _Send_-menyn, där du kan bygga upp transaktionen med de valda UTXO:erna.



![img](assets/en/37.webp)



## Hardware Wallet



Var och en av de programvaruplånböcker som visas i den här guiden kan vara den enda Interface-vakten till en av dina maskinvaruplånböcker. Det innebär att Coin-kontrollen för offline-signeringsenhet utförs med de steg som hittills har setts.



### Allmänna rekommendationer



Coin-kontroll är en mycket effektiv metod för att välja ut dina transaktionsinmatningar. Manuellt urval är ännu mer effektivt om du, när du köper / tar emot dina medel, har märkt källan till dina Satoshis väl. Om du vill lära dig denna teknik väl rekommenderar jag följande handledning:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Vi har tidigare talat om `segregering av kvarlevor`. Om du vill låsa kvarlevor för senare bearbetning och återfå integritet (byt på Layer 2) måste du se till att "märka" dem varje gång du får en. Av de mjukvaruplånböcker som hittills setts är det bara Electrum som grafiskt färgar UTXO-rester för att göra dem synliga med en blick. Andra, som Sparrow, visar dig kedjan i härledningsvägen för den enskilda UTXO (`m/84'/0'/0'/1/11`).



För att tillämpa denna teknik effektivt, kom ihåg att alltid lägga till en beskrivning på den förändring du får: den person som du skickade dina pengar till (en betalning, en handledning eller annat), känner till Address associerad med förändringen och vet att den tillhör dig, eftersom den kommer från den transaktion du gjorde tillsammans!