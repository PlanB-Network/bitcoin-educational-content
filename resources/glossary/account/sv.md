---
term: Konto
definition: I en HD-plånbok en härledningsnivå (djup 3) som tillåter hierarkisk organisering av nycklar och adresser.
---

I HD-plånböcker (Hierarchical Deterministic) representerar ett konto en avledning Layer på djup 3 enligt BIP32. Varje konto är sekventiellt numrerat med början från `/0'/` (härdad avledning, så i verkligheten `/2^31/` eller `/2 147 483 648/`). Det är på detta avledningsdjup som de välkända `xpubarna` finns. Numera används vanligtvis bara ett konto inom en HD Wallet. Ursprungligen var de dock tänkta att segregera olika kategorier av användning inom samma Wallet. Om vi till exempel tar en standard härledningsväg för en extern Taproot (P2TR) mottagning Address: `m/86'/0'/0'/0/0`, är kontoindexet den andra `/0'/`.


