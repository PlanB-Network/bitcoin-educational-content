---
name: Liquid Bootcamp Essentials
goal: Získejte komplexní znalosti o projektech Liquid Network a Elements a naučte se implementovat pokročilá řešení v oblasti důvěrných transakcí, tokenizace a decentralizované síťové architektury.
objectives: 

  - Porozumět základům architektury Liquid a jejímu vztahu ke Bitcoin.
  - Naučte se konfigurovat a ovládat uzly Liquid pomocí softwaru Elements.
  - Prozkoumat využití důvěrných transakcí a vydávání aktiv v systému Liquid Network.
  - Porozumět obchodním a technickým aspektům Liquid pro aplikace na kapitálových trzích.

---

# Představení sítě Liquid


Vydejte se na vzdělávací cestu, jejímž cílem je hlubší pochopení projektu Liquid Network a Elements. Tento bootcamp kombinuje teorii a praxi a naučí vás technické, architektonické a obchodní základy nezbytné pro implementaci a využití možností Liquid. Tento kurz je ideální pro ty, kteří si chtějí rozšířit své znalosti o pokročilé nástroje v rámci ekosystému Bitcoin. Od důvěrných transakcí až po návrh ekosystému.


Kurz s prezentacemi odborníků z oboru zahrnuje témata, jako je architektura Liquid, tokenizační aplikace, technické koncepty Elements a inovativní případy použití, jako je Breez SDK. Kurz je navržen tak, aby byl přístupný začátečníkům a středně pokročilým uživatelům, ale nabízí hodnotu i zkušeným vývojářům, kteří se snaží zvládnout Liquid jako platformu pro optimalizaci svých projektů.

+++

# Úvod


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Přehled kurzů


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Vítejte na Liquid Bootcamp, komplexním školení, jehož cílem je vybavit vás znalostmi a dovednostmi pro efektivní využití projektu Liquid Network a Elements. Tento kurz nabízí komplexní seznámení s charakteristickými funkcemi Liquid, včetně Confidential Transactions, vydávání aktiv a jeho federativní síťové architektury, a zároveň představuje základní koncepty Elements, softwaru, který Liquid pohání.


V průběhu boot campu se seznámíte s praktickými aplikacemi Liquid Network, od nastavení a provozu uzlů až po pochopení jeho využití na kapitálových trzích a tokenizaci Bitcoin. Díky prezentacím odborníků z oboru získáte také vhled do pokročilých témat, jako jsou HTLC, SDK Breez a projekt Blockstream AMP.


Tento bootcamp byl původně pořádán jako osobní akce podle strukturovaného plánu (jak je znázorněno na obrázku) určeného pro živá setkání. Pro tuto úpravu kurzu byl však obsah přeorganizován tak, aby lépe vyhovoval online formátu a usnadnil studentům porozumění. Nové pořadí zajišťuje logický postup od základních pojmů k pokročilejším a technickým tématům, čímž maximalizuje zážitek z učení.


Tato cesta je strukturována tak, aby vyhovovala účastníkům s různou úrovní odborných znalostí, a nabízí kombinaci teoretických znalostí a praktických zkušeností. Na konci tohoto výcvikového tábora budete dobře rozumět architektuře Liquid, jeho integraci s Bitcoin a tomu, jak využívat jeho inovativní funkce k vytváření a optimalizaci finančních řešení.


Ponořte se do světa sidechainu Liquid a uvolněte jeho plný potenciál právě teď!

# Základy


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Architektura Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Architektura Liquid Network a model konsensu


