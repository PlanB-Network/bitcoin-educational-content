---
name: RGB
description: Úvod a tvorba aktiv na RGB
---

![cover](assets/cover.webp)

## Úvod

Dne 3. ledna 2009 spustil Satoshi Nakamoto první uzel Bitcoinu, od tohoto okamžiku se přidávaly nové uzly a Bitcoin začal fungovat jako by to byla nová forma života, forma života, která neustále evoluuje, postupně se stal nejbezpečnější sítí na světě díky svému jedinečnému designu, velmi dobře promyšlenému Satoshiho, protože prostřednictvím ekonomických pobídek přitahuje uživatele, běžně nazývané těžaře, k investování energie a výpočetního výkonu, což přispívá k bezpečnosti sítě.

Jak Bitcoin pokračuje ve svém růstu a adopci, setkává se s problémy škálovatelnosti, síť Bitcoin umožňuje těžit nový blok s transakcemi přibližně každých 10 minut, předpokládáme-li, že máme za den 144 bloků s maximálními hodnotami 2700 transakcí na blok, Bitcoin by umožnil pouze 4,5 transakce za sekundu, Satoshi byl tohoto omezení vědom, můžeme to vidět v emailu1 poslaném Mike Hearnovi v březnu 2011, kde vysvětluje, jak funguje to, co dnes známe jako platební kanál. mikroplatby rychle a bezpečně bez čekání na potvrzení. Zde vstupují do hry protokoly off-chain.

Podle Christiana Deckera2 jsou protokoly off-chain obvykle systémy, ve kterých uživatelé používají data z blockchainu a spravují je bez dotyku samotného blockchainu až do poslední chvíle. Na základě tohoto konceptu vznikla Lightning Network, síť, která umožňuje provádět platby Bitcoinem téměř okamžitě a protože ne všechny tyto operace jsou zapsány na blockchain, umožňuje tisíce transakcí za sekundu a škálování Bitcoinu.

Výzkum a vývoj v oblasti protokolů off-chain na Bitcoinu otevřel Pandorinu skříňku, dnes víme, že můžeme dosáhnout mnohem více než přenos hodnoty decentralizovaným způsobem, nezisková asociace LNP/BP Standards Association se zaměřuje na vývoj protokolů vrstvy 2 a 3 na Bitcoinu a Lightning Network, mezi tyto projekty vyniká RGB.

## Co je RGB?

RGB vzešlo z výzkumu Petera Todda3 na téma jednorázových pečetí a validace na straně klienta, který byl v letech 2016-2019 Giacomem Zuccem a komunitou přetvořen do lepšího protokolu pro aktiva pro Bitcoin a Lightning network. Další vývoj těchto myšlenek vedl k vývoji RGB do plně vybaveného systému chytrých kontraktů pod vedením Maxima Orlovského, který od roku 2019 s účastí komunity vede jeho implementaci.

RGB můžeme definovat jako sadu otevřených protokolů, které nám umožňují provádět složité chytré kontrakty škálovatelným a důvěrným způsobem. Nejedná se o konkrétní síť (jako Bitcoin nebo Lightning); každý chytrý kontrakt je pouze sada účastníků kontraktu, kteří mohou interagovat pomocí různých komunikačních kanálů (výchozí je Lightning network). RGB používá blockchain Bitcoinu jako vrstvu závazku stavu a udržuje kód chytrého kontraktu a data off-chain, což z něj činí škálovatelné, využívající transakce Bitcoinu (a Script) jako systém kontroly vlastnictví pro chytré kontrakty; zatímco vývoj chytrého kontraktu je definován off-chain schématem, nakonec je důležité poznamenat, že vše je validováno na straně klienta.

