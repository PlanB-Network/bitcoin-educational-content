---
name: Ocean Mining
description: Úvod do těžby v oceánu
---

![signup](assets/cover.webp)

**Květen 2024**

Těžba v oceánu je poněkud jedinečný těžební pool. Zde nejsou vyžadovány žádné účty, žádné emailové adresy, žádná hesla. Stejně jako u Bitcoinu, vše je transparentní, pseudonymní a přispěvatelé si mohou vybrat ze čtyř různých šablon bloků.

### Systém odměn

Systém odměn v Oceanu se nazývá TIDES, "Transparentní index rozlišených rozšířených podílů". Tento systém zaznamenává práci poskytnutou horníky, známou jako "podíly". Pool vypočítá procento "podílů" pro každého přispěvatele, poté přidá jejich Bitcoinovou adresu do šablony bloku poolu jako příjemce tohoto procenta odměny za blok.

Šablona bloku se aktualizuje přibližně každých 10 sekund, aby zohlednila nejvýnosnější nové transakce a v případě potřeby změnila rozdělení odměny za blok.

![signup](assets/rem.webp)

Nemá význam, zda jsou vaše stroje v době, kdy pool těží nový blok, připojeny či ne. Již odeslaná práce se uchovává pro dalších osm bloků nalezených poolem.

Uchování práce pro osm bloků místo resetování čítačů na nulu s každým nově vytěženým blokem znamená, že vaše odměna bude 100% pouze tehdy, pokud pool najde osm bloků poté, co jste začali přispívat. To také znamená, že budete nadále odměňováni za osm bloků, pokud přestanete přispívat do poolu.

Tento mechanismus vyrovnává odměny a odrazuje od "skákání mezi pooly", což zahrnuje pravidelné přepínání poolů v závislosti na tom, který má největší šanci najít další blok.

### Výběry

Provoz těžby v Oceanu umožňuje jeho přispěvatelům získat "čisté" bitcoiny, což znamená bitcoiny, které jsou přímo vydány odměnou za blok.

Na rozdíl od většiny ostatních poolů Ocean nepřijímá nově vytěžené bitcoiny; adresy přispěvatelů jsou přímo integrovány do šablony bloku.

Prozatím je minimální částka pro skutečné využití čistých bitcoinů 1,048,576 sats. S každým blokem vytěženým poolem musí váš podíl "podílů" opravňovat k více než 1,048,576 sats, aby vám byly tyto sats přímo vyplaceny odměnou za blok.
V opačném případě Ocean uchová vaše sats, dokud celkové odměny nepřesáhnou tuto částku.

Všechny bitcoiny dočasně uchovávané Oceanem jsou na této adrese: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, vše je ověřitelné na TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Je také možné vybrat vaše sats prostřednictvím Lightning pomocí BOLT12. Podíváme se, jak to nastavit.

### Poplatky za pool

Poplatky se pohybují od 0% do 2% v závislosti na vybrané šabloně bloku.

## Transparentnost Oceanu

### Data přispěvatelů

![signup](assets/1.webp)

Všechny informace o poolu jsou transparentní, včetně všech uživatelských dat. Abychom tento bod pochopili, vezměme si příklad:

[Na dashboardu Oceanu](https://ocean.xyz/dashboard) máte mnoho informací, jako je hashrate za posledních šest měsíců, počet účastníků v poolu, celkový počet vytěžených bitcoinů atd.

Zaměříme se na sekci "Přispěvatelé". Můžete vidět seznam všech přispěvatelů s jejich průměrným hashratem za poslední tři hodiny, stejně jako procento **"podílů"** a **"hash"** ve vztahu k zbytku poolu.
**"Podíl %"** je procento práce poskytnuté přispěvatelem v okně posledních osmi bloků ve srovnání se zbytkem poolu.
**"Hash %"** je procento průměrného hashrate poskytnutého přispěvatelem za poslední tři hodiny ve srovnání se zbytkem poolu.

![signup](assets/2.webp)

Všimnete si, že "Přispěvatelé" jsou identifikováni Bitcoinovou adresou. Na kteroukoli z těchto adres můžete kliknout pro více detailů.

Pokud vezmeme tu první, tu s nejvyšším hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), můžete vidět všechny detaily o tomto uživateli: hashrate, počet vyminovaných bitcoinů, s kterým blokem, a dokonce i detaily každého z jejich strojů (ASICs). Přesto zůstávají anonymní, jako na Bitcoinu.

### Šablona Bloku

V levém horním rohu na dashboardu máte "Další blok". Na této stránce jsou čtyři různé šablony bloků. Ocean umožňuje každému přispěvateli vybrat si šablonu bloku, kterou chtějí podporovat. To nemá přímý dopad na vaši odměnu. Když pool vyminuje blok, všichni přispěvatelé jsou odměněni bez ohledu na šablonu, kterou si vybrali. To jednoduše umožňuje každému "hlasovat" pro šablonu bloku, která jim vyhovuje.

