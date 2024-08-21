---
term: ASICBOOST
---

ASICBOOST je metoda algoritmické optimalizace vynalezená v roce 2016, která je navržena tak, aby zvýšila efektivitu těžby Bitcoinu o přibližně 20% snížením množství výpočtů potřebných pro každý pokus o hash hlavičky. Tato technika využívá funkci hashovací funkce SHA256, používané pro těžbu, která data rozděluje do bloků před jejich zpracováním. ASICBOOST si ponechává jeden z těchto bloků nezměněný napříč několika pokusy o hashování, což umožňuje těžaři provést pouze část práce pro tento blok při několika pokusech. Sdílení dat umožňuje opětovné využití výsledků z předchozích výpočtů, čímž se snižuje celkový počet výpočtů potřebných k nalezení platného hash.

ASICBOOST lze použít ve dvou formách: Overt ASICBOOST a Covert ASICBOOST. Forma Overt ASICBOOST je viditelná pro všechny, protože zahrnuje použití pole `nVersion` bloku jako nonce a nezměnu skutečného `Nonce`. Skrytá forma se snaží tyto úpravy skrýt použitím Merkleových stromů. Tato druhá metoda se však stala méně efektivní od zavedení SegWit kvůli druhému Merkleovu stromu, který zvyšuje počet výpočtů potřebných k jeho použití.

Shrnutí, ASICBOOST umožňuje těžařům, aby nemuseli provádět skutečný kompletní SHA256 pro všechny pokusy o hashování, protože část výsledku zůstává nezměněná, což urychluje práci těžařů.