---
name: Zeus Embedded - Pokročilý
description: Víceuzlová samosprávná Lightning peněženka
---

![Zeus](assets/cover.webp)


## Úvod do systému ZEUS Wallet


ZEUS je mobilní aplikace pro správu Bitcoin Wallet a uzlů s plnými funkcemi bleskového Bitcoin Wallet, která usnadňuje platby Bitcoin, poskytuje uživatelům úplnou kontrolu nad jejich financemi a pokročilejším uživatelům umožňuje spravovat jejich bleskové uzly z ruky.


### Pro koho je ZEUS určen?

V současné době je ZEUS určen pro lidi, kteří provozují vlastní domácí / obchodní uzly [Lightning Network Daemon (LND)](https://lightning.engineering/) nebo [Core Lightning (CLN)](https://blockstream.com/lightning/) a spravují je vzdáleně prostřednictvím Zeusu.


Obchodníci používající [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) nebo [Alby](https://getalby.com/) (nebo jakýkoli jiný účet LNDhub) se také mohou připojit ke svým uzlům / účtům, používat je a spravovat je prostřednictvím ZEUS.


[Od verze v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) začne ZEUS vycházet vstříc běžným uživatelům, kteří chtějí jednoduchý způsob, jak provádět rychlé a levné bitcoinové platby ze svého mobilního zařízení, prostřednictvím [integrovaného mobilního Lightning uzlu](https://docs.zeusln.app/category/embedded-node) s vestavěným [Lightning Service Providerem (LSP)](https://docs.zeusln.app/lsp/intro).


### Důležité zdroje systému Zeus:


- Oficiální stránky Zeus - [https://zeusln.app/](https://zeusln.app/)
- Dokumentace k programu Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repozitář Zeus na Githubu](https://github.com/ZeusLN/zeus)
- [Telegramová skupina podpory Zeus](https://t.me/ZeusLN)
- [Zeus na NOSTR](https://iris.to/zeus@zeusln.app)
- [Oznámení na blogu Zeus](https://blog.zeusln.com)


### Funkce systému Zeus

#### Obecné vlastnosti:


- Pouze pro vlastní potřebu, Bitcoin a Lightning Wallet
- Žádné poplatky za zpracování, žádný KYC
- Plně otevřený zdrojový kód (APGLv3)
- Podpora více uzlů / účtů (můžete spravovat vlastní domácí uzel (uzly), spustit vložený uzel LND, připojit se k více účtům LNDhub)
- Snadno použitelná nabídka aktivit
- Šifrování PIN nebo passphrase, režim soukromí - skrývání citlivých údajů
- Kontaktní kniha, více témat, více jazyků


#### Technické vlastnosti


- Připojení přes Tor
- Plná podpora LNURL (platba, výběr, ověření, kanál), odesílání na adresy Lightning
- Podrobná správa kanálů osvětlení, podpora MPP/AMP, Keysend, správa poplatků za směrování
- Replace-by-fee (RBF) a podpora "dítě platí za rodiče" (CPFP)
- Platby a žádosti NFC, podepisování a ověřování zpráv
- Podpora SegWit a Taproot
- Jednoduché kanály Taproot
- Bleskové adresy pro vlastní potřebu (@zeuspay.com)
- Prodejní místo od Square (brzy otevřené PoS)


### Průvodci a videonávody

Abyste mohli Zeus používat a spravovat kanály Blesku, likviditu, poplatky atd., je lepší si nejprve přečíst několik důležitých příruček o Lightning Network.


#### Průvodci:


- [LND - Dokumentace Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Dokumentace Core Lightning](https://lightning.readthedocs.io/index.html)
- [Průvodce Lightning pro začátečníky](https://bitcoiner.guide/lightning/) – od Bitcoin Q&A
- [Správa Lightning uzlu](https://www.lightningnode.info/) – od openoms
- [Lightning Network a analogie s letištěm](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Správa likvidity Lightning uzlu](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Údržba Lightning uzlu](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Videonávod od BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Průvodce, jak začít používat vestavěný uzel Zeus LN v mobilním zařízení


![Image](assets/en/01.webp)


Tuto příručku věnuji všem novým uživatelům Lightning Network (LN), kteří se chtějí vydat na novou suverénní cestu pomocí samospustitelného uzlu Wallet na svých mobilních zařízeních.


Uvažujme, že jste již prošli celou tou spoustou úschovných peněženek LN, ale ještě nejste připraveni začít provozovat PUBLIC routingový uzel LN, jen chcete naskládat více Sats nad LN více samospádem a provádět své pravidelné platby přes LN.


Zde přichází Zeus, počínaje [verzí v0.8.0 oznámenou na jejich blogu](https://blog.zeusln.com/new-release-zeus-v0-8-0/), nyní nabízí vestavěný uzel LND přímo v aplikaci. Až dosud byl Zeus aplikací pro správu vzdálených uzlů + účtů LNDhub. Ale teď… uzel je v telefonu!


![Image](assets/en/02.webp)


### Stručná rekapitulace hlavních funkcí pro Zeus Node:



- Soukromý uzel LND - To znamená, že tento uzel NEBUDE provádět veřejné směrování ostatních plateb přes váš uzel. Uzel a kanály jsou neohlášené (soukromé, nejsou viditelné ve veřejném grafu LN). Přijímání a provádění plateb bude probíhat důkladně přes vaše připojené vrstevníky LSP. PAMATUJTE: Uzel Zeus Embedded NEBUDE provádět veřejné směrování!
- **Trvalá služba LND** - uživatel může tuto funkci aktivovat a udržovat službu LND nepřetržitě aktivní jako jakýkoli běžný uzel LN. Aplikace nemusí být otevřená, trvalá služba udrží veškerou komunikaci online.
-   **Filtry bloků Neutrino** - synchronizace bloků je prováděna pomocí [blokových filtrů a protokolu Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (aniž by byly sdíleny informace o on-chain prostředcích našich uživatelů). Připomínka: pro vysokou latenci / pomalé internetové připojení může tato synchronizace bloků založená na Neutrinu občas selhat. Zkuste se přepnout na blízký Neutrino server, což může pomoci obnovit synchronizaci. Bez této synchronizace váš LND uzel nemůže začít!
- Jednoduché kanály **Taproot** - Při uzavření těchto kanálů jsou uživatelům účtovány nižší poplatky a je jim poskytnuto více soukromí, protože se při zkoumání jejich stopy On-Chain jeví jako jakýkoli jiný výdaj Taproot.
- **Integrovaný LSP** - Olympus je nový uzel LSP pro Zeus. Uživatelé mohou ihned znovu přijímat signál Sats přes LN, aniž by předtím museli nastavovat kanály LN. Jednoduše budou muset vytvořit LN Invoice a platit z jakéhokoli jiného LN Wallet, se službou Zeus 0-conf channel. Více informací o Zeus LSP najdete zde. Služba LSP také poskytuje našim uživatelům dodatečné soukromí tím, že jim poskytuje zabalené faktury, které před plátci skrývají veřejné klíče jejich uzlů.
- **Kniha kontaktů** - kontakty můžete ukládat ručně nebo je importovat z NOSTR, abyste mohli snadno posílat platby na svá pravidelná místa určení.
- Plná podpora LNURL, odesílání a přijímání **LN Address** - nyní si můžete nastavit vlastní samospustitelný LN Address s @zeuspay.com. Připomínáme: Zeus můžete používat také pro LN-auth na webech, kde se můžete přihlásit pomocí LN autentizace. Je velmi praktické.
- **Prodejní místo** - Nyní si mohou uživatelé z řad obchodníků nastavit vlastní položky produktů a prodávat je přímo ze systému Zeus díky integrovanému PoS. Zatím obsahuje základní potřeby, ale v budoucnu bude obsahovat rozšířené funkce.
- **Protokoly služby LND** - uživatel může v reálném čase číst protokoly služby LND a používat je k ladění případných problémů (především špatných připojení)
- **Automatické zálohování** - kanály uzlu LN jsou automaticky zálohovány na serveru Olympus. Tato automatická záloha je šifrována s vaším uzlem Wallet seed (bez uzlu seed je zcela nepoužitelná). Uživatel může také ručně exportovat SCB (statickou zálohu kanálů) pro obnovu po havárii.


### Jak se dostat na palubu s uzlem Zeus LN (LND embedded)


V této příručce budu hovořit pouze o vestavěném LND uzlu a ne o jiných způsobech používání této skvělé aplikace (správa vzdálených uzlů a účty LNDhub). Pro jiné typy připojení se prosím podívejte na [stránku dokumentace Zeus](https://docs.zeusln.app/category/getting-started), která je velmi dobře vysvětlena a není třeba psát samostatný návod.


#### KROK 1 - POČÁTEČNÍ NASTAVENÍ


Vzhledem k tomu, že Zeus je kompletní uzel LND, budu mít několik počátečních doporučení:



- Nepoužívejte staré zařízení, které by mohlo ovlivnit používání této výkonné aplikace. Zejména v období synchronizace by aplikace mohla intenzivně využívat procesor a paměť RAM. Jejich nedostatek by mohl dokonce znemožnit používání aplikace Zeus.
- Jako mobilní operační systém používejte alespoň Android 11 a co nejvíce jej aktualizujte. Pro iOS totéž, snažte se používat mnohem vyšší verzi OS.
- Pro ukládání dat budete potřebovat alespoň 1 GB místa na disku. Časem by mohl narůst i více, ale existuje funkce pro zkompaktnění databáze na úroveň MB.
- Není nutné používat Zeus se službou Tor nebo Orbot. Prosím, nekomplikujte věci víc, než je nutné. Tor vám v tomto případě nenabídne více soukromí, ale pouze zhorší situaci při počáteční synchronizaci. Dávejte si také pozor na to, jakou VPN používáte, a zkontrolujte latenci připojení směrem k neutrinovým serverům. Mějte na paměti, že blokovací filtr Neutrino nevypouští ani nesleduje identitu vašeho zařízení, jsou to pouze obslužné bloky. Provoz LN je také za LSP s privátními kanály, takže ven se dostane jen velmi málo informací, není důvod se děsit o soukromí.
-   Mějte trpělivost při počáteční synchronizaci, může to trvat několik minut. Snažte se být připojeni k širokopásmovému internetovému připojení s nízkou latencí. Pokud provozujete vlastní Bitcoin uzel, [můžete aktivovat službu neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) a připojit svůj Zeus k vlastnímu uzlu, dokonce i pomocí interní LAN, takže budete mít maximální rychlost.


Jakmile nastavíte typ připojení "Embedded node", aplikace se začne na chvíli synchronizovat. Trpělivě vyčkejte na dokončení této části a poté vstupte na hlavní stránku Nastavení.


![Image](assets/en/03.webp)


Než začnete Zeus používat, projděme si stručně jednotlivé sekce Nastavení a pochopíme některé hlavní funkce:


**A - NASTAVENÍ**


Toto je sekce s obecnými nastaveními pro celou aplikaci


**1 - Lightning Service Provider (LSP)**


Zde jsou uvedeny dvě služby LSP:



- _Kanály v pravý čas_ - pokud nemáte otevřený žádný kanál nebo k dispozici příchozí likviditu, aktivovaná služba vám otevře kanál za běhu. Tuto možnost lze vypnout, pokud nechcete otevírat více kanálů tohoto typu.
- _Požádat o kanály předem_ - příchozí kanály si můžete zakoupit od poskytovatele služeb Olympus LSP přímo v aplikaci s několika možnostmi a částkami (pro příchozí a odchozí kanály).


LSP pomáhá uživatelům připojit se k síti Lightning tím, že otevírá platební kanály k jejich uzlům. [Přečtěte si více o LSP zde](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS má nový integrovaný LSP s názvem [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), který je k dispozici všem uživatelům využívajícím nový vestavěný uzel.


V této sekci je ve výchozím nastavení Olympus LSP (https://0conf.lnolymp.us), ale brzy můžete nastavit i jiný 0conf LSP, který tento protokol podporuje.


_Keep in mind:_

_když si otevřete kanál s Olympus LSP pomocí zabalených faktur LN, získáte také likviditu 100k příchozích! To je opravdu dobrá volba v případě, že potřebujete ihned obdržet další Sats._

_Příklad: vložíte 400k Sats pro otevření kanálu LSP, pak LSP otevře kanál s kapacitou 500k Sats směrem k vašemu uzlu Zeus a posune 400k Sats, které jste vložili, na vaši stranu._

_"Příchozí likvidita" = více "prostoru" ve vašem kanálu pro příjem._


Doufáme, že v budoucnu bychom mohli mít mnoho dalších LSP, které by mohly být integrovány do systému Zeus a používat alternativně každý z nich. Je jen otázkou času, kdy nové LSP přijmou otevřený standard pro tento druh 0conf kanálů.


Pokud nechcete otevírat nové kanály "za běhu", můžete tuto možnost zakázat.


V téže sekci máte také možnost zvolit "request Simple Taproot Channels", když LSP otevře kanál směrem k uzlu Zeus. Tyto jednoduché kanály Taproot nabízejí lepší soukromí On-Chain a nižší poplatky při uzavření kanálu. Existují pouze dva důvody, proč byste je neměli chtít používat:



- Jsou nové a při jejich používání se v LND mohou stále vyskytovat chyby.
- Vaše protistrana je nepodporuje. Dokonce i uzly LND se k nim musí prozatím výslovně přihlásit.


**2 - Nastavení plateb**


Tato funkce vám nabídne možnost nastavit si vlastní preferované poplatky za platby přes LN nebo onchain. Rovněž poskytne možnost zvýšit nebo snížit časový limit pro vaše faktury.


Pokud některé z plateb LN selžou, můžete poplatek zvýšit a najít lepší cestu. Také pokud děláte onchain txs, můžete nastavit konkrétní poplatek, aby váš tx nemohl skončit na dlouhou dobu zaseknutý v Mempool, v případě vysokých poplatků období.


**3 - Nastavení faktur**


V této části jsou uvedeny některé možnosti pro faktury generate:



- Nastavení standardní poznámky, která se má zobrazit v Invoice you generate
- Doba vypršení platnosti v sekundách, pokud chcete, aby byl váš Invoice zaplacen za určitou dobu, delší nebo kratší
- Zahrňte nápovědu k trase - poskytněte informace k nalezení neinzerovaných nebo soukromých kanálů. To umožňuje směrování plateb do uzlů, které nejsou v síti veřejně viditelné. Nápověda ke směrování poskytuje částečnou trasu mezi soukromým uzlem příjemce a veřejným uzlem. Tato směrovací nápověda je pak zahrnuta do příkazu Invoice generovaného příjemcem a poskytnutého plátci. Navrhuji, aby byla ve výchozím nastavení povolena, jinak by příchozí platby mohly selhat (nebyla nalezena žádná trasa).
- AMP Invoice - Atomic Multi-path Payments jsou novým typem bleskových plateb implementovaných pomocí LND, které umožňují přijímat platby Sats bez konkrétního Invoice pomocí [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Je prakticky statickým kódem platby. [Více informací naleznete zde](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Zobrazit vlastní pole předobrazu - tuto možnost použijte pouze ve velmi specifických případech, kdy chcete v předobrazu opravdu použít vlastní pole. [Více informací zde](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Další možností v této části je nastavení typu řetězce Address, který chcete použít: SegWit vnořený, SegWit, Taproot.


![Image](assets/en/04.webp)


Klikněte na horní tlačítko kolečka a zobrazí se vyskakovací okno pro výběr požadovaného typu Address. Jakmile jej nastavíte, při příštím stisknutí tlačítka pro příjem onchain se zobrazí generate vybraného typu Address. Kdykoli jej můžete změnit.


**4 - Nastavení kanálů**


V této sekci můžete přednastavit některé funkce úvodních kanálů, jako jsou:



- počet potvrzení
- Oznamovat kanál (ve výchozím nastavení je vypnuto), to znamená, že se bude jednat o neoznámené kanály
- Jednoduché kanály Taproot
- Zobrazit tlačítko pro nákup kanálu


**5 - Nastavení ochrany osobních údajů**


Zde najdete několik základních nastavení pro zvýšení soukromí pomocí aplikace Zeus:



- Block explorer pro otevření detailů tx (Mempool.space, blockstream.info nebo vlastní osobní)
- Číst schránku - přepínač zapnuto/vypnuto, pokud chcete, aby Zeus četl schránku vašeho zařízení
- Režim Lurker - přepínač zapnutí/vypnutí, pokud chcete skrýt konkrétní citlivé informace z aplikace Zeus. Je dobrou volbou při vytváření ukázek nebo snímků obrazovky.
- Návrh poplatků Mempool - tuto možnost aktivujte, pokud chcete použít doporučené úrovně poplatků z [Mempool.space](https://Mempool.space/)


**6 - Bezpečnost**


V této části jsou pouze dvě možnosti zabezpečení aplikace při otevření: nastavení hesla nebo kódu PIN.


Po nastavení kódu PIN pro otevření aplikace můžete také nastavit "PIN pro vynucení". Tento tajný dodatečný kód PIN bude použit POUZE v případě nátlakové situace, pokud vás někdo ohrozí. Pokud tento kód PIN zadáte, konfigurace se celá VYMAŽE. Proto raději aktualizujte své zálohy. Automatické zálohování je ve výchozím nastavení ZAPNUTO, ale je dobré mít i vlastní zálohy mimo zařízení.


**7 - Měna**


Povolte nebo zakažte možnost zobrazení převodu fiat měny při používání aplikace Zeus. V současné době podporuje více než 30 světových fiat měn.


**8 - Jazyk**


Můžete přepínat mezi několika jazyky překladu, které byly přezkoumány komunitou Zeus s rodilými mluvčími.


**9 - Zobrazení**


V této části můžete přizpůsobit displej Zeus, vybrat různá barevná témata, výchozí obrazovku (klávesnice nebo rovnováha), zobrazit alias uzlu, aktivovat velká tlačítka klávesnice, zobrazit více desetinných míst.


**10 - Prodejní místo**


Jedná se o speciální funkci, která umožňuje povolit nebo zakázat integrovaný systém PoS v systému Zeus. Můžete provozovat samostatný PoS nebo propojený se systémem PoS Square. V současné době podporuje základní funkce jako PoS, ale pro dobrý začátek stačí a mohl by pomoci těm malým obchodníkům (bary/restaurace, potraviny) začít přijímat BTC nativním způsobem.


V tomto nastavení najdete různé možnosti nastavení PoS:



- Typ platby potvrzení: Pouze LN, 0-conf, 1-conf
- Povolení / zakázání spropitného pro zaměstnance obsluhující PoS
- Zobrazení / skrytí klávesnice
- Procento daně, které se uplatní na letenku
- Vytváření produktů a kategorií produktů
- Jednoduchý výpis všech prodejů


Zde je živé demo video, jak používat Zeus PoS:


**B - Záložní zdroj Wallet**


Vložený uzel v systému ZEUS je založen na formátu LND a používá formát [aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ten se liší od typického formátu [BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki), který můžete vidět ve většině peněženek Bitcoin, i když se může zdát podobný. Aezeed obsahuje některé další údaje včetně data narození Wallet, které pomohou efektivněji provést opětovné skenování během obnovy.


Formát klíče aezeed by měl být kompatibilní s následujícími mobilními peněženkami: Blixt, BlueWallet a Breez. Upozorňujeme, že samotný kód seed nebude stačit k obnovení všech zůstatků, pokud máte otevřené nebo čekající uzavírací kanály !


Další informace o procesu zálohování a obnovy naleznete na stránce [Zeus Docs](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


MOCNÁ PORADNA: Při ukládání seed si prosím uložte také klíč k uzlu! Někdy je dobré mít ho po ruce spolu s vaším seed a SCB (záloha statických kanálů) pro případ, že byste potřebovali ověřit obnovení.


SCB je nutný pouze v případě, že máte otevřené kanály LN. V případě, že máte pouze onchain fondy, není nutný.


Pokud vidíte, že po dlouhé době se stále nezobrazuje stará historie txs, přejděte do Vložený uzel - Peers a vypněte možnost použít seznam vybraných peers (ve výchozím nastavení je btcd.lnolymp.us). To vyvolá restart a připojí se k prvnímu dostupnému neutrálnímu uzlu s lepší časovou odezvou. Nebo použijte níže uvedené další známé neutrino peery.


Pokud chcete vidět další možnosti obnovy uzlu LND, [přečtěte si prosím můj předchozí návod](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), kde najdete postup, jak importovat aezeed seed do Sparrow Wallet nebo další metody.


**C - Vestavěný uzel**


V této části naleznete několik základních nástrojů pro správu integrovaného uzlu:



- _Záchrana po katastrofě_ - Automatické a ruční zálohování kanálů LN. Více informací o použití této funkce naleznete na stránce Zeus Docs.
- _Express Graph Sync_ - Aplikace Zeus stáhne datový graf drbů LN z vyhrazeného serveru, aby byla synchronizace rychlejší a lepší, a nabídne nejlepší platební cesty. Můžete si také zvolit vymazání předchozích dat grafu při spuštění.
- _Peers_ - sekce pro správu neutrinových peerů a peerů 0-conf. Pokud máte problémy s počáteční synchronizací, kanály nejsou online, je to proto, že vaše zařízení má vysokou latenci s nakonfigurovaným neutrino peerem. Zkuste přepnout seznam preferovaných peerů nebo přidejte svého konkrétního peera, o kterém víte, že má lepší latenci pro synchronizaci. Dobře známé servery neutrina jsou:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - pro region USA
 - sg.lnolymp.us - pro asijský region
 - btcd-Mainnet.lightning.computer - pro oblast USA
 - uswest.blixtwallet.com (Seattle) - pro region USA
 - europe.blixtwallet.com (Německo) - pro region EU
 - asia.blixtwallet.com - pro oblast Asie
 - node.eldamar.icu - pro oblast USA
 - noad.sathoarder.com - pro oblast USA
 - bb1.breez.technology | bb2.breez.technology - pro region USA
 - neutrino.shock.network - Region USA



- _LND logs_ - velmi užitečný nástroj pro ladění problémů s uzlem LN a pro podrobnou kontrolu toho, co se děje na vyšší technické úrovni.
- _Rozšířená nastavení_ - další nástroje pro ovládání používání uzlu LND:



 - _Režim hledání cesty_ - bimodální nebo apriorní, způsoby hledání lepší trasy pro platby LN a také obnovení předchozích informací o trase. Přečtěte si tyto velmi dobré návody o vyhledávání cest: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - autor: Docs Lightning Engineering a [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - autor: Voltage
 - _Persistent LND_ - tento režim aktivujte, pokud chcete, aby služba LND běžela nepřetržitě na pozadí a udržovala váš uzel online 24 hodin denně. To je velmi užitečné, pokud používáte Zeus jako PoS v malém obchodě nebo pokud přijímáte mnoho tipů LN přes LN Address.
 - _Rescan wallet_ - tato možnost spustí při restartu úplné skenování všech txs v řetězci Wallet. Aktivujte ji pouze v případě, že vám v Wallet chybí některé tx. Úloha rescan bude trvat nějakou dobu, několik minut, takže buďte trpěliví a vždy zkontrolujte protokoly, abyste viděli další podrobnosti o průběhu.
 - _Compact Database_ - tato možnost je velmi užitečná, pokud aplikace Zeus zabírá hodně místa v zařízení (viz podrobnosti o aplikaci v nastavení zařízení). Pokud používáte Zeus hodně aktivně, doporučuji toto zhušťování provádět častěji. Jakmile zjistíte, že máte více než 1-1,5 GB dat pro aplikaci Zeus, proveďte kompakci. Bude se restartovat a nějakou dobu potrvá, takže buďte trpěliví.
 - _Delete Neutrino files_ - tato možnost odstranění neutrinových souborů (s restartem) výrazně sníží využití datového úložiště. Snížení využití dat má také velký dopad na využití baterie, snižuje její spotřebu, zejména pokud Zeus používáte v trvalém režimu.


**D - Informace o uzlu**


V této části naleznete další podrobnosti o stavu uzlu Zeus jako:



- Alias - krátké ID uzlu
- Veřejný klíč - úplný veřejný klíč vašeho uzlu, který je potřebný pro ostatní uzly k nalezení cesty k vašemu uzlu. Nezapomeňte, že tento veřejný klíč NENÍ viditelný v běžných průzkumnících LN (Mempool, Amboss, 1ML atd.). Tento pubkey je dosažitelný POUZE prostřednictvím vašich připojených vrstevníků a kanálů LN.
- Implementační verze LN
- Verze aplikace Zeus
- Synchronizováno s řetězcem a Synchronizováno s grafem - velmi důležité údaje, které ukazují správný stav uzlu. Pokud se u těchto dvou nezobrazuje "true", znamená to, že se váš uzel stále synchronizuje nebo má nějaké problémy se synchronizací. Proto se doporučuje podívat se do protokolů LND nebo ještě chvíli počkat.
- Výška bloku a Hash - zobrazuje poslední blok a Hash, které váš uzel viděl a synchronizoval.


**E - Informace o síti**


V této části se zobrazují další podrobnosti o obecném stavu zařízení Lightning Network získané z dat synchronizace grafu: počet dostupných veřejných kanálů, počet uzlů, počet zombie kanálů (offline nebo mrtvých), průměr grafu, průměrný a maximální stupeň grafu.


Tato informační data mohou být užitečná pro ladění nebo jen pro statistiku.


**F - Lightning Address**


V této části si uživatel může nastavit vlastní úschovu LN Address @zeuspay.com.


ZEUS PAY využívá uživatelské předobrazy hashů, faktury HODL a atestační schéma Zaplocker Nostr, aby umožnil uživatelům, kteří nemusí být online 24 hodin denně, 7 dní v týdnu, přijímat platby na statický blesk Address. Uživatelé se pouze musí do 24 hodin přihlásit do své peněženky ZEUS, aby si mohli platby vyzvednout, jinak budou vráceny odesílateli.


Pokud aktivujete "trvalý režim", budou všechny platby na váš účet LN Address přijaty okamžitě.


Přečtěte si, jak fungují platby [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works), a více informací o [ZeusPay Fees here](https://docs.zeusln.app/lightning-Address/fees).


**G - Adresy v řetězci**


V této části můžete konzultovat své vygenerované adresy v řetězci pro lepší kontrolu mincí


**H - Kontakty**


Ve verzi 0.8.0 programu Zeus byl představen nový adresář kontaktů, který můžete použít k rychlému odesílání plateb svým přátelům a rodině, a to i s možností importu kontaktů z aplikace Nostr.


Jednoduše zadejte svůj Nostr npub nebo lidsky čitelný NIP-05 Address a ZEUS se zeptá Nostru na všechny vaše kontakty. Odtud můžete odeslat rychlou platbu kontaktu nebo importovat všechny nebo vybrané kontakty do místního adresáře./<


Zde je krátké video, jak nastavit a používat kontakty Zeus:


**I - Nástroje**


Zde máme různé podsekce s dalšími nástroji:



- _Účty_ - zde můžete importovat externí účty / peněženky, peněženky Cold, peněženky Hot, které můžete ovládat nebo používat jako externí zdroj financování pro kanály uzlů Zeus. Tato funkce je zatím experimentální.
- _Zrychlení transakce_ - Tato funkce by mohla být užitečná, když se vám zasekne tx do Mempool a chcete zvýšit poplatek. Budete muset zadat výstup tx z detailů tx a vybrat požadovaný nový poplatek, který chcete použít. Musí být vyšší než předchozí a vyžaduje, abyste měli v řetězci Wallet k dispozici více prostředků.


![Image](assets/en/05.webp)


Musíte přejít do čekajícího tx a zkopírovat výstupní bod txid. Poté přejděte do této sekce a vložte jej, poté vyberte nový poplatek, který chcete použít k jeho naražení. V tu chvíli se objeví nová obrazovka s doporučenými poplatky, nebo si můžete nastavit vlastní. Nezapomeňte, že MUSÍ být vyšší než předchozí.


Vždy je lepší mít v řetězci Wallet na Zeusovi UTXO s maximálně 100k Sats, abyste ho mohli použít k nárazovým poplatkům, když je to nutné.



- _Podepsat nebo ověřit_ - Pomocí této funkce můžete podepsat konkrétní zprávu pomocí klíčů Wallet. Lze ji také použít k ověření zprávy, aby se prokázalo, že pochází z konkrétních klíčů Wallet.
- _Currency converter_ - jednoduchý nástroj pro výpočet převodu kurzu mezi BTC a jinými fiat měnami.


**J - Obchod a podpora**


Zde najdete další informace a odkazy o Zeusovi, internetovém obchodě, sponzorech a sociálních médiích.


**K - Nápověda**


V této poslední sekci najdete odkazy na stránku s dokumentací Zeus, na Github issues (pokud chcete odeslat chybu nebo požadavek přímo vývojářům aplikace) a na e-mailovou podporu.



### KROK 2 - ZAHÁJENÍ POUŽÍVÁNÍ UZLU ZEUS



Pamatujte, že Zeus je určen především k použití jako LN Wallet, pro snadné a rychlé platby přes LN. Jistě, obsahuje také onchain Wallet, ale ten by měl být používán výhradně pro otevírání/zavírání kanálů LN a ne pro pravidelné platby kávy.


Přečtěte si prosím můj další návod [jak se stát vlastní bankou pomocí 3 úrovní Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


V tuto chvíli má uživatel 2 možnosti, jak začít Zeus používat:



- Přímo přes LN, pomocí kanálu 0-conf od Olympus LSP
- Vložte nejprve v řetězci Wallet a poté otevřete normální kanál LN s požadovaným partnerem.


#### Metoda A - Použití Olympus LSP


Jedná se o velmi snadný a přímočarý způsob, jak zapojit nového uživatele LN do systému Zeus. Může se jednat o zcela nového uživatele Bitcoin, který nemá žádný Sats, kterého na palubu nalodil přítel, nebo o nového obchodníka, který začíná se svou první platbou LN.


Ve výchozím nastavení bude Zeus používat svůj vlastní LSP Olympus. Později však můžete pro otevření kanálů přepnout i na jiné LSP, které tento protokol 0-conf podporují.


Stačí, když si na svém systému Zeus vytvoříte účet Invoice (zadáte částku a kliknete na tlačítko "požádat"), a budete moci tyto účty Sats ihned obdržet.


Invoice, kterou jste generate, bude [zabalena](https://docs.zeusln.app/lsp/wrapped-invoices) a budou vám zobrazeny poplatky spojené se službou, pokud jsou zaplaceny. Tento zabalený Invoice obsahuje směrové nápovědy k vašemu uzlu Zeus, takže LSP by mohl najít váš nový uzel a otevřít kanál s novými prostředky, které vkládáte.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Chcete-li získat kanál LN od LSP s prostředky, které chcete obdržet 1. čas, musí být tento Invoice zaplacen z jiného LN Wallet a počkat několik okamžiků, až LSP otevře kanál směrem k vašemu uzlu Zeus, odečte poplatek a přenese zbývající částku platby na vaši stranu kanálu.


Stačí, když zaplatíte Invoice vygenerovaný v systému ZEUS dalším bleskem Wallet a kanál se vám okamžitě otevře. [Podívejte se prosím na poplatky za LSP v systému Zeus](https://docs.zeusln.app/lsp/fees).


Další výhodou placení za kanál je nulový poplatek za směrování. To znamená, že při směrování plateb není první skok přes OLYMPUS by ZEUS spojen s žádnými poplatky za směrování. Všimněte si, že přeskoky mimo společnost OLYMPUS by ZEUS jsou stále zpoplatněny.


Jakmile je kanál připraven, klikněte na pravé tlačítko ve spodní části obrazovky, které zobrazí kanály Zeus.


![Image](assets/en/08.webp)


A zobrazí se vám kanál, jako je tento, zobrazující vaši stranu vyvážení kanálu:


![Image](assets/en/09.webp)


Pokud z tohoto kanálu utratíte více, získáte větší příchozí likviditu. Za více Sats, které obdržíte do tohoto kanálu, budete mít méně prostoru pro příchozí likviditu.


Zde je pěkná jednoduchá názorná ukázka (od Reného Pickhardta), jak fungují kanály LN:


V tuto chvíli, vzhledem k ukázkové obrazovce kanálů, klikněte na název kanálu a zobrazí se o něm další podrobnosti.


Máte jeden kanál se společností Olympus o celkové kapacitě 490 000 Sats, přičemž na vaší straně je 378 000 Sats a na straně společnosti Olympus 88 000 Sats. To znamená, že na stejném kanálu můžete získat maximálně o 88k Sats více.


Pokud potřebujete získat více než 88k Sats (dostupná příchozí likvidita v tomto případě), řekněme dalších 500k Sats, prostým vytvořením nového LN Invoice s tímto množstvím se spustí nový požadavek na kanál LSP Olympus. Získáte tedy druhý kanál.


Proto, abyste nemuseli platit více poplatků za otevření více kanálů, doporučujeme otevřít poprvé větší kanál, řekněme 1-2M Sats. Jakmile je otevřen, můžete vyměnit za onchain část těchto Sats, řekněme 50 %, pomocí libovolné externí výměnné služby popsané v této příručce.


Jakmile z tohoto kanálu vyměníte řekněme 50 % a dostanete zpět Sats do svého vlastního Zeus onchain Wallet, jste připraveni přejít k dalšímu způsobu otevření nového kanálu - z onchain balance.


#### Metoda B - Použití zůstatku na řetězci


Pomocí této metody můžete otevřít kanály směrem k jakémukoli jinému uzlu LN, včetně stejného uzlu LSP společnosti Olympus. Pokud však již máte kanál s Olympusem, doporučuje se mít jej také s jiným uzlem, abyste byli spolehlivější a mohli také použít MPP (vícedílnou platbu).


![Image](assets/en/10.webp)


Výše je uveden příklad platby za LN Invoice pomocí MPP. Jak vidíte, v dolní části obrazovky máte "nastavení" a otevírá se rozbalovací stránka s dalšími podrobnostmi pro platbu, kterou se chystáte provést. Na této obrazovce, pokud máte otevřené alespoň 2 kanály, bude funkce MPP ve výchozím nastavení zapnutá. Také můžete aktivovat AMP (atomic multi-path) a nastavit konkrétní části, které chcete. Jedná se o výkonnou funkci!


Pro soukromý uzel jako Zeus bych doporučil mít 2-3 dobré kanály (max. 4-5), s dobrými LSP a dobrou likviditou, které pokryjí všechny vaše potřeby pro placení nebo příjem Sats přes LN. [Další rady ohledně likvidity uzlu LN najdete v této příručce](/nodes/managing-lightning-node-liquidity-cs.html). Také zde najdete další [obecnou příručku o likviditě uzlu LN](https://Bitcoin.design/guide/how-it-works/liquidity/) od týmu Bitcoin Design.


Vím, že výběr správných vrstevníků není snadný úkol ani pro zkušené uživatele. [Proto vám pro začátek uvedu několik možností](https://github.com/ZeusLN/zeus/discussions/2265), jedná se o peer uzly, které jsem sám testoval pomocí programu Zeus (snažil jsem se připojovat pouze k uzlům LND, abych se vyhnul problémům s nekompatibilitou)


Zde je také seznam zaručených rovnocenných uzlů pro Zeus. Pokud znáte dobré, můžete je do tohoto seznamu přidat.


Kanál v programu Zeus otevřete tak, že přejdete do zobrazení Kanály kliknutím na ikonu kanálu v pravém dolním rohu hlavního zobrazení a poté stisknete ikonu + v pravém horním rohu.


![Image](assets/en/11.webp)


Pokud chcete otevřít kanál s konkrétním uzlem, klikněte na (A) v horním rohu a naskenujte QR identifikátor uzlu (u Mempool, Amboss, 1ML můžete získat tento QR) a všechny údaje o partnerovi se vyplní.


UPOZORNĚNÍ:


- Vložený uzel Zeus nepoužívá službu Tor ! Proto se prosím nepokoušejte otevírat kanály s uzly, které jsou pod Tor! Spíše si tím uškodíte, než že byste si přidali více soukromí. Tor pro LN nenabízí více soukromí, ale přidává více problémů.
- vybírejte si moudře své partnery, raději dobré LSP, dobré směrovací uzly, ne náhodné plebejské uzly, které by mohly uzavřít vaše kanály a nemohly by nabídnout dobrou likviditu. [Zde jsem napsal speciální příručku](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) o likviditě a příkladu uzlů.


Pokud přímo kliknete na tlačítko "Open Channel to Olympus", vyplníte požadovaná pole pro otevření kanálu [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Na rozdíl od placených kanálů LSP bude váš kanál vyžadovat potvrzení On-Chain pomocí vašich prostředků v řetězci (můžete si vybrat z vašich UTXO v zobrazení otevřeného kanálu); neotevře se okamžitě. Nejprve se prosím podívejte na aktuální poplatky Mempool a podle toho je upravte v závislosti na tom, jak rychle chcete daný kanál otevřít.


Před stisknutím tlačítka pro otevření kanálu posuňte dolů rozšířené možnosti:


![Image](assets/en/12.webp)


Musíte se také ujistit, že kanál je neohlášený (soukromý). Ve výchozím nastavení je tato možnost pro oznámené kanály vypnutá. Tuto možnost se nedoporučuje aktivovat pro vestavěný uzel Zeus, je užitečná pouze v případě, že používáte Zeus se vzdáleným uzlem, jako veřejný směrovací uzel.


Na rozdíl od placených kanálů LSP nebudete při otevření kanálů touto metodou využívat směrování bez poplatků.


A hotovo, stačí kliknout na tlačítko "Otevřít kanál" a počkat na potvrzení tx těžaři. Jakmile je kanál otevřen, můžete s Sats ze svých kanálů provádět transakce podle svého uvážení.


Mějte na paměti, že tyto kanály budou mít veškerý zůstatek na VAŠÍ straně, takže nebudete mít příchozí likviditu. Jak jsem již řekl, vyměňte nebo utratte část Sats nákupem věcí přes LN, abyste si "udělali více místa" pro příjem.


Představte si kanály LN jako sklenici vody. Do prázdné sklenice (svého kanálu) nalijete trochu vody (Sats), dokud ji nenaplníte. Další vodu nemůžete nalít, dokud ji nevypijete (nevydáte / nevyměníte). Když je sklenice téměř prázdná, nalijte do ní další vodu (Sats) pomocí výměny. [Více informací o externích výměnných službách naleznete zde](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Existují také další služby LSP, které vám prodávají příchozí kanály: LNBig nebo Bitrefill. Myslím, že takových služeb je víc, ale teď si na ně nemůžu vzpomenout.


Pokud tedy potřebujete prakticky prázdný kanál LN (zůstatek je od začátku 100% na straně peera) pro příjem většího počtu plateb, než kolik zvládnete na svých stávajících zaplněných kanálech, může to být velmi dobrá volba. Za otevření těchto kanálů zaplatíte určitý poplatek a získáte dostatek příchozího prostoru.



## TIPY A TRIKY


### Limity příchozích rezerv


V tuto chvíli není možné kvůli některým omezením kódu LN získat přesně tolik, kolik se zobrazuje v položce "Příchozí". Vždy mějte na paměti, že byste měli faktury vystavovat s o něco nižší částkou, resp. částkou "Místní rezerva kanálu".


![Image](assets/en/13.webp)


Jak můžete vidět na výše uvedeném obrázku, "příchozí" zobrazuje, že mohu stále přijímat 5101 Sats, ale ve skutečnosti v tomto okamžiku je nemožné přijímat více. A můžete si všimnout, že je to stejné množství jako "Místní rezerva".


Proto mějte na paměti, že když vystavujete faktury k přijetí, podívejte se také na likviditu svých kanálů a odečtěte od této částky místní rezervu, pokud chcete pohledávku posunout až na hranici.


### Rychlá rada pro nové uživatele, kteří začínají s uzlem Zeus:



- Využijte správně své nové kanály.


Pokud například víte, že za týden obdržíte řekněme 1 milion Sats, otevřete si kanál 2 milionů Sats a vyměňte do onchainu Wallet nebo na jiný (dočasný) depozitní účet LN 50-60 % své odchozí likvidity. Vždy buďte připraveni s větším množstvím likvidity. Jakmile budete potřebovat více likvidity zpět do svých kanálů Zeus, můžete ji přesunout zpět z custodial účtů.


Pokud víte, že budete posílat řekněme 500 tisíc Sats týdně, otevřete si kanál s 1 milionem Sats. Tímto způsobem budete mít stále rezervu, dokud ji opět nenaplníte.



- Pokud jste obchodník a vždy budete pravidelně dostávat více, než utratíte, kupte si vyhrazený příchozí kanál. Je to nejlevnější způsob. Zaplatíte minimální poplatek a získáte "prázdný" kanál.



- Neotvírejte malé nesmyslné kanály 50-100-300-500k Sats. Zaplníte je během několika dní, i když je budete používat pouze pro zaps. Otevřete si větší a různé, NE jen jeden kanál.


Jakmile si otevřete větší kanál, můžete kdykoli použít externí podmořské swapy k přesunu Sats do svých onchain peněženek (včetně zpět do Zeus onchainu). Udržování rovnováhy mezi vstupní a výstupní likviditou je dobré a také můžete tyto Sats "znovu použít" k otevření dalších kanálů, pokud chcete.


### Zabalený Invoice


Pokud chcete při příjmu zajistit větší soukromí, můžete použít metodu "wrapped Invoice". Připomínám, že abyste mohli tuto funkci použít, potřebujete kanál se službou Olympus LSP. Zabalené faktury "skryjí" konečné místo určení (váš uzel Zeus) a zobrazí váš uzel LSP jako místo určení pro plátce.


Chcete-li získat zabalenou kartu Invoice, přejděte na hlavní obrazovku klávesnice, zadejte částku a stiskněte tlačítko Request. Zobrazí se normální QR kód pro váš Invoice. Nyní klikněte na tlačítko "X" vpravo nahoře a budete přesměrováni na další možnosti pro Invoice.


![Image](assets/en/14.webp)


Nyní musíte aktivovat tuto možnost nahoře "Enable LSP" a stisknout tlačítko "Create Invoice". Tato volba vytvoří zabalený Invoice a nezapomeňte, že bude účtovat malý poplatek.


### Faktury s nápovědou trasy


Tato funkce je velmi užitečná, pokud chcete spravovat likviditu více příchozích kanálů. Prakticky můžete určit, do kterého příchozího kanálu chcete přijímat Sats z Invoice.


Tuto funkci lze použít také pro kruhové rebalancování, když chcete přesunout likviditu z jednoho zaplněného kanálu do jiného vyčerpaného.


Jak vytvořit Invoice s nápovědou trasy?



- Na hlavní obrazovce posuňte zásuvku LN doprava a klikněte na "Receive"
- V nastavení Invoice přejděte do spodní části a aktivujte tlačítko "Vložit nápovědy k trase", poté vyberte záložku "Vlastní". Otevře se obrazovka se všemi vašimi dostupnými kanály. Vyberte ten, který chcete přijímat.
- Vyplňte všechny ostatní údaje Invoice, částku, poznámku atd. a klikněte na "create Invoice".
- Zaplacením této částky Invoice se Sats dostane do uvedeného kanálu.


Pokud chcete zaplatit sami sobě tento Invoice (kruhové vyrovnávání), při platbě ze stejného uzlu Zeus vyberte na obrazovce platby odchozí kanál (kanál s vyšší likviditou), který chcete použít jako odesílací platbu.


### Platba pomocí služby Keysend


Keysend je velmi podceňovaná funkce LN a uživatelé by ji měli používat častěji.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) umožňuje uživatelům v Lightning Network posílat platby ostatním , a to přímo na jejich veřejný klíč, pokud má jejich uzel veřejné kanály a povolený keysend. Keysend nevyžaduje, aby příjemce platby vydal Invoice.


Jak to můžete udělat se systémem Zeus?


Jednoduše naskenujte nebo zkopírujte ID cílového uzlu (nebo použijte kontakty Zeus pro uložení běžných cílových uzlů jako kontaktů) a poté na hlavní obrazovce Zeus klikněte na tlačítko "Odeslat". Na této obrazovce pak vložte ID uzlu nebo vyberte z kontaktů.


Zadejte částku Sats, případně zprávu (ano, můžete ji použít i jako tajný chat přes LN) a klikněte na tlačítko "Odeslat". Hotovo!


![Image](assets/en/15.webp)


Pokud máte přímý kanál s cílovým partnerem, nebudete platit žádné poplatky.


Pokud nemáte přímý kanál s cílovým partnerem, pak platba za odeslání klíčů zaplatí poplatky jako běžná platba LN Invoice, směrovaná po regulované cestě jako jakákoli jiná platba. Pouze nezapomeňte, že po ní nezůstane žádná stopa jako po LN Invoice.


## Conlusion


Doporučuji přečíst si navazující příručku [Advanced usage of Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) s dalšími pokyny a případy použití.


A... to je vše! Od této chvíle budete Zeus Node používat jako běžný BTC/LN Wallet v mobilu. Uživatelské rozhraní je poměrně přímočaré a snadno použitelné, intuitivní pro jakýkoli typ uživatele, myslím, že nemusím zadávat další podrobnosti o tom, jak provádět a přijímat platby.


Na závěr je zde srovnávací tabulka ochrany osobních údajů:


![Image](assets/en/16.webp)
