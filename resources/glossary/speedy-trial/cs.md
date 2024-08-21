---
term: SPEEDY TRIAL
---

Metoda aktivace soft forku, která byla původně koncipována pro Taproot na začátku roku 2021 Davidem A. Hardingem na základě nápadu Russella O'Connora. Jejím principem je použití metody BIP8 s parametrem `LOT` nastaveným na `false`, přičemž doba pro aktivaci je zkrácena na pouhé 3 měsíce. Toto zkrácené období hlasování umožňuje rychlou verifikaci schválení těžaři. Pokud je během jednoho z období dosaženo požadovaného prahu schválení, soft fork je poté uzamčen. Jeho aktivace proběhne několik měsíců později, čímž se těžařům poskytne potřebný čas na aktualizaci jejich softwaru.

Úspěch této metody pro Taproot, který se těšil širokému konsenzu v rámci komunity Bitcoinu, však nezaručuje její účinnost pro všechny aktualizace. Ačkoliv metoda Speedy Trial umožňuje rychlejší aktivaci, někteří vývojáři vyjadřují obavy ohledně jejího budoucího použití. Obávají se, že by to mohlo vést k příliš rychlému sledu soft forků, což by mohlo potenciálně ohrozit stabilitu a bezpečnost protokolu Bitcoinu. Ve srovnání s BIP8 s parametrem `LOT=true` je metoda Speedy Trial pro těžaře mnohem méně hrozivá. Automaticky není plánován žádný UASF. Tato metoda aktivace ještě nebyla formalizována v rámci BIP.

> ► *Termín "Speedy Trial" je převzat z právní terminologie, která označuje "urychlený soudní proces". To evokuje fakt, že návrh na vylepšení je rychle předložen "soudnímu dvoru" těžařů, aby bylo určeno jejich rozhodnutí. Je obecně přijato používat anglický termín přímo v češtině.*