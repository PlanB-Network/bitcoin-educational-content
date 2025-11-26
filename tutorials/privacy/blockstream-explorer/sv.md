---
name: Blockstream Explorer
description: Utforska huvudlagret i Bitcoin och Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer är ett projekt som underlättar utforskningen av transaktioner och det globala tillståndet för Bitcoin-protokollet, samt [*sidechain*] (https://planb.academy/en/resources/glossary/sidechain) Liquid som utvecklats av Blockstream-företaget.



Utforskaren [blockstream.info] (https://blockstream.info) initierades 2014 av Blockstream, ett företag grundat av Adam Back, och syftar till att tillhandahålla en robust infrastruktur för Bitcoin, som garanterar interoperabilitet och transaktionsspårning mellan lager (on-chain och Liquid), samtidigt som användarnas säkerhet och integritet stärks.



I den här handledningen tittar vi på vad som skiljer den åt, dess tjänster och hur den erbjuder sömlös övervakning av driften och statusen för Bitcoin:s on-chain- och Liquid-lager.



## Komma igång med Blockstream explorer



### Navigera i huvudkanalen



När du går till Blockstream.info-utforskaren, på "** Dashboard**", är Bitcoin-protokollets huvudkedja vald som standard. Från detta gränssnitt har du en översikt över :





- Huvudkedjans storlek: Nyligen utvunna block.



![blocks](assets/fr/01.webp)



I det här avsnittet finns information om de senaste blocken, tidsstämpeln, antalet transaktioner som ingår i varje block, storleken i kilobyte (kB) och mätningen av varje block i viktenheter (**WU** = *Weight Units*). Den sista mätningen är av intresse eftersom den gör det möjligt för oss att utvärdera optimeringen av blocket, med tanke på att varje block i huvudkedjan är begränsat till 4 000 000 WU, eller 4 000 kWU.





- Nyligen genomförda transaktioner.



![transactions](assets/fr/02.webp)



Transaktionsavsnittet innehåller information om transaktionens unika identifierare, det involverade bitcoinvärdet, storleken i virtuella byte (vB) - som representerar summan av all data (in- och utdata) - och den tillhörande avgiftssatsen. Till exempel kommer en transaktion med en storlek på 153 vB och en avgift på 2 sat/vB att medföra en avgift på 306 satoshis.



### Prospektering av vätskor



I menyn "**Blocks**" kan du spåra hela huvudkedjans historia tillbaka till det senast utvunna blocket.



![blocs](assets/fr/03.webp)



Genom att klicka på ett specifikt block kan du få mer information om den information och de transaktioner som ingår i det. Till exempel för block 919330: du ser blockets hash. Du kan också navigera till föregående block, eftersom varje utvunnet block (förutom Genesis) är länkat till det föregående och behåller sin föregångares hash.



![metadata](assets/fr/04.webp)



Genom att klicka på knappen **"Detaljer"** kan du få mer information om det här blocket, till exempel dess status, som bekräftar att det har lagts till i den bevarade och spridda huvudkedjan. Du har också den svårighet med vilken detta block bryts: denna svårighet representerar den datorkraft som krävs för att lösa det kryptografiska problemet med mining och justeras vart 2016:e block (cirka 2 veckor).



![details](assets/fr/05.webp)



Under denna detaljsektion hittar vi alla transaktioner som ingår i detta block.



Den allra första transaktionen i blocket kallas **transaction coinbase**. Den används för att fördela minarens mining-belöning (alla avgifter som är förknippade med de transaktioner som ingår i blocket och blockbidraget). De bitcoins som skapas genom den här transaktionen kan bara användas när ytterligare 100 block i följd har minats. Med andra ord, för att kunna använda dem måste gruvarbetaren vänta på produktionen av block **919430**. Detta kallas för [*"löptid"*] (https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase är en speciell transaktion: det är den enda som inte har någon verklig input, eftersom den inte spenderar några bitcoins från en tidigare transaktion.




![coinbase](assets/fr/06.webp)



Alla andra transaktioner delas in i två avsnitt: inmatningar och utmatningar.



För att bitcoins ska kunna användas som inputs i en ny transaktion måste initiativtagaren till transaktionen bevisa sitt innehav genom att tillhandahålla en signatur som motsvarar ett specifikt skript. Varje bit av bitcoins (UTXO) innehåller ett skript som i allmänhet kräver en specifik signatur som endast innehavarens privata nyckel kan tillhandahålla. Dessa skript är ***scriptSig*** (i ASM), skrivna i Bitcoin Script, och kan vara av olika typer. I det här exemplet kan vi se att de UTXO:er som användes var av typen P2SH till en utgång av typen P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Du kan spåra historiken för en specifik UTXO med hjälp av heuristik. Vi inbjuder dig att upptäcka de olika Bitcoin-heuristikerna och sätten att stärka sekretessen för dina transaktioner på Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Låt oss ta ett exempel på den här transaktionens utgående utgift. Genom att klicka på transaktionsidentifieraren omdirigeras vi till avsnittet **Transaktioner** på sidan med transaktionsdetaljer.



![transaction](assets/fr/08.webp)



På den här sidan kan du se vilket block som transaktionen ingick i. Beroende på vilken typ av adress som används kan transaktionen optimera sina data (*virtuella bytes*) och därför betala mindre transaktionsavgifter. Den här transaktionen sparade till exempel 53% i avgifter genom att använda ett inbyggt SegWit Bech32-adressformat som börjar med `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid lager



Liquid Network är en [*sidechain*] (https://planb.academy/en/resources/glossary/sidechain) och en nivå 2-lösning med öppen källkod för Bitcoin-protokollet. Det möjliggör framför allt snabbare och mer konfidentiella bitcoin-transaktioner.



I Blockstream.info-utforskaren klickar du på knappen **"Liquid"** för att växla till Liquid-nätverket.



![liquid](assets/fr/10.webp)



När vi klickar på en av transaktionerna som vi vill spåra ser vi att bitcoinsummorna ersätts av orden "**Confidential**". På det här nätverket kan transaktioner vara konfidentiella, så vi kan inte se beloppen för varje UTXO, varken i eller utanför transaktionen.



![liquid_trx](assets/fr/11.webp)



Vi noterar dock att de principer och mekanismer som finns på huvudlagret i Bitcoin-protokollet är desamma: bitcoin-låsningsskript och UTXO-spårbarhet.



![liquid_details](assets/fr/12.webp)



Liquid Network tillhandahåller också digitala tillgångar som inte är deponerade och som kan användas av organisationer. I menyn **"Tillgångar"** hittar du en lista över registrerade tillgångar, deras total och den domän som de hänför sig till.



![assets](assets/fr/13.webp)



För varje tillgång kan du spåra historiken för emissions- och bränningstransaktioner (radering av den totala mängden i omlopp).



![assets_trxs](assets/fr/14.webp)




## Fler alternativ



Blockstream.info explorer innehåller även visualiseringar och spårning av transaktioner på Testnet, Bitcoin, on-chain och Liquid Network.



![testnet](assets/fr/15.webp)



När du går till Testnet-nätverket använder du inte riktiga bitcoins, men du har alla de funktioner som beskrivs ovan.



![liquid_testnet](assets/fr/16.webp)



Detta nätverk har en annan kedjelängd, som du kan ansluta till och testa driften av mekanismerna Bitcoin och Liquid.





- Avsnittet API är avsett för alla som vill integrera vissa Explorer-funktioner i sin egen applikation. Genom denna API kan du till exempel förhöra huvudkedjan i de olika lagren (on-chain och Liquid), spåra transaktioner och ta reda på de genomsnittliga avgifterna för transaktioner i ett block.



![api](assets/fr/17.webp)



Du är nu redo att utnyttja Blockstream Explorers fulla potential för att fråga blockkedjor på on-chain- och Liquid-lagren. Vi hoppas att du har funnit denna handledning informativ och rekommenderar vår handledning om en annan Bitcoin-utforskare:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f