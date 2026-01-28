---
term: Fee sniping
definition: Attack där brytare skriver om ett nyligen skapat block för att samla in dess höga transaktionsavgifter.
---

Ett attackscenario där utvinnare försöker skriva om ett nyligen bekräftat block för att ta ut de transaktionsavgifter som det innehåller, samtidigt som de lägger till transaktioner med höga avgifter som har anlänt under tiden i Mempool. Det yttersta målet med denna attack för Miner är att öka deras lönsamhet. Fee sniping kan bli alltmer lönsamt när Block reward minskar och transaktionsavgifter utgör en större del av miners intäkter. Det kan också vara fördelaktigt när avgifterna i det föregående blocket är betydligt högre än i det näst bästa kandidatblocket. För att förenkla står Miner inför detta val när det gäller incitament:


- Minera på normalt sätt efter det sista blocket, med hög sannolikhet att vinna en låg belöning;
- Försök att bryta ett tidigare block (fee sniping), med låg sannolikhet att vinna en hög belöning.


Denna attack utgör en risk för Bitcoin-systemet, eftersom ju fler gruvarbetare som använder den, desto fler andra gruvarbetare, som ursprungligen är ärliga, får incitament att göra detsamma. Varje gång en ny Miner ansluter sig till dem som försöker snipa avgifter ökar sannolikheten för att en av de attackerande gruvarbetarna lyckas, och sannolikheten för att en av de ärliga gruvarbetarna förlänger kedjan minskar i gengäld. Om denna attack utförs massivt och upprätthålls över tid skulle blockbekräftelser inte längre vara en tillförlitlig indikator på oföränderligheten i en Bitcoin-transaktion. Detta skulle potentiellt kunna göra systemet oanvändbart.


För att motverka denna risk fyller de flesta Wallet-program automatiskt i fältet "nLocktime" så att valideringen av transaktionen villkoras av att den ingår i nästa blockhöjd. På så sätt blir det omöjligt att inkludera transaktionen i en omskrivning av föregående block. Om den utbredda användningen av `nLocktime` antas av Bitcoin-användare, minskar det avsevärt incitamenten för avgiftssnipning. Det uppmuntrar faktiskt utvecklingen av Blockchain snarare än omskrivningen av den genom att minska de potentiella vinsterna från den. För Taproot-transaktioner föreslår BIP326 att fältet `nSequence` används på ett liknande sätt för att uppnå motsvarande effekt som fältet `nLocktime` för andra typer av transaktioner. Denna användning skulle slå två flugor i en smäll genom att även förbättra integriteten för andra Layer-protokoll som använder samma fält.