---
name: Boltz
description: Byt mellan olika Bitcoin-lager samtidigt som du behåller kontrollen.
---


![cover](assets/cover.webp)



Sedan lanseringen 2009 har Bitcoin:s peer-to-peer-system för elektroniska kontanter vuxit exponentiellt och gett upphov till lösningar som idag gör det möjligt att använda systemet direkt i vår vardag, framför allt genom Lightning Network.



Det återstod dock ett stort problem mellan Bitcoin-protokollets lager: interoperabilitet mellan vätskorna. För att kunna utnyttja Bitcoin:s fulla potential var det absolut nödvändigt att hitta en lösning som skulle möjliggöra transaktioner mellan protokollets olika lager. Detta behov gav 2019 upphov till Boltz, en bro som länkar samman flera Bitcoin-lager.



## Vad är Boltz?



[Boltz] (https://boltz.Exchange) är en plattform utan förvaring som är idealisk för alla som vill göra transaktioner mellan de olika lagren i Bitcoin-protokollet:




- on chain**: Bitcoin:s huvudkedja där transaktioner bekräftas var 10:e minut i genomsnitt, är transaktionsavgifterna ofta höga, vilket inte nödvändigtvis uppfyller användarnas behov ;
- Lightning Network**: Bitcoin-överlägget för omedelbara betalningar till låga avgifter, vilket gör att Bitcoin kan användas för dagliga betalningar;
- Liquid Network**: ett överlägg för Bitcoin skapat av Blockstream, vilket möjliggör snabba, Confidential Transactions och användning av andra Bitcoin-baserade finansiella instrument;
- RootStock**: En lösning för att utveckla smarta kontrakt baserade på Bitcoin-protokollet.



![layers](assets/fr/01.webp)



Interoperabilitet mellan dessa olika lager är av stor betydelse, eftersom det ger användarna den flexibilitet de behöver för att dra full nytta av allt som Bitcoin-ekosystemet har att erbjuda.



Boltz använder atomic swaps. Denna teknik gör det möjligt att byta bitcoins mellan två lager (t.ex. BTC onchain i Exchange mot BTC på Lightning) direkt mellan två parter, utan behov av förtroende och utan behov av en mellanhand. Dessa utbyten kallas "atomära" eftersom de bara kan ge två resultat:




- Antingen är Exchange framgångsrik och de två deltagarna har effektivt utbytt sina BTC ;
- Antingen misslyckas Exchange, och båda deltagarna lämnar med sin ursprungliga BTC.



På så sätt behåller du permanent självförvaring av dina bitcoins, och Exchange baseras inte på något förtroende för motparten: antingen lyckas eller misslyckas Exchange, men ingen av parterna kan stjäla den andra partens medel.



En atomär Exchange fungerar med smarta kontrakt [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). I denna typ av Contract är beloppet "låst" i en tvåvägskanal och en tidsbegränsning införs, så att om transaktionen inte slutförs inom en viss tid återgår saldot till insättaren. Detta är den mekanism som används av Boltz-plattformen.



## Ditt första utbyte med Boltz



Boltz är en webbplattform som inte kräver någon personlig information från dig. Boltz har en minimalistisk, flytande Interface som gör att du kan börja handla på mindre än en minut.



![boltz](assets/fr/02.webp)



Väl på plattformen kan du skapa atomära utbyten mellan de olika lagren i Bitcoin:s ekosystem.



![home](assets/fr/03.webp)



Du ser det lägsta och högsta antalet satoshis (den minsta enheten av Bitcoin) som du kan handla med via Boltz, inklusive nätverksavgifter och en procentsats som Boltz tar ut på mellan 0,1 % och 0,5 %.



![fees](assets/fr/04.webp)



Välj sedan den Layer från vilken du vill göra en atomär Exchange, och välj den Layer på vilken du vill ta emot bitcoins.



![couches](assets/fr/05.webp)



I denna handledning kommer vi att fokusera på atom Exchange från huvud Layer till Lightning Network.



Du kan konfigurera basenheten för dina växlar genom att välja mellan alternativen :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



När du har slutfört dina grundläggande konfigurationer anger du beloppet för din atomära Exchange och skapar sedan en Lightning Invoice för motsvarande belopp, eller anger helt enkelt din LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



För att vara på den säkra sidan, kontrollera parametrarna för din atomära Exchange för att exportera reservnycklarna som är länkade till din Exchange.



På ikonen **Settings**, ladda ner backup-nyckeln och spara filen på lämpligt sätt.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Den här filen innehåller de 12 nyckelorden för den portfölj som är kopplad till dina atombörser.



Klicka sedan på knappen **Create atomic Exchange** och fortsätt med betalningen av det angivna beloppet.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

När din betalning har gjorts och bekräftats kommer du automatiskt att få motsvarande belopp på din Lightning Wallet.



I menyn **Återbetalning** hittar du din atomära Exchange-historik för att identifiera den Exchange som du vill ha återbetalning för. Du kan också importera en historik över utbyten som du har gjort på en annan enhet, till exempel med hjälp av den säkerhetskopierade nyckelfilen som är kopplad till dessa utbyten.



![refund](assets/fr/11.webp)



I menyn **History** kan du ladda ner en mer detaljerad historik över de utbyten som är kopplade till din räddningsnyckel genom att klicka på knappen **Backup**.



![backup](assets/fr/12.webp)



⚠️ Lämna inte ut den här filen heller, eftersom den innehåller all information som är kopplad till dina transaktioner och den säkerhetskopieringsnyckel som är kopplad till dessa transaktioner.



Boltz erbjuder dig en hög sekretessnivå tack vare dess åtkomst via en `.onion`-länk i Tor-nätverket. Gör atomutbyten helt anonyma genom att välja menyn **Onion** efter att du har aktiverat Tor-surfning i din webbläsare.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Vid det här laget är du bekant med Boltz, en unik Exchange-plattform som möjliggör interoperabilitet mellan de olika lagren i Bitcoin-ekosystemet.