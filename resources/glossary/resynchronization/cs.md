---
term: RESYNCHRONIZATION
---

Odkazuje na jev, kdy blockchain podstoupí modifikaci své struktury kvůli existenci konkurenčních bloků ve stejné výšce. To se stává, když je část blockchainu nahrazena jiným řetězcem s větším množstvím nahromaděné práce.

Tyto resynchronizace jsou součástí přirozeného fungování Bitcoinu, kde různí těžaři mohou najít nové bloky téměř současně, čímž se Bitcoinová síť rozdělí na dvě. V takových případech se síť může dočasně rozdělit na konkurenční řetězce. Nakonec, když jeden z těchto řetězců nahromadí více práce, ostatní řetězce jsou uzly opuštěny a jejich bloky se stávají tzv. "zastaralými bloky" nebo "sirotčími bloky". Tento proces nahrazení jednoho řetězce jiným se nazývá resynchronizace.

![](../../dictionnaire/assets/9.png)

Resynchronizace mohou mít různé důsledky. Za prvé, pokud uživatel měl transakci potvrzenou v bloku, který se nakonec opustí, ale tato transakce není nalezena v nakonec platném řetězci, pak se jejich transakce stává znovu nepotvrzenou. Proto se doporučuje vždy počkat na alespoň 6 potvrzení, aby bylo možné transakci považovat za skutečně neměnnou. Po 6 bloků hluboko jsou resynchronizace tak nepravděpodobné, že šance na jejich výskyt lze považovat za prakticky nulovou.

Dále, na globální úrovni systému, resynchronizace znamenají plýtvání výpočetním výkonem těžařů. Skutečně, když dojde k rozdělení, někteří těžaři budou na řetězci `A` a jiní na řetězci `B`. Pokud je řetězec `B` nakonec opuštěn během resynchronizace, pak veškerý výpočetní výkon nasazený těžaři na tomto řetězci je, definicí, plýtván. Pokud je na Bitcoinové síti příliš mnoho resynchronizací, celková bezpečnost sítě je tím pádem snížena. To je částečně důvod, proč zvětšení velikosti bloku nebo snížení intervalu mezi jednotlivými bloky (10 minut) může být nebezpečné.

> ► *Někteří bitcoinisté dávají přednost použití termínu "sirotčí blok" pro označení zastaralého bloku. Navíc, i když jde o anglicismus, v běžném jazyce se často preferuje "reorganizace" nebo "reorg" před "resynchronizací".*