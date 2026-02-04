---
term: Blocks/rev*.dat
definition: Filer som lagrar ångringsdata (undo data) för att möjliggöra återgång till ett tidigare tillstånd av UTXO-mängden.
---

Namn på filerna i Bitcoin Core som lagrar den information som behövs för att potentiellt reversera de ändringar som gjorts i UTXO-uppsättningen av tidigare tillagda block. Varje fil identifieras med ett unikt nummer som är detsamma som blk*.dat-filen som den motsvarar. Rev*.dat-filerna innehåller de omvända data som motsvarar de block som lagras i blk*.dat-filerna. Dessa data är i huvudsak en lista över alla UTXO:er som används som ingångar i ett block. Dessa omvändningsfiler gör det möjligt för noden att återgå till ett tidigare tillstånd i händelse av en Blockchain-omorganisation som gör att tidigare validerade block kasseras.