Jednoduše řečeno, RGB je systém, který umožňuje uživateli auditovat chytrý kontrakt, provést ho a ověřit individuálně kdykoliv bez dodatečných nákladů, protože pro to nepoužívá blockchain jako "tradiční" systémy, systémy složitých chytrých kontraktů byly průkopníkem Ethereum, ale kvůli tomu, že vyžaduje od uživatele významné množství plynu pro každou operaci, nikdy nedosáhly slibované škálovatelnosti a v důsledku toho nikdy nebyly možností pro bankovnictví uživatelů vyloučených ze současného finančního systému.
Aktuálně odvětví blockchainu propaguje, že jak kód chytrých kontraktů, tak data musí být uložena v blockchainu a vykonávána každým uzlem sítě, bez ohledu na nadměrné zvětšování velikosti nebo zneužití výpočetních zdrojů. Schéma navržené RGB je mnohem inteligentnější a efektivnější, protože přerušuje blockchainový paradigma tím, že má chytré kontrakty a data oddělená od blockchainu a tím se vyhýbá saturaci sítě viděné na jiných platformách, zároveň nenutí každý uzel k vykonání každého kontraktu, ale spíše strany zapojené, což přidává důvěrnost na úroveň dosud nevídanou.
![RGB vs Ethereum](assets/1.webp)

## Chytré kontrakty v RGB

Ve chytrém kontraktu RGB vývojář definuje schéma určující pravidla, jak se kontrakt vyvíjí v čase. Schéma je standardem pro konstrukci chytrých kontraktů v RGB, a jak vydavatel při definování kontraktu pro vydání, tak peněženka nebo burza musí dodržovat určité schéma, proti kterému musí kontrakt validovat. Pouze pokud je validace správná, může každá strana přijímat požadavky a pracovat s aktivem.

Chytrý kontrakt v RGB je směrovaný acyklický graf (DAG) změn stavu, kde je vždy známa pouze část grafu a k zbytku není přístup. Schéma RGB je základní sada pravidel pro vývoj tohoto grafu, se kterým chytrý kontrakt začíná. Každý účastník kontraktu může k těmto pravidlům přidávat (pokud to schéma dovoluje) a výsledný graf je postaven z iterativní aplikace těchto pravidel.

## Zaměnitelná aktiva

Zaměnitelná aktiva v RGB následují specifikaci LNPBP RGB-20, když je definován RGB-20, data aktiva známá jako "genesis data" jsou distribuována přes Lightning network, která obsahují to, co je potřebné k použití aktiva. Nejzákladnější forma aktiv nedovoluje sekundární vydání, spalování tokenů, přejmenování nebo nahrazení.

Někdy bude vydavatel potřebovat v budoucnu vydat více tokenů, např. stablecoiny jako USDT, které udržují hodnotu každého tokenu vázanou na hodnotu inflační měny jako je USD. K dosažení toho existují složitější schémata RGB-20, a kromě genesis dat vyžadují, aby vydavatel vyprodukoval konzignace, které budou také cirkulovat v Lightning network; s těmito informacemi můžeme znát celkové množství aktiva v oběhu. Totéž platí pro spalování aktiv nebo změnu jejich názvu.

Informace související s aktivem mohou být veřejné nebo soukromé: pokud vydavatel vyžaduje důvěrnost, může se rozhodnout nezveřejňovat informace o tokenu a provádět operace v absolutním soukromí, ale máme také opačný případ, kdy vydavatel a držitelé potřebují, aby celý proces byl transparentní. Toho je dosaženo sdílením dat tokenu.

## Postupy RGB-20

Postup spalování deaktivuje tokeny, spálené tokeny již nelze používat.

Postup nahrazení nastane, když jsou tokeny spáleny a je vytvořeno nové množství stejného tokenu. To pomáhá snižovat velikost historických dat aktiva, což je důležité pro udržení rychlosti aktiva.

Pro podporu případu použití, kdy je možné spalovat aktiva bez nutnosti je nahrazovat, se používá podschéma RGB-20, které umožňuje pouze spalování aktiv.

## Nezaměnitelná aktiva
Nefungibilní aktiva v RGB následují specifikaci LNPBP RGB-21, když pracujeme s NFT, máme také hlavní schéma a podschéma. Tato schémata mají proceduru gravírování, která nám umožňuje připojit vlastní data ze strany majitele tokenu, nejběžnějším příkladem, který dnes u NFT vidíme, je digitální umění spojené s tokenem. Vydavatel tokenu může toto gravírování dat zakázat použitím podschématu RGB-21. Na rozdíl od jiných blockchainových systémů NFT, RGB umožňuje distribuovat data médií velké velikosti u tokenu zcela decentralizovaným a odolným proti cenzuře způsobem, využívajícím rozšíření Lightning P2P sítě nazvané Bifrost, které se také používá pro vytváření mnoha dalších forem funkcionalit chytrých kontraktů specifických pro RGB.
Kromě fungibilních aktiv a NFT, RGB a Bifrost lze použít k vytváření dalších forem chytrých kontraktů, včetně DEXů, likviditních poolů, algoritmických stabilních mincí atd., o kterých se dozvíme v budoucích článcích.

