---
term: Initial blocknedladdning (IBD)
definition: Processen att ladda ner och verifiera blockkedjan när man startar en ny nod.
---

Avser den process genom vilken en nod laddar ner och verifierar Blockchain från Genesis-blocket och synkroniserar med andra noder i Bitcoin-nätverket. IBD måste utföras när en ny Full node startas. I början av denna initiala synkronisering har noden ingen information om tidigare transaktioner. Den hämtar därför varje block från andra noder i nätverket, verifierar dess giltighet och lägger sedan till det i sin lokala version av Blockchain. Det är värt att notera att IBD kan ta lång tid och vara resurskrävande på grund av den växande storleken på Blockchain- och UTXO-uppsättningen. Hur snabbt den körs beror på datorkapaciteten hos den dator som är värd för noden, dess RAM-kapacitet, lagringsenhetens hastighet och bandbredden. För att ge dig en uppfattning: om du har en kraftfull internetanslutning och noden finns på den senaste MacBook med gott om RAM-minne tar IBD bara några timmar. Om du däremot använder en mikrodator som en Raspberry Pi kan IBD ta en vecka eller mer.


