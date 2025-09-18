---
name: Samourai Wallet - Recover
description: Hur återställer jag bitcoins som fastnat på Samourai Wallet?
---

![cover](assets/cover.webp)


Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är vissa funktioner i applikationen nu ur funktion, och användare som inte har en egen Dojo kan inte längre sända transaktioner.


Efter att ha hjälpt flera användare att återhämta sina bitcoins de senaste dagarna tror jag att jag har stött på de flesta av de problem som kan uppstå under restaureringen av en Samourai Wallet. Därför kommer denna handledning att börja med en situationsrapport för att identifiera de funktioner som förblir operativa och de som inte längre är tillgängliga inom Samourai Wallet-ekosystemet och den programvara som påverkas av denna incident. Därefter fortsätter vi steg för steg för att återställa en Samourai Wallet med hjälp av Sparrow wallet-programvaran. Vi kommer att undersöka alla potentiella hinder som uppstår under denna process och se lösningar för att lösa dem. Slutligen, i den sista delen, kommer du att upptäcka de potentiella riskerna för din integritet efter serverbeslaget.


_Ett stort tack till [@Louferlou] (https://twitter.com/Louferlou), som har hjälpt flera användare i deras återhämtning och delat med sig av sina erfarenheter till mig, och som också har bidragit till tester för att avgöra vad som fortfarande fungerar._


## Är Samourai Wallet fortfarande i arbete?


Ja, **appen Samourai Wallet fungerar fortfarande**, men under vissa förutsättningar.


För det första är det nödvändigt att appen tidigare hade installerats på din smartphone. Google Play Store har tagit bort appen, och APK var värd på den beslagtagna webbplatsen. Därför är det komplicerat att installera Samourai just nu. Du kanske hittar APK: er online, men jag avråder från att ladda ner dem om du inte är säker på källan.


Eftersom Samourai Wallet-sidan inte längre är tillgänglig i Google Play Store är det inte möjligt att inaktivera automatiska uppdateringar. Om appen återkommer till nedladdningsplattformarna är det klokt att **avaktivera automatiska uppdateringar** tills mer information finns tillgänglig om utvecklingen av ärendet.


Om Samourai Wallet redan är installerat på din smartphone bör du fortfarande kunna komma åt appen. För att använda Wallet-funktionaliteten i Samourai är det viktigt att ansluta en Dojo. Tidigare var användare utan en personlig Dojo beroende av Samourais servrar för att få tillgång till Bitcoin Blockchain information och för att sända transaktioner. I och med att dessa servrar har beslagtagits kan appen inte längre komma åt dessa data.

Om du inte hade en ansluten Dojo tidigare men har en nu kan du ställa in den så att den använder din Samourai-app igen. Detta innebär att du kontrollerar dina säkerhetskopior, raderar Wallet (Wallet, inte applikationen) och återställer Wallet genom att ansluta din Dojo till applikationen. För mer information om dessa steg kan du läsa [denna handledning, i avsnittet "_Preparing your Samourai Wallet_" : CoinJoin - DOJO](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

Om din Samourai-app redan var ansluten till din egen Dojo, fungerar Wallet-delen perfekt för dig. Du kan fortfarande se ditt saldo och sända transaktioner. Trots allt som händer tycker jag att Samourai Wallet fortfarande är den bästa mobila Wallet-programvaran för tillfället. Personligen planerar jag att fortsätta använda den.


Det största problemet du kan stöta på är otillgängligheten för Whirlpool-konton från appen. Vanligtvis försöker Samourai upprätta en anslutning till din Whirlpool CLI och starta CoinJoin-cyklerna innan du får tillgång till dessa konton. Men eftersom den här anslutningen inte längre är möjlig fortsätter appen att söka på obestämd tid utan att någonsin ge dig tillgång till Whirlpool-kontona. I det här fallet kan du återställa dessa konton på en annan Wallet-programvara medan du bara behåller insättningskontot på Samourai.


### Vilka verktyg finns fortfarande tillgängliga på Samourai?


Å andra sidan är vissa verktyg antingen påverkade av serverns avstängning eller helt otillgängliga.


När det gäller enskilda utgiftsverktyg fungerar allt normalt förutsatt, naturligtvis, att du har din egen Dojo. Normala Stonewall-transaktioner (och inte Stonewall x2) fungerar utan problem.


Kommentarer på Twitter har lyft fram att den integritet som en Stonewall-transaktion erbjuder nu kan komma att minska. Mervärdet av en Stonewall-transaktion ligger i det faktum att den inte går att skilja från en Stonewall x2-transaktion när det gäller struktur. När en analytiker stöter på detta specifika mönster kan han eller hon inte avgöra om det rör sig om en vanlig Stonewall med en enda användare eller en Stonewall x2 med två användare. Som vi kommer att se i de följande styckena har det dock blivit mer komplicerat att genomföra Stonewall x2-transaktioner på grund av att Soroban inte längre är tillgängligt. Vissa anser därför att en analytiker nu kan anta att varje transaktion med denna struktur är en normal Stonewall. Personligen delar jag inte detta antagande. Även om Stonewall x2-transaktioner kan vara mindre frekventa (och jag tror att de var det redan före denna incident), kan det faktum att de fortfarande är möjliga ogiltigförklara en hel analys baserad på antagandet att de inte är det.

**[-> Läs mer om Stonewall-transaktioner](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

När det gäller Ricochet har jag inte kunnat verifiera om tjänsten fortfarande är i drift, på grund av att jag inte äger en Dojo på Testnet, och jag föredrar att inte riskera att spendera 100 000 Sats` på en Wallet som kan kontrolleras av myndigheterna. Om du har haft möjlighet att testa det här verktyget nyligen, inbjuder jag dig att kontakta mig så att vi kan uppdatera den här artikeln.


Om du behöver använda Ricochet ska du vara medveten om att du alltid kan utföra denna operation manuellt med vilken Wallet-programvara som helst. För att lära dig hur du manuellt utför de olika hoppen korrekt rekommenderar jag att du konsulterar den här andra artikeln: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


JoinBot-verktyget är inte längre i drift, eftersom det var helt beroende av att en Wallet som administrerades av Samourai deltog.


När det gäller andra typer av samarbetstransaktioner, som ofta kallas "cahoots", är de fortfarande möjliga, men endast manuellt. Innan servern stängdes av hade du två alternativ för att utföra Stonewall x2- eller Stowaway (PayJoin)-transaktioner:



- Använd Soroban-nätverket för att automatiskt och fjärrstyrt Exchange PSBT:erna;
- Eller utför dessa utbyten manuellt genom att skanna flera QR-koder.


Efter flera tester verkar det som om Soroban inte längre fungerar. För att utföra dessa samarbetstransaktioner måste Exchange av data därför göras manuellt. Här är två alternativ för att utföra denna Exchange:



- Om du befinner dig fysiskt nära din medarbetare kan du skanna QR-koderna successivt;
- Om du befinner dig långt från din medarbetare kan du Exchange PSBT:erna via en extern kommunikationskanal till applikationen. Var dock försiktig eftersom uppgifterna i dessa PSBT:er är känsliga ur integritetssynpunkt. Jag rekommenderar att du använder en krypterad meddelandetjänst för att säkerställa sekretessen för Exchange.


**[-> Läs mer om Stonewall x2 transaktioner.](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Läs mer om Stowaway-transaktioner](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


När det gäller Whirlpool verkar protokollet inte längre fungera, inte ens för användare som har sin egen Dojo. Jag har övervakat min RoninDojo de senaste dagarna och försökt med några grundläggande manipuleringar, men Whirlpool CLI har inte kunnat ansluta sedan servern stängdes av.


Jag är dock fortfarande hoppfull om att detta protokoll kan återaktiveras eller kanske omformuleras på ett annat sätt under de kommande veckorna, beroende på hur situationen utvecklas. Denna paus skulle kunna vara ett tillfälle att utforska nya tillvägagångssätt eller potentiella förbättringar av detta system.


### Vilka externa verktyg finns fortfarande tillgängliga?


När det gäller andra verktyg som är relaterade till Samourai-miljön är vissa fortfarande tillgängliga medan andra inte är det.


Den kostnadsfria webbplatsen för kedjeanalys OXT.me är tyvärr inte längre tillgänglig för närvarande.


Whirlpool Stats Tool är inte längre tillgängligt för nedladdning, eftersom det fanns på Samourais GitLab. Även om du tidigare hade laddat ner detta Python-verktyg lokalt på din maskin, eller om det var installerat på din RoninDojo-nod, kommer WST inte att fungera för tillfället. Det var faktiskt beroende av data från OXT.me för sin funktion, och den här webbplatsen är inte längre tillgänglig. För närvarande är WST inte särskilt användbart eftersom Whirlpool-protokollet är inaktivt.


Webbplatsen KYCP.org är för närvarande inte längre tillgänglig.


Det GitLab som innehöll koden för Python-verktyget Boltzmann Calculator har också beslagtagits. För närvarande är det därför inte längre möjligt att ladda ner detta verktyg. Men om du har en RoninDojo kan du fortsätta att använda Boltzmann Calculator på samma sätt som tidigare.


När det gäller RoninDojo fortsätter denna node-in-box-programvara att fungera korrekt trots att vissa specifika verktyg som Whirlpool, CLI och WST inte är tillgängliga. Den kan fortfarande användas för annan Wallet-programvara tack vare Fulcrum eller Electrs. Om du vill få mer information om RoninDojo eller om du har specifika frågor, uppmuntrar jag dig att gå med i [deras Telegram-grupp] (https://t.me/RoninDojoNode).


Källkoden för RoninDojo är dock för närvarande inte längre tillgänglig, eftersom den fanns på Samourais GitLab. Det är därför inte möjligt att manuellt installera den på en Raspberry Pi för tillfället.


När det gäller Watch-only wallet-programvaran Sentinel är situationen liknande den för Samourai-appen. Om du har en egen Dojo kan du fortsätta att använda Sentinel utan problem. Men om du inte har någon Dojo kommer du inte längre att kunna upprätta en anslutning. Till skillnad från Samourai är Sentinels webbplats fortfarande tillgänglig online. Men var försiktig med den här webbplatsen och APK som erbjuds där, eftersom det är oklart vem som för närvarande kontrollerar dessa resurser.


### Är Sparrow wallet påverkad?


Sparrow wallet fortsätter att fungera normalt, med undantag för Samourai-verktyg som inte längre är tillgängliga. För närvarande är det inte längre möjligt att utföra coinjoins via Sparrow. På samma sätt är verktyg för gemensamma utgifter inte längre tillgängliga, eftersom Sparrow inte erbjuder möjligheten till manuell Exchange av PSBT, till skillnad från Samourai. För alla andra funktioner fungerar Sparrow utan problem. Du kan också använda den här programvaran för att återställa en Samourai Wallet om det behövs.


## Hur återställer man en Samourai Wallet?


Som vi har sett i de tidigare avsnitten, om du äger din egen Dojo, är det inte nödvändigtvis nödvändigt att byta programvara. **Samourai är fortfarande ett utmärkt val av Hot Wallet** för dina dagliga utgifter. Men om du inte har en Dojo eller om du föredrar att välja en annan programvara kommer jag att förklara hela återställningsprocessen och beskriva alla potentiella hinder du kan stöta på.


I vilket fall som helst är det viktigt att ta god tid på sig och se till att inte göra några misstag. Kom ihåg att det inte är någon brådska, eftersom du har dina privata nycklar, och beslagtagandet av Samourais servrar påverkar inte detta på något sätt. Vad som än händer kan de uppenbarligen inte komma åt dina privata nycklar.


### Verifiera passphrase


För att återställa din Wallet måste du ha din passphrase, även om du väljer att återställa via backupfilen. Börja med att verifiera giltigheten av denna passphrase. Öppna din Samourai Wallet-app, klicka på din Paynym-ikon längst upp till vänster och välj sedan `Inställningar`.


![samourai](assets/1.webp)


Klicka sedan på `Felsökning` och sedan på `passphrase/backup test`.


![samourai](assets/2.webp)


Ange din passphrase och klicka på `Ok`. Om det är korrekt kommer Samurai att bekräfta det. Du har också möjlighet att verifiera backup-filen om du planerar att använda den senare.


![samourai](assets/3.webp)


Detta steg är valfritt men rekommenderas. Det bekräftar att passphrase är korrekt, vilket eliminerar en potentiell källa till problem senare. Om Samourai i det här skedet anger att passphrase är felaktig är det inte möjligt att återhämta sig. Kontrollera att du har angett passphrase korrekt och kontrollera det igen.


### Alternativ 1: Återställ Wallet på Sparrow med backup-filen


Sedan version 1.8.6 av Sparrow wallet är det möjligt att direkt importera din Samourai Wallet med hjälp av den säkerhetskopierade textfilen med namnet `samourai.txt`, som ditt program automatiskt genererar. Denna fil innehåller all nödvändig information för att återställa din Wallet och är krypterad med din passphrase för säkerhets skull.


Om du väljer det här alternativet behöver du din uppdaterade `samourai.txt`-fil och din passphrase. För att generate denna fil på Samourai Wallet, klicka på de tre små prickarna längst upp till höger och välj sedan `Export Wallet backup`.


![samourai](assets/4.webp)

Välj sedan `Exportera till urklipp`. Därefter måste du överföra den här filen till din dator på ett säkert sätt. Eftersom filen är krypterad, men passphrase ensam räcker för att dekryptera den, är det viktigt att vidta försiktighetsåtgärder under överföringen. Om du väljer att överföra filen direkt i klartext måste du skapa filen "samourai.txt" på din dator och klistra in innehållet i urklippet i den. Ett alternativ skulle vara att direkt hämta filen `samourai.txt` från filerna som lagras på din telefon.

När du har tillgång till filen på din dator öppnar du Sparrow wallet, klickar på fliken `Fil` och väljer `Importera Wallet` för att börja importera din Wallet.


![samourai](assets/5.webp)


Bläddra ner till `Samourai Backup`, klicka på `Import File` och välj sedan din `samourai.txt`-fil.


![samourai](assets/6.webp)


Sparrow kommer sedan att be dig om ett lösenord för att dekryptera filen. Detta lösenord är faktiskt din passphrase. Ange det i motsvarande fält och klicka på `Importera`.


![samourai](assets/7.webp)


Om din Wallet inte visas i det här skedet är det möjligt att du gjorde ett misstag när du kopierade filen `samourai.txt` eller när du angav passphrase. Du kan konsultera felsökningsavsnittet för mer hjälp.


![samourai](assets/8.webp)


För skripttypen, om du inte har konfigurerat andra skript i Samourai, bör du normalt bara använda SegWit V0 (Native SegWit / P2WPKH). Behåll detta standardskript och klicka på `Importera`.


![samourai](assets/9.webp)


Namnge din Wallet, till exempel "Samourai Recovery", och klicka sedan på `Create Wallet`.


![samourai](assets/10.webp)


Sparrow kommer sedan att be dig välja ett lösenord. Detta lösenord skyddar endast åtkomsten till din Wallet på den här datorn och gäller inte härledningen av din Wallet:s nycklar. Se till att välja ett starkt lösenord, anteckna det så att du kommer ihåg det och klicka på "Set Password".


![samourai](assets/11.webp)


Sparrow kommer sedan att härleda nycklarna till din Wallet och söka efter motsvarande transaktioner.


![samourai](assets/12.webp)


För närvarande är det bara ditt insättningskonto som är tillgängligt. Om du bara använde Samourai för detta konto bör du se alla dina medel. Men om du också använde Whirlpool måste du härleda kontona `premix`, `postmix` och `badbank`. På Sparrow klickar du helt enkelt på fliken `Inställningar` och sedan på `Lägg till konton...`.


![samourai](assets/13.webp)

I fönstret som öppnas väljer du `Whirlpool Accounts` i rullgardinsmenyn och klickar sedan på `OK`.

![samourai](assets/14.webp)


Du kommer då att se dina olika Whirlpool-konton visas, och Sparrow kommer att härleda de nödvändiga nycklarna för att använda de associerade bitcoins.


![samourai](assets/15.webp)


Om du använder en annan programvara än Sparrow, som Electrum, för att återställa din Samourai Wallet, här är Whirlpool-kontoindexen för manuell återställning:



- Insättning: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Du har nu tillgång till dina bitcoins på Sparrow. Om du behöver hjälp med att använda Sparrow wallet kan du också kolla in [vår dedikerade handledning] (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Jag rekommenderar också att du manuellt importerar de etiketter som du hade associerade med dina UTXO:er på Samourai. Detta gör att du kan utföra effektiv myntkontroll på Sparrow därefter.


### Alternativ 2: Återställ Wallet på Sparrow med Mnemonic-fras


Om du inte vill utföra återställningen med backup-filen kan du välja en mer traditionell metod genom att helt enkelt använda din 12-ords återställningsfras och din passphrase. Detta andra alternativ är ofta enklare.


För att börja, se till att du har din återställningsfras och din passphrase till hands. Öppna sedan programvaran Sparrow wallet, klicka på fliken `File` och välj `Import Wallet` för att börja importera din Wallet.


![samourai](assets/16.webp)


Välj `Mnemonic Words (BIP39)` och klicka på `Use 12 Words` i rullgardinsmenyn.


![samourai](assets/17.webp)


Ange de 12 orden i din återhämtningsfras i rätt ordning.


![samourai](assets/18.webp)


Om Sparrow visar meddelandet "Ogiltig kontrollsumma" innebär det att kontrollsumman för återställningsfrasen inte är giltig, vilket förmodligen innebär att du gjorde ett misstag när du skrev in orden.


![samourai](assets/19.webp)


Om din fras är korrekt, kryssa i rutan `Use passphrase?` och ange din passphrase i det dedikerade fältet. Slutligen, om allt verkar korrekt, klicka på knappen `Discover Wallet`.


![samourai](assets/20.webp)


Namnge din Wallet, till exempel "Samourai Recovery", och klicka sedan på `Create Wallet`.


![samourai](assets/21.webp)

Sparrow kommer sedan att be dig att välja ett lösenord. Detta lösenord skyddar endast åtkomsten till din Wallet på den här datorn och har inget att göra med hur du får fram nycklarna till din Wallet. Se till att välja ett starkt lösenord, skriv ner det så att du kommer ihåg det och klicka på "Ange lösenord".

![samourai](assets/22.webp)


Sparrow kommer sedan att härleda nycklarna till din Wallet och söka efter motsvarande transaktioner.


![samourai](assets/23.webp)


Om din Wallet inte visas i det här skedet är det möjligt att du gjorde ett misstag när du angav passphrase eller återställningsfrasen. Du kan konsultera det särskilda felsökningsavsnittet för mer hjälp.


För närvarande är det bara ditt insättningskonto som är tillgängligt. Om du bara använde Samourai för detta konto bör du se alla dina medel. Men om du också använde Whirlpool måste du härleda kontona `premix`, `postmix` och `badbank`. I Sparrow klickar du helt enkelt på fliken `Inställningar` och sedan på `Lägg till konton...`.


![samourai](assets/24.webp)


I fönstret som öppnas väljer du `Whirlpool Accounts` i rullgardinsmenyn och klickar sedan på `OK`.


![samourai](assets/25.webp)


Du kommer då att se dina olika Whirlpool-konton visas, och Sparrow kommer att härleda de nödvändiga nycklarna för att använda de associerade bitcoins.


![samourai](assets/26.webp)


Om du använder en annan programvara som Electrum för att återställa din Samourai Wallet, här är Whirlpool-kontoindexen för manuell återställning:



- Insättning: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Du har nu tillgång till dina bitcoins på Sparrow. Om du behöver hjälp med att använda Sparrow wallet kan du också läsa [vår dedikerade handledning] (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Jag rekommenderar också att du manuellt importerar de etiketter som du hade associerade med dina UTXO:er på Samourai. Detta gör att du kan utföra effektiv myntkontroll på Sparrow därefter.


### Vilka är de vanligaste problemen som uppstår?


Efter att ha hjälpt flera personer under de senaste dagarna tror jag att jag har stött på de flesta av de problem som kan förhindra återställning av din Wallet. Om du fortfarande inte kan komma åt din Wallet trots de tidigare handledningarna, här är några ytterligare rekommendationer.

Först och främst är det absolut nödvändigt att återställningsfrasen är korrekt för att återställningen ska fungera. Om du inte kan hitta din 12-ordsfras kan du använda _alternativ 1_ för att återställa från Samourais säkerhetskopieringsfil. Du kan också komma åt din återställningsfras direkt i Samourai Wallet genom att navigera till `Inställningar`, sedan `Wallet` och slutligen välja `Visa 12-ords återställningsfras`.


Därefter kommer ett skrivfel i din passphrase under återställningen att resultera i felaktiga härledda nycklar, vilket förhindrar återställning av din Wallet på Sparrow. **passphrase måste vara helt korrekt!**


För att lösa detta råder jag dig först att kontrollera giltigheten för din passphrase i Samourai-programmet enligt beskrivningen i avsnittet "_Verifiera lösenfrasen_" i den här artikeln:


1. **Validering i Samourai:** Om Samourai bekräftar att passphrase är korrekt, försök återställningen igen från början och se till att ange passphrase korrekt i Sparrow utan fel;

2. **passphrase Error:** Om Samourai indikerar att passphrase är felaktig är det meningslöst att fortsätta försöken med Sparrow. Så länge den korrekta passphrase inte hittas är det omöjligt att återfå din Wallet. Om du har förlorat din passphrase permanent ska du förvara din Samourai-applikation säkert. Allt du kan göra är att hoppas att servrarna startas om så att du kan göra utlägg direkt från programmet utan att behöva återskapa det. **Försök inte ansluta en Dojo i det här fallet**, eftersom det skulle innebära att du återställer din Wallet på Samourai, vilket kräver tillgång till passphrase.


Bland andra fel som uppstått är många relaterade till nätverkskonfigurationen på Sparrow.


Kontrollera först att Sparrow är korrekt konfigurerad i läget `Mainnet` snarare än i läget `Testnet`. Om Sparrow söker efter dina transaktioner på Testnet kommer den inte att hitta något, eftersom din Wallet finns på Mainnet. Testnet är en alternativ version av Bitcoin, som endast används för testning och utveckling, och fungerar på ett separat nätverk från huvudnätverket (Mainnet), med egna block och transaktioner. För att kontrollera vilket nätverk du befinner dig på, klicka på fliken `Tools` och sedan på `Restart In`. Om alternativet `Mainnet` visas befinner du dig inte i huvudnätverket. Välj det för att starta om Sparrow på Mainnet och börja sedan din återställningsprocess igen.


![samourai](assets/27.webp)

Vissa har också stött på svårigheter med att ansluta Sparrow till sin nod. Längst ner till höger på Sparrow finns en färgad brytare som visar om din programvara är korrekt ansluten till en Bitcoin-nod. För att hämta dina Samourai-transaktioner är det viktigt att programvaran är väl ansluten. Kontrollera att omkopplaren är aktiverad, som i min bild nedan (gul för en offentlig nod, Green för Bitcoin Core och blå för en Electrum-server).

![samourai](assets/28.webp)


Om omkopplaren inte är aktiverad, klicka på den för att återaktivera anslutningen.


![samourai](assets/29.webp)


Om problemet kvarstår finns här några möjliga lösningar:



- Om du försöker ansluta till din egen Electrum-server (blå) eller om din Bitcoin Core (Green) och Sparrow inte kan ansluta, kontrollera anslutningsinformationen under `File > Preferences... > Server`;


![samourai](assets/30.webp)



- Om anslutningsproblemet kvarstår kan det bero på en ofullständig synkronisering av din nod. Se till att din nod och din indexerare är 100% synkroniserade. Om det behövs som en sista utväg, koppla bort din nod från Sparrow och anslut till en publik nod;
- Om du redan var ansluten till en publik nod och anslutningen misslyckas kan du försöka byta nod genom att välja en annan i rullgardinsmenyn.


![samourai](assets/31.webp)


Om du har lyckats återställa din Wallet, men den verkar ofullständig, kan det finnas ett problem relaterat till härledning.


Ett problem kunde uppstå om du använde ditt Samourai-insättningskonto med en annan skripttyp än `P2WPKH`. Som standard använder Samourai den här skripttypen, men om du har ändrat den manuellt måste du också justera den när du återställer på Sparrow.


För att härleda grenar för andra skripttyper måste du upprepa återställningsprocessen för varje skripttyp som används. För detta går du till `Fil > Ny Wallet` på Sparrow, väljer en annan skripttyp i rullgardinsmenyn, klickar på `Ny eller importerad Software Wallet` och följer samma steg som i den inledande handledningen.


![samourai](assets/32.webp)


Ett annat problem jag stött på när det gäller härledning är relaterat till värdet Gap Limit. Detta värde talar om för Sparrow efter hur många tomma adresser den ska sluta härleda nya adresser. Om du efter återställning märker att vissa transaktioner saknas kan detta bero på en för låg Gap Limit. För att lösa detta går du till det konto som orsakar problemet, t.ex. postmix-kontot (om flera konton berörs upprepar du denna åtgärd för varje konto).


![samourai](assets/33.webp)


Klicka på fliken `Inställningar` och sedan på knappen `Avancerat...`.

![samourai](assets/34.webp)

Öka gradvis värdet på Gap Limit, till exempel ställer jag in det till `400` här. Klicka sedan på knappen `Close`.


![samourai](assets/35.webp)


Klicka på `Apply` för att slutföra. Sparrow kommer sedan att härleda ett större antal adresser och söka efter medel på dem, vilket bör hjälpa till att återställa alla dina transaktioner.


![samourai](assets/36.webp)


Det täcker de olika återhämtningsproblem som jag har stött på under de senaste dagarna. Om du fortfarande har problem efter att ha provat alla dessa lösningar, inbjuder jag dig att gå med i [Discover Bitcoin Discord] (https://discord.gg/xKKm29XGBb) för att be om hjälp. Jag besöker regelbundet denna Discord och skulle vara glad att hjälpa till om jag har lösningen. Andra bitcoiners kommer också att kunna dela med sig av sina erfarenheter och erbjuda sin hjälp. **I vilket fall som helst är det viktigt att hålla din återställningsfras, din backup-fil och dina passphrase konfidentiella**. Dela dem inte med någon, eftersom det skulle kunna göra det möjligt för dem att stjäla dina bitcoins.


När återställningen är klar har du nu tillgång till dina bitcoins. Det är bra, men det kanske inte är tillräckligt. Beslagtagandet av servrar innebär nämligen nya potentiella risker för din integritet. I följande avsnitt kommer vi att undersöka dessa risker i detalj och beskriva de försiktighetsåtgärder som du kan vidta för att skydda din integritet.


## Vilka konsekvenser får det för integriteten i dina transaktioner?


### Som Samourai-användare utan Dojo


Om du använde Samourai Wallet utan att ha anslutit din egen Dojo, var dina xpubar tvungna att kommuniceras till Samourais servrar för att appen skulle fungera. I och med beslagtagandet av dessa servrar är det möjligt att myndigheter nu har tillgång till dessa xpubar.


Detta scenario förblir hypotetiskt. Vi vet inte om dessa xpubar spelades in, om eventuell lagring förstördes, om myndigheterna har återfunnit dem och om de planerar att använda dem för kedjeanalys. I en sådan situation är det dock klokt att överväga det värsta tänkbara scenariot, där myndigheterna har xpubar från användare som inte anslöt sin egen Dojo.

Som referens är en xpub en teckensträng som innehåller alla nödvändiga Elements för att generera underordnade publika nycklar (publik nyckel + chain code). Den används i hierarkiska deterministiska plånböcker för att generate ta emot adresser och observera transaktioner för ett konto utan att exponera de tillhörande privata nycklarna. Detta möjliggör till exempel skapandet av en "watch-only" Wallet. Att avslöja xpubar kan dock äventyra användarens integritet, eftersom de gör det möjligt för tredje part att spåra transaktioner och se saldon på associerade konton.

Den som känner till dina xpubar kan alltså se alla mottagningsadresser för din Wallet, de som använts tidigare och de som kommer att genereras i framtiden.


För användare som inte har en Dojo får en potentiell läcka av dina xpubs två stora konsekvenser:



- De coinjoins som du kan ha utfört görs ineffektiva ur integritetssynpunkt för alla som känner till dina xpubs, vilket innebär att dina mynt förlorar all anonset;
- Denna person kan också spåra alla mottagningsadresser för din Samourai Wallet.


Det är därför viktigt att överväga det värsta tänkbara scenariot och göra sig av med denna Wallet, som kan vara integritetskränkande. För att göra detta, skapa en ny Wallet från grunden med en annan programvara, som Sparrow wallet. Efter att ha verifierat giltigheten av dina säkerhetskopior överför du alla dina medel genom att göra transaktioner. Även om denna operation inte bryter spårbarhetslänken för dina mynt, kommer den att förhindra att myndigheterna med säkerhet känner till adresserna till din nya Wallet.


Under denna överföring rekommenderar jag att du undviker konsolidering av dina mynt. Om vi antar att dina xpubar är komprometterade kommer konsolideringen inte att ha någon inverkan ur synvinkeln för den person som har tillgång till dessa xpubar, eftersom din integritet redan är komprometterad med dem. Jag råder dig dock att inte konsolidera dina mynt för mycket, främst för att skydda din integritet från andra människor. I värsta fall kan det vara så att endast myndigheterna har tillgång till dina xpubar, men resten av världen känner inte till dem. Ur andras synvinkel kan konsolidering av dina mynt således skada din integritet avsevärt på grund av Common Input Ownership Heuristic (CIOH).


**För att definitivt bryta spårningen kan du också överväga att utföra coinjoins från denna nya Wallet.**

** Varning:** Att bara hämta din Samourai Wallet på Sparrow wallet räcker inte. Det är nödvändigt att skapa en helt ny Wallet med en ny återställningsfras om du vill undvika att använda xpubar som kan ha läckt. Om du importerar din befintliga seed till Sparrow ändrar du bara Wallet:s hanteringsprogramvara, men Wallet förblir densamma.


### Som användare av Sparrow eller Samourai med Dojo


Om din Wallet endast hanteras på Sparrow wallet kan dina xpubar inte ha läckt ut, oavsett om du använder en offentlig nod eller din egen Bitcoin-nod. På samma sätt, om du använder Samourai-appen och alltid har anslutit den här appen till din egen Dojo sedan skapandet av din Wallet, är dina xpubar också säkra.


Men om du har använt samma Wallet under en period **utan din egen Dojo** och sedan med din egen Dojo, är det möjligt att Samourai-servrarna kan ha haft tillgång till dina xpubar, och därför kan myndigheterna känna till dem. Om du befinner dig i denna specifika situation råder jag dig att följa rekommendationerna i föregående avsnitt och betrakta dina xpubar som komprometterade.


För dem som alltid har använt Sparrow eller Samourai med sin egen Dojo är den största risken att anonsets av dina mynt potentiellt kan minskas. Anta, i värsta fall, att alla användare utan en Dojo har sina xpubar i myndigheternas händer, då skulle deras mynts väg genom CoinJoin-cyklerna kunna spåras av dessa myndigheter.


Låt oss ta ett konkret exempel för att illustrera detta. Föreställ dig att du deltog i en första cykel av CoinJoin, följt av ytterligare två nedströms CoinJoin-cykler. Om xpubarna för användare utan en Dojo inte har läckt ut, skulle den potentiella anonset för ditt mynt vara 13.


![samourai](assets/37.webp)


Om vi emellertid anser att xpubarna har läckt ut och att du stötte på en användare utan dojo under den första CoinJoin, och sedan 2 under den första nedströms CoinJoin, skulle din potentiella anonset bara vara 10 istället för 13 ur myndighetens synvinkel.


![samourai](assets/38.webp)

Denna potentiella minskning av anonset är komplex att kvantifiera eftersom den beror på många faktorer och varje mynt påverkas olika. Till exempel påverkar en användare utan Dojo som påträffas i de tidiga cyklerna den potentiella anonset mycket mer än en som påträffas i de senare cyklerna. För att ge dig en uppfattning om situationen, som fortfarande är hypotetisk, visade den senaste statistiken från Samourai att mellan 85 och 90 procent av de mynt som var inblandade i coinjoins kom från användare med Dojo, Sparrow eller Bitcoin Keeper, det vill säga användare som inte ens i värsta fall skulle ha sett sina xpubar läcka ut.

Även om dessa siffror är svåra att verifiera tycker jag att de verkar stämma av två skäl:



- Sparrow wallet används i stor utsträckning;
- De flesta "node-in-box"-programvaror erbjuder Dojo-implementeringar, och dessa vanliga programvaror som Umbrel är mycket populära idag.


Det finns alltså flera aspekter som måste beaktas. Om dina mynts integritet gentemot myndigheterna är extremt viktigt för dig, skulle det vara klokt att förbereda sig för det värsta scenariot, och det är svårt att garantera 100% att dina Whirlpool CoinJoin cykler inte kunde spåras på grund av den potentiella läckan av xpubs från användare utan Dojo. Även om detta antagande är mycket osannolikt är det inte omöjligt.


Om å andra sidan integriteten för dina mynt gentemot den myndighet som eventuellt har tillgång till dessa xpub-filer inte är avgörande för dig, kan situationen betraktas på ett annat sätt.


Jag anger "gentemot myndigheten" eftersom det är viktigt att komma ihåg att endast den myndighet som beslagtog servrarna potentiellt är medveten om dessa xpubar. Om ditt mål med att använda CoinJoin var att förhindra din bagare från att kunna följa dina medel, är han inte bättre informerad än före serverbeslaget.


Slutligen är det viktigt att beakta den ursprungliga anonset för ditt mynt, före serverns beslagtagande. Låt oss ta exemplet med ett mynt som hade nått en prospektiv anonset på 40 000; den potentiella minskningen i denna anonset är förmodligen försumbar. Med en redan mycket hög basanonset är det faktiskt osannolikt att några få användare utan Dojo radikalt skulle kunna förändra situationen. Men om ditt mynt hade en anonset på 40 skulle denna potentiella läcka allvarligt kunna påverka dina anonsets och potentiellt möjliggöra spårning.

Eftersom WST-verktyget nu är ur drift efter nedläggningen av OXT.me kan du bara uppskatta dessa anonsets. För den retrospektiva anonset finns det inte så mycket att oroa sig för eftersom Whirlpool-modellen säkerställer att den är mycket hög från den första CoinJoin, tack vare arvet från dina kamrater. Det enda fallet där detta kan utgöra ett problem är om ditt mynt inte har blivit remixat på flera år och det mixades i början av en pools lansering. När det gäller den potentiella anonset kan du undersöka hur länge ditt mynt har varit tillgängligt för coinjoins. Om det har gått flera månader så har det förmodligen en extremt hög prospektiv anonset. Omvänt, om det lades till i en pool bara några timmar innan servrarna beslagtogs, så är dess prospektiva anonset förmodligen mycket lågt.

[**-> Lär dig mer om anonsets och deras beräkningsmetod.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


En annan aspekt att beakta är konsolideringens inverkan på anonsets av mynt som har blandats. Med tanke på att Whirlpool-konton inte längre är tillgängliga via Samourai-appen är det troligt att många användare har överfört sina Wallet till annan programvara och försökt ta ut sina medel från Whirlpool. I synnerhet förra helgen, när transaktionsavgifterna i Bitcoin-nätverket var relativt höga, fanns det ett starkt tekniskt och ekonomiskt incitament att konsolidera post-mix-mynt. Detta innebär att det är troligt att många användare har gjort betydande konsolideringar.


Problemet med dessa konsolideringar efter mixning är att de alltid minskar anonsets, inte bara för den användare som utför dem utan även för de användare som de mötte under sina CoinJoin-cykler. Även om jag inte har kunnat verifiera eller kvantifiera detta fenomen exakt, kan de ekonomiska incitamenten relaterade till transaktionsavgifter vid den tidpunkten leda oss till att anta att anonsets potentiellt är lägre.


### Som Sentinel-användare


Nätverksdriften för Watch-only wallet-applikationen Sentinel liknar den för Samourai. För att komma åt din Wallet-information måste applikationen överföra de xpubar, publika nycklar och adresser som du har angett till en Dojo. Om du alltid har använt din egen Dojo på Sentinel är det inget problem, och du kan fortsätta att använda applikationen utan bekymmer. Men om du var beroende av Samourais servrar för din Sentinel är det möjligt att dina xpubar har exponerats. I det här fallet är det lämpligt att följa samma Wallet-ändringsprocess som rekommenderas för Samourai Wallet när du är ansluten till Samourais servrar.


I den osannolika händelsen att du använde din Dojo med Samourai men inte med Sentinel, skulle det vara klokare att överväga att dina xpubar är komprometterade.


## Slutsats


Tack för att du läste den här artikeln till slutet. Om du tycker att information saknas eller om du har förslag, tveka inte att kontakta mig för att dela dina tankar. Dessutom, om du behöver ytterligare hjälp med att återställa din Samourai Wallet trots denna handledning, inbjuder jag dig att gå med i [Discover Bitcoin Discord] (https://discord.gg/xKKm29XGBb) för att be om hjälp. Jag besöker regelbundet denna Discord och skulle med glädje hjälpa dig om jag har lösningen. Andra bitcoiners kommer också att kunna dela med sig av sina erfarenheter och erbjuda sitt stöd. **I vilket fall som helst är det viktigt att hålla din återställningsfras, din backup-fil och din passphrase konfidentiella**. Dela dem inte med någon, eftersom det skulle kunna göra det möjligt för dem att stjäla dina bitcoins.