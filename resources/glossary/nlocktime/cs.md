---
term: NLOCKTIME
---

Vestavěné pole v transakcích, které nastavuje časovou podmínku, před kterou nemůže být transakce přidána do platného bloku. Tento parametr umožňuje specifikovat přesný čas (Unixový časový otisk) nebo specifický počet bloků jako podmínku pro to, aby byla transakce považována za platnou. Jedná se tedy o absolutní časový zámek (nikoli relativní). `nLockTime` ovlivňuje celou transakci a efektivně umožňuje ověření času, zatímco operační kód `OP_CHECKLOCKTIMEVERIFY` umožňuje pouze porovnání nejvyšší hodnoty v zásobníku s hodnotou `nLockTime`.