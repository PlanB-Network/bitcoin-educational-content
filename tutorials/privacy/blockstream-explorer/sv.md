---
name: BLOCKSTREAM Explorer
description: Utforska de viktigaste Layer i Bitcoin och Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer är ett projekt som underlättar utforskningen av transaktioner och Global State i Bitcoin-protokollet, samt [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid som utvecklats av BLOCKSTREAM-företaget.



Utforskaren [BLOCKSTREAM.info] (https://BLOCKSTREAM.info) initierades 2014 av BLOCKSTREAM, ett företag grundat av Adam Back, och syftar till att tillhandahålla en robust infrastruktur för Bitcoin, som garanterar interoperabilitet och transaktionsspårning mellan lager (On-Chain och Liquid), samtidigt som användarnas säkerhet och integritet förbättras.



I den här handledningen presenterar vi vad som gör den annorlunda, dess tjänster och hur den erbjuder sömlös övervakning av driften och statusen för Bitcoin:s On-Chain- och Liquid-lager.



## Komma igång med BLOCKSTREAM



### Navigera i huvudkanalen



När du går till BLOCKSTREAM.info explorer, på "**Dashboard**", väljs den huvudsakliga Bitcoin protokollkanalen som standard. Från denna Interface har du en översikt över :





- Huvudkedjans storlek: Nyligen utvunna block.



![blocks](assets/fr/01.webp)



Detta avsnitt innehåller information om de senaste blocken som har utvunnits, Timestamp, antalet transaktioner som ingår i varje BLOCK, storleken i kilobyte (kB) och mätningen av varje BLOCK i viktenheter (**WU** = *Weight Units*). Den sista mätningen är av intresse eftersom den gör det möjligt för oss att utvärdera optimeringen av BLOCK, med tanke på att varje BLOCK i huvudkedjan är begränsad till 4 000 000 WU, eller 4 000 kWU.





- Nyligen genomförda transaktioner.



![transactions](assets/fr/02.webp)



Transaktionsavsnittet innehåller information om transaktionens unika identifierare, det Bitcoin-värde som är involverat, storleken i virtuella bytes (vB) - som representerar summan av alla data (in- och utdata) - och den tillhörande avgiftssatsen. Till exempel kommer en transaktion med en storlek på 153 vB och en hastighet på 2 sat/vB att medföra en avgift på 306 satoshis.



### Prospektering av vätskor



Från menyn "**Blocks**" kan du spåra hela huvudkedjans historia tillbaka till den senaste BLOCK som utvanns.



![blocs](assets/fr/03.webp)



Genom att klicka på en specifik BLOCK kan du få mer information om den information och de transaktioner som ingår i den. Till exempel för BLOCK 919330: du har Hash av BLOCK. Du kan också navigera till föregående BLOCK, eftersom varje utvunnen BLOCK (bortsett från Genesis) är länkad till den föregående och behåller Hash från sin föregångare.



![metadata](assets/fr/04.webp)



Genom att klicka på **"Detaljer"**-knappen kan du få mer information om denna BLOCK, till exempel dess status, som bekräftar att den har lagts till i den bevarade och spridda huvudkedjan. Du har också den svårighet med vilken denna BLOCK bryts: denna svårighet representerar den datorkraft som krävs för att lösa det kryptografiska problemet med Mining och justeras var 2016:e block (cirka 2 veckor).



![details](assets/fr/05.webp)



Under detta detaljavsnitt hittar vi alla transaktioner som ingår i denna BLOCK.



Den allra första transaktionen i BLOCK kallas **transaktion coinbase**. Den används för att fördela Miner:s Mining-belöning (alla avgifter i samband med de transaktioner som ingår i BLOCK och BLOCK-anslaget). De bitcoins som skapas av denna transaktion kan endast användas när ytterligare 100 block i följd har utvunnits. Med andra ord, för att kunna använda dem måste Miner vänta på produktionen av BLOCK **919430**. Detta är känt som [*"löptid"*](https://planb.network/fr/resources/glossary/maturity-period).



Coinbase är en speciell transaktion: det är den enda som inte har någon verklig input, eftersom den inte spenderar några bitcoins från en tidigare transaktion.




![coinbase](assets/fr/06.webp)



Alla andra transaktioner delas in i två avsnitt: inmatningar och utmatningar.



För att bitcoins ska kunna användas som input i en ny transaktion måste initiativtagaren till transaktionen bevisa sitt innehav genom att tillhandahålla en signatur som motsvarar ett specifikt skript. Varje bit av bitcoins (UTXO) innehåller ett skript som i allmänhet kräver en specifik signatur som endast innehavarens privata nyckel kan tillhandahålla. Dessa skript är ***scriptSig*** (i ASM), skrivna i Bitcoin Script, och kan vara av olika typer. I det här exemplet kan vi se att de UTXO:er som användes var av typen P2SH till en utgång av typen P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Du kan spåra historiken för en specifik UTXO med hjälp av heuristik. Vi inbjuder dig att upptäcka de olika Bitcoin-heuristikerna och hur du kan stärka sekretessen för dina Bitcoin-transaktioner:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Låt oss ta ett exempel på den här transaktionens utgående utgift. Genom att klicka på transaktionsidentifieraren omdirigeras vi till avsnittet **Transaktioner** på sidan med transaktionsdetaljer.



![transaction](assets/fr/08.webp)



På den här sidan kan du se vilken BLOCK som transaktionen ingick i. Beroende på vilken typ av Address som används kan transaktionen optimera sina data (*virtuella bytes*) och därför betala mindre transaktionsavgifter. Den här transaktionen sparade till exempel 53% i avgifter genom att använda ett inbyggt SegWit BECH32 Address-format som börjar med `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid beläggning



Liquid Network är en [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) och en öppen källkodslösning på nivå 2 för Bitcoin-protokollet. Den möjliggör framför allt snabbare och mer konfidentiella Bitcoin-transaktioner.



I utforskaren BLOCKSTREAM.info klickar du på knappen **"Liquid"** för att växla till Liquid Network.



![liquid](assets/fr/10.webp)



När vi klickar på en av de transaktioner som vi vill följa ser vi att beloppen för Bitcoin-delarna ersätts av orden "**Confidential**". På det här nätverket kan transaktioner vara konfidentiella, så vi kan inte se beloppen för varje UTXO, varken i eller utanför transaktionen.



![liquid_trx](assets/fr/11.webp)



Vi noterar dock att de principer och mekanismer som finns i Layer i Bitcoin-protokollet är desamma: Bitcoin-låsningsskript och UTXO-spårbarhet.



![liquid_details](assets/fr/12.webp)



Liquid Network tillhandahåller också digitala tillgångar som inte är depåer och som kan användas av organisationer. I menyn **"Tillgångar"** hittar du en lista över registrerade tillgångar, deras total och den domän som de hänför sig till.



![assets](assets/fr/13.webp)



För varje tillgång kan du spåra historiken för emissions- och bränningstransaktioner (radering av den totala mängden i omlopp).



![assets_trxs](assets/fr/14.webp)




## Fler alternativ



Utforskaren BLOCKSTREAM.info innehåller även visualiseringar och spårning av transaktioner på Testnet, Bitcoin, On-Chain och Liquid Network.



![testnet](assets/fr/15.webp)



När du går till Testnet-nätverket använder du inte riktiga bitcoins, men du har alla funktioner som beskrivs ovan.



![liquid_testnet](assets/fr/16.webp)



Detta nätverk har en annan kedjelängd, som du kan ansluta till och testa driften av mekanismerna Bitcoin och Liquid.





- Avsnittet API är avsett för alla som vill integrera vissa Explorer-funktioner i sin egen applikation. Genom denna API kan du till exempel fråga ut huvudkedjan i de olika lagren (On-Chain och Liquid), spåra transaktioner och ta reda på de genomsnittliga avgifterna för transaktioner i en BLOCK.



![api](assets/fr/17.webp)



Du är nu redo att utnyttja den fulla potentialen i BLOCKSTREAM Explorer för att fråga blockkedjor på On-Chain- och Liquid-lagren. Vi hoppas att du har hittat den här handledningen informativ och rekommenderar vår handledning om en annan Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f