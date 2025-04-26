---
term: OP_SUCCESS

---
`OP_SUCCESS` představují řadu opcodes, které byly v minulosti zakázány a nyní jsou vyhrazeny pro budoucí použití v Tapscriptu. Jejich konečným cílem je usnadnit aktualizace a rozšíření skriptovacího jazyka tím, že umožní zavedení nových funkcí prostřednictvím soft forků. Pokud se ve skriptu vyskytne některý z těchto opkódů, znamená to automatický úspěch dané části skriptu bez ohledu na přítomná data nebo podmínky. To znamená, že skript pokračuje ve svém provádění bez selhání, nezávisle na předchozích operacích.

Pokud je tedy na `OP_SUCCESS` přidán nový opkód, znamená to nutně přidání přísnějšího pravidla, než bylo pravidlo předchozí. Aktualizované uzly pak mohou ověřit soulad s tímto pravidlem a uzly, které nejsou aktualizovány, neodmítnou související transakce a bloky, které je obsahují, protože `OP_SUCCESS` ověřuje tuto část skriptu. Proto nedochází k hard forku.

Oproti tomu `OP_NOP` (*No Operation*) slouží ve skriptu také jako zástupné znaky, ale nemají žádný vliv na provádění skriptu. Když se vyskytne `OP_NOP`, skript jednoduše pokračuje, aniž by se změnil stav zásobníku nebo průběh skriptu. Klíčový rozdíl je tedy v jejich vlivu na provádění: `OP_SUCCESS` zaručuje úspěšný průchod danou částí skriptu, zatímco `OP_NOP` je neutrální a nemá vliv ani na zásobník, ani na průběh skriptu. Tyto opcodes se označují `OP_SUCCESSN`, kde `N` je číslo sloužící k odlišení `OP_SUCCESS`.