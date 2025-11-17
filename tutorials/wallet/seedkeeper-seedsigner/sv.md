---
name: Seedkeeper x SeedSigner
description: Hur använder jag Seedkeeper med min SeedSigner?
---

![cover](assets/cover.webp)



*Tack till [Satochip](https://satochip.io/)-teamet för att de gick med på att återanvända [deras videor](https://www.youtube.com/@satochip/videos) i den här handledningen. Tack också till [Crypto Guide](https://www.youtube.com/@CryptoGuide/) för dess fork av SeedSigner-firmware, vilket möjliggör stöd för smartkort



---

SeedSigner är en wallet-hårdvara som du monterar själv från standardhårdvara, vanligtvis runt en Raspberry Pi Zero. Denna wallet kallas "*stateless*": till skillnad från de flesta andra modeller på marknaden (Coldcard, Trezor, Ledger, etc.) lagrar den inte någon data i permanent minne och fungerar endast live från RAM. Som ett resultat lagras din portföljs seed aldrig på SeedSigner. Varje gång du startar om måste du fylla i den för att göra det möjligt för enheten att signera dina transaktioner. Den vanligaste metoden är att spara din seed som en QR-kod, som du sedan skannar varje gång du använder den (*SeedQR*).



Detta tillvägagångssätt innebär dock en betydande risk: seed måste förbli tillgänglig i klartext så att den kan skannas. I händelse av stöld eller intrång kan en angripare enkelt få tag på den och stjäla dina bitcoins.



För att övervinna denna svaghet kan SeedSigner kombineras med [**Seedkeeper**] (https://satochip.io/product/seedkeeper/), ett smartkort som utvecklats av Satochip. Detta gör det möjligt att lagra minnesfraser (eller andra hemligheter) i en secure element som skyddas av en PIN-kod. Seedkeeper-appleten är öppen källkod och dess secure element har EAL6+-certifiering. I kombination med SeedSigner erbjuder den en mycket intressant säkerhetsfunktion: dina nycklar hanteras helt offline, du signerar dina transaktioner på en betrodd skärm och seed är fysiskt skyddad i ett smartkort som är motståndskraftigt mot fysiska attacker.



Allt du behöver för att slutföra installationen är följande artiklar:




- Den vanliga utrustningen som behövs för en klassisk SeedSigner: en Raspberry Pi Zero, en Waveshare 1,3"-skärm, en kompatibel kamera och ett microSD-kort (du hittar mer information i SeedSigner-handledningen nedan);
- SeedSigner Extension Kit, tillgängligt [på den officiella Satochip-butiken] (https://satochip.io/product/seedsigner-extension-kit/), som gör att du kan läsa och skriva till smartkortet direkt från din SeedSigner. Ett annat alternativ är att använda en extern smartkortsläsare, som kan anslutas med kabel till en Micro-USB-port på Raspberry Pi. Jag har dock inte testat denna lösning själv;
- En Seedkeeper, eller alternativt ett tomt smartkort som du kan installera Seedkeeper-appleten på (i det tilläggskit som säljs av Satochip ingår redan ett tomt smartkort).



![Image](assets/fr/01.webp)



Denna handledning omfattar två scenarier:




- Om du redan har en Bitcoin-portfölj som hanteras via din SeedSigner behöver du bara installera den nya firmware. Du kan sedan fortsätta att använda din befintliga wallet, den här gången med Seedkeeper för ökad säkerhet.
- Om du ännu inte har en Bitcoin wallet kopplad till din SeedSigner måste du följa steg **5** och **6** i den handledning som nämns nedan. Dessa avsnitt förklarar hur man generate en mnemonisk fras med SeedSigner, sparar den via en *SeedQR* och sedan ansluter denna wallet till Sparrow Wallet för att hantera den. Jag kommer inte att gå in på dessa procedurer här och ** Jag antar att du redan har en fungerande Bitcoin wallet, konfigurerad med Sparrow och din SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Installera firmware



För att använda din SeedSigner med en Seedkeeper måste du installera en alternativ firmware, som skiljer sig från den ursprungliga SeedSigner, för att stödja smartkortläsning. För detta [rekommenderar jag att du använder fork från "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Ladda ner [den senaste versionen av bilden](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) som motsvarar den Raspberry Pi-modell du använder.



![Image](assets/fr/02.webp)



Om du inte redan har det, ladda ner programvaran [Balena Etcher] (https://etcher.balena.io/) och gör sedan på följande sätt:




- Sätt i microSD-kortet i din dator;
- Launch Etcher ;
- Välj filen `.zip` som du just har laddat ner;
- Välj microSD-kortet som mål;
- Klicka på `Flash!`.



![Image](assets/fr/03.webp)



Vänta tills processen är klar: ditt microSD-kort är nu klart för användning. Du kan nu gå vidare med att montera ihop din enhet.



Mer information om installation av firmware och verifiering av programvara (ett steg som jag starkt rekommenderar att du tar) finns i följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montering av smartkortläsaren



![video](https://youtu.be/jqE8HDMCImA)



Börja med att installera kameran på Raspberry Pi Zero, sätt försiktigt in den i kamerans stift och lås den med den svarta fliken. Placera sedan Pi på botten av höljet och se till att rikta in portarna med motsvarande öppningar.



![Image](assets/fr/04.webp)



Anslut sedan smartkortläsaren till Raspberry Pi Zeros GPIO-stift.



![Image](assets/fr/05.webp)



Skjut plastskyddet över smartkortläsaren tills det är korrekt placerat.



![Image](assets/fr/06.webp)



Lägg sedan till skärmen på tilläggets GPIO-stift.



![Image](assets/fr/07.webp)



Slutligen sätter du in microSD-kortet som innehåller den inbyggda programvaran i sidoporten på Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Du kan nu ansluta din SeedSigner antingen via Raspberry Pi Zeros Micro-USB-port eller via förlängningens USB-C-port. Båda alternativen fungerar. Vänta några sekunder på uppstart, sedan bör du se välkomstskärmen visas.



![Image](assets/fr/09.webp)



För mer information om den första installationen av din SeedSigner rekommenderar jag följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flasha ett smartkort med Seedkeeper-appleten (valfritt)



![video](https://youtu.be/NF4HemyEcOY)



Om du redan äger en Seedkeeper kan du hoppa över detta steg och gå direkt till steg 4. I det här avsnittet går vi igenom hur du installerar Seedkeeper-appleten på ett tomt smartkort (DIY-metod).



För att komma igång, öppna menyn `Tools > Smartcard Tools` på din SeedSigner.



![Image](assets/fr/10.webp)



Välj sedan `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Sätt in ditt smartkort i SeedSigner-läsaren med chipet nedåt och välj sedan appleten `SeedKeeper`.



![Image](assets/fr/12.webp)



Ha tålamod under installationen: processen kan ta flera tiotals sekunder.



![Image](assets/fr/13.webp)



När appleten har installerats kan du gå vidare till steg 4.



![Image](assets/fr/14.webp)



## 4. Spara en befintlig SeedQR på Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Nu när din Seedkeeper är i drift kan du spara din Bitcoin wallet mnemonic på smartkortet. Börja med att slå på din SeedSigner som vanligt och skanna sedan din wallet:s *SeedQR* för att ladda in den i enheten. När seed har importerats väljer du helt enkelt `Done`.



![Image](assets/fr/15.webp)



När seed är laddad, gå till menyn `Backup Seed`.



![Image](assets/fr/16.webp)



Sätt sedan in din Seedkeeper i SeedSigner-enheten och välj alternativet "Till SeedKeeper".



![Image](assets/fr/17.webp)



SeedSigner kommer sedan att be dig att ange en PIN-kod för din Seedkeeper. Eftersom det här är ett tomt kort har ingen kod ännu definierats. Ange valfri kod för att hoppa över detta steg och bekräfta sedan.



![Image](assets/fr/18.webp)



SeedSigner upptäcker att Seedkeeper ännu inte har initialiserats (dvs. inget lösenord har ställts in). Klicka på "Jag förstår" för att fortsätta.



![Image](assets/fr/19.webp)



Välj nu din Seedkeepers nya PIN-kod, mellan 4 och 16 tecken. För ökad säkerhet, välj en lång, slumpmässig kod: det är den enda barriären som skyddar fysisk åtkomst till din minnesfras.



Kom ihåg att spara PIN-koden så snart den har skapats, antingen i en tillförlitlig lösenordshanterare eller på ett separat fysiskt medium beroende på din strategi. I det senare fallet ska du se till att aldrig förvara mediet som innehåller PIN-koden på samma plats som din Seedkeeper, annars blir skyddet ineffektivt. Det är viktigt att ha en säkerhetskopia: **Utan denna PIN-kod kommer du inte att kunna komma åt din seed, och dina bitcoins kommer att gå förlorade**.



![Image](assets/fr/20.webp)



Du kan sedan definiera en "etikett" som är associerad med din minnesfras. Denna etikett är användbar om du lagrar flera hemligheter på Seedkeeper, så att du enkelt kan identifiera dem.



![Image](assets/fr/21.webp)



Din minnesfras är nu sparad på smartkortet.



![Image](assets/fr/22.webp)



När det gäller säkerhetsstrategi är flera tillvägagångssätt möjliga, beroende på dina behov och din riskexponeringsnivå. Personligen rekommenderar jag att du behåller minst 2 kopior av din seed:




- Detta är en nyhet för smartkort, som du kan ha lättillgängliga i vardagen, till exempel för att verifiera adresser eller signera transaktioner. Denna metod är praktisk (som vi kommer att se i del 5) och förblir säker tack vare det skydd som PIN-koden erbjuder, så att du kan hålla den tillgänglig utan större risk;
- En andra kopia av din okrypterade minnesfras, som fungerar som den ultimata säkerhetskopian av din portfölj, och som endast ska användas i händelse av förlust eller stöld av Seedkeeper. Eftersom denna version är okrypterad måste den förvaras på en separat, säkrare plats för att förhindra att de två säkerhetskopiorna äventyras samtidigt.



Beroende på din skyddsstrategi och riskprofil kan du också duplicera seed på flera olika Seedkeepers eller skapa flera fysiska kopior av mnemoniken. För att lära dig mer om dessa metoder, ta en titt på följande handledning:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Lastning av en seed från Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Du kan nu använda din Seedkeeper för att ladda din mnemoniska fras i SeedSigner vid uppstart och därmed signera dina Bitcoin-transaktioner. För att börja, slå på din SeedSigner genom att koppla in den och öppna sedan menyn `Seeds`.



![Image](assets/fr/23.webp)



Välj sedan alternativet `From SeedKeeper`.



![Image](assets/fr/24.webp)



Sätt in din Seedkeeper i smartkortläsaren och ange sedan din PIN-kod för att låsa upp den. Bekräfta din inmatning genom att trycka på den nedre högra bekräftelseknappen, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper kan innehålla flera hemligheter, så SeedSigner uppmanar dig sedan att välja den du vill ladda. Den etikett som visas motsvarar det namn som du definierade i steg 4. Om du, som i mitt fall, bara har registrerat en seed, kommer bara ett alternativ att vara tillgängligt.



![Image](assets/fr/26.webp)



Din seed är nu laddad. Kontrollera att detta är rätt wallet genom att jämföra fingeravtrycket som visas på skärmen med det som anges i inställningarna för Sparrow Wallet. Detta fingeravtryck lämnades också när wallet först skapades.



Om du använder en passphrase kan du applicera den i det här skedet (se del 6 i den här handledningen). Annars är det bara att klicka på "Klar".



![Image](assets/fr/27.webp)



Du kan sedan använda din wallet som vanligt: kontrollera dina leveransadresser och signera transaktioner, precis som med en klassisk SeedSigner. För att ta reda på mer om hur du använder den, se den dedikerade handledningen :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Använda Seedkeeper med en passphrase BIP39



Använder du en passphrase för att skydda din Bitcoin-portfölj? Du kan också registrera den i din Seedkeeper, tillsammans med din seed. Denna lösning gör det möjligt för dig att snabbt ladda din wallet på SeedSigner, utan att behöva ange passphrase manuellt på den lilla knappsatsen varje gång du använder den.



Jag tycker att den här metoden är särskilt intressant, eftersom den låter dig dra nytta av säkerhetsfördelarna med passphrase, samtidigt som du eliminerar de begränsningar som är förknippade med den dagliga användningen. Här är ett exempel på en konfiguration som jag skulle rekommendera:




- Förvara din seed och passphrase i en Seedkeeper, skyddad med en stark PIN-kod (detta är viktigt). Denna säkerhetskopia gör att du enkelt kan använda din wallet dagligen. Om du vill kan du kopiera denna information till en andra Seedkeeper;
- Förvara också en tydlig kopia av din minneslista och passphrase, på papper eller metall. Detta är din sista utväg om du förlorar din Seedkeeper eller dess PIN-kod. Se till att förvara dessa kopior på separata platser, så att de inte kan äventyras samtidigt.



I den här konfigurationen, om någon får tag på din mnemoniska fras i klartext, kommer de inte att kunna stjäla något utan att känna till passphrase (förutsatt, naturligtvis, att den är tillräckligt stark för att motstå en brute-force-attack). Omvänt, om någon upptäcker din passphrase i klartext, kommer den att förbli oanvändbar utan motsvarande mnemoniska fras.



Slutligen, om någon lyckas få fysisk tillgång till din Seedkeeper som innehåller seed och passphrase, kommer de inte att kunna ta ut något utan att känna till PIN-koden. Till skillnad från en passphrase kan denna kod inte forceras, eftersom smartkortet automatiskt låser sig efter 5 ogiltiga försök.



Säkerheten i denna konfiguration baseras därför på två viktiga punkter:




- En **passphrase strong**: den måste vara lång, slumpmässig och innehålla en mängd olika tecken. Dess komplexitet är inget problem för dig, eftersom du bara behöver ange det en gång på tangentbordet under initialiseringen; därefter kommer det att överföras av Seedkeeper ;
- En **stark PIN-kod** för Seedkeeper: även den slumpmässig och består av 16 tecken.



För att konfigurera den här inställningen börjar du med att ladda din passphrase i SeedSigner på vanligt sätt. Du kan följa proceduren som beskrivs i denna handledning:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

När din portfölj med passphrase har laddats korrekt på SeedSigner, öppna menyn `Seeds` och välj det fotavtryck som motsvarar denna portfölj. Observera att detta fotavtryck skiljer sig från det för portföljen utan passphrase.



![Image](assets/fr/28.webp)



Klicka sedan på `Backup Seed`, sätt in Seedkeepern i enheten och välj `To SeedKeeper`.



![Image](assets/fr/29.webp)



Ange din PIN-kod för att låsa upp Seedkeeper och tilldela sedan en etikett till denna hemlighet. Du kan lämna fingeravtrycket som etikett för att upprätthålla någon form av trovärdig förnekelse, eller uttryckligen ange `Passphrase Wallet`, till exempel.



![Image](assets/fr/30.webp)



Din passphrase-portfölj är nu registrerad på Seedkeeper.



![Image](assets/fr/31.webp)



Nästa gång du startar datorn sätter du bara in din Seedkeeper i hårddisken och navigerar sedan till `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Ange din PIN-kod för att låsa upp smartkortet och välj sedan den wallet som motsvarar din passphrase.



![Image](assets/fr/33.webp)



Kontrollera passphrase och ditt wallet avtryck och bekräfta sedan.



![Image](assets/fr/34.webp)



Du kan nu komma åt din portfölj med passphrase och signera dina transaktioner som du normalt skulle göra på en SeedSigner.



## 7. Ytterligare alternativ



I menyn `Tools > Smartcard Tools` hittar du flera alternativ för att hantera din Seedkeeper:





- I menyn "Gemensamma verktyg" kan du :
 - Kontrollera kortets äkthet;
 - Ändra PIN-kod ;
 - Ändra de etiketter som är associerade med dina hemligheter ;
 - Avaktivera NFC-funktionen (rekommenderas om du endast använder chipläsare) ;
 - Utför en fabriksåterställning.





- I menyn `SeedKeeper-funktioner` kan du :
 - Se listan över registrerade hemligheter ;
 - Spara en ny hemlighet ;
 - Ta bort en befintlig hemlighet ;
 - Spara eller ladda dina deskriptorer (användbar funktion för multi-sig-portföljer).





- I menyn `DIY Tools` kan du :
 - Kompilera Seedkeeper-appleten ;
 - Installera appleten på ett tomt kort ;
 - Ta bort en Seedkeeper-applet för att återställa den och göra den tom igen.



Nu vet du hur du kan använda Seedkeeper för att säkerhetskopiera din portfölj på ett säkert sätt i kombination med SeedSigner.



Om du har blivit övertygad av det här upplägget, tveka inte att stödja de projekt som gör det möjligt:




- Genom att köpa din utrustning direkt [på Satochips webbplats] (https://satochip.io/shop/);
- Genom att göra [en donation till SeedSigner-projektet] (https://seedsigner.com/donate/);
- Genom att prenumerera på [Crypto Guides YouTube-kanal] (https://www.youtube.com/@CryptoGuide/), som drivs av den person som underhåller GitHub-arkivet som är värd för den modifierade firmware.