---
term: OP_NUMEQUALVERIFY (0X9D)
---

Kombinuje operacije `OP_NUMEQUAL` i `OP_VERIFY`. Numerički poredi dve najgornje Elements na steku. Ako su vrednosti jednake, `OP_NUMEQUALVERIFY` uklanja tačan rezultat sa steka i nastavlja izvršavanje skripta. Ako vrednosti nisu jednake, rezultat je netačan i skript odmah ne uspeva.