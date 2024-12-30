---
name: Teoretický úvod do Lightning Network
goal: Objevte Lightning Network z technické perspektivy
objectives:
  - Porozumět fungování kanálů sítě.
  - Seznámit se s termíny HTLC, LNURL a UTXO.
  - Pochopit správu likvidity a poplatky LNN.
  - Rozpoznat Lightning Network jako síť.
  - Porozumět teoretickým využitím Lightning Network.
---

# Cesta k druhé vrstvě Bitcoinu

Ponořte se do jádra Lightning Network, zásadního systému pro budoucnost transakcí s Bitcoinem. LNP201 je teoretický kurz o technickém fungování Lightning. Odhaluje základy a mechanismy této druhé vrstvy sítě, navržené k tomu, aby platby Bitcoinem byly rychlé, ekonomické a škálovatelné.

Díky své síti platebních kanálů umožňuje Lightning rychlé a bezpečné transakce bez nutnosti zaznamenávat každou výměnu na blockchainu Bitcoinu. V průběhu kapitol se naučíte, jak funguje otevírání, správa a zavírání kanálů, jak jsou platby směrovány přes prostředníkové uzly bezpečně a s minimální potřebou důvěry a jak spravovat likviditu. Objevíte, co jsou závazné transakce, HTLCs, revokační klíče, mechanismy trestání, cibulové směrování a faktury.

Ať už jste začátečník v Bitcoinu nebo zkušenější uživatel, tento kurz poskytne cenné informace k pochopení a používání Lightning Network. Ačkoli se v prvních částech budeme věnovat některým základům fungování Bitcoinu, je nezbytné ovládnout základy Satoshiho vynálezu, než se ponoříme do LNP201.

Užijte si objevování!

+++

