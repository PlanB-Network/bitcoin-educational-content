---
term: Nod
definition: Dator som kör en Bitcoin-klient och deltar i nätverket genom att upprätthålla en kopia av blockkedjan.
---

I Bitcoin-nätverket är en nod (eller "nod" på engelska) en dator som kör en Bitcoin-protokollklient (som till exempel Bitcoin Core). Den deltar i nätverket genom att upprätthålla en kopia av Blockchain, vidarebefordra och verifiera transaktioner och nya block samt eventuellt delta i Mining-processen. Summan av alla Bitcoin-noder representerar själva Bitcoin-nätverket.


Det finns flera typer av noder i Bitcoin, inklusive fulla noder och lätta noder. Fullständiga noder behåller en fullständig kopia av Blockchain, verifierar alla transaktioner och block enligt konsensusregler och deltar aktivt i spridningen av transaktioner och block över nätverket. Light-noder, eller SPV-noder (*Simple Payment Verification*), behåller å andra sidan bara blockens rubriker och förlitar sig på fullnoder för att få transaktionsinformation.


> ► *Vissa skiljer också mellan s.k. "pruned nodes" ("beskuren nod" på engelska). Dessa är fullständiga noder som laddar ner och verifierar alla block från Genesis-blocket, men som bara håller de senaste blocken i minnet*