---
term: OP_CHECKSIG (0XAC)

---
Ověřuje platnost podpisu proti danému veřejnému klíči. Vezme dva horní prvky ze zásobníku: podpis a veřejný klíč a vyhodnotí, zda je podpis správný pro hash transakce a zadaný veřejný klíč. Pokud je ověření úspěšné, vloží na zásobník hodnotu `1` (true), jinak `0` (false). Tento opkód byl v Tapscriptu upraven pro ověřování Schnorrových podpisů.