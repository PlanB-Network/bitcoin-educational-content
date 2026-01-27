---
name: Satochip x SeedSigner
description: Hur använder man en Satochip med sin SeedSigner?
---

![cover](assets/cover.webp)



*Tack till [Crypto Guide](https://www.youtube.com/@CryptoGuide/) för dess fork av SeedSigner-firmware för smartkortstöd, som vi kommer att använda i den här handledningen



---

Satochip är en hårdvara i wallet-smartkortsformat med ett EAL6+-certifierat säkerhetselement, en av de högsta säkerhetsstandarderna. Den är designad och producerad av det belgiska företaget med samma namn: Satochip.



Satochip kostar ca 25 euro och skiljer sig från konkurrenterna genom sitt utmärkta värde för pengarna. Tack vare sitt säkra chip är den motståndskraftig mot fysiska attacker. Dessutom är appletens källkod helt öppen källkod, licensierad under *AGPLv3*.



Å andra sidan innebär dess format vissa funktionella begränsningar. Den största nackdelen med Satochip är avsaknaden av en integrerad skärm: användarna måste därför underteckna transaktioner i blindo och enbart förlita sig på datorns display.



För att övervinna denna svaghet är en särskilt intressant konfiguration att använda den tillsammans med en SeedSigner. I den här konfigurationen sker kommunikationen inte längre direkt mellan datorn och Satochip, utan via QR-kodutbyte mellan datorn och SeedSigner. SeedSignern fungerar då som en "trust screen": den visar den information som ska signeras, medan själva signeringen utförs av Satochip. Till skillnad från konventionell användning av SeedSigner (eller till och med användning i kombination med Seedkeeper) laddas seed aldrig in i SeedSigner. SeedSigner blir därmed Satochips skärm, vilket eliminerar de risker som är förknippade med blind signering.



Om vi ser på problemet från andra hållet, så fyller SeedSigner med Satochip en stor lucka i SeedSigner: möjligheten att lagra och använda seed i en secure element.



Enligt min mening erbjuder denna konfiguration flera fördelar jämfört med konventionella hårdvaruplånböcker:




- Satochip kostar cirka 25 euro, och eftersom appleten är öppen källkod kan du installera den själv på ett tomt smartkort. Sedan tillkommer kostnaden för SeedSigner-komponenterna och tillägget för läsning av smartkort: beroende på var du köper hårdvaran blir summan mellan 70 och 100 euro.
- All programvara som ingår i installationen är öppen källkod: SeedSigners firmware och Satochip-appleten.
- Du drar nytta av ett certifierat säkerhetselement.
- Konfigurationen kan utföras helt själv, utan att använda hårdvara som uttryckligen är avsedd för Bitcoin-användning, vilket kan ge en form av trovärdig förnekelse och motståndskraft mot vissa externa hot (inklusive, beroende på land, statliga påtryckningar). Detta är också en intressant lösning om tillgången till kommersiella hårdvaruplånböcker är begränsad eller omöjlig i din region.




## 1. Material som krävs



För att utföra denna installation behöver du följande saker:




- Den vanliga utrustningen som behövs av en klassisk SeedSigner :
 - en Raspberry Pi Zero med GPIO-stift,
 - 1.3" Waveshare-skärm,
 - en kompatibel kamera,
 - ett microSD-kort.



![Image](assets/fr/01.webp)





- SeedSigner extension kit, tillgängligt [från den officiella Satochip-butiken](https://satochip.io/product/seedsigner-extension-kit/), som låter dig läsa och skriva till ett smartkort direkt från din SeedSigner. Ett annat alternativ är att använda [en extern smartkortsläsare](https://satochip.io/product/chip-card-reader/), som kan anslutas med kabel till en Micro-USB-port på Raspberry Pi. Jag har dock inte testat den här lösningen själv;
- [En Satochip](https://satochip.io/product/satochip/), eller alternativt ett [tomt smartkort](https://satochip.io/product/card-for-diy-project/) på vilket Satochip-appleten kan installeras (i det tilläggskit som Satochip säljer ingår redan ett tomt smartkort). Satochips tilläggssats stöder också formatet [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Så du kan välja detta format om du föredrar det.



![Image](assets/fr/02.webp)



För mer information om den utrustning som krävs för att montera en SeedSigner, se del 1 av denna andra handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Installera firmware



För att använda din SeedSigner med en Satochip måste du installera en alternativ firmware, som skiljer sig från den ursprungliga SeedSigner, för att stödja smartkortläsning. För detta [rekommenderar jag att du använder fork från "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Ladda ner [den senaste versionen av bilden](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) som motsvarar den Raspberry Pi-modell du använder.



![Image](assets/fr/03.webp)



Om du inte redan har det, ladda ner programvaran [Balena Etcher](https://etcher.balena.io/) och gör sedan på följande sätt:




- Sätt i microSD-kortet i din dator;
- Launch Etcher ;
- Välj filen `.zip` som du just har laddat ner;
- Välj microSD-kortet som mål;
- Klicka på `Flash!`.



![Image](assets/fr/04.webp)



Vänta tills processen är klar: ditt microSD-kort är nu klart för användning. Du kan nu gå vidare med att montera ihop din enhet.



Mer information om installation av firmware och verifiering av programvara (ett steg som jag starkt rekommenderar att du tar) finns i följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montering av smartkortläsaren



Börja med att installera kameran på Raspberry Pi Zero, sätt försiktigt in den i kamerans stift och lås den med den svarta fliken. Placera sedan Pi på botten av höljet och se till att rikta in portarna med motsvarande öppningar.



![Image](assets/fr/05.webp)



Anslut sedan smartkortläsaren till Raspberry Pi Zeros GPIO-stift.



![Image](assets/fr/06.webp)



Skjut plastskyddet över smartkortläsaren tills det är korrekt placerat.



![Image](assets/fr/07.webp)



Lägg sedan till skärmen på tilläggets GPIO-stift.



![Image](assets/fr/08.webp)



Slutligen sätter du in microSD-kortet som innehåller den inbyggda programvaran i sidoporten på Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Du kan nu ansluta din SeedSigner antingen via Raspberry Pi Zeros Micro-USB-port eller via förlängningens USB-C-port. Båda alternativen fungerar. Vänta några sekunder på uppstart, sedan bör du se välkomstskärmen visas.



![Image](assets/fr/10.webp)



För mer information om den första installationen av din SeedSigner rekommenderar jag att du läser del 4 i följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flasha ett smartkort med Satochip-appleten (valfritt)



Om du redan äger en Satochip kan du hoppa över detta steg och gå direkt till steg 4. I det här avsnittet ska vi titta på hur du installerar Satochip-appleten på ett tomt smartkort (DIY-metoden). Appleten är helt enkelt ett litet program som körs på smartkortet och som gör det möjligt för oss att hantera specifika funktioner.



För att komma igång, öppna menyn `Tools > Smartcard Tools` på din SeedSigner.



![Image](assets/fr/11.webp)



Välj sedan `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Sätt in ditt smartkort i SeedSigner-läsaren med chipet nedåt och välj appleten `Satochip`.



![Image](assets/fr/13.webp)



Ha tålamod under installationen: processen kan ta flera tiotals sekunder.



![Image](assets/fr/14.webp)



När appleten har installerats kan du gå vidare till steg 4.



![Image](assets/fr/15.webp)




## 5. Skapa och spara seed



### 5.1. Generera seed



Nu när du har fått all din hårdvara och mjukvara att fungera korrekt kan du fortsätta med att skapa din Bitcoin-portfölj. Detta gör du genom att koppla in din SeedSigner och sedan generate:a din seed som med en vanlig SeedSigner, antingen genom att kasta tärningen eller genom att ta ett foto:




- Gå till menyn `Verktyg > Kamera / Tärningsrullar`;
- Följ sedan processen för entropigenerering enligt den valda metoden;
- Slutligen ska du säkerhetskopiera seed på fysiska medier och kontrollera säkerhetskopian noggrant.



![Image](assets/fr/16.webp)



Om du vill se detaljerna i denna procedur, följ del 5 i denna handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Spara seed på en Seedkeeper



När seed har genererats är detta den enda gången den finns i SeedSigners RAM-minne. I mitt fall vill jag spara den på en [Seedkeeper](https://satochip.io/product/seedkeeper/), en annan Satochip-produkt som är utformad för att lagra hemligheter. Jag kommer att använda den här enheten som en sista utväg, om jag förlorar min Satochip.



Vilken backup-strategi som väljs här beror på dina preferenser, men det är absolut nödvändigt att ha minst en kopia av din mnemotekniska fras, antingen på fysiska medier (papper eller metall) eller, som här, i en Seedkeeper. Du kan också multiplicera antalet säkerhetskopior efter behov. För mer information om strategier för säkerhetskopiering av portföljer föreslår jag att du läser den här handledningen :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

För att säkerhetskopiera din seed på en Seedkeeper, gå direkt till menyn `Backup Seed`.



![Image](assets/fr/17.webp)



Sätt sedan in din Seedkeeper i smartkortläsaren och välj `To SeedKeeper`.



![Image](assets/fr/18.webp)



Ange din PIN-kod för att låsa upp den.



![Image](assets/fr/19.webp)



Välj en `Label` för att enkelt identifiera dina olika hemligheter som lagras på Seedkeeper. Du kan till exempel helt enkelt behålla wallet-avtrycket eller uttryckligen ange `Seed`. Valet beror på dina preferenser och risker.



![Image](assets/fr/20.webp)



Om din backup-strategi enbart förlitar sig på denna Seedkeeper rekommenderar jag starkt att du kör ett tomt återställningstest nu och sedan jämför fingeravtrycken för att kontrollera att backupen fungerar.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

PIN-koden för Seedkeeper bör vara så lång och slumpmässig som möjligt för att förhindra försök till brute force i händelse av att kortet fysiskt äventyras. Du bör också ha en säkerhetskopia av denna PIN-kod, lagrad på en annan plats än Seedkeeper. Utan denna PIN-kod kommer du inte att kunna komma åt den mnemonic som lagras i Seedkeeper, och dina bitcoins kommer att gå förlorade permanent.



### 5.3. Spara seed på Satochip



Nu när din portfölj har genererats, sparats och verifierats ska vi överföra den till Satochip. För att göra detta, se till att seed är laddad i SeedSigners RAM. Gå sedan till `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Sätt i din Satochip i smartkortläsaren och välj sedan `Initialisera med Seed`.



![Image](assets/fr/22.webp)



Enheten uppmanar dig att ange PIN-koden för Satochip; eftersom kortet är nytt och inte initierat finns det ännu ingen PIN-kod. Ange valfri kod för att hoppa över detta steg (det är inte en blockeringskod).



![Image](assets/fr/23.webp)



SeedSigner upptäcker att din Satochip inte har initialiserats. Klicka på "Jag förstår" för att bekräfta.



![Image](assets/fr/24.webp)



Du kan sedan ställa in Satochip PIN-koden, från 4 till 16 tecken. För att förstärka säkerheten för din wallet, välj en lång, slumpmässig kod: det är det enda skyddet mot fysisk tillgång till din minnesfras.



Kom ihåg att spara denna PIN-kod så snart den skapats, antingen i en säker lösenordshanterare eller på ett fysiskt medium, beroende på din personliga strategi. I det senare fallet ska du se till att aldrig förvara mediet som innehåller PIN-koden på samma plats som din Satochip, annars blir skyddet värdelöst. Det är viktigt att ha en säkerhetskopia: **Utan denna PIN-kod kommer du inte att kunna komma åt din seed, och dina bitcoins kommer att gå förlorade för alltid**.



![Image](assets/fr/25.webp)



SeedSigner frågar dig sedan vilken seed som ska importeras till Satochip. Välj den vars fingeravtryck matchar den portfölj som du just har skapat.



![Image](assets/fr/26.webp)



Din seed är nu importerad till Satochip.



![Image](assets/fr/27.webp)



Du kan nu stänga av din SeedSigner.



Om du vill använda en passphrase BIP39 för att förbättra säkerheten för din wallet, se del 6 i denna handledning:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importera wallet till Sparrow



Nu när din portfölj är igång importerar vi dess offentliga information ("*keystore*") till Sparrow Wallet eller annan programvara för portföljhantering. Denna programvara kommer att användas för att skapa, distribuera och spåra dina transaktioner. Det kommer dock inte att kunna signera dem, eftersom endast Satochip (och eventuella säkerhetskopior) har de privata nycklar som behövs för denna operation.



### 6.1 Förberedelse av SeedSigner och Satochip



Sätt i microSD-kortet som innehåller operativsystemet och slå sedan på din SeedSigner. För tillfället kan den inte göra någonting, eftersom den ännu inte känner till din seed. Du måste börja med att sätta in Satochip i smartkortläsaren, eftersom det är den som innehåller din seed.



Gå till menyn Verktyg > Smartcard-verktyg > Satochip-funktioner på startskärmen.



![Image](assets/fr/28.webp)



Klicka sedan på "Exportera Xpub".



![Image](assets/fr/29.webp)



Välj portföljtyp. I vårt fall är det en singelportfölj: välj `Single Sig`.



![Image](assets/fr/30.webp)



Därefter kommer valet av skriptstandard. Välj den senaste: `Native SegWit`.



![Image](assets/fr/31.webp)



Slutligen väljer du "Coordinator", dvs. det program för portföljhantering som du vill använda. Här kommer vi att använda Sparrow Wallet.



![Image](assets/fr/32.webp)



Ett varningsmeddelande visas: detta är helt normalt. Den utökade publika nyckeln (`xpub`) gör att du kan se alla adresser som härrör från din seed (på det första kontot). Den ger dig dock inte tillgång till dina pengar: om den avslöjas skulle det äventyra din integritet, men inte säkerheten för dina bitcoins. Med andra ord kan du se dina saldon, men inte spendera dem.



Klicka på "Jag förstår".



![Image](assets/fr/33.webp)



Ange sedan PIN-koden för din Satochip för att låsa upp den. Det är den kod som du definierade och sparade i steg 5.



![Image](assets/fr/34.webp)



Klicka slutligen på "Exportera Xpub" om du är nöjd med den information som visas.



![Image](assets/fr/35.webp)



SeedSigner genererar sedan din xpub i form av en dynamisk QR-kod, som innehåller alla uppgifter du behöver för att hantera din portfölj i Sparrow Wallet. Du kan justera ljusstyrkan på skärmen med hjälp av joysticken för att göra det lättare att skanna QR-koden.



### 6.2 Importera en ny portfölj till Sparrow Wallet



Se till att programvaran Sparrow Wallet är installerad på din dator. Om du inte vet hur du laddar ner den, kontrollerar dess äkthet och installerar den korrekt, se vår fullständiga handledning i ämnet :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Öppna Sparrow Wallet på din dator och klicka sedan på `Fil → Importera Wallet` i menyraden.



![Image](assets/fr/36.webp)



Bläddra ner till `SeedSigner` och välj sedan `Scan...`. Din webbkamera kommer att aktiveras: skanna den dynamiska QR-koden som visas på din SeedSigner-skärm.



![Image](assets/fr/37.webp)



Tilldela ett namn till din portfölj och klicka sedan på "Skapa Wallet". Sparrow kommer sedan att be dig att ange ett lösenord för att låsa lokal åtkomst till denna wallet. Välj ett starkt lösenord: det skyddar dina data i Sparrow (offentliga nycklar, adresser, etiketter och transaktionshistorik). Detta lösenord krävs dock inte för att återställa wallet i framtiden: endast din minnesfras (och eventuellt din passphrase) kommer att göra det.



Jag rekommenderar att du sparar lösenordet i en lösenordshanterare så att du inte tappar bort det.



![Image](assets/fr/38.webp)



Din keystore har importerats framgångsrikt.



![Image](assets/fr/39.webp)



Kontrollera nu att det `Master fingeravtryck` som visas i Sparrow Wallet stämmer överens med det som tidigare hittades på din SeedSigner.



SeedSigner kommer sedan att be dig att skanna en slumpmässig mottagningsadress från din Sparrow wallet för att bekräfta importens giltighet.



![Image](assets/fr/40.webp)



Din Satochip (via SeedSigner) och Sparrow Wallet är nu säkert anslutna. Sparrow fungerar som ett komplett hanteringsgränssnitt, medan Satochip förblir den enda enheten som kan signera dina transaktioner. Du är nu redo att ta emot och skicka bitcoins i en helt luftgapad konfiguration.



![Image](assets/fr/41.webp)



## 7. Ta emot och skicka bitcoins



Din Satochip och Sparrow Wallet är nu konfigurerade för att fungera tillsammans. I det här avsnittet förklarar vi steg för steg hur du tar emot och skickar bitcoins i det här läget.



### 7.1 Ta emot bitcoins



#### 7.1.1 Skapa en mottagningsadress



Öppna Sparrow Wallet på din dator och lås upp din `Satochip-SeedSigner` wallet med hjälp av ditt lösenord. Kontrollera att programvaran är ansluten till en server (indikator längst ned till höger). Klicka sedan på `Receive` i sidofältet.



![Image](assets/fr/42.webp)



En ny Bitcoin-adress visas. Du kommer att hitta :




- Adressen i textformat (börjar med `bc1q...` om du använder P2WPKH, som i det här exemplet) ;
- Den tillhörande QR-koden ;
- Ett "Label"-fält, användbart för att spåra dina transaktioner.



Jag rekommenderar starkt att du lägger till en etikett på varje bitcoin-kvitto i din wallet. Detta kommer att hjälpa dig att enkelt identifiera ursprunget för varje UTXO och bättre hantera din integritet. För att ta reda på mer om detta viktiga ämne, kolla in den dedikerade utbildningen på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

För att lägga till en etikett anger du bara ett namn i fältet "Etikett" och bekräftar sedan.



Till exempel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Din adress är nu associerad med den här etiketten i alla Sparrow-avdelningar.



![Image](assets/fr/43.webp)



#### 7.1.2 Address-verifiering på SeedSigner



Innan du meddelar betalaren din mottagningsadress är det viktigt att kontrollera att den tillhör din seed. Detta steg säkerställer att din Satochip sedan kan signera transaktioner som är kopplade till den här adressen. Det förhindrar också potentiella attacker där Sparrow skulle visa en bedräglig adress. Tänk på att Sparrow körs i en osäker miljö (din dator), vars attackyta är mycket större än din Satochip, som är helt isolerad. Därför bör du aldrig lita blint på de adresser som visas i Sparrow innan du har kontrollerat dem på din wallet-maskinvara.



I Sparrow, klicka på QR-koden för adressen för att förstora den: den kommer då att visas i helskärm.



![Image](assets/fr/44.webp)



På din SeedSigner, sätt in Satochip i läsaren, välj sedan `Scan` från huvudmenyn. Skanna QR-koden som visas på din dator och välj sedan `Använd Satochip-kort`.



![Image](assets/fr/45.webp)



Bekräfta sedan vilken typ av skript som används (i det här fallet `Native SegWit`), ange Satochip PIN-koden för att låsa upp det och validera `xpub`-informationen.



![Image](assets/fr/46.webp)



Om den skannade adressen matchar den som härrör från din seed, kommer SeedSigner att visa meddelandet: `Address verifierad`.



![Image](assets/fr/47.webp)



Då kan du vara säker på att adressen tillhör din portfölj.



#### 7.1.3 Mottagande av medel



Du kan nu överföra denna adress i textform eller via QR-koden till den person eller avdelning som behöver skicka dig satss. När transaktionen har sänts ut i nätverket kommer den att visas under fliken Transaktioner i Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Skicka bitcoins



Att skicka bitcoins med Satochip-SeedSigner-konfigurationen innebär 3 steg:




- Skapande av transaktioner i Sparrow ;
- Signerar denna transaktion på Satochip, via SeedSigner ;
- Slutligen sänds transaktionen över nätverket från Sparrow.



Alla utbyten mellan de två enheterna sker uteslutande via QR-koder.



#### 7.2.1 Skapa en transaktion i Sparrow



I Sparrow Wallet kan du skapa en transaktion genom att klicka på fliken `Send` i den vänstra sidofältet. Jag föredrar dock att använda fliken `UTXOs`, som låter dig utöva *Coin Control*. Denna metod erbjuder exakt kontroll över de UTXO:er som spenderas, för att begränsa den information som avslöjas under dina transaktioner.



Välj de mynt du vill spendera på fliken `UTXOs` och klicka sedan på `Send Selected`.



![Image](assets/fr/49.webp)



Fyll sedan i transaktionsfälten:




- I "Betala till" klistrar du in mottagarens adress eller skannar deras QR-kod med hjälp av kameraikonen ;
- I `Label`, lägg till en etikett för att spåra denna kostnad;
- I `Amount` anger du det belopp som ska skickas;
- Slutligen väljer du laddningshastighet efter aktuella nätförhållanden (uppskattningar finns på [mempool.space](https://mempool.space/)).



När du har fyllt i alla fält, granska informationen noggrant och klicka sedan på `Create Transaction >>`.



![Image](assets/fr/50.webp)



Kontrollera en sista gång att transaktionsuppgifterna är korrekta och klicka sedan på "Slutför transaktionen för signering".



![Image](assets/fr/51.webp)



Transaktionen är nu klar, men har ännu inte undertecknats. För att visa [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) som en QR-kod, klicka på "Visa QR".



![Image](assets/fr/52.webp)



#### 7.2.2 Signera transaktionen med Satochip



Slå på din SeedSigner och sätt i din Satochip som vanligt. Välj `Scan` från startskärmen och skanna sedan QR-koden som visas på Sparrow.



![Image](assets/fr/53.webp)



Välj alternativet `Använd Satochip-kort`.



![Image](assets/fr/54.webp)



Ange din PIN-kod för att låsa upp smartkortet.



![Image](assets/fr/55.webp)



SeedSigner upptäcker att detta är en PSBT och visar en sammanfattning av transaktionen:




   - Det belopp som skickats,
   - Destinationsadresser,
   - Förknippade transaktionskostnader.



Klicka på "Granska detaljer" och granska all information direkt på SeedSigner-skärmen. De viktigaste punkterna att kontrollera är de skickade beloppen, destinationsadresserna och transaktionsavgifterna.



![Image](assets/fr/56.webp)



Om allt är i sin ordning väljer du `Approve PSBT` för att signera transaktionen med Satochip.



![Image](assets/fr/57.webp)



När signaturen är klar genererar SeedSigner en ny QR-kod som innehåller den signerade transaktionen, redo att skannas av Sparrow.



#### 7.2.3 Sändning av transaktionen från Sparrow



Nu när transaktionen är signerad och validerad återstår bara att sända den i Bitcoin-nätverket så att en miner kan inkludera den i ett block. I Sparrow klickar du på `Scan QR`.



![Image](assets/fr/58.webp)



Presentera QR-koden som visas på din SeedSigner (den som innehåller den signerade transaktionen) för webbkameran. Sparrow kommer då att visa alla transaktionsdetaljer. Kontrollera att all information är korrekt och klicka sedan på "Broadcast Transaction" för att sända ut den i Bitcoin-nätverket.



![Image](assets/fr/59.webp)



Din transaktion överförs nu till nätverket. Du kan följa dess bekräftelse på fliken `Transaktioner` i Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Få tillbaka din wallet



Som vi har sett i tidigare avsnitt finns det, beroende på din säkerhetsstrategi, flera sätt att säkerhetskopiera din återställningsfras utöver din Satochip :




- Använda en klassisk *SeedQR* med SeedSigner ;
- Genom att registrera den mnemotekniska frasen på ett fysiskt medium;
- Eller genom att lagra den på en Seedkeeper, enligt vad som förklaras i avsnitt 5.2.



I vilket fall som helst finns det två huvudsituationer där du måste ingripa: förlust av Satochip eller förlust av SeedSigner. Låt oss ta en titt på hur vi ska reagera i vart och ett av dessa scenarier.



### 8.1. Hämta din wallet med Satochip



Om du fortfarande har ditt Satochip men din SeedSigner är trasig eller förlorad är situationen ganska enkel att hantera, eftersom din wallet fortfarande finns i Satochip.



Det bästa alternativet är att rekommendera de nödvändiga komponenterna och bygga upp en ny SeedSigner från grunden. Eftersom det här är en "stateless" enhet spelar det ingen roll om du använder samma eller en annan SeedSigner: så länge du kan sätta in din Satochip fungerar allt normalt.



Om du inte vill bygga om en kan du också använda din Satochip på det klassiska sättet, dvs. direkt från din dator, utan att gå via SeedSigner. Den här metoden fungerar perfekt, men den minskar avsevärt säkerheten för din Bitcoin wallet: du förlorar "*air-gapped*"-isoleringen och måste nu signera blint, eftersom SeedSigner fungerade som en betrodd skärm. Detta kan dock vara en tillfällig lösning i en nödsituation, eller om du inte kan bygga om en SeedSigner.



För att göra detta behöver du en USB-läsare för smartkort eller NFC. Öppna den wallet som du vill återställa i Sparrow, gå sedan till fliken "Inställningar" och klicka på "Ersätt".



![Image](assets/fr/61.webp)



Sätt i din Satochip i smartkortläsaren som är ansluten till datorn och klicka sedan på `Importera` bredvid `Satochip`.



![Image](assets/fr/62.webp)



Slutligen anger du PIN-koden för ditt smartkort för att låsa upp det. Du kommer då att kunna komma åt dina wallet, skapa transaktioner och signera dem direkt med den anslutna Satochip.



### 8.2. Hämta ut din portfölj med SeedSigner



Det andra, mer känsliga scenariot är när du förlorar tillgången till din Satochip som innehåller seed: oavsett om den är trasig, borttappad, stulen eller om du har glömt PIN-koden. Om din Satochip har stulits eller förkommit rekommenderar vi starkt att du omedelbart överför dina bitcoins till en helt ny wallet, genererad med en annan seed, när du har fått tillgång till dina pengar igen. Detta säkerställer att en potentiell angripare aldrig kan få tillgång till dina Satochip.



För att återfå tillgång till din portfölj och flytta dina medel, ladda bara din seed i SeedSigner. Beroende på vilken backupmedia du använde har du flera alternativ:





- Ange din mnemoniska fras manuellt i menyn `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skanna din *SeedQR* genom att klicka på knappen `Scan` på hemsidan.



![Image](assets/fr/64.webp)





- Eller ladda din seed från en Seedkeeper, via menyn `Seeds > From SeedKeeper` (det här är den metod jag använder i den här handledningen). Du behöver bara ange PIN-koden för Seedkeeper och välja den hemlighet som ska användas som seed på SeedSigner.



![Image](assets/fr/65.webp)



När seed har laddats in i SeedSigner, oavsett vilken metod du använder, kommer du att kunna signera en eller flera skanningstransaktioner för att flytta dina bitcoins till en ny, okompromitterad wallet. För att ta reda på hur du gör detta, se del 7.2 i följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nu vet du hur du kan använda Satochip för att hantera din Bitcoin-portfölj på ett säkert sätt i kombination med SeedSigner.



Om du har blivit övertygad av det här upplägget, tveka inte att stödja de projekt som gör det möjligt:




- Genom att köpa din utrustning direkt [på Satochips webbplats](https://satochip.io/shop/);
- Genom att göra [en donation till SeedSigner-projektet](https://seedsigner.com/donate/);
- Genom att prenumerera på [Crypto Guides YouTube-kanal](https://www.youtube.com/@CryptoGuide/), som drivs av den person som underhåller GitHub-förvaret som är värd för den modifierade firmware som vi använde i den här handledningen.