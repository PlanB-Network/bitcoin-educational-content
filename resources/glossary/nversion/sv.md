---
term: nVersion
definition: Fält som indikerar transaktionsformatets version, nödvändigt för att aktivera nSequence.
---

Fältet "nVersion" i en Bitcoin-transaktion används för att ange vilken version av transaktionsformatet som används. Det gör det möjligt för nätverket att skilja mellan olika utvecklingar av transaktionsformatet över tiden och att tillämpa motsvarande regler. Detta fält har ingen inverkan på konsensusreglerna. Detta innebär att ett värde som tilldelas detta fält inte leder till att transaktionen ogiltigförklaras. Fältet `nVersion` har dock standardiseringsregler som för närvarande endast accepterar värdena `1` och `2`. För närvarande är detta fält endast användbart för aktivering av fältet `nSequence`.