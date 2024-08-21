---
term: OP_SUCCESS
---

`OP_SUCCESS` představuje sérii operačních kódů, které byly v minulosti zakázány a nyní jsou rezervovány pro budoucí použití v Tapscriptu. Jejich konečným cílem je usnadnit aktualizace a rozšíření jazyka skriptů tím, že umožní zavedení nových funkcionalit prostřednictvím měkkých forků. Když je v skriptu narazeno na jeden z těchto operačních kódů, znamená to automatický úspěch té části skriptu, bez ohledu na přítomná data nebo podmínky. To znamená, že skript pokračuje ve svém provádění bez selhání, nezávisle na předchozích operacích.

Takže, když je na `OP_SUCCESS` přidán nový operační kód, nutně to představuje přidání přísnějšího pravidla než to předchozí. Aktualizované uzly pak mohou ověřit dodržování tohoto pravidla, a uzly, které nebyly aktualizovány, neodmítnou přidružené transakce a bloky, které je zahrnují, protože `OP_SUCCESS` validuje tu část skriptu. Proto nedochází k tvrdému forku.

Ve srovnání, `OP_NOP` (*No Operation*, žádná operace) také slouží jako zástupné symboly ve skriptu, ale nemají žádný vliv na provádění skriptu. Když je narazeno na `OP_NOP`, skript jednoduše pokračuje bez změny stavu zásobníku nebo postupu skriptu. Klíčový rozdíl je tedy v jejich dopadu na provádění: `OP_SUCCESS` zaručuje úspěšný průchod tou částí skriptu, zatímco `OP_NOP` je neutrální a nemá vliv ani na zásobník, ani na tok skriptu. Tyto operační kódy jsou označeny jako `OP_SUCCESSN`, kde `N` je číslo použité k odlišení `OP_SUCCESS`.