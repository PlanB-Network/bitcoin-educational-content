---
term: OP_ENDIF (0X68)

definition: Opcode, joka merkitsee ehdollisen rakenteen loppua scriptissä.
---
Merkitsee `OP_IF`- tai `OP_NOTIF`-komennolla aloitetun ehdollisen ohjausrakenteen lopun, jota seuraa yleensä yksi tai useampi `OP_ELSE`. Se ilmaisee, että komentosarjan suorituksen pitäisi jatkua ehdollisen rakenteen jälkeen riippumatta siitä, mikä haara on suoritettu. Toisin sanoen `OP_ENDIF` osoittaa skriptien ehdollisten lohkojen lopun.