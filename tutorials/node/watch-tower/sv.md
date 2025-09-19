---
name: Lightning Watchtower
description: Förstå och använda en Watchtower på din Lightning-nod
---
![cover](assets/cover.webp)



## Hur fungerar vakttorn?



_Watchtowers_ är en viktig del av Lightning Network:s ekosystem och ger en extra skyddsnivå för användarnas Lightning-kanaler. Deras huvudsakliga roll är att övervaka kanalens status och ingripa om en sida av kanalen försöker lura den andra.



Hur kan en Watchtower avgöra om en kanal har äventyrats? Den får från kunden (en av parterna i kanalen) den information som behövs för att korrekt identifiera och hantera ett eventuellt intrång. Denna information inkluderar detaljer om den senaste transaktionen, kanalens aktuella status och den Elements som krävs för att skapa strafftransaktioner. Innan dessa data överförs till Watchtower kan kunden kryptera dem för att bevara sekretessen. Så även om Watchtower tar emot uppgifterna kommer de inte att kunna dekryptera dem förrän ett intrång faktiskt har inträffat. Denna krypteringsmekanism skyddar kundens integritet och hindrar Watchtower från att få obehörig tillgång till känslig information.



I denna handledning tittar vi på 3 sätt att använda en **Watchtower** :




- först, den klassiska råa metoden via LND,
- sedan en annan inflygning med Eye of Satoshi,
- och slutligen den förenklade konfigurationen av en Watchtower på din Lightning-nod som hostas med Umbrel.



## 1 - Konfigurera en Watchtower eller en klient via LND



*Denna handledning är hämtad från [den officiella LND-dokumentationen] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Vissa ändringar kan ha gjorts i den ursprungliga versionen



Sedan v0.7.0 stöder `LND` utförandet av en privat altruistisk Watchtower som ett helt integrerat delsystem i `LND`. Watchtowers ger en andra försvarslinje mot skadliga eller oavsiktliga intrångsscenarier när kundnoden är offline eller inte kan svara vid tidpunkten för intrånget, vilket ger en ökad grad av säkerhet för kanalfonder.



Till skillnad från ett _reward watchtower_, som kräver en andel av kanalens medel i utbyte mot sin tjänst, återlämnar ett _altruist watchtower_ alla offrets medel (minus On-Chain-avgifter) utan att ta ut någon provision. Belöningsvakttorn kommer att aktiveras i en senare version; de befinner sig fortfarande i test- och förbättringsfasen.



Dessutom kan `LND` nu konfigureras för att fungera som en _vakttornsklient_, som sparar krypterade transaktioner för att åtgärda överträdelser (så kallade "rättvisetransaktioner") från andra altruistiska vakttorn. Watchtower lagrar krypterade blobbar av fast storlek och kan endast dekryptera och publicera rättvisetransaktionen efter att den felande parten har sänt ett återkallat Commitment-tillstånd. Kommunikationen mellan kund och Watchtower krypteras och autentiseras med hjälp av efemära nyckelpar, vilket begränsar Watchtower:s möjlighet att spåra sina kunder med hjälp av långsiktiga referenser.



Observera att vi i den här versionen har valt att distribuera en begränsad uppsättning funktioner som redan ger betydande säkerhet för LND-användare. Många andra Watchtower-relaterade funktioner är antingen nära färdigställande eller långt framskridna; vi kommer att fortsätta att leverera dem när vi testar dem och så snart de anses vara säkra.



notera: för närvarande sparar vakttorn endast `to_local` och `to_remote`-utdata från återkallade åtaganden; att spara HTLC-utdata kommer att distribueras i en framtida version, eftersom protokollet kan utökas för att inkludera ytterligare signaturdata i krypterade blobbar



### Konfigurera en Watchtower



För att konfigurera en Watchtower måste kommandoradsanvändare kompilera den valfria underservern `watchtowerrpc`, som tillåter interaktion med Watchtower via gRPC eller `lncli`. Publicerade binärfiler inkluderar underservern `watchtowerrpc` som standard.



Minimikonfigurationen för att aktivera Watchtower är `Watchtower.active=1`.



Du kan hämta din Watchtower-konfigurationsinformation med `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Den fullständiga uppsättningen konfigurationsalternativ för Watchtower är tillgänglig via `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Gränssnitt för lyssning



