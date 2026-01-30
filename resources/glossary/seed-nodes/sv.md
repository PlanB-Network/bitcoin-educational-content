---
term: Seed-noder
definition: Statisk lista över offentliga Bitcoin-noder integrerad i källkoden för initiala anslutningar.
---

Statisk lista över offentliga Bitcoin-noder, integrerad direkt i källkoden för Bitcoin Core (`Bitcoin/src/chainparamsseeds.h`). Den här listan fungerar som anslutningspunkter för nya Bitcoin-noder som ansluter till nätverket, men den används endast om DNS-fröna inte ger ett svar inom 60 sekunder efter deras begäran. I så fall kommer den nya Bitcoin-noden att ansluta till dessa seed-noder för att upprätta en första anslutning till nätverket och begära IP-adresser till andra noder. Det slutliga målet är att få den information som krävs för att utföra IBD (Initial Block Download) och synkronisera med den kedja som har mest arbete ackumulerat. Listan över seed-noder omfattar nästan 1000 noder, identifierade i enlighet med den standard som fastställts av BIP155. seed-noder utgör således den tredje metoden för anslutning till nätverket för en Bitcoin-nod, efter den möjliga användningen av filen `peers.dat`, som skapas av noden själv, och begäran om DNS-frön.


> observera att seed-noder inte ska förväxlas med "DNS seeds", som är den andra metoden för att upprätta anslutningar