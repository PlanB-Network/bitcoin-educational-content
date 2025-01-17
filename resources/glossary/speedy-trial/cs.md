---
term: SPEEDY TRIAL

---
Metoda aktivace měkké vidlice, kterou původně pro Taproot na začátku roku 2021 koncipoval David A. Harding na základě nápadu Russella O'Connora. Její princip spočívá v použití metody BIP8 s parametrem `LOT` nastaveným na `false`, přičemž doba aktivace se zkrátí na pouhé 3 měsíce. Toto zkrácené období hlasování umožňuje rychlé ověření schválení horníků. Pokud je během jednoho z období dosaženo požadovaného prahu schválení, soft fork je následně uzamčen. Aktivován bude o několik měsíců později, čímž těžaři získají potřebný čas na aktualizaci svého softwaru.

Úspěch této metody pro Taproot, která se těšila širokému konsenzu v komunitě bitcoinů, však nezaručuje její účinnost pro všechny aktualizace. Přestože metoda Speedy Trial umožňuje rychlejší aktivaci, někteří vývojáři vyjadřují obavy z jejího budoucího použití. Obávají se, že by mohla vést k příliš rychlému střídání soft forků, což by mohlo potenciálně ohrozit stabilitu a bezpečnost protokolu Bitcoin. Ve srovnání s BIP8 s parametrem `LOT=true` je metoda Speedy Trial pro těžaře mnohem méně ohrožující. Automaticky se neplánuje žádný UASF. Tato aktivační metoda zatím nebyla v rámci BIP formalizována.

> ► Termín "zrychlený proces" je převzat z právnické terminologie označující "zrychlený proces" Odvolává se na skutečnost, že zlepšovací návrh je rychle předložen hornickému soudu, aby se zjistily jeho záměry. Obecně je přijato používat anglický termín přímo ve francouzštině*