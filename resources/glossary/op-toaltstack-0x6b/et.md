---
term: OP_TOALTSTACK (0X6B)

---
Võtab peamise virna (*main stack*) ülemise osa ja teisaldab selle alternatiivsesse virna (*alt stack*). Seda opkoodi kasutatakse andmete ajutiseks kõrvalejätmiseks, et neid hiljem skriptis kasutada. Seega eemaldatakse teisaldatud element põhihunnikust. seejärel kasutatakse `OP_FROMALTSTACK`, et panna see tagasi peamise virna tippu.