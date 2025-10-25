---
name: Sparrow Wallet
description: Installera, konfigurera och använda Sparrow wallet
---
![cover](assets/cover.webp)


![video](https://youtu.be/yJpvfRl03Tw)


Sparrow wallet är en självförvaltande Bitcoin Wallet hanteringsprogramvara som utvecklats av Craig Raw. Denna programvara med öppen källkod uppskattas av bitcoiners för sina många funktioner och intuitiva Interface.


Det finns två sätt att använda Sparrow:




- Som en Hot Wallet, där dina privata nycklar lagras på din dator.
- Som en Cold Wallet manager, där privata nycklar hålls på en Hardware Wallet. I det här läget manipulerar Sparrow endast offentlig Wallet-information, spårar medel, genererar adresser och bygger transaktioner, men Hardware Wallet-signaturen krävs för att göra dessa transaktioner giltiga. Den kan därför ersätta applikationer som Ledger Live eller Trezor Suite.


Sparrow stöder plånböcker med en eller flera signaturer och möjliggör smidig hantering av flera plånböcker. Du kan till exempel samtidigt styra en Wallet som är ansluten till en Ledger, en annan till en Trezor och även ha en Hot Wallet.


Programvaran erbjuder också avancerade funktioner för myntkontroll, så att du kan välja exakt vilka UTXO:er som ska användas i dina transaktioner för att optimera din sekretess.


När det gäller anslutning låter Sparrow dig ansluta till din egen Bitcoin-nod, antingen på distans via en Electrum Server eller med Bitcoin Core. Det är också möjligt att använda en offentlig nod om du ännu inte har en egen. Fjärranslutningar görs via Tor.


## Installera Sparrow wallet


Gå till [den officiella nedladdningssidan för Sparrow wallet] (https://sparrowwallet.com/download/) och välj den programvaruversion som motsvarar ditt operativsystem.


![Image](assets/fr/01.webp)


Det är viktigt att kontrollera programvarans integritet och äkthet innan du installerar den. Om du inte vet hur du gör detta hittar du en fullständig handledning här :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

När Sparrow har installerats kan du hoppa över de inledande förklarande skärmarna och gå direkt till skärmen för anslutningshantering.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Ansluta till Bitcoin-nätverket


För att interagera med Bitcoin-nätverket och sända dina transaktioner måste Sparrow vara ansluten till en Bitcoin-nod. Det finns tre huvudsakliga sätt att upprätta denna anslutning:



- 🟡 Använda en publik nod, dvs. ansluta till en tredjepartsnod som tillåter sådana anslutningar. Om du inte har en egen Bitcoin-nod kan du med det här alternativet snabbt komma igång med Sparrow. Den nod du ansluter till kommer dock att se alla dina transaktioner, vilket kan äventyra din sekretess. Att ha kontroll över dina nycklar är viktigt, men att ha en egen nod är ännu bättre. Så använd det här alternativet endast om du precis har börjat, samtidigt som du är medveten om riskerna för din integritet.
- 🟢 Ansluta till en Bitcoin Core-nod. Om du har en egen Bitcoin Core-nod kan du ansluta den till Sparrow wallet, antingen lokalt om Bitcoin Core är installerat på samma maskin, eller på distans.
- 🔵 Anslutning via en Electrum-server. Om din Bitcoin-nod är utrustad med Electrums, vilket är fallet med node-in-a-box-lösningar som Umbrel eller Start9, kan du fjärransluta till den från Sparrow.


**Det är att föredra att använda en anslutning via Electrs eller Bitcoin Core på din egen nod för att minska behovet av att lita på en tredje part och optimera din sekretess**


### Anslut till en offentlig nod 🟡


Att ansluta till en publik nod är mycket enkelt. Klicka på fliken "*Public Server*".


![Image](assets/fr/03.webp)


Välj en nod i rullgardinsmenyn.


![Image](assets/fr/04.webp)


Klicka sedan på "*Test Connection*".


![Image](assets/fr/05.webp)


När du är ansluten kommer Sparrow wallet att visa en gul bock i det nedre högra hörnet av Interface för att ange att du är ansluten till en offentlig nod.


![Image](assets/fr/06.webp)


### Ansluta till en Bitcoin Core 🟢


Den andra metoden för att ansluta till en Bitcoin-nod är att länka Sparrow till en Bitcoin Core. Om Bitcoin Core är installerat på samma maskin sker autentiseringen via cookie-filen. Om Bitcoin Core finns på en fjärrmaskin måste du använda det lösenord som definieras i filen `Bitcoin.conf`.


Observera att om du använder en beskuren Bitcoin Core-nod kommer du inte att kunna återställa en Wallet som innehåller transaktioner som föregår de lokalt lagrade blocken. För en ny Wallet som skapats på Sparrow är detta dock inget problem: dina nya transaktioner kommer att vara synliga, även med en beskuren nod.


För att konfigurera en Bitcoin Core-nod kan du läsa någon av följande handledningar, beroende på operativsystem:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

På Sparrow, gå till fliken "*Bitcoin Core*".


![Image](assets/fr/07.webp)


**Med Bitcoin Core local:**


Om Bitcoin Core är installerat på din dator, leta reda på filen `Bitcoin.conf` bland programvarufilerna. Om den här filen inte finns kan du skapa den. Öppna den med en textredigerare och infoga följande rad:


```ini
server=1
```


Spara sedan dina ändringar.


Du kan också göra detta via Bitcoin-QT:s Interface-grafik genom att navigera till "*Inställningar*" > "*Options...*" och aktivera alternativet "*Enable RPC server*".


Glöm inte att starta om programvaran efter att du har gjort dessa ändringar.


![Image](assets/fr/08.webp)


Gå sedan tillbaka till Sparrow wallet och ange sökvägen till din cookie-fil, som vanligtvis finns i samma mapp som `Bitcoin.conf`, beroende på ditt operativsystem:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


Lämna de andra parametrarna som standard, URL `127.0.0.1` och port `8332`, och klicka sedan på "*Test Connection*".


![Image](assets/fr/10.webp)


Anslutningen är upprättad. En Green-fästing visas i det nedre högra hörnet för att ange att du är ansluten till en Bitcoin Core-nod.


![Image](assets/fr/11.webp)


**Med Bitcoin Core fjärrkontroll:**


Om Bitcoin Core är installerad på en annan maskin som är ansluten till samma nätverk, leta först upp filen `Bitcoin.conf` bland programfilerna. Om filen ännu inte finns kan du skapa den. Öppna filen med en textredigerare och lägg till följande rad:


```ini
server=1
```


När du har redigerat filen ska du se till att spara den i rätt mapp för ditt operativsystem:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

Denna operation kan också utföras via Bitcoin-QT Interface grafiska Interface. Gå till menyn "*Settings*", sedan "*Options...*" och aktivera alternativet "*Enable RPC server*" genom att markera motsvarande ruta. Om filen `Bitcoin.conf` inte finns, kan du skapa den direkt från denna Interface genom att klicka på "*Open Configuration File*".


![Image](assets/fr/12.webp)


Hitta IP Address för den maskin som är värd för Bitcoin Core i ditt lokala nätverk. För att göra detta kan du använda ett verktyg som [Angry IP Scanner] (https://angryip.org/). Låt oss anta, för argumentets skull, att IP Address för din nod är `192.168.1.18`.


I filen `Bitcoin.conf` lägger du till följande rader och ställer in `rpcbind=192.168.1.18` så att den matchar IP Address för din nod.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


I filen `Bitcoin.conf` lägger du till ett användarnamn och lösenord för fjärranslutningar. Se till att ersätta `loic` med ditt användarnamn och `my_password` med ett starkt lösenord:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


När du har ändrat och sparat filen startar du om programvaran Bitcoin-QT.


Du kan nu återvända till Sparrow wallet. Gå till fliken "*User / Pass*". Ange det användarnamn och lösenord som du konfigurerade i filen `Bitcoin.conf`. Lämna de andra parametrarna som standard, dvs URL `127.0.0.1` och port `8332`. Klicka sedan på "*Test Connection*".


![Image](assets/fr/15.webp)


Anslutningen är upprättad. En Green-bock visas i det nedre högra hörnet för att ange att du är ansluten till en Bitcoin Core-nod.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### Ansluta till en Electrum-server 🔵


Det sista alternativet för att ansluta är att använda en fjärrserver för Electrum. Med den här metoden kan du ansluta till din nod via Tor från en annan enhet och dra nytta av en indexerare för att bläddra igenom dina plånböcker på Sparrow snabbare. Det är särskilt lämpligt om du har en node-in-a-box-lösning som Umbrel eller Start9, som låter dig installera Electrum med ett enda klick.


För att göra detta, skaffa Tor `.onion' Address för din Electrum-server. Med Umbrel, till exempel, hittar du den i Electrs applikation.


![Image](assets/fr/17.webp)


På Sparrow wallet, gå till fliken "*Private Electrum*".


![Image](assets/fr/18.webp)


Ange din Tor Address i det utrymme som tillhandahålls. Andra inställningar kan förbli standard. Klicka sedan på "*Test Connection*".


![Image](assets/fr/19.webp)


Anslutningen är bekräftad. Om du stänger det här fönstret visas en blå bock i det nedre högra hörnet, vilket indikerar att du är ansluten till en Electrum-server.


![Image](assets/fr/20.webp)


## Skapa en Hot Wallet


Nu när Sparrow wallet är konfigurerad för att kommunicera med Bitcoin-nätverket är du redo att skapa din första Wallet. Det här avsnittet guidar dig genom skapandet av en Hot Wallet, dvs. en Wallet vars privata nycklar lagras på din dator. Eftersom din dator är en komplex maskin som är ansluten till Internet utgör den en mycket stor attackyta. Följaktligen bör en Hot Wallet endast användas för begränsade mängder bitcoins. För att lagra större belopp, välj en säker Wallet med en Hardware Wallet. Om det här är vad du letar efter kan du hoppa vidare till nästa avsnitt.


För att skapa en Hot Wallet, klicka på fliken "*File*" från Sparrow wallet:s startskärm och sedan på "*New Wallet*".


![Image](assets/fr/21.webp)


Ange ett namn för din Wallet och klicka på "*Create Wallet*".


![Image](assets/fr/22.webp)


Längst upp på Interface kan du välja om du vill skapa en "*Single Signature*" eller "*Multi Signature*" Wallet. Strax nedanför väljer du vilken typ av skript som ska låsa dina UTXO:er. Jag rekommenderar att du använder den senaste standarden: "*Taproot (P2TR)*".


![Image](assets/fr/23.webp)


Klicka sedan på "*Ny eller importerad Software Wallet*".


![Image](assets/fr/24.webp)


Välj BIP39-standarden, eftersom den stöds av praktiskt taget all Bitcoin Wallet-programvara. Välj sedan längden på din återställningsfras. För närvarande räcker det med en 12-ordsfras, eftersom båda erbjuder liknande säkerhet, men 12-ordsfrasen är enklare att spara.


![Image](assets/fr/25.webp)


Klicka på knappen "*generate New*" för att generate din Wallet:s Mnemonic-fras. Denna fras ger full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har tillgång till den här frasen kan stjäla dina pengar, även utan fysisk tillgång till din dator.


Den 12 ord långa frasen återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din dator. Det är därför mycket viktigt att spara den noggrant och förvara den på ett säkert ställe.


Du kan gravera den på papper eller, för ökad säkerhet, gravera den på rostfritt stål för att skydda den mot brand, översvämning eller kollaps. Valet av medium för din Mnemonic beror på din säkerhetsstrategi, men om du använder Sparrow som en varm utgift för Wallet som innehåller måttliga mängder bör papper vara tillräckligt.


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**Självklart får du aldrig dela dessa ord på Internet, som jag gör i denna handledning. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**


Du kan också välja att lägga till en passphrase BIP39 genom att klicka på rutan "*Use passphrase*". Varning: att använda en passphrase kan vara mycket användbart, men om du inte förstår hur den fungerar kan det vara mycket riskabelt. Därför rekommenderar jag starkt att du läser den här korta teoretiska artikeln om ämnet:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

När du har sparat din Mnemonic och alla passphrase till ett fysiskt medium klickar du på "*Bekräfta säkerhetskopiering*".


![Image](assets/fr/27.webp)


Skriv in dina 12 ord igen för att bekräfta att de har sparats korrekt och klicka sedan på "*Create Keystore*".


![Image](assets/fr/28.webp)


Klicka sedan på "*Importera Keystore*" för att generate dina Wallet-nycklar från Mnemonic-frasen.


![Image](assets/fr/29.webp)


Klicka på "*Apply*" för att slutföra skapandet av Wallet.


![Image](assets/fr/30.webp)


Ange ett starkt lösenord för att säkra åtkomsten till din Sparrow wallet. Det är en bra idé att spara lösenordet i en lösenordshanterare så att du inte glömmer det. Observera att detta lösenord inte spelar någon roll vid härledningen av dina nycklar. Det används endast för att komma åt din Wallet via Sparrow wallet. Så även utan det här lösenordet räcker din Mnemonic-fras för att komma åt dina bitcoins från alla BIP39-kompatibla applikationer.


![Image](assets/fr/31.webp)


Din Hot Wallet är nu skapad. Du kan hoppa till avsnittet *Mottagning av bitcoins* i denna handledning om du inte planerar att använda en Hardware Wallet med Sparrow.


## Hantering av en Cold Wallet


Det andra sättet att använda Sparrow wallet är att konfigurera den som en Wallet-hanterare med en Hardware Wallet. I den här konfigurationen finns de privata nycklarna för dina Bitcoin Wallet uteslutande på Hardware Wallet, medan Sparrow endast har åtkomst till den offentliga informationen. Detta tillvägagångssätt erbjuder en högre säkerhetsnivå än de Hot-plånböcker som diskuteras ovan, eftersom de privata nycklarna förvaras på en specialiserad enhet, ofta med ett säkert chip, som inte är ansluten till Internet och därför utgör en mycket mindre attackyta än en traditionell dator.


Det finns två huvudsakliga sätt att ansluta din Hardware Wallet till Sparrow:




- Med kabel, används vanligtvis med nybörjarmodeller som Trezor Safe 3 eller Ledger Nano S Plus ;
- I Air-Gap-läge, dvs. utan direkt kabelanslutning, via ett MicroSD-kort eller QR-kod Exchange.


Sparrow stöder alla dessa kommunikationsmetoder och är kompatibel med de flesta hårdvaruplånböcker på marknaden.


I den här handledningen använder jag en Ledger Nano S med en kabel, men proceduren är liknande i Air-Gap-läge. Du hittar detaljer som är specifika för din Hardware Wallet i dess dedikerade handledning om Plan ₿ Network.


Innan du börjar ska du kontrollera att Wallet redan är konfigurerad på din Hardware Wallet. Om du använder en trådbunden anslutning ansluter du den till datorn via kabeln.


För att importera den så kallade "*Keystore*" (den offentliga information som behövs för att hantera Wallet) till Sparrow wallet, klicka på fliken "*File*" och sedan på "*New Wallet*".


![Image](assets/fr/32.webp)


Namnge din Wallet och klicka på "*Create Wallet*". Jag råder dig att ange namnet på din Hardware Wallet för att enkelt kunna identifiera den senare.


![Image](assets/fr/33.webp)


På toppen av Interface kan du välja mellan "*Single Signature*" eller "*Multi Signature*" Wallet. I vårt exempel kommer vi att konfigurera en Wallet med en enda signatur.


Precis nedanför väljer du vilken typ av skript som ska låsa dina UTXO:er. Om din Hardware Wallet stöder det föreslår jag att du väljer "*Taproot (P2TR)*".


![Image](assets/fr/34.webp)


Därefter skiljer sig proceduren åt beroende på din anslutningsmetod. Om du använder en Air-Gap-metod väljer du "*Airgapped Hardware Wallet*". Följ sedan instruktionerna som är specifika för din enhet.


![Image](assets/fr/35.webp)


Om du använder en kabelanslutning, som i mitt fall, väljer du "*Connected Hardware Wallet*".


![Image](assets/fr/36.webp)


Klicka på "*Scan*" för att Sparrow ska upptäcka din enhet. Kontrollera att den är inkopplad och upplåst. För vissa modeller, t.ex. Ledger, måste du öppna programmet "*Bitcoin*" för att aktivera detektering.


![Image](assets/fr/37.webp)


Välj "*Importera nyckelförvaring*".


![Image](assets/fr/38.webp)


Klicka på "*Apply*" för att slutföra skapandet av Wallet.


![Image](assets/fr/39.webp)


Ange ett starkt lösenord för att säkra åtkomsten till din Sparrow wallet. Detta lösenord skyddar dina publika nycklar, adresser och transaktionshistorik. Vi rekommenderar att du sparar det i en lösenordshanterare. Observera att det här lösenordet inte spelar någon roll i härledningen av dina nycklar. Även utan det kan du återfå åtkomst till dina bitcoins med din Mnemonic via valfri BIP39-kompatibel programvara.


![Image](assets/fr/40.webp)


Din hantering Wallet är nu konfigurerad på Sparrow.


![Image](assets/fr/41.webp)


## Ta emot bitcoins


Nu när din Wallet är konfigurerad på Sparrow kan du ta emot bitcoins. Öppna helt enkelt menyn "*Motta*".


![Image](assets/fr/42.webp)


Sparrow kommer att visa den första oanvända Address i din Wallet. Du kan lägga till en "*Label*" till denna Address för att påminna dig om ursprunget till dessa satoshis i framtiden.


![Image](assets/fr/43.webp)


Om du använder en Hot Wallet kan den Address som visas användas omedelbart, antingen genom att kopiera den eller genom att skanna den tillhörande QR-koden.


Om du använder en Hardware Wallet är det mycket viktigt att du kontrollerar Address på enhetens skärm innan du använder den. För trådbundna enheter, anslut och lås upp din Hardware Wallet och klicka sedan på "*Display Address*" i Sparrow. Se till att den Address som visas på din Hardware Wallet matchar den som visas på Sparrow.


![Image](assets/fr/44.webp)


För Hardware Wallet Air-Gap-användare varierar Address-verifieringen beroende på enhetsmodell. Se den dedikerade Plan ₿ Network-handledningen för exakta instruktioner.


När betalaren har sänt transaktionen visas den på fliken "*Transaktioner*". Du kan klicka på den för att få mer information, till exempel txid.


![Image](assets/fr/45.webp)


På fliken "*Addresser*" finns en lista över alla dina inkorgsadresser. Du kan se om de redan har använts och om en etikett har lagts till. *Adresserna "Receive*" är de som Sparrow visar när du klickar på "*Receive*" och är avsedda för inkommande betalningar. Adresserna "*Change*" används för Exchange i dina transaktioner, dvs. för att återvinna den oanvända delen av dina UTXO:er i ingångar.


![Image](assets/fr/46.webp)


Fliken "*UTXOs*" visar alla dina UTXO:er, dvs. de Bitcoin-fragment som du innehar. Du kan se mängden av varje UTXO och den tillhörande etiketten.


![Image](assets/fr/47.webp)


## Skicka bitcoins


Nu när du har några satoshis i din Wallet har du också möjlighet att skicka några. Även om det finns flera sätt att göra detta på rekommenderar jag att du använder menyn "*UTXOs*" för mer exakt kontroll över de mynt du spenderar (*coin control*), snarare än att gå direkt till menyn "*Send*" (även om det senare kan räcka om du är nybörjare).


![Image](assets/fr/48.webp)


Välj de UTXO som du vill använda som ingångar för den här transaktionen och klicka sedan på "*Send Selected*". På så sätt kan du välja de lämpligaste källorna bland dina UTXO:er, beroende på dina utgifter och de etiketter som används när de tas emot, för att optimera sekretessen för dina betalningar. Se till att summan av de valda UTXO:erna är större än det belopp som du vill skicka.


![Image](assets/fr/49.webp)


Ange mottagarens Address i fältet "*Pay to*". Du kan också skanna Address med din webbkamera genom att klicka på kameraikonen. Med knappen "*+Add*" kan du betala flera adresser i en och samma transaktion.


![Image](assets/fr/50.webp)


Lägg till en etikett på din transaktion för att påminna dig om dess syfte. Denna etikett kommer också att associeras med din eventuella Exchange.


![Image](assets/fr/51.webp)


Ange det belopp som ska skickas till denna Address.


![Image](assets/fr/52.webp)


Justera avgiftssatsen efter rådande marknadsförhållanden. Du kan göra detta genom att ange ett absolut avgiftsvärde eller genom att justera avgiftssatsen med skjutreglaget.


![Image](assets/fr/53.webp)


Längst ned på Interface kan du välja mellan "*Efficiency*" och "*Privacy*". I mitt fall är alternativet "*Privacy*" inte tillgängligt, eftersom jag bara har en UTXO i denna Wallet. "*Efficiency*" motsvarar en klassisk transaktion, medan "*Privacy*" är en transaktion av Stonewall-typ, en transaktionsstruktur som förstärker din sekretess genom att simulera en mini-CoinJoin, vilket gör kedjeanalysen mer komplex.


![Image](assets/fr/54.webp)


Sparrow visar ett sammanfattande diagram som visar dina inmatningar, utmatningar och transaktionsavgifter (observera att avgifter faktiskt inte är en utmatning, i motsats till vad detta diagram antyder). Om du är nöjd med allt klickar du på "*skapa transaktion*".


![Image](assets/fr/55.webp)


Detta tar dig till en sida som beskriver Elements för din transaktion. Kontrollera att all information är korrekt och klicka sedan på "*Finalize Transaction for Signing*".


![Image](assets/fr/56.webp)


Det är viktigt att behålla Sighash som standard. För att förstå varför, ta en titt på den här utbildningen, där jag förklarar allt du behöver veta om Sighash:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

På nästa skärm varierar alternativen beroende på vilken typ av Wallet du använder:




- För en Hardware Wallet Air-Gap, klicka på "*Show QR*" för att visa en PSBT som du kan signera med din enhet, ladda sedan den signerade PSBT till Sparrow med "*Scan QR*". Alternativet "*Save Transaction*" fungerar på liknande sätt, men med utbyten på ett microSD;
- För en Hot Wallet klickar du bara på "*Signera*" och anger lösenordet för Wallet för att signera;
- För en trådbunden Hardware Wallet klickar du även på "*Signera*" för att skicka den osignerade transaktionen till din enhet.


![Image](assets/fr/57.webp)


På din Hardware Wallet kontrollerar du mottagarens Address, det skickade beloppet och avgifterna. Om allt är korrekt går du vidare med underskriften.


När transaktionen har signerats visas den på nytt i Sparrow, redo att sändas ut i Bitcoin-nätverket för att därefter inkluderas i ett block. Om allt är korrekt klickar du på "*Broadcast Transaction*".


![Image](assets/fr/58.webp)


Din transaktion är nu sänd och väntar på bekräftelse.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Hantera och konfigurera plånböcker på Sparrow


På fliken "*Settings*" hittar du detaljerad information om din Wallet, t.ex:



- Portföljtyp (single-sig eller multi-sig) ;
- Typ av skript som används ;
- Det namn som du har tilldelat Wallet ;
- Huvudnyckelavtryck;
- Förbikopplingsvägen ;
- Kontots utökade publika nyckel.


![Image](assets/fr/60.webp)


Med knappen "*Export*" kan du exportera din Wallet-information så att du kan använda den i andra program samtidigt som du behåller den information som ställts in i Sparrow.


Med knappen "*Add Account*" kan du lägga till ytterligare ett konto i din Wallet. Ett konto motsvarar en separat uppsättning inkorgsadresser. Den här funktionen kan vara användbar om du t.ex. vill separera ett personligt konto och ett företagskonto med en enda Mnemonic-fras.


Knappen "*Avancerat*" ger tillgång till avancerade inställningar, t.ex. anpassning av Sparrow:s Address-sökning och ändring av Wallet-lösenordet.


![Image](assets/fr/61.webp)


När du stänger Sparrow wallet låses din Wallet automatiskt. Nästa gång du öppnar programvaran kommer ett fönster att uppmana dig att låsa upp din Wallet med dess lösenord.


![Image](assets/fr/62.webp)


Om detta fönster inte öppnas, eller om du vill öppna en annan Wallet på Sparrow, klickar du på fliken "*File*" och väljer "*Open Wallet*".


![Image](assets/fr/63.webp)


Detta kommer att öppna din filhanterare till mappen där Sparrow lagrar dina plånböcker. Välj bara den Wallet som du vill öppna och ange lösenordet för att låsa upp den.


![Image](assets/fr/64.webp)


I menyn "*File*" under "*Settings*" hittar du Bitcoin:s parametrar för nätverksanslutning som redan har utforskats i tidigare avsnitt. Du kan också justera olika parametrar som t.ex. den enhet som används, fiat-valuta för konverteringar och informationskällor.


![Image](assets/fr/65.webp)


Fliken "*View*" erbjuder anpassningsalternativ och tillgång till några användbara kommandon, t.ex. "*Refresh Wallet*", som uppdaterar transaktionssökningen för din Wallet.


![Image](assets/fr/66.webp)


Fliken "*Tools*" samlar flera avancerade verktyg, bland annat :



- med "*Sign/Verify Message*" kan du bevisa innehav av en mottagande Address eller verifiera en signatur.
- "*Send To Many*" erbjuder en förenklad Interface för att utföra transaktioner till flera mottagningsadresser samtidigt, vilket är bekvämt för batchutgifter.
- "*Sweep Private Key*" gör att du kan hämta bitcoins som skyddas av en enkel privat nyckel och överföra dem till din Sparrow wallet. Detta kan vara särskilt användbart för dem som har bitcoins från början av 2010-talet, före HD-plånböckerna.
- "Verify Download" verifierar integriteten och äktheten hos den nedladdade programvaran innan den installeras på din enhet.
- "*Restart In*" gör att du kan växla till dina plånböcker på Testnet eller Signet-nätverk. Detta kan vara användbart om du vill komma åt testnätverk med mynt som inte har något verkligt värde.


![Image](assets/fr/67.webp)


Du känner nu till allt om Sparrow wallet-programvaran, ett utmärkt verktyg för att hantera dina Bitcoin-plånböcker på daglig basis.


Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green tumme nedan. Dela gärna det på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också den här andra handledningen där jag förklarar hur man konfigurerar Hardware Wallet COLDCARD Q med Sparrow wallet :


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3