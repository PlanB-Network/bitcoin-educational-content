namn: Vakttorn
beskrivning: Förstå och använda ett vakttorn

# Vakttorn Blixt

> Kredit till: https://blog.summerofbitcoin.org/bitcoin-lightning-and-the-eye-of-satoshi-watchtower-revolutionizing-transactions-and-security//

## Hur fungerar vakttorn?

En viktig del av Lightning Network-ekosystemet ger vakttornen en extra grad av skydd för användarnas blixtkanaler. Dess huvudsakliga ansvar är att övervaka kanalernas hälsa och ingripa om en kanalpart försöker lura den andra.

Så hur kan ett vakttorn avgöra om en kanal har komprometterats? Vakttornet får den information det behöver från klienten, en av kanalpartierna, för att korrekt identifiera och svara på eventuella överträdelser. De senaste transaktionsuppgifterna, den aktuella kanalens tillstånd och informationen som krävs för att skapa strafftransaktioner inkluderas ofta i denna information. Innan klienten skickar data till vakttornet kan den kryptera den för att skydda integritet och sekretess. Detta förhindrar att vakttornet dekrypterar den krypterade datan om inte en överträdelse faktiskt har ägt rum, även om det får datan. Klientens integritet skyddas av detta krypteringssystem, som också förhindrar att vakttornet får åtkomst till privat data utan behörighet.

## Hur du ställer in din egen Eye of Satoshi och börjar bidra

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) är ett icke-förvarande Lightning-vakttorn som följer [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Den har två huvudkomponenter:

1. teos: inkluderar ett CLI och den serverbaserade kärnfunktionaliteten för tornet. Två binärer - teosd och teos-cli - kommer att skapas när denna katalog byggs.

2. teos-common: inkluderar delad serverbaserad och klientbaserad funktionalitet (användbart för att skapa en klient).

För att köra tornet framgångsrikt måste du ha bitcoind igång innan du kör tornet med kommandot teosd. Innan du kör båda dessa kommandon måste du konfigurera din bitcoin.conf-fil. Här är stegen för hur du gör detta:-

1. Installera bitcoin core från källan eller ladda ner det. Efter nedladdning, placera bitcoin.conf-filen i Bitcoin core-användarkatalogen. Kolla länken för mer information om var filen ska placeras eftersom det beror på vilket operativsystem du använder.

2. Efter att ha identifierat platsen där filen ska skapas, lägg till dessa alternativ:-

'''
#RPC
server=1
rpcuser=<ditt-användarnamn>
rpcpassword=<ditt-lösenord>

#chain
regtest=1
'''

* server: För RPC-förfrågningar
* rpcuser och rpcpassword: RPC-klienter kan autentisera sig hos servern
* regtest: Inte nödvändigt men användbart om du planerar för utveckling.

rpcuser och rpcpassword måste väljas av dig. De måste skrivas utan citattecken. Exempel:-

'''
rpcuser=aniketh
rpcpassword=starktlösenord
'''

Nu, om du kör bitcoind ska det börja köra noden.

1. För tornet, först måste du installera teos från källan. Följ instruktionerna som ges i denna länk.
2. Efter att ha installerat teos framgångsrikt på ditt system och kört testerna kan du gå vidare till det sista steget, vilket är att konfigurera teos.toml-filen i teos-användarkatalogen. Filen måste placeras i en mapp som heter .teos (observera punkten) under din hemmapp. Det vill säga, till exempel, /home/<ditt-användarnamn>/.teos för Linux. När du har hittat platsen, skapa en teos.toml-fil och ställ in dessa alternativ som motsvarar de saker vi har ändrat på bitcoind.
'''
#bitcoind
btc_network = "regtest"
btc_rpc_user = <ditt-användarnamn>
btc_rpc_password = <ditt-lösenord>
'''

Observera att användarnamnet och lösenordet måste skrivas inom citattecken, det vill säga för samma exempel som tidigare:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
'''

När du har gjort det är du redo att köra tornet. Eftersom vi kör på regtest är det troligt att inga block bryts i vårt bitcoin-testnätverk första gången tornet ansluter till det (om det finns, är något definitivt fel). Tornet bygger en intern cache av de senaste 100 blocken från bitcoind, så vid första körningen kan vi få följande felmeddelande:

> ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more

Eftersom vi kör på regtest kan vi bryta block genom att utfärda ett RPC-kommando, utan att behöva vänta på den 10-minuters median-tiden som vi vanligtvis ser i andra nätverk (som mainnet eller testnet). Kolla bitcoin-cli help och leta efter hur man bryter block. Om du behöver hjälp kan du gå igenom den här artikeln.

![image](assets\2.png)

Det var allt, du har framgångsrikt kört tornet. Grattis. 🎉

https://blog.summerofbitcoin.org/bitcoin-lightning-and-the-eye-of-satoshi-watchtower-revolutionizing-transactions-and-security//