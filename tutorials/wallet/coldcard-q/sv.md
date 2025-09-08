---
name: COLDCARD Q
description: Konfigurera och använda ett COLDCARD Q
---
![cover](assets/cover.webp)


En Hardware Wallet är en elektronisk enhet som är avsedd att hantera och säkra de privata nycklarna för en Bitcoin Wallet. Till skillnad från mjukvaruplånböcker (eller Hot-plånböcker) som installeras på maskiner för allmänt bruk som ofta är anslutna till Internet, gör hårdvaruplånböcker det möjligt att fysiskt isolera privata nycklar, vilket minskar risken för piratkopiering och stöld.


Huvudsyftet med en Hardware Wallet är att minska enhetens funktionalitet så mycket som möjligt för att minimera dess attackyta. Mindre attackyta innebär också färre potentiella attackvektorer, dvs. färre svaga punkter i systemet som angripare kan utnyttja för att få tillgång till bitcoins.


Det är tillrådligt att använda en Hardware Wallet för att säkra dina bitcoins, särskilt om du har stora mängder, antingen i absolut värde eller som en andel av dina totala tillgångar.


Hårdvaruplånböcker används tillsammans med Wallet-hanteringsprogram på en dator eller smartphone. Den senare hanterar skapandet av transaktioner, men den kryptografiska signatur som krävs för att göra dessa transaktioner giltiga utförs enbart inom Hardware Wallet. Detta innebär att privata nycklar aldrig exponeras för en potentiellt sårbar miljö.


Hårdvaruplånböcker erbjuder dubbelt skydd för användaren: å ena sidan skyddar de dina bitcoins mot fjärråttacker genom att hålla de privata nycklarna offline, och å andra sidan erbjuder de i allmänhet större fysiskt motstånd mot försök att extrahera nycklarna. Och det är just på dessa två säkerhetskriterier som vi kan bedöma och klassificera de olika modellerna på marknaden.


I den här handledningen vill jag presentera en sådan lösning: **COLDCARD Q**.


---
Eftersom COLDCARD Q erbjuder en mängd olika funktioner, föreslår jag att vi delar upp användningen i 2 handledningar. I den första handledningen går vi igenom den första konfigurationen och enhetens grundläggande funktioner. I en andra handledning går vi sedan igenom hur du kan utnyttja alla avancerade alternativ på COLDCARD.


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Vi presenterar COLDCARD Q


COLDCARD Q är en Hardware Wallet för enbart Bitcoin som utvecklats av det kanadensiska företaget Coinkite, känt för sina tidigare MK-modeller. Q representerar deras mest avancerade produkt hittills och är positionerad som den ultimata Bitcoin Hardware Wallet.


När det gäller hårdvara är COLDCARD Q utrustad med alla funktioner som krävs för en optimal användarupplevelse:




- En stor LCD-display förenklar navigering och användning;
- Ett komplett QWERTY-tangentbord;
- Integrerad kamera för skanning av QR-koder;
- Två microSD-kortplatser ;
- Ett helt isolerat strömalternativ via tre AAA-batterier (ingår ej) eller via en USB-C-kabel ;
- Två Secure Elements från två olika tillverkare för ökad säkerhet;
- Möjlighet att kommunicera via NFC.


Enligt min mening har COLDCARD Q bara två nackdelar. För det första är den på grund av sina många funktioner ganska skrymmande och mäter nästan 13 cm i längd och 8 cm i bredd, vilket nästan är storleken på en liten smartphone. Den är också ganska tjock på grund av batterifacket. Om du letar efter en mindre, mer mobil Hardware Wallet kan den mycket mer kompakta MK4 vara ett bättre alternativ. Den andra nackdelen är uppenbarligen kostnaden för enheten, som är prissatt till ** $ 239,99 ** på den officiella webbplatsen, dvs $ 72 mer än MK4, vilket sätter Q i direkt konkurrens med premium hårdvaruplånböcker som Ledger Flex eller Foundation's Passport.


