---
term: OP_PUSHDATA4 (0X4E)

---
Umožňuje vložit na zásobník velmi velké množství dat. Následují čtyři bajty (little-endian), které udávají délku dat, která se mají odeslat (až do velikosti přibližně 4,3 GB). Tento opkód se používá k vkládání velmi velkých dat do skriptů, i když jeho použití je velmi vzácné kvůli praktickým omezením velikosti transakcí.