Som standard lyssnar Watchtower på `:9911`, vilket motsvarar port `9911` på alla tillgängliga gränssnitt. Användare kan definiera sina egna lyssningsgränssnitt via alternativet `--Watchtower.listen=`. Du kan kontrollera din konfiguration i fältet `"listeners"` i `lncli tower info`. Om du har problem med att ansluta till din Watchtower ska du kontrollera att `<port>` är öppen eller att din proxy är korrekt konfigurerad till en aktiv Interface.



#### Externa IP-adresser



Användare kan också ange Watchtower:s externa IP Address(es) med `Watchtower.externalip=`, vilket exponerar Watchtower:s fullständiga URI (pubkey@host:port) via RPC eller `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI:er kan kommuniceras till kunder för anslutning och användning med följande kommando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Om Watchtower:s kunder behöver fjärråtkomst till den, se till att :




- Öppna port 9911 (eller en port som definieras via `Watchtower.listen`).
- Använd en proxy för att omdirigera trafik från en öppen port till Watchtower:s lyssnande Address.



#### Tor dolda tjänster



Watchtowers stöder Tor dolda tjänster och kan automatiskt generate en vid start med följande alternativ:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



.onion Address visas sedan i fältet `"uris"` under en `lncli tower info`-fråga:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



notera: Watchtower:s publika nyckel skiljer sig från den publika nyckeln för noden `LND`. För närvarande fungerar den som en "Soft-vitlista", eftersom kunder behöver känna till Watchtower:s publika nyckel för att använda den som en säkerhetskopia i väntan på mer avancerade vitlistningsmekanismer. Vi rekommenderar att du INTE avslöjar denna publika nyckel öppet, såvida du inte är beredd att exponera din Watchtower för hela Internet._



#### Watchtower databas katalog



Watchtower-databasen kan flyttas med hjälp av alternativet `Watchtower.towerdir=`. Observera att suffixet `/Bitcoin/Mainnet/Watchtower.db` kommer att läggas till den valda sökvägen för att isolera databaser efter sträng. Om du anger `Watchtower.towerdir=/path/to/towerdir` kommer en databas att skapas på `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Under Linux finns t.ex. Watchtower:s standarddatabas på adressen :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfigurera en Watchtower-klient



För att konfigurera en Watchtower-klient behöver du två saker:





- Aktivera Watchtower-klienten med alternativet `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI för en aktiv Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Du kan konfigurera flera vakttorn på detta sätt.



#### Avgiftssatser för juridiska transaktioner



Användare kan välja att ställa in avgiftssatsen för rättvisetransaktioner via alternativet `wtclient.sweep-fee-rate`, som accepterar värden i sat/byte. Standardvärdet är 10 sat/byte, men det är möjligt att sikta på högre priser för att uppnå högre prioritet under toppavgifter. Ändring av `sweep-fee-rate` gäller för alla nya uppdateringar efter omstart av daemon.



#### Övervakning



Med kommandot `lncli wtclient` kan användare nu interagera direkt med Watchtower-klienten för att få eller ändra information om alla registrerade vakttorn.



Med `lncli wtclient tower` kan du t.ex. ta reda på antalet sessioner som för närvarande förhandlas med Watchtower som lades till ovan och avgöra om den används för säkerhetskopiering tack vare fältet `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Om du vill få information om Watchtower-sessioner använder du alternativet `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Alla konfigurationsalternativ för Watchtower-klienten är tillgängliga via `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Installera ditt eget Satoshi-öga



*Denna handledning är delvis hämtad från en artikel på [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/). Ändringar har gjorts i originalversionen*



