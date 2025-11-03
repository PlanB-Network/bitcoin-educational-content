---
name: Lightning Watchtower
description: Pochopení a používání modulu Watchtower v uzlu Lightning
---
![cover](assets/cover.webp)



## Jak strážní věže fungují?



Strážní věže, které jsou nezbytnou součástí ekosystému Lightning Network, poskytují dodatečnou úroveň ochrany kanálů Lightning uživatelů. Jejich hlavním úkolem je monitorovat stav kanálu a zasáhnout, pokud se jedna strana kanálu pokusí podvést druhou.



Jak může jednotka Watchtower zjistit, zda byl kanál narušen? Od zákazníka (jedné ze stran kanálu) obdrží informace potřebné ke správné identifikaci a řešení případného narušení. Tyto informace zahrnují podrobnosti o poslední transakci, aktuální stav kanálu a Elements, který je nutný k vytvoření sankčních transakcí. Před přenosem těchto údajů do Watchtower je zákazník může zašifrovat, aby byla zachována důvěrnost. Takže i když Watchtower data obdrží, nebude je moci dešifrovat, dokud skutečně nedojde k narušení. Tento šifrovací mechanismus chrání soukromí zákazníka a brání společnosti Watchtower získat neoprávněný přístup k citlivým informacím.



V tomto návodu se podíváme na 3 způsoby použití **Watchtower** :




- nejprve klasická surová metoda prostřednictvím LND,
- pak další přiblížení s okem Satoshi,
- a nakonec zjednodušená konfigurace Watchtower v uzlu Lightning hostovaném pomocí Umbrelu.



## 1 - Konfigurace Watchtower nebo klienta prostřednictvím LND



*Tento návod je převzat z [oficiální dokumentace ke LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). V původní verzi mohly být provedeny některé změny



Od verze 0.7.0 podporuje `LND` provádění soukromého altruistického Watchtower jako plně integrovaného subsystému `LND`. Strážní věže poskytují druhou linii obrany proti scénářům zlomyslného nebo náhodného narušení, když je zákaznický uzel v době narušení offline nebo není schopen reagovat, a nabízejí tak vyšší stupeň zabezpečení prostředků kanálu.



Na rozdíl od _odměnové strážní věže_, která za své služby požaduje podíl z prostředků kanálu, _altruistická strážní věž_ vrací oběti všechny její prostředky (po odečtení poplatků On-Chain), aniž by si účtovala provizi. Odměnové strážní věže budou aktivovány v pozdější verzi; zatím jsou ve fázi testování a vylepšování.



Kromě toho lze nyní `LND` nakonfigurovat tak, aby fungoval jako _klient strážní věže_ a ukládal šifrované transakce nápravy narušení (tzv. "transakce spravedlnosti") z jiných altruistických strážních věží. Watchtower ukládá zašifrované bloby pevné velikosti a může dešifrovat a zveřejnit transakci spravedlnosti až poté, co porušující strana odvysílá odvolaný stav Commitment. Komunikace zákazník ↔ Watchtower je šifrována a ověřována pomocí párů efemérních klíčů, což omezuje schopnost Watchtower sledovat své zákazníky prostřednictvím dlouhodobých pověření.



Všimněte si, že jsme se rozhodli v této verzi nasadit omezenou sadu funkcí, které již uživatelům `LND` poskytují významné zabezpečení. Mnoho dalších funkcí souvisejících s Watchtower je buď těsně před dokončením, nebo jsou již v pokročilém stádiu; budeme je dodávat tak, jak je budeme testovat a jakmile budou považovány za bezpečné.



poznámka: prozatím watchtowery ukládají pouze výstup `to_local` a `to_remote` odvolaných závazků; ukládání výstupu HTLC bude zavedeno v některé z budoucích verzí, protože protokol může být rozšířen o další podpisová data v šifrovaných blobech._



### Konfigurace zařízení Watchtower



Pro nastavení Watchtower musí uživatelé příkazového řádku zkompilovat volitelný subserver `watchtowerrpc`, který umožňuje interakci s Watchtower prostřednictvím gRPC nebo `lncli`. Zveřejněné binární soubory standardně obsahují subserver `watchtowerrpc`.



Minimální konfigurace pro aktivaci Watchtower je `Watchtower.active=1`.



Informace o konfiguraci Watchtower můžete získat pomocí příkazu `lncli tower info` :



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



Úplná sada konfiguračních možností Watchtower je k dispozici pomocí `LND -h` :



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



#### Poslechová rozhraní



Ve výchozím nastavení naslouchá Watchtower na `:9911`, což odpovídá portu `9911` na všech dostupných rozhraních. Uživatelé mohou definovat vlastní naslouchající rozhraní pomocí volby `--Watchtower.listen=`. Svou konfiguraci můžete zkontrolovat v poli `"listeners"` v poli `lncli tower info`. Pokud máte potíže s připojením ke svému Watchtower, zkontrolujte, zda je otevřen `<port>` nebo zda je váš proxy server správně nakonfigurován na aktivní Interface.