Liquid Network je federativní postranní řetězec postavený na kódové základně Elements, který je navržen tak, aby rozšířil možnosti Bitcoin a zároveň se opíral o jeho základní zabezpečení. Na rozdíl od Bitcoin [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) funguje Liquid na modelu federativního [konsensu](https://planb.academy/resources/glossary/consensus). Síť je udržována globálně distribuovanou skupinou členů, včetně burz, obchodních míst a poskytovatelů infrastruktury. Z tohoto členstva je vybráno patnáct "funkcionářů", kteří působí jako podepisovači [bloků](https://planb.academy/resources/glossary/block).


Tito funkcionáři vytvářejí bloky deterministickým způsobem, přičemž každou minutu je vygenerován nový blok. Tento přesný časový plán je v kontrastu s pravděpodobnostními desetiminutovými intervaly Bitcoin. Aby byl blok platný, musí jej podepsat alespoň 11 z 15 funkcionářů (práh dvě třetiny plus jedna). Tento mechanismus zajišťuje Liquid "konečnost dvou bloků", což znamená, že jakmile má [transakce](https://planb.academy/resources/glossary/transaction-tx) dvě potvrzení (přibližně dvě minuty), je matematicky nemožné řetězec reorganizovat. Tato rychlost a jistota jsou rozhodující pro arbitráž, automatizované obchodování a rychlé vypořádání mezi burzami.


Federace je dynamická. Prostřednictvím protokolu dynamické federace (Dynafed) může síť střídat funkcionáře nebo aktualizovat parametry, aniž by bylo nutné provést tvrdý [fork](https://planb.academy/resources/glossary/fork). To umožňuje bezproblémový vývoj a výměnu hardwaru nebo členů systému při zachování nepřetržitého provozu.


### Confidential Transactions a správa majetku


Charakteristickým rysem systému Liquid je jeho nativní podpora systému Confidential Transactions (CT) a více prostředků. V hlavním řetězci Bitcoin jsou všechny údaje o transakci - odesílatel, příjemce a částka - veřejné. V Liquid využívá CT kryptografické závazky, které skrývají typ aktiva a částku před veřejnou účetní knihou a zároveň umožňují síti ověřit, že transakce je platná (tj. nedošlo k [inflaci](https://planb.academy/resources/glossary/inflation)). Konkrétní hodnoty mohou vidět pouze účastníci, kteří jsou držiteli zaslepovacích klíčů, což nabízí úroveň obchodního soukromí nezbytnou pro instituce, které přesouvají velké pozice.


Liquid považuje všechna aktiva za "nativní" občany [blockchainu](https://planb.academy/resources/glossary/blockchain). To zahrnuje Liquid Bitcoin (LBTC), stablecoiny jako USDT a bezpečnostní tokeny. Vydání aktiva nevyžaduje složité chytré smlouvy; jedná se o základní funkci protokolu.


#### Regulovaná aktiva a AMP

Pro aktiva vyžadující soulad s předpisy, jako jsou bezpečnostní tokeny, využívá Liquid platformu pro správu aktiv Blockstream (AMP). Ta zavádí vrstvu s povolením, kde transakce vyžadují druhý podpis od autorizačního serveru. To umožňuje emitentům prosazovat pravidla - například whitelisting nebo požadavky KYC - na granulární úrovni, čímž se kombinuje efektivita blockchainu s regulačními kontrolami tradičních financí.


### Obousměrný kolík a bezpečnostní infrastruktura


Spojení mezi Liquid a Bitcoin je udržováno pomocí obousměrného kolíku. Pro "peg-in" uživatel odešle Bitcoin na vygenerovanou adresu na mainchain. Tyto prostředky jsou uzamčeny na 102 potvrzení (zhruba 17 hodin), aby se eliminovalo riziko reorganizace. Po potvrzení je na sidechainu Liquid vyraženo ekvivalentní množství LBTC.


Proces "peg-out" umožňuje uživatelům vyměnit LBTC za Bitcoin. K tomu je zapotřebí spálení LBTC a kryptografická autorizace od federace. Aby se zabránilo krádežím, je peg-out přísně kontrolován autorizačními klíči (Peg-out Authorization Keys, PAK), které drží členové federace. Prostředky lze navíc okamžitě vyměnit prostřednictvím poskytovatelů třetích stran, jako je SideSwap, čímž se obejde zpoždění při vypořádání a zrychlí se likvidita.


#### Hardwarové bezpečnostní moduly (HSM)

Zabezpečení je přísně vynucováno prostřednictvím hardwaru. Funkcionáři neuchovávají [soukromé klíče](https://planb.academy/resources/glossary/private-key) na standardních serverech, ale používají hardwarové bezpečnostní moduly (HSM). Tato zařízení jsou vzdušně oddělena od logiky hostitelského serveru a jsou naprogramována podle přísných pravidel. HSM například odmítne podepsat blok, pokud jeho výška není větší než výška předchozího bloku, čímž zabrání přepisování historie. Tento "protichůdný" model zabezpečení předpokládá, že hostitelský server může být kompromitován, což zajišťuje, že klíče zůstanou v bezpečí i v případě narušení fyzického umístění.


## Základy Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Základ Liquid


Elements je blockchainová platforma s otevřeným zdrojovým kódem odvozená z kódové základny Bitcoin Core. Rozšiřuje funkčnost Bitcoin tím, že umožňuje na sidechainech nezávislé blockchainy, které mohou převádět aktiva do a z Bitcoin. Zatímco jádro Bitcoin Core pohání síť Bitcoin, Elements je softwarový motor stojící za Liquid Network a dalšími vlastními sidechainy.


Vztah je přímočarý: Liquid je specifická "instance" postranního řetězce Elements, nakonfigurovaná pro produkční použití s federativním modelem konsensu. Pro vývojáře, kteří znají Bitcoin, bude Elements intuitivní, protože zachovává stejné rozhraní RPC (vzdálené volání procedur) a strukturu příkazového řádku (`elements-cli`, `elements-d`, `elements-qt`). Klíčový rozdíl spočívá v konfiguraci: nastavení `chain=liquidv1` připojí [uzel](https://planb.academy/resources/glossary/node) k hlavní síti Liquid, zatímco `chain=elementsregtest` roztočí místní prostředí pro regresní testování, kde mohou vývojáři okamžitě generate bloky testovat bez externích závislostí.


#### Emise aktiv

Výraznou funkcí systému Elements je nativní vydávání aktiv. Na rozdíl od Etherea, kde tokeny představují složité chytré kontrakty, jsou aktiva v Elements občany první třídy vytvořenými pomocí jednoduchého příkazu RPC (`issueasset`).


- Jedinečné identifikátory:** Každé aktivum získá jedinečné 64znakové hexadecimální ID.
- Tokeny pro opakovanou emisi:** Emitenti mohou volitelně vytvořit tokeny pro opakovanou emisi, které dávají držiteli právo později vytěžit další aktivum (užitečné pro stablecoiny nebo bezpečnostní tokeny).
- Registr aktiv:** Protože hexadecimální ID nejsou čitelná pro člověka, registr aktiv Blockstream mapuje tato ID na názvy a tickery (např. "USDT"), podobně jako DNS pro aktiva.


### Ochrana soukromí prostřednictvím Confidential Transactions


Elements řeší jedno z hlavních omezení veřejných blockchainů: nedostatek komerčního soukromí. Na Bitcoin je každá částka transakce viditelná pro celý svět. Elements zavádí **Confidential Transactions (CT)**, který kryptograficky zaslepuje částku a typ aktiva a zároveň umožňuje síti ověřit platnost transakce.


Toho lze dosáhnout pomocí **Pedersenových závazků** a **důkazů rozsahu**.


- Pedersenovy závazky** nahrazují viditelnou částku kryptografickým závazkem. Díky homomorfnímu šifrování mohou validátory kontrolovat, zda *Vstupní závazky = Výstupní závazky + poplatky*, aniž by kdy viděly skutečné hodnoty.
- Důkazy rozsahu** zabraňují uživateli vytvořit peníze ze vzduchu (např. použitím záporných čísel) tím, že matematicky prokáží, že skrytá hodnota je kladné celé číslo v platném rozsahu.


Důvěrná transakce zobrazuje platné vstupy a výstupy, ale vnějšímu pozorovateli nezobrazuje, co a kolik se posílá. Pouze odesílatel a příjemce (kteří vlastní zaslepující klíče) mohou vidět data v jasném textu.


### Vývoj a pracovní postup RPC


Interakce s uzlem Elements probíhá především prostřednictvím jeho rozhraní JSON-RPC. To umožňuje aplikacím napsaným v jazycích Python, JavaScript nebo Go komunikovat s blockchainem.



- Nastavení:** Vývojář obvykle začíná v režimu `regtest`. Ten umožňuje okamžité generování bloků (`generateblock`) pro okamžité potvrzení transakcí, čímž se obejde 1minutová doba blokování v reálné síti.
- Příkazy:** K dispozici jsou standardní příkazy Bitcoin jako `getblockchaininfo` a specifické příkazy Elements jako `dumpblindingkey` (pro auditování CT) nebo `pegin` (pro přesun BTC do sidechainu).
- Aliasy:** Pro správu více uzlů (např. "odesilatele" a "přijímače" pro testování) vývojáři často používají aliasy shellu jako `e1-cli` a `e2-cli`, které ukazují na různé datové adresáře a simulují tak síť [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) na jednom počítači.


Tato architektura umožňuje vývojářům vytvářet sofistikované finanční aplikace - například platformy pro cenné papíry nebo soukromé platební brány - s využitím robustních a známých nástrojů ekosystému Bitcoin.


## Propojení vrstev Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastruktura Cross-Layer a HTLC


Ekosystém Bitcoin se vyvinul ve vícevrstvou architekturu, přičemž Mainchain zajišťuje vypořádání, Lightning nabízí rychlost a Liquid umožňuje pokročilé funkce aktiv. Přesun hodnoty mezi těmito vrstvami bez centralizovaných zprostředkovatelů vyžaduje kryptografické primitivum bez důvěry: Hash Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


HTLC vytváří podmíněný [platební kanál](https://planb.academy/resources/glossary/payment-channel), který atomicky propojuje nezávislé systémy. Funguje prostřednictvím dvou základních omezení: **zámku hesla** a **časového zámku**.


- Zámek Hash:** Prostředky lze utratit okamžitě, pokud příjemce odhalí tajný "předobraz", který odpovídá určitému kryptografickému [hashi](https://planb.academy/resources/glossary/hash-function).
- Časový zámek:** Pokud příjemce neodhalí tajemství ve stanoveném časovém rámci (výška bloku), může původní odesílatel získat prostředky zpět.


Tato dvoucestná struktura zajišťuje bezpečnost. Při výměně mezi vrstvami se v obou sítích používá stejný hashovací zámek. Když příjemce odhalí tajemství, aby si nárokoval prostředky na jedné vrstvě (např. Liquid), toto tajemství se stane viditelným pro odesílatele, který jej pak může použít k nároku na reciproční prostředky na druhé vrstvě (např. Lightning). Tato kryptografická vazba zaručuje, že výměna buď pro obě strany proběhne úspěšně, nebo se pro obě strany nezdaří, čímž se eliminuje riziko, že jedna strana o prostředky přijde, zatímco druhá je získá.


### Upgrade Taproot a MuSig2


Starší HTLC ([SegWit](https://planb.academy/resources/glossary/segwit) v0) fungovaly dobře, ale trpěly nedostatky v oblasti soukromí a účinnosti. Vyžadovaly publikování celé logiky [skriptu](https://planb.academy/resources/glossary/script) on-chain, díky čemuž byly swapové transakce snadno identifikovatelné pro analytiky blockchainu, a byly dražší vzhledem k jejich datové velikosti. Zavedení [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) a protokolu MuSig2 způsobilo v této architektuře revoluci.


Taproot umožňuje **agregaci klíčů** prostřednictvím MuSig2. Namísto odhalování složitého skriptu s několika [veřejnými klíči](https://planb.academy/resources/glossary/public-key) umožňuje MuSig2 účastníkům výměny spojit své klíče do jediného agregovaného veřejného klíče.


- Kooperativní "klíčová cesta":** Pokud obě strany se směnou souhlasí ("šťastná cesta"), transakci spolupodepisují. Pro síť to vypadá stejně jako standardní platba s jedním podpisem. Spotřebovává minimální blokový prostor a neprozrazuje absolutně žádné informace o podmínkách směny.
- "Cesta skriptu" protivníka:** Pokud jedna ze stran přestane reagovat nebo se stane škodlivou, teprve tehdy je odhalen základní skript (obsahující hash/časové zámky). Ten je uspořádán do [Merkleho stromu](https://planb.academy/resources/glossary/merkle-tree), což poctivé straně umožňuje odhalit pouze konkrétní větev potřebnou k získání prostředků a zbytek smluvní logiky zůstává skrytý.


### Praktické provádění: Liquid-Lightning Swaps


V praxi tyto protokoly umožňují bezproblémovou výměnu mezi vrstvami Bitcoin. Typická výměna z Liquid na Lightning začíná tím, že klient požádá poskytovatele služeb o výměnu. Klient poskytne [fakturu Lightning](https://planb.academy/resources/glossary/invoice-lightning) a poskytovatel uzamkne ekvivalentní Liquid Bitcoin (L-BTC) na adresu HTLC s podporou Taproot. V případě, že klient poskytne fakturu Lightning, poskytovatel uzamkne ekvivalentní Liquid Bitcoin (L-BTC) na adresu HTLC s podporou Taproot.


Atomicita je vynucena při zúčtování platby. Aby mohl poskytovatel služby nárokovat L-BTC, musí mít předobraz. Tento preimage získá pouze tehdy, když úspěšně uhradí klientovu bleskovou fakturu. V okamžiku, kdy je platba Lightning dokončena, je předobraz odhalen, což poskytovateli umožňuje odblokovat prostředky Liquid.


#### Wallet Abstrahování a řízení UTXO

Pro koncové uživatele je tato složitost zcela abstrahována. Moderní [peněženky](https://planb.academy/resources/glossary/wallet), jako je Aqua, zpracovávají procesy generování klíčů, vytváření faktur a podepisování na pozadí. Uživatel jednoduše "zaplatí" fakturu Lightning pomocí svého zůstatku na Liquid. V zákulisí služba řídí konsolidaci [UTXO](https://planb.academy/resources/glossary/utxo) a pravidelně zametá malé, nevyzvednuté nebo vrácené výstupy, aby zachovala efektivitu wallet a minimalizovala dopady poplatků v obdobích vysokého provozu.


## Liquid Network Přehled


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architektura a konsensus


Liquid Network funguje jako federativní postranní řetězec postavený na kódové základně **Elements**. Zatímco Elements - fork jádra Bitcoin - poskytuje softwarový základ, Liquid je implementací produkční sítě. Na rozdíl od Bitcoin Proof-of-Work, který se opírá o konkurenční [mining](https://planb.academy/resources/glossary/mining), využívá Liquid model **Federated Consensus**.


Síť udržuje patnáct globálně rozmístěných "funkcionářů" Tyto subjekty provozují specializované servery, které plní dvě klíčové úlohy:

1.  **Vytváření bloků:** Funkcionáři se střídají při vytváření bloků v deterministickém kruhovém rozvrhu a přesně každou minutu vytvářejí nový blok.

2.  **Podepisování bloků:** Aby byl blok platný, musí být podepsán alespoň 11 z 15 funkcionářů.


Tento práh 11 z 15 zajišťuje, že síť snese výpadek až čtyř uzlů, aniž by se zastavila. Hlavní výhodou tohoto kompromisu je **deterministická konečnost**. Zatímco Bitcoin se zabývá pravděpodobností, Liquid dosahuje jistoty vypořádání po dvou blocích (přibližně dvě minuty). Jakmile má blok na sobě jediné potvrzení, nelze řetězec reorganizovat, což jej činí vysoce efektivním pro arbitráže a rychlé vypořádání.


### Confidential Transactions a původní aktiva


Charakteristickým rysem Liquid je výchozí použití **Confidential Transactions (CT)**. U Bitcoin mainchain jsou odesílatel, příjemce a částka veřejné. Liquid toto vylepšuje tím, že kryptograficky zaslepuje částku a typ aktiva, zatímco adresy odesílatele a příjemce ponechává viditelné pro ověření.


Aby bylo zajištěno, že uživatel nemůže tisknout peníze (např. odesláním záporných částek), používá Liquid **Pedersenovy závazky** a **Důkazy rozsahu**. Tyto kryptografické primitivy umožňují síti ověřit, že *Vstupy = Výstupy + Poplatky* a že všechny hodnoty jsou kladná celá čísla, aniž by se konkrétní čísla kdy dostala do veřejné účetní knihy. Dešifrovaná data mohou zobrazit pouze účastníci, kteří jsou držiteli zaslepovacích klíčů.


#### Emise aktiv

Liquid považuje všechna aktiva za "původní" Ať už se jedná o Liquid Bitcoin (L-BTC), stablecoin jako USDT nebo cenný papír token, všechny mají stejnou architekturu. Vydání aktiva nevyžaduje žádné inteligentní smlouvy - pouze jednoduché volání RPC.


- Neregulovaná aktiva:** Může je vydávat kdokoli bez povolení.
- Regulovaná aktiva:** S využitím platformy Blockstream Asset Management Platform (AMP) mohou emitenti prosazovat dodržování pravidel (například KYC/AML) tím, že před přesunem aktiva vyžadují druhý podpis z autorizačního serveru.


### Oboustranný kolík a dynamická federace


Můstek mezi Bitcoin a Liquid je **oboustranný kolík**. Umožňuje uživatelům přesouvat BTC do postranního řetězce (Peg-in) a zpět do mainchain (Peg-out).


**Proces zavádění:**

To je bez povolení. Uživatel odešle BTC na adresu kontrolovanou federací. Kvůli ochraně před reorganizací blockchainu Bitcoin musí tyto prostředky počkat na **102 potvrzení** (cca 17 hodin), než je na sidechainu vyražen ekvivalentní L-BTC.


**Proces Peg-out:**

Pro návrat do Bitcoin se spálí L-BTC. Aby se však zabránilo krádeži podkladových rezerv Bitcoin, nejsou peg-outy plně automatizovány. Vyžadují autorizaci od člena, který je držitelem **autorizačního klíče pro peg-out (PAK)**. Samotné prostředky Bitcoin jsou zabezpečeny v multipodpisovém systému wallet s 11 z 15 klíčů, které jsou uloženy v hardwarových bezpečnostních modulech (HSM), jež jsou vzdušně odděleny od hlavních serverů funkcionářů.


**Dynamická federace (Dynafed):**

Aby byla zajištěna dlouhá životnost, používá Liquid protokol Dynafed, který umožňuje střídání funkcionářů nebo aktualizaci parametrů sítě bez pevného fork. Pokud je třeba vyměnit funkcionáře, síť vysílá transakci o přechodu. Po dvoutýdenním období překrývání přebírá novou konfiguraci, což umožňuje federaci plynulý vývoj při zachování nepřetržité provozuschopnosti.


## Ekosystém a kapitálové trhy


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Obchodní strategie a ekosystém


Liquid je víc než jen technický sidechain; je to vrstva infrastruktury zaměřená na obchod, která je navržena tak, aby zvládala komplexní požadavky kapitálových trhů, které Bitcoin mainchain nemůže efektivně podporovat. Zatímco [Lightning Network](https://planb.academy/resources/glossary/lightning-network) optimalizuje pro vysokofrekvenční platby s nízkou hodnotou, Liquid se zaměřuje na převody s vysokou hodnotou, vydávání aktiv a vypořádání mezi burzami.


Ekosystém řídí **Liquid Federation**, konsorcium ~73 společností včetně burz, obchodních míst a poskytovatelů infrastruktury. Tento model spolupráce odráží tradiční finanční clearingová centra, ale funguje s větší transparentností a výrazně kratší dobou vypořádání (2 minuty oproti T+2 dny).


### Tokenizace aktiv reálného světa (RWA)


Hlavním obchodním případem Liquid je "tokenizace" - reprezentace reálné hodnoty (akcie, dluhopisy, smlouvy mining) jako digitálních tokenů v blockchainu. To nabízí tři hlavní výhody:

1.  **24/7 Global Markets:** Odstranění bankovních hodin a geografických omezení.

2.  **Operační efektivita:** Eliminace chyb při odsouhlasování díky sdílené, neměnné účetní knize.

3.  **Atomické zúčtování:** Snížení rizika protistrany zajištěním, že dodávka proběhne současně s platbou.


#### Regulovaná aktiva a AMP

S většinou institucionálních aktiv nelze obchodovat bez povolení kvůli zákonným požadavkům. Technickým standardem, který tato pravidla prosazuje, je **Platforma pro správu aktiv (AMP)**.


- Whitelisting:** Emitenti mohou omezit držení a obchodování na adresy ověřené KYC.
- Kontrola Multisig:** Akce pro zajištění shody (jako je zmrazení ukradených prostředků nebo opětovné vydání ztracených tokenů) jsou řízeny prostřednictvím autorizace více podpisů, což zajišťuje, že žádný zaměstnanec nemůže jednat jednostranně.


Tato infrastruktura je dnes v provozu. Platformy jako **Stalker** poskytují v Evropě komplexní tokenizační služby, zatímco **Sideswap** funguje jako decentralizovaná burza a neúřední wallet, která umožňuje peer-to-peer obchodování s aktivy, jako jsou **Blockstream Mining Note (BMN)** a tokenizované akcie MicroStrategy (CMSTR).


### Úspěch v reálném světě: Případová studie Mayfell


Nejpřesvědčivější důkaz o užitečnosti Liquid pochází z **Mayfellu** v Mexiku. Na trhu, kde se tradiční financování opírá o papírové směnky - které jsou náchylné ke ztrátám, podvodům a pomalému zpracování - společnost Mayfell přesunula celou infrastrukturu na Liquid.



- Rozsah:** Více než 25 000 vydaných směnek v hodnotě přes 1,5 miliardy dolarů**.
- Ochrana osobních údajů:** Při použití Liquid's Confidential Transactions jsou částky půjček viditelné pouze pro věřitele a dlužníka, což zachovává obchodní soukromí a zároveň umožňuje auditorům ověřit integritu účetní knihy.
- Dopad:** Propojením nebankovních věřitelů s globálními kapitálovými trhy prostřednictvím blockchainu společnost Mayfell snížila náklady a rozšířila přístup k úvěrům pro mexické malé a střední podniky, čímž prokázala, že přínos Liquid sahá daleko za hranice spekulativního obchodování.


### Strategická pozice oproti ostatním řetězcům


Liquid konkuruje na přeplněném trhu tokenizačních platforem (Ethereum, Solana atd.), ale má výrazné strategické výhody:


- Regulační jasnost:** Liquid používá Bitcoin (L-BTC) jako své původní aktivum. Nemá předem vytěžený token ani ICO, čímž se vyhýbá rizikům "neregistrovaného cenného papíru", která trápí ostatní blockchainy L1.
- Stabilita:** Na rozdíl od modelu účtu Etherea, kde neúspěšné transakce stále spalují poplatky za plyn, je model Liquid deterministický a spolehlivý pro kritická finanční data.
- Soukromí:** Výchozí důvěrnost je požadavkem většiny finančních institucí, což je funkce, kterou Liquid nabízí nativně a kterou veřejné řetězce jen těžko implementují bez složitých doplňků.


Vývojářům tento ekosystém nabízí jasnou příležitost: vytváření nástrojů (ovládací panely, peněženky, integrace pro zajištění shody), které propojí tradiční finance s bezpečnou vrstvou pro vypořádání Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Povolená kontrola majetku na Liquid


Blockstream AMP (Asset Management Platform) slouží jako kritická vrstva infrastruktury na Liquid Network, která je určena speciálně pro emitenty regulovaných digitálních cenných papírů a stablecoinů. Zatímco Liquid poskytuje základní vrstvu bez oprávnění s nativním vydáváním aktiv, regulované subjekty často vyžadují přísný dohled a možnosti dodržování předpisů. AMP tuto mezeru překlenuje zavedením kontrolní vrstvy s oprávněním nad konkrétními aktivy, aniž by se obětovaly výhody Liquid pro ochranu soukromí Confidential Transactions.


Hlavní přínos platformy spočívá ve dvou hlavních funkcích: komplexní přehled o emitentech a autorizace transakcí. Na rozdíl od standardních aktiv Liquid, kde jsou částky a typy blinded dostupné všem kromě účastníků, aktiva AMP umožňují emitentovi udržovat kompletní auditní stopu unblinded. Tato transparentnost je nezbytná pro regulatorní výkaznictví a interní audity. AMP navíc prosazuje přísný autorizační model prostřednictvím mechanismu spolupodepisování. Každý převod aktiva AMP vyžaduje podpis ze serveru AMP. To umožňuje emitentům prosazovat komplexní pravidla off-chain - například zmrazení účtů, zařazení akreditovaných investorů na whitelist nebo zavedení limitů převodů - a tím fakticky fungovat jako centralizovaný strážce v rámci decentralizované sítě.


#### Provozní kompromisy

Tato architektura přináší specifické kompromisy. Systém je závislý na dostupnosti serveru AMP; pokud server funguje jako spoludlužník a vypadne z provozu, likvidita aktiv se pozastaví. Kromě toho je sice zachováno soukromí mezi uživateli, ale investoři musí akceptovat, že emitent má plný přehled o jejich držbě. Tento model je ideální pro bezpečnostní tokeny splňující požadavky, ale nevhodný pro [kryptoměny](https://planb.academy/resources/glossary/cryptocurrency) odolné vůči cenzuře.


### Vývoj architektury a cesty integrace


Ekosystém AMP v současné době přechází ze své první verze na flexibilnější a interoperabilnější architekturu "verze 2". Starší systém vyžadoval, aby vydavatelé udržovali plně synchronizované uzly Elements, a nutil vývojáře, aby se do značné míry spoléhali na monolitickou sadu SDK Green. To bylo sice funkční, ale vytvářelo to vysoké technické překážky vstupu a omezovalo možnosti volby wallet.


Architektura nové generace tyto požadavky zásadně zjednodušuje tím, že složitost přesouvá na server. V tomto novém modelu se server AMP stará o těžkou práci při vytváření transakcí, výběru UTXO a výpočtu poplatků. Vydavateli předkládá částečně podepsanou transakci Elements (PSET), která jednoduše vyžaduje podpis. Tento přístup "chytrý server, hloupý wallet" eliminuje potřebu emitentů provozovat plné uzly a umožňuje používat hardwarové peněženky a standardní nastavení více podpisů pro správu pokladny.


Pro vývojáře tento vývoj znamená odklon od proprietárních sad SDK ke standardním deskriptorům a pracovním postupům PSET. Peněženky nyní mohou registrovat deskriptory s více podpisy na serveru AMP a stanovit tak autorizační práva. Tím se vývoj AMP sjednocuje s širšími standardy Bitcoin wallet, což zpřístupňuje integraci jakékoli aplikaci schopné pracovat s formáty PSBT/PSET. Vývojářům, kteří dnes vytvářejí aplikace, doporučujeme, aby využívali nástroje jako Liquid Wallet Kit (LWK), které podporují tyto moderní architektury založené na deskriptorech, a zajistili tak, že jejich aplikace budou připraveny na nové standardy AMP.


### Ekosystém Liquid Wallet a utajení


Vytváření aplikací na platformě Liquid vyžaduje složitější stack než standardní vývoj na platformě Bitcoin díky funkcím, jako jsou nativní aktiva a Confidential Transactions. Ekosystém je podporován vrstvenou architekturou: nízkoúrovňové knihovny jako `secp256k1-zkp` zpracovávají kryptografická primitiva, zatímco logiku wallet spravují sady nástrojů vyšší úrovně.


Vývojová sada Green (GDK) v minulosti poskytovala komplexní, ale rigidní řešení. Moderní alternativou je Liquid Wallet Kit (LWK), který nabízí modulární přístup. LWK rozděluje problémy do samostatných beden - nezávisle zpracovává deskriptory, podepisování a komunikaci s hardwarem - a poskytuje tak vývojářům flexibilitu při vytváření vlastních řešení bez režie monolitické knihovny.


#### Manipulace s Confidential Transactions

Nejvýraznější výzvou v tomto ekosystému je řízení životního cyklu zaslepení. V systému Liquid jsou výstupy transakcí šifrovány pomocí výměny klíčů ECDH (Elliptic Curve Diffie-Hellman). Odesílatel používá k zašifrování částek a typů aktiv veřejný klíč příjemce, čímž vytváří důkaz o rozsahu, který ověřuje platnost transakce, aniž by došlo k odhalení hodnot.


Aby byl přístroj wallet funkční, musí tento proces úspěšně zvrátit. Když wallet zjistí příchozí transakci, pokusí se pomocí svého soukromého zaslepovacího klíče výstup odblokovat. Pokud se sdílený tajný klíč shoduje, může wallet dešifrovat hodnotu a přidat ji k zůstatku uživatele. Tento proces je výpočetně náročný a vyžaduje přesnou správu zaslepovacích faktorů, aby se zajistilo, že transakce budou matematicky vyvážené, což je složitost, kterou se nástroje jako LWK snaží pro vývojáře abstrahovat.


# Technická stránka


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - bez uzlu


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Úvod do Breez Liquid SDK


Breez Liquid SDK je samostatně použitelná sada nástrojů s otevřeným zdrojovým kódem, která má překlenout propast mezi Liquid Network a širším ekosystémem Bitcoin. Jeho hlavním posláním je abstrahovat složitosti správy uzlů Lightning Network a atomických výměn a umožnit vývojářům vytvářet finanční aplikace bez tření.


Jádro logiky je kvůli výkonu a bezpečnosti napsáno v jazyce Rust, ale využívá UniFFI (Unified Foreign Function Interface), který poskytuje nativní vazby pro jazyky Kotlin, Swift, Python, C#, Dart a Flutter. To zajišťuje, že vývojáři mohou integrovat funkce Bitcoin do svého preferovaného prostředí, aniž by museli spravovat nízkoúrovňové kryptografické operace.


**Podporované typy transakcí:**

SDK pracuje s Liquid jako se svou "domovskou základnou" Vyniká ve třech specifických operacích:

1.  **Přenosy z Liquid na Liquid:** Přímé přenosy on-chain.

2.  **Liquid-to-Lightning:** Úhrada faktur Lightning z prostředků Liquid.

3.  **Liquid-to-Bitcoin:** Výměna prostředků přímo do Bitcoin mainchain.


*Poznámka: SDK nepodporuje přímé transakce Lightning-to-Lightning nebo Bitcoin-to-Bitcoin. Jedná se o nástroj zaměřený výhradně na Liquid.*


### Platební architektury: Podmořské swapy


Pro dosažení interoperability mezi Liquid, Lightning a Bitcoin bez centralizovaných správců se Breez spoléhá na **podmořské výměny**. Jedná se o atomické operace, při nichž se transakce buď úspěšně dokončí v obou sítích, nebo v obou sítích selže, což zajišťuje, že se finanční prostředky nikdy neztratí při přepravě.


#### Odeslání blesku (Výměna ponorek)

Když uživatel zaplatí fakturu Lightning, SDK odvysílá na Liquid Network transakci "uzamčení". Tím se finanční prostředky efektivně uloží do úschovy. Poskytovatel swapu (Boltz) to zjistí, zaplatí fakturu Lightning a poté použije předobraz platby (kryptografickou stvrzenku), aby si vyžádal uzamčené prostředky Liquid.


#### Příjem blesku (Reverzní výměna ponorek)

Přijímání blesků je opačný proces. Uživatel vygeneruje fakturu a poskytovatel swapu zablokuje prostředky na Lightning Network. SDK tento proces monitoruje prostřednictvím WebSockets. Jakmile je uzamčení potvrzeno, SDK automaticky provede transakci reklamace, aby přesunul ekvivalentní prostředky na uživatelův Liquid wallet.


#### Cross-Chain Bitcoin

Pro přenosy z Liquid do Bitcoin používá architektura mechanismus "dual-swap". Transakce uzamčení probíhají na obou řetězcích současně. Odesílatel požaduje prostředky na Bitcoin, zatímco příjemce požaduje prostředky na Liquid. To umožňuje bezdůvěryhodné přemostění bez závislosti na federated peg-outs nebo centralizovaných výměnách.


### Vývojář Interface a automatizovaná správa


SDK Breez zjednodušuje práci vývojářů tím, že složité finanční toky shrnuje do standardizovaného procesu o třech krocích: **Připojit, připravit a provést**.


1.  **Připojení:** Inicializuje wallet, synchronizuje se s blockchainem pomocí Liquid Wallet Kit (LWK) a navazuje spojení WebSocket pro monitorování v reálném čase.

2.  **Připravit:** Před přidělením prostředků tento krok vypočítá a vrátí všechny související síťové poplatky a náklady na výměnu, což umožní uživatelskému rozhraní zobrazit uživateli jasnou celkovou částku.

3.  **Uskutečnění:** Tento krok vytvoří transakci, odvysílá ji a zahájí výměnu.


#### Automatizované bezpečnostní mechanismy

Jednou z nejdůležitějších funkcí sady SDK je **Automatická správa vrácení peněz**. V případě výpadku sítě nebo nespolupracující protistrany by teoreticky mohlo dojít k uvíznutí finančních prostředků v časově zablokované smlouvě. Sada SDK zcela abstrahuje logiku obnovy. Sleduje stav každé výměny; pokud výměna selže nebo vyprší její časový limit, SDK automaticky zkonstruuje a odvysílá transakci vrácení prostředků na účet wallet uživatele.


Kromě toho SDK zpracovává **Rozlišení metadat**. Sloučí výměnná data off-chain (poskytnutá výměnným programem Boltz) s historií transakcí on-chain. Tím je zajištěno, že historie transakcí uživatele je čitelná pro člověka a zobrazuje podrobnosti faktury a kontext platby, nikoli pouze surové hexadecimální hashe transakcí.


# Závěrečná část


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Recenze a hodnocení


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Závěrečná zkouška


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Závěr


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>