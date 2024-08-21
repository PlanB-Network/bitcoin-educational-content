---
term: OP_PUSHDATA4 (0X4E)
---

Umožňuje vložit velmi velké množství dat na zásobník. Za tímto operačním kódem následují čtyři bajty (little-endian), které udávají délku vkládaných dat (až do přibližně 4,3 GB). Tento operační kód se používá k vložení velmi velkých dat do skriptů, ačkoli jeho použití je extrémně vzácné kvůli praktickým omezením velikosti transakce.