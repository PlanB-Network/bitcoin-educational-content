---
term: BATERIE
---

V kontextu skriptovacího jazyka, který se používá k přiřazování podmínek výdajů k UTXO Bitcoin, je zásobník datová struktura LIFO (*Last In, First Out*), která se používá k ukládání dočasných Elements během provádění skriptu. Každá operace ve skriptu manipuluje s těmito zásobníky, do nichž lze přidávat (*push*) nebo z nich odebírat (*pop*) Elements. Skripty používají zásobníky k vyhodnocování výrazů, ukládání dočasných proměnných a správě podmínek.


Při spouštění skriptu Bitcoin lze použít 2 zásobníky: hlavní zásobník a alternativní zásobník. Hlavní zásobník se používá pro většinu operací skriptu. Na tomto zásobníku se provádějí operace skriptu, při kterých se přidávají, odebírají nebo manipulují data. Alternativní zásobník naopak slouží k dočasnému uložení dat během provádění skriptu. Specifické operační kódy, jako například `OP_TOALTSTACK` a `OP_FROMALTSTACK`, umožňují přenášet Elements z hlavního zásobníku do alternativního a naopak.


Například při ověřování transakce se podpisy a veřejné klíče přesunou do hlavního zásobníku a zpracují se pomocí po sobě jdoucích operačních kódů, aby se ověřilo, zda podpisy odpovídají klíčům a datům transakce.