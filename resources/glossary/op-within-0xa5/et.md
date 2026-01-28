---
term: OP_WITHIN (0XA5)

definition: Opcode, mis kontrollib, kas väärtus on kahe teise väärtusega määratud vahemikus.
---
Kontrollib, kas virna ülemine element on teise ja kolmanda ülemise elemendi poolt määratletud vahemikus. Teisisõnu, `OP_WITHIN` kontrollib, kas ülemine element on suurem või võrdne teise elemendiga ja väiksem kolmanda elemendiga. Kui see tingimus on tõene, lükkab ta virna `1` (true), vastasel juhul lükkab ta virna `0` (false).