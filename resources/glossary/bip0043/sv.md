---
term: BIP0043
definition: Standard som introducerar fältet purpose i HD-härledningssökvägar för att identifiera vilken typ av plånbok som används (t.ex. m/84' för SegWit).
---

Förslag till förbättring som introducerar användningen av en härledningsnivå för att beskriva ändamålsfältet i strukturen för HD-plånböcker, tidigare introducerad i BIP32. Enligt BIP43 är den första härledningsnivån för en HD Wallet, strax efter huvudnyckeln som betecknas med `m/`, reserverad för ändamålsnumret som anger den härledningsstandard som används för resten av vägen. Detta nummer registreras som ett härdat index. Om t.ex. Wallet följer SegWit-standarden (BIP84), skulle början på dess härledningsväg vara: `m/84'/`. BIP43 gör det alltså möjligt att förtydliga de standarder som varje Wallet-program följer för att få bättre interoperabilitet mellan dem. Standardiseringen av resten av härledningsvägen beskrivs i BIP44.