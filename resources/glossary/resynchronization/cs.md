---
term: RESYNCHRONIZACE

---
Označuje jev, při kterém dochází ke změně struktury blockchainu v důsledku existence konkurenčních bloků ve stejné výšce. K tomu dochází, když je část blockchainu nahrazena jiným řetězcem s větším množstvím nahromaděné práce.

Tyto resynchronizace jsou součástí přirozeného fungování Bitcoinu, kdy různí těžaři mohou nalézt nové bloky téměř současně, čímž se síť Bitcoinu rozdělí na dvě části. V takových případech se síť může dočasně rozdělit na konkurenční řetězce. Nakonec, když jeden z těchto řetězců nahromadí více práce, uzly ostatní řetězce opustí a jejich bloky se stanou takzvanými "zastaralými bloky" nebo "osiřelými bloky" Tento proces nahrazování jednoho řetězce jiným je resynchronizace.

![](../../dictionnaire/assets/9.webp)

Resynchronizace může mít různé důsledky. Zaprvé, pokud si uživatel nechal potvrdit transakci v bloku, který se ukázal jako opuštěný, ale tato transakce se v konečném platném řetězci nenachází, pak se jeho transakce stane opět nepotvrzenou. Proto se doporučuje vždy počkat alespoň na 6 potvrzení, aby bylo možné transakci považovat za skutečně neměnnou. Po 6 blocích do hloubky je resynchronizace tak nepravděpodobná, že šanci na její výskyt lze považovat prakticky za nulovou.

Na úrovni globálního systému navíc resynchronizace znamená plýtvání výpočetním výkonem těžařů. Když totiž dojde k rozdělení, někteří těžaři budou na řetězci `A` a jiní na řetězci `B`. Pokud je řetězec `B` během resynchronizace nakonec opuštěn, pak je veškerý výpočetní výkon nasazený těžaři na tomto řetězci z definice promarněn. Pokud je v síti Bitcoin příliš mnoho resynchronizací, snižuje se tím celková bezpečnost sítě. To je částečně důvod, proč může být nebezpečné zvětšení velikosti bloku nebo zkrácení intervalu mezi jednotlivými bloky (10 minut).

> ►Někteří bitcoináři raději používají výraz "osiřelý blok" pro označení bloku, jehož platnost vypršela. Ačkoli jde o anglicismus, v běžném jazyce se také často dává přednost "reorganizaci" nebo "reorg" před "resynchronizací" *