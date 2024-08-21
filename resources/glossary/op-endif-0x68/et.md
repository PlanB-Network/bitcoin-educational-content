---
term: OP_ENDIF (0X68)
---

Märgib tingimusliku kontrollstruktuuri lõppu, mille algatas `OP_IF` või `OP_NOTIF`, millele tavaliselt järgneb üks või mitu `OP_ELSE`. See näitab, et skripti täitmine peaks jätkuma tingimusliku struktuuri tagant, olenemata sellest, millist haru täideti. Teisisõnu, `OP_ENDIF` toimib tingimuslike plokkide lõpu piiritlejana skriptides.