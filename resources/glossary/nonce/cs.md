---
term: NONCE

---
V kontextu výpočetní techniky označuje pojem "nonce" číslo, které se použije pouze jednou a poté se nahradí. Často je náhodné nebo pseudonáhodné. Nonces se používají v různých kryptografických protokolech k zajištění bezpečnosti procesu. Například podpisy ECDSA používané v rámci protokolu Bitcoin zahrnují použití nonce. To znamená, že toto číslo musí být pro každý podpis nové. Pokud tomu tak není, je možné vypočítat použitý soukromý klíč porovnáním dvou podpisů, které používají stejnou nonce.

Nonces se používají také při těžbě bitcoinů. Těžaři tyto modifikovatelné hodnoty inkrementují v rámci svých kandidátských bloků. Hodnotu nonce upravují tak, aby našli kryptografický hash, který je nižší nebo roven cílové obtížnosti. Tento proces vyžaduje značný výpočetní výkon, protože zahrnuje vyčerpávající hledání mezi velkým počtem možných nonces. Když těžař najde nonce, která po zahrnutí do jeho bloku vytvoří digest, který splňuje kritéria obtížnosti, blok je vysílán do sítě a těžař získává odměnu.

> ► V roce 2010 výzkumníci zjistili, že systém PlayStation 3 od společnosti Sony používá při podepisování různých balíčků kódu stejnou nonce. Toto opakované použití nonce umožnilo útočníkům vypočítat soukromý klíč použitý k podpisu softwaru. S privátním klíčem v ruce mohli útočníci vytvořit platné podpisy pro jakýkoli kód, což jim umožnilo spustit neautorizovaný software, včetně pirátských her nebo vlastních operačních systémů, přímo na systému PS3.*
> ►Původ pojmu "nonce" je často mylný Někteří tvrdí, že představuje zkratku pro "číslo použité pouze jednou" Ve skutečnosti pochází původ slova z 18. století a vzniklo sémantickým vývojem staroanglického výrazu "then anes", který znamenal "pro příležitost" *