Satoshi:s öga ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) är en Watchtower-blixt utan depå, som överensstämmer med [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Den består av två huvudkomponenter:





- teos**: innehåller en Interface (CLI) för kommandoraden och de viktigaste serverfunktionerna i Watchtower. Två binärfiler - **teosd** och **teos-CLI** - produceras när denna _crate_ kompileras.





- teos-common**: innehåller delad funktionalitet på server- och klientsidan (användbart för att skapa en klient).



För att köra Watchtower korrekt måste du köra **bitcoind** innan du startar Watchtower med kommandot **teosd**. Innan du kör dessa två kommandon måste du konfigurera din **Bitcoin.conf**-fil. Så här gör du det:





- Installera Bitcoin core från källan eller ladda ner den. Efter nedladdningen placerar du filen **Bitcoin.conf** i Bitcoin core-användarkatalogen. Se den här länken för mer information om var filen ska placeras, eftersom detta beror på vilket operativsystem som används.





- När platsen har identifierats lägger du till följande alternativ:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: för RPC-förfrågningar





- rpcuser** och **rpcpassword**: autentiserar RPC-klienter till servern





- regtest**: krävs inte, men är användbart om du planerar utveckling.



Värdena för **rpcuser** och **rpcpassword** ska väljas av dig. De måste skrivas utan citattecken. Till exempel



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Om du nu kör **bitcoind** bör noden starta.





- För Watchtower-delen måste du först installera **teos** från källan. Följ instruktionerna som ges i den här länken.





- När du har installerat **teos** på ditt system och kört testerna kan du gå vidare till det sista steget: att konfigurera filen **teos.toml** i teos användarkatalog. Filen ska placeras i en mapp med namnet **.teos** (notera punkten) under din hemkatalog. Till exempel **/home//.teos** under Linux. När du har hittat platsen skapar du en fil **teos.toml** och ställer in dessa alternativ i enlighet med ändringarna som gjordes på **bitcoind**:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Observera att här måste användarnamn och lösenord skrivas **inom citationstecken**. Med hjälp av föregående exempel :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



När detta har gjorts bör du vara redo att starta Watchtower. Eftersom vi kör på **regtest** är det troligt att inga block utvanns på vårt Bitcoin-testnätverk när Watchtower först anslöts (om de gjorde det är något fel). Watchtower bygger en intern cache av de senaste 100 blocken av **bitcoind**; så vid första lanseringen kan du få följande fel:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Eftersom vi använder **regtest** kan vi Miner-blockera genom att utfärda ett RPC-kommando utan att behöva vänta på den medianfördröjning på 10 minuter som förekommer i andra nätverk (t.ex. Mainnet eller Testnet). Se **bitcoin-cli**-hjälpen för mer information om hur du gör Miner-block.



![Image](assets/fr/01.webp)



Det var allt: du har kört Watchtower med framgång. Vi gratulerar dig. 🎉




## 3 - Konfigurera en Watchtower på Umbrel



På Umbrel är det extremt enkelt att ansluta till en Watchtower för att skydda din Lightning-nod, eftersom allt görs via den grafiska Interface. När du har fjärranslutit till din nod öppnar du applikationen "**Lightning Node**".



![Image](assets/fr/02.webp)



Klicka på de tre små prickarna längst upp till höger på Interface och välj sedan "**Avancerade inställningar**".



![Image](assets/fr/03.webp)



I menyn "**Watchtower**" finns två alternativ tillgängliga:





- Watchtower Service**: Med det här alternativet kan du driva en Watchtower, dvs. en tjänst som övervakar andra noders kanaler för att upptäcka bedrägeriförsök. I händelse av ett intrång publicerar din Watchtower en transaktion på Blockchain, vilket gör det möjligt för användare att återfå sina låsta medel. När den har aktiverats visas din Watchtower:s URI och kan kommuniceras till andra noder så att de kan lägga till den i sin Watchtower-klient;





- Watchtower Client**: med det här alternativet kan du ansluta till externa vakttorn för att skydda dina egna kanaler. När det är aktiverat kan du lägga till Watchtower-tjänster till vilka din nod kommer att överföra nödvändig information om sina kanaler. Dessa vakttorn kommer sedan att övervaka deras status och ingripa i händelse av bedrägeriförsök.



Det viktigaste för dig är naturligtvis att aktivera *Watchtower Client* för att skydda din nod, men jag rekommenderar också att du aktiverar *Watchtower Service* för att i gengäld bidra till andra användares säkerhet.



![Image](assets/fr/04.webp)



Klicka sedan på Green:s "**Spara och starta om noden**"-knapp. Din LND kommer att starta om.



I samma meny hittar du också URI:n för din Watchtower-tjänst om du har aktiverat den. Du kan också lägga till URI för en extern Watchtower för att skydda dina kanaler. Klicka på "**ADD**" för att bekräfta.



![Image](assets/fr/05.webp)



Det finns flera Watchtowers tillgängliga online. Till exempel [LN+ och Voltage erbjuder en altruistisk Watchtower](https://lightningnetwork.plus/Watchtower) som du kan ansluta till:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Ett annat alternativ är att Exchange din Watchtower URI med dina andra bitcoinare, så att var och en skyddar den andras nod.



Jag rekommenderar också att ni sätter upp flera vakttorn för att minska riskerna om ett av dem skulle bli otillgängligt.



Slutligen kan du justera parametern "**Watchtower Client Sweep Fee Rate**". Detta definierar den maximala avgiftssats som du är villig att betala för att en Watchtower broadcast punishment-transaktion ska inkluderas i ett block. Se till att du ställer in ett tillräckligt högt värde, anpassat till de belopp som är låsta i dina kanaler.