# Základy

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Porozumění Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Porozumění Lightning Network](https://youtu.be/PszWk046x-I)

Vítejte v kurzu LNP201, jehož cílem je vysvětlit technické fungování Lightning Network.

Lightning Network je síť platebních kanálů postavená na protokolu Bitcoinu, která má umožnit rychlé a nízkonákladové transakce. Umožňuje vytváření platebních kanálů mezi účastníky, v rámci kterých mohou být transakce prováděny téměř okamžitě a s minimálními poplatky, aniž by bylo nutné zaznamenávat každou transakci jednotlivě na blockchainu. Tímto způsobem se Lightning Network snaží zlepšit škálovatelnost Bitcoinu a učinit jej použitelným pro platby nízké hodnoty.

Před prozkoumáním aspektu "sítě" je důležité pochopit koncept **platebního kanálu** na Lightning, jak funguje a jeho specifika. To je předmětem této první kapitoly.

### Koncept platebního kanálu

Platební kanál umožňuje dvěma stranám, zde **Alice** a **Bob**, vyměňovat si prostředky přes Lightning Network. Každý protagonista má uzel, symbolizovaný kruhem, a kanál mezi nimi je reprezentován úsečkou.

![LNP201](assets/en/01.webp)

V našem příkladu má Alice na své straně kanálu 100 000 satoshi a Bob 30 000, což dává dohromady 130 000 satoshi, což představuje **kapacitu kanálu**.

**Ale co je satoshi?**

**Satoshi** (nebo "sat") je jednotka účtu na Bitcoinu. Podobně jako cent pro euro, satoshi je prostě zlomek Bitcoinu. Jedno satoshi je rovno **0.00000001 Bitcoinu**, nebo jedné sté milionté Bitcoinu. Používání satoshi se stává stále praktičtější, jak hodnota Bitcoinu roste.

### Rozdělení prostředků v kanálu

Vraťme se k platebnímu kanálu. Klíčovým pojmem zde je "**strana kanálu**". Každý účastník má na své straně kanálu určité prostředky: Alice 100 000 satoshi a Bob 30 000. Jak jsme viděli, součet těchto prostředků představuje celkovou kapacitu kanálu, číslo, které je nastaveno při jeho otevření.

![LNP201](assets/en/02.webp)

Vezměme si příklad transakce v Lightning Network. Pokud Alice chce poslat 40 000 satoshi Bobovi, je to možné, protože má dostatek prostředků (100 000 satoshi). Po této transakci bude mít Alice na své straně 60 000 satoshi a Bob 70 000.

![LNP201](assets/en/03.webp)

**Kapacita kanálu**, která činí 130 000 satoshi, zůstává konstantní. To, co se mění, je rozdělení prostředků. Tento systém neumožňuje posílat více prostředků, než kolik máte. Například, pokud by Bob chtěl poslat zpět 80 000 satoshi Alici, nemohl by, protože má pouze 70 000.

Další způsob, jak si představit rozdělení prostředků, je představit si **posuvník**, který ukazuje, kde se prostředky v kanálu nacházejí. Původně, s 100 000 satoshi pro Alici a 30 000 pro Boba, je posuvník logicky na straně Alice. Po transakci 40 000 satoshi se posuvník mírně posune na stranu Boba, který nyní má 70 000 satoshi.

![LNP201](assets/en/04.webp)

Toto znázornění může být užitečné pro představu o rovnováze prostředků v kanálu.

### Základní pravidla platebního kanálu

První bod, který si je třeba zapamatovat, je, že **kapacita kanálu** je pevná. Je to trochu jako průměr potrubí: určuje maximální množství prostředků, které lze v jednom okamžiku přes kanál poslat.
Vezměme si příklad: pokud má Alice na své straně 130 000 satoshi, může maximálně poslat 130 000 satoshi Bobovi v jedné transakci. Bob však může tyto prostředky poslat zpět Alici, částečně nebo celé.

Důležité je pochopit, že pevná kapacita kanálu omezuje maximální množství jedné transakce, ale ne celkový počet možných transakcí, ani celkový objem vyměněných prostředků v rámci kanálu.

**Co si odnést z této kapitoly?**

- Kapacita kanálu je pevná a určuje maximální množství, které lze v jedné transakci poslat.
- Prostředky v kanálu jsou rozděleny mezi dva účastníky, a každý může poslat druhému pouze prostředky, které vlastní na své straně.
- Lightning Network tak umožňuje rychlou a efektivní výměnu prostředků, přičemž respektuje omezení daná kapacitou kanálů.

Toto je konec této první kapitoly, kde jsme položili základy pro Lightning Network. V nadcházejících kapitolách se podíváme, jak otevřít kanál a prozkoumáme hlouběji koncepty zde diskutované.

## Bitcoin, Adresy, UTXO a Transakce

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, adresy, utxo a transakce](https://youtu.be/cadCJ2V7zTg)
Tato kapitola je trochu speciální, protože nebude přímo věnována Lightning Network, ale Bitcoinu. Skutečně, Lightning Network je vrstva postavená na Bitcoinu. Je tedy zásadní pochopit určité základní koncepty Bitcoinu, aby bylo možné správně chápat fungování Lightning Network v následujících kapitolách. V této kapitole si projdeme základy Bitcoinových přijímacích adres, UTXO, stejně jako fungování Bitcoinových transakcí.

### Bitcoinové Adresy, Soukromé a Veřejné Klíče

Bitcoinová adresa je řada znaků odvozených z **veřejného klíče**, který je sám vypočítán z **soukromého klíče**. Jak jistě víte, používá se k uzamčení bitcoinů, což je ekvivalentní jejich přijetí do naší peněženky.

Soukromý klíč je tajný prvek, který by **nikdy neměl být sdílen**, zatímco veřejný klíč a adresa mohou být sdíleny bez rizika pro bezpečnost (jejich zveřejnění představuje pouze riziko pro vaše soukromí). Zde je běžná reprezentace, kterou budeme v průběhu tohoto školení používat:

- **Soukromé klíče** budou reprezentovány **vertikálně**.
- **Veřejné klíče** budou reprezentovány **horizontálně**.
- Jejich barva označuje, kdo je vlastní (Alice v oranžové a Bob v černé...).

### Bitcoinové Transakce: Odesílání Fondů a Skripty

Na Bitcoinu transakce zahrnuje odeslání fondů z jedné adresy na druhou. Vezměme si příklad Alice, která posílá 0.002 Bitcoinu Bobovi. Alice použije soukromý klíč spojený s její adresou k **podepsání** transakce, čímž prokáže, že je skutečně schopna tyto fondy utratit. Ale co přesně se děje za touto transakcí? Fondy na Bitcoinové adrese jsou uzamčeny **skriptem**, jakýmsi mini-programem, který klade určité podmínky pro utrácení fondů.

Nejběžnější skript vyžaduje podpis soukromým klíčem spojeným s adresou. Když Alice podepíše transakci svým soukromým klíčem, **odemkne skript**, který blokuje fondy, a ty pak mohou být převedeny. Převod fondů zahrnuje přidání nového skriptu k těmto fondům, který stanoví, že pro jejich utrácení tentokrát bude vyžadován podpis **Bobova** soukromého klíče.

![LNP201](assets/en/05.webp)

### UTXO: Nevyužité Transakční Výstupy

Na Bitcoinu ve skutečnosti neobchodujeme přímo bitcoiny, ale **UTXO** (_Unspent Transaction Outputs_), což znamená "nevyužité transakční výstupy".

UTXO je kus bitcoinu, který může mít jakoukoliv hodnotu, například **2,000 bitcoinů**, **8 bitcoinů**, nebo dokonce **8,000 satoshi**. Každé UTXO je uzamčeno skriptem a pro jeho utrácení je nutné splnit podmínky skriptu, často podpisem soukromým klíčem odpovídajícím dané přijímací adrese.

UTXO nelze dělit. Při každém použití k utracení množství bitcoinů, které reprezentují, musí být utraceno v celku. Je to trochu jako s bankovkou: pokud máte bankovku v hodnotě 10 € a dlužíte pekaři 5 €, nemůžete bankovku prostě rozpůlit. Musíte mu dát bankovku 10 €, a on vám dá 5 € zpět. Tento princip platí přesně stejně pro UTXO na Bitcoinu! Například, když Alice odemkne skript svým soukromým klíčem, odemkne celé UTXO. Pokud si přeje poslat Bobovi pouze část fondů reprezentovaných tímto UTXO, může jej "rozfragmentovat" na několik menších. Poté pošle 0.0015 BTC Bobovi a zbytek, 0.0005 BTC, na **změnovou adresu**.

Zde je příklad transakce se 2 výstupy:

- UTXO 0.0015 BTC pro Boba, uzamčené skriptem vyžadujícím Bobův soukromý klíč pro podpis.
- UTXO 0.0005 BTC pro Alici, uzamčené skriptem vyžadujícím její vlastní podpis.

![LNP201](assets/en/06.webp)

### Multi-podpisové adresy

Kromě jednoduchých adres generovaných z jednoho veřejného klíče je možné vytvořit **multi-podpisové adresy** z více veřejných klíčů. Zvláště zajímavý případ pro Lightning Network je **2/2 multi-podpisová adresa**, generovaná ze dvou veřejných klíčů:

![LNP201](assets/en/07.webp)

Pro utrácení prostředků uzamčených touto 2/2 multi-podpisovou adresou je nutné podepsat oběma soukromými klíči spojenými s veřejnými klíči.

![LNP201](assets/en/08.webp)

Tento typ adresy je přesně reprezentací platebních kanálů na Lightning Network na Bitcoin blockchainu.

**Co si odnést z této kapitoly?**

- **Bitcoinová adresa** je odvozena z veřejného klíče, který je sám odvozen ze soukromého klíče.
- Prostředky na Bitcoinu jsou uzamčeny **skripty**, a pro utrácení těchto prostředků je nutné splnit podmínky skriptu, což obvykle zahrnuje poskytnutí podpisu s odpovídajícím soukromým klíčem.
- **UTXOs** jsou kusy bitcoinů uzamčené skripty, a každá transakce na Bitcoinu spočívá v odemčení UTXO a poté vytvoření jednoho nebo více nových na oplátku.
- **2/2 multi-podpisové adresy** vyžadují podpis dvou soukromých klíčů pro utrácení prostředků. Tyto specifické adresy se používají v kontextu Lightningu pro vytváření platebních kanálů.

Tato kapitola o Bitcoinu nám umožnila probrat některé základní pojmy pro následující obsah. V další kapitole se konkrétně podíváme na to, jak funguje otevírání kanálů na Lightning Network.

# Otevírání a zavírání kanálů

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Otevírání kanálu

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![open a channel](https://youtu.be/B2caBC0Rxko)

V této kapitole se podrobněji podíváme na to, jak otevřít platební kanál na Lightning Network a pochopíme spojení této operace s podkladovým systémem Bitcoinu.

### Platební kanály na Lightningu

Jak jsme viděli v první kapitole, **platební kanál** na Lightningu lze přirovnat k "potrubí" pro výměnu prostředků mezi dvěma účastníky (**Alicí** a **Bobem** v našich příkladech). Kapacita tohoto kanálu odpovídá součtu dostupných prostředků na každé straně. V našem příkladu má Alice **100 000 satoshi** a Bob **30 000 satoshi**, což dává **celkovou kapacitu** **130 000 satoshi**.

![LNP201](assets/en/09.webp)

### Úrovně výměny informací

Je zásadní jasně rozlišovat různé úrovně výměny na Lightning Network:

- **Peer-to-peer komunikace (protokol Lightning)**: Jsou to zprávy, které si Lightning uzly posílají navzájem pro komunikaci. Tyto zprávy budeme na našich diagramech znázorňovat čárkovanými černými čarami.
- **Platební kanály (protokol Lightning)**: Jsou to cesty pro výměnu prostředků na Lightningu, které budeme znázorňovat plnými černými čarami.
- **Bitcoinové transakce (protokol Bitcoin)**: Jsou to transakce provedené onchain, které budeme znázorňovat oranžovými čarami.

![LNP201](assets/en/10.webp)
Je důležité poznamenat, že Lightning node může komunikovat prostřednictvím P2P protokolu bez otevření kanálu, ale pro výměnu finančních prostředků je kanál nezbytný.

### Kroky k otevření Lightning kanálu

1. **Výměna zpráv**: Alice chce otevřít kanál s Bobem. Pošle mu zprávu obsahující částku, kterou chce v kanálu vložit (130 000 satoshi) a svůj veřejný klíč. Bob odpoví sdílením svého vlastního veřejného klíče.

![LNP201](assets/en/11.webp)

2. **Vytvoření multisignature adresy**: S těmito dvěma veřejnými klíči Alice vytvoří **2/2 multisignature adresu**, což znamená, že prostředky, které budou později na této adrese vloženy, budou vyžadovat oba podpisy (Alice a Bob) k jejich utracení.

![LNP201](assets/en/12.webp)

3. **Transakce vkladu**: Alice připraví Bitcoinovou transakci pro vklad prostředků na tuto multisignature adresu. Například se může rozhodnout poslat **130 000 satoshi** na tuto multisignature adresu. Tato transakce je **sestavena, ale ještě nebyla publikována** na blockchainu.

![LNP201](assets/en/13.webp)

4. **Transakce výběru**: Před publikováním transakce vkladu Alice sestaví transakci výběru, aby mohla získat zpět své prostředky v případě problému s Bobem. Jakmile Alice publikuje transakci vkladu, její satoshi budou zamčeny na 2/2 multisignature adrese, která vyžaduje oba podpisy (její a Bobův) k jejich odemčení. Alice se chrání před rizikem ztráty tím, že sestaví transakci výběru, která jí umožní získat zpět své prostředky.

![LNP201](assets/en/14.webp)

5. **Bobův podpis**: Alice pošle transakci vkladu Bobovi jako důkaz a požádá ho, aby podepsal transakci výběru. Jakmile je získán Bobův podpis na transakci výběru, Alice má jistotu, že si může kdykoli získat zpět své prostředky, protože nyní je potřeba pouze její vlastní podpis k odemčení multisignature.

![LNP201](assets/en/15.webp)

6. **Publikace transakce vkladu**: Jakmile je získán Bobův podpis, Alice může publikovat transakci vkladu na Bitcoinovém blockchainu, čímž oficiálně otevře Lightning kanál mezi oběma uživateli.

![LNP201](assets/en/16.webp)

### Kdy je kanál otevřen?

Kanál je považován za otevřený, jakmile je transakce vkladu zahrnuta do Bitcoinového bloku a dosáhne určité hloubky potvrzení (počet následujících bloků).

**Co si z této kapitoly máte zapamatovat?**

- Otevření kanálu začíná výměnou **zpráv** mezi oběma stranami (výměna částek a veřejných klíčů).
- Kanál je vytvořen vytvořením **2/2 multisignature adresy** a vkladem prostředků na ni prostřednictvím Bitcoinové transakce.
- Osoba otevírající kanál se ujistí, že si může **získat zpět své prostředky** prostřednictvím transakce výběru podepsané druhou stranou před publikováním transakce vkladu.

V další kapitole prozkoumáme technické fungování transakce uvnitř kanálu na Lightning Network, tj. když jsou prostředky přesunuty z jedné strany kanálu na druhou.

### Připomenutí životního cyklu kanálu

Jak bylo viděno dříve, Lightning kanál začíná **otevřením** prostřednictvím Bitcoinové transakce. Kanál může být kdykoliv **uzavřen**, také prostřednictvím Bitcoinové transakce. Mezi těmito dvěma okamžiky může být v rámci kanálu proveden téměř nekonečný počet transakcí, aniž by procházely Bitcoinovým blockchainem. Podívejme se, co se děje během transakce v kanálu.
![LNP201](assets/en/17.webp)

### Počáteční stav kanálu

V okamžiku otevření kanálu Alice vložila **130 000 satoshi** na multisignaturní adresu kanálu. Takže v počátečním stavu jsou všechny prostředky na straně Alice. Před otevřením kanálu Alice také nechala Boba podepsat **transakci pro výběr**, která by jí umožnila získat zpět své prostředky, pokud by si přála kanál uzavřít.

![LNP201](assets/en/18.webp)

### Nepublikované transakce: Commitment transakce

Když Alice provede v kanálu transakci k odeslání prostředků Bobovi, vytvoří se nová Bitcoinová transakce, která odráží tuto změnu v rozdělení prostředků. Tato transakce, nazývaná **commitment transakce**, není publikována na blockchainu, ale reprezentuje nový stav kanálu po Lightning transakci.

Vezměme si příklad, kdy Alice posílá 30 000 satoshi Bobovi:

- **Původně**: Alice má 130 000 satoshi.
- **Po transakci**: Alice má 100 000 satoshi a Bob 30 000 satoshi.
  Pro validaci tohoto převodu Alice a Bob vytvoří novou **nepublikovanou Bitcoinovou transakci**, která by poslala **100 000 satoshi Alice** a **30 000 satoshi Bobovi** z multisignaturní adresy. Obě strany konstruují tuto transakci nezávisle, ale s týmiž daty (částky a adresy). Jakmile je transakce sestavena, každý ji podepíše a vymění si podpis s druhou stranou. To umožňuje kterékoli straně kdykoliv publikovat transakci, pokud je to nutné, aby získala svůj podíl na kanálu na hlavním Bitcoinovém blockchainu.
  ![LNP201](assets/en/19.webp)

### Proces převodu: Faktura

Když Bob chce přijmout prostředky, pošle Alice **_fakturu_** na 30 000 satoshi. Alice poté zaplatí tuto fakturu zahájením převodu v rámci kanálu. Jak jsme viděli, tento proces závisí na vytvoření a podepsání nové **commitment transakce**.

Každá commitment transakce reprezentuje nové rozdělení prostředků v kanálu po převodu. V tomto příkladu, po transakci, má Bob 30 000 satoshi a Alice 100 000 satoshi. Pokud by se kterýkoliv z účastníků rozhodl publikovat tuto commitment transakci na blockchainu, mělo by to za následek uzavření kanálu a prostředky by byly rozděleny podle tohoto posledního rozdělení.

![LNP201](assets/en/20.webp)

### Nový stav po druhé transakci

Vezměme si další příklad: po první transakci, kdy Alice poslala Bobovi 30 000 satoshi, se Bob rozhodne poslat **10 000 satoshi zpět Alice**. To vytváří nový stav kanálu. Nová **commitment transakce** bude reprezentovat toto aktualizované rozdělení:

- **Alice** nyní má **110 000 satoshi**.
- **Bob** má **20 000 satoshi**.

![LNP201](assets/en/21.webp)

Opět, tato transakce není publikována na blockchainu, ale může být kdykoliv v případě uzavření kanálu.

Shrnutí, když jsou prostředky převáděny v rámci Lightning kanálu:

- Alice a Bob vytvoří novou **transakci závazku**, která odráží nové rozdělení prostředků. - Tato Bitcoinová transakce je **podepsána** oběma stranami, ale **není publikována** na Bitcoinovém blockchainu, dokud kanál zůstává otevřený.
- Transakce závazku zajišťují, že každý účastník může kdykoliv získat zpět své prostředky na Bitcoinovém blockchainu publikováním poslední podepsané transakce.

Avšak tento systém má potenciální nedostatek, který řešíme v následující kapitole. Uvidíme, jak se každý účastník může chránit proti pokusu o podvod ze strany druhé strany.

## Revokační klíč

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transakce část 2](https://youtu.be/RRvoVTLRJ84)
V této kapitole se podrobněji podíváme na to, jak transakce fungují na Lightning Network tím, že probereme mechanismy zajišťující ochranu proti podvodům, čímž zajistíme, že každá strana dodržuje pravidla v rámci kanálu.

### Připomenutí: Transakce závazku

Jak jsme již viděli, transakce na Lightningu spoléhají na nepublikované **transakce závazku**. Tyto transakce odrážejí aktuální rozdělení prostředků v kanálu. Když je provedena nová Lightning transakce, vytvoří se nová transakce závazku, která je oběma stranami podepsána, aby odrážela nový stav kanálu.

Pojďme si vzít jednoduchý příklad:

- **Počáteční stav**: Alice má **100 000 satoshi**, Bob **30 000 satoshi**.
- Po transakci, kde Alice pošle **40 000 satoshi** Bobovi, nová transakce závazku rozdělí prostředky takto:
  - Alice: **60 000 satoshi**
  - Bob: **70 000 satoshi**

![LNP201](assets/en/22.webp)

Kdykoliv mohou obě strany publikovat **poslední transakci závazku** podepsanou k uzavření kanálu a získání svých prostředků.

### Nedostatek: Podvod publikováním staré transakce

Potenciální problém nastává, pokud se jedna ze stran rozhodne **podvádět** publikováním staré transakce závazku. Například Alice by mohla publikovat starší transakci závazku, kde měla **100 000 satoshi**, i když nyní ve skutečnosti má pouze **60 000 satoshi**. To by jí umožnilo ukrást **40 000 satoshi** od Boba.

![LNP201](assets/en/23.webp)

Ještě hůře, Alice by mohla publikovat úplně první výběrovou transakci, tu před otevřením kanálu, kde měla **130 000 satoshi**, a tím ukrást celé prostředky kanálu.

![LNP201](assets/en/24.webp)

### Řešení: Revokační klíč a časový zámek

Aby se zabránilo tomuto druhu podvodu ze strany Alice, na Lightning Network jsou do transakcí závazku přidány **bezpečnostní mechanismy**:

1. **Časový zámek**: Každá transakce závazku zahrnuje časový zámek pro prostředky Alice. Časový zámek je primitivum chytré smlouvy, které nastavuje časovou podmínku, která musí být splněna, aby byla transakce přidána do bloku. To znamená, že Alice nemůže získat zpět své prostředky, dokud neprojde určitý počet bloků, pokud publikuje jednu z transakcí závazku. Tento časový zámek začíná platit od potvrzení transakce závazku. Jeho délka je obecně proporcionální velikosti kanálu, ale může být také manuálně konfigurována.
2. **Revokační klíč**: Prostředky Alice mohou být také okamžitě utraceny Bobem, pokud má **revokační klíč**. Tento klíč se skládá z tajemství drženého Alicí a tajemství drženého Bobem. Poznamenejme, že toto tajemství je pro každou transakci závazku jiné.
   Díky kombinaci těchto dvou mechanismů má Bob čas odhalit pokus Alice o podvod a potrestat ji tím, že pomocí revokačního klíče získá zpět svůj výstup, což pro Boba znamená získání všech prostředků kanálu. Náš nový závazný transakční záznam bude nyní vypadat takto:
   ![LNP201](assets/en/25.webp)

Podívejme se podrobněji na fungování tohoto mechanismu.

### Proces aktualizace transakce

Když Alice a Bob aktualizují stav kanálu novou Lightning transakcí, vymění si předem své příslušné **tajemství** pro předchozí závazný transakční záznam (ten, který se stane zastaralým a mohl by umožnit jednomu z nich podvádět). To znamená, že v novém stavu kanálu:

- Alice a Bob mají nový závazný transakční záznam reprezentující aktuální rozdělení prostředků po Lightning transakci.
- Každý z nich má tajemství toho druhého pro předchozí transakci, což jim umožňuje použít revokační klíč, pouze pokud se jeden z nich pokusí podvádět zveřejněním transakce se starým stavem v mempoolech Bitcoin uzlů. Skutečně, aby bylo možné potrestat druhou stranu, je nutné držet obě tajemství a závazný transakční záznam toho druhého, který zahrnuje podepsaný vstup. Bez této transakce je revokační klíč sám o sobě k ničemu. Jediný způsob, jak získat tuto transakci, je její získání z mempoolů (v transakcích čekajících na potvrzení) nebo v potvrzených transakcích na blockchainu během časového zámku, což dokazuje, že druhá strana se pokouší podvádět, ať už úmyslně nebo ne.

Pojďme si vzít příklad, abychom tento proces dobře pochopili:

1. **Počáteční stav**: Alice má **100 000 satoshi**, Bob **30 000 satoshi**.

![LNP201](assets/en/26.webp)

2. Bob chce od Alice přes jejich Lightning kanál přijmout 40 000 satoshi. K tomu:
   - Pošle jí fakturu spolu se svým tajemstvím pro revokační klíč jeho předchozího závazného transakčního záznamu.
   - Jako odpověď Alice poskytne svůj podpis pro Bobův nový závazný transakční záznam, stejně jako své tajemství pro revokační klíč jejího předchozího transakčního záznamu.
   - Nakonec Bob pošle svůj podpis pro Alice nový závazný transakční záznam.
   - Tyto výměny umožní Alice poslat **40 000 satoshi** Bobovi přes Lightning prostřednictvím jejich kanálu, a nové závazné transakční záznamy nyní odrážejí toto nové rozdělení prostředků.

![LNP201](assets/en/27.webp)

3. Pokud se Alice pokusí zveřejnit starý závazný transakční záznam, kde stále vlastnila **100 000 satoshi**, Bob, který získal revokační klíč, může okamžitě získat zpět prostředky pomocí tohoto klíče, zatímco Alice je zablokována časovým zámkem.

![LNP201](assets/en/28.webp)

I když v tomto případě Bob nemá ekonomický zájem na pokusu o podvod, pokud by to přesto udělal, Alice také těží ze symetrické ochrany, která jí nabízí stejné záruky.

**Co si odnést z této kapitoly?**

**Závazné transakční záznamy** na Lightning Network zahrnují bezpečnostní mechanismy, které snižují jak riziko podvodu, tak motivaci k němu. Před podepsáním nového závazného transakčního záznamu si Alice a Bob vymění svá příslušná **tajemství** pro předchozí závazné transakční záznamy. Pokud se Alice pokusí zveřejnit starý závazný transakční záznam, Bob může použít **revokační klíč** k získání všech prostředků dříve, než to stihne Alice (protože je zablokována časovým zámkem), což ji trestá za pokus o podvod.

Tento bezpečnostní systém zajišťuje, že účastníci dodržují pravidla Lightning Network, a nemohou profitovat zveřejněním starých závazných transakčních záznamů.
V tomto bodě školení již víte, jak jsou otevírány kanály Lightning a jak fungují transakce v rámci těchto kanálů. V další kapitole objevíme různé způsoby, jak kanál uzavřít a získat zpět vaše bitcoiny na hlavním blockchainu.

## Uzavření kanálu

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![uzavřít kanál](https://youtu.be/FVmQvNpVW8Y)

V této kapitole budeme diskutovat o **uzavření kanálu** na Lightning Network, které se provádí prostřednictvím Bitcoinové transakce, stejně jako otevření kanálu. Po pochopení, jak fungují transakce v rámci kanálu, je nyní čas zjistit, jak kanál uzavřít a získat zpět prostředky na Bitcoin blockchainu.

### Připomenutí životního cyklu kanálu

**Životní cyklus kanálu** začíná jeho **otevřením**, prostřednictvím Bitcoinové transakce, poté se v něm provádějí Lightning transakce a nakonec, když strany chtějí získat zpět své prostředky, je kanál **uzavřen** prostřednictvím druhé Bitcoinové transakce. Mezilehlé transakce provedené na Lightningu jsou reprezentovány nepublikovanými **commitment transakcemi**.

![LNP201](assets/en/29.webp)

### Tři typy uzavření kanálu

Existují tři hlavní způsoby, jak tento kanál uzavřít, které lze nazvat **dobrý, hrubý a záškodník** (inspirováno Andreasem Antonopoulosem v _Mastering the Lightning Network_):

1. **Dobrý**: **kooperativní uzavření**, kde se Alice a Bob dohodnou na uzavření kanálu.
2. **Hrubý**: **vynucené uzavření**, kde jedna ze stran se rozhodne kanál uzavřít čestně, ale bez souhlasu druhé strany.
3. **Záškodník**: **uzavření s podvodem**, kde jedna ze stran se pokusí ukrást prostředky publikováním staré commitment transakce (jakékoli kromě poslední, která odráží skutečné a spravedlivé rozdělení prostředků).

Pojďme si vzít příklad:

- Alice vlastní **100 000 satoshi** a Bob **30 000 satoshi**.
- Toto rozdělení je odráženo ve **2 commitment transakcích** (jedna na uživatele), které nejsou publikovány, ale mohly by být v případě uzavření kanálu.

![LNP201](assets/en/30.webp)

### Dobrý: kooperativní uzavření

Při **kooperativním uzavření** se Alice a Bob dohodnou na uzavření kanálu. Takto to probíhá:

1. Alice pošle Bobovi zprávu prostřednictvím komunikačního protokolu Lightning s návrhem na uzavření kanálu.
2. Bob souhlasí a obě strany v kanálu již neprovádějí žádné další transakce.

![LNP201](assets/en/31.webp)

3. Alice a Bob společně vyjednávají poplatky za **uzavírací transakci**. Tyto poplatky jsou obvykle vypočítány na základě trhu s poplatky Bitcoinu v době uzavření. Je důležité poznamenat, že **vždy osoba, která kanál otevřela** (v našem příkladu Alice), platí poplatky za uzavření.
4. Sestaví novou **uzavírací transakci**. Tato transakce se podobá commitment transakci, ale bez časových zámků nebo mechanismů pro odvolání, protože obě strany spolupracují a neexistuje riziko podvodu. Tato kooperativní uzavírací transakce se tedy liší od commitment transakcí.
   Například, pokud Alice vlastní **100 000 satoshi** a Bob **30 000 satoshi**, závěrečná transakce pošle **100 000 satoshi** na adresu Alice a **30 000 satoshi** na adresu Boba, bez omezení timelock. Jakmile je tato transakce podepsána oběma stranami, publikuje ji Alice. Jakmile je transakce potvrzena na Bitcoin blockchainu, Lightning kanál je oficiálně uzavřen.
   ![LNP201](assets/en/32.webp)

**Kooperativní uzavření** je preferovanou metodou uzavření, protože je rychlé (bez timelock) a transakční poplatky jsou upraveny podle aktuálních tržních podmínek Bitcoinu. To zabrání placení příliš malé částky, což by mohlo zablokovat transakci v mempoolech, nebo zbytečnému přeplácení, což vede k zbytečné finanční ztrátě pro účastníky.

### Špatné: nucené uzavření

Když Alicein uzel pošle zprávu Bobovu uzlu s žádostí o kooperativní uzavření, pokud neodpoví (například kvůli výpadku internetu nebo technickému problému), Alice může pokračovat v **nuceném uzavření** publikováním **poslední podepsané závazné transakce**.
V tomto případě Alice jednoduše publikuje poslední závaznou transakci, která odráží stav kanálu v okamžiku, kdy poslední Lightning transakce proběhla s správným rozdělením prostředků.

![LNP201](assets/en/33.webp)

Tato transakce zahrnuje **timelock** pro prostředky Alice, což zpomaluje uzavření.

![LNP201](assets/en/34.webp)

Také poplatky za závaznou transakci mohou být v době uzavření nevhodné, protože byly nastaveny v době vytvoření transakce, někdy několik měsíců předtím. Obecně klienti Lightningu přeceňují poplatky, aby se vyhnuli budoucím problémům, ale to může vést k nadměrným poplatkům, nebo naopak příliš nízkým.

Shrnutí, **nucené uzavření** je poslední možností, když druhá strana již neodpovídá. Je pomalejší a méně ekonomické než kooperativní uzavření. Proto by se mělo vyhnout, pokud je to možné.

### Podvod: podvádění

Nakonec, uzavření s **podváděním** nastane, když jedna ze stran se pokusí publikovat starou závaznou transakci, často kde držela více prostředků, než by měla. Například, Alice by mohla publikovat starou transakci, kde vlastnila **120 000 satoshi**, zatímco nyní vlastní pouze **100 000**.

![LNP201](assets/en/35.webp)

Bob, aby zabránil tomuto podvodu, sleduje Bitcoin blockchain a jeho mempool, aby zajistil, že Alice nepublikuje starou transakci. Pokud Bob zjistí pokus o podvod, může použít **revokační klíč** k získání prostředků Alice a potrestat ji tím, že vezme celé prostředky kanálu. Jelikož je Alice blokována timelockem na jejím výstupu, Bob má čas jej utratit bez timelocku na své straně, aby získal celou sumu na adresu, kterou vlastní.

![LNP201](assets/en/36.webp)

Samozřejmě, podvod může potenciálně uspět, pokud Bob nejedná v čase uloženém timelockem na Aliceině výstupu. V tomto případě je Alicein výstup odemčen, což jí umožňuje jej spotřebovat k vytvoření nového výstupu na adresu, kterou kontroluje.

**Co si odnést z této kapitoly?**

Existují tři způsoby, jak uzavřít kanál:

1. **Kooperativní uzavření**: Rychlé a méně nákladné, kde se obě strany dohodnou na uzavření kanálu a publikují přizpůsobenou závěrečnou transakci.
2. **Nucené uzavření**: Méně žádoucí, protože se spoléhá na publikování závazné transakce, s potenciálně nevhodnými poplatky a timelockem, který zpomaluje uzavření.
3. **Podvádění**: Pokud se jedna ze stran pokusí ukrást prostředky zveřejněním staré transakce, druhá může použít revokační klíč k potrestání tohoto podvodu.
   V nadcházejících kapitolách prozkoumáme Lightning Network z širší perspektivy, zaměříme se na to, jak její síť funguje.

# Síť likvidity

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning network](https://youtu.be/RAZAa3v41DM)

V této kapitole prozkoumáme, jak mohou platby na Lightning Network dosáhnout příjemce, i když nejsou přímo spojeni platebním kanálem. Lightning je skutečně **síť platebních kanálů**, která umožňuje posílání prostředků na vzdálený uzel prostřednictvím kanálů ostatních účastníků. Zjistíme, jak jsou platby směrovány napříč sítí, jak se likvidita pohybuje mezi kanály a jak se vypočítávají transakční poplatky.

### Síť platebních kanálů

Na Lightning Network odpovídá transakce převodu prostředků mezi dvěma uzly. Jak bylo vidět v předchozích kapitolách, je nutné otevřít kanál s někým, aby bylo možné provádět Lightning transakce. Tento kanál umožňuje téměř nekonečný počet transakcí mimo hlavní řetězec, než se uzavře a znovu získá zůstatek na hlavním řetězci. Tato metoda však má nevýhodu vyžadování přímého kanálu s druhou osobou pro příjem nebo odeslání prostředků, což znamená otevírací a zavírací transakci pro každý kanál. Pokud plánuji provést velké množství plateb s touto osobou, stává se otevření a zavření kanálu nákladově efektivním. Naopak, pokud potřebuji provést jen několik Lightning transakcí, otevření přímého kanálu není výhodné, protože by mě to stálo 2 transakce na hlavním řetězci pro omezený počet transakcí mimo hlavní řetězec. Tento případ by mohl nastat například při platbě Lightningem u obchodníka, aniž bych plánoval návrat.

K vyřešení tohoto problému umožňuje Lightning Network směrování platby přes několik kanálů a prostředníků, čímž umožňuje transakci bez přímého kanálu s druhou osobou.

Představte si například, že:

- **Alice** (v oranžové) má kanál se **Suzie** (v šedé) s **100 000 satoshi** na její straně a **30 000 satoshi** na straně Suzie.
- **Suzie** má kanál s **Bobem**, ve kterém vlastní **250 000 satoshi** a Bob nemá žádné satoshi.

![LNP201](assets/en/37.webp)

Pokud Alice chce poslat prostředky Bobovi bez otevření přímého kanálu s ním, musí to udělat přes Suzie, a každý kanál bude muset upravit likviditu na každé straně. **Poslané satoshi zůstávají v rámci jejich příslušných kanálů**; ve skutečnosti "nepřekračují" kanály, ale převod se uskuteční úpravou vnitřní likvidity v každém kanálu.

Předpokládejme, že Alice chce poslat **50 000 satoshi** Bobovi:

1. **Alice** pošle 50 000 satoshi **Suzie** ve společném kanálu.
2. **Suzie** replikuje tento převod posláním 50 000 satoshi **Bobovi** v jejich kanálu.

![LNP201](assets/en/38.webp)
Takto je platba směrována Bobovi prostřednictvím pohybu likvidity v každém kanálu. Na konci operace má Alice 50 000 satoshi. Skutečně převedla 50 000 satoshi, protože původně měla 100 000. Bob, na své straně, skončí s dalšími 50 000 satoshi. Pro Suzie (prostřední uzel) je tato operace neutrální: původně měla 30 000 satoshi ve svém kanálu s Alicí a 250 000 satoshi ve svém kanálu s Bobem, celkem 280 000 satoshi. Po operaci drží 80 000 satoshi ve svém kanálu s Alicí a 200 000 satoshi ve svém kanálu s Bobem, což je stejná suma jako na začátku.
Tento přenos je tedy omezen **dostupnou likviditou** ve směru přenosu.

### Výpočet trasy a limitů likvidity

Pojďme si vzít teoretický příklad jiné sítě s:

- **130 000 satoshi** na straně Alice (v oranžové) ve svém kanálu se **Suzie** (v šedé).
- **90 000 satoshi** na straně **Suzie** a **200 000 satoshi** na straně **Carol** (v růžové).
- **150 000 satoshi** na straně **Carol** a **100 000 satoshi** na straně **Boba**.

![LNP201](assets/en/39.webp)

Maximální množství, které Alice může poslat Bobovi v této konfiguraci, je **90 000 satoshi**, jelikož je omezena nejmenší dostupnou likviditou v kanálu od **Suzie k Carol**. V opačném směru (od Boba k Alici) není platba možná, protože na straně **Suzie** v kanálu s **Alicí** nejsou žádné satoshi. Proto není **žádná trasa** použitelná pro přenos v tomto směru.
Alice posílá **40 000 satoshi** Bobovi prostřednictvím kanálů:

1. Alice převádí 40 000 satoshi do svého kanálu se Suzie.
2. Suzie převádí 40 000 satoshi Carol ve svém sdíleném kanálu.
3. Carol nakonec převádí 40 000 satoshi Bobovi.

![LNP201](assets/en/40.webp)

**Satoshis poslané** v každém kanálu **zůstávají v kanálu**, takže satoshis poslané Carolem Bobovi nejsou stejné jako ty, které poslala Alice Suzie. Přenos se provádí pouze úpravou likvidity uvnitř každého kanálu. Navíc celková kapacita kanálů zůstává nezměněna.

![LNP201](assets/en/41.webp)

Stejně jako v předchozím příkladu, po transakci má zdrojový uzel (Alice) o 40 000 satoshi méně. Prostřední uzly (Suzie a Carol) si udržují stejnou celkovou částku, což operaci činí pro ně neutrální. Konečný uzel (Bob) obdrží dalších 40 000 satoshi.

Role prostředních uzlů je tedy velmi důležitá pro fungování Lightning Network. Umožňují převody nabízením více cest pro platby. Aby se tyto uzly podnítilo k poskytování své likvidity a účasti na směrování plateb, jsou jim vypláceny **poplatky za směrování**.

### Poplatky za směrování

Prostřední uzly uplatňují poplatky, aby umožnily platby procházet jejich kanály. Tyto poplatky jsou stanoveny **každým uzlem pro každý kanál**. Poplatky se skládají ze 2 prvků:

1. "**Základní poplatek**": pevná částka za kanál, často **1 sat** ve výchozím nastavení, ale přizpůsobitelná.
2. "**Proměnlivý poplatek**": procento z přenesené částky, vypočítané v **částech na milion (ppm)**. Ve výchozím nastavení je to **1 ppm** (1 sat na milion přenesených satoshi), ale lze to také upravit.
   Poplatky se také liší v závislosti na směru převodu. Například pro převod z Alice na Suzie se použijí poplatky Alice. Naopak, z Suzie na Alice, se použijí poplatky Suzie.

Například pro kanál mezi Alice a Suzie bychom mohli mít:

- **Alice**: základní poplatek 1 sat a 1 ppm za proměnlivé poplatky.
- **Suzie**: základní poplatek 0,5 sat a 10 ppm za proměnlivé poplatky.

![LNP201](assets/en/42.webp)

Pro lepší pochopení fungování poplatků se podívejme na stejnou Lightning Network jako předtím, ale nyní s následujícími směrovacími poplatky:

- Kanál **Alice - Suzie**: základní poplatek 1 satoshi a 1 ppm pro Alice.
- Kanál **Suzie - Carol**: základní poplatek 0 satoshi a 200 ppm pro Suzie.
- Kanál **Carol - Bob**: základní poplatek 1 satoshi a 1 ppm pro Suzie 2.
  ![LNP201](assets/en/43.webp)

Pro stejnou platbu **40 000 satoshi** Bobovi bude muset Alice poslat o něco více, protože každý prostředník si odečte své poplatky:

- **Carol** odečte 1,04 satoshi na kanálu s Bobem:
  $$ f*{\text{Carol-Bob}} = \text{základní poplatek} + \left(\frac{\text{ppm} \times \text{částka}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0,04 = 1,04 \text{ sats} $$

- **Suzie** odečte 8 satoshi na poplatcích na kanálu s Carol:
  $$ f*{\text{Suzie-Carol}} = \text{základní poplatek} + \left(\frac{\text{ppm} \times \text{částka}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001,04}{10^6} = 0 + 8,0002 \approx 8 \text{ sats} $$

Celkové poplatky za tuto platbu na této cestě jsou tedy **9,04 satoshi**. Alice tedy musí poslat **40 009,04 satoshi**, aby Bob přesně obdržel **40 000 satoshi**.

![LNP201](assets/en/44.webp)

Likvidita je tedy aktualizována:

![LNP201](assets/en/45.webp)

### Onion Routing

Pro směrování platby od odesílatele k příjemci používá Lightning Network metodu nazvanou "**onion routing**". Na rozdíl od směrování klasických dat, kde každý router rozhoduje o směru dat na základě jejich cíle, onion routing funguje jinak:

- **Odesílající uzel vypočítá celou trasu**: Alice například určí, že její platba musí projít přes Suzie a Carol, než dosáhne Boba.
- **Každý prostředník zná pouze svého bezprostředního souseda**: Suzie ví pouze, že obdržela prostředky od Alice a že je musí převést Carol. Nicméně Suzie neví, jestli je Alice zdrojový uzel nebo prostředník, a také neví, jestli je Carol konečný příjemce nebo jen další prostředník. Tento princip platí také pro Carol a všechny ostatní uzly na cestě. Onion routing tak chrání důvěrnost transakcí maskováním identity odesílatele a konečného příjemce. Aby mohl odesílající uzel v onion routing vypočítat kompletní trasu k příjemci, musí udržovat **síťový graf**, aby znal jeho topologii a určil možné trasy.
  **Co byste si měli odnést z této kapitoly?**

1. Na Lightning mohou být platby směrovány mezi uzly nepřímo spojenými prostřednictvím prostředníků. Každý z těchto prostředníků usnadňuje přenos likvidity.
2. Prostředníci obdrží provizi za svou službu, která se skládá z pevných a variabilních poplatků.
3. Onion routing umožňuje odesílajícímu uzlu vypočítat kompletní trasu bez toho, aby prostředníci znali zdroj nebo konečný cíl.

V této kapitole jsme prozkoumali směrování plateb na Lightning Network. Ale vyvstává otázka: co brání prostředníkům v přijetí příchozí platby bez jejího přeposlání do další destinace, s cílem zachytit transakci? To je přesně role HTLC, kterou prozkoumáme v následující kapitole.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

V této kapitole objevíme, jak Lightning umožňuje platby přecházet prostřednictvím prostředníků bez nutnosti jim důvěřovat, díky **HTLC** (_Hashed Time-Locked Contracts_). Tyto chytré kontrakty zajišťují, že každý prostředník obdrží prostředky z jeho kanálu pouze v případě, že přepošle platbu konečnému příjemci, jinak nebude platba ověřena.

Problém, který vzniká při směrování plateb, je tedy nutná důvěra v prostředníky a mezi samotnými prostředníky. Abychom to ilustrovali, pojďme se vrátit k našemu zjednodušenému příkladu sítě Lightning s 3 uzly a 2 kanály:

- Alice má kanál se Suzie.
- Suzie má kanál s Bobem.

Alice chce poslat 40 000 satoshi Bobovi, ale nemá s ním přímý kanál a nechce jej otevřít. Hledá trasu a rozhodne se jít přes uzl Suzie.

![LNP201](assets/en/46.webp)

Pokud Alice naivně pošle 40 000 satoshi Suzie s nadějí, že Suzie tuto sumu převede Bobovi, Suzie by mohla prostředky zadržet pro sebe a nic nepředat Bobovi.

![LNP201](assets/en/47.webp)
Aby se této situaci na Lightning zabránilo, používáme HTLC (Hashed Time-Locked Contracts), které dělají platbu prostředníkovi podmíněnou, což znamená, že Suzie musí splnit určité podmínky, aby mohla přistoupit k prostředkům Alice a převést je Bobovi.

### Jak HTLC fungují

HTLC je speciální kontrakt založený na dvou principech:

- **Podmínka přístupu**: Příjemce musí odhalit tajemství, aby odemkl platbu, která mu náleží.
- **Expirace**: Pokud není platba plně dokončena v určeném období, je zrušena a prostředky se vrátí odesílateli.

Takto tento proces funguje v našem příkladu s Alicí, Suzie a Bobem:

![LNP201](assets/en/48.webp)
**Vytvoření tajemství**: Bob vygeneruje náhodné tajemství označené jako _s_ (předobraz) a vypočítá jeho hash označený jako _r_ pomocí hashovací funkce označené jako _h_. Platí:

$$
r = h(s)
$$

Použití hashovací funkce znemožňuje najít _s_ pouze s _h(s)_, ale pokud je _s_ poskytnuto, je snadné ověřit, že odpovídá _h(s)_.

![LNP201](assets/en/49.webp)

**Odeslání žádosti o platbu**: Bob pošle Alici **fakturu** s žádostí o platbu. Tato faktura zvláště zahrnuje hash _r_.

![LNP201](assets/en/50.webp)

**Odeslání podmíněné platby**: Alice pošle Suzie HTLC na 40 000 satoshi. Podmínkou pro Suzie, aby tyto prostředky obdržela, je, že poskytne Alici tajemství _s'_ splňující následující rovnici:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Převod HTLC konečnému příjemci**: Suzie, aby získala 40 000 satoshi od Alice, musí převést podobné HTLC na 40 000 satoshi Bobovi, který má stejnou podmínku, totiž že musí Suzie poskytnout tajemství _s'_ splňující rovnici:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Ověření tajemstvím _s_**: Bob poskytne _s_ Suzie, aby obdržel slíbených 40 000 satoshi v HTLC. S tímto tajemstvím může Suzie poté odemknout Alicino HTLC a získat 40 000 satoshi od Alice. Platba je poté správně směrována Bobovi.

![LNP201](assets/en/53.webp)
Tento proces brání Suzie v zadržení Aliciných prostředků bez dokončení převodu Bobovi, protože musí platbu poslat Bobovi, aby získala tajemství _s_ a tím odemkla Alicino HTLC. Operace zůstává stejná i v případě, že trasa zahrnuje několik prostředníků: jedná se pouze o opakování kroků Suzie pro každého prostředníka. Každý uzel je chráněn podmínkami HTLC, protože odemknutí posledního HTLC příjemcem automaticky spouští odemknutí všech ostatních HTLC v kaskádě.

### Expirace a řízení HTLC v případě problémů

Pokud během procesu platby jeden z prostředníků nebo příjemný uzel přestane odpovídat, zejména v případě výpadku internetu nebo elektrické energie, pak platbu nelze dokončit, protože tajemství potřebné k odemknutí HTLC není přeneseno. Vezmeme-li náš příklad s Alicí, Suzie a Bobem, tento problém nastane například, pokud Bob nepředá tajemství _s_ Suzie. V tomto případě jsou všechna HTLC v cestě zablokována a také prostředky, které zajišťují.

![LNP201](assets/en/54.webp)

Aby se tomu zabránilo, HTLC na Lightningu mají expiraci, která umožňuje odstranění HTLC, pokud není po určité době dokončeno. Expirace následuje specifické pořadí, protože začíná nejprve s HTLC nejbližším příjemci a poté postupně přechází k vydavateli transakce. V našem příkladu, pokud Bob nikdy neposkytne tajemství _s_ Suzie, to by nejprve způsobilo expiraci Suziina HTLC směrem k Bobovi.

![LNP201](assets/en/55.webp)

Poté HTLC od Alice k Suzie.

![LNP201](assets/en/56.webp)

Pokud by se pořadí vypršení platnosti HTLC obrátilo, Alice by mohla získat zpět svou platbu dříve, než by Suzie mohla ochránit sebe před možným podvodem. Skutečně, pokud by se Bob vrátil pro své HTLC, zatímco Alice už své odstranila, Suzie by byla ve ztrátě. Toto kaskádové pořadí vypršení platnosti HTLC tak zajišťuje, že žádný prostředník neutrpí nespravedlivé ztráty.

### Reprezentace HTLC v transakcích závazku

Transakce závazku reprezentují HTLC takovým způsobem, že podmínky, které ukládají na Lightning, mohou být přeneseny na Bitcoin v případě nuceného uzavření kanálu během životnosti HTLC. Jako připomínka, transakce závazku reprezentují aktuální stav kanálu mezi dvěma uživateli a umožňují jednostranné nucené uzavření v případě problémů. S každým novým stavem kanálu jsou vytvořeny 2 transakce závazku: jedna pro každou stranu. Pojďme se vrátit k našemu příkladu s Alicí, Suzie a Bobem, ale podívejme se podrobněji na to, co se děje na úrovni kanálu mezi Alicí a Suzie, když je HTLC vytvořeno.
![LNP201](assets/en/57.webp)

Před zahájením platby 40 000 satoshi mezi Alicí a Bobem má Alice v kanálu se Suzie 100 000 satoshi, zatímco Suzie drží 30 000. Jejich transakce závazku jsou následující:

![LNP201](assets/en/58.webp)

Alice právě obdržela Bobovu fakturu, která obsahuje _r_, hash tajemství. Může tedy sestavit HTLC o 40 000 satoshi se Suzie. Toto HTLC je reprezentováno v nejnovějších transakcích závazku jako výstup nazvaný "**_HTLC Out_**" na straně Alice, protože prostředky jsou odchozí, a "**_HTLC In_**" na straně Suzie, protože prostředky jsou příchozí.

![LNP201](assets/en/59.webp)

Tyto výstupy spojené s HTLC sdílejí přesně stejné podmínky, a to:

- Pokud Suzie dokáže poskytnout tajemství _s_, může tento výstup okamžitě odemknout a převést jej na adresu, kterou kontroluje.
- Pokud Suzie tajemství _s_ nevlastní, nemůže tento výstup odemknout, a Alice ho bude moci odemknout po časovém zámku a poslat jej na adresu, kterou kontroluje. Časový zámek tedy dává Suzie období k reakci, pokud získá _s_.

Tyto podmínky platí pouze v případě, že je kanál uzavřen (tj. transakce závazku je publikována na řetězci) zatímco HTLC je stále aktivní na Lightning, což znamená, že platba mezi Alicí a Bobem ještě nebyla finalizována a HTLC ještě nevypršely. Díky těmto podmínkám může Suzie získat zpět 40 000 satoshi HTLC, které jí dluží, poskytnutím _s_. V opačném případě Alice získá prostředky po vypršení časového zámku, protože pokud Suzie _s_ nezná, znamená to, že nepřevedla 40 000 satoshi Bobovi, a tedy Alici nejsou dlužné žádné prostředky.

Navíc, pokud je kanál uzavřen, zatímco několik HTLC je nevyřešených, bude tam tolik dalších výstupů, kolik je probíhajících HTLC.
Pokud kanál není uzavřen, pak po vypršení nebo úspěchu platby Lightning jsou vytvořeny nové transakce závazku, které odrážejí nový, nyní stabilní stav kanálu, tj. bez jakýchkoli nevyřešených HTLC. Výstupy související s HTLC mohou být tedy odstraněny z transakcí závazku.

![LNP201](assets/en/60.webp)

Nakonec, v případě kooperativního uzavření kanálu, zatímco je HTLC aktivní, Alice a Suzie přestanou přijímat nové platby a čekají na vyřešení nebo vypršení platnosti probíhajících HTLC. To jim umožňuje publikovat jednodušší transakci pro uzavření, bez výstupů souvisejících s HTLC, čímž snižují poplatky a vyhýbají se čekání na možný časový zámek.
**Co byste si měli odnést z této kapitoly?**

HTLC umožňují směrování plateb Lightning přes více uzlů bez nutnosti jim důvěřovat. Zde jsou klíčové body, které si zapamatovat:

1. HTLC zajišťují bezpečnost plateb prostřednictvím tajemství (preimage) a času vypršení platnosti.
2. Vyřešení nebo vypršení platnosti HTLC probíhá v určitém pořadí: poté od cílového uzlu směrem ke zdroji, aby byl chráněn každý uzel.
3. Dokud není HTLC vyřešeno nebo nevyprší jeho platnost, je udržováno jako výstup v nejnovějších transakcích závazku.

V další kapitole zjistíme, jak uzel vydávající transakci Lightning najde a vybere trasy pro doručení platby příjemcovu uzlu.

## Hledání cesty

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![hledání cesty](https://youtu.be/wnUGJjOxd9Q)

V předchozích kapitolách jsme viděli, jak používat kanály jiných uzlů k směrování plateb a dosažení uzlu, aniž bychom byli přímo s ním spojeni přes kanál. Také jsme diskutovali o tom, jak zajistit bezpečnost převodu bez důvěry v prostředníkovy uzly. V této kapitole se zaměříme na nalezení nejlepší možné trasy k dosažení cílového uzlu.

### Problém směrování v Lightning

Jak jsme viděli, v Lightning je to uzel odesílající platbu, který musí vypočítat kompletní trasu k příjemci, protože používáme systém cibulového směrování. Prostředníkovy uzly neznají ani bod původu ani konečný cíl. Vědí pouze, odkud platba přichází a kterému uzlu ji musí předat dále. To znamená, že odesílající uzel musí udržovat dynamickou lokální topologii sítě, s existujícími uzly Lightning a kanály mezi nimi, s přihlédnutím k otevřením, uzavřením a aktualizacím stavu.

![LNP201](assets/en/61.webp)
I s touto topologií sítě Lightning existují zásadní informace pro směrování, které zůstávají odesílajícímu uzlu nedostupné, což je přesné rozdělení likvidity v kanálech v daném okamžiku. Skutečně, každý kanál zobrazuje pouze svou **celkovou kapacitu**, ale vnitřní rozdělení finančních prostředků je známo pouze dvěma účastnícím se uzlům. To představuje výzvy pro efektivní směrování, protože úspěch platby závisí zejména na tom, zda je její částka menší než nejnižší likvidita na zvolené trase. Nicméně, likvidity nejsou všechny viditelné odesílajícímu uzlu.
![LNP201](assets/en/62.webp)

### Aktualizace mapy sítě

Aby uzly udržely svou mapu sítě aktuální, pravidelně si vyměňují zprávy prostřednictvím algoritmu nazvaného "**_gossip_**". Jedná se o distribuovaný algoritmus používaný k šíření informací epidemiologickým způsobem mezi všechny uzly v síti, což umožňuje výměnu a synchronizaci globálního stavu kanálů v několika komunikačních cyklech. Každý uzel šíří informace jednomu nebo více sousedům vybraným náhodně nebo ne, ti zase šíří informace dalším sousedům a tak dále, dokud není dosaženo globálně synchronizovaného stavu.

2 hlavní zprávy vyměňované mezi uzly Lightning jsou následující:

- "**Oznámení kanálů**": zprávy signalizující otevření nového kanálu.
- **Aktualizace kanálů**: aktualizační zprávy o stavu kanálu, zejména o vývoji poplatků (ale ne o distribuci likvidity).
  Uzly Lightning také sledují Bitcoinový blockchain, aby detekovaly transakce uzavírající kanály. Uzavřený kanál je poté odstraněn z mapy, protože již nemůže být použit k směrování našich plateb.

### Směrování platby

Pojďme si vzít příklad malé Lightning Network se 7 uzly: Alice, Bob, 1, 2, 3, 4 a 5. Představme si, že Alice chce poslat platbu Bobovi, ale musí projít přes prostředníkové uzly.

![LNP201](assets/en/63.webp)

Zde je aktuální rozdělení prostředků v těchto kanálech:

- **Kanál mezi Alicí a 1**: 250 000 sats na straně Alice, 80 000 na straně 1 (celková kapacita 330 000 sats).
- **Kanál mezi 1 a 2**: 300 000 sats na straně 1, 200 000 na straně 2 (celková kapacita 500 000 sats).
- **Kanál mezi 2 a 3**: 50 000 sats na straně 2, 60 000 na straně 3 (celková kapacita 110 000 sats).
- **Kanál mezi 2 a 5**: 90 000 sats na straně 2, 160 000 na straně 5 (celková kapacita 250 000 sats).
- **Kanál mezi 2 a 4**: 180 000 sats na straně 2, 110 000 na straně 4 (celková kapacita 290 000 sats).
- **Kanál mezi 4 a 5**: 200 000 sats na straně 4, 10 000 na straně 5 (celková kapacita 210 000 sats).
- **Kanál mezi 3 a Bobem**: 50 000 sats na straně 3, 250 000 na straně Boba (celková kapacita 300 000 sats).
- **Kanál mezi 5 a Bobem**: 260 000 sats na straně 5, 100 000 na straně Boba (celková kapacita 360 000 sats).

![LNP201](assets/en/64.webp)

Pro provedení platby 100 000 sats od Alice k Bobovi jsou možnosti směrování omezeny dostupnou likviditou v každém kanálu. Optimální trasa pro Alici, na základě známého rozdělení likvidity, by mohla být sekvence `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Ale protože Alice nezná přesné rozdělení prostředků v každém kanálu, musí optimální trasu odhadnout pravděpodobnostně, s ohledem na následující kritéria:

- **Pravděpodobnost úspěchu**: kanál s vyšší celkovou kapacitou má větší pravděpodobnost, že bude obsahovat dostatečnou likviditu. Například kanál mezi uzlem 2 a uzlem 3 má celkovou kapacitu 110 000 sats, takže je nepravděpodobné, že by na straně uzlu 2 bylo nalezeno 100 000 sats nebo více, i když to zůstává možné.
- **Transakční poplatky**: při výběru nejlepší trasy také odesílající uzel zohledňuje poplatky uplatňované každým prostředníkovým uzlem a snaží se minimalizovat celkové náklady na směrování.
- **Expirace HTLCs**: aby se zabránilo zablokování plateb, je také parametrem k zvážení doba expirace HTLCs.
- **Počet mezilehlých uzlů**: konečně, v širším smyslu, odesílající uzel se bude snažit najít trasu s co nejmenším počtem uzlů, aby snížil riziko selhání a omezil poplatky za Lightning transakce.
  Analýzou těchto kritérií může odesílající uzel testovat nejpravděpodobnější trasy a pokusit se je optimalizovat. V našem příkladu by Alice mohla nejlepší trasy seřadit takto:

1. `Alice → 1 → 2 → 5 → Bob`, protože je to nejkratší trasa s nejvyšší kapacitou.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, protože tato trasa nabízí dobré kapacity, ačkoli je delší než první.
3. `Alice → 1 → 2 → 3 → Bob`, protože tato trasa zahrnuje kanál `2 → 3`, který má velmi omezenou kapacitu, ale zůstává potenciálně použitelný.

### Provedení platby

Alice se rozhodne otestovat svou první trasu (`Alice → 1 → 2 → 5 → Bob`). Proto pošle HTLC o 100 000 sats uzlu 1. Tento uzel zkontroluje, že má dostatečnou likviditu s uzlem 2, a pokračuje v přenosu. Uzel 2 poté přijme HTLC od uzlu 1, ale uvědomí si, že nemá dostatečnou likviditu ve svém kanálu s uzlem 5 pro přesměrování platby 100 000 sats. Poté pošle zpět uzlu 1 chybovou zprávu, která se přenese Alici. Tato trasa selhala.

![LNP201](assets/en/66.webp)

Alice poté pokusí směrovat svou platbu pomocí své druhé trasy (`Alice → 1 → 2 → 4 → 5 → Bob`). Pošle HTLC o 100 000 sats uzlu 1, který ji přenese uzlu 2, poté uzlu 4, uzlu 5 a nakonec Bobovi. Tentokrát je likvidita dostatečná a trasa je funkční. Každý uzel postupně odemkne svůj HTLC pomocí předobrazu poskytnutého Bobem (tajemství _s_), což umožní úspěšné dokončení Aliciny platby Bobovi.

![LNP201](assets/en/67.webp)

Hledání trasy probíhá takto: odesílající uzel začne identifikací nejlepších možných tras, poté postupně zkouší platby, dokud nenajde funkční trasu.

Je důležité poznamenat, že Bob může Alici poskytnout informace ve **faktuře** usnadňující směrování. Například může uvést blízké kanály s dostatečnou likviditou nebo odhalit existenci soukromých kanálů. Tyto indikace umožňují Alici vyhnout se trasám s malou šancí na úspěch a nejprve se pokusit o cesty doporučené Bobem.

**Co si odnést z této kapitoly?**

1. Uzly udržují mapu topologie sítě prostřednictvím oznámení a sledováním uzavření kanálů na Bitcoin blockchainu.
2. Hledání optimální trasy pro platbu zůstává pravděpodobnostní a závisí na mnoha kritériích.
3. Bob může poskytnout indikace ve **faktuře** k usměrnění směrování Alice a ušetřit ji od testování nepravděpodobných tras.

V následující kapitole se budeme konkrétně zabývat fungováním faktur, kromě některých dalších nástrojů používaných na Lightning Network.

# Nástroje Lightning Network

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Faktura, LNURL a Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![faktura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
V této kapitole se podrobněji podíváme na fungování Lightning **faktur**, tedy platebních požadavků, které odesílá příjemce uzlu odesílateli. Cílem je pochopit, jak platit a přijímat platby na Lightning. Také probereme 2 alternativy klasických faktur: LNURL a Keysend.
![LNP201](assets/en/68.webp)

### Struktura Lightning faktur

Jak bylo vysvětleno v kapitole o HTLCs, každá platba začíná generováním **faktury** příjemcem. Tato faktura je poté předána plátci (prostřednictvím QR kódu nebo kopírováním a vložením) k zahájení platby. Faktura se skládá ze dvou hlavních částí:

1. **Část čitelná člověkem**: tato sekce obsahuje jasně viditelná metadata pro zlepšení uživatelského zážitku.
2. **Payload**: tato sekce obsahuje informace určené pro strojové zpracování platby.

Typická struktura faktury začíná identifikátorem `ln` pro "Lightning", následovaným `bc` pro Bitcoin, poté částkou faktury. Oddělovač `1` rozlišuje část čitelnou člověkem od datové (payload) části.

Pojďme se podívat na následující fakturu jako příklad:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Už teď ji můžeme rozdělit na 2 části. Nejprve je tu Část čitelná člověkem:

```invoice
lnbc100u
```

Poté část určená pro payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Dvě části jsou odděleny `1`. Tento oddělovač byl zvolen místo speciálního znaku, aby bylo možné snadno kopírovat celou fakturu dvojitým kliknutím.
V první části můžeme vidět, že:

- `ln` naznačuje, že jde o transakci Lightning.
- `bc` naznačuje, že síť Lightning je na blockchainu Bitcoinu (a ne na testnetu nebo na Litecoinu).
- `100u` označuje množství faktury, vyjádřené v **mikrosatoshis** (`u` znamená "mikro"), což zde odpovídá 10 000 sats.

Pro označení částky platby je vyjádřena v podjednotkách bitcoinu. Zde jsou použité jednotky:

- **Millibitcoin (označeno `m`):** Představuje tisícinu bitcoinu.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Mikrobitcoin (označeno `u`):** Také někdy nazývaný "bit", představuje miliontinu bitcoinu.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (označeno `n`):** Představuje miliardtinu bitcoinu.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Pikobitcoin (označeno `p`):** Představuje biliontinu bitcoinu.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### Obsah faktury

Obsah faktury zahrnuje několik informací nezbytných pro zpracování platby:

- **Časové razítko:** Okamžik vytvoření faktury, vyjádřený v Unix Timestamp (počet sekund, které uplynuly od 1. ledna 1970).
- **Hašování tajemství**: Jak jsme viděli v sekci o HTLCs, přijímající uzel musí poskytnout odesílajícímu uzlu haš předobrazu. To se používá v HTLCs k zabezpečení transakce. Odkazovali jsme na to jako na "_r_".
- **Tajemství platby**: Další tajemství je generováno příjemcem, ale tentokrát je předáno odesílajícímu uzlu. Používá se v cibulovém směrování, aby se zabránilo meziuzlům v odhadu, zda je další uzel konečným příjemcem nebo ne. Tím se udržuje určitá forma důvěrnosti pro příjemce vůči poslednímu meziuzlu na trase.
- **Veřejný klíč příjemce**: Označuje plátci identifikátor osoby, které má být zaplaceno.
- **Doba expirace**: Maximální doba pro zaplacení faktury (standardně 1 hodina).
- **Nápovědy pro směrování**: Další informace poskytnuté příjemcem, které pomáhají odesílateli optimalizovat trasu platby.
- **Podpis**: Zaručuje integritu faktury ověřením všech informací.

Faktury jsou poté zakódovány ve formátu **bech32**, stejně jako adresy Bitcoin SegWit (formát začínající `bc1`).

### LNURL Výběr

V tradiční transakci, jako je nákup v obchodě, je vygenerována faktura na celkovou částku k zaplacení. Jakmile je faktura prezentována (ve formě QR kódu nebo řetězce znaků), zákazník ji může naskenovat a dokončit transakci. Platba pak následuje tradiční proces, který jsme studovali v předchozí sekci. Tento proces však někdy může být pro uživatelskou zkušenost velmi zdlouhavý, protože vyžaduje, aby příjemce poslal informace odesílateli prostřednictvím faktury.
Pro určité situace, jako je vybírání bitcoinů z online služby, je tradiční proces příliš zdlouhavý. V takových případech řešení **LNURL** pro výběr zjednodušuje tento proces zobrazením QR kódu, který naskenuje peněženka příjemce a automaticky vytvoří fakturu. Služba poté zaplatí fakturu a uživatel jednoduše vidí okamžitý výběr.

![LNP201](assets/en/69.webp)

LNURL je komunikační protokol, který specifikuje sadu funkcionalit navržených k zjednodušení interakcí mezi Lightning uzly a klienty, stejně jako s aplikacemi třetích stran. LNURL výběr, jak jsme právě viděli, je tedy jen jedním příkladem mezi dalšími funkcionalitami.
Tento protokol je založen na HTTP a umožňuje vytváření odkazů pro různé operace, jako je žádost o platbu, žádost o výběr nebo jiné funkce, které zlepšují uživatelskou zkušenost. Každé LNURL je bech32 kódované URL s předponou lnurl, které, jakmile je naskenováno, spustí sérii automatických akcí v Lightning peněžence.
Například funkce LNURL-withdraw (LUD-03) umožňuje vybírat prostředky ze služby skenováním QR kódu, bez nutnosti ručně generovat fakturu. Podobně LNURL-auth (LUD-04) umožňuje přihlášení do online služeb pomocí soukromého klíče v Lightning peněžence místo hesla.

### Odesílání Lightning platby bez faktury: Keysend

Dalším zajímavým případem je převod prostředků bez předchozího přijetí faktury, známý jako "**Keysend**". Tento protokol umožňuje odesílání prostředků přidáním preimage do šifrovaných platebních dat, přístupných pouze příjemci. Tato preimage umožňuje příjemci odemknout HTLC, čímž získá prostředky bez předchozího vygenerování faktury.

Zjednodušeně, v tomto protokolu je to odesílatel, kdo generuje tajemství použité v HTLCs, spíše než příjemce. Prakticky to umožňuje odesílateli provést platbu bez předchozí interakce s příjemcem.

![LNP201](assets/en/70.webp)

**Co byste si měli odnést z této kapitoly?**

1. **Lightning Invoice** je žádost o platbu skládající se z části čitelné pro člověka a části s daty pro stroj.
2. Faktura je kódována v **bech32**, s oddělovačem `1` pro usnadnění kopírování a datovou částí obsahující všechny informace potřebné k zpracování platby.
3. Na Lightning existují i jiné platební procesy, zejména **LNURL-Withdraw** pro usnadnění výběrů a **Keysend** pro přímé převody bez faktury.

V následující kapitole uvidíme, jak může operátor uzlu spravovat likviditu ve svých kanálech, aby nikdy nebyl blokován a vždy mohl odesílat a přijímat platby na Lightning Network.

## Správa vaší likvidity

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![správa vaší likvidity](https://youtu.be/YuPrbhEJXbg)

V této kapitole prozkoumáme strategie pro efektivní správu likvidity na Lightning Network. Správa likvidity se liší v závislosti na typu uživatele a kontextu. Podíváme se na hlavní principy a existující techniky, abychom lépe pochopili, jak tuto správu optimalizovat.

### Potřeby likvidity

Na Lightning existují tři hlavní uživatelské profily, z nichž každý má specifické potřeby v oblasti likvidity:

1. **Platící (The Payer)**: Toto je ten, kdo provádí platby. Potřebují odchozí likviditu, aby mohli převádět prostředky ostatním uživatelům. Například to může být spotřebitel.
2. **Prodávající (The Seller or Payee)**: Toto je ten, kdo přijímá platby. Potřebují příchozí likviditu, aby mohli přijímat platby na svůj uzel. Například to může být podnik nebo internetový obchod.
3. **Router**: Prostředník, uzel často specializovaný na směrování plateb, který musí optimalizovat svou likviditu v každém kanálu, aby mohl směrovat co nejvíce plateb a vydělávat poplatky.

Tyto profily samozřejmě nejsou pevně dané; uživatel může přecházet mezi rolí platícího a příjemce v závislosti na transakcích. Například Bob může přijímat svůj plat na Lightning od svého zaměstnavatele, což ho staví do pozice "prodávajícího", který potřebuje příchozí likviditu. Následně, pokud chce použít svůj plat na nákup jídla, stává se "platícím" a musí pak mít odchozí likviditu.

Pro lepší pochopení si vezměme příklad jednoduché sítě složené ze tří uzlů: kupujícího (Alice), router (Suzie) a prodávajícího (Bob).

![LNP201](assets/en/71.webp)

Představte si, že kupující chce poslat 30 000 satoshi prodávajícímu a že platba prochází přes uzel routeru. Každá strana musí pak mít minimální množství likvidity ve směru platby:

- Platící musí mít na své straně kanálu s routerem alespoň 30 000 satoshi.
- Prodávající musí mít kanál, kde jsou na opačné straně 30 000 satoshi, aby je mohl přijmout.
- Router musí mít 30 000 satoshi na straně platícího ve svém kanálu a také 30 000 satoshi na své straně v kanálu s prodávajícím, aby mohl platbu směrovat.

![LNP201](assets/en/72.webp)

### Strategie řízení likvidity

Platící musí zajistit dostatečnou likviditu na své straně kanálů, aby garantovali odchozí likviditu. To se ukazuje jako relativně jednoduché, protože stačí otevřít nové Lightning kanály, aby měli tuto likviditu. Skutečně, počáteční prostředky uzamčené v multisig on-chain jsou zcela na straně platícího v Lightning kanálu na začátku. Platící kapacita je tedy zajištěna, pokud jsou kanály otevřeny s dostatečnými prostředky. Když je odchozí likvidita vyčerpána, stačí otevřít nové kanály.
Na druhou stranu, pro prodávajícího je úkol složitější. Aby mohli přijímat platby, musí mít likviditu na opačné straně svých kanálů. Proto otevření kanálu nestačí: musí také provést platbu v tomto kanálu, aby přesunuli likviditu na druhou stranu, než mohou sami přijímat platby. Pro určité profily uživatelů Lightning, jako jsou obchodníci, existuje jasná disproporce mezi tím, co jejich uzel odesílá a co přijímá, protože cílem podnikání je primárně inkasovat více, než utratí, aby generovalo zisk. Naštěstí pro tyto uživatele se specifickými potřebami příchozí likvidity existuje několik řešení:

- **Přitahování kanálů**: Obchodník těží z výhody díky objemu očekávaných příchozích plateb na svém uzlu. S ohledem na to se mohou pokusit přilákat směrovací uzly, které hledají příjem z transakčních poplatků a které by mohly otevřít kanály směrem k nim, s nadějí, že budou směrovat jejich platby a inkasovat přidružené poplatky.
- **Pohyb likvidity**: Prodávající může také otevřít kanál a převést část prostředků na opačnou stranu tím, že provede fiktivní platby na jiný uzel, který peníze vrátí jiným způsobem. V další části uvidíme, jak tuto operaci provést.
- **Trojúhelníkové otevření**: Existují platformy pro uzly, které chtějí společně otevřít kanály, což každému umožňuje těžit z okamžité příchozí a odchozí likvidity. Například [LightningNetwork+](https://lightningnetwork.plus/) nabízí tuto službu. Pokud si Alice, Bob a Suzie chtějí otevřít kanál s 100 000 sats, mohou se na této platformě dohodnout, že Alice otevře kanál směrem k Bobovi, Bob směrem k Suzie a Suzie směrem k Alici. Tímto způsobem každý má 100 000 sats odchozí likvidity a 100 000 sats příchozí likvidity, přičemž zablokovali pouze 100 000 sats.

![LNP201](assets/en/73.webp)

- **Nákup kanálů**: Existují také služby pro pronájem Lightning kanálů, aby bylo možné získat příchozí likviditu, jako například [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) nebo [Lightning Labs Pool](https://lightning.engineering/pool/). Například Alice si může koupit kanál o jednom milionu satoshi směrem k jejímu uzlu, aby mohla přijímat platby.

![LNP201](assets/en/74.webp)

Nakonec, pro směrovače, jejichž cílem je maximalizovat počet zpracovaných plateb a vybrané poplatky, musí:

- Otevřít dobře financované kanály se strategickými uzly.
- Pravidelně upravovat rozdělení prostředků v kanálech podle potřeb sítě.

### Služba Loop Out

Služba [Loop Out](https://lightning.engineering/loop/), kterou nabízí Lightning Labs, umožňuje přesunout likviditu na opačnou stranu kanálu a zároveň si vrátit prostředky na Bitcoin blockchainu. Například Alice pošle 1 milion satoshi přes Lightning na loop uzel, který jí tyto prostředky vrátí v on-chain bitcoinech. Tím vyváží její kanál s 1 milionem satoshi na každé straně, optimalizuje její kapacitu přijímat platby.

![LNP201](assets/en/75.webp)

Tato služba tedy umožňuje získat příchozí likviditu a zároveň si vrátit své bitcoiny na-chain, což pomáhá omezit imobilizaci hotovosti potřebné k přijímání plateb pomocí Lightning.

**Co si odnést z této kapitoly?**

- K odesílání plateb na Lightningu musíte mít dostatečnou likviditu na vaší straně ve vašich kanálech. Pro zvýšení této odesílací kapacity stačí otevřít nové kanály.
- K přijímání plateb potřebujete mít likviditu na opačné straně ve vašich kanálech. Zvýšení této přijímací kapacity je složitější, protože vyžaduje, aby ostatní otevřeli kanály směrem k vám, nebo aby provedli (fiktivní nebo skutečné) platby k přesunu likvidity na druhou stranu.
- Udržení likvidity tam, kde je požadováno, může být ještě náročnější v závislosti na využití kanálů. Proto existují nástroje a služby, které pomáhají vyvážit kanály podle přání.

V další kapitole navrhuji projít nejdůležitější koncepty tohoto školení.

# Jít dál

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Závěr školení

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![závěr](https://youtu.be/MaWpD0rbkVo)
V tomto závěrečném kapitole, která označuje konec školení LNP201, navrhuji znovu navštívit důležité koncepty, které jsme společně probrali.
Cílem tohoto školení bylo poskytnout vám komplexní a technické porozumění Lightning Network. Zjistili jsme, jak Lightning Network spoléhá na Bitcoin blockchain k provádění transakcí mimo řetězec, přičemž si zachovává základní charakteristiky Bitcoinu, zejména absenci potřeby důvěřovat ostatním uzlům.

### Platební kanály

V úvodních kapitolách jsme prozkoumali, jak dvě strany mohou provádět transakce mimo Bitcoin blockchain tím, že otevřou platební kanál. Zde jsou kroky, které jsme probrali:

1. **Otevření kanálu**: Vytvoření kanálu se provádí prostřednictvím Bitcoin transakce, která uzamkne prostředky na 2/2 multisignature adrese. Tento vklad reprezentuje Lightning kanál na blockchainu.

![LNP201](assets/en/76.webp) 2. **Transakce v kanálu**: V tomto kanálu je pak možné provádět mnoho transakcí bez nutnosti je zveřejňovat na blockchainu. Každá Lightning transakce vytváří nový stav kanálu, který je reflektován v commitment transakci.
![LNP201](assets/en/77.webp)

3. **Zajištění a uzavření**: Účastníci se zavážou k novému stavu kanálu výměnou revokačních klíčů k zajištění prostředků a prevenci podvodu. Obě strany mohou kanál uzavřít kooperativně vytvořením nové transakce na Bitcoin blockchainu, nebo jako poslední možnost prostřednictvím nuceného uzavření. Tato poslední možnost, ačkoli méně efektivní kvůli delší době a někdy špatně odhadovaným poplatkům, stále umožňuje získání prostředků zpět. V případě podvodu může oběť potrestat podvodníka získáním všech prostředků z kanálu na blockchainu.

![LNP201](assets/en/78.webp)

### Síť kanálů

Po studiu izolovaných kanálů jsme rozšířili naši analýzu na síť kanálů:

- **Směrování**: Když dvě strany nejsou přímo spojeny kanálem, síť umožňuje směrování prostřednictvím intermediárních uzlů. Platby pak přecházejí z jednoho uzlu na druhý.

![LNP201](assets/en/79.webp)

- **HTLCs**: Platby, které procházejí intermediárními uzly, jsou zajištěny "_Hash Time-Locked Contracts_" (HTLC), které umožňují uzamknout prostředky, dokud není platba dokončena od začátku do konce.

![LNP201](assets/en/80.webp)

- **Onion Routing**: Aby byla zajištěna důvěrnost platby, onion routing maskuje konečný cíl před intermediárními uzly. Odesílající uzel musí tedy vypočítat celou trasu, ale v absenci úplných informací o likviditě kanálů postupuje prostřednictvím postupných pokusů o směrování platby.

![LNP201](assets/en/81.webp)

### Správa likvidity

Viděli jsme, že správa likvidity je na Lightning výzvou, aby se zajistil plynulý tok plateb. Odesílání plateb je relativně jednoduché: stačí otevřít kanál. Nicméně přijímání plateb vyžaduje mít likviditu na opačné straně svých kanálů. Zde jsou některé diskutované strategie:

- **Přitahování kanálů**: Povzbuzením ostatních uzlů, aby otevřely kanály směrem k sobě, uživatel získá příchozí likviditu.

- **Přesun likvidity**: Odesíláním plateb do jiných kanálů se likvidita přesune na opačnou stranu.

![LNP201](assets/en/82.webp)

- **Využití služeb jako Loop a Pool**: Tyto služby umožňují rebalancování nebo nákup kanálů s likviditou na opačné straně.
  ![LNP201](assets/en/83.webp)
- **Spolupracující otevření**: Existují také platformy dostupné pro spojení k provádění trojúhelníkových otevření a získání příchozí likvidity.

![LNP201](assets/en/84.webp)

# Závěr

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Ohodnoťte tento kurz

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Závěrečná zkouška

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Závěr

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Gratulujeme! 🎉

Dokončili jste školení LNP 201 - Úvod do Lightning Network!

Můžete být na sebe hrdí, protože tohle není jednoduché téma.

Jen málo lidí se ponoří tak hluboko do králičí nory Bitcoinu.

Velké poděkování **Fanisi Michalakisovi** za poskytnutí tohoto skvělého bezplatného kurzu o technickém fungování Lightning Network.

Neváhejte ho sledovat na [Twitteru](https://x.com/FanisMichalakis), na [jeho blogu](https://fanismichalakis.fr/) nebo skrze jeho práci v [LN Markets](https://lnmarkets.com/).

Nyní, když ovládáte Lightning Network, vás zvu k prozkoumání našich dalších bezplatných kurzů na Plan ₿ Network pro prohloubení znalostí dalších aspektů Satoshi Nakamotova vynálezu:

#### Pochopte, jak funguje Bitcoin peněženka s

https://planb.network/courses/cyp201

#### Objevte historii původu Bitcoinu s

https://planb.network/courses/his201

#### Nakonfigurujte BTC platební server s

https://planb.network/courses/btc305

#### Ovládněte principy soukromí v Bitcoinu

https://planb.network/courses/btc204

#### Objevte základy těžby s

https://planb.network/courses/min201

#### Naučte se vytvořit svou Bitcoin komunitu s

https://planb.network/courses/btc302
