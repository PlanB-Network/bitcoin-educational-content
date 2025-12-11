---
name: Bitfeed
description: Prozkoumejte hlavní řetězec protokolu Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed je platforma pro vizualizaci onchain vrstvy protokolu Bitcoin. Vznikla z iniciativy jednoho z přispěvatelů projektu Mempool.space a vyniká především svým minimalistickým vzhledem a snadným používáním.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

V tomto tutoriálu se podíváme na tento nástroj, který vám umožní prozkoumat všechny transakce a bloky v síti.



## Začínáme se službou Bitfeed



Bitfeed je platforma, která se zaměřuje na tři hlavní body:





- Konzultace Blockchain**,
- Vyhledávání transakcí**,
- Vizualizace mempoolu**.



### Konzultace s blockchainem



Na domovské stránce služby Bitfeed najdete především :





- Vyhledávací panel: Tato část je vstupním bodem pro dotazy týkající se blockchainu. Zde můžete vyhledat konkrétní blok podle jeho čísla nebo hashe. Můžete také vyhledávat konkrétní transakce a adresy Bitcoin, abyste si ověřili určité informace o transakcích v síti.



![searchBar](assets/fr/01.webp)



V levém horním rohu vidíte aktuální cenu bitcoinu odhadovanou v amerických dolarech (USD).



![price](assets/fr/02.webp)



Na pravém postranním panelu je nabídka platformy. V této nabídce si můžete přizpůsobit rozhraní platformy podle svých představ, přidávat nebo odebírat položky a upravovat filtry zobrazení. Můžete například zobrazit velikost každého bloku podle hodnoty nebo podle hmotnosti ve virtuálních bajtech (vBajtech).



![menu](assets/fr/03.webp)



Uprostřed stránky je poslední vytěžený blok se zobrazením všech transakcí zahrnutých v tomto bloku. Tato část poskytuje informace o časovém razítku, celkovém počtu bitcoinů zahrnutých do bloku, velikosti bloku v bajtech, počtu transakcí a průměrném poměru transakčních nákladů na virtuální bajt v bloku.



![block](assets/fr/04.webp)



Vyhledáním konkrétního bloku ve vyhledávacím řádku se můžete vrátit zpět do historie kanálu a zobrazit jej podle zadaných kritérií.



Chceme například zobrazit transakce v bloku `879488`.



![bloc](assets/fr/05.webp)



První transakce tohoto bloku představuje transakci **coinbase**, která těžaři tohoto bloku umožňuje získat odměnu mining, kterou lze utratit až po vytěžení 100 bloků, jež se skládá ze zahrnutých transakčních poplatků a blokového grantu. Právě tato transakce umožňuje vydávat v systému nové bitcoiny.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Ve výchozím nastavení jsou transakce v bloku reprezentovány podle dvou kritérií:




- Velikost, která se může lišit mezi hodnotou a váhou (vBajty) ;
- Barva se může lišit podle věku a poměru transakčních poplatků za virtuální bajt.



![options](assets/fr/07.webp)



Můžeme tedy konstatovat, že všechny transakce zahrnuté do stejného bloku mají v blockchainu stejný počet potvrzení. Největší kostky představují transakce obsahující nejvyšší množství bitcoinů.



Tento výklad dále potvrzuje možnost nabídky **"Info "**, která nás informuje o překladu barvy a velikosti transakcí bloku.



![infos](assets/fr/08.webp)



Můžete také zobrazit transakce bloku podle virtuálních bajtů a poměru poplatků. Toto zobrazení se může lišit od předchozího, protože hodnota bitcoinu obsažená v transakci neurčuje její velikost.



![visualisation](assets/fr/09.webp)



### Zobrazení transakcí



Transakci můžete vyhledat pomocí jejího identifikátoru na vyhledávacím panelu. Můžete také kliknout na kostku a zobrazit informace týkající se dané transakce.



V našem případě vezměme transakci, která zabírá největší místo v bloku `879488`.



![biggest](assets/fr/10.webp)



Uvidíte, že tato transakce má hodnotu `42 989`, která představuje rozdíl mezi posledním vytěženým blokem a námi vybraným blokem. Tato potvrzení pomáhají posílit bezpečnost sítě Bitcoin, protože k zákeřné změně této transakce by útočníci museli disponovat ekvivalentním výpočetním výkonem k přepsání celého hlavního řetězce bloků.



Velikost této transakce je `57 088 vBajtů`, zejména kvůli velkému počtu UTXO použitých při její konstrukci (842 záznamů). Překvapivě zůstává použitý poměr poplatků relativně nízký (pouze 4 sats/vByte) ve srovnání s celkovým průměrem bloku 5,82 sats/vByte.



Transakce, která zabírá nejvíce místa, proto nemusí být nutně transakcí s nejvyšším poměrem transakčních nákladů.



![transaction](assets/fr/11.webp)



Pokud sledujete stupnici v nabídce **Info**, je transakce s nejvyšším poměrem transakčních nákladů fialová. Jedná se o transakci [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) s poměrem transakčních nákladů `147,49 sats/vBajtech`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Vizualizace Mempool



Mempool je virtuální místo, kde jsou seskupeny transakce Bitcoin čekající na zařazení do bloku. Bitfeed umožňuje nahlížet do [mempool](https://planb.academy/resources/glossary/mempool) několika těžařů Bitcoin a nabízí tak širokou škálu sledování transakcí.



![mempool](assets/fr/13.webp)



V této části můžete sledovat všechny platné i dosud nepotvrzené transakce v hlavním řetězci sítě Bitcoin.



![unconfirmed](assets/fr/14.webp)



Nyní máte k dispozici průvodce používáním platformy Bitfeed k analýze bloků a transakcí, abyste mohli vizualizovat informace dostupné v hlavním řetězci sítě Bitcoin a zároveň využívat minimalistické a snadno použitelné rozhraní. Pokud se vám tento návod líbil, doporučujeme vám udělat další krok: objevte Lightning Network prostřednictvím projektu Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017