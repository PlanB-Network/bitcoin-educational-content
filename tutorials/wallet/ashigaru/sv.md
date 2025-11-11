---
name: Ashigaru
description: fork från Samourai Wallet för att säkra, hantera och blanda dina bitcoins
---

![cover](assets/cover.webp)



Ashigaru är en Bitcoin mobil wallet applikation som är en fortsättning på Samourai Wallet projektet, men i en ny form. Denna programvara föddes i ett särskilt sammanhang: i april 2024 greps grundarna av Samourai Wallet av de amerikanska myndigheterna och deras servrar beslagtogs. Även om Samurai-applikationen i sig förblev användbar, underhålls den för närvarande inte längre. Ashigaru är en gratis fork-version av Samurai Wallet, som underhålls av ett anonymt team för att garantera kontinuiteten i Samurais funktionalitet och skydda dess ursprungliga filosofi: att försvara Bitcoin-användarnas integritet och suveränitet.



Ashigaru tar upp mycket av Samourais DNA: ett liknande gränssnitt, ett uppenbart självförvar, öppen källkod och ett fokus på integritet. Koden distribueras under GNU GPLv3-licensen, som säkerställer att vem som helst kan granska, modifiera eller vidaredistribuera programvaran.



Ashigaru-applikationen innehåller en uppsättning avancerade verktyg för sekretess och hantering av dina UTXO:er:




- Whirlpool**, ett coinjoin-protokoll baserat på Zerolink, som gör det möjligt för dig att bryta de deterministiska länkarna mellan transaktionens in- och utgångar, utan att förlora suveräniteten över dina medel.
- PayNym**, som implementerar återanvändbara betalningskoder (BIP47), nu representerat via ett "*Pepehash*"-avatarsystem.
- Ricochet**, en funktion som lägger till mellanliggande hopp till transaktioner för att göra dem svårare att spåra.
- Och naturligtvis ***Coin Control*** för att välja, frysa och märka dina UTXO:er exakt.
- Batch Spending***, för att minska kostnaderna genom att gruppera flera betalningar i en enda transaktion.
- **Stealth Mode**, som döljer applikationen på din mobil bakom en falsk startmotor så att den inte märks vid en fysisk inspektion av din telefon.
- Avancerade utgiftsverktyg för att optimera din sekretess (payjoin, stonewall ...).
- Ett optimerat återställningssystem med hjälp av lösenordsfras BIP39.
- Ett system för att automatiskt optimera valet av transaktionsavgifter.



![Image](assets/fr/01.webp)



Ashigaru riktar sig därför till användare som är medvetna om problemen kring spårbarhet av transaktioner på Bitcoin. Oavsett om du är en integritetsmedveten användare, en erfaren bitcoiner som är engagerad i självförvaring eller en individ som utsätts för riskerna med ökad övervakning, ger denna wallet-applikation dig de verktyg du behöver för att återfå kontrollen över din aktivitet på Bitcoin.



Ashigaru finns i en mobilversion via sin app, som vi kommer att utforska i denna handledning. Men det kan också användas på datorn med ***Ashigaru Terminal***, som vi kommer att introducera i en framtida handledning.



![Image](assets/fr/02.webp)



I den här handledningen vill jag introducera dig till den grundläggande användningen av Ashigaru: installation, anslutning till Dojo, säkerhetskopiering, mottagande och sändning av bitcoins. Avancerade verktyg kommer att presenteras i andra dedikerade handledningar.



## 1. Förutsättningar för Ashigaru



Applikationen kräver några förutsättningar för att fungera korrekt. Först och främst är det inte en applikation som finns tillgänglig i klassiska butiker som Google Play Store eller App Store. Den installeras manuellt på din telefon endast från dess `.apk`-fil, nedladdningsbar via Tor-nätverket. Så om du använder en iPhone fungerar inte den här metoden: du behöver en Android-enhet.



