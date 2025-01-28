---
term: OP_CHECKSIGADD (0XBA)

---
Extrahuje tři nejvyšší hodnoty ze zásobníku: `veřejný klíč`, `CScriptNum` `n` a `podpis`. Pokud podpis není prázdný vektor a není platný, skript se ukončí s chybou. Pokud je podpis platný nebo je prázdným vektorem (`OP_0`), zobrazí se dva scénáře:


- Pokud je signatura prázdný vektor: na zásobník se vloží `CScriptNum` s hodnotou `n` a pokračuje se ve vykonávání;
- Pokud signatura není prázdným vektorem a zůstává platná: na zásobník se vloží `CScriptNum` s hodnotou `n + 1` a pokračuje se v provádění.

Pro zjednodušení, `OP_CHECKSIGADD` provede operaci podobnou `OP_CHECKSIG`, ale místo toho, aby na zásobník vložil true nebo false, přidá `1` k druhé hodnotě na vrcholu zásobníku, pokud je signatura platná, nebo tuto hodnotu ponechá beze změny, pokud signatura představuje prázdný vektor. `OP_CHECKSIGADD` umožňuje vytvářet v Tapscriptu stejné politiky více podpisů jako pomocí `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY`, ale dávkově ověřitelným způsobem, což znamená, že odstraňuje proces vyhledávání při ověřování tradičního více podpisu, a tím urychluje ověřování a zároveň snižuje provozní zatížení procesorů uzlů. Tento opkód byl do Tapscriptu přidán výhradně pro potřeby Taprootu.