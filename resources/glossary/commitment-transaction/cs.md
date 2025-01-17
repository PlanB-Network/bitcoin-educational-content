---
term: ZÁVAZKOVÁ TRANSAKCE

---
V kontextu obousměrného kanálu v rámci Lightningu je závazková transakce transakcí, kterou obě strany vytvoří a podepíší, aniž by ji zveřejnily v hlavním řetězci. Představuje aktuální stav rozdělení finančních prostředků mezi stranami kanálu, přičemž každá platba v systému Lightning vede k nové transakci závazku. Tyto transakce jsou platné, ale vysílají se pouze při jednostranném uzavření kanálu. Obsahují výstupy pro každou stranu, které odrážejí rozdělení prostředků podle plateb Lightning provedených od otevření kanálu. Jsou přidruženy sankční mechanismy, které mají strany odradit od vysílání neaktuálních stavů kanálu, tj. starých závazkových transakcí, které odrážejí nesprávné rozdělení finančních prostředků.