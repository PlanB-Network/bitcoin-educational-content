---
name: Watch Tower
description: Förstå och använda en Watch Tower
---

## Hur fungerar vakttorn?


Watchtowers är en viktig del av Lightning Network:s ekosystem och ger en extra grad av skydd för användarnas blixtkanaler. Dess huvudsakliga ansvar är att hålla ett öga på kanalernas hälsa och ingripa om en kanalpart försöker bedra den andra.


Så hur kan en Watchtower avgöra om en kanal har äventyrats? Watchtower får den information den behöver från klienten, en av kanalparterna, för att korrekt kunna identifiera och reagera på eventuella intrång. De senaste transaktionsuppgifterna, det aktuella kanaltillståndet och den information som krävs för att skapa strafftransaktioner ingår ofta i denna information. Innan data överförs till Watchtower kan klienten kryptera den för att skydda integritet och sekretess. Detta hindrar Watchtower från att dekryptera de krypterade uppgifterna om inte ett intrång verkligen har ägt rum, även om Watchtower får tillgång till uppgifterna. Kundens integritet skyddas av detta krypteringssystem, som också hindrar Watchtower från att få tillgång till privata data utan tillstånd.


## Så här skapar du ditt eget Eye of Satoshi och börjar bidra


Satoshi:s öga ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)) är en icke frihetsberövande blixt Watchtower som överensstämmer med [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Den har två huvudkomponenter:


1. teos: inklusive en CLI och tornets kärnfunktionalitet på serversidan. Två binärfiler - teosd och teos-CLI - kommer att produceras när den här lådan byggs.

2. teos-common: Inkluderar delad funktionalitet på serversidan och klientsidan (användbart för att skapa en klient).


För att köra tornet framgångsrikt måste du köra bitcoind innan du kör tornet med teosd-kommandot. Innan du kör båda dessa kommandon måste du ställa in din Bitcoin.conf-fil. Här är stegen för hur du gör detta


1. Installera Bitcoin core från källan eller ladda ner den. Efter nedladdning, placera filen Bitcoin.conf i användarkatalogen för Bitcoin core. Se den här länken för mer information om var filen ska placeras eftersom det beror på vilket operativsystem du använder.

2. När du har identifierat den plats där filen ska skapas lägger du till följande alternativ


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword````


Om du nu kör bitcoind bör den börja köra noden.


1. För torndelen måste du först installera teos från källan. Följ instruktionerna som ges i den här länken.

2. När du har installerat teos i ditt system och kört testerna kan du fortsätta med det sista steget, som är att konfigurera filen teos.toml i teos användarkatalog. Filen måste placeras i en mapp som heter .teos (tänk på punkten) under din hemmapp. Det är till exempel /home/<ditt-användarnamn>/.teos för Linux. När du har hittat platsen skapar du en teos.toml-fil och ställer in dessa alternativ som motsvarar de saker vi har ändrat på bitcoind.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"```


När du har gjort det bör du vara redo att köra tornet. Med tanke på att vi kör på regtest är chansen stor att det inte kommer att finnas några block som bryts i vårt Bitcoin-testnätverk första gången tornet ansluter till det (om det finns det är något verkligen fel). Tornet bygger en intern cache av de senaste 100 blocken från bitcoind, så när vi kör för första gången kan vi få följande fel:


_ERROR [teosd] Inte tillräckligt med block för att starta tornet (krävs: 100). Minera minst 100 till_


Givet att vi kör på regtest kan vi minera block genom att utfärda ett RPC-kommando, utan att behöva vänta på den 10-minuters mediantid som vi vanligtvis ser i andra nätverk (som Mainnet eller Testnet). Kontrollera bitcoin-cli-hjälpen och leta efter hur man minerar block. Om du behöver lite hjälp kan du gå igenom den här artikeln.


![image](assets/2.webp)


Det var allt, du har lyckats köra tornet. Gratulerar till det. 🎉