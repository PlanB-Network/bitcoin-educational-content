---
term: UTXO SET
---

Avser samlingen av alla befintliga UTXO:er vid en given tidpunkt. Med andra ord är det en stor lista över alla olika bitar av bitcoins som väntar på att spenderas. Om du lägger till beloppen för alla UTXO:er i UTXO-uppsättningen ger det oss den totala monetära massan av bitcoins i omlopp. Varje nod i Bitcoin-nätverket upprätthåller sin egen UTXO-uppsättning i realtid. Den uppdaterar den när nya giltiga block bekräftas, med de transaktioner de innehåller, som förbrukar vissa UTXO:er från UTXO-uppsättningen och skapar nya i gengäld.


Denna UTXO-uppsättning behålls av varje nod för att snabbt verifiera om de UTXO som använts i transaktioner verkligen är legitima. Detta gör att de kan upptäcka och avvisa Double-spending-försök. UTXO-uppsättningen är ofta kärnan i oro över Bitcoin:s decentralisering, eftersom dess storlek naturligt ökar mycket snabbt. Eftersom en del av den måste förvaras i RAM-minnet för att verifiera transaktioner inom rimlig tid, kan UTXO-uppsättningen gradvis göra det för kostsamt att driva en Full node. UTXO-uppsättningen har också en betydande inverkan på IBD (*Initial Block Download*). Ju mer av UTXO-uppsättningen som kan placeras i RAM, desto snabbare är IBD. På Bitcoin Core lagras UTXO-uppsättningen i mappen med namnet `/chainstate`.


> ► *På engelska kan "UTXO set" översättas med "UTXO set"*