## NFT z RGB vs NFT z jiných platforem

- Není potřeba drahého blockchainového úložiště
- Není potřeba IPFS, místo toho se používá rozšíření Lightning sítě (nazvané Bifrost) (a je plně šifrováno end-to-end)
- Není potřeba speciálního řešení pro správu dat – opět, Bifrost plní tuto roli
- Není potřeba důvěřovat webovým stránkám, aby udržovaly data pro NFT tokeny nebo o vydávaných aktivech / kontraktních ABI
- Vestavěné DRM šifrování a správa vlastnictví
- Infrastruktura pro zálohy pomocí Lightning Network (Bifrost)
- Způsoby monetizace obsahu (nejen prodej samotného NFT, ale i přístup k obsahu, několikrát)

## Závěry

Od spuštění Bitcoinu před téměř 13 lety bylo provedeno mnoho výzkumů a experimentů v této oblasti, úspěchy i chyby nám umožnily lépe pochopit, jak se decentralizované systémy chovají v praxi, co je činí skutečně decentralizovanými a jaké akce je vedou k centralizaci, to vše nás dovedlo k závěru, že skutečná decentralizace je vzácný a těžko dosažitelný jev, skutečnou decentralizaci dosáhl pouze Bitcoin a z tohoto důvodu se snažíme stavět právě na něm.

RGB má svou vlastní zajímavost uvnitř zajímavosti Bitcoinu, zatímco padám těmito zajímavostmi, budu psát o tom, co jsem se naučil, v dalším článku budeme mít úvod do LNP a RGB uzlů a jak je používat.

# Návod na RGB-uzel

## Úvod

V tomto návodu vysvětlíme, jak používat RGB-uzel k vytvoření fungibilního tokenu a jak jej převést, tento dokument je založen na demo RGB-uzlu a liší se tím, že tento návod používá skutečná testnetová data a pro to musíme sestavit vlastní částečně podepsanou Bitcoinovou transakci, psbt odteď.

## Požadavky

Doporučuje se použití distribuce Linuxu, tento návod byl napsán s použitím Pop!OS, který je založen na Ubuntu a budete potřebovat:

- cargo
- Bitcoin core
- git
Poznámka: Tento tutoriál ukazuje provádění příkazů v terminálu Linuxu, aby bylo možné rozlišit, co uživatel píše a jakou odpověď dostává v terminálu, používáme symbol $ symbolizující bash prompt.
Budete potřebovat nainstalovat některé závislosti:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Sestavení & Spuštění

RGB-node je ve vývoji (WIP), a proto se musíme umístit na konkrétní commit (3f3c520c19d84c66d430e76f0fc68c5a66d79c84), abychom jej mohli správně zkompilovat a používat, pro toto provedeme následující příkazy.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Nyní to zkompilujeme, nezapomeňte použít přepínač --locked, protože byla zavedena zásadní změna ve verzi clap.

