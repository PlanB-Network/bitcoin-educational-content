---
term: NLOCKTIME

---
Vložené pole v transakcích, které nastavuje časovou podmínku, před jejímž splněním nelze transakci přidat do platného bloku. Tento parametr umožňuje zadat přesný čas (časové razítko Unixu) nebo určitý počet bloků jako podmínku pro to, aby transakce byla považována za platnou. Jedná se tedy o absolutní časový zámek (nikoli relativní). Parametr `nLockTime` ovlivňuje celou transakci a fakticky umožňuje ověření času, zatímco opkód `OP_CHECKLOCKTIMEVERIFY` umožňuje porovnat pouze horní hodnotu zásobníku s hodnotou `nLockTime`.