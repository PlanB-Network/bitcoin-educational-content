---
term: NONCE
---

V kontextu výpočetní techniky termín "nonce" odkazuje na číslo, které je použito pouze jednou a poté nahrazeno. Často je náhodné nebo pseudonáhodné. Nonce se používají v různých kryptografických protokolech, aby zajistily bezpečnost procesu. Například, podpisy ECDSA používané v rámci protokolu Bitcoin zahrnují použití nonce. To znamená, že toto číslo musí být pro každý podpis nové. Pokud tomu tak není, je možné vypočítat soukromý klíč použitý porovnáním dvou podpisů, které používají stejný nonce.

Nonce se také používají v procesu těžby Bitcoinu. Těžaři inkrementují tyto modifikovatelné hodnoty ve svých kandidátních blocích. Modifikují hodnotu nonce, aby našli kryptografický hash, který je nižší nebo roven cílové obtížnosti. Tento proces vyžaduje významný výpočetní výkon, protože zahrnuje vyčerpávající hledání mezi velkým počtem možných nonců. Když těžař najde nonce, které po začlenění do jejich bloku produkuje digest, který splňuje kritéria obtížnosti, blok je vysílán do sítě a těžař získá odměnu.

> ► *V roce 2010 objevili výzkumníci, že Sony PlayStation 3 používal stejný nonce při podepisování různých balíčků kódu. Toto opětovné použití nonce umožnilo útočníkům vypočítat soukromý klíč použitý k podepisování softwaru. S soukromým klíčem v ruce mohli útočníci vytvářet platné podpisy pro jakýkoliv kód, což jim umožnilo spouštět neautorizovaný software, včetně pirátských her nebo vlastních operačních systémů, přímo na PS3.*

> ► *Existuje běžný omyl ohledně původu termínu "nonce." Někteří tvrdí, že představuje zkratku "number only used once" (číslo použité pouze jednou). Ve skutečnosti původ slova sahá do 18. století a pochází z vývoje významu staroanglického výrazu "then anes," který znamenal "pro příležitost."*