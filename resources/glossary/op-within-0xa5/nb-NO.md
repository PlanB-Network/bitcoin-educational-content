---
term: OP_WITHIN (0XA5)

definition: Opcode som sjekker om en verdi ligger innenfor et intervall definert av to andre verdier.
---
Sjekker om det øverste elementet i stakken ligger innenfor det området som er definert av det andre og tredje øverste elementet. Med andre ord sjekker `OP_WITHIN` om det øverste elementet er større enn eller lik det andre og mindre enn det tredje. Hvis denne betingelsen er sann, skyver den `1` (true) på stakken, ellers skyver den `0` (false).