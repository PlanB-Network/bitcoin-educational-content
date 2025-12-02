---
name: Public Pool
description: Úvod do Veřejného bazénu
---

![signup](assets/cover.webp)

**Veřejný bazén** není jen tak nějaký bazén; jedná se o to, co se také nazývá **Solo bazén**. Pokud váš [miner](https://planb.academy/resources/glossary/miner) úspěšně vytěží blok, pak získáte celou odměnu za blok, která se nesdílí s ostatními účastníky bazénu ani s samotným bazénem.

**Veřejný bazén** poskytuje pouze **šablonu bloku** pro váš miner, aby mohl vykonávat svou úlohu, aniž byste potřebovali mít **Bitcoinový uzel** a software, který komunikuje s vaším minerem. Jelikož nesdružujete svůj výpočetní výkon s výkonem ostatních účastníků, vaše šance na úspěšné vytěžení bloku jsou samozřejmě velmi nízké, což připomíná jakýsi loterijní systém, kde někdy šťastný jedinec vyhraje jackpot.

![signup](assets/1.webp)

Na **Dashboardu** **Veřejného bazénu** máte stále nějaké statistiky, jako je celkový **hashrate** bazénu, stejně jako rozdělení různých typů minerů, které jsou k bazénu připojeny.

![signup](assets/2.webp)

V prvních několika řádcích můžeme vidět **Bitaxe** s 1323 připojenými **Bitaxe** pro celkový hashrate 649TH/s. **Bitaxe** je **Open source** projekt, který umožňuje jednoduché znovupoužití čipu z **[ASIC](https://planb.academy/resources/glossary/asic)** jako je **Antminer S19** na **opensource** elektronické desce, aby se vytvořil malý miner o výkonu 0.5TH/s pro 15W. Tento miner použijeme jako příklad pro tento tutoriál.

## Přidání **Pracovníka** 👷‍♂️

![signup](assets/cover.webp)

Na vrcholu stránky můžete zkopírovat adresu bazénu **stratum+tcp://public-pool.io:21496**.

Dále do pole **uživatel** zadejte **Bitcoinovou** adresu, kterou vlastníte.

Pokud máte více minerů, můžete pro všechny zadat stejnou adresu, aby se jejich **hashraty** kombinovaly a zobrazovaly jako jeden miner. Můžete je také odlišit přidáním rozlišovacího jména pro každý. K tomu stačí po **Bitcoinové** adrese přidat **.workername**.

Nakonec pro pole **heslo** použijte **‘x’**.

Příklad: Pokud je vaše **Bitcoinová** adresa **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** a chcete pojmenovat svůj miner **« Brrrr »**, pak byste do rozhraní vašeho mineru zadali následující informace:

- **URL**: stratum+tcp://public-pool.io:21496
- **UŽIVATEL**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Heslo**: **‘x’**
Pokud je váš miner **Bitaxe**, pole jsou trochu jiná, ale informace zůstávají stejné:
- **URL**: public-pool.io (zde musíte odstranit část na začátku **‘stratum+tcp://’** a část na konci **‘:21496’**, která bude uvedena v poli port)
- **Port**: 21496
- **Uživatel**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Heslo**: **‘x’**

![signup](assets/3.webp)
Několik minut po zahájení těžby uvidíte svá data na webové stránce **Public Pool** vyhledáním vaší adresy.
## Dashboard

![signup](assets/4.webp)

Jakmile se připojíte k **Public Pool**, můžete přistupovat k vašemu **Dashboardu** vyhledáním pomocí vaší **Bitcoin** adresy, kterou jste zadali do pole **Uživatel**. V našem případě je to **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

Na **Dashboardu** se zobrazují různé informace jak o vašich datech, tak o síti.

![signup](assets/5.webp)

Máte zde **Network Hash Rate**, což odpovídá celkové pracovní síle **Bitcoin** sítě.

**Network [Difficulty](https://planb.academy/resources/glossary/difficulty)** ukazuje obtížnost, která musí být dosažena pro validaci bloku.

A **Your Best Difficulty** je nejvyšší obtížnost, kterou jste dosáhli. Pokud se vám náhodou 🍀 podaří dosáhnout obtížnosti sítě, pak vyhráváte celou odměnu za blok... po 100 blocích. Museli byste počkat 100 bloků, než byste je mohli utratit.

Máte zde také **Block Height**, což je číslo posledního vytěženého bloku, stejně jako jeho váha vyjádřená ve WU, maximální je 4,000,000.

Níže můžete vidět statistiky každého z vašich zařízení individuálně, pokud jste jim dali rozlišovací název přidáním **.name** za vaši **Bitcoin** adresu v poli **Uživatel**.