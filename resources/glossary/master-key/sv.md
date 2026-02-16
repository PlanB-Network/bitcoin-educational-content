---
term: Huvudnyckel
definition: Privat nyckel härledd från seeden, som fungerar som utgångspunkt för alla nycklar i en HD-plånbok.
---

I samband med HD-plånböcker (Hierarchical Deterministic) är den privata huvudnyckeln en unik privat nyckel som härrör från Wallet:s seed. För att erhålla huvudnyckeln används funktionen `HMAC-SHA512` på seed, med orden "*Bitcoin seed*" bokstavligen som nyckel. Resultatet av denna operation ger en 512-bitars utdata, där de första 256 bitarna utgör huvudnyckeln och de återstående 256 bitarna utgör huvud-chain code. Huvudnyckeln och huvud-chain code fungerar som utgångspunkt för att härleda alla underordnade privata och offentliga nycklar i HD Wallet:s trädstruktur. Därför befinner sig den privata huvudnyckeln på djup 0 i härledningen.


