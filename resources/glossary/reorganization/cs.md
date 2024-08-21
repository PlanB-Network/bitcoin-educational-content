---
term: REORGANIZACE
---

Odkazuje na jev, kdy blockchain podstoupí modifikaci své struktury kvůli existenci konkurenčních bloků ve stejné výšce. To se stává, když je část blockchainu nahrazena jiným řetězcem, který má větší množství nahromaděné práce.

Tyto reorganizace jsou součástí přirozeného fungování Bitcoinu, kde různí těžaři mohou najít nové bloky téměř současně, čímž rozdělí Bitcoinovou síť na dvě. V takových případech se síť může dočasně rozdělit na konkurenční řetězce. Nakonec, když jeden z těchto řetězců nahromadí více práce, ostatní řetězce jsou uzly opuštěny a jejich bloky se stávají tzv. "zastaralými bloky" nebo "sirotčími bloky". Tento proces nahrazení jednoho řetězce jiným se nazývá reorganizace.

![](../../dictionnaire/assets/9.png)

Reorganizace mohou mít různé důsledky. Zaprvé, pokud uživatel měl transakci potvrzenou v bloku, který se nakonec ukáže jako opuštěný, ale tato transakce se neobjeví v nakonec platném řetězci, pak se jejich transakce stává znovu nepotvrzenou. Proto se doporučuje vždy počkat na alespoň 6 potvrzení, aby bylo možné transakci považovat za skutečně neměnnou. Po 6 bloků hluboko jsou reorganizace tak nepravděpodobné, že šance na jejich výskyt lze považovat za prakticky nulovou.

Dále, na globální úrovni systému, reorganizace znamenají plýtvání výpočetním výkonem těžařů. Skutečně, když dojde k rozdělení, někteří těžaři budou na řetězci `A` a jiní na řetězci `B`. Pokud je řetězec `B` nakonec opuštěn během reorganizace, pak veškerý výpočetní výkon nasazený těžaři na tomto řetězci je, definicí, plýtván. Pokud je na Bitcoinové síti příliš mnoho reorganizací, celková bezpečnost sítě je tím snížena. To je částečně důvod, proč zvětšení velikosti bloku nebo snížení intervalu mezi jednotlivými bloky (10 minut) může být nebezpečné.

> ► *Někteří bitcoinisté preferují používat termín "sirotčí blok" pro označení vypršeného bloku. Také, v běžné řeči se termín "reorg" používá pro odkaz na "reorganizaci". Termín "reorganizace" je anglicismus. Pro přesnější vyjádření by se dalo hovořit o "resynchronizaci".*