![signup](assets/3.webp)

**CORE:** Poplatek 2%, to je klasická šablona Bitcoin Core bez filtru, jak je napsáno na jejich stránce "Zahrnuje transakce a většinu spamu"

**CORE+ANTISPAM:** Poplatek 0%, Bitcoin Core s filtrem proti určitým transakcím jako Ordinals "Zahrnuje transakce a omezuje spam"

**OCEAN:** Poplatek 0%, Bitcoin Knot "Zahrnuje pouze transakce a rozumně malá data"

**DATA-FREE:** Poplatek 0%, Bitcoin Knot "Zahrnuje pouze transakce bez jakýchkoli libovolných dat"

### Rozlišení mezi Bitcoin Core a Bitcoin Knot
Bitcoin Core je software, který umožňuje asi 99% uzlů Bitcoinu po celém světě fungovat. Bitcoin je protokol, což znamená, že stejně jako na internetu, kde existuje více prohlížečů, může na stejném TimeChainu koexistovat několik různých softwarových programů. Avšak z obav o kompatibilitu a omezení rizika chyb, které by zanechaly nevymazatelné stopy na TimeChainu, téměř všichni vývojáři Bitcoinu pracují na Bitcoin Core. Bitcoin Knots je fork Bitcoin Core, což znamená, že sdílí většinu jejich kódu, což velmi omezuje riziko chyb. Tento fork vytvořil Luke Dashjr, který chtěl aplikovat přísnější pravidla než Bitcoin Core bez vytváření hard forku. Nyní Bitcoin Core a Bitcoin Knots koexistují díky konsenzu Nakamoto.

## Přidání Pracovníka

