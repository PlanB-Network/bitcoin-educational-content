---
term: STACK

---
V kontextu skriptovacího jazyka, který se používá k použití podmínek výdajů na bitcoinové UTXO, je zásobník datová struktura "LIFO" (*Last In, First Out*), která slouží k ukládání dočasných prvků během provádění skriptu. Každá operace ve skriptu manipuluje s těmito zásobníky, do kterých lze přidávat (*push*) nebo z nich odebírat (*pop*) prvky. Skripty používají zásobníky k vyhodnocování výrazů, ukládání dočasných proměnných a správě podmínek.

Během provádění skriptu Bitcoinu lze používat 2 zásobníky: hlavní zásobník a alternativní zásobník. Hlavní zásobník se používá pro většinu operací skriptu. Na tomto zásobníku se provádějí operace skriptu, při kterých se přidávají, odebírají nebo manipulují data. Alternativní zásobník naopak slouží k dočasnému ukládání dat během provádění skriptu. Specifické operační kódy, jako například `OP_TOALTSTACK` a `OP_FROMALTSTACK`, umožňují přenášet prvky z hlavního zásobníku do alternativního a naopak.

Například během ověřování transakce se podpisy a veřejné klíče přesunou na hlavní zásobník a zpracovávají se postupnými opcody, aby se ověřilo, zda podpisy odpovídají klíčům a datům transakce.

> ► *V angličtině se výraz " pile " překládá jako " stack ". Anglický termín se obecně používá i ve francouzštině při technických diskusích.*