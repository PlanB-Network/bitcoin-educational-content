---
term: OP_ENDIF (0X68)
---

Označava kraj strukture uslovne kontrole započete sa `OP_IF` ili `OP_NOTIF`, obično praćene sa jednim ili više `OP_ELSE`. Ukazuje da izvršavanje skripta treba da se nastavi izvan uslovne strukture, bez obzira koja grana je izvršena. Drugim rečima, `OP_ENDIF` služi za označavanje kraja uslovnih blokova u skriptama.