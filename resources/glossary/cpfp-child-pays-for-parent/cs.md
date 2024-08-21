---
term: CPFP (CHILD PAYS FOR PARENT)
---

Transakční mechanismus zaměřený na urychlení potvrzení Bitcoinové transakce, podobně jako to dělá Replace-by-Fee (RBF), ale ze strany příjemce. Když transakce s příliš nízkými poplatky ve srovnání s trhem uvízne v mempoolech uzlů a není dostatečně rychle potvrzena, může příjemce vytvořit novou transakci, která utratí bitcoiny přijaté v blokované transakci, ačkoli ještě není potvrzena. Tato druhá transakce nutně vyžaduje, aby byla první těžena a potvrzena. Těžaři jsou tak nuceni zahrnout obě transakce dohromady. Druhá transakce bude alokovat mnohem více na transakčních poplatcích než první, takovým způsobem, že průměrný poplatek motivuje těžaře zahrnout obě transakce. Dětská transakce (druhá) platí za rodičovskou transakci, která je uvíznutá (první). Proto se tomu říká "CPFP."

CPFP tedy umožňuje příjemci získat své prostředky rychleji navzdory nízkým počátečním poplatkům, které vynaložil odesílatel, na rozdíl od RBF (*Replace-By-Fee*), který umožňuje odesílateli převzít iniciativu k urychlení vlastní transakce zvýšením poplatků.