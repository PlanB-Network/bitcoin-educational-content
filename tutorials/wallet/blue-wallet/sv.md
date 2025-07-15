---
name: Blå Wallet

description: Bitcoin Radikalt enkel och kraftfull portfölj
---
![cover](assets/cover.webp)



Att komma igång med Bitcoin verkar vara en stor utmaning för människor som är skeptiska till enkelheten i dess användning. Att hitta rätt verktyg för att säkerställa denna enkelhet blir därför av största vikt för att Bitcoin bättre ska kunna användas som ett medium för Exchange och inte bara som en värdebevarare.



I den här handledningen tittar vi på Blue Wallet, en enkel men mycket effektiv Bitcoin Wallet som låter dig hantera dina bitcoins personligen och även skapa förvaltningskooperativ baserat på [Multisig] (https://planb.network/resources/glossary/Multisig) (oroa dig inte, vi kommer tillbaka till det).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Komma igång med Blue Wallet



Blue Wallet är en självhanterande Bitcoin Wallet med öppen källkod som låter dig ta kontroll över dina bitcoins. Den finns tillgänglig som en mobilapp på både Android- och iOS-plattformar. I den här handledningen kommer vi att basera oss på Android-versionen, men alla processer som kommer att utvecklas är lika giltiga på iOS.



![download](assets/fr/01.webp)



⚠️ Se till att ladda ner Blue Wallet Bitcoin Wallet-applikationen på en officiell plattform för att garantera dess äkthet och skydda dina bitcoins från eventuella läckor och hack.



När du har installerat den kan du skapa en ny Wallet och spara de 12 återställningsorden, eller importera en befintlig Bitcoin Wallet. Ta reda på hur du gör en effektiv säkerhetskopia av dina nyckelord så att du inte förlorar tillgången till dina bitcoins.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Med Blue Wallet kan du skapa separata, dedikerade Bitcoin-portföljer. Du kan till exempel ha en Wallet för dina besparingar och en annan för dina dagliga utgifter, allt i samma applikation.



![home](assets/fr/02.webp)



## Portföljtyper



I Blue Wallet hittar du två inhemska Bitcoin-portföljtyper.



### Bitcoin-portföljen



Om du är van vid andra Bitcoin-portföljer som Phoenix eller Aqua kommer du inte alls att vara i otakt på Interface med Blue Wallet:s Bitcoin-portfölj.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blå Wallet:s Bitcoin Wallet representerar standard Wallet i Bitcoin:s ekosystem. Du kan spendera bitcoins så länge du har tillgång till återvinningsorden som ger en giltig signatur i nätverket för att verifiera att du äger bitcoins.



För att skapa en Bitcoin-portfölj klickar du på knappen **Lägg till nu**, anger namnet på din portfölj och väljer typen Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



När du klickar på förhandsgranskningen av din Bitcoin Wallet kan du se din transaktionshistorik och skicka och ta emot bitcoins.



⚠️ Alla transaktioner i din Bitcoin Wallet är på Bitcoin-protokollets huvudkedja (Mainnet).





- Att ta emot bitcoins med Bitcoin Blue Wallet Wallet är intuitivt. Längst ner på skärmen klickar du på knappen **Receive**. Dela QR-koden eller din Bitcoin Address med din avsändare så att de kan skicka bitcoins till dig.



Du kan också konfigurera ett fördefinierat belopp för att ange hur mycket Bitcoin du vill ta emot.



![receive-bitcoin](assets/fr/04.webp)





- På **Send**-knappen skickar du bitcoins till en Bitcoin Address, ställer in önskat belopp och validerar transaktionen.



![send-bitcoin](assets/fr/05.webp)



Med Blue Wallet kan du konfigurera parametrarna för din Bitcoin-leverans som du vill.



Du kan därför välja det transaktionsavgiftsförhållande som passar dig om du vill att din transaktion snabbt ska valideras i en Mempool och inkluderas i ett block av miners. Beroende på vilket förhållande du väljer kommer miners att prioritera din transaktion i större eller mindre utsträckning. Ta reda på mer i vår handledning om Mempool Space.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Med Blue Wallet kan du lägga till flera mottagare i en och samma försändelse.



När du lägger till Bitcoin Address för din första mottagare, i alternativen, klicka på **Lägg till mottagare**, lägg till Bitcoin Address och ställ sedan in beloppet som ska skickas till den här mottagaren, och så vidare. Blue Wallet kommer att skicka bitcoins för flera leveranser baserat på din enda åtgärd.



![add-recipients](assets/fr/07.webp)



Du kan ta bort en eller alla mottagare genom att klicka på **Remove Recipient** respektive **Remove All Recipents**.



![remove-recipient](assets/fr/08.webp)





- Uppblåsta avgifter**: Har du gjort en transaktion som det tar lång tid att få bekräftad? Genom att aktivera avgiftsinflation kan du lägga till ytterligare transaktionsavgifter till din väntande transaktion för att påskynda dess bekräftelse.



![bumping](assets/fr/09.webp)



### Multisig Portfölj



Multisig (multisignatur) Wallet representerar en Wallet som skapats genom gruppering av ett visst antal (minst 2) Bitcoin-plånböcker. I denna typ av Wallet, beroende på vilken konfiguration och metod som väljs, blir utgifterna för bitcoins en kollektiv och kooperativ handling.



I Blue Wallet kan du skapa portföljer med flera signaturer för din förening, din familj eller ditt företag. I det här avsnittet kommer vi att utforska alla aspekter av denna speciella typ av portfölj.



Lägg till en ny portfölj och välj typ **Multisig Vault** för att skapa en portfölj med flera signaturer.



![multisig-vault](assets/fr/10.webp)



Definiera m-de-n-konfigurationen i din organisation med flera signaturer genom att klicka på **Vault Settings**.



⚠️ I en m-av-n-konfiguration representerar **m** det minsta antal signaturer som krävs för att godkänna en transaktion och **n** antalet portföljer i din organisation.



Var noga med att definiera ett minsta antal signaturer (m) för majoriteten av din organisation. Till exempel kräver en 2-av-3-konfiguration med flera signaturer att två plånböcker i din organisation signerar transaktionen innan den kan utföras.



❗ Att definiera en m-av-n-konfiguration där n är lika med m är en stor risk. När en medlem förlorar tillgången till sin Wallet förlorar du behörigheten att spendera bitcoins i Wallet.



Här är några exempel på optimala konfigurationer för att säkerställa säkerhet och tillgänglighet till bitcoins:





- 2-de-3 multi signatur.





- 5-de-7 multi signatur.



![vault-settings](assets/fr/11.webp)



Håll dig till bästa praxis genom att välja P2WSH-formatet.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) eller Pay to Witness Script Hash** är en låsmetod som låser din transaktions utgående bitcoins (Outputs) till Hash i ett anpassat skript som Blue Wallet sätter upp. Den största fördelen med denna typ av låsning är att den minskar transaktionsdatastorleken och implicit gör att du kan betala lägre transaktionsavgifter.



