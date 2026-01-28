---
name: Blockstream Explorer
description: Prozkoumejte hlavní vrstvu Bitcoin a Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer je projekt, který usnadňuje zkoumání transakcí a globálního stavu protokolu Bitcoin, jakož i [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid vyvinutého společností Blockstream.



Cílem průzkumníka [blockstream.info](https://blockstream.info), který v roce 2014 iniciovala společnost Blockstream založená Adamem Backem, je poskytnout robustní infrastrukturu pro Bitcoin, zaručit interoperabilitu a sledování transakcí mezi vrstvami (on-chain a Liquid) a zároveň zvýšit bezpečnost a soukromí uživatelů.



V tomto tutoriálu se podíváme na to, čím se liší, jaké jsou jeho služby a jak nabízí bezproblémové sledování provozu a stavu vrstev Bitcoin on-chain a Liquid.



## Začínáme s průzkumníkem Blockstream



### Navigace v hlavním kanálu



Když přejdete do průzkumníka Blockstream.info, na "**Panel**" je ve výchozím nastavení vybrán hlavní řetězec protokolu Bitcoin. V tomto rozhraní máte přehled o :





- Velikost hlavního řetězu: Nedávno vytěžené bloky.



![blocks](assets/fr/01.webp)



Tato část obsahuje informace o posledních vytěžených blocích, časové razítko, počet transakcí obsažených v každém bloku, velikost v kilobajtech (kB) a měření každého bloku v jednotkách hmotnosti (**WU** = *Weight Units*). Toto poslední měření je zajímavé, protože nám umožňuje vyhodnotit optimalizaci bloku, vzhledem k tomu, že každý blok hlavního řetězce je omezen na `4 000 000 WU` neboli `4 000 kWU`.





- Nedávné transakce.



![transactions](assets/fr/02.webp)



Sekce transakce poskytuje informace o jedinečném identifikátoru transakce, hodnotě bitcoinu, velikosti ve virtuálních bajtech (vB), která představuje součet všech dat (vstupních a výstupních), a související sazbě poplatku. Například za transakci o velikosti `153 vB` se sazbou `2 sat/vB` bude účtován poplatek `306 satoshis`.



### Průzkum tekutin



V nabídce "**Bloky**" můžete sledovat historii celého hlavního řetězce až k poslednímu vytěženému bloku.



![blocs](assets/fr/03.webp)



Kliknutím na konkrétní blok můžete získat podrobnější informace o informacích a transakcích v něm obsažených. Například u bloku 919330: zobrazí se hash bloku. Můžete také přejít na předchozí blok, protože každý vytěžený blok (kromě Genesis) je propojen s předchozím a zachovává hash svého předchůdce.



![metadata](assets/fr/04.webp)



Kliknutím na tlačítko **"Podrobnosti "** můžete získat další informace o tomto bloku, například jeho stav, který potvrzuje, že byl přidán do zachovaného a propagovaného hlavního řetězce. K dispozici máte také obtížnost, s jakou je tento blok těžen: tato obtížnost představuje výpočetní výkon potřebný k vyřešení kryptografického problému mining a upravuje se každých 2016 bloků (přibližně 2 týdny).



![details](assets/fr/05.webp)



Pod tímto oddílem s podrobnostmi nalezneme všechny transakce zahrnuté do tohoto bloku.



Úplně první transakce v bloku se nazývá **transakce coinbase**. Používá se k přidělení odměny těžaře mining (všechny poplatky spojené s transakcemi zahrnutými v bloku a dotace bloku). Bitcoiny vytvořené touto transakcí lze utratit až po vytěžení dalších 100 po sobě jdoucích bloků. Jinými slovy, aby je těžař mohl použít, bude muset počkat na vytvoření bloku **919430**. Tomu se říká [*"doba splatnosti "*](https://planb.academy/fr/resources/glossary/maturity-period).



Transakce coinbase je zvláštní: jako jediná nemá žádný skutečný vstup, protože se při ní neutrácejí žádné bitcoiny z předchozí transakce.




![coinbase](assets/fr/06.webp)



Všechny ostatní transakce jsou rozděleny do dvou částí: vstupy a výstupy.



Aby mohly být bitcoiny použity jako vstupy v nové transakci, musí iniciátor transakce prokázat své vlastnictví podpisem, který odpovídá určitému skriptu. Každý kus bitcoinu (UTXO) obsahuje skript obecně vyžadující specifický podpis, který může poskytnout pouze soukromý klíč držitele. Tyto skripty se nazývají ***scriptSig*** (v ASM), jsou napsány v jazyce Bitcoin Script a mohou být různých typů. V tomto příkladu vidíme, že použité UTXO byly typu P2SH na výstup typu P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Pomocí heuristiky můžete sledovat historii konkrétního modelu UTXO. Zveme vás k objevování různých heuristik Bitcoin a způsobů, jak posílit důvěrnost vašich transakcí na Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Vezměme si příklad výdajů této transakce. Kliknutím na identifikátor transakce jsme přesměrováni do sekce **Transakce** na stránce s podrobnostmi o transakci.



![transaction](assets/fr/08.webp)



Na této stránce můžete zjistit, do kterého bloku byla transakce zařazena. V závislosti na typu použité adresy může transakce optimalizovat svá data (*virtuální bajty*), a tudíž platit nižší transakční poplatky. Tato transakce například ušetřila 53 % poplatků tím, že použila nativní formát adresy SegWit Bech32 začínající na `bc1q`.



![trx_details](assets/fr/09.webp)



## Vrstva Liquid



Liquid Network je [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) a open source řešení úrovně 2 pro protokol Bitcoin. Umožňuje zejména rychlejší a důvěrnější bitcoinové transakce.



V průzkumníku Blockstream.info klikněte na tlačítko **"Liquid"** a přepněte se do sítě Liquid.



![liquid](assets/fr/10.webp)



Po kliknutí na jednu z transakcí, kterou chceme sledovat, vidíme, že částky v bitcoinech jsou nahrazeny slovy "**Důvěrné**". V této síti mohou být transakce důvěrné, takže nemůžeme vidět částky jednotlivých UTXO, ať už v transakci nebo mimo ni.



![liquid_trx](assets/fr/11.webp)



Podotýkáme však, že principy a mechanismy přítomné na hlavní vrstvě protokolu Bitcoin jsou stejné: bitcoinové zamykací skripty a sledovatelnost UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network poskytuje také nedepozitní digitální aktiva, která mohou organizace využívat. V nabídce **"Aktiva "** najdete seznam registrovaných aktiv, jejich celkový počet a doménu, ke které se vztahují.



![assets](assets/fr/13.webp)



Pro každé aktivum můžete sledovat historii transakcí emise a spálení (smazání celkového množství v oběhu).



![assets_trxs](assets/fr/14.webp)




## Další možnosti



Průzkumník Blockstream.info zahrnuje také vizualizace a sledování transakcí na Testnet, Bitcoin, on-chain a Liquid Network.



![testnet](assets/fr/15.webp)



Když přejdete do sítě Testnet, nepoužíváte skutečné bitcoiny, ale máte k dispozici všechny výše popsané funkce.



![liquid_testnet](assets/fr/16.webp)



Tato síť je vybavena různě dlouhým řetězem, ke kterému můžete připojit a otestovat fungování mechanismů Bitcoin a Liquid.





- Sekce API je určena všem, kteří chtějí integrovat určité funkce Průzkumníka do své vlastní aplikace. Prostřednictvím této části API můžete dotazovat hlavní řetězec různých vrstev (on-chain a Liquid), sledovat transakce a zjistit například průměrné poplatky za transakce v bloku.



![api](assets/fr/17.webp)



Nyní jste připraveni využít plný potenciál aplikace Blockstream Explorer pro dotazování na blockchainy na vrstvách on-chain a Liquid. Doufáme, že pro vás byl tento návod poučný, a doporučujeme vám náš návod na jiný průzkumník Bitcoin:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f