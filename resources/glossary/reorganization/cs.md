---
term: REORGANIZACE

---
Označuje jev, při kterém dochází ke změně struktury blockchainu v důsledku existence konkurenčních bloků ve stejné výšce. K tomu dochází, když je část blockchainu nahrazena jiným řetězcem, který má větší množství nahromaděné práce.

Tyto reorganizace jsou součástí přirozeného fungování Bitcoinu, kdy různí těžaři mohou nacházet nové bloky téměř současně, čímž se síť Bitcoin rozdělí na dvě části. V takových případech se síť může dočasně rozdělit na konkurenční řetězce. Nakonec, když jeden z těchto řetězců nahromadí více práce, uzly ostatní řetězce opustí a jejich bloky se stanou takzvanými "zastaralými bloky" nebo "osiřelými bloky" Tento proces nahrazování jednoho řetězce jiným je reorganizace.

![](../../dictionnaire/assets/9.webp)

Reorganizace může mít různé důsledky. Zaprvé, pokud si uživatel nechal potvrdit transakci v bloku, který se ukáže jako opuštěný, ale tato transakce se neobjeví v nakonec platném řetězci, pak se jeho transakce stane opět nepotvrzenou. Proto se doporučuje vždy počkat alespoň na 6 potvrzení, aby bylo možné transakci považovat za skutečně neměnnou. Po 6 blocích do hloubky je reorganizace tak nepravděpodobná, že šanci na její výskyt lze považovat prakticky za nulovou.

Na úrovni globálního systému navíc reorganizace znamená plýtvání výpočetním výkonem těžařů. Když totiž dojde k rozdělení, někteří těžaři budou v řetězci `A` a jiní v řetězci `B`. Pokud je řetězec `B` během reorganizace nakonec opuštěn, pak je veškerý výpočetní výkon nasazený těžaři na tomto řetězci z definice promarněn. Pokud je v síti Bitcoin příliš mnoho reorganizací, snižuje se tím její celková bezpečnost. To je částečně důvod, proč může být nebezpečné zvětšení velikosti bloku nebo zkrácení intervalu mezi jednotlivými bloky (10 minut).

> ►Někteří bitcoináři raději používají výraz "osiřelý blok" pro označení bloku, jehož platnost vypršela. V běžné mluvě se také používá výraz "reorg" pro označení "reorganizace" Výraz "reorganizace" je anglicismus. Přesnější by bylo mluvit o "resynchronizaci "*