```
$ cargo install --path . --all-features --locked

....
....
    Dokončeno vydání [optimalizované] cíle(ů) za 2m 14s
  Instalace do /home/user/.cargo/bin/fungibled
  Instalace do /home/user/.cargo/bin/rgb-cli
  Instalace do /home/user/.cargo/bin/rgbd
  Instalace do /home/user/.cargo/bin/stashd
   Nainstalovaný balíček `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (spustitelné soubory `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Jak nám říká rust kompilátor, binární soubory byly zkopírovány do adresáře $HOME/.cargo/bin, pokud váš kompilátor je zkopíroval na jiné místo, musíte se ujistit, že tento adresář je zahrnut v $PATH.

Mezi nainstalovanými binárními soubory můžeme vidět tři daemony nebo služby (soubory, které končí na d) a jedno cli (rozhraní příkazové řádky), cli nám umožňuje interagovat s hlavním daemonem rgbd. V tomto tutoriálu budeme spouštět dva uzly, budeme také potřebovat dva klienty, každý se musí připojit ke svému vlastnímu uzlu, pro to vytvoříme dva aliasy.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Můžeme spustit pouze aliasy nebo je přidat na konec souboru $HOME/.bashrc a spustit source $HOME/.bashrc.
Předpoklad

RGB-node nezpracovává žádnou funkcionalitu související s peněženkou, provádí pouze úkoly specifické pro RGB na datech, která budou poskytnuta externí peněženkou jako bitcoin core. Konkrétně, abychom demonstrovali základní pracovní postup s vydáním a převodem, budeme potřebovat:

- issuance_utxo, ke kterému rgb-node-0 přiřadí nově vydaný majetek
- receive_utxo, kde rgb-node-1 přijme majetek
- change_utxo, kde rgb-node-0 přijme změnu majetku
- částečně podepsanou bitcoinovou transakci (tx.psbt), jejíž výstupní veřejný klíč bude upraven tak, aby obsahoval závazek k převodu.

Budeme používat bitcoin core cli, potřebujeme mít běžící bitcoind daemon na testnetu, což nám poskytne interoperabilitu a nakonec budeme moci poslat naše vlastní aktiva jinému uživateli RGB, který následoval tento tutoriál.
Pro zjednodušení přidáme tento alias na konec našeho souboru ~/.bashrc.
```
alias bcli="bitcoin-cli -testnet"
```

Pojďme si vypsat naše nepoužité transakční výstupy a vybrat dva, jeden bude issuance_utxo a druhý change_utxo, nezáleží na tom, který je který, důležité je, že vydavatel má kontrolu nad těmito dvěma UTXO.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Než budeme pokračovat, musíme mluvit o outpointech, jedna transakce může zahrnovat více výstupů, outpoint zahrnuje jak 32-bajtový TXID, tak 4-bajtové číslo indexu výstupu (vout) k odkazování na konkrétní výstup oddělené dvojtečkou :. V našem seznamu nepoužitých výstupů můžeme najít dva UTXO, na každém vidíme txid a vout, to jsou naše outpointy pro issuance_utxo a change_utxo.

receive_utxo je UTXO kontrolované příjemcem, v tomto případě použijeme e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0, což je outpoint z jiné peněženky.
- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Nyní budeme vytvářet částečně podepsanou transakci (tx.psbt), jejíž výstup bude upraven tak, aby zahrnoval závazek k převodu, nezapomeňte nahradit txid a vout vašimi vlastními, cílová adresa není důležitá, může být vaše nebo od někoho jiného, nezáleží na tom, kam ty sats půjdou, důležité je, že používáme issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

Výstup nám dal psbt v kódování base64, které použijeme k vytvoření tx.psbt.
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt```

Vytvořme nový adresář nazvaný rgbdata, ve kterém budou uloženy datové adresáře každého uzlu.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Už se nacházíme v $HOME/rgbdata, spustíme každý uzel v různých terminálech, kde ~/.cargo/bin je adresář, kam cargo zkopírovalo všechny binární soubory po instalaci rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Vydání

Pro vydání aktiva spustíme rgb0-cli s podpříkazy fungible issue, poté argumenty, ticker USDT, název "USD Tether" a v alokaci použijeme vydávané množství a issuance_utxo, jak vidíme níže:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Aktivum úspěšně vydáno. Použijte tyto informace pro sdílení:
Informace o aktivu:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
název: USD Tether
popis: ~
známýOběh: 1000
jeVydáníZnámé: ~
limitVydání: 0
řetězec: testnet
desetinnáPřesnost: 0
datum: "2022-02-23T20:53:26"
známéProblémy:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    množství: 1000
    původ: ~
známáInflace: {}
známéAlokace:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    odhalenéMnožství:
      hodnota: 1000
      zaslepení: "0000000000000000000000000000000000000000000000000000000000000001"
genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0

Získáme assetId, které potřebujeme pro převod aktiva.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Generování zaslepeného UTXO

Aby mohl rgb-node-1 přijmout nové USDT, musí vygenerovat zaslepené UTXO odpovídající receive_utxo pro držení aktiva.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Zaslepený outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Tajemství zaslepení outpointu: 1679197189805229975
```

Abychom mohli přijímat převody související s tímto UTXO, budeme potřebovat původní receive_utxo a blinding_factor.

## Převod

Pro převod určitého množství aktiva na rgb-node-1 potřebujeme poslat jej na zaslepené UTXO, rgb-node-0 musí vytvořit konzignaci a odhalení a zapsat je do bitcoinové transakce. Poté budeme potřebovat psbt, který upravíme tak, aby zahrnoval závazek. Kromě toho nám možnosti -i a -a umožňují poskytnout vstupní outpoint, který by byl původem aktiva, a alokaci, kde obdržíme změnu, musíme to uvést následovně @<change_utxo>.
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Převod byl úspěšný, konzignace a odhalení jsou zapsány do "consignment.rgb" a "disclosure.rgb", částečně podepsaná transakce svědka do "witness.psbt"
Údaje k zásilce k sdílení: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6w5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
Tento příkaz vytvoří tři nové soubory, consignment, disclosure a psbt včetně úpravy, tento psbt se nazývá witness transaction, consignment je odeslán do rgb-node-1.

## Witness

Witness transaction by měla být podepsána a vysílána, pro to potřebujeme zpětně zakódovat do base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Podepište to pomocí subpříkazu walletprocesspsbt.
```yaml
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=", "complete": true

Nyní finalizujte a získejte hex.
```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Vysílání

Vysílejte to pomocí příkazu sendrawtransaction, aby bylo potvrzeno do blockchainu.

```
```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```

## Přijmout

Pro přijetí příchozího převodu by rgb-node-1 měl obdržet soubor consignment od rgb-node-0, mít receive_utxo a odpovídající blinding_factor vygenerovaný během generování slepého UTXO.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Převod aktiva úspěšně přijat.
```

Nyní můžeme vidět (v poli knownAllocations) nové rozdělení 100 jednotek aktiva v <receive_utxo> spuštěním:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```
```
název: USD Tether
popis: ~
známýOběh: 1000
jeVydáníZnámé: ~
limitVydání: 0
řetězec: testnet
desetinnáPřesnost: 0
datum: "2022-02-23T20:53:26"
známéProblémy:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    množství: 1000
    původ: ~
známáInflace: {}
známéAlokace:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    odhalenéMnožství:
      hodnota: 1000
      zaslepení: "0000000000000000000000000000000000000000000000000000000000000001"
  - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
    index: 1
    outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
    odhalenéMnožství:
      hodnota: 100
      zaslepení: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0

Protože receive_utxo bylo zaslepeno při převodu, platící rgb-node-0 nemá informace o tom, kam bylo posláno 100 USDT, takže místo není zobrazeno v známýchAlokacích.

$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
```
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

Ale jak vidíte, rgb-node-0 nemůže vidět změnu 900 aktiv, kterou jsme poskytli příkazu transfer s argumentem -a. Aby rgb-node-0 mohl změnu zaregistrovat, musí přijmout odhalení.

```
$ rgb0-cli fungible enclose disclosure.rgb

Data odhalení úspěšně uzavřena.
```

Pokud byl rgb-node-0 úspěšný, změnu můžete vidět výpisem aktiva.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether
```
```
popis: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  datum: "2022-02-23T20:53:26"
  známéProblémy:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      množství: 1000
      původ: ~
  známáInflace: {}
  známéAlokace:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      odhalenéMnožství:
        hodnota: 1000
        zaslepení: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      odhalenéMnožství:
        hodnota: 900
        zaslepení: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```

## Závěry

Byli jsme schopni vytvořit zaměnitelný aktivum a přesunout jej z jedné transakce do druhé soukromým způsobem, pokud bychom zkontrolovali potvrzenou transakci v prohlížeči bloků, nenašli bychom nic odlišného od běžné transakce, to je díky tomu, že RGB používá jednorázové pečetě pro úpravu transakcí. V tomto příspěvku dělám úvod do toho, jak RGB funguje.

Tento příspěvek může obsahovat chyby, pokud něco najdete, prosím, dejte mi vědět, abych mohl tento průvodce vylepšit, návrhy a kritiky jsou také vítány, šťastné hackování! 🖖