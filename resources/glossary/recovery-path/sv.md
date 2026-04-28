---
term: Återställningssökväg
definition: Uppsättning nycklar som aktiveras efter ett timelock för att återställa medel i Miniscript.
---

I en Wallet-programvara som använder Miniscript, som till exempel Liana, hänvisar återställningsvägarna till uppsättningar nycklar som endast blir operativa efter en definierad period av inaktivitet i skriptet som låser bitcoins (timelock). Återställningsvägarna kan endast användas när tidslåset har löpt ut och erbjuder därmed en metod för att återvinna medel när den primära vägen inte är tillgänglig. Tänk på exemplet med ett skript som innehåller två olika nycklar: nyckel A, som tillåter omedelbar användning av bitcoins, och nyckel B, som tillåter användning av dem efter en fördröjning som definieras av en tidslåsning på 52 560 block. I det här exemplet kommer nyckel A från den primära sökvägen, medan nyckel B kommer från återställningsvägen.