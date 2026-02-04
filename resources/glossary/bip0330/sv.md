---
term: BIP0330
definition: Erlay, optimering av transaktionsspridning som minskar bandbreddsanvändningen med cirka 40 %.
---

Ett förslag känt som "*Erlay*", som syftar till att optimera spridningen av obekräftade transaktioner i Bitcoin-nätverket. För närvarande sänds transaktioner till alla peers i en nod, vilket resulterar i redundans och överanvändning av bandbredd. BIP330 föreslår att denna sändning begränsas till 8 peers som standard och att man sedan använder en avstämningsmekanism för att effektivt dela saknade transaktioner. Erlay minskar bandbreddsförbrukningen med cirka 40%. Den undviker också en linjär ökning av bandbreddsförbrukningen med antalet peers som är anslutna till noden.