Pro přidání pracovníka začněte výběrem šablony bloku. Tento výběr určí URL poolu, kterou zadáte do vašeho těžaře (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Dále, do pole uživatele, zadejte Bitcoinovou adresu, kterou vlastníte. Zde je seznam kompatibilních typů adres:
- **P2PKH** (Původní typ adresy. Začíná na “1”)
- **P2SH** (Multisignatura nebo P2SH-Segwit. Začíná na "3")- **Bech32** (Segwit. Začíná na "bc".)
- **Bech32m** (Taproot. Začíná na "bc". Delší než Bech32.)

Pokud máte více těžařů, můžete pro všechny zadat stejnou adresu, takže jejich hash rate budou kombinovány a zobrazí se jako jeden těžař. Můžete je také rozlišit přidáním jedinečného jména každému. K tomu stačí přidat ".workername" za Bitcoinovou adresu.

Nakonec pro pole hesla použijte `x`.

**Příklad:**
Pokud si vyberete šablonu **OCEAN**, vaše Bitcoinová adresa je `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` a přejete si pojmenovat svého těžaře "Brrrr", pak budete muset zadat následující informace do rozhraní vašeho těžaře:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **UŽIVATEL**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **HESLO**: `x`

Několik minut po zahájení těžby uvidíte svá data na stránkách Oceanu vyhledáním vaší adresy.

### Přehled dashboardu
- **Podíly v okně odměn**: Tato data ukazují počet podílů, práci, kterou jste poslali do poolu v okně posledních 8 bloků těžených poolem.
- **Odhadované odměny v okně**: Odhad počtu satoshi, které vyděláte za již odvedenou práci. Nezahrnuje poplatky za transakce, pouze coinbase, nové bitcoiny vydané sítí.
- **Odhadované výdělky příští blok**: Odhad počtu satoshi vydělaných, pokud by blok byl těžen nyní. Pamatujte, pokud je tato hodnota menší než 1,048,576 satoshi, satoshi přímo nedostanete na svou adresu. Budou poslány na adresu Oceanu, dokud vaše výdělky nepřekročí tento práh.

Níže máte graf zobrazující historii vašeho hash rate až 6 měsíců.

![signup](assets/4.webp)

Zde máte váš průměrný hash rate v různých časových škálách, od 60s do 24h, stejně jako historii bloků těžených poolem, za které jste přispěli a byli odměněni.

![signup](assets/5.webp)

Máte možnost exportovat soubor CSV této historie pomocí tlačítka **Download CSV**.

![signup](assets/6.webp)

V následující sekci máte seznam všech těžařů, které jste připojili k poolu s touto adresou. Samozřejmě máte jejich individuální hash rate, ale také počet satoshi, které každý z nich individuálně obdržel za svou práci.

![signup](assets/7.webp)

Můžete kliknout na **Přezdívku** jakéhokoli těžaře. Poté uvidíte všechny informace, které jsme právě viděli, ale konkrétně pro tohoto těžaře.

A na konci stránky některé další informace, kde můžete vidět historii plateb na vaší adrese, satoshi, které jste vytěžili, ale ještě nebyly vyplaceny, a celkový počet satoshi, které jste vytěžili.

![signup](assets/8.webp)

Zde můžete vidět, že v boxu **Odhadovaný čas do minimální výplaty** je napsáno Lightning, protože jsme nastavili nabídku BOLT12.

### Nastavení výběrů přes Lightning
Jak jste pochopili, Ocean si klade za cíl maximalizovat transparentnost a minimalizovat držení (držení vašich satoshi za vás).
Proto je pro výběry přes Lightning nutné používat **BOLT12 nabídky**. Jedná se o nový způsob platby v síti Lightning, který začíná v roce 2024 nabývat na významu a umožňuje několik věcí:
- Je to opakovaně použitelný platební odkaz, který umožňuje automatické platby a na rozdíl od Lightning adresy je BOLT12 nezákonný.
- Je to také platební metoda, která poskytuje důkaz o provedení platby, což u LNURL není možné.
- Velmi důležité je, že lze použít ve spojení s podpisem Bitcoinu, aby se prokázalo, že jste držitelem BTC adresy i nabídky BOLT12.
K dnešnímu dni (květen 2024) existuje málo řešení, jak tuto metodu použít. V tomto příkladu použijeme server Start9 s Core Lightning. Když další nástroje, jako například Phoenix Wallet, integrují nabídky BOLT12, tento tutoriál zůstane použitelný. Ujistěte se, že máte otevřené kanály s příchozí likviditou, jinak platby nebudou fungovat.

Začněte tím, že na stránce Ocean přejdete na svůj dashboard zadáním vaší BTC adresy, poté klikněte na záložku **Konfigurace**.

![signup](assets/9.webp)

Zkopírujeme text **Popis**, zde:
`OCEAN Výplaty pro bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Nyní přejděte na rozhraní Core Lightning na vašem serveru Start9 (nebo jakékoli peněžence schopné poskytnout nabídku BOLT12).

![signup](assets/10.webp)

Klikněte na **Přijmout**.

Zaškrtněte **Nabídka**, poté vložte dříve zkopírovaný text do pole **Popis** a pole **Částka** nechte prázdné.

![signup](assets/11.webp)

Klikněte na **Generovat nabídku**.

![signup](assets/12.webp)

Vygenerovali jste opakovaně použitelný a trvalý platební odkaz, který nevyžaduje centrální server, jak je tomu u Lightning adres. Zkopírujte odkaz a poté se vraťte na stránku Ocean.

Do pole **Lightning BOLT12 Nabídka** vložte platební odkaz a pole **Výška bloku** nechte na výchozí hodnotě. Klikněte na **GENERATE**.

![signup](assets/13.webp)

Aby Ocean mohl ověřit, že tento platební odkaz je skutečně váš bez použití systému účtů, budete muset podepsat právě vygenerovanou zprávu svým soukromým klíčem odpovídajícím Bitcoinové adrese, kterou používáte. Existuje mnoho řešení, jak zprávu podepsat vaším soukromým klíčem. V tomto tutoriálu vezmeme jako příklad BlueWallet, ale metoda je stejná pro všechny peněženky.

![signup](assets/14.webp)

Předpokládáme, že váš soukromý klíč je v BlueWallet (můžete udělat totéž s hardware peněženkou), klikněte na příslušnou peněženku.

![signup](assets/15.webp)

Poté na **…** v pravém horním rohu.

![signup](assets/15bis.webp)

A **Podepsat/Ověřit zprávu**.

![signup](assets/16.webp)

V tomto okně máte tři pole: **Adresa**, **Podpis** a **Zpráva**.

Do pole **Adresa** zadejte vaši Bitcoinovou adresu. Pokud se vrátíme k našemu příkladu, je to adresa: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Pole **Podpis** nechte prázdné.
A vložte vygenerovanou zprávu do pole **Zpráva** na stránce Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klikněte na **Podepsat**.

Tím se vygeneruje kryptografický podpis, který dokazuje, že jste majitelem adresy `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, a tento podpis je jedinečný díky zprávě poskytnuté Oceanem, generované z platebního odkazu BOLT12.

![signup](assets/17.webp)

Zkopírujte podpis a vložte ho na stránku Ocean, poté klikněte na **POTVRDIT**.

![signup](assets/18.webp)

Měli byste vidět potvrzovací zprávu.

![signup](assets/19.webp)

Nyní přejděte na záložku **Moje statistiky**. Na vrchu se zobrazí další informace s platebním odkazem BOLT12, který jste dříve vygenerovali s Core Lightning na Start9.

![signup](assets/20.webp)