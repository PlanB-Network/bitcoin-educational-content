---
term: COMMITMENT TRANSACTION
---

V kontextu obousměrného kanálu v rámci Lightning je commitment transaction transakcí, kterou obě strany vytvoří a podepíší, aniž by ji publikovaly na hlavním řetězci. Reprezentuje aktuální stav rozdělení finančních prostředků mezi stranami kanálu, přičemž každá platba v Lightning vede k vytvoření nové commitment transaction. Tyto transakce jsou platné, ale jsou vysílány pouze tehdy, když je kanál uzavřen jednostranně. Obsahují výstupy pro každou stranu, odrážející rozdělení finančních prostředků podle platby Lightning provedených od otevření kanálu. K odrazení stran od vysílání zastaralých stavů kanálu, tj. starých commitment transactions, které odrážejí nesprávné rozdělení finančních prostředků, jsou přidruženy mechanismy sankcí.