#### Externí IP adresy



Uživatelé mohou také zadat externí IP adresu Watchtower pomocí `Watchtower.externalip=`, čímž se zobrazí úplný URI Watchtower (pubkey@host:port) prostřednictvím RPC nebo `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



URI Watchtower lze sdělit zákazníkům k připojení a použití pomocí následujícího příkazu:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Pokud zákazníci Watchtower potřebují vzdálený přístup, ujistěte se, že :




- Otevřete port 9911 (nebo port definovaný pomocí `Watchtower.listen`).
- Pomocí proxy serveru přesměrujte provoz z otevřeného portu na naslouchající port Watchtower Address.



#### Skryté služby Tor



Strážní věže podporují skryté služby Tor a mohou automaticky generate při spuštění pomocí následujících možností:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Při dotazu `lncli tower info` se pak v poli `"uris"` objeví soubor .onion Address:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



poznámka: veřejný klíč Watchtower je odlišný od veřejného klíče uzlu `LND`. Prozatím slouží jako "bílá listina Soft", protože zákazníci musí znát veřejný klíč Watchtower, aby jej mohli používat jako zálohu, dokud nebudou k dispozici pokročilejší mechanismy bílé listiny. Doporučujeme tento veřejný klíč NEZVEŘEJŇOVAT, pokud nejste připraveni vystavit svůj Watchtower celému internetu._



#### Adresář databáze Watchtower



Databázi Watchtower lze přesunout pomocí volby `Watchtower.towerdir=`. Všimněte si, že ke zvolené cestě bude přidána přípona `/Bitcoin/Mainnet/Watchtower.db`, aby se databáze oddělily podle řetězce. Nastavení `Watchtower.towerdir=/path/to/towerdir` tedy vytvoří databázi na adrese `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Například v systému Linux je výchozí databáze Watchtower umístěna na adrese :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfigurace klienta Watchtower



Pro konfiguraci klienta Watchtower potřebujete dvě položky:





