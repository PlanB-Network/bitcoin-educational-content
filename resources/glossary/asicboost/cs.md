---
term: ASICBOOST

---
ASICBOOST je algoritmická optimalizační metoda vynalezená v roce 2016, která má zvýšit efektivitu těžby Bitcoinu přibližně o 20 % snížením množství výpočtů potřebných pro každý pokus o hash hlavičky. Tato technika využívá vlastnost hašovací funkce SHA256, používané pro těžbu, která data před zpracováním rozděluje do bloků. ASICBOOST zachovává jeden z těchto bloků beze změny napříč několika pokusy o hašování, což těžaři umožňuje provést pouze část práce pro tento blok během několika pokusů. Toto rozdělení dat umožňuje opakovaně použít výsledky předchozích výpočtů, čímž se snižuje celkový počet výpočtů potřebných k nalezení platného hashe.

ASICBOOST lze použít ve dvou formách: Overt ASICBOOST a Covert ASICBOOST. Forma Overt ASICBOOST je viditelná pro každého, protože zahrnuje použití pole `nVersion` bloku jako nonce a nemění skutečné `Nonce`. Skrytá forma se snaží tyto změny skrýt pomocí Merkleho stromů. Tato druhá metoda se však od zavedení SegWit stala méně účinnou kvůli druhému Merkleho stromu, který zvyšuje počet výpočtů potřebných k jejímu použití.

ASICBOOST umožňuje těžařům, aby nemuseli provádět skutečné kompletní SHA256 pro všechny pokusy o hašování, protože část výsledku zůstává nezměněna, což urychluje práci těžařů.