---
term: OP_ENDIF (0X68)
definition: Opcode die het einde van een voorwaardelijke structuur in een script markeert.
---

Markeert het einde van een voorwaardelijke controlestructuur die wordt gestart door een `OP_IF` of een `OP_NOTIF`, meestal gevolgd door een of meer `OP_ELSE`. Het geeft aan dat de uitvoering van het script verder moet gaan dan de voorwaardelijke structuur, ongeacht welke vertakking is uitgevoerd. Met andere woorden, `OP_ENDIF` dient om het einde van voorwaardelijke blokken in scripts af te bakenen.