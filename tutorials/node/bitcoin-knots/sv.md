---
name: Bitcoin Knots
description: Hur startar jag en nod med den alternativa klienten Bitcoin Knots?
---
![cover](assets/cover.webp)


![video](https://youtu.be/zT4NuAaH3EM)


Bitcoin Knots är en alternativ implementering av Bitcoin-protokollet, som härrör från Bitcoin Core. Den är designad och underhålls av Luke Dashjr och erbjuder några ytterligare funktioner och regeljusteringar från Mempool, samtidigt som den förblir kompatibel med andra noder i nätverket. Bitcoin Knots integrerar en Bitcoin Wallet, men kan också användas som en enkel Bitcoin-nod tillsammans med annan Wallet-programvara.


## Varför använda knutar i stället för kärnor?


För närvarande är Core den mest använda implementeringen av Bitcoin-protokollet i nätverket. Bitcoin-protokollet är bara en uppsättning regler. Det krävs programvara för att tillämpa dem. En maskin som kör programvara som implementerar Bitcoin-protokollet kallas en nod, och alla dessa noder utgör tillsammans Bitcoin-nätverket.


Under hela Bitcoin:s historia har många klienter som härrör från den ursprungliga programvaran som utvecklats av Satoshi Nakamoto dykt upp. Idag (mars 2025) är Bitcoin Core den överväldigande majoriteten, med nästan 98% av noderna i Bitcoin-nätverket som använder denna klient.


Alternativ programvara finns dock också tillgänglig. Dessa är inte Altcoin-länkade noder som Bitcoin Cash, utan alternativa klienter som är kompatibla med det riktiga Bitcoin-nätverket. Av dessa är Bitcoin Knots den mest kända. Den representerar för närvarande cirka 1,4% av nätverket. Andra alternativa kunder är fortfarande mycket i minoritet.


![Image](assets/fr/01.webp)


Det finns två huvudsakliga skäl till att använda en alternativ klient som Knots i stället för Core:




- **Tekniska**: Dessa klienter erbjuder ofta olika alternativ till Core, särskilt när det gäller Mempool-hantering, genom att bestämma vilka transaktioner som accepteras och sänds av din nod.
- **Policy**: En del människor föredrar att använda alternativa klienter som Knots av icke-tekniska skäl, framför allt för att stödja ett alternativ till Core och därmed minska dess monopol. Om Core någonsin skulle äventyras skulle det vara användbart att inte bara ha solida, väl underhållna alternativa klienter, utan också att veta hur man använder dem. Andra använder Knots i protestsyfte, eftersom de har tappat förtroendet för Core-utvecklarna eller ogillar majoritetsklientens hantering.


## Hur installerar jag Bitcoin Knots?


Gå till [den officiella webbplatsen för Bitcoin Knots] (https://bitcoinknots.org/#download) för att ladda ner versionen för ditt operativsystem. Glöm inte att ladda ner fingeravtryck och signaturer för att verifiera programvaran. Dessa filer finns också tillgängliga [på Bitcoin Knots GitHub repository](https://github.com/bitcoinknots/Bitcoin).


![Image](assets/fr/02.webp)


Innan du installerar programvaran på din maskin rekommenderar vi starkt att du kontrollerar dess äkthet och integritet. Om du inte vet hur du gör kan du titta på den här andra handledningen:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
När programvaran har verifierats installerar du den genom att följa de steg som anges i installationspanelen.


![Image](assets/fr/03.webp)


## Lansering IBD


Första gången du startar Bitcoin Knots kommer du att kunna välja den lokala katalog där dina noddata (inklusive Blockchain, UTXO set och parametrar) kommer att lagras.


![Image](assets/fr/04.webp)


Du kan också välja att beskära Blockchain-data så att endast de senaste blocken sparas. Med det här alternativet kan din nod kontrollera varje block i sin helhet inom en fastställd lagringsgräns och därmed gradvis ta bort de äldsta blocken. Om du har tillräckligt med diskutrymme (för närvarande cirka 650 GB, men antalet växer), lämna det här alternativet omarkerat. Om ditt diskutrymme är begränsat aktiverar du beskärning och anger den maximala kapacitet som tillåts.


Observera: Om din nod har beskurits och du använder den för att synkronisera en återställd Wallet kommer du inte att kunna hämta transaktioner före det äldsta lokalt lagrade blocket.


![Image](assets/fr/05.webp)


Ett annat tillgängligt alternativ är "*Assume Valid*". Det påskyndar den inledande synkroniseringen genom att hoppa över signaturverifieringen för transaktioner som ingår i block före ett visst block.


Syftet med "*Assume Valid*" är att påskynda nodens första synkronisering utan att avsevärt minska säkerheten, genom att anta att dessa transaktioner redan har validerats massivt av nätverket i förväg. Den enda viktiga kompromissen är att din nod inte kommer att upptäcka några tidigare Bitcoin-stölder, men den kommer fortfarande att garantera riktigheten i det totala antalet utfärdade bitcoins. Din nod kommer att verifiera alla transaktionssignaturer efter det angivna blocket. Detta tillvägagångssätt baseras på antagandet att en transaktion som länge har accepterats av nätverket utan utmaning troligen är giltig.


Här är till exempel "*Assume Valid*" inställt på block nr. 855 000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, publicerat den 1 augusti 2024. Under IBD kommer min nod därför endast att starta fullständig signaturverifiering från detta block.


![Image](assets/fr/06.webp)


Klicka sedan på "*OK*"-knappen för att starta *Initial Block Download*. Du måste ha tålamod under den första synkroniseringen av noderna. Om du vill återuppta synkroniseringen senare stänger du bara programmet och stänger av datorn. Synkroniseringen kommer att återupptas utan problem nästa gång du öppnar programmet.


![Image](assets/fr/07.webp)


## Uppsättning av din Bitcoin-knut


Klicka på fliken "*Settings*" och välj sedan "*Options*".


![Image](assets/fr/08.webp)


I fliken "*Main*" kommer du åt nodens huvudparametrar:




- "*Start...*" startar automatiskt noden när datorn startas så att synkroniseringen kan påbörjas direkt;
- "*Prune...*" justerar lagringsgränsen om du har valt att beskära Blockchain ;
- "*Database cache...*" anger den maximala mängden RAM-minne som är tillåten för din nod;
- Slutligen aktiverar du "*Enable RPC server*" om du vill ansluta din Bitcoin Knots-nod till annan Wallet-programvara, som till exempel Sparrow wallet eller Liana.


![Image](assets/fr/09.webp)


På fliken "*Wallet*" hittar du inställningarna för den integrerade Wallet som du kan skapa senare på Knots. Jag rekommenderar att du aktiverar RBF och myntkontroll. Du kan också definiera vilken typ av skript som ska användas.


![Image](assets/fr/10.webp)


Fliken "*Network*" innehåller nätverksparametrar som du kan anpassa efter dina specifika behov.


![Image](assets/fr/11.webp)


På fliken "*Mempool*" kan du konfigurera *Memory Pool*, dvs. hanteringen av obekräftade transaktioner som lagras i minnet, och den maximala storleken som tilldelas denna funktion (300 MB som standard).


![Image](assets/fr/12.webp)


Fliken "Spamfiltrering" är en Bitcoin Knots-funktion. Här hittar du ett antal inställningar som gör att du kan välja vilka transaktioner du ska acceptera eller vägra att sända. Huvudsyftet är att begränsa vissa marginella användningar av Bitcoin, i synnerhet metaprotokoll, för att bekämpa dessa metoder samtidigt som du undviker att överbelasta din nod. Det är ett politiskt val, beroende på din personliga vision av Bitcoin.


Du hittar också klassiska parametrar som t.ex. definitionen av tröskeln "*Dust*".


Dessa parametrar påverkar dock endast standardiseringsreglerna. Din nod kommer att fortsätta att acceptera obekräftade transaktioner endast när de ingår i ett block, för att förbli kompatibel med resten av Bitcoin-nätverket. Dessa inställningar ändrar bara hur din nod bearbetar och distribuerar obekräftade transaktioner till sina kollegor. I praktiken, eftersom Knots är i minoritet, är det de regler som fastställs som standard på Bitcoin Core som definierar standardisering i nätverket.


![Image](assets/fr/13.webp)


På fliken "*Mining*" kan du konfigurera din nods eventuella deltagande i Mining, om du vill aktivera denna funktion.


![Image](assets/fr/14.webp)


Fliken "*Display*" innehåller slutligen parametrar som rör Interface:s grafik, inklusive programvarans språk.


![Image](assets/fr/15.webp)


## Skapa en Bitcoin Wallet


När den inledande synkroniseringen är klar är din Bitcoin Knots-nod fullt funktionell. Du har nu möjlighet att ansluta den här noden till annan Wallet-programvara eller använda den inbyggda Hot Wallet direkt. För att göra detta klickar du på knappen "*Skapa en ny Wallet*".


![Image](assets/fr/16.webp)


Ge din Wallet ett namn. Du kan också skydda den med en passphrase BIP39 genom att klicka på "*Kryptera Wallet*". När du är klar klickar du på knappen "*Create*".


![Image](assets/fr/17.webp)


passphrase BIP39 är ett valfritt lösenord som du kan välja fritt, utöver din Mnemonic-fras, för att öka säkerheten för din Wallet. Innan du konfigurerar den här funktionen rekommenderar vi starkt att du läser följande artikel, som förklarar i detalj hur passphrase fungerar i teorin och hur du undviker misstag som kan leda till permanent förlust av dina bitcoins:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Om du har aktiverat alternativet passphrase ska du välja ett robust alternativ och spara det noggrant på ett eller flera säkra fysiska medier.


![Image](assets/fr/18.webp)


Din Bitcoin Wallet är nu skapad.


![Image](assets/fr/19.webp)


## Säkerhetskopiera din Bitcoin Wallet


Redan innan du får dina första bitcoins är det viktigt att göra en säkerhetskopia av din Bitcoin Wallet så att du kan återställa dina pengar i händelse av förlust eller datorfel. För att göra detta, klicka på fliken "*File*" och sedan på "*Backup Wallet*".


![Image](assets/fr/20.webp)


Denna operation genererar en enda fil som kan användas för att återställa alla dina bitcoins. Så var mycket försiktig och spara den på ett säkert externt medium.


## Ta emot bitcoins


För att ta emot bitcoins direkt till din Knots Wallet, klicka på "*Receive*"-knappen.


![Image](assets/fr/21.webp)


Tilldela en "*Label*" till din Address för att enkelt identifiera dess syfte och underlätta framtida användning av *Coin Control*. Du kan också i förväg definiera ett exakt belopp som ska tas emot på denna Address, eller lägga till ett meddelande för betalaren. När du har ställt in parametrarna klickar du på "*Request payment*".


![Image](assets/fr/22.webp)


Bitcoin Knots visar sedan en mottagande Address, som du kan kopiera eller skanna och skicka till betalaren.


![Image](assets/fr/23.webp)


När en transaktion har sänts kan du följa dess status direkt i menyn "*Transaktioner*".


![Image](assets/fr/24.webp)


## Skicka bitcoins


Nu när du har bitcoins i din Knots Wallet kan du skicka dem. För att göra det, klicka på "*Sänd*"-knappen.


![Image](assets/fr/25.webp)


Klicka på knappen "*Inputs...*" för att välja de exakta UTXO som du vill spendera på den här transaktionen.


![Image](assets/fr/26.webp)


Ange mottagarens Bitcoin Address.


![Image](assets/fr/27.webp)


Lägg till en etikett för att komma ihåg syftet med denna transaktion.


![Image](assets/fr/28.webp)


Ange det belopp som du vill skicka till denna Address.


![Image](assets/fr/29.webp)


Klicka på knappen "*Välj...*" för att välja lämplig avgiftssats för din transaktion, baserat på aktuell nätverksstatus.


![Image](assets/fr/30.webp)


Om allt är till belåtenhet klickar du på knappen "*Sänd*". Om du använder en passphrase kommer du att bli ombedd att fylla i den i detta skede.


![Image](assets/fr/31.webp)


Kontrollera transaktionsparametrarna en sista gång och om allt är korrekt klickar du på knappen "*Send*" igen för att signera och distribuera din transaktion.


![Image](assets/fr/32.webp)


Din transaktion som väntar på bekräftelse visas nu under fliken "*Transaktioner*".


![Image](assets/fr/33.webp)


## Ansluta din nod till ett annat program


Bitcoin Knots integrerade Interface för att hantera din Bitcoin Wallet är inte nödvändigtvis den mest intuitiva och dess funktionalitet är fortfarande relativt begränsad. Du kan dock ansluta din Bitcoin Knots-nod till specialiserad Wallet-hanteringsprogramvara för att enkelt få tillgång till Blockchain Bitcoin-data och sända dina transaktioner.


Proceduren beror på vilken programvara som används, men det finns två huvudscenarier: antingen installeras Bitcoin Knots på samma dator som din Wallet-programvara, eller så körs den på en separat maskin.


### Med lokala Bitcoin-knutar :


Om Bitcoin Knots är installerat på din dator, leta reda på filen `Bitcoin.conf` bland programfilerna. Om den här filen inte finns kan du skapa den. Öppna den med en textredigerare och infoga följande rad:


```ini
server=1
```


Spara sedan dina ändringar.


Du kan också göra detta via Bitcoin-QT:s Interface-grafik genom att navigera till "*Settings*" > "*Options...*" och aktivera alternativet "*Enable RPC server*".


Glöm inte att starta om programvaran efter att du har gjort dessa ändringar.


![Image](assets/fr/34.webp)


Gå sedan till din Wallet-hanteringsprogramvara (t.ex. Sparrow wallet eller Liana) och ange sökvägen till din cookie-fil, som vanligtvis finns i samma mapp som `Bitcoin.conf`, beroende på ditt operativsystem:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


Lämna de andra parametrarna som standard, URL `127.0.0.1` och port `8332`, och klicka sedan på "*Test Connection*".


![Image](assets/fr/36.webp)


### Med fjärrkontroll Bitcoin knopar :


Om Bitcoin Knots är installerat på en annan maskin som är ansluten till samma nätverk, leta först upp filen `Bitcoin.conf` bland programfilerna. Om denna fil ännu inte finns kan du skapa den. Öppna filen med en textredigerare och lägg till följande rad:


```ini
server=1
```


När du har redigerat filen ska du se till att spara den i rätt mapp för ditt operativsystem:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

Denna operation kan också utföras via Bitcoin-QT:s Interface-grafik. Gå till menyn "*Settings*", sedan "*Options...*" och aktivera alternativet "*Enable RPC server*" genom att markera motsvarande ruta. Om filen `Bitcoin.conf` inte finns, kan du skapa den direkt från denna Interface genom att klicka på "*Open Configuration File*".


![Image](assets/fr/37.webp)


Hitta IP Address för den maskin som är värd för Bitcoin Knots i ditt lokala nätverk. För att göra detta kan du använda ett verktyg som [Angry IP Scanner] (https://angryip.org/). Låt oss anta, för argumentets skull, att IP Address för din nod är `192.168.1.18`.


I filen `Bitcoin.conf` lägger du till följande rader och ställer in `rpcbind=192.168.1.18` så att den matchar IP Address för din nod.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


Lägg också till ett användarnamn och lösenord för fjärranslutningar i filen `Bitcoin.conf`. Se till att ersätta `loic` med ditt användarnamn och `my_password` med ett starkt lösenord:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


När du har ändrat och sparat filen startar du om Bitcoin Knots.


Du kan nu gå till din Wallet-hanteringsprogramvara (t.ex. Sparrow wallet eller Liana). På Sparrow går du till fliken "*User / Pass*". Ange det användarnamn och lösenord som du har konfigurerat i filen `Bitcoin.conf`. Lämna övriga parametrar som standard, dvs. URL `127.0.0.1` och port `8332`. Klicka sedan på "*Test Connection*".


![Image](assets/fr/40.webp)


Anslutningen är upprättad.


Nu vet du allt om den alternativa implementeringen av Bitcoin Knots.


Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Dela gärna det på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också den här andra handledningen där jag förklarar hur du ställer in din egen Lightning-nod:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a