---
term: Beskuren nod
definition: Fullständig nod som raderar gamla verifierade block för att spara lagringsutrymme.
---

En beskuren nod, på engelska "Pruned Node", är en Full node som utför beskärning av Blockchain. Detta innebär att de äldsta blocken successivt tas bort, efter att de vederbörligen verifierats, så att endast de senaste blocken behålls. Lagringsgränsen anges i filen `Bitcoin.conf` via parametern `prune=n`, där `n` är den maximala storleken som blocken tar upp i megabyte (MB). Om `0` anges efter den här parametern inaktiveras beskärning och noden behåller Blockchain i sin helhet.


Beskurna noder betraktas ibland som olika typer av noder jämfört med fullständiga noder. Användningen av en beskuren nod kan vara särskilt intressant för användare som står inför begränsningar i lagringskapaciteten. För närvarande måste en Full node ha nästan 600 GB bara för att lagra Blockchain. En beskuren nod kan begränsa den nödvändiga lagringen till upp till 550 MB. Även om den använder mindre diskutrymme upprätthåller en beskuren nod en nivå av verifiering och validering som liknar den hos en Full node. Beskurna noder erbjuder därför mer förtroende för sina användare i jämförelse med lätta noder (SPV).