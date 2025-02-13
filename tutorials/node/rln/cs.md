---
name: Uzel RGB Lightning
description: Jak spustím uzel Lightning kompatibilní s RGB pomocí RLN?
---
![cover](assets/cover.webp)

V tomto tutoriálu se krok za krokem dozvíte, jak nastavit uzel Lightning RGB v prostředí Regtest. Ukážeme si, jak vytvářet tokeny RGB a obíhat je v kanálech.

## Projekt RLN

Tým RGB společnosti Bitfinex pracuje od roku 2022 na obohacení ekosystému RGB vývojem kompletního technologického zásobníku. Spíše než na vytvoření jediného komerčního produktu se jeho úsilí zaměřuje na zpřístupnění open-source softwarových cihel, přispívání ke specifikacím protokolu RGB a vytváření implementačních referencí.

Mezi významné příspěvky společnosti Bitfinex do ekosystému RGB patří [knihovna *RGBlib*](https://github.com/RGB-Tools/rgb-lib) napsaná v jazyce Rust a přístupná prostřednictvím vazeb v jazycích Kotlin a Python, která výrazně zjednodušuje vývoj aplikací RGB tím, že zapouzdřuje složité mechanismy validace a zapojení.

Tým Bitfinexu také navrhl mobilní peněženku RGB s názvem "[*Iris Wallet*](https://iriswallet.com/)", která je k dispozici pro Android. Tato peněženka integruje použití RGB proxy serveru pro snadnou správu výměn dat mimo řetězec (*consignments*) pro *Client-side Validation* na RGB.

Společnost Bitfinex také vyvinula projekt `rgb-lightning-node` (RLN). Jedná se o démona Rust založeného na forku `rust-lightning` (LDK), upraveného tak, aby zohledňoval existenci aktiv RGB v kanálu. Při otevření kanálu lze zadat přítomnost tokenů RGB a při každé aktualizaci stavu kanálu se vytvoří přechod stavu, který odráží rozložení tokenů ve výstupech Lightning. To umožňuje :


- Otevřete například kanály Lightning v USDT;
- Směrovat tyto tokeny po síti za předpokladu, že směrovací cesty mají dostatečnou likviditu;
- Využití logiky trestu a časového zámku blesku bez úprav: stačí ukotvit přechod RGB v dalším výstupu transakce závazku.

Kód RLN je stále ve fázi alfa: doporučujeme jej používat pouze v **regtestu** nebo na **testnetu**.

## Připomenutí protokolu RGB

RGB je protokol, který běží nad Bitcoinem a napodobuje funkce chytrých smluv a správu digitálních aktiv, aniž by přetěžoval blockchain, na kterém je založen. Na rozdíl od běžných on-chain chytrých smluv (jako například na Ethereu) se RGB spoléhá na systém "*Client-side validation*": většinu dat a historie stavů si vyměňují a ukládají výhradně zúčastnění účastníci, zatímco v blockchainu Bitcoinu se nacházejí pouze malé kryptografické závazky (prostřednictvím mechanismů jako *Tapret* nebo *Opret*). V protokolu RGB tedy bitcoinový blockchain slouží pouze jako server pro časové razítkování a systém ochrany proti dvojímu utrácení.

Smlouva RGB je strukturována jako evoluční stavový stroj. Začíná Genesis, která definuje počáteční stav (popisující například nabídku, ticker nebo jiná metadata) podle striktně typovaného a sestaveného Schema. Poté se použijí stavové přechody a v případě potřeby stavová rozšíření, aby se tento stav upravil nebo rozšířil. Každá operace, ať už jde o převod zastupitelných aktiv (RGB20), nebo o vytvoření jedinečných aktiv (RGB21), zahrnuje *Jednorázové pečetě*. Ty propojují bitcoinové UTXO se stavy mimo řetězec a zabraňují dvojímu utrácení, přičemž zajišťují důvěrnost a škálovatelnost.

Chcete-li se dozvědět více o tom, jak protokol RGB funguje, doporučuji vám absolvovat toto komplexní školení:

https://planb.network/courses/csv402
## Instalace uzlu Lightning kompatibilního s RGB

Pro kompilaci a instalaci binárního souboru `rgb-lightning-node` začneme klonováním úložiště a jeho podmodulů a poté spustíme příkaz :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Volba `--recurse-submodules` rovněž klonuje potřebná dílčí zařízení (včetně upravené verze `rust-lightning`);
- Volba `--shallow-submodules` omezuje hloubku klonu, aby se urychlilo stahování, a zároveň poskytuje přístup k základním revizím.

V kořenovém adresáři projektu spusťte následující příkaz pro kompilaci a instalaci binárního souboru :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` zajistí, že bude dodržena verze závislostí;
- `--debug` není povinné, ale může vám pomoci se soustředit (pokud chcete, můžete použít `--release`) ;
- `--path .` říká `cargo install`, aby instaloval z aktuálního adresáře.

Na konci tohoto příkazu bude ve vašem `$CARGO_HOME/bin/` k dispozici spustitelný soubor `rgb-lightning-node`. Ujistěte se, že je tato cesta ve vašem `$PATH`, abyste mohli příkaz vyvolat z libovolného adresáře.

## Předpoklady

Démon `rgb-lightning-node` potřebuje ke své funkci přítomnost a konfiguraci :


- Uzel `bitcoind`**

Každá instance RLN bude muset komunikovat s `bitcoind`, aby mohla vysílat a monitorovat své transakce v řetězci. Démonovi bude třeba poskytnout autentizaci (přihlašovací jméno/heslo) a adresu URL (hostitel/port).


- Indexer** (Electrum nebo Esplora)

Démon musí být schopen vypsat a prozkoumat transakce v řetězci, zejména najít UTXO, na kterém bylo aktivum ukotveno. Je třeba zadat adresu URL serveru Electrum nebo Esplora.


- Proxy server RGB**

Proxy server je součást (volitelná, ale velmi doporučená), která zjednodušuje výměnu *konzistencí RGB* mezi rovnocennými uživateli Lightning. Opět je třeba zadat adresu URL.

ID a adresy URL se zadávají při *odemknutí* démona prostřednictvím rozhraní API.

## Spuštění Regtestu

Pro jednoduché použití je k dispozici skript `regtest.sh`, který prostřednictvím nástroje Docker automaticky spustí sadu služeb: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

To umožňuje spustit místní, izolované a předem nakonfigurované prostředí. Při každém restartu vytvoří a zničí kontejnery a datové adresáře. Začneme tím, že spustíme :

```bash
./regtest.sh start
```

Tento skript bude :


- Vytvoření adresáře `docker/` pro uložení ;
- Spusťte `bitcoind` v regtestu, stejně jako indexer `electrs` a `rgb-proxy-server` ;
- Počkejte, až bude vše připraveno k použití.

![RLN](assets/fr/04.webp)

Dále spustíme několik uzlů RLN. V samostatných shellech spusťte například (pro spuštění 3 uzlů RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- Parametr `--network regtest` označuje použití konfigurace regtest;
- `--daemon-listening-port` udává, na kterém portu REST bude uzel Lightning naslouchat voláním API (JSON);
- `--ldk-peer-listening-port` určuje, na kterém portu Lightning p2p se má naslouchat;
- `dataldk0/`, `dataldk1/` jsou cesty k úložným adresářům (každý uzel ukládá své informace samostatně).

Díky rozhraní API můžete nyní provádět příkazy na uzlech RLN z prohlížeče. Zejména zde můžete *odemknout* démony. Stačí otevřít prohlížeč na stejném počítači jako vaše uzly a zadat adresu URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Aby mohl uzel otevřít kanál, musí mít nejprve bitcoiny na adrese vygenerované následujícím příkazem (například pro uzel č. 1):

```bash
curl -X POST http://localhost:3001/address
```

Odpověď vám poskytne adresu.

![RLN](assets/fr/06.webp)

V regtestu `bitcoind` budeme těžit několik bitcoinů. Spusťte :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Zašlete finanční prostředky na výše vygenerovanou adresu uzlu:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Poté vytěžte blok a potvrďte transakci:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Spuštění Testnetu (bez Dockeru)

Pokud chcete testovat realističtější scénář, můžete uzly RLN spustit v síti Testnet, nikoli v Regtestu, a nasměrovat je na veřejné služby nebo služby, které máte pod kontrolou:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Ve výchozím nastavení, pokud není nalezena žádná konfigurace, se démon pokusí použít :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

S přihlášením :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Tyto prvky můžete také přizpůsobit prostřednictvím rozhraní API `init`/`unlock`.

## Vydání tokenu RGB

Pro vydání tokenu začneme vytvořením "barevných" UTXO:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Pořadí můžete samozřejmě upravit. Pro potvrzení transakce těžíme :

```bash
./regtest.sh mine 1
```

Nyní můžeme vytvořit aktivum RGB. Příkaz bude záviset na typu aktiva, které chcete vytvořit, a jeho parametrech. Zde vytvářím token NIA (*Non Inflatable Asset*) s názvem "PBN" se zásobou 1000 jednotek. Příkaz `přesnost` umožňuje definovat dělitelnost jednotek.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

Odpověď obsahuje ID nově vytvořeného aktiva. Nezapomeňte si tento identifikátor poznamenat. V mém případě je to :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Poté ji můžete přenést do řetězce nebo ji přidělit do kanálu Lightning. Přesně to uděláme v následující části.

## Otevření kanálu a přenos aktiva RGB

Nejprve je nutné připojit uzel k partnerovi v síti Lightning pomocí příkazu `/connectpeer`. V mém příkladu ovládám oba uzly. Tímto příkazem tedy získám veřejný klíč svého druhého uzlu Lightning:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Příkaz vrátí veřejný klíč mého uzlu č. 2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Dále otevřeme kanál zadáním příslušného aktiva (`PBN`). Příkaz `/openchannel` umožňuje definovat velikost kanálu v satoshi a rozhodnout se pro zařazení aktiva RGB. Záleží na tom, co chcete vytvořit, ale v mém případě je příkaz :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Více informací najdete zde:


- `peer_pubkey_and_opt_addr`: Identifikátor peera, ke kterému se chceme připojit (veřejný klíč, který jsme našli dříve);
- `capacity_sat`: Celková kapacita kanálu v satoshi ;
- `push_msat`: (zde okamžitě přenesu 10 000 sats, aby mohl později provést přenos RGB) ;
- `asset_amount`: Množství prostředků RGB, které mají být přiděleny kanálu ;
- `asset_id` : Jedinečný identifikátor aktiva RGB zapojeného do kanálu;
- `public`: Uvádí, zda má být kanál veřejný pro směrování v síti.

![RLN](assets/fr/14.webp)

K potvrzení transakce je vytěženo 6 bloků:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Kanál Lightning je nyní otevřen a obsahuje také 500 tokenů `PBN` na straně uzlu č. 1. Pokud chce uzel č. 2 obdržet tokeny `PBN`, musí vygenerovat fakturu. Zde je návod, jak to udělat:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

S :


- `amt_msat`: (minimálně 3000 sats) ;
- `expiry_sec` : Doba platnosti faktury v sekundách ;
- `asset_id` : Identifikátor aktiva RGB přiřazeného k faktuře ;
- `asset_amount`: Částka aktiva RGB, která má být převedena s touto fakturou.

V reakci na to obdržíte fakturu RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Tuto fakturu nyní zaplatíme z prvního uzlu, který má potřebnou hotovost s tokenem `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Platba byla provedena. To lze ověřit provedením příkazu :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Zde se dozvíte, jak nasadit uzel Lightning upravený pro přenos prostředků RGB. Tato ukázka je založena na :


- Prostředí regtest (přes `./regtest.sh`) nebo testnet ;
- Uzel Lightning (`rgb-lightning-node`) založený na `bitcoind`, indexeru a `rgb-proxy-serveru` ;
- Řada rozhraní JSON REST API pro otevírání/uzavírání kanálů, vydávání tokenů, přenos aktiv prostřednictvím služby Lightning atd.

Díky tomuto procesu :


- Transakce Lightning engagement zahrnují další výstup (OP_RETURN nebo Taproot) s ukotvením přechodu RGB;
- Převody se provádějí úplně stejným způsobem jako tradiční platby Lightning, ale s přidáním tokenu RGB;
- Více uzlů RLN může být propojeno, aby bylo možné směrovat a experimentovat s platbami napříč více uzly, pokud je na cestě dostatečná likvidita jak v bitcoinech, tak v aktivech RGB.

Pokud vám tento návod přišel užitečný, budu vám vděčný, když mi pod něj dáte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Doporučuji také tento další návod, ve kterém vysvětluji, jak použít nástroj RGB CLI vyvinutý sdružením LNP/BP k vytvoření smlouvy RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4