För att ladda ner filen `.apk` via Tor behöver du en webbläsare som kan komma åt `.onion`-webbplatser. Det enklaste sättet är att installera Tor Browser-applikationen på din telefon, tillgänglig från [Google Play Store] (https://play.google.com/store/apps/details?id=org.torproject.torbrowser) eller direkt [via dess `.apk`] (https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



De flesta nya smartphones blockerar installationen av applikationer från okända källor som standard. Du måste tillfälligt aktivera det här alternativet för Tor Browser i dina enhetsinställningar för att tillåta installation. När applikationen har installerats, kom ihåg att avaktivera den här funktionen för att förstärka telefonens säkerhet.



En annan viktig förutsättning för att använda Ashigaru är en Bitcoin Dojo-nod. Av säkerhets- och suveränitetsskäl upprätthåller Ashigaru-teamet inte en centraliserad server för att ansluta din applikation. Så du måste köra din egen Dojo-instans eller ansluta till en betrodd sådan.



Dojo gör det möjligt för din Ashigaru-applikation att konsultera blockchain-information, se dina adressbalanser och sända dina transaktioner på Bitcoin-nätverket.



Om du vill veta mer om Dojo och lära dig hur du installerar det, uppmanar jag dig att följa denna dedikerade handledning :



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Om du verkligen inte har råd att driva en egen Dojo kan du hitta personer som är villiga att dela med sig av sin instans gratis på [dojobay.pw] (https://www.dojobay.pw/mainnet/). Detta kan vara en tillfällig lösning, men på lång sikt rekommenderar jag att du använder din egen Dojo för att garantera din suveränitet och sekretess.



## 2. Kontrollera och installera Ashigaru-applikationen



### 2.1. Ladda ner Ashigaru-applikationen



På din telefon öppnar du Tor Browser och går till [den officiella Ashigaru-webbplatsen] (https://ashigaru.rs/download/), i avsnittet `Download`. Klicka sedan på knappen `Download for Android` för att ladda ner installationsfilen.



![Image](assets/fr/04.webp)



Innan vi installerar applikationen på din enhet kontrollerar vi dess äkthet och integritet. Detta är ett mycket viktigt steg, särskilt när du installerar en applikation direkt från en `.apk'-fil.



### 2.2. Kontrollera Ashigaru ansökan



Gå tillbaka till [den officiella Ashigaru-webbplatsen](https://ashigaru.rs/download/) i avsnittet `Download` och kopiera sedan meddelandet som visas under titeln `SHA-256 Hash av APK-filen`. Kopiera hela blocket, från `BEGIN PGP SIGNED MESSAGE` till `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Fortfarande på din telefon, öppna en ny flik i Tor Browser och gå till [Keybase-verifieringsverktyget] (https://keybase.io/verify). Klistra in meddelandet som du just kopierat i det angivna fältet och klicka sedan på knappen "Verifiera".



![Image](assets/fr/06.webp)



Om signaturen är äkta kommer Keybase att visa ett meddelande som bekräftar att filen har signerats av Ashigaru utvecklarna. Du kan också klicka på profilen `ashigarudev` som anges av Keybase och kontrollera att deras nyckelfingeravtryck motsvarar exakt : `A138 06B1 FA2A 676B`.



Om ett felmeddelande visas i det här skedet betyder det dock att signaturen är ogiltig. I det här fallet ska du **inte installera APK**. Börja om från början, eller be communityn om hjälp innan du fortsätter.



![Image](assets/fr/07.webp)



Keybase har försett dig med applikationens hash. Vi ska nu kontrollera att hashen för filen `.apk` som du har laddat ner matchar den som verifierats på Keybase. För att göra detta, gå till [HASH FILE ONLINE] (https://hash-file.online/).



![Image](assets/fr/08.webp)



Klicka på knappen `BROWSE...` och välj filen `.apk` som hämtades i steg 2.1.


Välj sedan hashfunktionen `SHA-256` och klicka på `CALCULATE HASH` för att beräkna hashen för din fil.



![Image](assets/fr/09.webp)



Webbplatsen kommer att visa hashen för din `.apk`-fil. Jämför den med den hash som du verifierade på Keybase.io. Om de två hasharna är identiska har äkthets- och integritetskontrollen varit framgångsrik. Du kan nu fortsätta att installera applikationen.



![Image](assets/fr/10.webp)



### 2.3. Installera Ashigaru-applikationen



För att installera programmet öppnar du telefonens filhanterare och går till mappen Nedladdningar. Klicka sedan på filen `.apk` som du just har kontrollerat och bekräfta installationen när du uppmanas till det.



![Image](assets/fr/11.webp)



Ashigaru är nu installerat på din telefon.



## 3. Initiera appen och skapa en Bitcoin-portfölj



När du startar programmet för första gången väljer du `MAINNET`.



![Image](assets/fr/12.webp)



Klicka sedan på `Get Started`.



![Image](assets/fr/13.webp)



Vi ska nu skapa en ny Bitcoin-portfölj. Tryck på knappen `Create a new wallet`.



![Image](assets/fr/14.webp)



### 3.1. Skapa en Bitcoin-portfölj



Ashigaru behöver en passphrase BIP39. Välj din passphrase och skriv in den i lämpliga fält. Den måste vara så lång och slumpmässig som möjligt för att motstå en brute-force-attack.



Gör en fysisk säkerhetskopia av denna passphrase omedelbart. Detta är ett mycket viktigt steg: om du förlorar din telefon, **om du inte längre har denna passphrase, kommer du inte längre att kunna komma åt dina bitcoins** som lagras med din Ashigaru wallet. Samma passphrase används också för att kryptera wallet:s återställningsfil.



Om du inte vet vad en passphrase är, eller inte helt förstår hur den fungerar, rekommenderar jag starkt att du läser den här extra handledningen. Detta är viktigt eftersom passphrase är en kritisk del av din säkerhet: om du missförstår hur den används kan det leda till att du förlorar dina pengar permanent.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

När du har angett ditt passphrase klickar du på `NEXT`.



![Image](assets/fr/15.webp)



Välj sedan en PIN-kod. Denna kod kommer att användas för att låsa upp din Ashigaru wallet och skydda den mot obehörig fysisk åtkomst. Den är inte inblandad i den kryptografiska härledningen av dina wallet-nycklar. Detta innebär att även utan att känna till PIN-koden kan vem som helst med din mnemoniska fras och passphrase återfå åtkomst till dina bitcoins.



Välj en lång, slumpmässig PIN-kod. Kom ihåg att förvara en säkerhetskopia på en annan plats än din telefon för att förhindra att de komprometteras samtidigt.



![Image](assets/fr/16.webp)



När PIN-koden har skapats visar Ashigaru din wallet:s mnemoniska fras. Varning: denna fras, i kombination med din passphrase, ger full tillgång till dina bitcoins. Alla som har den kan ta dina pengar i besittning, även om de inte har tillgång till din telefon. Denna sekvens på 12 ord kan användas för att återställa din wallet om din telefon skulle förloras, stjälas eller gå sönder. Det är därför viktigt att spara den med största försiktighet på ett fysiskt medium (papper eller metall).



Spara aldrig den här frasen i digital form, för då riskerar du att dina pengar blir stulna. Beroende på din säkerhetsstrategi kan du skapa flera fysiska kopior, men dela aldrig upp den. Behåll orden i exakt ordning och se till att de är numrerade.



Slutligen, förvara aldrig mnemoniken och passphrase på samma plats. Om båda äventyras samtidigt kan en angripare få tillgång till din wallet.



![Image](assets/fr/17.webp)



Om du vill veta mer om hur du säkrar din minnesfras kan du läsa denna kompletterande handledning :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru ber dig sedan att bekräfta din passphrase. Ta tillfället i akt att kontrollera att din fysiska säkerhetskopia är korrekt.



![Image](assets/fr/18.webp)



### 3.2. Ansluta en dojo



Nästa steg är att ansluta till din Dojo. Som förklarades i inledningen måste Ashigaru vara ansluten till en Dojo för att kunna interagera med Bitcoin-nätverket.



Logga in på din Dojos "Maintenance Tool" och öppna menyn `PAIRING`.



![Image](assets/fr/19.webp)



På Ashigaru trycker du på knappen `Scan QR` och scannar sedan QR-koden för anslutningen som visas av din DMT. Klicka sedan på "Fortsätt" för att bekräfta.



![Image](assets/fr/20.webp)



Ange din PIN-kod för att låsa upp wallet. Detta tar dig till synkroniseringssidan. Det är normalt att se *PayNym*-fel i det här skedet, eftersom wallet är ny. Klicka bara på "Fortsätt".



![Image](assets/fr/21.webp)



Du kommer då till startsidan för din portfölj.



![Image](assets/fr/22.webp)



Innan du går vidare rekommenderar jag att du genomför en teståterställning medan wallet fortfarande inte innehåller några bitcoin. Detta gör att du kan kontrollera att dina pappersbackuper fungerar korrekt. För att ta reda på hur, följ denna handledning:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Konfigurera Ashigaru-applikationen



För att komma åt applikationsinställningarna, klicka på bilden av din *PayNym* i det övre vänstra hörnet och välj sedan `Settings`.



![Image](assets/fr/23.webp)



Här hittar du flera alternativ för att anpassa Ashigarus funktion till dina behov. Jag rekommenderar dock starkt att du aktiverar 2 viktiga parametrar redan från början.



Börja med att öppna menyn `Säkerhet > Stealth-läge` och aktivera sedan den här funktionen om du behöver den. Den döljer Ashigaru-programmet bakom namnet, logotypen och gränssnittet för ett vanligt program som är installerat på din telefon. Syftet är att förhindra att någon identifierar Ashigaru vid en eventuell fysisk inspektion av din telefon.



![Image](assets/fr/24.webp)



Varje falsk applikation som erbjuds har en specifik metod för att låsa upp det riktiga Ashigaru-gränssnittet. Om du till exempel väljer kalkylatorn försvinner Ashigaru-applikationen från din startskärm och ersätts av en falsk kalkylator. När du öppnar den ser du ett klassiskt fungerande miniräknargränssnitt, men för att komma åt Ashigaru behöver du bara trycka på symbolen `=` fem gånger snabbt.



Den andra parametern som är viktig att aktivera är [**RBF** (*Replace-by-Fee*)] (https://planb.academy/resources/glossary/rbf-replacebyfee). Med det här alternativet kan du öka kostnaden för en transaktion om den fastnar i mempoolerna på grund av att kostnaden är för låg. Du kan aktivera det via menyn `Transaktioner > Använd RBF`.



![Image](assets/fr/25.webp)



Tips: Du kan ändra visningsenheten för din portfölj från `BTC` till `sat` genom att klicka på det totala saldot som visas på startsidan.



## 5. Ta emot bitcoins på Ashigaru



Nu när din portfölj är i drift kan du ta emot satss. För att göra det, tryck på `+`-knappen längst ner till höger i gränssnittet och sedan på den gröna `Receive`-knappen.



![Image](assets/fr/26.webp)



Ashigaru visar dig sedan den första oanvända mottagningsadressen i din wallet, för att förhindra återanvändning av adresser (återanvändning av adresser är en mycket dålig metod för din integritet). Du kan sedan vidarebefordra den här adressen till den person eller tjänst som behöver skicka bitcoins till dig.



![Image](assets/fr/27.webp)



När transaktionen har sänts ut i nätverket kommer den automatiskt att visas på applikationens startsida.



![Image](assets/fr/28.webp)



## 6. Skicka bitcoins med Ashigaru



Nu när du har bitcoins i din Ashigaru wallet kan du också skicka dem. För att göra det, tryck på `+` knappen längst ner till höger och välj sedan den röda `Send` knappen.



![Image](assets/fr/29.webp)



Välj sedan det konto från vilket du vill göra utgifterna. För tillfället har vi ännu inte tagit itu med `Postmix`-kontot, reserverat för coinjoins, som vi kommer att titta på i en senare handledning. Så vi kommer att skicka pengar från det huvudsakliga insättningskontot.



![Image](assets/fr/30.webp)



Ange dina transaktionsuppgifter: beloppet som ska skickas och mottagarens Bitcoin-adress.



![Image](assets/fr/31.webp)



Genom att klicka på de tre små prickarna i det övre högra hörnet och sedan på "Visa outnyttjade medel" kan du också välja exakt vilka UTXO:er du vill använda för att öka din integritet.



![Image](assets/fr/32.webp)



När du har fyllt i alla uppgifter klickar du på den vita pilen längst ner i gränssnittet för att fortsätta.



Du kommer då till en sammanfattningssida som visar alla detaljer om din transaktion. Flera viktiga element visas:




- I blocket "Destination" kontrollerar du en sista gång att mottagaradressen och det skickade beloppet är korrekta;
- I blocket `Fees` kan du se den avgiftssats som Ashigaru automatiskt väljer och vid behov ändra den genom att klicka på `MANAGE` ;
- Blocket `Transaction` anger vilken typ av transaktion du är på väg att utföra. Här talar vi om en enkel transaktion, men Ashigaru stöder också andra typer av sekretessoptimerade transaktioner, som vi kommer att täcka i detalj i en framtida handledning;
- Det röda blocket "Transaction Alert" varnar dig om din transaktion uppvisar mönster som kan identifieras av kedjans analysverktyg och som kan äventyra din integritet. Genom att klicka på det kan du se detaljerna. I mitt fall berättar Ashigaru till exempel att det skickade beloppet är runt (`3000 sats`), vilket gör att jag kan dra slutsatsen vilken utgång som motsvarar kostnaden och vilken som är utbytet. För att ta reda på mer om dessa kedjeanalysheuristiker inbjuder jag dig att följa min BTC 204-utbildning på Plan ₿ Academy ;
- Slutligen kan du lägga till en etikett på din transaktion för att hålla reda på dess syfte.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

När du har kontrollerat all information använder du den gröna pilen för att skicka bitcoins. Håll ner pilen och dra den sedan åt höger för att bekräfta överföringen.



![Image](assets/fr/33.webp)



Din transaktion har sänts ut på Bitcoin-nätverket.



![Image](assets/fr/34.webp)



## 7. Återställer din Ashigaru wallet



Återställning av en Ashigaru wallet skiljer sig något från den för en klassisk Bitcoin wallet, eftersom applikationen använder samma metoder som Samurai Wallet. Om du förlorar åtkomsten till din wallet (antingen för att du har glömt din PIN-kod, avinstallerat den eller tappat bort din telefon) finns det flera sätt att återfå dina bitcoins.



Om du fortfarande har tillgång till din telefon, eller om du har gjort en säkerhetskopia av den här filen, är den enklaste metoden att använda säkerhetskopian `ashigaru.txt`. Den här filen innehåller all information du behöver för att återställa din portfölj på en ny instans av Ashigaru (eller på Sparrow Wallet), men den är krypterad med passphrase som du definierade i steg 3.1 i den här handledningen. Du måste därför ha både filen `ashigaru.txt` och din passphrase för att kunna använda den här metoden.



Med dessa två element kan du till exempel återställa din portfölj på Sparrow Wallet.



![Image](assets/fr/35.webp)



Om du inte har tillgång till filen `ashigaru.txt` kan du fortfarande återfå tillgång till dina medel med hjälp av din passphrase minnesfras, precis som du skulle göra för alla andra Bitcoin-portföljer. Jag rekommenderar att du utför denna återställning antingen på en ny Ashigaru-instans eller direkt på Sparrow Wallet, för att enkelt återställa förbikopplingsvägarna från Whirlpool om du använde den. Alternativt kan du importera den här informationen till någon annan BIP39-kompatibel programvara genom att manuellt ange derivationsvägarna.



För mer information om denna process, se den fullständiga handledning som jag har skrivit om att återställa en Wallet Samurai wallet. Eftersom Ashigaru är en fork är proceduren identisk:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Som du kan se, oavsett vilken restaureringsmetod du använder, är passphrase oumbärlig. Så se till att säkerhetskopiera den noggrant. Du kan också göra flera kopior, beroende på din säkerhetsstrategi.



## 8. Uppdatera applikation



För att uppdatera Ashigaru-appen, eftersom du installerade den från en `.apk`-fil och inte via Play Store som en vanlig app, måste du ladda ner den nya `.apk`-filen som motsvarar den uppdaterade versionen och sedan installera den manuellt.



Upprepa stegen som beskrivs i avsnitt 2 i denna handledning, förutom att när du klickar på filen `.apk` för att starta installationen, **din Android-telefon ska erbjuda dig alternativet `Update`, inte `Install`**.



![Image](assets/fr/41.webp)



Detta är en mycket viktig punkt: om Android visar `Install` istället för `Update`, installerar du förmodligen en bedräglig version. I det här fallet avbryter du installationsproceduren omedelbart.



Precis som vid den första installationen ska du kontrollera äktheten och integriteten hos filen `.apk` innan du fortsätter med uppdateringen.



För att ta reda på när en ny version finns tillgänglig, kontrollera den officiella Ashigaru-webbplatsen då och då. Var säker på att Ashigaru är en stabil, mogen applikation, ärvd från Samourai Wallet, och uppdateringar är relativt sällsynta jämfört med yngre programvara.



## 9. Donera till Ashigaru-projektet



Ashigaru är ett projekt med öppen källkod. Om du vill stödja dess utveckling kan du göra en donation direkt från applikationen via PayNym.



För att göra detta klickar du på din PayNym längst upp till höger i gränssnittet och väljer sedan din betalningskod som börjar med `PM...`.



![Image](assets/fr/36.webp)



Tryck sedan på knappen `+` längst ner till höger på skärmen.



![Image](assets/fr/37.webp)



Välj `Ashigaru Open Source Project` som mottagare.



![Image](assets/fr/38.webp)



Klicka på knappen `CONNECT` för att upprätta en BIP47-kommunikationskanal (mer om detta protokoll i handledningen nedan).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



När meddelandetransaktionen har bekräftats kan du skicka dina donationer till projektet genom att klicka på den lilla vita pilen i gränssnittets övre högra hörn.



![Image](assets/fr/40.webp)



Du vet nu hur man använder de grundläggande funktionerna i Ashigaru-programmet. I framtida handledningar kommer vi att titta på hur man drar nytta av avancerade utgiftstransaktioner, liksom Whirlpool, coinjoin-implementeringen som ärvs från Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
