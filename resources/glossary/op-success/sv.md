---
term: OP_SUCCESS
definition: Opcodes reserverade i Tapscript som indikerar automatisk framgång, används för framtida soft forks.
---

`OP_SUCCESS` representerar en serie opkoder som tidigare har varit inaktiverade och som nu är reserverade för framtida användning i Tapscript. Deras yttersta syfte är att underlätta uppdateringar och utvidgningar av skriptspråket genom att tillåta införandet av nya funktioner via Soft-forks. När en av dessa opkoder påträffas i ett skript innebär det att den delen av skriptet automatiskt lyckas, oavsett vilka data eller villkor som finns. Detta innebär att skriptet fortsätter sin exekvering utan att misslyckas, oberoende av tidigare operationer.


När en ny opcode läggs till på en `OP_SUCCESS` innebär det alltså nödvändigtvis att en mer restriktiv regel läggs till än den tidigare. Uppdaterade noder kan sedan verifiera att denna regel följs och noder som inte är uppdaterade kommer inte att vägra de associerade transaktionerna och de block som innehåller dem, eftersom `OP_SUCCESS` validerar den delen av skriptet. Därför finns det ingen Hard Fork.


Som jämförelse kan nämnas att `OP_NOP` (*No Operation*) också fungerar som platshållare i skriptet, men de har ingen effekt på skriptets exekvering. När en `OP_NOP` påträffas fortsätter skriptet helt enkelt utan att ändra stackens tillstånd eller skriptets utveckling. Den viktigaste skillnaden ligger därför i deras inverkan på exekveringen: `OP_SUCCESS` garanterar en lyckad passage genom den delen av skriptet, medan `OP_NOP` är neutral och inte påverkar vare sig stacken eller skriptets flöde. Dessa opkoder betecknas med `OP_SUCCESSN` där `N` är ett nummer som används för att skilja `OP_SUCCESS` från `OP_SUCCESS`.