![CCQ](assets/fr/001.webp)


På mjukvarusidan är COLDCARD Q lika välutrustad som Coinkites andra enheter, med en mängd avancerade funktioner:




- Tärningsslag för att generate din egen återhämtningsfras ;
- PIN-kod ;
- Nedräkning till slutgiltigt PIN-lås;
- BIP39 passphrase ;
- Slutlig låsning PIN ;
- Nedräkning av anslutning ;
- SeedXOR;
- BIP85...


Kort sagt, COLDCARD Q erbjuder en förbättrad användarupplevelse jämfört med MK4 och kan vara idealisk för mellanliggande till avancerade användare som vill ha större användarvänlighet.


COLDCARD Q finns till försäljning [på Coinkites officiella webbplats] (https://store.coinkite.com/store/coldcard). Det kan också köpas från en återförsäljare.


## Förbereda handledningen


När du har fått ditt COLDCARD är det första steget att inspektera förpackningen för att säkerställa att den inte har öppnats. Om förpackningen är skadad kan detta tyda på att Hardware Wallet har äventyrats och kanske inte är äkta.


![CCQ](assets/fr/002.webp)


När du öppnar lådan bör du hitta följande föremål:




- COLDCARD Q i en försluten påse;
- Ett kort för att registrera din Mnemonic-fras.


![CCQ](assets/fr/003.webp)


Se till att påsen inte har öppnats eller skadats. Kontrollera också att numret på din påse stämmer överens med numret på papperet i påsen. Spara detta nummer för framtida bruk.


![CCQ](assets/fr/004.webp)


Om du föredrar att driva ditt COLDCARD utan att ansluta det till en dator (luftgap), sätter du i tre AAA-batterier på baksidan av enheten. Alternativt kan du ansluta den till din dator via en USB-C-kabel.


![CCQ](assets/fr/005.webp)


För denna handledning behöver du också Sparrow wallet för att hantera dina Bitcoin Wallet på din dator. Ladda ner [Sparrow wallet](https://sparrowwallet.com/download/) från den officiella webbplatsen. Jag rekommenderar starkt att du kontrollerar både dess äkthet (med GnuPG) och integritet (via Hash) innan du fortsätter med installationen. Om du inte vet hur du gör det kan du följa den här handledningen:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Val av PIN-kod


Du kan nu sätta på ditt COLDCARD genom att trycka på knappen uppe i vänstra hörnet.


![CCQ](assets/fr/006.webp)


Tryck på knappen "*ENTER*" för att godkänna användarvillkoren.


![CCQ](assets/fr/007.webp)


Ditt COLDCARD Q visar då ett nummer längst upp på skärmen. Kontrollera att numret stämmer överens med det som finns på den förseglade påsen och på plastbiten inuti påsen. Detta säkerställer att ditt paket inte har öppnats mellan den tidpunkt då det packades av Coinkite och den tidpunkt då du öppnade det. Tryck på "*ENTER*" för att fortsätta.


![CCQ](assets/fr/008.webp)


Navigera till menyn "*Välj PIN-kod*" och bekräfta med knappen "*ENTER*".


![CCQ](assets/fr/009.webp)


Denna PIN-kod används för att låsa upp ditt COLDCARD. Den utgör därför ett skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även utan tillgång till denna PIN-kod kommer innehav av din Mnemonic-fras att göra det möjligt för dig att återfå tillgång till dina bitcoins.


PIN-koder för COLDCARD är uppdelade i två delar: ett prefix och ett suffix, som var och en kan innehålla mellan 2 och 6 siffror, totalt 4 till 12 siffror. När du låser upp ditt COLDCARD måste du först ange prefixet, varefter enheten visar dig 2 ord. Ange sedan suffixet. Dessa två ord får du under detta konfigurationssteg och du bör spara dem noggrant eftersom du behöver dem varje gång du låser upp ditt COLDCARD. Om de två ord som visas vid upplåsningen stämmer överens med dem som du sparade under konfigurationen, bekräftar detta att din enhet inte har äventyrats sedan den senast användes.


Klicka igen på "*Välj PIN-kod*"


![CCQ](assets/fr/010.webp)


Bekräfta att du har läst varningarna.


![CCQ](assets/fr/011.webp)


Du ska nu välja din PIN-kod. Vi rekommenderar en lång, slumpmässig PIN-kod. Se till att du förvarar denna kod på en annan plats än där ditt COLDCARD förvaras. Du kan använda det kort som medföljer i ditt paket för att registrera koden.


Ange önskat prefix och tryck sedan på knappen "*ENTER*" för att bekräfta den första delen av PIN-koden.


![CCQ](assets/fr/012.webp)


De två anti-phishing-orden kommer sedan att visas på din skärm. Spara dem noggrant för framtida referens. Du kan använda kortet som ingår i ditt paket för att skriva ner dem.


![CCQ](assets/fr/013.webp)


Ange sedan den andra delen av din PIN-kod och tryck på "*ENTER*".


![CCQ](assets/fr/014.webp)


Bekräfta din PIN-kod genom att ange den en andra gång och kontrollera att de två anti-phishing-orden överensstämmer med dem du sparade tidigare.


![CCQ](assets/fr/015.webp)


Från och med nu, varje gång du låser upp ditt COLDCARD, kom ihåg att kontrollera giltigheten av de två anti-phishing-orden som visas på skärmen efter att du har angett ditt PIN-kodprefix.


## Uppdatering av firmware


När du använder din enhet för första gången är det viktigt att kontrollera och uppdatera den fasta programvaran. Detta gör du genom att gå till menyn "*Avancerat/Tools*".


![CCQ](assets/fr/016.webp)


**Viktigt:** Om du planerar att uppgradera din firmware och det inte är första gången du använder COLDCARD (dvs. du har redan en Wallet skapad på COLDCARD), se till att du har din Mnemonic-fras och att den är funktionell (liksom den valfria passphrase, om tillämpligt). Detta är viktigt för att undvika att förlora dina bitcoins i händelse av ett problem under enhetsuppdateringen.


Välj "*Uppgradera firmware*".


![CCQ](assets/fr/017.webp)


Välj "*Visa version*".


![CCQ](assets/fr/018.webp)


Du kan kontrollera den aktuella firmware-versionen på ditt COLDCARD. I mitt fall är versionen till exempel "*1.2.3Q*".


![CCQ](assets/fr/019.webp)


Kontrollera [på COLDCARD:s officiella webbplats] (https://coldcard.com/downloads) om det finns en nyare version tillgänglig. Klicka på "*Download*" för att ladda ner den nya firmware.


![CCQ](assets/fr/020.webp)


I det här läget rekommenderar vi starkt att du kontrollerar integriteten och äktheten hos den nedladdade fasta programvaran. För att göra detta, ladda ner [dokumentet som innehåller hasharna för alla versioner, signerat av utvecklarna](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifiera signaturen med [utvecklarens publika nyckel](https://keybase.io/dochex), och kontrollera att Hash som anges i det signerade dokumentet matchar det som finns i den fasta programvaran som laddats ner från webbplatsen. Om allt är korrekt kan du fortsätta med uppdateringen.


Om du inte är bekant med denna verifieringsprocess rekommenderar jag att du följer denna handledning:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Ta ett microSD-kort och överför firmware-filen (dokument i `.dfu`) till det. Sätt i microSD-kortet i en av COLDCARD:s portar.


![CCQ](assets/fr/021.webp)


Välj sedan "*Från MicroSD*" i menyn för uppdatering av den fasta programvaran.


![CCQ](assets/fr/022.webp)


Välj den fil som motsvarar den fasta programvaran.


![CCQ](assets/fr/023.webp)


Bekräfta ditt val genom att trycka på knappen "*ENTER*".


![CCQ](assets/fr/024.webp)


Vänligen vänta medan den fasta programvaran uppdateras.


![CCQ](assets/fr/025.webp)


När uppdateringen är klar anger du din PIN-kod för att låsa upp enheten.


![CCQ](assets/fr/026.webp)


Din firmware är nu uppdaterad.


## COLDCARD Q parametrar


Om du vill kan du utforska inställningarna för ditt COLDCARD genom att gå till menyn "*Settings*".


![CCQ](assets/fr/027.webp)


I den här menyn hittar du olika anpassningsalternativ, t.ex. inställning av skärmens ljusstyrka eller val av standardmåttenhet.


![CCQ](assets/fr/028.webp)


Vi kommer att titta på andra avancerade inställningar i nästa handledning:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Skapa en Bitcoin Wallet


Nu är det dags att generate en ny Bitcoin Wallet! För att göra detta måste du skapa en Mnemonic-fras. På Coldcard har du tre metoder för att generera denna fras:




- Använd endast den interna slumptalsgeneratorn (TRNG);
- Använd en kombination av TRNG och tärningskastning för att lägga till entropi;
- Använd endast tärningsslag.


**För nybörjare och avancerade användare rekommenderar vi att endast använda COLDCARD:s interna slumptalsgenerator**


Jag rekommenderar inte alternativet med enbart tärningar, eftersom dåligt utförande kan leda till en mening med otillräcklig entropi, vilket äventyrar säkerheten för din Wallet.


Det bästa alternativet är dock helt klart det andra, som kombinerar användningen av TRNG med en extern entropikälla. Denna metod garanterar en lägsta entropi som är likvärdig med den för enbart TRNG och ger en extra säkerhetsnivå i händelse av att den interna generatorn skulle sluta fungera (frivilligt eller inte). Genom att välja detta alternativ, som kombinerar TRNG och tärningsrullning, får du större kontroll över genereringen av domen, utan att öka riskerna i händelse av dåligt utförande från din sida.


Klicka på "*Nya seed-ord*".


![CCQ](assets/fr/029.webp)


Du kan välja längden på din dom. Jag rekommenderar att du väljer en dom på 12 ord, eftersom den är mindre komplex att hantera och inte erbjuder mindre Wallet-säkerhet än en dom på 24 ord.


![CCQ](assets/fr/030.webp)


COLDCARD visar sedan din TRNG-genererade återställningsfras. Om du vill lägga till ytterligare extern entropi trycker du på "*4*"-tangenten.


![CCQ](assets/fr/031.webp)


Då kommer du till en sida där du kan lägga till entropi genom att kasta tärningen. Gör så många kast som möjligt (minst 50 rekommenderas, men mindre är inte så farligt eftersom du redan drar nytta av TRNG:s entropi) och registrera resultatet med knapparna "*1*" till "*6*". När du är klar trycker du på "*ENTER*" för att bekräfta.


![CCQ](assets/fr/032.webp)


En ny Mnemonic-fras visas, baserad på den entropi som du just har tillhandahållit och TRNG:s entropi.


**Varning: Denna Mnemonic ger full, obegränsad tillgång till alla dina bitcoins**. Vem som helst som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till ditt COLDCARD. Frasen på 12 ord återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på ditt COLDCARD. Det är därför mycket viktigt att spara det noggrant och förvara det på en säker plats.


Du kan skriva ner det på kartongen som medföljer ditt COLDCARD, eller för ökad säkerhet rekommenderar jag att du graverar det på ett rostfritt stålstöd för att skydda det från risken för brand, översvämning eller kollaps. Spara det under inga omständigheter på ett digitalt medium, annars kan du förlora dina bitcoins.


Skriv ner de ord som visas på skärmen på det fysiska medium som du väljer. Beroende på din säkerhetsstrategi kan du överväga att göra flera fullständiga fysiska kopior av meningen (men framför allt, dela inte upp den). Det är viktigt att hålla orden numrerade och i ordningsföljd.


Självklart får **du aldrig dela med dig av dessa ord** på Internet, till skillnad från i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.


När du har skrivit ner orden trycker du på "*ENTER*".


![CCQ](assets/fr/033.webp)


För att säkerställa att du har sparat din fras korrekt kommer systemet att be dig att bekräfta vissa ord. Välj den siffra som motsvarar varje ord på knappsatsen.


![CCQ](assets/fr/034.webp)


Din Wallet är nu skapad! I det övre högra hörnet av skärmen kan du se ditt fingeravtryck för den privata huvudnyckeln. Tryck på "*ENTER*".


![CCQ](assets/fr/035.webp)


Du har nu tillgång till COLDCARD:s huvudmeny.


![CCQ](assets/fr/036.webp)


## Konfigurera en ny Wallet på Sparrow


Det finns flera alternativ för att upprätta kommunikation mellan programvaran Sparrow wallet och ditt COLDCARD. Det mest okomplicerade är att använda en USB-C-kabel. Som standard är dock kabel- och NFC-kommunikation inaktiverad på ditt COLDCARD. För att återaktivera dem, navigera till "*Inställningar*", sedan "*Hårdvara på/av*" och aktivera önskat kommunikationsalternativ.


![CCQ](assets/fr/037.webp)


Om du föredrar att hålla ditt COLDCARD helt isolerat från din dator kan du välja indirekt kommunikation med "luftgap", med hjälp av QR-koder eller ett microSD-kort. Det är den metod vi använder i den här guiden.


Gå till "*Advanced/Tools*".


![CCQ](assets/fr/038.webp)


Välj "*Export Wallet*".


![CCQ](assets/fr/039.webp)


Välj sedan "*Sparrow wallet*".


![CCQ](assets/fr/040.webp)


Tryck på "*ENTER*" för att ändra konfigurationsfilen till generate.


![CCQ](assets/fr/041.webp)


Välj sedan hur du vill skicka filen till Sparrow. I det här exemplet har jag satt in ett microSD-kort i kortplats "*A*", så jag väljer knappen "*1*". Du kan också visa informationen som en QR-kod på COLDCARD-skärmen genom att trycka på "*QR*"-knappen och skanna QR-koden med datorns webbkamera.


![CCQ](assets/fr/042.webp)


Starta Sparrow wallet och hoppa över introduktionssidorna för att komma till huvudskärmen. Kontrollera att du är korrekt ansluten till en nod genom att kontrollera omkopplaren längst ned till höger på skärmen.


![CCQ](assets/fr/043.webp)


Det rekommenderas starkt att du använder din egen Bitcoin-nod. I den här handledningen använder jag en publik nod (gul), eftersom jag sitter på Testnet, men för produktionsanvändning är det bäst att använda Bitcoin Core lokalt (Green) eller en Electrum-server på en fjärrnod (blå).


Gå till menyn "*File*" och välj "*New Wallet*".


![CCQ](assets/fr/044.webp)


Ge din Wallet ett namn och klicka på "*Create Wallet*".


![CCQ](assets/fr/045.webp)


I rullgardinsmenyn "*Script Type*" väljer du vilken typ av script som ska säkra dina bitcoins.


![CCQ](assets/fr/046.webp)


Klicka på "*Airgapped Hardware Wallet*".


![CCQ](assets/fr/047.webp)


Under fliken "*Coldcard*" klickar du på "*Scan...*" om du planerar att skanna QR-koden som visas på ditt COLDCARD, eller "*Import File...*" för att importera filen från microSD (detta är filen `.json`).


![CCQ](assets/fr/048.webp)


Efter importen ska du kontrollera att det "*Master fingerprint*" som visas på Sparrow stämmer överens med det som visas på ditt COLDCARD. Bekräfta skapandet genom att klicka på "*Apply*".


![CCQ](assets/fr/049.webp)


Skapa ett starkt lösenord för att säkra åtkomsten till din Sparrow wallet. Detta lösenord skyddar dina publika nycklar, adresser, taggar och transaktionshistorik från obehörig åtkomst.


Det är en god idé att spara lösenordet så att du inte glömmer det (t.ex. i en lösenordshanterare).


![CCQ](assets/fr/050.webp)


Din Wallet är nu installerad på Sparrow wallet.


![CCQ](assets/fr/051.webp)


Innan du får dina första bitcoins i din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Skriv ner lite referensinformation, t.ex. din xpub, och återställ sedan ditt COLDCARD Q medan Wallet fortfarande är tom. Försök sedan återställa din Wallet till COLDCARD med hjälp av dina pappersbackuper. Kontrollera att den xpub som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga.


Om du vill veta mer om hur du utför ett återställningstest föreslår jag att du läser den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ta emot bitcoins


För att få dina första bitcoins börjar du med att slå på och låsa upp ditt COLDCARD.


![CCQ](assets/fr/052.webp)


På Sparrow wallet klickar du på fliken "*Receive*".


![CCQ](assets/fr/053.webp)


Innan du använder den Address som föreslås av Sparrow wallet ska du kontrollera den på din COLDCARD-skärm. Denna metod gör att du kan bekräfta att den Address som visas på Sparrow inte är bedräglig och att Hardware Wallet verkligen har den privata nyckel som behövs för att därefter spendera de bitcoins som är säkrade med denna Address. Detta hjälper dig att undvika flera typer av attacker.


För att utföra denna kontroll, klicka på menyn "*Address Explorer*" på COLDCARD.


![CCQ](assets/fr/054.webp)


Välj den typ av skript som du använder på Sparrow. I mitt fall är det SegWit P2WPKH. Jag klickar på det.


![CCQ](assets/fr/055.webp)


Du kan sedan se dina olika härledda adresser i ordning.


![CCQ](assets/fr/056.webp)


Kontrollera med Sparrow att Address matchar. I mitt fall är Address med avledningssökvägen `m/84'/1'/0'/0/0` verkligen `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` på både Sparrow och COLDCARD.


![CCQ](assets/fr/057.webp)


Ett annat sätt att verifiera Ownership av denna Address är att skanna dess QR-kod direkt på Sparrow från ditt COLDCARD. Från COLDCARD:s startskärm väljer du "*Scan Any QR Code*". Du kan också använda "*QR*"-tangenten på tangentbordet.


![CCQ](assets/fr/058.webp)


Skanna QR-koden för Address som visas på Sparrow wallet.


![CCQ](assets/fr/059.webp)


Kontrollera att den Address som visas på ditt COLDCARD överensstämmer med den som visas på Sparrow. Tryck sedan på "*1*"-knappen.


![CCQ](assets/fr/060.webp)


Address är därmed framgångsrikt bekräftat.


![CCQ](assets/fr/061.webp)


Du kan nu lägga till en "*Label*" för att beskriva källan till bitcoins som kommer att säkras med denna Address. Detta är en bra praxis som gör att du kan hantera dina UTXO:er bättre.


![CCQ](assets/fr/062.webp)


För mer information om märkning rekommenderar jag även denna andra handledning:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du kan sedan använda denna Address för att ta emot bitcoins.


![CCQ](assets/fr/063.webp)


## Skicka bitcoins


Nu när du har fått din första Sats i din COLDCARD-säkrade Wallet kan du spendera dem också!


Börja som vanligt med att slå på och låsa upp ditt COLDCARD Q, öppna sedan Sparrow wallet och navigera till fliken "*Sänd*" för att förbereda en ny transaktion.


![CCQ](assets/fr/064.webp)


Om du vill ha "coin control", dvs. välja specifikt vilka UTXO som ska användas i transaktionen, går du till fliken "*UTXO*". Välj de UTXO:er du vill använda och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.


![CCQ](assets/fr/065.webp)


Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Lägg till*".


![CCQ](assets/fr/066.webp)


Skriv ner en "*Label*" för att komma ihåg syftet med denna kostnad.


![CCQ](assets/fr/067.webp)


Välj det belopp som ska skickas till denna Address.


![CCQ](assets/fr/068.webp)


Justera avgiftssatsen för din transaktion enligt den aktuella marknaden.


![CCQ](assets/fr/069.webp)


Kontrollera att alla dina transaktionsparametrar är korrekta och klicka sedan på "*Create Transaction*".


![CCQ](assets/fr/070.webp)


Om allt är till belåtenhet klickar du på "*Finalize Transaction for Signing*".


![CCQ](assets/fr/071.webp)


När du har byggt upp din transaktion i Sparrow är det dags att signera den med ditt COLDCARD. För att överföra PSBT (osignerad transaktion) till din enhet har du flera alternativ. Om trådbunden dataöverföring är aktiverad kan du skicka transaktionen direkt via en USB-C-anslutning, precis som du skulle göra med vilken annan Hardware Wallet som helst. I det här fallet, på Sparrow, måste du klicka på "*Sign*"-knappen i det nedre högra hörnet. I mitt exempel är den här knappen blockerad eftersom COLDCARD inte är anslutet med kabel.


![CCQ](assets/fr/072.webp)


Om du föredrar att upprätthålla en "luftgapsanslutning" utan direktkontakt mellan Hardware Wallet och din dator har du två alternativ. Det första, och mer komplexa, är att använda ett microSD-kort. Sätt i microSD-kortet i datorn, spela in transaktionen via knappen "*Save Transaction*" på Sparrow och överför sedan kortet till en port på COLDCARD.


![CCQ](assets/fr/073.webp)


Gå sedan till menyn "*Ready To Sign*".


![CCQ](assets/fr/074.webp)


Granska transaktionsuppgifterna på ditt COLDCARD, inklusive mottagande Address, det skickade beloppet och transaktionsavgiften.


![CCQ](assets/fr/075.webp)


Om allt är korrekt trycker du på knappen "*ENTER*" för att signera transaktionen.


![CCQ](assets/fr/076.webp)


Sätt sedan tillbaka microSD-kortet i din dator och klicka på "*Load Transaction*" på Sparrow för att ladda den signerade transaktionen från microSD-kortet. Du kommer då att kunna utföra en sista kontroll innan du laddar upp den till Bitcoin-nätverket.


![CCQ](assets/fr/077.webp)


Den andra metoden för att signera med ditt COLDCARD i Air-Gap, som är mycket enklare än microSD-metoden, är att skanna PSBT direkt via enhetens kamera. På Sparrow väljer du "*Show QR*".


![CCQ](assets/fr/078.webp)


På COLDCARD väljer du "*Scan Any QR Code*". Du kan också använda "*QR*"-tangenten på tangentbordet.


![CCQ](assets/fr/079.webp)


Använd COLDCARD:s kamera för att skanna QR-koden som visas på Sparrow.


![CCQ](assets/fr/080.webp)


Transaktionsuppgifterna visas igen för verifiering. Tryck på "*ENTER*" för att signera om allt är som du vill.


![CCQ](assets/fr/081.webp)


Ditt COLDCARD visar sedan den signerade transaktionen som en QR-kod. Använd datorns webbkamera för att skanna denna QR-kod genom att välja "*Scan QR*" på Sparrow.


![CCQ](assets/fr/082.webp)


Din signerade transaktion är nu synlig på Sparrow. Kontrollera en sista gång att allt är korrekt och klicka sedan på "*Broadcast Transaction*" för att sända den på Bitcoin-nätverket.


![CCQ](assets/fr/083.webp)


Du kan spåra din transaktion i Sparrow wallet:s flik "*Transaktioner*".


![CCQ](assets/fr/084.webp)


Gratulerar, du har nu lärt dig den grundläggande användningen av COLDCARD Q med Sparrow wallet!


Om du tyckte att denna handledning var användbar skulle jag vara mycket tacksam om du lämnar en Green tumme nedan. Du är välkommen att dela denna handledning på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du tar en titt på den här andra handledningen där vi diskuterar de avancerade alternativen för COLDCARD Q :


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0