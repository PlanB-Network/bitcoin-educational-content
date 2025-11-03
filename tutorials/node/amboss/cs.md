---
name: Amboss
description: Prozkoumejte a analyzujte Lightning Network
---

![cover](assets/cover.webp)



Lightning Network je Layer protokolu Bitcoin, který byl primárně vyvinut na podporu přijetí plateb Bitcoin na každodenní bázi zvýšením rychlosti zpracování každé transakce. Protokol Lightning Network je založen na principu decentralizace a skládá se z uzlů (počítačů s implementací Lightning), které komunikují peer-to-peer a vzájemně si předávají data (platby a ověření plateb).



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Stejně jako v hlavním řetězci je i zde nezbytné umožnit uživatelům znát informace a stav sítě, aby se usnadnilo propojení mezi uzly a minimalizoval problém s likviditou, který v síti obecně vzniká. Na Lightning Network skutečně doporučujeme mikroplatby v relativně menších částkách než u transakcí na hlavním řetězci Bitcoin.



Je důležité poznamenat, že ne všechny uzly Lightning jsou na platformě Amboss k dispozici.



Stejně jako [Mempool Space](https://Mempool.space), který poskytuje užitečné informace o hlavním řetězci protokolu Bitcoin, poskytuje od roku 2022 [Amboss](https://amboss.space) informace o :





- Uzly na Lightning Network
- Platební kanály a jejich platební kapacita
- Vývoj Lightning Network v čase
- Statistiky poplatků za vaše platby v přenosových uzlech.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

V tomto návodu vás provedeme touto platformou, která je základním zdrojem informací pro uživatele Lightning Network, pro ty, kteří chtějí připojit svůj uzel a rozšířit tak síť atd.




## Najít dvojice



Jedním z cílů platformy Amboss je umožnit různým uzlům v síti propojit se a vzájemně si předávat informace. Na domovské stránce platformy můžete přímo vyhledat jméno uzlu, který již znáte, nebo najít uzly z nejoblíbenějších portfolií Lightning, které používáte.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Na domovské stránce najdete také uzly rozdělené podle :




- Vývoj kapacity: množství Bitcoin spojené s veřejným klíčem uzlu a celkové množství dostupné ve všech jeho kanálech.
- Vývoj kanálů: počet nových spojení s jinými uzly v síti.
- Oblíbenost uzlu: jak často je uzel používán.



![nodes](assets/fr/03.webp)



Výběr správného uzlu, ke kterému se chcete připojit, proto spočívá v ověření následujících kritérií:





- Ujistěte se, že uzel má dostatečné množství bitcoinů; čím větší je kapacita uzlu, tím větší množství bitcoinů můžete zaplatit.





- Zajistěte, aby měl uzel velký počet připojení a otevřených kanálů s ostatními uzly v síti.





- Zkontrolujte, zda je uzel aktivní a zda si ho jeho kolegové stále váží, a to tak, že zkontrolujete počet nových kanálů; čím více nových kanálů má uzel otevřených, tím více si ho ostatní uzly v síti váží.



Jakmile najdete správný uzel, klikněte na jeho název a budete přesměrováni na stránku s informacemi o uzlu.



Na tomto kanálu Interface získáte kontrolou kanálu Timestamp nově vytvořeného kanálu informaci o aktivitě tohoto uzlu. Najdete zde také informaci o kapacitě kanálů tohoto uzlu: tato informace je zásadní, pokud chcete tento uzel aktivně využívat k provádění plateb.




![node_info](assets/fr/04.webp)



V levé části najdete další podrobnosti o umístění tohoto uzlu. Můžete si například zobrazit :




- Veřejný klíč: identifikátor hned pod názvem uzlu.
- Zeměpisná poloha tohoto uzlu.




![channels](assets/fr/05.webp)



Tento údaj Interface udává připojení Address pro tento uzel: má tvar `pubkey@ip:port`. V našem příkladu se chceme připojit k uzlu, jehož :




- veřejný klíč `pubkey` je: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Přístav: `9735`



![geoinfo](assets/fr/06.webp)



V části **Kanály** se zobrazí seznam otevřených kanálů a připojení uzlu k ostatním uzlům v síti. Na této stránce Interface je několik informací, které jsou zásadní pro potvrzení, že tento uzel odpovídá našim potřebám nebo je spolehlivý:





- Příchozí poměr**: V závislosti na zvoleném kanálu vám uzel naúčtuje poplatek za každý milion přijatých Satoshi.
- Poměr (parts per million)** : který představuje počet Satoshi na milion jednotek, které vám uzel naúčtuje, když se rozhodnete provést platbu prostřednictvím některého z jeho kanálů. Řekněme, že se rozhodnete provést platbu ve výši `10_000 Sats` prostřednictvím kanálu, jehož poměr ppm je `500 Sats`, budete muset uzlu zaplatit `10_000 * 500 / 1_000_000` satošů, což odpovídá `5 Sats`.
- Maximální hodnota [HTLC](https://planb.academy/resources/glossary/htlc)** : Maximální částka, kterou tento uzel umožňuje tranzit jedním z těchto kanálů.



Nahlédnutím do tabulky v tomto dokumentu Interface můžete všechny tyto informace zjistit také o uzlu, ke kterému je přiřazen.



![channels_info](assets/fr/07.webp)



V části **Mapy kanálů** můžete zobrazit rozložení a kapacitu různých kanálů v tomto uzlu. Zobrazená kritéria distribuce můžete změnit výběrem jedné z možností v rozevíracím seznamu vpravo.



![cha_maps](assets/fr/08.webp)



Sekce **Uzavřené kanály** seskupuje všechny bývalé kanály uzlu podle typu uzávěru:




- Vzájemné uzavření**: představuje dohodu obou stran, které pomocí svých soukromých klíčů podepíší transakci označující uzavření kanálu a rozdělení zůstatků v něm
- **vynucený uzávěr**: představuje náhlé, jednostranné uzavření jedné části kanálu. Tento typ uzavření se nedoporučuje, protože protokol Lightning Network je založen na trestech: při pokusu o zpronevěru zůstatku kanálu riskujete ztrátu veškerého dostupného zůstatku v daném kanálu.



![closed](assets/fr/09.webp)



Získejte informace o tranzitních poplatcích za směrování plateb přes kanál v uzlu, který používáte



![fees](assets/fr/10.webp)



## Informace o síti



Amboss se zaměřuje nejen na informace o členech sítě, ale také na stav samotné sítě.



V části **Statistika** v levém menu "Simulace" najdete graf, který zobrazuje pravděpodobnost úspěšné platby v závislosti na výši platby.



Ve skutečnosti si všimnete, že křivka klesá, protože s rostoucí výší platby máte menší šanci, že platba proběhne. To odráží skutečný problém s likviditou na Lightning Network. Například vaše platba ve výši `10_000` satošů má `79%` šanci, že bude provedena. Na druhou stranu u platby ve výši `3_000_000` satošů máte méně než `13%` šanci na úspěch.



![network](assets/fr/11.webp)



Nabídka **Síťové statistiky** umožňuje graficky zobrazit statistiky pro :




- Platební kanály
- Uzly
- Kapacita
- Poplatky
- Vývoj kanálu.



![network_stat](assets/fr/12.webp)



V nabídce **Statistiky trhu** umožňuje možnost **Detaily objednávky** zobrazit poptávku po likviditě na Lightning Network. Tento graf může také ukázat, po kterých kanálech je největší poptávka a/nebo které mají značnou kapacitu.



![markets](assets/fr/13.webp)




## Nástroje



Společnost Amboss nabízí řadu nástrojů, které vám pomohou optimalizovat vyhledávání a akce.



### Dekodér Lightning Network



Tento nástroj je zodpovědný především za poskytnutí podrobností o struktuře blesku Invoice, blesku Address nebo blesku URL.



Na domovské stránce v části **Nástroje** odešlete například svůj blesk Address.



![decoder](assets/fr/14.webp)



Z tohoto dekodéru můžete získat informace jako :




- veřejný klíč uzlu spojený s vaším bleskem Address;
- Doba vypršení platnosti karty Invoice z vaší karty Address;
- Minimální a maximální počet, který můžete odeslat;
- Uzel Nostr přidružený k vašemu Address, pokud je v tomto uzlu povolen Nostr.



![decode](assets/fr/15.webp)



### Magma IA



Seznamte se s nejnovějším nástrojem společnosti Amboss pro efektivní správu připojení k uzlům Lightning Network. Magma AI využívá specializovanou umělou inteligenci, která se zaměřuje na důležitý problém: správný výběr uzlů pro připojení.



![magma](assets/fr/16.webp)



### Kalkulačka Satoshi



Zjistěte aktuální cenu produktu Bitcoin ve vaší místní měně (EUR / USD). Na domovské stránce použijte kalkulačku satoši a zjistěte aktuální tržní cenu.



![calculator](assets/fr/17.webp)




Nyní jste se seznámili s kompletními funkcemi a analytickými nástroji platformy. Níže naleznete náš článek o průzkumníku Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f