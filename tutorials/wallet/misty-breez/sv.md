---
name: Misty Breez
description: Den bågformade blixten Wallet.
---

![misty-breez-cover](assets/cover.webp)



![video](https://youtu.be/mibKrTvtlyQ)


Misty Breez är en Lightning self-holding Wallet som utvecklats av Breez baserat på deras Software Development Kit och **Liquid**-nätverket som utvecklats av BlockStream.


Den levereras med ett helt nytt tillvägagångssätt för att fungera utan en Lightning-nod: en potentiell **GAME CHANGER** i Bitcoin-internätverksöverföringar.


I denna handledning beskriver vi hur denna Wallet fungerar och ger dig en fullständig översikt.



## Hur fungerar Misty Breez?



Misty Breez är en implementation utan en Lightning-nod som backend. Den har utvecklats på grundval av Breez SDK och Liquid.



Liquid är en parallell Layer till Bitcoin-nätverket och erbjuder betydande förbättringar i hastighet och transaktionskostnader. Denna Layer gör det möjligt för Misty Breez att avstå från en Lightning-nod och istället använda Exchange-tjänster från tredje part som **Boltz** för att säkerställa interoperabilitet mellan Liquid Network och Lightning Network. Skynda dig inte, vi kommer tillbaka till detta.



Låt oss nu börja vårt äventyr med Misty Breez Wallet.



## Komma igång med Misty Breez



Misty Breez mobilapp finns tillgänglig på officiella nedladdningsplattformar som Google Play Store (på Android) och Apple Store (på iOS). Du kan också omdirigeras till rätt app från den officiella [Misty Breez] webbplatsen (https://breez.technology/misty/).



⚠️ Se till att du inte förväxlar Misty Breez med Breez Wallet.



⚠️ **VIKTIGT**: För säkerheten för dina bitcoins är det viktigt att ladda ner applikationen från officiella plattformar för att säkerställa dess äkthet.



![download-misty-breez](assets/fr/01.webp)



I den här handledningen utgår vi från en Android-enhet. Alla steg och specifika funktioner som beskrivs i det här avsnittet gäller dock även för iOS.



Vid installationen ger Misty Breez dig möjlighet att skapa en ny Wallet eller återställa en gammal Lightning Wallet som du har återställningsorden för.


I den här handledningen väljer vi att skapa en ny Wallet.



⚠️Misty Breez befinner sig för närvarande i utvecklingsfasen, så vi rekommenderar att du börjar med rimliga mängder.



![create-wallet](assets/fr/02.webp)


### Spara dina återhämtningsord :


En av de första sakerna du bör göra när du skapar en ny Wallet är att säkerhetskopiera dina 12 återhämtningsord.


Här är några tips om hur du säkerhetskopierar din säkerhetskopieringsfras.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

För att säkerhetskopiera dina fraser väljer du menyn **Inställningar > Säkerhet** och sedan alternativet **Kontrollera din säkerhetskopierade fras**.



![backup](assets/fr/03.webp)


För ökad säkerhet kan du också **skapa en PIN-kod** för att verifiera åtkomst till din Wallet.




Hitta din lokala valuta bland de många valutor som Misty Breez accepterar. Konfigurera din valuta från menyn **Inställningar > Fiatvalutor** och välj sedan den eller de valutor du behöver.



![devises](assets/fr/04.webp)



### Gör dina första transaktioner


Om du redan är bekant med Breez Wallet kommer du inte alls att bli avskräckt av Misty Breez intuitiva Interface.



På menyn Interface **Balance** klickar du på alternativet **Receive** för att skapa fakturor för att ta emot dina bitcoins på din Wallet.



⚠️ Misty Breez kommer att be dig att aktivera aviseringar för applikationen i telefonens inställningar för att ge dig rätt till en Lightning Address.



Med Misty Breez kan du :




- Ta emot bitcoins på Lightning Network från **100 satoshis** upp till **25 000 000 satoshis**.
- Ta emot bitcoins på Bitcoin:s huvudnätverk från **25 000 satoshis**.



![transactions](assets/fr/05.webp)



Det är här som magin med Misty Breez börjar.


Till skillnad från Breez Wallet, som förser dig med en Lightning-nod och ber dig att själv täcka kostnaderna för att öppna och stänga betalningskanaler, ber Misty Breez dig inte att göra någonting. Som tidigare nämnts fungerar Misty Breez inte ens på grundval av en Lightning-nod.



Låt oss ta en närmare titt bakom kulisserna.



I verkligheten äger du en Liquid Wallet som är associerad med din Misty Breez Wallet. Logiskt sett kommer du att hantera L-BTC (Liquid Bitcoin) till fasta kurser som är kopplade till tredje parts konverteringstjänster för ubåtssatoshis som gör att du kan samverka med Lightning Network.



När du får en betalning på din Misty Breez Wallet skickar din avsändare satoshis till dig som kommer att gå igenom en konverteringstjänst som Boltz (som för närvarande används av Misty Breez), för att konvertera de skickade satoshis till L-BTC som kommer att tas emot på din Misty Breez Wallet (associerad Liquid Wallet).


Här är ett förenklat diagram över processen bakom kulisserna.



![lnswap-in](assets/fr/06.webp)



Klicka på Interface i menyn **Balans**, klicka på alternativet **Sänd** för att betala en blixt Invoice.


Sätt i Lightning Invoice, din mottagares Lightning Address eller skanna QR-koden på Invoice för att göra din betalning.



![send-bitcoins](assets/fr/07.webp)



Bakom kulisserna aktiverar du Liquid Wallet som är associerad med din Misty Breez Wallet för att konvertera motsvarande L-BTC till satoshis via Boltz, och överför sedan dessa satoshis till din mottagares Lightning Wallet (som finns på Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Denna funktion i Misty Breez infrastruktur gör det möjligt för användare att genomföra transaktioner även när Misty Breez är offline.



För de mer erfarna finns det också en meny **Preferences > Developers** som ger dig lite mer information om :




- Versionen av Breez Software Development Kit.
- Den publika nyckeln för din Misty Breez Wallet.
- Låntagaren, den unika identifieraren som härleds från den primära publika nyckeln.
- Din Wallet-balans.
- Tips Liquid, för att skicka små mängder L-BTC.
- Bitcoin-tipset, för att skicka små mängder Bitcoin.



Du kan också utföra vissa åtgärder, t.ex. synkronisera med Liquid Network, säkerhetskopiera dina nycklar, dela din aktivitetslogg och välja att skanna om Liquid Network.



![dev-mode](assets/fr/09.webp)


Gratulerar till detta! Du har nu en god förståelse för Misty Breez Wallet och dess bidrag till Bitcoin-transaktioner mellan nätverk. Om du har funnit denna handledning användbar, vänligen ge oss en Green tumme. Vi skulle bli glada att höra från dig.



För att gå vidare rekommenderar jag också att du upptäcker vår handledning om Aqua Wallet, som fungerar på ett liknande sätt som Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125