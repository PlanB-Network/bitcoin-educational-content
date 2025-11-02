---
name: BLOCKSTREAM Explorer
description: Prozkoumejte hlavní Layer Bitcoin a Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer je projekt, který usnadňuje zkoumání transakcí a Global State protokolu Bitcoin, jakož i [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid vyvinutého společností BLOCKSTREAM.



Cílem průzkumníka [BLOCKSTREAM.info](https://BLOCKSTREAM.info), který v roce 2014 iniciovala společnost BLOCKSTREAM založená Adamem Backem, je poskytnout robustní infrastrukturu pro Bitcoin, zaručit interoperabilitu a sledování transakcí mezi vrstvami (On-Chain a Liquid) a zároveň zvýšit bezpečnost a soukromí uživatelů.



V tomto tutoriálu představíme, čím se liší, jaké jsou jeho služby a jak nabízí bezproblémové sledování provozu a stavu vrstev Bitcoin On-Chain a Liquid.



## Začínáme s BLOCKSTREAM



### Navigace v hlavním kanálu



Když přejdete do průzkumníka BLOCKSTREAM.info na "**Panel**", je ve výchozím nastavení vybrán hlavní kanál protokolu Bitcoin. Z tohoto kanálu Interface máte přehled o :





- Velikost hlavního řetězu: Nedávno vytěžené bloky.



![blocks](assets/fr/01.webp)



Tato část obsahuje informace o nedávno vytěžených blocích, Timestamp, počtu transakcí zahrnutých v každém BLOCK, velikosti v kilobajtech (kB) a měření každého BLOCK v jednotkách hmotnosti (**WU** = *Weight Units*). Toto poslední měření je zajímavé, protože nám umožňuje vyhodnotit optimalizaci BLOCK, vzhledem k tomu, že každý BLOCK hlavního řetězce je omezen na `4 000 000 WU` neboli `4 000 kWU`.





- Nedávné transakce.



![transactions](assets/fr/02.webp)



Sekce transakce poskytuje informace o jedinečném identifikátoru transakce, příslušné hodnotě Bitcoin, velikosti ve virtuálních bajtech (vB), která představuje součet všech dat (vstupních a výstupních), a související sazbě poplatku. Například transakce o velikosti `153 vB` se sazbou `2 sat/vB` bude zpoplatněna částkou `306 satoshis`.



### Průzkum tekutin



V nabídce "**Bloky**" můžete sledovat historii celého hlavního řetězce až k poslednímu vytěženému bloku BLOCK.



![blocs](assets/fr/03.webp)



Kliknutím na konkrétní položku BLOCK získáte podrobnější informace o informacích a transakcích, které jsou v ní obsaženy. Například pro BLOCK 919330: máte k dispozici Hash z BLOCK. Můžete také přejít na předchozí BLOCK, protože každý vytěžený BLOCK (kromě Genesis) je propojen s předchozím a zachovává si Hash svého předchůdce.



![metadata](assets/fr/04.webp)



Kliknutím na tlačítko **"Podrobnosti "** získáte další informace o tomto BLOCK, například jeho stav, který potvrzuje, že byl přidán do zachovaného a propagovaného hlavního řetězce. K dispozici máte také obtížnost, s jakou je tento BLOCK těžen: tato obtížnost představuje výpočetní výkon potřebný k vyřešení kryptografického problému Mining a upravuje se každých 2016 bloků (přibližně 2 týdny).



![details](assets/fr/05.webp)



Pod tímto oddílem s podrobnostmi nalezneme všechny transakce zahrnuté v tomto BLOCK.



Úplně první transakce v BLOCK se nazývá **transakce coinbase**. Používá se k přidělení odměny Miner za Mining (všechny poplatky spojené s transakcemi zahrnutými v grantu BLOCK a BLOCK). Bitcoiny vytvořené touto transakcí lze utratit až po vytěžení dalších 100 po sobě jdoucích bloků. Jinými slovy, aby je bylo možné použít, bude muset Miner počkat na výrobu BLOCK **919430**. Tomu se říká [*"doba splatnosti "*](https://planb.network/fr/resources/glossary/maturity-period).



Transakce coinbase je zvláštní: jako jediná nemá žádný skutečný vstup, protože se při ní neutrácejí žádné bitcoiny z předchozí transakce.




![coinbase](assets/fr/06.webp)



Všechny ostatní transakce jsou rozděleny do dvou částí: vstupy a výstupy.



Aby mohly být bitcoiny použity jako vstupy v nové transakci, musí iniciátor transakce prokázat své vlastnictví podpisem, který odpovídá určitému skriptu. Každý kus bitcoinu (UTXO) obsahuje skript obecně vyžadující specifický podpis, který může poskytnout pouze soukromý klíč držitele. Tyto skripty se nazývají ***scriptSig*** (v ASM), jsou napsány v jazyce Bitcoin Script a mohou být různých typů. V tomto příkladu vidíme, že použité UTXO byly typu P2SH na výstup typu P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Pomocí heuristiky můžete sledovat historii konkrétního kódu UTXO. Zveme vás, abyste se seznámili s různými heuristikami Bitcoin a s tím, jak posílit důvěrnost vašich transakcí Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Vezměme si příklad výdajů této transakce. Kliknutím na identifikátor transakce jsme přesměrováni do sekce **Transakce** na stránce s podrobnostmi o transakci.



![transaction](assets/fr/08.webp)



Na této stránce můžete zjistit, do kterého z čísel BLOCK byla transakce zahrnuta. V závislosti na typu použitého Address může transakce optimalizovat svá data (*virtuální bajty*), a tudíž platit nižší transakční poplatky. Tato transakce například ušetřila 53 % poplatků použitím nativního formátu SegWit BECH32 Address začínajícího na `bc1q`.



![trx_details](assets/fr/09.webp)



## Povlak Liquid



Liquid Network je [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) a open source řešení 2. úrovně pro protokol Bitcoin. Umožňuje zejména rychlejší a důvěrnější transakce Bitcoin.



V průzkumníku BLOCKSTREAM.info klikněte na tlačítko **"Liquid"** a přepněte na Liquid Network.



![liquid](assets/fr/10.webp)



Po kliknutí na jednu z transakcí, kterou chceme sledovat, vidíme, že částky kusů Bitcoin jsou nahrazeny slovy "**Důvěrné**". V této síti mohou být transakce důvěrné, takže nemůžeme vidět částky jednotlivých kusů UTXO, a to ani v transakci, ani mimo ni.



![liquid_trx](assets/fr/11.webp)



Poznamenáváme však, že principy a mechanismy přítomné v hlavním Layer protokolu Bitcoin jsou stejné: zamykací skripty Bitcoin a sledovatelnost UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network poskytuje také nedepozitní digitální aktiva, která mohou organizace využívat. V nabídce **"Aktiva "** najdete seznam registrovaných aktiv, jejich celkový počet a doménu, ke které se vztahují.



![assets](assets/fr/13.webp)



Pro každé aktivum můžete sledovat historii transakcí emise a spálení (smazání celkového množství v oběhu).



![assets_trxs](assets/fr/14.webp)




## Další možnosti



Průzkumník BLOCKSTREAM.info zahrnuje také vizualizace a sledování transakcí na Testnet, Bitcoin, On-Chain a Liquid Network.



![testnet](assets/fr/15.webp)



Když přejdete do sítě Testnet, nepoužíváte skutečné bitcoiny, ale máte k dispozici všechny výše popsané funkce.



![liquid_testnet](assets/fr/16.webp)



Tato síť je vybavena různě dlouhým řetězem, ke kterému můžete připojit a otestovat fungování mechanismů Bitcoin a Liquid.





- Sekce API je určena všem, kteří chtějí do své vlastní aplikace integrovat určité funkce Exploreru. Prostřednictvím tohoto API můžete dotazovat hlavní řetězec různých vrstev (On-Chain a Liquid), sledovat transakce a zjistit například průměrné poplatky za transakce v BLOCK.



![api](assets/fr/17.webp)



Nyní jste připraveni využít plný potenciál aplikace BLOCKSTREAM Explorer k dotazování blokových řetězců na vrstvách On-Chain a Liquid. Doufáme, že pro vás byl tento návod poučný, a doporučujeme vám náš návod na další aplikaci Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f