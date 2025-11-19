---
term: INDEX/TXINDEX/
---

Filer i Bitcoin Core som är avsedda för indexering av alla transaktioner som finns i Blockchain. Denna indexering möjliggör snabb sökning av detaljerad information om en transaktion med hjälp av dess identifierare (txid), utan att behöva gå igenom hela Blockchain. Skapandet av dessa indexeringsfiler är ett alternativ som inte är aktiverat som standard i Bitcoin Core. Om den här funktionen inte är aktiverad kommer din nod endast att indexera transaktioner som är associerade med plånböcker som är kopplade till din nod. För att aktivera indexering av alla transaktioner måste du ställa in parametern `-txindex=1` i filen `Bitcoin.conf`. Detta alternativ är särskilt användbart för applikationer och tjänster som ofta söker igenom transaktionshistoriken för Bitcoin.