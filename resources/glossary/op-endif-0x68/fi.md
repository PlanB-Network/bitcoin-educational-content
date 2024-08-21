---
termi: OP_ENDIF (0X68)
---

Merkitsee ehdollisen ohjausrakenteen loppua, jonka on aloittanut `OP_IF` tai `OP_NOTIF`, ja jota yleensä seuraa yksi tai useampi `OP_ELSE`. Se osoittaa, että skriptin suoritus tulisi jatkua ehdollisen rakenteen ulkopuolelle riippumatta siitä, kumpi haara suoritettiin. Toisin sanoen, `OP_ENDIF` toimii merkkinä ehdollisten lohkojen lopusta skripteissä.