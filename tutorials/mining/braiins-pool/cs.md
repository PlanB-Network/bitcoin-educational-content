---
name: Braiins Pool

description: Úvod do Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, dříve známý jako Slush Pool, je první Bitcoinový těžební pool. Byl založen v listopadu 2010 a svůj první blok vytěžil 16. prosince 2010, blok 97834.

Května 2024 má Braiins Pool výpočetní výkon 13 EH/s, což představuje asi 1,8% celkového hashrate Bitcoinu. Celkem vytěžil 1 307 188 bitcoinů, což je přibližně 6% z maximálních 21 milionů bitcoinů, které kdy budou existovat.

### Systém odměn

Od konce roku 2023 změnil Braiins Pool svůj systém odměn na systém FPPS (Full Pay Per Share). To znamená, že těžaři dostávají odměny každý den za veškerou svou práci z předchozího dne, i když pool nenašel blok. To se liší od starého systému, kde těžaři dostali odměnu pouze v případě, že pool našel blok.

**Je důležité poznamenat, [podle tweetu od Mononauta](https://x.com/mononautical/status/1777686545715089605), který analyzuje Bitcoin TimeChain, že mnoho těžebních poolů používajících systém FPPS by posílalo vytěžené bitcoiny na adresu AntPool, což by znamenalo, že AntPool kontroluje hashrate všech těchto poolů, asi 47% celosvětového Bitcoin hashrate. To je velmi špatná zpráva pro decentralizaci sítě.**

### Poplatky za pool

Poplatky za Braiins Pool jsou 2,5%, nicméně pokud používáte na svých strojích BraiinsOS, budou poplatky 0%

### Výběry

**Výběry přes Lightning**
Výběry přes Lightning vám umožní vybrat vaše odměny bez minimální částky jednou denně prostřednictvím Lightning adresy.
Pro použití této metody musíte mít peněženku kompatibilní s Lightning adresami.

**Výběry On-Chain**
Výběry On-Chain jsou omezeny na minimální částku a mohou podléhat poplatkům.
Minimální částka: 20 000 sats
Poplatky: 10 000 sats pro částky menší než 500 000 sats
Zdarma pro částky nad 500 000 sats
Výběry mohou být spuštěny podle časového intervalu nebo podle částky.

## Vytvoření účtu

Pro začátek používání Braiins Pool [přejděte na jejich webové stránky](https://braiins.com/pool) a klikněte v pravém horním rohu na "SIGN UP"


![signup](assets/3.webp)

Zadejte své informace a potvrďte, poté obdržíte email s žádostí o potvrzení vaší adresy. Potvrďte pomocí odkazu v emailu, který jste obdrželi, a poté se přihlaste na platformu

![signup](assets/4.webp)


## Přidání "workeru"
Worker je těžař, kterého připojíte k poolu. Pro přidání nového těžaře klikněte v levém bočním menu na "Workers".
![signup](assets/7.webp)

Poté klikněte na fialové tlačítko "Connect Workers +".

V tomto okně vyberte svou geografickou oblast.

Pokud těžař, kterého chcete připojit, používá BraiinsOS, vyberte protokol "Stratum V2". V opačném případě vyberte "Stratum V1".

![signup](assets/8.webp)

Zde budete mít informace, které zadáte na webové stránce vašeho těžaře (viz dokumentaci vašeho těžaře, kde tyto informace zadat).

Zde, **"stratum+tcp://eu.stratum.braiins.com:3333"** je URL poolu.
**JimZap.workerName** je váš identifikátor a název vašeho těžaře, kde JimZap je identifikátor a .workerName je název těžaře. Pokud máte více těžařů, můžete jim buď dát stejný název, v takovém případě se jejich výpočetní výkon na dashboardu sečte, nebo jim dát různé názvy pro individuální monitorování.
A heslo je vždy stejné **"anything123"**

Jakmile tyto informace zadáte na webové stránce vašeho těžaře a začne s těžbou, uvidíte ho po několika minutách objevit se na Braiins Pool Dashboardu.

## Přehled Dashboardu

![signup](assets/9.webp)

V horním banneru můžete vidět průměrný celkový hashrate všech vašich těžařů za 5 minut, 1 hodinu a 24 hodin. A souhrn počtu těžařů online nebo offline.
Níže graf umožňuje sledovat vývoj vašeho výpočetního výkonu.

![signup](assets/10.webp)

Pod tímto grafem máte několik informací o vašich odměnách v sats.

**"Today's Mining Rewards"** Udává počet sats, které jste dnes vytěžili. Na konci dne bude tato hodnota resetována na 0 a sats budou poslány na váš účet.

**"Yesterday's Total Reward"** Počet sats, které jste vytěžili den předtím

**"Est. Profitability (1 TH/s)"** Je odhad počtu sats, které vyděláte za jeden den při výpočetním výkonu 1 TH/s. Například, pokud je hodnota 77 sats, a máte výpočetní výkon 10 TH/s nepřetržitě po celý den, pak byste teoreticky vydělali 77 x 10 = 770 sats za den.

**"All Time Reward"** Celkový počet sats, které jste vytěžili s Braiins Pool

**"Reward Scheme"** Sazba poplatku uplatněná poolem

**"Next Payout ETA"** Odhad doby, než budete moci vybrat sats z platformy. Zde odhad neukazuje nic, protože těžba probíhá teprve několik minut.

**"Account Balance"** Počet sats dostupných na vašem účtu, které poté můžete vybrat.
## Nastavení Výběrů
Své odměny můžete vybírat buď on-chain nebo přes lightning s adresou.

Nahoře klikněte na "Funds". Ve výchozím nastavení máte "Bitcoin Account". Můžete vytvořit další pro sdílení odměn. K tomu se vrátíme v další sekci.

Prozatím klikněte na "Set up".

![signup](assets/17.webp)

V tomto novém okně můžete vybrat "Onchain payout".

Pojmenujte tuto peněženku, poskytněte BTC adresu a vyberte typ spouštěče, který chcete. "Threshold" znamená, že platba bude spuštěna, když jste nahromadili určené množství BTC, a s "Time interval", platba bude spuštěna v pravidelných intervalech (den/týdny/měsíce).

Vezměte na vědomí, že minimální částka je 0.0002 BTC a že pod 0.005 BTC bude uplatněn poplatek 0.0001 BTC.

![signup](assets/18.webp)

Pokud chcete použít Lightning výběry, budete potřebovat peněženku, která poskytuje Lightning adresu. Například můžete použít getAlby.

Nahoře v okně klikněte na "Lightning payout".

Zadejte svou Lightning adresu a zaškrtněte políčko "I understand..." poté potvrďte.

S touto metodou výběru budou vaše odměny posílány do vaší peněženky každý den.

![signup](assets/14.webp)
Jakmile ověříte nastavení vašich výplat, obdržíte potvrzující email.
![signup](assets/15.webp)

## Sdílení odměn

Braiins Pool také umožňuje sdílet vaše odměny mezi více peněženkami.

Provedete to tak, že kliknete nahoře na "Mining" a poté vlevo na "Settings".

![signup](assets/19.webp)

Na této stránce budete moci přidat další "Financial Account" kliknutím na "Add Another Financial Account" a distribuovat vaše odměny v % mezi tyto různé účty, ke kterým musíte přiřadit peněženku. Pro přiřazení nové peněženky k Financial Account se odkazujte na předchozí sekci.