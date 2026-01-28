---
term: Gap limit
definition: Maximalt antal på varandra följande oanvända adresser innan sökningen efter transaktioner stoppas.
---

En parameter som används i Bitcoin Wallet-programvara för att bestämma det maximala antalet oanvända adresser i följd till generate innan sökningen efter ytterligare transaktioner stoppas. Det är ofta nödvändigt att justera denna parameter vid återställning av en Wallet för att säkerställa att alla transaktioner hittas. En otillräcklig Gap Limit kan leda till att vissa transaktioner missas om adresser hoppades över under derivationsfaserna. Om Gap Limit ökas kan Wallet söka längre fram i Address-sekvensen för att återskapa alla associerade transaktioner.


En enda "xpub" kan teoretiskt härleda mer än 4 miljarder mottagaradresser (både interna och externa adresser). Wallet-programvaran kan dock inte härleda och kontrollera alla dessa för användning utan att ådra sig en enorm driftskostnad. Därför fortsätter de i indexordning, eftersom detta normalt är den ordning i vilken all Wallet-programvara genererar adresser. Programvaran registrerar varje använd Address innan den går vidare till nästa, och den stoppar sin sökning när den stöter på ett antal tomma adresser i följd. Detta antal är vad som kallas Gap Limit.


Om till exempel Gap Limit är inställt på `20`, och Address `m/84'/0'/0'/0/15/` är tom, kommer Wallet att härleda adresser upp till `m/84'/0'/0'/0/34/`. Om detta adressintervall förblir oanvänt stannar sökningen där. Följaktligen skulle en transaktion som använder Address `m/84'/0'/0'/0/40/` inte upptäckas i detta exempel.