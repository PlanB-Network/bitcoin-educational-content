---
term: Primär sökväg
definition: Uppsättning nycklar som tillåter omedelbart spenderande utan timelock i Miniscript.
---

I en Wallet-programvara som använder Miniscript, som till exempel Liana, hänvisar den primära sökvägen till den uppsättning nycklar som tillåter omedelbar användning av medel, utan några tidsbaserade villkor. Denna väg är alltid tillgänglig och används för den dagliga hanteringen av bitcoins, utan att kräva en väntan (timelock) till skillnad från återhämtningsvägar. Ta exemplet med ett skript som innehåller två olika nycklar: nyckel A, som tillåter omedelbar användning av bitcoins, och nyckel B, som tillåter användning av dem efter en fördröjning som definieras av en tidslåsning på 52 560 block. I det här exemplet kommer nyckel A från den primära sökvägen, medan nyckel B kommer från återställningsvägen.