- Aktivujte klienta Watchtower pomocí možnosti `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI aktivního serveru Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Tímto způsobem můžete nakonfigurovat několik strážních věží.



#### Sazby poplatků za právní úkony



Uživatelé mohou volitelně nastavit sazbu poplatků za transakce justice pomocí volby `wtclient.sweep-fee-rate`, která přijímá hodnoty v sat/byte. Výchozí hodnota je 10 sat/byte, ale je možné usilovat o vyšší sazby, aby se dosáhlo vyšší priority během poplatkové špičky. Změna `sweep-fee-rate` se vztahuje na všechny nové aktualizace po restartu daemon.



#### Dohled



Pomocí příkazu `lncli wtclient` mohou nyní uživatelé komunikovat přímo s klientem Watchtower a získávat nebo upravovat informace o všech registrovaných strážních věžích.



Například pomocí příkazu `lncli wtclient tower` můžete zjistit počet relací, které jsou aktuálně vyjednány s výše přidaným zařízením Watchtower, a díky poli `active_session_candidate` zjistit, zda se používá pro zálohování.



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



Chcete-li získat informace o relacích Watchtower, použijte volbu `--include_sessions`.



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



Všechny možnosti konfigurace klienta Watchtower jsou dostupné pomocí `lncli wtclient -h` :



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




## 2 - Instalace vlastního oka Satoshi



*Tento návod je částečně převzat z článku na blogu [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). V původní verzi byly provedeny úpravy*



Oko Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) je nedepoziční blesk Watchtower, který odpovídá [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Skládá se ze dvou hlavních součástí:





- teos**: obsahuje příkazový řádek Interface (CLI) a základní serverové funkce Watchtower. Při kompilaci tohoto _crate_ se vytvoří dva binární soubory - **teosd** a **teos-CLI**.





- teos-common**: obsahuje sdílené funkce na straně serveru a klienta (užitečné při vytváření klienta).



Pro správné spuštění Watchtower je třeba před spuštěním Watchtower příkazem **teosd** spustit **bitcoind**. Před spuštěním těchto dvou příkazů je třeba nakonfigurovat soubor **Bitcoin.conf**. Zde je návod, jak to udělat:





- Nainstalujte Bitcoin core ze zdrojového kódu nebo si jej stáhněte. Po stažení umístěte soubor **Bitcoin.conf** do uživatelského adresáře Bitcoin core. Další informace o tom, kam soubor umístit, naleznete na tomto odkazu, protože to závisí na použitém operačním systému.





- Po určení místa přidejte následující možnosti:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: pro požadavky RPC





- rpcuser** a **rpcpassword**: ověřování klientů RPC na serveru





- regtest**: není vyžadován, ale je užitečný, pokud plánujete vývoj.



Hodnoty **rpcuser** a **rpcpassword** si zvolíte sami. Musí být zapsány bez uvozovek. Například:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Pokud nyní spustíte **bitcoind**, uzel by se měl spustit.





- Pro část Watchtower musíte nejprve nainstalovat **teos** ze zdrojového kódu. Postupujte podle pokynů uvedených na tomto odkazu.





- Po úspěšné instalaci systému **teos** a spuštění testů můžete přejít k poslednímu kroku: nastavení souboru **teos.toml** v uživatelském adresáři teos. Soubor by měl být umístěn ve složce s názvem **.teos** (všimněte si tečky) ve vašem domovském adresáři. Například **/home//.teos** pod Linuxem. Po nalezení umístění vytvořte soubor **teos.toml** a nastavte tyto volby v souladu se změnami provedenými na **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Všimněte si, že zde musí být uživatelské jméno a heslo zapsány **v uvozovkách**. Na základě předchozího příkladu :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Po provedení těchto úkonů byste měli být připraveni ke spuštění Watchtower. Protože běžíme na **regtest**, je pravděpodobné, že při prvním připojení Watchtower nebyly v naší testovací síti Bitcoin vytěženy žádné bloky (pokud ano, je něco špatně). Watchtower vytváří interní mezipaměť posledních 100 bloků **bitcoind**; při prvním spuštění se tedy může objevit následující chyba:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Protože používáme **regtest**, můžeme bloky Miner vydat příkazem RPC, aniž bychom museli čekat na průměrné desetiminutové zpoždění, které se vyskytuje v jiných sítích (např. Mainnet nebo Testnet). Podrobnosti o tom, jak provádět bloky Miner, najdete v nápovědě **bitcoin-cli**.



![Image](assets/fr/01.webp)



To je vše: úspěšně jste spustili Watchtower. Gratulujeme. 🎉




## 3 - Konfigurace zařízení Watchtower v systému Umbrel



V systému Umbrel je připojení k uzlu Watchtower za účelem ochrany uzlu Lightning velmi jednoduché, protože vše se provádí prostřednictvím grafického rozhraní Interface. Po vzdáleném připojení k uzlu otevřete aplikaci "**Lightning Node**".



![Image](assets/fr/02.webp)



Klikněte na tři malé tečky vpravo nahoře na displeji Interface a vyberte možnost "**Rozšířená nastavení**".



![Image](assets/fr/03.webp)



V nabídce "**Watchtower**" jsou k dispozici dvě možnosti:





- Služba Watchtower**: tato možnost umožňuje provozovat službu Watchtower, tj. službu, která monitoruje kanály ostatních uzlů a odhaluje pokusy o podvod. V případě narušení váš Watchtower zveřejní transakci na Blockchain a umožní tak uživatelům získat zpět své zablokované prostředky. Po aktivaci se objeví URI vašeho Watchtower, který lze sdělit ostatním uzlům, aby jej mohly přidat do svého klienta Watchtower;





- Watchtower Client**: tato možnost umožňuje připojení k externím strážním věžím pro ochranu vlastních kanálů. Po aktivaci můžete přidávat služby Watchtower, kterým bude váš uzel předávat potřebné informace o svých kanálech. Tyto hlídací věže pak budou monitorovat jejich stav a v případě pokusu o podvod zasáhnou.



Prioritou pro vás je samozřejmě aktivace *Watchtower Client* pro ochranu vašeho uzlu, ale doporučuji vám také aktivovat *Watchtower Service*, abyste na oplátku přispěli k bezpečnosti ostatních uživatelů.



![Image](assets/fr/04.webp)



Poté klikněte na tlačítko Green "**Uložit a restartovat uzel**". Váš LND se restartuje.



Ve stejné nabídce najdete také URI služby Watchtower, pokud jste ji aktivovali. Můžete také přidat URI externí služby Watchtower pro ochranu svých kanálů. Kliknutím na tlačítko "**ADD**" potvrďte výběr.



![Image](assets/fr/05.webp)



Na internetu je k dispozici několik strážních věží. Například [LN+ a Voltage nabízejí altruistickou Watchtower](https://lightningnetwork.plus/Watchtower), ke které se můžete připojit:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Další možností je Exchange váš Watchtower URI s vašimi kolegy bitcoinery, takže každý chrání uzel toho druhého.



Doporučuji také zřídit několik strážních věží, aby se snížilo riziko v případě, že jedna z nich nebude dostupná.



Nakonec můžete upravit parametr "**Sazba poplatku za prověření klienta Watchtower**". Ten definuje maximální sazbu poplatku, kterou jste ochotni zaplatit za zahrnutí vysílací trestné transakce Watchtower do bloku. Ujistěte se, že jste nastavili dostatečně vysokou hodnotu, přizpůsobenou částkám blokovaným ve vašich kanálech.