Skapa eller importera var och en av de **n** portföljerna i din konfiguration. I vår handledning kommer vi att använda en 2-av-3 multisignaturkonfiguration. Se till att spara återställningsorden för varje portfölj individuellt.



![vault-keys](assets/fr/12.webp)





- Ta emot bitcoins



På din Multisig Wallet-sida hittar du din transaktionshistorik och knapparna Receive och Send.



Att ta emot bitcoins i en multi-signatur Wallet är samma process som när du är i en standard Bitcoin Wallet.





- Skicka bitcoins** :



Genom att hantera en Wallet med flera signaturer blir utgifterna för bitcoins en sammansatt åtgärd, oavsett om det är med andra människor eller en andra egen Wallet. Den enda signaturen för din Wallet är inte längre tillräcklig. Detta ger dina bitcoins en Layer av säkerhet, eftersom en illvillig individ inte kommer att kunna spendera dessa bitcoins när han kommer i besittning av bara en av dina privata nycklar.



Precis som med standardportföljen Bitcoin för Blue Wallet kan du ange flera mottagare i alternativet **Lägg till mottagare**.



När du validerar din transaktion behöver du en andra signatur för att godkänna utgifterna för bitcoins. Kom ihåg att vi är i en 2-de-3 multisignaturkonfiguration.



Den andra Wallet-signatören, om han eller hon också är en användare, kan signera transaktionen även om han eller hon inte är uppkopplad mot internet (inget Wi-Fi, ingen mobildata) genom att skanna QR-koden för den [delvis signerade transaktionen] (https://planb.network/resources/glossary/PSBT) som du just har skapat.



![mutisig-send](assets/fr/13.webp)





- Gå längre med portföljen Multi signature**:



På Interface i din Wallet med flera signaturer klickar du på knappen **Hantera nycklar**.



Genom att glömma ett av återställningsorden för en av de undertecknande portföljerna (**Glöm detta seed...**), meddelar du Blue Wallet att radera säkerhetskopian av dessa ord från dess minne. Du kommer därför att ha gjort en extern säkerhetskopia.



![revoke-key](assets/fr/14.webp)



Genom att utföra denna åtgärd behåller du endast den offentliga nyckel som är kopplad till dessa återställningsord.



⚠️ Genom att bara spara offentliga nycklar (XPUB) kan du lägga till en extra säkerhetsnivå i din 2-av-3-konfiguration med flera signaturer. Det kan faktiskt vara skadligt att hålla alla återställningsord på ett ställe när din telefon är under attack. Angripare med tillgång till endast en **VAULT** (nyckelord) som du använder för att signera dina transaktioner kommer inte att kunna stjäla dina bitcoins (minst 02 signaturer krävs) eftersom offentliga nycklar inte kan användas för att signera transaktioner.



## Fler alternativ med Blue Wallet



### Förbättra säkerheten för portföljåtkomst



I Inställningar, alternativet **Säkerhet** kan du definiera användningen av ett fingeravtryck för att utföra en transaktion, exportera eller radera din Wallet. Detta autentiserar den person som använder din smartphone.



![biometry](assets/fr/15.webp)



## Aktivera Lightning Network



Lightning Network har inte längre något inbyggt stöd i Blue Wallet-applikationen.



I Inställningar > **Lightning-inställningar** kan du manuellt associera din Lightning Wallet när du kör en Lightning Network Daemon (LND)-nod. Installera LND Hub och associera sedan din Wallet genom att ange länken som genereras av hubben.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Du har nu slutfört den blå Wallet-turnén och är redo att använda Bitcoin i all sin enkelhet och kraft. Vi rekommenderar att du tar nästa steg och tar reda på hur du kan acceptera Bitcoin-betalningar i dina butiker tack vare kraften i Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06