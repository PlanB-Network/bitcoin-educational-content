---
term: OP_CHECKSIG (0XAC)
---

Ověřuje platnost podpisu vůči danému veřejnému klíči. Bere dva nejvyšší prvky ze zásobníku: podpis a veřejný klíč, a hodnotí, zda je podpis správný pro hash transakce a specifikovaný veřejný klíč. Pokud je ověření úspěšné, vloží na zásobník hodnotu `1` (pravda), v opačném případě `0` (nepravda). Tento operační kód byl v Tapscriptu modifikován pro ověřování Schnorrůvých podpisů.