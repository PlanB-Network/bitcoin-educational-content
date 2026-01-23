---
term: BIP0066
definition: Standaardisatie van het handtekeningformaat met strikte DER-codering, om discrepanties tussen systemen te voorkomen.
---

Standaardiseerde het formaat van handtekeningen in transacties. Deze BIP werd voorgesteld als reactie op een verschil in de manier waarop OpenSSL handtekeningcodering afhandelde tussen verschillende systemen. Deze heterogeniteit bracht het risico met zich mee dat de Blockchain zou worden gesplitst. BIP66 standaardiseerde het handtekeningformaat voor alle transacties met strikte DER codering (*Distinguished Encoding Rules*). Deze verandering vereiste een Soft Fork. Voor de activering gebruikte BIP66 vervolgens hetzelfde mechanisme als BIP34, waarbij het `nVersion` veld moest worden verhoogd naar versie 3 en alle versie 2 of lagere blokken werden geweigerd zodra de Miner drempel van 95% was bereikt. Deze drempel werd overschreden bij blok nummer 363.725 op 4 juli 2015.